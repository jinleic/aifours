# F741 independent author reconstruction: compactified zero dual and same-frequency steering

**Status:** NONBLIND same-harness GENERAL AUTHOR, written reconstruction conditional on the explicitly identified imports below; **UNADOPTED**. This is not a family, human, formal/kernel, source-identity, novelty, or global-closure gate. No actual eligible zero dual, strict-negative certificate, counterexample, or universal common numerator is produced. The parent must read this entire return and separately disposition it.

Native clock observed before this artifact's creation: `2026-10-30T17:21:56-0700 PDT`; this is an observation, not a claimed creation time or earlier cognition record. The reconstruction below is independent reasoning after reading S2; it is therefore **nonblind**, not an independent model-family review.

## 1. Exact object and the claims reconstructed

Let K be a nonempty compact independent real coefficient box of monic septics
\[
a(s)=s^7+\sum_{j=0}^6a_js^j,\qquad \ell_j\le a_j\le u_j,
\]
including zero-width intervals. Eligibility means **every actual member** of K is strictly Hurwitz. Put t=ω² and
\[
E_a=a_0-a_2t+a_4t^2-a_6t^3,\quad O_a=a_1-a_3t+a_5t^2-t^3,
\quad r_a=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]
Vectors are ordered by numerator coefficients q0,…,q7, and e0,e7 are the first and last unit vectors. The raw row is linear in the actual coefficient vector. At t>0 the four actual fixed parity-corner polynomials Cστ attain E_σ and O_τ simultaneously. Explicitly, E+ uses `(u0,ℓ2,u4,ℓ6)` on the even coefficients, E− the opposite endpoints; O+ uses `(u1,ℓ3,u5)` on the odd coefficients, O− the opposite endpoints. Thus the four corners are actual members. They generate each **row at that same t**, not the entire seven-dimensional coefficient box as polynomials.

The reconstructed conditional Theorem A has three parts:

1. For **every nontrivial** finite zero relation
   \[
   \sum_{j=1}^m w_j r_{C_j}(t_j)+\lambda e_0+\mu e_7=0,
   \quad w_j,t_j>0,\quad \lambda,\mu\ge0,\tag{1}
   \]
   with actual corners Cj of the eligible K, there are at least six **distinct finite positive frequencies** t_j. The endpoint terms are included; distinct corners at a single t count only once.
2. If any same-box zero dual exists, one exists in form (1), with
   \[
   m+\mathbf1_{\lambda>0}+\mathbf1_{\mu>0}\le8.\tag{2}
   \]
   Hence its number n of distinct positive finite frequencies is 6, 7, or 8. The eight bound counts **total compactified atoms**, including endpoints and repeated-frequency corner atoms; it does not assert six distinct frequencies or eight distinct frequencies.
3. If either all four even coefficient intervals or all three odd coefficient intervals are fixed, there is no same-box zero dual. Strict common-SPR on that box then follows only through the explicitly imported same-box equivalence.

The no-go for n=4 or 5 below is **conditional on the five-distinct-frequency strict-negative import**. The connected-hull reduction, endpoint handling, interpolation and fixed-parity arguments are written out here. The physical-band backtracking Theorem B in S2 was not independently assessed in this assignment and is not an ingredient or conclusion of this return.

## 2. Imports, boundaries and actual-member grouping

**S3 import:** on an eligible K, strict common-SPR with one monic degree-seven Q and one positive uniform margin for all actual members/frequencies is equivalent to the origin's exclusion from the convex hull of the four compactified actual-corner row curves. At t=0 a compactified row is `a0 e0`; at ∞ it is e7. S1 fixes the common polynomial, degree, margin, and ROOT-interface scope. This return does not re-prove the SPR/zero-hull equivalence or claim universal feasibility.

**S5 five-frequency import:** an eligible actual independent septic box admits no all-eight-strict-negative raw aggregate of positive weights at at most FIVE distinct positive finite squared frequencies, with actual members. This is the earlier no-go expressly retained in S5, in the actual-member scope also described by S2; its original proof is not in this packet. In the application below the box is an eligible two-coordinate enlargement L, with nondegenerate odd interval, and there are no endpoint atoms in the strict-negative aggregate. We do not replace this import with an unproved six-frequency claim, an atom-count bound, or scalar nonnegativity of individual rays.

