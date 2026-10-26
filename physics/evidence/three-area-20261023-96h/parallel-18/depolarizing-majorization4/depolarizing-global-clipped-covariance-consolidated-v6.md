# Global actual clipped-covariance theorem: ALL containing ranks2/3/4, with no epsilon cutoff

Actual `/bin/date` immediately before this freeze: **Sun Oct 25 11:39:37 PDT 2026**. Owner PhysicsDepol4-2 / physics-2. **NEW AUTHOR-WRITTEN CANDIDATE**, fresh source-pinned reconstruction and parent disposition pending. This is ONE consolidated successor under the102319 primary push, not an accepted unrestricted output-majorization theorem.

**New global result.** For EVERY actual pure four-qubit state, with the full COMPLEX centered local-Pauli Gram Gamma and R=sum local Bloch-length squares,

    K2(Gamma)<=8-R,
    K3(Gamma)<=10-R.

Together with the named supported one-mode inequality, these prove

    Tr(Gamma-2I)_+<=4-R,
    Tr min(Q X3 Q,I_Q)>=4.                            (CLIP)

Thus the ENTIRE actual containment face is covered at k2,k3,k4, pure and mixed. The proof includes EVERY strict epsilon>0 state, however close to0, and the equality locus; it imposes NO positive cutoff and no input ansatz. It uses genuine marginal compatibility through connected Pauli correlation complementarity and the linear-entropy polygon, not a relaxed covariance spectrum or scalar purity alone.

**The original arbitrary-projector low-noise k2/k3/k4 problem remains OPEN.** All general d>0 physical quartics are still required. A leading output projector is not assumed to contain the input. No actual channel counterexample is supplied.

## 1. Authority, chronology, exact imports and evidence limits

The frozen contract is `primary-continuation-20261025-102319-v1.json`, SHA256 `b4dce3ac050ee6688295eff9cbf3e2f3f6326f93e8f973db8374e752770e594b`. The separate own ACK, SHA256 `1f7e0222bf49cce8cd274818d97f81dc112987a7d00ed9ab206ea748fb650a5e`, preceded this new proof body. It discloses same-author exposure and earlier unsubmitted near-product reasoning; that continuity/compactness lead is NOT the proof here. Mandatory v9,v10,v11 and HOLD were read in order. The complete pinned280LF v5 baseline and relevant parent corrections were actually read. V11 remains a LATER evidence correction, with no invented parent clocks or backdating.

The temporary v80-C NL242 review was completely reconstructed, frozen and actually returned to Main before the11:09:25 resumption checkpoint. Its review SHA256 is `ce32bca434781c782dc6b2cd510fc7136c5d7e3ed8a63d73164dd0f05f5c93d2`. The current primary findings were then recorded in substantive checkpoints019 and020 with actual clocks. No serial review was dropped.

The mathematical input boundary is explicit:

- `depolarizing-containment-covariance-consolidated-v3.md`, SHA256 `8c80174c393ec051401bd5d1951efb3f17b738ba94c79978060360aebd237653`: actual centered frame, strong three-copy TC, pure-sector identities and the commutator floors;
- current parent `depol-rank2-containment-parent-v1.md`, SHA256 `c923177f2624ceb8d9cd4c93e4d1d79259201ec691ec06bb23a56ccc233b40cf`, complete28LF read: same-harness written support for that named TC/purity/one-mode boundary, not previously for CLIP;
- current scalar boundary `depol-quartic-frontier-parent-v1.md`, SHA256 `47e727b0b6a03c4ac693057eec6c174d913c3174e1e3ccf6b0360cd33c8ec7a6`, complete19LF read: used ONLY to infer the original trace comparison when c<=0, not to assert D>=0 off the face.

The TC representation proof is a NAMED written import, not a new formal or independent reproof in this successor. Its scalar consequences and the commutator argument used below are displayed explicitly. The new pair/star/Schmidt/marginal arguments are all derived here.

