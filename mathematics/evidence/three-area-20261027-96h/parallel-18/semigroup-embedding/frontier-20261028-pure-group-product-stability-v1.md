# Exact R/L and canonical-faithfulness stability under a pure-group product

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 17:30:17 PDT 2026**. Same-author bounded Bic×Rees checks are reported in §8; they do not prove the universal claim. No novelty or original all-source closure is claimed.

## 1. Main theorem: exact equivalence, not merely a product witness

Let A be any nonempty regular semigroup with an **onto idempotent-pure group homomorphism** `θ:A→G`. Suppose there is a faithful homomorphism over θ

`ι_A(a)=(b_a,θ(a)) : A→B_A⋊G`,

where B_A belongs to the actual band variety V of bands whose local corners are regular bands, and G acts by automorphisms. The group coordinate of ι_A must be this SAME θ. No identity in A is assumed.

Let C be ANY nonempty regular semigroup whose actual syntactic idempotence quotient `q_C:C→D=C/τ_C` is idempotent pure and completely simple. Let its canonical V-band/actor map be `(β_C,q_C)`. Put S=A×C, define τ_S by ALL two-sided source idempotence tests (allowing absent factors), and take its actual canonical map `(β_S,q_S)`.

**Claim.**

1. `τ_S = ker(θ) × τ_C`, so the actual pure actor is `S/τ_S ≅ G×D`, with `q_S(a,c)=(θ(a),q_C(c))`.
2. Canonical faithfulness is EXACTLY stable:

   `κ_S is injective  iff  κ_C is injective`.                  (2)

3. The same exact equivalence holds **separately** for same-actor R-idempotent separation and same-actor L-idempotent separation. The two obligations are not conflated and neither is silently replaced by injectivity of β on every source element.

If A and C also satisfy the original locally r-orthodox hypotheses, then S is an original-class weakly E-unitary locally r-orthodox regular source (§5). Thus taking A to be the explicit bicyclic monoid gives this exact lifting/restriction result for EVERY original C, including C for which the original R/L obligation is still open. It does not solve those obligations for arbitrary C: the theorem identifies the product problem with the SAME residual problem for C.

## 2. Preliminary facts and pure quotient of A

For regular A and pure onto θ, every idempotent maps to 1, and θ(a)=1 iff a is idempotent. For any mutual inverse a' of a, `θ(a')=θ(a)^(-1)`. The image is the entire specified group; if one starts with a homomorphism into a larger group, regularity makes its image a subgroup.

The actual syntactic congruence τ_A is exactly ker θ. Equality of group images makes all two-sided idempotence tests equal by purity, including an absent factor interpreted by the group identity. Conversely, if a τ_A b, choose a'∈V(a); the context `x=a'`, `y=absent` compares the idempotent a'a with a'b, giving θ(a')θ(b)=1 and θ(a)=θ(b). This uses no adjoined common source identity.

A nonempty regular semigroup contains an idempotent: choose any a and a'∈V(a), and aa' is idempotent. Fix an arbitrary such actual e0∈A only for the restriction argument. Its θ-image is 1; no common unit, finiteness, selected table or other structure is needed.

## 3. Why actual two-sided tests detect τ_C

We require a detail that is false to assume merely from a finite sample: for this C, equality of idempotence tests `xcy↔xdy` for all **actual** x,y∈C already implies c τ_C d, including both individually absent contexts.

Because q_C is onto and pure, equality of those tests implies equality of all actual two-sided tests for `q_C(c),q_C(d)` in D. In arbitrary Rees coordinates `D=M[H;I,Λ;P]`, for `u=(i,g,λ)`, `v=(j,h,μ)` put

`K_u(ν,k)=p_(ν,i)g p_(λ,k)`, `K_v(ν,k)=p_(ν,j)h p_(μ,k)`.

For every ν,k, actual context elements with suitable group coefficients can make the u-product the idempotent of any chosen H-class; the equivalent v-product being idempotent forces `K_u(ν,k)=K_v(ν,k)`. Conversely these equalities imply the tests for both actual factors. They also imply either one-absent test: a right-context test is equivalent to `K_u(η,k)v=1`, and a left-context test to `u K_u(ν,a)=1`, with the same expression for v. For both factors absent, if u is idempotent then `g p_(λ,i)=1`, and the K equality at `(ν,k)=(μ,i)` yields `p_(μ,j)h=1`, so v is idempotent; the reverse interchanges them. These are group equalities, valid for noncommutative H and nonnormalized P.

