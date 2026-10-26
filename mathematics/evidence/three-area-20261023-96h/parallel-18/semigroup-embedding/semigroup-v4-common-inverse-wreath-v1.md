# Later additive one-sided construction: common inverse fibres and an explicit faithful wreath cocycle

MathSemigroup-2. Actual `/bin/date` BEFORE this write: **Sun Oct 25 13:38:36 PDT 2026**. **AUTHOR-WRITTEN / PARTIAL / NOVELTY_UNCLEAR.** LATER additive source, not a retroactive input or an edit. No interpreter/eval/program, symbolic/numerical computation, enumeration, solver, checker/table, replay, CLI or nested agent. Mandatory v9/v10/v11/HOLD retained.

This note gives a COMPLETE injective multiplicative map for the one-sided source into an AUXILIARY ordinary semidirect/wreath product. Its acting factor is the actual locally inverse quotient T, not the required completely simple C, and its coefficient semigroup is not proved a band in the nonorthodox case. It is therefore NOT the original embedding acceptance. The exact two missing host upgrades are stated, rather than hidden by the word ‘wreath’.

## 1. Actual one-sided hypotheses

Let p:A->T be a surjective homomorphism of a regular source A with

`ker p subset L_A`, `p idempotent pure`.

For the current original problem A=S_R, T=S/theta, these are PROVED in `semigroup-v4-local-Green-splitting-v1.md`, SHA256 `b6abe477273fe3c6141f2a81f8ac2175c4a711a08f5bafa962c9d352754bfc89`; its source and reconstructed scope remain separately frozen. A is locally R-unipotent (local idempotent bands LEFT regular), p is an actual R-class covering, and T is weakly E-unitary locally inverse with its supplied pure C quotient. The new lemmas below use only the displayed regular/pure/L-kernel hypotheses unless stated otherwise.

No global orthodox or global R-unipotent hypothesis is inserted. The dual applies to S_L by passing to opposite semigroups.

## 2. Every fibre has the SAME inverse set and a common domain unit

**Lemma.** If p(a)=p(b), then V_A(a)=V_A(b). For ANY a' in V_A(a),

`a'b=a'a`, `b a' b=b`, `a' b a'=a'`.

In particular a'a is a common RIGHT identity for the whole p-fibre, not a speculative inverse assigned to unrelated q-types.

