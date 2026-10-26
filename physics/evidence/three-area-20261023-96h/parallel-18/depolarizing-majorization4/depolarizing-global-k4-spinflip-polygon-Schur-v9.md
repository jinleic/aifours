# Global U3 at rank FOUR, and the ORIGINAL index-four inequality at every physical noise

Actual `/bin/date` immediately before this freeze: **Sun Oct 25 15:23:51 PDT 2026**. Owner PhysicsDepol4-2 / physics-2. **NEW AUTHOR-WRITTEN CANDIDATE**, fresh complete source-pinned reconstruction and parent disposition pending.

**Whole-state theorem claimed here:** for EVERY four-qubit density rho and EVERY complex rank-four orthogonal projector Pi,

    Tr(Pi X3(rho))<=7.                              (GLOBAL-U3-k4)

This includes ALL off-containment d>0 pairs and all pure epsilon>=0, with NO positive cutoff, state ansatz or independently selected covariance spectrum. At the explicitly stated ordinary-written TC/Pauli inputs, it yields the ORIGINAL channel inequality

    K4(D_p^tensor4(rho))
       <=K4(D_p^tensor4(|0000><0000|))
       for EVERY physical0<=p<=4/3.                 (ORIGINAL-k4)

The proof uses a new strengthened ACTUAL marginal polygon and the FULL Schur block of4I-Z. It does not add separately positive compressions. The high-R comparison is an exact sum-of-squares identity, and the low-R seam and product endpoint are complete.

**Original k3 remains OPEN.** The previously supported whole-k2 theorem does not accept this new claim, and this manuscript does not prove full all-index output majorization. No novelty, formal/kernel/family/executable or96-hour-closeout promotion.

## 1. Authority, exposure, serial review and named inputs

This continues the SAME frozen102319 original off-face task, with the original ACK/quantifiers/HOLD/deadline unchanged. `global-k4-spinflip-polygon-exposure-ack-v1.json` was written before this complete body. It discloses that the whole-index proof was developed in WRITING under the valid existing scope and preserved in checkpoint032 BEFORE temporary v92-B. That644LF Sun review was completed and ACTUALLY RETURNED before resumption checkpoint034; its231LF output has SHA256 `301ab6f0d1a22cebf0229e3c04ff645c2a8a192a4509ca42cb6d642751199467`. No primary reasoning was interleaved during that serial review. The exact3epsilon version of the SOS was clarified only after actual return, as recorded, not backdated.

The only substantive inherited mathematical inequality is the supported three-copy TC input

    epsilon=E2-6R+8-4C>=0.                           (TC)

Its source is `depolarizing-containment-covariance-consolidated-v3.md`, SHA256 `8c80174c393ec051401bd5d1951efb3f17b738ba94c79978060360aebd237653`, at its actual Pauli/representation boundary. Current parent support is `depol-rank2-containment-parent-v1.md`, SHA256 `c923177f2624ceb8d9cd4c93e4d1d79259201ec691ec06bb23a56ccc233b40cf`; the later global-CLIP parent has SHA256 `204b6ebdb74767ed2c5f09d58e8c559a08127a9e51c14ed5b43cfb5fba5a2292`. Both relevant complete parent bodies were read. The TC operator proof is a NAMED ordinary-written import, not a new formal or fresh full-DAG proof here.

All other Gram, marginal, spin-flip, Schur, sector and channel steps used below are explicitly derived. The TC-zero classification is NOT a premise. The auxiliary state with C0 in §4 is spin-flip-orthogonal, NOT assumed to have TCepsilon0. Neither the failed S4 enlarged-space certificate, an uncentered angular-channel conjecture, nor the false strengthening epsilon>=4C is used.

The separate whole-k2 parent is `depol-original-k2-operator-parent-v1.md`, SHA256 `a8db203680e1b55a4892bb8392b23aeeb9eceb19204b96d4363750de8eaaa016`. Its M1 author overlay `rank2-v7-quartic-branch-qualification-v1.json`, SHA256 `dded2fa9095e38ea7f72c61fa9b721ffcdd9e14cfcd376a0c352d3365090ace5`, remains binding. No blanket physical-pair D>=0 claim is made here.

