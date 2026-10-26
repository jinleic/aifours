# Shor FACT gate — the end-side factor A cannot have prime-power size

Owner MathShor (runtime MathShor-2). Actual `/bin/date` immediately before composing: `Sun Oct 25 22:42:02 PDT 2026` (an earlier-observation bound, not an exact creation instant).

**WRITTEN CANDIDATE, unreviewed.** This is a new partial result in the SAME 102319 continuation. It does not settle the Shor question or the FACT gate. No frozen file is edited.

## 0. Statements, imports and scope

**FACT gate.** Every finite raw UD factor-complete superset of Shor's code C yields a direct factorization A ⊕ B = Z_n with I = {0,3,8,11} ⊂ A and J0 = {0,1,7,13,14} ⊂ B (`shor-common-complement-uniform-trades-consolidated-v1.md` §1.1; route note R1). The same section proves 2 | |A|, 330 | |B| and 1320 | n.

**Theorem A (FACT-specific, import-free beyond the written multiplier lemma).** In every FACT solution, |A| is not a power of a prime. Since 2 | |A|, it follows that |A| has an odd prime divisor.

**Theorem B (general prime-power Rédei-type lemma).** Suppose A ⊕ B = Z_n, 0 ∈ A ∩ B, |A| = p^α with p prime, and A generates Z_n. Then B ⊂ pZ_n, so in particular B does not generate Z_n.

The proof of Theorem B uses the written multiplier lemma M (§1). For each prime q of the p′-part of n it also needs one of:
- an element of A that is a unit modulo p^v q^w (this suffices on its own, see Lemma U), or
- the named import I3 (Sands 1979): for n = p^a q^b, in every factorization with 0 in both factors, one factor lies in a proper subgroup. Dai 2026 (arXiv 2601.07135v2, §1.1) states it exactly so; the parent-visible page was re-read at this clock.

Theorem A is the case where the FACT seeds 3 and 11 supply such units, so Theorem A needs no I3, I2, Szabó, Cordero or Coven–Meyerowitz input.

**Relation to the old boundary.** The earlier conditional statement "each FACT cardinality has at least three distinct primes" rested on Cordero 2023 Lemma 5.2, quoted from the unread Szabó–Sands monograph proof (Szabó 2006). It remains unauthenticated. The power-of-two case was otherwise covered only by the restricted results |A| ≥ 6 and R4.

Theorem A now excludes every |A| = 2^α unconditionally. Theorem B is a special case of the published Rédei-property results; an independent elementary proof is given here, and no novelty is claimed.

**NOT proved here:**
- two-prime sizes such as |A| = 2^α 3^β (for example the surviving |A| = 6 examples);
- the FACT gate itself;
- the three-mate gate;
- any raw PR/STAB obligation;
- the Shor question, which remains NOT_PROVED in either direction.

## 1. The written multiplier lemma M

**Lemma M** (proved in writing in consolidated-v1 §1.2; recalled). Let G be a finite cyclic group and U, V finite sets with 1_U * 1_V = 1 on G. Let d be a positive integer none of whose prime factors divides |U|.

Then x ↦ dx is injective on U, and dU ⊕ V = G.

*Proof.* Take a prime r | d, with r not dividing |U|. In the commutative group ring F_r[G], Frobenius gives (T_r 1_U) = (1_U)^{*r}. Hence

    (T_r 1_U) * 1_V = (1_U)^{*(r−1)} * 1 = |U|^(r−1)·1 = 1  (mod r).

The left side has nonnegative integer values with total |U||V| = |G|. Being ≡ 1 mod r, each value is at least 1, so every value is exactly 1.

Since 0 can be assumed in V after translation, T_r 1_U is 0/1 valued of total |U|. So multiplication by r is injective on U and rU ⊕ V = G. Iterate over the prime factors of d. Nonunit d are allowed.

## 2. CRT fibres

Write n = p^v m with p ∤ m, and use CRT coordinates x = (x_p, x_m).

Let N be a divisor of n with p^v | N and gcd(N, n/N) = 1. Choose a positive integer d with d ≡ 1 mod N and d ≡ 0 mod n/N. Then p ∤ d, so Lemma M gives dA ⊕ B = Z_n, where dA is the set of CRT points (a mod N, 0).

**Lemma F.**
- (i) Reduction mod N is injective on A. Write Ā_N for the image.
- (ii) For every z ∈ Z_(n/N), the fibre B_z = {b mod N : b ∈ B, b ≡ z mod n/N} satisfies Ā_N ⊕ B_z = Z_N directly.
- (iii) In particular |B_z| = N/p^α, and every fibre is nonempty.

*Proof.* (i) is the set property in Lemma M.

For (ii), an element x with x ≡ z mod n/N is uniquely x = α + b with α ∈ dA and b ∈ B. Since α ≡ 0 mod n/N, we get b ≡ z mod n/N. Comparing residues mod N gives a unique representation (a mod N) + (b mod N).

(iii) is counting. ∎

We apply Lemma F twice:
- **N = p^v:** this gives the m-fibres B_y ⊂ Z_(p^v), one for each y ∈ Z_m, each of size p^(v−α) ≥ 1. (Injectivity of A mod p^v forces α ≤ v.)
- **N = p^v q^w,** for a prime q | m with w = v_q(n), and W_q the product of the remaining prime-power components: this gives the W_q-fibres.

Each W_q-fibre is the union of the m-fibres B_(y_q, z) over all y_q ∈ Z_(q^w). By (iii) for N = p^v, it therefore contains elements of EVERY q-coordinate.

## 3. Unit-collision lemma U

**Lemma U.** Let G be cyclic and Ā ⊕ X = G, with 0 ∈ Ā ∩ X and |Ā| = p^α. Suppose Ā contains a unit u of G. Then X contains no nonzero x for which some integer t ≡ x·u^(−1) mod |G| has p ∤ t.

