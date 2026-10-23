# Zero geometry: model-reviewed exclusion of balanced residue type(rank4,weight128)

**Result (model-reviewed, conditional on the reviewed lemmas):** assuming the separately reviewed zero-set/magnitude and next-bit lemmas, no balanced nine-variable peak<=28 function has intrinsic quadratic residue type **(polar rank4,weight128)**. A fresh independent Codex `gpt-6.1-sol` (max effort, read-only) referee returned **ACCEPT with no required fixes** on the pinned `PROOF.md` (SHA-256 `96cdb42de949d9838fb67098ceb2db48078cb3483b7d32b5948bfce1206203c4`) and handoff manifest `226784b232a37b6371537bbe75d4b46a417572801504c60ab272d38ba4af7fe2`, including Appendix B (1–3 Walsh zeros ⇒ NL<=240). The parent's isolated replay of `code/audit.py` passed, and its kernel and projection corruptions exited 1. Records: `institute/review/continuation-20261015/info-zero-exclusion-{review.json,codex-review.md,parent-check.json}`. **This is a model review, not human peer review or formal verification.** It is also **not** global balanced nonexistence: seven residue types remain under the stated premises, and no NL242 witness is constructed. `PROOF.md` and all code/certificates are byte-identical to the reviewed snapshot; only this README, `result.json`, the seed bundle and the handoff status text changed. Pre-review copies are kept in `results/pre-review-status/`.

`PROOF.md` is self-contained about hypotheses, coordinate maps, stabilizer action, residue extension and the strict Fourier-energy contradiction. Known2-adic/canonical-sign methods are prior art; correctness, priority and significance remain separate. There is no Lean or human-peer-review claim.

## Dependency and review gate

The pinned Codex report is `inputs/odd-pair-codex-attempt.txt`, SHA256:

`cd7b02b3990b1d037cb4cba83812b89e08b92dd6662c7153abc9b6f53debad2d`.

Its parent-owned hostile Opus5.5 review returned **CORRECT-WITH-FIXES**, with no mathematical error. The review and the parent's archived601-control audit are copied under `inputs/parent-candidate-{review,audit}.json`. All requested errata are incorporated in `PROOF.md`: the exact `B^T a` split map and specific neighboring normal `v`; applying identities directly after linear normalization; the broad pruning-only scope of moment/next-bit identities; and replacement of the unarchived300-control claim by the archived parent audit. We did not rerun those accepted parent computations.

The new proof depends specifically on: the canonical transform alphabet0/±64; zero moments and the zero-flat conclusion; the reviewed slack accounting forcing exactly8 zeros and no |p|=1 values; linearity from balance; and the full Pfaffian quartic statement for E. It does not assume that three histogram profiles are three Boolean functions. `inputs/review-gate.json` records the current dependency status. The classification was computed before that review closed and retains its historical pending-status field; that field is not a new review verdict.

## Exact geometric classification

Use linear coordinates

`D=u0*u1+u2*u3+z`, with radical `span(z,k0,k1,k2)`.

Balance puts0 in the candidate zero-three-flat. The proof shows this normal form is reached by a **linear** change, preserving that linear-flat property. Projecting away `z=q(u)` identifies zero-flats with isotropic3-subspaces of `U4+K3`.

| Radical-intersection dimension tau | Zero-three-flats | Pass necessary E-extension |
|---|---:|---:|
| 1 | 1680 | 0 |
| 2 | 210 | 210 |
| 3 | 1 | 1 |
| **Total** | **1891** | **211** |

The producer enumerates all97155 linear3-subspaces of F2^8. The independent checker enumerates all11811 linear3-subspaces of F2^7 with a different least-vector algorithm, reconstructs the graph flats and tests the quartic criterion rather than the producer's128-point cubic restriction system. Explicit8x8 D-stabilizer matrices map every flat to one of the three representatives. Each rejected flat has a binary dual-refutation certificate; every compatible flat has an explicit cubic extension.

The stabilizer proof is complete: a subgroup with symplectic U-block, invertible K-block and arbitrary U-to-K shear is transitive at each tau; tau is invariant under the full D-stabilizer. This is not an orbit assertion inferred only from equal histograms.

## From8192 residue lifts to an impossibility

The restriction `RM(3,8)|D=0` has rank80, so its kernel has dimension13. For the two surviving representatives all E are one particular E plus `D*b`, with

`b in span{1,u0,u1,u2,u3,k0,k1,k2,u0u2,u0u3,u1u2,u1u3,q}`.

Thus each representative has8192 possible **residue lifts**, not8192 functions. An independent point-by-monomial nullspace calculation reconstructs the whole kernel; all8192 lifts at each representative are checked independently for the necessary constant-character property.

Let `K=Z intersect rad(B)`, with dimension2 or3. The particular E is K-invariant, and every kernel element is K-affine on D=1. Hence on all128 points where D=1 the integer function p has magnitude3 and one common translation character along K. Projecting p to that character leaves those values unchanged, so the projected squared norm is at least1152. Its Fourier support has at most64 points (tau2) or32 (tau3), with every coefficient at most64. Parseval gives the contradictory bounds:

