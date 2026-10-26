# v43-D — exact quartic noise elimination at the actual state/projector interface

Reviewer **InfoHinfPreview-2**, retaining info-3. Author **PhysicsDepol4**, physics-2. Actual exposure-ACK clock: **Sun Oct 25 06:40:47 PDT 2026**. Actual post-reconstruction clock before this return: **Sun Oct 25 06:43:46 PDT 2026**, both returned `/bin/date` outputs.

## 1. Verdict and the essential non-verdict

**0 FATAL / 0 MAJOR / 0 MINOR findings in the NEW exact noise-elimination theorem and its physical-interface derivation, at the named inherited U1/U2/high-noise endpoint imports.** All its new load-bearing steps are reconstructed below: actual channel expansion and deficit signs, complete scalar degeneracies, unique interior minimizer, reversible radical squaring, every quartic coefficient, pure-to-mixed extension through the ORIGINAL channel inequality, and the actual physical counterexample interface.

In particular the displayed polynomial has **no coefficient error**:

$$D=27a^2d^2+18abcd+4b^3d-b^2c^2-4ac^3.$$

**This review does NOT prove D>=0 for physical pairs.** The universal physical quartic/quadratic tradeoff remains OPEN, as do low-noise channel indices k2,3,4. Relaxed four-number tuples are not states/projectors and do not become counterexamples through an exact scalar minimizer. No full target, actual counterexample, independent-model/formal proof, novelty or parent acceptance follows.

This is a same-harness different-domain supplied-proof written reconstruction, not blind/cross-vendor/configured-dual-family/human/executable certification. Parentv7/v8 and HOLD remain binding.

## 2. Exact pins, full coverage, exposure and operation inventory

Parent evidence erratumv8 was read FIRST, all37LF. Then the exact v43-D manifest entry/common rules and full39-line packet receipt were read. Exposure ACK was written before proof body in `peer-review-depol-exact-quartic-noise-ack-v1.json`. All earlier assigned reviews, including v41-A, had already been returned.

Fresh metadata SHA-256 observations:

| Record | SHA-256 |
|---|---|
| v43 manifest | `97cdf16df4713419ac41fa50741eab54667ae6033f68bd617f949bf3621787b6` |
| v43 packet receipt | `3ec5b87eb2fb944c4b474bf17f5b2569781b42683e9908732ecc2eb08ece7638` |
| parentv8 | `52408180ac48dec69d2144ea0dee07acf08f0739f65a8cdb2b007656243527e9` |
| mandatory literal `peer-review-wave-v43-depol-exact-quartic-noise-sources-v1.md` | `168745b4201cb176fd7f35aaa0bae3cea1473678739f8a21eecf58b1074f523c` |
| author `depolarizing-low-noise-consolidated-frontier-v1.md` | `8b5ae28f34795f2b750e11e1c57f458935bb5af3fcb421bf531a7800878db4b1` |

The complete320-line mandatory literal packet was read in windows covering LF1–148,149–273,274–320, including **every original source LF1–313**, all tables, the whole new section6 and the final nonclaims. No reader-truncated source line was treated as read; none was reported in these windows. Citations below mean the original S1 source LF labels in that literal packet, not packet line numbers. The packet/source pins matched the exact manifest and receipt.

Prior exposure was the round README's central/high-noise depolarizing summaries and unresolved low-noise indices, plus the manifest's quartic/degeneracy headline. The current consolidation and detailed previous depolarizing reviewer returns had not been read before the ACK. No historical arithmetic or parent promotion supplies a proof premise here.

**No scientific code/eval/interpreter, arithmetic or symbolic program, sampling, enumeration, certificate replay, solver, CLI, nested agent, git operation, deletion or author/shared write was used.** The proof below is written algebra and elementary minimization. Metadata clocks/hashes and source reads are the only machine operations. Unadmitted pre-correction computations retain zero executable-verification credit; no GO exists.

## 3. Exact actual-pair coordinates and channel expansion — S1 LF35–77

