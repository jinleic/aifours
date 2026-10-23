# CFR(6,21) lane plan v1 (ContinueCFR21) — frozen 2026-10-18T23:33:57-0700

Target (unchanged, frozen in the old contract 498efb75…): construct CFR(6,21) = a 7-row difference matrix over CYCLIC Z_21,
or prove unrestricted nonexistence. Status: OPEN. Inputs: evidence/inherited-map-v1.json (cff22b61…),
evidence/stop-registry-v1.json (0c758fa4…). Restricted results below are never promoted to the target.

## Baseline facts measured this round (frozen stdlib probes, receipts under evidence/probes/)
* p1-p21-structure-v1-a2 (stdout e7eb039e…): all 96 pinned P21 six-row Z21 DMs pass; their 20 row triples have mod-3
  sum types only (3,2,2)x10, (3,3,1)x5, (4,2,1)x5 (every DM identical profile); no constant translation-invariant
  mod-3 character; mod-3 affine rank 5 (full); ZERO 7-column mod-7 blocks (so no three-affine-block CRT structure).
  (attempt p1-p21-structure-v1 failed before any computation: relative probe path; retained.)
* p2-p21-mod7-rank-v1 (stdout 7ba5aad4…): mod-7 affine rank 5 (full) and no mod-3 twin columns in all 96.
  => the only known Z21 DM6 family has GENERIC (full-rank) projections; old CRT families were rank-deficient.

## New representation PROJ (projection stratification), to be written as proofs in evidence/proj-theory-v*.md
n = 3q, gcd(3,q)=1 (here q=7). A (Z_n,k;1)-DM is exactly a pair (alpha mod 3, beta mod q) with
 (i) alpha a (Z3,k;q)-DM, (ii) beta a (Zq,k;3)-DM, (iii) fibre orthogonality: for every row pair the q-classes of
 beta_i-beta_j (size 3) carry three distinct values of alpha_i-alpha_j (equivalently CRT bijectivity).
Planned lemmas (all unrestricted, elementary):
 PROJ-1 uniformity principle: if a homomorphism of the column image onto an abelian B pulls every nontrivial
        character of B back to a root character (x_i - x_j, up to constant on the image), the pushforward is
        uniform, so |B| divides n. (L3 is the case B=F3^2.)
 PROJ-2 mod-3: no constant translation-invariant character of support <= 5 (triples = L3, pairings, (4,1));
        every 4 rows have mod-3 affine rank 3.
 PROJ-3 mod-q set property: for k>=4 no two columns coincide mod q up to translation; mod-q rank >= 2.
 PROJ-4 rank strata: beta = 7 distinct row functionals on F_q^r plus a 21-point SET S with every root-direction
        hyperplane carrying exactly 3 points; uniformity forbids root-direction sets containing a full line of
        PG(r-1,q) (Redei-type restriction for r=2).
Exact anchors: the 96 P21 DM6 (generic ranks, measured), small prime/Z9/Z15 controls, CRT-lift controls.

## Bounded decisive experiment LR (needs item-specific parent GO before any native run)
Exhaust every (Z21,7;1)-DM whose mod-7 image has affine rank <= 3 (then rank 4 if measured cost fits), exactly:
enumerate row-functional configurations up to AGL(r,7) x S7, the 21-point sets S by exact cover, then the EXACT
F3 lift (147 triple-sum equations + inequalities), every lift re-checked over Z21. Scientific consequence if
complete and negative: theorem-level restricted exclusion "every CFR(6,21) has mod-7 affine rank >= 4 (resp. 5)",
strictly containing the old common-parallel-line and common-slope CRT families. It is NOT unrestricted
nonexistence; the generic full-rank stratum stays OPEN. A lift found = candidate, immediately to parent.

## Not planned
No ADD-26/27/28 resumption, no old driver reuse, no g00/g10 rerun without a new representation, no SAT supervisors.
Primary refresh (CPro1 OPEN_INSTANCES, MOLS table entry n=21, recent arXiv/DataCite hits) before any large search.
