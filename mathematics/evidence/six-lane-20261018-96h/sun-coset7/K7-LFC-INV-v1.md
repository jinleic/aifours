# LFC and INV: a left-fibre count, the inversion duality q = alpha*, and two subclass exclusions (K7 with M empty; K6.3 fully unmarked)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-18T23:19:58-0700.
- **Lane:** math-1 sun-coset7, 96-hour continuation (`mathematics/evidence/six-lane-20261018-96h/sun-coset7`).
- **Status:** CANDIDATE written mathematics, unreviewed, no computation run for it. "[NEW]" means written in this lane;
  it is not a novelty claim. **No class is removed by this file as an accepted result; K7, K6.2*, K6.3 stay OPEN**
  (Theorems K7-M0 and K63-U0 exclude only the stated SUBclasses, pending parent check and hostile review).
- **Notation** follows `rules-k7-v1.md` (77b9afec...) section 0 with the accepted overlay: n_i = [G:U_i], g_ij = gcd(n_i,n_j),
  I_ij = [G : U_i cap U_j], alpha_ij = I_ij / lcm(n_i,n_j); mu(X) = |X|/|G|; the 5-valuation is h_i (overlay A-1);
  the VFC integer of (V1) is q. In class K7 write n_i = 6 r_i (r_i pairwise coprime), r_i = m_i w_i with m_i the
  {2,3,5}-part ("marker product") and gcd(w_i, 30) = 1; vertex i is UNMARKED iff m_i = 1, i.e. n_i = 6 w_i.
- **Imports, at exactly these scopes:** R0 (finite quotient; README section 1); L0.1, L0.2, L0.6; Zhu Sun(3), Sun(4);
  accepted local Sun(5) (verdict 2cf02436...5301) and Sun(6) (verdict efe1d849...1e29), always applied inside the
  subgroup U_v to at most six pieces; VFC (V1) of rules-k7-v1 section 2 (accepted in the written verdict 73a25ba6...).
  **Not used:** T, Ppair, K, RPLP, TWIN, Q-trichotomy, BLOCK/PAIR, any least-order frame, Sun(7), FH, Prop 4.5,
  M-S Lemma 4.6, Menon, any computation or producer/checker output.

## 1. Lemma LFC (left-fibre count) [NEW]

Let G be finite, let g_1U_1, ..., g_kU_k (k <= 7) be pairwise disjoint left cosets, and fix a vertex v.
For j != v put

  lambda_j := [U_v : U_v cap U_j],   t_j := [U_j : U_j cap U_v].

**(a)** lambda_j = I_vj / n_v = n_j alpha_vj / g_vj and t_j = I_vj / n_j = n_v alpha_vj / g_vj.

**(b)** g_jU_j meets exactly t_j left cosets of U_v, and none of them is g_vU_v.

**(c)** For a left coset C = xU_v != g_vU_v let S_C := { j != v : g_jU_j cap C != empty }. Then S_C is
*lambda-allowed*: every T subset S_C with |T| >= 2 contains j != j' with gcd(lambda_j, lambda_j') >= |T|.

**(d) (count)** For every y >= 0 on V \ {v} with sum_{j in T} y_j <= 1 for every lambda-allowed T,

  sum_{j != v} y_j alpha_vj / g_vj  <=  1 - 1/n_v  <  1.

