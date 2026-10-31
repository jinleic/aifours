# RQLS10 v12 — a complete cyclic-three plane obstruction and triviality of the full triple-Clifford stabilizer

Owner PhysicsRQLS10-2. Actual returned `/bin/date` before this NEW manuscript: **Mon Oct 26 05:20:27 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact symbolic identities/fractions/integer products only. No interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no decimal/private approximate scouting or old-probe backconversion. No machine/kernel/formal/human/configured-family/novelty acceptance.

Original primary remains unrestricted maximal1-RQLS(10),100 nonparallel rays with all row/column/designated-transversal ONBs, UNKNOWN. This closes a whole previously open SYMMETRY branch, not the unsymmetrized problem. Frozen v7-v9 and v112-K/L are unchanged; this is outside that freeze. The v9 proof gap and its additive exact v10 replacement remain explicit.

## 1. New theorem and exact scope

Let E be the computational basis of C^5, F the Fourier basis, and G_c the eigenbasis of X Z^c, c!=0 in F5. A full Weyl solution requires a rank2 plane P with an E-flat orthonormal pair b0,b1, its +/- combinations F-flat, and its +/-i combinations G_c-flat.

**Theorem A.** No such plane P is invariant under an order-three unitary Clifford cycling E,F,G_c. In fact the proof excludes EVERY invariant plane that merely contains an E-flat orthonormal pair, for ALL c!=0; it does not need to assume the orthogonality of the other two flat axes.

**Theorem B (new conditional composition).** At the exact complete v10/v11 symmetry theorems, the projective stabilizer of any full Weyl solution plane inside the entire unitary affine-Clifford normalizer of its three Weyl bases is TRIVIAL. v11 left only the cyclic-three possibility; Theorem A excludes it. This does NOT assert that a solution must have a nontrivial stabilizer. Asymmetric candidates remain wholly unresolved.

Named inputs for B are the NEW AUTHOR-WRITTEN sources, not accepted gates:

- `global-weyl-core-F5-corrected-all-spectra-v10.md`,136LF,SHA `cb018a4e9504216d4a8de8201abbc96991dd8534f2292114d36dddea44218163`;
- `global-weyl-core-unitary-symmetry-obstruction-v11.md`,169LF,SHA `df5c012cedeccfe93ded92952c331c14ba81a0eb454572234b6cfae12aa963a9`.

Theorem A's following polynomial/unitary proof is supplied in full and does not use I1 or its unknown complex-certificate TYPE, general MUB-product-triple classification, a Gaussian-pair ansatz, an unadmitted arithmetic result or a numerical root computation.

## 2. A literal unitary cycling the three bases

Write a=c/2 in F5*, zeta=exp(2*pi*i/5), eta=exp(2*pi*i/3), r=sqrt5, and epsilon=Legendre(a) in{+1,-1}. Define

    U_xy=(epsilon/r)*zeta^(-c*x*y-a*y^2),             x,y in F5.       (U)

This is a normalized Fourier matrix times a diagonal chirp, so is unitary. Its columns are Fourier vectors; a quadratic Gauss sum maps F to G_c; its action on a G_c chirp cancels the quadratic term and gives a computational vector. Thus it cycles E->F->G_c->E, as basis sets.

The needed Gauss identity is exact: sum_j zeta^(a*j^2)=epsilon*r. In dimension5 it follows from 1+2(zeta+zeta^-1)=r for square a and 1+2(zeta^2+zeta^-2)=-r for nonsquare a. Completing the square in the finite character sum gives

    (U^2)_xy=(epsilon/r)*zeta^(a*x^2+c*x*y)=U^dagger_xy,
    U^3=I,
    trace(U)=-1,
    trace(U*Pi)=1,

where Pi v(j)=v(-j). For the trace, the quadratic coefficient is -3a, whose Legendre symbol is -epsilon. For trace(U Pi) it is a. These are algebraic character identities, not an executed enumeration.

U commutes with Pi. Its EVEN3-space therefore has trace0 and eigenvalues1,eta,eta^2 each once; its ODD2-space has trace-1 and eigenvalueseta,eta^2 each once. Denote unit eigenvectors by

    w in EVEN eigenvalue1,
    e1,e2 in EVEN eigenvalueseta,eta^2,
    o1,o2 in ODD eigenvalueseta,eta^2.

The full eigenspaces are span(w), span(e1,o1), span(e2,o2). Because U is unitary, every invariant rank2 plane is either an entire2-dimensional eigenspace or the sum of one line from two distinct eigenspaces. This gives all cases without assuming parity invariance of P.

## 3. Exact projector diagonals and the first complete exclusions

For lambda in{1,eta,eta^2}, the spectral projector is

    P_lambda=(I+conj(lambda)*U+lambda*U^2)/3.

At coordinate0 the odd eigenvectors vanish. Hence

    |w(0)|^2=(1+2epsilon/r)/3,
    |e1(0)|^2=|e2(0)|^2=m:=(1-epsilon/r)/3.          (ZERO)