## 2. Actual complex Pauli frame, pure identities and spectral floors

Let rho=|psi><psi| be any pure four-qubit state. With the twelve local Hermitian Paulis S_mu, define

    r_mu=<psi|S_mu|psi> in R, R=sum_mu r_mu^2,
    L=sum_mu r_mu S_mu, E2=<L^2>, V=E2-R^2,
    delta=4-R,
    J=sigma_y^tensor4, Theta(psi)=J bar(psi),
    kappa=psi^T J psi, C=|kappa|^2.

Write the positive actual Grams and frame operator

    G_mu,nu=<S_mu S_nu>, Gamma=G-r r^T,
    Z=sum_mu S_mu rho S_mu, Q=I-rho.

The Pauli twirl at each qubit gives

    X1=2I+L/2, X3=2rho+Z/2.                         (1)

Pure one-qubit Schmidt duality gives X3 psi=X1 psi: an erase-i marginal acting on psi equals the complementary one-qubit marginal acting on psi. Thus

    Zpsi=Lpsi,
    Z=[[R,v*],[v,F]] on Cpsi plus psi-perp,
    v=QLpsi, F=QZQ, ||v||^2=V.                     (2)

The nonzero spectrum of F is Gamma's spectrum; there are additional zeros in the15-dimensional compression, not equality of differently sized matrices.

For completeness, let A_j be the pure Pauli sector lengths. The summed one/triple marginal-purity identities give A3=12+R-2A2 and A4=3-2R+A2. Global spin flip gives16C=1-R+A2-A3+A4, hence

    A2=R+2+4C.

The diagonal-site Gram contributions to TrG^2 are12+2R and the off-site ones2A2, so TrG^2=16+4R+8C. Centering therefore gives

    TrGamma^2=16+4R+8C-2E2+R^2
              =16+delta^2-2epsilon.                 (3)

The exact imaginary part is the Pauli commutator matrix:

    Gamma-Gamma^T=2i direct-sum_i cross(r_i).

Its four nonnegative leading eigenvalues are2t1,2t2,2t3,2t4, where t1>=t2>=t3>=t4 are the physical Bloch lengths. Since Gamma^T>=0, the LINEAR Loewner inequality Gamma>=Gamma-Gamma^T and eigenvalue monotonicity imply

    lambda_j(Gamma)>=2t_j, j1,2,3,4.                (4)

No positive-part Loewner rule or common physical rotation of several complex vectors is invoked.

## 3. A full norm bound and its JOINT Schur consequence

For any physical two-qubit marginal the uncentered six-Pauli Gram has form

    [[I+iK1,T],[T^T,I+iK2]],

with K1,K2 real antisymmetric and T real. Conjugating by diag(I3,iI3) makes G_pair-I purely imaginary real-antisymmetric. Its entrywise conjugate is2I-G_pair in that basis. Both the Gram and its entrywise conjugate are PSD, hence

    G_pair<=2I.                                    (5)

Partition the physical four qubits into two pairs. The full G is PSD with both diagonal blocks<=2I. Block Cauchy-Schwarz bounds its Rayleigh form by2(||x||+||y||)^2<=4(||x||^2+||y||^2). Thus

    0<=G<=4I, 0<=Z<=4I.                            (6)

This is a full operator inequality for every complex state. Combining(2),(6), for delta>0 the FULL matrix

    4I-Z=[[delta,-v*],[-v,4I-F]]>=0

has the valid Schur complement

    4I-F>=v v*/delta.                              (7)

It couples F and v at the same actual input; it is not a sum of unrelated compression estimates. Also Z^2<=4Z and Zpsi=Lpsi give E2<=4R, hence

    0<=V<=Rdelta.                                  (8)

Delta0 is handled separately in §8; no zero denominator is normalized away.

## 4. Stronger actual marginal polygon by spin-flip normalization