Therefore q_C(c),q_C(d) agree on **all** D¹ idempotence tests. For arbitrary x,y∈C¹, apply q_C and use its purity to transfer the test back; this gives c τ_C d. No assertion that a completely simple actor has a global identity or that D's syntactic relation is trivial is needed.

## 4. Exact product congruence and actual actor

If θ(a)=θ(b) and c τ_C d, then every actual/absent product context gives equal idempotence results in A by group-coordinate purity, and equal results in C by τ_C. Since a product pair is idempotent iff BOTH components are idempotent, `(a,c) τ_S (b,d)`.

Conversely suppose `(a,c) τ_S (b,d)`. Choose a'∈V(a), c'∈V(c) and any actual idempotent e0∈A. The actual contexts

`x=(a',c')`,     `y=(e0,c'c)`

make x(a,c)y idempotent: θ(a'a e0)=1 and q_C is not needed to see `(c'c)^2=c'c`. Equivalence makes x(b,d)y idempotent, and the A component has group image `θ(a)^(-1)θ(b)`; hence θ(a)=θ(b).

Now for arbitrary **actual** x_C,y_C choose product contexts `x=(a',x_C)`, `y=(e0,y_C)`. The A components of both products have θ-image1 and are idempotent. The product tests therefore yield

`x_C c y_C ∈E(C) iff x_C d y_C ∈E(C)`.

Section 3 upgrades this to c τ_C d, including the missing-context cases. This proves the full equality `τ_S=ker θ×τ_C`, with no A identity or numerical enumeration. Since θ and q_C are onto, q_S has exactly the product image G×D. Product purity follows because `(θ(a),q_C(c))` is an idempotent iff θ(a)=1 and q_C(c) is idempotent, exactly when both source components are idempotent.

G×D is completely simple: if `D=M[H;I,Λ;P]`, it is the Rees matrix semigroup `M[G×H;I,Λ;((1_G,p_(λ,i)))]`. Ordinary Rees representation of D is a named classical structural import; the product identification is the displayed multiplication, not an external embedding theorem.

## 5. Original source hypotheses under products

A×C is regular, since pairs of mutual inverses are mutual inverses. If each factor is locally r-orthodox, then for any idempotent `(e,f)` its local monoid is `eAe×fCf`; the product of orthodox regular monoids is orthodox and its idempotent band is the product of their regular idempotent bands. A product of regular bands satisfies the regular-band identity componentwise. Thus S is locally r-orthodox, including collapsed/one-element corners and no identities in the global factors.

Since q_S is a pure map to the completely simple semigroup G×D, S is weakly E-unitary. Indeed natural-order witnesses map to natural-order witnesses. Natural order on a completely simple Rees semigroup is equality: if u=f v=v g with f,g idempotent, the two products force u,v to have the same source row and column; then f has v's row and the Rees product of that idempotent with v is v, so u=v. Consequently if an idempotent e≤a in S, q_S(a)=q_S(e) is idempotent and purity makes a idempotent.

This uses the SAME actual quotient in §4. It does not infer the original printed question from an arbitrary direct product, and it does not assume the local-r property for a factor where it was not given.

## 6. Constructing the product invariant: sufficiency and separate R/L

Choose Rees coordinates `D=M[H;I,Λ;P]`. Let B_C be the canonical V-band of C with H-action α^C and coefficient β_C. Put `B=B_A×B_C`, still a V-band, and let `G×H` act componentwise:

`α_(g,h)(u,v)=(α^A_g u, α^C_h v)`.

The Rees coordinates for G×D have sandwich weights `(1_G,p_(λ,i))`. For EVERY source `(a,c)` define the actual band coefficient

`b_(a,c)=(b_a,β_C(c))`.

The A component satisfies `b_a α^A_θ(a)(b_b)=b_(ab)` because ι_A is a homomorphism. The C component satisfies its full canonical M relation with its actual weight. Thus the pair coefficients satisfy EVERY source product relation with the **actual** q_S weight. Sending each product generator `X_((g,h),(a,c))` to `α_(g,h)(b_a,β_C(c))` induces an equivariant band homomorphism `H_S:B_S→B` with

`H_S β_S(a,c)=(b_a,β_C(c))`.                              (3)

This construction is valid even if κ_C has not been proved injective.

For an idempotent e∈A, θ(e)=1. Since ι_A is faithful, distinct A idempotents have distinct b_e. Now take same-q_S R-idempotents `(e,u),(f,v)` in S with equal β_S. Equation (3) gives b_e=b_f and β_C(u)=β_C(v); thus e=f. The R relations `xy=y, yx=x` hold componentwise, and actor equality gives q_C(u)=q_C(v). If C has its same-q R-separation property, u=v. The proof for the L convention `xy=x, yx=y` is identical with the roles of its product equations retained. Thus C's R property implies S's R property, and C's L property separately implies S's L property. The stronger all-idempotent SEP implication also follows, without any Green assumptions.

