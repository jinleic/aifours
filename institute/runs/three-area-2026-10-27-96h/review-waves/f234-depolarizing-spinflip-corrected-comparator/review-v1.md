# f234: fresh same-harness review of corrected spin-flip comparator

## Disposition and claim-by-claim findings

**Corrected scientific scope: supported by the written reconstruction below, with 0 outstanding FATAL / 0 outstanding MAJOR / 0 outstanding MINOR findings.** This applies to the complete quantified inequality and sufficient criterion in 190 and to the expressly corrected 186 comparison, not to global four-qubit k3. In the table, `0F/0M/0m` means no finding of those severities against that *corrected, stated claim*; it is not an assertion of formal or human verification. Historical source questions are separately INCONCLUSIVE. The false uncorrected overlap wording is recorded explicitly below and is not silently treated as true.

| ID | Exact claim and finding |
|---|---|
| C1 | **0F/0M/0m.** For every actual four-qubit density, every actual complex orthogonal rank-three projector and every physical `0 <= p <= 4/3`, the same-Q spin-flip identities, signed gap inequality, and scalar all-Q envelope (190 (1)–(4)) follow as written. The lower bound may be negative. |
| C2 | **0F/0M/0m.** `B1+B3=24-8kappa`, `B2+B4=15+8kappa`, `x<=min(20,24-8kappa)`, and `|q-qtilde|<=min(d,sqrt(3-kappa))` hold for the same objects. The scalar k maximization is a relaxation, not an assertion that each k is realized. |
| C3 | **0F/0M/0m.** Both signs of `s=1-p`, the singular endpoint `t=0`, and the physical endpoints are handled; no reflection, independent projector, or sign substitution is needed. |
| C4 | **0F/0M/0m.** The displayed state is physical and genuinely entangled across every nontrivial bipartition. At `p=9/16`, the strict all-projector gap is greater than `13363/5242880`. This is one state, not an all-density statement. |
| C5 | **0F/0M/0m.** The stated actual complex Q, its Pauli budgets, same-Q spin-flip overlap, fixed-Q certificate, direct channel trace and reference are correct. That Q is not asserted optimal. |
| C6 | **0F/0M/0m.** The complete unreviewed 186 same-projector bound and relaxed optimizer are independently reconstructed below. For the state at `t=7/16`, that *sufficient test* fails strictly, while the 190 all-Q test succeeds. This is not failure of the original k3 inequality. |
| C7 | **0F/0M/0m.** The 186 `t=1/3` strict all-Q certificate, stated actual diagonal-Q traces, and exclusion of the corrected named fixed-p pure-class hull are reconstructed. The same named-hull exclusion holds at `t=7/16`. |
| C8 | **0F/0M/0m.** Erratum 192 gives the correct *squared* product-overlap argument. The original line-161 unsquared reading is false; its uncorrected literal amplitude-bound defect is a **historical MAJOR, resolved within this corrected gate by 192**, not an outstanding defect of the corrected conclusion. |
| C9 | **0F/0M/0m for the displayed algebra only; INCONCLUSIVE for source provenance.** The pure-state `A2,A3,A4` identities and the quoted 192 polynomial equivalence are independently derived below, and the rational comparator failure is checked. Whether the unlisted historical source actually states that expression, and its priority, are not established here. |
| I1 | **INCONCLUSIVE, not a defect in C1–C8.** The later source-identity/read assertions in 192, the original historical definition and threshold for `G`, the stated public clipped-tail attribution/support/priority, and any author-code execution or previous-review outcomes are not independently verified. Their linked bodies are not declared inputs and were not opened. No novelty, earlier-source exclusion or priority claim is made. |
| I2 | **Inherited premise only.** The expressly adopted f200 all-density window is `|1-p|<=1/142`; no linked source, prior review, or underlying f200 proof is imported. Scope erratum 192 and the class-H correction are read as declarations and reconstructed where used, not as independent proofs. |

No F/M/m finding above implies an all-density theorem at `9/16` or `4/3`, a global k3 proof, full majorization, equality classification, or R-positivity. The adopted f200 window is around complete depolarization, not the identity. Same-harness review is not human, independent-model-family, formal/kernel, or novelty verification.

## Read, measurement, and control chronology