Fix an ACTUAL density matrix rho on four qubits and an ACTUAL complex rank-k orthogonal projector Pi, k2,3,4. Define X_s with unnormalized identity factors exactly as in the source:

$$X_s(\rho)=\sum_{|I|=s}\rho_I\otimes I_{I^c}.$$

Write `r=Tr(Pi rho)`, `d=1-r`, and

$$a=3k+1-\operatorname{Tr}(\Pi X_1),\qquad
b=3k+3-\operatorname{Tr}(\Pi X_2),$$

$$c=\operatorname{Tr}(\Pi X_3)-(k+3).$$

Because rho is positive trace1 and Pi is a projector, `0<=r<=1`, so d>=0. The inherited U1 and rank-matched U2 comparisons give a,b>=0. Those are explicit prior mathematical inputs, not facts inferred from an arbitrary four-number relaxation. c is real and may have either sign.

For `0<p<2/3` put `alpha=1-p>0`, `beta=p/2>0`, and `u=beta/alpha`. The product channel expands EXACTLY as

$$\mathcal D_p^{\otimes4}(\rho)
=\alpha^4\rho+\alpha^3\beta X_3
 +\alpha^2\beta^2X_2+\alpha\beta^3X_1+\beta^4I.$$

The single-qubit product-reference eigenvalues are alpha+beta and beta, with the first larger. For k2,3,4 the top-k reference sum is

$$(\alpha+\beta)^4+(k-1)(\alpha+\beta)^3\beta.$$

Expanding this reference, term by term, gives

$$\alpha^4+(k+3)\alpha^3\beta+(3k+3)\alpha^2\beta^2
 +(3k+1)\alpha\beta^3+k\beta^4.$$

Thus the actual trace gap G_k against this SAME Pi, divided by `a3=alpha^3 beta`, is

$$G_k/a3=c-au^2-bu-d/u.$$

The identity contribution cancels since `Tr Pi=k`; the coefficients of X1,X2,rho relative to X3 are u-squared,u,1/u. No normalized identity or missing power of2 is inserted.

Define

$$q(u)=au^3+bu^2-cu+d.$$

Then

$$G_k=-(a3/u)q(u),\qquad a3/u>0.                            \tag{1}$$

The map `u=p/[2(1-p)]` bijects `(0,2/3)` with `(0,1)` and has inverse `p=2u/(1+2u)`. All divisions in (1) are made only on that open interval.

### Endpoint inputs are correctly scoped

`q(0)=d>=0` is an elementary actual-pair fact. At `p=2/3`, u1 and alpha,beta are positive and equal; the inherited ALL-STATE high-noise endpoint theorem, combined with the Ky-Fan variational principle for ANY Pi, gives

$$q(1)=a+b-c+d\ge0.$$

This is the exact endpoint import used, not a claim that the quartic or low-noise interval was already solved. Continuity gives equivalence of q-nonnegativity on `(0,1)` and `[0,1]`; in particular no untested open-endpoint boundary is lost.

## 4. Complete scalar case split, including all zero cases — S1 LF177–211

Assume only `a,b,d>=0`, c real and `q(1)>=0`.

### Case1: c<=0

All coefficients of q are nonnegative, so q>=0 on `[0,1]`. This includes c0 and arbitrary a0,b0,d0 coincidences. No discriminant test or division is needed.

### Case2: c>0 and c>=3a+2b

On `[0,1]`,

$$q'(u)=3au^2+2bu-c\le3a+2b-c\le0.$$

Therefore the minimum is q(1), already nonnegative. Equality `c=3a+2b` belongs here, even though the derivative may vanish at1. If a=b0, every c>0 belongs here and q is simply `d-cu`; the endpoint assumption is the exact remaining requirement. No division by a or b is made in this case.

### Remaining interior: 0<c<3a+2b

Here `q'(0)<0<q'(1)` and `q''(u)=6au+2b>=0`. At least one of a,b is positive. The derivative is strictly increasing on the open interval (if b0,a>0 it is still strictly increasing for u>0), so there is exactly one critical point s in `(0,1)`, the global minimum.

