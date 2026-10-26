# Actual off-face continuation: full operator couplings, a whole low-R theorem, and an exact code-extension obstruction

Actual `/bin/date` immediately before this freeze: **Sun Oct 25 14:01:44 PDT 2026**. Owner PhysicsDepol4-2 / physics-2. **NEW AUTHOR-WRITTEN CANDIDATE**, fresh complete reconstruction and parent disposition pending. Same102319 original task, no new scope/GO/park.

**New unrestricted-projector theorem on an intrinsic domain:** EVERY actual pure four-qubit state with R=sum_i t_i^2<=1/5 satisfies U3 at EVERY spectral index. At the named global U1/U2/common-order/reflection imports, the ORIGINAL depolarizing-output comparison therefore holds for EVERY physical p and EVERY index on this entire low-R domain and its specified pure-state convex hull. This does not impose a state ansatz or an epsilon cutoff; all R>1/5 states remain in the assigned whole target.

**Independent whole off-face branch:** EVERY actual pair with a<=9d satisfies the full low-noise comparison by an exact SOS identity, for pure OR mixed rho.

**New full joint operators:** X1-X3 and M=A+tilde(rho) have complete PSD/operator-norm proofs below. These are actual whole-operator couplings, not sums of separately known compressed inequalities. The remaining common-projector Schur determinant is explicitly retained.

**Original unrestricted k3/k4 remain OPEN.** The v7 whole-k2 theorem is a SEPARATE candidate under its own gate, not a premise here. A tempting FULL-space S4 extension is explicitly false on an entangled reference/code vector; this is a method obstruction, not a physical counterexample.

## 1. Authority and exact input boundaries

Main continued the SAME `primary-continuation-20261025-102319-v1.json` scope after v6. The original immutable ACK remains authority. `offface-regional-successor-exposure-ack-v1.json` was written before this complete body and discloses all preceding valid-scope reasoning in checkpoints023,024,026,028. No backdated preregistration or blindness.

Current parent `depol-global-CLIP-v6-parent-v1.md`, SHA256 `204b6ebdb74767ed2c5f09d58e8c559a08127a9e51c14ed5b43cfb5fba5a2292`, complete15LF including the long rows read raw, now supports global PURE CLIP/all complex containing ranks/affine-only mixed containment/ALL-BRIDGE at the named TC/scalar imports. This is a later gate, not inherited acceptance of new work.

The new low-R proof does NOT require TC, the TC-zero classification or the pending v7 theorem. It uses actual Pauli-sector identities, a directly proved spin-flip bound, actual complex Gram norms, and the same-projector comparison derived below. Original channel composition consumes the existing global analytic U1/U2 imports: ENERGY's X2<=3I+3rho for indices1–5, central U2 for6–10 in `proof-unrestricted-central-indices-v1.md` SHA256 `10e4689c7ac8586fc920651eade6db37fa60be3b693f73b5f4ec7b6644fe6d23`, and trace24 for11–15. These old DAGs are NAMED imports, not newly formal or fully re-audited here.

The scalar noise interface is the supported `depol-quartic-frontier-parent-v1.md`, SHA256 `47e727b0b6a03c4ac693057eec6c174d913c3174e1e3ccf6b0360cd33c8ec7a6`, complete19LF read. This successor supplies its own exact scalar SOS and full operator derivations; no certificate program is imported or replayed.

## 2. Actual Pauli fields and a direct pair-Gram proof

Let rho=|psi><psi|, S_mu the twelve local Paulis, r_mu=<S_mu>, R=r^T r, L=sum r_mu S_mu, E2=<L^2>, V=E2-R^2, delta=4-R. Let J=sigma_y^tensor4, tilde(psi)=J bar(psi), kappa=psi^T J psi and C=|kappa|^2. Write

    G_mu,nu=<S_mu S_nu>, Gamma=G-r r^T,
    Z=sum_mu S_mu rho S_mu, Q=I-rho.

G and Gamma are actual COMPLEX positive Grams. The original maps have

    X1=2I+L/2, X3=2rho+Z/2,
    QX3Q has nonzero spectrum Gamma/2.               (1)

