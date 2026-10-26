# R-minus: the coordinate-revealing ribbon route is exactly redundant

Owner `InfoGuessingRminus`, info-5. Actual source/derivation clock observed before this freeze: `2026-10-24T06:20:26-0700`. **Complete written CANDIDATE; no execution, no new numeric guessing-number bound and no public novelty verdict.** This is an unrestricted all-law/FD attack note, not a support/order increment. The earlier quasigroup candidate remains a separate pinned candidate, not an accepted premise of the main redundancy theorem here.

## 1. Fixed problem and exact imports

The graph, arbitrary finite alphabet conventions and deterministic local-FD definition remain those of `inputs-v1.json`, SHA256 `bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`. The unrestricted interval remains `20/3 <= gn(R-minus) <= 1847/276`.

For any finite law or normalized polymatroid h on V={1,...,10}, put

`Phi(h)=2 sum_v h({v}) - 3 h(V)`.

The only special graph import is the complete ordinary-WRITTEN I2 ledger, `I2-complete-written-verification-v1.md`, SHA256 `152f6fed3f7654c9207383892effdd8abe1cc796bca5544cfc7c2271cc077585`,1402LF. Its actual233LF peer return is pinned by SHA256 `9697e619e7c6129c47da178c3b9ce608fe2b43358a0cc6862d71e267a961a412`; Main's v16 disposition is SHA256 `0189f2186aa54e486736db167235eb78ca3ee184e6d1628f8ecb25a0ce57aa8c`. These support the exact I2 identities at WRITTEN scope; stronger executed/triple finite-certificate certification remains UNMET. No I1 deletion identity or classification import is used.

For every literal diamond D=(U,V;P,Q), with Z the other six coordinates,

`Phi=J_D+3S_D`,

`J_D=I(U;V|PZ)+I(U;V|QZ)+I(P;Q|Z)-I(U;V|Z)`,

where S_D is an explicitly nonnegative Shannon combination and the equality holds on the graph FDs. As a coefficient identity it also applies to FD-consistent Shannon polymatroids, not only entropic vectors. This is an algebraic use of the supported import, not a newly executed coefficient check.

## 2. Why the classical ribbon framework is a genuine all-law interface

Fix any finite FD-consistent support C. Minimize Phi over all probability laws supported on C, allowing arbitrary weights and smaller positive-probability supports. Compactness and continuity give a minimizer p with value m. If an original law on C has negative Phi, this minimizer has m<0.

For ANY finite auxiliary W jointly distributed with X under p, every conditional law X|W=w is supported on a subset of C, so its Phi is at least m. Chain rules give

`Phi(p)-E_w Phi(p_(X|W=w)) = 2 sum_v I(W;X_v)-3 I(W;X_V)`.

Therefore every minimizing law satisfies

`(2/3) sum_v I(W;X_v) <= I(W;X_V)`, for EVERY finite W.         (R)

Thus `(2/3,...,2/3)` lies in its ten-variable hypercontractivity ribbon. No entropy maximality among minimizers is needed here. This is a standard variational/ribbon consequence, not a newly invented definition or a general inequality asserted for arbitrary non-minimizing laws.

Primary antecedents actually read at the relevant statements:

