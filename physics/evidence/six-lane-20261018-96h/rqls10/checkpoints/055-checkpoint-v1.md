# Physics-2 checkpoint055 - F-closure: complete argument derived (working form); note being written

Actual `/bin/date` before this write: 2026-10-19T18:13:27-0700. Previous checkpoint054 18:00:14 (13m13s). Next target
18:33:27, binding 18:43:27.

## Actual partial result (after the scope freeze fb3caaa5...8049; being written with proofs into 01-...)
Expected outcome CLOSURE, with an argument that needs no roots and no numerics:
1. Column form: a Z-flat H is X- and T-flat iff its column-1 function has Fourier support {1,2,3} and its column-2
   function support {1,2,4}; column 2 is fixed by column 1 through the Z-triangle invariants (invariant under diagonal
   conjugation).
2. Column-1 classification (degree-2 Fejer-Riesz, proved via a polynomial identity on the 5th roots of unity): the
   column 1 of any flat diagonal conjugate of P_tau is, up to a constant, one of four root choices R0 = col1(P_tau),
   R1 = col1(P_(-tau)) (reciprocal-conjugate polynomial), R2, R3 (real-coefficient polynomials a + bY + cY^2, a != c).
3. Pair lemma: two flat planes in the orbits of P_tau and P_(-tau) with proportional column 1 force the vectors of
   column sums to be complex multiples of one real vector, PROVIDED the triangle invariants do not share a phase (F1).
4. Exact inequalities (signs of explicit products): F1 for both classes; F2 = p01/p23 not real. Case R1 contradicts F2;
   case R2/R3 (pair with the Pi-image) forces a = c, contradiction. Hence E P_tau E^* flat iff E = lambda Z^c.
5. Extensions: Z-couples of any WH translate (unconditional given flatness of P_tau); T, X couples via U (explicit
   hypothesis from the unreviewed E2/E3 candidate); W8 with one F-plane excluded CONDITIONAL on the internal-F theorem.
Hypotheses to be exposed (not re-derived here): flatness of the four P_tau and U facts (E1/E2 candidates), W8 couple
structure and internal-F Theorem B (E2/E3 candidate c625b377...08ec).

## Scope
No computation, scripts, CLI beyond /bin/date, shasum, chmod; decimals only as orientation. Earlier slices untouched.
Global HOLD unchanged; full flat-plane classification and 1-RQLS(10) remain OPEN.
