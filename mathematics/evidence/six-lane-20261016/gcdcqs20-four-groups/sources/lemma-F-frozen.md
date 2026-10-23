# Lemma F, Corollaries F1, F2 — frozen statement for later review

Frozen 2026-10-17 (host clock after 06:15 PDT) by worker `MathMcDsqs38` at the parent's request.
**Scope: restricted-symmetry obstructions only.** They say that certain *symmetric* colourings
or certain *group-invariant* CQS cannot exist. They say NOTHING about the existence of a
gcDCQS(20⁴ : 0) without that symmetry. Controls: `sources/lemma-F-controls.json` (produced by
`code/lemma_controls.py`; all three PASS). The working note with context is
`sources/obstruction-lemmas.md`.

## Hypotheses (common)

H1. (X, 𝒢, A) is a CQS(gⁿ : 0): 𝒢 partitions X into n groups of size g, every 3-subset of X not
contained in a group lies in exactly one block of A, no 3-subset of a group lies in a block.
H2. x ∈ G₀ ∈ 𝒢; D = {B∖{x} : x ∈ B ∈ A}; H = G₀∖{x}. gn − 1 ≡ 1 (mod 6) (so r = χ′(gn−1) =
gn/2 and every point of X∖G₀ lies in exactly r − 1 triples of D).
H3. 𝒞 is a partition of D into r partial parallel classes (pairwise disjoint triples).
H4. ρ is a permutation of X preserving A, with ρ(x) = x, of prime order q, and ρ maps every class
of 𝒞 onto a class of 𝒞. F = Fix(ρ)∖{x}; L = {t ∈ D : t ⊆ F}.

(The good-colouring condition "exactly s classes avoid H" is not used.)

## Statements

**Lemma F (q = 3).** Under H1–H4 with q = 3, for every p ∈ F∖H:
  χ′(F, L) ≤ N ≤ r_L(p) + 1,
where N is the number of ρ-invariant classes, r_L(p) = #{t ∈ L : p ∈ t}, and χ′(F, L) is the
least number of partial parallel classes partitioning L.

*Proof.* (i) If t ∈ L lies in C then t = ρt ∈ ρC, so ρC = C: all triples of L lie in ρ-invariant
classes, and intersecting triples of L lie in different classes: N ≥ χ′(F, L). (ii) If C is
ρ-invariant and p ∈ t ∈ C with p ∈ F, then p ∈ t ∩ ρt and ρt ∈ C, so ρt = t; a ρ-invariant
triple of a permutation of order 3 containing a fixed point is pointwise fixed, so t ∈ L. Hence
at most r_L(p) ρ-invariant classes contain p. (iii) p ∉ G₀ lies in r − 1 triples, all in
distinct classes, so exactly one class misses p; therefore N ≤ r_L(p) + 1. ∎

**Corollary F1.** Under H1–H4 with q = 3, if |F| = 7 and |F ∩ H| = 1, no such 𝒞 exists.
*Proof.* For p ≠ p' in F (not both in H, as |F ∩ H| = 1) the triple of D through {p, p'} is
mapped to itself by ρ and has two fixed points, hence its third point is fixed: (F, L) is an
STS(7); any two of its 7 lines meet, so χ′ = 7, while r_L(p) = 3: 7 > 4. ∎

**Corollary F2.** Under H1 alone (no colouring), let ρ preserve A and fix the groups setwise
acting on (i, a) as (i, h(a)) with h a permutation of the coordinates of order 3 fixing exactly k
coordinates, 2 ≤ k < g. Then {0..n−1} × Fix(h) carries a CQS(kⁿ : 0) (the blocks through three
fixed points), so (n = 4) its derived designs are incomplete STS(4k−1, k−1): necessarily
k − 1 ≡ 1, 3 (mod 6) and 4k − 1 ≡ 1, 3 (mod 6). For g = 20 and order 3: k ∈ {2, 5, 8, 11, 14, 17};
k ∈ {5, 11, 17} impossible. (With H2–H4 and x = (0, y), h(y) = y, k = 2 is excluded by F1.)
*Proof.* A block through three fixed points B ⊇ T is ρ-invariant (ρB ⊇ T), and a permutation of
B fixing three of its points fixes the fourth; so the fixed points carry a CQS(kⁿ : 0). ∎

## One exact control each (`sources/lemma-F-controls.json`)

| Statement | Control | Recorded outcome |
|---|---|---|
| Lemma F (no restriction when F ⊆ H) | g = 8, A4 × C8 design `runs/c0b/g8_a4c8_c3/summary.json:0`, ρ = π₁: F = 7 hole points (F ⊆ H); the certificate `runs/c0b/g8_a4c8_c3/gcdcqs8_s0_a0.txt` (both checkers PASS) has a ρ-invariant colouring at x | PASS: lemma consistent with an existing ρ-invariant good colouring |
| Corollary F1 | A4 × A5 design `runs/e2a/A4xA5/summary.json:0`, ρ = conj(c₀): F = {1, 20, 21, 40, 41, 60, 61}, one hole point, L an STS(7), r_L = 3, all lines meet | PASS: predicted no ρ-invariant colouring; the 11 recorded ρ-invariant SAT models of that design are UNSAT |
| Corollary F2 | A4 × AGL(1,4) × Z5: m_ω has order 3 and fixes exactly k = 5 coordinates (4 is not ≡ 1, 3 mod 6) | PASS: predicted no invariant CQS; recorded KM status UNSAT |
