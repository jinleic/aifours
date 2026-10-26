# Shor FACT gate — two-prime sizes: A is equidistributed mod 2q, and B has one of three residue configurations

Owner MathShor (runtime MathShor-2). Actual `/bin/date` immediately before composing: `Sun Oct 25 23:35:36 PDT 2026` (an earlier-observation bound only).

**WRITTEN CANDIDATE, unreviewed.** These are structural restrictions in the SAME 102319 continuation. They exclude no further size, and they do not settle the Shor question or the FACT gate.

## 0. Setting and inputs

Let A ⊕ B = Z_n be a FACT solution with |A| = 2^α q^β, α, β ≥ 1, q an odd prime. By Theorem D (`shor-FACT-two-prime-crossing-partition-exclusion-v1.md`, SHA256 83b57215…87bd), q ∈ {3, 5, 7, 11}.

Notation and inputs are those of that packet:
- π(x) = x mod 2 and ρ(x) = x mod q;
- r-classes X^(r,c) for r ∈ {3, 5, 11} \ {q};
- Lemma P: every r-class is π- or ρ-constant;
- Lemma X: classes for different r cross, and every intersection contains a whole fibre X_y of Lemma F′ with N = 2^v q^w.

Throughout, X is a complement of A with 0, 1 ∈ X, so X = B or X = D3.

## 1. Lemma K2 — two crossing partitions

**Lemma K2.** Let 𝒫 and 𝒫′ be the r-classes and r′-classes of X, for two distinct r, r′ ∈ {3, 5, 11} \ {q}. Then exactly one of the following configurations holds.

- **(I)** Every 𝒫-class is π-constant and not ρ-constant, and every 𝒫′-class is ρ-constant and not π-constant. So π is a function of x mod r^(u_r), and ρ a function of x mod r′^(u_(r′)).
- **(II)** The same with 𝒫 and 𝒫′ exchanged.
- **(III)** There are (p, σ), (p′, σ′) ∈ {(0, 1), (1, 0)} with the following properties:
  - every π-constant 𝒫-class has parity p, and every ρ-constant 𝒫-class has residue σ;
  - the same holds for 𝒫′ with (p′, σ′);
  - both kinds of class occur in each partition.

*Proof.* Consider 𝒫.

(i) Suppose two π-constant 𝒫-classes have different parities. Every 𝒫′-class meets both (Lemma X), so it is not π-constant and is therefore ρ-constant (Lemma P). Now suppose some 𝒫-class C were ρ-constant, with value σ. Every 𝒫′-class meets C, so every 𝒫′-class has value σ, and ρ ≡ σ on X. This contradicts ρ(0) ≠ ρ(1). So no 𝒫-class is ρ-constant, which is (I).

(ii) Suppose two ρ-constant 𝒫-classes have different values. The symmetric argument gives (II).

(iii) Otherwise all π-constant 𝒫-classes share one parity p, and all ρ-constant 𝒫-classes share one residue σ. Both kinds occur, because X is neither π-constant nor ρ-constant. Every x then has π(x) = p or ρ(x) = σ. The seeds 0 and 1 give (p, σ) ∈ {(0,1), (1,0)}, exactly as in Theorem D §3.

Now 𝒫′ is not in case (i): that would make every 𝒫-class ρ-constant, all with the one value σ, so ρ would be constant. Symmetrically 𝒫′ is not in case (ii). So 𝒫′ is also in case (iii), and the configuration is (III). ∎

## 2. Proposition F — A is equidistributed mod 2q

**Proposition F.** For every FACT solution with |A| = 2^α q^β (α, β ≥ 1):

    |A ∩ (j + 2qZ)| = |A|/(2q)  for every j ∈ Z_(2q).

*Proof.* Apply Lemma K2 to X = B. Two partitions are available in every case:
- for q ∈ {3, 5, 11}, the two members of {3, 5, 11} \ {q};
- for q = 7, any two of {3, 5, 11}.