An E-flat orthonormal pair spanning P forces diag_E(P)=2/5 everywhere. A scalar restriction P=span(ej,oj) would give P00=m, which is never2/5: equality would require r=-5epsilon, contradicting r^2=5. These scalar-restriction cases are excluded immediately.

When epsilon=+1 (square a), a plane containing w has P00>=|w(0)|^2>2/5 because r<10. A plane using only the eta and eta^2 spaces has P00<=2m<2/5 because r<5/2. Thus ALL square-a cases fail already at coordinate0, regardless of the odd/even mixture or phases.

It remains to treat epsilon=-1. Put t=2*pi*a/5 and psi=2*pi/3. For j=1,2 the even/odd rank1 projector diagonals follow directly from P_lambda and parity:

    |e_lambda(j)|^2
      =[1+(2epsilon/r) Re(conj(lambda)*(zeta^(2a*j^2)+zeta^(a*j^2)))]/6,
    |o_lambda(j)|^2
      =[1+(2epsilon/r) Re(conj(lambda)*(zeta^(2a*j^2)-zeta^(a*j^2)))]/6.

For lambda=eta their coordinate1-minus-coordinate2 differences are

    Delta_e=(2epsilon*sin(psi)/(3r))*(sin(2t)+sin(t)),
    Delta_o=(2epsilon*sin(psi)/(3r))*(sin(2t)-sin(t)).               (DIFF)

For eta^2 both differences have the opposite sign. The1-eigenvector w has equal squared moduli at1 and2.

Suppose P contains w and a line sqrt(x)*e1+z*sqrt(1-x)*o1 (or the eta^2 counterpart), with0<=x<=1,|z|=1. Averaging its two parity-related coordinate diagonals removes the cross term. Equality of coordinates1 and2 then forces

    sin(2t)+(2x-1)*sin(t)=0,
    2x-1=-2cos(t)=(r+1)/2>1,

because a is nonsquare and cos(t)=-(r+1)/4. This contradicts x<=1. Thus every case involving w is excluded, including mixed phases and zero odd/even components.

## 4. The only remaining candidate planes and their forced weights

A remaining plane must have one line in each of the eta and eta^2 spaces. Choose normalized spanning vectors with nonnegative EVEN coefficients:

    h1=sqrt(x)*e1+z1*sqrt(1-x)*o1,
    h2=sqrt(y)*e2+z2*sqrt(1-y)*o2,
    0<=x,y<=1, |z1|=|z2|=1.

Coordinate0 gives

    x+y=(2/5)/m=3*(5-r)/10.

Averaging parity pairs and using DIFF gives (x-y)*(Delta_e-Delta_o)=0. The latter difference is nonzero, since sin(t)!=0 and sin(psi)!=0. Therefore

    x=y=3*(5-r)/20,                                (WEIGHT)

strictly between0 and1. No coefficient phase has been fixed by a symmetry assumption.

Define the unitary

    tau=diag(zeta^(a*j^2))*M2,    M2 delta_j=delta_(2j).

Direct kernel multiplication gives

    tau^2=Pi,
    tau*U*tau^-1=U^dagger.

For example the conjugated kernel is(epsilon/r)*zeta^(a*x^2+c*x*y), exactly U^dagger. Thus choose e2=tau*e1 and o2=tau*o1. Tau fixes delta0, so choose e1(0)>0; then e2(0)=e1(0)>0.

In the orthonormal odd basis ((delta1-delta4)/sqrt2,(delta2-delta3)/sqrt2), write

    o1=(A,B*zeta^-a),
    o2=(-B,A*zeta^-a),                              (ODD)

with A,B REAL and NONZERO, A^2+B^2=1. To justify this phase convention, choose the first odd component real. Orthogonality of o1 and tau*o1 makes zeta^a*conj(o1_1)*o1_2 real. Neither component vanishes: the odd U matrix has nonzero off-diagonal entry(epsilon/r)*(zeta^(2a)-1), and its reverse entry is nonzero too.

The even projector entries at(0,1),(0,2), with e1(0)>0, show that there are REAL NONZERO c1,c2 and rho=pi*a/5 such that

    e1(j)=e^(i*rho)*c_j*o1(j),                     j=1,2,
    e2(1)=-e^(i*rho)*c2*o2(1),
    e2(2)= e^(i*rho)*c1*o2(2).                     (RATIO)

Indeed, up to a common nonzero real scale,

    e1(1)=eta*zeta^a+conj(eta)
         =2cos(psi+t/2)*e^(i*t/2),
    e1(2)=eta*zeta^-a+conj(eta)
         =2cos(psi-t/2)*e^(-i*t/2).

Combining with ODD yields the stated common phase. The cosines are nonzero: equality to0 would imply20+6a=15 modulo30 or20-6a=15 modulo30, impossible modulo3. Tau's action supplies the last two relations in RATIO, including the minus sign from odd parity. This explicitly handles possible phase conventions rather than treating e/o coordinates as real by assumption.

