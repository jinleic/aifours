# Notes: S(p) <=> IDX1-odd(p+1), and an independent complete finite re-check for p <= 17 (aid), v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:53:10-0700.  Status: the equivalence is a written 3-line argument [W], unreviewed;
the finite check is an aid, never a premise.  Prompted by the parent's IRC route (unproved, not assumed).

## Statements
S(p): every zero-sum-free sequence U of p odd elements of C_(2p) is SC (some odd generator g with least positive
coefficients summing to <= 2p - 1).  IDX1-odd(p+1): every minimal zero-sum sequence of p + 1 odd elements of C_(2p) has
index 1 (some generator g with least positive coefficients summing to exactly 2p).

## Equivalence
(=>) Let M be an all-odd minimal zero-sum of length p + 1 and m a term; U := M - m is zero-sum-free of length p, SC with g
and sum W <= 2p - 1; m = -sigma(U) = (2p - W) g has coefficient 2p - W, so M has coefficient sum 2p: index 1.
(<=) Let U be zero-sum-free of length p and x := -sigma(U), odd (a sum of p odd elements is odd).  M := U x is a zero-sum of
length p + 1, and minimal: a proper nonempty zero-sum S of M avoiding x lies in U; one containing x leaves the nonempty
zero-sum M - S inside U; both contradict zero-sum-freeness.  Index 1 of M with g gives coefficient sum 2p - (coefficient of
x) <= 2p - 1 on U: U is SC.  []
(The general index-one theorem needs length >= p + 2; at length p + 1 it fails with even terms, e.g. 1^(p-2) p (p+1)^2 in
Z_(2p) as noted by the parent; the all-odd restriction is essential.)

## Independent finite re-check (probe v13; aid)
code/sp_falsify_probe_v13.py 9b0d6a7aab239c1b4fa8cb5453afc090cdc00219b83689fb16623ff5ab1a6e88, gated launcher, pid
57453, rc 0, wall 0.08 s; pre/post/stdout sha256 098316ce237a4dbb44355a03de446515466da0b831aae7d5bfd2f3d78f8715cc / 8640e8f4b423e66b698f56afa7607dd4dbb7ff5928505ff19ec189a2b4e09ae2 / 6b4e98dd5afe6929ea62f6e5274ed0c42df9b16d27978c4a0713eef3113c9c45.
Complete canonical DFS (value 1 a most frequent generator value) over zero-sum-free odd multisets:
| p | zero-sum-free, length p | SC | non-SC | zero-sum-free, length p-1 | non-SC at p-1 |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 0 | 6 | 1 |
| 7 | 7 | 7 | 0 | 10 | 2 |
| 11 | 19 | 19 | 0 | 22 | 2 |
| 13 | 30 | 30 | 0 | 33 | 2 |
| 17 | 67 | 67 | 0 | 70 | 2 |
The length-p counts equal sum_(d <= (p-1)/2) p(d) (partitions), i.e. exactly the SC coefficient patterns with g = 1 most
frequent, a built-in consistency control.  Consistent with the earlier round's observation (notes-SC-lengthp-v2.md Sec. 3,
not a premise).  S(p) for p <= 17 could be promoted only by a parent replay/acceptance of an exhaustive check; not claimed.