- If a0, then b>0. One has `s=c/(2b)` and

  $$q(s)=d-c^2/(4b).$$

  Hence nonnegativity is equivalent to `4bd-c^2>=0`. The root is interior because c<2b. This includes d0, which correctly fails whenever c>0.

- If a>0, no division by b or d is used. Thus b0 and d0 remain included. The exact radical minimum is reconstructed next.

These cases are exhaustive and their boundary allocation is correct. There is no missing linear or constant-polynomial exception.

## 5. Interior a>0, reversible squaring, and EVERY quartic coefficient — S1 LF205–233

Set

$$\Delta=b^2+3ac>0,\qquad R=\sqrt\Delta,\qquad
s=(R-b)/(3a).$$

Since a,c>0, `R>b`, so s>0. Moreover

$$\Delta<(b+3a)^2\quad\Longleftrightarrow\quad c<2b+3a,$$

so the strict interior hypothesis gives s<1. At q'(s)0,

$$c=3as^2+2bs,\qquad q(s)=d-s^2(2as+b).$$

The exact subtraction is

$$s^2(2as+b)={(R-b)^2(2R+b)\over27a^2}
={2R^3-3bR^2+b^3\over27a^2}$$

$$={2\Delta^{3/2}-2b^3-9abc\over27a^2}.$$

Therefore

$$q(s)\ge0\quad\Longleftrightarrow\quad
L:=27a^2d+2b^3+9abc\ge2\Delta^{3/2}.                        \tag{2}$$

Both sides of (2) are nonnegative. In particular L may be zero when b=d0, but can never be negative in this branch. Squaring is therefore **reversible**, including that zero case; it does not accept a negative L with large absolute value.

The complete monomial cancellation in the squared expression is:

|monomial|coefficient in L-squared|coefficient in4Delta-cubed|difference|
|---|---:|---:|---:|
|a4 d2|729|0|729|
|a3 b c d|486|0|486|
|a2 b3 d|108|0|108|
|b6|4|4|0|
|a b4 c|36|36|0|
|a2 b2 c2|81|108|-27|
|a3 c3|0|108|-108|

Consequently

$$L^2-4\Delta^3
=729a^4d^2+486a^3bcd+108a^2b^3d
 -27a^2b^2c^2-108a^3c^3$$

$$=27a^2\left(27a^2d^2+18abcd+4b^3d-b^2c^2-4ac^3\right).
                                                               \tag{3}$$

Because `27a^2>0`, this difference has exactly the sign of D. Combining (2),(3) proves

$$q(u)\ge0\ \text{for all }u\in[0,1]
\quad\Longleftrightarrow\quad D\ge0$$

in precisely the stated interior a>0 branch. Every coefficient and both canceled monomials have been accounted for. In particular the coefficients18 and4 and the negative b-squared/c-squared and a/c-cubed terms have the advertised signs.

As boundary checks in writing, b0 reduces D to `27a^2d^2-4ac^3` without invalidating the radical argument; d0,c>0 makes D strictly negative, agreeing with q's negative initial slope from q(0)0. The a0 boundary is not passed through the zero factor27a-squared: it was handled separately by the actual quadratic test.

**No quartic coefficient error is found.** This is an exact scalar theorem, not a physical proof that D is always nonnegative.

## 6. Exact equivalence to all missing channel parameters — S1 LF235–243

For each fixed ACTUAL rho,Pi, equations(1) and the u/p bijection prove that the channel trace inequality for all `0<p<2/3` is equivalent to the scalar theorem's case predicate. The noninterior cases are already automatic at the inherited endpoint and deficit sign inputs.

Thus the remaining universal physical obligation at each k2,3,4 is exactly:

- for every actual state/projector pair in `0<c<3a+2b` with a>0, prove D>=0;
- for every such actual pair with a0 (hence b>0), prove `4bd>=c^2`;
- or supply an actual pair with a strict failure.