*Proof.* (a) |U_v cap U_j| = |G|/I_vj gives both indices; I_vj = lcm(n_v,n_j) alpha_vj.
(b) The left U_v-cosets meeting g_jU_j are g_j u U_v (u in U_j), and g_j u U_v = g_j u' U_v iff u^-1 u' in U_j cap U_v;
so there are [U_j : U_j cap U_v] of them. If g_j u U_v = g_vU_v then g_j u in g_jU_j cap g_vU_v = empty, impossible.
(c) Let j in S_C and pick y_j in g_jU_j cap C. Then g_jU_j = y_jU_j and C = y_jU_v, so g_jU_j cap C = y_j(U_j cap U_v).
Fix x in C. Then x^-1 y_j in U_v, and x^-1 (g_jU_j cap C) = (x^-1 y_j)(U_j cap U_v) is a left coset, inside the finite
group U_v, of the subgroup U_j cap U_v, whose index in U_v is lambda_j. For distinct j these cosets are pairwise
disjoint (the g_jU_j are). By (b), v is not in S_C, so |S_C| <= k - 1 <= 6. Apply Sun(|T|) (imports, |T| <= 6) inside
U_v to the sub-family indexed by T.
(d) Summing the constraint over the n_v - 1 cosets C != g_vU_v and using (b):
sum_j y_j t_j = sum_C sum_{j in S_C} y_j <= n_v - 1. Divide by n_v and use t_j / n_v = alpha_vj / g_vj. QED

*Remarks.* (1) LFC is rules-k7-v1 L5 with the single choice H = U_v; the fibre g_vU_v is exclusive, so at most six
pieces share a fibre and only Sun(t), t <= 6, is used (no least-order frame). (2) The packing rule K (L2/L3) is the
special case in which every S_C is a singleton. (3) By Lemma INV below, the accepted VFC-count is exactly LFC applied to
the inverted configuration, so LFC is the "row" companion of VFC with alpha in place of q.

## 2. Lemma INV (inversion duality) [NEW]

Let (G; U_i; g_i) be finite with pairwise disjoint g_iU_i. Put U_i* := g_i U_i g_i^-1 and g_i* := g_i^-1.

**(a)** g_i* U_i* = (g_iU_i)^-1. Hence the g_i*U_i* are pairwise disjoint left cosets and [G : U_i*] = n_i:
the *inverted configuration* has the same indices, the same profiles and the same gcd matrix, so it lies in the same
class (K7, K6.2*, K6.3, K5.2*, K5.3, KII) with the same marking. Inverting twice returns (U_i; g_i).

**(b)** Let alpha* be the alpha-matrix of the inverted configuration. For every v != j, the VFC integer q_j of (V1)
at v (after the normalisation g_v = 1) equals alpha*_vj. In particular q is symmetric (q at v towards j equals q at j
towards v), and (V1) becomes

  alpha_vj + alpha*_vj <= g_vj.

*Proof.* (a) (g_iU_i)^-1 = U_i g_i^-1 = g_i^-1 (g_i U_i g_i^-1); inversion is a bijection of G; conjugate subgroups have
equal index. (b) alpha*_vj = [G : g_vU_vg_v^-1 cap g_jU_jg_j^-1] / lcm(n_v,n_j) = [G : U_v cap hU_jh^-1] / lcm(n_v,n_j)
with h = g_v^-1 g_j (conjugate by g_v^-1). After left multiplication by g_v^-1 (which (V1) uses) j's representative is h,
and D_j = U_v h U_j has |D_j| = |U_v||U_j| / |U_v cap hU_jh^-1| = |G| [G : U_v cap hU_jh^-1] / (n_v n_j), so
mu(D_j) = alpha*_vj / g_vj, which is q_j / g_vj by the definition of q_j in (V1). (V1) states D_j cap U_vU_j = empty
with mu(U_vU_j) = alpha_vj / g_vj (L0.3), whence the inequality. QED

*Consequence used below.* Every statement proved for all configurations of a class applies verbatim to the inverted
configuration, i.e. to the matrix alpha* (= the VFC q-matrix). Old VFC kills quantify over every admissible q; INV
shows q is itself the alpha-pattern of an actual configuration of the same class and must pass every rule.

## 3. Lemma ROW-U (LFC on an all-unmarked neighbourhood in K7) [NEW]

Let the configuration be in class K7 and let v be a vertex (marked or not) all six of whose neighbours are unmarked.
Then:
- (i) alpha_vj in {1, 2, 4} for every j;
- (ii) alpha_vj = 1 for at most one j;
- (iii) alpha_vj = 4 for at least three j.

