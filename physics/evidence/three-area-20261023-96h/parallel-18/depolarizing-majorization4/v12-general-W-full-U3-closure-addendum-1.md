# Additive v12 closure — ENTIRE nonuniform vacuum-plus-single-excitation family, full U3 majorization

## 0. New theorem, not an in-place correction or global closure

Owner PhysicsDepol4-2. Actual `/bin/date` immediately before this body: **Sun Oct25 20:57:02 PDT2026**. **NEW COMPLETE AUTHOR-WRITTEN CANDIDATE, not accepted.** This addendum PROSPECTIVELY closes the NONUNIFORM-W matrix gap that was honestly open at the original v12 pin. It does not edit/relabel that historical source or backdate this proof into its earlier gate.

Original v12 is `depolarizing-paired-parity-full-majorization-and-W-incidence-v12.md`,291LF, SHA256 `779898344765088b2be8c291ae844a923c260320b2a22b43440a30076c4e16e7`. Its optional external-row transpose addendum, SHA256 `c1ca10e981e393bcbe5f94538bc3c3e678424c04fc7c44cf46af6af4bf53b94c`, remains mandatory when consuming that WHOLE source: the actual optional row matrix is2(X^dagger X)^T, with the same eigenvalues. No step of the NEW W proof uses that optional block, the flagged-code theorem or a prior verdict.

The complete v108-B review was ACTUALLY returned before the separate20:30:42 primary ACK. This entire new proof follows that ACK; checkpoint058, actual20:55:17, records its central spectral argument. BOTH cadence findings/private-WRITTEN-approximation ZERO-credit/global clean-exact-history withdrawal/v104 primary-pause MAJOR/v106 inventory/v11 wording/v12 optional orientation and ALL parent v9/v10/v11/v101/root/freeze/clock/cadence068/peer histories remain. There is no process cure, invented timing/private-thought count, blind/family or clean-runtime census.

Strict exact WRITTEN/static-source/metadata only; no scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/GO or historical approximate replay. Same18/own root/HOLD/October27 cutoff11:05:38/deadline12:35:38/30-minute substantive cadence; no pinned/shared edits, Git, deletion, publication, new slot or park. Zhang's matched complementary-clipping attribution and unclear priority remain explicit through the original source-audit note. This actual-state clipping construction is not itself worldwide novelty clearance.

## 1. Exact complete theorem and actual mixed scope

Let rho=|psi><psi|, where the ACTUAL four-qubit pure state is

    psi=a|0000>+sum_(i1..4) x_i |1_i>,
    |a|^2+sum_i |x_i|^2=1,

with arbitrary COMPLEX coefficients. Define ORIGINAL X3=sum_i rho_(bar i) tensor I_i with UNNORMALIZED identities. Then

    lambda(X3(rho)) is majorized by
                   (4,1,1,1,1,0,...,0).                   (W-FULL)

This gives EVERY U3 prefix, not only a containing or real rank-three code. In particular K3(X3)<=6 for ALL complex rank-three projectors. The ORIGINAL four-qubit depolarizing k3 comparison holds for every physical p in[0,4/3], with NO positive epsilon/SP/noise cutoff.

By ORIGINAL affine traces the U3 theorem and original k3 statement extend to EVERY mixed density supported on the FIVE-dimensional physical vacuum-plus-single-excitation code, all physical local-unitary/permutation images, and their specified convex hull. There is no assumption that arbitrary mixed-state invariants characterize this hull, and no assertion that every four-qubit pure state belongs to it. This is a genuine whole family, still not the unrestricted original task.

## 2. Re-derivation of the FULL actual matrix, all couplings retained

An overall phase and physical single-qubit Z rotations make a,x_i>=0 without changing the channel/reference spectra. Put s=sum x_i^2, a^2=1-s, x=(x_i), D=diag(x_i^2). Let M be the4-by6 weighted incidence matrix on unordered pairs:

    M_(i,{i,j})=x_j, M_(j,{i,j})=x_i, other entries0.

In vacuum /one-excitation /two-excitation subspaces the EXACT X3 is

    [ 1+3a^2            3a x^T                   0    ]
    [ 3a x        a^2 I+2D+2xx^T                a M   ]
    [ 0                  a M^T                 M^T M ]. (2.1)

The weight3/4 space contributes FIVE zeros. Here are the actual entry derivations, rather than an assumed allowed matrix profile:

