# Written facts used by lane sw25-16 (version 1, written 2026-10-17 before any search computation)

Notation. An SW(n,w) is W in {-1,0,1}^{n x n} with W = W^T and W W^T = w I (equivalently W^2 = w I). B_n is the group
of n x n signed permutation matrices. For a signed permutation H we write H e_j = s_j e_{pi(j)}; then
(H W H^T)_{pi(i),pi(j)} = s_i s_j W_{ij}. [W] = proved here; nothing below is a claim about existence.

## F1 [W] spectrum and trace
W real symmetric with W^2 = wI is orthogonally diagonalizable with eigenvalues +-sqrt(w). For w = 16 let p, q be the
multiplicities of +4, -4 (p + q = n). Then trace W = 4(p - q) = 8p - 4n. Diagonal entries lie in {-1,0,1}, so
|trace W| <= n.
* n = 25: trace W = 8p - 100 in {-20,-12,-4,4,12,20}; in particular the diagonal of an SW(25,16) is not zero.
* n = 27: trace W = 8p - 108 in {-20,-12,-4,4,12,20}.
* n = 29: trace W = 8p - 116 in {-28,-20,-12,-4,4,12,20,28}.

## F2 [W] symmetries of the problem
If W is an SW(n,w) and H in B_n then H W H^T is symmetric, has entries in {-1,0,1}, and
(H W H^T)(H W H^T)^T = H W W^T H^T = w I; so it is an SW(n,w). Also -W is an SW(n,w).

## F3 [W] equivalence of a weighing matrix to a symmetric one
Let W be any W(n,w) (W W^T = wI, not necessarily symmetric). Claim: there are P, Q in B_n with P W Q symmetric iff
there is M in B_n with M W symmetric.
(<=) take P = M, Q = I. (=>) let S = P W Q be symmetric. Then Q S Q^T is symmetric (congruence) and
Q S Q^T = Q P W Q Q^T = (Q P) W because Q Q^T = I. So M = Q P works.
Consequence: deciding "is the equivalence class of W (under signed row and column permutations) free of symmetric
matrices" is the single search "no signed permutation M with M W symmetric". Transposition need not be added: if
P W^T Q is symmetric then so is its transpose Q^T W P^T, which is in the class of W.
Encoding used (code/equiv_cnf.py): M has rows M_{i,pi(i)} = e_i (e_i in {+1,-1}); (MW)_{ij} = e_i W_{pi(i),j}.
MW symmetric iff for all i < j: e_i W_{pi(i),j} = e_j W_{pi(j),i}.

## F4 [W] restricted models are conjugacy-invariant
For a subgroup G <= B_n let Fix(G) = { SW W : H W H^T = W for all H in G }. For K in B_n,
K Fix(G) K^T = Fix(K G K^{-1}) (if H W H^T = W then (K H K^{-1})(K W K^T)(K H K^{-1})^T = K H W H^T K^T = K W K^T).
So "some SW has a symmetric automorphism group containing a conjugate of G" is decided by Fix(G) for one
representative G of its B_n-conjugacy class. Also W in Fix(G) iff -W in Fix(G).

## F5 [W] elements of odd prime order
Let H = (pi, s) in B_n have odd prime order r. Every cycle of pi has length 1 or r. A fixed point i with s_i = -1
would make the order even; an r-cycle whose sign product is -1 would give H^r = -1 on that cycle (order 2r). So
every cycle has sign product +1, and conjugating by a diagonal sign matrix (choose the signs successively along
each cycle) removes all signs: H is B_n-conjugate to an unsigned permutation matrix of cycle type r^s 1^f with
f + r s = n.

