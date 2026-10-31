# Actual k3 continuation v24 — ALL-complex paired-cut bound and necessary concentration on EVERY cut

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 06:57:19 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN CANDIDATE, NOT adopted or global closure.** Exact SYMBOLIC written proof including privately; no numeric parameter/control trial, decimal scout, scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO. The v120-C review was ACTUALLY RETURNED before separate whole-primary ACK `983bccfa9ada0c482a95ccb18e48e6fd26cee5963aa9694e79819c683ad8e36a` was WRITTEN AND SENT before this new primary source/reasoning. Parent v35 was then fully read; entire v22 withdrawal/local MATHEMATICAL MAJOR and all old histories remain.

This theorem uses the CORRECT START of the paired Werner–Holevo identity, not withdrawn FINAL F3. Mandatory `v14-F3-final-clause-withdrawal-and-v19-citation-qualification-v1.md` remains. The complete predecessor `residual-low-noise-operator-attack-v2.md` was reread: its false common arbitrary-U(4)xU(4) Schmidt-covariance shortcut remains FALSE. We use only the INDIVIDUAL summands' spectra with their DIFFERENT output unitaries, then a valid Ky Fan inequality; no common Schmidt spectrum for X3 is asserted.

## 1. Statement for EVERY actual complex pure state

Choose ANY physical two-qubit versus two-qubit partition A:B. Let p1>=p2>=p3>=p4>=0 be the four eigenvalues of the actual pair marginal rho_A, sum p_i=1 (equivalently squared Schmidt coefficients of the ACTUAL pure psi). Then

    K3(X3(psi))<=max(4+4p1, 6-4p4).                       (PAIR)

Consequences at the named original all-p coefficient-transfer interface:

1. If ANY of the THREE physical2|2 cuts has p1<=1/2, then K3(X3)<=6 and ORIGINAL k3 holds for all physical0<=p<=4/3, all complex rank-three testing projectors. The actual convex hull and physical LU/permutation images inherit the ORIGINAL comparison.
2. The bound is STRICT when that cut has p1<1/2 and p4>0. Its explicit certified margin is at least `min(2-4p1,4p4)>0`, supplying an arbitrary-direction trace-norm tube via v20's L4 if that separate candidate is imported.
3. EVERY pure U3 violator with K3(X3)=6+kappa,kappa>0 MUST satisfy

       lambda_max(rho_ij)>=1/2+kappa/4
             for EACH of the THREE complementary cuts.   (CONCENTRATE)

In particular it is strictly>1/2 on EVERY cut. This is a genuine ALL-state necessary restriction, not a condition imposed by a sampled ansatz or a scope reduction to one family. The unrestricted complement is still the original task.

For mixed inputs only the stated actual convex hull is acquired; imposing the same pair-marginal eigenvalue condition on a mixed density does NOT supply a decomposition into these pure states and is NOT claimed sufficient here.

## 2. The fixed magic-basis map identity is valid WITHOUT Schmidt realification

In a physical pair's magic basis the six single-qubit Pauli matrices are a real orthogonal frame for the purely imaginary Hermitian skew-transpose4x4 matrices. The entrywise identity

    sum_(six physical Paulis) S Y S=2[Tr(Y)I-Y^T]

holds for EVERY complex Y. Thus with W(Y)=[Tr(Y)I-Y^T]/3,

    X3(rho)=2rho+A+B,
    A=3(W_A tensor id)(rho)=I_A tensor rho_B-rho^(T_A),
    B=3(id tensor W_B)(rho)=rho_A tensor I_B-rho^(T_B).   (WH)

Each A,B is PSD: the displayed map has the explicit imaginary-skew Kraus sum. TraceA=TraceB=3. This is the correct physical transpose convention from the predecessor/v14START, not partial-transpose positivity of rho or the REFUTED finalF3 spectrum.

Write an ABSTRACT bipartite Schmidt decomposition psi=(U tensor V)sum_i sqrt(p_i)|ii> with arbitrary complex U,V. The individual maps obey contragredient covariance:

    A=(bar U tensor V) A0 (U^T tensor V^*),
    B=(U tensor bar V) B0 (U^* tensor V^T).

These are DIFFERENT output unitary conjugations in general. We derive the two individual spectra below, but do NOT replace their SUM or rho by one commonly conjugated diagonal-Schmidt operator. The actual interference/transposes remain unconstrained; the bound is valid despite losing their relative information by a one-direction subadditivity inequality.

## 3. BOTH complete individual spectra, including all zeros/degeneracies

For the canonical Schmidt state rho0, on EACH two-dimensional span{|ij>,|ji>}, i<j,

    A0=[[p_j,-sqrt(p_i p_j)],[-sqrt(p_i p_j),p_i]],
    B0=[[p_i,-sqrt(p_i p_j)],[-sqrt(p_i p_j),p_j]].

