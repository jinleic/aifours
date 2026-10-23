# RDSQS(52): self-contained construction note

## 0. Claim, evidence level, limits

**Claim.** There is a Steiner quadruple system SQS(52) whose derived STS(51) at every one of
its 52 points is resolvable (an RDSQS(52)). An explicit labelled certificate with all 5,525
blocks and all 52 resolutions is pinned below. **Evidence level:** finite-exact
(computer-found; checked by independent programs). **Validity rests only on the certificate
checks (§5)**; §§2–4, 6 explain the construction. Not peer reviewed. Priority: no earlier
RDSQS(52) located (`sources/prior-art-search-20261017.md`; parent priority audit pending).
Consequences stated in the literature (Tan–Zhou arXiv:2503.11934 Thm 1.1/Cor 1.4: RDSQS(v+1)
⇒ LKTS(3v); RDSQS(n) ⇒ q0′(3,4,n)=n/2) are **not** re-proved here.

## 1. Definitions

SQS(v): 4-subsets ("blocks") of a v-set with every 3-subset in exactly one block. The derived
design at x is {b∖{x} : x∈b}, an STS(v−1). RDSQS(v): an SQS(v) all of whose derived designs
are resolvable (partitionable into (v−2)/2 parallel classes of (v−1)/3 triples).

## 2. Points and group

X = Z52. G = {y ↦ m·y + b : b∈Z52, m∈⟨23⟩} with ⟨23⟩ = {1, 9, 23, 29, 43, 51} = ⟨9⟩×⟨−1⟩
(23 has order 6 mod 52). |G| = 312.

## 3. The SQS

The block set is the union of the G-orbits of the 24 representatives listed in
`evidence/rdsqs52-z52m23/orbit_description.md` (orbit lengths: one 13, two 104, eight 156,
thirteen 312). Under translations alone: 106 orbits of length 52 plus the orbit of
{0,13,26,39} (length 13): 106·52+13 = 5525.

## 4. The resolutions

The derived STS(51) at 0 (points Z52∖{0}) has a resolution invariant under ⟨23⟩ with one
fixed class and eight ⟨23⟩-orbits of three classes; every class is invariant under x↦−x
(class-orbit representatives in `orbit_description.md`). The resolution at x is the
translate by x of the resolution at 0 (an automorphism image, since translations preserve
the SQS). In the certificate, POINT x lists g(resolution at 0) in class order, where g is
the lexicographically least element of G with g(0)=x (`code/audit_rdsqs52_symmetry.py`
checks both statements).

## 5. Pinned files, reproduction, verification

| Object | Path | SHA256 |
|---|---|---|
| Certificate (5525 blocks; POINT 0..51 × 25 classes × 17 triples) | `evidence/rdsqs52-z52m23/rdsqs52_z52_m23.txt` | `7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6` |
| Seed (multiplier generator + the 25 classes at 0, file order) | `evidence/rdsqs52-z52m23/rdsqs52_z52_m23_seed.json` | `a0fe9247f93d1f16007eff24b65c3dddf0f409c33f847f8a7382399b09dcefce` |
| Stdlib expander (seed → exact bytes) | `code/expand_rdsqs_seed.py` | `c60236df72bb78372feefe0652ea89a89ed128cbe056512cc23b2b63020e3de0` |

```sh
cd mathematics/evidence/six-lane-20261016/rdsqs52
python3 code/expand_rdsqs_seed.py evidence/rdsqs52-z52m23/rdsqs52_z52_m23_seed.json /tmp/r52.txt evidence/rdsqs52-z52m23/rdsqs52_z52_m23.txt   # byte-identical: True
python3 code/check_rdsqs.py evidence/rdsqs52-z52m23/rdsqs52_z52_m23.txt                  # Python, stdlib: PASS
clang -O2 -o /tmp/chk code/check_rdsqs.c && /tmp/chk evidence/rdsqs52-z52m23/rdsqs52_z52_m23.txt   # C: PASS
python3 code/audit_rdsqs52_symmetry.py evidence/rdsqs52-z52m23/rdsqs52_z52_m23.txt 23 /tmp/audit.json  # PASS
python3 code/mutation_controls_rdsqs.py evidence/rdsqs52-z52m23/rdsqs52_z52_m23.txt /tmp/mut52       # 15/15 as intended
```

Checkers assume no symmetry and check: block count, distinct in-range points, every triple in
exactly one block (explicit equality with all C(52,3)=22100 triples), a POINT section for
every x, 25 classes × 17 triples avoiding x, every class a partition of X∖{x}, every listed
triple a derived triple, every derived triple listed once. Receipts in
`evidence/rdsqs52-z52m23/` (lane-checker-receipt.json, mutations/mutation-results.json —
both checkers per case, symmetry-audit.json). Parent: independent definition-first checker
VALID; controls; mutation suite (receipts under `institute/runs/six-lane-2026-10-16/review/`).

## 6. How it was found (search reproduction; not needed for validity)

`PYTHONHASHSEED=0 python code/mult_pipeline.py 52 OUT --mult 23 --res-mult 23 --anchor 26
--samples 12 --res-timeout 120 --workers 1` (Python 3.14.3, numpy 2.4.3, kissat 4.0.4;
sources `mult_pipeline.py` 09753950…2337, `rdsqs_lib.py` cbab319d…d6ce, `symres.py`
47ff365a…dc2). Kramer–Mesner exact cover over G-orbits of triples (SAT in 0.02 s), then the
⟨23⟩-invariant resolution of the derived design at 0 with class structure forced by the
⟨23⟩-orbits of triples through the anchor 26 (kissat 0.05–3.3 s). 12/12 sampled SQS gave
PASS certificates; sample 0 is pinned and was re-run byte-identically
(`code/runs/replay_m23_sample0/`). Earlier failures that shaped the choice (README §5):
groups containing the involution 25 gave UNSAT symmetric models; ⟨9⟩ alone (order 3) was
UNKNOWN. [Interpretation, not a theorem: adding −1 to ⟨9⟩ makes every class −1-invariant
(each class contains a triple {26,a,−a}) and halves the model, which kissat then solves.]
That every class is −1-invariant follows from the audit: ⟨23⟩ has the unique involution −1,
and the class orbits [1,3^8] under a group of order 6 force each class stabilizer ∋ −1.

## 7. Limits

One finite object; no family theorem. Group G acts on the SQS; resolutions are transported.
"New" means only that no earlier RDSQS(52) was located.
