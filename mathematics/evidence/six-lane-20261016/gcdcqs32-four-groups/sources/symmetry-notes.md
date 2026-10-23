# Symmetry and parity notes for the gcDCQS(32⁴ : 0) search (lane notes; proofs; not peer reviewed)

Written 2026-10-17 after 08:24 PDT host clock, before any E3 run. Setting as in README §1:
a CQS(32⁴ : 0) on X = F4-labels × coordinates, x ∈ G₀, D = D_x an incomplete STS(127, 31) with
hole H = G₀∖{x}, non-hole set N = G₁ ∪ G₂ ∪ G₃ (96 points); a good colouring has 48
non-avoiding classes (each contains every hole point exactly once, hence exactly 31 hole
triples) and 16 hole-avoiding classes. These are restricted statements about particular
designs or symmetry models; none of them decides the target.

**Status of claims (file frozen 2026-10-17 after 11:50 PDT host clock; later material goes to
`symmetry-notes-2.md`).** *Proved* (pen-and-paper proofs below, lane-written, not peer reviewed):
Lemma P, Lemma P′, Claims 1–2, Lemma A, Lemma S (both parts), Lemma T, Lemma T⁺, the design
condition after Lemma T, the block-type Fact, Lemma Q′, the ν (k = 8) statement, C31, C5, and the
failure of the natural ×4 lift. *Solver-reported* (kissat 4.0.4 UNSAT, no DRAT certificate): the
G_S KM with the Lemma S exclusion (hence "no G_S design has an A4-invariant good colouring"); the
E3a, E3c, E3e colouring UNSATs, which are consistent with Lemmas A and T⁺ but not needed for
them. *Scope:* every statement concerns colourings invariant under the named symmetry (and, where
stated, designs invariant under the named group); none is a global exclusion and none bears on
the unrestricted target.

## Lemma P (parity)

Let g ≡ 2 (mod 6) and let a CQS(g⁴ : 0) and x satisfy (i) every triple of D_x containing a hole
point has its two other points in one group, and (ii) every hole-free triple of D_x meets three
different groups. Then D_x has no good colouring.

*Proof.* In a non-avoiding class the g − 1 hole triples use two points of one non-hole group
each, so the numbers r₁, r₂, r₃ of non-hole points of G₁, G₂, G₃ not covered by them are even
and sum to 3g − 2(g − 1) = g + 2. Hole-free triples of the class are transversal, so there are
at most min rᵢ ≤ 2⌊(g + 2)/6⌋ of them, and the class misses at least
(g + 2) − 6⌊(g + 2)/6⌋ = 4 non-hole points (g + 2 ≡ 4 mod 6). There are 3g/2 non-avoiding classes,
so at least 6g misses, but every non-hole point is missed by exactly one of the r classes:
3g misses in total. ∎

*Instance.* The Boolean CQS(2ᵐ)⁴ (planes {a, b, c, d}, a + b + c + d = 0, of AG(m + 2, 2) not
inside a coset of a fixed m-space U; groups = cosets of U) satisfies (i) and (ii) at every
point: a plane meeting a coset in exactly three points does not exist, so blocks have type 2+2
or 1+1+1+1. For odd m (g = 2ᵐ ≡ 2 mod 6), e.g. g = 8 and g = 32, it has no good colouring.

## Lemma P′ (parity breakers; added between the 08:31:58 and 08:33:15 PDT host-clock readings, before any E2c run)

Call a triple of D_x *parity-breaking* if it is a skew hole triple (one hole point, the other
two in different groups) or a hole-free triple of type 2+1. Each block of type 2+1+1 through x
gives exactly one parity-breaking triple of D_x and every parity-breaking triple arises so.
**Claim.** In a good colouring of D_x (g = 32) at least 32 non-avoiding classes miss exactly one
non-hole point, and each of them contains a parity-breaking triple; hence x lies in at least 32
blocks of type 2+1+1 (for a point-transitive design: at least 1024 such blocks).
*Proof.* A non-avoiding class with v vertical and k skew hole triples (v + k = 31), t transversal
and w hole-free 2+1 triples covers cᵢ ≡ kᵢ + t + wᵢ (mod 2) points of Gᵢ (i = 1, 2, 3), where kᵢ
counts skew triples meeting Gᵢ and wᵢ counts points of 2+1 triples in Gᵢ; it misses
34 − 3(t + w) ∈ {1, 4, 7, …} non-hole points. If a classes miss 1 and the other 48 − a miss ≥ 4,
then a + 4(48 − a) ≤ 96 (total misses), so a ≥ 32. A class missing one point has
(c₁, c₂, c₃) = (32, 32, 31) up to order, not all of one parity; with k = w = 0 all cᵢ ≡ t. ∎

