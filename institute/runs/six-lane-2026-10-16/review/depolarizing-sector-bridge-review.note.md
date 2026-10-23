# Referee report: exact channel bridge, Claims 1–5

## Verdict: ACCEPT-WITH-FIXES

I found no mathematical error in Claims 1–5. All required fixes are expository. Two of them (F1, F3) matter in practice: an implementation that reads the text the other way would compute a different quantity. I did every check below by hand and ran no code.

## Mathematical errors

None found.

## Claim-by-claim verification

**Claim 1: correct.**
- **Determinant.** The eigenvalues of A_uv are bg and (b+η)g = ag, so det A_uv = ab·g².
- **Schur–Weyl block.**
  - The (M−λ, λ) isotypic block of A^{⊗M} is π(A) ⊗ I_{m_N}, with π ≅ det^λ ⊗ Sym^N.
  - The intertwiner V_N is one fixed unitary. This follows from Schur's lemma on U(2), and holomorphic extension carries it to all of M_2(ℂ), so the singular case g = 0 is covered.
  - Both sides of the block identity are linear in X and agree on a spanning set, so they agree everywhere.
- **Subset expansion.**
  - D(Y) = ηY + b·tr(Y)·I.
  - P_N(Y_S ⊗ I)P_N does not depend on the subset S, because P_N P_σ = P_N and Y ∈ L(Sym^N).
  - C(N,s)·(N+1)/(s+1) = C(N+1, s+1).
  - The cloner is trace-preserving because tr_{N−s} P_N = ((N+1)/(s+1))·P_s, by Schur's lemma.
- **Normalisation.**
  - Σ_s C(N+1,s+1) η^s b^{N−s} = (a^{N+1} − b^{N+1})/η, and the conversion to the stated π_s is exact.
  - p_N > 0 because a > b > 0, and Σ_N p_N = 1 follows from trace preservation.
- **Independent check of p_N.** p_N equals m_N·s_{(M−λ,λ)}(a,b) = m_N (ab)^λ (a^{N+1} − b^{N+1})/(a − b). This is exactly the N-weight of diag(a,b)^{⊗M} = D^{⊗M}(|0⟩⟨0|^{⊗M}), and Σ_N p_N = (a+b)^M = 1.
- **Spot check at M = 2.**
  - The N = 0 weight is ab for input |00⟩. For |ψ+⟩ it is (a²+b²)/2 − η²/2 = (1−η²)/4 = ab, as claimed.
  - Φ_2(|00⟩⟨00|) = diag(a², ab, b²)/(a²+ab+b²).
  - This equals π_0·I/3 + π_1·diag(2/3, 1/3, 0) + π_2·diag(1, 0, 0), with (π_0, π_1, π_2) = (3(1−η)², 6η(1−η), 4η²)/(3+η²).
- **Input independence.**
  - It also holds for off-diagonal inputs |φ_i⟩⟨φ_j|, because the decomposition is one linear map with fixed coefficients. Tensoring with id_R therefore creates no cross-sector terms.
  - The Sym^M hypothesis is essential, not decorative: the M = 2 singlet input has N = 0 weight (1+3η²)/4 ≠ ab.
- **Entropies.** S(B) and S(RB) both contain H(p) + Σ_N p_N log m_N, and these terms cancel exactly.

**Claim 2: correct.**
- **Loss formula.** It follows from |n;x⟩ = √((n−x)/n)·|n−1;x⟩|0⟩ + √(x/n)·|n−1;x−1⟩|1⟩.
- **Clone formula.** It follows from P_{n+1}|n;x⟩|0⟩ = √((n+1−x)/(n+1))·|n+1;x⟩ and P_{n+1}|n;x⟩|1⟩ = √((x+1)/(n+1))·|n+1;x+1⟩.
- **Trace preservation.** Summing the diagonals confirms that both maps are trace-preserving.
- **Clone composition.**
  - Sym^{s+2} ⊂ Sym^{s+1} ⊗ ℂ² gives P_{s+2}(P_{s+1} ⊗ I) = P_{s+2}.
  - The prefactors multiply correctly: (s+2)/(s+3) · (s+1)/(s+2) = (s+1)/(s+3).
  - Induction then gives Z_s = Σ_{t=s_min}^{s} π_t C_{t→s}(Y_t).
