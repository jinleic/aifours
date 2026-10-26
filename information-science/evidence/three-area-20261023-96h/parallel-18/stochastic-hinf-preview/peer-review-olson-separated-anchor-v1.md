# v55-B — separated-anchor coefficient machinery and its literal obstruction word

Reviewer **InfoHinfPreview-2**, retaining info-3. Author **MathOlson-2**. Actual ACK clock: **Sun Oct 25 08:13:56 PDT 2026**. Actual post-reconstruction clock before this return: **Sun Oct 25 08:18:26 PDT 2026**, both returned `/bin/date` outputs.

## 1. Exact verdict; no selector or residual-closure promotion

**0 FATAL / 0 MAJOR / 0 MINOR findings in the separated-anchor polynomial identities, necessary coupling consequence and explicit obstruction-word calculations at their stated scope.** All requested colour degrees, mixed-difference signs/factor, parity/half-status step, REF coordinate, actual identity14, matching recurrence and exact F7 extractions are reconstructed below.

This is NOT a proof of a selector for every R=p+2 word, of emptiness of the full (R2) residual, or of the literal example's membership/nonmembership in the old-caller-failing class. The averaged coupling is only a necessary FIELD identity under hypothetical avoidance, and the example itself has an actual mixed identity14. The old LOW-ODD-coverage assertion is withdrawn by the operative erratum, not reused. No new selection theorem, full ordered Olson result, executable certification or novelty claim follows.

This is same-harness cross-domain supplied-proof WRITTEN reconstruction, not blind/configured-family/cross-vendor/human/formal/global-union or parent acceptance.

## 2. Pins, complete coverage, exposure and serial order

The complete35-line parentv9 was read FIRST; the exact v55-B entry including its raw full scope line90, and the complete26-line byte-equality receipt were read before author body. The pre-body ACK is `peer-review-olson-separated-anchor-ack-v1.json`.

Fresh metadata SHA-256 observations:

|Record|SHA-256|
|---|---|
|v55 manifest|`57933f7f691423a04fed91fdc6ec171a8738e9bd5f4d6dd753bc5189c8c6cf9d`|
|v55 receipt|`19eec3b8524de450d845f5b26fe0489ccf48cd18dbe93c3223f5a0c8caadd4a5`|
|only literal part `peer-review-wave-v55-v55-B-part1-v1.md`|`45307fb8ef081b2934db260e34c1dfc9341f25c2e93d63fa583bbefb1b59cab0`|
|S1 parentv9|`b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`|
|S2 primary265LF|`25b3a23ee2f0a46fe5c30ce53454286e0883add327bf239b74756ad125c796b4`|
|S3 current-parent29LF|`fb9d8f534d2c626d1a55af9c94774054fb048d4a0c3d4735ca88aae489cd7234`|
|operative11LF scope erratum|`aa7895f0376075b541d2b71a6c738b791453648540bc449baae6bb861169fd1f`|

The complete347-line literal part was read in ranges covering1–193 and194–347, including every S1 LF1–35, S2 LF1–265 and S3 LF1–29. No reported cut source line was treated as read. The separately named `separated-anchor-scope-erratum-v1.json` was also read completely and its hash matched. Citations below use original S2 LF numbers unless identified otherwise.

Prior exposure: I previously reconstructed the different R=p+1 double-box argument in v31-A and had seen round summaries of L_MAX/L_RES. Current separated-anchor body and word computations were unread before the ACK; target field values were exposed in the manifest. This is not blind review. The prior exact-boundary box verdict is not inherited for the present M+1 case.

All earlier actual reviews were returned. v56-B arrived while v55-B was active; Main confirmed that this review must be fully returned before a distinct v56-B pre-body ACK. No v56 body was read in parallel and no assignment was dropped.

**No scientific eval/interpreter/program, arithmetic or symbolic program, enumeration, sampling, replay, solver, CLI, nested agent or author/shared write was used.** All arithmetic below is written field/polynomial algebra. Only metadata clocks/hashes and source reads accompany it. Parentv1–v9/HOLD, original cutoff/deadline and the zero-credit status of unadmitted computations remain binding.

## 3. Actual colour polynomial and the M+1 boundary — LF36–87

