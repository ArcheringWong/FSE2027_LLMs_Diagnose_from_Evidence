# Citation and licensing

## RCA100

The model-visible evidence panels in this package are constructed derivatives
of RCA100 v1.1. They contain selected and transformed evidence cards rather
than the benchmark's full raw telemetry corpus.

RCA100 is distributed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International license. A copy is
included at `licenses/RCA100_CC_BY_NC_SA_4.0.txt`. The benchmark's requested
citation is:

```bibtex
@misc{rca100_2026,
  title  = {RCA-100: A Chain-Reasoning Benchmark for Root Cause Analysis on Cloud-Native Microservices},
  author = {Wen, Xidao and Liu, Haibin and Liu, Guiyang and Zhang, Cheng and Situ, Fang and Zhou, Qi},
  year   = {2026},
  note   = {103 chaos-drill incidents, OpenTelemetry demo store, CC BY-NC-SA 4.0}
}
```

Public benchmark location:
`https://aiops-benchmark.oss-cn-hongkong.aliyuncs.com/rca/rca100/v1.1/`

The RCA100 answer-key package is intentionally absent because its accompanying
instructions request controlled redistribution. This review artifact does not
contain the original per-case ground-truth JSON files.

## Artifact code

The two scripts under `analysis/` are licensed under the MIT License included
at `licenses/CODE_LICENSE_MIT.txt`.

The RCA100-derived panels remain governed by CC BY-NC-SA 4.0. The remaining
research result tables and annotations are provided for noncommercial peer
review; the archival release will state their final reuse license explicitly.