**Proof.** p(a)=p(b) and the kernel condition give b L a. Put d=a'a, f=a'b. The element p(f)=p(a')p(a)=p(d) is idempotent, so purity makes f an actual idempotent. Since b L a, bd=b. Also

`df=a'a a'b=a'b=f`, `fd=a'bd=f`.

Thus f belongs to the actual corner dAd. Equal p-images give f L d, again by the kernel condition. For idempotents f L d the Green criterion gives df=d; but df=f. Therefore f=d. It follows that

`b a'b=bd=b`, `a'b a'=da'=a'`.

So a' is an inverse of b. Interchanging a,b gives equality of the entire inverse sets. The common right-unit assertion also follows directly from b L a and a'a being a right identity on that L-class. QED.

A useful exact consequence is that for any c,d in one p-fibre and any inverse a' of one member,

`c a'd=c`.

There is no assertion of a common inverse for a whole ORIGINAL q-fibre, which can contain many different p-types. The old endpoint-only/common-unit counterexamples are not being contradicted or reinterpreted.

## 3. Sections and a right T-set with a FORMAL start state only

Choose for each t in T an element r_t in p^(-1)(t) and a mutual inverse r_t' in A. The lemma makes `r_t' r_t` a right identity on the ENTIRE fibre p^(-1)(t). These choices require no compatibility or multiplicativity.

Let X be the right T-set

`X=T disjoint-union {star}`,

with x dot u=xu for x in T and `star dot u=u`. This is an actual associative right action. The state star is distinct even if T already has an identity. It is NOT an identity element adjoined to A, a band, or the acting semigroup T. In formulas an initial r_star means an ABSENT left context only; every coefficient below is an actual A element.

For a in A, with u=p(a), define F_a:X->A by

`F_a(star)=a r_u'`,

`F_a(t)=r_t a r_(tu)'`, t in T.                            (F)

Every value is an actual IDEMPOTENT. At star its p-image is u p(r_u'), an idempotent. At t its p-image is `tu p(r_(tu)')`, also an idempotent because p(r_(tu)') is an inverse of tu. p-purity proves the assertion. No unproved closure of ALL products of such idempotents is inferred from it.

## 4. The exact global cocycle — every source product, no load equations left over

For all a,b in A and all x in X,

`F_(ab)(x)=F_a(x) F_b(x dot p(a))`.                        (COC)

For x=t in T, put u=p(a),v=p(b). Then

`F_a(t)F_b(tu)`

` =r_t a r_(tu)' r_(tu) b r_(tuv)'`

` =r_t ab r_(tuv)'=F_(ab)(t)`.

The removed middle source factor is justified EXACTLY: r_t a has p-image tu, so `r_(tu)'r_(tu)` is its actual common RIGHT unit by Section2. It is not a generic inserted idempotent being cancelled in a band. At star the same calculation starts with a instead of r_t a and uses the common right unit for p(a)=u. All source a,b and all coordinates are included, so this is a global cocycle proof, not another designated-anchor recipe or a finite sample.

The complete source-value equalities here rely on ker p subset L and purity. They are not claimed for the original broader q-fibres before the proven source splitting.

## 5. A genuine auxiliary host embedding and injectivity recovery

Let M=A^X with pointwise multiplication. T acts on M by endomorphisms

`(alpha_u H)(x)=H(x dot u)`.

Indeed alpha_u alpha_v=alpha_(uv) by the right T-action law. Form the ORDINARY semidirect product M semidirect T, with

`(F,u)(H,v)=(F alpha_u(H),uv)`.

Define

`Phi:A -> M semidirect T`, `Phi(a)=(F_a,p(a))`.

Equation(COC) proves multiplicativity. If Phi(a)=Phi(b), then p(a)=p(b)=u and evaluation at star gives `a r_u'=b r_u'`. Right multiplication by r_u, which is an ACTUAL source multiplication, recovers

`a=a r_u'r_u=b r_u'r_u=b`.

Thus Phi is injective. This is a complete explicit faithful map, not an uncomputed ‘there should be a cocycle’ claim. The actor is T, and M is an ordinary semigroup; associativity of the host is elementary pointwise/semidirect associativity. No regularity, band identity or restricted-carrier condition is assumed for the whole host.

One can replace M by the subsemigroup generated by ALL T-translates of the F_a, which is T-invariant; this changes none of the map or injectivity proof. Generators are coordinatewise idempotent, but a semigroup generated by idempotents is NOT automatically a band.

If A is GLOBALLY ORTHODOX and E(A) belongs to a band variety W, that coefficient subsemigroup does lie in `E(A)^X`, so it is a W-band. This is an explicitly qualified extra conclusion, not a substitution of the orthodox case for the nonorthodox target. Even there the actor remains T rather than C, and no original Pastijn/R product embedding follows without the next missing upgrade.

## 6. Why this is not already the required host

For the general full-Rees one-sided source A, E(A) need not be a subsemigroup. Therefore products of the pointwise idempotent functions may be nonidempotent, and M/the generated coefficient semigroup is NOT proved a band. For the orthodox subcase, the band conclusion is legitimate, but T is the actual LOCALLY INVERSE quotient and need not be completely simple or a group.

The classical normal-band Pastijn model `T -> N odot C` does NOT automatically extend the endomorphism action of T on M to an action of the larger host or to the group G underlying C. Ordinary semigroup action extension is not the injective-GROUP action-extension lemma proved in the normal-reflection packet. No such actor substitution is made here.

Likewise an ordinary semidirect image need not satisfy a lambda/restricted carrier condition. Source idempotency implies `F_a alpha_(p(a))(F_a)=F_a` when a is idempotent; it does NOT by itself imply `alpha_(p(a))(F_a)=F_a`. These are different assertions. The target in this note is not called the frozen restricted R product, and no Jones–Trotter/Auinger–Polak/Billhardt product equivalence is assumed.

The exact remaining tasks are: preserve this source separation while obtaining a V-BAND coefficient model for all relevant products, and reorganize the actual T action using its normal-band-by-C model with the required group automorphisms/P product (or prove the exact restricted-carrier analogue). These are nontrivial faithfulness/host obligations, not bookkeeping or a permitted scope reduction.

## 7. Source calibration and no improper classical import

The actual Billhardt1993 *On a wreath product embedding for regular semigroups*, Theorem5, printed63, was reread at the original scan

`https://gdz.sub.uni-goettingen.de/iiif/image/gdz:PPN362162808_0046:00000067/full/full/0/default.jpg`.

It assumes a regular semigroup WITH IDENTITY and a GROUP congruence, plus a classwise right-unit condition `t r' r=t`. Its target is the standard wreath product of the identity class by the quotient group. Our one-sided p has the needed right-unit equations, but its quotient T is generally only locally inverse, and no band-preserving monoidalization is available for a nonregular global E(A). That theorem is therefore NOT imported as the missing original host theorem. The state star above is only a function-evaluation seed, not that forbidden monoidalization.

The actually read Billhardt2001 *On lambda-semidirect products by locally R-unipotent semigroups*, Acta Sci.Math.67,161–176, primary archive record/download id2600, gives the lambda product and wreath product, and Theorems8/10 embed ALREADY GIVEN iterated lambda products into wreath products. Its e-variety associativity also uses homomorphic images/divisions. It does not assert that every one-sided p here embeds in such an iterated product, and division is not injection. The extracted formula layout has superscript/OCR limitations; no unread exact formula from it is used to certify a carrier or a product in this proof. The source is method guidance, not a premise for Sections2–5.

The 2021 Billhardt–Marques-Smith–Martins paper *Extensions of left regular bands by R-unipotent semigroups*, DOI10.1007/s10998-021-00384-z, was inspected at its public publisher ABSTRACT only. It retains GLOBAL R-unipotent source/quotient hypotheses and discusses a separate lambda-product question. No full body or theorem proof was obtained from the inspected lawful routes, and it is not a correctness import or a local-generalization license.

## 8. Exact status

The new actual cocycle/faithful auxiliary embedding uses arbitrary sections but no unproved simultaneous inverse-load solution: the necessary classwise right units follow from the PROVEN one-sided kernel. It is genuine progress in the exact full-source decomposition, but is not the specified band-by-completely-simple embedding. No conclusion about all-pure-CS quotient existence for arbitrary infinite book-class sources is added.

All formulas are WRITTEN with named ordinary regular-semigroup facts and explicit proofs. No formal/kernel, human/configured-family/cross-vendor, executable/triple-certificate, novelty/SOTA or publication acceptance. The new note is LATER than the splitting/covering packets and must be literally included in any gate that consumes it. Original embedding/nonembedding acceptance remains UNMET. Research continues on the two precise host upgrades, with BOTH one-sided factors retained; original cutoff/deadline unchanged.
