# P44 addendum3 — exact PPT budget range, universal separable false positives, and the minimizing-face caller

Owner **PhysicsPPT44-2**, physics-3. Actual native `/bin/date` immediately BEFORE this NEW immutable write: **Tue Oct 27 16:40:22 PDT 2026**. **WRITTEN UNREVIEWED**, no identity machine-checked and no original P44 outcome claimed.

## 1. New admitted branch and precise dependency

After the actual w62 review return, Main directed continuation inside the existing S1, specifically allowing a genuinely different coupling through the actual-pair budget `b_A+b_B<t`, rather than another positive-reconstruction iteration. I read the COMPLETE new parent disposition `physics-3-ppt-complement-cone-and-reconstruction-barrier-parent-v1.md` as exact adoption/status. It adopts the v1+addendum1 chain at same-harness written scope; addendum2 is NOT assumed parent-adopted from a reported no-defect review.

The mathematical inputs here are ONLY the original parent-supplied S2 state/SR2/separator definitions; the actual-pair inequality and positive double-complement proved in current v1 (`7d00196376108da34c416b8e80f815adfc337d01cb24191f8ad40f6a47d8cdc4`); and the explicitly named elementary spectral/trace/positive-matrix facts proved below. No peer-review body, old proof, JL construction or private method is opened or imported.

This branch uses NO nonunitary local congruence, marginal balancing, inverse filter, witness scaling or replacement preserving a given state's marginals. Local eigenvectors are quantified as a COMPLETE theorem for EVERY W, not selected inputs for a sanity test. No actual dimension, spectrum, witness or state is substituted to test viability. Historical authorship/exposure and all stopped guides remain; there is no counterfactual untouched-cognition, independent-reconstruction or novelty claim.

The new content is an EXACT optimization over the entire PPT state set and a universal actual-object false-positive family, not a coordinate encoding. It proves that feasibility of the necessary budget condition is, by itself, existentially nondiscriminating: EVERY nonzero two-block-positive W has a separable state satisfying it strictly.

## 2. Exact original objects and notation

The original application is C^4 tensor C^4. Prove a uniform statement for local dimensions d_A,d_B>=3. Let W be ANY Hermitian operator nonnegative on EVERY complex vector of Schmidt rank<=2. Define its ACTUAL partial traces and trace by

    A=Tr_B W,      B=Tr_A W,      t=Tr W.

For an ACTUAL density operator rho let rho_A=Tr_B rho, rho_B=Tr_A rho and

    b_A(rho)=Tr(W(I_A tensor rho_B))=Tr(B rho_B),
    b_B(rho)=Tr(W(rho_A tensor I_B))=Tr(A rho_A),
    beta_W(rho)=b_A(rho)+b_B(rho)-t,
    a_W(rho)=Tr(W rho).

Thus beta_W is the expectation of the SAME local-cost operator

    H_W=A tensor I_B+I_A tensor B-t I_AB.                  (2.1)

For every eligible PPT rho, the adopted v1 inequality gives

    beta_W(rho)<=a_W(rho).                                (2.2)

Strict negativity therefore requires beta_W(rho)<0. No converse was adopted or assumed.

## 3. Elementary positivity and the nonzero-trace boundary

A and B are positive. For arbitrary Alice vector u and arbitrary orthonormal Bob basis, `<u|A|u>` is the sum of the product-vector W expectations over that ENTIRE basis, each nonnegative. The Bob-side proof is identical. Partial trace gives

    Tr A=Tr B=t>=0.

In fact W!=0 implies t>0. To pay that boundary without a hidden definiteness assumption, fix an ARBITRARY full orthonormal product basis. For ANY two basis vectors their whole complex linear span has Schmidt rank<=2. W's compression to it is therefore a positive two-by-two Hermitian matrix. In particular every basis diagonal is nonnegative and each off-diagonal entry obeys the positive-matrix inequality `|W_ij|^2<=W_ii W_jj`.

If t=0, all those diagonals are zero, so all off-diagonal entries vanish too. W=0. This proves the asserted contrapositive for EVERY W. It is an entire-basis argument, not evaluation on a chosen state, not a rank-chart/zero-ensemble construction and not a trace normalization of W.

These are elementary consequences of the given full complex SR2 condition. They do not assert W itself positive or decomposable.

## 4. Exact optimization over PPT and all states

