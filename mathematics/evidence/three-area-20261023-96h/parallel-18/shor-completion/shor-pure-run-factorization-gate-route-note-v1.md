# Shor completion — the pure-run factorization gate (route note v1)

Owner MathShor (runtime MathShor-2). Last actual `/bin/date` before composing this note: `Sun Oct 25 12:18:37 PDT 2026` (an earlier-observation bound).

Push: `primary-continuation-20261025-102319-v1.json`, MathShor-2 entry LF275–298.

**Status.** WRITTEN route control plus one CONDITIONAL reduction. **The full Shor target is NOT_PROVED.** This note gives:
- no finite completion;
- no nonexistence proof;
- no novelty claim;
- no review or formal check.

It consolidates checkpoints 01–04 of this push so they can be reviewed. The baseline `shor-heterogeneous-completion-consolidated-v2.md` (SHA-256 `164a31e4…9852`) and its parent interface are unchanged.

## 1. The gate

C = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11 b{1,a,a^2}.

**FACT.** There exist n ≥ 1 and A, B ⊆ Z_n such that:
- the sum A + B = Z_n is direct;
- {0,3,8,11} ⊆ A and {0,1,7,13,14} ⊆ B, with distinct residues.

**Necessity.** Let M be a finite raw UD factor-complete superset of C, with pure-a word a^n. Its pure-run polynomials satisfy PR, LR + (1 − z^n)H = S_n (v2 §2). Here L includes the endpoint marker and the start exponents r of the words b^e a^r, and R includes the marker and the end exponents s of the words a^s b^d. H is a nonnegative series, so LR ≡ S_n mod z^n − 1 with 0/1 coefficients: a direct cyclic factorization. From C, L ⊇ {0,1,7,13,14} (b, ba, ba^7, ba^13, ba^14) and R ⊇ {0,3,8,11} (b, a^3b, a^8b, a^11b). This is also the RSS89 theorem as quoted by Cordero (arXiv 2301.13566 Thm1.1).

**Literature status.** Cordero 2019 (LATA note, p.7) writes: *"We still do not know if there exists a factorisation associated to Shor's code, i.e. if there exists an integer n such that (L ⊇ {0,3,8,11}, R ⊇ {0,1,7,13,14}) is a (Sands) factorisation of Z/nZ."* So no actual PR-saturated prefix containing C is known to exist. The assigned negative quantifier ranges over a set not known to be nonempty.
- A proof of ¬FACT would answer the Shor question negatively at the written PR interface.
- A FACT witness is only the first positive step; the v2 joint-delay and all-arity obligations remain.

## 2. Named imports (not reconstructed here)

- **I1 (Tijdeman multiplier).** If A ⊕ B = Z_n and gcd(t, |A|) = 1, then tA ⊕ B = Z_n. Stated in Dai 2026 (arXiv 2601.07135v2) §1.1, from Coven–Meyerowitz/Tijdeman.
- **I2 (Sands 1979 Thm 3, = Dai 2026 Thm 2.2).** A ⊕ B = Z_n iff |A||B| = n and Div(A) ∩ Div(B) = {n}, where Div(E) = {gcd(e − e′, n)}.
- **I3 (Sands 1979; Tijdeman).** If A ⊕ B = Z_n with n = p^a q^b, or with n "good", then one factor lies in a proper subgroup. Szabó 1985, Lagarias–Szabó 2001 (n = 900) and Dai 2026 give counterexamples for other n.
- **I4 (Cordero 2023, J. Automata Lang. Combin.; arXiv 2301.13566).** Prop 2.6, Prop 3.3 and Thm 7.2, the multiplier stability of complete bayonet codes. Its proof uses the unread Prop 3.5.

## 3. Results

**R0 (a-order).** Any finite completion has 660 | n by RSS89 and I1, and 1320 | n with I4 added.

For the 660 part, write P_R = {0,3,8,11} (the a^k b^+ exponents) and Q_R = {0,1,7,13,14} (the b^+ a^k exponents). Each line below gives two distinct representations of one element; the coprimality of t is then excluded by I1.

| Multiplier | Set | Identity | Conclusion |
|---|---|---|---|
| t = 2 | P_R | 0+7 = 6+1 | 2 divides \|P_R\| |
| t = 3 | Q_R | 0+3 = 3+0 | 3 divides \|Q_R\| |
| t = 5 | Q_R | 3+5 = 8+0 | 5 divides \|Q_R\| |
| t = 11 | Q_R | 0+11 = 11+0 | 11 divides \|Q_R\| |
| t = 8 | Q_R | 0+8 = 8+0 | \|Q_R\| is even |

For the extra factor 2 via I4: d2 = 2 gives (a^3ba^8)(b) = (a^3b)(a^8b). If 8 ∤ n, write n = 4m with m odd and take d2 = m+2; it is coprime to |P′| and sends a^3ba^4 to a^3ba^8, giving the same relation.

Cordero 2019 already states 330 | n, with n = 330k, k ≥ 4. R0 only sharpens that statement.

**R1.** By I2, FACT is equivalent to a cardinality-plus-disjoint-gcd-division-set problem with the two containments.

**R2.** In a FACT solution, neither factor lies in a proper subgroup: 3, 8 ∈ A with gcd 1, and 1 ∈ B. So FACT is a counterexample to Sands' (equivalently Tijdeman's) conjecture mod n. With I3 this needs n bad with at least three primes, already implied by R0. There is no contradiction, since such counterexamples exist.