- **Truncation.**
  - A clone entry (x,y) reads only entries (x,y) and (x−1,y−1). So the index set {x,y ≤ D} is closed, and the truncated recursion returns P_D Z_N P_D exactly, not approximately.
  - A loss entry reads (x+1,y+1), so loss must run on the full input support, as the claim states.
  - Both steps conserve x−y exactly (U(1) covariance).

**Claim 3: correct.**
- **CPTP.** T_D has Kraus operators {P_D} ∪ {|⊥⟩⟨N;x| : x > D}.
- **Why the flag block is diagonal.** The underlying fact is stronger than the claim states. Because x−y is conserved, the diagonal of Φ(X) depends only on the diagonal of X. Hence tr(Q_D Φ(|φ_i⟩⟨φ_j|)) = 0 whenever φ_i and φ_j have disjoint Dicke supports. Pairwise-distinct residues mod k are a special case of this.
- **Flag identity.**
  - The output is Ω_P ⊕ (F ⊗ |⊥⟩⟨⊥|) with F = diag(q_i w_i), and the two pieces are orthogonal on B.
  - Hence I_c(ρ, T_DΦ) = (1−w)·I_c^P + h(w) − Σ_i h(q_i w_i) = (1−w)·I_c^P − w·H({q_i w_i / w}).
  - The flag term is ≤ 0, because h is subadditive.
  - The formula w_i = 1 − tr(P_D Φ(φ_i)) uses the fact that Φ is trace-preserving.
- **Data processing.** T_D post-processes B, so I_c(ρ,Φ) ≥ I_c(ρ, T_DΦ). This is the correct direction for a lower bound.

**Claim 4: correct.**
- **Lower bound.** It follows from concavity of S(B), almost-convexity of S(RB), and I_c(ρ, Φ_R) ≥ −S(R) = −H(q).
- **Upper bound.** It is valid as stated, but the +h2(ε) term is unnecessary: concavity of S(R|B) alone gives I_c(ρ,Φ_N) ≤ (1−ε)·I_c(ρ,Φ̂) + ε·H(q).
- **Uncomputed sectors.** Every sector has I_c ∈ [−H(q), H(q)], so the ±p_rest·H(q) remainder holds.
- **Edge cases.**
  - For 0 < η < 1 every p_N > 0, so the "zero-mass sectors" clause is vacuous.
  - Rank-deficient outputs are harmless. For example, N = 0 gives I_c = −H(q), which lies inside the interval.
  - Any q_i = 0 must be removed before r is defined.

**Claim 5: correct.**
- **Trace-norm bound.**
  - Ω ≥ 0 implies its off-diagonal block can be written C = A^{1/2} K B^{1/2} with ‖K‖ ≤ 1.
  - Hence ‖C‖₁ ≤ √(tr A · tr B), and ‖PΩQ + QΩP‖₁ ≤ 2√(w(1−w)).
- **Continuity bound.**
  - Winter's tight Alicki–Fannes–Winter (AFW) bound applies for ½‖ρ−σ‖₁ ≤ ε ≤ 1, and it is monotone in ε.
  - Using d_R = r is legitimate because the pinching acts on B only, so the support on R is unchanged.
- **Pinched state.**
  - The pinched state is a direct sum, so −S(R|B)_pinch = (1−w)·I_c^P + w·(−S(R|B)_Q).
  - This is at most (1−w)·I_c^P + w·log r.
- **Flag identity.** It matches Claim 3, and dropping −h(w) ≤ 0 goes in the correct direction.

## Required fixes (exposition only)

**F1. Define the split explicitly.**
- Define:
  - ε_N := Σ_{s<s_min} π_s^{(N)}
  - Φ̂_N := (1−ε_N)^{−1} Σ_{s≥s_min} π_s^{(N)} C_{s→N} L_{M→s}
  - Φ_R similarly over s < s_min.
- Both Φ̂_N and Φ_R are CPTP.
- The Claim 2 recursion returns (1−ε)·Φ̂(X), not Φ̂(X). Therefore:
  - w_i = 1 − tr(P_D Z_N[φ_i])/(1−ε);
  - the kept block must be rescaled by 1/(1−ε).
