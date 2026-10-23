# FROZEN r3 — candidate proof: the random 12-regular graph has chromatic number 5 a.a.s.

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the
file (README §1, evidence/LOG.md, evidence/SHA256SUMS.txt). r3 supersedes r2 (`review/PROOF_CHI12.r2.md`, SHA-256
5fee0295e1ec3716b26924920f015d4a2116e63516ac12f6431724ef1d6e1a00), which supersedes r1 (`review/PROOF_CHI12.r1.md`,
SHA-256 0b608b0790887d8ade912b6cf5700ab57df3b2ff57ad7936430eafdb7b35d85e); both are kept unchanged. r3 is r2 plus
exactly the two editorial fixes of §11, items 7–8. §11 lists every change.

**Status.** CANDIDATE PROOF, worker-written. r3 itself has not been reviewed. r2 received an independent Codex delta
review, `chi12-r2-delta-codex-review-v1.note.md`: ACCEPT-WITH-FIXES, with two minor findings and no fatal or major
finding. Both fixes are applied (§11, items 7–8).
- Reviews of r1 (parent-held, under `institute/runs/six-lane-2026-10-16/review/`):
  - Codex CLI hostile review, `chi12-codex-hostile-review-v1.note.md`: ACCEPT-WITH-FIXES, with no fatal or major
    finding. Its one minor finding: the general small-subgraph-conditioning formulation quoted in r1 (I3) is
    overstrong, while the colouring application is unaffected. Applied in §§1, 4, 5.2, 5.3 and 9 (§11, item 1).
  - Claude CLI complete review, `chi12-claude-complete-review-v1.note.md`: ACCEPT-WITH-FIXES, with no fatal or major
    finding. Of its six minor findings, m1–m5 are applied (§11, items 2–6); m6 asks for no change, because the
    sketched Theorem 10 steps were already disclosed.
  - Parent replay of the verifier, `chi12-parent-verifier-replay-v1/parent-result.json`: byte-identical output,
    all_required_true = true.
- Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-random12reg-colour-contract.json` (SHA-256
  9b33f97f42179c6b15a50cdd3ae3ec907821cf4e9330663a7dadf43a406f15bb). Its acceptance items (1)–(7) are mapped in §10.
- The route is the one of the accepted χ8 proof (`physics/evidence/six-lane-20261016/random8reg-colour/review/
  PROOF_CHI8.r3.md`, SHA-256 e7c506d0bcd75aad69ce004c4633ffa15e5a8ee64d90f53bf9c6867b95187e2d), re-run concretely at
  (k, d) = (5, 12). The χ8 route was proposed by the parent orchestrator.
- No novelty or priority claim. Priority and significance are shared with χ8, because the mechanism is the same
  (§9). The entropy duality of Lemma A is standard, and its closed form is GSVY's Φ_1 (§2.1).

## Theorem

Let G_{n,12} be the uniformly random 12-regular simple graph on n vertices (dn = 12n is even for every n). Then
P(χ(G_{n,12}) = 5) → 1 as n → ∞.

**Context (cited, not used).**
- KPW Theorem 1 (l.105–107) takes k smallest with d < 2(k − 1) log(k − 1) and concludes χ ∈ {k − 1, k}. At d = 12
  this k is 6, since 8 log 4 = 11.09… < 12 < 10 log 5 = 16.09…, so χ(G_{n,12}) ∈ {5, 6} a.a.s. The exact-value clause
  d > (2k − 3) log(k − 1) = 9 log 5 = 14.48… fails (verifier A).
- ACG Table 1 (pinned layout l.131–135): for q = 5, d_{5,smm} = 11 and d_5 = 15, so d = 12 is undetermined there;
  for q = 4, d_4 = 10 ≤ 12.
- Achlioptas–Naor's Theorem 7 (c ≤ 4 log 4, i.e. d ≤ 11.09…) and display (12) (d < (128/15) log 4 = 11.83…), and
  Nir–Pérez-Giménez Theorem 1.2 (ℓ_5 = 11.83…, random lifts of loopless graphs), do not reach d = 12.
- The accepted χ8 proof settles (k, d) = (4, 8) by the same route.
- GSV (J. ACM 2015) and GSVY (SIAM J. Comput. 2016) introduced the ℓ_{d/(d−1)} reformulation Φ of the pairing-model
  moment exponents. U(M) below is GSVY's Φ_1 for the paired interaction B ⊗ B, evaluated at M^{11/12} (§2.1).

**Proof outline.**
- **Upper bound (§§2–5).** KPW's balanced-colouring second moment plus small subgraph conditioning, at k = 5 colours
  and d = 12. KPW's hypothesis d < 2(k−1) log(k−1) fails here (8 log 4 < 12). The audit (§4) shows that at (5, 12)
  it enters KPW §§2–4 only through:
  - (H1) k² − 2k − d + 2 > 0, here 5 > 0, which is all the S_1 asymptotics need;
  - the S_2 estimate, i.e. Lemma 5 → (3.7) → (3.9) combined with AN's bound (3.15), which is unavailable at d = 12.
  The S_2 estimate is replaced by:
  - Lemma A (§2): KPW's exact count (3.4) at k = 5, Stirling bounds and pointwise weak duality, with an explicit
    polynomial factor and empty cells handled;
  - Theorem C (§3): global quadratic decay of U(M) = −11 log 5 + 6 log(2E(M)), proved by a k = 5 row reduction and an
    analytic row inequality on the 5-point simplex (hypercontractivity of the resampling chain).
- **Every n (§5.3).** KPW Theorem 10, with r ∈ {1, 2, 3, 4} deleted vertices and ℓ = 6r distinguished edges whose
  endpoints induce a perfect matching. Conditional uniformity is exact.
- **Lower bound (§6).** Molloy–Reed at q = 4, plus a self-contained weak-duality first moment.

## 0. Sources, conventions, notation

- **Line numbers** count LF-terminated lines of the `.layout.txt` files; a form feed is not a line break.
- **Pinned by the parent**, read in place at `institute/runs/six-lane-2026-10-16/review/colour7-parent-source-screen-v1/`:
  - **KPW**: Kemkes, Pérez-Giménez, Wormald, *On the chromatic number of random d-regular graphs*, arXiv:0812.2937v1
    (Adv. Math. 223 (2010) 300–328). PDF bf56a321c5da2f9c65f42fabce19a6aed0cf98ed09521e14a78ecc98ecb5657f; layout
    c75d6c7da3988ccc4d4e44c8e47456fcb3fba6dd7e4826f8af49ef4d48462afd.
  - **AN**: Achlioptas, Naor, Ann. of Math. 162 (2005). Layout b22f7ba1…0430.
  - **ACG**: Ayre, Coja-Oghlan, Greenhill, arXiv:1812.09691v4, pinned at `…/colour7-parent-source-screen-v2/`.
- **Read-only prior-lane sources** under `physics/evidence/six-lane-20261016/random7reg-colour/sources/`:
  - **W99**: Wormald, *Models of random regular graphs* (1999). PDF 987de47e…cb70; layout
    61ed000620fdbc0e9da1423d08a9996d6f64efa9d4e5c83374551d39dc855693.
  - **D–SC**: Diaconis, Saloff-Coste, *Logarithmic Sobolev inequalities for finite Markov chains*, Ann. Appl.
    Probab. 6 (1996) 695–750. PDF 6a67ed8683035f09e351c67db8430e22a0e00b39e084d3152ca7270acba6db0c; layout
    63905a28baa71497059c014e0251c51f7db5e34263a6e9aa8212641eb985502f.
  - **NPG**: Nir, Pérez-Giménez, arXiv:2109.13347v1. PDF 09161e92…5893.
- **Read-only prior-lane sources** under `physics/evidence/six-lane-20261016/random8reg-colour/sources/`:
  - **GSV**: arXiv:1305.2902v3, PDF 1539a5ec1d0e76f724691bb6680c044f2019414b23ebcd92f1bc955883a9a366.
  - **GSVY**: arXiv:1311.4839v3, PDF 545891749f573b925c348dfae11a88155bc4ff7f12d398ec1af8353d883f352a.
- log is the natural logarithm.
- **Colours and cells.** k = 5, d = 12. Cells are u = (p, q) ∈ [5]². A colour count is a 5×5 doubly stochastic
  matrix M = (m_u), as in KPW §3, so Σ_u m_u = 5. M is the set of such matrices, and S_5 the set of 5×5
  row-stochastic matrices. J_5 is the all-ones matrix and J := (1/5)J_5; KPW's (1/k)J_k is J.
- **Allowed pairs.** u = (p, q) and v = (r, s) are allowed, u ~ v, iff p ≠ r and q ≠ s. The allowed pairs form the
  graph K_5 × K_5, with 200 unordered pairs (verifier A).
- **Norms and the simplex.** ‖M − J‖² := Σ_u (m_u − 1/5)². Δ_5 is the probability simplex in R⁵,
  u_* := (1/5, …, 1/5) is the uniform row, and |r − u_*|² := Σ_j (r_j − 1/5)².
- **Main functions.**
  - β := 11/12, and f_u := m_u^{β}, with 0^{β} = 0.
  - E(M) := Σ_{unordered allowed {u,v}} f_u f_v.
  - U(M) := −11 log 5 + 6 log(2E(M)).
- **Constants.**
  - ρ := 1/4; α := 3/(5 log 4);
  - a := 11^{−5 log 4/12};
  - κ := (121/18)(a² − 1/16);
  - E_0 := E(J) = 200·5^{−11/6};
  - C_12 := 6κ/E_0.
- **Row functions.** For r ∈ Δ_5: S(r) := Σ_j r_j^{11/12}, Q(r) := Σ_j r_j^{11/6} and F(r) := (3/2)S(r)² + Q(r)/2.
- **Other symbols kept distinct.**
  - supp M := {u : m_u > 0} is the support. S(r) is the row function. S_1 and S_2 are KPW's two parts of E(Y²).
  - c_0 is the additive constant in the multipliers μ_u = c_0 + (11/12) log m_u (Proposition B).
  - c_row := 1/40 is the constant of the supplementary interval check, and K_b is its boundary constant (§3).
  - c_KPW := d/(2k²(k−1)²) is the constant in KPW's Lemma 8.
  - c_1 is the multiplier constant in §6.2.
  - η denotes the random perfect matching in §5.3.
  - K(x, y) denotes only the Markov kernel of §3.
- **Conventions.** 0 log 0 = 0 and 0⁰ = 1.

## 1. Imports, with exact hypotheses checked at (k, d) = (5, 12)

- **(I1) KPW Proposition 2(a)** (l.122–140). Hypotheses: "Fix integers d, k ≥ 3"; Y is the number of balanced
  k-colourings of P_{n,d}, with n a multiple of k. At (5, 12): d = 12 ≥ 3 and k = 5 ≥ 3, and dn is always even.
  Conclusions:
  - EY ∼ k^{k/2}((k−1)/(2π(k−2)))^{(k−1)/2} n^{−(k−1)/2} k^n (1 − 1/k)^{dn/2}, which here is
    (100√5/(9π²))·n^{−2}·5^n (4/5)^{6n} (verifier A);
  - (1.1): E(Y[X_1]_{p_1}…[X_j]_{p_j}) ∼ Π_m (λ_m(1+δ_m))^{p_m} EY, with λ_m = (d−1)^m/(2m) = 11^m/(2m) and
    δ_m = (−1)^m/(k−1)^{m−1} = (−1)^m/4^{m−1}.
- **(I2) KPW §3 machinery used:**
  - the count (3.1)–(3.4);
  - the Stirling estimate (3.5)–(3.6);
  - Lemmas 4, 6, 7, 8 and 9;
  - the S_1 asymptotics (3.10)–(3.14).
  The audit (§4) is carried out at (k, d) = (5, 12) only; no statement is made for other (k, d). At (5, 12),
  (3.13)–(3.14) use (H1) = 5 > 0, and the remaining hypotheses that occur are k = 5 and conditions on ε that do not
  depend on d.
  - Lemma 4 (l.373–384), quoted: "Let k be a positive integer. Define the function f : R^k → C by
    f(θ) = ia(n, θ) − c_1 nθᵀBθ where i is the imaginary unit, a is a real function, B is a fixed k-by-k positive
    definite real matrix, and c_1 > 0 is a real constant. Let δ = c_2 n^{−1/2} log n for some real constant c_2 > 0.
    Then, as n → ∞, ∫_{[−δ,δ]^k} e^{f(θ)} dθ = ∫_{[−∞,∞]^k} e^{f(θ)} dθ + O(e^{−c(log n)²}) for some constant c > 0."
    Its k is a dimension, not the number of colours. Its proof (l.387–390) uses only that the real part of f is
    −c_1 nθᵀBθ ≤ −c_1 nλ|θ|², with λ > 0 the smallest eigenvalue of B. **It has no degree hypothesis.** KPW apply it
    at l.534 (Lemma 3, with A = r²(11ᵀ + (k − 2)I_k) positive definite), at l.983 (S_1, with B = H, positive definite
    by (H1); row A15) and at l.1436 (Lemma 8, with B = (k−1)²I_{k²} + (J_k − I_k)^{⊗2}, whose smallest eigenvalue is
    (k − 1)(k − 2) = 12 > 0 by Lemma 6(a)).
  - Lemma 9's proof (l.1251) uses "(k − 1)² + (k − 1)² exceeds k²": at k = 5 this is 32 > 25 (verifier A).
  - Lemma 8, first ε-condition: "ε′ < d/(16k²(k−1)²)" (l.1356). In (3.20) (l.1296–1311), I is a constant times
    n^{−k²/2} e^{dn/2} exp(−nd(k−1)²(vecÃ)ᵀ(J_{k−1}+I_{k−1})^{⊗2}vecÃ/(2(k²−2k+2))); the factor n^{−k²/2} comes from
    the Gaussian factors (π/(cnλ_{p,q}))^{1/2} of (3.22). Under |a_pq| < ε log n/n^{1/2}, the eigenvalues of
    (J_{k−1}+I_{k−1})^{⊗2} are at most k², so the exponential factor is at least exp(−D_1ε² log² n) with
    D_1 := dk²(k−1)⁴/(2(k²−2k+2)) = 38400/17 at (5, 12). Because n^{−k²/2} = e^{−o(log² n)}, (3.20) holds with a
    constant K for every constant ε′ > D_1ε²; the strict inequality is needed to absorb the factor n^{−k²/2}. An ε′ with
    D_1ε² < ε′ < d/(16k²(k−1)²) = 3/1600 exists iff ε² < (k²−2k+2)/(8k⁴(k−1)⁶) = 17/20480000, in which d cancels
    (verifier A, symbolic in d and k; verifier r2, M1).
  - Lemma 8, second ε-condition (l.1436–1452). There Lemma 4 replaces ∫_{[−δ,δ]^{k²}} e^{h} by the full Gaussian
    integral with error O(e^{−c′ log² n}), where δ = log n/n^{1/2} (l.1289) and h(θ) = −i(dn/k)(vecA)ᵀθ − cnθᵀBθ;
    KPW note that "c′ does not depend on ε and we will choose ε to be sufficiently small" (l.1452).
    - The tail is at most a power of n times e^{−cλ_min log² n} (union bound over the k² coordinates and the
      one-dimensional Gaussian tail), so any constant c′ < cλ_min is admissible. Here
      cλ_min = d(k−2)/(2k²(k−1)) = 9/50 at (5, 12).
    - The main term is at least a constant times n^{−k²/2} exp(−D_2ε² log² n). By Lemma 7(a), (b) its exponent is
      −nd(k−1)²‖A‖²/(2(k²−2k+2)), and ‖A‖² < k²ε² log² n/n, so D_2 := dk²(k−1)²/(2(k²−2k+2)) = 2400/17.
    - The error is therefore o(main term) once D_2ε² < cλ_min, i.e. ε² < (k−2)(k²−2k+2)/(k⁴(k−1)³) = 51/40000; d
      cancels again. The first condition implies this one, since 17/20480000 < 51/40000. With the cruder
      coefficient D_1 in place of D_2 the condition would read ε² < 51/640000, which is also implied.
    Verifier r2 (M1, L67) checks these constants, the spectrum of B and Lemma 7(a)–(c) at k = 5 exactly.
  - c_KPW = d/(2k²(k−1)²) = 3/200 > 0, and ρ_KPW = √(dn)/(k(k−1)) = √(12n)/20.
  **Not imported:** Lemma 5, (3.7), (3.9), (3.15) and AN Theorem 7. Lemma A and Theorem C replace them.
- **(I3) Small subgraph conditioning**, W99 Theorem 4.1 (l.1561–1596), stated exactly. Let λ_i > 0 and δ_i ≥ −1,
  i = 1, 2, …, be reals. For each n let X_i = X_i(n) (non-negative integer valued) and Y = Y(n) (non-negative, with
  EY > 0 for n sufficiently large) be random variables on one probability space G = G(n). Suppose:
  - (a) for each k ≥ 1, X_1, …, X_k are asymptotically independent Poisson random variables with EX_i → λ_i;
  - (b) E(Y[X_1]_{j_1}…[X_k]_{j_k})/EY → Π_{i=1}^{k} (λ_i(1+δ_i))^{j_i} for every finite sequence j_1, …, j_k of
    non-negative integers;
  - (c) Σ_i λ_iδ_i² < ∞;
  - (d) EY_n²/(EY_n)² ≤ exp(Σ_i λ_iδ_i²) + o(1) as n → ∞.
  Conclusion (l.1584–1596): "Then P(Y_n > 0) = exp(−Σ_{δ_i=−1} λ_i) + o(1), and, provided Σ_{δ_i=−1} λ_i < ∞,
  G^{(Y)} ≈ Ĝ where Ĝ is the probability space obtained from G by conditioning on the event ∧_{δ_i=−1}(X_i = 0)."
  The layout drops the hat of Ĝ at l.1592 and l.1594. W99 attributes the theorem to its references [56] and [87]
  (l.1561). W99's index k in (a)–(b) is not the number of colours.
  - *Definitions* (W99 §4.1, l.1519–1548). For a non-negative integer random variable Y on G with EY ≠ 0, the space
    G^{(Y)} has the same underlying set as G, and "the probability of G in G^{(Y)} equals the probability in G
    multiplied by Y(G)/EY" (l.1523–1525). So an event H has probability E_G(Y·1_H)/E_G Y in G^{(Y)} (l.1526).
    Sequences of spaces (G_n) and (Ĝ_n) that differ only in the probabilities are contiguous, G_n ≈ Ĝ_n, if "a
    sequence of events A_n is a.a.s. true in G_n if and only if it is a.a.s. true in Ĝ_n" (l.1531–1536);
    equivalently, lim P(A_n) = 0 in one sequence iff it holds in the other, for every sequence of events A_n
    (footnote 2, l.1545–1548).
  - **Only the contiguity conclusion G^{(Y)} ≈ Ĝ is used.** The first displayed conclusion is overstrong under
    (a)–(d) alone, and this proof does not use it. Counterexample (Codex hostile review of r1): replace this
    proof's Y by Y + 1. Because EY grows exponentially, the added terms are negligible in every normalised moment,
    so (a)–(d) hold with the same parameters; but P(Y + 1 > 0) = 1 ≠ e^{−11/2}. The example leaves the contiguity
    conclusion intact: for every event A, P_{G^{(Y+1)}}(A) − P_{G^{(Y)}}(A) = (EY·P(A) − E(Y·1_A))/(EY(EY + 1)),
    whose absolute value is at most 1/(EY + 1).
- **(I4) Cycle counts**, W99 Theorem 2.6 (Bollobás; l.361–366). For fixed d, the cycle counts X_1, …, X_k of P_{n,d}
  are asymptotically independent Poisson with means (d−1)^i/(2i). So P(Simple) = P(X_1 = X_2 = 0) → e^{(1−d²)/4},
  which is e^{−143/4} at d = 12 (W99 (3), l.248). G_{n,d} is P_{n,d} conditioned on Simple, because each simple graph
  arises from exactly (d!)^n pairings.
  - Hypothesis (a) of (I3) also asks for EX_i → λ_i, which convergence in law alone does not give. It holds: for
    every i ≥ 1 (i = 1 loops, i = 2 double edges),
      EX_i = [n]_i (d(d−1))^i / (2i·Π_{j=0}^{i−1}(dn − 1 − 2j)) → (d−1)^i/(2i).
    Here [n]_i (d(d−1))^i counts oriented descriptions: a sequence of i distinct vertices together with an ordered
    pair of distinct points at each vertex (the points used to enter and to leave it). Each i-cycle of the complete
    configuration has exactly 2i oriented descriptions (i starting vertices and two directions), so dividing the
    complete count by 2i counts these cycles, for every fixed i ≥ 1, loops (i = 1) and double edges (i = 2)
    included. Finally, 1/Π_{j<i}(dn − 1 − 2j) is the probability that the i resulting disjoint point pairs all lie
    in the random pairing. Verifier r2 (M4) checks the formula
    exactly against exhaustive enumeration of all pairings for eleven small (n, d) and i ≤ 4, and checks the limit
    symbolically in d.
- **(I5) KPW Theorem 10** (l.1536–1541): "Fix nonnegative integers d ≥ 3, k and ℓ such that d < 2(k − 1) log(k − 1).
  Consider the d-regular graphs with n vertices (n divisible by k and dn even) and a distinguished ordered set of ℓ
  edges whose endpoints induce a perfect matching (i.e. no two edges in the distinguished set are adjacent to the
  same edge or incident with the same vertex). Let G be chosen uniformly at random from such structures. Then G
  a.a.s. has a k-colouring in which all ℓ distinguished edges have end vertices coloured 1 and 2."
  - The hypothesis d < 2(k − 1) log(k − 1) fails at (5, 12).
  - Audit rows A12 and A14 show that its proof (l.1542–1621) uses the hypothesis only through:
    - Proposition 2(b), via (4.2);
    - the S_2 restriction at l.1610–1615;
    - "the argument in the last few sentences of the proof of Theorem 1" (l.1558–1559), which uses Proposition 2,
      (1.2) and (1.3).
  - Proposition 5.1 below supplies all of these at (5, 12). Here ℓ = 6r ∈ {6, 12, 18, 24}.
- **(I6) Molloy–Reed criterion**, in the pinned sources:
  - KPW l.67–68: "For fixed d, Molloy and Reed [16] showed that if q(1 − 1/q)^{d/2} < 1 then χ(G_{n,d}) > q a.a.s."
  - KPW l.175–178: the weaker form "if d > (2q − 1) log q then χ(G_{n,d}) > q", with "(Their proof is reported in
    [20], Theorem 1.3.)"
  - W99 l.1102–1107: Molloy and Reed's calculation shows that the nth root of the expected number of r-colourings
    "is at most r((r−1)/r)^{d/2} + o(1) (for fixed r and d)".
- **(I7) D–SC.** Used only in the analytic proof of Lemma 3.2, on which Theorem C rests.
  - l.34–36: "We work with a finite state space X and an irreducible Markov kernel K(x, y) ≥ 0, Σ_y K(x, y) = 1.
    The continuous time semigroup associated to K is H_t = exp(−t(I − K))."
  - l.77: E(f, f) = (1/2) Σ_{x,y} |f(x) − f(y)|² K(x, y) π(x).
  - l.99: L(f) = Σ |f|² log(|f|²/‖f‖₂²) π.
  - l.101–105, (1.7): α = min {E(f, f)/L(f); L(f) ≠ 0}.
  - Theorem 3.5(ii) (l.1365–1371): "Assume that (K, π) is reversible. Then ‖H_t‖_{2→q} ≤ 1 for all t > 0 and all
    2 ≤ q < +∞ satisfying e^{4αt} ≥ q − 1."
  - Theorem A.1 (l.2727–2739): "Let π be a probability measure on the finite set X. … Consider the chain
    K(x, y) = π(y) which has invariant measure π. The log-Sobolev constant α of this chain is given by
    α = (1 − 2π_*)/log(1/π_* − 1). In particular, for π ≡ 1/|X|, α = (1 − 2/|X|)/log(|X| − 1)."
  - D–SC use L² duality of H_t in the same way at l.2672–2676.
  - K(x, y) = π(y) is the resampling chain, including its diagonal entries (holding probability π(x)). D–SC
    Corollary A.5 shows that the walk without holding has a different constant; only Theorem A.1's chain is used.
- **(I8) Elementary facts.**
  - Stirling bounds: (m/e)^m ≤ m! ≤ e√(m+1)(m/e)^m for every integer m ≥ 0.
  - Multinomial bound: N!/Π_i N_i! ≤ Π_i (N/N_i)^{N_i} for N_i ≥ 0 with Σ N_i = N.
  - max_{x ≥ 0}(−x log x + θx) = e^{θ−1}, attained at x = e^{θ−1}; the function is concave.
  - e^x = Σ_{j≥0} x^j/j! with all terms positive for x > 0; Hölder's inequality, the Cauchy–Schwarz inequality and
    the mean value theorem.

## 2. Lemma A at k = 5: exact count and pointwise weak duality

**The exact count** (KPW (3.2)–(3.4), l.597–645). Fix M ∈ M ∩ (5/n)Z^{5×5} and put n_u := m_u n/5. B(M, n) is the
set of tuples (b_e) of non-negative integers, indexed by the 200 unordered allowed pairs e = {u, v}, such that
Σ_{v ~ u} b_{uv} = d n_u for every cell u ((3.2)–(3.3)). Then
  |T(M)| = n!/(Π_u n_u!) · Π_u (d n_u)! · Σ_{b ∈ B(M,n)} Π_e 1/b_e!,   |P_{n,d}| = (dn)!/((dn/2)! 2^{dn/2}),
and E(Y²) = Σ_{M ∈ M ∩ (k/n)Z^{k×k}} |T(M)|/|P_{n,d}| (KPW (3.1)). T(M) is the set of triples (P, C_1, C_2): P a
pairing, and C_1, C_2 balanced colourings of P with colour count M.

### Lemma A
Let d ≥ 1, n ≥ 1 with 5 | n and dn even, and M ∈ M ∩ (5/n)Z^{5×5} with support supp M := {u : m_u > 0}. For every
μ ∈ R^{supp M},
  |T(M)|/|P_{n,d}| ≤ P_d(n)·exp(n·V_μ(M)),
where
  V_μ(M) := ((d−1)/5) Σ_u m_u log m_u + (1−d) log 5 + (d/2) log d + Σ_{e = {u,v} ⊆ supp M, u ~ v} e^{μ_u + μ_v − 1}
           − (d/5) Σ_{u ∈ supp M} μ_u m_u
and P_d(n) := e^{26}(dn + 1)^{25/2} (dn/2 + 1)^{401/2}. P_d(n) depends on neither M nor μ.

*Proof.* Each bound is applied to the exact count.
1. *Colourings.* By the multinomial bound, n!/Π_u n_u! ≤ Π_{u ∈ supp M} (n/n_u)^{n_u} = exp(n H_5(M)), where
   H_5(M) := −Σ_u (m_u/5) log(m_u/5). Empty cells contribute 0! = 1 and 0⁰ = 1.
2. *Points of each cell.* For u ∈ supp M, (d n_u)! ≤ e√(dn_u + 1)(dn_u/e)^{dn_u} ≤ e√(dn + 1)(dn_u/e)^{dn_u}. For
   u ∉ supp M, (d n_u)! = 0! = 1 = (0/e)⁰. There are 25 cells, so
   Π_u (d n_u)! ≤ e^{25}(dn + 1)^{25/2} Π_{u ∈ supp M} (dn_u/e)^{dn_u}.
3. *Edge factorials.* For every b ∈ B(M, n) and every e, 1/b_e! ≤ (e/b_e)^{b_e} (lower Stirling bound; b_e = 0 gives
   1 ≤ 1). Summing (3.3) over u gives Σ_e b_e = dn/2, so Π_e 1/b_e! ≤ e^{dn/2} exp(−Σ_e b_e log b_e).
4. *Number of tuples.* Each b_e lies in {0, …, dn/2}, so |B(M, n)| ≤ (dn/2 + 1)^{200}.
5. *Pairings.* 1/|P_{n,d}| = (dn/2)! 2^{dn/2}/(dn)! ≤ e√(dn/2 + 1)(dn/(2e))^{dn/2} 2^{dn/2}/(dn/e)^{dn}
   = e√(dn/2 + 1)·(dn/e)^{−dn/2}.
6. *Empty cells in B(M, n).* If u ∉ supp M then (3.3) forces b_e = 0 for every e ∋ u. Such edges contribute
   b_e log b_e = 0, so only edges e ⊆ supp M remain.
7. *Pointwise weak duality.* Fix b ∈ B(M, n) and write b_e = nβ_e. Then
   −Σ_e b_e log b_e = −n Σ_e β_e log β_e − (dn/2) log n.
   The constraints read Σ_{v ~ u} β_{uv} = d m_u/5 for u ∈ supp M. For any μ ∈ R^{supp M}, with all sums over
   e = {u, v} ⊆ supp M and u ∈ supp M,
     −Σ_e β_e log β_e = Σ_e [−β_e log β_e + β_e(μ_u + μ_v)] − Σ_u μ_u Σ_{v~u} β_{uv}
                      ≤ Σ_e e^{μ_u+μ_v−1} − (d/5) Σ_u μ_u m_u.
   The equality holds because each edge contributes β_e to both endpoint constraints. The inequality is (I8)
   applied to each term with θ = μ_u + μ_v. No strong duality and no exact inner optimum is needed.
8. *Collecting exponents.* Multiply items 1–5 and substitute item 7 for every b. Since Σ_u d n_u = dn and
   Σ_e b_e = dn/2, the factors (dn_u/e)^{dn_u}, e^{dn/2}, n^{−dn/2} and (dn/e)^{−dn/2} give exactly
     n[Σ_u (d m_u/5) log(d m_u/5) − (d/2) log d] + dn log n − dn + dn/2 − (dn/2) log n − (dn/2) log n + dn/2.
   The n log n terms and the linear terms cancel. Using Σ_u m_u = 5,
     H_5(M) + Σ_u (d m_u/5) log(d m_u/5) − (d/2) log d = ((d−1)/5) Σ_u m_u log m_u + (1−d) log 5 + (d/2) log d
   (verifier B, symbolic in the 25 cell variables).
9. *Polynomial factor.* The non-exponential factors are e^{25}(dn+1)^{25/2}, (dn/2+1)^{200} and e√(dn/2+1), whose
   product is P_d(n). ∎

### Proposition B (closed form at d = 12)
For every M ∈ M ∩ (5/n)Z^{5×5},
  |T(M)|/|P_{n,12}| ≤ P_12(n)·e^{n U(M)},   U(M) = −11 log 5 + 6 log(2E(M)),
  P_12(n) = e^{26}(12n + 1)^{25/2}(6n + 1)^{401/2}.
Moreover E(M) ≥ (15 + ‖M‖_F²)/2 ≥ 8 > 0 on M, and U(J) = 24 log 2 − 10 log 5 = 2(log 5 + 6 log(4/5)), which is
the exponent of (EY)².

*Proof.*
- Take μ_u := c_0 + (11/12) log m_u for u ∈ supp M, with c_0 real.
- Since (d−1)/5 = (d/5)(11/12) = 11/5, the entropy terms cancel, and (d/5)Σ_{u ∈ supp M} μ_u m_u = 12c_0 +
  (11/5)Σ m log m (verifier B). Also Σ_{e ⊆ supp M} e^{2c_0−1}(m_u m_v)^{11/12} = e^{2c_0−1} E(M), where pairs
  touching an empty cell contribute 0 to E anyway. So, with w := e^{2c_0−1} > 0,
  V_μ(M) = −11 log 5 + 6 log 12 + wE(M) − 6(1 + log w).
- This is strictly convex in w and minimal at w = 6/E(M), with value −11 log 5 + 6 log(2E(M)) (verifier B, the general
  form (1−d) log k + (d/2) log(2E) at w = d/(2E)). The choice requires E(M) > 0.
- *Lower bound on E.* m^{11/12} ≥ m on [0, 1], so E(M) ≥ Σ_{allowed} m_u m_v. For doubly stochastic 5×5 M this
  equals (15 + ‖M‖_F²)/2 (verifier B, a symbolic check on the generic doubly stochastic matrix). Since
  ‖M‖_F² ≥ (Σ m)²/25 = 1, E(M) ≥ 8.
- *At J.* E(J) = 200·(1/25)^{11/12} = 200·5^{−11/6}, so U(J) = −11 log 5 + 6 log(400·5^{−11/6}) = 24 log 2 − 10 log 5
  (verifier B). By (I1) this is the exponent of (EY)² = Θ(n^{−4}) 5^{2n}(4/5)^{12n}. ∎

### 2.1 Relation to prior work (precursors), at k = 5
Nothing in Lemma A or Proposition B is a new entropy duality; see the accepted χ8 proof (r3 §2.1) for the full
discussion. At k = 5:
- With R := M^{11/12}, GSVY's Φ_1 (their (15), Δ = 12) for the paired interaction B ⊗ B, B = J_5 − I_5, is
  Φ_1^{B⊗B}(R) = 6 log(Σ_{u,v}(B⊗B)_{uv}R_uR_v) − 11 log Σ_u R_u^{12/11} = 6 log(2E(M)) − 11 log 5 = U(M) (verifier D,
  general d and k). GSVY's map (20) sends M^{11/12} to M/5.
- GSV/GSVY drop the overlap-marginal constraints and evaluate the unconstrained maximum through induced matrix norms,
  which needs a bipartite form or a PSD interaction. Here B has eigenvalues 4, −1 (four times), so B ⊗ B has
  eigenvalues 16, −4 (eight times) and 1 (sixteen times) and is not PSD (verifier D, exact). GSVY Remark 2's
  obstruction (a negative first-moment exponent) does not arise: log 5 + 6 log(4/5) = log(4096/3125) > 0.
- The distinction is as in χ8: Lemma A keeps the 25 per-cell constraints (3.3); Theorem C bounds U on doubly
  stochastic M (its E-inequality holds on all row-stochastic M) with quantitative decay. No claim is made that either
  constraint is logically necessary.
- *Float observation (not evidence, not used).* KPW's relaxed exponent φ_12(M) = −(1/5)Σ m log m +
  6 log(3/5 + Σm²/25) appears, numerically, to be maximised at J over 5×5 doubly stochastic matrices: 320 SLSQP
  starts all ended at J, and three one-parameter families stay below φ_12(J) (`explore/explore_k5.json`). So, unlike
  at (4, 8), no evidence is offered here that the relaxed route fails at (5, 12) for a structural reason; what is
  unavailable at d = 12 is a proof of the relaxed decay bound (AN Theorem 7 covers d ≤ 11.09… and AN (12) covers
  d < 11.83…). This proof uses Theorem C because it supplies a complete rigorous decay bound.

## 3. Theorem C at k = 5: global quadratic decay

### Lemma 3.1 (row reduction at k = 5)
Let (f_pq) be any 5×5 array of non-negative reals, with row sums R_p, column sums C_q, total Σf and
E(f) := Σ_{unordered allowed} f_u f_v. Then
  2E(f) = (Σf)² − Σ_p R_p² − Σ_q C_q² + Σ f_pq²,
and
  E(f) ≤ Σ_p ((3/2)R_p² + Q_p/2),   Q_p := Σ_q f_pq².

*Proof.* The first identity is inclusion–exclusion over the pairs with p = r or q = s (verifier B, symbolic in the
25 entries). For the second, an exact identity (verifier B) gives
  3Σ_p R_p² + Σ f² − 2E(f) = [Σ_q C_q² − (Σf)²/5] + (4/5)[5Σ_p R_p² − (Σ_p R_p)²].
Both brackets are ≥ 0 by Cauchy–Schwarz over the five columns and the five rows. ∎

If M ∈ S_5 and f = m^{11/12}, then row p contributes (3/2)R_p² + Q_p/2 = F(r_p), where r_p is the p-th row of M.
Hence E(M) ≤ Σ_p F(r_p).

### Lemma 3.2 (row inequality on Δ_5)
For every r ∈ Δ_5, F(r) ≤ F(u_*) − κ|r − u_*|², where F(u_*) = 8·5^{−5/6} = 40·5^{−11/6}.

**Proof (analytic, by hypercontractivity). This is the proof on which Theorem C rests.**
1. *The chain.* Let X = {1, …, 5} with the uniform measure π, and K(x, y) := π(y). K is irreducible, and reversible
   because π(x)K(x, y) = π(x)π(y). K is the projection g ↦ Eg, so (I − K)² = I − K and
   H_t = exp(−t(I − K)) = K + e^{−t}(I − K) (I7). Thus H_t g = T_ρ g := Eg + ρ(g − Eg) with ρ = e^{−t}.
2. *Normalisation.* D–SC Theorem A.1 with |X| = 5 gives α = (1 − 2/5)/log 4 = 3/(5 log 4) (verifier B). By
   Theorem 3.5(ii) with q = 12, ‖H_t‖_{2→12} ≤ 1 whenever e^{4αt} ≥ 11, i.e. t ≥ t_0 := (5/12)(log 4)(log 11).
3. *Duality.* H_t is self-adjoint on L²(π). By Hölder with exponents 12/11 and 12, for every g:
   ‖H_t g‖₂ = sup_{‖h‖₂ ≤ 1} ⟨g, H_t h⟩_π ≤ ‖g‖_{12/11} sup_{‖h‖₂ ≤ 1} ‖H_t h‖₁₂ ≤ ‖g‖_{12/11}
   for t ≥ t_0. Equivalently, ‖T_ρ g‖₂ ≤ ‖g‖_{12/11} for 0 ≤ ρ ≤ a := e^{−t_0} = 11^{−5 log 4/12}.
4. *ρ = 1/4 is admissible, strictly.* 1/4 < a ⟺ log 4 > (5/12)(log 4)(log 11) ⟺ log 11 < 12/5 ⟺ 11⁵ < e¹².
   Exact proof: e¹² = Σ_j 12^j/j! > Σ_{j=0}^{21} 12^j/j! = 161767.65… > 161051 = 11⁵, since every omitted term is
   positive and the partial sum is computed in exact rational arithmetic (verifier B; 22 terms is the minimum
   needed). The arb enclosure is a = 0.250304119353463942637… > 1/4, and the margin is
   12/5 − log 11 = 0.0021047272016294559… (verifier B).
5. *Identification.* Put g_j := r_j^{11/12}.
   - (3/2)S(r)² + Q(r)/2 = 40‖T_{1/4} g‖₂² (verifier B).
   - ‖g‖²_{12/11} = ((1/5)Σ r_j)^{11/6} = 5^{−11/6} (verifier B), and 40·5^{−11/6} = F(u_*).
6. *Decay.* ‖T_ρ g‖₂² = (Eg)² + ρ² Var_π g (verifier B). So
   F(r) = 40[(Eg)² + Var_π g/16] = 40[‖T_a g‖₂² − (a² − 1/16) Var_π g] ≤ F(u_*) − 40(a² − 1/16) Var_π g.
7. *Variance comparison.* By the mean value theorem, |s^{11/12} − t^{11/12}| ≥ (11/12)|s − t| for s, t ∈ [0, 1],
   including s = 0, because the derivative (11/12)ξ^{−1/12} ≥ 11/12 for ξ ∈ (0, 1]. Writing
   Var_π g = (1/50) Σ_{i,j} (g_i − g_j)² (verifier B), this gives Var_π g ≥ (121/144) Var_π r = (121/144)|r − u_*|²/5.
8. *Conclusion.* F(r) ≤ F(u_*) − 40·(121/720)(a² − 1/16)|r − u_*|² = F(u_*) − κ|r − u_*|². ∎

Only κ > 0 is used later. It follows from a > 1/4, i.e. from the exact inequality 11⁵ < e¹²; the decimal enclosures
of κ and C_12 are reported, not needed. The margin is small (12/5 − log 11 ≈ 0.0021), which is why it is certified
exactly.

**Supplementary rigorous interval check (independent of D–SC; not needed for Theorem C).** It shows the stronger
F(r) ≤ F(u_*) − c_row|r − u_*|² with c_row := 1/40 > κ = 0.00102… Let G(r) := F(r) + c_row|r − u_*|². G is
continuous on the compact set Δ_5, so it attains its maximum.
1. *No maximiser on the boundary.* Suppose r_j = 0 < r_i. For 0 < ε ≤ r_i/2, move ε from coordinate i to j, and put
   K_b := (11/12)(r_i/2)^{−1/12}.
   - By the mean value theorem, (r_i − ε)^{11/12} − r_i^{11/12} ≥ −K_b ε. So the change ΔS of S satisfies
     ΔS ≥ ε^{11/12} − K_b ε, which is > 0 for small ε.
   - S ≥ Σ_j r_j = 1, since t^{11/12} ≥ t on [0, 1]. With ΔS > 0 this gives (3/2)[(S + ΔS)² − S²] ≥ 3ΔS.
   - Q changes by ≥ −(11/6)ε, since the derivative of t^{11/6} is at most 11/6 on [0, 1].
   - |r − u_*|² changes by 2ε² − 2r_i ε ≥ −2ε.
   So G increases by at least 3(ε^{11/12} − K_b ε) − (11/12)ε − 2c_row ε > 0 for small ε.
2. *Interior maximisers take at most two values.* At an interior maximiser ∂G/∂r_j is the same for all j, and
   ∂G/∂r_j = ψ(r_j) − 2c_row/5 with ψ(t) := (11/4)S t^{−1/12} + (11/12)t^{5/6} + 2c_row t (verifier C). Since
   t^{13/12} ψ′(t) = −(11/48)S + (55/72)t^{11/12} + 2c_row t^{13/12} is strictly increasing in t > 0 (verifier C), ψ′
   changes sign at most once, from − to +. So ψ takes each value at most twice, the coordinates of r take at most
   two values, and up to permutation r lies on one of two families:
   - family 1: (x, y, y, y, y), y = (1 − x)/4, x ∈ [0, 1] (one coordinate against four);
   - family 2: (x, x, y, y, y), y = (1 − 2x)/3, x ∈ [0, 1/2] (two coordinates against three).
   The point u_* is x = 1/5 on both.
3. *Away from u_** (verifier C). On both families, outside |x − 1/5| < 1/25, an arb subdivision into 8000 pieces
   per family certifies G < F(u_*) on every piece. It uses a monotone enclosure, with a centred mean-value form on
   the 89 pieces of family 1 where the monotone enclosure is too coarse.
   - The certified piece slacks are lower bounds. The smallest is 3.68·10⁻⁶, on the family-1 piece near x = 0.257
     (6.34·10⁻⁴ on family 2).
   - The arb point values of the slack F(u_*) − G on family 1 are 3.84·10⁻⁴ at x = 6/25 (the cut),
     7.31·10⁻⁴ at x = 257/1000 and 1.80·10⁻² at x = 201/250; on family 2, 1.13·10⁻³ at x = 6/25 (verifier C).
   - So the certificate is tight but valid; interval overestimation is not a mathematical flaw.
4. *Near u_**. For |x − 1/5| ≤ 1/25, let h(x) := G(r(x)) − F(u_*) along each family. Then h(1/5) = 0 and
   h′(1/5) = 0 exactly (sympy; the distance term has value and slope 0 at 1/5). Also h″ < 0 is certified on 400 arb
   balls covering the interval; the largest upper bounds are −0.3401 and −1.3053. Taylor's theorem with the
   mean-value remainder gives h ≤ 0, with equality only at x = 1/5.
5. *Conclusion.* Items 1–4 give G ≤ F(u_*) on Δ_5. ∎

### Theorem 3.3 (Theorem C at k = 5)
For every M ∈ S_5,
  E(M) ≤ E(J) − κ‖M − J‖².
For every M ∈ M (doubly stochastic, where E(M) ≥ 8 > 0),
  U(M) ≤ U(J) − C_12‖M − J‖².
On row-stochastic M, E can vanish (for example when every row is (1, 0, 0, 0, 0)), and the proof uses U only on
doubly stochastic M. The arb enclosures at 256 bits (verifier B) are:
- a² − 1/16 = 1.5215216531312264531…·10⁻⁴;
- κ = 1.0228006668271022268…·10⁻³;
- E(J) = 10.461283888094644729…;
- C_12 = 5.8662053975483251108…·10⁻⁴ ∈ (5.866·10⁻⁴, 5.867·10⁻⁴).

*Proof.*
- By Lemma 3.1, Lemma 3.2 (analytic proof) and 5F(u_*) = 200·5^{−11/6} = E(J) (verifier B):
  E(M) ≤ Σ_p F(r_p) ≤ 5F(u_*) − κ Σ_p |r_p − u_*|² = E(J) − κ‖M − J‖².
- For M ∈ M we also have E(M) > 0 (Proposition B). So 1 − κ‖M − J‖²/E(J) ≥ E(M)/E(J) > 0, and log(1 − x) ≤ −x gives
  U(M) − U(J) = 6 log(E(M)/E(J)) ≤ −(6κ/E(J))‖M − J‖² = −C_12‖M − J‖². ∎

The supplementary interval check would allow c_row = 1/40 in place of κ. Theorem C uses only κ from the analytic
proof.

## 4. Audit at (k, d) = (5, 12): where KPW's hypothesis and Lemma 5 enter (acceptance item 4)

The rows are those of the accepted χ8 audit (r3 §4, LF line numbers), re-evaluated at (k, d) = (5, 12). **The audit
is at (5, 12) only.** Statements of KPW quantified over all k ≥ 3 are checked here only at k = 5.

| # | Place (layout line) | Role | Status at (5, 12) |
|---|---|---|---|
| A1–A2 | abstract l.23–27; Thm 1 l.105–107 | definition of k in the statement | not used; the mechanism is run at k = 5 directly |
| A3 | Prop 2(b), l.142 | hypothesis of the E(Y²) asymptotics | replaced by Proposition 5.1 |
| A4 | proof of Thm 1, l.168–178 | SSC conditions; lower bound via minimality of k | SSC hypotheses verified in §5.2; KPW's conclusion there, P(Y > 0 \| E) → 1 with E = {X_1 = 0} (l.170–171), is obtained from the contiguity conclusion of (I3) (§5.2); lower bound in §6 |
| A5 | §3 standing hypothesis, l.570 | invoked only at A6 and A7 | fails at (5, 12) (8 log 4 < 12); its consequences are audited in A6, A7 |
| A6 | l.982–983, "k² − 2k − d + 2 > 0" | H positive definite in (3.13)–(3.14) | (H1) = 25 − 10 − 12 + 2 = 5 > 0 |
| A7 | l.1004–1020, AN Theorem 7 ⇒ (3.15) | global decay for S_2 | **unavailable at d = 12**: AN Theorem 7 needs d < d_{k−1} = 8 log 4 = 11.09…, and AN (12) gives only d < 11.83…; replaced by Lemma A + Theorem C (A14). No claim is made that (3.15)-type decay of the relaxed φ_12 is false (§2.1) |
| A8 | Lemma 5, l.713–723; proof l.1035–1138 | relaxation behind (3.7), (3.9) | not used (A14) |
| A9 | Lemma 8, l.894–909; proof l.1253–1525 | saddle point near J | d enters only via ρ_KPW = √(dn)/(k(k−1)) = √(12n)/20, c_KPW = d/(2k²(k−1)²) = 3/200 and the two ε-conditions of §1 (I2). At l.1356, ε′ < 3/1600, where (3.20) holds for every constant ε′ > (38400/17)ε² (l.1296–1311), so ε² < 17/20480000. At l.1436–1452, Lemma 4's tail exponent cλ_min = 9/50 must exceed the damping coefficient (2400/17)ε², so ε² < 51/40000, which the first condition implies. Both are d-free (verifier A; verifier r2, M1) |
| A9′ | Lemma 9, proof l.1239–1252 | phase separation used by Lemma 8 | uses "(k − 1)² + (k − 1)² exceeds k², the total number of ordered pairs" (l.1251): at k = 5, 32 > 25 (verifier A); no d-dependence |
| A9″ | Lemma 6, l.787–803 | eigenvalue data used in KPW §3 | at k = 5, (J_5 − I_5)^{⊗2} + 16 I_25 has eigenvalues 17 (sixteen times), 12 (eight times) and 32 (once); smallest 12 = (k − 1)(k − 2) > 0 (verifier A, exact); no d-dependence |
| A10 | §2: Prop 2(a) l.122, Lemma 3, Lemma 4 | first moments, (1.1) | "Fix integers d, k ≥ 3"; no d-hypothesis. Lemma 4 (l.373–384, quoted in §1 (I2)) has no degree hypothesis; at l.534 it is applied with A = r²(11ᵀ + (k − 2)I_k), which is positive definite |
| A11 | (1.2)–(1.3), l.152–165 | SSC (c), (d) | needs (d−1)/(k−1)² = 11/16 < 1, i.e. (H1) |
| A12 | Thm 10, l.1536; proof l.1542–1621 | n ≢ 0 (mod k) | uses Prop 2(b) via (4.2) (l.1552–1554), the S_2 restriction (l.1610–1615, see A14), and l.1558–1559 (Prop 2, (1.2), (1.3)); the b_pqrs concentration (l.1616–1621) refers to Lemma 8 (A9) |
| A13 | l.1622–1623, 1643 | final extension; "Note that k ≥ 3" | uses Theorem 10 only; k = 5 ≥ 3 |
| **A14** | Lemma 5, (3.7), (3.8), (3.9), (3.15) | where the relaxed bound is used | Re-checked on the pinned layout for this file, by searching for "Lemma 5", "(3.7)", "(3.8)", "(3.9)" and "(3.15)"; this agrees with the χ8 audit (r3 row A14). They occur only at l.713–779, l.912, l.999–1033 (S_2) and l.1034–1138 (proof of Lemma 5); §4 (Theorem 10) has none; S_1 improves (3.9) through Lemma 8 and (3.10) (l.912); Theorem 10 reuses only the conclusion of the S_2 estimate (l.1610–1615). **So Lemma 5, (3.7), (3.9) and (3.15) enter only through the S_2 estimate and, through its conclusion, Theorem 10's restriction.** |
| **A15** | S_1: (3.10)–(3.14), l.911–996 | asymptotics near J | Uses (3.10), Lemma 8 (A9, A9′), Euler–Maclaurin, Lemma 6(b) eigenvalues, positive definiteness of H, which needs (H1) at l.982, and Lemma 4 at l.983 (quoted in §1 (I2); no degree hypothesis). **So at (5, 12) the S_1 asymptotics need only (H1) = 5 > 0 and the d-free choice of ε.** At (5, 12), H = (5/17)(J_4 + I_4)^{⊗2} has eigenvalues 125/17 (once), 25/17 (six times) and 5/17 (nine times), and det H = 5²⁴/17¹⁶ = k^{2k−2}((k²−2k−d+2)/(k²−2k+2))^{(k−1)²}, matching KPW (3.13) (verifier A, exact). |

**Conclusion.** At (5, 12), KPW §§2–4 go through after two changes:
- (H1) = 5 is used at A6 and A11;
- the S_2 estimate is replaced by Lemma A and Theorem C (§5.1).
Everything else in KPW §§2–4 is used only at (k, d) = (5, 12), where it holds by the rows above; no claim is made for
other (k, d).

## 5. Upper bound: G_{n,12} is a.a.s. 5-colourable

### Proposition 5.1 (KPW Proposition 2(b) at (k, d) = (5, 12))
For n divisible by 5,
  E(Y²) ∼ k^k (k−1)^{k(k−1)}/((k²−2k−d+2)^{(k−1)²/2}(2π(k−2))^{k−1}) · n^{−(k−1)} k^{2n} (1−1/k)^{dn}
        = 4²⁰/(5³(6π)⁴) · n^{−4} · 5^{2n} (4/5)^{12n} = (68719476736/(10125π⁴)) · n^{−4} · 5^{2n} (4/5)^{12n}
(verifier A).

*Proof.* Follow KPW's proof of Proposition 2(b) (§3) with E(Y²) = S_1 + S_2 (l.937–945).
- S_1 is the sum over M′ ∈ B_{k−1}(δ) ∩ (k/n)Z^{(k−1)²}, with δ := ε log n/((k−1)² n^{1/2}) = ε log n/(16 n^{1/2})
  (l.925–928).
  - By A15, (3.12)–(3.14) give S_1 ∼ the displayed right-hand side.
  - This uses (H1) = 5 > 0 for H positive definite, with det H = 5²⁴/17¹⁶ (KPW (3.13)).
- S_2 collects the remaining M ∈ M ∩ (5/n)Z^{5×5}. For each, M ∉ B_5(δ) (l.997–998), so ‖M − J‖² ≥ δ².
  - By Proposition B and Theorem C,
    |T(M)|/|P_{n,12}| ≤ P_12(n) e^{n U(M)} ≤ P_12(n) e^{n U(J)} e^{−C_12 n δ²} = P_12(n)·5^{2n}(4/5)^{12n}·
    e^{−C_12 ε² log² n/256}, since nδ² = ε² log² n/(k−1)⁴.
  - There are at most (n+1)^{25} terms. So S_2 ≤ (n+1)^{25} P_12(n)·5^{2n}(4/5)^{12n}·n^{−C_12 ε² (log n)/256}
    = 5^{2n}(4/5)^{12n} n^{−Θ(log n)}.
  - This is o(S_1), because S_1 = Θ(n^{−4}) 5^{2n}(4/5)^{12n} and C_12 > 0. Explicitly,
    S_2/S_1 = O(n^{242} exp(−C_12 ε² log² n/256)), since 25 + 25/2 + 401/2 + 4 = 242 (verifier A).
- Theorem C holds for every ε, so no coupling between ε and C_12 is needed. ∎

### 5.2 n ≡ 0 (mod 5): small subgraph conditioning at (k, d) = (5, 12)
Apply W99 Theorem 4.1 (I3) on P_{n,12} along n = 5t, indexed by t → ∞, with Y the number of balanced 5-colourings,
X_i the number of i-cycles, λ_i = 11^i/(2i) > 0 and δ_i = (−1)^i/4^{i−1} ≥ −1. Here δ_1 = −1 and |δ_i| ≤ 1/4 for
i ≥ 2.
- (a) holds by (I4), including EX_i → λ_i.
- (b) is KPW (1.1) (I1).
- (c) λ_iδ_i² = 8(11/16)^i/i, so Σ_i λ_iδ_i² = 8 log(16/5) < ∞. This is KPW (1.2),
  (k−1)² log((k−1)/√(k²−2k−d+2)) = 16 log(4/√5), at (5, 12) (verifier A).
- (d) By (I1) and Proposition 5.1, E(Y²)/(EY)² → (4/√5)^{16} = (16/5)^8 = exp(8 log(16/5)). This is KPW (1.3)
  (verifier A, exact symbolic identities).
- EY > 0, and EY grows exponentially, since k(1 − 1/k)^{d/2} = 5(4/5)⁶ = 4096/3125 > 1 (exact).

**Contiguity.** The only index with δ_i = −1 is i = 1, so Σ_{δ_i=−1} λ_i = λ_1 = 11/2 < ∞. Y is a non-negative
integer random variable with EY > 0, as W99's definition of G^{(Y)} requires. The contiguity conclusion of
Theorem 4.1 (I3) therefore gives P_{n,12}^{(Y)} ≈ Ĝ_n, where Ĝ_n is P_{n,12} conditioned on {X_1 = 0} (no loops).
- *No loops.* In P_{n,12}^{(Y)}, P(Y = 0) = E(Y·1{Y = 0})/EY = 0 for every n. Contiguity with A_n := {Y = 0} gives
  P_{Ĝ_n}(Y = 0) → 0, that is, P(Y = 0 | X_1 = 0) → 0. This is the conclusion P(Y > 0 | E) → 1, E = {X_1 = 0},
  that KPW draw at l.170–171.
- *Double edges.* P(Y = 0 | X_1 = X_2 = 0) ≤ P(Y = 0 | X_1 = 0)/P(X_2 = 0 | X_1 = 0) → 0, since
  P(X_2 = 0 | X_1 = 0) → e^{−121/4} > 0 by (I4).
- By (I4), G_{n,12} is P_{n,12} conditioned on Simple = {X_1 = X_2 = 0}. So G_{n,12} is a.a.s. 5-colourable along
  n ≡ 0 (mod 5).
- *Remark (not used).* A loop at v would require σ(v) ≠ σ(v); equivalently, KPW's enumeration (l.184–194) joins only
  points of different colour classes. So Y = 0 on every pairing with a loop, {Y > 0} ⊆ {X_1 = 0}, and
  P(Y > 0) = P(X_1 = 0)·P(Y > 0 | X_1 = 0) → e^{−11/2}. This equality rests on the loop support together with
  contiguity; it does not follow from (a)–(d) alone (I3).

### 5.3 n ≢ 0 (mod 5): residues r = 1, 2, 3, 4
KPW §4 sets k′ = 2k if dk is odd and k′ = k otherwise. Here dk = 60, so k′ = 5. Since d is even, dr is even for
every r, so all of r = 1, 2, 3, 4 occur, with ℓ = dr/2 = 6r ∈ {6, 12, 18, 24} (verifier A).

*Theorem 10 at (5, 12, 6r).* By audit row A12 (with A14), its proof needs only:
- Proposition 2(a) and (1.1), which hold for every d (A10);
- Proposition 2(b), which is Proposition 5.1;
- the S_2 restriction, which is the conclusion of Proposition 5.1's S_2 estimate;
- (1.2)–(1.3), see §5.2;
- the Lemma 8 concentration (A9).
So, for m ≡ 0 (mod 5), let Ω′_m be the set of structures (G′, L): G′ a simple 12-regular graph on a fixed m-set, and
L an ordered ℓ-tuple of edges of G′ whose 2ℓ endpoints induce a perfect matching in G′. If (G′, L) is uniform on
Ω′_m, then a.a.s. G′ has a 5-colouring in which every edge of L has end colours 1 and 2.

*Inherited sketched steps (disclosed).* KPW's proof of Theorem 10 is a sketch. Two of its steps are imported as KPW
state them; the marked-space transfer around them is derived below.
1. *Small subgraph conditioning on the marked space Ω_{n,d,ℓ}.* KPW assert that (1.1) holds with Y replaced by Ŷ
   (l.1551, l.1560–1593), together with (4.1) and (4.2), and conclude by "the argument in the last few sentences of
   the proof of Theorem 1" (l.1558–1559). Those sentences (l.168–173) draw the conditional conclusion
   P(Y > 0 | E) → 1 with E = {X_1 = 0}, and then remove double edges. On Ω_{n,d,ℓ} this is the contiguity argument
   of §5.2 applied to Ŷ; the overstrong first conclusion of (I3) is not used. Left implicit there, and supplied by
   the supporting derivation below: hypothesis (a) of (I3) on Ω_{n,d,ℓ}, and the passage from marked pairings to
   uniform marked simple structures.
2. *Edge-count concentration.* KPW: "We can easily bound the weight in F′ due to terms in which some b_pqrs is not
   dn/(k²(k − 1)²) ± O(n^{1/2} log n), and find an extra factor of O(n^{−Θ(log n)})" (l.1616–1621). The
   single-colouring analogue for b_ij is at l.1575–1584.
Neither step involves a degree threshold (audit rows A9 and A12).

*Supporting derivation for the marked-space transfer (this file's; not in KPW).* Fix r, ℓ = 6r and m ≡ 0 (mod 5),
and let Ω_{m,12,ℓ} be KPW's marked space (l.1542–1544): the uniform measure on pairs (P, L), with P ∈ P_{m,12} and L
an ordered ℓ-tuple of pairs of P, no two incident with the same vertex. Write X_i for the cycle counts of P, and B for
the event that some pair of P outside L joins two endpoint vertices of L (possibly the same vertex twice). Let
A := Simple ∩ B^c; on Simple, B^c says exactly that the L-edges induce a perfect matching in the simple graph of P.
1. *Cycle laws.* Let m > 4ℓ; this suffices, because the argument is used only as m → ∞. For every P, the number
   N_L(P) of admissible L then satisfies (dm/2 − 2ℓd)^ℓ ≤ N_L(P) ≤ (dm/2)^ℓ: when the j-th pair is chosen, the
   j − 1 earlier pairs meet at most 2(j − 1) vertices, which carry at most 2(j − 1)d pairs, and
   dm/2 − 2(j − 1)d ≥ dm/2 − 2ℓd > 0. So the law of P under Ω_{m,12,ℓ} has density
   N_L(P)/E N_L ∈ [(1 − 4ℓ/m)^ℓ, (1 − 4ℓ/m)^{−ℓ}]
   with respect to the uniform P_{m,12}. Hence, on Ω_{m,12,ℓ}, the X_i have the same joint Poisson limits (the total
   variation distance is at most (1 − 4ℓ/m)^{−ℓ} − 1 = O(1/m)), and EX_i → λ_i still holds. So hypothesis (a) of
   (I3) holds on Ω_{m,12,ℓ}.
2. *Extra pairs among the endpoints.* Each admissible L, an ordered ℓ-tuple of vertex-disjoint point pairs, has
   exactly (dm − 2ℓ − 1)!! completions to a pairing. So under Ω_{m,12,ℓ}, L is uniform and, given L, the other pairs
   form a uniform pairing of the remaining dm − 2ℓ points. The endpoint vertices of L carry at most 2ℓ(d − 1)
   further points, so the expected number of pairs outside L that join two endpoint vertices is at most
   C(2ℓ(d−1), 2)/(dm − 2ℓ − 1) = O(ℓ²d/m), and P(B) is at most this. With step 1 and P(X_1 = 0) → e^{−11/2},
   P(A | X_1 = 0) ≥ P(X_2 = 0 | X_1 = 0) − P(B)/P(X_1 = 0) → e^{−121/4} > 0.
3. *Exact uniformity.* On A, the map (P, L) ↦ (G′, L), with G′ the simple graph of P and L read as edges, is exactly
   (d!)^m-to-one onto Ω′_m. A pairing that projects to a given simple G′ is a choice, at each vertex, of a bijection
   between its d points and its d edges; the pairs of L are then determined by the edges of L. So, conditional on A,
   (G′, L) is uniform on Ω′_m.
4. *Transfer.* On A, Ŷ > 0 gives a 5-colouring of G′ in which every L-edge has end colours 1 and 2. Since
   A ⊆ Simple ⊆ {X_1 = 0},
     P(Ŷ = 0 | A) ≤ P(Ŷ = 0 | X_1 = 0)/P(A | X_1 = 0) → 0.
   Here P(Ŷ = 0 | X_1 = 0) → 0 is the contiguity argument of §5.2 for Ŷ on Ω_{m,12,ℓ}: hypothesis (a) holds by
   step 1, (b) is KPW's assertion for Ŷ (inherited step 1), (c) is unchanged, and (d) follows from (4.1), (4.2) and
   Proposition 5.1. Ŷ is a non-negative integer random variable with EŶ > 0, by (4.1).
Verifier r2 (M3) checks the finite statements of steps 1–3 exactly, by exhaustive enumeration on eight small
instances (m, d, ℓ): the bounds on N_L(P); |Ω| = (number of admissible L)·(dm − 2ℓ − 1)!!;
P(B) ≤ E[number of extra pairs] ≤ C(2ℓ(d−1), 2)/(dm − 2ℓ − 1); and the exactly (d!)^m-to-one map onto an
independently enumerated Ω′_m. The asymptotic statements are the hand arguments above.

*Reduction* (KPW l.1625–1643, with the conditioning made exact). Let n ≡ r (mod 5) with r ∈ {1, 2, 3, 4},
G = G_{n,12} on V, and fix vertices v_1, …, v_r. Let 𝒢_r be the event that the v_i are pairwise at distance ≥ 4 and
none lies in a triangle.
- **P(𝒢_r) → 1.** KPW l.1627–1628: the vertices are a.a.s. at distance at least 4. KPW l.1632–1633: a fixed vertex
  is a.a.s. in no cycle of length less than 4. In P_{n,12}, the expected numbers of paths of length ≤ 3 between two
  fixed vertices and of triangles through a fixed vertex are O(1/n), and P(Simple) is bounded below (I4).
- **Induced matching.** On 𝒢_r, the neighbourhoods N(v_i) are pairwise disjoint 12-sets (distance ≥ 3). There is
  no edge between different N(v_i) (distance ≥ 4), and each N(v_i) is independent (no triangle at v_i). So
  W := ∪_i N(v_i) is an independent 12r-set in G − {v_1, …, v_r}.
  - Delete v_1, …, v_r. Add a uniformly random perfect matching η on W, and order its 6r edges uniformly at random
    as L.
  - The result G′ is a simple 12-regular graph on V ∖ {v_i}, which has n − r ≡ 0 (mod 5) vertices.
  - Since W was independent, the only edges of G′ inside W are those of η. So the endpoints of L induce a perfect
    matching, and (G′, L) ∈ Ω′_{n−r}.
- **Exact conditional uniformity.** Consider the map (G, η, order) ↦ (G′, L) on {G ∈ 𝒢_r} × {perfect matchings η of
  W(G)} × {orderings of η}.
  - Every G ∈ 𝒢_r has exactly (12r − 1)!!·(6r)! choices of (η, order) (7484400 for r = 1; verifier A).
  - The map is exactly multinomial(12r; 12, …, 12)-to-one onto Ω′_{n−r}. These counts are 1, 2704156,
    3384731762521200 and 235809301462142612780721600 for r = 1, 2, 3, 4 (verifier A); compare KPW's count of ways to
    reinstate the edges at l.1638–1640.
  - *Preimages.* Given (G′, L) ∈ Ω′_{n−r} with endpoint set W, choose an ordered partition of W into
    (N_1, …, N_r) with |N_i| = 12. There are multinomial(12r; 12, …, 12) choices. Delete the edges of L and join v_i
    to N_i.
  - Each choice gives a simple 12-regular graph G on V. In it the N_i are disjoint and W spans no edge, because W
    induced only L in G′. So the v_i are pairwise at distance ≥ 4 and no v_i lies in a triangle, i.e. G ∈ 𝒢_r.
    The pair (η, order) is recovered from L.
  - Distinct choices give distinct G, since N(v_i) = N_i. Every preimage arises this way.
  - Hence, conditional on 𝒢_r, (G′, L) is exactly uniform on Ω′_{n−r}.
- **Colouring (checked at k = 5).** Colour G′ by Theorem 10 with the five colours {1, …, 5}, and keep these colours on
  V ∖ {v_i}. Give every v_i colour 3, which exists because k = 5 ≥ 3.
  - Each neighbour of v_i lies in N_i ⊆ W and is an endpoint of an L-edge, so it has colour 1 or 2.
  - The v_i are pairwise non-adjacent (distance ≥ 4).
  - Every edge of G avoiding the v_i is an edge of G′, because G′ = (G − {v_i}) + η.
  So this is a proper 5-colouring of G.
- **A.a.s. transfer.** P(G_{n,12} is not 5-colourable) ≤ P(𝒢_r^c) + P_{Ω′_{n−r}}(no 5-colouring with every L-edge
  coloured {1, 2}) → 0.

Together with §5.2, χ(G_{n,12}) ≤ 5 a.a.s. as n → ∞.

## 6. Lower bound: G_{n,12} is a.a.s. not 4-colourable (acceptance item 7)

### 6.1 Molloy–Reed (published route)
By the Molloy–Reed criterion (I6) at q = 4 and d = 12: q(1 − 1/q)^{d/2} = 4·(3/4)⁶ = 729/1024 < 1 (exact;
verifier A). Hence χ(G_{n,12}) > 4 a.a.s.
- KPW's weaker formulation (l.175–176) gives the same, since (2q − 1) log q = 7 log 4 = 9.70… < 12 (verifier A).
- ACG Theorem 1.1 with d_4 = 10 ≤ 12 also gives χ > 4 (context).

### 6.2 Self-contained first-moment bound (cross-check)
Let Z_4 be the number of proper 4-colourings of P_{n,12}. Fix class proportions r = (r_1, …, r_4), with n r_i
non-negative integers and Σ r_i = 1.
- If at most one class is non-empty, no pair of points may be matched while every vertex has degree 12, so the
  number of proper colourings with these class sizes is 0. Otherwise 1 − Σ r_i² > 0.
- *Count and factorial bounds.* The exact count has the structure of KPW (3.4) with four colour classes in place of
  the 25 cells and the six pairs {i, j} (i ≠ j) in place of the 200 allowed pairs. Steps 1–8 of Lemma A apply
  verbatim. Before duality they give the exponent (d − 1)Σ r_i log r_i + (d/2) log d − Σ_{i<j} β_ij log β_ij, subject
  to Σ_{j≠i} β_ij = d r_i, with polynomial factor e⁵(12n + 1)²(6n + 1)^{13/2} (points e⁴(dn + 1)², pair tuples
  (dn/2 + 1)⁶, pairings e(dn/2 + 1)^{1/2}).
- *Weak duality.* Take multipliers μ_i = c_1 + log r_i on the non-empty classes, and w := e^{2c_1−1}. Then
  e^{μ_i + μ_j − 1} = w r_i r_j, and Σ_{i<j} r_i r_j = (1 − Σ r_i²)/2.
- *Optimising w.* The minimum over w > 0 (strictly convex) gives the exponent H(r) + (d/2) log(1 − Σ r_i²), where
  H(r) = −Σ r_i log r_i (verifier G).
- *Maximum over r.* Since H(r) ≤ log 4 and Σ r_i² ≥ 1/4, the exponent is at most log 4 + 6 log(3/4) =
  log(729/1024) < 0.
- *Conclusion.* There are at most (n + 1)³ class-size vectors, so E Z_4 ≤ (n + 1)³ e⁵(12n + 1)²(6n + 1)^{13/2}
  (729/1024)^n → 0. By (I4), P(G_{n,12} is 4-colourable) ≤ E Z_4/P(Simple) → 0.
- *Exact-count control (verifier G).* For 4 ≤ n ≤ 10 the exact E Z_4 (all class vectors, inclusion–exclusion matching
  counts) satisfies the bound; at n = 10, (1/n) log E Z_4 = −0.5789, against log(729/1024) = −0.3398.

**Proof of the Theorem.** Combine §5 (χ ≤ 5 a.a.s.) and §6 (χ ≥ 5 a.a.s.). ∎

## 7. Controls (contract "controls"; verifier D, E, F, G, S)

- **C1. The k = 4 constants of the accepted χ8 proof are reproduced by the same general-k code** (verifier D):
  - κ_8 and C_8 agree with χ8's values to within 10⁻⁷⁰; E(J) = 9/√2 and a = 7^{−(log 3)/2};
  - the counts and arithmetic at (4, 8): (H1) = 2, ratio 7/9, growth 81/64, Molloy–Reed 16/27, residue preimage
    counts 1, 12870, 9465511770, H eigenvalues 16/5, 4/5, 1/5 with det 4⁶5⁻⁹, polynomial exponents (17, 8, 145/2)
    and degree 199/2;
  - the hypercontractive condition e⁸ > 7⁴ (exact partial sum, 11 terms) and χ8's form 109/15 > 7.
- **C2. The route fails at d = 13; no d = 13 claim** (verifier D).
  - The condition ρ ≤ a is log(d − 1) ≤ 4 − 8/k = 12/5. At d = 13: e¹² < 12⁵ = 248832, by an exact rational upper
    bound for e¹² (partial sum to j = 39 plus a geometric tail, 162754.79…); the margin is 12/5 − log 12 = −0.0849…,
    and 12^{−5 log 4/12} < 1/4 (certain).
  - At k = 5 the route therefore reaches exactly d ≤ 12 (1 + e^{12/5} = 12.023…).
- **C3. Theorem C at explicit rational doubly stochastic 5×5 matrices** (consistency, not proof; verifier F), all
  certain: (J + I)/2; M_{3/4} := J/4 + 3I/4 (rows (4/5, 1/20, 1/20, 1/20, 1/20)); I; J_2/2 ⊕ J_3/3; 1 ⊕ J_4/4;
  J + (1/100)(I − J); and the circulant with first row (1/2, 1/4, 1/4, 0, 0). For example
  U((J + I)/2) − U(J) = −0.0472460… < −C_12‖M − J‖² = −0.0005866….
- **C4. Exact-count control at M = I** (verifier E). Overlap M = I forces the two colourings to coincide, so
  |T(I)|/|P_{n,12}| = EY exactly, and U(I) = log 5 + 6 log(4/5) is the first-moment exponent.
  - For n = 5t, t ≤ 20, EY was computed exactly (inclusion–exclusion over intra-class pairs). The rate
    (1/n) log EY stays below U(I) + (1/n) log P_12(n); the gap U(I) − rate is positive and strictly decreasing
    (0.0831 at n = 100), with n·gap/log n = 1.80, consistent with the n^{−2} prefactor (C1 = 100√5/(9π²)).
  - The same code at k = 4, n = 120 reproduces χ8's independently computed rate 0.18083321333111818.
- **C5. First-moment exact control** for 4 ≤ n ≤ 10 (verifier G; §6.2).
- **C6. Float sanity (not evidence; verifier S).**
  - max (E(M) − E(J))/‖M − J‖² is −0.0939 over 3000 random 5×5 doubly stochastic M, and −0.1765 over row-stochastic
    M; both are ≤ −κ.
  - U − Ψ_12 ≥ 3.7·10⁻⁴ over 200 random doubly stochastic M (weak duality), and is 0 at J (3.6·10⁻¹⁵).
- **C7. Exploration (floats, not evidence; `explore/explore_k5.json`).**
  - The minimum of (F(u_*) − F)/|r − u_*|² on Δ_5 is about 0.0644, at (0.804, 0.049, 0.049, 0.049, 0.049); the
    local coefficient at u_* is 0.2497. Both are far above κ ≈ 0.00102 and above c_row = 1/40.
  - KPW's relaxed φ_12 appears to be maximised at J over 5×5 doubly stochastic matrices (§2.1).

## 8. Verification record

`code/verify_chi12.py` (SHA-256 aa326a1f54ee15f38138684392d9ae2a50ed98e4662be8a4db179b61be6fbaa1) →
`evidence/verify_chi12.json` (595b7389559bc4a52863061debaea0e8eca35ff859630ce7229a11456f1b0118) and
`evidence/verify_chi12.stdout.txt` (16fc8a7915f6583d8fd2a8c59bf5b0bd7c869010e5af3344946303fcd831d2ed).

The run of 09:39:10–09:39:37 PDT returned all_required_true = true. Its layers are:
- exact rationals and big integers;
- sympy symbolic identities;
- python-flint arb at 256 bits, where a comparison counts only when certain.

The script is general-k and self-contained: it reads nothing from other lanes, and the χ8 comparison values are
copied into it as constants. Section S is floats and is not evidence. Its sections:
- A: arithmetic at (5, 12) (KPW, SSC, residues, Molloy–Reed, Lemmas 6, 8, 9, the S_1 Hessian, Proposition 2
  constants, P(n) and the degree);
- B: Lemma A, Proposition B and Theorem C identities at k = 5, the exact proof of 11⁵ < e¹², and the arb constants;
- C: the supplementary interval check;
- D: controls at (4, 8) and (5, 13), B ⊗ B, and the GSVY identification;
- E: the exact-count control at M = I;
- F: Theorem C at explicit test matrices;
- G: the self-contained first moment.

**r2 addition.** `code/verify_chi12_r2.py` (SHA-256 0eca7bc546947fa49eb9c5eaa035401187dac51bf5812ebbd9bb454d513d6086)
→ `evidence/verify_chi12_r2.json` (19e12327af3af6f70496c2d9950e833a740c181887248fd47e36e2acd8b6990f) and
`evidence/verify_chi12_r2.stdout.txt` (4679c1191154e224d5683b3fdae63dd778bdd68ae0540620e0587a9de2d080ae). The run of
10:15:59–10:16:13 PDT returned all_required_true = true. It uses exact integers, rationals and sympy only, and it is
a new file: `code/verify_chi12.py` and its outputs are unchanged. Its sections:
- M1: Lemma 8's two ε-conditions (c_KPW = 3/200; the spectrum of B by exact ranks; cλ_min = 9/50; D_1 = 38400/17;
  D_2 = 2400/17; ε² < 17/20480000 and ε² < 51/40000, both d-free);
- L67: Lemma 6(a), (b) and Lemma 7(a)–(c) at k = 5, for a generic A with zero row and column sums;
- M4: the formula for EX_i against exhaustive enumeration (eleven (n, d), i ≤ 4) and its limit;
- M3: the finite statements of the marked-space derivation (§5.3) on eight small instances.

The float exploration `explore/explore_k5.py` → `explore/explore_k5.json`
(d7c26de9377959b6a0ae531f113ca0078f4b03a82b1628f14e536f023606fa92) is not evidence and is used by no proof.

Lemma A, Lemma 3.1, the analytic proof of Lemma 3.2, Theorem C, the audit and §§5–6 are hand arguments; the script
certifies their numerical and symbolic ingredients. The supplementary interval check of Lemma 3.2 is computer-assisted
and not needed for Theorem C.

## 9. Scope, reliance, prior work, priority

- *Reliance.* The proof imports:
  - KPW §§2–4, including Theorem 10, whose proof KPW only sketch, all used only at (k, d) = (5, 12);
  - W99 Theorem 4.1 (its contiguity conclusion only; see (I3)) and Theorem 2.6;
  - the Molloy–Reed criterion, which §6.2 re-derives in a self-contained way;
  - in the analytic proof of Lemma 3.2 only, D–SC Theorems A.1 and 3.5(ii). The supplementary interval check avoids
    D–SC.
  The audit (§4) shows that at (5, 12) only (H1) and the S_2 estimate carry the d-dependence. The S_2 estimate is
  re-proved here.
  - KPW's proof of Theorem 10 is a sketch. Two of its steps are imported exactly as sketched there (§5.3, "Inherited
    sketched steps"): small subgraph conditioning on the marked space, and the edge-count concentration. Neither
    involves a degree threshold. The marked-space transfer around them (hypothesis (a) on the marked space and the
    passage to uniform simple structures) is derived in §5.3.
- *Prior work, stated explicitly.*
  - Published: KPW's framework; AN's balanced second moment and display (12); NPG Theorems 1.2 and 3.1 (d < 11.83 at
    k = 5, random lifts of loopless graphs); D–SC's complete-graph log-Sobolev constant and Gross's
    hypercontractivity (D–SC Theorem 3.5); GSV and GSVY's Φ reformulation and the maximum-entropy duality.
  - The accepted χ8 proof (same mechanism at k = 4) is this route's immediate precursor; this file adds the
    concrete verification at (5, 12).
- *Priority.* Priority and significance are shared with χ8; no separate novelty claim is made. The parent's χ8
  priority audit (`institute/runs/six-lane-2026-10-16/review/chi8-priority-audit.md`) found no source stating
  χ(G_{n,12}) = 5 for the uniform model. A search miss is not novelty.
- *Significance* is separate from correctness and is not assessed here. If correct, this closes KPW's {5, 6} window at
  d = 12 for the uniform model. At k = 5 the route needs log(d − 1) ≤ 12/5, so d = 12 is its last degree; for k ≥ 6
  the route's reach 1 + e^{4−8/k} is below KPW's 2(k − 1) log(k − 1) ([INFERENCE] from the χ8 lane's exploratory
  general-k lead, not checked here). The float observation of §2.1 (J appears to maximise KPW's relaxed φ_12) means
  that at (5, 12), unlike at (4, 8), the per-cell constraints are not shown to be needed.

## 10. Contract acceptance map (phys-2-random12reg-colour-contract.json)

| Item | Where |
|---|---|
| (1) imports with exact hypotheses verified at (5, 12): KPW §§2–4 and Theorem 10, W99 Theorem 4.1, Molloy–Reed or a first moment, D–SC Theorems A.1 and 3.5(ii) | §1 (I1)–(I8) (W99 Theorem 4.1: contiguity conclusion only, (I3)), audit §4, §6 |
| (2) Lemma A at k = 5, finite n, every factorial bound, explicit polynomial factor, empty cells | §2, Lemma A, items 1–9; Proposition B |
| (3) k = 5 row reduction; analytic row inequality on Δ_5; log 11 < 12/5 and a > 1/4 by exact rationals; constants exact or arb | §3: Lemma 3.1; Lemma 3.2 analytic proof, step 4; verifier B (and supplementary check, verifier C) |
| (4) KPW audit at (5, 12): (H1) = 5, Lemma 9 (32 > 25), Lemma 8 constants, S_1 Hessian exactly | §4 rows A6, A9, A9′, A9″, A10, A14, A15 and §1 (I2) (both Lemma 8 ε-conditions; Lemma 4 quoted); verifier A; verifier r2 (M1, L67) |
| (5) small subgraph conditioning at (5, 12): ratio 11/16, Σλδ² explicit | §5.2 (contiguity conclusion of (I3); EX_i → λ_i in (I4), verifier r2, M4) |
| (6) residues r = 1..4, ℓ = 6r, exact multinomial(12r; 12, …, 12)-to-one uniformity | §5.3, with the supporting derivation for the marked space (verifier r2, M3) |
| (7) χ > 4 a.a.s. (Molloy–Reed 729/1024 < 1) | §6.1; self-contained cross-check §6.2 |

## 11. Changes from r1

Apart from the title, supersession and status lines at the top of the file, r2 differs from r1 only as follows.

1. Codex hostile review of r1 (`institute/runs/six-lane-2026-10-16/review/chi12-codex-hostile-review-v1.note.md`),
   minor finding. W99 Theorem 4.1's first displayed conclusion, P(Y > 0) = exp(−Σ_{δ_i=−1} λ_i) + o(1), is overstrong
   under (a)–(d) alone (the Y + 1 counterexample). r1 used it in §5.2. r2 uses only W99's contiguity conclusion
   G^{(Y)} ≈ Ĝ, as the parent instructed:
   - §1 (I3): the conclusion is quoted in full, with W99's definitions of G^{(Y)} and of contiguity (l.1519–1548),
     the counterexample, and the statement that only the contiguity conclusion is used.
   - §5.2: P(Y = 0 | X_1 = 0) → 0 now follows from contiguity, because P(Y = 0) = 0 in G^{(Y)}. The loop argument is
     kept as a remark that gives P(Y > 0) → e^{−11/2}; it is not needed. The subsequence n = 5t is made explicit.
   - §5.3 (inherited step 1), §4 (row A4), §9 and §10, item (1): KPW's own conclusion at l.170–171 is the
     conditional P(Y > 0 | E) → 1, which is what the contiguity conclusion gives; on the marked space it is applied
     to Ŷ.
   No arithmetic changed. `code/verify_chi12.py` and its outputs are unchanged.
2. Claude complete review of r1 (`institute/runs/six-lane-2026-10-16/review/chi12-claude-complete-review-v1.note.md`),
   m1. §1 (I2) and §4 (row A9) now audit KPW Lemma 8's second ε-condition (l.1436–1452): the tail exponent
   cλ_min = d(k−2)/(2k²(k−1)) = 9/50 against the damping coefficient (2400/17)ε² from Lemma 7(b). This gives the
   d-free condition ε² < (k−2)(k²−2k+2)/(k⁴(k−1)³) = 51/40000, which r1's ε² < 17/20480000 implies.
3. Claude m2. §1 (I2) and row A9: because I in (3.20) carries the factor n^{−k²/2}, (3.20) with a constant K holds
   for every constant ε′ > (38400/17)ε², strictly; r1's "ε′ ≤ (38400/17)ε²" is corrected. The condition at l.1356 and
   the resulting bound ε² < 17/20480000 are unchanged.
4. Claude m3. §5.3 gains a supporting derivation for the marked-space transfer, labelled as this file's, in four steps:
   cycle laws on the marked space, extra pairs among the endpoints, exact (d!)^m-to-one uniformity, and transfer. The
   disclosure of KPW's two sketched steps is kept; §9 states that the transfer around them is derived in §5.3.
5. Claude m4. §1 (I4) and §5.2 (a): hypothesis (a) of (I3) requires EX_i → λ_i. The exact formula for EX_i and its
   limit are stated.
6. Claude m5. §1 (I2) quotes KPW Lemma 4 (l.373–384) and confirms that it has no degree hypothesis; rows A10 and A15
   refer to it, with its uses at l.534, l.983 and l.1436. Row A14's list of occurrences of Lemma 5, (3.7), (3.8),
   (3.9) and (3.15) was re-checked on the pinned layout for this file.

Claude m6 asked for no change: the sketched Theorem 10 steps were already disclosed. `code/verify_chi12.py` and its
outputs are unchanged throughout. The new arithmetic of items 2–5 is checked exactly by the new
`code/verify_chi12_r2.py` (§8): M1 and L67 for items 2 and 3, M3 for item 4 and M4 for item 5. For item 6, M1 also
checks the spectrum of B, whose smallest eigenvalue 12 > 0 is what Lemma 4 needs at l.1436.

**r2 → r3** (from the Codex delta review of r2,
`institute/runs/six-lane-2026-10-16/review/chi12-r2-delta-codex-review-v1.note.md`; apart from the title,
supersession and status lines at the top of the file, nothing else changed):
7. §1 (I4), the explanation of the formula for EX_i. r2's statement that [n]_i/(2i) counts cyclic vertex sequences
   up to rotation and reflection fails for i = 1, 2 (for i = 1 it gives n/2). r3 counts oriented descriptions,
   including the ordered point choices, and divides the complete count by 2i, which is valid for every fixed
   i ≥ 1. The formula itself is unchanged.
8. §5.3, supporting derivation, step 1. The bounds on N_L(P) and the density and total-variation claims are
   qualified by m > 4ℓ. Read literally for all m, the lower bound fails (m = 10, d = 12, ℓ = 6); the argument is
   used only as m → ∞.
No verifier changed: `code/verify_chi12.py`, `code/verify_chi12_r2.py` and their outputs are unchanged.