For ANY physical two-qubit marginal its uncentered six-Pauli Gram has block form

    G_pair=[[I+iK1,T],[T^T,I+iK2]],

where K1,K2 are real antisymmetric and T is real. Conjugate by diag(I3,iI3). The transformed G_pair-I is purely imaginary real-antisymmetric, so its entrywise conjugate is2I-G_pair in that basis. Entrywise conjugation preserves positivity. Hence

    0<=G_pair<=2I.                                  (PAIR)

This proves the FULL complex-vector bound without simultaneously rotating any independent physical modes. Centering only subtracts r r^T>=0, so the covariance block is bounded too.

Partition four qubits into two pairs. The full G is positive with both diagonal blocks<=2I. Block Cauchy-Schwarz bounds its quadratic form by2(||x||+||y||)^2<=4(||x||^2+||y||^2). Thus

    G<=4I, Gamma<=4I, Z<=4I                         (2)

for every pure input. No epsilon threshold or scalar-spectrum ansatz enters this proof.

## 3. A genuine full positive difference, not a compression shortcut

Let tildeZ=Z(tilde(rho)). The Pauli-word multiplier of Z is12-4w at weight w. Therefore Z(rho)-Z(tilde(rho)) has multiplier(12-4w)(1-(-1)^w): it is16 at w1 and0 at every other weight0..4. With the actual Pauli normalization this gives the exact operator identity

    Z-tildeZ=L.                                    (3)

For every local S_mu, the spin-flip bilinear J S_mu is antisymmetric. Hence <psi|S_mu tilde(psi)>=0. Every Kraus vector of tildeZ is orthogonal to psi, so tildeZ psi=0. Applying(2) to the actual tilde input gives0<=tildeZ<=4Q as a FULL operator, not an invalid positive-part rule.

Using(1),(3), define D_op=X1-X3. Then

    D_op=2Q-tildeZ/2,
    0<=D_op<=2Q, D_op psi=0.                       (4)

For a mixed density input, test this linear operator inequality against any fixed vector and average the ORIGINAL affine traces. Thus0<=X1(rho)-X3(rho)<=2(I-rho) extends to density inputs too. No covariance, epsilon or quartic is averaged.

A further exact sandwich follows from the spin-flip identity tilde(rho)=I-X1+X2-X3+rho:

    2X1-3I+rho+tilde(rho)<=X2
       <=2X1-I-rho+tilde(rho).                      (5)

These are full actual-state inequalities. They do not by themselves imply the original off-face quartic.

## 4. The ENERGY Gram and a full three-operator decomposition

The supported ENERGY operator A=3I-X2+3rho also has the explicit actual Gram representation

    A=(1/2) sum_(i<j,a,b) S_i^a S_j^b
                           tilde(rho) S_j^b S_i^a. (6)

For completeness, the weight-two Pauli conjugation sum has multipliers54,18,-2,-6,6 at input weights0,1,2,3,4. Applying spin flip and dividing by2 gives27,-9,-1,3,3, exactly the multipliers of3Tr(.)I-X2+3id. This proves(6) by written Pauli algebra and establishes A>=0 without a solver or a historical replay.

Put M=A+tilde(rho). Algebra gives

    M=4I-X1-X3+4rho,
    Z+D_op+M=4I.                                   (7)

All THREE operators in the last identity are PSD: Z is a Kraus Gram, D_op has(4), and M has(6) plus tilde(rho)>=0. Moreover X1>=X3>=2rho by(1),(4), so M<=4I. Thus

    0<=M<=4I.                                      (8)

This is a joint full-operator statement. It is not obtained by adding bounds on unrelated compressions.

Pure one-qubit Schmidt duality gives X3 psi=X1 psi=(2I+L/2)psi. Therefore with v=QLpsi and qtilde=Qtilde(psi),

    Mpsi=delta psi-v,
    Apsi=(delta-C)psi-v-kappa qtilde.               (9)

For delta>0, the true M Schur block gives QMQ>=vv*/delta; M^2<=4M gives delta^2+V<=4delta, hence

    V<=R(4-R).                                     (10)

At delta0 no division is used. The A block separately retains v+kappa qtilde and delta-C. Neither vector is replaced by g, and no V<=constant*epsilon assertion is made.

