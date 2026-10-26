# Actual k3 on the entire spin-flip/polygon equality locus — consolidated author candidate v10

## 0. Status, chronology, and exact limits

**NEW AUTHOR-WRITTEN CANDIDATE, not a returned review or an accepted global k3 theorem.** This is one complete actual-state theorem, including arbitrary complex rank-three projectors and all physical channel parameters, on a precisely defined locus and its specified convex hull. The original unrestricted k3 question remains OPEN off this locus. There is no scientific-execution, formal/kernel, configured-family, human, executable, priority, or novelty credit.

Verbatim metadata clock observed before this body: `Sun Oct 25 19:05:52 PDT 2026`. The actual complete two-gate v104-A review was returned to Main BEFORE the separate `primary-post-v104-resumption-exposure-ack-v1.json`, whose observed clock is `Sun Oct 25 18:58:09 PDT 2026`. The present re-derivation and body follow that ACK. The earlier SP-equality core and the later forbidden primary-pause refinements were separately disclosed in checkpoint044; they receive no clean pre-pause/preregistration or independent-verification credit. This prospective author reconstruction does NOT clear, backdate, or erase the permanent primary-pause process finding SHA256 `44fb09bb6d4fb5be9c19631313e552ae4a3f155b59f15d7a52c11fa2fff3087e`.

All older cadence, approximate-private-written-scoping, parent-admission/freeze/clock/root, and reviewer-history findings remain. In particular, the private approximate-scoping disclosure SHA256 `5b49e61483a80113eefc4a18047c7876676916fe631caaa923a46c7f783b4329` has ZERO theorem/certificate/verification/preregistration credit. There is no claim of a globally clean exact-written history. The word “independently” in checkpoint048 means an explicit owner re-derivation of the formulas, NOT an independent referee, fresh exposure, or new model-family gate.

No scientific interpreter, calculator, program, CAS, enumeration, solver, or replay was used for this body. All calculations below are displayed exact written identities and inequalities. No scientific GO was issued. The dead interpreter was not restarted. HOLD, the original eighteen owners, original science cutoff/deadline, exclusive owned write root, and no-park instruction remain unchanged.

The earlier complete k4 packet is `depolarizing-global-k4-spinflip-polygon-Schur-v9.md`, 271 LF, SHA256 `7cf35c988881c4d8d1d870359c1cdeca0ccf19195df906e0af9cef097734cf98`. Its parent disposition is `RUN/depol-original-global-k4-parent-v1.md`, 44 LF, SHA256 `e5d8f5f3f0c8a7742263e1d4c595eeb6b861a7c1fe0c6a4be9d81e8f5adfbb8f`, actually read in full before v104. Those are provenance for the already used SP/Schur approach, NOT acceptance of the NEW k3 theorem here. The new normal form, its actual complex Gram spectrum, and the rank-three application are derived below rather than transferred from a k4 or enlarged S4/S5 verdict.

Zhang attribution remains explicit: `source-audit-v2-zhang-prior-claim.md`, SHA256 `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`, records the prior matched-complement/clipping overlap and unresolved priority scope. This paper-level question is not given a clean novelty claim by changing the boundary representation.

## 1. The exact theorem and its unresolved complement

Let psi be a unit pure state of four qubits. Let S_mu range over the twelve single-site Pauli matrices. Put

    r_mu = <psi,S_mu psi>,   R = sum_mu r_mu^2,
    Theta = sigma_y^(tensor 4) followed by complex conjugation,
    kappa = <Theta psi,psi>,   C = |kappa|^2.

The four local Bloch lengths are ordered t1 >= t2 >= t3 >= t4 >= 0. Define

    eta_SP = t4^2 - (R/2 - 1 + C).

The inequality eta_SP >= 0 is proved in Section 2, including the C=1 endpoint. Let E_SP be the set of pure states for which eta_SP=0. For j=1,2,3 define the ORIGINAL affine operators

    X_j(rho) = sum_(|I|=j) rho_I tensor I_(I-complement),

where the identities are UNNORMALIZED. For pure rho=|psi><psi| the theorem is

    K3(X3(rho)) <= 6                              for EVERY psi in E_SP.       (T)

