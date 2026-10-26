# Later additive step: pure same-type stability and one-sided Green-class coverings

MathSemigroup-2. Actual `/bin/date` BEFORE this write: **Sun Oct 25 13:18:50 PDT 2026**. **AUTHOR-WRITTEN / PARTIAL / NOVELTY_UNCLEAR.** LATER additive to the full-source splitting packet, not a modification or retroactive review input. No scientific interpreter/eval/program, symbolic/numerical computation, enumeration, solver, checker/table, replay, CLI or nested agent. Mandatory v9/v10/v11/HOLD and the original October27 cutoff/deadline remain binding.

The exact one-sided lift remains unproved. This note proves an actual range-prescribed UNIQUE lifting property for its two quotient maps. It does NOT replace local R-unipotence by the stronger global property or claim a band model from selectors.

## 1. Pure same-type stability inside a Green L- or R-class

Let A be ANY regular semigroup with an ACTUAL pure homomorphism q_A to a completely simple semigroup C. Suppose

`c in a A^1`, `c L a`, `q_A(c)=q_A(a)`.

Then **c=a**. This is a statement about the Green right-ideal preorder at a fixed q-type and an actual L-class; it is NOT multiplication compatibility of the natural partial order.

**Proof.** Choose a' in V_A(a), and put d=a'a, f=a'c. The common q-value makes `q_A(f)=q_A(a')q_A(a)=q_A(d)` idempotent, so purity makes f an ACTUAL idempotent.

Since c L a, the idempotent d is a right identity on c: writing c=u a gives cd=u aa'a=c. Hence df=f=fd. Since c belongs to aA^1, the range idempotent aa' fixes it on the left, and

`c=aa'c=a f`.

Again c L a gives a=v c=v a f. Thus

`d=a'a=a' v a f`,

so d belongs to A^1 f. Conversely c=u a gives `f=a' u a=(a' u a)d`, so f belongs to A^1 d. Therefore f L d. Both are idempotents, so f L d implies df=d; but df=f. Hence f=d, and c=af=ad=a. QED.

Dually, if `c in A^1 a`, c R a and q_A(c)=q_A(a), then c=a. The proof is the preceding one in the opposite semigroup; C^op is again completely simple and the same purity condition holds.

No finiteness, stable-semigroup assumption, unit in a band, or source quotient-existence theorem is used.

## 2. H-class injectivity recalled with its exact scope

Purity of q_A also makes it injective on every H-class. If a H b and q_A(a)=q_A(b), choose a' inverse to a. Green translation puts ba' in the H-group of aa'. Its q-image is the idempotent q_A(aa'), so purity makes ba' idempotent and hence ba'=aa'. Since b L a, b(a'a)=b, giving `b=(ba')a=aa'a=a`.

This is only H-class injectivity. It does not separate an entire source R-class, L-class or idempotent q-fibre, and it is not substituted for original SEP.

## 3. A pure L-congruence extension is an actual R-class covering

Let p:A->T be a surjective homomorphism, and suppose

`ker p subset L_A`,

`q_A=q_T p` with q_A pure to a completely simple C.

A is regular; hence T is regular. Purity of q_A also makes p pure: if p(a) is idempotent, so is q_A(a), and hence a. In particular every preimage of a target idempotent is an actual source idempotent.

**Theorem.** For EVERY a in A, the restriction

`p: R_A(a) -> R_T(p(a))`

is a BIJECTION. Consequently, for each target idempotent f in that target R-class, there is EXACTLY ONE idempotent e in R_A(a) with p(e)=f.

**Injectivity.** Equal p-images are L-related by the kernel hypothesis. If their source elements also lie in one R-class they are H-related and have equal q_A-images. Section2 makes them equal.

**Surjectivity.** Let t R p(a). Choose x,y in T^1 with

`t=p(a)x`, `p(a)=t y`.

Lift x,y to X,Y in A^1, using a formal absent context only when the target multiplier is the formal identity. Put c=aXY. Then p(c)=p(a), so c L a by the kernel condition and q_A(c)=q_A(a). Also c belongs to aA^1. Section1 gives c=a. Now b=aX maps to t and `bY=a`, while b=aX. Thus b R a and it is the required lift. This proves surjectivity and uniqueness. If t=f is idempotent, p-purity makes b idempotent; no independent inverse-lifting theorem is assumed. QED.

Dually, a surjection whose kernel is contained in R, with the same pure CS factorization, restricts to a BIJECTION on EVERY L-class and lifts each target idempotent uniquely within the chosen source L-class.

These are actual bijections of Green classes. No additional categorical covering, action-extension or semigroup embedding theorem is inferred from the word ‘covering’.

