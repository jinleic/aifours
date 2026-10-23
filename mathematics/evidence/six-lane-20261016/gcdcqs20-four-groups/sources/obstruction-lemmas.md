# Fixed-point lemmas for symmetric good colourings (lane notes; proofs; not peer reviewed)

Setting: (X, 𝒢, A) a CQS(gⁿ : 0) (empty stem), x ∈ G₀ ∈ 𝒢, D = D_x the derived design (an
incomplete STS(gn−1, g−1) with hole H = G₀∖{x}), and 𝒞 a good colouring of D (r = χ′(gn−1)
partial parallel classes, s of them avoiding H). For gn − 1 ≡ 1 (mod 6) (the target: 79) a point
of X∖G₀ lies in (gn−2)/2 = r − 1 triples of D, so it is missed by exactly one class; a hole
point lies in (gn−g)/2 triples and is missed by exactly the s hole-avoiding classes.

Let ρ be an automorphism of the CQS with ρ(x) = x, of prime order q, such that ρ maps every class
of 𝒞 onto a class of 𝒞 (𝒞 is ρ-invariant). Put F = Fix(ρ)∖{x} and L = {t ∈ D : t ⊆ F}.

**(a) Closure.** If p ≠ p' ∈ F are not both in H, ρ maps the triple of D through {p, p'} to
the triple through {ρp, ρp'} = {p, p'}, i.e. to itself, fixing two of its points and hence the
third. So (F, L) is a partial triple system covering every pair of F not inside H once.

**(b)** Every t ∈ L lies in a ρ-invariant class: t = ρt ∈ ρC, and each triple is in one class.

**(c)** If C is ρ-invariant and t ∈ C contains p ∈ F, then ρt ∈ C and p ∈ t ∩ ρt, so ρt = t.
For q = 3 a ρ-invariant triple with a fixed point is pointwise fixed, so t ∈ L.

**Lemma F (q = 3, gn − 1 ≡ 1 mod 6).** For every non-hole p ∈ F the number N of ρ-invariant
classes satisfies χ′(F, L) ≤ N ≤ r_L(p) + 1, where r_L(p) = #{t ∈ L : p ∈ t}. Hence
χ′(F, L) > r_L(p) + 1 for some non-hole p ∈ F rules out every ρ-invariant good colouring.
*Proof.* By (c) a ρ-invariant class contains p only in a triple of L, distinct classes contain
distinct triples, so at most r_L(p) ρ-invariant classes contain p, and at most one class misses
p. The lower bound is (b) together with disjointness inside classes. ∎

**Corollary F1 (Fano obstruction).** If |F| = 7 and |F ∩ H| = 1, then by (a) (F, L) is an STS(7)
(every pair of F is covered), χ′ = 7 and r_L(p) = 3 for non-hole p: 7 > 4, no ρ-invariant good
colouring.

**Corollary F2 (fixed coordinates in "diagonal" groups).** Let the group act on (i, a) by a
permutation of the group index times a permutation h of the coordinates (the same in every
group), and let ρ = (1, h) have order 3 with h fixing exactly k ≥ 2 coordinates, x = (0, y),
h(y) = y. A block through a triple of fixed points is ρ-invariant with three fixed points, hence
lies inside Fix(ρ) ∪ {x} = {0,1,2,3} × Fix(h); these blocks form a CQS(k⁴ : 0), whose derived
designs are incomplete STS(4k−1, k−1): this needs k − 1 ≡ 1, 3 (mod 6) and 4k − 1 ≡ 1, 3 (mod 6).
An order-3 permutation of 20 coordinates has k ∈ {2, 5, 8, 11, 14, 17, 20}; k ∈ {5, 11, 17} is
impossible, k = 2 gives the STS(7) of Corollary F1, so only k ∈ {8, 14} (h ≠ 1) can occur in an
R-invariant good colouring. Elements (π, h) with π a 3-cycle fixing the group index 0 fix only
hole points of D (F ⊆ H): no constraint from Lemma F.

## Consistency with the computations (restricted models; the lemmas, not the SAT runs, are the proofs)

| Run | element of R (or of the group) | fixed structure in D | lemma | computed |
|---|---|---|---|---|
| E2a A4 × A5, R = ⟨π₁, conj(c₀)⟩ | conj(c₀) fixes coordinates c₀, c₀⁻¹ (k = 2) | 1 hole + 6 non-hole points (Fano) | F1 | 22/22 UNSAT |
| E2b/E2c A4 × PSL(2,19), R ∋ m₄³ (C3×C9, C9, C9tw = ⟨π₁m₄⟩ ∋ (π₁m₄)³ = m₄³) | y ↦ 7y fixes 0, ∞ (k = 2) | Fano | F1 | 380/380 UNSAT |
| E2a A4 × AGL(1,4) × Z5 (group element, not only R) | m_ω fixes the 5 coordinates (0, c) (k = 5) | would be a CQS(5⁴ : 0) | F2 | KM UNSAT (no invariant CQS) |
| E1 A4 × C20, R = ⟨π₁⟩ | π₁ fixes only G₀ | F = H | none | UNKNOWN (300 s) |

**Design rule.** In diagonal groups, every order-3 element of R must fix only hole points (like
π₁) or fix k ∈ {8, 14} coordinates; in the latter case the ρ-invariant classes (≤ 2k of them)
restrict to a good colouring of the derived design of the fixed sub-CQS(k⁴ : 0).

## Lemma Q (involutions fixing two groups; added after E9, ≈06:50 PDT)

Setting H1–H3 of `lemma-F-frozen.md` with n = 4, g = 20, and ι an involution preserving A with
ι(x) = x that fixes G₀ and one further group G_ℓ pointwise and has no fixed point outside
G₀ ∪ G_ℓ (e.g. a label involution of AGL(2,2) acting on Q(S)).
**Claim.** At most two non-avoiding classes of a good colouring are mapped onto themselves by ι.
*Proof.* The 40 points outside G₀ ∪ G_ℓ form 20 two-cycles of ι; the triple of D through such a
pair is ι-invariant with its third point in H ∪ G_ℓ ("swap triples": exactly 20 of them). Let C
be an ι-invariant non-avoiding class. It contains every hole point q (19 of them) in a triple t_q
with ιt_q ∈ C and q ∈ t_q ∩ ιt_q, so ιt_q = t_q: either t_q = {q, p, p'} with p, p' ∈ G_ℓ, or a
swap triple. The first kind uses two of the 20 points of G_ℓ, so at most 10 of them, and C
contains at least 9 swap triples. Swap triples lie in one class each, so at most 20/9 < 3 such
classes exist. ∎
**Consequence (E9).** For Q(S) every triple of D through h = (0,1) lies, apart from h, inside one
group G_c (the blocks through (0,0),(0,1) are lifts {(0,0),(0,1),(c,y),(c,w)} and
{(0,0),(δ,0),(0,1),(δ,1)}), so it is fixed by the label involution fixing c. In any S3 = ⟨π₁,φ⟩
model every non-avoiding class is therefore fixed by one of the three label involutions and each
involution fixes 10 of them > 2: no such colouring exists. Computed: E9 hybrid and anchored
S3 models on Q(S₀), Q(S₁) all UNSAT in ≤ 0.015 s (consistent; restricted symmetry only).
