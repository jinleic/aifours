# Notes SC at length p, addendum v1: reduction of the open large-s case to a pure form

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T07:47:41-07:00.  Status NOTES [W]: one proved
reduction lemma, a reformulation and finite observations.  Not a proof of S(p); no import of Savchev-Chen.  Extends
notes-SC-lengthp-v2.md (0c991ac3...0adf; notation (1e): generator g, FULL prefix T with A(T) = [0, M] in g-units,
jumpers U, s = p - M; (1f)-(1g): a stuck process at length p has 3s >= p + 4).

## 1. Lemma (pure form)

If S(p) fails, there is a zero-sum-free sequence Y = g^M U of odd elements of Z_(2p) with
 (P1) |U| = s = p - M and 3s >= p + 4;
 (P2) every u in U has g-weight in [M + 2, 2p - M - 1] (a jumper);
 (P3) every value of U occurs at most M times (so g is a most frequent value of Y);
 (P4) Y is not SC.
Proof.  Let Y0 be a non-SC zero-sum-free odd sequence of length p and g a most frequent value of Y0 (multiplicity m).
Its AP process is stuck (FULL would make Y0 SC), with prefix T (n_A <= M terms), jumpers U0, t = p - n_A >= s, and
3s >= p + 4 by (1g).  All copies of g lie in T, so every value of U0 occurs <= m <= n_A <= M times.
(i) Y1 := g^M U0 is zero-sum-free: a nonempty zero-sum g^i V (i <= M, V in U0) gives T' V with T' in T of g-weight i
(A(T) = [0, M]); T' V is nonempty (if V is empty then i >= 1 and i g = 0 forces i >= 2p > M), a zero-sum of Y0.
(ii) Delete any t - s jumpers: Y := g^M U with |U| = s keeps zero-sum-freeness, (P2), (P3), and its AP process is
stuck at M.  (iii) If Y were SC, its SC generator would have multiplicity >= (3p - (2p - 1))/2 = (p + 1)/2 > p/2,
hence be the unique most frequent value, i.e. g, and the process relative to g would be FULL: so (P4).  []

## 2. Reformulation (half-offsets)

Write the g-weight of u in U as p + 2 eps_u (it is odd, p is odd), eps_u an integer in [-(s-2)/2, (s-1)/2].  For a
nonempty sub-multiset V of U with j terms and E := sum_V eps, the zero-sum-freeness of Y = g^M U is equivalent to:
 * j even: E mod p in [1, floor((p + s - 1)/2)];
 * j odd:  E mod p in [0, floor((s - 1)/2)] u [(p + 1)/2, p - 1].
(Proof: V g^i has g-weight jp + 2E + i, i in [0, M]; it is never 0 mod 2p iff (jp + 2E) mod 2p lies in
[1, 2p - M - 1] = [1, p + s - 1]; split by the parity of j.)  So the open case asks: can s = p - M >= (p + 4)/3 small
integers eps (each value at most M times, value 0 at most once) satisfy these window conditions for every sub-multiset?
Immediate consequences: two eps with negative sum have sum <= -(M + 1)/2; an odd number of terms with small positive
sum has sum <= (s - 1)/2; at most one eps equals 0.  For s <= (p + 3)/3 the window [(s+1)/2, (p-1)/2] cannot be jumped
by positive partial sums, which is the mechanism of (1f); for larger s it can, and (P3) must be used: the sequence
g^((p-1)/2) u^((p-1)/2) with u = 3^(-1) g (length p - 1, zero-sum-free, SC relative to u) shows that s - 1 equal
jumpers are possible at length p - 1, and e.g. at p = 11 the pure form with M = 5 and U = u^6 (eps = 2) satisfies every
window condition but violates (P3) (6 > M).

## 3. Observations [O] (code/sc_stuck_v1.py cfdbb48b...00ff, out/sc_stuck_v1.jsonl 37ee566d...e5ac7; not premises)

Over all zero-sum-free odd multisets of Z_(2p), p = 11, 13, 17, 19, and every most frequent value g: the AP process
is stuck only at lengths <= p - 1; for every s the longest stuck example is listed, and the large-s maxima at length
p - 1 are the ties g^((p-1)/2) u^((p-1)/2), g = 3u.  So no pure-form sequence exists for these p.

## 4. Status

S(p) remains open in this lane for s >= (p + 4)/3; the reduction leaves exactly the pure form of Sec. 1-2.  The
kappa = 0 slice of ROT beyond 3 o_F <= 2p + 1 is therefore still conditional on S(p).
