# Actual original low-noise continuation v12 — whole paired-parity majorization and a strict-positive-epsilon W-family certificate

## 0. Exact status, chronology and unchanged original task

**NEW COMPLETE AUTHOR-WRITTEN CANDIDATE.** Two actual-state subtheorems are proved here: FULL original all-index/all-physical-p majorization on the entire paired-parity code family, including arbitrary complex/mixed inputs; and original k3 on the entire symmetric vacuum-plus-W4 family, whose nonproduct members have STRICT positive TC epsilon and positive SP defect with no cutoff. The original unrestricted arbitrary-state k3 task remains OPEN outside the stated families/regions. Neither this packet nor a new review gate is a park or completion of that original ticket.

Actual `/bin/date` immediately before this body: **Sun Oct25 20:40:31 PDT2026**. The complete467LF v108-B review, SHA256 `25e69d4ce7699a1ff279bfb41158a5ffbcb29d0c8656d17a28ce05bf9061c3d3`, was ACTUALLY RETURNED to Main before the separate `primary-post-v108-resumption-exposure-ack-v1.json`, actual20:30:42. The new flagged-channel theorem and all fresh primary reasoning here follow THAT ACK. Checkpoint057, actual20:37:32, saved the complete flagged-channel/block proof and the already exposed W/incidence representation. The epsilon identity below was derived later, not backdated into057.

Permanent BOTH cadence findings, historical PRIVATE WRITTEN approximate-scoping disclosure SHA256 `5b49e61483a80113eefc4a18047c7876676916fe631caaa923a46c7f783b4329` with ZERO verification/proof credit and global clean-exact-history implication withdrawn, v104 primary-pause PROCESS MAJOR SHA256 `44fb09bb6d4fb5be9c19631313e552ae4a3f155b59f15d7a52c11fa2fff3087e`, v106 inventory correction and v11 generator-wording qualification remain. All parent v9/v10/v11/v101/root/freeze/clock/cadence068 and peer histories remain; correct new symbolic work does not cure them, backdate earlier SP refinements or establish a clean thought/runtime/cadence census.

This packet is **EXACT WRITTEN/static-source/metadata ONLY**, no scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent or GO. The dead interpreter was not restarted. No historical approximate scout was replayed or back-converted into evidence; all claims are derived in symbolic variables below. No author/shared/pinned edit, deletion, Git or publication. Same eighteen owners, exclusive root, October27 science cutoff11:05:38/deadline12:35:38 and30-minute substantive checkpoints, no new slot/deadline reset/park.

Zhang attribution stays explicit: `source-audit-v2-zhang-prior-claim.md`, SHA256 `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`, records matched complementary-clipping overlap and ambiguous exact support/certificate. There is no clean novelty/priority/first claim. The public BW/DDVV/Lu-Wenzel material read in bounded windows is NOT a mathematical premise of this packet; no unproved global commutator inequality is imported.

## 1. Original conventions and the TWO complete conclusions

Let D_p(A)=(1-p)A+(p/2)Tr(A)I on a qubit, with the physical p interval[0,4/3]. For a four-qubit density rho put

    X_j(rho)=sum_(|I|=j) rho_I tensor I_(I-complement),

using UNNORMALIZED identities. Let sigma_prod=|0000><0000|. The original statement at index k is

    K_k(D_p^(tensor4)(rho))
       <=K_k(D_p^(tensor4)(sigma_prod)).                 (ORIG-k)

K_k is the supremum over ALL complex orthogonal rank-k projectors, not a containing/real code.

### Theorem PP — FULL all-index original majorization on the ACTUAL paired-parity family

Let C12=span{|00>,|11>} on sites12 and C34 the same on34. For EVERY density rho supported on C12 tensor C34, EVERY physical p in[0,4/3], and EVERY k1..16,

    lambda(D_p^(tensor4)(rho))
       is majorized by lambda(D_p^(tensor4)(sigma_prod)). (PP)

In particular this covers arbitrary complex normalized a|0000>+b|0011>+c|1100>+d|1111>, not just one phase relation or the earlier SP-equality normal form. ALL mixed densities on that physical four-dimensional code are included directly. Local single-qubit unitary/permutation images and their specified convex hull are included by channel covariance/ORIGINAL fixed-projector affine traces. This is not an assertion that every four-qubit pure state is LU-equivalent to such a code state.

