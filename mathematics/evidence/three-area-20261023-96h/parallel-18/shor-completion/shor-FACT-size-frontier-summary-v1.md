# Shor FACT gate — size frontier summary after the 102319 continuation

Owner MathShor (runtime MathShor-2). Actual `/bin/date` immediately before composing: `Sun Oct 25 23:54:59 PDT 2026`.

**WRITTEN, unreviewed index.** This file collects statements and scopes. The proofs are in the pinned packets named below. Two small restrictions (R1, R2 in §3) are proved here for the first time. Nothing here settles the Shor question, which remains **NOT_PROVED in either direction**.

## 1. The gate

Every finite raw UD factor-complete superset of the literal 16-word Shor code C yields a direct factorization

    A ⊕ B = Z_n,  I = {0,3,8,11} ⊂ A,  J0 = {0,1,7,13,14} ⊂ B,

together with two further complements of the same A: D2 ⊇ {0,2,4,6} and D3 ⊇ {0,1,2}. This is consolidated-v1 §1–§2 (`shor-common-complement-uniform-trades-consolidated-v1.md`, 1697ed1a…ca83).

Consolidated-v1 §1.2 gives 2 | |A|, 330 | |B|, 660 | n and n ≥ 1320. The stronger statement 1320 | n is the inherited full-code divisibility (erratum E1, `shor-FACT-size-packets-erratum-v1.md`, d5760461…a5f1).

The FACT gate is necessary for a completion, not sufficient. Every raw PR, isolated-word, delay and STAB/GP bridge obligation of the baseline (`shor-heterogeneous-completion-consolidated-v2.md`, 164a31e4…9852) remains in addition.

## 2. Size results

| result | statement (FACT solutions) | imports | packet |
|---|---|---|---|
| Theorem A | \|A\| is not a prime power | written Lemma M only | `shor-FACT-prime-power-side-exclusion-v1.md` (f286f623…8a29) |
| Theorem B | general: if \|A\| = p^α and A generates, then B ⊂ pZ_n | M; I3 (Sands 1979) only when no unit seed exists | same |
| Theorem C | \|A\| ∉ {6, 10, 22} | M only (v_2(n) = 2 case in E1) | `shor-FACT-size-2q-exclusion-v1.md` (d3a796c9…559b) + E1 |
| Theorem D | \|A\| ≠ 2^α q^β for every odd prime q ∉ {3, 5, 7, 11} | M only | `shor-FACT-two-prime-crossing-partition-exclusion-v1.md` (83b57215…87bd) |
| Proposition E | if \|A\| = 2^α 7^β: B ⊂ odd ∪ 7Z, D3 ⊂ even ∪ (1+7Z), A equidistributed mod 14 | M only | same |
| Proposition F | if \|A\| = 2^α q^β: A equidistributed mod 2q; for q ∈ {5, 11} every N-fibre of B lies in one coset of 2qZ_N | M only | `shor-FACT-two-prime-balance-and-configuration-v1.md` (cd4d1b22…44f8) |

**Unconditional WRITTEN consequence.** |A| is even and not a prime power. If it has exactly two primes, it is 2^α q^β with q ∈ {3, 5, 7, 11}, and it is not 6, 10 or 22.

The open sizes below 52 are:

    12, 14, 18, 20, 24, 28, 30, 36, 40, 42, 44, 48, 50

**Conditional consequence (named import I4).** Cordero 2023 (arXiv 2301.13566v1, p. 17) states Lemma 5.2 as Theorem 5.5 of Szabó–Sands 2009: in a normalized factorization of Z_n with |P| = p^α q^β, P or Q lies in a proper subgroup. The statement was read in the primary arXiv text. One "≠" sign was lost in text extraction, and Cordero's own use of the lemma fixes the reading. The proof is NOT read and NOT reconstructed.

In FACT both A and B generate. So, conditional on I4, |A| has at least three distinct primes, and the smallest candidates are 30, 42, 60, 66, 70, 78, 84, 90. Theorems A, C and D are independent written proofs of special cases. No novelty or priority is claimed.