Fix p>=7 prime, R=p+2, F=3p-3 and N4p-1. Occupied cyclic reflection gaps are singleton. Choose an ACTUAL rotation r0 in gap1 and cut immediately before that gap. Then u1=u_(F+1)=0, with the M=F-1=3p-4 remaining Boolean colour variables. M is ODD.

The reflection selector is the actual colour-change indicator

$$u_t+u_{t+1}-2u_tu_{t+1}.$$

Its sum S(u) is the exact INTEGER selected-reflection count, always even. Prefix parity before gap t is u_t. Thus, for an actual rotation subset K, the actual product is a rotation with coordinate `C(1_K)+L(1_K;u)` and its size is `k(1_K)+S(u)`, where

$$C(z)=\sum_r z_rx_r,\quad k(z)=\sum_rz_r,$$

$$L(z;u)=\sum_{t=2}^F(y_{t-1}-y_t)u_t
                 -2\sum_r z_rx_ru_{g(r)},$$

$$Z_2(u)=-2\sum_{t=2}^{F-1}u_tu_{t+1}.$$

The reflection coordinate follows by summing `(u_(t+1)-u_t)y_t`; selected rotations contribute `(1-2u_(g(r)))x_r`. No actual rotation is commuted across a selected reflection.

Let n=p-1. The colour indicator product

$$(1-(C+L)^n)(1-(k+S)^n)$$

has degree at most `n+2n=3p-3=M+1`, NOT at most M. Full-support monomials of degree M+1 can have one colour squared and still have a nonzero signed Boolean sum. Therefore one cannot initially replace the entire signed colour sum by its ordinary squarefree degree-M coefficient.

For an ordinary colour monomial missing a colour, pairing the two values of that colour cancels its signed sum. This cancellation is valid over `F_p[z]`, so formal rotation statuses may be retained. It proves exactly the omissions used in the source:

|discarded kind|maximum colour degree|reason below M|
|---|---|---|
|isolated1|0|strictly below M|
|isolated `(C+L)^n`|p-1|strictly below M|
|isolated `(k+S)^n`|2p-2|strictly below M for p>=7|
|at least one k factor in the product|`(p-1)+2(p-2)=3p-5`|M-1|
|at least two C factors in the product|`(p-3)+2(p-1)=3p-5`|M-1|

The zero-C product can retain degrees M and M+1. Exactly one C factor can attain degree M and MUST remain. Thus the exact polynomial identity is

$$H(z)=\sum_u(-1)^{|u|}\left(L(z;u)^{p-1}S(u)^{p-1}
 +(p-1)C(z)L(z;u)^{p-2}S(u)^{p-1}\right).                \tag{1}$$

Its total ordinary STATUS degree is at most p-1, for all formal statuses. No Boolean reduction in statuses or avoidance hypothesis was used to obtain(1).

For actual EVEN K, selected size is even and lies in `[0,4p-1]`. Its only positive even multiple of p is2p. Fermat's indicator then gives, under hypothetical absence of EVERY actual identity2p,

$$H(1_K)=0\quad(K\ne\varnothing\text{ even}),\qquad H(0)=1.$$

Only u0 gives genuinely empty selection because the colour-change recurrence starts and ends at0. Odd K can yield sizes p or3p and their H-values are NOT set to zero. This parity qualification is essential.

## 4. Full mixed-difference derivation, both signs and multiaffinity — LF89–120

Take a second actual anchor r1 in distinct gap s, with x0,x1 nonzero. There are exactly p other rotation statuses. Gap1 is singleton, so its initial anchor changes C but no term of L because u1=0. In(1), differencing first in z0 therefore leaves exactly

$$(p-1)x_0\sum_u(-1)^{|u|}L(z_1;u)^{p-2}S(u)^{p-1}.$$

Now `L(1;u)=L_A-2x1 u_s`. The mixed Boolean difference in the order `H11-H10-H01+H00` is thus

$$(p-1)x_0\sum_u(-1)^{|u|}
 [(L_A-2x_1u_s)^{p-2}-L_A^{p-2}]S(u)^{p-1}.              \tag{2}$$

This checks both subtraction signs; there is no remaining C or k dependence from the anchors in(2).

