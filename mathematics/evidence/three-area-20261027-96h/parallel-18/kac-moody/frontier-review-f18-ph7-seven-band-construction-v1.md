# f18 PH7 review — explicit nonuniform band and equal-rate chart obstruction

Reviewer **MathKacMoody-2**, existing math-3; author **MathResearch96h-2**, existing math-1. Actual returned native `/bin/date` BEFORE this new review write: **Wed Oct 28 17:21:38 PDT 2026**. Precreation observation only.

## 0. Verdict and exact scientific scope

**Construction mathematics: SUPPORTED WITH ONE DOCUMENTARY MINOR at exact scope.** The complete same-matrix seven-state realization is valid for EVERY c,d>0 and EVERY real z=b²/d² in the CLOSED interval [7/9,813/1000], with a=c+d,b=d sqrt(z). Its upper conclusion is **PH order <=7**, not exact minimum without the separately named lower theorem. I independently reconstructed the actual PH rows, numerator, characteristic polynomial, all interval-positivity certificates, stability and dimensional scaling below.

**Equal-rate chart obstruction: NO SUBSTANTIVE MATHEMATICAL DEFECT at exact scope.** For EVERY real u>0,z>=389/500,c>0 the specified SAME `3+1+3` chain cannot have its nonnegative initial coefficient and its required nonnegative feedback simultaneously, including the singular L=0 case. This is a chart-specific impossibility, NOT an exclusion of all PH7 topologies or of z=8/9 itself.

**Counts:** zero FATAL, zero MAJOR, **one MINOR** as follows.

- **M1 — overbroad wording about strict entries, candidate 6a879654 LF140.** The phrase “Strict positivity of all G off-diagonal coefficients” is literally too broad: the displayed G at LF57–63 has many off-diagonal entries fixed at zero. The proved needed claim is that all NAMED variable feedback coefficients are strictly positive and all remaining off-diagonal entries are either1 or0. Thus G and its positive diagonal similarity are Metzler (nonnegative off-diagonal), not entrywise strictly positive off diagonal. This is a localized wording correction; every required PH row, conclusion and positivity proof remains valid. It does not require changing frozen source bytes.

No mathematical inference is made from the historical unsuccessful numerical searches. No independent human, model-family, formal/kernel, novelty/priority or source-wide authentication is conferred.

## 1. Actual coverage, prior familiarity and independent checking

Main's assignment `f18-ph7-seven-band-construction/assignment-v1.json` was read FIRST. I then read ALL178LF of the new upper candidate `6a879654414265014cfc8effb65c5d5b58341a57d5624b3da973b92915b283e7`, raw1–90/91–178, and ALL145LF of the obstruction candidate `27d92a17b438888e052c9d8d0b423d76b660c2cd7c87cad104306e47a69417ca`, raw1–75/76–145, including their endings. Live hashes matched.

I read the registered original PH definition, `math-1-ph-order-definitions-v1.md`,17LF, SHA256 `a4db7478cf384fabdddccede032efe2cd1f33d12ad3e771788e58d5596682e85`: arbitrary real Hurwitz Metzler T, T1<=0, alpha>=0, alpha1=1 and exact transform alpha(sI−T)^−1(−T1), with ALL topologies/cancellations included. This is the registered target cut, not a freshly authenticated book source.

To reconstruct the earlier equal-rate chart I read its complete201LF actual family `PH7-u-deformation-actual-family-v1.md`, SHA256 `9f9b048bd4113b5008bdebf56f1e8eed78dbcd7ebb1a01e`, raw1–135/136–201. I read the complete37LF `PH6-unrestricted-parent-disposition-v1.md` ONLY to identify the named earlier lower import; I did NOT re-review its195LF proof or historical reviewer. The later exact-order composition is therefore explicitly CONDITIONAL on B6, not a new independent verification of B6.

I previously reviewed phase-type and other same-harness work in the old round and have prior source familiarity. This is a serial same-harness review, not blind/cross-vendor evidence. Old held or quarantined outcomes are not adopted as premises merely by the owner direction; my exact checks below are newly written. No author checker/certificate, coauditor report, external model or author contact was used. The author’s local SymPy package supplies the SAME library version as their reported check, not an independent computer-algebra vendor.

### Newly executed independent symbolic check

I wrote `frontier-review-f18-ph7-independent-check.py`,180LF/7363B, SHA256 `0d1b35f603c45eb503436d1bdd5fa89f185af32d93adcdcec74051e1fc8f345d`, from the candidate definitions, without importing any author checker/certificate. The code loads the existing owner-local SymPy1.14.0 library read-only; no package was installed or modified. Actual command from my exclusive root:

    python3 frontier-review-f18-ph7-independent-check.py
    PASS: SymPy 1.14.0; full 7x7 determinant/numerator, 7 normalization rows, 10 Bernstein lists, equal-rate 8 intervals, tail and monotonicity identities
    frontier-review-f18-ph7-independent-check-v1.json

