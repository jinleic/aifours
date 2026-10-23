# FROZEN r2 — candidate proof: the random 8-regular graph has chromatic number 4 a.a.s.

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the
file (README §1, evidence/LOG.md, evidence/SHA256SUMS.txt). r2 supersedes r1 (`review/PROOF_CHI8.r1.md`, SHA-256
7ed7f8c865468326b307b2ce8fd93048cc5ceed807eb98503e7b1c32248a4c8a), which is kept unchanged. §11 lists every change.

**Status.** CANDIDATE PROOF, worker-written. r2 itself has not been reviewed.
- Reviews of r1 (parent-held, under `institute/runs/six-lane-2026-10-16/review/`):
  - Codex CLI hostile review, `chi8-codex-hostile-review-v1.note.md`: ACCEPT. No fatal or major finding; no proof
    fix requested. One minor source remark: KPW's sentence at l.1251 is false at k = 3 and true at k = 4 (applied in
    §1 and §4).
  - Claude CLI complete review, first run: timed out with no verdict. Second run,
    `chi8-claude-complete-review-v2.note.md`: ACCEPT-WITH-FIXES, with seven editorial minors and no fatal, major or
    gap finding. All seven are applied (§11, items 7–13).
  - Parent priority and method audit, `chi8-priority-audit.md` (recorded 2026-10-17 08:22:54 PDT). It identifies
    the closed form of Lemma A with Galanis–Štefankovič–Vigoda(–Yang)'s Φ formulation and the counterpoint in
    Achlioptas–Moore §6 (applied in §§2.1, 2.2 and 9).
- Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-random8reg-colour-contract-r2.json` (SHA-256
  dc451d82e266db8e6b9f166bdc1e7a647570dfa47f12a1ec2c2b864d1d6d46aa). Its acceptance items (1)–(7) are mapped in §10.
- The route (exact-exponent weak duality with multipliers μ_u = c_0 + (7/8) ln m_u and exponent e^{μ_u+μ_v−1}, then
  complete-graph hypercontractivity) was proposed by the parent orchestrator. An exploratory pilot is
  `physics/evidence/six-lane-20261016/random7reg-colour/review/D8_PILOT.md` (read-only prior input); it uses a
  differently scaled multiplier convention, related to μ in Proposition B's convention note.
- No novelty or priority claim (§9). The entropy duality of Lemma A is standard, and its closed form is GSVY's Φ_1
  (§2.1).

## Theorem

Let G_{n,8} be the uniformly random 8-regular simple graph on n vertices (dn = 8n is even for every n). Then
P(χ(G_{n,8}) = 4) → 1 as n → ∞.

**Context (cited, not used).**
- KPW Theorem 1 at d = 8 gives χ ∈ {4, 5} a.a.s. *Convention:* KPW Theorem 1 (l.105–107) and their abstract
  (l.23–27) take k to be the smallest integer with d < 2(k − 1) log(k − 1) and conclude χ ∈ {k − 1, k}. At d = 8 this
  gives k = 5, since 6 log 3 = 6.59… < 8 < 8 log 4 = 11.09…. Their exact-value clause d > (2k − 3) log(k − 1) =
  7 log 4 = 9.70… fails. In the shifted convention k′ = k − 1 (smallest k′ with d < 2k′ log k′, as in NPG
  Corollary 1.4) one has k′ = 4 and χ ∈ {k′, k′ + 1}. The window is {4, 5} either way.
- The Achlioptas–Moore table gives {4, 5, 6}.
- ACG Table 1 has d_{4,smm} = 6 and d_4 = 10.
- Achlioptas–Naor display (12) and Nir–Pérez-Giménez Theorem 1.2 reach only d < (27/4) log 3 = 7.4156…, the latter
  for random lifts of loopless graphs.
- The accepted χ7 proof (`random7reg-colour/review/PROOF_CHI7.r2.md`) stops below d = 8. KPW's relaxed exponent φ_8
  is not maximised at J (its control C2).
- GSV (J. ACM 2015) and GSVY (SIAM J. Comput. 2016) introduced the ℓ_{d/(d−1)} reformulation Φ of the pairing-model
  moment exponents. U(M) below is GSVY's Φ_1 for the paired interaction B ⊗ B, evaluated at M^{7/8} (§2.1).
- AM04 §6 asserts that the Erdős–Rényi relaxation of the regular-graph second-moment exponent is tight. That holds
  only for overlaps that are constant on their support; at (J + I)/2 the relaxation is strictly lossy (§2.2).

**Proof outline.**
- **Upper bound (§§2–5).** KPW's balanced-colouring second moment plus small subgraph conditioning, at k = 4 colours
  and d = 8. KPW's hypothesis d < 2(k−1) log(k−1) fails here. The audit (§4) shows it enters KPW §§2–4 only
  through:
  - (H1) k² − 2k − d + 2 > 0, here 2 > 0, which is all the S_1 asymptotics need;
  - the S_2 estimate, i.e. Lemma 5 → (3.7) → (3.9) combined with AN's bound (3.15).
  At d = 8 KPW's S_2 estimate is unavailable. It is replaced by:
  - Lemma A (§2): KPW's exact count (3.4), Stirling bounds and pointwise weak duality, with an explicit polynomial
    factor and empty cells handled;
  - Theorem C (§3): global quadratic decay of the resulting closed-form bound U(M) = −10 log 2 + 4 log E(M). Its
    proof is a row reduction plus a per-row inequality, and the per-row inequality gets two independent proofs.
- **Every n (§5.3).** KPW Theorem 10, with r ∈ {1, 2, 3} deleted vertices and ℓ = 4r distinguished edges whose
  endpoints induce a perfect matching. Conditional uniformity is exact.
- **Lower bound (§6).** Molloy–Reed, plus a self-contained weak-duality first moment (§6.2).

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
  - **NPG**: Nir, Pérez-Giménez, arXiv:2109.13347v1. PDF 09161e92…5893; layout c4bd2801…c5083.
  - **AM04**: Achlioptas, Moore, cond-mat/0407278v1. PDF 80ac409d…6327; layout
    4c5714e331313c8806981419c8d17b3cf564c99b793da491ccfbfc817ee91a02.
- **Pinned in this lane** (`sources/`, fetched 2026-10-17 08:35:43–08:39:33 PDT):
  - **GSV**: Galanis, Štefankovič, Vigoda, *Inapproximability for antiferromagnetic spin systems in the tree
    non-uniqueness region*, arXiv:1305.2902v3 (J. ACM 62(6), 2015). PDF
    1539a5ec1d0e76f724691bb6680c044f2019414b23ebcd92f1bc955883a9a366; layout
    c24b88364b56b79dec2b88845d27f218ee03481c323b2a88e77bb8210092a6c5.
  - **GSVY**: Galanis, Štefankovič, Vigoda, Yang, *Ferromagnetic Potts model: refined #BIS-hardness and related
    results*, arXiv:1311.4839v3 (SIAM J. Comput., 2016). PDF
    545891749f573b925c348dfae11a88155bc4ff7f12d398ec1af8353d883f352a; layout
    6d2b5a7eb82808e2f602374bcaf6c879a3ef9988984295180ba9ef451e97664a.
  - **CLMS**: Coja-Oghlan, Loick, Mezei, Sorkin, *The Ising antiferromagnet and max cut on random regular graphs*,
    arXiv:2009.10483v2. PDF a8788f83e145ceb8c3b331bfa8c6185505634e4f4c29d00707907842e0f47dd8; layout
    a6a30f2abb94c834211d71c2b4af1ee4a905f7356d4e759ded2d5039a2b5ff9e.
- log is the natural logarithm.
- **Colours and cells.** k = 4, d = 8. Cells are u = (p, q) ∈ [4]². A colour count is a 4×4 doubly stochastic
  matrix M = (m_u), as in KPW §3, so Σ_u m_u = 4. M is the set of such matrices, and S_4 the set of 4×4
  row-stochastic matrices. J_4 is the all-ones matrix and J := (1/4)J_4; KPW's (1/k)J_k is J.
- **Allowed pairs.** u = (p, q) and v = (r, s) are allowed, u ~ v, iff p ≠ r and q ≠ s. The allowed pairs form the
  graph K_4 × K_4, with 72 unordered pairs (KPW's index set p < r, q ≠ s).
- **Norms and the simplex.** ‖M − J‖² := Σ_u (m_u − 1/4)². Δ_4 is the probability simplex in R⁴,
  u_* := (1/4, 1/4, 1/4, 1/4) is the uniform row, and |r − u_*|² := Σ_j (r_j − 1/4)².
- **Main functions.**
  - f_u := m_u^{7/8}, with 0^{7/8} = 0.
  - E(M) := Σ_{unordered allowed {u,v}} f_u f_v.
  - U(M) := −10 log 2 + 4 log E(M). The letter U is used only for this function, never for the uniform row u_*.
- **Constants.**
  - a := 7^{−(log 3)/2};
  - κ := (441/128)(a² − 1/9);
  - C_8 := 4κ/E(J) = (49√2/32)(a² − 1/9).
- **Row functions.** For r ∈ Δ_4: S(r) := Σ_j r_j^{7/8}, Q(r) := Σ_j r_j^{7/4} and F(r) := S(r)² + Q(r)/2.
- **Other symbols kept distinct.**
  - supp M := {u : m_u > 0} is the support. S(r) is the row function. S_1 and S_2 are KPW's two parts of E(Y²).
  - c_0 is the additive constant in the multipliers μ_u = c_0 + (7/8) log m_u (Proposition B).
  - c_row := 1/40 is the constant of the supplementary interval check, and K_b is its boundary constant (§3).
  - c_KPW := d/(2k²(k−1)²) is the constant in KPW's Lemma 8.
  - c_1 is the multiplier constant in §6.2.
  - K(x, y) denotes only the Markov kernel of §3.
- **Conventions.** 0 log 0 = 0 and 0⁰ = 1.

## 1. Imports, with exact hypotheses checked at (k, d) = (4, 8)

- **(I1) KPW Proposition 2(a)** (l.122–140). Hypotheses: "Fix integers d, k ≥ 3"; Y is the number of balanced
  k-colourings of P_{n,d}, with n a multiple of k. At (4, 8): d = 8 ≥ 3 and k = 4 ≥ 3, and dn is always even.
  Conclusions:
  - EY ∼ k^{k/2}((k−1)/(2π(k−2)))^{(k−1)/2} n^{−(k−1)/2} k^n (1 − 1/k)^{dn/2}, which here is
    16·(3/(4π))^{3/2}·n^{−3/2}·4^n (3/4)^{4n};
  - (1.1): E(Y[X_1]_{p_1}…[X_j]_{p_j}) ∼ Π_m (λ_m(1+δ_m))^{p_m} EY, with λ_m = (d−1)^m/(2m) = 7^m/(2m) and
    δ_m = (−1)^m/(k−1)^{m−1} = (−1)^m/3^{m−1}.
- **(I2) KPW §3 machinery used:**
  - the count (3.1)–(3.4);
  - the Stirling estimate (3.5)–(3.6);
  - Lemmas 6, 7, 8 and 9;
  - the S_1 asymptotics (3.10)–(3.14), with Lemma 4.
  The audit (§4) is carried out at (k, d) = (4, 8) only; no statement is made for other k. At (4, 8), (3.13)–(3.14)
  use (H1), and the remaining hypotheses that occur are k = 4 and conditions on ε that do not depend on d.
  - Lemma 9's proof (l.1251) uses "(k − 1)² + (k − 1)² exceeds k²". This holds at k = 4 (18 > 16) but fails at
    k = 3 (8 < 9) (verifier G). Only k = 4 is used here.
  Two of the ε conditions:
  - Lemma 8's choice "ε′ < d/(16k²(k−1)²)" (l.1356). The ε′ of (3.20) (l.1296–1311) bounds the displayed exponent
    −nd(k−1)²(vecÃ)ᵀ(J_{k−1}+I_{k−1})^{⊗2}vecÃ/(2(k²−2k+2)) under |a_pq| < ε log n/n^{1/2}. Since the eigenvalues
    of (J_{k−1}+I_{k−1})^{⊗2} are at most k², ε′ ≤ d(k−1)⁴k²ε²/(2(k²−2k+2)), which is proportional to d·ε². So d
    cancels from the condition.
  - c_KPW = d/(2k²(k−1)²) = 1/36 > 0.
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
  G^{(Y)} ≈ Ĝ …". Only the first conclusion is used. W99's index k in (a)–(b) is not the number of colours.
- **(I4) Cycle counts**, W99 Theorem 2.6 (Bollobás; l.361–366). For fixed d, the cycle counts X_1, …, X_k of P_{n,d}
  are asymptotically independent Poisson with means (d−1)^i/(2i). So P(Simple) = P(X_1 = X_2 = 0) → e^{(1−d²)/4},
  which is e^{−63/4} at d = 8 (W99 (3), l.248). G_{n,d} is P_{n,d} conditioned on Simple, because each simple graph
  arises from exactly (d!)^n pairings.
- **(I5) KPW Theorem 10** (l.1536–1541): "Fix nonnegative integers d ≥ 3, k and ℓ such that d < 2(k − 1) log(k − 1).
  Consider the d-regular graphs with n vertices (n divisible by k and dn even) and a distinguished ordered set of ℓ
  edges whose endpoints induce a perfect matching (i.e. no two edges in the distinguished set are adjacent to the
  same edge or incident with the same vertex). Let G be chosen uniformly at random from such structures. Then G
  a.a.s. has a k-colouring in which all ℓ distinguished edges have end vertices coloured 1 and 2."
  - The hypothesis d < 2(k − 1) log(k − 1) fails at (4, 8).
  - Audit rows A12 and A14 show that its proof (l.1542–1621) uses the hypothesis only through:
    - Proposition 2(b), via (4.2);
    - the S_2 restriction at l.1610–1615;
    - "the argument in the last few sentences of the proof of Theorem 1" (l.1558–1559), which uses Proposition 2,
      (1.2) and (1.3).
  - Proposition 5.1 below supplies all of these at (4, 8). Here ℓ = 4r ∈ {4, 8, 12}.
- **(I6) Molloy–Reed criterion**, in the pinned sources:
  - KPW l.67–68: "For fixed d, Molloy and Reed [16] showed that if q(1 − 1/q)^{d/2} < 1 then χ(G_{n,d}) > q a.a.s."
  - KPW l.175–178: the weaker form "if d > (2q − 1) log q then χ(G_{n,d}) > q", with "(Their proof is reported in
    [20], Theorem 1.3.)"
  - W99 l.1102–1107: "… a.a.s. χ(G) ≥ 4 for G ∈ G_{n,d} when d ≥ 6."
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
    Corollary A.5 shows that the walk without holding, K(x, y) = 1/(|X| − 1) for x ≠ y, has a different constant;
    only Theorem A.1's chain is used.
- **(I8) Elementary facts.**
  - Stirling bounds: (m/e)^m ≤ m! ≤ e√(m+1)(m/e)^m for every integer m ≥ 0.
  - Multinomial bound: N!/Π_i N_i! ≤ Π_i (N/N_i)^{N_i} for N_i ≥ 0 with Σ N_i = N.
  - max_{x ≥ 0}(−x log x + θx) = e^{θ−1}, attained at x = e^{θ−1}; the function is concave.
  - Hölder's inequality, the Cauchy–Schwarz inequality and the mean value theorem.

## 2. Lemma A: exact count and pointwise weak duality

**The exact count** (KPW (3.2)–(3.4), l.597–645). Fix M ∈ M ∩ (4/n)Z^{4×4} and put n_u := m_u n/4. B(M, n) is the
set of tuples (b_e) of non-negative integers, indexed by the 72 unordered allowed pairs e = {u, v}, such that
Σ_{v ~ u} b_{uv} = d n_u for every cell u ((3.2)–(3.3)). Then
  |T(M)| = n!/(Π_u n_u!) · Π_u (d n_u)! · Σ_{b ∈ B(M,n)} Π_e 1/b_e!,   |P_{n,d}| = (dn)!/((dn/2)! 2^{dn/2}),
and E(Y²) = Σ_{M ∈ M ∩ (k/n)Z^{k×k}} |T(M)|/|P_{n,d}| (KPW (3.1)). T(M) is the set of triples (P, C_1, C_2): P a
pairing, and C_1, C_2 balanced colourings of P with colour count M.

### Lemma A
Let d ≥ 1, n ≥ 1 with 4 | n and dn even, and M ∈ M ∩ (4/n)Z^{4×4} with support supp M := {u : m_u > 0}. For every
μ ∈ R^{supp M},
  |T(M)|/|P_{n,d}| ≤ P_d(n)·exp(n·V_μ(M)),
where
  V_μ(M) := ((d−1)/4) Σ_u m_u log m_u + (1−d) log 4 + (d/2) log d + Σ_{e = {u,v} ⊆ supp M, u ~ v} e^{μ_u + μ_v − 1}
           − (d/4) Σ_{u ∈ supp M} μ_u m_u
and P_d(n) := e^{17}(dn + 1)^8 (dn/2 + 1)^{145/2}. P_d(n) depends on neither M nor μ.

*Proof.* Each bound is applied to the exact count.
1. *Colourings.* By the multinomial bound, n!/Π_u n_u! ≤ Π_{u ∈ supp M} (n/n_u)^{n_u} = exp(n H_4(M)), where
   H_4(M) := −Σ_u (m_u/4) log(m_u/4). Empty cells contribute 0! = 1 and 0⁰ = 1.
2. *Points of each cell.* For u ∈ supp M, (d n_u)! ≤ e√(dn_u + 1)(dn_u/e)^{dn_u} ≤ e√(dn + 1)(dn_u/e)^{dn_u}. For
   u ∉ supp M, (d n_u)! = 0! = 1 = (0/e)⁰. There are at most 16 cells, so
   Π_u (d n_u)! ≤ e^{16}(dn + 1)^8 Π_{u ∈ supp M} (dn_u/e)^{dn_u}.
3. *Edge factorials.* For every b ∈ B(M, n) and every e, 1/b_e! ≤ (e/b_e)^{b_e} (lower Stirling bound; b_e = 0 gives
   1 ≤ 1). Summing (3.3) over u gives Σ_e b_e = dn/2, so Π_e 1/b_e! ≤ e^{dn/2} exp(−Σ_e b_e log b_e).
4. *Number of tuples.* Each b_e lies in {0, …, dn/2}, so |B(M, n)| ≤ (dn/2 + 1)^{72}.
5. *Pairings.* 1/|P_{n,d}| = (dn/2)! 2^{dn/2}/(dn)! ≤ e√(dn/2 + 1)(dn/(2e))^{dn/2} 2^{dn/2}/(dn/e)^{dn}
   = e√(dn/2 + 1)·(dn/e)^{−dn/2}.
6. *Empty cells in B(M, n).* If u ∉ supp M then (3.3) forces b_e = 0 for every e ∋ u. Such edges contribute
   b_e log b_e = 0, so only edges e ⊆ supp M remain.
7. *Pointwise weak duality.* Fix b ∈ B(M, n) and write b_e = nβ_e. Then
   −Σ_e b_e log b_e = −n Σ_e β_e log β_e − (dn/2) log n.
   The constraints read Σ_{v ~ u} β_{uv} = d m_u/4 for u ∈ supp M. For any μ ∈ R^{supp M}, with all sums over
   e = {u, v} ⊆ supp M and u ∈ supp M,
     −Σ_e β_e log β_e = Σ_e [−β_e log β_e + β_e(μ_u + μ_v)] − Σ_u μ_u Σ_{v~u} β_{uv}
                      ≤ Σ_e e^{μ_u+μ_v−1} − (d/4) Σ_u μ_u m_u.
   The equality holds because each edge contributes β_e to both endpoint constraints. The inequality is (I8)
   applied to each term with θ = μ_u + μ_v. No strong duality and no exact inner optimum is needed.
8. *Collecting exponents.* Multiply items 1–5 and substitute item 7 for every b. Since Σ_u d n_u = dn and
   Σ_e b_e = dn/2, the factors (dn_u/e)^{dn_u}, e^{dn/2}, n^{−dn/2} and (dn/e)^{−dn/2} give exactly
     n[Σ_u (d m_u/4) log(d m_u/4) − (d/2) log d] + dn log n − dn + dn/2 − (dn/2) log n − (dn/2) log n + dn/2.
   The n log n terms and the linear terms cancel. Using Σ_u m_u = 4,
     H_4(M) + Σ_u (d m_u/4) log(d m_u/4) − (d/2) log d = ((d−1)/4) Σ_u m_u log m_u + (1−d) log 4 + (d/2) log d
   (verifier item B "Lemma A exponent").
9. *Polynomial factor.* The non-exponential factors are e^{16}(dn+1)^8, (dn/2+1)^{72} and e√(dn/2+1), whose product
   is P_d(n). ∎

### Proposition B (closed form at d = 8)
For every M ∈ M ∩ (4/n)Z^{4×4},
  |T(M)|/|P_{n,8}| ≤ P_8(n)·e^{n U(M)},   U(M) = −10 log 2 + 4 log E(M),   P_8(n) = e^{17}(8n+1)^8(4n+1)^{145/2}.
Moreover E(M) ≥ (8 + ‖M‖_F²)/2 ≥ 9/2 > 0 on M, and U(J) = 2 log 4 + 8 log(3/4) = 8 log 3 − 12 log 2, which is the
exponent of (EY)².

*Proof.*
- Take μ_u := c_0 + (7/8) log m_u for u ∈ supp M, with c_0 real.
- Since (d−1)/4 = (d/4)(7/8) = 7/4, the entropy terms cancel, and Σ_{u ∈ supp M} m_u = 4. Also
  Σ_{e ⊆ supp M} e^{2c_0−1}(m_u m_v)^{7/8} = e^{2c_0−1} E(M), where pairs touching an empty cell contribute 0 to E
  anyway. So V_μ(M) = −7 log 4 + 4 log 8 + e^{2c_0−1} E(M) − 8c_0.
- This is strictly convex in c_0 and minimal at e^{2c_0−1} = 4/E(M), with value −10 log 2 + 4 log E(M) (verifier
  items B "Prop B"). The choice requires E(M) > 0.
- *Convention note.* This is the only multiplier convention used in this proof. The pilot and D8_SCREEN write the
  same bound as U_λ = C_d + ((d−1)/4) Σ m log m − (d/4) Σ m_u λ_u + (1/4) Σ_e e^{λ_u+λ_v}, with
  C_d := (1 − d/2) log 4 + (d/2) log d − d/2 and λ_u = ln C + (7/8) ln m_u.
  - Under λ_u = μ_u + (ln 4 − 1)/2, i.e. ln C = c_0 + (ln 4 − 1)/2, U_λ equals V_μ term by term, using Σ m = 4
    (verifier K, symbolic for general d).
  - Hence both forms optimise to −10 log 2 + 4 log E(M).
- *Lower bound on E.* m^{7/8} ≥ m on [0, 1], so E(M) ≥ Σ_{allowed} m_u m_v. For doubly stochastic M this equals
  (8 + ‖M‖_F²)/2 (verifier item, a symbolic check on the generic doubly stochastic matrix). Since ‖M‖_F² ≥ 1,
  E(M) ≥ 9/2.
- *At J.* E(J) = 72·4^{−7/4} = 9/√2, so U(J) = −10 log 2 + 4 log(9/√2) = 2 log 4 + 8 log(3/4) (verifier B). By
  (I1) this is the exponent of (EY)² = Θ(n^{−3}) 4^{2n}(3/4)^{8n}. ∎

### 2.1 Relation to the Galanis–Štefankovič–Vigoda(–Yang) Φ formulation (precursors)

Nothing in Lemma A or Proposition B is a new entropy duality.
- *Same exponent.* In GSVY's notation (layout l.590–640), the second moment of the balanced-colouring count is the
  first moment of the paired-spin system with interaction matrix B ⊗ B, where B = J_4 − I_4 (their Remark 1,
  l.638–640). With γ := M/4, the exact exponent of |T(M)|/|P_{n,8}| at fixed M (the inner entropy optimum over b;
  D8_SCREEN §1, used here only as context) is GSVY's Ψ_1^{B⊗B}(γ) of (13)–(14). Their edge variables y and
  constraints Σ_{j,l} y_{ik,jl} = γ_ik ((11), l.590–598) correspond to (3.3) via ℓ_e = dk·y_e (verifier H, constant
  bookkeeping for general d, k).
- *Same closed form.* GSVY (15) (l.645–656) defines Φ_1(R) = (Δ/2) ln Σ_{i,j} B_ij R_i R_j − (Δ − 1) ln Σ_i
  R_i^{Δ/(Δ−1)}. For the paired interaction B ⊗ B and R := M^{7/8},
  - Σ_{u,v} (B ⊗ B)_{uv} R_u R_v = 2E(M);
  - Σ_u R_u^{8/7} = Σ_u m_u = 4;
  so Φ_1^{B⊗B}(M^{7/8}) = 4 log(2E(M)) − 7 log 4 = U(M) (verifier H).
  Their map (20) (l.690–692), α_i = R_i^{Δ/(Δ−1)}/Σ_i R_i^{Δ/(Δ−1)}, sends M^{7/8} to M/4 = γ. The multiplier choice
  μ_u = c_0 + (7/8) log m_u in Proposition B is exactly this map.
- *Bipartite analogue.* GSV (§3.2, l.566–570) has the bipartite analogue Φ(r, c). Its Lemma 4.3 (l.784–808) is the
  same maximum-entropy problem, with product-form optimiser x_ij = B_ij R_i C_j.

**What GSV and GSVY prove with Φ.**
- GSV Lemma 3.1 (l.577–579) and Theorem 4.1 (l.729–744), and GSVY Lemma 9 (l.688–700), relate Φ and Ψ_1 at
  critical points and give equality of global maxima. GSVY state that "Φ_1 is not a reparameterization of Ψ_1,
  however they do agree at the critical points" (l.677–678).
- They then bound the second moment by dropping the overlap-marginal constraints. GSVY: "Ignoring the two
  constraints in (23) can only increase the value of (22)" (l.744); the same step is GSV (13)–(14), l.618–623.
- The unconstrained maximum is then evaluated through induced matrix norms and Bennett's multiplicativity (GSVY
  (18)–(25), l.672–752; GSV (10) and (15)). That needs either GSV's bipartite bilinear form or a ferromagnetic
  B = B̂ᵀB̂ (GSVY (18)).
- Here B = J_4 − I_4 has eigenvalues 3, −1, −1, −1, so B ⊗ B has eigenvalues 9, −3 (six times) and 1 (nine times)
  (verifier H). B ⊗ B is not positive semidefinite, and GSVY (18) is unavailable.
- GSVY Remark 2 (l.764–775) shows that their Theorem 6 (Ψ_2 = 2Ψ_1 at dominant phases) fails for antiferromagnetic
  models with 0/1 interaction matrices whenever Ψ_1 < 0, e.g. 3-colourings of random 10-regular graphs. That
  obstruction does not arise here: the balanced 4-colouring first-moment exponent at d = 8 is
  log 4 + 4 log(3/4) = log(81/64) > 0.

**What distinguishes the present argument.** Two things, and neither is a new entropy duality.
1. Lemma A keeps the 16 per-cell constraints (3.3) at each fixed M, and applies weak duality pointwise with an
   explicit polynomial factor. KPW's Lemma 5 and AM04 §6 instead relax (3.3) to their sum, i.e. the Erdős–Rényi
   bound. CLMS (l.65–68) describe this as "the trick of bounding the second moment of random regular graphs by that
   of the Erdős-Rényi as applied in [1, 13]" (their [1] is AM04, [13] is Coja-Oghlan–Efthymiou–Hetterich). §2.2
   shows the relaxation is strictly lossy at the point where the χ7 route fails.
2. Theorem C bounds Φ_1^{B⊗B}(M^{7/8}) = U(M) on all row-stochastic M, a superset of the doubly stochastic overlaps.
   It keeps the overlap (balancedness) constraint on the rows, which GSV and GSVY drop. It also gives quantitative
   decay in ‖M − J‖² at every such M, which the S_2 estimate needs, rather than an equality of maxima. The row
   constraint enters through the row reduction (Lemma 3.1) and the row inequality (Lemma 3.2, which uses
   Σ_j r_j = 1). No claim is made that the overlap constraint is logically necessary for the inequality: the essential
   gain over AM04/KPW is item 1.

The pointwise inequality Ψ_1^{B⊗B}(γ) ≤ Φ_1^{B⊗B}(γ^{7/8}) was not found stated in the parts of GSV (§§2–4.1)
and GSVY (§§4–5) that were read. It is standard weak duality, and no claim is made for it.

*Float observation (not evidence, not a global-maximum proof, not used).* At (4, 8), 396 of 400 BFGS starts for the
unconstrained maximum of Φ_1^{B⊗B} over R ≥ 0 converge to R ∝ 1, with value U(J) (`explore/unconstrained_phi1.json`).
This is consistent with the overlap constraint being used by the proof method without being needed for the
inequality, but nothing is claimed either way about the true unconstrained maximum. GSVY's matrix-norm route to
that maximum is unavailable here, because B ⊗ B is not PSD.

### 2.2 The relaxation of AM04 §6 and KPW Lemma 5 is strictly lossy at (J + I)/2

**AM04's assertion.**
- AM04 §6 (layout l.404–455) holds the overlap α fixed and maximises over β. Here α_ij = a_ij/n, so for balanced
  colourings every row and column of α sums to 1/k (AM04 (6), l.316–318).
- The maximisation is under the single summed constraint (13) in place of the k² constraints (12) (l.406–419).
- The Lagrange condition gives β_ijkℓ = Cα_ijα_kℓ ((15), l.452), and C = d/p with p = 1 − 2/k + Σα² ((16),
  l.456–464).
- AM04 then assert (l.454–455): "Clearly, such β_ijkℓ also satisfy the original constraints (12), and therefore the
  upper bound we obtain from this relaxation is in fact tight."

**The assertion holds only for overlaps that are constant on their support.**
- For balanced α, Σ_{k≠i, ℓ≠j} α_kℓ = 1 − 2/k + α_ij.
- So the maximiser (16) has marginal Σ_{k≠i, ℓ≠j} β_ijkℓ = (d/p)α_ij(1 − 2/k + α_ij), and
  (d/p)α_ij(1 − 2/k + α_ij) − dα_ij = dα_ij(α_ij − Σα²)/p.
- Hence (12) holds iff α_ij = Σα² for every cell with α_ij > 0, i.e. iff all nonzero entries of α are equal. This
  is verified symbolically for a generic doubly stochastic M at k = 4 (verifier F).
- Doubly stochastic overlaps that are constant on their support satisfy it: J, permutation matrices, and block
  matrices such as J_2/2 ⊕ J_2/2. The verifier checks J and I as positive controls.

**Counterexample at M = (J + I)/2.**
- Here α = M/4 is 5/32 on the diagonal and 1/32 off it, so Σα² = 7/64 and p = 39/64.
- The relaxed maximiser has marginals 35/26 at diagonal cells and 17/78 at off-diagonal cells. Constraint (12)
  requires dα = 5/4 and 1/4 (exact; verifier F). The marginals still sum to d = 8, as (13) requires.
- The same happens at M_{2/3}: 99/62 against 3/2, and 25/186 against 1/6.

**The loss is strict.**
- The relaxed exponent at M is ln 4 + φ_8(M) (KPW (3.9)). The exact exponent satisfies Ψ_8(M) ≤ U(M) (Lemma A,
  Proposition B).
- At (J + I)/2, ln 4 + φ_8(M) − U(J) = φ_8(M) − φ_8(J) = +0.0074193… > 0, since 13³² > 2⁵⁶·3³²·5⁵.
- Meanwhile U(M) − U(J) = −0.0287642… < 0 (arb; verifier F, control C4).
- So Ψ_8((J + I)/2) < U(J) = ln 4 + φ_8(J) < ln 4 + φ_8((J + I)/2), and the relaxation overestimates the exponent
  there by more than 0.036 (verifier F).

**Scope.**
- This identifies one pointwise feasibility assertion, AM04 l.454–455. It does not show that any published
  colouring theorem is false.
- AM04 use the relaxed value only as an upper bound on E[X²] (l.474–514).
- KPW state and prove Lemma 5 as an inequality (l.713–723, l.1035–1138). It remains a valid upper bound and is
  simply not used here.
- AM04 §7 (l.530–534) says that their proof establishes E[X]²/E[X²] = Θ(E[Y]²/E[Y²]) for G_{n,d} and
  G(n, m = dn/2). [INFERENCE] The direction of that Θ statement that bounds E[X²] from below would need the tightness
  assertion. It is not used here.

## 3. Theorem C: global quadratic decay

### Lemma 3.1 (row reduction)
Let (f_pq) be any 4×4 array of non-negative reals, with row sums R_p, column sums C_q, total Σf and
E(f) := Σ_{unordered allowed} f_u f_v. Then
  2E(f) = (Σf)² − Σ_p R_p² − Σ_q C_q² + Σ f_pq²,
and
  E(f) ≤ Σ_p (R_p² + Q_p/2),   Q_p := Σ_q f_pq².

*Proof.* The first identity is inclusion–exclusion over the pairs with p = r or q = s (verifier item S3). For the
second, an exact identity (verifier item "row-reduction certificate") gives
  2Σ_p R_p² + Σ f² − 2E(f) = [Σ_q C_q² − (Σf)²/4] + (3/4)[4Σ_p R_p² − (Σ_p R_p)²].
Both brackets are ≥ 0 by Cauchy–Schwarz over the four columns and the four rows. ∎

If M ∈ S_4 and f = m^{7/8}, then row p contributes R_p² + Q_p/2 = F(r_p), where r_p is the p-th row of M. Hence
E(M) ≤ Σ_p F(r_p).

### Lemma 3.2 (row inequality)
For every r ∈ Δ_4, F(r) ≤ F(u_*) − κ|r − u_*|², where F(u_*) = 9/(4√2) = 18·4^{−7/4}.

**Proof (analytic, by hypercontractivity). This is the proof on which Theorem C rests.**
1. *The chain.* Let X = {1, 2, 3, 4} with the uniform measure π, and K(x, y) := π(y). K is irreducible, and
   reversible because π(x)K(x, y) = π(x)π(y). K is the projection g ↦ Eg, so (I − K)² = I − K and
   H_t = exp(−t(I − K)) = K + e^{−t}(I − K) (I7). Thus H_t g = T_ρ g := Eg + ρ(g − Eg) with ρ = e^{−t}.
2. *Normalisation.* D–SC Theorem A.1 with |X| = 4 gives α = (1 − 2/4)/log 3 = 1/(2 log 3) (verifier B, item D-SC).
   By Theorem 3.5(ii) with q = 8, ‖H_t‖_{2→8} ≤ 1 whenever e^{4αt} ≥ 7, i.e. t ≥ t_0 := (log 3)(log 7)/2.
3. *Duality.* H_t is self-adjoint on L²(π). By Hölder with exponents 8/7 and 8, for every g:
   ‖H_t g‖₂ = sup_{‖h‖₂ ≤ 1} ⟨g, H_t h⟩_π ≤ ‖g‖_{8/7} sup_{‖h‖₂ ≤ 1} ‖H_t h‖₈ ≤ ‖g‖_{8/7}
   for t ≥ t_0. Equivalently, ‖T_ρ g‖₂ ≤ ‖g‖_{8/7} for 0 ≤ ρ ≤ a := e^{−t_0} = 7^{−(log 3)/2}.
4. *ρ = 1/3 is admissible.* 1/3 ≤ a ⟺ log 3 ≥ (log 3)(log 7)/2 ⟺ log 7 ≤ 2 ⟺ 7 ≤ e². This holds because
   e² = Σ_j 2^j/j! > Σ_{j≤5} 2^j/j! = 109/15 > 7 (exact; verifier B). The enclosure is
   a = 0.343385896618341840676… > 1/3.
5. *Identification.* Put g_j := r_j^{7/8}.
   - S(r)² + Q(r)/2 = 18‖T_{1/3} g‖₂² (verifier S4).
   - ‖g‖²_{8/7} = ((1/4)Σ r_j)^{7/4} = 4^{−7/4} (verifier S5), and 18·4^{−7/4} = F(u_*).
6. *Decay.* ‖T_ρ g‖₂² = (Eg)² + ρ² Var_π g (verifier item). So
   F(r) = 18[(Eg)² + Var_π g/9] = 18[‖T_a g‖₂² − (a² − 1/9) Var_π g] ≤ F(u_*) − 18(a² − 1/9) Var_π g.
7. *Variance comparison.* By the mean value theorem, |s^{7/8} − t^{7/8}| ≥ (7/8)|s − t| for s, t ∈ [0, 1],
   including s = 0, because the derivative (7/8)ξ^{−1/8} ≥ 7/8 for ξ ∈ (0, 1]. Writing
   Var_π g = (1/32) Σ_{i,j} (g_i − g_j)², this gives Var_π g ≥ (49/64) Var_π r = (49/64)|r − u_*|²/4.
8. *Conclusion.* F(r) ≤ F(u_*) − 18·(49/256)(a² − 1/9)|r − u_*|² = F(u_*) − κ|r − u_*|². ∎

Only κ > 0 is used later. It follows from a > 1/3, i.e. from the exact inequality e² > 109/15 > 7; the decimal
enclosures of κ and C_8 are reported, not needed.

**Supplementary rigorous interval check (independent of D–SC; not needed for Theorem C).** It shows the stronger
F(r) ≤ F(u_*) − c_row|r − u_*|² with c_row := 1/40 > κ = 0.02343… Let G(r) := F(r) + c_row|r − u_*|². G is
continuous on the compact set Δ_4, so it attains its maximum.
1. *No maximiser on the boundary.* Suppose r_j = 0 < r_i. For 0 < ε ≤ r_i/2, move ε from coordinate i to j, and put
   K_b := (7/8)(r_i/2)^{−1/8}.
   - By the mean value theorem, (r_i − ε)^{7/8} − r_i^{7/8} ≥ −K_b ε. So the change ΔS of S satisfies
     ΔS ≥ ε^{7/8} − K_b ε, which is > 0 for small ε.
   - S ≥ Σ_j r_j = 1, since t^{7/8} ≥ t on [0, 1]. With ΔS > 0 this gives (S + ΔS)² − S² = 2SΔS + ΔS² ≥ 2ΔS.
   - Q changes by ≥ −(7/4)ε, since the derivative of t^{7/4} is at most 7/4 on [0, 1].
   - |r − u_*|² changes by 2ε² − 2r_i ε ≥ −2ε.
   So G increases by at least 2(ε^{7/8} − K_b ε) − (7/8)ε − 2c_row ε > 0 for small ε.
2. *Interior maximisers take at most two values.* At an interior maximiser ∂G/∂r_j is the same for all j, and
   ∂G/∂r_j = ψ(r_j) − c_row/2 with ψ(t) := (7/4)S t^{−1/8} + (7/8)t^{3/4} + 2c_row t. Since
   t^{9/8} ψ′(t) = −(7/32)S + (21/32)t^{7/8} + 2c_row t^{9/8} is strictly increasing in t > 0, ψ′ changes sign at most
   once, from − to +. So ψ takes each value at most twice, and up to permutation r lies on one of two families:
   - family 1: (x, y, y, y), y = (1 − x)/3, x ∈ [0, 1];
   - family 2: (x, x, y, y), y = 1/2 − x, x ∈ [0, 1/2].
   The point u_* is x = 1/4 on both.
3. *Away from u_** (verifier C). On both families, outside |x − 1/4| < 1/25, an arb subdivision into 8000 pieces
   per family certifies G < F(u_*) on every piece. It uses a monotone enclosure, with a centred mean-value form on
   the 113 pieces of family 1 where the monotone enclosure is too coarse.
   - The certified piece slacks are lower bounds, and they are dominated by enclosure overestimation. The smallest is
     1.83·10⁻⁶, on the family-1 piece near x = 0.310 (5.5·10⁻⁴ on family 2).
   - The arb point values of the slack F(u_*) − F − c_row|r − u_*|² on family 1 are 2.37·10⁻⁴ at x = 29/100 and
     4.93·10⁻⁴ at x = 31/100 (verifier K).
   - So the certificate is tight but valid. Interval overestimation is not a mathematical flaw.
4. *Near u_**. For |x − 1/4| ≤ 1/25, let h(x) := G(r(x)) − F(u_*) along each family. Then h(1/4) = 0 and h′(1/4) = 0
   exactly (sympy; the distance term has value and slope 0 at 1/4). Also h″ < 0 is certified on 400 arb balls
   covering the interval; the largest upper bounds are −0.2087 and −1.0331. Taylor's theorem with the mean-value
   remainder gives h ≤ 0, with equality only at x = 1/4.
5. *Conclusion.* Items 1–4 give G ≤ F(u_*) on Δ_4. ∎

### Theorem 3.3 (Theorem C)
For every M ∈ S_4,
  E(M) ≤ E(J) − κ‖M − J‖².
For every M ∈ M,
  U(M) ≤ U(J) − C_8‖M − J‖².
The arb enclosures at 256 bits (verifier B) are:
- a² − 1/9 = 0.006802762885271439260…;
- κ = 0.023437644003161755578…;
- C_8 = 0.014731481786375019801… ∈ (0.0147, 0.0148).

*Proof.*
- By Lemma 3.1, Lemma 3.2 (analytic proof) and 4F(u_*) = 9/√2 = E(J) (verifier B):
  E(M) ≤ Σ_p F(r_p) ≤ 4F(u_*) − κ Σ_p |r_p − u_*|² = E(J) − κ‖M − J‖².
- For M ∈ M we also have E(M) > 0 (Proposition B). So 1 − κ‖M − J‖²/E(J) ≥ E(M)/E(J) > 0, and log(1 − x) ≤ −x gives
  U(M) − U(J) = 4 log(E(M)/E(J)) ≤ −(4κ/E(J))‖M − J‖² = −C_8‖M − J‖². ∎

The supplementary interval check would allow c_row = 1/40 in place of κ. Theorem C uses only κ from the analytic
proof.

## 4. Audit: where KPW's hypothesis and Lemma 5 enter (acceptance item 4)

Rows A1–A13 are those of the accepted χ7 audit (`random7reg-colour/review/PROOF_CHI7.r2.md` §3, LF line numbers),
re-evaluated at (k, d) = (4, 8). Rows A9′, A14 and A15 are new. **The audit is at k = 4 only.** Statements of KPW
that are quantified over all k ≥ 3 are checked here only at k = 4; at least one of them fails at k = 3 (row A9′).

| # | Place (layout line) | Role | Status at (4, 8) |
|---|---|---|---|
| A1–A2 | abstract l.23–27; Thm 1 l.105–107 | definition of k in the statement | not used; the mechanism is run at k = 4 directly |
| A3 | Prop 2(b), l.142 | hypothesis of the E(Y²) asymptotics | replaced by Proposition 5.1 |
| A4 | proof of Thm 1, l.168–178 | SSC conditions; lower bound via minimality of k | SSC verified in §5.2; lower bound in §6 |
| A5 | §3 standing hypothesis, l.570 | invoked only at A6 and A7 | — |
| A6 | l.982–983, "k² − 2k − d + 2 > 0" | H positive definite in (3.13)–(3.14) | (H1) = 16 − 8 − 8 + 2 = 2 > 0 |
| A7 | l.1004–1020, AN Theorem 7 ⇒ (3.15) | global decay for S_2 | **false at d = 8** (control C2 of χ7 r2); replaced by Lemma A + Theorem C (A14) |
| A8 | Lemma 5, l.713–723; proof l.1035–1138 | relaxation behind (3.7), (3.9) | not used (A14) |
| A9 | Lemma 8, l.894–909; proof l.1253–1525 | saddle point near J | d enters only via ρ = √(dn)/(k(k−1)), c_KPW = d/(2k²(k−1)²) = 1/36 and "ε′ < d/(16k²(k−1)²)" (l.1356), with ε′ ∝ dε² (l.1306–1311); no d-hypothesis |
| A9′ | Lemma 9, proof l.1239–1252 | phase separation used by Lemma 8 | uses "(k − 1)² + (k − 1)² exceeds k², the total number of ordered pairs" (l.1251): true at k = 4 (18 > 16), false at k = 3 (8 < 9) (verifier G); no d-dependence; used here only at k = 4 |
| A10 | §2: Prop 2(a) l.122, Lemma 3, Lemma 4 | first moments, (1.1) | "Fix integers d, k ≥ 3"; no d-hypothesis |
| A11 | (1.2)–(1.3), l.152–165 | SSC (c), (d) | needs (d−1)/(k−1)² = 7/9 < 1, i.e. (H1) |
| A12 | Thm 10, l.1536; proof l.1542–1621 | n ≢ 0 (mod k) | uses Prop 2(b) via (4.2) (l.1552–1554), the S_2 restriction (l.1610–1615, see A14), and l.1558–1559 (Prop 2, (1.2), (1.3)); the b_pqrs concentration (l.1616–1621) refers to Lemma 8 (A9) |
| A13 | l.1622–1623, 1643 | final extension; "Note that k ≥ 3" | uses Theorem 10 only; k = 4 ≥ 3 |
| **A14** | Lemma 5, (3.7), (3.8), (3.9), (3.15) | where the relaxed bound is used | A grep of the KPW layout for "Lemma 5", "(3.7)", "(3.8)", "(3.9)" and "(3.15)" finds them only at: l.713–779 (statement, (3.7), definition (3.8) and derivation of (3.9)); l.912; l.999–1033 (S_2); l.1034–1138 (proof of Lemma 5). §4 (Theorem 10) has none. At l.912, Lemma 8 with (3.10) yields an asymptotic for M near J "which improves the bound already stated in (3.9)", so S_1 does not use (3.9). l.775–777: (3.9) "is a sufficient bound … since it will allow us to show that the sum in (3.1) receives a negligible contribution due to terms with M away from (1/k)J_k". l.1610–1615: Theorem 10 recalls "from the last lines of the proof of Proposition 2(b)" that only M with \|m_pq − 1/k\| < ε log n/n^{1/2} matter, i.e. it reuses the S_2 conclusion, not (3.9) directly. **So Lemma 5, (3.7), (3.9) and (3.15) enter only through the S_2 estimate and, through its conclusion, Theorem 10's restriction.** |
| **A15** | S_1: (3.10)–(3.14), l.911–996 | asymptotics near J | Uses (3.10), Lemma 8 (A9, A9′), Euler–Maclaurin, Lemma 6(b) eigenvalues, positive definiteness of H, which needs (H1) at l.982, and Lemma 4. **So at k = 4 the S_1 asymptotics need only (H1) = 2 > 0 and the d-free choice of ε.** At (4, 8), H = (1/5)(J_3 + I_3)^{⊗2} has eigenvalues 1/5 (four times), 4/5 (four times) and 16/5 (once), and det H = 4⁶5⁻⁹, matching KPW (3.13) (verifier K, exact). |

**Conclusion.** At (4, 8), KPW §§2–4 go through after two changes:
- (H1) = 2 is used at A6 and A11;
- the S_2 estimate is replaced by Lemma A and Theorem C (§5.1).
Everything else in KPW §§2–4 is used only at (k, d) = (4, 8), where it holds by the rows above; no claim is made for
other (k, d).

## 5. Upper bound: G_{n,8} is a.a.s. 4-colourable

### Proposition 5.1 (KPW Proposition 2(b) at (k, d) = (4, 8))
For n divisible by 4,
  E(Y²) ∼ k^k (k−1)^{k(k−1)}/((k²−2k−d+2)^{(k−1)²/2}(2π(k−2))^{k−1}) · n^{−(k−1)} k^{2n} (1−1/k)^{dn}
        = 4⁴·3¹²/(2^{9/2}(4π)³) · n^{−3} · 4^{2n} (3/4)^{8n}
(verifier A).

*Proof.* Follow KPW's proof of Proposition 2(b) (§3) with E(Y²) = S_1 + S_2 (l.937–945).
- S_1 is the sum over M′ ∈ B_{k−1}(δ) ∩ (k/n)Z^{(k−1)²}, with δ := ε log n/((k−1)² n^{1/2}) (l.925–928).
  - By A15, (3.12)–(3.14) give S_1 ∼ the displayed right-hand side.
  - This uses (H1) = 2 > 0 for H positive definite. Here det H = k^{2k−2}((k²−2k−d+2)/(k²−2k+2))^{(k−1)²}
    = 4⁶(1/5)⁹ (KPW (3.13)).
- S_2 collects the remaining M ∈ M ∩ (4/n)Z^{4×4}. For each, M ∉ B_4(δ) (l.997–998), so ‖M − J‖² ≥ δ².
  - By Proposition B and Theorem C,
    |T(M)|/|P_{n,8}| ≤ P_8(n) e^{n U(M)} ≤ P_8(n) e^{n U(J)} e^{−C_8 n δ²} = P_8(n)·4^{2n}(3/4)^{8n}·e^{−C_8 ε² log² n/81},
    since nδ² = ε² log² n/(k−1)⁴.
  - There are at most (n+1)^{16} terms. So S_2 ≤ (n+1)^{16} P_8(n)·4^{2n}(3/4)^{8n}·n^{−C_8 ε² (log n)/81}
    = 4^{2n}(3/4)^{8n} n^{−Θ(log n)}.
  - This is o(S_1), because S_1 = Θ(n^{−3}) 4^{2n}(3/4)^{8n} and C_8 > 0. Explicitly,
    S_2/S_1 = O(n^{199/2} exp(−C_8 ε² log² n/81)), since 16 + 8 + 145/2 + 3 = 199/2.
- Theorem C holds for every ε, so no coupling between ε and C_8 is needed. ∎

### 5.2 n ≡ 0 (mod 4): small subgraph conditioning at (k, d) = (4, 8)
Apply W99 Theorem 4.1 (I3) on P_{n,8}, with Y the number of balanced 4-colourings, X_i the number of i-cycles,
λ_i = 7^i/(2i) > 0 and δ_i = (−1)^i/3^{i−1} ≥ −1. Here δ_1 = −1 and |δ_i| ≤ 1/3 for i ≥ 2.
- (a) holds by (I4).
- (b) is KPW (1.1) (I1).
- (c) λ_iδ_i² = (9/2)(7/9)^i/i, so Σ_i λ_iδ_i² = (9/2) log(9/2) = 9 log(3/√2) < ∞. This is KPW (1.2),
  (k−1)² log((k−1)/√(k²−2k−d+2)), at (4, 8) (verifier A).
- (d) By (I1) and Proposition 5.1, E(Y²)/(EY)² → (3/√2)⁹ = exp((9/2) log(9/2)). This is KPW (1.3) (verifier A,
  exact symbolic identities).
- EY > 0, and EY grows exponentially, since k(1 − 1/k)^{d/2} = 4(3/4)⁴ = 81/64 > 1 (exact).

The first conclusion of Theorem 4.1 gives P(Y > 0) = e^{−λ_1} + o(1) = e^{−7/2} + o(1).
- *Loops.* A loop at v would require σ(v) ≠ σ(v). Equivalently, KPW's enumeration (l.184–194) joins only points of
  different colour classes. So Y = 0 on every pairing with a loop, and {Y > 0} ⊆ {X_1 = 0}. Since
  P(X_1 = 0) → e^{−7/2}, we get P(Y > 0 | X_1 = 0) → 1.
- *Double edges.* P(Y = 0 | X_1 = X_2 = 0) ≤ P(Y = 0 | X_1 = 0)/P(X_2 = 0 | X_1 = 0) → 0, since
  P(X_2 = 0 | X_1 = 0) → e^{−49/4} > 0.
- By (I4), G_{n,8} is a.a.s. 4-colourable along n ≡ 0 (mod 4).

### 5.3 n ≢ 0 (mod 4): residues r = 1, 2, 3
KPW §4 sets k′ = 2k if dk is odd and k′ = k otherwise. Here dk = 32, so k′ = 4. Since d is even, dr is even for
every r, so all of r = 1, 2, 3 occur, with ℓ = dr/2 = 4r ∈ {4, 8, 12} (verifier A).

*Theorem 10 at (4, 8, 4r).* By audit row A12 (with A14), its proof needs only:
- Proposition 2(a) and (1.1), which hold for every d (A10);
- Proposition 2(b), which is Proposition 5.1;
- the S_2 restriction, which is the conclusion of Proposition 5.1's S_2 estimate;
- (1.2)–(1.3), see §5.2;
- the Lemma 8 concentration (A9).
So, for m ≡ 0 (mod 4), let Ω′_m be the set of structures (G′, L): G′ a simple 8-regular graph on a fixed m-set, and
L an ordered ℓ-tuple of edges of G′ whose 2ℓ endpoints induce a perfect matching in G′. If (G′, L) is uniform on
Ω′_m, then a.a.s. G′ has a 4-colouring in which every edge of L has end colours 1 and 2.

*Inherited sketched steps (disclosed).* KPW's proof of Theorem 10 is a sketch. Two of its steps are imported as KPW
state them, with no further detail supplied here.
1. *Small subgraph conditioning on the marked space Ω_{n,d,ℓ}.* KPW assert that (1.1) holds with Y replaced by Ŷ
   (l.1551, l.1560–1593), and conclude by "the argument in the last few sentences of the proof of Theorem 1"
   (l.1558–1559). Left implicit there:
   - the cycle counts stay asymptotically independent Poisson on Ω_{n,d,ℓ}, since every pairing carries
     (dn/2)^ℓ(1 + O(1/n)) admissible ordered ℓ-tuples L, uniformly in the pairing;
   - the passage from marked pairings to uniform marked simple structures conditions on Simple and on L inducing a
     perfect matching.
2. *Edge-count concentration.* KPW: "We can easily bound the weight in F′ due to terms in which some b_pqrs is not
   dn/(k²(k − 1)²) ± O(n^{1/2} log n), and find an extra factor of O(n^{−Θ(log n)})" (l.1616–1621). The
   single-colouring analogue for b_ij is at l.1575–1584.

Neither step involves a degree threshold (audit rows A9 and A12). An independent derivation of both appears as a
reviewer's note in the Codex review of r1 (item 4). It is not part of this proof and is not relied on here.

*Reduction* (KPW l.1625–1643, with the conditioning made exact). Let n ≡ r (mod 4) with r ∈ {1, 2, 3},
G = G_{n,8} on V, and fix vertices v_1, …, v_r. Let 𝒢_r be the event that the v_i are pairwise at distance ≥ 4 and
none lies in a triangle.
- **P(𝒢_r) → 1.** KPW l.1627–1628: the vertices are a.a.s. at distance at least 4. KPW l.1632–1633: a fixed vertex
  is a.a.s. in no cycle of length less than 4. In P_{n,8}, the expected numbers of paths of length ≤ 3 between two
  fixed vertices and of triangles through a fixed vertex are O(1/n), and P(Simple) is bounded below (I4).
- **Induced matching.** On 𝒢_r, the neighbourhoods N(v_i) are pairwise disjoint 8-sets (distance ≥ 3). There is no
  edge between different N(v_i) (distance ≥ 4), and each N(v_i) is independent (no triangle at v_i). So
  W := ∪_i N(v_i) is an independent 8r-set in G − {v_1, …, v_r}.
  - Delete v_1, …, v_r. Add a uniformly random perfect matching η on W, and order its 4r edges uniformly at random
    as L.
  - The result G′ is a simple 8-regular graph on V ∖ {v_i}, which has n − r ≡ 0 (mod 4) vertices.
  - Since W was independent, the only edges of G′ inside W are those of η. So the endpoints of L induce a perfect
    matching, and (G′, L) ∈ Ω′_{n−r}.
- **Exact conditional uniformity.** Consider the map (G, η, order) ↦ (G′, L) on {G ∈ 𝒢_r} × {perfect matchings η of
  W(G)} × {orderings of η}.
  - Every G ∈ 𝒢_r has exactly (8r − 1)!!·(4r)! choices of (η, order).
  - The map is exactly multinomial(8r; 8, …, 8)-to-one onto Ω′_{n−r}. These counts are 1, 12870 and 9465511770 for
    r = 1, 2, 3 (verifier A); compare KPW's count of ways to reinstate the edges at l.1638–1640.
  - *Preimages.* Given (G′, L) ∈ Ω′_{n−r} with endpoint set W, choose an ordered partition of W into
    (N_1, …, N_r) with |N_i| = 8. There are multinomial(8r; 8, …, 8) choices. Delete the edges of L and join v_i to
    N_i.
  - Each choice gives a simple 8-regular graph G on V. In it the N_i are disjoint and W spans no edge, because W
    induced only L in G′. So the v_i are pairwise at distance ≥ 4 and no v_i lies in a triangle, i.e. G ∈ 𝒢_r.
    The pair (η, order) is recovered from L.
  - Distinct choices give distinct G, since N(v_i) = N_i. Every preimage arises this way.
  - Hence, conditional on 𝒢_r, (G′, L) is exactly uniform on Ω′_{n−r}.
- **Colouring.** Colour G′ by Theorem 10 and keep these colours on V ∖ {v_i}. Give every v_i colour 3.
  - Each neighbour of v_i is an endpoint of an L-edge, so it has colour 1 or 2.
  - The v_i are pairwise non-adjacent.
  - Every edge of G avoiding the v_i is an edge of G′, because G′ = (G − {v_i}) + η.
  So this is a proper 4-colouring of G.
- **A.a.s. transfer.** P(G_{n,8} is not 4-colourable) ≤ P(𝒢_r^c) + P_{Ω′_{n−r}}(no 4-colouring with every L-edge
  coloured {1, 2}) → 0.

Together with §5.2, χ(G_{n,8}) ≤ 4 a.a.s. as n → ∞.

## 6. Lower bound: G_{n,8} is a.a.s. not 3-colourable (acceptance item 7)

### 6.1 Molloy–Reed (published route)
By the Molloy–Reed criterion (I6) at q = 3 and d = 8: q(1 − 1/q)^{d/2} = 3·(2/3)⁴ = 16/27 < 1 (exact; verifier A).
Hence χ(G_{n,8}) > 3 a.a.s.
- KPW's weaker formulation (l.175–176) gives the same, since (2q − 1) log q = 5 log 3 < 8 (verifier A).
- W99 l.1107 states χ ≥ 4 a.a.s. for every d ≥ 6.

### 6.2 Self-contained first-moment bound (cross-check)
Let Z_3 be the number of proper 3-colourings of P_{n,8}. Fix class proportions r = (r_1, r_2, r_3), with n r_i
non-negative integers and Σ r_i = 1.
- If at most one class is non-empty, no pair of points may be matched while every vertex has degree 8, so the
  number of proper colourings with these class sizes is 0. Otherwise 1 − Σ r_i² > 0.
- *Count.* The exact count has the same structure as KPW (3.4), with three colour classes in place of the 16 cells
  and the three pairs {i, j} (i ≠ j) in place of the 72 allowed pairs (χ7 r2 Lemma 5.1).
- *Factorial bounds.* Steps 1–8 of Lemma A apply verbatim. Before duality, they give the exponent
  (d − 1)Σ r_i log r_i + (d/2) log d − Σ_{i<j} β_ij log β_ij, subject to Σ_{j≠i} β_ij = d r_i, with polynomial factor
  P_3(n) := e⁴(8n + 1)^{3/2}(4n + 1)^{7/2}. The factor collects points e³(dn + 1)^{3/2}, pair tuples (dn/2 + 1)³ and
  pairings e(dn/2 + 1)^{1/2}.
- *Weak duality.* Take multipliers μ_i = c_1 + log r_i on the non-empty classes. Then
  e^{μ_i + μ_j − 1} = e^{2c_1−1} r_i r_j, and Σ_{i<j} r_i r_j = (1 − Σ r_i²)/2.
- *Optimising c_1.* The minimum over c_1 (strictly convex in w = e^{2c_1−1} > 0) gives the exponent
  H(r) + (d/2) log(1 − Σ r_i²), where H(r) = −Σ r_i log r_i (verifier I).
- *Maximum over r.* Since H(r) ≤ log 3 and Σ r_i² ≥ 1/3, the exponent is at most log 3 + 4 log(2/3) = log(16/27) < 0.
- *Conclusion.* There are at most (n + 1)² class-size vectors, so E Z_3 ≤ (n + 1)² P_3(n) (16/27)^n → 0. By (I4),
  P(G_{n,8} is 3-colourable) ≤ E Z_3/P(Simple) → 0.
- *Exact-count control (verifier I).* For 3 ≤ n ≤ 60, the exact E Z_3 satisfies
  (1/n) log E Z_3 ≤ log(16/27) + (1/n) log[(n + 1)² P_3(n)]. At n = 60, (1/n) log E Z_3 = −0.5484, against
  log(16/27) = −0.5232.

This is the Molloy–Reed bound 3(2/3)^{d/2}, reproduced by the weak-duality step of Lemma A with the Erdős–Rényi
multiplier choice (exponent 1 on r), which is tight at the balanced point. The prior lane's rigorous maximisation of
the exact first-moment exponent over all class sizes is a further cross-check: `random7reg-colour/evidence/
verify_rigorous.json` (34c27dcd462be3d0ea29460e8474961ea8f54e46bf3c5bcc848cff2e804138b8), key C."d=8", with balanced
value log 3 + 4 log(2/3) = −0.5232… and every piece certainly < 0.

**Proof of the Theorem.** Combine §5 (χ ≤ 4 a.a.s.) and §6 (χ ≥ 4 a.a.s.). ∎

## 7. Controls (contract "controls"; verifier D, E, S)

- **C1. The pilot's arb constants are reproduced:** a, a² − 1/9, κ and C_8, as in §3.
- **C2. The route fails at d = 9; no d = 9 claim.**
  - The condition 1/3 ≤ (d−1)^{−(log 3)/2} is equivalent to log(d − 1) ≤ 2. At d = 9, log 8 > 2 and
    8^{−(log 3)/2} < 1/3 (certain).
  - The entropy cancellation would need multipliers (8/9) log m, not (7/8) log m.
  - Independently, the prior lane's rigorous enclosure Ψ_9(M_{3/4}) − Ψ_9(J) = +0.01863 > 0 shows that the plain
    balanced second moment itself fails at d = 9 (`random7reg-colour/evidence/d9_failure_enclosure.json`). This is
    context, not used.
- **C3. Mutations, all rejected as required.**
  - The row inequality with c_row replaced by 3/50 is violated at (19/25, 2/25, 2/25, 2/25):
    G − F(u_*) = +0.00179… (certain).
  - The identity S² + Q/2 = 18‖T_{1/2} g‖² is false.
- **C4. Lemma A beats KPW's relaxation at the χ7 obstruction.** At (J + I)/2, KPW's φ_8 exceeds φ_8(J), since
  13³² > 2⁵⁶·3³²·5⁵. But U((J+I)/2) − U(J) = −0.028764… < −C_8‖M − J‖² = −0.011049… (certain).
- **C5. Theorem C at explicit rational doubly stochastic matrices** (consistency, not proof), all certain:
  - (J+I)/2;
  - M_{2/3};
  - I;
  - J_2/2 ⊕ J_2/2;
  - 1 ⊕ J_3/3;
  - J + (1/100)(I − J).
- **C6. Exact-count check of Lemma A's exponent** at M = I, the scaled permutation matrix where the dual is tight
  (U(I) = Ψ_8(I) = 4 log 3 − 6 log 2).
  - For n = 4t, t ≤ 30, |T(I)|/|P_{n,8}| was computed exactly. (3.2)–(3.3) force b_12 = b_34, b_13 = b_24 and
    b_14 = b_23.
  - The rate (1/n) log(|T(I)|/|P|) stays below U(I) + (1/n) log P_8(n).
  - The gap U(I) − rate is positive and strictly decreasing for 5 ≤ t ≤ 30: 0.0547 at n = 120, with
    n·gap/log n ≈ 1.37, consistent with an n^{−3/2} prefactor.
  - So the exponent's constants carry no missing factor.
- **C7. Float sanity (not evidence).**
  - max (E(M) − E(J))/‖M − J‖² is −0.0720 over 4000 random doubly stochastic M, and −0.1141 over row-stochastic
    M; both are ≤ −κ.
  - U − Ψ_8 ≥ 1.4·10⁻⁴ over 300 random doubly stochastic M, and is 0 at J (−8.9·10⁻¹⁶).
- **C8. AM04's relaxed maximiser (verifier F).**
  - It is infeasible at (J + I)/2 (marginals 35/26 against 5/4, and 17/78 against 1/4) and at M_{2/3} (99/62
    against 3/2, and 25/186 against 1/6).
  - It is feasible at J and I (positive controls).
  - The relaxation overestimates the exponent at (J + I)/2 by at least 0.0361835… (arb).
- **C9. KPW l.1251 (verifier G).** 2(k − 1)² > k² holds at k = 4 (18 > 16) and fails at k = 3 (8 < 9).
- **C10. First-moment exact-count control** for 3 ≤ n ≤ 60 (verifier I; §6.2).

## 8. Verification record

`code/verify_chi8.py` (SHA-256 3884de76215e66f8488de6b40e6a83774e371e76255e44411fd0ad7b5b2d4329) →
`evidence/verify_chi8.json` (4d20589ae0a669027ae94268b6ace85c6166c0d9459a7c2af9ada1bc48271713) and
`evidence/verify_chi8.stdout.txt` (7acd78d605b5c8c970396a06a90cfd5da58af16d524cc5b5a65f35ca1c54150c).

The run of 07:37:16–07:37:24 PDT returned all_required_true = true. Its layers are:
- exact rationals and big integers;
- sympy symbolic identities;
- python-flint arb at 256 bits, where a comparison counts only when certain.

The script is self-contained and reads nothing from other lanes. Section S is floats and is not evidence.

`code/verify_chi8_r2.py` (SHA-256 1885293866b996d0f65f11314de8c9f6669171fd7a72fc79b596d422463e5f0e) →
`evidence/verify_chi8_r2.json` (cb3fe9b0921c16ff3cfb51f27a4f08fa99ee41136ae4fa2242044a1116a711ab) and
`evidence/verify_chi8_r2.stdout.txt` (27c11bf501478245ef1d97bbc2fd81cfc5a21d393e3ecac04b5253454207dece) cover the
items added in r2. Exact, sympy and arb only; self-contained. The run of 09:00:44–09:00:49 PDT returned
all_required_true = true. Its sections:
- F: the AM04 feasibility identity and witnesses, and the relaxation overestimate;
- G: KPW l.1251 at k = 3, 4 and 5;
- H: the GSVY identification and the eigenvalues of B ⊗ B;
- I: the first-moment weak duality and the exact-count control;
- K: the multiplier-convention scaling identity, the arb slack point values for the supplementary interval check,
  and KPW's H at (4, 8).

The float exploration `explore/unconstrained_phi1.py` → `explore/unconstrained_phi1.json`
(054d47caa03553de850a00ab71bcb9ae366546d0e328841de6e9c7245cdbc521) is not evidence and is used by no proof.

**Parent evidence (not this worker's execution).** The parent's independent rational arithmetic,
`institute/runs/six-lane-2026-10-16/review/chi8-parent-rational-arithmetic-v1.json` (SHA-256
cc17d09d6c465a25fbce62b4d17fcf9ffa6ce1bcf1edee0d35881156605263a9; recorded 2026-10-17 08:48:58 PDT; script SHA-256
abeee6a9…e0e4), uses exact atanh/Taylor remainder enclosures and integer square roots, without FLINT, SymPy or
NumPy. It certifies:
- 1473148178637501980/10²⁰ < C_8 < 1473148178637501981/10²⁰;
- 680276288527143926/10²⁰ < a² − 1/9 < 680276288527143927/10²⁰, and log 7 < 2;
- the row-variance factor 441/128, (H1), the series ratio 7/9 < 1, the EY growth 81/64 > 1 and Molloy–Reed
  16/27 < 1;
- the Gaussian-tail polynomial degree 199/2 and the residue preimage counts.
Its stated scope: "Independent rational constant/count arithmetic; does not by itself prove the universal matrix
inequality or the probabilistic transfer."

Lemma A, Lemma 3.1, the analytic proof of Lemma 3.2, Theorem C, the audit and §§5–6 are hand arguments; the scripts
certify their numerical and symbolic ingredients. The supplementary interval check of Lemma 3.2 is computer-assisted
and not needed for Theorem C.

## 9. Scope, reliance, prior work, priority

- *Reliance.* The proof imports:
  - KPW §§2–4, including Theorem 10, whose proof KPW only sketch, all used only at (k, d) = (4, 8);
  - W99 Theorems 4.1 and 2.6;
  - the Molloy–Reed criterion, which §6.2 re-derives in a self-contained way;
  - in the analytic proof of Lemma 3.2 only, D–SC Theorems A.1 and 3.5(ii). The supplementary interval check avoids
    D–SC.
  The audit (§4) shows that at (4, 8) only (H1) and the S_2 estimate carry the d-dependence. The S_2 estimate is
  re-proved here.
  - KPW's proof of Theorem 10 is a sketch. Two of its steps are imported exactly as sketched there (§5.3, "Inherited
    sketched steps"): small subgraph conditioning on the marked space, and the edge-count concentration. Neither
    involves a degree threshold.
- *Prior work, stated explicitly.*
  - Published: KPW's framework; AN's balanced second moment and display (12); NPG Theorems 1.2 and 3.1 (d < 7.4156,
    random lifts of loopless graphs); D–SC's complete-graph log-Sobolev constant and Gross's hypercontractivity (D–SC
    Theorem 3.5).
  - GSV and GSVY introduced the Φ reformulation of the pairing-model moment exponents. Lemma A's closed form is
    GSVY's Φ_1 for B ⊗ B at M^{7/8}, and the underlying maximum-entropy duality appears as GSV Lemma 4.3 (§2.1).
    This is not new here.
  - The Erdős–Rényi relaxation of the regular-graph second moment (AM04 §6, KPW Lemma 5; CLMS's "trick") is
    published. §2.2 shows it is strictly lossy away from overlaps that are constant on their support.
  - What may be new: the constrained global-decay inequality (Theorem C) at k = 4, proved by a row reduction and
    complete-graph hypercontractivity, and its use in place of Lemma 5 and AN's maximisation in KPW's S_2 estimate.
    The parent's bounded priority and method audit (`institute/runs/six-lane-2026-10-16/review/chi8-priority-audit.md`,
    recorded 2026-10-17 08:22:54 PDT) found no source proving such a constrained decay step. A search miss is not
    novelty, and no novelty or priority is claimed.
- *Priority searches.*
  - This worker's bounded searches found no source stating χ(G_{n,8}) = 4 for the uniform model:
    - 07:22:23–07:24:04 PDT, five queries (prior-lane LOG): "random 8-regular" 4-colourable; G_{n,8} / χ(G_{n,8});
      4-colourability threshold at d = 8, 9; "8-regular" with {4, 5}; a recent-year query on small-degree colouring;
    - between 07:24:04 and 07:31:29 PDT, three kill-check queries (this lane's LOG): an improvement of the AN
      maximisation beyond (27/4) log 3 for regular graphs; hypercontractivity or log-Sobolev treatments of the
      colouring second moment; "(k−1)³ log(k−1)/(k(k−2))" for the uniform model.
  - The parent's audit (17 web searches, OpenAlex citer and co-citation sweeps, arXiv API) reached the same
    conclusion. It read the Pérez-Giménez talks of 2012, 2019 and 2020, found nothing on d = 8, and lists its
    access holes.
  - A miss is not novelty.
- *Significance* is separate from correctness and is not assessed here. If correct, this closes KPW's {4, 5} window
  at d = 8 for the uniform model. The route needs log(d − 1) ≤ 2, so at k = 4 it stops at d = 8. [INFERENCE, not
  checked] The same route would also apply at d = 7 (log 6 < 2), where the accepted χ7 proof already gives the
  result.

## 10. Contract acceptance map (phys-2-random8reg-colour-contract-r2.json)

| Item | Where |
|---|---|
| (1) imports with exact hypotheses, verified at (4, 8): KPW §§2–4 and Theorem 10, W99 Theorem 4.1, Molloy–Reed | §1 (I1)–(I7), audit §4 |
| (2) Lemma A at finite n, every factorial bound, the polynomial factor, empty cells | §2, Lemma A, items 1–9; Proposition B |
| (3) Theorem C with both row proofs, the hypercontractivity normalisation quoted, constants exact or arb | §3: Lemma 3.2 analytic proof (the route used) and supplementary interval check; (I7) quotes; verifier B, C and K |
| (4) audit row: Lemma 5, (3.7), (3.9) only in S_2 and Theorem 10's restriction; S_1 needs only (H1) = 2 | §4 rows A14, A15 |
| (5) small subgraph conditioning at (4, 8) | §5.2 |
| (6) every residue r = 1, 2, 3, ℓ = 4r, induced perfect matching, exact conditional uniformity | §5.3 |
| (7) lower bound via Molloy–Reed, 3(2/3)⁴ = 16/27 < 1 | §6.1; self-contained cross-check §6.2 |

## 11. Changes from r1

1. §§0, 2.1 and 9, from the parent priority audit.
   - GSV and GSVY are cited as precursors: U(M) = Φ_1^{B⊗B}(M^{7/8}), GSVY's map (20), and GSV Lemma 4.3's
     maximum-entropy duality.
   - The distinction is stated: per-cell constraints (3.3) kept, against AM04/KPW; overlap constraint kept with
     pointwise decay, against GSV/GSVY.
   - The float observation on the unconstrained Φ_1 is recorded.
   - Sources pinned in `sources/` with SHA-256.
2. §2.2, from the parent's instruction. AM04 §6's pointwise feasibility assertion (l.454–455) is shown, exactly, to
   hold only for overlaps that are constant on their support, and to fail at (J + I)/2 and M_{2/3}. The relaxation
   is strictly lossy there (overestimate > 0.036). Scope: no published theorem is claimed false; KPW Lemma 5 remains
   a valid upper bound.
3. §1 (I2) and §4 (row A9′, conclusion), from the Codex minor. The audit is stated at k = 4 only; KPW l.1251 holds at
   k = 4 (18 > 16) and fails at k = 3.
4. §1 (I7), from Codex item 2: the resampling-chain normalisation note.
5. §6.2, from Codex item 5: a self-contained first-moment bound, with an exact-count control.
6. §§7–8: controls C8–C10 and the r2 verifier record (`code/verify_chi8_r2.py`). `code/verify_chi8.py` and its
   outputs are unchanged. §8 cites the parent's independent rational arithmetic as parent evidence. §5.1 states the
   S_2/S_1 polynomial degree 199/2 explicitly.
7. Claude m1 (§3, supplementary check, step 1). The undefined K is now K_b := (7/8)(r_i/2)^{−1/8}, distinct from the
   Markov kernel K. The text states that ΔS > 0 for small ε, and that (S + ΔS)² − S² ≥ 2ΔS because S ≥ 1.
8. Claude m2 (context). KPW's convention is stated: Theorem 1 (l.105–107) and the pinned abstract (l.23–27) take k
   smallest with d < 2(k − 1) log(k − 1) and conclude χ ∈ {k − 1, k}, so k = 5 at d = 8. The shifted convention
   (k′ = 4, χ ∈ {k′, k′ + 1}) is also stated. The window {4, 5} and every bound are unchanged.
9. Claude m3 (§3).
   - Theorem C now rests on the analytic (hypercontractivity) proof of Lemma 3.2. The interval argument is presented
     as a supplementary rigorous check, not needed for Theorem C.
   - Arb point values of its slack are added: 2.37·10⁻⁴ at x = 29/100 and 4.93·10⁻⁴ at x = 31/100, against the
     certified 1.83·10⁻⁶ (verifier K). Enclosure overestimation is not a mathematical flaw.
10. Claude m4 (§4). The appeals to earlier reviews as support are removed from the audit conclusion and from row A15.
    A15 now states H = (1/5)(J_3 + I_3)^{⊗2}, its eigenvalues and det H = 4⁶5⁻⁹ directly (verifier K). Review credits
    appear only in this change map and in the status block.
11. Claude m5 (status line and Proposition B).
    - A single multiplier convention, μ_u = c_0 + (7/8) ln m_u with exponent e^{μ_u+μ_v−1}, is used throughout.
    - A convention note gives the explicit scaling λ_u = μ_u + (ln 4 − 1)/2 (ln C = c_0 + (ln 4 − 1)/2) to the
      pilot's U_λ. The identity is verified symbolically for general d (verifier K), and both forms optimise to
      −10 log 2 + 4 log E.
12. Claude m6 (symbols).
    - The uniform row U is now u_*, and the support S is now supp M.
    - Proposition B's c is c_0; the interval check's c and K are c_row and K_b; KPW's Lemma 8 constant is c_KPW;
      §6.2's constant is c_1.
    - The §5.3 matching μ is now η, to avoid a clash with the multipliers.
    - A symbol list is added to §0.
13. Claude m7 (§5.3 and §9).
    - A new paragraph, "Inherited sketched steps (disclosed)", names the two Theorem 10 steps imported as KPW sketch
      them: small subgraph conditioning on the marked space, and edge-count concentration (KPW l.1616–1621 and
      l.1575–1584).
    - A matching reliance bullet is added to §9.
    - The Codex review's independent derivation is mentioned as a reviewer's note and is not relied on.
