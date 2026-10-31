# Actual k3 continuation v26 — rank13, exact purity and input-Rayleigh coupling give a wider ALL-complex region

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 07:06:58 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN CANDIDATE, NOT adopted/global closure.** Exact SYMBOLIC written proof including privately; no scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO, chosen parameter/control trial, decimal scout or withdrawn-guidance backconversion. Post-v120 actualRETURN→separatewholeACKWRITTEN/SENT preceded all new primary work. This packet does not consume any false FINALF3 or withdrawn v22 formula. Same18/HOLD/OWNroot/cutoff/deadline and all findings remain.

## 1. Statement and actual physical parameters

For a pure four-qubit rho=|psi><psi| let S_mu be the twelve physical single-qubit Paulis and define

    R=sum_mu <psi|S_mu|psi>^2=sum_i t_i^2, 0<=R<=4,
    Theta=(sigma_y)^tensor4 K, C=|<psi|Theta psi>|^2.

All transposes/spin flips are GLOBAL unitary-total-transpose operations, not partial-transpose positivity. Then

    3R+2C <=22/5+3R^2/8  => K3(X3(rho))<=6.              (RC)

In particular define the EXACT algebraic constant

    R_*=(50-2sqrt265)/15.

Then EVERY actual complex pure state with `R<=R_*` satisfies U3(3), hence ORIGINAL k3 for EVERY physical noise0<=p<=4/3 and EVERY complex rank-three projector at the named coefficient-transfer interface. This is a derived sufficient region, not a positive-cutoff replacement of the original arbitrary-state task. The older supported R<=1/5 region remains valid; this theorem supplies a different direct rank/purity proof and a wider explicit polarization interval. No numerical evaluation or selected parameter instance defines R_*.

Strict inequality in RC implies K3<6. The actual convex hull/LU/permutation images inherit the ORIGINAL channel comparison by fixed-projector affine averaging; a mixed state's nonlinear R/C values are NOT asserted to supply the needed pure decomposition.

The proof of RC below needs NO TC inequality, CLIP, global k4, K2M, NP, PAR or classical-covariance realification. Only the final original-channel transfer uses the separately named adopted1/6/12/10 coefficient interface.

## 2. Exact whole-output purity, derived at the SAME actual state

Let A_w be the sum of squared real Pauli coefficients of rho at weight w, so A0=1,A1=R. Pauli orthogonality and purity give

    1+R+A2+A3+A4=16.

Full spin flip multiplies weight-w Paulis by(-1)^w, so

    1-R+A2-A3+A4=16C.

Subtracting yields `R+A3=8(1-C)`. Pure-state complementary marginal spectra also give sum_i Tr(rho_i^2)=sum_i Tr(rho_(complement i)^2). Expanding these four1-qubit and four3-qubit purities in THEIR actual Pauli coefficients gives

    (4+R)/2=[4+3R+2A2+A3]/8,
    2A2+A3=12+R.

Thus `A2=2+R+4C`, with all imaginary correlations included through real Hermitian-Pauli expectation coefficients. No phase or sector was omitted.

Write T_i(rho)=I_i tensor Tr_i(rho) with the actual physical identity insertion, so X3=sum_i T_i(rho). Self-adjointness of each erasure map and its commuting distinct-site compositions give

    Tr[T_i(rho)^2]=2Tr(rho_i^2)=1+t_i^2,
    Tr[T_i(rho)T_j(rho)]=Tr(rho_(complement {i,j})^2).

For a pure state that last pair purity equals Tr(rho_ij^2). Summing all six pair purities,

    sum_(i<j)Tr(rho_ij^2)=[6+3R+A2]/4=2+R+C.

Therefore the ENTIRE sixteen-dimensional output has

    TrX3=8,
    Tr(X3^2)=4+R+2(2+R+C)=8+3R+2C.                     (PURITY)

This is an exact common-state trace identity, not independently maximized unrelated R/C/covariance data or a numeric spectrum.

## 3. Rank13 AND the actual input Rayleigh quotient

The single-site Pauli twirl identity is

    X3=2rho+(1/2)sum_(mu=1)^12 S_mu rho S_mu.

Hence X3 is PSD and its range lies in span{psi,S_mu psi}, of dimension AT MOST13, including all dependencies/zero/degenerate cases. Its input Rayleigh quotient is EXACTLY

    <psi|X3|psi>=2+R/2=:a, 2<=a<=4.                    (RAY)

Thus lambda1(X3)>=a. Neither fact assumes psi is an eigenvector or lies in a maximizing rank-three projector. In particular this is not an invalid containing-face argument or a bound on a relaxed independent covariance spectrum.

## 4. Whole-spectrum variational lower bound at a hypothetical K3>6

