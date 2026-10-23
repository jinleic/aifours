# Structural note S5 — no column-fixing automorphisms for 3 || n, k odd (2026-10-19T04:25:46-0700, ContinueCFR21)

Status: worker proof, UNREVIEWED. Uses only Lemma L3 (= Theorem A, support 3; parent CORRECTNESS_ACCEPTED scoped partial,
verdict NEW RUN/review/cfr21-theoremA-parent-verdict-v1.md 937b980e...). No novelty claimed.
Generalises structural-note-S1-v1.md (5427feb3...) Observation O1 from the single element (-1,(12)(34)(56)).

## Lemma S5
Let 3 | n, 9 ∤ n, k odd, k >= 5, and let D be a (Z_n,k;1)-DM (rows R, column set C, no normalisation assumed).
Let s = (mu, pi, tau) (mu a unit, pi in Sym(R), tau in Z_n^R) act by (s.c)_x = mu c_(pi^-1 x) + tau_x.
If s.c = c for EVERY column c, then s is the identity (mu = 1, pi = id, tau = 0).

## Proof
s.c = c for all c means, as functions on C:  D_(pi x) = mu D_x + tau_(pi x) for every row x.        (*)
(1) pi = id. Then (mu - 1) D_x = -tau_x is constant for every x; for x != y, (mu - 1)(D_x - D_y) is constant while
    D_x - D_y is a bijection C -> Z_n, so (mu - 1) Z_n = {0}, mu = 1, and then tau = 0.
(2) pi != id. Pick x with y = pi x != x. By (*), D_y - D_x = (mu - 1) D_x + tau_y is a bijection. If mu - 1 were not a
    unit its values would lie in one coset of the proper subgroup (mu - 1) Z_n; so mu - 1 is a unit and D_x is a
    bijection. Since 3 | n, mu = ±1 (mod 3) and mu - 1 is a unit mod 3, so mu = -1 (mod 3).
    (a) No cycle of pi has length >= 3: otherwise D_(pi^2 x) - D_x = (mu^2 - 1) D_x + const is a bijection, but
        mu^2 - 1 = 0 (mod 3) is not a unit.
    (b) Hence pi is a product of transpositions; k odd gives a fixed row z, and pi != id gives a transposition (x y).
        From (*) at z: (mu - 1) D_z = -tau_z, so D_z is constant (mu - 1 a unit). From (*) at x: D_y = mu D_x + tau_y;
        reducing mod 3 with mu = -1: a_x + a_y = tau_y (mod 3) is constant, and a_z is constant. So the sum-zero mod-3
        character e_x + e_y + e_z (support 3) is constant on the columns, contradicting L3 (k >= 4). ∎
(For k even the same proof leaves only fixed-point-free involutions pi with mu = -1 mod 3 and mu^2 = 1 mod n; not needed.)

## Consequences (scoped)
* For n = 39 (and 21, 33, 51, ...) and k = 7 the automorphism group of any DM acts faithfully on the column set.
* The "skew" mechanism of the two known nearby seven-row cyclic DMs — DM35 (Sym2026 Ex. 3, twisted element
  (-1,(12)(34)(56),tau') fixing all 35 columns) and Sage DM_55_7_1 (untwisted (-1,(03)(14)(25)) fixing all 55 columns)
  — cannot occur for 3 || n with k = 7, in any variant (mu, pi, tau). Computation in S1 confirms both examples have such
  a kernel element; 3 ∤ 35 and 3 ∤ 55.
* Calibration consequence for this lane: re-finding DM35 in model z35_m1 exercises an instance whose existence relies on
  this excluded mechanism, so it is not a positive analogue for z39_m1. No known seven-row cyclic DM with 3 || n is
  available as a same-mechanism calibration (the Singer-type (57,8;1)-DM uses a pure row group AGL(1,8) of order
  56 = n - 1; for n = 39 no faithful group of order dividing 38 with an element of order 19 exists, since 19 ∤ |Z_39^*| = 24
  and pure row permutations act on 7 rows).
This is a restriction of mechanisms only, not a statement about the existence of a (Z_39,7;1)-DM.
