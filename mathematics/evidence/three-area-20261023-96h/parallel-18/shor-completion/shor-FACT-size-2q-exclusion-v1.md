# Shor FACT gate — |A| = 2q is impossible for q = 3, 5, 11 (so |A| ≠ 6, 10, 22)

Owner MathShor (runtime MathShor-2). Actual `/bin/date` immediately before composing: `Sun Oct 25 22:57:25 PDT 2026` (an earlier-observation bound only).

**WRITTEN CANDIDATE, unreviewed.** This is a new partial result in the SAME 102319 continuation. It does not settle the Shor question or the FACT gate.

## 0. Statement, inputs and scope

Let A ⊕ B = Z_n be a FACT solution, so I = {0,3,8,11} ⊂ A and J0 = {0,1,7,13,14} ⊂ B. By consolidated-v1 §1.2 and §1.3, 1320 | n, 330 | |B| and 2 | |A|.

**Theorem C.** |A| ≠ 2q for q ∈ {3, 5, 11}. In particular |A| ∉ {6, 10, 22}.

This closes the |A| = 6 branch that survived every earlier elementary filter (checkpoint05/06), including the explicit control A = {0,3,8,11,85,256}.

**Inputs.** Everything is taken from the pinned packet `shor-FACT-prime-power-side-exclusion-v1.md` (SHA256 f286f623…8a29):
- the written multiplier lemma M;
- the fibre lemma F;
- the unit-collision lemma U.

Lemmas F and U are stated there for |A| = p^α. Here they are used in the following general-size forms. Their proofs are the same text, because Lemma M only needs every prime factor of the multiplier to avoid |A|.

- **F′.** Let N | n with gcd(N, n/N) = 1, and suppose N contains the full prime-power part of every prime dividing |A|. Then d ≡ 1 mod N, d ≡ 0 mod n/N is prime to |A|. Consequently reduction mod N is injective on A, and every fibre B_z is a complement of A mod N in Z_N, of size N/|A|.
- **U′.** Let Ā ⊕ X = G, with 0 ∈ Ā ∩ X and u ∈ Ā a unit of G. If x ∈ X is nonzero, then no integer t with t·u ≡ x mod |G| is prime to |Ā|.

To these the proof adds only elementary set counting. I3, I2, Coven–Meyerowitz T1/T2, the Szabó/Cordero Rédei property and H* are NOT used.

**Not covered.**
- Other two-prime sizes: 2q for q ∉ {3,5,11} (|A| = 14, 26, …), all 2^α q^β with α ≥ 2 or β ≥ 2 (|A| = 12, 18, 20, …), and every size with three or more primes.
- The FACT gate as a whole, the three-mate gate, every raw PR/STAB obligation, and the Shor question (NOT_PROVED in either direction).

## 1. Setting and the coset dichotomy

Fix q ∈ {3, 5, 11}. Suppose, for contradiction, that |A| = 2q. Write n = N·m′ with N = 2^v q^w, where v = v_2(n) ≥ 3 and w = v_q(n) ≥ 1, so gcd(m′, 2q) = 1. Note that 3, 5 and 11 all divide n.

**(1a) N-fibres.** Lemma F′ applies with this N, because N contains the full 2- and q-parts of n. Hence:
- reduction mod N is injective on A, with image A_N;
- every fibre B_y (y ∈ Z_(m′)) is a complement of A_N in Z_N, of size N/(2q) = 2^(v−1) q^(w−1).

**(1b) No unit differences.** The seed u = 11 (if q = 3) or u = 3 (if q = 5, 11) is odd and prime to q, hence a unit of Z_N. Apply Lemma U′ to every translate B_y − b, b ∈ B_y.

For x ∈ B_y − b, take any integer t ≡ x·u^(−1) mod N. Since N is even and u is odd, t is odd exactly when x is odd, and q ∤ t exactly when q ∤ x. So t is prime to |A_N| = 2q exactly when x is a unit of Z_N.

Hence no difference of two elements of B_y is a unit of Z_N, i.e. odd and prime to q.

**(1c) Dichotomy.** Each B_y lies in ONE coset of 2Z_N or in ONE coset of qZ_N.

*Proof.* Fix x ∈ B_y and suppose neither alternative holds. Then there is y′ ∈ B_y with x − y′ odd; by (1b), q | (x − y′). There is also z ∈ B_y with q ∤ (x − z); by (1b), x − z is even. Then y′ − z is odd and prime to q, i.e. a unit of Z_N, contradicting (1b). ∎

## 2. Type-q fibres are cosets of 2qZ_N

Let B_y ⊂ b + qZ_N. Covering each residue class mod q exactly N/q times forces every q-class of A_N to have exactly N/(q·|B_y|) = 2 elements.

Choose the q-class that contains a seed pair at distance q:

| q | seed pair | distance |
|---|---|---|
| 3 | {0, 3} | 3 |
| 5 | {3, 8} | 5 |
| 11 | {0, 11} | 11 |

This class is exactly that pair. After translating its smaller element to 0 and dividing by q, it becomes {0, 1}.

Let Y′ = (B_y − b)/q ⊂ Z_(N/q). The class tiles its own coset of qZ_N with B_y − b, so {0, 1} ⊕ Y′ = Z_(N/q).

N/q is even, and ⟨1⟩ is the whole group. The complements of {0,1} are therefore exactly the even residues and the odd residues, and 0 ∈ Y′ gives Y′ = 2Z_(N/q).

Hence B_y = b + 2qZ_N, a single coset.