## Colouring symmetry R = ⟨π₁, A⟩ for G_E = A4 × (F₂⁵ ⋊ ⟨A⟩)

A fixes the coordinates W = Fix(A) = {0,…,7}, so its fixed set in X is F = W × F4 (32 points);
every block with three points in F is A-invariant, hence lies in F: F carries a sub-CQS(8⁴ : 0)
(gcdcqs20 lane, Lemma F2). In D, F∖{x} has 7 hole points and 24 non-hole points; the derived
sub-design D_F is an incomplete STS(31, 7) (148 triples; a non-hole point of F lies in 15 of
them, a hole point of F in 12).

**Claim 1.** In every ⟨A⟩-invariant good colouring of D exactly 16 classes are A-invariant:
12 non-avoiding and 4 hole-avoiding, and their restrictions to F are 16 nonempty PPCs of D_F of
which exactly 4 avoid the hole of D_F (a good colouring of D_F, r = 16, s = 4).

*Proof.* A triple of D through a point p ∈ F that lies in an A-invariant class C is fixed by A
(C contains p once), hence lies in F. A non-hole p ∈ F lies in 15 triples of D_F and is missed by
at most one class, so at most 16 classes are A-invariant (gcdcqs20 Lemma F); every triple of D_F
lies in an A-invariant class, and two triples of D_F through p lie in different classes, so at
least 15 classes are A-invariant; the number of non-invariant classes is divisible by 3, so the
number is ≡ 64 ≡ 1 (mod 3): exactly 16. A hole point q ∈ F lies in every non-avoiding class, in an
A-invariant one through a triple of D_F; q lies in 12 triples of D_F: exactly 12 non-avoiding and
4 avoiding A-invariant classes. Each non-hole p ∈ F is then missed by exactly one A-invariant
class; an empty restriction would miss all 24 non-hole points of F, forcing the 12 non-avoiding
restrictions to cover F∖{x} with 7 hole triples and (24 − 14)/3 hole-free triples — not an
integer. ∎

**Claim 2.** π₁ and π₁Aʲ (j = 1, 2) fix no non-hole point, so no non-avoiding class is invariant
under them (its triple through a fixed hole point would be fixed, with two fixed non-hole
points). Hence the 48 non-avoiding classes form 4 R-orbits of size 3 (stabilizer ⟨A⟩) and 4 of
size 9; the 16 avoiding classes contain exactly 4 A-invariant ones (R-orbit structures
[1, 1, 1, 1] or [1, 3_⟨A⟩]) and 12 others (stabilizers ⟨π₁⟩, ⟨π₁A⟩, ⟨π₁A²⟩ or trivial:
[9, 3_*] or [3_*, 3_*, 3_*, 3_*]). In the anchored model with h = (0, 1) ∈ F the non-avoiding
orbits are read off the R-orbits of the triples through h (12 of them A-fixed).

**Consequences used for E3.** (a) Avoid structures in `pipeline2.py` tokens (a = π₁, b = A):
`R;b;1;a`, `R;b;1;ab`, `R;b;1;ab2`, `R;R;R;R;1;a`, `R;b;a;a;a;a`; any structure with a number
of A-invariant avoiding classes other than 4 is UNSAT by Claim 1 and is not run. (b) The fixed
sub-CQS(8⁴ : 0) must have a good colouring at x; if it satisfies the hypotheses of Lemma P
(computed per design) the model is UNSAT and is not run.

## Lemma A (added between the 08:38:17 and 08:53:23 PDT host-clock readings, after the E3a UNSATs)

