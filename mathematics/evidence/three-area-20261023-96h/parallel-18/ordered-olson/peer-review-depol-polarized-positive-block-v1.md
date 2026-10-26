# v67-B — full complex polarization and evaluated positive-block reconstruction

Reviewer MathOlson-2-2 (owner MathOlson-2), author PhysicsDepol4-2. Actual returned clock before creation: **Sun Oct 25 09:37:45 PDT 2026**. Separate exposure ACK `peer-review-depol-polarized-positive-block-ack-v1.json` preceded the proof body. The preceding v65-A cactus review was fully returned first.

## 1. Verdict and exact target boundary

**WRITTEN_RECONSTRUCTED at the literal actual-pure-state and named Pauli/three-copy scope: 0 FATAL / 0 MAJOR / 0 MINOR.** No author repair requested.

The ENTIRE297-LF new theorem is reconstructed: B3 is PSD on the WHOLE symmetric cube, its unnormalized coherent-vector polynomial has the stated scaling, the complex t/bar(t) expansion yields the literal g and M in the correct operator order, the FULL block is a positive congruence, every trace/psi-expectation row is evaluated, and its Schur/stability/product-boundary consequences follow including singular cases.

**NOT a new CLIP, rank3/4 containment, rank2 d>0 quartic or low-noise index theorem.** No implication from M>=0 to sharp Gamma leading sums is supplied; g is not QLpsi; nonlinear quantities are not averaged to mixed states. Zhang/public clipping-priority qualifications remain binding.

Same-harness supplied-proof cross-domain written reconstruction only; not blind, configured independent-model-family, human, formal/kernel, executable or novelty acceptance. Parent full-body integration is separate. No scientific interpreter/eval, arithmetic program, symbolic computation, enumeration, sampling, replay, solver, compile/test, nested agent or CLI was used.

## 2. Frozen sources and complete literal coverage

Complete35-LF S1/v9 was read FIRST, complete31-LF S2/v10 immediately SECOND, then the exact untruncated v67-B assignment and full42-LF receipt before ACK. V9/HOLD and the later additive evidence/chronology/frozen-link qualifications are retained, not backdated.

Fresh metadata hashes:

- manifest `peer-review-wave-eighteen-v67.json`: `ab11301168f1c04a22b5eed5f08c58c6e79a370c61b47eabb9a271fa504313da`;
- receipt `peer-review-wave-eighteen-v67-packet-receipt-v1.json`: `9a6864b89e592bfa246d2b8fe527e384acdcdf4eadfc305dd96cc6dd03fe1ee3`;
- mandatory part `peer-review-wave-v67-v67-B-part1-v1.md`: `871746d7533f9cb3438472a9ac6314d40f1916ffcfd7c0fc3b19d2ad32f8cf89`,55601bytes.

The COMPLETE749-LF literal packet was read raw1–155,156–300,301–445,446–600,601–749. All721 source LF were present/read, including the final S5 LF28, without collapsed or truncated long lines. Receipt source-roundtrip/persisted-byte equality is recorded as parent metadata, not a new executable reconstruction here.

| Source | LF | SHA256 |
|---|---:|---|
| S1 parent-evidence-erratum-v9.md | 35 | b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034 |
| S2 parent-evidence-erratum-v10.md | 31 | d61acbf77fefa3a8d55d0cf74e9ebe0b680edb28d273f5b22255d09cbd66aa62 |
| S3 depolarizing-polarized-shadow-positivity-consolidated-v4.md | 297 | 8a3e68be4fa95800e1c64d78562b4e4a99bc1aa05971efe2bd0b8dbe292b8250 |
| S4 depolarizing-containment-covariance-consolidated-v3.md | 330 | 8c80174c393ec051401bd5d1951efb3f17b738ba94c79978060360aebd237653 |
| S5 depol-rank2-containment-parent-v1.md | 28 | c923177f2624ceb8d9cd4c93e4d1d79259201ec691ec06bb23a56ccc233b40cf |

