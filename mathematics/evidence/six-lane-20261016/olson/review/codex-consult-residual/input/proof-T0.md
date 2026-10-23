# Theorem T0 (group-algebra tiling with rotation nesting) for D_{2p}

Lane MathOlson, written 2026-10-16 ~21:15 PDT (host clock 21:11:52 read just before
writing).  Status: written proof [W]; computer sanity checks [C] listed at the end;
NOT yet independently reviewed.

## Statement

**Theorem T0.** Let p be an odd prime and w a word of length 4p-1 over D_{2p}.
Read cyclically, w is a cyclic sequence of maximal runs of reflections
("F-runs") separated by maximal runs of rotations.  If at most one F-run has odd
length, then w has an identity 2p-subword.

(No condition on the values of the letters.)

## Setting

Conventions as in proof-theoremP.md: (v,e)(v',e') = (v+ev', ee'), rho_x = (x,+1),
sigma_y = (y,-1).  For a finite sequence of letters, its ordered product is
(sum_i s_i v_i, prod e_i) with s_i = (-1)^{#reflections before i}.  Existence of
an identity 2p-subword is invariant under cyclic rotation of w (ab = 1 iff ba = 1),
so we may cut the cyclic word anywhere and work with the resulting linear word.

H := Z_p x Z_p, A := F_p[H], J := augmentation ideal.  With s := [(1,0)]-1 and
t := [(0,1)]-1, A = F_p[s,t]/(s^p, t^p) and J = (s,t).

**Fact L (Loewy length).** J^{2p-1} = 0.  Proof: J^{2p-1} is spanned by products
containing monomials s^i t^j with i+j >= 2p-1, hence i >= p or j >= p.  []

For a selection T (set of positions) with an even number of reflections, the
ordered product is a rotation rho_{val(T)}; if moreover |T| is even put
phi(T) := (val(T), |T|/2) in H.

**Fact A (additivity).**
(a) If T_1, ..., T_m lie in consecutive disjoint blocks B_1 < ... < B_m and each
    has an even number of reflections, then val(T_1 u ... u T_m) = sum val(T_i)
    (each partial product is a rotation and rotations commute), and sizes add.
(b) If B = r B' r' with r, r' rotations (values x, x') at the two ends of B and T'
    is a selection inside B' with an even number of reflections, then
    val({r} u T' u {r'}) = x + val(T') + x' (r' lies in a +-zone because T' has an
    even number of reflections).

## Units and their elements

A *unit* is a block of consecutive positions together with an element
theta in A given as an explicit formal sum over selections T inside the block,
each with an even number of reflections and even size, written
theta = sum_T c_T [phi(T)], with the empty selection having coefficient 1.
Its *depth* is any d with theta in J^d.

* single letter: theta = [0] (empty selection only), depth 0.
* "ff" (two consecutive reflections sigma_y sigma_y'):
  theta = [0] - [(y - y', 1)]  (selections: empty; both), depth 1.
* "rr" (two consecutive rotations): theta = [0] - [(x + x', 1)], depth 1.
* **Nest** N = r B' r' where B' is a concatenation of units u_1..u_m (in order)
  with elements theta_1..theta_m:
  theta_N := theta_1 ... theta_m ([0] - [(x + x', 1)]).
  Expanding, every term is c [phi(T)] for the selection T = (union of the chosen
  selections of the u_i) possibly together with {r, r'}: by Fact A(a),(b) the
  group element is exactly phi(T) (even number of reflections, even size), and
  the empty selection has coefficient 1.  depth(N) >= sum depth(u_i) + 1 since
  [0] - [g] lies in J.

## Lemma G (global step)

Cut the cyclic word to a linear word W' and partition W' into top-level units
u_1 < ... < u_K with elements theta_k in J^{d_k}.  If sum d_k >= 2p-1 then w has
an identity 2p-subword.

Proof.  Theta := theta_1 ... theta_K lies in J^{2p-1} = 0 (Fact L).  Expanding the
product term by term (no collection), each term corresponds to a selection T of
W' (union of the chosen selections), with coefficient the product of the chosen
coefficients and group element sum phi = phi(T) by Fact A(a).  The coefficient of
[0] in Theta is therefore 1 (the all-empty choice) plus the sum over nonempty
choices with phi(T) = 0.  As Theta = 0, some nonempty T has phi(T) = 0:
val(T) = 0 and |T|/2 = 0 mod p.  T is nonempty of even size at most 4p-2 (it misses
at least the positions not in W'; in any case |W'| <= 4p-1 and |T| is even), so
1 <= |T|/2 <= 2p-1, whence |T| = 2p; T has an even number of reflections and
product rho_0 = 1.  Undo the cyclic cut.  []

## Proof of Theorem T0

Case 1: exactly one F-run F* has odd length.  Then F is odd and R = 4p-1-F is
even.  Remove the first letter of F* as a single-letter unit and cut the cyclic
word there; the linear word W' (length 4p-2) begins with the remaining l*-1 (even)
letters of F* and every F-run of W' has even length.
Case 2: every F-run has even length.  Then F is even and R is odd.  Remove any
rotation as a single-letter unit and cut there.  F-runs of w adjacent to it
appear at the two ends of W' (or merge cyclically, but in W' each piece is a
whole even run), so every F-run of W' has even length and W' has an even number
of rotations.

In both cases tile W': split every F-run of W' into consecutive pairs ("ff"
units).  List the rotations of W' in order r_1, ..., r_{2m}; for each i form the
nest N_i = r_{2i-1} [ff units strictly between r_{2i-1} and r_{2i}] r_{2i}
(between two consecutive rotations there is at most one F-run, which is whole and
even).  The remaining ff units are top-level.  Every letter of W' lies in exactly
one top-level unit.  Total depth = (#ff units) + (#rotation pairs)
= F'/2 + R'/2 = (4p-2)/2 = 2p-1, where F', R' count letters of W'.  Lemma G
applies.  []

## Lemma TRI (sufficient fullness criterion, for later use)

Let a unit have option set S (its selections' phi-values, i.e. points of H) and
let D < p.  If for every h = 1..D the "level" {v : (v,h) in S} has at least
D+1-h elements, then the unit admits theta in J^D supported on S with
coefficient 1 at the empty selection ("depth D").
Proof.  Use the point-indexed ansatz theta = [0] + sum_{s in S, s != 0} c_s [s]
(one selection representative per nonzero point; for units shorter than 2p the
empty selection is the only one with phi = 0).  theta lies in J^D iff
sum_s c_s P(s) = 0 for every polynomial P of total degree < D (binomial basis
C(v,i)C(h,j) of such polynomials), so such c exists iff every polynomial g of
degree <= D-1 vanishing on S\{0} vanishes at 0 (linear-algebra duality; only the
sufficient direction is used below).  Under the level hypothesis, g(.,1) has
degree <= D-1 and >= D zeros, so (h-1) | g; inductively (h-1)...(h-D) | g,
impossible unless g = 0.  []
[Review fix, Codex 2026-10-17 review/codex-T0-R: duality stated for the
point-indexed ansatz.]

## Computer sanity checks [C] (not part of the proof)

* code/tiling.py exact depth routine: 900 random nests r[U]r (U = up to two rr/ff
  units, p in {5,7,11}) all have depth = len/2.
* 800 random words of length 4p-1 (p in {5,7}) with at most one odd F-run: every
  one has an identity 2p-subword by exact DP (code/coverage_all.has_solution).