**Claim.** Let a CQS(32⁴ : 0) be invariant under the diagonal order-3 map A (Fix(A) = W, |W| = 8)
and under π₁. No good colouring of D_x (x = (0, 0)) has its family of non-avoiding classes
invariant under ⟨π₁, A⟩. For ⟨A⟩-invariant good colourings the profile is forced: all 16
avoiding classes have 32 triples; of the 12 A-invariant non-avoiding classes (Claim 1), 8 contain
3 hole-free triples inside F and have 40 triples (missing 7 non-hole points) and 4 contain 2 and
have 42 triples (missing 1); the other 36 non-avoiding classes have 42 triples.

*Proof.* (1) The A-invariant triples of D are exactly those inside F = W × F4: an A-invariant
triple not fixed pointwise is an A-orbit {p, Ap, A²p}, which lies in one group and is not a
triple of D. (2) Let C be an A-invariant non-avoiding class (non-avoiding classes permuted
by A). Its triples through the 7 hole points of F are A-invariant, hence in F; let m′ ≤ 3 be the
number of its hole-free triples inside F; its other triples form A-orbits of size 3. So
31 + m = |C| = 7 + m′ + 3j, m ≡ m′ (mod 3) where m ≤ 11 counts hole-free triples of C, and C
misses 34 − 3m ≥ 7, 1, 4, 7 non-hole points for m′ = 3, 2, 1, 0, of which exactly 10 − 3m′ lie
in F (a point of F in C lies in an A-invariant triple). (3) Every triple of D through a fixed
hole point lies in an A-invariant class, so there are exactly 12 A-invariant non-avoiding
classes (12 triples of D_F through such a point). Let n₃, n₂, n₁, n₀ count them by m′. Each of the
24 non-hole points of F is missed by exactly one class: n₃ + 4n₂ + 7n₁ + 10n₀ ≤ 24. The other 36
non-avoiding classes miss ≥ 1 point each and all misses total 96:
7n₃ + n₂ + 4n₁ + 7n₀ ≤ 60. With n₃ + n₂ + n₁ + n₀ = 12 these give n₂ + 2n₁ + 3n₀ ≤ 4 and
2n₂ + n₁ ≥ 8, whose only solution is (n₃, n₂, n₁, n₀) = (8, 4, 0, 0) with equality throughout
(this gives the stated profile). (4) π₁ commutes with A, preserves F and the hole, so it permutes
the 12 A-invariant non-avoiding classes preserving m′, without fixed class (Claim 2): n₂ ≡ 0
(mod 3), contradicting n₂ = 4. ∎

*Scope.* This excludes R = ⟨π₁, A⟩ in the anchored and in the hybrid model for every
G_E-invariant design (restricted symmetry only). The E3a runs (P16, and without P16) are
consistent controls.

## Lemma S (shears; added between the 09:24:59 and 09:30:40 PDT host-clock readings, before any G_S run)

G_S = A4 ⋉ (F₂⁵ × Ψ) (`groups.py` "A4xES"): shears S_ψ(i, a) = (i, a ⊕ ψ(i)), ψ ∈ Ψ = {0, id, ω·, ω²·}
(additive injective maps F4 → {0,1,2,3} ⊂ F₂⁵). R = Stab((0,0)) = ⟨π₁, S_id⟩ ≅ A4 fixes G₀
pointwise and no non-hole point (checked by closure, 1536 elements).

**Claim.** If D_x has a good colouring whose non-avoiding classes form an R-invariant family,
then (a) R acts freely on the 48 non-avoiding classes (4 orbits of 12) and (b) no triple of D_x
has the form {u, q, q ⊕ δ} with u ∈ H, q in a non-hole group and δ ∈ {1, 2, 3}; for a
G_S-invariant design (b) is equivalent to: no block of type 2+2 has a pair whose coordinate
difference lies in {1, 2, 3}.