*Proof.* For an unmarked neighbour j, lambda_j = n_j alpha_vj / 6 = w_j alpha_vj (Lemma LFC (a), g = 6). Since the w's
are pairwise coprime, coprime to 30 and hence to every alpha <= 5, gcd(lambda_j, lambda_j') = gcd(alpha_vj, alpha_vj').
Split the neighbours into R1 = {alpha = 1}, R24 = {alpha in {2,4}}, R3 = {alpha = 3}, R5 = {alpha = 5}, with sizes
k1, a + b (a twos, b fours), k3, k5. Cross-class gcds are 1, so every allowed set of size >= 2 lies inside one class,
and R1 elements lie only in singletons. Inside R3 allowed sets have size <= 3 (four pieces of pairwise gcd 3: Sun(4));
inside R5 size <= 5 (Sun(6)); inside R24 allowed sets are the singletons, all pairs, and the sets of size 3 or 4
containing at most one two (a triple with two twos has all gcds 2: Sun(3); five pieces have gcds <= 4: Sun(5)).
By LFC (d) every feasible y satisfies sum_j y_j alpha_vj <= 6 - 6/n_v < 6. We exhibit, for every row violating
(i), (ii) or (iii), a feasible y with sum_j y_j alpha_vj >= 6. Feasibility is checked class by class, since allowed sets
do not cross classes. Standard partial weights:
- on R1: y = 1 (value k1);
- on R3 (k3 >= 1): y = 1/min(3, k3) (value 3 if k3 <= 3, else k3);
- on R5 (k5 >= 1): y = 1/min(5, k5) (value 5 if k5 <= 5, else 6);
- on R24 with b <= 2: y = 1/2 on twos, 1/4 on fours. Feasible: pairs sum <= 1; the only allowed sets of size >= 3 are
  {two, four, four} (sum 1); no allowed 4-set exists when b <= 2. Value a + b;
- on R24 with b = 3: y = 0 on twos, 1/3 on fours (allowed sets hold at most three fours). Value 4;
- on R24 with b >= 4: y = 1/4 on every element (allowed sets have size <= 4). Value a/2 + b >= 4.
Every nonempty class therefore has value >= 1, and >= 3 for R3, >= 5 for R5, >= 4 for R24 when b >= 3.
- (i) If k5 >= 1: value >= 5 + 1 when some other class is nonempty, and 6 when k5 = 6. If k5 = 0 and k3 >= 1:
  k3 >= 6 gives 6; k3 in {4,5} gives k3 + (6 - k3) >= 6 because the 6 - k3 remaining elements contribute at least
  one each (R1 elements 1 each; R24 with b <= 2 contributes a + b, with b >= 3 at least 4); k3 <= 3 gives
  3 + (value of the >= 3 remaining elements) >= 3 + 3.
- (ii), (iii) with entries in {1,2,4}: if b <= 2 the value is k1 + a + b = 6; if b >= 3 and k1 >= 2 the value is
  >= k1 + 4 >= 6.
In every case sum y alpha >= 6, contradicting LFC. QED

## 4. Theorem K7-M0: no class-K7 configuration has an empty marked set [NEW]

*Statement.* There is no finite group G with seven pairwise disjoint left cosets g_iU_i whose indices are
n_i = 6 w_i with w_i pairwise coprime and coprime to 30. (By R0 the same holds for arbitrary G with finite-index U_i.)

*Proof.* Every vertex has six unmarked neighbours, so Lemma ROW-U (iii) gives |A4(v)| >= 3 for every v, where
A4(v) := { j : alpha_vj = 4 }. By INV (a) the inverted configuration is again a K7 configuration with every vertex
unmarked, so ROW-U applies to alpha* as well: |A4*(v)| >= 3 with A4*(v) := { j : alpha*_vj = 4 }. By INV (b),
alpha_vj + alpha*_vj <= 6, so A4(v) and A4*(v) are disjoint subsets of the six neighbours of v. Hence |A4(v)| = 3 for
every v, and the graph on the seven vertices with edge set { ij : alpha_ij = 4 } (alpha is symmetric) is 3-regular.
Its degree sum 7 * 3 = 21 is odd, which is impossible. QED

