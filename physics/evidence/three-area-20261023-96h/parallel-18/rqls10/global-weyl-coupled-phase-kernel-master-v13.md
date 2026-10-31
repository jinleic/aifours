# RQLS10 v13 — a rank-free coupled phase-kernel master, complete rank3/4 fibers, and actual100-ray reconstruction

Owner PhysicsRQLS10-2. Actual returned `/bin/date` before this NEW successor: **Mon Oct 26 05:29:14 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact symbolic/fraction/integer-product reasoning only; no interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no decimal/private approximate scout or discarded-probe backconversion. Machine/kernel/formal/independent-family/human/novelty checks NONE.

The unrestricted maximal1-RQLS(10) primary remains UNKNOWN. This is a genuinely asymmetric EXACT MASTER for the defined Weyl-orbit route, not another symmetry ansatz or a claim that the route is WLOG for every RQLS10. No actual solving gamma point is supplied. Frozen v7-v9, v112-K/L and every prior finding remain unchanged. v10-v12 are separate pending-written successors.

## 1. Exact target inside this route and new result

Let zeta=exp(2*pi*i/5), E computational, F the Fourier basis, and G_c the basis with vectors

    g_M(j)=zeta^((c/2)j^2+M*j)/sqrt5,   c in F5*.

We require orthonormal E-flat b0=a/sqrt5,b1=b/sqrt5, with (b0+/-b1)/sqrt2 F-flat and (b0+/-i*b1)/sqrt2 G_c-flat. All coordinates of a,b have modulus1.

**Theorem A (rank-free master).** The required pairs are equivalent, modulo one overall phase, to vectors gamma,rho in T^5 satisfying

    sum_j gamma_j=0,
    product_j rho_j=1,
    M1(gamma)*rho=0,
    M2(gamma)*(rho_j*rho_(j+1))_j=0.                 (MASTER)

The literal4x5 matrices are given in Section2. The second kernel vector is the coordinatewise product of the FIRST vector with its cyclic shift; it is NOT freely or independently selected from another kernel.

**Theorem B (no hidden low-rank waiver).** For EVERY gamma in T^5 with sum gamma=0 and EVERY c!=0, BOTH M1 and M2 have rank at least3. Hence the master has ONLY rank3 and rank4 fibers. The full proof uses unit phases and the odd cycle, not a generic-rank statement.

**Theorem C (exact phase elimination).** In rank4, the first kernel is given by its FIVE cofactors. Equal nonzero cofactor moduli and one explicit coupled M2 identity are NECESSARY AND SUFFICIENT. In rank3 the corresponding necessary/sufficient fiber is the COMPLETE projective kernel line, with one complex projective parameter including infinity. Every rank/zero boundary is retained; the fifth-root phase reconstruction introduces no field restriction.

**Theorem D (actual witness consequence).** Any exact MASTER point gives an explicit maximal1-RQLS(10) with100 distinct rays, without any further nonparallelness guess. This is a proved reconstruction interface, NOT a delivered point or finite-witness certification.

No I1 real/complex certificate, Sylow/NEB classification, general product-triple theorem or novelty assumption is used in A-D.

## 2. Literal matrices and derivation

Put gamma_j=b_j/a_j and, for m in{1,2}, let j+m be read modulo5 and define

    A_j(m)=1+gamma_(j+m)/gamma_j,
    B_j(m)=gamma_(j+m)+1/gamma_j,
    C_j(m)=gamma_(j+m)-1/gamma_j,
    chi_j(m)=zeta^(-c*m*j).

M_m(gamma) has four rows

    ( A_j(m) )_j,
    ( B_j(m) )_j,
    ( chi_j(m)*A_j(m) )_j,
    ( chi_j(m)*C_j(m) )_j.                          (M)

Every denominator is nonzero because gamma is a unit vector coordinatewise. Define rho_j(m)=conj(a_j)*a_(j+m). The two F-flat conditions have off-zero autocorrelations equivalent to

    sum_j rho_j(m)*(1+conj(gamma_j)*gamma_(j+m))=0,
    sum_j rho_j(m)*(gamma_(j+m)+conj(gamma_j))=0.

The G_c-flat conditions multiply a and b by the SAME chirp zeta^(-(c/2)j^2), then take the +/-i combinations. Their two equations are

    sum_j chi_j(m)*rho_j(m)*(1+conj(gamma_j)*gamma_(j+m))=0,
    sum_j chi_j(m)*rho_j(m)*(gamma_(j+m)-conj(gamma_j))=0.

The common factor zeta^(-(c/2)m^2) in the chirp autocorrelation is nonzero and cancels. These are exactly M_m*rho(m)=0. No phase field, projective real form, selected gamma alphabet or positivity relaxation was imposed.