### Theorem W — original k3 on the ENTIRE actual vacuum-plus-W4 family

Let

    |W4>=(|1000>+|0100>+|0010>+|0001>)/2,
    psi_s=sqrt(1-s)|0000>+sqrt(s)|W4>,  0<=s<=1.

Then K3(X3(|psi_s><psi_s|))<=6 for EVERY s, hence(ORIG-3) for every physical p and every complex rank-three projector. Its local-unitary/permutation images and specified affine convex hull are included. For EVERY0<s<=1 the exact invariants are

    C=0, R=4-3s^2, eta_SP=3s^2/4>0, epsilon_TC=3s^3>0.  (W-inv)

Thus this is an actual strict-positive-epsilon/positive-SP-defect branch, allowing arbitrarily small positive epsilon, not just continuity at an equality locus or a compact region above an imposed epsilon cutoff.

Both are genuine SUBTHEOREMS. Full original k3 outside them and the separately stated v10/v11/older regions remains OPEN. Whole original k2 with mandatory M1 and whole original k4 keep their separate supported scopes, not an automatic all-index unrestricted composition.

## 2. Actual pair-channel restriction: an exact orthogonally flagged logical qubit

For0<=p<=1 set

    t=1-p in[0,1], alpha=(1+t)/2, beta=(1-t)/2,
    e=alpha beta=(1-t^2)/4,
    w=alpha^2+beta^2=(1+t^2)/2,
    r=t/w=2t/(1+t^2) in[0,1].                           (2.1)

Here w>=1/2, so no denominator vanishes. The last bound follows from(1-t)^2>=0, not a numerical test.

Encode a logical qubit by |0_L>=|00>, |1_L>=|11>. Direct application of D_p to the four logical matrix units gives:

- |0_L><0_L| maps to diagonal alpha^2 on00, beta^2 on11, and e on EACH01/10.
- |1_L><1_L| maps to beta^2 on00, alpha^2 on11, and e on EACH01/10.
- |0_L><1_L| maps to t^2|00><11|; its adjoint similarly. No coherence to an external flag is created.

Therefore on ANY logical matrix A, including off-diagonal pieces of a bipartite density, the actual pair channel E has the EXACT direct sum

    E(A)=w T(A) in the code C,
           directsum e Tr(A) on flag |01>,
           directsum e Tr(A) on flag |10>.              (2.2)

The normalized logical code channel T is trace-preserving/unital with Bloch multipliers

    (t^2/w,t^2/w,t/w)=(r t,r t,r).

Let Delta_t be the logical dephasing map, multiplying off-diagonals by t and fixing the computational diagonal. It is CPTP because

    Delta_t=((1+t)/2)Id+((1-t)/2)(Z . Z).

Let P_r be the logical depolarizing channel of Bloch multiplier r. Then

    T=P_r composed with Delta_t.                       (2.3)

This is an ACTUAL channel identity on all matrix units, not a scalar spectrum or a guessed independent-marginal replacement. Delta_t fixes logical |0><0|, so the same logical reference is optimal for the bounds below.

## 3. Complete two-logical-qubit depolarizing majorization proof, no imported theorem

We need the following standard-sized fact, proved here rather than imported: for ANY two-qubit density omega and r in[0,1],

    (P_r tensor P_r)(omega)
       is majorized by P_r(|0><0|) tensor P_r(|0><0|).   (3.1)

By fixed-projector Ky Fan convexity it suffices to take omega pure. P_r is covariant under arbitrary qubit unitaries, so Schmidt form is legitimate here:

    sqrt(theta)|00>+sqrt(1-theta)|11>, 0<=theta<=1.

Put a_r=(1+r)/2,b_r=(1-r)/2 and v=(1-r^2)/4=a_r b_r. The two isolated01/10 eigenvalues of the actual output equal v. The00/11 block has trace(1+r^2)/2, diagonal difference r(2theta-1), and off-diagonal r^2 sqrt(theta(1-theta)). Its eigenvalues are EXACTLY

    eta_+-=[1+r^2 +- 2r sqrt(1-4(1-r^2)theta(1-theta))]/4. (3.2)

