# Addendum 3 — an eight-CMI proof of a universal four-variable inequality

InfoGuessingRminus-2, original info-5. Actual native clock immediately before this writing: **Tue Oct 27 15:11:17 PDT 2026**.

**AUTHOR-WRITTEN, UNREVIEWED.** This resumes a genuinely source-separated finite-probability line inside S1 after the assigned w12 review was returned. The earlier prerequisite report was not an exhaustion claim. No additional public source, closed incidental fragment, historical proof, held guide or selected probability law is used here. The source-scope MINOR and all earlier findings persist. No novel-information-inequality or original-bound-improvement claim is made: this is an explicit proof candidate, not literature authentication.

## 1. Statement and original-object scope

For EVERY four jointly distributed finite random variables A,B,C,D, including deterministic, overlapping or identical variable blocks, the following inequality holds:

`I(A;B) <= 2 I(A;B|C) + I(A;C|B) + I(B;C|A) + I(A;B|D) + I(C;D)`.   (F)

All entropies and mutual informations use one common logarithm base. There is no alphabet-size bound or independence premise on A,B,C,D.

For the original R-minus task, take A,B,C,D to be ANY four finite-valued functions or blocks of an original ten-variable FD law X. The construction below augments that SAME law with one auxiliary variable; it never replaces, independently reoptimizes or changes the original ten variables. All original FDs are retained automatically on the unchanged X-marginal. The auxiliary is not a new game player or an altered observation edge.

This supplies an admissible, fully proved information inequality at the all-finite-law interface. It does not supply a graph-specific certificate at an improved constant or a strict-gain law.

## 2. Elementary facts and zero-probability conventions

For finite variables, define conditional entropies by the weighted sum over conditioning values of positive probability, and let 0 log 0=0. The chain rule gives

`I(U;V|Z)=H(U|Z)-H(U|V,Z)`.

Nonnegativity follows by writing each conditional mutual information as the probability-weighted relative entropy of the joint conditional law against the product of its marginals. The scalar inequality log t<=t-1 proves nonnegative relative entropy. A positive joint atom has positive marginals, so no undefined denominator occurs on such an atom; zero atoms contribute zero.

Only finite conditional kernels, the entropy chain rule and this elementary nonnegativity fact are used below. No general copy theorem is imported.

## 3. Actual finite extension — existence and exact identities

Given the original joint law p(a,b,c,d), create R on the SAME finite alphabet as C by

`P(A=a,B=b,C=c,D=d,R=r) = p(a,b,c,d) p(C=r | A=a,B=b)`

whenever p(a,b)>0. On zero-probability (a,b) choose any probability kernel; it contributes zero joint mass. Summing over r recovers exactly the original A,B,C,D law.

This construction has both properties:

1. `(A,B,R)` has exactly the law of `(A,B,C)`.
2. `I(R;C,D | A,B)=0`.

Indeed conditional on A,B the displayed joint density factors into the original conditional law of C,D and the new conditional kernel for R. In particular

`I(R;D|A,B)=0`, `I(R;D|A,B,C)=0`,
`H(R|A,B,C)=H(R|A,B)=H(C|A,B)`.

Marginal matching also gives H(R|A)=H(C|A), H(R|B)=H(C|B), and I(A;B|R)=I(A;B|C). These identities hold for all finite laws, without a full-support assumption.

## 4. First exact nonnegative remainder

Set

`E1=I(A;B|R)+I(A;B|D)+I(R;D)-I(A;B)`.

The entropy chain rule, expanded without any inequality, gives

`E1 + I(R;D|A,B)`
` = I(A;B|R,D) + I(R;D|A) + I(R;D|B)`.

For example, expanding either side into joint entropies gives exactly

`H(A,R)+H(B,R)+H(A,D)+H(B,D)`
` -H(R,D)-H(A)-H(B)-H(A,B,R,D)`.

By the constructed extension I(R;D|A,B)=0. Hence

`E1=I(A;B|R,D)+I(R;D|A)+I(R;D|B) >= 0`.   (E1)

This is a conditional-coupling identity, not an unrestricted Ingleton assumption about the original four variables.

## 5. Second exact nonnegative remainder

Set

`E2=I(C;D)+I(R;A,B|C)-I(R;D)`.

