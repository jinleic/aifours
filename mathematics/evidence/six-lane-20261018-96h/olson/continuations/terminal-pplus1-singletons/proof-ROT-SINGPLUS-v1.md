# Theorem ROT-SING+: terminal k = p+1, kappa^ = p-1 (all-singleton terminal blocks) forces one nonzero rotation pair, v1

Owner OlsonAssemblyLS. Written after /bin/date 2026-10-19T11:12:55-0700. Status: CANDIDATE_UNVERIFIED written proof (word level).
Scope frozen BEFORE derivation: TERMINAL-PPLUS1-SINGLETONS-scope-v1.md, sha256
8c4239c6fd6a9159ba17bf4db379bd5e1499a269cda2babad1ea2249b5d10f9d (10:59:40). Inputs: the accepted normal form, GRX (all-plus,
two-change and four-change sign patterns), Lemma CT and Lemma RS(b), all at accepted scopes; RS(b) rests on the classical
Cauchy-Davenport theorem. No (S1), Lev, index-one theorem, ONE-SHORT-LS, ROT-SING, ROT-LS, ROT-KP/KP+, ROT-FB or REFL is used.
No computation, model call, novelty, priority, Lean or human-review claim. The multiset classification of Sec. 3 is a NEW lemma
proved here at length 3p-3; nothing is inherited from the k = p case.

## 0. Statement

THEOREM ROT-SING+. Let p >= 7 be prime and w an avoider of length 4p-2 over D_(2p) (no 2p letters in increasing original index
order with identity product). Suppose SOME admissible normal form w^ of w has terminal k = p+1 and kappa^ = p-1. Then every rotation
letter of w lies in one set {rho_c, rho_-c} with c != 0. More precisely, the rotation multiset of w is rho_c^(2p-2) rho_(-c)^(p-1).

No hypothesis on o_F(w); nothing is asserted about reflection runs or about any other (k, kappa^). No step uses p >= 7 beyond
p >= 5; p = 5 is not claimed.

## 1. Conventions and accepted inputs

Group law (v,e)(v',e') = (v+ev', ee'); rho_x = (x,+1), sigma_y = (y,-1). Rotation values lie in Z_p; Y(x) := (1,x) in
C_2 x C_p = C_(2p). Multisets are occurrence multisets; v_x counts letters of value x.
(NF) proof-ROT-few-E-v4.md lines 28-43 (accepted chain: fewodd addendum line 12; ZX overlays 1-3; lowodd item 2, M1, M4).
     w^ is an avoider of length 4p-2 with the same F and rotation multiset as w, written cyclically R_1 S_1 ... R_k S_k with k odd
     blocks S_i = sigma_(y_i)^(l_i) (S_i between R_i and R_(i+1); indices mod k), and EVERY EMPTY RUN SEPARATES BLOCKS OF DIFFERENT
     VALUES (line 38). H^ = (F-k)/2, kappa^ = p-1-H^, R = 2p+2kappa^-k.
(GRX) notes-GRX-v1.md lines 7-20 (lowodd verdict item 1): for every cyclic constant-block representation (empty runs allowed) and
     every z in {+1,-1}^k, with f_i := [z_i != z_(i+1)], Phi := sum f_i, delta := #{i : l_i != f_i (mod 2)}, C_max := F - delta,
     T(z) := sum over z_i = +1 of theta_i, theta_i := y_(i-1) - y_i: w^ has an identity 2p-subword iff for some z there is an even C
     with Phi <= C <= C_max, 0 <= 2p-C <= R, and 2p-C rotation letters whose signed value sum (a letter of run i counted z_i times
     its value) is T(z) (mod p).
(CT) proof-LSplus-e2-v1.md lines 13-19 (STAB-delta item 6): p >= 5 prime, 0 <= kappa <= p-1, odd (ZP_kappa) Y, 1 <= n <= |Y|,
     |Y|-n even in [2kappa+2, 2p]  =>  sum_x min(n, v_x(Y)) <= p+n-2.
(RS(b)) proof-ROW-v1.md lines 16-19 with erratum-2-prereq-consolidated.md R5 (CFXT verdict item 4): for a sequence S of NONZERO
     elements of Z_p (p prime) and an integer K >= 0, the set Sigma_(<=K)(S) of sums of at most K terms (empty sum 0 included)
     has at least min(p, 1 + sum_x min(K, v_x(S))) elements.

## 2. The singleton shape and the selection rule