For the SAME actual rank-k Pi, with zeta=TrPi tilde(rho),

    TrPiA=b-3d>=0,
    TrPiM=b-3d+zeta=a-c-4d.                        (11)

Every complex cross term in(9) remains part of the actual pair, rather than an independently selected scalar energy.

## 5. A full unrestricted-projector theorem when R<=1/5

### 5.1 Spin-flip and purity bounds, with no TC input

At any physical qubit Schmidt-expand psi=sqrt(mu)|0 alpha>+sqrt(nu)|1 beta>. The odd-three-qubit spin-flip matrix on the rest is antisymmetric. The global bilinear amplitude is2sqrt(mu nu) times a unitary bilinear contraction of normalized alpha,beta, whose absolute value is<=1. Thus

    C<=4mu nu=1-t_i^2 for EACH i,
    R+4C<=4.                                      (12)

The actual pure Pauli-sector identity A2=R+2+4C yields

    TrGamma^2=16+4R+8C-2E2+R^2.

Using E2>=R^2 and(12),

    TrGamma^2<=24+2R-R^2<=122/5, R<=1/5.           (13)

This uses the actual same state, not independently maximized unrelated coordinates.

Cauchy-Schwarz for the leading eigenvalues gives

    K2(Gamma)<=sqrt(244/5)<=7-1/70,
    K3(Gamma)<=sqrt(366/5)<=9-13/30.                (14)

For the rational final bounds, 7-sqrt(244/5) equals(1/5)/(7+sqrt(244/5))>=1/70; similarly the squared gap39/5 divided by at most18 gives13/30. Also K1(Gamma)<=4 by(2).

For ANY containing rank-k Pi0, not necessarily a leading one, formula(1) therefore gives

    c0<=-9/10 at k2,
    c0<=-57/140 at k3,
    c0<=-37/60 at k4.                              (15)

For example c0=(R+K_(k-1)(Gamma)-2k-2)/2, so these are the direct rational consequences of R<=1/5 and(14). No global CLIP verdict is silently substituted for the stronger bounds needed here.

### 5.2 Actual off-face comparison at every d

Let Pi have arbitrary missing input weight d. Compare it to the ACTUAL containing Pi0 sharing the orthogonal rank(k-1) part, as in the supported bridge geometry. On psi-perp, QX3Q<=2I by(2), whereas <psi|X3|psi>=2+R/2. Its exact cross vector is v/2. Thus the change in trace is at most

    -(R/2)d+sqrt[d(1-d)V].                         (16)

This is stronger than the older1-R penalty in this low-R region. Maximizing the genuine two-ray quadratic form gives

    h<=(-R+sqrt(R^2+4V))/4
       <=(-R+sqrt(16R-3R^2))/4<=2/5.               (17)

The last inequality follows by squaring nonnegative sides:

    (R+8/5)^2-(16R-3R^2)
       =4[R^2-(16/5)R+16/25]>=0,

because0<=R<=1/5. Equations(10),(16) retain the actual variance and common projector; they are not separate-compression PSD assertions. The d0/d1 endpoints use the usual unnormalized comparison and never normalize a zero vector.

Combining(15),(17), EVERY actual rank-k projector satisfies

    c<=-1/2 at k2,
    c<=-1/140 at k3,
    c<=-13/60 at k4,                               (18)

on the ENTIRE pure R<=1/5 domain. In particular ALL d>0 projectors are covered.

### 5.3 Complete original comparison on this domain

U3 at index1 follows from X3<=4I. At indices2/3/4 it follows from(18); at indices>=5 the product U3 reference has reached the full trace8. Thus X3 is majorized by the product spectrum(4,1 repeated4,0 repeated11) at EVERY index on this whole domain.

The named analytic U1 and global U2 bounds, together with X0=I,X4=rho and common product Hamming order, combine by Ky-Fan subadditivity with nonnegative tensor-channel coefficients for0<=p<=1. Global output spin flip/transpose gives1<=p<=4/3. Therefore the ORIGINAL all-p/all-index comparison follows for EVERY actual pure state satisfying R<=1/5.

