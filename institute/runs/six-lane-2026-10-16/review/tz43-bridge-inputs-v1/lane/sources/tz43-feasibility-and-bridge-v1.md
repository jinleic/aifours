# Tan–Zhou §4(3): feasibility, exact parameters and the fan/RDS input

Written after host-clock reading 2026-10-17 19:16:07 PDT. This is a planning/consequence note within the frozen
math-1 slot, not a new target or a formal proof. Primary authority: Tan–Zhou arXiv:2503.11934v1, pinned text
`sources/tz/tan-zhou-2503.11934.txt`, SHA `df52a8f1…4c3c8164`; citations below are LF line numbers.
No priority/novelty claim. The frozen contract requires BOTH ingredients, and a restricted-model UNSAT is not
an unrestricted obstruction.

## Exact obligations

* gcDCQS(18⁴:2): 74 points, four groups of 18, two stem points. Every triple not inside S∪G for a group G is
  covered once; no forbidden triple is covered: 60,264 triples, 15,066 quadruples. At every group point x,
  H=(G_x∪S)∖{x} has size 19, and the derived system is gcSTS(73,19): r=χ′(73)=37 classes, exactly
  37−(73−19)/2=10 avoiding H, 819 triples in total (LF 211–220, 256–288). At each stem point the derived
  design is KF(18⁴): 648 triples, 36 frame classes of size 18, nine missing each group (LF 237–240, 288).
* FDGDD(3,4,5{18}): 90 points, five groups of 18, 14,580 transverse quadruples; at each point a derived
  KF(18⁴) on the other 72 points. Or RDGDD(3,4,5{18}): the same transverse design with 27 full parallel
  classes of 24 triples at every point (LF 241–247).

The gcDCQS partial `1382d572…282e` and its directly verified mcDSQS(74) consequence `eaff77fc…16c3` have now been
pinned. Therefore the remaining bottleneck for the frozen gate is the FDGDD/RDGDD ingredient, not the fan/RDS
import. Earlier estimates that the gcDCQS search would necessarily dominate did not predict the actual run:
the new Z8×Z3²/C4 representation found it, while all small-seed symmetry models tried for B have failed or
remain UNKNOWN.

## Symmetry models and actual dimensions

The naive A4 action with a pointwise-fixed stem is impossible: a stem-fixing involution swapping y,z in
*different* groups forces the unique fourth point of {α,y,z} to be a fixed group point outside their groups;
a double transposition has no such point (README Lemma I). Allowing the C18 factor to swap the stems does
not rescue a direct-product A4 action: every homomorphism A4→S2 is trivial.

Z72 with a stem-swapping generator is viable for the underlying CQS but hard for KM at weak stabilizers.
Z8×Z3², groups indexed by the Z8 coordinate modulo 4, supplies a different regular action of degree 72.
The Singer cycle S on Z3² gives an order-four stabilizer when S² is used; with explicit forbidden-row
restriction `--excl36`, avoid-class stabilizers 4;4;2;2;1, a colouring at 0 transports to all group points;
the regular subgroup {0,4}×Z3² supplies explicit stem frames. These are search choices only: both raw
checkers assume none of them.