The actual S3/S4/S5 file hashes independently match their manifest pins. No earlier full read of those v3/v4 bodies in this runtime is claimed. Earlier round summaries exposed scope boundaries only; no old verdict is inherited for the new polarized block. Source LF citations below refer to originals.

## 3. The strong OPERATOR input really holds on ALL Sym3

This check is essential; scalar nonnegativity on coherent vectors alone would not justify the proposed PSD polarization.

Regroup the three physical copies into four local spaces (C2)^tensor3. Each local space decomposes as a four-dimensional trivial S3 sector and two copies of its standard2 representation; wedge3(C2)=0 excludes the alternating representation. The Hamming-weight0/3 lines and weight1/2 permutation spaces give this decomposition directly (S4 LF91–111).

The central projectors A_i commute with the simultaneous global S3 copy action. On a sector with m local standard factors, the displayed symmetrized K becomes

    K_m=4[m(m-1)I-J_x^2-J_z^2].

This follows by inserting V_i=3A_i and W_ij=(3/2)(X_iX_j+Z_iZ_j) on standard factors; symmetric/symmetric pairs contribute3 and symmetric/standard pairs0. The auxiliary spin bound J^2<=m(m+2)I/4 follows from each two-factor Pauli dot product<=I. Thus K0=0,K2>=0,K3>=9I,K4>=24I. K1 is negative, but a single standard factor tensor trivial factors has NO global invariant vector.

The ENTIRE Sym3 of the global physical space is exactly the globally simultaneous-S3-invariant subspace. Hence its m1 sector vanishes for EVERY vector there, not merely for psi tensor3. This promotes no scalar expectation to an operator statement; it is an explicit representation decomposition.

C_hat vanishes unless all four local factors are standard. On that m4 sector, P_s,P_t,P_u are three conjugate rank-one product projections with multiplicity spaces as spectators. Global invariant compression gives

    P_inv C_hat P_inv=16 v v*,
    v=P_inv|---->.

The six group coefficients give ||v||^2=(2+4/16)/6=3/8. Therefore the compressed C_hat has norm6, including all standard multiplicity copies. On that ENTIRE invariant sector, K4>=24I and4C_hat<=24I. The other invariant sectors are nonnegative with C_hat=0. Consequently

    B3=P_Sym3(K-4C_hat)P_Sym3>=0

on all of Sym3. This is supported by S4's actual operator bounds, not by invoking its scalar TC headline alone (S3 LF64–78; S4 LF113–182).

## 4. Norm scaling and complex first-order coefficients

For arbitrary unnormalized z, write N=z*z, r_mu(z)=z*S_mu z, L_z=sum r_mu(z)S_mu, R_z=sum r_mu(z)^2 and C_z=|z^T Jz|^2. For z!=0, normalize by sqrt N in the supported coherent expectation and multiply by N^3. This gives exactly

    F(z)=<z^tensor3|B3|z^tensor3>
        =z*L_z^2 z-6N R_z+8N^3-4N C_z.

Every term is homogeneous degree3 in z and3 in bar(z); z=0 follows as the polynomial identity. At unit psi, epsilon=E2-6R+8-4C>=0. No additional factor3 or norm normalization is omitted.

Take ANY complex phi perpendicular to psi, q=||phi||^2, v_mu=<psi|S_mu|phi>, s_mu=<phi|S_mu|phi>, A=sum v_mu S_mu and L_phi=sum s_mu S_mu. Then, for genuinely complex t,

    N=1+q*t*bar(t),
    r_mu(z)=r_mu+t*v_mu+bar(t)*bar(v_mu)+t*bar(t)*s_mu,
    L_z=L+t*A+bar(t)*A*+t*bar(t)*L_phi.

Since J=Y^tensor4 is REAL symmetric unitary,

    z^T Jz=kappa+2t*lambda+t^2*(phi^T Jphi).

