# Olson terminal k=p+1 frontier — v2

Recorded 2026-10-21T03:09:54-0700 (`/bin/date`). Union of separately accepted scopes; no new mathematics. Each row carries its own literal imports/errata. Terminal-kappa_hat range0..p−1 by NF/GRX (clarification c7789ee917f80e558c114a635a4c7b4efda55d3386bd968891a900ddc2bac39a).

## Closed primes (every terminal k=p+1 cell excluded, full existential NF antecedent)

p=7 (k8), p=11 (k12), p=13 (k14), p=17 (k18: FC717), p=19 (k20: FC19).

## p=23, terminal k=24

| kappa_hat | accepted scope | verdict |
|---|---|---|
| 0–3 | K0T; LOWER-K1; K2; K3 | [olson-K0T-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-parent-verdict-v1.md) |
| 4 | USK (3≤kappa_hat≤floor((p−1)/4)) | [olson-USK-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-USK-parent-verdict-v1.md) |
| 5 | FCW (p=4·5−1) | [olson-FCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-verdict-v1.md) |
| 6 | TCW (p=4·6−5) | [olson-TCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-verdict-v1.md) |
| 7 | SCW (p=4·7−3) | [olson-SCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-parent-verdict-v1.md) |
| 8–9 | UFC U0 (p=4j−1, j=6, v∈{2,3}) | [olson-UFC-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-verdict-v1.md) |
| 10 | FC1023 (pending second family) | [olson-FC1023-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC1023-parent-verdict-v1.md) |
| 11–21 | upper-half composite [(p−1)/2,p−2] | [olson-BOTTOM-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-parent-verdict-v1.md) |
| 22 | PP1-EXCL (kappa_hat=p−1) | [olson-PP1-EXCL-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-PP1-EXCL-parent-verdict-v1.md) |

**p=23 closes iff FC1023 passes its Claude review** (the only non-accepted cell). FC1023 currently has Codex 0F/0M/0m, a parent written check and a provisional parent verdict; Claude running (bg_3105).

## p=29, terminal k=30

| kappa_hat | accepted scope | verdict |
|---|---|---|
| 0–3 | K0T; LOWER-K1; K2; K3 | [olson-K0T-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-parent-verdict-v1.md) |
| 4–7 | USK (floor((29−1)/4)=7) | [olson-USK-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-USK-parent-verdict-v1.md) |
| 8 | FCW (p=4·8−1) | [olson-FCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-verdict-v1.md) |
| 9 | TCW (p=4·9−5) | [olson-TCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-verdict-v1.md) |
| 10–12 | UFC U0 (p=4·8−3, j=8, v∈{2,3,4}) | [olson-UFC-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-verdict-v1.md) |
| 13–14 | UFC high strip / R_U — OPEN | [olson-UFC-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-verdict-v1.md) |
| 15–27 | upper-half composite [(p−1)/2,p−2]=[14,27] minus14 | [olson-BOTTOM-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-parent-verdict-v1.md) |
| 28 | PP1-EXCL | [olson-PP1-EXCL-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-PP1-EXCL-parent-verdict-v1.md) |

At p=29 the cells **kappa_hat=13,14 remain OPEN** (UFC complementary strip j≤2v−2, residual R_U; HIGH-COVER unproved). Correction: kappa_hat=15..27 lie in the upper half [(p−1)/2,p−2]=[14,27]; the lower endpoint kappa_hat=14 belongs to the OPEN strip (14>(3p+7)/8=11.75 and14>12=UFC p1mod4 bound), and15..27 are upper-half. So OPEN at p29: kappa_hat=13,14 only.

## Remaining open terminal cells for p≥23

Exactly the complementary strip floor((p+7)/4)<kappa_hat≤(p−3)/2 outside T0, i.e. j≤2v−2 (both residue classes), minus any separately proved cell. Currently no cell with j≤2v−2 is accepted except FC717/FC19/FC1023 (which cover p17 lower single, p19 both, p23 kappa10). For p≥31 no cells are proved in the strip beyond T0's coverage kappa≤(3p+5)/8 resp (3p+7)/8.

Other terminal k, inverse-normalisation/assembly obligations and full ordered Olson remain OPEN. No novelty/first claim; primary-source status per the priority records.