Here K3 is the sum of the three largest eigenvalues, equivalently the supremum over ALL complex orthogonal rank-three projectors Pi. This is not merely a containing-code assertion, a real-projector assertion, or a positive-compression assertion.

Consequently, for every rho in the specified convex hull conv(E_SP), every such complex Pi, and every physical p in [0,4/3],

    Tr Pi D_p^(tensor 4)(rho)
        <= K3(D_p^(tensor 4)(|0000><0000|)).                              (CH)

The mixed statement is proved ONLY by the original fixed-Pi affine traces in Section 7. No nonlinear averaging of R, C, Gamma, eta_SP, or a pure-state normal form is asserted.

**Exact original residual:** arbitrary actual pure states with eta_SP>0, and hence the original unrestricted k3/all-state comparison, are NOT settled here. Existing supported TC-zero results and full k2/k4 results keep their original separate scopes. No union audit of a new all-index unrestricted theorem is implied. The positive eta_SP region has no imposed cutoff; continuity at eta_SP=0 or compactness above a positive cutoff is not a substitute for its missing uniform estimate.

## 2. Spin-flip normalization, the polygon inequality, and the COMPLETE equality classification

For a single-site Pauli S, Theta S Theta^(-1)=-S, whereas Theta^2=1 on four qubits. Choose the irrelevant global phase of psi so kappa=sqrt(C) is nonnegative real. If C<1, set

    alpha = (1+sqrt(C))/2,   beta = (1-sqrt(C))/2,
    psi = sqrt(alpha) x + i sqrt(beta) y,

where x and y are orthonormal and Theta-real. Explicitly they are the normalized real and imaginary parts of psi relative to Theta; alpha,beta>0 and their orthogonality follows from real kappa. Put

    chi = (x+i y)/sqrt(2),
    u = 2 sqrt(alpha beta) = sqrt(1-C).

Then chi is an actual unit pure state and <Theta chi,chi>=0. For Theta-real x,y the diagonal Pauli expectations vanish and <x,S y> is purely imaginary. Expanding both expectations therefore gives the EXACT local-vector scaling

    <psi,S_mu psi> = u <chi,S_mu chi>                         for all twelve mu. (2.1)

This statement transports local Bloch vectors only. It does NOT transport the covariance matrix, channel spectrum, purity, or output projector from chi to psi.

Here is a direct proof of the only marginal-polygon fact needed. If lambda_i is the smaller eigenvalue of the ith one-qubit marginal of any pure state, choose on the other qubits their larger-eigenvalue eigenvectors and let P be their product projector. The commuting projector union bound gives

    <I_i tensor P> >= 1 - sum_(j != i) lambda_j.

Projection of the pure state onto that product vector gives an unnormalized rank-one contribution |z><z| to rho_i, with norm squared <I_i tensor P>. Hence lambda_max(rho_i) >= ||z||^2, and

    lambda_i <= sum_(j != i) lambda_j.                       (2.2)

Apply (2.2) to chi. Write its ordered Bloch lengths tau_1 >= tau_2 >= tau_3 >= tau_4=m. The inequality for the fourth marginal is

    tau_1 + tau_2 + tau_3 <= 2+m.

For each j=1,2,3, because m<=tau_j<=1,

    tau_j^2 <= (1+m) tau_j - m.

Adding the three inequalities and then m^2 gives

    sum_i tau_i^2 <= 2+2m^2.

Using (2.1), R=u^2 sum tau_i^2 and t4=u m, so

    R <= 2(1-C) + 2 t4^2,                                  (2.3)

which is exactly eta_SP>=0.

The equality conditions are important. If m<1, equality in (2.3) forces equality in the sum bound and in ALL three chord inequalities. Thus tau_1,tau_2,tau_3 are in {m,1}; their sum is 2+m, so precisely two are 1 and the third is m. If m=1, all four are 1 anyway. Therefore

    C<1 AND eta_SP=0   ==>   tau_1=tau_2=1, tau_3=tau_4.     (2.4)

A pure one-qubit marginal factors out of a pure global state. Thus the ACTUAL chi in (2.4) is two pure single-qubit factors times an arbitrary pure two-qubit state. Up to qubit permutation and local SU(2) matrices,

    chi = exp(i theta) |00> tensor (c|00>+d|11>),
    c>=d>=0,  c^2+d^2=1.                                   (2.5)