k = p+1 and kappa^ = p-1 give H^ = sum (l_i - 1)/2 = 0: every terminal block is one reflection S_i = sigma_(y_i), F = p+1 and
R = 4p-2-(p+1) = 3p-3. Let X be the rotation multiset of w^ (= that of w), T_i := y_i - y_(i-1).
For a pattern z with Phi = 2m: every l_i = 1, so delta = #{i : f_i = 0} = p+1-2m and C_max = F - delta = 2m = Phi. Hence GRX selects
exactly the 2m sign-change reflections and 2p-2m rotation letters, with signed sum T(z) (mod p) (2p-2m <= R as 2m <= p+1).

## 3. Lemma CL (new: the rotation multiset at length 3p-3)

Step 1 (all-plus). For z = all +1: Phi = 0, delta = p+1, C_max = 0, so C = 0, 2p rotations (2p <= 3p-3), T = 0. As w^ avoids, no
2p letters of X have value sum 0 (mod p); i.e. the sequence of the Y(x) satisfies (ZP_(p-1)).
Step 2 (CT). CT with kappa = p-1, n = p-3: 1 <= n <= |X| = 3p-3 and |X| - n = 2p is even and in [2kappa+2, 2p] = {2p}. Hence
sum_x min(p-3, v_x) <= 2p-5, and the excess sum_x (v_x - min(p-3, v_x)) >= (3p-3) - (2p-5) = p+2 lies on HEAVY values
(v_x >= p-2), each of which contributes p-3 to the truncated sum; there are at most two (3(p-3) > 2p-5).
- One heavy value a: v_a >= (p-3) + (p+2) = 2p-1, and v_a <= 2p-1 by Step 1 (2p equal letters sum to 0). So v_a = 2p-1.
- Two heavy values a, b: 2(p-3) + sum_(others) v_x <= 2p-5, so at most ONE other letter c; v_a + v_b = 3p-3-eps, eps in {0,1}.
  A choice a^i b^j with i + j = 2p sums to j(b - a) (mod p), zero iff p | j; j = 0 or 2p needs 2p equal letters (impossible:
  v_a, v_b <= 2p-1), and j = p needs v_a, v_b >= p. So min(v_a, v_b) <= p-1; label v_a >= v_b. The possibilities are
  (v_a, v_b, eps) = (2p-1, p-2, 0), (2p-2, p-1, 0), (2p-2, p-2, 1), (2p-3, p-1, 1).
- If eps = 1, a choice a^i b^j c with i + j = 2p-1 sums to j(b - a) - (a - c) (mod p); let j* in [0, p-1] with
  j*(b - a) = a - c (mod p). j* = 0 iff c = a, and j* = p-1 iff c = b; both are excluded, so 1 <= j* <= p-1, and a^(2p-1-j*) b^(j*) c
  is a zero-sum of 2p letters as soon as j* <= v_b and 2p-1-j* <= v_a. For (2p-2, p-2, 1) this holds for every j* in [1, p-2]
  and j* = p-1 is excluded: so this type is IMPOSSIBLE. For (2p-3, p-1, 1) it holds for j* in [2, p-1]: so j* = 1, i.e. c = 2a - b.
Conclusion (Lemma CL). X is of exactly one of the types
  (H1)  v_a = 2p-1, the other p-2 letters forming B (no letter of B equals a);
  (H2a) X = a^(2p-2) b^(p-1), b != a;
  (H2c) X = a^(2p-3) b^(p-1) c with c = 2a - b, b != a (so a, b, c are distinct).
(The type (2p-1, p-2, 0) is contained in (H1).)

## 4. Lemma OM (pattern omission) and its full-coverage corollary

Let a in Z_p, z a pattern with Phi = 2m, m >= 1, Pi_+ / Pi_- the runs with z = +1 / -1, alpha_+ the number of letters of value a in
Pi_+, and K := p-3+2m. Assume alpha_+ >= K. Call FREE every rotation letter except the a-letters of Pi_+; give a free letter u in run
r the weight omega(u) := z_r u - a; let N_z be the multiset of weights and D := sum over all rotation letters of z_r u.
LEMMA OM. If D - aK - T(z) lies in Sigma_(<=K)(N_z), then w^ has an identity 2p-subword.
Proof. Take free letters C with |C| <= K and sum_(u in C) omega(u) = D - aK - T(z), and K - |C| <= K <= alpha_+ further a-letters of
Pi_+ (these are not free, so disjoint from C). Omit these K letters and select the other 3p-3-K = 2p-2m rotation letters together
with the 2m sign-change reflections. The selected signed sum is
  D - sum_C z u - a(K - |C|) = D - aK - sum_C omega(u) = T(z),
