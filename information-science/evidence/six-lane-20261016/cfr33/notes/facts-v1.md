# Written facts for lane cfr33 / cfr27 (written 2026-10-17 14:58:09 PDT; proofs by hand, cross-checked by code where noted)

Notation: rows R_0..R_(r-1) are sequences (R_i[c] = symbol in column c); p_i = R_i^(-1) is the position map
(p_i(s) = column of symbol s). Arithmetic in Z_n.

## E1 (position-difference criterion and normal form)
Event (a,b,m) occurs in row i iff p_i(b) - p_i(a) = m (m != 0 automatically for a != b). Inside one row the
events are pairwise distinct ((a,b) determines m). Rows i != j share an event iff there are a != b with
p_i(b) - p_i(a) = p_j(b) - p_j(a), i.e. iff d_ij := p_i - p_j is not injective. Hence the array is a CFR(r,n)
iff every d_ij (i != j) is a bijection of Z_n, iff the number of distinct events is r*n*(n-1).
Symbol relabelling s -> t(s) replaces p_i by p_i o t^(-1) and d_ij by d_ij o t^(-1); rotating row i by c_i
replaces p_i by p_i + c_i and d_ij by d_ij + (c_i - c_j). Both preserve bijectivity, so WLOG p_0 = id and
p_i(0) = 0. In this normal form (f_i := p_i): CFR iff each f_i is a bijection, each f_i - id is a bijection
(i >= 1) and each f_i - f_j is a bijection. Rows are recovered as R_i = f_i^(-1). [Checker B implements the
d_ij test, checker A the events; they agree on every control.]

## E2 (difference matrices)
A (Z_n, k; 1)-DM is a k x n array D over Z_n such that for all rows i != j the n differences D[i][t] - D[j][t]
are distinct. (=>) Given a CFR(r,n) in normal form, the rows 0, f_0, ..., f_(r-1) (functions of t in Z_n) form a
(Z_n, r+1; 1)-DM (differences with 0 are the bijections f_i, the others are the bijections f_i - f_j).
(<=) Given a (Z_n, k; 1)-DM, set e_i = D_i - D_0 (i = 1..k-1); e_i and e_i - e_j = D_i - D_j are bijections from
the column set T onto Z_n. Put p_i = e_i o e_1^(-1); then p_i and p_i - p_j are bijections of Z_n, so the rows
R_i = p_i^(-1) (i = 1..k-1) form a CFR(k-1, n). (code/dm_to_cfr.py implements this direction.)
Consequences: CFR(r,n) <=> (Z_n, r+1; 1)-DM <=> r-1 pairwise orthogonal normalized orthomorphisms of Z_n
(F_c(n) = omega(Z_n) + 1) <=> r-1 mutually orthogonal diagonally cyclic Latin squares of order n. A
(g,k;1)-DM gives a resolvable TD(k,g) (parallel classes indexed by columns), hence TD(k+1,g), i.e. k-1 MOLS(g);
also k <= g for lambda = 1. So CFR(6,21) would give 6 MOLS(21). Only the CYCLIC group Z_n is relevant: DMs
over other groups of order n (e.g. GF(27)^+ = (Z_3)^3, Z_9 x Z_3) are not CFRs.

## E3 (fixed-set lemma for symmetric DMs)
Let D be a (Z_n, k; 1)-DM with column multiset C (|C| = n). Suppose mu in Z_n^* and a row permutation pi are
such that s: (x_0..x_(k-1)) -> (mu*x_(pi^-1(0)), ..., mu*x_(pi^-1(k-1))) maps C onto C (as multisets).
Let F be the set of pi-fixed rows and H = Fix(mu) = {x : (mu-1)x = 0} (a cyclic subgroup).
If |F| >= 2 then the s-fixed columns restricted to F form an (H, |F|; 1)-DM; in particular |F| <= kmax(H).
Proof. For i != j in F the map delta(c) = c_i - c_j is a bijection C -> Z_n with delta(s c) = mu delta(c).
If s c = c then mu delta(c) = delta(c), so delta(c) in H. If x in H and c = delta^(-1)(x) then
delta(s c) = mu x = x = delta(c), so s c = c (delta is injective on C). So delta maps Fix_C(s) bijectively
onto H. For c in Fix_C(s) and i in F, mu c_i = c_i so c_i in H. Hence the |F| x |H| array
(c_i) (i in F, c in Fix_C(s)) has all pairwise row differences bijective onto H. QED.
* Per-row multiplier equivariance (every CFR row in normal form commutes with x -> mu x) is the case pi = id,
  F = all k = r+1 DM rows (row 0 and id are mu-equivariant), so r + 1 <= kmax(Fix(mu')) for every
  mu' in K \ {1}.
* n = 33: every mu' of order 5 (the subgroup <4>, all = 1 mod 3) and mu' = 10 have Fix = 11Z_33 = Z_3, and
  kmax(Z_3) = 3, so r <= 2. mu' = 23: Fix = 3Z_33 = Z_11 (no constraint for r <= 10); mu' = -1: Fix = 0.
  Usable K at n = 33, r = 4: {1}, <-1>, <23>.
* n = 27: every mu' = 1 mod 3, mu' != 1, has Fix = 3Z_27 (order 9; mu' in {10,19}) or 9Z_27 (order 3; mu' of
  order 9). kmax(Z_3) = 3 gives r <= 2 for the latter; for the former r + 1 <= kmax(Z_9) = 3 (no CFR(3,9):
  re-verified exhaustively by code/z9_pairs_check.py). So per-row multiplier models at n = 27 can only use
  K in {{1}, <-1>}; K = <-1> is the odd model.
* Models where mu also permutes rows (Sage DM_33_6_1: mu = 4 with a 5-cycle on 5 of the 6 DM rows; Sage
  DM_21_6_1: mu = 1 with a 5-cycle) are constrained only through their pi-fixed rows.

## E4 (quotient)
If D is a (Z_27, k; 1)-DM then D mod 9 is a (Z_9, k; 3)-DM and D mod 3 a (Z_3, k; 9)-DM (reduction is 3-to-1 /
9-to-1 on differences). Nonexistence of a (Z_9, 6; 3)-DM would therefore exclude CFR(5,27). Not yet tested.