*Proof.* Elements of order 3 of R move the non-hole groups, so they fix no non-hole point and no
non-avoiding class (Claim 2). Let ι = S_ψ ≠ 1 and C an ι-invariant non-avoiding class. ι fixes
every hole point u, so it fixes the triple t_u of C through u: t_u = {u, q, ιq} with
ιq = q ⊕ ψ(j) for q ∈ G_j (ι has no fixed non-hole point). Such triples correspond to the 48
pairs {q, q ⊕ ψ(j)} (j = 1, 2, 3), so C uses 31 of them, and distinct ι-invariant classes use
disjoint ones: at most one non-avoiding class is ι-invariant. If C is ι₁-invariant, ι₂C is also
ι₁-invariant (V4 is abelian), so ι₂C = C and C is V4-invariant; then C, π₁C, π₁²C are three
distinct (π₁ acts freely) ι₁-invariant classes — impossible. Hence (a). Every ι-invariant triple
of D_x lies in an ι-invariant class, and the ι-invariant triples are exactly the triples
{u, q, q ⊕ ψ(j)} (a hole-free ι-invariant triple would contain a fixed non-hole point); by (a)
there are none: (b), since ψ(j) runs over {1, 2, 3} as ψ runs over Ψ∖0 for each j ≠ 0. The
coordinate difference of a pair inside a group is invariant under G_S (translations and shears
add the same vector to both points; label maps do not change coordinates) and A4 is
2-transitive on the labels, so every 2+2 block is the image of one through x with either of its
pairs inside G₀ ∋ x. ∎

*Use.* KM rows of type 2+2 with a pair difference in {1, 2, 3} are excluded before sampling
G_S designs (sound for this symmetry model); the non-avoiding orbits in the anchored model are
then automatically free.

*Computation (E3d, 10:04:17–10:04:24 PDT).* The KM of G_S with the Lemma S rows excluded
(`runs/e3d/es_kissat_km/`, 384 rows forbidden) is UNSAT for kissat in 0.016 s: no G_S-invariant
CQS(32⁴ : 0) satisfies (b), so no G_S design has an R-invariant good colouring (restricted; the
UNSAT is a kissat result, not DRAT-certified).

## Lemma T (transvection involution; written between the 10:08:43 and 10:10:21 PDT readings, before any G_T run)

G_T = A4 × (F₂⁵ ⋊ ⟨μ⟩), μ(a) = a ⊕ b₄(a)·1 (a transvection, Fix(μ) = {0,…,15}); R = ⟨π₁, μ⟩ ≅ C6.
F_μ = Fix(μ) × F4 carries a sub-CQS(16⁴ : 0); in D_x: 15 fixed hole points, 48 fixed non-hole
points, 16 moved hole points, 48 moved non-hole points (24 μ-pairs {q, μq}).

**Claim.** In a μ-invariant good colouring: (i) every μ-pair {q, μq} lies in a triple {q, μq, w}
with w fixed (the block through {x, q, μq} is μ-invariant), and with π₁ ∈ R no such w is a hole
point; (ii) exactly 32 classes are μ-invariant: 24 non-avoiding (8 R-orbits of 3) and 8
avoiding; (iii) at least 12 of the 24 μ-invariant non-avoiding classes miss ≥ 4 non-hole points
(so the P16 ansatz is impossible), and the hole-avoiding classes miss ≤ 12 points in total.

*Proof.* (i) as stated; a μ-invariant triple not inside F_μ contains a fixed point and a μ-pair.
For a fixed non-hole p, the μ-invariant triples through p (15 + 15 + 1 = 31 inside F_μ, plus e_p
μ-pair triples with w = p) lie in distinct μ-invariant classes and p is missed by one class, so
#μ-inv = 31 + e_p + δ_p with δ_p ∈ {0, 1}, the same for all p; 64 − #μ-inv is even, so
e_p + δ_p = c is odd, and Σ e_p ≤ 24 forces c = 1. For a fixed hole point u every μ-invariant
non-avoiding class contains u in a μ-invariant triple: 24 (inside F_μ) + e_u classes, e_u the
same for all 15 such u; π₁ permutes these classes freely, so 3 | 24 + e_u, and 15e_u ≤ 24 gives
e_u = 0: (ii). (iii) In a μ-invariant non-avoiding class C the 16 moved hole points lie in 8
pairs {t, μt} of hole triples avoiding F_μ; with m′ hole-free triples inside F_μ, ε μ-pair
triples and y pairs of hole-free triples outside F_μ, C misses s = 18 − 3m′ − ε fixed and
16 − 2ε − 6y moved non-hole points. Missing exactly one point forces the moved count 0 (it is
even) and s = 1, hence ε ∈ {8, 5, 2}; the 24 μ-pair triples are shared by the μ-invariant
classes, so at most 12 such classes miss one point; each other one misses ≥ 4; with ≥ 1 miss
for each of the 24 other non-avoiding classes the total 96 leaves ≤ 12 for avoiding classes. ∎