Only the specified convex hull of these pure states is included for mixed inputs, by original affine channel traces/Ky-Fan convexity. This is NOT a criterion based on a nonlinear mixed-state value of R, and not a proof for all states with R>1/5. No epsilon cutoff occurs anywhere.

## 6. An independent whole off-face SOS branch a<=9d

For any actual density/projector pair, pure or mixed, retain a,b,c,d and zeta>=0 with

    c=a-b-d-zeta, B=b-3d=TrPiA>=0.

The normalized original low-noise trace gap is nonpositive exactly when q(u)=au^3+bu^2-cu+d>=0, with0<u<1. Direct substitution gives the EXACT identity

    q(u)=(1+u)[d(3u-1)^2+(9d-a)u(1-u)+B*u]
                                  +zeta*u.        (19)

Every term is nonnegative if a<=9d. Hence this ENTIRE actual off-face branch satisfies the original comparison at EVERY0<p<2/3. This is a direct scalar proof for the same mixed pair as well, not averaging D-values.

A stronger sufficient target, NOT proved globally here, is c<=3d: its Bernstein expansion

    q=d(1-u)^3+(3d-c)u(1-u)^2
       +(3d-2c+b)u^2(1-u)+(a+b-c+d)u^3

has nonnegative coefficients using b>=3d and a+b-c+d=2b+2d+zeta. One route to that target would be an uncentered Pauli-Gram theorem Tr(G-2I)_+<=2. This uncentered theorem remains UNPROVED and is not inferred from centered CLIP or from angular-entropy headlines.

## 7. The full common-projector Schur gap remains explicit

For a fixed actual rank(k-1) P orthogonal to psi and eta, put

    H_u=rho+uX3+u^2X2+u^3X1,
    L_k=1+(k+3)u+(3k+3)u^2+(3k+1)u^3.

The whole family Pi=P+|sqrt(1-d)psi+sqrt(d)e^(itheta)eta><...| is governed EXACTLY by the Hermitian two-ray deficit matrix with

    q0=L_k-Tr(P H_u)-<psi|H_u|psi>,
    q1=L_k-Tr(P H_u)-<eta|H_u|eta>,
    w=<eta|H_u|psi>
      =[u(1+u)^2/2]<eta|v>+u^2 kappa<eta|qtilde>.

The condition is q0>=0,q1>=0 and q0*q1>=|w|^2. The two diagonal inequalities, separate coercivity bounds and face support do NOT establish that determinant. Full complex w and the same physical P are required.

From(4), if ell=Tr(P tildeZ)/2, then TrPiD_op=2(k-1)-ell+d<eta|D_op|eta>, so c=ell-a-d<eta|D_op|eta>. In particular c<=2(k-1)-a. Any remaining strict failure after(19) must obey a>9d and a<2(k-1), hence d<2(k-1)/9. These are exact necessary conditions, not an entire-case exclusion.

## 8. Exact NONPHYSICAL obstruction to transferring the k2 full-space certificate

For k3, the natural reference-plus-three-code-copy space has local S4 irreps T=[4],V=[31],W=[22], of dimensions1,3,2 and physical-spin multiplicities5,3,1. Code S3 restriction is V=trivial+standard, W=standard. In a fixed code standard basis x,y and local V basis(t,x,y), the first reference swap is

    R_V=[[-1/3,-2sqrt2/3,0],
         [-2sqrt2/3,1/3,0],[0,0,1]],
    R_W=diag(1,-1).

The other two swaps are code-S3 conjugates. Between CODE-SIGN vectors, the three-term tensor sum therefore has matrix elements THREE times the first tensor product's matrix elements.

Take physical pattern V,V,W,W. Let D^-=(YXX+XYX+XXY-YYY)/2 be the normalized code-sign cubic tensor. Let d1 use D^- on standard sites1,3,4 and trivial site2; let d2 be its V-site swap. One unit vector is u=(d1-d2)/sqrt2. A second unit vector v is the four-standard sign tensor associated with v0=(1,-1,0,0)/sqrt2: its coefficients are(v0)_j/sqrt2 on the one-Y word j and-(v0)_j/sqrt2 on the triple-Y word missing j. These two vectors are orthonormal and have V-swap parity minus, W-swap parity plus.