The now-supported v5 entire TC-zero classification has source SHA256 `08c166f20a90f40eebc74ef98eedc981d98aca1ad96cfdea4eb98eefcccdc63c` and parent SHA256 `9b55c9a10e0362b05c862739e87f5523f3f0e7754908966e05e74baae10643e0`. Its complete current parent28LF was read. **That classification is NOT a premise for the new global CLIP proof.** No equality-locus acceptance is silently promoted to nearby states.

The H-Hermiticity erratum is retained: h=Gr is real and H*=H. Nothing replaces g by QLpsi, deletes TT* or realifies the complex Pauli Gram. The polarized block is not needed for the new proof.

## 2. Actual fields and the exact covariance identities

Let rho=|psi><psi| be ANY pure four-qubit state. S_mu denotes the twelve local Hermitian Pauli operators, with all other factors identity. Put

    r_mu=<psi|S_mu|psi> in R,
    R=r^T r=sum_i t_i^2,
    L=sum_mu r_mu S_mu,
    E2=<L^2>, C=|psi^T(sigma_y^tensor4)psi|^2,
    epsilon=E2-6R+8-4C>=0,
    delta=4-R in[0,4].

Here epsilon>=0 is exactly the supported TC input, with its4C coefficient. Order the physical Bloch lengths t1>=t2>=t3>=t4 and define e_i=1-t_i^2, so delta=sum e_i.

Let W have columns S_mu psi, G=W*W, Q=I-rho, and Gamma=G-r r^T. This is the positive Gram of Q S_mu psi, not an independent spectrum. With Z=WW*,

    X3=2rho+Z/2,
    Q X3 Q=(1/2)QZQ.

The nonzero spectrum of QZQ is the spectrum of Gamma; the two matrices have different sizes and additional zero eigenvalues. Also TrGamma=12-R=8+delta.

For clarity, the pure Pauli-sector relation A2=R+2+4C gives TrG^2=16+4R+8C. Since r is real and r^T G r=E2,

    TrGamma^2=TrG^2-2E2+R^2
              =16+delta^2-2epsilon
              <=16+delta^2.                          (PURITY)

Off-site G entries are real; same-site imaginary entries are the Pauli commutators. Hence Gamma-Gamma^T has four nonnegative leading eigenvalues2t1,2t2,2t3,2t4. Since Gamma^T>=0, eigenvalue monotonicity gives

    lambda_j(Gamma)>=2t_j, j1,2,3,4.                 (FLOORS)

No false positive-part Loewner rule is used. As a check, if lambda1>2+delta, then

    TrGamma^2> (2+delta)^2+4(R-t1^2)
              >=16+delta^2,

contradicting PURITY. Thus the supported one-mode inequality is K1(Gamma)<=2+delta=6-R. The missing two- and three-mode sums require the NEW physical compatibility below.

## 3. Exact complex two-qubit block bound

**Lemma PAIR.** For ANY mixed two-qubit state, its six-local-Pauli uncentered Gram G_pair satisfies G_pair<=2I. Its centered covariance therefore also satisfies Gamma_pair<=2I.

Proof. For ONE arbitrary complex coefficient vector, write its local operator as A tensor I+I tensor B, with A,B traceless complex2-by2 matrices. Each Pauli coefficient has a real and an imaginary three-vector. Choose a real unit axis perpendicular to BOTH; in the corresponding orthonormal qubit basis that matrix has zero diagonal. This can be done separately for A and B. Write the transformed matrices

    A=[[0,a],[b,0]], B=[[0,c],[d,0]].

In even/odd computational parity order00,11 |01,10, the Kronecker sum has the two off-diagonal blocks

    M=[[c,a],[b,d]], N=[[d,a],[b,c]].

Therefore

    ||A tensor I+I tensor B||^2
       =max(||M||^2,||N||^2)
       <=|a|^2+|b|^2+|c|^2+|d|^2
       =Tr(A*A)+Tr(B*B)
       =2 sum |Pauli coefficients|^2.

