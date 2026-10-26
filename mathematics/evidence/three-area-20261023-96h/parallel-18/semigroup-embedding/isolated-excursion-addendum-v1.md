# Operative purity boundary and named residual cases

MathSemigroup, math-4. Actual clock immediately before creation: **2026-10-23T14:39:14-0700**.

Applies to immutable `isolated-excursion-lemma-v1.md`, SHA-256 `325067cc92a383147e0c4294951225b1dd1fc81c7f6ec301155e725015771452`, especially its §§3–4. The original stays unchanged. **CANDIDATE / PARTIAL; no broad embedding or formal acceptance.** This addendum records the exact requested dependency, a concrete rejection control, three measurable residual regimes, and one bounded extension covering the third regime under its stated isolation hypotheses.

## A. The substitution chain needs purity, not merely local r-orthodoxy

The old lemma derives, for same-grade s,v,

    s=v s' v,   v=s v' s,

using actual mutual inverses s',v'. To interpret these as s<=v and v<=s, the four multipliers

    v s', s' v, s v', v' s

MUST be idempotents. They have identity group grade, but grade alone is not idempotence. **The precise additional step is idempotent-purity of the grading.** It converts those four identity-grade products to actual idempotents, after which

    s=(v s')v=v(s' v),
    v=(s v')s=s(v' s)

are the exact book natural-order witnesses. Local r-orthodoxy is not used to turn those products into idempotents.

In the orthodox branch actually frozen in the lemma, sigma is the **least group quotient of an E-unitary orthodox semigroup**, so sigma^(-1)(1)=E(S). That classical equivalence is already an explicit baseline, and supplies the needed purity. Purity is therefore not a newly added condition to that branch, but it must not be dropped when transporting the algebraic argument to another grading or to a bare locally-r-orthodox source. The weak-E-unitary-to-E-unitary implication used here is the existing **orthodox** reduction, not an assertion about arbitrary nonorthodox regular semigroups.

## B. Concrete nonpure-grading falsifier for this algebraic step

Let H={1,h,0} be the group C2={1,h}, h^2=1, with an absorbing zero adjoined. Let K={1,g} be another C2, g^2=1, and set

    S=H cross K,
    (a,k)(b,l)=(ab,kl),
    q:S --> K, q(a,k)=k.

S is an inverse semigroup, hence regular and locally r-orthodox: every local monoid is inverse and its idempotent semilattice is a regular band. Its idempotents are exactly(1,1) and(0,1).

q is in fact the least group quotient. For any homomorphism rho:S-->L to a group, e0=(0,1) is idempotent and rho(e0)=1. Thus

    rho(a,k)=rho((a,k)e0)=rho(0,k),

so rho factors through q; the subset {0} cross K is itself a group, and q is onto K. But q is **not pure**, since q(h,1)=1 while(h,1)^2=(1,1)!=(h,1).

Take

    s=(1,g), v=(h,g), s'=s, v'=v.

Both s and v are actual self-inverse regular elements with the SAME nonidentity grade g. Every inverse-grade bridge is t=(a,g), a in H. Since H is commutative and h a h=a for a=1,h,0,

    s t s=(a,g)=v t v                             (B.1)

for EVERY such t. Hence the entire sandwich identity used by the isolated-excursion proof holds, including substitutions t=s' and t=v'. In particular s=v s' v and v=s v' s.

Nevertheless s!=v and s is not below v in the natural order. Indeed an idempotent left multiplier is either(1,1), which sends v to v, or(0,1), which sends it to(0,g); neither gives s. The supposedly idempotent multipliers v s'=s'v=(h,1) are not idempotent. The reverse comparison fails similarly.

This is an exact written falsifier of the **purity-omitted substitution implication**, not a counterexample to the original lemma or book problem. S is not weakly E-unitary: the idempotent(0,1) lies below the nonidempotent(h,1), using(0,1) as both natural-order multipliers. Thus it deliberately fails the hypothesis that supplies purity in the legitimate orthodox branch. Equation(B.1) alone is also not claimed to be an actual canonical band-congruence excursion.

## C. Three named residual regimes, frozen at the original lemma's scope

For an absolute-object-labelled word W define its gap count

    d(W)=number of consecutive arrow pairs with unmatched endpoints.