## F6 [W] orbit-matrix identities for an unsigned automorphism of prime order
Let g be an unsigned permutation of prime order r with W = g W g^T, fixed set F (|F| = f) and nontrivial orbits
O_1..O_s (each of size r). Invariance gives W_{g(i),g(j)} = W_{ij}. Let C be the n x m orbit indicator matrix
(m = f + s orbits, fixed points are orbits of size 1) and define B_{ab} = sum_{k in O_b} W_{ik} for any i in O_a
(independent of i by invariance). Then W C = C B, so 16 C = W^2 C = C B^2 and, C having full column rank,
B^2 = 16 I (w = 16). For i in F and a nontrivial orbit O put c_{iO} = W_{ij} (j in O; constant in j because
W_{i,g(j)} = W_{g(i),g(j)} = W_{ij}). Then B_{O,i} = c_{iO} and B_{i,O} = r c_{iO}. For nontrivial orbits O, O' the
total of the block (O,O') equals r B_{OO'} and also equals the total of the block (O',O) (W symmetric), so
B_{OO'} = B_{O'O}. Hence, with n_O = #{ i in F : c_{iO} != 0 }:
   (B^2)_{OO} = r n_O + sum_{O'} B_{OO'}^2 = 16.                                                   (E1)
Row weights (all rows have weight 16): for i in F, with f_i = #{ i' in F : W_{ii'} != 0 } <= f and
t_i = #{ O : c_{iO} != 0 }:  f_i + r t_i = 16.                                                     (E2)
For j in O, with w_{OO'} = #{ k in O' : W_{jk} != 0 } (0 <= w_{OO'} <= r):  n_O + sum_{O'} w_{OO'} = 16.   (E3)
Double counting the nonzero c's: sum_{i in F} t_i = sum_O n_O.                                     (E4)
Also |B_{OO'}| <= w_{OO'} and B_{OO'} = w_{OO'} (mod 2).                                           (E5)

## F7 [W] consequences for n = 25, w = 16 (prime orders r >= 5, and r = 3)
From (E1): n_O <= floor(16/r).
* r = 23 (f=2,s=1), 19 (f=6,s=1), 17 (f=8,s=1): n_O = 0, so by (E4) every t_i = 0 and (E2) gives f_i = 16 > f.
  Impossible.
* r = 13 (f=12,s=1): n_O <= 1 and (E3) gives n_O + w_{OO} <= 1 + 13 < 16. Impossible.
* r = 11: f=3,s=2: n_O <= 1 so sum_O n_O <= 2, while (E2) with f_i <= 3 forces t_i >= 2 for all 3 fixed rows,
  sum t_i >= 6, contradicting (E4). f=14,s=1: (E3) gives n_O >= 16 - 11 = 5 > 1. Impossible.
* r = 7: n_O <= 2. f=4,s=3: (E2) with f_i <= 4 forces t_i = 2, sum t_i = 8 > 6 >= sum n_O. f=11,s=2: t_i >= 1,
  sum t_i >= 11 > 4. f=18,s=1: (E3) gives n_O >= 9. Impossible in every case.
* r = 5: n_O <= 3. f=5,s=4: t_i >= 3 (5*2+5 < 16), sum t_i >= 15 > 12. f=10,s=3: t_i >= 2, sum >= 20 > 9.
  f=15,s=2: t_i >= 1, sum >= 15 > 6. f=20,s=1: sum >= 20 > 3. So f = 0 (cycle type 5^5) is the only possibility.
* r = 3: n_O <= 5. f=22,s=1: (E3) n_O >= 16-3 = 13. f=19,s=2: n_O >= 10. f=16,s=3: n_O >= 7. All impossible, so
  f in {1,4,7,10,13} (f = 25 is the identity).
* r = 3, f = 13 (s = 4), refinement: (E3) gives n_O >= 4, so n_O in {4,5}. If n_O = 5 then sum_{O'} w_{OO'} = 11
  over four blocks of size <= 3, so the w's are a permutation of (3,3,3,2); by (E5) three B's are odd and
  sum B^2 >= 3 > 16 - 15 = 1. So n_O = 4, every w_{OO'} = 3 and every B_{OO'} = +-1. (Information only.)
By F5, F7 covers every symmetric automorphism of odd prime order of an SW(25,16): any such automorphism is
B_25-conjugate to a permutation of cycle type 5^5, or 3^8 1^1, 3^7 1^4, 3^6 1^7, 3^5 1^10, 3^4 1^13.

## F8 [W] trace in the semiregular Z_5 model
If g has cycle type 5^5 and W = g W g^T then W_{g(j),g(j)} = W_{jj}: the diagonal is constant on each orbit, so
trace W = 5 * (sum of the five orbit diagonal values) = 0 (mod 5). With F1: trace W = +-20 (p = 15 or 10).

## F9 [W] involutions
An element of order 2 of B_n is conjugate to: a fixed points with sign +1, b fixed points with sign -1 and c plain
transpositions (a transposition whose sign product is -1 squares to -1 on its pair, so it has order 4; a
transposition with sign product +1 is conjugate by a diagonal sign matrix to a plain swap), a + b + 2c = n.
Since H and -H define the same Fix (H W H^T = (-H) W (-H)^T), the classes (a,b,c) and (b,a,c) give the same model;
we list a >= b.
* c = 0, b >= 1, a >= 1: H = diag(I_a, -I_b) forces W_{ij} = 0 between the two parts, so W would be the direct sum of
  an SW(a,16) and an SW(b,16) with a + b = 25; both need order >= 16. Impossible. (c = 0, b = 0 is H = I.)
* For a swap pair (j,k) = (j_t,k_t): rows j and k agree on the a positive fixed columns, are negatives on the b
  negative fixed columns, and on the other pairs (j_u,k_u) row j reads (A_tu, B_tu) and row k reads (B_tu, A_tu)
  with A_tu = W_{j_t j_u}, B_tu = W_{j_t k_u}. Their inner product is
     nP(t) - nN(t) + 2 sum_u A_tu B_tu = 0,                                                       (E6)
  where nP(t), nN(t) count the nonzeros of row j on the positive / negative fixed columns.
  For b = 0: nP(t) = -2 sum_u A_tu B_tu <= 2c and the weight of row j is nP(t) + sum_u (|A_tu| + |B_tu|) <= 2c + 2c,
  so c >= 4 when b = 0.
(Information for the order of the involution batch; every involution class that is run is run without using F9.)
