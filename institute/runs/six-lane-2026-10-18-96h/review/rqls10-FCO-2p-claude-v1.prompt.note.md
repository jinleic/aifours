## Referee report: Proposition FCO-2p (parent derivation v1)

**Verdict: ACCEPT.** The proposition is true, and the proof is correct and complete as written. There are no FATAL or MAJOR findings. The six MINOR findings below are about presentation and scope wording, and none of them affects an inference.

I checked the derivation text embedded in the request by hand. As instructed, I did not open the file, check the SHA256, or compute anything. I did not check the linked scout record, the enumeration audit, or the Ball–Simoens citation. The proof uses none of them.

### Step-by-step check

- **Rows and columns.** The row inner product `(1/n) Σ_t ζ^(t(j'−j))` equals δ(j,j′) with no hypothesis, and j = j′ gives unit norm. For columns, substitute u = π(t), which is valid because π is a bijection. This gives δ(ρ(i),ρ(i′)), which equals δ(i,i′) because ρ is injective. In the class inner product the shift s cancels, so the single condition (F) covers every class. ✔
- **(F) ⇔ HH\* = nI ⇒ (F\*).** The entry `(HH*)_{ii'}` is the (F)-sum for the ordered pair (i′, i), and the diagonal entries are n. H is square, so H/√n is unitary and H\*H = nI. The (t, t′) entry of H\*H = nI is exactly (F\*). Note that (F\*) is (F) with π and ρ swapped. ✔
- **CRT.** The identity `1/2 + c'/p = (p + 2c')/(2p) = 1/(2p)` holds exactly, so ζ = −ω^c′. Since c′ ≡ c (mod p), this equals −ω^c. Both sides of ζ^x = (−1)^x ω^(cx) depend only on x mod 2p. ✔
- **Vanishing criterion.** Set `N(cv mod p) = M⁺(v) − M⁻(v)`, an integer, and `g(x) = Σ_{w<p} N(w) x^w`. Then g(ω) = 0 holds iff Φ_p divides g. Because deg g ≤ p − 1, that holds iff g = κΦ_p, i.e. iff all N(w) equal a common κ ∈ Z. ✔ The text leaves the degree step implicit (m2).
- **|κ| ≤ 2.** pκ = #even − #odd, which lies in [−2p, 2p]. ✔ Also, #even − #odd = 2·#even − 2p is always even, so κ is even for every pair.
- **Odd pair.** Suppose no pair has a and b both odd. Then ρ(i) ≡ ρ(i′) (mod 2) for every even i and odd i′. So all values of ρ share one parity, which is impossible because ρ takes p even and p odd values. Since a is odd, i ≠ i′ automatically. ✔ This step works for any even n.
- **Count and mod 4.** The classes even→even, even→odd, odd→even, odd→odd have sizes k, p−k, p−k, k. So #even − #odd = 4k − 2p ≡ 2 (mod 4). κ = 0 would give 0 and κ = ±1 an odd number, so κ = ±2, and then k = p(κ+2)/4 ∈ {0, p}. ✔
- **Transfer to ρ via (F\*).** The criterion, the bound on κ and Step 2 apply verbatim to `Σ_i ζ^(a'i + b'ρ(i))`, with a′ = t′ − t and b′ = π(t′) − π(t). The odd pair comes from π. ✔
  - This step does real work. From (F) and the parity of π alone, a pair with a ≢ b (mod 2) gives κ = 0, i.e. M⁺(v) = M⁻(v), which is no contradiction.
  - So the parity of ρ really does come from the HH\* ⇒ H\*H step, and that step is valid.
- **Constant parity and two-fold equidistribution.** Write ρ(i) ≡ i + ε and π(t) ≡ t + δ. Then b ≡ a, and E_t ≡ aδ (mod 2) is constant in t. So one of M⁺, M⁻ vanishes identically and the other equals 2 for every v. Hence E_t mod p is exactly 2-to-1 onto F_p, for every pair i ≠ i′. ✔
- **Distinct P_i.** Reduction from Z_2p to F_p is a ring map, so E_t mod p = (P_i′ − P_i)·Q_t. If P_i = P_i′, all 2p values of E_t would be 0 mod p, contradicting the equidistribution. ✔
- **Directions.** Suppose no pair determines the direction ⟨u⟩. Then each of its p parallel lines holds at most one point, so there are at most p < 2p points. This is the trivial bound and needs no Rédei-type input. For u ≠ 0, take a pair whose difference is λu with λ ≠ 0. Then u·Q_t = λ⁻¹E_t, which is again exactly 2-to-1. ✔
- **Fourier.** f̂(u) = 2 Σ_v ω^v = 0 for u ≠ 0, and f̂(0) = 2p. So f ≡ 2p/p² = 2/p, which is not an integer for p ≥ 3. ✔
  - Fourier-free cross-check: the p + 1 lines through any point x₀ each carry mass 2.
  - So p·f(x₀) + 2p = 2(p + 1), which again gives f(x₀) = 2/p.

