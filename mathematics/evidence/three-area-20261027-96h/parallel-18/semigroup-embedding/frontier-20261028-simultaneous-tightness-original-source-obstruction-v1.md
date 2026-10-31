# An actual original-class source defeats simultaneous tightness of its Rees entries

**NEW AUTHOR CANDIDATE with an exhaustive finite same-author check; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 18:20:55 PDT 2026**. This falsifies a concrete proposed proof bridge, not the original embedding question. Full independent finite-witness/proof review and literature/priority assessment remain outstanding.

## 1. The exact false premise

The reverse-fibre theorem in `frontier-20261028-rees-reverse-fibre-weu-v1.md`, SHA `96b34ec43125dabe1e9cc33cdc7055c37b0933a1f5c81a424913b5dd5230f52b`, showed that every sandwich of a weak-E Rees source over a pure group quotient satisfies the intrinsic RF identity. The earlier tight-lift theorem establishes faithful embedding when a **single faithful A→B⋊G model** makes all P entries tight.

A tempting bridge is:

> For every regular original-class Rees source over A, one can choose a faithful model over its fixed pure group quotient in which ALL intrinsic RF-good sandwich entries actually used by P are simultaneously tight.

**This statement is false.** The concrete A and 3×3 P in §§2–4 yield a45-element original-class source with TWO distinct RF-good entries p,x in the SAME group fibre. In ANY faithful model `ι(a)=(b_a,θ(a))`, if both were tight then

`b_p=b_1 α_(θ(p))(b_1)=b_1 α_(θ(x))(b_1)=b_x`.

Their group coordinates also agree, so ι(p)=ι(x), contradicting faithfulness. This proof is independent of the choice of band variety, representation, action or target cardinality. It only excludes this **unmodified, simultaneous-tight A-factor lift**. It does not exclude a host whose source coefficients depend on row/column, a different source presentation, a non-tight action-dependent invariant or an actual canonical embedding.

A previous attempt to generalize the inverse-base result “RF(p) iff p is greatest in its group fibre” is likewise false for this A: both p and x are RF-good but neither lies below the other. This is the promised precise obstruction to transporting the inverse-semigroup max/preorder proof to arbitrary regular-band bases.

## 2. A five-element regular pure-group monoid

Let R={0,1} be the **right-zero** band, and let C2 act on it by flipping the two labels. Define A to be the four-element semidirect product R⋊C2 together with a new identity `1_A`. Write its four nonidentity elements `(i,g)`, i,g∈{0,1}, with

`(i,g)(j,h)=(j+g, g+h)`  (all additions mod2),

and extend multiplication by the identity. This is associative: R is a band, C2 acts by automorphisms, and adjoining a unit preserves associativity. All four nonidentity elements have mutual inverses (the exact table/checker below verifies every element), and 1_A is its own inverse, so A is regular.

The idempotents are `1_A,(0,0),(1,0)`; their products form the right-zero band R with an identity adjoined. It is a regular band: the subband R is rectangular and any evaluation involving the identity either reduces to an R identity or is trivial. The group projection

`θ(1_A)=0`, `θ((i,g))=g`

is onto C2 and idempotent pure. Let

`p=(0,1)`, `x=(1,1)`.

For ANY a=(j,1) in their common inverse fibre and ANY k∈{0,1},

`a (k,1) a = (j,1)=a`.

Thus p and x are distinct RF-good elements of the same θ-fibre. Every idempotent e of A satisfies `e p=p` and `e x=x`; in particular x is not e p for any idempotent e, so x≰p, and similarly p≰x. There is no greatest element in the θ=1 fibre. Both are nonunits because the four nonidentity elements form a proper two-sided ideal.

For complete reproducibility, the checker labels `(0,0),(0,1),(1,0),(1,1),1_A` by 0,1,2,3,4 respectively and uses the exact product table

```text
0 1 2 3 0
3 2 1 0 1
0 1 2 3 2
3 2 1 0 3
0 1 2 3 4
```

The displayed operation gives this table directly; the finite program exhausts associativity, regularity, E-closure/regular-band identity, group homomorphism/purity, both RF predicates and the two failed natural-order comparisons.

## 3. A concrete original-class 45-element Rees source

Let I=Λ={0,1,2}, and take the FULL source S=M[A;I,Λ;P] with

`P=[[1_A,1_A,1_A],[1_A,p,1_A],[1_A,1_A,x]]`.