Every term in (2) has colour degree at most `(p-2)+2(p-1)=M`. NOW the exact degree-boundary signed-box rule applies. Its factor is `(-1)^M=-1`; the outside factor `p-1=-1` in F_p cancels that sign. To attain degree M, every S factor must supply its quadratic part Z2. A linear S part loses one degree with no possible compensation.

In the binomial difference, two or more explicit u_s factors cannot contribute to the ordinary full-squarefree coefficient. The sole possible term is

$$(p-2)(-2x_1)u_s L_A^{p-3}=4x_1u_s L_A^{p-3}$$

in F_p. Any further u_s in L_A or Z2 is likewise excluded; this is ordinary coefficient extraction BEFORE Boolean reduction, so a square u_s cannot be treated as u_s. Therefore

$$\boxed{D_s(A)=4x_0x_1\left[\prod_{2\le t\le F,t\ne s}u_t\right]
 (L_A|_{u_s=0})^{p-3}(Z_2|_{u_s=0})^{p-1}.}              \tag{3}$$

The remaining colour-degree is exactly `p-3+2(p-1)=M-1`, the size of the extracted variable set. D has outside-status degree at most p-3.

Each outside rotation status occurs only with its OWN gap variable. Singleton gaps make those gap variables distinct and separate from1,s. A squared status would force its own colour squared, incompatible with(3). Hence D is an ORDINARY multiaffine polynomial, not merely a multiaffine representative of its Boolean values. Repeated/equal rotation VALUES do not break this argument; occurrence/gap distinctness, not distinct values, is what matters.

Thus the mixed term can genuinely survive. Its low outside degree does not make the two anchor variables jointly affine.

## 5. Parity and the half-status coupling are FIELD identities — LF122–150

Let `G(A)=H00(A)+H11(A)`, a polynomial of total status degree<=p-1 in p outside variables. Under hypothetical avoidance:

- If |A| is even, H00 is1 only at the empty A, and otherwise0; H11 always represents a nonempty even subset and is0.
- If |A| is odd, H10 and H01 represent nonempty even subsets and vanish. Consequently `G(A)=D_s(A)`.

Every monomial of G misses an outside variable, so its signed outer-box sum is0. The exact parity split gives

$$0=1-\sum_{A\text{ odd}}D_s(1_A),\qquad
\sum_{A\text{ odd}}D_s(1_A)=1.                            \tag{4}$$

D also has degree<p, so its signed sum is0. Its even and odd sums therefore both equal1, and its total sum is2 in F_p.

For an ordinary multiaffine monomial of status degree j, its sum over all p-variable Boolean points is `2^(p-j)`, while its value at the all-half point is `2^-j`. Thus by linearity

$$\sum_A D_s(1_A)=2^pD_s(1/2,\ldots,1/2).$$

Because p is odd,2 is invertible; Fermat gives `2^(p-1)=1` IN F_p, hence `2^p=2`. Combining with the total sum2 and dividing by2 yields

$$\boxed{D_s(1/2,\ldots,1/2)=1.}                          \tag{5}$$

This is a field-polynomial consequence, not an integer equality `2^(p-1)=1`, a real probabilistic average or an actual half-selected rotation witness. In (3), the all-half point simply changes each outside occupied-gap coefficient from beta_t to `beta_t-x_r`.

For a genuinely avoiding word, (5) is necessary for EVERY ordered actual anchor/cut choice, with the actual colour coordinates for that cut. No simultaneous realizability or rank classification of all those different-cut equations has been proved. In particular one equation alone is not avoidance.

## 6. Literal p7 word, all gaps and REF product coordinates — LF152–178

Take

$$w=(\rho_3\sigma_0)^9\sigma_0^2
          \sigma_1\sigma_2\sigma_3\sigma_4\sigma_5\sigma_6\sigma_0.$$

There are9 rotations and18 reflections, total27=4p-1. Every rotation value3 is nonzero in F7. The occupied actual cyclic gaps are1 through9, each with one rotation. The end gap contains the first rho3; it is not an adjacent-rotation resource. All other gaps are empty.