For C=z+1 and R3(z)=(1+z)^3(1+3z), direct contraction of the displayed local matrices gives the FULL deficit block

    (R3 I-C_(3,z)) on(u,v)
       =zC [[9z+5,4],[4,6z+2]].                    (20)

Its determinant is6z^2 C^3(9z-1), negative for0<z<1/9. On the normalized vector(u-2v)/sqrt5 its expectation is(3/5)zC(11z-1), equal to EXACT-69/4840 at z1/22 (p1/12). All factors were derived in writing, not computed by a scientific interpreter.

This is NOT a physical counterexample. W=[22] is total physical spin0 on the four copies at that site. No nonzero reference-PRODUCT-code vector psi tensor Phi can lie entirely in W: total-spin annihilation would imply(S_i^a psi) tensor Phi+psi tensor(J_code^a Phi)=0 for all three axes; projecting the reference orthogonally to psi would force every S_i^a psi proportional to psi, impossible for three anticommuting Paulis. The witness is reference/code entangled, not an actual input times a Slater code.

Thus the naive stronger FULL-space k3 extension is genuinely FALSE. It neither refutes original k3 nor affects the separately derived k2 v7 certificate. A rank3 proof must retain the actual reference-product/Slater-Plucker constraints or establish a genuine block-positive/decomposable certificate; a sum of pairwise full-space certificates is not enough.

## 9. Current per-index disposition and exact residual

|original index|new regional disposition here|whole-state frontier|
|---|---|---|
|k2|R<=1/5 all-p/all-projector proof; a<=9d low-noise SOS|v7 whole original k2 is separately UNREVIEWED, not inherited here|
|k3|R<=1/5 all-p/all-projector proof; a<=9d low-noise SOS; full joint operator constraints|R>1/5,epsilon>0,a>9d,d>0,c>0 actual quartic still OPEN|
|k4|same unrestricted-projector low-R theorem and SOS branch|same entire physical off-face residual still OPEN|

The epsilon0 full-channel theorem remains separately supported at its own named imports. No positive lower epsilon cutoff is imposed on the strict-positive residual. Original mixed failures reduce to pure failures only through original affine traces, not nonlinear averaging of these state inequalities.

**First unproved step:** prove the common-P determinant, or the equivalent original quartic, for EVERY remaining physical k3/k4 pair, or supply an actual state/projector/noise failure. Positive D_op/M/Schur/CLIP constraints separately are not the determinant proof. The exact enlarged-space negative block is explicitly NONPHYSICAL.

## 10. Attribution and execution boundaries

Zhang's matched complementary clipping/public uniform-weight claim remains binding through `source-audit-v2-zhang-prior-claim.md`, SHA256 `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`. No clean novelty/priority clearance. The refreshed Song–Wang–Tomamichel–Fang [arXiv:2609.37240v1](https://arxiv.org/abs/2609.37240v1) is the already-inventoried exact general conjecture/approximate-majorization baseline, not a new discovery or a proof of the missing exact indices. [Wyderka–Guhne arXiv:1905.06928v3](https://arxiv.org/abs/1905.06928v3), Proposition3/AppendixA, explicitly proves the uncentered star-correlation principle; v6 re-derived it as a classical tool and made no new-mechanism claim. Those primary-source refreshes do not certify publication priority.

Every new result is WRITTEN at the exact stated analytic imports, requiring its own frozen review. No formal/kernel/human/configured-family/cross-vendor/executable/novelty acceptance is claimed. No scientific eval/interpreter/program, enumeration, symbolic calculator, replay/sampling/solver/compile, CLI, nested agent, Git/publication/config/deletion or GO occurred. Only static sources, metadata clocks/hashes and owned-root outputs. Earlier unadmitted computations remain preserved with ZERO verification credit and were not rerun.

All v9/v10/v11/HOLD qualifications and immutable source histories remain. H*=H; TT* and complex fields are not deleted or realified. Original science cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38 remain. This is a genuine regional/off-face continuation, NOT a whole original k3/k4 solution, a park or96-hour closeout.
