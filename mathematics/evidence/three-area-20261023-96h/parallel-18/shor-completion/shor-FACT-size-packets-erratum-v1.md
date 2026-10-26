# Erratum E1 to the FACT size packets — source of "1320 | n", and Theorem C at v_2(n) = 2

Owner MathShor (runtime MathShor-2). Actual `/bin/date` immediately before composing: `Sun Oct 25 23:45:42 PDT 2026`.

**WRITTEN, unreviewed.** This erratum is additive. The pinned packets are NOT edited:

| packet | SHA256 |
|---|---|
| `shor-FACT-prime-power-side-exclusion-v1.md` | f286f623…8a29 |
| `shor-FACT-size-2q-exclusion-v1.md` | d3a796c9…559b |
| `shor-FACT-two-prime-crossing-partition-exclusion-v1.md` | 83b57215…87bd |
| `shor-FACT-two-prime-balance-and-configuration-v1.md` | cd4d1b22…44f8 |

## E1.1 Citation correction

The first three packets say that consolidated-v1 §1.2 (or §1.2–§1.3) "proves 1320 | n". That is inaccurate.

Consolidated-v1 §1.2 (SHA256 1697ed1a…ca83, lines 62–67) proves only:
- 2 | |A| and 330 | |B|, hence 660 | n;
- the inequality n ≥ 1320.

It refers to "the stronger inherited full-code 1320 divisibility" without re-deriving it.

So, for FACT factorizations as such, only 660 | n is established in that section. In particular 4 | n, i.e. v_2(n) ≥ 2, but not v_2(n) ≥ 3. The divisibility 1320 | n is available only through the inherited full-code statement, which applies to factorizations that actually come from a completion.

## E1.2 Which results depend on v_2(n) ≥ 3

**Theorems A, B and D and Propositions E and F.** These use only 330 | |B| and 2 | |A|. From those they need just two facts: 3, 5 and 11 divide n, and 2q divides n. They therefore hold for EVERY FACT factorization, with no change.

**Theorem C.** §1 sets v = v_2(n) ≥ 3, and the §3 recursion uses this. With v ≥ 3 the proof stands as written. The case v = 2 is supplied below, so Theorem C also holds for every FACT factorization with 660 | n.

## E1.3 Supplement: Theorem C when v = v_2(n) = 2

Set N = 4q^w. The steps of Theorem C change as follows.

**§1–§2 (dichotomy and type-q fibres).** Unchanged. They use only that N is even and N/q is even, and both hold.

**§3 (type-2 fibres).** Level 1 lies in Z_(N/2) = Z_(2q^w).

- *An odd element at level 1.* If S_e or S_o contains an odd element, the leaf argument applies at ℓ = 1 exactly as written. Each piece Y has size N/(2q) = 2q^(w−1) = |qZ_(2q^w)|, so it is a coset. Hence B_y = b + 2qZ_N.
- *No odd element at level 1.* Otherwise both sets lie in 2Z_(N/2). Split every piece by parity and halve. The level-2 sets lie in Z_(N/4) = Z_(q^w), which has ODD order. They contain 0 and 2, the images of 0, 8 and of 3, 11.

  In that case 2 is a unit of Z_(q^w). Lemma U, with |S| = q and unit 2, forbids exactly the x with q ∤ x. So each level-2 piece lies in a coset of qZ_(q^w).

  Its size is |Y|/2 = q^(w−1) = |qZ_(q^w)|, so it is a full coset. Lifting through the two halvings, B_y is a union of cosets of 4qZ_N.

**§4 (descent).** Use H = 4qZ_N × {0}. It is contained in 2qZ_N and in every type-2 period, and |H| = N/(4q) = q^(w−1). Then

    |B̄| = |B|/|H| = (2q^(w−1) m′)/q^(w−1) = 2m′,

which is prime to q. The seeds keep distinct images, because m′ ≥ 15. The q-multiplier collisions in Theorem C's §4 table then apply unchanged. ∎

## E1.4 Unchanged

- The cumulative FACT size status in park-v14.json and in the Theorem D and Proposition F packets.
- The open-size list 12, 14, 18, 20, 24, 28, 30, 36, 40, 42, 44, 48, 50.
- NOT_PROVED for the original Shor question.

**Assurance.** WRITTEN only, checked by hand with exact integers. No scientific interpreter, calculator, eval, program, CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO was used. The owner's permanent v109-A reviewer exactness finding (f32c51d3…8584) remains. This is not formal, kernel, configured-family, human, executable, priority or novelty acceptance.
