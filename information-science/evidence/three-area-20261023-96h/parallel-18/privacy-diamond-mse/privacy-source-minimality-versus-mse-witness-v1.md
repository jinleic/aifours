# Exact source-order control: lower MSE but opposite probabilities on two origin ideals

Owner InfoResearch96h-2. Last actual pre-body observation: **Sun Oct 25 14:38:06 PDT 2026**. **AUTHOR-WRITTEN registered-privacy SOURCE-DEFINITION control**, not independently reviewed or parent accepted. The existing1049 privacy source-equivalence scope controls; `privacy-source-order-witness-continuation-ack-v1.json` discloses already-explored generic clipping/ideal reasoning before this later body. No auxiliary graph derivation is continued.

## 1. Exact question and named imports

The accepted manuscript of [Soria-Comas–Domingo-Ferrer2013, *Optimal data-independent noise for differential privacy*](https://doi.org/10.1016/j.ins.2013.07.004), [UOC primary manuscript](https://openaccess.uoc.edu/handle/10609/152758), defines its multivariate order by probabilities on EVERY coordinate-origin-box ideal S: if x is in S, the full coordinate box from0to x is contained in S. Definition5 calls a law optimal when it is MINIMAL in that partial order, not least and not a minimizer of a prescribed MSE functional. The actual complete Definitions3–5 were reread at local sourceLF260–314 before this body. Full-source SHA256 `3e625b3c6d2d47fc73accbe3f66be916658be6949e005fd8f4d6ea47da07c6a1`; the entire source was read earlier. The original constructionLF926–945 was also reread; its later malformed Theorem13 recurrence is not silently fixed or used as a theorem here.

This note gives TWO actual full-continuous-diamond-private Borel laws from that PRIOR arbitrary-core construction, both with rationally specified cores, such that:

- the clipped law has STRICTLY LOWER squared-Euclidean loss;
- it puts MORE probability on one actual origin ideal;
- it puts LESS probability on another actual origin ideal.

Thus the laws are INCOMPARABLE in the exact source's Definition4. This does **not** establish that either law is globally minimal in the full privacy class; it does not independently certify/refute source Theorem13. It makes the distinction from a prescribed-MSE comparison concrete, rather than relying only on the word optimal.

Named correctness imports are **STD** only: planar Lebesgue integration/Tonelli, translation invariance, convex-polytope/Minkowski geometry, the geometric series/factorial moments and elementary integer/rational algebra. No registered LAW-STD, BRANCH-OLD, CAL, MDA theorem, scalar critical polynomial or numerical table is needed. The separate218LF whole-homothetic-family counterexample is context, NOT a correctness premise or accepted theorem for this note.

## 2. Two literal laws with full privacy quantifiers

Set

`q=1/101`, `epsilon=log101`, `gamma=1/2`, `delta=1/1000`,

`D={||x||_1<=1}`, `K0=D_gamma`,

`Kdelta=D_gamma intersect {||x||_infinity<=gamma-delta}`.

For a=0 or delta, let C_(a,j)=K_a+jD and `nu_a(x)=min{j>=0:x in C_(a,j)}`. Put

`p_a(x)=q^(nu_a(x))/A_a`.

Both cores are compact convex origin-box ideals contained in D, with nonempty interior. For EVERY h in CLOSED D, `C_(a,j)+h subset C_(a,j+1)` and the reverse-shift inclusion hold, hence `|nu_a(x+h)-nu_a(x)|<=1` for ALL x. Therefore `p_a(x)<=101*p_a(x+h)` pointwise, and for EVERY Borel E,

`mu_a(E)<=101*mu_a(E+h)`.

This is the original ALL-Borel/full-continuous-closed-D model, not a gradient/Lipschitz class, a lattice of shifts or only selected events. Exponential tails give finite normalizers and moments.

Let J have algebraic weights `(1-q)q^j`, and T_n=E(gamma+J)^n. The nonnegative identity

`q^(nu_a(x))=(1-q)*sum_(j>=0)q^j 1_(C_(a,j))(x)`

gives all probabilities/costs below by Tonelli. It is not an unadjusted uniform-mixture sampling claim.

For L=gamma+j, the actual cumulative clipped set is

`C_(delta,j)=D_L intersect {||x||_infinity<=L-delta}`.

Equality follows directly from the vertices `(L-delta,delta)` and their sign changes/permutations: they are the corresponding core vertices plus j times a signed coordinate axis; the converse is the two triangle inequalities. Four disjoint axis caps of area delta^2 are removed. Their individual Euclidean moment is

`integral_0^delta [2u(L-u)^2+(2/3)u^3]du`

`=L^2delta^2-(4/3)Ldelta^3+(2/3)delta^4`.

Consequently

`A0=2T2`, `Adelta=2T2-4delta^2`,

`N0=(2/3)T4`,

`Ndelta=(2/3)T4-4delta^2*T2+(16/3)delta^3*T1-(8/3)delta^4`,

and the costs are F0=N0/A0 and Fdelta=Ndelta/Adelta. These are squared EUCLIDEAN moments, not squared-l1 moments.

The exact geometric factorial moments at u=q/(1-q)=1/100 give

`EJ=1/100`, `EJ^2=51/5000`, `EJ^3=5303/500000`, `EJ^4=142953/12500000`.

At gamma=1/2, ordinary binomial expansion yields the complete rational table:

|quantity|exact value|
|---|---:|
|T1|51/100|
|T2|1351/5000|
|T4|1443103/12500000|
|A0|1351/2500|
|Adelta|135099/250000|
|F0=T4/(3T2)|1443103/10132500|

All these are WRITTEN identities, not machine checks.

## 3. Actual LOWER MSE, independently of a global optimum

The exact comparison identity is

`Ndelta-F0*Adelta`

`=4delta^2[-(T2-F0)+(4/3)delta*T1-(2/3)delta^2]`.

Here F0<3/20, certified by

`3*10132500-20*1443103=1535440>0`.

Thus `T2-F0>1351/5000-3/20=601/5000`, while `(4/3)delta*T1=17/25000`. Dropping only the negative final term gives

`Ndelta-F0*Adelta <4delta^2[-601/5000+17/25000]`

`=-4delta^2*(747/6250)<0`.

Since Adelta>0, **Fdelta<F0**. This is a direct two-law comparison. It does not say gamma=1/2 minimizes the homothetic family, or that either displayed law is the registered global optimizer.

## 4. First exact ideal: the central diamond favors the clipped law

Take the Borel origin-box ideal

`I_c=D_(1/4)`.

It lies in BOTH highest plateaux, since1/4<gamma-delta and1/4<gamma. Its area is1/8. Therefore

`mu_delta(I_c)=(1/8)/Adelta=31250/135099`,

`mu_0(I_c)=(1/8)/A0=625/2702`.

Their ordering is STRICT, as

`31250*2702-625*135099=625>0`.

Thus `mu_delta(I_c)>mu_0(I_c)`.

## 5. Second exact ideal: a narrow axis strip favors the diamond law

Take the Borel origin-box ideal

`I_s=R cross[-delta,delta]`.

Unboundedness is allowed by the ACTUAL source Definition4, which tests every set with the coordinate-box property, not only bounded balls. For L>=gamma>2delta, direct horizontal slicing gives

`area(D_L intersect I_s)=4delta*L-2delta^2`,

`area(C_(delta,j) intersect I_s)=4delta*(L-delta)`.

For the second formula, throughout |y|<=delta the clipped horizontal half-width is L-delta: `min(L-|y|,L-delta)=L-delta`. The y-cap does not bind. Hence the actual probabilities, including ALL shell tails, are

`mu_0(I_s)=(4delta*T1-2delta^2)/A0=1019/270200`,

`mu_delta(I_s)=4delta*(T1-delta)/Adelta=509/135099`.

Again the sign is certified entirely by integers:

`1019*135099-509*270200=134081>0`.

Thus `mu_0(I_s)>mu_delta(I_s)`. This is a finite-width actual Borel event, not a line of zero planar measure, a pointwise-density impression or an unevaluated limiting strip.

## 6. Exact source consequence and acceptance ceiling

The source's relation `mu_1<=mu_2` means mu_1 gives at least as much mass to EVERY allowed ideal. I_c prevents `mu_0<=mu_delta`; I_s prevents `mu_delta<=mu_0`. The laws are therefore genuinely incomparable in that order even though Fdelta<F0. Both test sets satisfy the exact coordinate-origin-box condition, not merely a norm-radial substitute.

This is a concrete reason not to substitute source Definition5's MINIMALITY conclusion for a prescribed-MSE optimizer statement. If source Theorem13 is consumed as a named research theorem, it calls its broad ideal-core family optimal in THAT Definition5 sense; it cannot be silently reread as making every such member an MSE minimizer, since the displayed members have unequal MSE. Conversely this two-law incomparability does not prove their global minimality and does not independently audit Theorem13's proof or all its assumptions. No source-theorem correctness waiver is made.

The family itself is PRIOR: both K0 and Kdelta are origin-box ideals inside the sensitivity set D, and their disjoint cumulative shells match the actual construction preceding Theorem13. This source-control note is not a new mechanism, global selector/equality theorem, current-openness/priority certificate or proof that no earlier equivalent comparison exists. The separate218LF note establishes a stronger WHOLE-homothetic-family failure at an algebraically specified parameter; this all-rational note has the different, narrower purpose of authenticating the source-order/MSE distinction with actual probabilities.

The first remaining SOURCE acceptance is independent full-body mathematical/source-equivalence reconstruction of the481LF dossier,218LF counterexample and any source controls adopted with them, followed by explicit parent disposition. **NOVELTY_UNCLEAR** remains the ceiling. Existing parent adoption of the registered642LF ALL-law theorem is separate and is not undone, widened or made a priority acceptance by this note.

Kernel/program checks: **NONE**. Written integer/rational integration only; no float proof arithmetic, scientific eval/interpreter/calculator/program/solver/enumeration/replay/modelCLI/nestedagent/tests/build/formatter/newGO. Both permanent process findings and strict auxiliary STOP remain; no graph work is resumed, no continuous-compliance claim made, and no frozen file edited. Original registered scope/cutoff/deadline are unchanged.