In particular, if |G| = p^v or |G| = p^v q^w, then X ⊂ pG = {x : x_p ∈ pZ_(p^v)}.

*Proof.* With such a t, Lemma M in G gives tĀ ⊕ X = G. Now tĀ ∋ tu = x and tĀ ∋ 0, while X ∋ 0 and X ∋ x. So x = x + 0 = 0 + x is represented twice, which forces x = 0.

For |G| = p^v q^w, the p-coordinate of x·u^(−1) is x_p·u_p^(−1). It is prime to p exactly when x_p is a unit, so every x ∉ pG yields such a t. ∎

## 4. Proof of Theorem A

Assume a FACT solution with |A| = 2^α, and write n = 2^v m with m odd. Since 1320 | n, the primes 3, 5 and 11 all divide m.

**Step 1 (m-fibres).**
- Each m-fibre B_y is a complement of A mod 2^v in Z_(2^v).
- 3 ∈ A is a unit modulo 2^v.
- Fix b_y ∈ B_y. Lemma U applied to B_y − b_y shows that all elements of B in one m-fibre have the same parity.

**Step 2 (W_q-fibres, for every odd prime q | m).**
- Take u_q = 3 if q ≠ 3, and u_q = 11 if q = 3. In either case u_q ∈ I is odd and prime to q, hence a unit of G_q = Z_(2^v q^w).
- Its image lies in Ā_(2^v q^w), and each W_q-fibre B_z is a complement of Ā_(2^v q^w) (Lemma F).
- Lemma U shows that all elements of B with the same W_q-coordinate have the same parity.

No two-prime Sands theorem is used here.

**Step 3 (connection).** Let b, b′ ∈ B and let q_1, …, q_s be the odd primes of m.
- In the W_(q_1)-fibre of b there is an element b_1 ∈ B whose q_1-coordinate equals b′_(q_1) and whose other odd coordinates equal those of b (§2, every q-coordinate occurs). By Step 2, b_1 has the parity of b.
- Repeat from b_1 with q_2, and so on through q_s. This yields b* ∈ B with the parity of b and with b*_m = b′_m.
- Then b* and b′ lie in one m-fibre, so they have equal parity by Step 1.

Hence every element of B has the parity of 0 ∈ B, i.e. B ⊂ 2Z_n. This contradicts 1 ∈ B.

Therefore |A| is not a power of 2. Because 2 | |A|, it is not an odd prime power either. ∎

## 5. Proof of Theorem B

Let |A| = p^α, with 0 ∈ A ∩ B and A generating Z_n.

**Case m = 1.** A generating Z_(p^v) contains a unit, and Lemma U with G = Z_(p^v) gives B ⊂ pZ_n.

**Case m > 1.** The steps of §4 go through with parity replaced by the residue mod p:

1. A mod p^v generates Z_(p^v), so it contains a unit. Lemma U makes every m-fibre constant modulo p.
2. Fix a prime q | m. The image Ā_q of A in G_q = Z_(p^v q^w) generates G_q, since it is the image of a generating set.
   - If Ā_q contains a unit of G_q, Lemma U gives B_z − b_z ⊂ pG_q.
   - Otherwise I3 applies to the two-prime cyclic group G_q: one factor lies in pG_q or qG_q. It is not Ā_q, which generates. It is not qG_q, because the q-coordinates of B_z exhaust Z_(q^w) and so include two that differ by 1.
   - So B_z − b_z ⊂ pG_q, and the residue mod p is constant on every W_q-fibre.
3. The connection argument of §4 Step 3 then makes the residue mod p constant on B. It equals the residue of 0, so B ⊂ pZ_n. ∎

## 6. Consequences, boundaries and the exact remaining gap

**What the FACT gate now gives unconditionally.**
- |A| is even, has an odd prime factor, and is at least 6.
- |B| is divisible by 330.
- 1320 | n.
- No factor lies in a proper subgroup (route R2).

**Two-prime sizes are open.** The method does not settle |A| = 2^α q^β.

For |A| = 2^α 3^β, the analogous steps give:
- Each m′-fibre (with m′ = n/(2^v 3^w)) is a complement in Z_(2^v 3^w) that contains no G-unit difference, because 11 ∈ A is a unit there. By I3 it lies in a coset of 2G or of 3G.
- A third prime r cannot be handled by I3. Lemma U with the unit 11 (for r ≠ 11) only forbids differences that are units at both 2 and 3, i.e. it forbids cyclically adjacent residue pairs mod 6 inside each W_r-fibre.

No contradiction was derived from these constraints. The surviving explicit example A = {0,3,8,11,85,256} (|A| = 6, checkpoint05/06) is consistent with every filter used here.

**Original first unproved step (unchanged in kind).** Decide the FACT/three-mate gate for all n in 1320Z and all |A| with at least two distinct primes. On the negative side this means an all-order obstruction; on the positive side, a non-CRT, non-coset-shift witness. After that, every raw PR, isolated-word, heterogeneous-delay and STAB/GP bridge obligation remains.

The following are NOT used as a substitute for that step:
- H* (withdrawn);
- the unread Szabó 2006 proof;
- commutative-equivalence or factorization conjectures;
- residue-only cancellation;
- finite-depth misses.

**Assurance.** The finite and logical identities were checked in WRITING only. The statement of I3 was re-read in Dai 2026 §1.1; Sands' original proof is NOT reconstructed.

No scientific interpreter, calculator, eval, program, CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO was used. Exact symbols and integers only; the owner's permanent v109-A reviewer exactness finding remains and is not cured.

This is not formal, kernel, configured-family, human, executable, priority or novelty acceptance. The original cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 are unchanged.
