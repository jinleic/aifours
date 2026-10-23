# Notes: independent check of the parent's involution reduction of S(p), and an all-unit reformulation, v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:56:16-0700.  Status [W], unreviewed; complements evidence/notes-Sp-IDX1-v1.md
(7af84f0d...1e53).  Write C_(2p) = C_2 x C_p; odd elements are (1, x); the involution is pg = (1, 0); 'unit' = odd element
other than pg (an odd generator).

## 1. The involution case (parent's argument, checked)
(a) Let U be zero-sum-free, |U| = p, odd, containing pg.  U' := U - pg has x-projection X' (length p - 1 in C_p) which is
zero-sum-free in C_p: an even-size zero-sum of X' is a zero-sum of U; an odd-size one plus pg is an even-size zero-sum of U.
A zero-sum-free sequence of length p - 1 in C_p is constant, X' = h^(p-1) with h != 0 (classical: subset sums grow by at least
one per term, so by exactly one, which forces equal terms).  With g := (1, h): U = g^(p-1) (pg), coefficient sum 2p - 1: SC.
(b) Let T be an all-odd minimal zero-sum of length p + 1 containing pg.  The x-projection of T - pg is a minimal zero-sum of
length p in C_p (a proper even-size zero-sum, or a proper odd-size one plus pg, would be a proper zero-sum of T), hence h^p,
and T = g^p (pg) has index 1.
So S(p) (equivalently IDX1-odd(p+1)) reduces to sequences of units only.

## 2. All-unit reformulation
For units, a_i(g) (the least positive coefficient w.r.t. g = (1, c)) is b_i := x_i / c mod p in [1, p - 1] when b_i is odd and
b_i + p >= p + 2 when b_i is even.  A coefficient sum <= 2p - 1 over p terms leaves room for no term >= p + 2 (the other
p - 1 terms contribute >= p - 1).  Hence, for a unit sequence U of length p:
    U is SC  <=>  some c in Z_p^* has every x_i / c in {1, 3, ..., p - 2} with integer sum <= 2p - 1.
And U is zero-sum-free in C_(2p) <=> its x-projection has no nonempty EVEN-size zero-sum in C_p.  So the remaining content of
S(p) is: p nonzero residues mod p with no nonempty even-size zero-sum are, after a dilation, odd integers in [1, p - 2] with
integer sum <= 2p - 1.  Structure available (not yet used to a proof): every zero-sum of the projection has odd size >= 3, any
two zero-sums intersect, and no zero-sum properly contains another; with M a minimal zero-sum, U - M is zero-sum-free in C_p.