*Relation to the accepted frontier.* This removes, at configuration level and by a route independent of T/Ppair/Q/BLOCK,
the whole M = empty part of K7: the open seven-singleton all-2 pattern (killed already by ROW-U (iii) at any vertex) and
all of Q24 with M = empty. It also reproves the accepted M = empty sub-results (Q5, Q23U). Marked K7 (|M| = 1, 2, 3)
is NOT covered: with a marked neighbour, gcd(lambda_z, lambda_j) can exceed gcd(alpha_vz, alpha_vj) and ROW-U does not
apply as stated.

## 5. Theorem K63-U0: no fully unmarked K6.3 configuration [NEW]

*Statement.* There is no finite group with seven pairwise disjoint left cosets whose indices are n_i = 6 w_i
(i in C, |C| = 6) and n_d = 3 w_d, with all w's pairwise coprime and coprime to 30. (These are exactly the K6.3
configurations with no vertex of e >= 2, f >= 2 or h >= 1.)

*Proof.* Step 1 (alpha_vd = 2 for every v in C). Fix v in C and suppose alpha_vd = 1 (g_vd = 3, so alpha_vd in {1,2}).
Then lambda_d = n_d alpha_vd / 3 = w_d is coprime to every lambda_j = w_j alpha_vj (j in C \ {v}), so d lies only in
singleton allowed sets; put y_d = 1, contributing alpha_vd / g_vd = 1/3. For the five C-neighbours use the partial
weights of ROW-U's proof (the class analysis there needs only that these neighbours are unmarked with g = 6). Their
value is >= 4: if k5 >= 1 it is >= 5; if k3 >= 1 it is >= 3 + 1 (k3 <= 3, some other element exists since 5 > 3) or
>= k3 >= 4; with entries in {1,2,4} it is k1 + a + b = 5 if b <= 2 and >= 4 if b >= 3. So sum_j y_j alpha_vj / g_vj
>= 4/6 + 1/3 = 1, contradicting LFC (d) at v.
Step 2. Hence alpha_di = 2 for all six i in C. At v = d, lambda_i = n_i * 2 / 3 = 4 w_i, all pairwise gcds equal 4, so
allowed sets have size <= 4 (five such pieces: Sun(5)). With y = 1/4 on every i, sum_i y_i alpha_di / 3 =
6 * (1/4) * (2/3) = 1, contradicting LFC (d) at d. QED

*Relation to the frontier.* This subsumes the accepted partial D3 only on its unmarked part; K6.3 with any marker
(an index of C with e >= 2, any vertex with f >= 2, or the 5-vertex) is NOT covered.

## 6. Exact remaining gap after this file (if the candidates are accepted)

- K7 with 1 <= |M| <= 3 (some vertex carries marker 2, 3 or 5): OPEN.
- K6.3 with at least one marker: OPEN.
- K6.2* (inherently marked: e_d >= 2 and e_i* >= 2): OPEN.
- K5.3: parent disposition pending (StageA v2 qualification run by the parent); not affected by this file.
No Sun(7) theorem, counterexample, enumeration, or novelty claim.

## 7. Verification boundary and requested checks

Written, single-author, unreviewed. Requested: independent parent re-derivation of LFC (c)-(d) and INV (b) (the two new
bridges), of the ROW-U class analysis, and of the parity step; hostile Codex and Claude reviews of this exact file.
Suggested mutation controls for reviewers: (1) drop "v not in S_C" (then |S_C| = 7 would need Sun(7)); (2) replace
alpha* by an unconstrained q (the old all-q quantifier, under which the all-2 M = empty pattern survived VFC at a vertex);
(3) replace the parity step by |A4(v)| >= 3 alone (no contradiction: e.g. rows with three or more fours exist).