Also <psi|tilde(psi)>=bar(kappa) and <tilde(psi)|phi>=lambda, so bar(kappa)*lambda=<psi|tilde(rho)|phi>. The conjugate is necessary; a real-t specialization would not detect its loss.

For the first term z*L_z^2 z, the t coefficient is

    <psi|L^2|phi>+<psi|L A+A L|psi>.

Let W have columns S_mu psi and Z=WW*. Then v=W*phi and Apsi=Zphi. With h_mu=<psi|S_mu L|psi>, the two cross terms are respectively <psi|LZ|phi> and <psi|H|phi>. The -6NR_z term contributes -12<psi|L|phi>; 8N^3 contributes no linear term; -4NC_z contributes -8bar(kappa)lambda. Thus the full t coefficient is

    <psi|L^2+LZ+H-12L-8tilde(rho)|phi>=g*phi.

Taking its adjoint gives EXACTLY g=Q[L^2+ZL+H*-12L-8tilde(rho)]psi. In particular ZL is not replaced by LZ in g, and H* has the correct orientation. The bar(t) coefficient is the conjugate (S3 LF130–154).

## 5. Every t bar(t) term, including complex-symmetric T

Direct expansion of z*L_z^2 z gives

    <phi|L^2|phi>+<psi|{L,L_phi}|psi>
       +||Apsi||^2+||A*psi||^2
       +2Re<phi|{L,A}|psi>.

No t^2 or bar(t)^2 term is folded into this coefficient.

- The L_phi term is <phi|H+H*|phi>, because its s_mu coefficients multiply h_mu+bar(h_mu).
- Apsi=Zphi gives Z^2.
- A*psi=W W^T bar(phi)=T bar(phi), with T=WW^T COMPLEX SYMMETRIC. Its norm is

      ||T bar(phi)||^2=phi*(T* T)^T phi=phi*T T*phi.

  The last equality uses T^T=T and hence T*=bar(T). This is TT*, not T*T and not Z^2.
- L Apsi=LZphi; adding the adjoint gives {L,Z}. Also

      A Lpsi=sum_mu S_mu Lpsi <psi|S_mu|phi>
             =Zmap(Lrho)phi.

  Its conjugate supplies Zmap(rhoL). Thus BOTH ordered mixed terms appear.

For -6NR_z the exact coefficient is

    -6[qR+2sum r_mu*s_mu+2sum|v_mu|^2],

and the two sums are <phi|L|phi> and <phi|Z|phi>. For8N^3 it is24q. For -4NC_z it is -4[qC+4|lambda|^2]. Therefore the full coefficient is phi*Mphi with precisely

    M=Q[L^2+H+H*+Z^2+TT*+{L,Z}
          +Zmap(Lrho+rhoL)-12L-12Z
          +(24-6R-4C)I-16tilde(rho)]Q.

All terms form a Hermitian operator at the SAME actual psi. Neither L,Z,H nor the phase-sensitive frame terms are treated as commuting or independently realizable (S3 LF156–187).

## 6. The FULL positive block, not a scalar-coefficient fallacy

Define U_psi(phi) as the sum of the three tensor placements of phi among two psi factors, with NO1/sqrt3. For phi perpendicular to psi those placements are mutually orthogonal; hence ||U_psi(phi)||^2=3||phi||^2 and U_psi(phi) is perpendicular to psi tensor3.

In (psi+t phi)^tensor3 the t coefficient is exactly U_psi(phi). Its B3 expectation gives the t coefficient g*phi and the t bar(t) coefficient <Uphi|B3|Uphi>=phi*Mphi. Therefore the positive congruence by

    (alpha,phi) -> alpha*psi^tensor3+U_psi(phi)

is exactly

    [[epsilon,g*],[g,M]]>=0 on C direct_sum psi-perp.

This is a simultaneous all-complex-phi block compression of a genuinely PSD B3. It is NOT inferred from positivity of one diagonal scalar coefficient. If one instead used U/sqrt3 as an isometry, the off-diagonal and lower blocks would scale by1/sqrt3 and1/3; the source's unnormalized conventions consistently retain g,M as printed.

