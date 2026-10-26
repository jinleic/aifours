# Shor FACT gate — |A| = 2^α q^β is impossible for every odd prime q ∉ {3, 5, 7, 11}

Owner MathShor (runtime MathShor-2). Actual `/bin/date` immediately before composing: `Sun Oct 25 23:25:32 PDT 2026` (an earlier-observation bound only).

**WRITTEN CANDIDATE, unreviewed.** This is a new partial result in the SAME 102319 continuation. It does not settle the Shor question or the FACT gate. No frozen file is edited.

## 0. Statement, inputs and scope

Let A ⊕ B = Z_n be a FACT solution: I = {0,3,8,11} ⊂ A and J0 = {0,1,7,13,14} ⊂ B. By consolidated-v1 §1.2–§1.3, 1320 | n, 330 | |B| and 2 | |A|. D3 ⊇ {0,1,2} denotes the third mate, another complement of the same A (consolidated-v1 three-mate equivalence).

**Theorem D.** If q is an odd prime with q ∉ {3, 5, 7, 11}, then |A| is not of the form 2^α q^β (α ≥ 1, β ≥ 1).

Together with Theorem A (|A| is not a prime power; `shor-FACT-prime-power-side-exclusion-v1.md`, SHA256 f286f623…8a29) and Theorem C (|A| ∉ {6, 10, 22}; `shor-FACT-size-2q-exclusion-v1.md`, SHA256 d3a796c9…559b): **if |A| has exactly two prime factors, then |A| = 2^α q^β with q ∈ {3, 5, 7, 11}, and (α, β) ≠ (1, 1) when q ∈ {3, 5, 11}.**

**Inputs**, all from those two pinned packets:
- the written multiplier lemma M;
- the general-size fibre lemma F′;
- the unit-collision lemma U′.

Everything else is elementary set reasoning on residues mod 2 and mod q. I3, I2, Coven–Meyerowitz T1/T2, the Szabó/Cordero Rédei property and H* are NOT used.

**Notation.** For x ∈ Z_n with 2q | n, write π(x) = x mod 2 and ρ(x) = x mod q. A set is *π-constant* if π is constant on it and *ρ-constant* if ρ is constant on it.

**Not covered.**
- q ∈ {3, 5, 11} with (α, β) ≠ (1, 1), for example |A| = 12, 18, 20, 44;
- q = 7, for example |A| = 14, 28 (§5 records the forced residue structure only);
- every |A| with three or more distinct primes;
- the FACT gate as a whole, the three-mate gate, every raw PR/STAB obligation, and the Shor question, which remains NOT_PROVED in either direction.

## 1. Lemma P — residue classes over r ∈ {3, 5, 11} are π- or ρ-constant

**Lemma P.** Let |A| have prime set {2, q}, q an odd prime, and let r ∈ {3, 5, 11} with r ≠ q. Put u_r = v_r(n) ≥ 1 and N_r = n/r^(u_r). Let X be any complement of A in Z_n (X = B, D2 or D3). For c ∈ Z_(r^(u_r)), every r-class

    X^(r,c) = {x ∈ X : x ≡ c mod r^(u_r)}

is π-constant or ρ-constant.

*Proof.*

1. **Fibres.** N_r contains the full 2- and q-parts of n, and gcd(N_r, r^(u_r)) = 1. So Lemma F′ applies with N = N_r. Reduction mod N_r is injective on A, with image A_(N_r), and each X^(r,c) reduces injectively (CRT) to a complement of A_(N_r) in Z_(N_r). Residues mod 2q are preserved, since 2q | N_r.
2. **The unit.** Take u = r. It lies in A_(N_r) − a_r, where a_r = 0 for r ∈ {3, 11} and a_r = 3 for r = 5 (because 5 = 8 − 3). Since r ∤ N_r, u is a unit of Z_(N_r).
3. **No 2q-unit differences.** Apply Lemma U′ in Z_(N_r) to Ā = A_(N_r) − a_r and to X^(r,c) − x₀ for x₀ ∈ X^(r,c). Because 2q | N_r, every integer t ≡ x·r^(−1) mod N_r has t ≡ x·r^(−1) mod 2q. Since r is odd and prime to q, t is prime to |A| exactly when x is odd and q ∤ x. Hence no two elements of X^(r,c) differ by an element that is odd and prime to q.
4. **Dichotomy.** Suppose X^(r,c) is neither π- nor ρ-constant, and fix x in it. There is y′ with x − y′ odd, so q | (x − y′) by step 3. There is z with q ∤ (x − z), so x − z is even by step 3. Then y′ − z is odd and prime to q, contradicting step 3. ∎

