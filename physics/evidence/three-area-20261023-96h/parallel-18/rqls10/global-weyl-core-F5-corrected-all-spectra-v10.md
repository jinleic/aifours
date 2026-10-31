# RQLS10 v10 — an additive v9 proof-gap erratum and a complete exact Fourier-plane obstruction

Owner PhysicsRQLS10-2. Actual preceding `/bin/date`: **Mon Oct 26 04:52:08 PDT 2026**. NEW AUTHOR-WRITTEN CANDIDATE after the actual v112-B review return and separate primary-resumption ACK sent to Main. No interpreter/calculator/eval/program/CAS/enumeration/solver/replay/CLI/nested agent or scientific GO. All arithmetic below is symbolic identities and exact fractions/integer products, not decimal magnitude scouts. No machine/kernel/formal/independent-family/human/novelty acceptance.

The original unrestricted maximal1-RQLS(10) target is UNKNOWN. This corrects one proof inside the restricted Weyl-core route; it is not a100-ray witness, core-emptiness proof or all-topology no-go. All v7-v9 frozen bytes and the live v112-K/L scope remain unchanged. This successor is OUTSIDE that freeze.

## 1. MAJOR mathematical proof gap in the frozen v9

Frozen `global-weyl-core-prior-art-v9.md`, SHA256 `a39864e1df34cd4b278ef8390a25d505636a4aa90a2847d7138a5ce6c850fcb4`, Theorem3.2 claims that orthogonality of the two Bloch normals forces a quarter turn and an eigenvalue ratio +/-i. **WITHDRAW that inference and the claim that the printed proof exhausted all Fourier spectra.**

For a rotation R of angle gamma around unit axis k, the actual identity is

    n dot Rn = cos(gamma)+(1-cos(gamma))*(n dot k)^2.

Orthogonality also permits gamma=pi and (n dot k)^2=1/2. For instance a half-turn around k sends n=(k+l)/sqrt2 to (k-l)/sqrt2 when k,l are orthogonal. Thus the ratio -1 branch was not excluded by the old inference. This is a new explicit AUTHOR MATHEMATICAL MAJOR/proof-coverage correction, not a source edit or an interpreter/exactness finding. The old conclusion must not be cited from that defective proof. The new complete written proof below re-establishes the same restricted theorem, including the omitted half-turn cases, by a different exact invariant.

The v9 equation-count/generic-emptiness and broad product-triple/prior-art assertions receive no new support here. No I1 certificate TYPE or class-A/core/dihedral emptiness is inferred. All existing findings and ZERO-credit quarantines remain.

## 2. Core, unique flat axes and correct rotation criterion

Let E be the computational basis of C^5 and let F be the unitary DFT, F_{jk}=omega^{jk}/sqrt5, omega=exp(2*pi*i/5). A Weyl-core solution is an orthonormal pair b0,b1 which is E-flat, with (b0+/-b1)/sqrt2 both F-flat. Let P=span(b0,b1).

For the isometry V:C^2->P and u_j=V^dagger e_j, E-flatness gives |u_j|^2=2/5. Its Bloch vectors r_j have length2/5, sum zero, and are perpendicular to the E-flat axis n_E. Five equal nonzero collinear vectors cannot sum zero: they would be an odd number of +/-r terms. Hence these five vectors span n_E^perp, and the ONLY E-flat rays in P are the antipodal pair with axes +/-n_E.

Assume P is invariant under F. Then F(P)=P and an element of P is F-flat iff its F^dagger image is E-flat. Thus the F-flat pair has axes +/-R n_E, where R is the Bloch rotation induced by F restricted to P. The core requires the E-flat and F-flat axes perpendicular, so

    n_E dot R n_E=0.                                  (ROT)

Equivalently, if S=b0*b0^dagger-b1*b1^dagger on P, then S^2=P, trace(S)=0, diag_E(S)=0, and

    trace(S*F*S*F^dagger)=0.                           (HS)