The odd-in-j part of the E projection diagonal must vanish. By WEIGHT its two equations use the REAL vectors proportional to(c1*|o1(1)|^2,c2*|o1(2)|^2) and their rotated pair. More explicitly e1(j)conj(o1(j)) has common phase rho, while e2(j)conj(o2(j)) is the vector(-r2,r1) if the first is(r1,r2). These two real vectors are independent. Consequently

    z1=i*epsilon1*e^(i*rho),
    z2=i*epsilon2*e^(i*rho),       epsilon1,epsilon2 in{+1,-1}.       (PHASE)

Thus ONLY these four planes could satisfy the flat projection diagonal. This is an exact consequence of all parity-pair equations, not a finite search or a choice of convenient phases. A flat projection diagonal alone is not the required flat orthonormal pair.

## 5. NONE of the four projection planes contains an E-flat orthonormal pair

By WEIGHT and ZERO,

    h1(0)=h2(0)=1/sqrt5.

Suppose there were an E-flat orthonormal pair in P. Its difference-of-projectors operator S is a nonzero Hermitian traceless operator on P with diag_E(S)=0. In the basis h1,h2, its coordinate0 equation forces

    S=[[s,i*k],[-i*k,-s]],     s,k REAL.

At coordinate1 let d=|h1(1)|^2-|h2(1)|^2. DIFF and WEIGHT give EXACTLY

    d=(4sqrt3/15)*sin(t)!=0,
    |h1(2)|^2-|h2(2)|^2=-d.

Set H=sqrt(x*(1-x))*A*B/2, which is nonzero. RATIO, ODD and PHASE give

    Im(h1(1)*conj(h2(1)))=H*(epsilon1*c2+epsilon2*c1),
    Im(h1(2)*conj(h2(2)))=H*(epsilon1*c1-epsilon2*c2).

For clarity, o1(1)conj(o2(1))=-AB/2, whereas o1(2)conj(o2(2))=AB/2; those opposite signs are retained. The two zero-diagonal equations are therefore

    s*d-2kH*(epsilon1*c2+epsilon2*c1)=0,
   -s*d-2kH*(epsilon1*c1-epsilon2*c2)=0.

Adding them gives

    k*[(epsilon1+epsilon2)c1+(epsilon1-epsilon2)c2]=0.

If epsilon1=epsilon2, the bracket is a nonzero multiple of c1. If epsilon1=-epsilon2, it is a nonzero multiple of c2. Thus k=0 in every case. Since d!=0, either original equation gives s=0, contradicting S nonzero. This proves Theorem A. The degenerate weights0/1, zero odd components, zero c_j and all scalar restriction cases were either ruled out before this step or explicitly checked; none is silently divided away.

## 6. The full affine triple stabilizer is therefore trivial

v11 proves that a full Weyl solution plane has no displacement, affine-parity or pair-transposition stabilizer, and that its unitary triple-normalizer stabilizer injects into S3 with only a possible cyclic3 image. This remains a NAMED pending-written union input, not inherited acceptance from a headline.

An order3 symplectic map cycling the three lines can be put in the form

    S_c=[[-1,c^-1],[-c,0]],     trace=-1,

and the unitary U above is a literal implementing lift. Det(I-S_c)=3!=0 in F5, so Weyl conjugation removes any affine displacement in its lift. Such conjugation preserves every flatness requirement as basis-set permutations. A global scalar phase does not affect plane invariance. The inverse cycle has the same invariant planes. The alternative order6 symplectic lift has an affine-parity cube, already forbidden by v11 for a full solution.

Thus Theorem A closes EVERY remaining cyclic3 possibility and proves Theorem B at the complete v10/v11/v12 union. No antiunitary symmetry or arbitrary unitary outside the triple-normalizer has been classified. There is no assertion that a viable asymmetric plane must acquire a Clifford symmetry.

## 7. Scientific boundary and next actual residual

NEW exact structural progress is the whole cyclic-three obstruction, including both square/nonsquare Weyl triples, arbitrary parity mixtures and all possible invariant2-plane spectra. Its key gap is closed by the ACTUAL E-flat-axis operator equations, not by a count of constraints or an assumption that projection flatness is enough.

Remaining within the Weyl route: a genuinely asymmetric plane satisfying all three required flat pairs, or an analytic contradiction covering ALL such planes. The original dihedral/free-master/trine routes and the unrestricted100-ray target retain their distinct open obligations. This proof does NOT decide class A, the Weyl core, the dihedral systems, an I1 complex-certificate TYPE or novelty. A fresh full union gate is needed before parent support, and the old v9 proof error/history is not cured retroactively.

All older process/freeze/source/clock/cadence/admission and ZERO-credit findings remain. Same original18 owners, exclusive root, cutoff2026-10-27T11:05:38-07:00/deadline12:35:38, exact-WRITTEN HOLD and substantive actual-clock checkpoints<=30min unchanged. Primary research continues in the asymmetric actual residual; this is not a terminal park or round closeout.