## 4. Application to the two exact quotient sources

The full source splitting packet is `semigroup-v4-local-Green-splitting-v1.md`, SHA256 `b6abe477273fe3c6141f2a81f8ac2175c4a711a08f5bafa962c9d352754bfc89`. At its explicit supplied-pure-quotient hypotheses it proves

`S is isomorphic to S_R times_T S_L`,

`T=S/theta locally inverse`,

`ker(S_R->T) subset L_(S_R)`,

`ker(S_L->T) subset R_(S_L)`,

with both factor sources regular and pure over the SAME C. Their local idempotent bands are respectively left and right regular.

Therefore S_R->T has the full R-class bijections and range-idempotent unique lifts of Section3, and S_L->T has the dual L-class/domain-idempotent unique lifts. This is stronger than merely knowing all target idempotents have some preimage. The prescribed target idempotent and the prescribed SOURCE Green class are both retained.

It does NOT say that a source R-class has only one idempotent: its image R-class in a locally inverse T may have MANY idempotents, and the covering supplies one for EACH of them. It does not select one such target idempotent multiplicatively, globalize all selected local maps, or prove the translated mixed(M) equations for a proposed coefficient band.

The exact new representation boundary is thus a one-sided R-/L-class covering of an actually modeled locally inverse T. A faithful V-band Pastijn realization of that covering, over the supplied C and without a common-unit completion, is still the missing construction.

## 5. Actually read classical comparison — GLOBAL, not local, R-unipotence

A new primary comparison was actually read in full: M.B.Szendrei, *E-unitary R-unipotent semigroups*, Semigroup Forum32(1985),87–96. [EuDML source locator](https://eudml.org/doc/134770) resolves to GDZ volume `PPN362162808_0032`; its actual IIIF manifest is

`https://manifests.sub.uni-goettingen.de/iiif/presentation/PPN362162808_0032/manifest?version=29486bf2`.

The manifest confirms printed87 at canvas00000091. ALL TEN original page images00000091 through00000100 (printed87–96) were read, including the entire proofs and final references, via the advertised service

`https://images.sub.uni-goettingen.de/iiif/image/gdz:PPN362162808_0032:00000091/full/full/0/default.jpg`

and its subsequent listed page identifiers. This is source reading, not OCR/math execution, a new local byte-hash receipt or a fresh retrieval of an inaccessible publisher PDF.

Its Proposition2.1/Theorem2.2 assumes GLOBAL R-unipotence: every source R-class contains a unique idempotent. The paper explicitly identifies that class with orthodox semigroups whose GLOBAL idempotent band is left regular. It embeds E-unitary such sources into band-by-GROUP products, with the band in the variety generated by E(S). Its left-normal refinement assumes the additional locally inverse property. These are not the present LOCALLY R-unipotent factor sources, and the present normal quotient is completely simple-graded, not silently group-graded.

The proof's useful actual representation is a partial band on E cross G with properties(A1)–(A6), in particular all single letters idempotent, a strong partial associativity/domain condition, a distinguished GLOBAL left regular band Y, and an actual group action. The free left regular band completion has a source-value invariant under its prefix-repeat and partial-product rewrites; the left-normal variant uses a meet and a unique projection in the quotient order. Those exact global hypotheses are not established for our one-sided covering. The paper is ancestry/method guidance, NOT a correctness premise discharging the present missing lift.

The old E5 positive control already warns against replacing the local hypothesis: it is locally left regular but not globally regular, so it cannot simply be treated as a global R-unipotent orthodox source with a left regular global idempotent band. Adding a common identity to force it into one corner would violate the original base variety. No such replacement is made here.

## 6. Exact continuation and ceiling

Next required step: construct the full-Rees analogue of the appropriate one-sided partial-band representation/completion for the ACTUAL R-class covering S_R->T, and the dual, with every coefficient relation proved; alternatively isolate a genuine canonical least-quotient obstruction. Unique range lifts alone are not that representation. No proposed partial multiplication or band model is declared associative, faithful or complete without its proof.

All new stability/Green-covering proofs are WRITTEN. Ordinary Green translations and uniqueness of the idempotent in an H-group are the named elementary imports; the same-type stability, surjective class lift and purity checks are displayed. The substantial classical LI embedding theorem is only used if one imports the preceding normal model of T, not to prove this note's covering theorem. No formal/kernel, human/configured-family/cross-vendor, executable/triple-certificate, novelty/SOTA or publication acceptance. Original full embedding/nonembedding acceptance remains UNMET; the separate arbitrary-infinite pure-quotient prerequisite and the original cutoff/deadline are unchanged. Research continues rather than ending at this source comparison.