If κ_C is injective, the explicit physical map

`(a,c) ↦ ((b_a,β_C(c)),(θ(a),q_C(c)))`

is injective: equality determines a by ι_A and c by κ_C. The all-generator map (3) then shows κ_S injective, without assuming a canonical all-host theorem.

## 7. Restriction: necessity in the SAME actor

Conversely suppose S's R-idempotent separation holds; choose the actual e0∈E(A) from §2. The map `c↦(e0,c)` is a semigroup embedding of C into S, and its q_S actor values are `(1_G,q_C(c))`. Restrict B_S's `G×H` action to the subgroup `{1_G}×H`. For every c,d∈C, the M relation in S gives

`β_S(e0,cd)=β_S(e0,c) α^S_(1_G,w_C(c,d))(β_S(e0,d))`.

Therefore `X_(u,c)↦α^S_(1_G,u)(β_S(e0,c))` defines an equivariant band homomorphism `H_C:B_C→B_S`; it maps β_C(c) to β_S(e0,c).

If C had a same-q_C R pair e≠f with β_C(e)=β_C(f), H_C would give a same-q_S R pair `(e0,e)≠(e0,f)` with equal β_S, contradicting S's R property. Thus S's R property implies C's R property. The L proof is separate and identical with the L identities. Likewise all-idempotent SEP of S implies SEP of C.

If κ_S is injective, the actual restricted physical map

`c↦(β_S(e0,c),q_C(c))`

is faithful, because equality implies equality of κ_S(e0,c) and κ_S(e0,d). Applying H_C to a hypothetical equality κ_C(c)=κ_C(d) then shows c=d. Hence κ_C is injective. Together with §6 this proves the equivalence (2), and proves the R/L and full SEP equivalences separately.

This is a genuine all-derivation relative-conservativity statement for this product operation. It does NOT assert that every original source is such a product, that θ may be an arbitrary non-pure actor, or that a C failing these tests has been found.

## 8. Explicit application and actually performed bounded check

Take A=Bic with θ(i,j)=i-j and the faithful upper-tail semilattice model `(i,j)↦(A_i,i-j)` from `frontier-20261028-trivial-action-boundary-bicyclic-v1.md`, SHA `7102febd323afebcf93cd9cc8af59741448f772bb9c9e737ae07c54aa4392f71`. Its multiplication/faithfulness are proved directly there. For every original C, Bic×C remains original and its R, L, SEP and full κ obligations are **equivalent** to C's corresponding obligations. This includes unital/nonunital and finite/infinite C; Bic×C is always infinite.

For the earlier completely simple18-element C with a nontrivial sandwich matrix, the checker `frontier-20261028-bicyclic-rees-checker-v1.py` SHA `b29630a070182fda0807d5d7518919c449b48fbfc7fc8650a3b96ba442659510` executed at native17:19:14 PDT, exit0/timeout30s, and reported72 bounded labels, 5329 bounded contexts,8 exact finite-C τ classes, 82 ordered same-q idempotent pairs including12 R and12 L, successful actor/host checks, and1944 wrong-action control mismatches. It checks every finite-C context but only a bounded sample in Bic; §§3–7 are the universal argument. It is the same-author checker, not an independent proof.

## 9. Exact limits, imports and next gap

Named ordinary inputs are: Rees representation of a completely simple semigroup, closure of the local regular-band identity under products, and the prior source-specific SQ-E proof that every original C has its **actual** pure CS syntactic quotient. The displayed Rees-context argument, τ-product identity, canonical action and both R/L directions are proved here; no Szendrei embedding theorem, old globalization outcome or previous external review is a premise. Source-specific SQ-E is reconstructed in `frontier-20261028-cryptogroup-band-retraction-v1.md` §2.1 and remains a peer-review/import boundary, not a newly formalized proof.

The result does not manufacture a faithful C-host when C's obligation is open. It rules out two possible unsound inferences: a product-counterexample cannot arise solely from adjoining this already-embeddable pure-group factor, and the product invariant does not settle the factor. A true general solution still needs source-level information on C, or an actual C producing collapse. The mathematical novelty and prior literature are unassessed; printed Question 2 and the full non-product original class are not solved. Disjoint proof review and independent certificate checking remain required before adoption.