No assumption about generic rank or a positive spectral gap is needed.

Recover psi, not merely chi. Define

    A = (sqrt(alpha)+sqrt(beta))/sqrt(2),
    B = (sqrt(alpha)-sqrt(beta))/sqrt(2).

Then A>=B>=0, A^2+B^2=1, A^2-B^2=u, 2AB=sqrt(C), and

    psi = A chi + B Theta chi.                              (2.6)

Local SU(2) matrices commute with Theta. In the basis of (2.5), the spin flip of |00>(c|00>+d|11>) is |11>(d|00>+c|11>), with a PLUS sign: the two two-qubit minus signs cancel. The two terms in (2.6) initially carry exp(i theta) and exp(-i theta). The actual SU(2) rotation diag(exp(-i theta),exp(i theta)) on the FIRST single site removes both phases. Consequently

    psi ~ A c |0000> + A d |0011> + B d |1100> + B c |1111>. (NF)

This is an ACTUAL local-unitary/permutation normal form for psi, not a nonunitary covariance normalization and not an ansatz for all four-qubit states.

Conversely every state (NF), with the stated inequalities and normalizations and C<1, satisfies eta_SP=0: setting v=c^2-d^2 in [0,1], its four local Bloch lengths are u,u,uv,uv, its spin-flip concurrence squared is C=4A^2B^2=1-u^2, and

    R=2u^2(1+v^2),  t4^2=u^2v^2=R/2-1+C.

This proves the complete C<1 equality classification.

The C=1 branch is separate and MUST NOT be discarded or falsely assigned (NF). Then, after phase choice, Theta psi=psi. Every local Pauli is Theta-odd, so all local expectations vanish: R=0 and eta_SP=0. This includes arbitrary Theta-real four-qubit states, whether or not they have the four-term normal form. Section 6 handles ALL of them without dividing by u.

## 3. The ACTUAL complex centered Gram spectrum on (NF)

Let W have columns S_mu psi. Write

    G=W^*W,   Gamma=G-r r^T,
    Z=W W^*=sum_mu S_mu rho S_mu,
    Q=I-rho,  F=Q Z Q.

Gamma and F have the same nonzero eigenvalues, with the appropriate additional zero eigenvalues in their different dimensions. There is no claim they are the same matrix.

For (NF), define w=2cd=sqrt(1-v^2). The local expectations are r_1z=r_2z=u and r_3z=r_4z=uv. The transverse pair correlations are

    <X1 X2>=sqrt(C) w,   <Y1 Y2>=-sqrt(C) w,
    <X3 X4>=w,          <Y3 Y4>=-w.

The mixed XY expectations on DIFFERENT sites of a pair vanish because the four amplitudes are real. The ON-SITE XY entries do NOT vanish:

    G_(i,x),(i,y)=i r_iz,   G_(i,y),(i,x)=-i r_iz.            (3.1)

All cross-pair transverse correlations vanish by even/even versus odd/odd pair parity. All transverse-longitudinal entries vanish as well. Thus the transverse part splits into two four-by-four Hermitian blocks. For either pair the block is exactly

    [ 1    i a    b     0  ]
    [-i a   1     0    -b  ]
    [ b     0     1    i a ]
    [ 0    -b    -i a   1  ],                              (3.2)

where (a,b)=(u,sqrt(C)w) for pair12 and (uv,w) for pair34. Passing to symmetric/antisymmetric combinations of the two sites produces two two-by-two blocks, each with eigenvalues 1+-sqrt(a^2+b^2). In BOTH pairs

    a^2+b^2 = 1-Cv^2.

Therefore the eight transverse eigenvalues are

    1+sqrt(1-Cv^2), multiplicity FOUR;
    1-sqrt(1-Cv^2), multiplicity FOUR.                       (3.3)

This derivation retains the imaginary on-site commutators and all their effect on the eigenvalues. It is not a real-Gram replacement.

For the z coordinates, the actual correlations are <Z1Z2>=<Z3Z4>=1 and every cross-pair <ZiZj>=v. Centering gives the four-by-four block whose pair-constant entries are C, 1-u^2v^2, and Cv. The two antisymmetric pair vectors are ZERO modes, and in the normalized symmetric pair basis the remaining block is

    B_long = 2 [ C        Cv        ]
               [ Cv    1-u^2 v^2   ].                      (3.4)