The process exited0; actual post-run clock **17:20:38 PDT**. The newly produced exact coefficient JSON is171LF/5462B, SHA256 `c39711613149475131daa7e02030322d684791885db062f58706fc99b2237958`. It independently constructs the two parameter systems; computes the ACTUAL full7×7 determinant and rank-one-update numerator; checks all seven normalizer equations and beta*h; computes every Bernstein coefficient and exact minimum in the ten new-band polynomials and eight obstruction intervals; and checks the equal-chart algebra, derivative, discriminant and shifted tail identities. It is exact symbolic/rational computation, not floating-point sampling. Code and certificate are review evidence, not a formal proof or an independent algebra library.

## 2. Nonuniform six-rate identities — same matrix, complete numerator

Use the exact six positive rational rates at candidate LF23–26 and their SAME elementary symmetric functions e_j. Define H0,L,N,p,q,w,B,C,phi,D1,D2,D3 exactly as LF28–53, not as independently selectable residues. The identity

    Q(y)=(y+u1)(y+u2)+B(y+u1)+C

follows by expanding its coefficients B=p−u1−u2 and C=q−u1u2−u1B. It holds for every z for which L is nonzero.

Let U(y)=product_j(y+u_j), V(y)=product_j(y+v_j). Direct block elimination from the one literal G at LF57–63 gives the polynomial identity

    det(yI−G)
       =(y+w)U(y)V(y)−phi U(y)
         −D1(y+v2)(y+v3)−D2(y+v3)−D3.                  (2.1)

The upstream and downstream ordered products are not interchanged. Substituting the actual definitions cancels every coefficient of(2.1) against D_z(y)Q(y), with D_z(y)=y[(y+1)^2+z]^2. My check also evaluates the actual symbolic7×7 determinant directly, so(2.1) is not being inferred from a partial coefficient match.

The first three entries of adj(yI−G)e7 are 1, y+u1, (y+u1)(y+u2). The beta combination is therefore exactly Q(y). Independently, the rank-one update

    det(yI−G+e7 beta)−det(yI−G)=beta adj(yI−G)e7

reproduces the FULL numerator Q, also checked directly. This polynomial identity does not require the matrix to be invertible at a root and remains valid if hidden and visible roots coincide. It uses ONE G,beta,e7, not separately optimized characteristic/numerator data.

## 3. Complete closed-band positivity, including both endpoints

For the actual closed interval I=[7/9,813/1000], the checker computes the full Bernstein coefficient list for L and for L times p,q,w,B,C,phi,D1,D2,D3. For a polynomial g of degree m, after y=a+(b−a)t the exact Bernstein coefficients are

    B_k = sum_(i=0..k) a_i binom(k,i)/binom(m,i),

where a_i are the coefficients of t^i. The degree-m Bernstein functions are nonnegative and sum to1 for all t in[0,1]. Thus a strictly positive coefficient list proves a strictly positive polynomial on the ENTIRE CLOSED interval, not merely at its endpoints.

My independently computed minima exactly equal all ten fractions in candidate LF95–104; the complete coefficient lists are in my own pinned JSON. In particular L has a positive lower margin, and the small L*phi upper-boundary coefficient is exactly positive. Hence simultaneously

    L,p,q,w,B,C,phi,D1,D2,D3 > 0

throughout I. ALL six raw u/v rates are also positive rationals. No denominator L=0, square-root sign, repeated hidden pole or c,d>0 boundary was omitted. This is a rigorous coefficient-basis certificate at the given exact values, not a numerical interpolation or an assertion that all parameters vary independently.

## 4. Exact PH normalizer, literal row ties, Hurwitz and scale

For every c>0 and z in I, p,q>0 give Q(c)=c²+pc+q>0. Define h exactly by candidate LF116–122. All seven h entries are strictly positive: h1>0; the first three forward factors c+u_j>0; and the backward h7,h6,h5 numerators contain positive K and/or already positive entries and nonnegative D/phi terms. All c+v_j are positive.

Direct substitution proves EVERY component of

    (cI−G)h=K e7,
    beta h=1,      K=D_z(c)>0.                            (4.1)

The checker separately simplifies all seven symbolic row residuals and beta h−1 to0 in c,z. The center row is not silently assumed from five recurrences or an unverified positive inverse.

