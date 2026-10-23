# FROZEN r2 — candidate proof: the random 7-regular graph has chromatic number 4 a.a.s.

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the
file (README §1, evidence/LOG.md, evidence/SHA256SUMS.txt). r2 supersedes r1 (`review/PROOF_CHI7.r1.md`, SHA-256
8a79ba3c9858137fa698c5f962ac6fe4e1fba38f2b61ce919772893d74ea906c), which is kept unchanged. §9 lists every change.

**Status.** CANDIDATE PROOF, worker-written. r1 was reviewed by Codex (hostile review: ACCEPT-WITH-FIXES, one
minor) and by Claude (complete review: ACCEPT-WITH-FIXES, no fatal or major finding, seven minors). r2 applies all
of those fixes; r2 itself has not been reviewed. The entropy constant used in §2 is prior work (§8). No novelty or
priority claim.

## Theorem

Let G_{n,7} be the uniformly random 7-regular simple graph on n vertices, n even. Then
P(χ(G_{n,7}) = 4) → 1 as n → ∞.

**Context (cited, not used).**
- KPW Theorem 1 at d = 7 gives χ ∈ {4, 5} a.a.s. (k = 5 there). The Achlioptas–Moore 2004 table gives {4, 5, 6}.
  ACG Table 1 has d_{4,smm} = 6 and d_4 = 10. The non-rigorous 1RSB prediction (ACG (1.5)–(1.7)) gives
  χ(G(n, d)) = 4 for 6 ≤ d ≤ 9.
- Prior work on the constant (§8). Achlioptas–Naor's display (12) already contains the sharper constant used in
  §2. Nir–Pérez-Giménez (NPG, Theorem 1.2) use it to prove k-colourability for d < ℓ_k = 2(k−1)³ log(k−1)/(k(k−2))
  for random lifts of any fixed loopless d-regular multigraph; ℓ_4 = (27/4) log 3 = 7.4156… > 7. They exclude
  loops and do not cover the uniform model G_{n,d}.

**Proof outline.**
- Upper bound (§§2–4). Rerun KPW's balanced-colouring second moment and small subgraph conditioning at k = 4
  colours and d = 7. KPW's hypothesis d < 2(k−1) log(k−1) fails here (6 log 3 = 6.59… < 7). §3 shows it enters
  KPW §§2–4 only through two facts:
  - (H1) k² − 2k − d + 2 > 0 (here 3 > 0);
  - (H2) a global quadratic-decay bound for φ on the Birkhoff polytope, KPW (3.15).
  §2 proves (H2) at d = 7 with an explicit constant. The inequality needed is the k = 4 case of Achlioptas–Naor's
  display (12) (prior work, restated as NPG Theorem 3.1); Lemma 2.1 gives a self-contained elementary proof of
  its per-row form with an explicit quadratic constant.
- Lower bound (§5). Primary: the published Molloy–Reed first-moment criterion, as recorded by KPW and W99.
  Cross-check: a self-contained first moment for 3-colourings, rigorously maximised over all class sizes
  (computer-assisted).

## 0. Sources, conventions, notation

- **Line numbers** count LF-terminated lines of the `.layout.txt` files; a form feed is not a line break. The
  parent's check `institute/runs/six-lane-2026-10-16/review/chi7-claude-source-visibility-addendum.json` confirms
  r1's citations in this convention, and r2 keeps them. Page numbers are the printed ones.
- Sources pinned by the parent, read in place at `institute/runs/six-lane-2026-10-16/review/colour7-parent-source-screen-v1/`:
  - **KPW**: Kemkes, Pérez-Giménez, Wormald, *On the chromatic number of random d-regular graphs*,
    arXiv:0812.2937v1 (Adv. Math. 223 (2010) 300–328). PDF bf56a321c5da2f9c65f42fabce19a6aed0cf98ed09521e14a78ecc98ecb5657f;
    layout c75d6c7da3988ccc4d4e44c8e47456fcb3fba6dd7e4826f8af49ef4d48462afd.
  - **AN**: Achlioptas, Naor, *The two possible values of the chromatic number of a random graph*, Ann. of Math.
    162 (2005). PDF b5cc85ace1e70ac61c517f4c822018983db31a7efbb97f565d5124ec7a7deef7; layout b22f7ba1…0430.
- **ACG**: Ayre, Coja-Oghlan, Greenhill, arXiv:1812.09691v4, pinned at `…/colour7-parent-source-screen-v2/`.
  PDF d0e46a24…5989; Table 1 at layout l.131–135.
- Fetched into this lane (`sources/`):
  - **W99**: Wormald, *Models of random regular graphs*, Surveys in Combinatorics 1999. PDF
    987de47eef4c32241f67af96d98ebbb40d55fbbd85a7a37dbb63ce0c03c9cb70. Theorem 4.1 at l.1561–1596 (conclusion
    l.1584–1596); Theorem 2.6 at l.361–366; P(Simple) (3) at l.248; Molloy–Reed remark at l.1102–1107.
  - **AM04**: Achlioptas, Moore, cond-mat/0407278v1. PDF 80ac409d…6327.
  - **NPG**: Nir, Pérez-Giménez, *The chromatic number of random lifts of complete graphs*, arXiv:2109.13347v1
    (27 Sep 2021). PDF 09161e920e11cddced47dd81bdb5c693f8eeef9f95b510d63fbc00fec2395893; layout
    c4bd28017f1a924c9a468fd3c9bc7a4d04c3645655b5ad21dd4879dec09c5083 (fetched 2026-10-17 07:07:39 PDT).
- log means the natural logarithm, as in KPW and AN. KPW's example χ(G_{n,10}) = 5 (p.2 l.89) holds only with
  natural logarithms.
- k = number of colours; here k = 4, d = 7. **J_4** := KPW's 4×4 all-ones matrix, and **J := (1/4)J_4**, the 4×4
  matrix with all entries 1/4. KPW's φ((1/k)J_k) and AN's g_c(J_k) (AN l.260: "the constant 1/k matrix") are φ(J) and
  g_c(J) in this notation. M := the set of 4×4 doubly stochastic matrices. S_4 := the set of 4×4 row-stochastic
  matrices. Δ_4 := the probability simplex in R⁴, U := (1/4,1/4,1/4,1/4), and D(p‖U) := Σ_i p_i log(4p_i), with
  0 log 0 = 0.