Its determinant is 4C(1-v^2)>=0, its trace is

    Tr B_long = 2(C+1-u^2v^2) = 4-R = delta,               (3.5)

and it is positive semidefinite. Equations (3.3)–(3.5), plus TWO additional zero modes, give all TWELVE actual complex Gamma eigenvalues, including degenerate endpoints. There is no missing free phase or independently chosen support.

Each eigenvalue in (3.3) lies in [0,2]. The two nonnegative eigenvalues in (3.4) sum to delta. Hence

    K2(Gamma) <= 4                    if 0<=delta<=2;
    K2(Gamma) <= delta+2              if 2<=delta<=4.        (3.6)

For the second line, a pair of long eigenvalues sums to delta, one long plus one transverse is at most delta+2, and two transverse are at most 4<=delta+2. In particular, for this C<1 NORMAL-FORM BRANCH ONLY,

    K2(Gamma) <= 4+delta/2 = (Tr Gamma)/2.                   (3.7)

We do NOT infer this stronger half-trace assertion for every C=1 state, or for arbitrary positive eta_SP states. They are not covered by the spectrum (3.3).

## 4. The full Schur constraint and rank-independent COMPLEX placement bound

This section derives the needed genuine off-face estimate. It does not discard the psi-to-Q coupling.

First, any six-by-six actual single-Pauli Gram matrix on a PAIR of sites has block form

    [ I+i K1     T      ]
    [ T^T      I+i K2   ],

with real skew matrices K1,K2 and real T. Conjugating by diag(I,iI) makes its difference from I purely imaginary. Its entrywise conjugate is therefore 2I minus the conjugated Gram matrix. Both are positive, so the pair Gram lies between 0 and 2I. This is an entrywise-conjugate PSD argument, NOT partial-transpose positivity of a state.

Partition the four sites into two pairs. In the full positive Gram G the two diagonal pair blocks are at most 2I. Block Cauchy–Schwarz bounds a cross quadratic form by twice the product of the two vector norms; hence the whole Rayleigh quotient is at most 4. Thus

    0<=G<=4I,  0<=Z<=4I.                                  (4.1)

For a pure state, the single-qubit Pauli expansion and the Schmidt identity give the ORIGINAL operator relations

    X1=2I+L/2,   X3=2rho+Z/2,   Z psi=L psi,
    L=sum_mu r_mu S_mu.

Set v0=Q L psi and V=||v0||^2. The notation v0 here is a vector; the scalar v in (NF) remains c^2-d^2. In the psi plus Q decomposition, 4I-Z has upper-left entry delta=4-R and off-diagonal vector -v0. For delta>0 its FULL Schur complement gives

    4I_Q-F >= v0 v0^*/delta.                               (4.2)

Also Z^2<=4Z gives <L^2><=4R and therefore

    V=<L^2>-R^2 <= R delta.                                (4.3)

These are actual-state coupled inequalities. No identification of v0 with a polarized-block vector g, no false coercion by epsilon, and no separate independently chosen covariance modes has been used.

Let Pi be ANY complex rank-three projector. Apart from endpoint choices, its range has an orthonormal description consisting of a rank-two subspace P orthogonal to psi and eta, and

    xi=sqrt(1-d0) psi + sqrt(d0) eta,   eta in Q, ||eta||=1.

The phase is absorbed in the actual complex vector eta. The containing comparison projector is Pi0=rho+P. Put a0=|<eta,v0>|^2. Equation (4.2) and the FULL complex cross term imply

    Tr(Pi-Pi0)X3
       <= -d0 (R+a0/delta)/2 + sqrt(d0(1-d0)) sqrt(a0).

The maximum over d0 in [0,1] is the upper eigenvalue of the corresponding two-by-two Hermitian matrix:

    g(a0)=[sqrt((R+a0/delta)^2+4a0)-(R+a0/delta)]/4.         (4.4)

The d0=0 and d0=1 cases satisfy the same bound directly or by continuity of THIS FINITE EXACT ROTATION FORMULA; this is not a compactness/cutoff argument for missing physical states.

For fixed R and delta with R+delta=4, g is increasing. For instance, writing y=a0/delta, the derivative comparison reduces to the exact positive difference

    (R+y+2delta)^2 - [(R+y)^2+4delta y] = 16delta.

