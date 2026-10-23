# mcDSQS(38): self-contained construction note

## 0. Claim, evidence level, limits

**Claim.** There is a Steiner quadruple system SQS(38) whose derived STS(37) at every one of
its 38 points admits a 19-colouring (partition of its 222 triples into 19 partial parallel
classes), i.e. an mcDSQS(38) in the sense of Tan–Zhou arXiv:2503.11934v1 (lines 78–134). An
explicit labelled certificate with all 2109 blocks and all 38 colourings is pinned below.
**Evidence level:** finite-exact and computer-found. Two separately written lane checkers (Python,C),
the parent definition-first checker, a prompt-only third implementation executed by the parent and
a Codex own verifier accept the pinned certificate. The seed and full producer replay byte-exactly.
This parent revision applies the minor findings in `../pc100-mcdsqs38-mathematical-review.note.md`;
the original note remains in `../pc100-mcdsqs38-review-snapshot-v1/`. Priority is separately under audit.
Validity rests on the direct checks, not the group explanation. No human peer review has occurred.
Tan-Zhou Section4(1) names38 as the smallest unknown mcDSQS(6n+2). This is not proof of current novelty.
Quoted lane-relative paths and historical commands below refer to the original mcDSQS38 lane.

## 1. Definitions

SQS(v): 4-subsets ("blocks") of a v-set with every 3-subset in exactly one block. Derived
design at x: {b∖{x} : x ∈ b}, an STS(v−1). An r-colouring of an STS is a partition of its
triples into r partial parallel classes (pairwise disjoint triples; a class need not cover
the points). Every STS(37) S has222 triples and each PPC has at most floor(37/3)=12 triples.
Thus chi'(S)>=ceil(222/12)=19, and chi'(37):=min_S chi'(S)>=19. The explicit19-colourings give
chi'(D_x)<=19 at every point x. Consequently chi'(D_x)=19=chi'(37) for every x: this is an mcDSQS(38).
The bridge agrees with Tan-Zhou(1.1) but does not depend on that theorem's upper bound.

## 2. Points and group

X=Z38. The element3 generates U(38), with order18, so k modulo18 has well-defined parity.
Let G={y->m*y+b: m=3^k mod38, b=k mod2}. The maps y->y+2 and y->3y+1 generate G.
It has order18*19=342 and is transitive. The stabilizer of0 is
<9>={1,5,7,9,11,17,23,25,35}, of odd order9, so it contains no involution.
G contains the even translations, not y->y+1, and differs from Z38 semidirect <9> on this point set.
It contains y->-y+19, which swaps0 and19.
Remark (algebra, not needed for validity): writing y ↔ (y mod 19, y mod 2), G acts on
Z19×Z2 by (x,i) ↦ (μx+β, i+χ(μ)) with μ = m mod 19 and χ(μ) = 0/1 for μ a square/non-square
mod 19, so G ≅ AGL(1,19) acting on two copies of AG(1,19), non-squares swapping the copies.

## 3. The SQS

The block set is the union of 9 G-orbits (least representatives and lengths in
`evidence/mcdsqs38-g342/orbit_description.md`; lengths 114, 114, 171, 171, 171, 342 ×4;
sum2109). The block set is not invariant under y->y+1 (parent symmetry audit). Whether its full
automorphism group contains a38-cycle was not tested. No noncyclicity claim is made.

## 4. The colourings

At 0: 18 classes of 12 triples forming two ⟨9⟩-orbits of 9 classes (each class contains one
triple through 19), plus one ⟨9⟩-invariant class of 6 triples
{2,14,22} {3,21,33} {8,12,18} {10,32,34} {13,15,29} {27,31,37}, the six triples x·{1,7,11}
of D0 (README Lemma D). Each point y ≠ 0 is missed by exactly one class. The colouring at x
is g_x(colouring at 0), g_x the least element of G (sorted image tuples) with g_x(0) = x;
valid because G preserves the block set and maps derived designs to derived designs. Every
derived STS(37) therefore carries 18 classes of 12 (each missing one point) and one class of
6 (class-size profile 12¹⁸6 at every point, recorded by the Python checker).

The colouring at0 is invariant under its stabilizer as an **unordered set of classes**; the group
permutes18 class labels. All transported colourings are G-equivariant only as unordered partitions,
not as ordered certificate sections. Validity and the explicit transport require neither stronger claim.


## 5. Pinned files, reproduction, verification