This retains the whole state space, all complex rank-k orthogonal projectors and the full open noise interval. It does not replace the target by the stronger c<=0 condition or by independently chosen marginal numbers. Quantifier elimination of u does **not** eliminate actual-pair compatibility.

For a fixed physical p, the Ky-Fan variational principle is

$$K_k(\mathcal D_p^{\otimes4}(\rho))
=\max_{\Pi:\operatorname{rank}\Pi=k}\operatorname{Tr}(\Pi\mathcal D_p^{\otimes4}(\rho)).$$

Hence all-Pi trace inequalities are exactly the k-th original spectral comparison. Conversely a trace gap for even ONE actual Pi already forces Ky-Fan violation; Pi need not have been identified as a leading spectral projector.

### Pure-to-mixed extension is through the ORIGINAL inequality

Suppose the exact scalar predicate is proved for all pure inputs and every actual Pi. For each fixed p,Pi it then implies `G_k(Pi,rho_pure)<=0` by (1). If `rho=sum_j t_j rho_j` is a pure-state decomposition, channel linearity and the state-independent reference sum give

$$G_k(\Pi,\rho)=\sum_j t_jG_k(\Pi,\rho_j)\le0.$$

Take the maximum over Pi to obtain the mixed-state channel inequality. Equivalently one may use Ky-Fan convexity after applying the channel.

No convexity of the quartic D or of its nonlinear feasible set is asserted or needed. In particular one must not average pure-state D-values and call the result the mixed D-value. Degenerate pure/mixed coordinates are safe because the original linear inequalities are extended BEFORE translating back to a scalar predicate. This reconstructs the source's stated pure-state reduction at its correct logical interface.

## 7. Exact physical counterexample interface — S1 LF245–255

If an ACTUAL pair is in the interior a>0 branch and D<0, reversible equivalence above gives `q(s)<0` at

$$s=(\sqrt{b^2+3ac}-b)/(3a)\in(0,1).$$

Then

$$p_\star=2s/(1+2s)\in(0,2/3)$$

is a physical low-noise parameter. The factor `a3/u` in (1) is strictly positive there, so the actual trace gap is **strictly positive**. The Ky-Fan maximum is at least that trace. Thus actual rho, actual Pi, and this exact algebraic parameter form a genuine original-channel counterexample interface, without a numerical eigensolver, a sampled p, or an approximate spectral-ordering assertion.

If a0,b>0 and the quadratic test fails, the interior root is `s=c/(2b)` and

$$p_\star={c\over b+c}.$$

The denominator is positive and c<2b implies `0<p_star<2/3`; again the actual trace gap is strictly positive. This includes d0 without division by d.

The interface requires the FULL actual density matrix and rank-k orthogonal projector. It does not construct them. Rational entries would make a,b,c,d and the sign predicate rational, while the critical parameter in the a>0 case can be algebraic; this is a witness FORMAT only. No such strict physical failure is supplied in the source or by this review.

## 8. Whole-consolidation scope audit, preserving earlier trust boundaries

I read all preceding and following sections, not just section6.

### Retained mathematical imports

The new actual-pair argument consumes the older U1/rank-matched U2 and full high-noise endpoint statements explicitly named at S1 LF15–22. Their pins are the central proof `10e4689c7ac8586fc920651eade6db37fa60be3b693f73b5f4ec7b6644fe6d23`, old U2/partial-channel proof `6789e392dbc70dbed479ba8f307e0eb6c786d735de691d425583ec0d8b2fce8a`, and operative addendum `73b6abb4e0a10b4fb9fe54ae5be853130c45a466b65a258c17385bc9911267d4`. This review does not re-prove or replay those complete packages. Their prior recorded scopes, not a new blanket parent promotion, are the physical reduction's explicit trust boundary.

