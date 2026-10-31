# f8 — independent written and exact-arithmetic review of the PH7 three-chain obstruction

Reviewer **PhysicsRQLS10-2**, physics-5. Native `/bin/date` before writing: **Wed Oct 28 17:17:46 PDT 2026**. **Verdict: FATAL0 / MAJOR0 / MINOR0 — NO SUBSTANTIVE DEFECT AT EXACT CANDIDATE SCOPE.** The all-u critical obstruction, singular boundary and non-effective uniform z-neighborhood are proved for the EXACT stated 3+3-chain/one-center/positive-diagonal-normalization family. They do not imply an all-topology PH7 exclusion, an exact global PH order, source novelty or that every possible PH7 realization can be brought into this form.

The coefficient identities and every printed Bernstein/tail coefficient were checked **independently** with newly written rational-polynomial code, including an independent symbolic determinant and cofactors of the actual 7×7 matrix. The compactness/continuity and physical-necessity arguments were reconstructed in writing below. This is same-harness review and exact computer arithmetic, **not** Lean/formal, human, independent-model-family, or prior-source adoption.

## 1. Actual inputs, coverage, exposure and pins

- Frozen assignment `review-waves/f8-ph7-three-chain/assignment-v1.json` read ENTIRELY FIRST, before the candidate. Its priority directs this one review, then return to my original physics-5 research.
- Candidate `mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-ph7-three-chain-critical-obstruction.md`, SHA256 **d231c72575c414d0891269e536100c05388896cfd8ce8a4325b50de07a37e817**, **145 LF**; ALL read RAW1–60,61–120,121–145 through ending. Live hash matched.
- Registered target `institute/runs/three-area-2026-10-27-96h/written-releases/math-1-ph-order-definitions-v1.md`, SHA256 **a4db7478cf384fabdddccede032efe2cd1f33d12ad3e771788e58d5596682e85**, **17 LF**; read completely and pin matched.
- The explicitly cited raw-family dependency `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-u-deformation-actual-family-v1.md`, SHA256 **9f9b048bd4113b5008bdebf56f1e5d903e06e0b6ffe1f8eed78dbcd7ebb1a01e**, **201 LF**, read completely through ending. The prior rational-band source `.../phase-type/PH7-rational-uniform-band-seven-ninths-v1.md`, SHA256 **ef6df980b2fbb5545a42ed7f3c72f17cea6f26f7148065670c104838f9a0c0f7**, **364 LF**, read completely through ending. Only their printed common matrix/family identification is used; its identities are independently reconstructed below. Their older interval, endpoint, minimum-order and external-review claims are NOT newly verified or required for the present obstruction.
- Prior math-1 contact includes my B1 documentary comparison/registration audit and earlier PH review exposure. The B1/registration episode was subsequently held and its outputs/consumers are NOT proof premises. Prior historical familiarity is disclosed; this is not a blind, clean-cognition or external-family review. No author contact, outside paper, old mixed/withdrawn packet or author's checker/result was used. The current owner direction allows scientific checks but does not retroactively validate held outcomes.

**Independent exact checker:** `physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-review-f8-exact-check-v1.py`, SHA256 **5ae7a6ae0864dc439827e7ab6de2825f21fcfaafd006dd3530638ecf6157b6a0**. It uses a newly written multivariate polynomial ring over Python `fractions.Fraction`, recursive determinant/cofactor expansion, formal coefficient extraction and exact binomial Bernstein conversion; it imports NO author source script or certificate. Executed `python3 frontier-review-f8-exact-check-v1.py`; actual output at17:17:03:

```text
PASS symbolic 7x7 determinant and beta-adjugate numerator
PASS symbolic degrees 7,6,5 vanish; degree4 is +/- (L p - N), sign +
PASS critical qL/P identities, singular remainder, z-independent leading coefficients
PASS all 7 full rational Bernstein vectors and both shifted tails
PASS: all listed Bernstein/tail coefficients strictly positive
```

The checker is exact coefficient arithmetic, not an executable search over PH models or a substitute for the written proof of the analytic uniform-neighborhood step. No author-supplied grid/Sturm/checker output is counted as my independent evidence.

## 2. Exact registered target, normalization and family boundary

The registered transform is

`H(s)=c_orig(a_orig^2+b_orig^2)^2 / [(s+c_orig)((s+a_orig)^2+b_orig^2)^2]`,