**S3/S4 boundary import:** eligibility is equivalent to stable actual center b, `ℓ0>0`, and no positive t satisfying both `E_b²≤H_E²` and `O_b²≤H_O²`, where
\[
H_E=h_0+h_2t+h_4t^2+h_6t^3,\quad H_O=h_1+h_3t+h_5t^2,\quad h_j=(u_j-\ell_j)/2.
\]
The inequalities are closed: equality, tangency, and degenerate widths are not silently discarded. This is all-member eligibility, not corner-stability sufficiency. Since K is compact and the set of Hurwitz monic coefficient vectors is open, sufficiently small positive independent buffers of the a0 and a1 intervals produce another eligible box L. Indeed, a finite open-ball subcover gives a uniform positive coefficient-space distance from K to the non-Hurwitz set; a sufficiently small two-coordinate enlargement lies within it. No other coefficient interval needs to be widened, and K itself may be degenerate.

For any nontrivial (1), combine its finite atoms at the same distinct node `u_i>0`. Let `W_i` be their positive total raw weight and `a_i` the weight-normalized average of their corner polynomials. Convexity of the actual coefficient box gives `a_i∈K`, and row linearity gives exactly
\[
\sum_{i=1}^n W_i r_{a_i}(u_i)+\lambda e_0+\mu e_7=0.\tag{3}
\]
The grouped a_i is one actual member, usually **not** a corner; the same actual member supplies both its E and O. Grouping changes neither the raw aggregate nor n. Endpoint atoms never count as finite frequencies. With no finite groups, (3) forces λ=μ=0 by linear independence of e0,e7, contrary to nontriviality.

Conversely, at each positive t the actual pair `(E,O)` fills the rectangle `[E−,E+]×[O−,O+]`. If a side is nondegenerate use its usual interpolation parameter θ in [0,1]; if a side is degenerate choose θ=0. The product weights `(1−θ_E)(1−θ_O)`, `(1−θ_E)θ_O`, `θ_E(1−θ_O)`, `θ_Eθ_O` express its row as a same-t convex combination of the four actual corner rows. This remains correct when widths vanish or corners coincide. It does not identify the actual polynomial with a convex combination of those four polynomials. Under steering, the members remain actual L-members, and if desired their **rows** can be split into L-corner rows on the same frequencies; this may increase the corner-atom count and is unnecessary for the five-frequency import.

## 3. At most three groups: direct test vector, including endpoints

Let n≤3 in (3), and write `E_i=E_{a_i}(u_i)`, `O_i=O_{a_i}(u_i)`. For n≥1, interpolate a polynomial H of degree at most n−1 at the distinct positive nodes with
\[
H(u_i)=\frac{E_i-1}{u_i},\quad F(t)=1+tH(t).
\]
Independently interpolate J of degree at most n−1 with `J(u_i)=O_i+u_i³`, and set `G(t)=−t³+J(t)`. Then F and G have degree at most three, `F(0)=1`, G's cubic coefficient is −1, and `F(u_i)=E_i`, `G(u_i)=O_i`. For n=0 simply choose F=1 and G=−t³.

There is a real monic degree-seven **test vector** q with even/odd parts F,G: if `F=∑f_k t^k` and `G=∑g_k t^k`, take `q_{2k}=(-1)^k f_k` and `q_{2k+1}=(-1)^k g_k`, k=0,…,3. Thus q0=q7=1 and `q·r_a=F E_a+t G O_a`. No Hurwitz stability or coefficientwise positivity of this test vector is asserted or needed. Pairing (3) gives
\[
0=\sum_i W_i(E_i^2+u_i O_i^2)+\lambda+\mu.\tag{4}
\]
Each actual a_i is Hurwitz, so E_i and O_i cannot simultaneously vanish at a positive u_i. Hence every present finite term is strictly positive. When n=0, nontriviality requires λ+μ>0. Either way (4) is impossible. This covers repeated corners after grouping, zero or nonzero endpoint weights, and all degenerate boxes.

## 4. Exactly four selected frequencies: actual buffered steering