- Claim 3's formula for w_i silently assumes trace preservation, which is why this matters.
- **What goes wrong otherwise.** If the flag is allowed to absorb ε, the computation is really of Φ′ = (1−ε)·T_DΦ̂ + ε·tr(·)|⊥⟩⟨⊥|.
  - Φ′ is not a post-processing of Φ_N, so the stated chain of claims does not cover it.
  - A different route still gives a valid lower bound: concavity gives I_c(Φ′) ≤ (1−ε)·I_c(T_DΦ̂) − ε·H(q), hence I_c(Φ_N) ≥ I_c(Φ′) − h2(ε).
  - However, Claim 5 would have to be re-derived for Φ′.

**F2. Residue wording.** Replace "disjoint residues" with "pairwise distinct residues mod k (k ≥ 2)", or more generally "pairwise disjoint Dicke supports". Add the one-line diagonal-to-diagonal argument from the Claim 3 verification above.

**F3. Off-diagonal reference blocks.**
- State explicitly that only the flag block is diagonal.
- The kept block retains P_D Φ(|φ_i⟩⟨φ_j|) P_D for i ≠ j. These blocks are generally nonzero; for example, [L_{n→n−1}(|n;0⟩⟨n;1|)]_{01} = √(n(n−1))/n.
- **If they were dropped:**
  - Claim 3's lower bound would stay valid, because dephasing R raises S(RB) and leaves S(B) unchanged.
  - Claim 5 would break. Counterexample:
    - Setup: s_min = N = M, so Φ̂ = id; D at least the input support, so w = 0; q = (½, ½).
    - The true value is I_c(Φ̂) = 1, but the dephased I_c^P is 0.
    - The "upper bound" would therefore be 0 < 1.

**F4. Signs.** Replace "plus the classical flag entropies" with the explicit formula I_c(ρ, T_DΦ) = (1−w)·I_c^P + h(w) − Σ_i h(q_i w_i).

**F5. Claim 1 details.** State the following explicitly. They are standard, but the bridge depends on them.
- the fixed intertwiner V_N;
- holomorphic extension to singular A;
- independence of the subset S via P_N P_σ = P_N;
- the Schur's-lemma proof that the cloner is trace-preserving.

**F6. Claim 5 hypotheses.**
- Cite the exact AFW version and its hypotheses: ½‖·‖₁ ≤ ε ≤ 1, and d = dim R.
- Define I_c^P only for w < 1, with the convention (1−w)·I_c^P := 0 when w = 1.

## Optional tightenings (all valid)

- **Claim 4 upper bound:** drop the +h2(ε) term.
- **Claim 5 continuity parameter:** use ε = √(w(1−w)) instead of √w, and keep the −h(w) term.
- **Claim 5 Q-block term:** with distinct residues, the R-marginal of the Q block is diag(q_i w_i)/w, so w·log r can be replaced by w·H({q_i w_i / w}).
- With these changes, Claim 5 becomes:

  I_c(ρ, Φ̂) ≤ I_c(ρ, T_DΦ̂) + 2w·H({q_i w_i / w}) + 2ε·log r + (1+ε)·h2(ε/(1+ε)).

## What the bridge rigorously establishes

Let S be any set of computed sectors and p_rest = 1 − Σ_{N∈S} p_N. Then:

- **Lower bound:**

  I_c(ρ, D^{⊗M}) ≥ Σ_{N∈S} p_N·[(1−ε_N)·I_c(ρ, T_{D_N}Φ̂_N) − ε_N·H(q) − h2(ε_N)] − p_rest·H(q)

- **Upper bound:**

  I_c(ρ, D^{⊗M}) ≤ Σ_{N∈S} p_N·[(1−ε_N)·U_N + ε_N·H(q) + h2(ε_N)] + p_rest·H(q)

Here U_N is the right-hand side of Claim 5. Each I_c(ρ, T_DΦ̂_N) can be computed exactly from the P_D blocks via Claim 2, provided F1 and F3 are respected.

As instructed, I did not review the interval arithmetic, rounding error, record integrity or novelty of the numerical candidate.