Every row and column contains the unit 1_A. Hence S is regular: for s=(i,a,λ), choose an inverse a' in A and use the actual inverse candidate `(0,a',0)` because `p_(λ,0)=p_(0,i)=1_A`.

The entries 1_A,p,x all satisfy RF, so the reverse-fibre theorem makes the natural actor

`r(i,a,λ)=(i,θ(a),λ) ∈ D=M[C2;I,Λ;θ(P)]`

pure. D is completely simple, whose natural order is equality, so S is weakly E-unitary. Because E(A) is a regular band and S is regular, the local-corner embedding `(i,b,λ)↦b p_(λ,i)` in `frontier-20261028-rees-local-corner-fibre-maxima-v1.md`, SHA `af71b4d3c7765ada362b99b6dbfc096d6635b165486800d8a6620b901c4b3133`, proves every source local monoid orthodox with regular-band idempotents. Thus S satisfies the full original class, not merely a band relaxation. The finite program also independently checks these source conditions directly from all45 elements.

The C2 sandwich matrix of D has zeros in its first row/column and ones only at(1,1),(2,2). Its three rows and three columns are distinct. For actor `(i,g,λ)`, the Rees-context K-array has `K(0,0)=g`, `K(ν,0)=Q_(ν,i)+g` and `K(0,k)=g+Q_(λ,k)`. These entries determine g,i,λ, so the actor's syntactic relation is equality. Purity and onto-ness give the ACTUAL source quotient `q_τ=r` (not merely a possible actor). The exhaustive source context check in §5 independently verifies this finite claim.

## 4. The example is outside earlier easy subclasses, but no nonembedding is inferred

S is **not globally orthodox**. Put `e=(0,1_A,0)` and `f=(1,p,1)`. Both are idempotents: P_(0,0)=1_A and p³=p. But `ef=(0,p,1)` has diagonal sandwich P_(1,0)=1_A and its square has middle p²=(1,0)≠p, so ef is not idempotent.

S is **not locally inverse**: eSe consists of its fixed row0/column0 component and is isomorphic to A because P_(0,0)=1_A. Its two idempotents (0,0),(1,0) do not commute. Its local idempotents nevertheless form a regular band, as required.

S is **not completely regular**, so it is not a cryptogroup. The actual element s=(1,1_A,1) has no commuting mutual inverse. If t=(j,a,μ) commuted with s, comparison of source Rees rows and columns would force j=μ=1. But then sts has middle `p a p`, which lies in A's proper ideal A\{1_A}; it cannot equal the middle 1_A of s. Thus s is in no subgroup. The full finite check agrees. Interestingly, its Green H relation IS a congruence; non-complete-regularity alone excludes the cryptogroup class. No contrary H-congruence claim is made.

The actual source has distinct same-q R-idempotent pairs (18 ordered pairs in §5); it has no distinct same-q L-idempotent pair in this one finite example. The counterargument in §1 does not require a chosen pair or claim that any such pair collapses in B_q.

## 5. Exact experiment, controls and corrected failed expectations

`frontier-20261028-simultaneous-tightness-obstruction-checker-v1.py`, SHA `b0e8ac71eef57113a8de122e350507370259760fa110b42985121b28632a5521`, executed `/opt/homebrew/bin/python3 -B` at **Wed Oct 28 18:19:14 PDT 2026**, timeout30s, exit0:

```text
A_size=5 idempotents=[0, 2, 4] RF_good_same_fibre=(1, 3) incomparable=True
S_size=45 idempotents=25 actual_actor=18
same_q_idempotent_pairs=46 R_pairs=18 L_pairs=0
PASS A regular/RB/pure-theta; S regular/WEU/local-r/nonorth/non-locally-inverse; complete tau
H_congruence=True non_completely_regular_element=(1, 4, 1)
PASS source outside cryptogroup class; no conclusion about any faithful host
CONTROL nontight idempotent sandwich yields actual WEU failure: (1, 4, 1) (1, 0, 1)
```

The standalone checker starts from the literal five-element multiplication table, not the preceding search implementation. It exhausts all source associativity/regularity checks, natural-order WEU tests, local idempotent closure/regular-band identities, every 46² actual/absent two-sided context per source element for τ, principal ideals for H and all same-q R/L idempotent pairs. Its control replaces one sandwich by a non-RF idempotent and verifies a concrete `x³=x²≠x` WEU violation. This is one same-author finite verifier and one control, not triple-independent witness certification.

The development history is material: the first run at18:17:58 failed my assertion that BOTH R and L pairs must be nonvacuous; the actual result has R pairs but no L pairs. The second at18:18:22 failed my expectation that H must be noncongruent; the finite source has H congruent. A third at18:18:53 correctly rejected an attempted assumption that H-congruence implies complete regularity. I corrected those false expectations and reran; the final output above is the actual passing run. No author/earlier artifact or source table was overwritten, and none of the failed expectations is claimed as a theorem.

The source A was discovered by the bounded local-band-submonoid search `frontier-20261028-orthodox-submonoid-rf-search-v1.py`, SHA `aa9fdd46710a7e33958f1479578208ea2febe69ed598a5ee2c2ac5a30123dbad`, which reported the five-element table. The separate source checker above reconstructs A directly from the displayed table rather than importing that search engine, but both are same-owner code. Search coverage is not an all-semigroup classification.

## 6. Exact consequence and remaining frontier

The central RF-to-**simultaneously tight model** implication is false for actual original sources: two distinct same-label P entries make it impossible by faithfulness alone. No choice of a different faithful A-band representation can repair that particular fixed-A/fixed-θ tightness requirement. The counterexample also shows that generalizing “RF iff fibre maximum” from inverse bases to all regular-band orthodox monoids is invalid.

The next correct target is an invariant that can retain the two P entries as different band data while allowing their equal actor weights, or a genuine full canonical collapse. This note does NOT claim such an invariant exists or fails, nor that S is nonembeddable. The printed first question, Question 2 and full registered original-class R/L obligation remain unresolved beyond the separately proved subclasses. No novelty, source-priority, external-model, human or formal/kernel acceptance is claimed; Main must freeze a disjoint review and independently verify the finite source before adopting any witness-level statement.