*Design condition (corollary of (ii), written 10:14:35–10:16 PDT before any steered G_T run).*
e_u = 0 for every fixed hole point u means: no block {x, u, q, μq} with u ∈ F_μ ∩ H and q ∉ F_μ.
For a G_T-invariant design this says: no 2+2 block {(i, a), (i, a ⊕ c), (j, b), (j, b ⊕ 1)} with
c ≠ 0, b₄(c) = 0 and b₄(a ⊕ b) = 1 (pair differences are translation invariant, μ fixes 1 and
b₄; labels do not move coordinates). The first G_T DFS design violates it (30 μ-fixed triples
through h = (0, 1), i.e. e_h = 6), so it has no ⟨π₁, μ⟩-invariant good colouring.

**Lemma T⁺ (written 10:16:39–10:20 PDT, after the E3e UNSAT at 10:16:39).** No G_T design has a
⟨π₁, μ⟩-invariant good colouring.
*Proof.* A G_T design is invariant under the diagonal translations, so the block through
{(1, a), (2, a), (3, a)} is {(0, a ⊕ d), (1, a), (2, a), (3, a)} for a constant d, and D_x contains
exactly one π₁-fixed triple. A π₁-invariant avoiding class therefore has ≡ 0 or 1 (mod 3)
triples, never 32: it misses ≥ 6 non-hole points, or ≥ 3 if it contains the π₁-fixed triple.
By Lemma T(iii) the avoiding classes miss ≤ 12 points in total, so at most two avoiding classes
are π₁-invariant. The μ-invariant avoiding classes (8, Lemma T(ii)) form π₁-orbits of size 1 or
3, so the number b of R-fixed ones satisfies b ≡ 8 (mod 3), b ∈ {2, 5, 8}; the other 8 avoiding
classes form R-orbits of size 6 or 2 (the latter π₁-invariant): 8 = 6c + 2d. π₁-invariant avoiding
classes number b + 2d ≤ 2, so b = 2, d = 0 and 8 = 6c — impossible. ∎
(Consistent with the kissat UNSAT of the steered sample 0 with `R;R;b;b;1;a` in < 1 s.)

## Block-type count and Lemma Q′ (written 10:20–10:26 PDT)

**Fact.** In every CQS(32⁴ : 0), n₂₂ − n₁₁₁₁ = 14848 (and 4n₂₂ + 2n₂₁₁ = 190464,
2n₂₁₁ + 4n₁₁₁₁ = 131072, counting 2+1 and 1+1+1 triples); so n₂₂ ≥ 14848, and in a
point-transitive design every point lies in ≥ 464 blocks of type 2+2, i.e. D_x has ≥ 464
vertical hole triples.

**Lemma Q′ (proved).** Let φ₁, φ₂, φ₃ be automorphisms of a point-transitive CQS(32⁴ : 0) fixing
x, such that φ_j fixes G₀ ∪ G_j pointwise and has no fixed point outside G₀ ∪ G_j (e.g. the three
label involutions of S4 that fix the label 0, all lying in ⟨π₁, φ⟩ ≅ S3). No good colouring of
D_x is invariant under all three φ_j (in particular none is ⟨π₁, φ⟩-invariant). *Proof.* Fix j.
φ_j swaps the two other non-hole groups; each of the 32 swapped pairs {q, φ_j q} lies in one
triple of D_x, whose third point is φ_j-fixed ("swap triples"). A φ_j-invariant non-avoiding
class contains every hole point in a φ_j-invariant triple: a vertical triple inside G_j (at most
16 of these, they use two points of G_j each) or a swap triple, hence ≥ 15 swap triples; so at
most 2 non-avoiding classes are φ_j-invariant. A vertical hole triple through a hole point u
inside G_j is φ_j-fixed, so its class is φ_j-invariant; the triples through u lie in distinct
classes, so u lies in ≤ 2 vertical triples inside G_j, ≤ 6 in total, and D_x has ≤ 186
vertical hole triples — fewer than the 464 forced by the Fact. ∎ (Invariance under one φ_j
alone is not excluded by this argument.)