- vacuum diagonal: sum_i(a^2+x_i^2)=4a^2+s=1+3a^2;
- one-excitation j diagonal: a^2+4x_j^2; distinct j,k entry2x_jx_k;
- pair ij diagonal: x_i^2+x_j^2; pairs ij/ik entryx_jx_k; disjoint-pair entry0;
- vacuum-to-j:3a x_j; j-to-jk:a x_k; other nonlisted entries0.

They follow by whether the traced-site identity has equal bit values in the two actual basis vectors. All resulting cross terms are in(2.1); no independent modes/projector directions are substituted.

The SAME M has

    K=MM^T=sI-2D+xx^T>=0.

Since a^2 I+2D+2xx^T=I+3xx^T-K, the actual state vector(a,x,0) gives

    X3=3rho+B,

where B is1 on vacuum, zero on the five higher-weight states, and on one-/two-excitation spaces is

    B=[ I-K     a M   ]
      [ a M^T   M^T M ].                                (2.2)

Extra edge-kernel modes are zero. This is an identity on the ACTUAL sixteen-dimensional space, not a compression to a hypothetical physical subspace.

## 3. At most ONE bad singular mode, with an EXACT trace-one pair

Use an ordinary mathematical singular-value basis for M to analyze the already derived full Hermitian matrix(2.2). This is not a claimed physical covariance transformation. Every squared singular value k>=0 supplies the exact block

    B_k=[ 1-k      a sqrtk ]
        [ a sqrtk      k  ],
    Tr B_k=1, det B_k=k(s-k).                            (3.1)

Zero singular values and all extra kernels are included by completing the basis; they give eigenvalues1/0, never an omitted mode. The actual K satisfies

    K-sI=xx^T-2D.

It is nonpositive on x-perpendicular, so it has at most ONE strictly positive eigenvalue. Therefore at most ONE squared singular value k exceeds s.

If0<=k<=s, the determinant and trace in(3.1) imply BOTH eigenvalues lie in[0,1]. If k>s, its determinant is negative and the TWO eigenvalues are exactly

    1+e, -e,   e>0,                                    (3.2)

because their sum is1. We do not need to solve for e, estimate its eigenvector alignment with x, or independently choose a bad mode. The entire B has at most ONE negative eigenvalue and at most ONE eigenvalue above1, and they are the SAME actual trace-one block.

This is the missing coupled representation. It is stronger than separately knowing a negative index or the norm bound, and it uses the full nonuniform matrix, not physical S4 symmetry or the old unphysical enlarged-copy control.

## 4. The valid full-operator clamp, negative-index balance and ALL U3 prefixes

If no k>s exists, B<=I and

    X3=B+3rho<=I+3rho.

Hence K_j(X3)<=j+3. Together with Tr X3=8 this proves(W-FULL).

Suppose the actual bad block exists. Let u_+,u_- be its normalized eigenvectors with eigenvalues1+e,-e. Define B_up by KEEPING BOTH of those actual eigenvalues/eigenvectors and replacing EVERY OTHER B eigenvalue in[0,1] by1. This explicit spectral replacement satisfies

    B_up-B>=0.

It is NOT the generally false rule that positive-part functions preserve arbitrary Loewner inequalities. It is a directly constructed PSD difference in ONE fixed spectral basis.

Now set

    Y=B_up+3rho>=X3>=0,
    F=Y-I=e|u_+><u_+|-(1+e)|u_-><u_-|+3rho.             (4.1)

The full Y is positive because it dominates the ACTUAL positive X3. Therefore every eigenvalue of F is at least-1. Its negative index is at most ONE: the first two terms have only one negative direction, and adding positive3rho cannot increase that index. Its trace is EXACTLY

    Tr F=e-(1+e)+3=2.

Consequently

    Tr F_-<=1,
    Tr F_+=Tr F+Tr F_-<=3.                              (4.2)

Here F_+ and F_- are spectral positive/negative parts used ONLY in a trace/eigenvalue identity; no invalid operator-positive-part monotonicity is used. Keeping only the positive contributions bounds EVERY Ky Fan sum K_j(F)<=Tr F_+<=3. Valid Loewner eigenvalue monotonicity X3<=Y then gives

    K_j(X3)<=K_j(Y)=j+K_j(F)<=j+3.                     (4.3)

The positive trace of X3 is8. For j1..5,(4.3) is exactly4,5,6,7,8, the prefixes of the product U3 spectrum; for j>=5, positivity gives K_j<=8. Trace equality holds at16. This proves the WHOLE majorization(W-FULL) for all nonuniform coefficients and ALL complex projectors, including every off-face choice.