m=1,2 suffice: each of the ACTUAL sequences a+b,a-b,chirp*(a+i*b),chirp*(a-i*b) has autocorrelation at -m equal to the conjugate at m. The remaining two nonzero shifts follow. The zero-shift norms are10, since sum gamma=0 makes both its real and imaginary parts zero. Fourier inversion of the squared magnitudes then proves the ENTIRE flatness equations, including every Fourier label, not just selected off-zero shifts.

Now rho_j=rho_j(1) obeys product rho=1 and

    rho_j(2)=rho_j*rho_(j+1).

Conversely, given MASTER choose a0=1 and recursively a_(j+1)=a_j*rho_j. Product rho=1 closes the5-cycle; all a_j are unit. Set b_j=gamma_j*a_j. Sum gamma=0 gives the ACTUAL orthogonality, and the preceding autocorrelation equivalence gives every required flatness equation. This proves Theorem A in both directions.

## 3. Uniform rank lower bound — no matrix census

The argument works for either m, since j->j+m is one5-cycle and chi_j takes five distinct unit values. Suppress m in notation.

### 3.1 The first two rows A,B are always independent

A cannot vanish identically: gamma_(j+m)=-gamma_j around an odd cycle would give gamma_j=-gamma_j. At any A_j!=0, the unit-phase identity

    B_j/A_j=(gamma_j*gamma_(j+m)+1)/(gamma_j+gamma_(j+m))

is REAL (write the two phases as exp(iu),exp(iv), obtaining cos((u+v)/2)/cos((u-v)/2)). Therefore a relation B=kappa*A would have REAL kappa.

Multiplying this relation by gamma_j gives

    (gamma_j-kappa)*(gamma_(j+m)-kappa)=kappa^2-1.    (EDGE)

If kappa is not+/-1, its recurrence

    gamma_(j+m)=(kappa*gamma_j-1)/(gamma_j-kappa)

has no zero denominator and is an involution: the representing2x2 matrix squares to(kappa^2-1)I. A5-cycle of an involution is fixed, so all gamma_j agree, contradicting sum gamma=0.

If kappa=+1 or-1, EDGE makes every adjacent pair include a coordinate equal to kappa. A vertex cover of an odd5-cycle has at least3 vertices, so at least3 coordinates equal the SAME unit kappa. The other at most2 unit coordinates cannot cancel their sum. Thus sum gamma=0 fails here as well. This proves independence, including all zero A_j/B_j boundaries.

Also A has support at least2: sum_j gamma_j*A_j=2sum_j gamma_j=0, so support1 is impossible, and support0 was already excluded.

### 3.2 Rank2 of the four-row matrix is impossible

Suppose rank M_m=2. Since A,B are independent, there are complex u,v,w,z with

    chi*A=u*A+v*B,
    chi*C=w*A+z*B.

v cannot vanish: otherwise all nonzero A_j would require the SAME value chi_j=u, contradicting its support>=2 and the five distinct chi values. If A_j=0, the first identity forces B_j=0, and the second forces C_j=0. But B_j=C_j=0 would give gamma_(j+m)=0, impossible. Thus EVERY A_j is nonzero.

Consequently chi_j=u+v*(B_j/A_j) places ALL FIVE distinct unit roots chi_j on the affine REAL line u+v*R. A line meets the unit circle in at most2 points, contradiction. Hence rank M_m>=3. Four rows give the upper bound4, proving Theorem B over the ENTIRE admitted gamma torus, not only a generic or symmetry-free subset.

## 4. Rank4: exact cofactor fiber and complete removal of a

Assume rank M1=4. For j=0,...,4 define

    v_j=(-1)^j*det(M1 with column j deleted).

The cofactor identity gives M1*v=0 and v!=0. Because the kernel is one-dimensional, a vector rho in that kernel has all coordinates unit iff

    |v_0|^2=|v_1|^2=...=|v_4|^2>0.                (MOD)

The strict inequality is essential: a rank4 kernel with a zero coordinate cannot supply a unit torus point.

The ENTIRE full-triple condition in this rank stratum is now

    gamma in T^5, sum gamma=0, rank M1=4,
    (MOD),
    M2*(v_j*v_(j+1))_j=0.                         (COFACTOR)

Necessity follows by writing rho=lambda*v. For sufficiency choose ANY fifth root satisfying

    lambda^5*product_j v_j=1.

Because the five |v_j| coincide and are positive, this identity automatically gives |lambda|=1/|v_0|. Thus rho=lambda*v is unit with product1. The second kernel equation is multiplied only by the nonzero common factor lambda^2. Theorem A reconstructs the full pair a,b.