with `a_orig>c_orig>0`, `b_orig>0`, `d=a_orig-c_orig>0`, `z=(b_orig/d)^2`. For normalized Laplace variable `s'=s/d` and `c=c_orig/d`, put `y=s'+c` and `D_z(y)=y[(y+1)^2+z]^2`, `K=D_z(c)>0`. Direct substitution gives `H(s)=K/D_z(s/d+c)`; the numerator and denominator each acquire the SAME factor d^(-5). Thus the stated z=8/9 comparison is with the registered target for every allowed scale, not a different transform. The source's local coefficient names a,b below are not the registered pole parameters.

The ACTUAL raw family uses a 7×7 G with upstream chain `J_u`, center -w, downstream chain `J_1`, links and feedback exactly as candidate LF24–33:

```text
J_u = [-u  1  0; 0 -u  1; 0  0 -u]
G   = [ J_u   e3      0
        0      -w    e1^T
        D       f     J_1 ]
D=[(D1,0,0);(D2,0,0);(D3,0,0)], f=(0,0,phi)^T
beta=(C,B,1,0,0,0,0), gamma=K e7.
```

The physical family further requires a POSITIVE diagonal h with `(G-cI)h=-gamma`, `T=diag(h)^(-1)(G-cI)diag(h)`, `alpha=beta diag(h)` and the remaining PH conditions. If such a realization exists, `alpha>=0` and h>0 require **B,C>=0**. The actual off-diagonal entry `T_(7,4)=phi*h4/h7` must be nonnegative for Metzler T, so **phi>=0**. These are NECESSARY conditions for the SAME physical object; positive h does not allow a sign change. Their contradiction suffices without assuming `D1,D2,D3>=0`, stability, q-Hurwitz, or normalizer existence. The theorem includes B=0/C=0 and all c>0; it does not classify representations with another graph, input/exit support, rate pattern or arbitrary non-diagonal similarity.

## 3. Reconstructed same-matrix determinant, numerator and coefficient matching

Let `M(y)=yI-G`, and write `U=y+u`, `V=y+1`. Direct block elimination, equivalently the independent 7×7 polynomial determinant, gives

`det M = (y+w) U^3 V^3 - phi U^3 - D1 V^2 - D2 V - D3`.                  (3.1)

The beta-adjugate numerator for the SAME matrix is

`beta adj(M) gamma = K[(y+u)^2+B(y+u)+C] = K Q(y)`.                 (3.2)

For an explicit path derivation, solve `M x=e7`: upstream equations give `x1=x4/U^3`, `x2=x4/U^2`, `x3=x4/U`; the center gives `x5=(y+w)x4`. The downstream equations yield `det(M)*x4/U^3=1`, as an identity of rational functions. Therefore `beta x=Q(y)/det(M)`. Clearing denominators yields (3.2) as a POLYNOMIAL identity, so no nonzero-denominator or noncoincident-root assumption is hidden. The independent checker obtains (3.1) by full determinant expansion and (3.2) by three actual cofactors, not by trusting this hand elimination.

If this family realizes `K/D_z(y)`, equality of the two rational transfers gives the NECESSARY polynomial identity

`det(M)=D_z(y) Q(y)`.

No cancellation is assumed to be impossible: cross-multiplication is an identity in the polynomial ring, K>0, and the numerator in (3.2) is the same Q from actual B,C,u. With

`Q=(y+u)^2+B(y+u)+C=y^2+p y+q`,

we have `p=2u+B`, `q=u^2+uB+C` and, for u>0 and B,C>=0, **q>0**, including B=C=0.

Expand the six-rate product `(y+u)^3(y+1)^3` with coefficients

`a=3u+3`, `b=3u^2+9u+3`, `c3=u^3+9u^2+9u+1`, `e4=3u^3+9u^2+3u`.

Degree7 cancels by monicity. Degree6 forces `w=p+4-a`. Degree5 forces `q=(a-4)p+h0-2z`, where `h0=b+4a-a^2-6`. Degree4 forces `L p=N`, where

`L=b-4a+10-2z`, `N=4h0+4-c3-b(4-a)-4z`.

Degree3 forces

`phi=e4+c3*w-[(6+2z)q+(4+4z)p+(1+z)^2]`.

All signs and the degree4 direction are independently confirmed by exact symbolic coefficient extraction; the computed degree4 coefficient is **+(Lp-N)**. Lower coefficients constrain the ACTUAL D1,D2,D3 but are unnecessary for the obstruction. Thus the displayed equations are necessary for EVERY target-matching realization in this family, not just a chosen numerical grid or a guessed decoupled characteristic factor.