The zero case is interpreted directly. By a0<=V<=Rdelta,

    Tr(Pi-Pi0)X3 <= g(V) <= g(Rdelta)
       = sqrt(R)-R/2 <= delta/4.                           (4.5)

For the last step let x=sqrt(R) in [0,2); then

    (sqrt(R)-R/2)/delta = x/[2(2+x)] <= 1/4.

All cross terms have been retained before taking their modulus. There is no assumption that Pi is real, contains psi, or has vanishing tilt. The argument is rank-independent; its application here is explicitly rank THREE, not an inherited S4/S5 operator-positivity claim.

## 5. Combining the actual spectrum with the actual placement — proof of (T) for C<1

For a containing rank-three projector Pi0=rho+P,

    Tr Pi0 X3 <= 2+R/2+K2(Gamma)/2.                         (5.1)

Combine (3.6), (4.5), and (5.1). If 0<delta<=2,

    Tr Pi X3 <= 2+R/2+2+delta/4 = 6-delta/4 <= 6.

If 2<=delta<4,

    Tr Pi X3 <= 2+R/2+(delta+2)/2+delta/4
              = 5+delta/4 = 6-R/4 <= 6.                   (5.2)

This proves (T) on the complete C<1 equality normal form, with no positive epsilon cutoff. At delta=0, all four Bloch lengths are one, so psi is a product state; X3 has eigenvalues 4, four copies of 1, and the remaining zeros. Its K3 is exactly 6. No Schur division by zero occurs.

As a consistency control, C=0 gives one arbitrary pure pair and two singles, in agreement with the previously supported TC-zero locus. More importantly, the new theorem is NOT only that old locus: on the GHZ subfamily A|0000>+B|1111> (v=1), one has R=4(1-C), <L^2>=4R, and the original TC expression is

    epsilon=<L^2>-6R+8-4C=4C.

Thus every C>0 member has strict positive epsilon, with arbitrarily small positive epsilon allowed. This is an exact symbolic identity, not an approximate scan, a new finite enumeration, or a claim that the whole positive-epsilon region is solved.

## 6. ALL C=1 states, not just a four-term endpoint

As Section 2 showed, C=1 forces R=0, L=0, v0=0 and eta_SP=0. The full placement bound (4.4) is then zero: an arbitrary off-face projector cannot improve on its containing comparison.

For completeness, the pure four-qubit Pauli sector identities are A2=R+2+4C and

    Tr G^2 = 12+2R+2A2 = 16+4R+8C.

They follow by expanding G: its four on-site blocks contribute 12+2R, and each weight-two Pauli expectation contributes twice. The relation for A2 follows from the one-versus-three marginal purities and the spin-flip overlap expansion; these are the same standard exact pure-Pauli identities used in v9, not the separate TC inequality epsilon>=0. At R=0,C=1, Gamma=G and Tr Gamma^2=24. Consequently

    K2(Gamma) <= sqrt(2 Tr Gamma^2) = 4sqrt(3).

Equations (5.1) and the zero placement gain give, for EVERY complex rank-three Pi,

    Tr Pi X3 <= 2+2sqrt(3) < 6,                            (6.1)

where the strict comparison is the exact inequality 3<4. No C=1 state was forced into (NF), and no stronger half-trace claim at this endpoint was smuggled in.

Together Sections 5 and 6 prove (T) on the ENTIRE eta_SP=0 pure-state locus.

## 7. ORIGINAL affine channel comparison, all physical p, specified mixed hull

The two other ORIGINAL coefficient bounds needed for rank three hold for all input states. X1 is a sum of four commuting one-qubit marginals lifted with identities; its three-eigenvalue Ky Fan maximum is bounded by the corresponding pure-local product spectrum 4,3,3. Hence Tr Pi X1<=10 for every rank-three Pi. One can equally obtain this by convexity in each local density matrix independently, whose extrema are pure.

The exact full operator inequality

    3I-X2+3rho = (1/2) sum_(weight(P)=2) P tilde(rho) P >= 0                 (7.1)