For any two-qubit density sigma, its Gram Rayleigh quotient is Tr sigma O*O, bounded by this operator norm. This proves G_pair<=2I for EVERY complex vector; subtracting the positive r r^T proves the covariance version. The bases can depend on this single test vector. No simultaneous physical rotation of two or three independent complex modes is asserted or needed. QED.

Consequently, for any partition of the four actual qubits into two pairs, the diagonal6-by6 blocks of Gamma are<=2I. Positivity also gives Gamma<=4I: on a vector(x,y), the cross term is at most twice the geometric mean of the two diagonal quadratic forms, so the total is at most2(||x||+||y||)^2<=4(||x||^2+||y||^2). This is an additional control, not a replacement for the sharper R-coupled sums.

## 4. Three anticommuting sets prove an actual connected-star bound

Fix a physical qubit i and name its three neighbours j0,j1,j2. The27 observables S_i^a S_j^b, with a,b in{x,y,z}, split into THREE sets of NINE: for each cyclic shift q, assign distinct central axes x,y,z to j0,j1,j2, and for each neighbour use all three of its axes. Inside one set, observables at the same neighbour anticommute on that neighbour; observables at different neighbours anticommute on the central qubit. Every square is I. The three cyclic assignments cover every one of the27 observables exactly once.

For pairwise anticommuting Hermitian involutions P_l and any state sigma, let u_l=Tr sigma P_l. Then (sum u_l P_l)^2=(sum u_l^2)I and its expectation is sum u_l^2. Cauchy-Schwarz gives sum u_l^2<=1. Thus, for EVERY four-qubit state,

    sum_(j!=i) ||T_ij||_F^2<=3,                     (STAR)

where T_ij is the real3-by3 two-body Pauli correlation matrix. This is the elementary anticommuting-observable uncertainty principle, proved here, not a numerical correlation census or novelty claim.

The crucial CENTERED version is stronger for an actual pure input:

    sum_(j!=i) ||T_ij-r_i r_j^T||_F^2<=3e_i.        (CSTAR)

To prove it, make ONLY a local Schmidt-axis change at i and write

    psi=sqrt(mu)|0 alpha>+sqrt(nu)|1 beta>,
    <alpha|beta>=0, e_i=4mu nu.

For any one-neighbour Pauli O put A=<alpha|O|alpha>, B=<beta|O|beta>, z=<alpha|O|beta>. The connected x/y squares sum to e_i|z|^2. The connected z expectation is(e_i/2)(A-B), so its square is(e_i^2/4)(A-B)^2.

Now apply STAR to the ACTUAL normalized four-qubit state

    chi=(|0 alpha>+|1 beta>)/sqrt2.

Its central Bloch vector is0, and its star norm is exactly sum[|z|^2+(A-B)^2/4]<=3. Since0<=e_i<=1, the original centered-star sum is at most e_i times that quantity. This proves CSTAR. A zero Schmidt coefficient gives a factored central qubit and zero connected correlations, without division by e_i. Frobenius norms are invariant under the local SO3 axis changes, so the conclusion is coordinate-free.

**No covariance spectrum is transported across this reweighting.** Both sets of entries were explicitly calculated. It is a physical auxiliary-state inequality, not the forbidden assumption of SLOCC spectral invariance.

## 5. GLOBAL two-mode placement, with an explicit margin

Place the two most pure physical qubits in A={1,2}, with the other two in B={3,4}, and write

    Gamma=[[Gamma_A,C_AB],[C_AB^T,Gamma_B]],
    s=e1+e2=2-t1^2-t2^2.

The cross entries are exactly the actual connected two-body correlations. By PAIR the diagonal blocks are<=2I. By CSTAR, dropping the nonnegative within-A correlations,

    ||C_AB||_F^2<=3s.

Thus Gamma-2I is Loewner-bounded above by the off-diagonal Hermitian block matrix with C_AB and C_AB^T. Its two leading eigenvalues are the first two singular values of C_AB. Therefore

    S:=K2(Gamma)<=4+sigma1(C_AB)+sigma2(C_AB)
                 <=4+sqrt2 ||C_AB||_F
                 <=4+sqrt(6s).                       (UP2)