## 3. Additional written restrictions (unpromoted, no contradiction)

**R1 (|A| = 4q, q ∈ {5, 11}).** Every class mod 2q of A is a pair whose two elements are congruent mod 4q².

*Proof.* Recorded in checkpoint 30. Proposition F and Corollary F1 make every fibre b_y + 2qY_y, where Y_y is a common complement of pairs {0, s_j}. So B is periodic under ⟨4qg⟩ × {0}, with g = gcd(s_j, N/2q). Unless 2q | g, that subgroup has the full 2-part or the full q-part of |B_y|. The descent would then give 2 ∤ |B̄| or q ∤ |B̄|, contradicting 330 | |B̄|. ∎

**R2 (|A| = 14).** Every even element of A is ≡ 0 mod 4 and every odd element is ≡ 3 mod 4. Hence A mod 28 = {0, 3} + 4Z_28.

*Proof.* By Proposition E(c), A is a complete residue system mod 14. So every 7-class of A_N (N = 2^v 7^w) is a pair at difference ≡ 7 mod 14. A ρ-constant fibre (B − b)/7 is then a common complement of pairs {0, t_j} with every t_j odd. It is therefore periodic under 2g with g = gcd(t_j, N/7) odd, and the fibre is 14gZ_N-periodic.

Suppose the conclusion fails. Then S_e = A_e/2 or S_o = (A_o − 3)/2 has an odd element, so in Theorem C §3 (valid for q = 7) the leaf occurs at ℓ = 1. Every π-constant fibre is then a single coset of 14Z_N. Hence B is periodic under 14gZ_N × {0}, whose 2-part 2^(v−1) equals that of |B|, and |B̄| is odd.

The multiplier 8, prime to |B̄|, collides: 0 + 8 = 8 + 0, using 1 ∈ B and 8 ∈ A. Contradiction.

So ℓ ≥ 2, which is the stated congruence condition. Since A has one element in each class mod 14, this condition determines A mod 28. ∎

Consequences of R2 recorded only:
- The mod-28 tiling forces B to meet residues 0 and 2 mod 4 equally often, and residues 1 and 3 mod 4 equally often.
- π-constant fibres of B with several residues mod 7 have the form b + {0, δ} + 28Z_N with δ ≡ 2 mod 4 and 7 ∤ δ.

## 4. Exact remaining gap

**Negative direction.** Decide the FACT and three-mate gates for all remaining |A| and all n with 660 | n:
- unconditionally, the two-prime sizes with q ∈ {3, 5, 7, 11} beyond 2q, and every size with three or more primes;
- under I4, only the latter.

A gate contradiction covering every size and every such n would by itself prove non-completion, because every completion yields a FACT solution. The raw bridge obligations matter only in the positive direction.

**Positive direction.** A FACT and three-mate witness in the open size set that is neither CRT-separable nor coset-shift. Then every raw PR, isolated-word, heterogeneous-delay and STAB/GP obligation.

**Not substitutes.** H* (withdrawn), commutative-equivalence and factorization conjectures, residue-only cancellation, the homogeneous or seed ansatz, finite-depth misses, and positive-potential or Kraft surrogates.

**Method limits.**
- Lemma P needs |A| to have exactly two primes.
- Lemma K needs three crossing partitions, available only for q ∉ {3, 5, 11}.
- For q = 7, the seed pattern J0 ⊂ odd ∪ 7Z is compatible with Proposition E.

## 5. Assurance

WRITTEN only. Exact integers throughout, hand-checked. Source reads, /bin/date, shasum and wc only. No scientific interpreter, calculator, eval, program, CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO.

The owner's permanent v109-A reviewer exactness finding (f32c51d3…8584) is disclosed and not cured. This is not formal, kernel, configured-family, human, executable, priority or novelty acceptance. The cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 are unchanged.