## 3. Type-2 fibres are unions of cosets of 2^ℓ qZ_N with ℓ ≤ 3

Let B_y ⊂ b + 2Z_N, write B_y − b = 2Y, and split A_N into its even part A_e and odd part A_o.

**Level 1.** As in Lemma U's covering count, A_e ⊕ 2Y = 2Z_N and A_o ⊕ 2Y = 1 + 2Z_N. So |A_e| = |A_o| = q.

Put S_e = A_e/2 and S_o = (A_o − 3)/2 in Z_(N/2). Both have size q, and both are complements of Y:

    S_e ⊕ Y = Z_(N/2) = S_o ⊕ Y.

Since 0, 8 ∈ A_e and 3, 11 ∈ A_o, we have 0, 4 ∈ S_e and 0, 4 ∈ S_o.

**Recursion.** Suppose at level ℓ both current sets lie in 2Z. Split every current piece Z by parity, Z = Z_0 ⊔ Z_1. Because the sets preserve parity, each half Z_c is a complement of both sets inside its parity class. Halve the sets and the halves:

    S′ ⊕ (Z_c − c)/2 = Z_(N/2^(ℓ+1))

for both sets. The distinguished elements become 0, 2 at level 2 and 0, 1 at level 3. So by level 3 at the latest, one current set S contains an odd element.

**Leaf.** Let ℓ ≤ 3 be the first level at which S_e or S_o contains an odd element. Let S be that set, M = N/2^ℓ, and t ∈ S odd.

S ∋ s_1 = 8/2^ℓ, a power of 2 prime to q:
- If ℓ ≤ 2, then t and t − s_1 are both odd and differ by s_1, so at most one of them is divisible by q. One of them is therefore a unit of Z_M.
- If ℓ = 3, then s_1 = 1 is itself a unit.

Translate S, by 0 or by s_1, so that it contains 0 and that unit. Lemma U in Z_M (|S| = q, multipliers prime to q) then shows every piece Z, translated to contain 0, lies in qZ_M. Since |Z| = M/q = |qZ_M|, each piece is a full coset of qZ_M.

**Lift.** Lifting through the ℓ halvings, B_y − b is a union of cosets of 2^ℓ qZ_N. Since ℓ ≤ 3, every type-2 fibre is a union of cosets of 8qZ_N.

## 4. Periodic descent contradiction

By §§1–3, every N-fibre of B is a union of cosets of 8qZ_N: 2qZ_N and 2^ℓ qZ_N with ℓ ≤ 3 all contain 8qZ_N. Hence B + H = B for the subgroup H = 8qZ_N × {0} of Z_n, of order 2^(v−3) q^(w−1).

As in consolidated-v1 §1.3, but with the period on the B side:
- (A − A) ∩ H = {0} because the sum is direct, so A projects injectively;
- Ā ⊕ B̄ = Z_n/H, which is cyclic of order 8q·m′.

The FACT seeds keep distinct images, because their m′-coordinates are distinct (m′ > 14). Moreover

    |B̄| = |B|/|H| = (2^(v−1) q^(w−1) m′)/(2^(v−3) q^(w−1)) = 4m′,

which is prime to q.

Lemma M in Z_n/H, with d = q prime to |B̄|, gives qB̄ ⊕ Ā = Z_n/H. This direct sum collides:

| q | in qB̄ | in Ā | collision |
|---|---|---|---|
| 3 | 0, 3 = 3·1 | 0, 3 | 0 + 3 = 3 + 0 |
| 5 | 0, 5 = 5·1 | 3, 8 | 3 + 5 = 8 + 0 |
| 11 | 0, 11 = 11·1 | 0, 11 | 0 + 11 = 11 + 0 |

In each case the two pairs are distinct in a group of order 8q·m′, so the sum is not direct. Contradiction. ∎

## 5. Control, consequences and the exact remaining gap

**Control.** For the earlier surviving example A = {0,3,8,11,85,256}:
- The odd half gives S_o = {0, 4, 41}, which contains the odd element 41 at level 1, so every type-2 fibre is a coset of 6Z_N.
- 85 ≡ 256 ≡ 1 mod 3, so type-3 fibres are cosets of 6Z_N as well.
- Hence B would be 6Z_N-periodic, and §4 excludes every complement containing J0 at every admissible order.

This is a written check of the displayed residues only.

**Consequences (combined with Theorem A).** In every FACT solution, |A| is even, not a power of 2, and not 6, 10 or 22. The smallest sizes still open are 12, 14, 18, 20, 24, 26, 28 and 30.

**Why the method stops here.**
- *2q with q ∉ {3,5,11}.* The four seeds lie in distinct q-classes, so no {0,1} class is forced. The two-point classes {0,t} only give periods ⟨2t⟩ with unknown q-part, and q need not divide |B|.
- *Larger exponents.* At the leaves the current sets are no longer of prime size, so the coset conclusion and the full q-part of the period are not forced.

No claim is made for these cases.

**First unproved original step.** Unchanged in kind: decide the FACT and three-mate gates for every remaining |A| and every n ∈ 1320Z, then every raw PR, isolated-word, delay and STAB/GP bridge obligation.

**Assurance.** WRITTEN only. All congruences and counts were checked by hand, with exact integers. No scientific interpreter, calculator, eval, program, CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO was used. The owner's permanent v109-A exactness finding remains.

This is not formal, kernel, configured-family, human, executable, priority or novelty acceptance; Theorem C is a special case of the published two-prime Rédei-type theorem as stated by Cordero 2023 Lemma 5.2, here proved independently. The original cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 are unchanged.