Let a_-,a_+ be the smallest/largest eigenvalues of A and b_-,b_+ those of B. Put

    mu_-=a_-+b_--t,       mu_+=a_++b_+-t.                 (4.1)

Let E_A^- and E_B^- denote the COMPLETE smallest-eigenvalue subspaces, with analogous E_A^+,E_B^+.

**Theorem1.** The set of values of beta_W over ALL density operators, over PPT density operators, over separable density operators, and over SN<=2 density operators is the SAME complete interval

    [mu_-,mu_+].                                         (4.2)

In particular both endpoints are ATTAINED by product pure states. The assertion is uniform over W and every spectral multiplicity; it selects no numerical witness/state or parameter.

**Proof.** The two local Hermitian terms in(2.1) commute. In their arbitrary local eigenbases the eigenvalues of H_W are ALL sums `a_i+b_j-t`, with no additional constraints. Hence every state expectation lies between(4.1).

For EVERY unit u in E_A^- and EVERY unit v in E_B^-, the ACTUAL product state `sigma_-=|u tensor v><u tensor v|` has beta_W(sigma_-)=mu_-. It is positive, trace one, PPT and Schmidt number one. The complete analogous product family at the largest eigenspaces attains mu_+. These are actual universal extremizer formulas, not existence of independent abstract coefficients.

Every intermediate scalar is attained by a convex combination of such endpoint product states. If the endpoints are distinct, the usual affine weights in[0,1] are well-defined; if they coincide, the expectation is constant and either endpoint family suffices without division. The combinations remain separable/PPT/SN<=2. Since each of those sets is contained in all states, their ranges cannot be larger and must equal the same interval. QED.

This theorem matches only the stated SCALAR budget value. It does NOT construct a replacement with the same full marginals or the same witness expectation. In particular it is not the held matching-marginal/scaling route.

### Complete endpoint faces, including degeneracies

All density minimizers are exactly the states supported in `E_A^- tensor E_B^-`; the PPT minimizers are their PPT subset. Indeed

    H_W-mu_- I=(A-a_- I) tensor I+I tensor(B-b_- I)>=0.

Zero expectation against a positive density operator forces its range into the kernel: `Tr(P rho)=||P^(1/2)rho^(1/2)||_HS^2=0` for positive P. The joint kernel of the two commuting positive local terms is exactly that tensor product, by their full eigenbasis. Conversely any state on it has the minimum expectation. The maximum face has the analogous description using the positive operator `mu_+ I-H_W`.

Thus repeated/zero local eigenvalues and arbitrary minimizer multiplicities are retained. I do NOT claim that every minimizer is product or separable; the guaranteed product EXTREMIZER families are only part of those faces. A flat budget interval is handled without creating a balanced normal form or invoking a normalization.

## 5. Universal strict false positives for the necessary budget condition

**Theorem2.** For EVERY nonzero complex two-block-positive W in the stated dimensions,

    mu_-<0.                                              (5.1)

Consequently EVERY product state in Theorem1's minimizing product family is an eligible PPT/SN1 state satisfying `b_A+b_B<t`, but has `Tr(W sigma_-)>=0`. Thus the necessary budget inequality alone is not a sufficient separator condition, for ANY such W.

**Proof.** Section3 gives t>0 and A,B positive of trace t. The smallest eigenvalue cannot exceed the average eigenvalue, so

    a_-<=t/d_A,       b_-<=t/d_B,
    mu_-<=t(1/d_A+1/d_B-1)<0.

The strict dimension inequality holds throughout d_A,d_B>=3; no chosen dimension is evaluated. The product states of §4 then attain the strict budget inequality, while the ORIGINAL product-vector positivity of W gives their nonnegative witness expectations. All statements quantify over EVERY nonzero W and EVERY unit vector in its minimum subspaces. No particular W or state was chosen as a test. QED.

For W=0 the entire interval and all three expectations are zero; there is no strict budget condition. Singular A/B and zero minimum eigenvalues require no inverse and are included. The trace-one state assumption is the original one. The unnormalized extension at any fixed trace s>=0 follows by positive homogeneity; for s=0 the only positive input is zero and all terms vanish.

The universal false-positive conclusion is stronger than showing one counterexample to a proposed inference. It completely characterizes the existential budget feasibility at the W level: nonzero two-block-positive W ALWAYS passes that feasibility test on an SN1/PPT state. It does not say that the ORIGINAL joint negative pair exists or that a given budget-feasible actual rho is separable.