Suppose (3) has n≥4. Select any four different positive nodes, relabel them `u_1,…,u_4`, and retain their original positive grouped weights `W_i`. Define
\[
L_i(x)=\prod_{j\ne i}\frac{x-u_j}{u_i-u_j},\qquad
\delta a_{0,i}=-\epsilon\frac{L_i(-1)}{W_i},\qquad
\delta a_{1,i}=-\epsilon\frac{L_i(-1)}{W_i u_i}.\tag{5}
\]
All denominators are nonzero. Leave every other coefficient and every unselected group unchanged. For k=0,1,2,3, interpolation of x^k gives
\[
\sum_{i=1}^4 L_i(-1)u_i^k=(-1)^k.\tag{6}
\]
For each k the change in coordinate 2k is `∑ W_i (-u_i)^k δa_{0,i}=−ε`; the change in coordinate 2k+1 is `∑ W_i (-1)^k u_i^{k+1} δa_{1,i}=−ε`. Consequently the finite raw aggregate, formerly `−λe0−μe7`, becomes exactly
\[
(-\lambda-\epsilon,-\epsilon,-\epsilon,-\epsilon,
 -\epsilon,-\epsilon,-\epsilon,-\mu-\epsilon),\tag{7}
\]
strictly negative in all eight coordinates. No approximation, limiting argument or solver is involved.

Take any eligible L that contains K and has positive *two-sided* a0- and a1-interval buffers. Let b0,b1 be the smaller of the lower and upper added margins in those respective coordinates. Each selected starting a_i lies in K, and all `L_i(-1)` are nonzero. Thus it suffices to choose
\[
0<\epsilon<\min_{1\le i\le4}\left\{\frac{W_i b_0}{|L_i(-1)|},\frac{W_i u_i b_1}{|L_i(-1)|}\right\}.\tag{8}
\]
The selected perturbed coefficient vectors are actual members of L, even when the original coefficients were at K's endpoints or had zero width; unchanged groups are actual L-members too. The positive weights and exactly the original n frequencies are preserved. The two different coordinate buffers are essential to this construction; infinitesimal motion is not assumed to remain in K. If additional within-K slack happens to exist at every selected member, the same formula may stay in K, but that extra hypothesis is not automatic.

For n=4 or 5, (7) is a positive-weight actual-member all-eight-strict-negative aggregate on the **different eligible box L**, on n≤5 distinct positive finite frequencies. This contradicts the S5 five-frequency import. Therefore every nontrivial (1) has n≥6, including relations with endpoint atoms and arbitrarily many corner atoms at one frequency. This uses neither a same-box weak-to-strict claim nor an assertion that the perturbed members are corners.

## 5. Eight TOTAL atoms: complete connected-hull proof

Let `S=⋃_{σ,τ}{ r_{Cστ}(t)/(1+t)^7 : 0≤t≤∞ }` in R⁸. Each of the four curves is continuous on the compact interval `[0,∞]`: at zero it is `a0e0` with a0>0; at infinity every coordinate except the last tends to zero and the last tends to one. All curves share e7 at ∞. Their union S is therefore compact and path connected, including when some curves coincide because intervals are degenerate.

If `0∈conv(S)`, ordinary Carathéodory gives a representation with at most nine points. Representations with at most eight positive coefficients already suffice. In a nine-point representation, discard any zero coefficients; if the nine points are affinely dependent, an affine dependence has positive and negative coefficients because its coefficients sum to zero. Moving the barycentric weights along it up to the first zero removes at least one point while keeping all weights nonnegative and their sum one. Thus only the case of nine affinely independent points `p_0,…,p_8` with all `α_i>0` remains.

Choose a continuous path p(s) in S from p0 to p1, s∈[0,1]. Since the nine points affinely span R⁸, its fixed affine coordinates c_i(s), defined by `p(s)=∑c_i(s)p_i`, `∑c_i(s)=1`, are continuous. Let τ be the first zero of c0. It exists, τ>0, and c0>0 on `[0,τ)` because c0(0)=1 and c0(1)=0. For s<τ put
\[
d_i(s)=\alpha_i-\frac{\alpha_0c_i(s)}{c_0(s)}\quad(i=1,\dots,8).
\]
The exact affine identity is
\[
0=\frac{\alpha_0}{c_0(s)}p(s)+\sum_{i=1}^8d_i(s)p_i,\qquad
\frac{\alpha_0}{c_0(s)}+\sum_{i=1}^8d_i(s)=1.\tag{9}
\]
At s=0 every d_i is positive. At τ, `∑_{i=1}^8 c_i(τ)=1`, so some c_j(τ)>0. Near τ from below, c_j remains bounded away from zero and c0 tends to zero, making d_j negative. By continuity there is a **first** zero among the finitely many d_i before τ. At that point every d_i is nonnegative and at least one is zero, while α0/c0>0. Equation (9) is a convex representation using p(s) and at most seven of p1,…,p8: at most eight points total. An earlier collision of path points, multiple simultaneous zeros, or a zero barycentric coefficient only decreases the count. No nondegeneracy of the box or of its endpoint rows is required.

