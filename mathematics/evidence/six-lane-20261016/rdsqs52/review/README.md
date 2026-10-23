# Review packet index (lane `rdsqs52`)

| Item | Path | SHA256 |
|---|---|---|
| RDSQS(52) certificate (pinned; do not edit) | `../evidence/rdsqs52-z52m23/rdsqs52_z52_m23.txt` | `7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6` |
| Seed | `../evidence/rdsqs52-z52m23/rdsqs52_z52_m23_seed.json` | `a0fe9247f93d1f16007eff24b65c3dddf0f409c33f847f8a7382399b09dcefce` |
| Stdlib expander | `../code/expand_rdsqs_seed.py` | `c60236df72bb78372feefe0652ea89a89ed128cbe056512cc23b2b63020e3de0` |
| Lane checker (Python stdlib) | `../code/check_rdsqs.py` | `af70d0a2b7a6326ef781b1c4568fd89f34ba0cd9496c54a59d0ae27e2ba3cc2e` |
| Lane checker (C) | `../code/check_rdsqs.c` | `28f6a6b60c184bacb04720368d377e5a769c06d6c78f4a2234d71887b96c9469` |
| Symmetry audit | `../code/audit_rdsqs52_symmetry.py` → `../evidence/rdsqs52-z52m23/symmetry-audit.json` | re-hash |
| Orbit description | `../evidence/rdsqs52-z52m23/orbit_description.{json,md}` | re-hash |
| Construction note | `../sources/construction-z52m23.md` | re-hash |
| Model lemmas (unreviewed) | `../sources/model-lemmas.md` | re-hash |
| Prior-art record | `../sources/prior-art-search-20261017.md` | re-hash |

What a reviewer should try to break: (1) false-PASS paths in either checker (header,
duplicate POINT/CLASS ids, missing sections, non-derived triples); (2) the claim that the
listed resolutions are G-images of the resolution at 0 (the certificate is valid without it);
(3) the source/open-status claim (Tan–Zhou arXiv:2503.11934v1 §4(1)); (4) any statement in
`model-lemmas.md` (restricted-model lemmas only). Parent receipts: `institute/runs/six-lane-2026-10-16/review/rdsqs52-*`.