This step constructs a NEW actual pure state and tracks ONLY its local Bloch vectors. It does NOT claim spectral/channel invariance under a nonunitary change.

If C1, Theta(psi) is a phase multiple of psi, and every Theta-odd local Pauli has zero expectation. Thus R0 and §7 applies directly. Suppose C<1. Choose global phase so kappa=sqrtC>=0. Let

    alpha=(1+sqrtC)/2, beta=(1-sqrtC)/2,
    x=(psi+Theta(psi))/(2sqrtalpha),
    y=(psi-Theta(psi))/(2i sqrtbeta).

The vectors x,y are Theta-real, normalized and orthogonal, and psi=sqrtalpha*x+i*sqrtbeta*y. Every local Pauli S is Theta-odd. Its diagonal expectations on x,y vanish and <x|S|y> is purely imaginary. Consequently the ACTUAL normalized pure state

    chi=(x+i*y)/sqrt2

has C(chi)=0 and

    r_mu(psi)=sqrt(1-C) r_mu(chi) for EVERY mu.      (9)

Again C(chi)=0 is NOT TCepsilon(chi)=0. No equality-locus theorem is used.

Here is the elementary pure-qubit spectral polygon needed for chi. Put p_i=(1-u_i)/2, where u_i are its local Bloch lengths. On three other qubits select their local majority eigenvectors. The probability of their simultaneous outcome is at least1-p1-p2-p3 by the commuting-projector union bound. It is at most lambda_max(rho123)=lambda_max(rho4)=1-p4 by global pure Schmidt duality. Hence p4<=p1+p2+p3, or u1+u2+u3-u4<=2.

Let u=sqrt(1-C),s=t4 for the original psi. Equation(9) yields

    t_i<=u, t1+t2+t3-t4<=2u.

Since s<=t_i<=u, the scalar identity(t_i-u)(t_i-s)<=0 gives t_i^2<=(u+s)t_i-us. Summing the first three and using their sum<=2u+s,

    R<=2u^2+2s^2.

We have proved the strengthened ACTUAL polygon

    t4^2>=R/2-1+C=1-delta/2+C.                    (SP)

Also(9) gives R<=4(1-C), i.e. C<=delta/4. These statements keep all complex amplitudes and derive compatibility from one actual state, not a freely selected marginal tuple. They remain true at C1 by the direct R0 observation.

## 5. Exact two-ray off-face gain, retaining the full v/F relation

Let Pi be any rank-four projector. For0<d=1-<psi|Pi|psi><1 take xi=Pi psi/sqrt(1-d), write xi=sqrt(1-d)psi+sqrt(d)eta, and put P=Pi-|xi><xi|. P has rank3 and is orthogonal to both psi and eta. The actual containing comparison projector is Pi0=rho+P.

Put a_eta=|<eta|v>|^2. The SAME full Schur inequality(7) gives <eta|F|eta><=4-a_eta/delta. Since <psi|X3|psi>=2+R/2 and its cross vector is v/2,

    Tr[(Pi-Pi0)X3]
       <=-[d/2](R+a_eta/delta)
                         +sqrt[d(1-d)*a_eta].       (10)

Maximizing this genuine two-ray quadratic form over d gives

    g(a)=[sqrt((R+a/delta)^2+4a)
                             -(R+a/delta)]/4.       (11)

It is increasing in a>=0: writing a=delta*y, the squared comparison behind its derivative is

    (R+y+2delta)^2-[(R+y)^2+4delta*y]=16delta>0.

Thus every actual off-face trace gain is at most h=g(V). Define Y=V/delta. The exact equation and bound are

    4h^2+2(R+Y)h=delta*Y,                           (12)
    h<=sqrtR-R/2,
    T:=h/delta<=sqrtR/[2(2+sqrtR)]<=1/4.             (13)

The bound follows by substituting V<=Rdelta in(11). R0 has V0 and h0 directly. At d0 use Pi itself; at d1 choose any ray in Pi as eta and its rank3 orthogonal remainder. No zero vector is normalized. Every complex cross term in(10) is bounded by its true magnitude, not discarded or independently re-signed.