## 2. Lemma X — classes over different r cross

**Lemma X.** Let r ≠ r′ be in {3, 5, 11} \ {q}, and let X be a complement of A. Then X^(r,c) ∩ X^(r′,c′) ≠ ∅ for all c, c′. In fact the intersection contains a whole fibre X_y of Lemma F′ with N = 2^v q^w, where v = v_2(n) and w = v_q(n).

*Proof.* Lemma F′ with N = 2^v q^w makes every fibre X_y, y ∈ Z_(m′) with m′ = n/N, nonempty (|X_y| = N/|A| ≥ 1). Since r, r′ ∉ {2, q}, r^(u_r) r′^(u_(r′)) divides m′. Choose y ≡ c mod r^(u_r) and y ≡ c′ mod r′^(u_(r′)). ∎

## 3. Lemma K — consistency (needs q ∉ {3, 5, 11})

**Lemma K.** Let q ∉ {3, 5, 11} and let X be a complement of A with 0, 1 ∈ X (so X = B or X = D3). For each r ∈ {3, 5, 11}:
- (i) all π-constant r-classes of X carry the same parity;
- (ii) all ρ-constant r-classes of X carry the same residue mod q.

*Proof.* Let r′, r″ be the other two members of {3, 5, 11}.

(i) Suppose two π-constant r-classes carry parities 0 and 1. By Lemma X, every r′-class meets both, so it is not π-constant; by Lemma P it is ρ-constant, with value σ_D say. Likewise every r″-class E is ρ-constant, with value τ_E. Every r′-class D meets every r″-class E (Lemma X), so σ_D = τ_E for all D, E. Hence all σ_D are equal to one value σ. The r′-classes cover X, so ρ ≡ σ on X. This contradicts ρ(0) = 0 ≠ 1 = ρ(1).

(ii) Symmetrically, two ρ-constant r-classes with different values make every r′- and r″-class π-constant with one common parity. This contradicts π(0) ≠ π(1). ∎

**Consequence.** By Lemma P every r-class is π- or ρ-constant. So for each r ∈ {3, 5, 11} there are p_r ∈ Z_2 and σ_r ∈ Z_q such that every x ∈ X satisfies π(x) = p_r or ρ(x) = σ_r.

Both values exist. If every class were π-constant, Lemma K(i) would make π constant on X; if every class were ρ-constant, Lemma K(ii) would make ρ constant. Both are impossible because 0, 1 ∈ X.

Apply the disjunction to the seeds. The element 0 gives p_r = 0 or σ_r = 0, and the element 1 gives p_r = 1 or σ_r = 1. If p_r = 0, the second forces σ_r = 1; if p_r = 1, the first forces σ_r = 0. Therefore

    (p_r, σ_r) ∈ {(0, 1), (1, 0)}.

## 4. Proof of Theorem D

Let q ∉ {3, 5, 7, 11} and suppose |A| = 2^α q^β with α, β ≥ 1. The primes 3, 5, 11 then divide n but not |A|, so Lemmas P, X and K apply to X = B. Fix r = 3. (Lemma K for r = 3 uses the classes for r = 5 and r = 11.)

| case | every b ∈ B satisfies | seed | fails because |
|---|---|---|---|
| (p_3, σ_3) = (0, 1) | b even or b ≡ 1 mod q | 7 | 7 is odd, and 7 ≡ 1 mod q would need q \| 6 |
| (p_3, σ_3) = (1, 0) | b odd or b ≡ 0 mod q | 14 | 14 is even, and 14 ≡ 0 mod q would need q \| 14 |

Since q ∉ {2, 3, 7}, both cases are impossible. ∎

The only seeds used are 0, 1, 7 and 14 ∈ B, together with the unit seeds 3, 11 ∈ A and 5 = 8 − 3 ∈ A − A.

## 5. The excluded prime q = 7: forced residue structure (WRITTEN, no contradiction)

**Proposition E.** Suppose |A| = 2^α 7^β with α, β ≥ 1. Then:

