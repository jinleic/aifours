# A direct selector for part of the third five-node phase pattern

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:46:22 PDT 2026**. **WRITTEN fixed-data LP characterization with a WRITTEN-checked-in-kernel realized phase example**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This does not settle pattern C or unrestricted SPR7.

## 1. Fixed-data selector LP

For an admissible independent odd coefficient box with root bands \([a,b],[c,d],[e,f]\), fix
\[
a<t_1<b<c<t_2<t_3<d<t_4<t_5<e. \tag{1}
\]
This is a subcase of direct phase pattern \(C=(2,4,3,5,4)\): the second/third nodes make the odd-band reversal and the fourth/fifth nodes make the even-band reversal. A nonzero odd-moment ray has signs \((- ,+,-,+,+)\).

Use
\[
\xi=(1-\theta)t_4+\theta t_5,\quad 0\le\theta\le1,\qquad
F_\theta(t)=(-t)(c-t)(\xi-t). \tag{2}
\]
It has nonnegative even numerator coefficients and its roots lie in the closed even-root gaps. The eight direct odd-moment rays, from `frontier-20261029-three-strict-pattern-eight-ray-reduction-v1.md`, SHA-256 `8591da67f304472da00e7afb7bf1ddfc1c2a7970802f7c844cf8cd495ee93686`, have supports \(X=(t_1,t_2,t_3,t_4)\) and \(Y=(t_1,t_2,t_3,t_5)\), with each of the four omitted odd moments.

At the first three nodes the actual even and \(F_\theta\) signs agree, so the worst odd endpoints are \((O_-,O_+,O_-)\). The last odd value is positive throughout its gap, and both \(O_-\) and \(O_+\) must be considered there. The correct mixed even envelopes are
\[
X:\ (E_+,E_-,E_-,E_-),\qquad
Y:\ (E_+,E_-,E_-,E_+). \tag{3}
\]
Each of the resulting 16 endpoint/moment mixed-envelope pairings is affine in \(\theta\) and linear in the eight even interval endpoints.

Consequently the exact uniform-selector LP is identical to equation (4) in `frontier-20261029-pattern-b-mixed-band-selector-lp-v1.md`, SHA-256 `5b5cb29a32ea08c074375bf35c5d2a88d7cd743302099607ffa18fc84e4e49df`, with the 16 functionals here: choose one \(0\le\theta\le1\), and for each functional nonnegative multipliers on the six strict stability forms, four width forms and four positive even lower coefficients, with positive total weight on strict forms. Motzkin's strict linear alternative makes this LP feasible **if and only if** the test (2) has strictly positive pairing on each direct odd-moment ray uniformly over every admissible even box and actual member choice. Feasibility excludes a strictly-negative all-eight-coordinate certificate for the fixed odd/node data. Failure excludes only this uniform test family, not a certificate or common numerator.

The restriction \(t_1<b\) is material: if \(t_1\in[b,c)\), a class-2 actual member has negative even value but the box's even upper envelope can be positive there, so the first odd endpoint cannot be fixed by the same positive-term argument. That remaining part of pattern C is not covered.

## 2. An actual full-width phase-C instance

Take the odd intervals \([260,672]\), \([292,293]\), \([34,35]\), with bands \([1,4],[7,13],[20,24]\), and nodes
\[
(t_1,t_2,t_3,t_4,t_5)=(2,8,10,15,18). \tag{4}
\]
At \(\theta=1/2\), \(\xi=33/2\). The 16 exact finite odd-moment and nonnegative dual identities are frozen in `frontier-20261029-pattern-c-first-band-sixteen-duals-frozen-v1.json`, SHA-256 `465b359a465b9271a2c3ac10f42e6795b05b7b49d0a3406333a53d1343fe450b`. Each identity has a positive coefficient on a strict box form. Exact integer/`fractions.Fraction` arithmetic on one Python Eval host checked all 16 moment vectors \(-e_k\) and all 16 eight-coordinate identities. The chosen selector excludes a direct strict certificate at these odd data and nodes for **all** stable even interval boxes.

The phase placement itself is genuinely realizable. Use the all-seven-positive-width even intervals
\[
\ell=(87/1000,36479/500,1089/50,911/1000),\quad
u=(87/500,99099/1000,21867/1000,1089/1000), \tag{5}
\]
whose six positive band-sign margins are displayed in the pattern-B predecessor. At nodes (4), choose odd endpoints \((O_-,O_+,O_-,O_-,O_+)\) and even endpoints \((E_-,E_-,E_-,E_-,E_+)\). Their odd values are
\((-198,64,-270,140,924)\), and their even values are
\[
(-119703/1000,\ 43647/1000,\ 98097/1000,\ -261273/1000,\ 229443/500).
\]
Thus the actual parity signs are \((--),(++),(+-),(-+),(++)\), exactly phase word \((2,4,3,5,4)\), with both required reversed bands. This is not a negative atom certificate; the 16 duals exclude one at these fixed nodes.

## 3. Limits

Universal selector feasibility for all admissible inputs in (1), the subcase with the first node outside the first odd band, patterns A/B, larger supports and the original unrestricted septic-box synthesis-or-obstruction verdict remain **OPEN**. All arithmetic claims above are same-host exact checks; Motzkin, root interlacing, phase assignment and endpoint minimization are written deductions. No independent scientific review, formal proof, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