Because0<=theta(1-theta)<=1/4, the radical lies between r and1. Hence eta_+>=v>=eta_-, including every endpoint, and

    eta_+<=a_r^2, eta_->=b_r^2.

The complete descending spectrum is eta_+,v,v,eta_-. Its first prefix is <=a_r^2; its second <=a_r^2+a_r b_r=a_r; its third is1-eta_-<=1-b_r^2; trace is1. These are exactly all nontrivial reference prefixes. This proves(3.1) for pure inputs, and averaging the ORIGINAL channel/fixed-projector traces proves it for arbitrary mixed omega. No finite scan, decimal eigenvalue estimate, code or CAS is used.

For a SINGLE logical qubit the corresponding statement is immediate: P_r Delta_t maps any Bloch vector of length<=1 to one of length<=r, because its largest multiplier is r. Thus

    T(omega_A) is majorized by P_r(|0><0|).             (3.3)

Crucially, the input to(3.1) in our application is the ACTUAL positive mixed density(Delta_t tensor Delta_t)(omega). We do not pretend that arbitrary different code/flag marginals are a common pure state; they are the actual marginals of this same omega in(2.2).

## 4. The whole16-dimensional block assembly proves(PP)

Apply the exact operator identity(2.2) to BOTH physical pairs of the same logical two-qubit density omega. The actual output has these orthogonal blocks:

|Actual flag sector|Dimension/multiplicity|Actual output block|
|---|---|---|
|code-code|4, once|w^2(T tensor T)(omega)|
|code-flag|2, TWO flags|w e T(omega_A) in EACH|
|flag-code|2, TWO flags|w e T(omega_B) in EACH|
|flag-flag|1, FOUR flags|e^2 in EACH|

There is no cross-flag coherence. The dimensions are4+4+4+4=16 and the trace is(w+2e)^2=1. This is a full actual output, not independent per-mode upper bounds pieced into a presumed physical spectrum.

Let tau=P_r(|0><0|). Equations(2.3),(3.1) give

    (T tensor T)(omega)
       =(P_r tensor P_r)((Delta_t tensor Delta_t)(omega))
       is majorized by tau tensor tau.

The code-flag and flag-code blocks are majorized by w e tau by(3.3); scalar blocks are identical. For the ACTUAL reference omega=|00><00|, the output has EXACTLY these reference blocks: w^2 tau tensor tau, four w e tau blocks, and four e^2 scalars. Indeed w tau has entries

    (w+t)/2=alpha^2, (w-t)/2=beta^2,

so adding the two flags e,e reproduces the actual pair product output, not a different surrogate reference.

Blockwise scaled majorization implies majorization of the full direct sum. Explicitly, for any k its Ky Fan sum is the maximum, over allocations k_j among the orthogonal blocks with sum k_j=k, of the sum of the block K_(k_j). Every actual block prefix is bounded by the corresponding reference prefix. Taking the SAME allocation then maximizing gives the full reference K_k. Trace equality holds. This proves(PP) for EVERY index1..16 and ALL complex projectors, including every off-face choice.

At p0,t1, e0: zero-weight flag blocks cause no problem and a pure reference majorizes every input. At p1,t0,r0: both physical pairs are completely mixed and output is I16/16. No division by e or t occurs in the proof.

For1<p<=4/3, put q=2-p in[2/3,1). Full spin flip multiplies every Pauli string of weight j by(-1)^j. Hence

    D_p^(tensor4)(rho)=Theta D_q^(tensor4)(rho) Theta^(-1).

Antiunitary conjugation preserves the entire spectrum, including the product reference. Thus(PP) holds on the whole physical interval. The input is the SAME original rho; no new compatibility assumption is made.

Logical omega was arbitrary mixed from the start. Physical local single-qubit unitary/permutation images retain(PP) because the original identical depolarizing channels are covariant under those transformations and the product reference spectrum is unchanged. Finally their specified convex hull is included by averaging the ORIGINAL fixed-Pi/p channel traces. No assertion that all states belong to that hull is made; pure states outside the union do not become covered by silently mixing them.