The Pauli norm/signed-map/overlap predecessors are named at LF24–29 with pins `5a067a6fb6c746ab0a47c20df2bc6b025986125dd18b2cda0ab045a82c896a83` and `7ad282ae26ca9cf96153866e82cd5c16121ea395dfa329da6812d4ca8efc4bb4`. Their separate review gates are not automatically accepted by this consolidation or by the present noise-elimination review.

### Nonclaims correctly preserved in sections3–5

The all-complex Pauli-pair argument gives the single-vector operator norm route and Z<=4I, not a simultaneous top2/3/4 Gram bound with a common rotation. The source explicitly warns that several complex coefficient vectors may not share a perpendicular axis. Its pure-state X3 interlacing statement is not extended to mixed states by an invalid rank-one argument.

The signed B-map Ky-Fan inequalities are marked SUFFICIENT targets, neither proved nor physically refuted. A failure of that stronger sufficient route would not alone be a channel counterexample. The overlap-budget statements are necessary actual-pair restrictions, not a proof that leading projectors have the forbidden overlap or can be replaced by projectors containing the state.

I did not turn these read predecessor proofs into new independent verdicts; they retain their named earlier mathematical/review boundaries. No proof of the physical quartic follows from merely retaining them.

### Relaxed controls remain nonphysical — sections7–8

The supplied relaxed controls have b=d0 and positive a,c. In that case D reduces algebraically to `-4ac^3`, explaining the displayed negative values `-68/11,-96,-8`. This is only a consistency check of the NEW scalar formula with their stated coordinates, not a re-audit of the full PPT/twirled relaxation or its Hx feasibility.

Crucially these tuples do not supply `omega=bar(rho) tensor Pi`, an actual projector, or the required nonlinear compatibility. Neither their negative D values nor an exact p_star turns them into physical states. Adding D>=0 as an optimization constraint before proving it on actual pairs would encode the sought conclusion, not certify it independently. The source explicitly says so.

The Zhang prior-claim ancestry is retained at S1 LF33 and the named source audit `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`. I have not newly authenticated that external note or removed its stated uniform-weight ambiguity. No clean novelty/priority claim is available from this review.

The final per-index ledger correctly leaves k2,3,4 OPEN for the whole low-noise interval. The old joint-Hessian gap, simultaneous Gram sums and full source/projector compatibility are not repaired by an exact one-variable scalar reduction.

## 9. NOT_RECONSTRUCTED obligations and disposition

**No new load-bearing section6 identity or degeneracy is left unreconstructed.** In particular the physical expansion, endpoint interface, exhaustive scalar split, reversible squaring and all quartic coefficients, pure-to-mixed logic and p_star witness interface have the displayed derivations.

The following are intentionally NOT_RECONSTRUCTED or OPEN:

1. **NOT_RECONSTRUCTED in this review:** full predecessor U1/U2/high-noise certificate proofs and replays; they are exact named imports, not newly passed gates.
2. **NOT_RECONSTRUCTED as separate new verdicts:** all predecessor Pauli/signed-map/overlap-budget proofs and their prior review packages, and complete feasibility arithmetic of the relaxed Hx tables. They were read in the consolidation to audit scope, not promoted beyond this assignment.
3. **OPEN:** D>=0 or the quadratic predicate for EVERY ACTUAL state/projector pair in the corresponding interior branches. No physical quartic theorem, actual strict failure or low-noise k2/3/4 solution is given.
4. **NOT_SUPPLIED:** actual rho/Pi counterexample matrices, a finite search bound, executable witness, or a sampled/eigensolver-certified channel failure.
5. **NOT_PERFORMED:** parent acceptance, formal/kernel verification, human/cross-vendor/configured-dual-family review or novelty clearance. Parentv8's withdrawn premature promotions are not reinstated.

**Recommended disposition:** retain the NEW exact noise-elimination theorem as a completed no-defect WRITTEN reconstruction at its stated endpoint/deficit imports. Its quartic is an exact physical frontier, NOT an established universal physical inequality. Keep all three channel indices, actual compatibility and Zhang ancestry explicitly open/qualified. No scientific permission is issued by this return.