Suppose S>4+delta. UP2 forces s>delta^2/6. On the other hand FLOORS and Cauchy-Schwarz give

    TrGamma^2>=S^2/2+lambda3^2+lambda4^2
              >=S^2/2+4(t3^2+t4^2)
              > (4+delta)^2/2+4(R-t1^2-t2^2)
              =16+delta^2/2+4s.

Comparing to PURITY forces s<delta^2/8-epsilon/2<=delta^2/8. This is impossible; at delta0 it also forces simultaneously s>0 and s<=0. Hence, on EVERY actual pure state,

    K2(Gamma)<=4+delta=8-R.                          (K2)

The actual physical ingredient that closes the relaxed-scalar gap is CSTAR plus PAIR. Scalar norm/purity alone is NOT assumed sufficient.

A useful uniform rational margin is also explicit:

    K2(Gamma)<=4+delta-delta^2/(24+14delta).          (K2M)

Indeed if S>=4 and x=S-4, UP2 gives s>=x^2/6. The same purity calculation gives S^2<=16+8delta+2delta^2-4epsilon-8s. Combining them yields7x^2+24x<=24delta+6delta^2-12epsilon. The already-proved K2 makes h=delta-x nonnegative, and substitution gives

    (24+14delta)h>=delta^2+12epsilon+7h^2>=delta^2.

If S<4, its gap from4+delta is larger than delta, so K2M follows directly. This covers all endpoints and has a strictly positive margin whenever delta>0, with NO epsilon cutoff.

## 6. GLOBAL three-mode placement from actual pure marginals

The additional marginal compatibility is the linear-entropy polygon

    e4<=e1+e2+e3, hence e4<=delta/2.                 (POLYGON)

Here is a direct proof. On two copies of rho_123, the three local swaps F1,F2,F3 commute. On a joint sector with m negative swap eigenvalues,

    I-F1F2F3<=sum_(i=1)^3(I-F_i)

is the scalar inequality0 or2<=2m. Taking the expectation gives1-Tr rho_123^2<=sum_(i=1)^3(1-Tr rho_i^2). Global PURE Schmidt duality equates Tr rho_123^2 with Tr rho_4^2. Since e_i=2(1-Tr rho_i^2), POLYGON follows. This is an actual marginal fact; it is false as a freely imposed relation on arbitrary t_i tuples.

Let S=K3(Gamma), T=6+delta. For0<=delta<=2, FLOORS and POLYGON give

    TrGamma^2>=S^2/3+4t4^2
              >=S^2/3+4-2delta,
    S^2<=36+6delta+3delta^2-6epsilon.

Thus

    T^2-S^2>=2delta(3-delta)+6epsilon>=0.

For2<=delta<=4, omit the fourth eigenvalue altogether. PURITY gives S^2<=48+3delta^2-6epsilon, so

    T^2-S^2>=6-2(delta-3)^2+6epsilon>=4>0.

Together these prove the GLOBAL bound

    K3(Gamma)<=6+delta=10-R.                         (K3)

There is also a simple uniform rational margin:

    K3(Gamma)<=6+delta-delta/20.                     (K3M)

For delta<=2, divide the first squared gap by T+S<=2T: the gap is at least delta/T>=delta/8. For delta>=2, the second gap is at least2/T, and2/T>=delta/20 because delta(6+delta)<=40 on[2,4]. Delta0 follows without division. Again this applies to arbitrarily small positive epsilon and does not use a positive cutoff or the TC-zero classification.

## 7. CLIP and the entire containing faces, including mixed inputs

Let m be the number of eigenvalues of Gamma strictly above2. If m1,2 or3, K1/K2/K3 give

    Tr(Gamma-2I)_+=K_m(Gamma)-2m<=delta.

If m0 the result is immediate. If m>=4, positivity and TrGamma=8+delta give that excess at most8+delta-2m<=delta. Therefore

    Tr(Gamma-2I)_+<=delta.                           (CLIP-G)