For REF-only calculations the omitted rotations are simply omitted, not commuted. The cyclic reflection SUBSEQUENCE can be cut as `sigma0^12 sigma1...sigma6`. A14-reflection selection must use a nonzero label because only12 zero reflections exist. Let its chosen nonzero labels be `b1<...<bt` in1,...,6; the number of selected preceding zeros is `14-t`, of parity t. Thus its alternating coordinate is `-L`, with

$$L=(b_2-b_1)+(b_4-b_3)+\cdots\quad(t\text{ even}),$$

$$L=b_1+(b_3-b_2)+(b_5-b_4)+\cdots\quad(t\text{ odd}).$$

These are positive disjoint interval lengths in `[0,6]`, so `1<=L<=6`; the coordinate is nonzero in F7. This handles all possible selected label subsets and zero counts; no14-reflection identity exists. Conjugating a cyclic cut preserves identity/nonidentity of the same selected occurrences, so the conclusion applies to the displayed original word.

Nevertheless select the FIRST TWO actual rho3 occurrences and ALL12 actual sigma0 occurrences. Their original-order product is

$$\rho_3\sigma_0\rho_3\sigma_0^{11}.$$

Using `(v,e)(v',e')=(v+ev',ee')`, the first three factors multiply to sigma0; sigma0 to the11th power is sigma0, so their product is1. The count is exactly14. This is an actual original-position mixed identity, not a formal polynomial selector. Hence w is NOT an Olson counterexample, regardless of its unresolved old-caller class membership.

## 7. Exact colour path and matching extraction — LF180–245

In the actual displayed cut, f1 through f11 are0; f12 through f17 have labels1 through6; f18 is0. Thus beta_t0 for2<=t<=11 and beta_t=-1 for12<=t<=18 (the last difference6 is-1 in F7).

Choose anchors in gaps1,2, both value3. The outside statuses are z3,...,z9 and

$$L_A=-\sum_{t=12}^{18}u_t-6\sum_{i=3}^{9}z_i u_i,
\qquad4x_0x_1=36=1\text{ in F7}.$$

Removing u2 leaves the16-vertex path u3,...,u18. Its monomer weights are seven equal a, two zeros, then seven equal-1. At all outside statuses1, a=-6=1; at all half statuses, a=-3=4 in F7.

For a constant-weight path, distinguish its last vertex as a monomer or the endpoint of its last dimer:

$$K_0=1,\quad K_1=a,\quad K_n=aK_{n-1}+tK_{n-2}.$$

Iterating the recurrence gives

$$K_6=a^6+5a^4t+6a^2t^2+t^3,$$

$$K_7=a^7+6a^5t+10a^3t^2+4at^3.$$

For example the successive coefficients count `binom(n-j,j)` placements of j disjoint adjacent dimers; equivalently K2 through K5 are `a²+t`, `a³+2at`, `a⁴+3a²t+t²`, `a⁵+4a³t+3at²`, from the same formal recurrence. No matching search is performed.

The two zero-weight middle vertices cannot be monomers. Either their internal dimer is chosen, leaving two seven-paths; or BOTH boundary dimers are chosen, leaving two six-paths. Exactly one boundary dimer leaves the other zero vertex uncovered and is impossible. Therefore the complete matching polynomial is

$$tK_7(a,t)K_7(-1,t)+t^2K_6(a,t)K_6(-1,t).$$

In (3) with p7, L-to-the4 and Z2-to-the6 must provide four distinct monomers and six disjoint dimers. Their coefficient-permutation factor is exactly

$$4!6!(-2)^6=3\cdot6\cdot1=4\quad\text{in F7}.$$

Repeated edges/overlapping dimers would repeat a colour and cannot appear in the extracted full-squarefree coefficient. With anchor factor1, the mixed term is therefore

$$D(a)=4\big([t^5]K_7(a,t)K_7(-1,t)
                +[t^4]K_6(a,t)K_6(-1,t)\big).             \tag{6}$$

### All-statuses1 value

At a1, the two coefficients in (6) are, as ordinary integer expressions,

$$10(-4)+4(-10)=-80,\qquad5+36+5=46.$$

Their sum-34 is1 in F7, giving

$$\boxed{D_s(1,1,1,1,1,1,1)=4\ne0.}                       \tag{7}$$