The first chain identity is

`I(C;D)+I(R;D|C)-I(R;D)=I(C;D|R)`.

The second is

`I(R;A,B|C)-I(R;D|C)`
` = I(R;A,B|C,D)-I(R;D|A,B,C)`.

The last term is zero in the actual extension. Therefore

`E2=I(C;D|R)+I(R;A,B|C,D) >= 0`.   (E2)

No independent optimization of R, C or D is used: the same finite extension supplies every term.

## 6. Third exact nonnegative remainder

Put

`T=I(A;B|C)+I(A;C|B)+I(B;C|A)`,
`E3=T-I(R;A,B|C)`.

Using marginal matching and conditional independence, the last two terms of T can be written as

`H(C|B)+H(C|A)-2H(C|A,B)`
` = H(R|B)+H(R|A)-2H(R|A,B,C)`.

Also I(R;A,B|C)=H(R|C)-H(R|A,B,C). Thus

`E3=I(A;B|C)+H(R|A)+H(R|B)-H(R|A,B,C)-H(R|C)`.

The chain-rule identity

`I(A;B|R,C)=I(A;B|C)+H(R|A,C)+H(R|B,C)`
`                         -H(R|A,B,C)-H(R|C)`

now yields

`E3=I(A;B|R,C)+I(R;C|A)+I(R;C|B) >= 0`.   (E3)

Again every identity concerns the same extension, with no source-specific entropy theorem as an extra premise.

## 7. Complete eight-CMI certificate

Adding (E1), (E2), (E3) cancels both I(R;D) and I(R;A,B|C). Replace I(A;B|R) by I(A;B|C) using marginal matching. The result is the EXACT identity

`2I(A;B|C)+I(A;C|B)+I(B;C|A)+I(A;B|D)+I(C;D)-I(A;B)`
` = I(A;B|R,D)+I(R;D|A)+I(R;D|B)`
`   +I(C;D|R)+I(R;A,B|C,D)`
`   +I(A;B|R,C)+I(R;C|A)+I(R;C|B)`.

All eight terms on the right are nonnegative, proving (F).

For a direct original-variable transcription, the same left side is

`3H(A,B)+3H(A,C)+3H(B,C)+H(A,D)+H(B,D)`
` -2H(A)-2H(B)-H(C)-4H(A,B,C)-H(A,B,D)-H(C,D)`.

This entropy expression follows by expanding the definition of each mutual information; it is not inferred from checks at selected laws or parameter values.

## 8. Application to actual original FD laws, and exact remaining gap

Let X be ANY finite joint law satisfying every original R-minus neighbour FD. Choose any four finite functions of X, form their marginal A,B,C,D, and attach R using its conditional kernel above while retaining the full X marginal. This is a legal probability extension of X. The original FDs still hold on X because its joint distribution has not changed. Applying the eight-CMI identity proves (F) on those original-variable functions/blocks.

No assertion is made that replacing an original coordinate by R preserves its original FD, or that R itself obeys a new graph observation rule. Such a replacement would require a separate coupled decoder proof; it is not part of the argument.

Combined with v1's actual-law/word caller, any valid ALL-ten-variable entropy certificate assembled from such universally valid inequalities and the original FDs could yield an original word-count upper bound. But THIS packet does not give the graph-specific coefficient identity or the improved constant. No particular four blocks, finite law, rational weights or numerical entropy profile were selected or evaluated.

The exact scientific next gap is a complete original-graph inequality using all necessary coupled variables and beating the inherited upper endpoint, or a finite strict-gain law. The already-read primary source names prior information-inequality bounds; that fact is NOT treated as a proof that (F) matches a particular published formula or that it improves any prior bound. A literature/source match would require a separate admitted source audit. Classical ancestry and non-novelty remain explicit.

This is a completed admissible inequality proof candidate, not a new numerical result, architecture exclusion, original-problem solution or stronger acceptance. Main's full-source and full-review gate remains unmet for this successor.

Same original slot, exclusive new root, scientific HOLDv2, all STOP/HOLD/ZERO histories, N4 outcome/exit UNKNOWN and aux214 STOP. No execution, selected check, source expansion, author contact or nested agent. Deadline 2026-10-31T21:23:27.000Z.