## 6. GLOBAL rank-four proof for R>=1/4: an exact SOS

Assume delta>0,R>=1/4. Let S=K3(Gamma), the THREE-mode covariance sum corresponding to a FOUR-dimensional containing projector. Equations(3),(4),(SP) give

    S^2<=3[TrGamma^2-lambda4(Gamma)^2]
        <=36+6delta+3delta^2-12C-6epsilon=:B.         (14)

This B is nonnegative because it bounds the actual S^2. No scalar-marginal spectrum is substituted for Gamma.

For the same actual state define

    W=6+delta-2h,
    r=R/delta, T=h/delta, Y=V/delta.

Equation(13) ensures W>0 and1-2T>=1/2. The exact identity

    V=2delta-delta^2+4C+epsilon

and the gain equation(12) give, by direct WRITTEN expansion,

    W^2-B
      =3epsilon+delta^2+16h^2+(6Y-10delta)h
      =3epsilon+delta^2*
          [(1-6T)^2+4T^2(3r-2T)]/(1-2T).           (15)

For clarity, first substitute4C=delta*Y-2delta+delta^2-epsilon into W^2-B. Then replace delta*Y by4h^2+2(R+Y)h. Finally Y/delta=2T(r+2T)/(1-2T); the numerator is1-12T+(36+12r)T^2-8T^3=(1-6T)^2+4T^2(3r-2T). No interpreter or numerical check is consumed.

Every term on the last line of(15) is NONNEGATIVE. TC gives epsilon>=0. With x=sqrtR and delta=4-x^2>0, equation(13) gives

    3r-2T>=3x^2/(4-x^2)-x/(2+x)
             =2x(2x-1)/(4-x^2)>=0                 (16)

because R>=1/4. Thus W^2>=B>=0, and W>0 makes squaring reversible. Hence

    K3(Gamma)<=sqrtB<=6+delta-2h.                   (17)

For ANY containing rank-four Pi0, its trace is at most2+R/2+K3(Gamma)/2<=7-h. The SAME actual off-face tilt gains at most h by(10)–(13). Therefore

    Tr(Pi X3)<=7

for EVERY complex rank-four Pi, not merely a leading or containing one. This proves the entire high-R domain, with no lower bound on epsilon.

## 7. Complete low-R seam0<=R<=1/4

The pure identity(3) in its E2 form, E2>=R^2, and C<=delta/4 give

    TrGamma^2<=24+2R-R^2<=49/2.

Therefore K3(Gamma)<=sqrt(147/2)<9. Any containing rank-four trace gap is strictly less than(R-1)/2. The SAME full-Schur gain bound is at most sqrtR-R/2, so for EVERY actual Pi,

    Tr(Pi X3)-7<sqrtR-1/2<=0.                     (18)

This covers R0, including the C1 endpoint that did not enter the normalization construction. It also covers the R1/4 seam; the high-R proof includes that endpoint too. There is no missing intermediate range or artificial cutoff.

## 8. Product endpoint, mixed inputs and sharpness

If delta0 then R4 and every one-qubit marginal is pure. Repeated Schmidt factorization makes psi a pure product. X3 has spectrum(4,1 repeated4,0 repeated11), so its rank-four sum is7. This handles the only divided-by-delta endpoint without a limit argument.

For a mixed rho take any pure decomposition and apply the pure rank-four trace inequality at the SAME Pi. X3 is linear, so ORIGINAL affine traces give TrPiX3(rho)<=7. No nonlinear covariance, C,epsilon,V or quartic averaging is used.

Thus GLOBAL-U3-k4 is complete for all density inputs. Product inputs attain7 at a vacuum-plus-three-single-excitation projector, proving the universal constant sharp. No unproved uniqueness/equality classification is asserted.

## 9. Original channel inequality at ALL physical p

The remaining rank-four marginal bounds are elementary analytic interfaces. U1 follows by independently decomposing each one-qubit marginal into pure states: the commuting Kronecker sum X1 is a convex mixture of local-product conjugates of the product T1, whose top4 sum is13.