For a finite primitive derivation D, its width is max_W d(W). Primitive steps are actual M_G relations, the displayed LR_P generating identity, and band idempotency U^2=U, all with nonempty substitution words and explicit contexts. Every hypothetical collapse can be refined to such a finite derivation by congruence generation.

The original isolated-excursion lemma handles only the stated M_G/LR-only, fixed-context width-one excursions. The residual regimes are named as follows; use this priority order when classifying an uncovered derivation:

1. **MULTIGAP (R1).** At least one word has d(W)>=2. This includes a further nonloop duplication before the first gap closes, or duplication of a block already containing a gap. No R1 normalization or separating construction is proved.
2. **CONTEXT-CROSSING (R2).** No word has more than one gap, but some maximal interval of nonpath words cannot be isolated between fixed literal outer contexts A,B so that the entry is A U→A U U B and exit A V V B→A V B, with every intermediate rewrite wholly inside the marked core. Rewrites across either marked core boundary, or changing outer contexts, are excluded from the old lemma. No use of global natural-order compatibility can repair this: such compatibility is not assumed and is false in the source class.
3. **INTERIOR-IDEMPOTENCY (R3).** Width is at most one and each nonpath interval is context-isolated as above, but interior primitive idempotency steps occur in addition to M_G/LR steps. These were not included in the original statement. SectionD below supplies a candidate extension for R3 while retaining all the same purity and context hypotheses.

These are not three new scientific problems. They measure the remaining coverage of the ONE mixed-relation/idempotent-fibre construction in its orthodox diagnostic branch. The general nonorthodox Rees-typed extension remains outside that branch, not silently counted as solved by this classification.

## D. Bounded next increment: R3 steps preserving one gap are closed-path steps

This section is a complete written **candidate extension**, not an already reviewed promotion.

Let k(U) be the number of incompatible internal adjacencies of a nonempty substitution word U, and let epsilon(U)=1 if end(U)!=start(U), otherwise0. Replacing U by UU inside any fixed context changes the total gap count by exactly

    k(U)+epsilon(U).                              (D.1)

Reason: the internal gaps of the single U become those of two copies, adding k(U); the new boundary between copies contributes epsilon(U); the two outer boundaries keep the same first/last letters and therefore are unchanged. A contraction changes the count by the negative of this expression.

If an interior idempotency step has exactly one gap on both sides, (D.1) forces k(U)=epsilon(U)=0. Therefore U is a **closed path**. Its value has group grade1 and is an actual idempotent by the same pure grading as §A. The unique gap lies outside U, possibly at an outer boundary. Inserting an arbitrary bridge t at that gap consequently leaves the identity value(U)^2=value(U) valid inside the completed path context. Thus the entire family of bridge values F_t from the original proof is preserved by these R3 steps as well.

It follows that the original isolated-excursion lemma extends to arbitrary primitive interior steps **provided every interior word still has exactly one gap and the excursion retains fixed untouched outer contexts**. The M_G/LR steps are handled by the original proof; any additional interior idempotency step is handled by the closed-path argument just given. The same all-t identity s t s=v t v follows, and §A's purity-dependent natural-order argument remains unchanged.

Hence, at the new written-candidate level, R3 can be discharged under its exact width-one/isolation hypotheses. **R1 and R2 remain open.** No claim that an arbitrary derivation can be normalized to avoid them is made. A proof of such a normalization, or a direct coherent treatment of the remaining overlapping/context-changing configurations, is still needed to establish idempotent-fibre separation and the actual embedding.

## E. Review and scope status

MathShor's complete review of the predecessor `path-separation-attack-v1.md` has been read: `../shor-completion/peer-review-Semigroup-path-separation-v1.md`, reported SHA-256 `a0a0fe027cd7b27a4773e92e5f20baaecb35756dd8df19d8ac8e32fe5d05e2b8`, recorded0FATAL/0MAJOR/0 substantiveMINOR at its typed-corner/first-escape/failed-fixed-bridge scope. It does NOT review the isolated-excursion lemma, this purity falsifier, or the R3 increment. Parent consideration and the queued bounded reconstruction of that later packet remain separate.

No program, solver, enumeration, compilation, formal kernel, model CLI, new environment or shared-index edit was performed. Original snapshots are immutable. The broad book embedding statement and all finite/infinite distinctions remain unchanged.
