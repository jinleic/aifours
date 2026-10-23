# K7-A2-ZT5-erratum-v3: a written t-row lemma before Corollary L is used

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T08:04:57-0700.
- **Owner:** Sun7K62Successor. No computation. Materially new step; candidate, pending the parent-owned A2 review.
- **Overlays:** `K7-A2-ZT5-A-v1.md` 4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919, `K7-A2-ZT5-B-v1.md` f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8,
  erratum-v1 82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4, erratum-v2 c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47. No original is changed.

## Why this additional step is needed

The proof of A1-STRUCT Corollary L begins with entries in {1,2,4}. Before Lemma ZW(ii) establishes W3* empty, one
cannot import that prerequisite for alpha*_tu. In both Lemma ZW(ii) and ZT5-B Step 1 the needed connectedness is for
Gamma^alpha, and alpha*_zt = 1. Lemma ZT below proves the required t-row conclusion directly, allowing threes initially;
it is to be inserted before the use of Corollary L in those two steps. This is not an accepted import.

## Lemma ZT (the t-row, allowing threes initially) [NEW]

In (a2-zt5), normalized alpha_zt = 5 and alpha*_zt = 1, if Gamma^alpha = {uv in W : alpha_uv <= 2} is connected, then
alpha*_tu is in {1,2,4} for all u in W and **at least two of these five entries equal 4**.

*Proof.* Work at apex t of C^alpha. Write b_u = alpha*_tu, d_u = b_u r_u, d_z = r_z = 2^E w_z. Lemma F gives b_u <= 4
for u in W; W = W' cup {p}, r_p = 5^B w_p, r_u = w_u on W'. The r_u (u in W) are odd, pairwise coprime, prime to 3,
and only r_p carries 5. Since no b is 5, every gcd among d_u is exactly gcd(b_u,b_v). The extra label d_z is coprime
to a one- or three-label, and has gcd 2 with any two-label.

PFG-t(i)-(ii) holds here as an index argument, without a row-type assumption: order W along a spanning tree of
Gamma^alpha. The base factor is <= 2 and every later factor k <= 2. Before p enters no factor 5 has entered; thus
its gcd with the current intersection index is 6, just as for other W-vertices. Consequently T_W = 6 product_(u in W)
r_u times a power of 2, so gcd(n_t,T_W) = 6 (n_t = 6 3^A w_t), and G0 gives mu(U_t W_W) >= 1/6. This product avoids
every D_u for u in W. Hence every feasible y on W has value sum_(u in W) y_u b_u <= 5. If equality holds, their union
has measure 5/6, mu(U_t W_W) = 1/6, and each occupied right U_t-coset in that union has y-weight 1. Since D_z has
measure 1/6 and avoids U_t, it must meet that union in a right U_t-coset; that coset's W-vertices, together with z,
must be allowed. This is PFG-t(ii), using only b_z = 1, not that the b_u avoid 3.

Let k be the number of b_u = 3. Three-labels cannot share a fibre with any other W-type (Sun(2)). On the k three-labels
use weights 1/min(3,k); allowed sets have at most three such elements (Sun(4)). Their value is 3 when 1 <= k <= 3,
and k when k >= 3. Standard E8 weights on the remaining 5-k vertices of types 1,2,4 have value >= min(5-k,4).
If k = 1 or 2, the total is >= 7 or 6, impossible. If k = 3, only remainders (1,1) and (2,2) avoid a value > 5:
(1,2) has value 3, (1,4) value 5, (2,4) value 3, and (4,4) value 4. The two surviving remainders have value 2, so the
full vector (threes 1/3, ones 1 resp. twos 1/2) has value exactly 5. Its weight-1 W-sets are a triple of threes, a single
one, or the pair of twos. None is allowed together with z: a three or a one is coprime to d_z (Sun(2)); z and two twos
have all pairwise gcds 2 (Sun(3)). This contradicts the equality clause. If k = 4, the one remaining entry must be 1
(otherwise value >= 6); the value-5 vector has weight-1 sets a triple of threes or the single one, again impossible with
z. If k = 5, weight 1/3 on all five has value 5 and each weight-1 set is a triple of threes, again impossible with z.
Thus k = 0.

Now b_u in {1,2,4}. If there is one four, weight 1 on ones and 1/2 on each two and the four is feasible and has value
6 when there is a two; if there is no two, weight 1 on all five gives value 8. If there is no four and a is the number
of twos, a = 1 gives value 6 (all singletons); a = 0 or a >= 2 gives value 5 with ones of weight 1 and twos of weight
1/2. In the equality cases every weight-1 W-set is a single one or a pair of twos, neither allowed together with z
(as above). These contradictions prove at least two fours. QED

## Active changes

1. In erratum-v2 Lemma ZW(ii), the sentence invoking Corollary L's at-least-two-fours conclusion is to invoke **Lemma ZT**
   instead, after the same proof of connectedness of Gamma^alpha. All other steps of ZW are unchanged.
2. In ZT5-B Step 1, replace its initial invocation of PFG-t / Corollary L with **Lemma ZT**. Connectedness follows from
   the displayed A x B subgraph in that step; the conclusions and the rest of Step 1 are unchanged.
3. The broad consequences paragraph of Lemma FG-zf must not be read as asserting the full Corollary L while W-threes
   remain unresolved. For (a2-zt5), the alpha-side connected-graph t-row conclusion used in these proofs is exactly
   Lemma ZT. Once Lemma ZW(ii)-(iii) has been applied in the T* = W branch, the ordinary {1,2,4} prerequisites hold.
4. Additional direct Sun use: Sun(4) rules out four W-three pieces inside U_t in Lemma ZT. The equality kills use
   Sun(2) and Sun(3). The spanning-tree argument uses integral subgroup indices and G0, not computation.

All candidate exclusions remain CONDITIONAL; neither this lemma nor the reinstatement in erratum-v2 is accepted.