Convert finite normalized weights α_j at t_j>0 to raw weights `w_j=α_j/(1+t_j)^7`. All t=0 contributions combine into `λe0`, with `λ=∑α_j a_{0,C_j}≥0`; all t=∞ contributions combine into `μe7`, with `μ=∑α_j≥0`. The total number of remaining finite corner atoms plus nonzero combined endpoints cannot exceed the original number, hence (2). The single formal λe0 is a positive multiple of an **actual** zero-frequency row when λ>0, because any actual corner has positive a0; μe7 is the shared actual infinity point. If a convex normalization is wanted after selecting one actual zero-endpoint corner, divide all resulting positive conic coefficients by their total. This explicitly handles distinct a0 endpoint values: their original convex coefficients need not themselves sum to λ divided by the chosen a0.

Conversely any nontrivial raw relation (1) is a positive conic zero combination of actual normalized corner rows: use finite coefficients `w_j(1+t_j)^7`, a chosen zero-corner coefficient `λ/a0` if λ>0, and infinity coefficient μ if μ>0. Dividing by the positive total yields a convex zero representation. Thus endpoints are neither discarded nor treated as finite frequencies; no rationality of the frequencies or weights is claimed.

For a chosen sparse representation let `z=1_{λ>0}+1_{μ>0}`. Since `n≤m` and n≥6, (2) gives 6≤n≤8. If n=6, the number of groups containing at least two finite corner atoms is at most `m−6≤2−z`, so at least `4+z` groups are single actual-corner rows. In particular both endpoints force all six groups to be single. This count applies to the **chosen sparse representation**, not every original zero relation or the buffered strict-negative aggregate.

## 6. Fixed-parity exclusion, with degenerate and endpoint cases

Let b be the actual center and suppose first that all odd coefficients are fixed, so `O_a=O_b` for all a. Apply the real test vector with F=0 and G=O_b to (3). The finite pairings are `u_i O_b(u_i)^2≥0`, the e0 pairing is zero, and the e7 pairing is 1. Equality forces μ=0 and `O_b(u_i)=0` for every finite group. At each such node, the actual E interval cannot contain zero: the common odd value is already zero, so an actual member with E=0 would have an imaginary-axis zero. Since E_b lies in that interval, every actual E there has the same nonzero sign as E_b. Test instead with F=E_b,G=0. Every finite term `W_i E_b(u_i)E_{a_i}(u_i)` is strictly positive and the zero-endpoint term `λb0` is nonnegative. At least one finite group exists, a contradiction.

If instead all even coefficients are fixed, first test F=E_b,G=0. Its finite terms are `W_i E_b(u_i)^2≥0` and the e0 term is `λb0` with b0>0, so λ=0 and all `E_b(u_i)=0`. Actual eligibility makes every possible odd value at each such node nonzero with the sign of O_b. Testing F=0,G=O_b gives strictly positive finite terms `W_i u_i O_b(u_i)O_{a_i}(u_i)` and nonnegative endpoint term μ, a contradiction. These arbitrary real test vectors need not themselves be Hurwitz or monic; they merely pair with a zero relation. The argument covers singleton K and all zero-width/tangency boundary situations allowed by actual eligibility. The same-box strict-SPR conclusion is subsequently imported from S3, not a new independent harmonic proof.

## 7. Exact conditional conclusion and unpaid frontier

Combining §§3–6, conditional on the stated five-frequency no-go and same-box zero-hull imports, every eligible K satisfies: either it has the imported one-Q strict common-SPR property, or there is a same-K actual-corner zero relation (1) with at most eight total finite-plus-endpoint atoms and six to eight distinct finite positive frequencies. A zero relation is an obstruction to same-K strict synthesis by the imported hull equivalence; its buffered all-negative consequence lives on a **different** eligible box L. This is an exact conditional alternative, not a proof that the zero branch is empty or occupied.