| Model | Measured dimensions/status |
|---|---|
| gcDCQS cyclic + multiplier17 | 437 columns, 5376 rows; KM UNKNOWN at 1200 s |
| gcDCQS cyclic + multiplier25 | 345 columns, 3024 rows; KM SAT in 22 s; an order-three fixed-subdesign constraint complicates the colouring |
| gcDCQS Z8×Z3² with S², accepted sample1 | KM 12,790 vars / 30,666 clauses, 65 selected block orbits; colouring 33,281 vars / 95,098 clauses, 219 triple orbits; SAT in 727.985 s |
| FD m=6, regular Z5×Z6 | 72 columns, 205 rows, 10,577 vars / 42,544 clauses; UNSAT (even the bare KM design is UNSAT under this symmetry) |
| RD m=6, regular Z5×Z6 | 36,817 vars / 322,326 clauses; UNSAT |
| FD m=6, no global symmetry, prescribed frame at0 | 334,800 vars / 1,390,176 clauses, 24.1 MB CNF; running (restricted at one point's frame) |

The two abelian group descriptions Z18 and Z9×Z2 are isomorphic, so merely renaming between them does not
provide an independent group portfolio. The other abelian order-18 group is Z3×Z3×Z2; nonabelian options
include D9, S3×Z3 and the generalized dihedral group of Z3². Different group actions, not alternative names
for the same regular action, are the meaningful variations.

## Does the 1-FG/RDS input already exist? Yes — parameter distinction matters

Lemma 3.8 (LF 1070–1071), citing Witt1938 [20] and Zhou–Chang2014 [25], states existence of
RDS(3,q+1,qᵗ+1) for every prime power q and positive t. In particular RDS(3,5,4ᵗ+1) is an imported known
object. The proof of Construction2.2 explicitly deletes ∞ and forms B∞={B∖{∞}:∞∈B} and T={B:∞∉B};
this is a 1-fan S(3,({4},{5}),4ᵗ), type 1^(4ᵗ) (LF 343–345). Every pair is in one 4-block B∞ and every triple
in one member of B∞∪T because its unique original 5-block either contains ∞ or does not.

For the **family** in §4(3), the appropriate Construction2.3 parameters are
(m,g,n,s)=(18,1,4ᵗ,2), K1={4}, K={5}. Its required gcDCQS is precisely 18⁴:2, and its required FDGDD is
5{18}; output is gcDCQS(18^(4ᵗ):2). Both congruences equal 2 mod6. With RDGDD instead, Construction2.2
uses m=18, k=4, n=4ᵗ and the same RDS(3,5,4ᵗ+1). Filling by mcDSQS(20) then gives the claimed family,
subject to separate bridge review and both finite ingredients.

The tuple **(m,g,n,s)=(18,4,4,2)** is different: Construction2.3 outputs gcDCQS(72⁴:2), NOT gcDCQS(18⁴:2).
Its 1-FG(3,({4},{5}),16) of type4⁴ is the classical fan underlying the earlier gcDCQS32 construction:
start from RDS(3,5,17), take a parallel class of the derived resolvable S(2,4,16) as the four groups, use
its other 4-blocks as B and the non-∞ 5-blocks as T. Removing those four B-blocks and declaring them to be
groups does not change either Steiner coverage identity. This known fan is not the missing ingredient.
Using it with m=18 still presupposes the gcDCQS(18⁴:2) and the FDGDD(5{18}) ingredients.

## Weighting route and stop rules

A seed FDGDD or RDGDD(3,4,5{6}) may be weighted by3 using the explicit RDTD(3,4,3): blocks on four copies
of Z3 with x0+x1+x2+x3=0. At fixed x0=a, for each t∈Z3 the triples (u,u+t,u−a−t), u∈Z3, are a full
parallel class. Every derived triple has a unique t; permutation symmetry of the four coordinates handles
all fixed positions. Theorem2.5's sufficient gcd criterion does not cover3, so this explicit check is
necessary. `weight_gdd.py` implements the exact inflation and both definition-first routes have checked its
FDGDD(5{8})→FDGDD(5{24}) calibration. A seed6 is still missing.

Stop on the first certificate for the remaining B ingredient that passes both routes; pin, notify the parent,
retain intended-reason mutants, regenerate seed/producer bytes, then request the parent's independent checks.
UNKNOWN or a symmetry-restricted UNSAT leaves the gate open. Caps remain four busy processes including the
parent's reserved slot, 8 GiB RSS, 10 GiB new data, free disk≥12e9 bytes, chunks≤3h, checkpoints≤30min, and the
fixed deadline 2026-10-18 18:31:43 PDT. No new scientific target is introduced by this note.