so GRX (Sec. 2) gives an identity 2p-subword. []
COROLLARY OM'. Under the same assumptions, if at least p-1 weights in N_z are nonzero, w^ has an identity 2p-subword.
Proof. Let N' be the nonzero weights. K >= p-1 (m >= 1); if some value occurs more than K times in N', then
sum_x min(K, v_x(N')) >= K >= p-1; otherwise it equals |N'| >= p-1. RS(b) gives |Sigma_(<=K)(N')| >= p, so
Sigma_(<=K)(N_z) contains Sigma_(<=K)(N') = Z_p and Lemma OM applies. []

## 5. Lemma ER (empty runs, type H1)

Assume type H1 and put B~ := (u - a)_(u in B), a sequence of p-2 NONZERO residues. By RS(b) with K = p-2, |Sigma(B~)| >= p-1, where
Sigma(B~) = Sigma_(<=p-2)(B~) is the set of all subsums (0 included). Sigma(B~) is invariant under s -> sigma(B~) - s, and
sigma(B~) = sigma(B) - (p-2)a = sigma(B) + 2a (mod p).
(i) Let R_i be an empty run and z = -1 on R_i only. Then Phi = 2 (changes at S_(i-1), S_i), T(z) = -theta_i = T_i, alpha_+ = 2p-1 >= K =
    p-1, the free letters are B (all in Pi_+) with N_z = B~, and D - aK - T(z) = (2p-1)a + sigma(B) - (p-1)a - T_i = sigma(B) - T_i.
    By Lemma OM, an avoider has sigma(B) - T_i not in Sigma(B~), i.e. T_i + 2a not in Sigma(B~). So Sigma(B~) != Z_p; write
    Sigma(B~) = Z_p \ {r0}; r0 != 0 (0 is the empty subsum), and T_i = r0 - 2a for EVERY empty run R_i.
(ii) Two adjacent empty runs R_i, R_(i+1): with z = -1 on both, Phi = 2 (changes at S_(i-1), S_(i+1)), T(z) = T_i + T_(i+1), N_z = B~ and,
    as in (i), T_i + T_(i+1) + 2a is not in Sigma(B~), so T_i + T_(i+1) = r0 - 2a = T_i, whence T_(i+1) = 0, i.e. y_i = y_(i+1); but the
    empty run R_(i+1) separates blocks of different values (NF). Contradiction.
(iii) Two non-adjacent empty runs R_i, R_k (k not in {i-1, i, i+1} mod p+1): with z = -1 on R_i and R_k, Phi = 4 (four distinct blocks
    S_(i-1), S_i, S_(k-1), S_k), T(z) = T_i + T_k, K = p+1 <= 2p-1 = alpha_+, N_z = B~, and D - aK - T(z) = sigma(B) - 2a - T(z). An
    avoider needs sigma(B) - 2a - T(z) not in Sigma(B~), i.e. T(z) + 4a = 2r0 not in Sigma(B~); so 2r0 = r0 and r0 = 0. Contradiction.
Hence an avoider of type H1 has at most ONE empty run.

## 6. Proof of the theorem

Type H1, a = 0. By pigeonhole two of the p+1 blocks have equal values y_j = y_(j'), j != j'. For z = -1 on the runs j+1, ..., j',
Phi = 2, T(z) = y_(j') - y_j = 0, and 2p-2 letters of value 0 (v_0 = 2p-1) have signed sum 0: an identity 2p-subword. Impossible.
Type H1, a != 0.
- For a run R_i with 1 <= alpha_i <= p, take z = -1 on R_i: alpha_+ = 2p-1-alpha_i >= p-1 = K. The free letters are B and the alpha_i
  a-letters of R_i; their weights u - a (u in B outside R_i), -u - a (u in B inside R_i) and -2a are nonzero except -u - a for the
  letters u = -a in R_i. Corollary OM' gives a contradiction unless (p-2) + alpha_i - v_(-a)(R_i) <= p-2, i.e. v_(-a)(R_i) >= alpha_i.
- If every run had alpha_i <= p, then 2p-1 = sum alpha_i <= sum v_(-a)(R_i) <= |B| = p-2: impossible. So exactly one run, say R_1, has
  alpha_1 >= p+1 (two such runs would need 2p+2 letters a), and every other run has alpha_i <= p-2.
- Hence every nonempty run other than R_1 contains a letter of B (a run with a-letters contains >= alpha_i >= 1 letters -a, which lie
  in B since -a != a). So at most 1 + (p-2) = p-1 of the p+1 runs are nonempty: at least two runs are empty, against Lemma ER.
Type H2a (X = a^(2p-2) b^(p-1)). Suppose b != -a. Take any two blocks j != j' and orient the arc pattern so that Pi_+ holds at least
p-1 letters a (possible as the two sides hold 2p-2 in total); alpha_+ >= p-1 = K (m = 1). The free letters include all p-1 letters b,
with weights b - a or -b - a, both nonzero (b != a, b != -a). Corollary OM' gives a contradiction. Hence b = -a, and b != a gives
a != 0: X = a^(2p-2) (-a)^(p-1).
Type H2c (X = a^(2p-3) b^(p-1) c, c = 2a - b). For m = 1, K = p-1. Weights: b-letters b - a or -b - a; the letter c: c - a or -c - a;
a-letters in Pi_-: -2a. A weight -u - a vanishes iff u = -a; the others vanish only for a = 0 (the -2a weights).
- If -a is neither b nor c (this includes a = 0, since then b, c = -b are nonzero): any arc, oriented so that alpha_+ >= p-1 (the sides
  hold 2p-3 letters a), has at least p nonzero weights (the b-letters and c). Corollary OM': contradiction.
- If b = -a (so a != 0 and c = 3a): the p-1 letters b lie in at most p-1 of the p+1 runs, so at least two runs contain no b; they
  cannot both hold >= p-1 letters a (2p-2 > 2p-3), so some run R contains no b and alpha(R) <= p-2. With z = -1 on R:
  alpha_+ >= p-1 = K and every b- and c-weight is nonzero (no b in Pi_-; -c - a = -4a, c - a = 2a are nonzero): at least p nonzero
  weights. Contradiction.
- If c = -a (so a != 0, b = 3a != -a): at most one weight (that of c in Pi_-) vanishes, and the p-1 b-weights are nonzero. Any arc
  oriented with alpha_+ >= p-1 gives a contradiction.
So type H2c is impossible. Type (2p-2, p-2, 1) was excluded in Lemma CL.
Conclusion: only type H2a with b = -a remains: X = rho_c^(2p-2) rho_(-c)^(p-1) with c := a != 0. Every rotation letter of w^, hence
of w, is rho_c or rho_(-c). []

## 7. Remarks, preserved branch, scope

- Preserved failed branch (exact). The k = p argument (one arc, omit p letters, all b-letters free) gives only p-1 free nonzero
  weights here because an arc omits p-1 letters; when all 2p-1 letters a lie on the filler side (type H1, every arc), the free letters
  are the p-2 letters of B and Sigma misses one residue. This is the predicted "fails by one" step; Lemma ER (empty runs, including the
  FOUR-change pattern) and the run count in Sec. 6 replace it.
- Lemma CL is new at length 3p-3 and differs from the k = p classification (three types; the value classes and multiplicities are
  different). Type H1 is shown impossible altogether, so the only surviving multiset is rho_c^(2p-2) rho_(-c)^(p-1); no existence of
  such avoiders is claimed.
- Relation to accepted/pending results (context, not premises): ROT-LS (now accepted for k <= p-1) and the pending ROT-SING (k = p)
  are not used; Lemma OM is the same omission idea as in ROT-SING, re-derived here with K = p-3+2m.
- Not claimed: reflection rigidity, INV*, any statement for other (k, kappa^) or for o_F, ordered Olson, p = 5, novelty, priority,
  Lean or human review.
- Inputs (whole-file sha256): proof-ROT-few-E-v4.md ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f; notes-GRX-v1.md
  afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30; proof-LSplus-e2-v1.md
  2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1; proof-ROW-v1.md
  a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md
  fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 (R5); verdicts olson-rotation-lowodd-parent-verdict-v2.md
  0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 (items 1-2, M1, M4), olson-zx-s1c-parent-verdict-v1.md
  2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af (overlays 1-3), olson-fewodd-parent-verdict-v1-addendum-1.md
  279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a (line 12), olson-STAB-delta-parent-verdict-v1.md
  ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 (CT, item 6), olson-CFXT-ROW-LSII-parent-verdict-v1.md
  ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0 (RS, item 4). No cited input rests on a computer-assisted step.