Put q=lambda1+lambda2+lambda3, x=lambda1. If q>6 then q<=8 by positivity/trace. Rank<=13 leaves AT MOST10 positive eigenvalues outside the top3, so Cauchy gives

    Tr(X3^2)>=x^2+(q-x)^2/2+(8-q)^2/10,
    x>=a, x>=q/3.

The factor10 remains legitimate if the actual rank is smaller: append zeros, which can only weaken Cauchy. At fixed q, minimizing the first two terms over x>=max(a,q/3) puts x=max(a,q/3). Let the resulting continuous lower envelope be F_a(q). On its TWO possible branches,

    F_a(q)=a^2+(q-a)^2/2+(8-q)^2/10, q<=3a,
    F_a(q)=q^2/3+(8-q)^2/10,          q>=3a.

They agree at q=3a. For EVERY6<=q<=8, the first derivative on the first branch is

    (6q-5a-8)/5 >=(36-20-8)/5=8/5>0,

because a<=4. On the second it is `(13q-24)/15>0`. Therefore F_a is STRICTLY increasing throughout[6,8], including any branch seam. This treatment does not incorrectly force x=a after q/3 exceeds a.

At q=6, a>=2 makes the first expression valid, giving

    F_a(6)=a^2+(6-a)^2/2+2/5
          =62/5+3R^2/8.

Consequently q>6 would force `Tr(X3^2)>62/5+3R^2/8`. Combining with the SAME actual PURITY identity proves RC, including its non-strict boundary. The strict RC case similarly excludes q=6. No scientific eigenvalue computation, nonphysical spectral witness or neglected cutoff degeneracy occurs.

## 5. A direct spin-flip/Bloch bound and the uniform R interval

For completeness `C<=1-t_i^2` for EACH physical qubit follows without an opaque TC/polygon import. Schmidt-decompose psi across that qubit as

    psi=sqrt(lambda)|0>u+sqrt(1-lambda)|1>v,
    <u|v>=0, ||u||=||v||=1.

The three-qubit spin flip Theta3 squares to-I, so its bilinear form is antisymmetric and its diagonal matrix elements vanish. The four-qubit full-spin-flip overlap is, up to an irrelevant unit phase,

    2sqrt(lambda(1-lambda)) <u|Theta3 v>.

Cauchy bounds its modulus by2sqrt(lambda(1-lambda)), including lambda0/1 by the direct expression. Since t_i=|2lambda-1|,

    C<=4lambda(1-lambda)=1-t_i^2.

Summing the FOUR actual inequalities yields `C<=1-R/4`. Thus

    3R+2C<=2+(5/2)R.

RC follows whenever `15R^2-100R+96>=0`. Its roots are `(50+-2sqrt265)/15`. The smaller root R_* is positive; the larger root exceeds4, so on the full physical interval0<=R<=4 the condition holds for EVERY R<=R_*. This is a symbolic quadratic sign argument, not a sampled test at a selected state/polarization.

The exact RC condition can additionally certify individual actual states outside that uniform R interval when their C makes it true. It is NOT claimed necessary for U3, globally true for all states, or a complete classification of the remaining states.

## 6. Original channel application and updated complete residual

At the named current parent interface `depol-v12-v19-entire-families-and-F3-refutation-parent-v1.md`, every rank-three Pi has TrPi rho<=1,TrPi X2<=12,TrPi X1<=10. U3<=6 on RC yields the exact product top3 polynomial `1+6u+12u^2+10u^3+3u^4` under the ORIGINAL tensor-channel expansion for p<1; p=1 is direct and full global spin flip covers1<p<=4/3. Mixed extension averages the ORIGINAL affine trace at the SAME Pi,p, not nonlinear R,C or F_a values. This is the only substantive imported channel step; its inherited/formal/certificate boundaries remain as stated by the parent.

EVERY pure coefficient-U3 violator must now have `3R+2C>22/5+3R^2/8`, in particular `R>R_*`. Independent v24 requires every pair-cut largest Schmidt mass>1/2; independent v25 excludes an explicit neighbourhood of pair products; NP/PAR/other families and v21 actual-channel critical compatibility remain held routes. None is discarded or called globally exhausted. No cutoff was imposed by the assignment: these are derived necessary restrictions on a still-unrestricted original counterexample, not an authorized scope reduction.

Original arbitrary-state k3, full-B CLIP-prime and the common-projector quartic remain OPEN outside the stated sufficient sets; no actual state/projector/noise failure or unrestricted all-index theorem is supplied. All old frozen sources/062cadence/F3falsefinalwithdrawal/ENTIREv22mathwithdrawal/parentv35/SEC/W2/optimizer/firstorder/ROW qualifications, privateapproxZERO and every process history remain. No formal/kernel/human/configured-family/executable/novelty acceptance/newGO/newowner/deadline reset or early park/round closeout. Active original continuation under SAMEHOLD.