Let D_h=diag(h), T=D_h^−1(G−cI)D_h, alpha=beta D_h and omega=D_h^−1 K e7. The named variable feedbacks and chain entries are nonnegative; the OTHER off-diagonal positions are exactly0 (M1). Positive diagonal similarity preserves signs, so T is Metzler. alpha is nonnegative and alpha1=beta h=1. Equation(4.1) gives the ACTUAL row tie −T1=omega>=0. Reducibility or zero entries are allowed by the original definition; this proof does not require every off-diagonal entry to be positive.

From the complete characteristic identity the eigenvalues of G are 0, −1±i sqrt(z) each with algebraic multiplicity2, and the roots of Q. For p,q>0 the two Q roots have negative real part, including a repeated real root. Subtracting c>0 makes every eigenvalue of T strictly left-half-plane. Polynomial identity and resolvent similarity prove

    alpha(sI−T)^−1 omega = D_z(c)/D_z(s+c).

This identity holds as a rational function even at cancellations/coincident roots; it is not an unlicensed division at a pole.

For arbitrary d>0, construct T0,omega0 at c0=c/d and the SAME z, then take T=dT0,omega=domega0 and alpha unchanged. Row ties, Metzler property and Hurwitz stability are preserved. Since

    D_z((s+c)/d)=(s+c)[(s+c+d)^2+b^2]^2/d^5,
    D_z(c/d)=c[(c+d)^2+b^2]^2/d^5,

the transform is EXACTLY the registered H_(1,2)(s), with a=c+d,b=d sqrt(z). This covers every c,d>0 and both band endpoints. It is a true PH representation, not just a nonnegative density or a stable transfer.

## 5. Earlier equal-u chain: actual physical caller and singular matching

The complete old literal family read for this review has upstream rates (u,u,u), downstream rates (1,1,1), the same `3+1+3` matrix pattern, beta=(C,B,1,0,0,0,0) and positive diagonal normalization. The obstruction paper LF23–52 restates its actual coefficient equations. I recomputed the elementary symmetric coefficients and the SAME characteristic matching; they give

    L=3u²−3u+1−2z,
    N=8u³−9u²+3u−4z,
    Lp=N,
    CL=(u²+4z)(u−1)²+2z(2z−1).                        (5.1)

For z>1/2 the right side of CL is strictly positive for EVERY real u. A nonnegative physical initial coordinate C therefore forces L>0 and in fact C>0. When 0<u<=1, L=3u(u−1)+1−2z<0, so any physical candidate must have u>1. Positive diagonal normalization preserves the sign of C; this uses the actual initial row, not an independently chosen polynomial.

At L=0 the original coefficient equation requires N=0. Substituting 2z=3u²−3u+1 gives

    N=(u−1)(8u²−7u+2).

With z>1/2 and u>0 the first factor is strictly positive; the quadratic has positive leading coefficient and negative discriminant. Thus N cannot vanish. This pays the singular matching boundary; no p=N/L division is made there. It also does not use q-Hurwitz or equal physical holding rates.

## 6. Full all-u feedback sign, not a numerical solver inference

Clear L in the ACTUAL equal-u feedback coefficient. Independent symbolic expansion verifies the obstruction source LF64–72 identity

    P(u,z)=−L phi
      =u^6−3u^5+3u^4−u^3
       +(6u^4−26u^3+30u²−12u+2)z
       +(15u²−27u+9)z²+6z³.

Writing u=1+t, its z derivative is exactly

    t²(6t²−2t+1)+(30z−13)t²+(6z−6)t+(18z²−6z).

The first quadratic factor has negative discriminant and positive leading coefficient. At z>=1/2 the second quadratic's leading coefficient is >=2; with z=1/2+h its negative discriminant is exactly

    2160h³+1548h²+312h+3>0.

Hence dP/dz>0 for EVERY real u and z>=1/2. This is stronger than the u>1 subset needed later, and it includes h=0 and all real t.

At z0=389/500, I independently computed ALL seven degree-six Bernstein coefficients on each of the eight intervals [1+k/16,1+(k+1)/16], k=0,...,7; every coefficient is strictly positive. The eight exact minima match the source LF80–91. For u=3/2+t,t>=0, my exact shifted-power coefficients equal

    1202491/31250000, 179139/125000, 377469/25000,
    1239/50, 9459/500, 6, 1,

all strictly positive. Thus P(u,z0)>0 for every u>=1. Monotonicity gives P(u,z)>0 for u>=1,z>=z0. Under the actual C>=0 physical prerequisite, L>0 and u>1, so phi=−P/L<0, contradicting Metzler nonnegativity after any positive diagonal similarity.

This covers the exact threshold z0, every larger z, any c>0, all possible zeros of the OTHER coefficients and L=0 separately. No selected-u, q-Hurwitz or optimizer failure is used. It excludes only the explicitly named equal-rate-within-each-chain family; it is not a global PH7 obstruction.