The first research artifact was the assigned manifest. Before reading it, `shasum -a 256` returned its supplied full hash `3c01716f61c3ea4aa213a841322e6751ea88892b98f6ff8f454b89f4b7939585`. I then displayed the manifest raw. Before **any declared input body**, a single measurement invocation returned all five whole-file SHA-256 values followed by `wc -lc`; each exactly matched all three manifest declarations below. Source bodies were then displayed raw, in the manifest order, in the actual windows stated here; no raw window exceeded 15 lines. All input line numbers including the final line were displayed before any mathematical reconstruction or scientific control.

| Order / role | Declared full path | SHA-256 | Bytes / LF | Actual raw windows, inclusive |
|---|---|---|---|---|
| 1, mandatory newly supplied correction 192 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261029-192-186-overlap-and-attribution-erratum-v1.json` | `57dc0cb45c78ea3a00422ebba52363e604dcdaae2044534fa17c054e2b958e89` | 5561 / 27 | 1–15, 16–27 |
| 2, class-H scope correction | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-depolarizing-k3-class-H-scope-erratum-v1.json` | `c9b5632e8285298a6b8438842498fc5a35695a889efcee0245836c2cbf038db2` | 2444 / 27 | 1–15, 16–27 |
| 3, adopted window for comparison only | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-depolarizing-k3-all-density-window-one-over-142-parent-v1.md` | `bb16e861cedad17fc2a9eb9520dba4cb7bdbd69ad3cd510df2e7bd59060f8b54` | 4873 / 17 | 1–15, 16–17 |
| 4, unreviewed comparator 186 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261029-186-common-projector-pauli-budget-v1.md` | `36aa530048387e244b27815e25fb93f38ad98366af37d839f047732dd9cba922` | 11016 / 167 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–167 |
| 5, target 190 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261029-190-spinflip-coupled-original-k3-v1.md` | `ef8e08229d3a84ec7051de7d3f9fc2dce717b3d4f57bdb377086df20c5ac1d34` | 11494 / 211 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–195, 196–210, 211–211 |

After those complete body reads, I independently reasoned, wrote and ran the reviewer control described below, and subsequently checked the last byte of each of the five inputs: all five were `0a`. Thus the final displayed lines were LF-terminated; the separate one-byte confirmation was chronologically **after** the control, not before it. The SHA/byte/LF-count measurements, and every raw ending read, were before the control. There was no manifest-order deviation or other research-input deviation. Process instructions and memory summary were consulted as instructions, not scientific premises. No held/f161/f162 source, other review/status/control/derivation, author code, linked unlisted body, web, solver output, literature recollection, or author contact was used as evidence.

## Independent derivation: physical domain and same-Q identities

Write `Phi_p(X)=(1-p)X+(p/2)Tr(X)I`, `s=1-p`, and `t=|s|`. The Pauli-channel decomposition has weights `1-3p/4` on the identity conjugation and `p/4` on each of X, Y, Z conjugation. These are precisely the four eigenvalues of the normalized Choi matrix in the orthogonal Bell basis, so the completely-positive trace-preserving physical range is exactly `0<=p<=4/3`. Consequently `0<=t<=1`, with negative s only for `1<p<=4/3`. At `p=0` the map is the identity; at `p=1` it is complete depolarization; at `p=4/3` it is still physical with `s=-1/3`.

For a product pure input, each local output has eigenvalues `a=(1+t)/2`, `b=(1-t)/2`, in either sign of s. The three largest four-fold product eigenvalues sum to `a^4+2a^3 b`, so

`16 R3(t)=3+8t+6t^2-t^4`.

Let `Theta=Y^tensor4 K`, `Gamma(X)=Theta X Theta^-1`, and put `rho_tilde=Gamma(rho)`, `Q_tilde=Gamma(Q)`. Because four Y factors make `Theta^2=1`, `Gamma` maps every weight-j phase-free Pauli to `(-1)^j` times itself, preserves positivity, trace and rank, and is self-adjoint for the real Hilbert–Schmidt pairing of Hermitian matrices. Therefore `qtilde=Tr(Q rho_tilde)=Tr(Q_tilde rho)`. Write `a_P=Tr(rho P)`, `b_P=Tr(Q P)`, `A_j=sum_wt=j a_P^2`, `B_j=sum_wt=j b_P^2`, and `kappa=Tr(Q Q_tilde)`. The quantities are real and all of these sums use **the very same** rho and Q.

Pauli orthogonality gives `B0=9`, `sum_j B_j=16 Tr(Q^2)=48`, and `16 kappa=sum_j (-1)^j B_j`. Adding and subtracting produces

`B1+B3=24-8kappa`, `B2+B4=15+8kappa`.

Both projectors are positive and rank three, so `0<=kappa<=3`. Since `B3>=0`, `x=B1<=24-8kappa`.

Independently, rotate each one-body trace vector of Q to its local Z axis. Its squared length, and hence x, is unchanged. The diagonal entries `z_v` of the rotated actual Q obey `0<=z_v<=1` and `sum_v z_v=3`. The squared norm of the four Z traces is convex in z, so its maximum on this hypersimplex occurs at a vertex: three distinct binary strings. If their pairwise Hamming-distance sum is h, then `x=36-4h`. Three distinct binary strings must vary in at least two coordinates, and each varied coordinate contributes two to h; thus h>=4 and x<=20. This argument uses only the diagonal of the actual complex projector; it does not replace it by a separate projector. Both bounds combine to `x<=min(20,24-8kappa)`.

Set `Delta=q-qtilde` and `d=(1/2)||rho-rho_tilde||_1`. The traceless Hermitian operator `rho-rho_tilde` has positive and negative parts each of trace d. Since `0<=Q<=I`, `|Delta|<=d`. Also let `D=Q-Q_tilde`. `Gamma(D)=-D`, so the antiunitary maps each eigenvector of D with real eigenvalue lambda to one with eigenvalue `-lambda`. As `Tr(D^2)=6-2kappa`, each nonzero absolute extremal eigenvalue occurs with an opposite partner and hence `||D||_op^2<=Tr(D^2)/2=3-kappa`. Because `Delta=Tr(rho D)`, also `|Delta|<=sqrt(3-kappa)`. These yield exactly the stated minimum. For pure rho, the two nonzero eigenvalues of `rho-rho_tilde` are `+-sqrt(1-C)` with `C=|<psi|Theta psi>|^2`, so `d=sqrt(1-C)`.

## Independent derivation: signed gap, scalar criterion and boundaries

For `c_j=sum_wt=j a_P b_P`, channel eigenvalues on Pauli strings imply

`16 Tr(Q Lambda_p(rho))=3+s c1+s^2 c2+s^3 c3+s^4 c4`.

The parity action and Pauli expansion give `c1+c3=8 Delta`, so for either sign of s the odd term is exactly

`s(1-t^2)c1+8s^3 Delta`.

Let `S=A1`, order the actual local Bloch radii `r1<=r2<=r3<=r4`, and let `L=r1+r2+3r3+3r4`, `m=min(L,sqrt(Sx))`. Cauchy–Schwarz gives `|c1|<=sqrt(Sx)`. Alternatively `c1=Tr(Q H)` for the commuting local Hamiltonian `H=sum_i r_i n_i.sigma_i`. Its three largest eigenvalues are `sum r_i`, `sum r_i-2r1`, `sum r_i-2r2`; their sum is L, while the three smallest sum to -L. Hence `|c1|<=L`. This top-three assertion follows by diagonalizing H and using `0<=<v_i|Q|v_i><=1`, `sum_i <v_i|Q|v_i>=3`.

For the even term, with `E_t=A2+t^4 A4`, Cauchy–Schwarz on the actual Pauli coefficients and the exact Q budget gives

`c2+t^2 c4 <= sqrt[(A2+t^4 A4)(B2+B4)] = sqrt[E_t(15+8kappa)]`.

For `t>0` write `epsilon=sign(s)`. Because physicality gives `1-t^2>=0`, insertion of these bounds gives

`16(R3-Tr Q Lambda_p(rho)) >= t[8+6t-t^3 -(1-t^2)m -8t^2 epsilon Delta -t sqrt(E_t(15+8kappa))]`.

The signed overlap is not replaced in this inequality. It is valid when `s<0` because `s^3=epsilon t^3`. When `t=0`, the channel output is `I/16`, the two sides are exactly zero, and epsilon need not be defined. At `t=1`, the coefficient of m is zero, so the same proof remains valid without dividing by `1-t^2`.

For the uniform criterion, the previously established bounds yield, for the actual Q,

`(1-t^2)m + 8t^2 epsilon Delta + t sqrt[E_t(15+8kappa)] <= F_t(rho,kappa)`,

where

`F_t(rho,k)=(1-t^2) min(L,sqrt(S min(20,24-8k))) + 8t^2 min(d,sqrt(3-k)) + t sqrt(E_t(15+8k))`.

The continuous function has a maximum `M_t` on `[0,3]`. This interval contains every actual kappa but can include infeasible combinations; it is an upper relaxation, not a joint-attainability statement. Taking the maximum over actual rank-three Q, equivalently the top-three eigenvalue sum `K3`, proves

`K3(Lambda_p(rho)) <= (3+t M_t)/16`,

`16(R3-K3) >= t[8+6t-t^3-M_t]`.

Thus the displayed test `M_t<=8+6t-t^3` is sufficient for this rho and p, including mixed rho without choosing a decomposition. It is not asserted necessary and need not hold for all inputs. At `t=0`, the direct `I/16` calculation is the equality case regardless of the numerical form of the relaxation.

## Independent reconstruction of unreviewed comparator 186

Let `H_t=A2+t^2 A3+t^4 A4`. From the same Q, `sum_{j>=2} B_j=39-x`. Weighted Cauchy–Schwarz over all weight-2,3,4 strings, retaining actual powers of s, gives

`|s^2 c2+s^3 c3+s^4 c4| <= t^2 sqrt[H_t(39-x)]`.

Together with `|c1|<=min(L,sqrt(Sx))`, this independently yields 186's same-rho/Q/p inequality

`16(R3-Tr Q Lambda_p(rho)) >= t[8+6t-t^3-min(L,sqrt(Sx))-t sqrt(H_t(39-x))]`.

For `S>0`, set `u=L^2/S`; Cauchy–Schwarz against `(1,1,3,3)` gives `u<=20`. On `[0,u]`, the bracket being subtracted is `f(x)=sqrt(Sx)+t sqrt(H_t(39-x))`, whose unconstrained maximizer is `x0=39S/(S+t^2 H_t)`; this also handles `t^2 H_t=0` by `x0=39`. On `x>=u` the first term is L and the second is nonincreasing. Thus the relaxed maximum is at `x*=min(u,x0)` and equals `B_t=sqrt(S x*)+t sqrt(H_t(39-x*))`. When `S=0`, L=0 and the relaxed maximum is `B_t=t sqrt(39H_t)`. The optimizer is not claimed physically attainable. Ky Fan maximization gives the 186 all-Q bound and its sufficient test `B_t<=8+6t-t^3` for mixed inputs as well. This derivation does not import 186 as adopted.

Parseval for rho gives `A2+A3+A4=16Tr(rho^2)-1-S<=15-S`, and physical `t<=1` gives `H_t<=15-S`. Therefore `B_t<=L+t sqrt(39(15-S))`, while `8+6t-t^3>=8+5t`. Consequently the corrected scope's pure-state `D_p` condition `8-L>=t(sqrt(39(15-S))-5)` implies the 186 sufficient test. The adopted named class is pure-input at fixed p; the algebra itself is not a mixed-state class-hull claim.

## Independent exact state, strict all-Q gap and comparison

Take `psi=(3|0000>+|0011>+|0101>+|1110>)/sqrt(12)` and `rho=|psi><psi|`. Normalization is `(9+1+1+1)/12=1`. No two support strings differ in only one site, so all one-site marginals are diagonal. Their radii, in site order, are `(5/6,2/3,2/3,2/3)`. Direct exact enumeration of the 256 Pauli expectations, with the density entries obtained solely from these four amplitudes, yields

`(A0,A1,A2,A3,A4)=(1,73/36,145/36,215/36,107/36)`, `S=73/36`, `L=35/6`.

No support string is the complement of another, so `<psi|Theta psi>=0`, `C=0`, and `d=1`. For each of the seven bipartitions, an explicit 2-by-2 coefficient minor has unnormalized determinant 3 (the reviewer control prints its row and column selectors). Dividing by 12 gives determinant `1/4` in the normalized coefficient matrix. Hence the state is not a product across any bipartition and is genuinely four-party entangled.

At physical `p=9/16`, put `t=7/16`, `T=8+6t-t^3=43177/4096`, `E=1084403/262144`, `u=L^2/S=1225/73`, and `k0=(24-u)/8=527/584`. The following is a written upper bound on **all** scalar k, not an optimization over a few sampled projectors.

* For `0<=k<=k0`, the first term in F is at most `(1-t^2)L`, the spin term at most `8t^2`, and the even square root at most `sqrt[E(39-u)]`. Since `(48/5)^2-E(39-u)=58990999/239206400>0`, this gives the strict bound `F<U0=26747/2560`.
* For `k0<=k<=2`, put `y=24-8k` in `[8,u]`. The spin term is at most `8t^2` and the remainder is the concave function `(1-t^2)sqrt(Sy)+t sqrt[E(39-y)]`. Its unconstrained maximum is at `y0=39(1-t^2)^2 S/[(1-t^2)^2 S+t^2 E]`, and `y0-u=79223837221/10373979995>0`; it is increasing on `[8,u]`. Thus this case is also strictly below U0.
* For `2<=k<=3`, use `x<=8`, the spin term `<=8t^2`, and `15+8k<=39`. The exact inequalities `(81/20)^2-8S=649/3600>0` and `(51/4)^2-39E=323067/262144>0` give `F<U2=53167/5120<U0`.

The three cases are uniform and cover `[0,3]`. Since `T-U0=1909/20480>0`, the uniform-Q inequality gives the strict, exact result

`R3(7/16)-K3(Lambda_(9/16)(rho)) > (7/16)(1909/20480)/16 = 13363/5242880`.

This p is outside the adopted f200 window (`7/16>1/142`), but the proof adds only this one input at that p.

For the *independently reconstructed 186* criterion at the same state and p, `H=12456587/2359296`, and `x0-u=412938801007/44654331921>0`, so its scalar maximum is at `u`. Moreover

`H(39-u)-[(T-L)/t]^2=2129511149/1406533632>0`.

Here `T-L>0` and `t>0`; taking positive square roots shows `B_t=L+t sqrt[H(39-u)]>T`. Thus that sufficient test fails strictly, while the separate spin-flip all-Q proof succeeds. No assertion that k3 fails or that all other previous methods fail follows.

## Actual complex Q and the 186 examples

Take Q as the orthogonal projection onto `|0000>`, `|0101>`, and `(|0011>+i|1111>)/sqrt(2)`. Exact arithmetic gives

`(B0,B1,B2,B3,B4)=(9,6,12,10,11)`, `kappa=1`, `q=7/8`, `qtilde=3/8`, `Delta=1/2`, and `(c1,c2,c3,c4)=(5/3,9/2,7/3,5/2)`.

These obey both Q budgets and `c1+c3=8Delta`. At `p=9/16`, `6S<(7/2)^2` and `23E<(49/5)^2`, so the signed same-Q bracket is strictly greater than

`T-(1-t^2)(7/2)-4t^2-t(49/5)=54437/20480`.

Its fixed-Q gap is therefore `>381059/5242880`. Independently applying the tensor product of the original single-qubit channel to matrix units yields

`Tr(Q Lambda_(9/16)(rho))=639301/2097152`, `R3=498847/1048576`, actual gap `358393/2097152`.

The same direct channel computation gives, for this same rho and complex Q, `(p, trace, gap)=(2/3,169/648,29/216)` and `(4/3,13/72,139/648)`, with reference `32/81`. These are fixed-object checks, not all-density theorems.

For 186's diagonal `Qd=|0000><0000|+|0011><0011|+|0101><0101|`, the actual B sectors are `(9,12,6,12,9)`. Direct matrix-unit channel traces and gaps are `(5/18,19/162)` at `p=2/3` and `(41/324,29/108)` at `p=4/3`. At `t=1/3`, the 186 relaxation has `H=13787/2916`, `x0=2075463/67004>u`, and `H(39-u)=11181257/106434<121`. Therefore `B_t<35/6+11/3=19/2`, and its all-Q conclusion is `K3<37/96=32/81-25/2592` for this particular rho at both physical signs. For Qd itself, `Sx=73/3<25` and `H(39-x)=13787/108<144`, so the 186 fixed-Q lower gap is indeed `>13/648`.

## Corrected named-hull and squared-overlap comparisons

The declared scope correction requires both the moment condition `4S+8C<=64/9` and its additional spin-flip condition for pure class H. Here `4S+8C=73/9>64/9`, so the necessary moment condition fails. The state is not P by the seven minors and not U because its one-site Bloch radii are nonzero. With `delta=8-L=13/6`, the pure class `D_p` test fails strictly: after comparing nonnegative quantities,

`39(15-S)-(5+delta/t)^2 = 1121/3 > 0` at `t=1/3`,

and `=717713/1764 > 0` at `t=7/16`.

If a rank-one density is a finite convex combination of pure states, expectation against every vector perpendicular to its ray forces every positively weighted summand to lie on that same ray. Thus rho is outside the **named fixed-p** finite convex hull of P, U, corrected H and `D_p` at these parameters. This is not an exhaustive statement about all other regions.

The mandatory 192 correction defines the local comparison quantity `G(psi)=max_product |<phi|psi>|^2`. For any normalized product phi and any site i, projection onto its one-site factor and Cauchy–Schwarz give `|<phi|psi>|^2 <= <phi_i|rho_i|phi_i> <= lambda_max(rho_i)`. Choosing a site with radius `2/3` gives `G<=5/6<124/125`. This proves the corrected squared-overlap exclusion against the threshold as **stated in 192**. It does not independently verify the definition or threshold in an unlisted historical source.

The square is essential. The displayed product vector `|0000>` has amplitude `3/sqrt(12)=sqrt(3)/2>5/6`, while its squared amplitude is `3/4<=5/6`. Thus the literal uncorrected 186 assertion that every *unsquared amplitude* is at most `5/6` is false. Erratum 192 supplies the correct proposition and proof before 186 is consumed in this gate; the earlier text or earlier review chronology is not rewritten.

## Pure-state polynomial comparison and historical boundary

The relevant algebra can be reconstructed without opening any historical source. For a pure four-qubit rho, Parseval and the spin-flip overlap give

`A1+A3=8(1-C)`, `A1+A2+A3+A4=15`.

Equality of complementary reduced purities follows directly by viewing psi as a matrix and comparing `Tr[(MM^dagger)^2]` with `Tr[(M^dagger M)^2]`. Summing this equality over the four one-versus-three cuts gives `2A2+A3=12+S`. With `A1=S`, these identities imply

`A2=2+S+4C`, `A3=8-8C-S`, `A4=5-S+4C`.

Consequently 192's displayed pure expression is algebraically exactly

`39[S+t^2 H_t]=39[S+t^2(2+S+4C)+t^4(8-8C-S)+t^6(5-S+4C)]`.

For the displayed state at `t=1/3`, direct fractions give `39(S+t^2 H_t)-(8+6t-t^3)^2=680/2187>0`. This is a mathematically checked failure of that specific scalar comparison. It does **not** independently establish that an unlisted historical body states the comparison, nor its validity, completeness, attribution or priority. Similarly, later source-reading assertions and public-source facts in 192/190 remain INCONCLUSIVE here, not imported premises.

## Reviewer-owned finite control and limitations

The only control was newly written `reviewer-control-v1.py` in this wave directory, full SHA-256 `a19f8a97d828d6fb3aea9857422f3fc27d41b8e437ed82d4d8cabffeecc1b9bb`. It imports no author code and uses standard-library `Fraction` pairs for exact complex arithmetic. The invocation measured the hash, then observed `/bin/date` start `2026-10-29T14:15:34-0700 PDT`, ran `python3 -B reviewer-control-v1.py` with a 120-second tool limit, observed `/bin/date` end `2026-10-29T14:15:34-0700 PDT`, and returned actual exit `0`. It did not hit its cap. Its exact output includes the A and B sectors, c sectors, kappa and overlap, seven explicit determinant-3 minors, the rational margin comparisons, and direct matrix-unit traces versus Pauli expansions at `p=0,9/16,2/3,1,4/3`. It also enumerates all 560 three-string diagonal vertices, obtaining maximum x=20; the separate convexity argument above covers arbitrary complex Q.

Intended-reason negatives were exercised, not merely listed: (i) omitting conjugation in the complex spin flip changes entry `(0,12)` from `-i/2` to `+i/2`; (ii) dropping epsilon for `s=-1/3` changes the exact odd term by `8/27`; (iii) the amplitude/square confusion is exposed by `3/4>(5/6)^2` although `3/4<5/6`; and (iv) unphysical `p=3/2` gives Choi identity weight `-1/8`. These negatives reject the designated wrong formulas/boundary; none is a k3 counterexample. The finite control supports arithmetic for its selected objects, not the universal quantifiers; those rest on the written derivations. No solver, build, test suite, author checker, external theorem lookup, or other scientific control was run.

**Remaining gap:** Outside the explicitly adopted f200 interval and states for which a proved sufficient criterion applies, this review does not decide the original all-density k3 conjecture. The later historical definitions, author execution claims and source attributions remain unverified as stated above. The full SHA-256 of this immutable review is supplied with the delivery message after the file is written, rather than as a self-referential digest inside its own bytes.