- KPW (3.8) (p.13 l.737–746), at k = 4:
  φ_d(M) = −(1/4) Σ_{p,q} m_pq log m_pq + (d/2) log(1/2 + Σ_{p,q} m_pq²/16).
  This is AN's g_c (p.1340 l.275–286) with c = d/2: g_c(A) = H(A) + c E(A), where H(A) = −(1/4)Σ a log a and
  E(A) = log(1 − 2/k + Σa²/k²).
- ρ_A := Σ_{ij} a_ij². For A ∈ S_4 the entries sum to 4, so ρ_A − 1 = Σ_{ij}(a_ij − 1/4)², and ρ_A ≥ 1.

## 1. What is imported, with exact hypotheses

- **(I1) KPW Proposition 2(a)** (p.3 l.122–140). Hypotheses: "Fix integers d, k ≥ 3"; n is a multiple of k and
  dn is even. Y is the number of balanced k-colourings of P_{n,d}, and X_m is the number of m-cycles. Conclusion:
  - EY ∼ k^{k/2}((k−1)/(2π(k−2)))^{(k−1)/2} n^{−(k−1)/2} k^n (1−1/k)^{dn/2};
  - (1.1) E(Y[X_1]_{p_1}…[X_j]_{p_j}) ∼ Π_m (λ_m(1+δ_m))^{p_m} EY, with λ_m = (d−1)^m/(2m) and
    δ_m = (−1)^m/(k−1)^{m−1}.
  No condition on d beyond d ≥ 3 (§3, item A10).
- **(I2) KPW §3 machinery** (pp.10–25), all valid for every d, k ≥ 3 except where §3 says otherwise:
  - (3.1)–(3.9);
  - Lemma 5 (p.13) and its proof (pp.17–19);
  - Lemmas 6, 7, 9;
  - Lemma 8 (p.15) and its proof (pp.21–25);
  - Lemma 4 (p.7).
  In particular (3.9): |T(M)|/|P_{n,d}| ≤ poly(n) k^n e^{nφ(M)} for every M ∈ M ∩ (k/n)Z^{k×k}.
