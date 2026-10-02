#!/usr/bin/env python3
"""Recompute the paper's deterministic statistical results offline."""

from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results/deterministic"
LOCALIZATION = "LOCALIZATION_DEMANDING"
FAULT = "SAME_SERVICE_FAULT"
PERMUTATIONS = 100_000
PERMUTATION_SEED = 20_270_827
BOOTSTRAPS = 10_000
BOOTSTRAP_SEED = 20_270_828


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def truth(value: str) -> bool:
    return value.strip().lower() == "true"


def sign_permutation(values: list[float], sidedness: str) -> dict[str, Any]:
    array = np.asarray(values, dtype=float)
    observed = float(array.mean())
    rng = np.random.default_rng(PERMUTATION_SEED)
    extreme = 0
    remaining = PERMUTATIONS
    while remaining:
        size = min(10_000, remaining)
        signs = rng.integers(0, 2, size=(size, len(array)), dtype=np.int8) * 2 - 1
        simulated = (signs * array).mean(axis=1)
        if sidedness == "one-sided-greater":
            extreme += int(np.count_nonzero(simulated >= observed - 1e-15))
        elif sidedness == "two-sided":
            extreme += int(np.count_nonzero(np.abs(simulated) >= abs(observed) - 1e-15))
        else:
            raise ValueError(sidedness)
        remaining -= size
    return {
        "observed": observed,
        "extreme": extreme,
        "p_value": (extreme + 1) / (PERMUTATIONS + 1),
    }


def bootstrap_ci(values: list[float]) -> list[float]:
    array = np.asarray(values, dtype=float)
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    estimates: list[np.ndarray] = []
    remaining = BOOTSTRAPS
    while remaining:
        size = min(2_000, remaining)
        indices = rng.integers(0, len(array), size=(size, len(array)))
        estimates.append(array[indices].mean(axis=1))
        remaining -= size
    low, high = np.quantile(np.concatenate(estimates), [0.025, 0.975])
    return [float(low), float(high)]


def metric(rows: list[dict[str, str]], stratum: str, field: str, sidedness: str) -> dict[str, Any]:
    values = [float(row[field]) for row in rows if row["study_stratum"] == stratum]
    permutation = sign_permutation(values, sidedness)
    return {
        "n": len(values),
        "estimate": statistics.fmean(values),
        "ci95": bootstrap_ci(values),
        "raw_p": permutation["p_value"],
        "extreme_permutations": permutation["extreme"],
    }


def holm(results: dict[str, dict[str, Any]]) -> None:
    names = sorted(results, key=lambda name: (results[name]["raw_p"], name))
    running = 0.0
    for rank, name in enumerate(names):
        adjusted = min(1.0, (len(names) - rank) * results[name]["raw_p"])
        running = max(running, adjusted)
        results[name]["adjusted_p"] = running
        results[name]["holm_rank"] = rank + 1


def mean_field(rows: list[dict[str, str]], stratum: str, field: str) -> float:
    return statistics.fmean(float(row[field]) for row in rows if row["study_stratum"] == stratum)


def assert_close(actual: float, expected: float, label: str, tolerance: float = 1e-12) -> None:
    if abs(actual - expected) > tolerance:
        raise AssertionError(f"{label}: expected {expected}, observed {actual}")


def main() -> None:
    incidents = read_csv(RESULTS / "incident_level_scores.csv")
    triplets = read_csv(RESULTS / "model_incident_triplets.csv")
    expected_primary = load_json(RESULTS / "primary_results.json")
    expected_secondary = load_json(RESULTS / "secondary_results.json")

    primary = metric(incidents, LOCALIZATION, "SER_i", "one-sided-greater")
    primary.update(
        {
            "targeted_flip_rate": mean_field(incidents, LOCALIZATION, "K_i"),
            "placebo_flip_rate": mean_field(incidents, LOCALIZATION, "P_i"),
            "full_accuracy": mean_field(incidents, LOCALIZATION, "full_correct_i"),
            "ko_accuracy": mean_field(incidents, LOCALIZATION, "ko_correct_i"),
            "placebo_accuracy": mean_field(incidents, LOCALIZATION, "placebo_correct_i"),
        }
    )

    secondary = {
        "fault_SER": metric(incidents, FAULT, "SER_i", "two-sided"),
        "localization_AccuracyGap": metric(incidents, LOCALIZATION, "AccuracyGap_i", "two-sided"),
        "fault_AccuracyGap": metric(incidents, FAULT, "AccuracyGap_i", "two-sided"),
    }
    holm(secondary)

    localization_triplets = [row for row in triplets if row["study_stratum"] == LOCALIZATION]
    full_correct = sum(truth(row["full_correct"]) for row in localization_triplets)
    transitions = {
        "full_correct": full_correct,
        "full_to_ko_incorrect": sum(truth(row["full_to_ko_incorrect"]) for row in localization_triplets),
        "full_to_placebo_incorrect": sum(truth(row["full_to_placebo_incorrect"]) for row in localization_triplets),
    }

    assert_close(primary["estimate"], expected_primary["estimate"], "primary SER")
    assert_close(primary["ci95"][0], expected_primary["confidence_interval"]["lower"], "primary CI lower")
    assert_close(primary["ci95"][1], expected_primary["confidence_interval"]["upper"], "primary CI upper")
    assert_close(primary["raw_p"], expected_primary["permutation"]["p_value"], "primary p")
    assert_close(primary["targeted_flip_rate"], expected_primary["K_rate"], "targeted flip rate")
    assert_close(primary["placebo_flip_rate"], expected_primary["P_rate"], "placebo flip rate")
    assert_close(primary["full_accuracy"], expected_primary["full_accuracy"], "Full accuracy")
    assert_close(primary["ko_accuracy"], expected_primary["ko_accuracy"], "KO accuracy")
    assert_close(primary["placebo_accuracy"], expected_primary["placebo_accuracy"], "Placebo accuracy")

    expected_tests = {item["name"]: item for item in expected_secondary["tests"]}
    for name, result in secondary.items():
        expected = expected_tests[name]
        assert_close(result["estimate"], expected["estimate"], f"{name} estimate")
        assert_close(result["ci95"][0], expected["confidence_interval"]["lower"], f"{name} CI lower")
        assert_close(result["ci95"][1], expected["confidence_interval"]["upper"], f"{name} CI upper")
        assert_close(result["raw_p"], expected["raw_p"], f"{name} raw p")
        assert_close(result["adjusted_p"], expected["adjusted_p"], f"{name} adjusted p")

    if transitions != {"full_correct": 68, "full_to_ko_incorrect": 66, "full_to_placebo_incorrect": 1}:
        raise AssertionError(f"transition mismatch: {transitions}")

    report = {
        "cohort": {"incidents": len(incidents), "localization": 57, "fault_identification": 13},
        "primary_localization": primary,
        "secondary_family": secondary,
        "full_correct_transitions": transitions,
        "resampling": {
            "permutations": PERMUTATIONS,
            "permutation_seed": PERMUTATION_SEED,
            "bootstrap_resamples": BOOTSTRAPS,
            "bootstrap_seed": BOOTSTRAP_SEED,
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("REPRODUCTION_CHECKS_PASSED")


if __name__ == "__main__":
    main()