- Beigi–Gohari, [Phi-Entropic Measures of Correlation, arXiv:1611.01335v1](https://arxiv.org/pdf/1611.01335), section2.1, Theorem2 and equation(9): the classical all-auxiliary mutual-information definition of the multivariate HC ribbon; its introduction and relevant section5 quadratic characterizations were also read. The unversioned PDF visibly identifies v1. The failed attempt at a v2 HTML URL is not treated as a source read.
- Wang–Gohari, [Ribbons from Independence Structure, arXiv:2601.18516v1](https://arxiv.org/html/2601.18516v1), introduction/preliminaries and section4.1: current HC-ribbon and non-Shannon interfaces. Its convex generator called Phi is NOT the graph functional Phi above. One printed coefficient domain in its Theorem4 fails the exact control in section6 below; it is not blindly imported.

A necessary quadratic consequence of(R), useful for distinguishing genuinely soft probes, is

`2 sum_v || E[f|X_v] ||_2^2 <= 3 ||f||_2^2`                  (V)

for every mean-zero real f on the finite positive-probability support. To derive it directly, choose a binary W with `P(W=+|X=x)=(1+epsilon f(x))/2`; boundedness allows sufficiently small positive/negative epsilon. Mean zero makes W unbiased. Binary entropy expansion gives `I(W;X)=epsilon^2 E[f^2]/(2 ln2)+O(epsilon^4)`, and replaces f by E[f|X_v] for I(W;X_v). Substitute into(R), divide by the positive quadratic factor and let epsilon tend to0. No numerical Taylor evaluation is involved.

For any two distinct nonconstant coordinates, take normalized mean-zero u(X_i),v(X_j), choose the sign so r=E[uv]>=0, and apply(V) to f=u+v. Cauchy–Schwarz gives `||E[f|X_i]||_2^2 >= (1+r)^2` and the same bound for j, while `||f||_2^2=2+2r`. Hence

`4(1+r)^2 <= 6(1+r)`, so r<=1/2.

Thus a Phi-minimizer has pairwise maximal correlation at most1/2 (constant variables are omitted). This is the known HC-to-MC consequence specialized to the coefficient2/3, not a new maximal-correlation theorem. Pairwise correlation tests alone do not establish(R), and none of this proves the original guessing-number bound.

## 3. A constant coordinate already forces Phi>=0 by I2 alone

This statement is needed at the **Shannon-polymatroid level**, not through an unverified projection/deletion certificate.

If h(v)=0, Shannon submodularity and monotonicity give h(S union{v})=h(S) for every S. Select an actual diamond containing v. If v is U or V, its J_D reduces to I(P;Q|Z)>=0. If v is P, J_D reduces to I(U;V|QZ)>=0; if v is Q, it reduces to I(U;V|PZ)>=0. Thus the I2 identity and S_D>=0 imply Phi(h)>=0.

Here is a literal covering choice for all ten vertices, so no absent diamond or graph-by-nickname is being assumed:

| constant vertex | diamond (U,V;P,Q) | its role |
| --- | --- | --- |
| 1 | (2,4;1,3) | P |
| 2 | (2,4;1,3) | U |
| 3 | (2,4;1,3) | Q |
| 4 | (2,4;1,3) | V |
| 5 | (3,5;1,4) | V |
| 6 | (2,6;1,7) | V |
| 7 | (2,6;1,7) | Q |
| 8 | (3,10;4,8) | Q |
| 9 | (4,9;3,8) | V |
| 10 | (3,10;4,8) | V |

This concerns full ten-coordinate FD-consistent polymatroids with a loop. It does NOT assert that an arbitrary six- or nine-coordinate projection inherits all induced-graph FDs, and does NOT discharge the separate I1 gate.

## 4. Exact all-coordinate-subset probe barrier

For a nonempty A subset V define the conditioned polymatroid

`h^A(S)=h(S union A)-h(A)`.

It is Shannon. It retains every graph FD because

`0 <= h^A(v|N(v)) = h(v|N(v),A) <= h(v|N(v))=0`.

Every v in A is a loop of h^A, so section3 proves

`Phi(h^A) >= 0`.                                             (P)

For the deterministic ribbon probe W=X_A, write

`C_A(h)=3 h(A)-2 sum_v I_h(X_A;X_v)`.

Directly expanding all ten mutual informations gives

`C_A(h)=2 sum_v h(A union{v})-17 h(A)-2 sum_v h({v})`,

and therefore the exact identity

`C_A(h)+Phi(h)=Phi(h^A) >= 0`.                                (B)

Consequently, for EVERY FD-consistent Shannon polymatroid with Phi(h)<=0,

`C_A(h) >= -Phi(h) >= 0`, for EVERY nonempty A subset V.        (B1)

This covers all1023 nonempty coordinate subsets simultaneously. The empty subset has C_empty=0 and is deliberately excluded from the positive-margin assertion. A=V is allowed and gives C_V=-Phi because Phi(h^V)=0.

### Matched-current-frontier margin

Under the usual guessing-number normalization h({v})<=1,

`-Phi(h)=3h(V)-2 sum_v h({v}) >= 3h(V)-20`.

Hence if h(V)=1847/276, then every one of the1023 probes has the **strict** margin

`C_A(h) >= 3*(1847/276)-20 = 7/92`.                           (M)

At a larger objective it has an even larger margin. More generally every feasible profile with h(V)>20/3 already passes all these cuts strictly.

Thus adjoining the entire finite family of optimizer-motivated inequalities C_A>=0 to ANY entropy outer region satisfying Shannon+FD+singleton caps removes **no** feasible profile above20/3. This remains true if that region has already imposed valid copy-lemma or non-Shannon constraints. If its supremum of h(V) is greater than20/3, that supremum is unchanged by adjoining these cuts: every feasible sequence approaching it eventually lies above20/3 and is untouched.

This is a symbolic obstruction to a whole proposed bound-improvement family, not a report that a particular LP was run, solved or had an exact published optimum independently reconstructed. In particular it does not promote the old floating Gürpınar replay's UNKNOWN status. It says such cuts cannot be the source of a matched improvement over1847/276 because all candidate profiles at and above that frontier already satisfy them with at least7/92 slack.

No new LP is needed or requested for this excluded family. The separate prepared five-variable Csirmaz MEM assay is a different family and is NOT invalidated or authorized by this result.

## 5. The stronger entropic barrier: any probe revealing even one coordinate is automatic

Let p be ANY finite FD-consistent law with Phi(p)<0, not necessarily a minimizer. Suppose a finite auxiliary W determines at least one coordinate X_v. In every supported W-fiber that coordinate is constant and the full graph FDs persist. Section3 therefore gives E Phi(X|W)>=0. The chain rule from section2 yields

`3 I(W;X_V)-2 sum_i I(W;X_i)`

`= E Phi(X|W)-Phi(X) >= -Phi(X)>0`.                           (F)

So such a law already passes every coordinate-revealing HC probe with a strict deficit margin. This includes tuples X_A, any channel output that contains X_A, and more general auxiliaries from which some X_v is exactly reconstructible.

Therefore a useful auxiliary for rejecting a hypothetical negative critical law must **not determine any nonconstant coordinate**. Replacing a genuine soft/non-coordinate probe by “just condition on a vertex/subset” cannot resolve the gap: it falls into the proved redundant family. The graph FDs are arbitrary deterministic dependencies; no quasiuniformity, group structure or support-size bound enters(F).

The all-auxiliary condition(R) at a minimizing law is still genuinely stronger than this automatic family. The packet does NOT prove that its needed non-coordinate auxiliaries exist, and does NOT turn the necessary correlation bound1/2 into a sufficient criterion for Phi>=0.

## 6. Current-source gate: the printed Theorem4 coefficient cube is false

The current arXiv Atom entry was read in raw XML and identifies `2601.18516v1`, updated26January2026. The HTML and PDF of that exact version were read at section4.1. The printed Theorem4 claims, for arbitrary U,R_1,...,R_n,S,T,

`sum_i gamma_i I(U;R_i)-I(U;R_1,...,R_n)`

`<= (1/3)[sum_(i<j)(I(R_i;R_j|S)+I(R_i;R_j|T))+I(S;T)]`,     (WG)

for gamma in[0,1]^n with sum gamma_i<=4/3. The notation R_i here avoids collision with the ten graph coordinates.

That coefficient domain fails already for n=2. Let A,B be independent uniform bits, put

`R_1=A OR B, R_2=A AND B, S=A, T=B, U=R_1`,

and take `gamma=(1,1/3)`. Each printed coefficient condition is met. Also U is a deterministic function of(R_1,R_2), so the proof's auxiliary recoupling Markov condition causes no issue.

Given A=0, R_2 is constant; given A=1, R_1 is constant. Thus I(R_1;R_2|A)=0. The analogous statement holds given B, and I(A;B)=0. The right-hand side of(WG) is0.

The joint pair probabilities are `(0,0):1/4, (1,0):1/2, (1,1):1/4`. Therefore

`H(R_1)=H(R_2)=2-(3/4)log2(3)`,

`H(R_1,R_2)=3/2`,

`I(R_1;R_2)=(1/2)log2(32/27)>0`.

The left-hand side of(WG) is

`H(R_1)+(1/3)I(R_1;R_2)-H(R_1)`

`= (1/6)log2(32/27)>0`,

contradicting(WG). This is an exact four-atom written counterexample; no numerical solver or finite search is involved.

It can even be placed inside the literal R-minus FD setting using the already displayed four-word code in `quasigroup-critical-law-obstruction-v1.md`, SHA256 `e36979ef85d24e7d71c0cd984400280e7c5a68105897033941652ae5da0b7744`: graph coordinates2 and4 are R_1,R_2, graph coordinates1 and3 are A,B, and5..10 copy A. The counterexample to the source formula itself needs only the independent bits above and does not depend on acceptance of the quasigroup theorem. Its positive graph Phi means it is NOT a guessing-number improvement or a counterexample to the R-minus target.

### What the displayed proof safely supports

Theorem1 used in that proof requires lambda_i in[0,1]. Keeping that restriction, the same argument gives the safe family

`0<=gamma_i<=2/3`, `sum_i gamma_i<=4/3`.

For completeness, at sum lambda_i=2 the two conditional Shannon bounds are

`sum_i lambda_i I(U;R_i|S)-I(U;R^n|S) <= sum_(i<j) I(R_i;R_j|S)`

and the analogous T-bound. Recouple U and(S,T) independently conditional on R^n, preserving both marginal tuples used in(WG). Chain rule and nonnegativity then give each bound with left side `sum_i lambda_i I(U;R_i)-I(U;S)-I(U;R^nST)`, and analogously for T. Add `I(U;S)+I(U;T)-I(U;R^nST)<=I(S;T)`. Division by3 gives gamma_i=(2/3)lambda_i. Smaller nonnegative coefficients follow by monotonicity; for n>=2 any allowed smaller vector can be extended to the sum2 lambda boundary within the coordinate caps.

The trivial coefficient vectors0 and the unit vectors are also valid by data processing and nonnegativity of the right side; their convex hull with the safe family is valid. This is not asserted to be the maximal corrected coefficient domain. In particular that convexification does NOT justify(1,1/3), which is expressly refuted above.

The unrestricted printed cube domain will NOT be inserted into a future entropy calculation. This finding concerns the exact accessible arXiv-v1 statement. The separate IEEE landing page returned a WAF challenge, so no assertion is made that a later conference version retains or repairs the domain. No contact, publication, paid access or bypass was attempted. Other results in the paper are not rejected by association.

## 7. Exact scientific outcome and what still remains

The new primary attack produced an exact **Shannon+FD redundancy barrier** with matched-frontier slack7/92 for all coordinate-subset ribbon probes, a stronger all-law coordinate-revealing-auxiliary barrier, and a counterexample excluding an overbroad current-source coefficient region before any scientific run. The generic HC/MC facts are credited to established literature and are not claimed as discoveries of this round.

The original unrestricted guessing gap remains open. A consequential next written step must use a genuinely non-coordinate/soft auxiliary or another all-law mechanism that is not in the proved automatic family. The current source's false coefficient enlargement and the1023 subset probes are not valid substitutes for that missing ingredient.

This note is frozen for a new exact-scope reconstruction, separate from the pending quasigroup candidate and earlier I2/T300 returns. The graph identity is an ordinary-WRITTEN import; no executable/triple certificate, formal/kernel proof, new bound, novelty or significance acceptance is supplied. No scientific program, LP, enumeration, arithmetic interpreter, code search, compilation, test, external-model CLI or old held runtime was run. Only source access, metadata and the written derivations stated here were used.