The eigenvalues of F are1 (multiplicity2), -1 (multiplicity1), i and -i (each multiplicity1). An invariant P is a sum of eigenspaces (subspaces in the repeated1 space are allowed). The possible restrictions are exhausted by:

1. scalar1 on P;
2. one even eigenvalue +/-1 and one odd eigenvalue +/-i;
3. eigenvalues i,-i (both odd);
4. eigenvalues1,-1 (both even).

Scalar1 makes R identity, contradicting ROT. A wholly odd P vanishes at coordinate0, contradicting E-flatness. The other two cases are treated next. This list does not assert that gamma=pi is impossible merely from orthogonality.

## 3. Quarter-turn cases — a fully algebraic comparison

Put r=sqrt5, g=(r-1)/4. In the even subspace use the orthonormal basis

    e0=delta0, e1=(delta1+delta4)/sqrt2,
    e2=(delta2+delta3)/sqrt2.

The1-eigenspace of F is spanned by (0,1,-1) and (1,(r-1)/(2sqrt2),(r-1)/(2sqrt2)); its -1 eigenvector is proportional to (1,-(r+1)/(2sqrt2),-(r+1)/(2sqrt2)). Odd eigenvectors have the form (0,x,y,-y,-x).

If the restricted eigenvalue ratio is +/-i, ROT forces n_E perpendicular to the eigenaxis. Consequently, for normalized eigenvectors phi_e,phi_o, the E-flat pair must be

    b0=(phi_e+e^{i*kappa}phi_o)/sqrt2,
    b1=(phi_e-e^{i*kappa}phi_o)/sqrt2.

At coordinate0, phi_o(0)=0, so |phi_e(0)|^2=2/5. The -1 eigenvector instead has squared coordinate0 equal to(5-r)/10, not2/5, and is excluded.

For the1 eigenvalue, choose the phase of phi_o so its nonzero odd components x,y are real. The E-flat cross condition is Re(e^{i*kappa} conj(phi_e(j))*phi_o(j))=0 at j=1,2 (and their negatives). Both x,y are nonzero. After an overall phase adjustment, the real part of phi_e must therefore be supported only at0. That real part is itself a1-eigenvector of the real even Fourier matrix, whereas delta0 is not. It is zero, so phi_e is a scalar phase times a REAL1-eigenvector.

Write its computational coordinates as

    phi_e=(t, s/sqrt2+g*t, -s/sqrt2+g*t,
                -s/sqrt2+g*t, s/sqrt2+g*t),

with real s,t. The coordinate0 and normalization equations give

    t^2=2/5, s^2=r/10.

The difference of its squared coordinate1 and coordinate2 values consequently satisfies

    (|phi_e(1)|^2-|phi_e(2)|^2)^2
       =8*g^2*s^2*t^2=(3r-5)/25.                    (EVEN-DIFF)

On odd vectors, F acts by i*(2/r)*[[s1,s2],[s2,-s1]], with s1=sin(2*pi/5), s2=sin(pi/5), s1^2+s2^2=5/4. For an i or -i eigenvector, 2(x^2+y^2)=1 and

    (x^2-y^2)^2=s1^2/5=(5+r)/40.                    (ODD-DIFF)

E-flatness requires |phi_e(j)|^2+|phi_o(j)|^2=2/5 at BOTH j=1,2. Their two differences have opposite signs and therefore equal squares. EVEN-DIFF and ODD-DIFF would imply

    40(3r-5)=25(5+r), hence 19r=65.

Squaring would give1805=4225, impossible. This closes ALL quarter-turn cases without replaying the frozen decimal-interval comparisons.

## 4. The omitted half-turn1/-1 case — an exact normal-angle invariant

Now P lies in the even3-space, includes the unique -1 line, and contains one line of the1 eigenspace. Its one-dimensional orthogonal complement in the even3-space is spanned by a unit vector w with Fw=w.

The projection onto the full even subspace has computational diagonal(1,1/2,1/2,1/2,1/2). Since diag_E(P)=2/5, the complement has squared moduli

    |w(0)|^2=3/5,
    |w(1)|^2=|w(2)|^2=|w(3)|^2=|w(4)|^2=1/10.