**R3 (no CRT-separable solution).** Take a coprime split n = n1·n2 with n1, n2 > 1 and a product solution. Some component, say n1, is prime to 3. In it, gcd(3, n1) = 1 = gcd(1, n1), so 1 lies in both division sets, contradicting I2 in Z_{n1}.

**R4 (|A| ≥ 6).** Suppose A = {0,3,8,11} = {0,3} ⊕ {0,8}. Then X = B + {0,8} complements {0,3}. A complement of {0,3} takes alternate positions on every +3 orbit. But X contains 0 and 9 = 1 + 8, three orbit steps apart. This is a reproof: the earlier restricted result, a pure-end word a^l b^β with l ≥ 26, already gives |A| ≥ 5, and R0 makes |A| even.

**R5 (residue invariance).** Let p | n be prime with p ∤ |A| or p² | n. Then every t_k = 1 + k·n/p is prime to |A|, so I1 gives t_k A ⊕ B = Z_n. Also t_k a = a + k(a mod p)·n/p. Summing the indicator identities against characters of k ∈ Z_p shows that each A^(r) + B is (n/p)-periodic, where A^(r) = {a ∈ A : a ≡ r mod p}. This holds on the A side for p ∈ {2,3,5,11}. It is recorded as a tool and not yet used.

**Definitions for R6–R9.** Fix *data*: a coprime split Z_n = ∏ Z_{m_i} (r ≥ 1) and divisors d_i | m_i with d_i ≥ 2. Let κ_i be reduction mod d_i in component i.
- A **product factor** is P = ∏ P_i with each P_i a complete residue system mod d_i.
- Q is a **universal complement** if Q ⊕ P′ = Z_n for EVERY product factor P′ with the same data.
- A pair q, q′ is **fully differing** if κ_i(q) ≠ κ_i(q′) for all i.

**R9 (universal complements).** A universal complement has no fully differing pair.

*Proof.* Suppose q, q′ are fully differing. Each δ_i = q_i − q′_i is in a nonzero class mod d_i. Pick P′_i as a complete residue system mod d_i containing 0 and δ_i. Then q + 0 = q′ + (q − q′) with 0, q − q′ ∈ P′, so the sum is not direct.

*Coverage.* Every translate of H = ∏ d_i Z_{m_i} is universal. A coset-shift move preserves universality. The move takes X = c + K_I ⊆ Q, where K_I = ∏_{i∈I} d_i Z_{m_i} and I is an arbitrary component set, and translates it by any g ∈ ∏_{i∈I} Z_{m_i}. This works because X + P′ = c + (∏_{i∈I} Z_{m_i} × ∏_{j∉I} P′_j) for every P′. Therefore all finite single-level or nested coset-shift constructions are universal. In particular this covers Szabó's 1985 construction as described by Lagarias–Szabó: their Z_900 B is three disjoint single-component coset shifts of 30Z_900, checked by hand. It also covers Dai 2026 Definition 1.1 Szabó pairs.

**R8 (no product-plus-universal FACT).** In a FACT solution, if one factor is a product factor for some data, the other factor is not a universal complement for that data.

- **Orientation α (A is the product factor).** A component with d_i = 1 forces m_i = 1, so every d_i ≥ 2. Then 0, 1 ∈ B are fully differing.
- **Orientation β (B is the product factor, with e_i := d_i).** Because B is a product,
  Div(B) = {(g_i) : g_i ∈ D_i ∪ {m_i}} minus the all-m vector, with D_i the gcds of differences inside P_i.
  1. The difference 3 ∈ A − A needs a component with 3 | m_i and 3 ∉ D_i ∪ {m_i}. An odd such m_i would give gcd(7−1, m_i) = 3 ∈ D_i. So the 3-part lies in the even component 1.
  2. By R0's sizes, |B| is divisible by 330 and |A| is even. Hence 6 | e_1 and m_1/e_1 is even.
  3. Containment of 1, 7, 13 in P_1 excludes e_1 ∈ {6, 12}: either value forces m_1 = e_1.
  4. So no e_i divides 3, and 0, 3 ∈ A are fully differing.

  In both orientations R9 applies. ∎

**R7 (conditional, NOT a substitute).** Hypothesis H\*: every Sands-conjecture counterexample has, up to automorphism and factor translation, one product factor and one universal complement for some data. Under H\*, R2 and R8 give ¬FACT, hence no finite completion of C.

H\* is OPEN. It is my formalization of Dai 2026's remark that no example essentially different from Szabó's is known. Dai proves the classification only for Z_{(pqr)²} with |A| = |B| = pqr, which FACT cannot meet. Conversely, any finite completion of C would yield a Sands counterexample of a new type, outside all known constructions.

## 4. Exact residual

- Decide FACT for some n ∈ 1320Z with |A| ≥ 6 even and 330 | |B|.
- **Negative route:** ¬FACT directly, or H\* for such n.
- **Positive route:** a FACT witness in which neither factor is in product-plus-universal form, followed by all v2 bridge obligations.

Neither is supplied. Explicit nonsubstitutes:
- H\*;
- the commutative-equivalence and factorization conjectures;
- residue-only cancellation;
- finite-depth misses.

## 5. Assurance

- Written only. No scientific program, eval, enumeration, replay, solver, nested agent, CLI or GO was used.
- I1–I4 are named imports. R3, R4, R8 and R9 are elementary written proofs given here. R5 is a written derivation from I1.
- Sources actually read: Cordero 2019 (full), Lagarias–Szabó 2001 (full), Dai 2026 LF26–116 (extracted), Cordero 2023 arXiv windows as listed in checkpoint-01; De Felice 2022 by grep only.
- No independent review, formal check or novelty clearance. Same-family, same-harness work.