## 5. Optional matching actual Z certificate on the same support class

This independent check illustrates why the earlier SP-equality restriction was unnecessary for the whole paired-parity family, while preserving the distinction from a global complex-SVD shortcut.

In a pair magic basis e1=(00+11)/sqrt2,e2=i(00-11)/sqrt2,e3=i(01+10)/sqrt2,e4=(01-10)/sqrt2, the paired-parity code is the REAL coordinate plane span(e1,e2) over complex amplitudes. Write psi=vecX with an arbitrary complex2-by2 coefficient block X and zeros elsewhere, ||X||_F=1. The six pair-local Pauli generators are a real orthogonal frame change of sqrt2 i(E_ij-E_ji); using this ENTIRE frame preserves the actual Z=sum S_mu rho S_mu.

The left/right12 generators give TWO actual core columns in the four-dimensional support, each of norm squared2. Their normalized overlap c has |c|<=1 by Cauchy–Schwarz. Their sum of outer products therefore has core eigenvalues2+2|c| and2-2|c|, plus TWO zeros.

The two external rows each give the positive matrix2X^dagger X, and the two external columns each give2XX^dagger. If p_+>=p_- are the actual Schmidt eigenvalues of X, p_++p_-=1, the external eigenvalues are2p_+,2p_-, EACH multiplicity FOUR. The external-row/external-column-both space contributes FOUR more zeros. These mutually orthogonal supports give the COMPLETE spectrum

    2+-2|c|;  2p_+ four times; 2p_- four times; SIX zeros. (5.1)

It has trace12, at most ONE eigenvalue above2, and maximum<=4. Thus K_j(Z)<=4+2(j-1)=2j+2 for j1..5, and all higher prefixes are at most total12. Hence on THIS ACTUAL support class

    lambda(Z) is majorized by(4,2,2,2,2,0,...,0).

Ky Fan subadditivity in X3=2rho+Z/2 gives the entire product U3 envelope(4,1,1,1,1,0,...,0). This is a proper majorization certificate on a genuine common state. It does NOT prove that envelope for arbitrary four-qubit states or authorize lambda2(Z)<=2 globally; v11's general critical-state three-edge modes need not have that latter property. No arbitrary complex SVD is treated as a covariance symmetry. The actual flag-channel proof already established every original p/index independently of this optional spectrum argument.

## 6. A NEW representation for the actual general W-class branch

The following exact representation is supplied both to prove Theorem W and to isolate a remaining genuinely coupled branch. For ANY actual

    psi=a|0000>+sum_(i1..4) x_i|1_i>,
    a,x_i>=0, a^2+s=1, s=sum x_i^2,

the phases can be removed by legitimate physical single-site Z rotations/global phase. Define x=(x_i), D=diag(x_i^2), and the4-by6 weighted incidence matrix on unordered pairs by

    M_(i,{i,j})=x_j, M_(j,{i,j})=x_i, other entries0.

On vacuum/one-excitation/two-excitation subspaces the EXACT X3 matrix is

    [ 1+3a^2          3a x^T                    0    ]
    [ 3a x      a^2 I+2D+2xx^T                 a M   ]
    [ 0                a M^T                  M^T M ].  (6.1)

All weight3/4 states give FIVE additional zeros. To derive every entry: vacuum diagonal is sum_i(a^2+x_i^2)=4a^2+s; one-excitation j diagonal is a^2+4x_j^2 and distinct j,k entry2x_jx_k; pair ij diagonal x_i^2+x_j^2 and pairs ij/ik sharing i have entryx_jx_k; vacuum-to-j is3a x_j; j-to-jk is a x_k; all other blocks vanish by the traced-site identity. Thus(6.1) retains the actual simultaneous coupling, not an eigenvalue profile assumed realizable.

The SAME matrix satisfies

    MM^T=K=sI-2D+xx^T,
    a^2 I+2D+2xx^T=I+3xx^T-K.

Therefore X3=3rho+B, where B has vacuum entry1 and V/edge block

    [ I-K     aM   ]
    [ aM^T   M^T M ].                                   (6.2)