| Geometry | Mandatory projected norm | Maximum projected norm |
|---|---:|---:|
| tau2 | >=1152 | <=1024 |
| tau3 | >=1152 | <=512 |

This closes the two remaining geometries after tau1's quartic obstruction. It does **not** transfer the three-variable parity argument incorrectly to two variables: the crucial tau2 input is the complete E-kernel and its fixed K-character.

An independent alternative tau3 proof through eight balanced6-variable fibers is included. Its finite gates cover all256 three-variable sign tables and all65536 quadratics on a five-space; the quadratic-vanishing kernel is exactly `{0,q}`. It ends with the separate contradiction `16*24^2=9216>4096`. All normalization, spanning and v=0 qualifications are explicit.

## Separate one-to-three-zero corollary

The reviewed **first** zero moments alone give another consequence, independent of the new rank4 exclusion: a nine-variable peak<=28 function with any Walsh zero has at least4 zeros. Shift one zero to the origin by linear output addition, apply the balanced nonzero-support lemma, and use that a nonempty even-cardinality XOR0 set cannot contain2 distinct points.

Therefore any nine-variable function with exactly1,2 or3 Walsh zeros has Walsh peak>=32 and **NL<=240**. A Walsh zero forces even weight, hence all coefficients are divisible by4; no unrestricted covering-radius theorem is needed. This is an upper bound, not an attainment claim.

Priority remains unresolved. The parent inspected only the abstract of Carlet–Méaux–Broll, [ePrint2026/037](https://eprint.iacr.org/2026/037), on one-zero functions. No nonlinearity claim was in that inspected abstract; full-PDF retrieval returned403 and was not repeated. We do not infer novelty, an answered open question, or a contradiction from that abstract.

## Attempted routes, controls and limits

- The direct E-extension test is complete for all1891 flats and provides the strict tau1 obstruction.
- A next-bit parity probe fixed F on D=1 and Z, leaving120 sign positions. Its moment matrix has rank79; all8192 E lifts at both surviving representatives pass, leaving41 free F parities. This probe gives **no extra E exclusion** and is independently replayed as a discarded route. It was not expanded into sign SAT or another old heuristic.
- The character-projection argument supplies the new contradiction without searching those signs.
- Sharp projection controls use the genuine integer function `p=64*delta0`, whose transform is bounded64 and whose projected energy attains1024/512. It is not claimed to satisfy the target magnitude profile.
- Partial integer profiles with the target magnitudes/E are explicitly rejected by their actual transform peak>64; profiles are not Boolean functions.
- Four genuine balanced6-variable Boolean controls exercise the residue/fiber identities. The one-zero corollary's output-shift controls are genuine relaxed peak32 tables, not one-zero target witnesses.

No exhausted252 corpus, symmetric SAT, balanced-swap heuristic or scalar-profile relaxation was rerun. No old snapshot, record, generated navigation or parent proof was edited. All new evidence is under this directory.

## Reproducible evidence

Python3.10+ standard library is sufficient. Independent replay:

```sh
python3 code/audit.py
```

Production commands already exercised:

```sh
python3 code/classify.py
python3 code/carry_probe.py
```

Those producers preserve existing completed outputs rather than overwrite them; run regeneration in a fresh copied directory without the generated output files. No deletion is needed for independent replay.

The single final audit driver is:

```sh
python3 code/final_verify.py
```

It also requires these meaningful corruptions to fail for their exact assertion:

```sh
python3 code/audit.py --corrupt-classification
python3 code/audit.py --corrupt-kernel
python3 code/audit.py --corrupt-projection
python3 -O code/audit.py --corrupt-kernel
```

The kernel corruption still vanishes on D=0 but inserts forbidden quartics/K-quadratic dependence; a restriction-only checker would miss it. All acceptance checks use explicit exceptions and remain active under `python -O`.

`result.json` records actual commands, elapsed times, input/source hashes, exact scope, review gates and all controls. `results/classification.json.gz` contains the1891 case certificates, coordinate maps and two complete affine residue families. `results/audit.json` is the independent arithmetic receipt; `results/carry-probe.json` preserves the failed-to-exclude route. `seed-bundle.json.gz` and `handoff/` provide compact replay material for parent review, not an automatic engine requeue.

## FRONTIER

**MODEL-REVIEW-ACCEPTED / SEVEN-TYPES-REMAIN.** The full(4,128) exclusion and Appendix B corollary received the fresh Codex ACCEPT verdict above (model review, not peer review or formal verification; novelty unestablished). Seven other residue types remain; no extension to them is claimed here. The generic projector requires a forced large-magnitude set and a large common-character translation group; no reviewed lemma in this directory supplies that whole combination for another type. Work on the remaining types is a separate lane in `../remaining-types/`; no sign search was launched here.