In the orthonormal even basis, fix the phase w0=sqrt(3/5). Write

    w=(sqrt(3/5), e^{i*theta}/sqrt5, e^{-i*theta}/sqrt5).

This form is FORCED: the last two coordinates have equal modulus, while the first row of Fw=w makes their sum real and nonzero. That same equation gives

    cos(theta)=sqrt6*(r-1)/4,
    sin(theta)^2=(3r-5)/4.                           (THETA)

The two signs of sin(theta) are both retained. No symmetric/real ansatz for w was imposed.

Let q=(sqrt3,1,1)/sqrt5, D=diag(1,e^{i*theta},e^{-i*theta}), so w=Dq. Write J=[q]_cross for the real antisymmetric cross-product matrix, with J01=-q2,J02=q1,J12=-q0. The unique Hermitian operator S on P with S^2=P and diag_E(S)=0 is, up to sign,

    S=i*D*J*D^dagger.                               (S)

Proof of uniqueness: after conjugating by D, the real symmetric zero-diagonal part of S annihilates q. Its three equations have only the zero solution because every q_j is nonzero. The imaginary antisymmetric part annihilating q is a scalar multiple of J. Normalizing its two nonzero eigenvalues to+/-1 forces that scalar to+/-1. Diagonal zero in computational coordinates is equivalent to diagonal zero in the orthonormal even basis because S is supported in that subspace.

The even Fourier matrix is

    M=(1/r)*[[1,sqrt2,sqrt2],
             [sqrt2,(r-1)/2,-(r+1)/2],
             [sqrt2,-(r+1)/2,(r-1)/2]].

Using S_ij=i*J_ij*exp(i(theta_i-theta_j)), real symmetry of M gives

    trace(M*S)=-2*sum_{i<j} M_ij*J_ij*sin(theta_i-theta_j)
              =-2*sqrt2*sin(theta).

For transparency, the01 and02 terms each contribute sqrt2*sin(theta)/5 inside the sum. The12 term contributes sqrt3*(r+1)*cos(theta)*sin(theta)/5, and sqrt3*(r+1)*cos(theta)=3sqrt2. Their total is sqrt2*sin(theta).

On P, M has eigenvalues1,-1. In that eigenbasis write S=[[a,b],[conj(b),-a]] with a^2+|b|^2=1. Therefore a=trace(MS)/2 and

    a^2=2*sin(theta)^2=(3r-5)/2,
    trace(S*M*S*M)=2*(2a^2-1)=6*(r-2).              (ANGLE)

Since r=sqrt5>2, ANGLE is strictly nonzero, contradicting HS. Equivalently the two flat axes have dot product3*(sqrt5-2), not zero. This excludes ALL invariant1/-1 planes, including both complex choices of w, rather than dropping the half-turn branch.

## 5. Corrected theorem and precise current consequence

**Theorem (NEW WRITTEN complete proof).** No Weyl-core solution has a plane invariant under the unitary DFT F5. Sections2-4 cover every restriction spectrum, all coordinate zeros allowed by the hypotheses, every phase and both omitted half-turn possibilities. The proof uses no I1/computer certificate, product-triple classification, Gaussian assumption or hidden-coordinate field assumption.

This re-establishes ONLY the restricted theorem of frozen v9 after withdrawing its defective completeness inference. It does NOT show that every plane is Fourier-invariant. No conclusion about the unsymmetrized Weyl core or either dihedral system follows. All original100-ray row/column/designated-transversal requirements remain. Frozen v7-v9 and ongoing v112-K/L reviews retain their own original sources, errors and qualifications; this later successor cannot be inserted retroactively into their freeze.

Next mathematical direction: use the correct invariant-axis criterion, not the false quarter-turn shortcut, to examine the whole E/F-exchanging Clifford symmetry family or abandon invariance entirely. This is a substantive exact replacement proof of the missed branch, not another numeric parameter trial. Original cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and every HOLD/process finding remain unchanged.