## 6. Exact residual coupling and the original caller

The current v1 proof also supplies the ACTUAL positive double complement

    Z_W=t I_AB-I_A tensor B-A tensor I_B+W>=0.             (6.1)

This is the same operator obtained by rank-two alternating congruences of W^T in v1, not an independently chosen positive matrix. No new source is used. For EVERY actual density operator rho,

    a_W(rho)=beta_W(rho)+Tr(Z_W rho).                     (6.2)

At a minimizing PRODUCT extremizer sigma_-, Theorem2 and product positivity imply

    Tr(Z_W sigma_-)>=-mu_->0.                            (6.3)

Thus exact optimization of the local budget reaches points at which a positive residual slack compensates the entire negative budget. Merely obtaining the strict inequality does not pay that joint slack. Equation(6.3) is only for the specified full product-extremizer families; no unproved inequality is asserted for every possibly entangled minimum-face state.

For an actually eligible rho,W, strict negative separation is equivalent to

    Tr(Z_W rho)<-beta_W(rho).                             (6.4)

The equivalence is just the exact original-object bookkeeping identity(6.2), NOT counted as a new solution or encoding advance. The new substantive claims are the full optimization/range theorem, uniform false-positive family, and the compensation/face obstruction showing WHY (6.4) remains unpaid after budget minimization.

A future actual construction must still supply rho>=0, trace one, rho^Gamma>=0 and globally complex-SR2-positive W with this actual strict slack inequality. Neither a scalar budget value nor a formal positive residual produces those joint facts. Conversely, whenever those actual original conditions and(6.4) ARE supplied, S2's stated separator equivalence yields the positive P44 alternative; that is the exact caller, not a claimed witness here.

## 7. Additional minimizing-face obstruction, not a global rank restriction

If either `dim E_A^-<=2` or `dim E_B^-<=2`, then EVERY positive state on the complete minimum face is C2. Spectral decomposition has vectors supported in that tensor product, and each such vector has Schmidt rank at most the smaller local support dimension. Therefore W has nonnegative expectation on ALL those states, including its PPT subset.

Consequently a negative eligible pair that ALSO minimizes beta_W would require BOTH minimum eigenspaces to have dimension at least three. This is a necessary condition ONLY for that explicitly constrained budget-minimum route. It is NOT a condition on all negative pairs away from the minimum, not a restriction proved for all PPT states and not an evaluation of an actual spectral multiplicity. No old rank-floor, chart or normalization theorem is imported.

## 8. What changes and what does not

This is genuinely different from the already adopted fixed-positive-reconstruction barrier. It is a complete optimization on the ACTUAL state set for every actual W, with attainment, converse scalar realizability, degenerate faces and the original negative-pair slack caller. No positive map combination is used to reconstruct rho.

It proves that the necessary strict marginal budget has the SAME feasible scalar interval even on separable states and is existentially satisfied by every nonzero two-block-positive W. The relevant next coupling must control the residual slack or correlations, rather than declare the budget alone discriminating. Nothing proves all rho C2 or W decomposable, and no candidate negative pair is produced.

The old nonunitary-congruence/marginal-balancing/scaling branch, JL construction audit, all old post40/other held guidance and every selected-control consumer remain NONINPUT. No local filtering, state-marginal matching, regauging or trace normalization of W was performed. Prior awareness persists; no historical absence/novelty or clean-cognition certificate is claimed. The proof graph is solely the current adopted budget/double-complement identity plus elementary positive-matrix/spectral/trace facts, each used above.

Main's new L1 quarantine notice is binding: L1 and ALL consumers are HELD/ZERO/NONINPUT. I read ONLY the IRC notice, did NOT open L1 or its quarantined guidance, and use none of it here. The notice expressly left unrelated duties unchanged; it is not a new mathematical input.

All results here are **WRITTEN UNREVIEWED**. No identity machine-checked, no scientific interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test/typechecker, chosen numerical/state/control/dimension/boundary sample, nested agent/modelCLI/paidAPI, Git/delete/contact/publication/infrastructure action. Original definitions remain parent-supplied, not newly book-authenticated. No original P44 closure, formal/kernel/executable/human/configured-family or novelty acceptance. All history/STOP/HOLD/ZERO/N4 UNKNOWN historical exit unestablished/old21 NR/auxiliary214 STOP and successor science end2026-10-31T21:23:27.000Z remain.