Thus the separated anchors are not jointly affine even on this zero-free singleton word with no REF-only identity14. This is an ambient algebraic obstruction, not a residual-avoidance theorem.

### All-half value

Using `4²=2,4³=1` in F7, the recurrence polynomials reduce exactly to

$$K_7(4,t)=4+5t+3t^2+2t^3,\quad K_6(4,t)=1+6t+5t^2+t^3,$$

$$K_7(-1,t)=6+t+4t^2+3t^3,\quad K_6(-1,t)=1+5t+6t^2+t^3.$$

The required coefficients are

$$[t^5]=3\cdot3+2\cdot4=17,$$

$$[t^4]=6+5\cdot6+5=41.$$

Their sum58 is2 in F7. Equation(6) gives

$$\boxed{D_s(1/2,\ldots,1/2)=4\cdot2=1\text{ in F7}.}     \tag{8}$$

Every coefficient/factor here has been derived from the actual path and recurrence. No executable arithmetic or sampled Boolean census is used.

Thus one necessary averaged coupling equation is already satisfied by an actual SOLVED word. It cannot alone imply avoidance or a contradiction. This does not show that every other anchor/cut equation also holds for w, and does not rule out a future argument retaining the full old residual failures.

## 8. Operative block-count erratum and prior-call trust boundary

The ACTUAL word has eight initial singleton zero-reflection blocks, then one length-three zero block, six nonzero singleton blocks, and a final singleton zero block. Every one is odd. The cyclic end gap contains rho3, so the final zero cannot fuse with the initial zero. Hence the actual odd-block count is

$$8+1+6+1=16.$$

By contrast, deleting the rotations before counting reflection-subsequence runs would merge the12 zeros into one even run, leaving only six odd nonzero runs. That is the withdrawn p-1 count and is NOT the actual block statistic. The separately read operative scope erratum correctly preserves the old frozen scope and withdraws its LOW-ODD-coverage claim additively.

No LOW-ODD coverage, full OLD-residual membership or nonmembership is established. The explicit selector does not by itself prove that one of the particular old callers would recognize this word; conversely REF failure is only one old failure and does not prove the entire C_p complement.

The current parent29-line input retains standalone OG/TA and identity-relocation callers at their exact written/import scopes. Its derived zero-free singleton residual is a legitimate starting class, but TA's same-gap joint affinity cannot be transferred to separated gaps by discarding (3). Old HIGH/GEN and other caller/certificate trust boundaries are not upgraded here. The whole R=p+1 theorem remains a separate predecessor, not a proof of R=p+2.

## 9. Exact NOT_RECONSTRUCTED/open obligations and recommendation

All NEW requested polynomial/coefficient/word identities in this packet are reconstructed above. The following remain explicitly outside the result:

1. **OPEN:** the full (R2) obligation to select exactly2p actual original positions for EVERY actual residual word, or prove that class empty. Neither (5) nor the example supplies that theorem.
2. **NOT_RECONSTRUCTED:** the example's membership/nonmembership in the ENTIRE old-caller-failing C_p or (R2) class, or coverage by any specific old LOW-ODD/OLD/TILE/GEN caller. No claim is inferred from the mistaken subsequence statistic.
3. **NOT_PROVED:** simultaneous sufficiency, realizability, rank classification or inconsistency of all anchor/cut coupling equations together with every original caller failure. Only necessary equations under avoidance have been derived; one solved example satisfies the displayed equation.
4. **Retained named imports, not newly re-proved:** full OG/TA and identity-relocation provider/caller proofs and all older certificate chains/other bands. The current parent boundary is read and preserved, not a substitute for their entire historical union audit.
5. **NOT_PERFORMED:** scientific execution/replay, configured-model-family/human/formal/kernel/global-union acceptance, novelty or parent disposition. No new scientific permission follows.

**Recommendation:** retain the separated-anchor residual machinery and literal obstruction as a completed no-defect WRITTEN reconstruction at the stated scope. Keep the mixed term, exact field-only half-status coupling, actual16-block correction and explicit identity14 inseparable from any headline. Do not promote this to R=p+2 closure, a new selection theorem or a residual counterexample. Return this v55-B before beginning the separately queued v56-B body.