For NONUNIFORM x, K-sI=xx^T-2D has at most one positive eigenvalue. In singular modes of M the B block is[[1-k,a sqrtk],[a sqrtk,k]], trace1, determinant k(s-k); so there is at most one B eigenvalue above1. Adding the actual rank-one3rho yields at most TWO X3 eigenvalues above1. This is a NEW actual coupled representation, not yet a full proof of the sharp trace-excess bound for every nonuniform x.

**Explicit remaining subgap:** Tr(X3-I)_+<=3 would finish this general W class; the rank-one coupling to the ACTUAL x in(6.1) is still missing. Dropping it or independently choosing its singular modes is not a proof. This general nonuniform branch is not included in Theorem W merely because its necessary index/eigenvalue structure is simple.

## 7. COMPLETE symmetric vacuum-plus-W4 proof, no enlarged-copy positivity

For x_i=sqrt(s)/2, use the fixed unweighted4-by6 vertex-edge incidence matrix B0, whose BB^T has diagonal3 and off-diagonal1, namely2I+J. Its trivial singular value is sqrt6 and its three sum-zero singular values are sqrt2; its two-dimensional edge kernel is exact. This is a physical Hamming-subspace decomposition, NOT an enlarged reference/code S4 certificate or the old unphysical negative-copy control.

Split the four one-excitation coordinates into their constant line and sum-zero3-space. Split the six edges into the image of B0^T and its2-dimensional kernel. The actual X3 from(6.1) has one THREE-dimensional block in normalized vacuum/W1/W2 basis:

    A_s=[ 4-3s       3sqrt(s(1-s))                0             ]
        [ 3sqrt(s(1-s))  1+3s/2          sqrt(3s(1-s)/2)       ]
        [ 0           sqrt(3s(1-s)/2)          3s/2            ]. (7.1)

It has trace EXACTLY5. The three standard directions each give the SAME two-dimensional block

    B_s=[ 1-s/2          sqrt(s(1-s)/2) ]
        [ sqrt(s(1-s)/2)      s/2      ],                 (7.2)

with eigenvalues[1+-sqrt(1-s^2)]/2 in[0,1]. The edge kernel contributes TWO zeros; weight3/4 contributes FIVE. Dimensions3+3*2+2+5=16 and traces5+3=8, as required for ORIGINAL X3. All bases can be fixed independently of s, so s0/s1 introduce no normalization of a zero vector.

Every eigenvalue of A_s is nonnegative because X3 is positive. Also universally X3=sum_i rho_(bar i) tensor I_i<=4I, because each marginal density is a contraction. Thus every A_s eigenvalue is<=4. Now EVERY possible top-three selection is controlled:

- three from A_s: sum<=Tr A_s=5;
- two from A_s plus one standard: sum<=5+1=6;
- one from A_s plus two standard: sum<=4+2=6;
- no A_s: sum<=3; zero modes cannot increase it.

This proves FULL K3(X3)<=6 for every s and every complex rank-three projector, not just the containing face. No cubic eigenvalue solving, computational enumeration, decimal trial, external theorem or positive-compression shortcut was used.

## 8. Exact actual epsilon/SP controls — STRICT positive states, no cutoff

For psi_s put a=sqrt(1-s),b=sqrt(s). Each local Bloch vector is(a b,0,1-s/2), so

    t_i^2=1-3s^2/4, R=4-3s^2.

Full spin flip maps the support of psi_s at weights0/1 into weights4/3, orthogonally, hence C=0. With eta_SP=t4^2-(R/2-1+C), this gives eta_SP=3s^2/4.

For the TC expression let L=sum_i(r_x X_i+r_z Z_i), r_x=a b,r_z=1-s/2. The ACTUAL simultaneous state expectations are

    <(sum X_i)^2>=4+6s,
    <(sum Z_i)^2>=16-12s,
    <{sum X_i,sum Z_i}>=24 a b.

The first follows from <X_iX_j>=s/2 for i!=j; the second from vacuum/one-excitation Z totals4/2; the third from the actual vacuum/W coherence and those two Z eigenvalues. Written expansion gives

    E2=<L^2>
       =s(1-s)(4+6s)+(1-s/2)^2(16-12s)
                              +24s(1-s)(1-s/2)
       =16-18s^2+3s^3.