- **(I3) Small subgraph conditioning**, W99 Theorem 4.1 (l.1561–1596), stated exactly. Let λ_i > 0 and δ_i ≥ −1,
  i = 1, 2, …, be reals. For each n let X_i = X_i(n) (non-negative integer valued) and Y = Y(n) (non-negative, with
  EY > 0 for n sufficiently large) be random variables on one probability space G = G(n). Suppose:
  - (a) for each k ≥ 1, X_1, …, X_k are asymptotically independent Poisson random variables with EX_i → λ_i;
  - (b) E(Y[X_1]_{j_1}…[X_k]_{j_k})/EY → Π_{i=1}^{k} (λ_i(1+δ_i))^{j_i} for every finite sequence j_1, …, j_k of
    non-negative integers;
  - (c) Σ_i λ_iδ_i² < ∞;
  - (d) EY_n²/(EY_n)² ≤ exp(Σ_i λ_iδ_i²) + o(1) as n → ∞.
  Conclusion (l.1584–1596): "Then P(Y_n > 0) = exp(−Σ_{δ_i=−1} λ_i) + o(1), and, provided Σ_{δ_i=−1} λ_i < ∞,
  G^{(Y)} ≈ Ĝ, where Ĝ is the probability space obtained from G by conditioning on the event ∧_{δ_i=−1}(X_i = 0)."
  Only the first conclusion is used. (The index k in (a) and (b) is W99's, not the number of colours.)
- **(I4) Cycle counts in P_{n,d}**, W99 Theorem 2.6 (Bollobás; l.361–366). For fixed d, X_1, …, X_k are
  asymptotically independent Poisson with means (d−1)^i/(2i). Hence P(Simple) = P(X_1 = X_2 = 0) → e^{(1−d²)/4} > 0
  (W99 (3), l.248). G_{n,d} is P_{n,d} conditioned on Simple, because each simple graph arises from exactly (d!)^n
  pairings.
- **(I5) KPW Theorem 10** (p.25 l.1536–1541), quoted: "Fix nonnegative integers d ≥ 3, k and ℓ such that
  d < 2(k − 1) log(k − 1). Consider the d-regular graphs with n vertices (n divisible by k and dn even) and a
  distinguished ordered set of ℓ edges whose endpoints induce a perfect matching (i.e. no two edges in the
  distinguished set are adjacent to the same edge or incident with the same vertex). Let G be chosen uniformly at
  random from such structures. Then G a.a.s. has a k-colouring in which all ℓ distinguished edges have end
  vertices coloured 1 and 2." Also the n ≢ 0 (mod k) argument (p.27 l.1622–1643). Both as audited in §3.
- **(I6) Molloy–Reed criterion**, as recorded in the pinned sources:
  - KPW l.67–68: "For fixed d, Molloy and Reed [16] showed that if q(1 − 1/q)^{d/2} < 1 then χ(G_{n,d}) > q a.a.s."
  - KPW l.175–178: "if d > (2q − 1) log q then χ(G_{n,d}) > q … This is just a slightly weaker formulation of the
    result given by Molloy and Reed [16]. (Their proof is reported in [20], Theorem 1.3.)"
  - W99 l.1102–1107: Molloy and Reed's calculation shows that the nth root of the expected number of r-colourings
    "is at most r((r−1)/r)^{d/2} + o(1) (for fixed r and d). Hence, for instance, a.a.s. χ(G) ≥ 4 for G ∈ G_{n,d}
    when d ≥ 6."
- **Elementary facts.**
  - Stirling bounds: (m/e)^m ≤ m! for all integers m ≥ 0, and m! ≤ e·√(m+1)·(m/e)^m for all m ≥ 0.
  - Multinomial bound: n!/(n_1!n_2!n_3!) ≤ Π_i (n/n_i)^{n_i}.

## 2. The Achlioptas–Naor inequality at k = 4 with the sharper constant, and the replacement for KPW (3.15)

**Attribution.** The constant in this section is not new. AN's display (12) (l.756–765) gives
(k−1)³ log(k−1)/(k(k−2)) > c_{k−1}, so their proof of Theorem 7 works for every c up to that value (§2.4), and NPG
restate it as their Theorem 3.1 (l.524–535), for c < c_q. Lemma 2.1 is a self-contained elementary proof of the
k = 4 per-row form, with explicit equality cases; Theorem 2.2 adds the explicit quadratic constant.

### Lemma 2.1 (per-row inequality)
For every p ∈ Δ_4,
  D(p‖U) ≥ (3/2)·log 3·(Σ_i p_i² − 1/4),
with equality iff p = U or p is a permutation of (3/4, 1/12, 1/12, 1/12).

*Proof.* Let F(p) := D(p‖U) − (3/2) log 3 (Σp_i² − 1/4). F is continuous on the compact set Δ_4 and F(U) = 0.

(a) *No minimiser on the boundary.* Suppose p_j = 0 and p_i > 0. For 0 < ε ≤ p_i/2, move ε from i to j and call
the result p′. Then:
- F(p′) − F(p) = ε log(4ε) + [(p_i − ε) log(4(p_i − ε)) − p_i log(4p_i)] − (3/2) log 3 [ε² + (p_i − ε)² − p_i²].
- By the mean value theorem the middle bracket has absolute value at most ε(|log(2p_i)| + |log(4p_i)| + 1).
- The last term is O(ε).
- So F(p′) − F(p) ≤ ε(log(4ε) + K) < 0 for small ε.
Hence every minimiser lies in the relative interior.

(b) *Minimisers take at most two values.* At an interior minimiser, Lagrange multipliers give
ψ(p_j) := log(4p_j) + 1 − 3 log 3·p_j = λ for all j. Since ψ″(u) = −1/u² < 0, ψ is strictly concave and takes
each value at most twice. So up to permutation p = (a, …, a, b, …, b) with m copies of a, 1 ≤ m ≤ 3 (m = 0 is
the uniform case). This leaves two one-parameter families:
- m = 1 or 3: (x, y, y, y) with y = (1 − x)/3 and x ∈ [0, 1];
- m = 2: (x, x, y, y) with y = 1/2 − x and x ∈ [0, 1/2].

(c) *Family (x, y, y, y).* Put x = (1 + 3v)/4, so y = (1 − v)/4 and v ∈ [−1/3, 1]. Then:
- D = [(1+3v) log(1+3v) + 3(1−v) log(1−v)]/4;
- Σp² − 1/4 = (4x − 1)²/12 = 3v²/4;
- so 4F = G(v) := (1+3v) log(1+3v) + 3(1−v) log(1−v) − (9/2) log 3·v².

Derivatives:
- G′(v) = 3L(v), where L(v) := log((1+3v)/(1−v)) − 3v log 3;
- L′(v) = q(v) − 3 log 3, where q(v) := 3/(1+3v) + 1/(1−v) = 4/((1+3v)(1−v)).

q is strictly convex on (−1/3, 1), since q″ = 54/(1+3v)³ + 2/(1−v)³ > 0. Also q(0) = q(2/3) = 4 and q(1/3) = 3
(the minimum of q). Since 3 < 3 log 3 < 4, which is the exact fact 1 < log 3 < 4/3 (verified in §7, item A1), L′
has exactly two zeros, v_1 ∈ (0, 1/3) and v_2 ∈ (1/3, 2/3). L′ > 0 on (−1/3, v_1) ∪ (v_2, 1) and L′ < 0 on
(v_1, v_2).

Also L(0) = 0 and L(2/3) = log 9 − 2 log 3 = 0. It follows that:
- L < 0 on (−1/3, 0) and L > 0 on (0, v_1];
- L is strictly decreasing on [v_1, v_2] with L(v_1) > 0 > L(v_2), so it has a unique zero v* there. In fact
  v* = 1/3 exactly, since L(1/3) = log(2/(2/3)) − log 3 = 0;
- L < 0 on [v_2, 2/3) and L > 0 on (2/3, 1).

So G is strictly decreasing on [−1/3, 0], increasing on [0, 1/3], decreasing on [1/3, 2/3] and increasing on
[2/3, 1], using continuity at the endpoints. Since G(0) = 0 and G(2/3) = 3 log 3 − log 3 − 2 log 3 = 0, we get
G ≥ 0, with equality only at v ∈ {0, 2/3}, i.e. p = U or p = (3/4, 1/12, 1/12, 1/12).

(d) *Family (x, x, y, y).* Put u = 4x − 1 ∈ [−1, 1]. Then:
- D = [(1+u) log(1+u) + (1−u) log(1−u)]/2 and Σp² − 1/4 = u²/4;
- r(u) := D − u²/2 is even with r(0) = 0, and r′(u) = atanh(u) − u ≥ 0 on [0, 1);
- so D ≥ u²/2 ≥ (3/8) log 3·u², because (3/8) log 3 < 1/2 ⟺ log 3 < 4/3.
Hence F ≥ 0 on this family, with equality only at u = 0.

(e) By (a) and (b), min F is attained in one of the two families, so min F = 0. Any zero of F is a minimiser,
hence lies in a family, hence is one of the stated equality points. ∎

### Theorem 2.2 (k = 4 case of AN's display (12), with an explicit constant)
For every A ∈ S_4 and every real c ≥ 0,
  g_c(J) − g_c(A) ≥ ((3/8) log 3 − c/9)·Σ_{ij}(a_ij − 1/4)².
In particular g_c(J) ≥ g_c(A) for all A ∈ S_4 whenever c ≤ c* := (27/8) log 3 = (k−1)³ log(k−1)/(k(k−2)) at
k = 4. AN state their Theorem 7 only for c ≤ c_{k−1} = 3 log 3, but their display (12) already gives c*
(§2.4); NPG Theorem 3.1 states it for c < c_q.

*Proof.* For a row a_i ∈ Δ_4, Σ_j a_ij log a_ij = D(a_i‖U) − log 4, so H(A) = log 4 − (1/4)Σ_i D(a_i‖U) and
H(J) = log 4. Also E(A) − E(J) = log((1/2 + ρ_A/16)/(9/16)) = log(1 + (ρ_A − 1)/9) ≤ (ρ_A − 1)/9. Hence
  g_c(J) − g_c(A) = (1/4)Σ_i D(a_i‖U) − c(E(A) − E(J))
                  ≥ (1/4)(3/2) log 3·Σ_i(Σ_j a_ij² − 1/4) − c(ρ_A − 1)/9
                  = ((3/8) log 3 − c/9)(ρ_A − 1),
by Lemma 2.1 applied row by row. Finally ρ_A − 1 = Σ(a_ij − 1/4)². ∎

### Corollary 2.3 (replacement for KPW (3.15) at d = 7)
Let C_7 := (3/8) log 3 − 7/18. Then C_7 ∈ (0.023, 0.024) (§7, item A2), and for every M ∈ M,
  φ_7(M) ≤ φ_7(J) − C_7·Σ_{p,q}(m_pq − 1/4)²,   φ_7(J) = log 4 + 7 log(3/4).
In particular, for every M ∈ M ∖ B_4(δ) (some |m_pq − 1/4| ≥ δ):
  φ_7(M) ≤ log 4 + 7 log(3/4) − C_7 δ².   (3.15′)

*Proof.* φ_7 = g_{7/2}. Apply Theorem 2.2 with c = 7/2, using M ⊂ S_4. ∎

The general form is: for d < (27/4) log 3 = 7.4156… the constant C_d = (3/8) log 3 − d/18 is positive, and C_8 < 0
(§7, item A2).

### 2.4 Cross-check through AN's own proof (not needed for the Theorem)
- *Theorem 9 hypotheses for h(x) = −x log x* (AN p.1342 l.377–379). h is continuous on [0, 1] and strictly concave
  (h″ = −1/x < 0). Also h′(x) = −log x − 1, so h′(0+) = ∞ and h′(1−) = −1 > −∞. Further h‴ = 1/x² > 0,
  h⁽⁴⁾ = −2/x³ < 0 and h⁽⁶⁾ = −24/x⁵ < 0. AN state this check themselves at p.1347 l.692–694.
- *AN (9)–(12), pp.1347–1348.* (11) reduces to c ≤ ((k−1)²/k)·η(y) for y ∈ [0, 1 − 1/k], where
  η(y) = (f(1/k) − f(1/k + y))/y. AN show that min η is attained at one of three points (l.744–753). At k = 4 these
  are:
  - η(0) = k/2 = 2;
  - η((k−2)²/(k(k−1))) = η(1/3) = ((k−1)/(k−2)) log(k−1) = (3/2) log 3, attained at p = (3/4, 1/12, 1/12, 1/12);
  - η(1 − 1/k) = η(3/4) = (k/(k−1)) log k = (4/3) log 4, attained at p = (1, 0, 0, 0).
- The global minimum is (3/2) log 3 ≈ 1.6479. This uses (3/2) log 3 < 2 ⟺ log 3 < 4/3, and
  (3/2) log 3 < (4/3) log 4 ⟺ 3⁹ < 2¹⁶, i.e. 19683 < 65536 (§7, item A4).
- AN's own display (12), l.756–765, reads "((k−1)²/k)·min{k/2, ((k−1)/(k−2))·log(k−1), (k/(k−1))·log k} =
  ((k−1)³/(k(k−2)))·log(k−1) > c_{k−1}", "where (12) follows from elementary calculus". Their proof therefore
  yields Theorem 7 for every c ≤ (k−1)³ log(k−1)/(k(k−2)), which is (27/8) log 3 ≈ 3.7078 > 7/2 at k = 4. This
  matches Theorem 2.2. Lemma 2.1 is the k = 4 per-row form of the same fact: η_min = (3/2) log 3.

## 3. Audit: every use of "d < 2(k − 1) log(k − 1)" in KPW §§1–4

A full read of KPW §§1–4 (layout l.1–1645) found the hypothesis stated or invoked only at the places below.
Quotes have their typography normalised; in quotes, KPW's (1/k)J_k is our J (§0).

| # | Place (page; layout line) | Quote | Role | Status at (k, d) = (4, 7) |
|---|---|---|---|---|
| A1 | p.1 abstract; l.23–27 | "k is the smallest integer satisfying d < 2(k − 1) log(k − 1)" | defines k in the statement | not used: we prove the upper-bound mechanism for k = 4 directly |
| A2 | p.3 Thm 1; l.105–107 | "let k be the smallest integer such that d < 2(k − 1) log(k − 1)" | statement | as A1 |
| A3 | p.3 Prop 2(b); l.142 | "(b) If furthermore d < 2(k − 1) log(k − 1) then E(Y²) ∼ …" | hypothesis of the second-moment asymptotics | replaced by Prop 4.1 under (H1)+(H2) |
| A4 | p.4 proof of Thm 1; l.168–178 | "all the conditions of Theorem 4.1 in [21] are verified by Proposition 2, (1.2) and (1.3)"; "from our choice of k we have d ≥ 2(k − 2) log(k − 2)" | SSC conditions; minimality of k (lower bound only) | SSC conditions verified in §4.2; lower bound is §5 |
| A5 | p.10 §3; l.570 | "Throughout this section, fix positive integers d and k ≥ 3 satisfying d < 2(k − 1) log(k − 1)." | standing hypothesis of §3 | invoked only at A6 and A7 |
| A6 | p.17; l.982–983 | "Here we used the fact that k² − 2k − d + 2 > 0, which is guaranteed from our assumptions on d and k." | H positive definite in (3.13)–(3.14) (Gaussian integral via Lemma 4) | (H1): 16 − 8 − 7 + 2 = 3 > 0 |
| A7 | p.17; l.1004–1020 | "From Theorem 7 in [3] (see also (5) in the same paper) we have that if d < d_{k−1} := 2(k − 1) log(k − 1) for each M ∈ M, φ(M) ≤ φ((1/k)J_k) − ((d_{k−1} − d)/(4(k − 1)²))(Σ_{p,q} m_{p,q}² − 1) … In particular, for each M ∈ M ∖ B_k(δ), φ(M) ≤ log k + d log(1 − 1/k) − ((d_{k−1} − d)/(4(k − 1)²)) δ². (3.15)" | global decay; makes S_2 = o(S_1) | (H2): replaced by Corollary 2.3, constant C_7 > 0 |
| A8 | p.13 Lemma 5; l.713–723; proof pp.17–19, l.1035–1138 | "Let M = [m_pq] be a fixed matrix in M, and let (b_pqrs) be any tuple of non-negative reals satisfying (3.2) and (3.3)." | relaxation bound behind (3.7) and (3.9) | no d-hypothesis: the proof uses Lagrange multipliers on L̂ and continuity only |
| A9 | p.15 Lemma 8; l.894–909; proof pp.21–25, l.1253–1525 | "There exists ε > 0 such that for each M ∈ M ∩ (k/n)Z^{k×k} ∩ B_k(ε log n/n^{1/2}) …" | saddle point | no d-hypothesis: d enters only via ρ = √(dn)/(k(k−1)), c = d/(2k²(k−1)²) and "ε′ < d/(16k²(k−1)²)" (l.1356); Lemma 9 needs only k ≥ 3 |
| A10 | §2, pp.4–10; Prop 2(a) l.122, Lemma 3 l.231, Lemma 4 l.373 | "Fix integers d, k ≥ 3"; "k ≥ 3, d positive" | first moments, joint moments (1.1) | no d-hypothesis |
| A11 | p.4 (1.2)–(1.3); l.152–165 | "Σ_{m≥1} λ_mδ_m² = (k − 1)² log((k − 1)/√(k² − 2k − d + 2))" | SSC conditions (c), (d) | needs (d − 1)/(k − 1)² < 1 ⟺ (H1): 6/9 < 1 |
| A12 | p.25 Thm 10; l.1536 | "Fix nonnegative integers d ≥ 3, k and ℓ such that d < 2(k − 1) log(k − 1)." | n ≢ 0 (mod k) | uses only A3 (via (4.2)), A7 (p.26 l.1610: "we first recall from the last lines of the proof of Proposition 2(b) that we can restrict our attention to triples … with colour count M … where \|m_{p,q} − 1/k\| < ε log n/n^{1/2}") and A4/A11 (l.1558: "by the argument in the last few sentences of the proof of Theorem 1"); the b_pqrs concentration (l.1616–1621) refers to Lemma 8 (A9) |
| A13 | p.27; l.1622–1623, 1643 | "if d ≥ 3 and d < 2(k − 1) log(k − 1), then G_{n,d} is a.a.s. k-colourable for n not divisible by k"; "(Note that k ≥ 3 from our assumptions on d and k)" | final extension | uses Theorem 10 only; k = 4 ≥ 3 |

**Conclusion of the audit.** In KPW §§2–4 the hypothesis d < 2(k−1) log(k−1) acts only through:
- (H1) k² − 2k − d + 2 > 0 (A6, A11); and
- (H2) a bound φ(M) ≤ φ(J) − C·Σ(m_pq − 1/k)² for all M ∈ M, with some constant C > 0, where J = (1/k)J_k (A7).
Everything else in §§2–4 holds for all integers d, k ≥ 3. (The Claude review of r1 reached the same conclusion
independently and adds that the consequence k ≥ 3 is also used, which holds at k = 4.)

*Remark (no effect).* In the S_2 display (l.1024–1031) KPW write exp(−((d_{k−1}−d)/(4(k−1)²)) ε² log² n). With
δ = ε log n/((k−1)² n^{1/2}) (l.926–928), the exponent should carry an extra factor (k−1)^{−4}. The conclusion
n^{−Θ(log n)} is unchanged.

## 4. Upper bound: G_{n,7} is a.a.s. 4-colourable

### Proposition 4.1 (KPW Proposition 2(b) under (H1) + (H2))
Let d, k ≥ 3 be integers satisfying (H1) and (H2). Then, for n divisible by k with dn even,
E(Y²) ∼ k^k (k−1)^{k(k−1)} / ((k²−2k−d+2)^{(k−1)²/2} (2π(k−2))^{k−1}) · n^{−(k−1)} k^{2n} (1 − 1/k)^{dn}.

*Proof.* This is KPW's proof of Proposition 2(b) (§3, pp.10–25) verbatim, with two substitutions:
- at l.982 (A6) use (H1);
- at l.1004–1020 (A7) use (H2) in place of the AN bound, which gives (3.15) with constant C.
The S_2 estimate then reads S_2 = O(n^{k²}) poly(n) k^{2n}(1−1/k)^{dn} exp(−C ε² log² n/(k−1)⁴) =
k^{2n}(1 − 1/k)^{dn} n^{−Θ(log n)}, so S_2 = o(S_1). By the audit (A5–A9) no other step of §3 depends on d beyond
d ≥ 3. ∎

At (k, d) = (4, 7), (H1) holds with value 3 and (H2) holds with C = C_7 by Corollary 2.3. Explicitly,
E(Y²) ∼ 4⁴·3¹²/(3^{9/2}(4π)³)·n^{−3}·4^{2n}(3/4)^{7n}.

### 4.2 n ≡ 0 (mod 4): small subgraph conditioning at (k, d) = (4, 7)
Apply W99 Theorem 4.1 (I3) on P_{n,7}, with Y the number of balanced 4-colourings and X_i the number of i-cycles,
λ_i = 6^i/(2i) > 0 and δ_i = (−1)^i/3^{i−1} ≥ −1. Here δ_1 = −1 and |δ_i| ≤ 1/3 for i ≥ 2.
- (a) holds by (I4).
- (b) is KPW (1.1) (I1).
- (c) Σ_i λ_iδ_i² = (9/2) Σ_i (2/3)^i/i = (9/2) log 3 < ∞.
- (d) By (I1) and Proposition 4.1, E(Y²)/(EY)² → 3¹²/(3^{9/2}·3³) = 3^{9/2} = exp((9/2) log 3). This is KPW (1.3)
  with ((k−1)/√(k²−2k−d+2))^{(k−1)²} = (3/√3)⁹.
- EY > 0, and indeed EY grows exponentially, since 4·(3/4)^{7/2} > 1 ⟺ 16·(3/4)⁷ > 1 (§7, item A6).

The first conclusion of Theorem 4.1 gives P(Y > 0) = exp(−Σ_{δ_i=−1} λ_i) + o(1) = e^{−λ_1} + o(1).

*Loops.* A proper colouring forbids loops: a loop at v would require σ(v) ≠ σ(v). Equivalently, KPW's
first-moment enumeration (l.184–194) only joins points of different colour classes ("b_ij = b_ji edges between
colour class i and colour class j (for 1 ≤ i, j ≤ k and i ≠ j)"). So Y = 0 on every pairing with a loop, i.e.
{Y > 0} ⊆ {X_1 = 0}. Since P(X_1 = 0) → e^{−λ_1}, we get P(Y > 0 | X_1 = 0) → 1. Then
P(Y = 0 | X_1 = X_2 = 0) ≤ P(Y = 0 | X_1 = 0)/P(X_2 = 0 | X_1 = 0) → 0, since P(X_2 = 0 | X_1 = 0) → e^{−λ_2} > 0.
By (I4), G_{n,7} is a.a.s. 4-colourable along n ≡ 0 (mod 4). This is KPW's proof of Theorem 1 for n divisible
by k (p.4 l.168–173), with its inputs verified at (4, 7).

### 4.3 n ≡ 2 (mod 4)
KPW §4 defines k′ = 2k if dk is odd and k′ = k otherwise. Here dk = 28, so k′ = 4. Since n is even, the only
residue left is r = 2 (0 < r < 4 with dr even), so dr = 14 and ℓ = dr/2 = 7.

*KPW Theorem 10 under (H1) + (H2).* Its proof (pp.25–26) uses the hypothesis only through A3, A7 and A4/A11
(audit row A12). So with (H1) and (H2) at (k, d, ℓ) = (4, 7, 7): for m ≡ 0 (mod 4), let Ω′_m be the set of
structures (G′, L), where G′ is a simple 7-regular graph on a fixed m-set and L is an ordered 7-tuple of edges of
G′ whose 14 endpoints induce a perfect matching in G′ (I5). If (G′, L) is uniform on Ω′_m, then a.a.s. G′ has a
4-colouring in which every edge of L has end colours 1 and 2.

*The reduction (KPW l.1625–1643), with its conditioning made explicit.* Let n ≡ 2 (mod 4), G = G_{n,7} on vertex
set V, and fix two vertices v_1, v_2. Let 𝒢 be the event that dist_G(v_1, v_2) ≥ 4 and neither v_1 nor v_2 lies
in a triangle.
- P(𝒢) → 1. KPW l.1627–1628 and l.1632–1633: two fixed vertices are a.a.s. at distance at least 4, and a fixed
  vertex is a.a.s. in no cycle of length less than 4. (In P_{n,7} the expected numbers of paths of length ≤ 3
  between v_1 and v_2 and of triangles through v_i are O(1/n), and P(Simple) is bounded below by (I4).)
- *Induced matching.* On 𝒢, N(v_1) and N(v_2) are disjoint 7-sets (distance ≥ 3), there is no edge between them
  (distance ≥ 4), and each is independent (no triangle at v_i). So W := N(v_1) ∪ N(v_2) is an independent 14-set
  in G − {v_1, v_2}. Delete v_1 and v_2, add a uniformly random perfect matching μ on W, and order its 7 edges
  uniformly at random as L. The result G′ is a simple 7-regular graph on V ∖ {v_1, v_2}, which has n − 2 ≡ 0
  (mod 4) vertices. Since W was independent, the only edges of G′ inside W are those of μ, so the endpoints of L
  induce a perfect matching in G′, as Theorem 10 requires. Hence (G′, L) ∈ Ω′_{n−2}.
- *Exact conditional uniformity.* Consider the map (G, μ, order) ↦ (G′, L), defined for G ∈ 𝒢, μ a perfect
  matching of W(G), and an ordering of μ. Every G ∈ 𝒢 has the same number 13!!·7! of choices of (μ, order). The
  map is exactly C(14,7)-to-one onto Ω′_{n−2}. Given (G′, L) ∈ Ω′_{n−2} with endpoint set W, choose which 7 of
  the 14 endpoints form N(v_1); the other 7 form N(v_2). Delete the edges of L, and join v_1 and v_2 to their
  chosen sets. Each of the C(14,7) choices gives a simple 7-regular graph G on V. In it, N(v_1) and N(v_2) are
  disjoint, and W spans no edge, because W induced only L in G′. So dist(v_1, v_2) ≥ 4, there is no triangle at
  v_1 or v_2, and G ∈ 𝒢. The original (μ, order) is recovered from L. Distinct choices give distinct G, and every
  preimage arises this way. Hence, conditional on 𝒢, (G′, L) is exactly uniform on Ω′_{n−2}. This agrees with
  KPW's reinstating count multinomial(dr; d, …, d) = C(14; 7, 7) at l.1638–1640.
- *Colouring.* Colour G′ by Theorem 10 and keep these colours on V ∖ {v_1, v_2}. Give v_1 and v_2 colour 3.
  Every neighbour of v_i is an endpoint of an L-edge, so it has colour 1 or 2. Also v_1 and v_2 are not adjacent.
  Every edge of G avoiding v_1, v_2 is an edge of G′, because G′ = (G − {v_1, v_2}) + μ. So this is a proper
  4-colouring of G.
- *A.a.s. transfer.* P(G_{n,7} is not 4-colourable) ≤ P(𝒢^c) + P_{Ω′_{n−2}}(no 4-colouring with all L-edges
  coloured {1, 2}) → 0.

So G_{n,7} is a.a.s. 4-colourable along n ≡ 2 (mod 4) as well. Together with §4.2, χ(G_{n,7}) ≤ 4 a.a.s. for
n even, n → ∞.

## 5. Lower bound: G_{n,7} is a.a.s. not 3-colourable

### 5.1 Published route (primary)
By the Molloy–Reed criterion (I6) at q = 3 and d = 7: 3·(2/3)^{7/2} < 1 ⟺ 9·(2/3)⁷ < 1 ⟺ 1152/2187 < 1 (exact,
§7, item A7). Hence χ(G_{n,7}) > 3 a.a.s. The weaker formulation in KPW l.175–176 gives the same conclusion,
since (2q − 1) log q = 5 log 3 < 6 < 7 (§7, item A5). W99 l.1107 states χ ≥ 4 a.a.s. for every d ≥ 6.

### 5.2 Self-contained cross-check (computer-assisted; not needed for the Theorem)
ACG (1.1) gives χ > q whenever log q + (d/2) log(1 − 1/q) < 0, for the random regular graph too; at q = 3 this is
log 3 + (7/2) log(2/3) < 0 (§7, item A7). The first moment over all class sizes is re-derived below. The Codex
review of r1 (item 6) independently reproduced the 6,000-piece certificate of Proposition 5.4 using exact
rational logarithm enclosures.

#### Lemma 5.1 (exact count)
Let N = dn be even. Colour the n cells with class sizes n_1, n_2, n_3 and put s_i = d n_i. The number of perfect
matchings of the N points with no pair inside a colour class is
- M(s) = s_1! s_2! s_3!/(b_12! b_13! b_23!), if all b_ij := (s_i + s_j − s_k)/2 ({i,j,k} = {1,2,3}) are
  non-negative integers;
- M(s) = 0 otherwise.

*Proof.* Such a matching has b_ij pairs between classes i and j, and s_i = b_ij + b_ik, which forces the stated
b_ij. Choose, in each class i, which b_ij of its points go to class j: s_i!/(b_ij! b_ik!) ways. Then match
across each pair of classes: b_ij! ways. ∎

#### Lemma 5.2 (exponential bound)
Let x_i = n_i/n, and let P := {x ∈ R³ : Σx_k = 1, 0 ≤ x_k ≤ 1/2}. Define
  w_d(a) := (d−1) a log a − d (1/2 − a) log(1/2 − a),   Φ_d(x) := Σ_k w_d(x_k).
Then the expected number Z_3 of proper 3-colourings of P_{n,d} satisfies
  E Z_3 ≤ e⁴ (n+1)² (dn+1)² · exp(n · max_P Φ_d).

*Proof.*
- E Z_3 = Σ_σ M(s(σ))/(N−1)!!, where (N−1)!! = N!/((N/2)! 2^{N/2}).
- Terms with some x_k > 1/2 vanish, since then b_ij < 0.
- The number of σ with given (n_i) is at most e^{nH(x)}, where H(x) = −Σ x log x.
- By the Stirling bounds of §1, with s_i = Nx_i and b_ij = N(1/2 − x_k), the factor M(s)/(N−1)!! is at most
  e⁴ (N+1)² · exp(N[Σ x_k log x_k − Σ_k (1/2 − x_k) log(1/2 − x_k)]). All the linear terms cancel because
  Σ s_i = N and Σ b_ij = N/2.
- Since nH(x) + N[…] = nΦ_d(x), and there are at most (n+1)² class-size vectors, the bound follows. ∎

#### Lemma 5.3 (KKT reduction)
max_P Φ_d = max over C_1 ∪ C_2, where
- C_1 = {(a, a, 1 − 2a) : a ∈ [1/4, 1/2]};
- C_2 = {(1/2, s, 1/2 − s) : s ∈ [0, 1/2]}.
This is up to permutation of the coordinates, which leaves Φ_d invariant.

*Proof.* Take a maximiser x*.
- If every coordinate lies in (0, 1/2), Lagrange multipliers give w_d′(x_k*) = λ.
  - w_d′(a) = (d−1)(log a + 1) + d(log(1/2 − a) + 1) and w_d‴(a) = −(d−1)/a² − d/(1/2 − a)² < 0, so w_d′ is
    strictly concave and x* takes at most two values.
  - So x* = (a, a, 1 − 2a) up to permutation, with 1 − 2a ∈ (0, 1/2), i.e. x* ∈ C_1.
- Otherwise some x_k* ∈ {0, 1/2}.
  - If x_k* = 1/2, the other two coordinates are (s, 1/2 − s), so x* ∈ C_2.
  - If x_k* = 0, the other two sum to 1 with each ≤ 1/2, so x* = (1/2, 1/2, 0) ∈ C_2. ∎

#### Proposition 5.4
max_P Φ_7 < 0. The balanced value is Φ_7(1/3, 1/3, 1/3) = log 3 + (7/2) log(2/3) ≈ −0.3205; the largest verified
piece bound is ≈ −0.3195 (float display). Only "< 0" is used.

*Proof (computer-assisted, rigorous).* `code/verify_rigorous.py` §C splits C_1 and C_2 into 3000 pieces each.
- On each piece it bounds Φ_7 from above in arb ball arithmetic, using the exact monotonicity of t log t
  (decreasing on [0, 1/e], increasing on [1/e, 1]) for every term.
- Every piece bound is certainly negative. The largest piece bounds are −0.3195 on C_1 (near a = 1/3) and −1.385 on
  C_2.
- Result in `evidence/verify_rigorous.json`, keys C."d=7"."C1 every piece certainly < 0" and "C2 every piece
  certainly < 0", both true. ∎

#### Corollary 5.5
E Z_3 → 0 for d = 7, so P(P_{n,7} has a proper 3-colouring) → 0. By (I4),
P(G_{n,7} is 3-colourable) ≤ P(P_{n,7} 3-colourable)/P(Simple) → 0, since P(Simple) → e^{−12} > 0. Hence
χ(G_{n,7}) ≥ 4 a.a.s., in agreement with §5.1.

**Proof of the Theorem.** Combine §4 (χ ≤ 4 a.a.s.) and §5.1 (χ ≥ 4 a.a.s.). ∎

## 6. Controls

- **C1. KPW's original arithmetic.** At k = 4, KPW need d < 6 log 3 = 6.5917…, so d = 6 is covered and d = 7 is
  not; 6 < 6 log 3 < 7 is item A5. At d = 7, KPW's k is 5, since 7 < 8 log 4. Their exact-value clause
  d > 7 log 4 = 9.70… fails at d = 7.
- **C2. The route fails at d = 8 (rigorous).** Take M = (J + I)/2, with rows (5/8, 1/8, 1/8, 1/8). It is doubly
  stochastic and ρ_M = 7/4. Then
  φ_d(M) − φ_d(J) = log 2 − (5/8) log 5 + (d/2) log(13/12).
  At d = 8 this is positive, which is exactly 13³² > 2⁵⁶·3³²·5⁵ (big-integer check, item B1). The arb value is
  +0.0074193…, and it agrees with a direct evaluation of φ (item B2). At d = 7 the same difference is −0.0326…
  (negative, consistent with Corollary 2.3). So no bound of type (H2) holds at d = 8: J is not the global maximiser
  of φ_8 on M. The row-wise relaxation threshold (27/4) log 3 = 7.4156… < 8 (item A3) fails as well. This stops
  this route at d = 8 and says nothing about χ(G_{n,8}).
- **C3. χ(G_{n,6}) = 4 and non-3-colourability for d ≥ 6.**
  - KPW at d = 6: k = 4, since 4 log 2 < 6 < 6 log 3, and the exact clause 6 > 5 log 3 holds (item A5). This
    reproduces Shi–Wormald's χ(G_{n,6}) = 4.
  - First moment at the balanced point: 3(2/3)³ = 8/9 < 1 (d = 6), and 9(2/3)⁷ = 1152/2187 < 1 (d = 7, squared).
    These are the Molloy–Reed criterion of §5.1.
  - The full rigorous maximisation of §5.2 gives max_P Φ_d < 0 for d = 6, 7, 8.
  - At d = 5 the test is positive, Φ_5(1/3,1/3,1/3) = +0.0849…, as it must be (item A7 and C."d=5").
- **C4. Mutation controls** (item M), all rejected as required:
  - the per-row inequality with constant (3/2) log 3 + 1/100 fails at (3/4, 1/12, 1/12, 1/12), where (3/2) log 3
    holds with equality;
  - C_{15/2} < 0;
  - the first-moment conclusion fails at d = 5;
  - the d = 7 value at the C2 matrix is negative.
- **C5. Sanity (floats, non-evidence).**
  - 2·10⁵ random p: min D/(Σp² − 1/4) = 1.64794 ≥ (3/2) log 3 = 1.64792.
  - 4000 random doubly stochastic M: min normalised gap 0.069 ≥ C_7 = 0.0231.
  - The best possible constant is at most ≈ 0.0435, attained along (1−t)J + tI.

## 7. Verification record

`code/verify_rigorous.py` → `evidence/verify_rigorous.json`. SHA-256 values are recorded in evidence/SHA256SUMS.txt.
Two independent rigorous layers are used:
- exact rational arithmetic, with log enclosures from atanh series plus explicit geometric tail bounds, and
  big-integer comparisons;
- python-flint arb at 256 bits; an arb comparison counts only when certain.

Items:
- A1: 1 < log 3 < 4/3.
- A2: C_7 ∈ (0.023, 0.024) and C_8 < 0.
- A3: c* > 7/2 and 2c* = 7.41563… < 8.
- A4: the η comparisons, including 3⁹ < 2¹⁶.
- A5: KPW threshold arithmetic, including 5 log 3 < 6.
- A6: SSC numbers, (H1) = 3, (d−1)/(k−1)² = 2/3, and EY growth 16(3/4)⁷ > 1.
- A7: balanced first-moment values for d = 5, 6, 7, including 9(2/3)⁷ < 1 exactly.
- B: d = 8 control, exact.
- C: first-moment maximisation, d = 5…8.
- M: mutation controls.
- S: sanity floats.
The run at 06:17:44 PDT returned all_required_true = true. r2 changes no computation, and the verifier was not
rerun for r2.

No other numeric fact is used. Lemma 2.1, Theorem 2.2, the audit and §4 are hand arguments.

## 8. Scope, reliance, prior work, and what is not claimed

- *Reliance.* The proof imports KPW's published arguments for every step of §§2–4 that is independent of d
  (audit A5–A13). Among them, Theorem 10's proof is itself only sketched in KPW. It also imports W99 Theorem 4.1 and
  Theorem 2.6, and the Molloy–Reed criterion (I6) for the lower bound. Proposition 4.1 is "KPW §3 verbatim under
  (H1) + (H2)". Its correctness inherits KPW's, and the audit shows that only (H1) and (H2) carry the
  d-dependence.
- *Prior work (explicit).*
  - **AN 2005, display (12)** (AN l.756–765). Its value (k−1)³ log(k−1)/(k(k−2)) > c_{k−1} means AN's proof of
    their Theorem 7 already covers every c up to (k−1)³ log(k−1)/(k(k−2)), which is (27/8) log 3 at k = 4, though
    the theorem is stated only for c ≤ c_{k−1} (AN l.290). Theorem 2.2 is the k = 4 case. Lemma 2.1 is an
    elementary proof of the per-row form, and is not new mathematics beyond that.
  - **NPG, arXiv:2109.13347v1.** Their Theorem 3.1 (l.530–535), attributed to Achlioptas and Naor, states this
    inequality for c < c_q = (q−1)³ log(q−1)/(q(q−2)) (their (8), l.524–527). Their Theorem 1.2 (l.113–118) uses
    it with c = d/2 (l.1778–1780). It states: for k ≥ 3 and d < ℓ_k = 2(k−1)³ log(k−1)/(k(k−2)), a random n-lift
    of any fixed d-regular loopless multigraph is a.a.s. k-colourable. At k = 4, ℓ_4 = (27/4) log 3 > 7.
  - **What NPG leave open.** They exclude loops. They state that L_n(G) is not contiguous to the uniform model
    G_{n|V(G)|,d} when G has more than one vertex (l.65–67). And they write (l.121–123): "It is conceivable that
    the result also holds for graphs with loops (of either type). In fact, such an extension would imply the main
    result in [18] for the uniform model G_{n,d}, by taking G = B_d." Here [18] is KPW.
  - **What this document adds, if correct.** It transfers the AN (12) constant into KPW's uniform-model argument
    through the d-dependence audit of §3, and supplies the reduction details of §4.3. A referee may regard this as
    a direct corollary of AN (12) and KPW. No novelty or priority is claimed.
- *Priority audits.* Two audits were run.
  - The parent's bounded audit (`institute/runs/six-lane-2026-10-16/review/chi7-priority-audit.md`, 2026-10-17)
    found no source stating χ(G_{n,7}) = 4 for the uniform model. Its access holes are listed there.
  - This worker's earlier bounded check (06:04–06:14 PDT; misses dated in evidence/LOG.md) also found no such
    statement. AM04 §7 remarks that any improvement of AN's second-moment bound "would immediately give an improved
    positive-probability k-colorability result for G_{n,d}" (layout l.532–534).
  - Correction of r1. r1 §8 said no source "uses AN's sharper constant … for regular graphs". That is wrong: NPG
    use it for random lifts of regular multigraphs, which are regular graphs.
  - A search miss is not novelty.
- *Significance* is separate from correctness. If correct, this closes KPW's {4, 5} window at d = 7 for the uniform
  model. Its mathematical content is AN's display (12) at k = 4 plus KPW's machinery and the audit. The route stops
  at d = 8 (control C2). Other degrees in [2(q−1) log(q−1), (2(q−1)³/(q(q−2))) log(q−1)) are not checked here.

## 9. Changes from r1

1. §4.3, from Codex finding 1 and Claude m2/m4. Theorem 10 is quoted exactly ("endpoints induce a perfect
   matching"). The event 𝒢 now includes the exclusion of triangles at v_1 and v_2. Conditional on 𝒢, uniformity
   is shown to be exact (every structure has C(14,7) preimages), followed by the a.a.s. transfer.
2. §4.2, from Claude m3. Loops are now excluded via the definition of a proper colouring and KPW's first-moment
   enumeration (l.184–194), not via (3.2)–(3.3).
3. §1 (I3), from Claude m5. W99 Theorem 4.1 is stated exactly, including its conclusion (l.1584–1596).
4. §5, from Claude m6. The published Molloy–Reed criterion (I6) is now the primary lower bound. The
   computer-assisted first moment is a cross-check.
5. §0 and §3, from Claude m7. The notation is unified: J = (1/4)J_4, and (H2) is written with φ(J).
6. §2 attribution, Theorem 2.2 heading, context and §8, from the priority audit. AN (12) and NPG (Theorems 1.2 and
   3.1) are stated as prior work, with no novelty language. r1's statement that no source uses the sharper
   constant for regular graphs is corrected.
7. §2 Lemma 2.1(c), from the Codex note (item 2). The intermediate zero is v* = 1/3, with q(v) = 4/((1+3v)(1−v)).
8. Claude m1 needs no change. The parent's addendum shows that r1's LF line numbers are correct and that the
   offsets came from the review prompt's numbering. The convention is now stated in §0.
9. Editorial. Audit row A4 now points to §4.2 (r1 said §4.1), and control C3 points to §5.2.