## 4. Critical identities: exact all-u proof including L=0

At z0=8/9, substitution and clearing L yield the polynomial identities

`L=3u^2-3u-7/9`, `N=8u^3-9u^2+3u-32/9`,

`qL=Q_*(u)=6u^4-8u^3+(25/3)u^2-(32/3)u+400/81`,

`-243 L phi=P_*(u)=243u^6-729u^5+2025u^4-5859u^3+9360u^2-7776u+3184`.

These identities follow without dividing by L: express `qL=(a-4)N+(h0-2z)L` and replace `wL` by `N+(4-a)L`, then clear the actual phi expression. They are formal equations for any coefficient-matched p,q,w; the independent checker verifies equality coefficient by coefficient.

For **L!=0**, any physical B,C>=0 gives q=u²+uB+C>0 for every u>0. The first identity and Q_*(u)>0 imply L>0. The second and P_*(u)>0 then give `phi=-P_*/(243L)<0`, contradicting phi>=0. All strict signs and the factor243 are retained; no separate q-Hurwitz or D_j sign is used.

For **L=0**, degree4 matching still demands N=0 even though p cannot be written as N/L. Exact polynomial division gives

`N=((8u-1)/3)L+(110u-103)/27`.

Simultaneous L=N=0 forces u=103/110 in (0,1), but `L=3u(u-1)-7/9<0` there. Hence no such finite p/coefficient-matched family point exists. This includes the singular branch rather than dropping it by division. Equivalently, positivity of the cleared Q_* already rules out L=N=0; the candidate's separate remainder proof is correct and gives the requested explicit boundary.

## 5. Full positive-sign certificate, not a sampled grid

For a polynomial of degree m, the Bernstein representation on `[a,b]` is

`P(a+(b-a)t)=sum_(j=0)^m B_j binom(m,j)t^j(1-t)^(m-j)`, `0<=t<=1`.

Every basis function is nonnegative and their sum is1, so **all B_j>0** implies strict positivity on the closed interval, including endpoints. For exact power coefficients p_i, the independent checker substitutes `u=a+(b-a)t` and converts via `B_j=sum_(k<=j) t_k binom(j,k)/binom(m,k)`. It checked EVERY coefficient printed in candidate LF80–105, not just the minimum. The smallest printed/checked coefficient on each interval is:

| Polynomial | Closed interval | Exact minimum of its Bernstein list |
|---|---|---|
| P_* | [0,1/2] | 64717/64 |
| P_* | [1/2,1] | 448 |
| P_* | [1,3/2] | 14731/64 |
| P_* | [3/2,2] | 18529/64 |
| Q_* | [0,1/2] | 689/648 |
| Q_* | [1/2,3/4] | 1547/10368 |
| Q_* | [3/4,1] | 137/2592 |

For u=2+t, t>=0, the checker verified exactly

`P_*(2+t)=2824+12492t+22806t²+20061t³+9315t⁴+2187t⁵+243t⁶`.

For u=1+t, t>=0, it verified exactly

`Q_*(1+t)=49/81+6t+(61/3)t²+16t³+6t⁴`.

All listed coefficients are strictly positive. The intervals and rays cover ALL u>=0 with overlaps at the boundaries. Thus both polynomials are strictly positive everywhere on that ray. This proof has no root oracle, finite-grid inference, floating-point comparison, selected u, missing endpoint or assumption of monotonicity. The original physical theorem restricts to u>0; the sign certificate covers u=0 as well, but the inference q>0 from B,C>=0 would require separate care at u=0, so no physical-u=0 theorem is asserted.

## 6. Uniform z-neighborhood and singular root: complete written reconstruction

Define polynomial continuations without division:

`Q_z=(a-4)N+(h0-2z)L`,

`P_z=-243{e4 L+c3[N+(4-a)L]-[(6+2z)Q_z+(4+4z)N+(1+z)^2 L]}`.

At any coefficient-matched point these are `Lq` and `-243 Lphi`. The exact checker verifies their u-leading coefficients are respectively6 at degree4 and243 at degree6 **independent of z**. They are joint polynomials in real z,u, including L=0.