Therefore the ORIGINAL TC quantity is

    epsilon=E2-6R+8-4C=3s^3.

Every0<s<=1 has epsilon>0 and eta_SP>0. There is no imposed lower cutoff; arbitrarily small positive s remains covered by the actual block proof. These invariants are controls identifying the theorem's actual scope, NOT premises replacing the state or an imported TC inequality. They are exact written identities, not machine-checked arithmetic, an approximate scout, a recovered historical verification or a conjecture counterexample.

## 9. Original all-p k3 consequence for Theorem W and precise affine hull

For any rank-three Pi and any density input the universal ORIGINAL bounds are

    Tr Pi rho<=1, Tr Pi X1<=10, Tr Pi X2<=12.

X1 is a sum of commuting lifted one-qubit marginals; Ky Fan convexity in the four independent marginals reduces to pure ones, with top eigenvalues4/3/3. The full positive identity

    3I-X2+3rho=(1/2)sum_(weight(P)=2) P tilde(rho) P>=0

implies Tr Pi X2<=9+3Tr Pi rho<=12. Its Pauli weight multipliers after the density's factor1/16 are(27,-9,-1,3,3), so no normalization/partial-transpose positivity is assumed.

For p<1, z=p/[2(1-p)]>=0,

    D_p^(tensor4)(rho)
       =(1-p)^4[rho+zX3+z^2X2+z^3X1+z^4I].

The FULL Theorem W K3(X3)<=6 bounds the actual trace by

    (1-p)^4[1+6z+12z^2+10z^3+3z^4]
       =(1-p)^4(1+z)^3(1+3z),

exactly the product-reference top-three sum. p0/p1 are direct and p>1 is the same full-spinflip spectral reflection proved in Section4. Fixing the SAME original Pi,p and averaging ORIGINAL affine traces proves the specified mixed convex hull, not nonlinear averaging of R/C/epsilon/SP moments. No blanket quartic discriminant D>=0 is claimed; the separate mandatory k2 branch qualification stays intact.

## 10. Exact input/trust scope and genuinely unresolved original frontier

Both new theorems are written from actual matrix units, positive channel/dephasing decompositions, the explicitly proved two-qubit depolarizing prefixes, direct-sum Ky Fan allocation, actual weighted incidence and elementary spectral facts. No global DDVV/Lu-Wenzel/starcommutator, generic complex SVD covariance, independently chosen marginal/spectrum mode, epsilon/g coercion, g=QLpsi identification, missing complex cross term, enlarged-copy positivity or finite-program result is an input.

The new all-index paired-parity result strictly removes the earlier four-amplitude phase/normal-form restriction INSIDE that actual support family. The strict-positive-epsilon W proof controls a different C0/positive-SP branch and exposes a new general W rank-one incidence interface. These are substantive new representations, not another inconsequential enumeration or restated limitation. They remain exactly SUBFAMILIES; no claim that the original global gap is a surviving scalar case automatically excluded by them.

The whole v10 SP-equality325LF packet and v11 critical-spectrum/high-C264LF packet with its mandatory HERMITIAN/skew-TRANSPOSE terminology addendum remain separate complete candidates unless their actual new parent dispositions are read. This packet does not inherit or backdate acceptance from those versions. A proposed union of their regions/families requires its OWN exact joint input scope; branch reviews alone do not accept an unrestricted all-state theorem.

**Original residual:** arbitrary actual four-qubit states outside the specified paired-parity/LU hull, symmetric W hull and other separately supported/proposed regions, with arbitrary complex off-face rank-three projectors, original affine traces and NO positive cutoff. General NONUNIFORM W incidence trace-excess coupling is still open. The stronger GLOBAL uncentered Z majorization or global half-trace covariance bound remains UNPROVED outside established loci and is not silently imported. The full actual common-P quartic remains an alternative unresolved route. No exact original counterexample or all-state k3 certificate has been delivered.

All original world-priority/source/process/assurance limits remain. This complete packet requires its own ENTIRE source-level reconstruction/current disposition; it is not formal/kernel/human/configured-family/executable/novelty clearance. Original active research continues after this checkpoint, with no park/closeout, same owners/HOLD/cutoff/deadline, and all permanent history preserved.