All five choices differ by a fifth root of unity, which modulates a_j,b_j by the SAME character zeta^(k*j). They are the ordinary Weyl modulation freedom, not an extra arbitrary input or a restriction to roots of unity for the unknown gamma itself. Gamma and all reconstruction coordinates remain arbitrary complex phases. This is a full necessary/sufficient rank4 elimination of four independent a-phases, not an existence proof from dimension counting.

## 5. Rank3: the COMPLETE exceptional fiber, including infinity

If all five4x4 cofactors vanish, Theorem B says rank M1 is3, NOT that the phase problem is empty. Let v,w be ANY two basis vectors of the ACTUAL kernel of M1(gamma). They are not independent physical weights or freely selected polynomial factors.

Every projective kernel direction has the form

    xi(tau)=v+tau*w, tau in C;
    xi(infinity)=w.

The exact necessary/sufficient fiber is

    |xi_0|^2=...=|xi_4|^2>0,
    M2*(xi_j*xi_(j+1))_j=0.                        (LINE)

Choose lambda by lambda^5*product xi=1 and set rho=lambda*xi as before. This gives every unit product1 kernel vector and the full required pair. Conversely every master solution supplies one such projective direction. Changing v,w merely changes the projective coordinate tau; it does not enlarge the fiber. Infinity, coincident equal-modulus equations, zero coordinates and the rank boundary are all explicit. A zero common modulus is never admitted.

Thus the whole remaining Weyl problem is the UNION of COFACTOR and LINE, with gamma arbitrary on the full unit torus and sum gamma=0. There is no missing rank<=2 case and no independent second-kernel selection. No field-descent or reality restriction of a complex nullspace is used.

## 6. Actual maximal1-RQLS10 reconstruction, not merely a phase tuple

Given a master solution, let b0=a/sqrt5,b1=b/sqrt5 and

    psi=(|0> tensor b0+|1> tensor b1)/sqrt2.

It has qubit marginal I2/2. Identify C^10 with C^2 tensor C^5 by t->(t mod2,t mod5). Then X10=X2 tensor X5 and Z10=Z2 tensor Z5^3. Choose the unique UNIT k mod10 with3k=c mod5 (its parity is odd). The three required unbiased bases are the eigenbases of Z10, X10 and X10*Z10^k; the last is the y-qubit basis times G_c. All flatness conditions were proved by MASTER, not assumed from spectra.

Put the100 vectors X10^p Z10^q psi on cells(p,q) in Z10^2. Rows are cosets of the Z line, columns cosets of the X line, and designated transversal classes cosets of<(1,k)>. The three subgroups have order10 and pairwise trivial intersection because k is a unit. Inner products within each coset are phases times the corresponding Weyl expectation. Unbiasedness to each simple-spectrum eigenbasis is exactly the vanishing of those nonidentity expectations, by finite Fourier inversion. Hence EVERY row, column and designated class is an ACTUAL ONB.

Finally suppose a nonidentity Weyl displacement fixes the ray of psi. Under CRT write its indices(g2,g5). If g2!=0, its fifth power is a nontrivial qubit displacement times identity and belongs to one of the THREE unbiased subgroups, whose expectation must vanish; a ray eigenvector would instead have modulus1. If g2=0 but g5!=0, the pentit displacement has simple eigenspaces. Its ray eigenvector psi must be a PRODUCT state, contradicting the already-derived qubit marginal I2/2. Thus no nonidentity displacement fixes its ray, and all100 cell rays are pairwise nonparallel. This proves Theorem D with every original normalization/ONB/nonparallelness requirement, conditional ONLY on supplying an actual master point.

## 7. Exact remaining gap, not an execution request

No gamma, cofactor point or projective-line point satisfying all displayed identities has been constructed, and no proof excludes ALL such points. In particular rank3 is NOT discarded because its cofactors vanish; its coupled fiber is part of the open residual. This is an exact replacement for a phase search with independent kernels, not an easier relaxation or a small alphabet. Both original Weyl classes are covered by c!=0, without invoking I1 to decide either class.

The v10-v12 symmetry obstructions, if accepted jointly, mean one should not expect a full-triple solution plane to be fixed by a nonidentity triple-Clifford symmetry. They do NOT settle COFACTOR/LINE or the unrestricted problem. A new exact point from either rank stratum would solve the original positive target via Section6; failure of both would close only this Weyl route, not all possible1-RQLS10 constructions.

Next action is an exact symbolic attack on the coupled rank3/4 fibers, retaining all phase variables and both kernel equations, or a genuinely different unrestricted construction. No scientific computation, finite checker, solver or GO is requested. All permanent findings, frozen bytes, original18 owners, exclusive root, cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and30min substantive actual-clock cadence remain. Primary research continues, not a final park for pending gates.
