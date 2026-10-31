# info-6: every peak 3-flat forces external autocorrelation compensation

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T15:46:21-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is a conditional universal compatibility statement, not a selected cube/direction, witness, unrestricted no-go, rank/type exclusion, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program or selected-state/plane probe was used.

## Claim

Suppose an actual original balanced peak≤28 f exists. For **every** affine 3-flat E in its peak set, at least one nonzero direction b of E has the following property: all four unordered b-pairs inside E have the same product sign, and at least four nonzero b-pairs entirely outside E have the opposite product sign. The number of such nonzero directions of E is either 1 or 7. Different E may reuse directions and outside pairs; no independence is claimed.

## Proof

Use the definition-first mod-4 coupling. On the odd affine 8-half containing E, the peak signs are given by one Boolean polynomial Q of degree at most 2, as in `walsh-odd-half-quadratic-sign-v1.md`. Restrict its second difference to the three-dimensional direction H of E; it is an alternating bilinear form 𝔅_H. For every b∈H,

    ε(a)ε(a+b)=(-1)^{Q(a)+Q(a+b)},   ε(a):=sgn k(a),  a∈E.

The exponent is affine-linear in a with linear part h↦𝔅_H(b,h). If that linear part vanishes, all eight products, hence all four unordered pair products, have one sign. If it does not vanish, it is balanced on E, so two unordered pairs have each sign.

An alternating bilinear form on a 3-dimensional binary space is either zero, or has exactly one nonzero vector in its common kernel: in the nonzero case choose u,v with 𝔅_H(u,v)=1, extend by w, and solve the two linear equations for the common kernel; the solution is a single nonzero vector and its zero multiple. This is an elementary local 3-space fact, not a selection or classification of an original polar rank. Therefore either all seven nonzero directions or exactly one have constant pair-product sign.

For any such b, the four unordered pairs inside E contribute ±4·49=±196 to the exact full-spectrum b-autocorrelation. Since E is b-invariant, every other unordered b-pair lies wholly outside E. The total autocorrelation is zero, so the outside pairs of opposite sign must contribute absolute product at least 196. Each product has magnitude at most 49, hence at least four such nonzero opposite-sign pairs are required. This holds for every actual E and each of its constant-product directions; it selects none. ∎

## Status and imports

The parent-notified ≥92-peak result plus `walsh-forced-peak-3flat-v1.md` would supply existence of at least one E only if that new combinatorial candidate is reviewed; the stronger ≥46 count is likewise unreviewed. The present theorem itself is conditional on any E, whether or not one is known to exist. It does not prove the required compensation impossible, construct a witness or close any original rank/weight or `(24,24,2)` alternative.

Inputs are the S1 definitions, exact autocorrelation/mod-4 caller `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF, and the unreviewed all-variable phase consequence `walsh-odd-half-quadratic-sign-v1.md` SHA-256 `be6421feeb80f076373e09aaccb4a6ed1401591db892e82fe77c64831aa215e7`, 35 LF. No parent disposition/review body, old Gate-I/candidate/HELD source, stopped half-split method or source-selection/method guide is an input. Full-scope independent review, book-source equivalence, human, formal/kernel, executable and novelty gates remain unperformed for this result. Prior exposure, metadata-poll MINOR, S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
