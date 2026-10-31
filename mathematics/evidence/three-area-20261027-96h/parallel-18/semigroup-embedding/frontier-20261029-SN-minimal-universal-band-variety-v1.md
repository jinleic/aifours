# SN is the least possible band variety for a positive universal original theorem

**Status: NEW AUTHOR WRITTEN UNIVERSAL NECESSITY with a finite test source; UNREVIEWED / UNADOPTED.** This does NOT prove SN suffices for all original sources. It proves that no strictly smaller band variety can replace it, even after arbitrary CS actors/actions are allowed. No novelty is asserted.

## 1. Exact nonabelian opposite physical product

Let `D=M[G;I,Λ;P]`, with G acting by automorphisms α on a band B. Represent `D^op=M[G^op;Λ,I;P^T]`, where `g∘h=hg` in G^op and `P^T_(i,λ)=P_(λ,i)`. Let G^op act on B^op by `γ_g=α_(g⁻¹)`. Then

`P(B,D)^op ≅ P(B^op,D^op)`

via

`(b,(i,g,λ)) ↦ (α_(g⁻¹)(b),(λ,g,i))`.                  (O)

Indeed, the source opposite product of x=(b,(i,g,λ)) and y=(c,(j,h,μ)) is the original yx, with band `c α_(hP_(μ,i))(b)` and group coordinate `hP_(μ,i)g`. Applying(O) gives band

`α_(g⁻¹P_(μ,i)⁻¹h⁻¹)(c) · α_(g⁻¹)(b)`.

In the target, the first actor weight in G^op is `g∘P_(μ,i)=P_(μ,i)g`, whose γ-action is `α_(g⁻¹P_(μ,i)⁻¹)`. Multiplication in B^op reverses the two transformed band factors and gives exactly that expression; the actor products also agree. The map is bijective because the action is by automorphisms. No commutative-group assumption is used.

`frontier-20261029-physical-opposite-S3-checker-v1.py`, SHA `b7454fb33d4c91a6cdd975bbe8ead752bb75a8b5629bebc1d9467012f2fc96d3`, verified all28,224 products and bijectivity for a168-element physical host with the nonabelian S₃ action on a7-element symmetric band and noncommuting sandwich entries, before Thu Oct29 01:15:37 PDT2026. The general statement is the written calculation, not the sample.

## 2. A source25 forces its host band to generate all SN

Let B5 be the symmetric five-band B_(2), and `K=B5×B5^op`, a25-element seminormal band. K is an original source: every band is regular and weakly E-unitary, and SN bands are locally regular. The exact finite-generator theorem `frontier-20261029-SN-25band-variety-carrier-v1.md`, SHA `42c33ed57571a25722ac1914847d3e65d0d166fe80fa93fafca8912e3aed2cf0`, proves `var(K)=SN` under its fully named fresh word/splitting inputs.

For ANY faithful physical host `K→P(C,D)` with C an arbitrary band and D an arbitrary CS actor, fix idempotents in the two K factors. The resulting source slices B5 and B5^op also embed in the same host. The direct essential-factor theorem `frontier-20261028-symmetric-band-essential-factor-v1.md`, SHA `2980fab2dddf055f2892b95940676b48d18054cf0daa5be0af9acaca78bcbbce`, says any faithful physical host of B5 has a band-coordinate embedding of B5 into its band. Hence B5 embeds in C.

Apply(O) to the B5^op slice. It gives a physical embedding of B5 into a product whose band is C^op. The same essential-factor theorem embeds B5 in C^op; reversing products embeds B5^op in C. Therefore C contains BOTH five-bands, and

`var(C) ⊇ var(B5×B5^op) = SN`.                         (V)

Thus if C itself is required to lie in SN, its generated variety is EXACTLY SN. No source-actor quotient, group gauge, finite-band enumeration or hypothetical universal original embedding is used for(V).

## 3. Consequence for the printed target

Let W be ANY variety of bands and suppose EVERY original regular weakly-E locally-r source embeds into some W-band-by-CS physical product, with actor/action chosen arbitrarily for each source. Apply that assertion only to the explicit25-element band K. Its host band C lies in W, and(V) gives `SN⊆var(C)⊆W`. Therefore

`ANY universally sufficient band variety W MUST contain SN`.

The printed seminormal-band target is consequently the smallest possible band variety for an affirmative theorem under the stated physical convention. This is a NECESSITY/optimality-of-variety statement, not proof of the open universal existence assertion. The finite K itself trivially has an SN-band host with singleton actor; we are not presenting it as a Q1 counterexample.

All fresh normal-form, splitting, essential-factor and source-convention inputs remain independently unreviewed. No formal proof, independent finite-witness certification, full printed-product identification, originalQ1/Q2 solution or novelty is claimed.