Each is PSD rank at most1, with eigenvalues p_i+p_j and0. Each kills all four diagonal vectors |ii>. Distinct unordered pairs have disjoint supports. Therefore BOTH individual sixteen-dimensional spectra are

    {p_i+p_j:1<=i<j<=4} plus TEN zeros.                  (SPEC-A/B)

Their trace is sum_(i<j)(p_i+p_j)=3, as required. The formula retains zero Schmidt masses and ties; it does not assert the full X3 spectrum depends only on p. In particular the omitted off-pair coherences in false FINAL F3 have NOT been dropped: they are the explicit negative entries in these two matrices.

Among the SIX nonnegative pair sums, the two largest are p1+p2,p1+p3. The third is max(p1+p4,p2+p3): every remaining edge p2+p4 or p3+p4 is no larger. Therefore

    K3(A)=K3(B)
      =2p1+p2+p3+max(p1+p4,p2+p3)
      =max(1+2p1,2(1-p4)).                              (EDGE3)

This is a direct quantified ordering proof, not an executed list enumeration or numeric comparison. All ties and vanishing eigenvalues obey the same expression.

## 4. Whole-output Ky Fan bound and exact ORIGINAL application

Ky Fan subadditivity applies to the ACTUAL three positive operators in WH regardless of their different eigenbases. Since rho is rank1,

    K3(X3)<=K3(2rho)+K3(A)+K3(B)
            =2+2max(1+2p1,2(1-p4))
            =max(4+4p1,6-4p4),

which proves PAIR for arbitrary complex psi and arbitrary complex rank-three projectors. It is a SUFFICIENT envelope, NOT an exact output spectrum, converse criterion, or assertion that the separately maximizing eigenvectors align.

If p1<=1/2 both terms are<=6; if p1<1/2,p4>0 both are strict, giving the printed margin. At the named parent-supported original channel interface, SAME-projector bounds TrPi rho<=1,TrPi X1<=10,TrPi X2<=12 combine with U3<=6 to give the exact product top-three polynomial

    (1-p)^4[1+6u+12u^2+10u^3+3u^4], u=p/[2(1-p)],

for0<=p<1. p=1 is direct; full global spin flip with q=2-p covers1<p<=4/3. This is the SAME ordinary-written interface adopted in `depol-v12-v19-entire-families-and-F3-refutation-parent-v1.md`, not a new certificate replay or general all-index composition. Mixed extension fixes Pi,p and averages the ORIGINAL affine channel traces over the specified pure states; it never averages Schmidt eigenvalue conditions or a nonlinear margin.

Conversely if K3=6+kappa>6, PAIR's second term6-4p4<=6 cannot carry that excess. Hence kappa<=4p1-2, proving CONCENTRATE for ANY chosen cut. The physical pair map exists for EACH physical partition, and permutations preserve X3/K3; apply the same proof to all three. No common Schmidt basis across cuts is posited.

At an actual original channel-failure pair, its deficit c=TrPi X3-6 is positive by d-cu+bu^2+au^3<0 with a,b,d>=0. Since K3(X3)>=6+c, every cut further obeys p1>=1/2+c/4. At v21's exact noise-critical witness c=2bu+3au^2, this gives `p1>=1/2+bu/2+3au^2/4` on EVERY cut. These are ACTUAL channel-pair deductions, not the unsupported channel a>9d condition imposed on coefficient-only violators.

## 5. What this adds and what remains

This is a new complete symbolic sufficient all-complex paired-entanglement region and an all-p original application, plus a quantitative restriction on EVERY possible residual pure violator. It is NOT a rediscovery of the invalid arbitrary-Schmidt-covariance shortcut: the two differing output rotations are retained and ONLY individual spectra enter a rigorously one-sided bound. No physical parameter/noise/control instance was chosen or evaluated, and no numerical witness was probed.

The original residual now additionally requires lambda_max>1/2 on ALL three pair cuts. It still includes arbitrary complex non-PAR states outside NP and all other supported regions, at every physical noise/projector and with no positive cutoff substituted for the target. Proving PAIR's complement harmless needs the ACTUAL joint rho/A/B/projector interference or the original critical/quartic compatibility; independent pair-sum bounds alone do not do that. Full-B CLIP-prime and the actual common-projector quartic remain held alternatives. No original counterexample/globalU3/all-index theorem, uniqueness, novelty/priority or stronger formal/kernel/human/family/executable adoption follows.

All F3falsefinal/SEC/W2/optimizer/firstorder/ROW qualifications, ENTIREv22mathwithdrawal/parentv35 and every prior cadence/exactness/privateapproxZERO/pause/inventory/orientation/readorder/freeze/clock/admission record remain. Same18/HOLD/exclusiveOWNroot/cutoff/deadline, no scientificGO or old frozen edit. Active continuation, NOT a park/closeout.