In each configuration there is a π-constant class D of one partition and a ρ-constant class E of the other:
- (I): any 𝒫-class and any 𝒫′-class;
- (II): symmetrically;
- (III): both kinds occur in each partition.

By Lemma X, D ∩ E contains a whole fibre B_y. All of its elements have one parity and one residue mod q, hence one residue mod 2q. So B_y − b ⊂ 2qZ_N.

Covering then gives |A_N ∩ (j + 2qZ_N)| = (N/(2q))/|B_y| = |A|/(2q) for every j. Reduction mod N preserves residues mod 2q. ∎

For q = 7 this is Proposition E(c) again. For q ∈ {3, 5, 11} it is new.

## 3. Which configurations the seeds allow

For X = B, the seed residues (π, ρ) of 0, 1, 7, 13, 14 are:

| q | 0 | 1 | 7 | 13 | 14 |
|---|---|---|---|---|---|
| 3 | (0,0) | (1,1) | (1,1) | (1,1) | (0,2) |
| 5 | (0,0) | (1,1) | (1,2) | (1,3) | (0,4) |
| 7 | (0,0) | (1,1) | (1,0) | (1,6) | (0,0) |
| 11 | (0,0) | (1,1) | (1,7) | (1,2) | (0,3) |

Configuration (III) requires every b to satisfy π(b) = p or ρ(b) = σ:
- (p, σ) = (0, 1) fails at 7 unless ρ(7) = 1, i.e. unless q = 3.
- (p, σ) = (1, 0) fails at 14 unless ρ(14) = 0, i.e. unless q = 7.

**Corollary F1.**
- **q ∈ {5, 11}.** B is in configuration (I) or (II). So EVERY fibre B_y (N = 2^v q^w) lies in one coset of 2qZ_N. Moreover:
  - its parity is a function of y mod r^(u_r) alone, and its residue mod q a function of y mod r′^(u_(r′)) alone, for {r, r′} = {3, 5, 11} \ {q} in one of the two orders;
  - if v_3(n) = 1, the residue mod q cannot be the function of y mod 3, because 1, 7 and 13 are congruent mod 3 but not mod q.
- **q = 3.** B is in (I), (II), or (III) with (p, σ) = (0, 1) for both partitions; in the last case every b ∈ B is even or ≡ 1 mod 3.
- **q = 7.** By Theorem D's three-partition argument, (p_r, σ_r) = (1, 0) for every r, which is Proposition E(a).

For X = D3 ⊇ {0, 1, 2}, (III) with (p, σ) = (0, 1) is compatible with the seeds for every q. No restriction is claimed for D3 beyond Lemma K2.

## 4. What this does and does not give

**Consistency check: Theorem C recovered.** For q ∈ {5, 11} and |A| = 2q, Corollary F1 together with Proposition F makes every fibre a coset of 2qZ_N, which gives Theorem C's contradiction again. This is a consistency check, not a new result.

**Boundary for |A| = 4q and beyond.** For |A| ≥ 4q, each class mod 2q of A has |A|/(2q) ≥ 2 elements. A doubly-constant fibre is then b + 2qY, where Y is a common complement of the sets (A^(j) − a_j)/(2q). Its period has a full 2-part or a full q-part only if those sets have suitable differences, and the seeds force none of them, since 0, 3, 8 and 11 lie in four different classes mod 2q.

No further size is excluded here. The open sizes below 52 remain:

    12, 14, 18, 20, 24, 28, 30, 36, 40, 42, 44, 48, 50

**First unproved original step.** Unchanged.

## 5. Assurance

WRITTEN only. Every residue and counting step was checked by hand with exact integers, and the seed table entries were computed by hand. No scientific interpreter, calculator, eval, program, CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO was used. The owner's permanent v109-A reviewer exactness finding (f32c51d3…8584) remains and is not cured.

This is not formal, kernel, configured-family, human, executable, priority or novelty acceptance. The cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 are unchanged.