The proof uses the actual positivity of X3 and keeps the negative bad partner. Dropping that partner or normalizing a missing eigenvector would destroy the trace balance. No cutoff, numerical diagonalization, cubic solving, independent eigenvalue relaxation or extra orthogonality assumption occurs.

## 5. ALL original physical-p k3 comparisons and the actual mixed hull

For any rank-three Pi and any density input,

    Tr Pi rho<=1, Tr Pi X1<=10, Tr Pi X2<=12.

For X1 the maximum over independent one-qubit marginals occurs at pure marginals by Ky Fan convexity, with top three eigenvalues4,3,3. For X2 the full-spin-flip identity

    3I-X2+3rho=(1/2)sum_(weight(P)=2)P tilde(rho) P>=0

gives the stated bound. This is the positive global spin flip, not partial transpose. All weight/identity normalizations are those of ORIGINAL X_j.

For0<=p<1 put z=p/[2(1-p)]>=0. The original expansion is

    D_p^(tensor4)(rho)
       =(1-p)^4[rho+zX3+z^2X2+z^3X1+z^4I].

The FULL actual W-family K3(X3)<=6 yields

    Tr Pi D_p^(tensor4)(rho)
       <=(1-p)^4[1+6z+12z^2+10z^3+3z^4]
       =(1-p)^4(1+z)^3(1+3z),

exactly the product-reference top-three sum. p1 gives I16/16. For1<p<=4/3 use q=2-p and full spin flip: the p/q outputs and references are antiunitarily conjugate and have identical entire spectra. No zero denominator is normalized or state compatibility changed.

The pure coefficient phases were removed only by legitimate local unitaries, to which the original identical depolarizing channels are covariant. Every pure state of the five-dimensional code is of the proved form. A mixed state supported there has an actual positive spectral decomposition into such pure states; averaging ORIGINAL fixed-Pi/p affine X_j and channel traces proves the mixed statement. The same applies to local-unitary/permutation images and their specified convex hull. No nonlinear condition on a mixed state's R/C/epsilon supplies a fictitious decomposition.

Theorem(W-FULL) is itself ALL-index U3 majorization. An all-index ORIGINAL channel composition with other coefficient theorems requires the exact named import union; this addendum claims the explicit original k3 statement above, not a silently widened all-state/all-index result. The separate paired-parity Theorem PP in v12 already has its own direct complete all-index channel proof.

## 6. General exact epsilon/SP invariants: a whole strict-positive residual class, not an equality-only repair

Let d_i=x_i^2, s=sum d_i, p2=sum d_i^2, p3=sum d_i^3, e2=sum_(i<j)d_i d_j and e3=sum_(i<j<k)d_i d_j d_k. With a^2=1-s, actual local Bloch vectors are(2a x_i,0,1-2d_i), hence

    C=0,
    R=4-4s^2+4p2=4-8e2.

C0 follows because full spin flip maps weights0/1 to4/3, orthogonally. Direct action of the ACTUAL L=sum r_mu S_mu on psi gives

    L psi=4a|0000>
        +4 sum_i(a^2+d_i)x_i|1_i>
        +4a sum_(i<j)x_i x_j|1_i1_j>.

Therefore

    E2=<L^2>
       =16[a^2+a^4 s+2a^2 p2+p3+a^2 e2],
    epsilon=E2-6R+8-4C
       =8(s^3-3s p2+2p3)=48e3.                         (6.1)

The last equality is the elementary cubic expansion of s^3. Also the smallest local length satisfies t4^2=1-4 max_i d_i(s-d_i), giving

    eta_SP=t4^2-(R/2-1+C)
       =4[e2-max_i d_i(s-d_i)]
       =4 min_i sum_(j<k, j,k!=i)d_j d_k.               (6.2)

Thus whenever AT LEAST THREE x_i are nonzero, epsilon>0 and eta_SP>0. The coefficients can approach a two-nonzero boundary with no positive lower bound; the proof remains exact throughout. At most two nonzero x_i are the expected arbitrary-pair/two-singles boundary, not a missing strict-epsilon case. These identities are scope controls, NOT an imported TC inequality or an epsilon/g coercion.

Since p2>=s^2/4 and s<=1, R>=4-3s^2>=1. This whole positive-defect C0 family is outside the old small-R/high-C regions and is not merely v10's eta_SP=0 branch. It closes a genuine original residual class with arbitrary nonuniform coefficients and phases. It still does NOT cover arbitrary four-qubit states.

