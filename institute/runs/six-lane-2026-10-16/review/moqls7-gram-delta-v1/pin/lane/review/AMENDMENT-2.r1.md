# Protocol amendment 2: three K3 row-frame cubes and forced same-ray identities

This amendment is to be frozen before generating or searching the new K3 instances. It changes only the necessary
representation used after the original Gram K3 chunk returned UNKNOWN at its 3600-second cap. It does not exclude
K3 or establish M(7). It depends on the minimal-counterexample G4 bridge in `GRAM-ENCODING.r1.md`, hence on the
K1/K2 exclusions before any unrestricted claim.

## 1. Three cubes cover K3 up to residual symmetry
The frozen K3 instance already fixes square 1 to have neighbours (0,1), (0,2), (0,3) at p = (1,0), using row 0 as
its frame. Define S_a = {k in {1,...,6}: g_a(p,(0,k)) = 1}. For each a, S_a is nonempty, because row 0 is an ONB.
The S_a are pairwise disjoint by G5, and S_1 contains {1,2,3}. Thus only these unordered size types occur:

| cube | S_1 | S_2 | S_3 | unused coordinates |
|---|---|---|---|---|
| C311 | {1,2,3} | {4} | {5} | {6} |
| C321 | {1,2,3} | {4,5} | {6} | empty |
| C411 | {1,2,3,4} | {5} | {6} | empty |

Proof of coverage: S_1 has size 3 or 4 (the other two are nonempty). For size 4 the others are both singletons.
For size 3 the remaining three coordinates split as sizes (1,1) with one unused, or (2,1)/(1,2). The residual
permutations of columns 4,5,6 and exchange of squares 2 and 3 put each case into the displayed representative.
These permutations preserve the fixed heavy triple and every G1-G5 condition. The cube fixes all 18 predicates
{g_a(p,(0,k)): a=1,2,3; k=1,...,6}, not only its positive literals.

A separate finite coverage control will enumerate all 4^3 assignments of coordinates 4,5,6 to unused/square1/
square2/square3, retain those with squares 2 and 3 nonempty, and check that the resulting 18 assignments are exactly
the residual-symmetry orbits of the three displayed cubes. This control checks coverage of predicates, not vector
existence.

## 2. Forced same-ray identities (G6, valid in the corresponding cube)
If S_a = {k}, the unit vector psi_a,p has exactly one nonzero coefficient in the ONB of row 0. Its norm is one,
so psi_a,p is a unit phase times psi_a,(0,k). Hence for every t other than p and (0,k):

    g_a(p,t) = g_a((0,k),t).

These are exact Gram-support equalities, not an ansatz. When a predicate is absent because its pair is collinear,
its value is false. A singleton in C311/C411 gives this equality in squares 2 and 3; C321 gives it in square 3.
No equality is imposed for a support with more than one coordinate. The argument is independent of phases,
fields, and magnitudes.

## 3. Procedure and stop rules
- Leave both frozen base encoders untouched. Append cube units and the above G6 equalities to their generated CNFs.
- A dedicated wrapper reads each encoder's actual g-variable order; it must confirm those orders agree with the
  frozen encoders' construction. Encoder A exposes its variable map. Encoder B creates exactly these g variables
  first in square, point, later-point order, omitting collinear pairs; this construction is replayed independently.
- Generate the finite coverage receipt before solver use.
- Screen the three cubes sequentially, at most one solver, each with a native 1800-second cap. No certification
  pipeline is overlapped. A SAT model is kept as a pattern only; UNKNOWN remains UNKNOWN.
- After successful screening, regenerate identical CNFs and stream DRAT proofs through the bounded monitored
  driver. Every acceptance requires an exact checker verdict, solver rc 20, and no safety stop.
- Each cube's claim remains conditional on whole-bridge review. Only exclusion of all three covering cubes under a
  sound bridge would exclude K3.