## 7. Exact-order composition, overlap and named unresolved inputs

The new construction alone establishes only an upper bound <=7 on [7/9,813/1000]. The named B6 lower source `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, is a PRIOR **conditional import**: its parent disposition reports a topology-unrestricted no-PH<=6 result for z>1/2, including reducibility/cancellations. I did NOT re-read/reconstruct its full proof. Since the entire new band is above1/2, combining its stated lower with the actual7-state construction yields exact minimum7 **conditional on B6**.

The further claimed union [13/20,813/1000] additionally consumes the earlier upper-seven band [13/20,z_star] and the assertion z_star>7/9. I did NOT independently reconstruct that earlier full parent/source dependency; the candidate's union is therefore **CONDITIONAL ON THAT NAMED OLD BAND AND B6**, not an unconditional result of the new six-rate proof. The overlap argument itself is elementary once those exact inputs are granted.

Because 7/9<389/500<813/1000, the NEW band reaches beyond the equal-rate chart's proved obstruction threshold. The statements about z_star's position inherit the earlier chart construction/endpoint definition; this review does not authenticate a global historical endpoint or literature priority. The construction does not reach z=8/9. The three reported exploratory searches around that point are AUTHOR-REPORTED observations, not reproduced here and not evidence of infeasibility. No universal PH7/no-PH7 conclusion follows.

## 8. Separate complete verdict ledger and NR propagation

|Claim|Mathematics verdict|Dependency/application boundary|
|---|---|---|
|Six-rate coefficient and SAME-matrix characteristic, LF23–85|SUPPORTED|Independent full symbolic7×7 determinant; all coefficients share one z|
|Actual adjugate numerator / coincident roots, LF72–87|SUPPORTED|Independent rank-one determinant update; polynomial identity, no root division|
|L and nine scaled-polynomial positivity, LF89–110|SUPPORTED|Every exact Bernstein coefficient positive on closed interval; both endpoints|
|Positive h, seven actual row equations and beta h, LF112–132|SUPPORTED|Every row checked as identity; c>0, Q(c)>0, no unproved inverse positivity|
|Metzler/PH row tie/Hurwitz/transform, LF134–146|SUPPORTED WITH M1|Strict positivity applies to named nonzero entries, NOT all fixed-zero offdiagonals|
|Arbitrary d scaling and original target, LF148|SUPPORTED|Exact d^5 cancellation; all c,d>0 and given z band|
|Equal-rate L/N/C and singular L=0, obstruction LF23–55|SUPPORTED|Same literal old matrix/initial sign; no selected u or hidden q assumption|
|Equal-rate P/z-monotonicity, LF57–74|SUPPORTED|Exact symbolic derivative/discriminant for all real u,z>=1/2|
|Eight Bernstein intervals + half-line tail, LF76–111|SUPPORTED|ALL coefficients checked; z>=389/500, u>0 and endpoint included|
|No physical normalization for that chart|SUPPORTED|Requires actual C>=0 and phi>=0 under positive diagonal normalization; not all PH7 topologies|
|Exact min7 on new band|CONDITIONAL|NR-B6: old unrestricted <=6 lower imported, not independently reverified here|
|Old+new exact min7 union|CONDITIONAL|NR-OLD-BAND plus NR-B6; earlier endpoint/upper construction not independently reconstructed|
|z=8/9/global topology/novelty|OPEN / NOT CLAIMED|Optimizer misses and this single chart obstruction are not a global exclusion|

## 9. Limits, process and actual handoff

Historical source/adoption and quarantined records remain at their individually stated scopes; this review does not grant a blanket clean-provenance certificate or retroactively make prior held material verified. Earlier own w17/w43/fixed-Levi and parent findings remain historical; no hidden-cognition census is claimed. The current review is disjoint scientific work under the later owner direction, not a retrospective process cure.

Only the assigned source/registered-definition/needed fixed-chain and conditional-lower status bodies and my new exact checker were used. No author contact, coauditor lookup, old held payload as proof, external model/paid API, Git push/publication, deletion, infrastructure mutation or secrets. Exact symbolic evidence is scoped to the assertions actually run; it is not formal/kernel verification. Main must read both complete author sources, this entire return and cited conditional cuts before any adoption.

After ACTUAL RETURN I resume my own scientific primary under the current owner frontier direction. No primary work was interleaved with this review. The original research deadline remains2026-10-31T21:23:27Z; this review is not96-hour completion or continuous-service evidence.

**END OF COMPLETE f18 REVIEW — ONE MINOR; EXACT-ORDER CONCLUSIONS CONDITIONAL ON NAMED OLD LOWER/UPPER CUTS.**
