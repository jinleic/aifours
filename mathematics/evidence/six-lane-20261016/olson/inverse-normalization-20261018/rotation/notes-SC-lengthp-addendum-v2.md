# Notes SC at length p, addendum v2: three further proved tools (the open case remains open)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T08:31:59-07:00.  Status NOTES [W]: proved partial
tools only; S(p) is NOT proved.  Continues notes-SC-lengthp-v2.md (0c991ac3...0adf) and addendum v1 (fc3feae3...a9c0);
addendum v1 is unchanged and remains valid.  Correction of purpose (from the Claude engine review M1 and
proof-ELT0-FEW-v3.md): through SHgen, S(p) would give the kappa = 0 slice of ROT only for 5o <= 4p - 1, not for every
o <= p; the 'every o' purpose lines of v1/v2 relied on the unaccepted Corollary ELT0-ROT.

Setting: Y = (1, x_1) ... (1, x_p) zero-sum-free in Z_(2p) = Z_2 x Z_p; X = (x_1, ..., x_p) in Z_p.  Then every
nonempty zero-sum subsequence of X (in Z_p) has odd length (an even one would be a zero-sum of Y).

(T1) Intersecting family.  Two zero-sum subsequences of X always share a term (two disjoint ones would form an even
zero-sum); and for every zero-sum Q of X, X - Q is zero-sum-free in Z_p (a zero-sum Q' of X - Q is odd, so Q Q' is an
even zero-sum).  X itself contains a zero-sum (p terms in Z_p; prefix sums), necessarily of odd length.
(T2) Reduction.  If X contains 0, or if X - x is zero-sum-free in Z_p for some term x, then Y is SC.  Proof: if X - x is
zero-sum-free of length p - 1, then for every ordering its p - 1 partial sums are distinct and nonzero, hence all of
Z_p - {0}; exchanging two consecutive terms changes exactly one partial sum, so those two terms are equal, and
X - x = c^(p-1), c != 0.  The zero-sums of X are then c^j x with j c + x = 0; they have odd length j + 1, so x = -j c
with j even in [0, p-1].  If j = 0 (x = 0), Y = g^(p-1) (p g) with g = (1, c); otherwise x has g-weight p - j (odd,
in [1, p-2]) and Y = g^(p-1) ((p-j) g), of total weight 2p - 1 - j.  Either way Y is SC.  (If X contains 0, X - 0 is
zero-sum-free by (T1).)  So in the open case every term of X is avoided by some zero-sum, while all zero-sums pairwise
intersect.
(T3) Exchange lemma.  Let Y (zero-sum-free in Z_(2p), any length L) contain g^A u^B, and let alpha g = beta u with
1 <= alpha <= A and 1 <= beta <= B.  Then Y with alpha copies of g replaced by beta copies of u is zero-sum-free.
Proof: a subsequence g^i u^j S of the new sequence (S outside the two values) with j <= B lies in Y; if j > B, then
j - beta in [0, B] and g^(i+alpha) u^(j-beta) S lies in Y, is nonempty and has the same sum.  []
Iterating (alpha copies of g remain available floor(A/alpha) times), if beta > alpha then
L + floor(A/alpha)(beta - alpha) <= 2p - 1, and symmetrically if alpha > beta then L + floor(B/beta)(alpha - beta) <= 2p - 1.
Example: in the pure form of addendum v1 with U = u^s and g = 3u (alpha = 1, beta = 3), L = p gives p + 2M <= 2p - 1,
i.e. M <= (p-1)/2, contradicting s <= M (s = p - M).  Such relations exist whenever M s > 2p (a nonzero point of the
lattice {(i, j) : i g + j u = 0} in [-M, M] x [-s, s] by Minkowski; a point with i j >= 0 would be a zero-sum), but the
two inequalities above need not contradict when |beta - alpha| is small, and a general U has many values: the pure
form stays open.