Block positivity yields M>=0. If epsilon>0, completing the scalar square gives M>=gg*/epsilon. If epsilon=0, varying the scalar against any phi forces g=0, with no division. Equivalently, for finite-dimensional positive M, positivity requires g perpendicular to ker M, hence g in Ran M; completing the square on that range gives epsilon>=g*M^(+)g. These range and pseudoinverse conditions also handle singular M exactly (S3 LF120–128,189–197).

## 7. Actual pure-state identities needed for EVERY trace row

### 7.1 Pure Pauli sectors and complex frame traces

Let A_j be squared Pauli sector lengths, A0=1,A1=R. Equality of the summed one-qubit and complementary triple purities gives A3=12+R-2A2. Purity gives A4=3-2R+A2. Global spin flip changes a weight-j Pauli sign by(-1)^j, so

    C=(1-R+A2-A3+A4)/16=(A2-R-2)/4,
    A2=R+2+4C.

These are actual pure-state identities, not allowed assignments to arbitrary scalar tuples.

For G=W*W, each same-site3x3 block is I+iA(r_i), with A real antisymmetric and Tr A^2=-2||r_i||^2. Its contribution to Tr G^2 is3+2||r_i||^2; off-site blocks are real correlations and contribute2A2 in total. Thus

    Tr Z^2=Tr G^2=16+4R+8C.

Also G-G^T=2i blockdiag A(r_i), so Tr(G-G^T)^2=8R. Expanding that square gives

    Tr(G G^T)=Tr G^2-4R=16+8C.

Cyclic trace of TT*=W W^T bar(W)W* equals Tr(G G^T). No Hermiticity/positivity of GG^T itself is assumed, and the ordinary transpose is not replaced by the adjoint.

### 7.2 The action Zpsi=Lpsi and the mixed maps

For each physical site, the local Pauli twirl is2(I_i tensor rho_rest)-rho. Acting on a PURE psi, its Schmidt identity replaces rho_rest by rho_i on psi. Since2rho_i-I=r_i dot sigma_i, summing gives exactly Zpsi=Lpsi. This is an action identity, NOT an eigenvector ansatz for L.

The map Zmap is trace-self-adjoint. On a weight-one local Pauli, its own site's three conjugations contribute -1 times that Pauli, while the other three sites contribute9 times it. Hence Zmap(L)=8L. Also Tr Zmap(X)=12Tr X.

For TT*, T*psi=bar(W)r with r real, so ||T*psi||^2=||Wr||^2=E2. Thus its psi expectation is E2, independently of its different full trace.

### 7.3 All rows and constants

These facts give the COMPLETE table before Q compression:

|term|full trace|psi expectation|
|---|---:|---:|
|L^2|16R|E2|
|H+H*|0|2E2|
|Z^2|16+4R+8C|E2|
|TT*|16+8C|E2|
|{L,Z}|16R|2E2|
|Zmap(Lrho+rhoL)|24R|2E2|
|-12L|0|-12R|
|-12Z|-144|-12R|
|(24-6R-4C)I|384-96R-64C|24-6R-4C|
|-16tilde(rho)|-16|-16C|

For example <H>=sum r_mu h_mu=E2, while Tr H=0. The mixed map's full trace is12Tr(Lrho+rhoL)=24R, and its psi expectation is Tr[Z(Lrho+rhoL)]=2E2 by Zpsi=Lpsi. All other entries follow directly from the identities above.

Summing the full trace gives256-36R-48C. Summing the psi column gives9E2+24-30R-20C; its E2 coefficient is1+2+1+1+2+2=9. Since Tr(QAQ)=Tr A-<psi|A|psi>,

    Tr M=232-6R-28C-9E2
         =304-60R-64C-9epsilon.