**Involutions commuting with π₁, fixing 8 points of every group (proved).** For such an
involution ν ∈ Stab(x) (fixed set a sub-CQS(8⁴ : 0)), the Lemma T counting gives c = 1 and e_u = 3,
hence 15 ν-invariant non-avoiding classes; the other 33 non-avoiding classes would have to pair
up under ν — impossible. So no good colouring is ⟨π₁, ν⟩-invariant.

**Scope of this section and the ones above.** Each listed symmetry model — ⟨π₁, A⟩ (Lemma A,
proved), ⟨π₁, μ⟩ on G_T designs (Lemma T⁺, proved), ⟨π₁, ν⟩ with ν as just described (proved),
⟨π₁, φ⟩ ≅ S3 on point-transitive designs (Lemma Q′, proved), ⟨π₁, S_id⟩ ≅ A4 on G_S designs
(Lemma S proved; the conclusion for all G_S designs rests on a kissat UNSAT, solver-reported) —
admits no invariant good colouring under the stated hypotheses. Nothing here concerns other
symmetry groups, colourings without these symmetries, or the unrestricted target.

## GF(32) multipliers and ×4 inflation (written 10:20–10:28 PDT; parent suggestions of 10:2x)

**C31.** λ ↦ λ·a (λ primitive in GF(32)) acting diagonally fixes x = (0,0) and (i,0), i = 1, 2, 3,
and is semiregular elsewhere. Avoiding classes: 16 < 31, so all are invariant; non-avoiding:
48 = 31a + f with f ≥ 17 invariant ones. An invariant non-avoiding class contains the 31 hole
points as one orbit of hole triples and its hole-free triples form orbits of size 31 apart from
the fixed triple {(1,0),(2,0),(3,0)}; with ≤ 11 hole-free triples it has ≤ 1, so it misses ≥ 31
non-hole points; f ≥ 17 gives ≥ 527 misses > 96. Impossible.
**C5.** a ↦ a² fixes GF(2) coordinates: fixed set at x = {(0,1)} ∪ {(i,0),(i,1)}, carrying a
sub-SQS(8) whose derived design at x is a Fano plane. Each Fano line is fixed, lies in an
invariant class, and two lines meet, so ≥ 7 classes are invariant; a fixed non-hole point lies in
3 Fano lines and is missed by one class, so ≤ 4 invariant classes contain it or miss it — every
invariant class contains a fixed triple through it or misses it: ≤ 3 + 1. Impossible.
**×4 inflation.** From a CQS(8⁴ : 0) on X, put an H(4,4,4,3) on B × I₄ for each block B and a
CQS(4² : 0) (blocks {(p,i),(p,j),(q,k),(q,l)}, {i,j} and {k,l} in the same 1-factor of K₄) on
{p,q} × I₄ for every pair p, q in different groups: every triple not inside some G × I₄ is
covered once, so this is a CQS(32⁴ : 0). At x = (p₀, i₀) the derived design is 148·16 lifted
triples plus 144 "cross" hole triples {(p₀, j), (q, k), (q, l)} (j ≠ i₀). Lifting each master
class C to 4 classes (one parallel class of each triple's Latin square) gives 64 classes with 16
avoiding, but each lifted non-avoiding class needs exactly 3 cross triples, taken from base
points it misses entirely, i.e. missed by C; each base point q supplies 6 cross triples and is
missed by exactly one master class, so a master non-avoiding class C must supply 12 = 6μ_C, μ_C =
2 — impossible since a master non-avoiding class misses ≡ 1 (mod 3) points. (Other colourings of
the inflated design are not excluded; this only rules out the natural lift.)
