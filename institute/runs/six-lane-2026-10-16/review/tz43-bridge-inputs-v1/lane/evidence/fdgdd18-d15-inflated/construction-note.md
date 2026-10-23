# FDGDD(3,4,5{18}): bare H-design inflation with newly found frames

Finite witness explanation for raw SHA-256
`3e22f5021631ac82ea5b5fa6f884984bb874f1f9a384fd35bfeff523e731a998`.
Source definition: Tan–Zhou arXiv:2503.11934v1 LF241–247 in the pinned text (SHA `df52a8f1…4c3c8164`):
a GDD(3,4,90) of type18⁵ whose derived design at every point is KF(18⁴). This is the same definition as
FDH(5,18,4,3). The raw checkers verify this definition directly, not by accepting the construction.
No priority, novelty, formal-proof or completed-gate claim is made here.

## 1. The master is a bare H(5,6,4,3), not a frame-derived seed

`master_H_5_6.json` pins540 quadruples on30 points in five groups6i…6i+5, together with30 explicit master
permutations. The group is D15 of order30, generated abstractly by r,s with r¹⁵=s²=1, srs=r⁻¹; groups are
left cosets of K=⟨r⁵,s⟩, |K|=6, under its regular action on the30 labelled points. Its KM model is pinned
in `master-inputs/`. The reconstructed model matches its CNF SHA exactly,
`7610a93110d5f4a6972fae9f30a31fafaae396a4c57b8bc5db9080f6f7fca74a`; the actual SAT model is checked
against that CNF. Independently of SAT, the producer checks all2160 transverse triples of the540-block
master once. Its30 permutations preserve the blocks.

**No hypothesis of a KF(6⁴) at the master points is used.** In fact, an exact finite diagnostic shows this
particular master is not frame-derived: at point0 the four missing-group families each have18 triples;
exhaustive enumeration of all C(18,6)=18564 candidate perfect matchings yields counts1,1,0,1, and no
three-class decompositions. The third family has no perfect matching at all. Code/receipt:
`code/diagnose_h6_frame.py`, `master-nonframe-diagnosis-v1.json`. Its positive control is a known KF(6⁴),
with nine matchings and six decompositions in each family. This says nothing about nonexistence of
FDGDD(3,4,5{6}) in general.

## 2. Inflate only the blocks by the explicit local RDTD(3,4,3)

Replace p by (p,β), β∈Z3, labelled3p+β. Each master group becomes a group of18 points. On every sorted
master block {p0,p1,p2,p3}, put all27 quadruples {(p_i,β_i)} with
β0+β1+β2+β3=0 in Z3. This is an H(5,18,4,3): a transverse triple has a unique master completion, and its
fourth copy coordinate is uniquely determined. Count540·27=14580 blocks and58320 transverse triples.

The local RDTD(3,4,3) is explicit and independently checked (`local_RDTD_3_4_3.txt`, SHA `fcdb4285…3d58`):
at fixed copy coordinate a, the triples (u,u+t,u−a−t), u∈Z3, form three parallel classes indexed by t.
This local ingredient is not inferred from Theorem2.5's sufficient gcd criterion (which does not cover3).

## 3. Find frames after inflation, rather than lifting nonexistent master frames

At (0,α), α=0,1, there are648 derived triples. A fixed-design SAT model partitions them into36 classes:
nine classes for each of the four missed groups, each a parallel class of the other54 points. The model
has26892 variables and63432 clauses at each representative. With seed1, the two models solved in about
2.17s and3.88s. Their output classes are subsequently checked directly by both definition-first routes.
This is the genuinely non-natural colouring step: the size18 frames are not projections/lifts of
size6 frames. Only the block-inflation proof above is used before the new frame search.

Every master permutation e acts as (p,β)↦(e(p),β), preserving the inflated block set. Copy negation
(p,β)↦(p,−β) also preserves it and maps representative(0,1) to(0,2). The master action is regular, so
these maps transport the two computed frames to all90 points. The actual raw certificate lists every
point's frame, and the checkers assume no action. In particular, no claim is made that the chosen frame
at copy0 is invariant under copy negation: only the designated transport maps are used.

## 4. Reproducibility and scope

* Both raw routes PASS on the pinned file:14580 blocks,58320 transverse triples once,36 frame classes at
  all90 points. Eight retained mutations are rejected by both for the intended reasons.
* `code/replay_fdgdd18_chain.py` re-solves the pinned bare-master CNF with seed0, then re-solves both
  inflated frame models with seed1 and regenerates byte-identical raw output.
* `code/seed_fdgdd18.py` independently reconstructs all blocks and point frames using only the540
  master blocks,30 master permutations and representative frames0,1; it reproduces the raw bytes
  without SAT or producer imports. A transposition(0 1) is rejected as a block automorphism.

All are finite checks. The infinite-family consequence uses the certified size18 FDGDD itself, together
with gcDCQS(18⁴:2), via source Construction2.3; it does not require a frame-derived size6 seed.