**Does the argument prove too much?** No.
- For odd n, π = ρ = id satisfies (F), because `Σ_t ζ^(2at) = 0` when 2 is a unit. The argument correctly has no starting point there, because the (−1)^x factor is absent.
- When 4 divides n, the CRT split fails.
- For n = 2m with m odd composite, the vanishing criterion is false; for example, 1 + ω₉³ + ω₉⁶ = 0.

So every hypothesis on n is actually used.

### Findings

- **m1 MINOR: orthogonality is never defined.** The "iff (F)" assumes the following definition. Q is orthogonal to a Latin square L iff, for each symbol s, the vectors {q_ij : L_ij = s} are pairwise orthogonal. Equivalently, {q_ij ⊗ e(L_ij)} is an orthonormal basis of C^(n²). *Repair:* state this definition in the Setting, since the proposition is relative to it.
- **m2 MINOR: Step 1 exposition.** The check uses c′ while the statement uses c. The claim "vanishes iff constant" also skips reindexing the exponents to 0…p−1 and the degree argument. *Repair:* add "ω^c′ = ω^c since c′ ≡ c (mod p)", plus the one-line g = κΦ_p argument above.
- **m3 MINOR: Step 3 cites too little.** The transfer needs Step 1's criterion for sums over i, not only Step 2. *Repair:* "(F\*) is (F) for (ρ, π), so Steps 1–2 apply verbatim with (i, ρ) ↔ (t, π)." Optionally, also note that the step does real work, as shown above.
- **m4 MINOR (optional): simplification.** κ is even for every pair, so only κ = 0 needs the mod-4 argument.
- **m5 MINOR: uncovered cases listed incompletely.** The sentence "Does not cover n = 8 … or n = 2m with m odd composite" omits n = 4 and every other n ≡ 0 (mod 4). *Repair:* "Covers exactly n = 2p, p an odd prime. Not covered: every n ≡ 0 (mod 4) (at n = 8 the 0 count rests on enumeration only), and n = 2m with m odd composite (18, 30, …). For odd n the family does contain mates, e.g. π = ρ = id."
- **m6 MINOR: external consistency claims are unsupported in the record.** "Agrees with the Ball–Simoens order-6 result" comes with no citation and no statement of the result. Agreement only means something if that result uses the same orthogonality notion. I did not check the audit counts. The proof uses neither. *Repair:* give a precise citation and statement, or drop the clause.

### Exact scope

**Proved:** let n = 2p with p an odd prime. For all permutations π, ρ of Z_n, the matrix `H = [ζ^(it + ρ(i)π(t))]` is not complex Hadamard. Equivalently, the array q, which is always a QLS, is never orthogonal in the m1 sense to L_ij = j − i.

**Also covered at no extra cost.** Each of these follows from a one-line invariance that the record does not state:
- **L_ij = i + j.** (π, ρ) is a mate of this square iff (π, ρ(−·)) satisfies (F).
- **U·q for any global unitary U, with arbitrary per-cell phases.** This includes coordinate permutations. So it also covers:
  - exponents of the form α(t)j + β(t)ρ(i), with α and β bijections;
  - affine column relabellings j ↦ uj + v, with u a unit.
- **Arbitrary maps π, ρ: Z_n → Z_n, so the permutation hypothesis costs nothing.**
  - If q is a QLS, ρ must be injective, otherwise two cells of a column coincide.
  - Then every d ≠ 0 arises as a difference ρ(i′) − ρ(i).
  - Column orthonormality then gives `Σ_t ζ^(d·π(t)) = 0` for every d ≠ 0, which forces π to be a bijection.

**Not covered:**
- unrestricted QLS mates of Cay(Z_2p);
- other Latin squares of order 2p (Cay(D_p), other isotopy classes);
- non-affine column relabellings in the exponent;
- n ≡ 0 (mod 4);
- n = 2m with m odd composite;
- 1-RQLS(10).

### Silent assumptions

None. The proof uses only:
- n = 2p with p an odd prime;
- bijectivity of π and ρ;
- the m1 definition of orthogonality.

(F\*) and the distinctness of the P_i are derived, not assumed. No step uses linearity of π or ρ, a normalisation such as π(0) = 0, or any enumeration result. The only outside inputs are irreducibility of Φ_p over Q and Fourier inversion on F_p², both standard.