implies Tr Pi X2<=9+3Tr Pi rho<=12. Here tilde(rho)=Theta rho Theta^(-1) is the full spin flip and is positive. To check the normalization in (7.1), multiply its Pauli expansion by 16: both sides have weight multipliers (27,-9,-1,3,3) on weights 0,1,2,3,4. The sum has 54 weight-two Paulis before the factor 1/2. This is a full global-transpose spin flip, NOT an invalid partial-transpose shortcut.

For p<1 put t=1-p and z=p/[2(1-p)]>=0. The ORIGINAL channel expansion is

    D_p^(tensor 4)(rho)
       =t^4 [rho+z X3+z^2 X2+z^3 X1+z^4 I].                (7.2)

For rho pure in E_SP, Sections 5–6 and the bounds above give, for any fixed complex rank-three Pi,

    Tr Pi D_p^(tensor 4)(rho)
       <=t^4[1+6z+12z^2+10z^3+3z^4]
       =t^4(1+z)^3(1+3z).                                (7.3)

The right side is exactly the sum of the three largest eigenvalues of the product-reference output: one copy of [t(1+z)]^4 plus two copies of [t(1+z)]^3 tz. At p=0 the same polynomial formula is direct; at p=1 both outputs are I/16, so the rank-three trace is 3/16.

For 1<p<=4/3, use q=2-p in [2/3,1). Full spin flip multiplies a Pauli term of weight w by (-1)^w, so D_p^(tensor 4)(rho) is the full spin flip of D_q^(tensor 4)(rho). Their spectra coincide. The product-reference spectra coincide under the same reflection, proving (CH) throughout the physical interval. No new-state approximation or asymptotic continuation is needed.

Finally let rho=sum lambda_j rho_j, lambda_j>=0 and sum lambda_j=1, with each rho_j pure in E_SP. For the SAME fixed original Pi and p, every X_j trace, the rho trace, and the channel trace in (7.2) are affine. Average their inequalities, or average (7.3) directly, to obtain (CH) on conv(E_SP). Nothing is inferred for a mixed state merely from a nonlinear equality imposed on its own R or spin-flip overlap.

Equivalently, on this exact locus/hull the original k3 quartic always lies in the automatic original excess branch c_excess=Tr Pi X3-6<=0. We make NO blanket discriminant D>=0 assertion. The separate k2 mandatory branch qualification SHA256 `dded2fa9095e38ea7f72c61fa9b721ffcdd9e14cfcd376a0c352d3365090ace5` and its actual negative-D/c<0 control remain unchanged.

## 8. What this advances, what it imports, and what remains

The genuinely new candidate interface here is: COMPLETE eta_SP=0 classification with the C=1 exception, the actual complex twelve-mode spectrum on its C<1 branch, and the FULL coupled rank-three placement estimate yielding the original all-p k3 bound on the entire locus and its explicit convex hull. The proof does not coerce v0 by epsilon/g, replace g by QLpsi, drop complex TT* terms, assume physical equality from scalar norm/purity data, or impose a positive noise/epsilon/eta cutoff.

The displayed derivation uses standard finite-dimensional spectral facts, the elementary pure-marginal projector argument, the single-site Pauli algebra, Schmidt factorization, full spin flip, and the standard pure four-qubit sector identity A2=R+2+4C at the C=1 endpoint. The latter identity is a NAMED ANALYTIC IMPORT at exactly that endpoint; its full literature/history is not newly reconstructed here. The TC inequality, the v4 polarized block, and a global half-trace/starcommutator conjecture are NOT mathematical premises for this locus theorem. Standard identities (4.1)–(4.5) and the new normal-form Gram entries have been explicitly re-derived in writing, not machine-checked.

The original unrestricted gap remains the actual eta_SP>0 sector, including arbitrary strict-positive-epsilon states, with arbitrary complex off-face rank-three Pi and NO positive cutoff. The missing estimate must control the actual multimode placement or the full actual common-P quartic there. A near-boundary perturbation needs its actual cross terms; continuity or a claim that the boundary maximizer automatically controls nearby states does not provide it. The global half-trace inequality is still an UNPROVED possible sufficient route, not an admitted fact. No original k3 counterexample, unrestricted all-index composition, whole-book resolution, or clean novelty/priority claim has been delivered.

This is a complete, parkable SUBTHEOREM packet, not a park/closeout of the continuing owner assignment. Original active research continues after this checkpoint, subject to serial review interruptions and the unchanged deadline/HOLD.