On psi-perp, C_psi=QX3Q has the nonzero spectrum Gamma/2 and trace4+delta/2. Hence

    Tr(C_psi-I_Q)_+<=delta/2,
    Tr min(C_psi,I_Q)>=4.                           (CLIP)

Only the SPECTRAL min/positive part is meant. There is no claim that taking a positive part preserves a Loewner inequality. The m>=4 step uses the scalar eigenvalues and trace, not that invalid rule.

For ANY complex rank-k orthogonal projector Pi containing psi, k2,3,4, write Pi=rho+P with rank(P)=k-1 in psi-perp. Then

    Tr(Pi X3)=2+R/2+(1/2)Tr(P QZQ)
              <=2+R/2+(1/2)K_(k-1)(Gamma)
              <=k+3.

Thus c:=Tr(Pi X3)-(k+3)<=0 on the ENTIRE actual containing face. The new quantitative margins are

    k2: c<=0;
    k3: c<=-delta^2/(48+28delta);
    k4: c<=-delta/40.                               (FACE)

Product inputs attain the universal non-strict bounds with a suitable containing Hamming-layer projector, so the unqualified face constants are sharp. At k3/k4 a nonproduct pure input has delta>0 and the stated strict gap.

For a MIXED input whose support lies in the SAME Pi, every pure component of any positive decomposition lies there: the nonnegative missing weights sum to0. Apply FACE at that same projector to each component and average ONLY the ORIGINAL affine X3 trace. This proves the mixed containment inequality. It does NOT average R,Gamma,epsilon, the strict margins or the quartic, and does not identify a nonlinear mixed-state equality class.

The accepted scalar low-noise criterion has a,b,d>=0. With d0 and c<=0 its original comparison is immediate for every0<p<2/3. This is a whole-face trace theorem, NOT an arbitrary leading-output-projector Ky-Fan theorem.

## 8. A uniform off-face BRIDGE now holds at ALL three ranks

Let Pi be ANY actual rank-k projector, k2,3,4, and d=1-<psi|Pi|psi>. Define V=Var_psi L=E2-R^2. For0<d<1 take xi=Pi psi/sqrt(1-d), write xi=sqrt(1-d)psi+sqrt(d)eta, and let P=Pi-|xi><xi|. Then P has rank k-1 and is orthogonal to both psi and eta. The actual containing projector Pi0=rho+P has the FACE bound.

Pure Schmidt duality gives X3 psi=X1 psi=(2I+L/2)psi. Also the one-mode bound gives <eta|X3|eta><=(6-R)/2, while <psi|X3|psi>=2+R/2. Consequently

    Tr[(Pi-Pi0)X3]
      <=d(1-R)+sqrt[d(1-d)] Re<eta|L|psi>
      <=d(1-R)+sqrt[d(1-d)V].

The d0 endpoint uses Pi itself; for d1 choose any ray in its range as eta and take the orthogonal rank k-1 remainder. No zero vector is normalized. Thus, for EVERY actual pure pair at the three ranks,

    c<=-gamma_k(delta)+d(1-R)+sqrt[d(1-d)V],          (ALL-BRIDGE)

where gamma2=0, gamma3=delta^2/(48+28delta), gamma4=delta/40. V is the ACTUAL variance; it is not replaced by g or bounded by epsilon through the false coercivity shortcut. The coarser V<=R(4-R) remains available from the bounded local-field spectrum, but is not treated as enough for the full quartic.

This is a quantitative off-face consequence of the new global placement, not a proof that every d>0 pair satisfies the original comparison. The actual a,b coordinates and their correlations with this same d,V still matter.

## 9. Method controls: no false strengthened TC or off-coherent witness

The tempting strengthening epsilon>=4C is FALSE. Consider the ACTUAL normalized pure state

    psi=(sqrt5|0000>+|0011>+|1100>+|1111>)/sqrt8.