- **(a)** Every b ∈ B is odd or ≡ 0 mod 7. Moreover, for each r ∈ {3, 5, 11}, every r-class of B lies in the odd residues or in 7Z.
- **(b)** Every d ∈ D3 is even or ≡ 1 mod 7.
- **(c)** A is equidistributed mod 14: |A ∩ (j + 14Z)| = |A|/14 for every j ∈ Z_14.

*Proof.*

(a) Lemmas P, X and K apply, since 7 ∉ {3, 5, 11}. The case (0, 1) fails at the seed 7, because 7 ≢ 1 mod 7. So (p_r, σ_r) = (1, 0) for every r.

(b) Apply the same lemmas to D3 ∋ 0, 1, 2. The case (1, 0) fails at the seed 2, which is even and not ≡ 0 mod 7. So (p_r, σ_r) = (0, 1).

(c) Consider two classes of B:
- The 3-class of 1 cannot be ρ-constant with value 0, since ρ(1) = 1. So it is π-constant with value 1 and lies in the odd residues.
- The 5-class of 0 cannot be π-constant with value 1. So it is ρ-constant with value 0 and lies in 7Z.

By Lemma X their intersection contains a whole fibre B_y (N = 2^v 7^w), all of whose elements are ≡ 7 mod 14. So B_y − b ⊂ 14Z_N. Covering then forces |A_N ∩ (j + 14Z_N)| = (N/14)/|B_y| = |A|/14 for every j. Residues mod 14 are preserved by reduction mod N. ∎

**Remark (|A| = 14).** By (c), A is then a complete residue system mod 14. Each 7-class of A_N is a pair at difference ≡ 7 mod 14, so after division by 7 the class becomes {0, t} with t odd. A ρ-constant fibre B_y ⊂ b + 7Z_N therefore satisfies (B_y − b)/7 + 2t = (B_y − b)/7, and its period has the full 2-part 2^(v−1) of |B_y|.

The obstruction is the π-constant fibres with several ρ-values. These require every even element of A to be ≡ 0 mod 4 and every odd element to be ≡ 3 mod 4; their periods then lose 2-adic order. No contradiction was derived, and none is claimed.

## 6. Consequences, boundary and the exact remaining gap

**Cumulative FACT size status (WRITTEN, Theorems A, C, D).** |A| is even and not a prime power. If |A| has exactly two primes, then |A| = 2^α q^β with q ∈ {3, 5, 7, 11}, excluding 6, 10 and 22.

The open sizes below 52 are therefore:

    12, 14, 18, 20, 24, 28, 30, 36, 40, 42, 44, 48, 50

Newly closed here: 26, 34, 38, 46 (and every 2^α q^β with q ≥ 13).

**Why the method stops.**
- *q ∈ {3, 5, 11}.* Only two crossing partitions remain, since the r = q classes are unavailable: q divides |A|, so it cannot be zeroed. Lemma K needs a third. With two partitions, configurations survive in which "π is a function of the residue mod r′^(u_(r′)) and ρ a function of the residue mod r″^(u_(r″))", and the seeds do not exclude them.
- *q = 7.* The pattern J0 is compatible with "odd or 0 mod 7", because 7 and 14 are multiples of 7 (Proposition E).
- *Three or more primes in |A|.* A set with no differences that are units mod 2qq′ need not lie in one coset of 2Z, qZ or q′Z. For example {0, 2, 5} mod 30 has differences 2, 5, 3. So Lemma P has no analogue.

**Relation to the literature.** The conditional statement that "each FACT cardinality has at least three distinct primes" (Cordero 2023 Lemma 5.2, citing the Szabó–Sands monograph, whose proof is unread here and unauthenticated) would subsume Theorems A, C and D. These theorems are an independent elementary proof of the stated special cases using the FACT seeds. No novelty or priority is claimed.

**First unproved original step.** Unchanged in kind: decide the FACT and three-mate gates for every remaining |A| and every n ∈ 1320Z, then every raw PR, isolated-word, delay and STAB/GP bridge obligation.

## 7. Assurance

WRITTEN only. Every residue, divisibility and counting step above was checked by hand with exact integers. No scientific interpreter, calculator, eval, program, CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO was used. The owner's permanent v109-A reviewer exactness finding (f32c51d3…8584) remains and is not cured.

This is not formal, kernel, configured-family, human, executable, priority or novelty acceptance. The original cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 are unchanged.