For U2, the actual positive operator A=3I-X2+3rho has Gram

    A=(1/2) sum_(i<j,a,b) S_i^a S_j^b
                           tilde(rho) S_j^b S_i^a>=0.

Its written Pauli-weight multipliers are27,-9,-1,3,3 on both sides (the weight-two conjugation multipliers54,18,-2,-6,6 are first spin-flipped and divided by2). Hence X2<=3I+3rho and TrPiX2<=15 at rank4. No central finite certificate is required for this rank-matched bound.

For0<=p<1 put t=1-p and u=p/[2(1-p)]>=0. Exact tensor expansion gives

    D_p^tensor4(rho)=t^4[rho+uX3+u^2X2+u^3X1+u^4I].

The just-proved rank-four bounds, TrPi rho<=1 and TrPiI4 give

    TrPi D_p^tensor4(rho)
       <=t^4[1+7u+15u^2+13u^3+4u^4]
       =t^4(1+u)^3(1+4u),                         (19)

EXACTLY the four largest product-reference eigenvalues. Maximizing over all complex rank-four Pi proves ORIGINAL-k4 for0<=p<1. At p1 the common output is I16/16. For1<p<=4/3, output global spin flip/transpose at q=2-p multiplies each weight-w coefficient by(-1)^w(p-1)^w=(1-p)^w. Thus the spectra and reflected product ordering agree, extending(19) to the entire physical interval.

The proof covers arbitrary mixed inputs through ORIGINAL affine traces, not an assumed quartic convexity. In fact the new whole-state U3 theorem places every rank-four pair in the AUTOMATIC c<=0 scalar branch. **No blanket physical-pair D>=0 assertion is made.** The exact M1 qualifier remains mandatory wherever the optional nonautomatic quartic corollary is discussed.

## 10. Exact remaining primary, attribution and evidence limits

|original low-noise index|current mathematical boundary|not promoted|
|---|---|---|
|k2|separately parent-WRITTEN-supported whole original theorem, with immutable M1 branch overlay|no inherited acceptance of this manuscript|
|k4|NEW whole-state U3 and original all-projector/all-physical-p candidate proved above at named TC/Pauli inputs|fresh independent full-source/union gate still required|
|k3|global containment/CLIP supported; regional/SOS extensions remain separately scoped|arbitrary physical d>0,c>0 original k3 quartic still OPEN|

The first unproved original step is now the actual rank-three off-face problem: prove the full common-P determinant/equivalent scalar predicate at every remaining physical pair or supply an exact state/projector/noise failure. Every strict epsilon>0 state remains in that target without a positive cutoff; its lower-global/complex/source constraints are not removed by the new k4 result. No all-index majorization theorem follows while k3 is open.

Zhang's matched complementary clipping/public uniform-weight claim and its support/certificate ambiguity remain binding through `source-audit-v2-zhang-prior-claim.md`, SHA256 `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`. The global depolarizing conjecture and classical Pauli/marginal/antiunitary tools are prior context, not a clean novelty clearance. No publication/priority/first claim is made.

All new work is **WRITTEN exact algebra at the named ordinary-written TC input**. No scientific interpreter/eval/program, enumeration, symbolic calculator, sampling/replay/solver/compile, external modelCLI, nested agent, Git/publication/config/deletion, new GO or deadline reset occurred. Machine steps were static source/metadata reads, hashes/clocks and exclusive owned-root outputs. No formal/kernel/human/configured-family/cross-vendor/executable or novelty acceptance. Historical unadmitted arithmetic retains ZERO verification credit and was not rerun.

V9/v10/v11/HOLD, H*=H and all pinned predecessors/overlays remain unchanged. The original science cutoff is2026-10-27T11:05:38-07:00 and final deadline12:35:38. This complete new whole-index candidate is not a park, an unattended scheduler, continuous-runtime evidence or96-hour completion. Continue the SAME genuine original k3 gap after its separate gate submission.