| Object | Path | SHA256 |
|---|---|---|
| Certificate (2109 blocks; POINT 0..37 × 19 classes) | `evidence/mcdsqs38-g342/mcdsqs38_g342_s0.txt` | `973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c` |
| Seed (group generators + the 19 classes at 0) | `evidence/mcdsqs38-g342/mcdsqs38_g342_s0_seed.json` | `b945898255dec37f7a6ef98a099a7ed89e60b3aa07a8fd4af0bf50567f6b187e` |
| Stdlib expander (seed → exact bytes) | `code/expand_seed.py` | `31bcd91c7039fcc32ddca4265ea96de660b2fb2e1002b4300b75f61c09ccb424` |
| Python checker (stdlib) | `code/check_mcdsqs.py` | `e2dc212d90119494f46e72807fcf64e82b0b9f842c23ffc27335f47a6a7f63a3` |
| C checker (independent source) | `code/check_mcdsqs.c` | `7d04c404ad37485aa96f7384f8d502a9c364f97f140704e240d855ec79bc72bd` |

```sh
cd mathematics/evidence/six-lane-20261016/mcdsqs38
/usr/bin/python3 code/expand_seed.py evidence/mcdsqs38-g342/mcdsqs38_g342_s0_seed.json OUT.txt evidence/mcdsqs38-g342/mcdsqs38_g342_s0.txt  # byte-identical: True
/usr/bin/python3 code/check_mcdsqs.py evidence/mcdsqs38-g342/mcdsqs38_g342_s0.txt          # PASS
clang -O2 -o CHK code/check_mcdsqs.c && ./CHK evidence/mcdsqs38-g342/mcdsqs38_g342_s0.txt   # PASS
python3 code/audit_symmetry.py evidence/mcdsqs38-g342/mcdsqs38_g342_s0.txt 1:2,3:1 9 AUDIT.json  # PASS
python3 code/mutation_controls.py evidence/mcdsqs38-g342/mcdsqs38_g342_s0.txt MUTDIR           # 15/15 as intended
```

Both checkers assume no symmetry and check: v ≡ 2 (mod 6) and 2109 blocks of 4 distinct
in-range points, no repeated block, every 3-subset in exactly one block (explicit), COLOURS =
χ′(37) = 19, a POINT section for every x, exactly 19 nonempty classes per point, triples of 3
distinct points avoiding x, pairwise disjoint inside a class, every listed triple t with
t∪{x} a block, no triple listed twice, and all 222 derived triples listed. Receipts:
`evidence/mcdsqs38-g342/lane-python-check.json` (Python 3.14.3), `lane-python39-check.json`
(Python 3.9.6; byte-identical receipt), `lane-c-check.txt`, `symmetry-audit.json`,
`mutations/mutation-results.json` (per mutation: both checkers' messages), `sha256-manifest.txt`.

## 6. How it was found (search reproduction; not needed for validity)

The following command is a historical search record, not a safe rerun recommendation: its original
multi-sample producer automatically removed some intermediate CNFs, contrary to the no-deletion rule.
Use the parent's pinned single-sample guarded replay in `../candidate_producer_parent_replay.py`.
Missing originals must not be relabelled as preserved evidence if later regenerated.

`PYTHONHASHSEED=0 python code/pipeline.py 38 OUT --affine 1:2,3:1 --res-mult 9 --samples 24
--col-timeout 60 --workers 1` (Python 3.14.3, numpy 2.4.3, kissat 4.0.4; `code/pipeline.py`
4dc82fb6…eabf, `code/mcdsqs_lib.py` 6f4c6802…391, `code/ppcsym.py` ea43b344…085276):
Kramer–Mesner exact cover over the 26 G-orbits of triples (167 valid block-orbit rows; SAT in
0.005 s), then the ⟨9⟩-invariant partial-class colouring of D0 with class structure forced
by the ⟨9⟩-orbits of triples through the anchor 19 (README Lemma B; kissat 0.41 s). 24/24
sampled SQS gave colourings (0.25–1.94 s) and 24/24 certificates pass both checkers; sample 0
is pinned and its search was re-run byte-identically (`runs/replay_e6_s0/`).
What shaped the choice (lane computations, not independently parent-replayed): the worker reports no
SQS(38) invariant under Z38 semidirect <9> or <31>; the <3> case follows since <9> is a subgroup.
These are restricted-model statements, not nonexistence of an mcDSQS(38). The <7> model gave three
UNKNOWN results at300s and was stopped. None is needed to validate the pinned witness.

The involution obstruction used to choose the odd stabilizer has a short independent proof.
Let tau be an involutory automorphism of an STS(37) fixing just p, and suppose it preserves an
unordered19-colouring. For each a!=p, the triple through{a,tau(a)} has a fixed third point, hence p.
Therefore all18 triples through p are fixed, and their18 distinct colour classes are fixed.
None can have12 triples: its unique omitted point would be fixed by tau and different from p.
Those18 classes have at most11 triples each, while the remaining class has at most12, giving
at most18*11+12=210<222 triples, a contradiction. Thus such an invariant19-colouring is impossible.

## 7. Limits

One finite object; no family theorem. G acts on the SQS, and the colourings are transported and
listed explicitly; invariance is of unordered classes, not their labels. Restricted UNSAT/UNKNOWN
reports remain lane-level statements. The historical intermediate-CNF retention deviation does not
alter the pinned certificate or the independently guarded parent replay.