## 7. The new FULL mixed-mode clipping interface for the ORIGINAL remaining gap

This section states an exact sufficient GLOBAL target, NOT a theorem established outside the proved classes. For an arbitrary pure four-qubit rho define

    B_full=X3-3rho=Z/2-rho,
    E=Tr(B_full-I)_+,
    e=Tr(B_full)_-.

Because Z>=0, B_full has at most ONE negative eigenvalue. The trace is5. A sufficient uniform full-state estimate is

    E<=e,
    equivalently Tr clip(B_full,0,1)>=5.                (CLIP-prime)

The equivalence is the scalar spectral identity Tr clip(B,0,1)=Tr B+Tr B_--Tr(B-I)_+. This is NOT the older compressed F=QZQ clipping inequality and is not transferred from it.

If(CLIP-prime) held at an ACTUAL state, keep all B>1 eigenvectors and its one possible negative eigenvector, replace the other[0,1] eigenvalues by1, and add3rho as in Section4. The resulting Y dominates X3 and is positive. F=Y-I has negative index<=1, eigenvalues>=-1 and trace2+E-e. Thus TrF_+<=3+E-e<=3 and the SAME Ky Fan argument proves entire U3 majorization. If no negative eigenvalue exists, e0 forces E0 and the direct B<=I argument applies. This derives the sufficient interface with all actual full-state/off-face coupling retained.

General W proves(CLIP-prime) because the ONLY excess/negative bad pair is1+e,-e. The R0 critical envelope in the separate v11 candidate also supports it at its exact source scope, since B has the actual negative eigenvalue-1 and its remaining Z/2 spectrum has positive excess<=1. Neither observation is a proof of(CLIP-prime) at arbitrary positive defect/middle C.

The available scalar moments alone do NOT settle the new interface. Exact pure-Pauli identities give TrB_full^2=5+2C, and Z Theta psi0 gives lambda_min(B_full)<=-C. But the UNPHYSICAL scalar list

    11/10 four times, 7/20 twice, -1/10 once, 0 nine times

has trace5, square trace1019/200, the corresponding C=19/400 and negative mass e=1/10>=C, while E=2/5>e. This is an exact WRITTEN rational negative control on ONLY those scalar restrictions, NOT a realizable state/matrix-spin-flip coupling, channel counterexample, numerical scout or executed certificate. No scientific interpreter/program was used. It prevents treating a necessary moment tuple as physical proof data.

The missing global bridge must exploit the actual B_full/spin-flip/projector coupling, or the complete original common-P quartic, not independently chosen scalar eigenvalues, a positive compression or g=QLpsi/epsilon coercion. The exact arbitrary-state(CLIP-prime) status remains UNPROVED.

## 8. Current consolidated candidate, assurance and remaining original scope

Current v12 family union is the original291LF paired-parity/full logical-channel and W-incidence source, its mandatory optional-row-transpose qualifier, and THIS COMPLETE general-W closure. Old sources/ACKs/gates are not edited or widened. A new entire joint gate must name that union and its EXACT separate original channel/U3/affine hull conclusions; neither v10/v11 nor the earlier v12 submission automatically reviews this addendum.

The new W theorem uses only explicitly derived matrix entries, actual Hermitian singular-mode analysis, an elementary rank-one inertia bound, a valid spectral upper replacement, actual X3 positivity and ordinary Ky Fan facts. No TC inequality, v4 polarized block, complex DDVV/Lu-Wenzel theorem, global half-trace bound, source program or historical unadmitted arithmetic is a premise. Standard finite-dimensional spectral/Ky Fan/Pauli facts are named analytic inputs, not a formal-library proof claim.

The original unrestricted actual four-qubit k3 problem remains OPEN outside the exact proved/candidate families/regions at their named imports, with no epsilon/noise/C/R cutoff allowed in a full theorem. General W's formerly open matrix gap is NOW CLOSED prospectively by this new full-operator trace balance; that does not exclude other actual pure states or supply the global(CLIP-prime) bridge. No exact original counterexample, all-state k3 certificate, all-index unrestricted composition, full-book result or novelty/priority claim is delivered.

All permanent findings/HOLD/actual-return-before-primary-ACK rules/same18/cutoff/deadline remain. This complete subtheorem packet is parkable evidence, NOT a park/closeout of the active original assignment. Continue the actual arbitrary-state mixed-mode/quartic frontier after freezing it.