No actual eligible box/weights/frequencies satisfying (1), and no actual strict-negative aggregate, is supplied. No universal strict-SPR, all-actual-ray/both-R5 ROOT theorem, quantifier-elimination outcome, or rational-frequency zero-dual result is established. The first global step remains to rule out all eligible both-parity zero relations at this exact support scope, or explicitly construct and independently verify one. Merely obtaining the support bound, an unverified finite search, nonpositive coordinates, a weak separator, or the existence of a buffer is not that step. S2's distinct Theorem B/backtracking and the complete ROOT ray interface remain outside this reconstruction; S1 and S5 state the latter import and its exclusions.

## 8. Complete packet coverage, pins and nonactions

Before any mathematical body access, I read the actual dispatch receipt and the complete manifest, freeze receipt, final binding, prepared metadata, and **all 22 manifest-listed controls through their endings**, then delivered the direct PREBODYACK to Main. Controls were used for permissions/status only. After the ACK I read the sole packet part serially in consecutive raw slices of at most 20 LF, covering packet LF 1–324 through its ending before mathematical comparison or research; no packet-body reads were parallel. The multipart policy as stated in the manifest and freeze receipt was read; the separately referenced policy file was not opened. All genuine held episodes and ALL proof/method/selection/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. No outgoing packet link, held history, unspecified sibling proof, or old code was followed. No private-cognition certificate is claimed.

The following local administrative SHA-256 observations were made after complete packet reading; file lengths and the input-source bindings were supplied by parent metadata, not independently re-rendered from original files:

- `manifest-v1.json` (270 LF): `5a4fcbd299a349123ec64883150948fcada2b2746c907c4b642cc0db67b2213b`.
- `freeze-receipt-v1.json` (116 LF): `64cd65a87e7329206da4b3e30469efc1992e7575f81938d64dc247397fedabd5`.
- `final-pre-dispatch-binding-v1.json` (198 LF): `bcf7120468da5ad16bb0ea46266f77849ffac06180bf4eaba3497b78877384ea`.
- `parent-live-metadata-supply-v1.json` (258 LF): `f221cc02b2bdc8c6bd8d469d3c3120c35ad709762da63dc715b3f48afde83eef`.
- `dispatch-receipt-v1.json`: `06625ef1484fde6e47a93b0d5494cd2f135b9dfd3cd3bbc09c29c0f7fd6c8557`.
- `literal-packet-part-01-v1.md` (324 LF): `d80214cc86e0e5ef068d9f1321b2b718a3c3c98a6f396ae0c8c0292528f5df74`.

All paths immediately above are under `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f741-septic-eight-atom-zero-dual-and-steering-proof-author/`. The packet gave COMPLETE_BODY for each of the following; the hashes here are the parent's frozen source pins, not independent original-source hash observations:

- S1 LF 1–5: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1-erratum-1.md`, SHA `513b44b2591954b535e138df611fab0698af2b8363b89768a5e45f320d50f5d4`.
- S2 LF 1–182: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f734-actual-septic-global-root-or-eligible-zero-dual-frontier-author/author-candidate-v1.md`, SHA `fd95da21d7ae3517475dae09516591688479c6bbddbfa593b452d5d48827b575`. This is the complete unadopted source, not a sibling source followed separately.
- S3 LF 1–29: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1.md`, SHA `949af8c879058b8be166086ab06dbba03d896a26adc64e1621dfbdf7a72e4d0b`.
- S4 LF 1–40: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-2-actual-septic-two-coordinate-buffer-strictification-and-universal-equivalence-parent-v1.md`, SHA `8fcf488e37f1415c98b48cccdcab391e6a2fa409f8c43561f73df4cd8e41f63d`.
- S5 LF 1–46: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-2-actual-box-three-root-dual-odd-cone-and-six-node-sparsification-parent-v1.md`, SHA `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae`.

**NOT TESTED / not performed:** No scientific child execution, source preparation, solver, numerical experiment, build, test, lint, formatter, public-source fetch, external-model CLI, dependency install, Git, deletion, paid/heavy action or live-infrastructure action. No new finite source or GO is proposed in this written reconstruction. Administrative hashing and one exclusive creation of this return are not scientific execution. Parent full-read/disposition and any later independent checks remain separate; parent-reported prior finite evidence in S3/S4 was not rerun or adopted as new evidence here. No correction to S2 is asserted: the present written argument addresses its Theorem A only, and identifies its dependencies rather than claiming the entire S2 body was proved.