Every local z Bloch expectation is1/2, so R1. Its local field is half the total Z; its squared expectation is E2=3. The global spin-flip amplitude is(sqrt5+1)/4, so C=(3+sqrt5)/8. Hence

    epsilon-4C=E2-6R+8-8C=2-sqrt5<0.

The established epsilon>=0 is not contradicted: epsilon=(7-sqrt5)/2>0. This is a method-only countercontrol, NOT a depolarizing majorization or CLIP counterexample. The proof above uses only the supported4C TC and bypasses that false strengthening.

Checkpoint017 also preserves the failure of the naive off-coherent symmetric-square PSD extension. No off-coherent negative witness is called a physical failure. The successful new representation is instead the ACTUAL connected-star estimate and actual pure-marginal polygon, explicitly proved before combining them with the scalar spectrum.

## 10. Per-index written verdict and the exact original residual

For an actual rank-k Pi retain the original SAME-pair coordinates

    a=3k+1-Tr(Pi X1), b=3k+3-Tr(Pi X2),
    c=Tr(Pi X3)-(k+3), d=1-Tr(Pi rho).

The all-noise scalar reduction leaves, in its genuine interior region, the exact physical quartic

    D=27a^2 d^2+18abcd+4b^3 d-b^2 c^2-4ac^3>=0.

No arbitrary tuple or sign/phase is substituted for the actual pair. The current whole frontier is:

|original low-noise index|global written advance in this successor|still required|
|---|---|---|
|k2|EVERY actual containing pair has c<=0; ALL-BRIDGE retained|every remaining actual d>0,c>0 quartic or an exact physical failure|
|k3|NEW entire containment face, global K2/CLIP and explicit margin; ALL-BRIDGE|every remaining actual d>0,c>0 quartic or an exact physical failure|
|k4|NEW entire containment face, global K3/CLIP and explicit margin; ALL-BRIDGE|every remaining actual d>0,c>0 quartic or an exact physical failure|

The ENTIRE strict epsilon>0 domain was used in the proof; no positive lower cutoff is imposed. The old epsilon0 full-channel theorem remains separately supported at its own analytic imports, but is not the basis of this new all-state covariance argument. Mixed strict failures still reduce to a pure failing component only through ORIGINAL affine channel traces, never through nonlinear averaging.

**First unproved step:** control the actual off-face a,b,c,d coupling strongly enough to prove D>=0 for EVERY remaining d>0 pair, or supply a literal state/projector/noise witness with exact trace failure. CLIP and ALL-BRIDGE alone are not that result. The original unrestricted all-p/all-index statement is NOT composed or accepted here.

## 11. Attribution and assurance

The binding Zhang note is `source-audit-v2-zhang-prior-claim.md`, SHA256 `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`. Zhang's public n4 uniform-weight claim and matched complementary clipping mechanism remain explicitly attributed; its support ambiguity and missing displayed certificate are not silently treated as settlement or as a clean novelty clearance. The anticommuting-Pauli uncertainty principle, Schmidt calculation, two-qubit matrix bound and linear-entropy subadditivity are classical tools, derived here, not new mechanisms claimed by priority.

All new results are **WRITTEN candidates at named ordinary-written TC/Pauli imports**. No interpreter/kernel/Lean/formal, human, configured-family/cross-vendor, executable or novelty acceptance is asserted. No scientific eval/arithmetic interpreter/program, symbolic calculator, enumeration/replay/sampling, solver, scientific compile, external modelCLI, nested agent, Git mutation/publication/config change/deletion, new GO or deadline reset occurred. Machine operations were static source/metadata reads, hashes, actual clocks and exclusive own-root outputs. All pinned predecessor and parent bytes remain unchanged.

V9/v10/v11/HOLD remain binding. The original new-science cutoff is2026-10-27T11:05:38-07:00 and final deadline2026-10-27T12:35:38-07:00. This genuine global mixed-mode/CLIP advance is not the completed96-hour round or an unrestricted primary solution. The next original-primary work is the actual off-face quartic, not another arbitrary cutoff or restricted support count.
