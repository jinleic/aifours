# Positive generalized-Q2 sources whose ACTUAL PURE syntactic quotients are negative

**Status: NEW AUTHOR WRITTEN general construction plus full literal12→9 certificate; UNREVIEWED / UNADOPTED.** This is a closure/nonreduction result for the generalized-Q2 image target, not a solution of largest-class Q2 and NOT a counterexample to originalQ1. The positive sources below are nonorthodox and NOTWEU.

## 1. A whole positive nonorthodox source family

Let D=M[G;I,Λ;P] be ANY NONORTHODOX completely simple semigroup. Adjoin an absorbing zero 0_A to G and form the UNREDUCED Rees semigroup

`S=M[G^0;I,Λ;P]`.

This has a DISTINCT zero-middle element `(i,0_A,λ)` for every cell; they form a rectangular-band ideal, not a single global zero. The nonzero-middle part is D. Let L={0,1} be the two-element semilattice. There is an onto homomorphism

`π:P(L,D)=L×D→S`, `π(1,(i,g,λ))=(i,g,λ)`, `π(0,(i,g,λ))=(i,0_A,λ)`.

The group acts trivially on L. Products agree because any factor with level0 produces a zero-middle element with the left row and right column, and otherwise the original D product is retained. Idempotents are exactly the upper D-idempotents and one lower zero-middle element per cell; these are all distinct under π. Thus π is IDEMPOTENT-SEPARATING. S is already the entire homomorphic image of a SEMILATTICE-by-CS physical host, a fortiori a positive fullSN generalized-Q2 source.

S is completely regular and locally inverse: its two semilattice levels are D and the rectangular ideal; a local corner at an upper idempotent is a group with zero adjoined, and at a lower idempotent is trivial. It is nonorthodox because the nonorthodox products of D-idempotents survive at the upper level. It is NOTWEU: the lower idempotent in any cell is below EVERY upper element in that cell, including nonidempotents. Every upper idempotent cone nevertheless is a one- or two-element semilattice.

## 2. Its actual syntactic quotient is negative for EVERY band target

Let τ_D be D's actual idempotence-context congruence and write D'=D/τ_D. Import the reconstructed general purity lemma at its exact regular-source scope: `frontier-20261028-syntactic-purity-all-regular-v1.md`, SHA `20b839e181bc4fff3655cc22cf07675357c0e4ddedb2998fdd1949642d1c1714`. Thus D→D' is pure and D' remains CS. In particular D' is NONORTHODOX: choose idempotents e,f with ef nonidempotent in D; purity keeps q(e)q(f) nonidempotent.

ALL lower zero-middle source elements have the same all-TRUE idempotence-context signature. For upper elements, any context containing a lower element produces an idempotent lower product, and contexts having only upper elements are EXACTLY D's full actual/absent idempotence contexts. No upper element has an all-TRUE signature: nonorthodox D has a nonidempotent k, and for any d∈D, complete simplicity gives x,y∈D with xdy=k. Consequently the ACTUAL quotient is

`S/τ_S ≅ (D/τ_D)^0 = (D')^0`,

where this time ALL lower cells are collapsed to ONE GLOBALZERO. The map S→S/τ_S is idempotent-pure, by the same regular-source purity lemma (and directly from the displayed quotient).

But `(D')^0` cannot embed into an idempotent-separating image of ANY physical band-by-CS host, ANY band or action: its upper cone above the globalzero is ALL its idempotents, which are not closed because D' is nonorthodox. Apply the universal upper-cone theorem at the ALLBANDS scope from `frontier-20261028-q2-upper-cone-obstruction-v1.md`, SHA `283fb012e02f730a86aaa72ecbb77f695de5bd572c73dfeed794a0ab77e7720a`. Therefore the generalized-Q2 image class is NOT closed under actual syntactic quotients, or even under idempotent-pure onto homomorphisms between regular locally inverse semigroups. No arbitrary actual-q reduction is valid for this Q2 target. This does not challenge the separately conditional pure-CS ACTOR transport for Q1, whose source/actor assumptions are different.

## 3. Small complete certificate and rectangular diagnostics

Take G=C₂, I=Λ={0,1}, P_(λ,i)=λi in bits. D has8 elements and is syntactically reduced. The positive source S has12 elements; its explicit physical semilattice host has16. The ACTUAL quotient has9 elements and is exactly the previously excluded D8 with a GLOBALzero.

`frontier-20261029-Q2-rectangular-quotient-checker-v1.py`, SHA `94e8ed82f201c9ae1d2ce63aa9b9f64828f76bc5669b6e293c7e3d387ed395d4`, completed before ThuOct29 02:43:33 PDT2026. It checks all256 host-to-source multiplication equations and onto/idempotent separation8→8, all1728 source associativity equations, source regularity, every local E-corner and upper cone semilattice, the literal NONWEU witness, all2028 full context tests (both absent-factor cases), all144 quotient equations and purity, and the quotient's nonclosed upper cone. It computes the source's finest rectangular quotient2×2 with idempotent cells2,2,2,2, whereas the actual quotient's finest rectangle is singleton with a NONCLOSED five-idempotent cell. These are actual finite computations; the arbitrary-D theorem above is written, not inferred from one example.

This positive-to-negative diagram preserves regularity, local inverseness and quotient purity but not generalized-Q2 eligibility. It supplies no original-Q1 negative, no largest-class characterization, no independent/formal verification and no novelty clearance. The universal purity/upper-cone imports and the new general proof require disjoint review before adoption.