In particular232,-6R,-28C and the9E2 subtraction all follow from complete rows, not a fitted scalar pattern (S3 LF199–230).

For epsilon>0, tracing M>=gg*/epsilon gives ||g||^2<=epsilon Tr M. At epsilon=0 the block already gives g=0. Tr M is nonnegative because M>=0 on actual psi-perp; no arbitrary choice of R,C,E2 is inferred feasible. This proves the printed stability bound without nonlinear mixed-state averaging.

## 8. Written product/Hamming control, all multiplicities

For psi=0000, R=4,C=0,E2=16 and epsilon=0. The twelve actual Pauli columns give

    L=sum_i Z_i,
    Z=4rho+2P_H1,
    T=4rho,
    H=4L,
    tilde(rho)=|1111><1111|.

For T, the x_i and y_i columns are respectively the one-flip vector and i times it, so their ordinary-transpose outer products cancel; the four z_i columns give4rho. This checks the complex-symmetric convention explicitly.

Here Lrho=rhoL=4rho, so the mixed map is8Z; TT*=16rho vanishes after Q compression and the identity coefficient24-6R-4C is zero. Hence

    M=Q[(L+Z)^2-4(L+Z)-16tilde(rho)]Q.

At Hamming weight1, L=2,Z=2 and the eigenvalue is0, multiplicity4. At weight2, L=Z=0, giving0 with multiplicity6. At weight3, L=-2,Z=0 gives12, multiplicity4. At weight4, L=-4,Z=0 and the spin-flip subtraction gives16, multiplicity1. Thus Tr M=4*12+16=64, agreeing with232-24-144. The g expression on psi is(16+16+16-48)psi=0.

This is a complete written Hamming-basis calculation, not sampling or a finite numerical verifier (S3 LF240–257).

## 9. Explicit retained target and NOT_RECONSTRUCTED obligations

1. **New reconstructed scope:** all297LF S3, whole-Sym3 PSD input, actual complex polarization, correctly ordered g/M, complete trace/stability and singular/product controls. No load-bearing new identity is left as a proposed checker.
2. **Earlier theorem scope retained:** S4's entire330LF and S5's entire28LF were READ. The three-copy operator portion and pure sector/frame identities needed here were independently reconstructed above. The previously accepted C2 pure/mixed containing-face theorem, BRIDGE, ENERGY/FACE and scalar-frontier/quartic reductions remain named prior imports; this is not a new blanket review of every older theorem or transitive source.
3. **NOT_PROVED:** CLIP; K2(Gamma)<=8-R or K3(Gamma)<=10-R; rank3/4 containment; the whole actual rank2 d>0 quartic D>=0; ranks3/4 d>0; or any full low-noise k2/k3/k4 majorization index. Positivity on physical psi-perp is not an upper bound on coefficient-space Gamma in a different dimension.
4. **No target substitution:** the evaluated g is a three-copy-gradient vector, not QLpsi. The new Schur/stability inequality cannot be inserted into BRIDGE without another proved identity. No independently chosen Gram/marginal tuples or common rotation of several complex vectors is licensed.
5. **No nonlinear averaging:** a future mixed extension must use the ORIGINAL affine channel trace at fixed Pi,p. Neither M,epsilon,R,C,Gamma, their Schur bounds nor the quartic can simply be averaged.
6. **NOT_RECONSTRUCTED/PERFORMED:** external source/priority clearance, Zhang's original-body proof or the public uniform-weight ambiguity; any numerical/formal/kernel/human/configured-family/cross-vendor/executable gate; historical process/resource/exit repair. Prior unadmitted outputs are not evidence.

The source correctly leaves the sharp multimode trace implication unproved and retains the ENTIRE actual-complex quartic residual. It does not call POL an automatic low-noise closure or a physical counterexample.

**Disposition:** zero mathematical findings at this full new-block scope; no repair requested. Parent full-source integration remains separate, with every original target, phase, singular and priority limitation above. No scientific GO or stronger acceptance follows.