For t=u/(1+u), form `(1-t)^4 Q_z(t/(1-t))` and `(1-t)^6 P_z(t/(1-t))`. By polynomial expansion these extend continuously at t=1 with values6 and243. At z0, §5 proves strict positivity for t<1; the leading coefficients prove it at t=1. Each continuous function therefore has a strictly positive minimum on the compact interval [0,1]. Uniform continuity on a compact rectangle around z0 supplies epsilon>0 such that BOTH compactified polynomials stay strictly positive for EVERY t∈[0,1] and every |z-z0|<epsilon. This is a genuine uniform all-u statement; its width is not evaluated, and no relation to any earlier endpoint is asserted.

For the matching singular case, `L(u,z)=3u²-3u+1-2z`. On a sufficiently small neighborhood of z0, its constant term is negative, so its two real roots have opposite sign and the positive root u_+(z) is unique. The quadratic formula gives its continuous dependence. At z0, L(1)<0 and L tends to +infinity as u grows, so u_+(z0)>1. By the exact remainder in §4, `N(u_+(z0),z0)=(110u_+-103)/27>0`. Continuity therefore keeps N nonzero at that positive root on some possibly smaller neighborhood. Taking the intersection with the uniform-sign neighborhood excludes L=N=0 for all u>0 there. (The cleared-Q positivity also excludes a matching singular point directly.)

For L!=0 the same q>0 -> L>0 -> phi<0 contradiction applies on this COMMON neighborhood; for L=0 no coefficient match exists. Thus there exists SOME open z-neighborhood of8/9 obstructed in precisely the specified family for ALL u>0, c>0. Shrink it if needed to maintain z>0. No numerical interval endpoint, global PH7 sign, prior feasible-band comparison or original all-topology exclusion is proved.

## 7. Claim-by-claim findings, historical imports and nonclaims

- **Candidate LF15–46:** normalized target, raw chain and actual input/feedback necessary signs are correctly specified at the source's stated literal-family scope. `h>0` is an antecedent to the excluded physical realization, not an assumed existence conclusion; it is needed only to translate the signs of alpha and T.
- **LF48–78:** all-u obstruction, q positivity, two identities and L=0 boundary reconstructed as in §§3–4. No unpriced hidden-Hurwitz assumption appears. Coefficient-matching necessity is for the same raw beta/G/gamma and target transfer, not independent choices of p,q,phi.
- **LF80–110:** all seven full exact Bernstein lists and both tails were independently checked; §5 proves why their positivity covers the whole half-line. The author's grid/Sturm outputs are NOT used as proof inputs or represented as my execution.
- **LF112–132:** joint-polynomial compactification and positive-root continuity pay the noneffective open-neighborhood claim; no numerical endpoint is asserted. L=0, endpoint t=1, B/C zeros, arbitrary u>0 and arbitrary c>0 are explicitly included.
- **LF7–13,136–145:** references to previously written-supported PH6 and earlier PH7 bands are HISTORICAL CONTEXT and are **NOT_RECONSTRUCTED as independent claims in this review**. Their truth is not needed to prove the family obstruction. Likewise no current literature/novelty/source-priority or original all-topology result is certified. Reading the two source bodies for the family does not newly adopt every prior construction/interval claim or an older review.
- **No claim that this graph exhausts PH7 models:** change of rates, topology, feedback, input/exit or another admissible realization remains outside the theorem. No extrapolation from a local chart to universal PH7 impossibility, minimum8, the general printed book question, or a full minimum-order function is licensed.

Named imports: elementary rational polynomial algebra and determinant/cofactor identities, positive-diagonal similarity sign preservation, exact Bernstein basis identity, finite-dimensional compactness/uniform continuity and elementary real-root continuity. The explicitly executed Fraction checker validates the formal identities and rational coefficients; the written compactness reasoning is not a machine-checked formal proof. Novelty, book-source authentication, old PH6/PH7 parent claims, formal/kernel/human/configured-family and global order are separate gates.

## 8. Return and continuation boundary

No external model/API, secret, source contact, publication, deletion or infrastructure mutation. Original personal RQLS historical episodes and earlier held artifacts remain historical/unvalidated, not imported premises; the prospective owner direction permits independent current work. The review does not decide those process records or sanitize past exposure. Full candidate/source reconstruction and independent exact check are delivered to Main; parent receipt is not adoption. I resume my primary physics-5 research after this return as assigned.

**Final verdict: FATAL0 / MAJOR0 / MINOR0 — NO SUBSTANTIVE DEFECT AT EXACT 3+3-CHAIN FAMILY SCOPE.**
