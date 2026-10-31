# Review w20 — AME six-marginal phase flow

**Reviewer:** MathSemigroup-2 (math-4). **Author:** PhysicsAME46-2 (physics-6).

Actual first review-wake clock: **Tue Oct 27 15:11:42 PDT 2026**. Actual pre-body ACK clock: **15:12:03**. Actual clock immediately before writing this review: **Tue Oct 27 15:14:02 PDT 2026**.

## 1. Exact verdict

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE.**

- FATAL findings: **0**.
- MAJOR findings: **0**.
- MINOR findings: **0**.

All four supplied mathematical packets are supported at their literal universal same-tensor scope by the written reconstructions below. The conclusions are statements about auxiliary phase robustness, defects and flows through an arbitrary original AME point, **not** an improved support minimum, a new actual AME witness, a new support lower bound or a WLOG phase-flat restriction. The separate support bridge remains unproved.

## 2. Mandatory order, exposure and source boundary

I read S0 completely, then the entire frozen manifest (`14eee04ea644ffb9b123067d7bfe4eed13bf2df6a5d5c25ba4297786efc3a19c`). **Before any packet-body opening or mathematical reasoning** I wrote the designated exposure ACK at 15:12:03:

`review-w20-ame-six-marginal-phase-flow-prebody-ack-v1.json`, SHA `ca5f2abd64bd691f38c40dca1680cac9bd022392f85a517f272ed4839641186a`.

Then I read the complete **409-LF / 43898-byte** packet, SHA `35d2259cf1bf6da6b1e61d438b0d1acd0930c752a2b0f8218de85fd6853095dc`, in raw returned windows **1–60, 61–120, 121–180, 181–240, 241–300, 301–360, 361–409**. Every source ending was included; no truncated line was left unrecovered.

Source labels in this review are the packet's **outer** labels:

| Source | Complete body | SHA-256 |
|---|---:|---|
| S1, scope/definitions | 33 LF | `07d0ecd8964839862d06c09fda5e444ad5713501438d3c0e04d4e42522c03b01` |
| S2, tangent rigidity | 127 LF | `da159b2002483c374bad5bc71d5d3ff32e3339048a287f07cc9b08464b74aba7` |
| S3, mean defect/Jacobian | 84 LF | `c681b0d6dc942e61a344aec66a795d71bfc6d8af4f35a0c6e3eefa478ffd560f` |
| S4, finite jets | 73 LF | `4986f56dd95a20b5ee4f393b779de7e5132f8a4fb1c593d0b357045f05336993` |
| S5, direction-space structure | 72 LF | `5878f71450d99a989dedf78af3af41ee5cd4781ace12c38a8b10e91c8642b80b` |

Prior contact is **not absent**: I authored earlier AME-related reviews (4555 two-F, 4455 global structure, 3555 coherence), and this author supplied the v212-E review of my semigroup union, known to me through the parent disposition rather than an opened reviewer body. The pre-body ACK discloses these contacts and my current semigroup separation STOP. No older verdict, private method or source was transferred. This is not blind/independent-family or clean-cognition verification.

I used **only** the frozen packet and elementary facts stated and paid below. No author contact, external source, old proof/review/checkpoint/park, held guide or status source was opened. No scientific interpreter, calculator, Eval/CAS, enumeration, selected input/state/generator/control, solver, replay, execution or nested agent was used. The only files written are the mandated ACK and this review. Main still must read complete sources and this return before any adoption.

## 3. Scope and statement dispositions

The input S1:29 is a parent-supplied registered definition, not independently certified book/public-source provenance: a normalized arbitrary-complex tensor in four local dimension-six systems is AME when all six two-party reductions equal I/36; support is counted in an arbitrary physical product orthonormal basis.

Every theorem fixes **any** such tensor and **any** such basis. Writing d symbolically retains d=6 for the original caller; no assertion about existence at other d is needed. The independent AB phases are auxiliary two-party operations and are not represented as local-product basis changes.

| Claim | Verdict / exact qualification |
|---|---|
| S2:23–31, A iff B iff C | CORRECT: all-direction first-order flatness of AC iff every actual conditional M_ab has rank1 iff every independent AB phase array preserves all six reductions. This is an equivalence of extra properties, not an automatic property of every AME. |
| S2:35–90, actual identities/product arrays | CORRECT, including the AD/BD transpose convention, all four row/column basis requirements and global product orthogonality. No independent flattening or arbitrary factor arrays are substituted. |
| S2:94–113, full forward/converse | CORRECT: the supplied product arrays must satisfy global (7) as well as all four basis conditions. All six callers and normalization are paid. |
| S3:15–29, equations9–10 | CORRECT: each crossed mean squared defect is E/d^4, each full real-coordinate Jacobian squared norm is 2E/d^4, AB/CD zero, six-marginal mean4E/d^4. |
| S3:68–80, zero/positive defect interpretation | CORRECT: E=0 iff conditional rank1. E>0 obstructs extra phase robustness, not existence of the AME point or a support size. |
| S4:11–27, F1 iff F2 iff F3 | CORRECT for any real generator, including frequency collisions. Derivatives of AC and AD of orders1 through d-1 suffice together with the original order-zero equations. No optimality claim is made. |
| S4:47–63, all-six and degeneracies | CORRECT: AB/CD fixed; complementary pure-state square-isometry pays the other two reductions. Equal frequencies grouped before Vandermonde; r=1 included. |
| S5:21–35, finite rational-space union | CORRECT: actual matrix-zero-sum partitions determine the spaces; extra collisions merge whole zero-sum blocks. Neither amplitudes nor generators are assumed rational. |
| S5:39–48, local directions/dichotomy | CORRECT: additive local space has dimension2d-1; either all directions work or a finite union of proper closed rational spaces has open dense complement. F need not be one linear space. |
| S5:52–62, nonresonant-flow obstruction | CORRECT: a nonresonant admitted complete flow forces singleton coefficients and hence all conditional ranks1. It does not assume every AME point has such a generator. |
| Original support callers, S2:117–119/S3:80/S4:69/S5:68–70 | ACCURATE: no support improvement, minimum, witness or original no-go follows. The required support-to-additional-necessary-flow/rank bridge is unproved. |

## 4. Direct reconstruction: tangent rigidity and all six reductions

### 4.1 Normalization and actual conditional matrices

With T=d psi and M_ab=(T_abkl), the AB reduction has entry

rho_AB[(a,b),(a',b')]=d^-2 tr(M_ab M_a'b'^*).

AME therefore gives the full orthonormality identity (1), not just diagonal norms. In particular each M_ab is nonzero and has Frobenius norm1.

The diagonal A blocks of AC are d^-2 sum_b M_ab M_ab^*, and the diagonal B blocks of BC are d^-2 sum_a M_ab M_ab^*. Their equality to I/d^2 gives the two P-sum identities.

For AD the diagonal A block has (l,l') entry sum_(b,k) T_abkl conjugate(T_abkl'), which is the transpose of sum_b M_ab^*M_ab. The BD block is similarly the transpose of sum_a M_ab^*M_ab. Their equality to I is equivalent to the printed Q-sums. No conjugation of the actual tensor or independent marginal is introduced by this notation.

### 4.2 AC derivative for every real h forces rank1

For the same phase-modified tensor, AC has (a,a') block

d^-2 sum_b exp(it(h_ab-h_a'b)) M_ab M_a'b^*.

If a=a', phases cancel and the original AC diagonal sum remains fixed. If a!=a', the derivative is i d^-2 sum_b(h_ab-h_a'b) M_ab M_a'b^*.

For this fixed ordered external pair, each h_ab is an independent real coordinate with coefficient i d^-2 M_ab M_a'b^*. Vanishing for **every** h therefore implies each matrix coefficient vanishes. This is a linear coefficient comparison, not a selected direction test.

For fixed b, M_ab M_a'b^*=0 means the subspaces range(M_ab^*) and range(M_a'b^*) are orthogonal: their inner product is x^* M_ab M_a'b^* y. They occupy one actual d-dimensional D-space. There are d such nonzero subspaces by AB norm1, so their ranks sum to at most d and each rank is at least1. Every rank equals1. This checks the all-direction, rather than one-direction, quantifier in A.

### 4.3 Rank1 factors and compatibility

Rank1 and Frobenius norm1 allow M_ab=u_ab v_ab^T with both factors unit. Then M_ab M_ab^*=u_ab u_ab^* and M_ab^*M_ab=conjugate(v_ab) v_ab^T. Thus each P-sum is a resolution by d unit C-vectors; conjugating each Q-sum gives the corresponding resolution by d unit D-vectors. A square column matrix U with UU^*=I is unitary, so these are genuine orthonormal bases at every fixed a and every fixed b.

Further,

tr(M_ab M_a'b'^*)=<u_a'b',u_ab><v_a'b',v_ab>.

Identity (1) is therefore exactly the global orthonormality of all d^2 product vectors u_ab tensor v_ab. There are d^2 vectors in a d^2-dimensional CD-space, hence a complete basis. Independent row/column frames without this global condition do not pay AB/CD.

### 4.4 All-phase preservation and converse arrays

For phi=d^-1 sum_(a,b) exp(i theta_ab)|a,b> tensor u_ab tensor v_ab:

- **Normalization:** the orthogonal AB labels and unit product factors give norm1.
- **AB:** tracing CD uses global orthogonality to leave only equal ab, giving I/d^2.
- **CD:** tracing AB gives d^-2 times the sum of projectors onto the complete product basis, again I/d^2.
- **AC:** for a!=a', the fixed-b v-inner product vanishes term by term; diagonal a uses the fixed-a u-basis.
- **AD:** fixed-b u-inner products kill the off-diagonal a blocks; diagonal a uses the fixed-a v-basis.
- **BC:** fixed-a v-inner products kill b!=b'; diagonal b uses the fixed-b u-basis.
- **BD:** fixed-a u-inner products kill b!=b'; diagonal b uses the fixed-b v-basis.

Every term uses the identical tensor factors/phases. Thus independently supplied factors satisfying **all** stated hypotheses really give the converse certificate. Conversely C implies A by choosing theta=t h. No tensor or such arrays are claimed actually constructed.

No coordinate division, generic rank assumption or simple singular spectrum is used. Zero entries and reciprocal factor phases are harmless; the full conditional blocks are nonzero only because the actual AB reduction says so.

## 5. Direct reconstruction: defect averages and every constant

Put Q_ab=M_ab^*M_ab, P_ab=M_ab M_ab^*, p_ab=tr(Q_ab^2)=tr(P_ab^2), and E=sum_(a,b)(1-p_ab). Q_ab is positive with trace1.

For AC and a!=a', let C_b=M_ab M_a'b^*. The phase character is exp(i(theta_ab-theta_a'b)). Different b give different characters of the **full independent** phase torus. Expanding the Frobenius norm square and extracting the constant character kills every cross-b term. Diagonal A blocks already have zero defect. Hence

mean defect_AC^2=d^-4 sum_b sum_(a!=a') ||M_ab M_a'b^*||_F^2
                 =d^-4 sum_b sum_(a!=a') tr(Q_ab Q_a'b).

Cyclic trace gives the second equality. At each b, the original BD identity sum_a Q_ab=I gives the ordered-pair sum

tr((sum_a Q_ab)^2)-sum_a tr(Q_ab^2)=d-sum_a p_ab.

Summing b gives d^2-sum_(a,b)p_ab=E. This proves the exact E/d^4 constant.

For the real phase-coordinate Jacobian, fix an ordered a!=a' block. Each coefficient C_b contributes to exactly two coordinate derivatives, with opposite signs and equal norm. Across different b these coordinate labels are distinct. Summing squared derivative norms over all coordinates therefore gives **twice** the coefficient squared-norm sum. Different matrix blocks are disjoint in the Frobenius norm; no cross-block cancellation is being assumed. Thus J_AC^2=2E/d^4.

For the other three crossed reductions the same argument has the following exact coefficients and complementary sums:

| Reduction | Coefficient | Squared norm after cyclic trace | Same-tensor identity |
|---|---|---|---|
| AD, a!=a' | M_ab^T conjugate(M_a'b) | tr(P_ab P_a'b) | sum_a P_ab=I, from BC |
| BC, b!=b' | M_ab M_ab'^* | tr(Q_ab Q_ab') | sum_b Q_ab=I, from AD |
| BD, b!=b' | M_ab^T conjugate(M_ab') | tr(P_ab P_ab') | sum_b P_ab=I, from AC |

For example the AD norm equals tr(P_ab^T P_a'b^T)=tr(P_a'b P_ab); cyclicity yields the displayed order. Frobenius norm is unchanged under transpose. The diagonal blocks are fixed by their own original marginal sums, so no omitted diagonal defect or derivative remains.

AB is conjugated by an AB diagonal unitary and stays I/d^2. CD is unchanged because tracing AB cancels the phase at each ab. Thus all four crossed means equal E/d^4, all four Jacobian squares equal2E/d^4, and the sum over all six mean defects is4E/d^4.

Finally, positive eigenvalues of Q_ab sum to1, so p_ab<=1, with equality exactly for rank1. There is no cancellation between the nonnegative terms of E. The zero-equivalences and strict positive consequences at S3:70–72 follow. E>0 yields some disrupting auxiliary phase/direction for each crossed marginal; it does not invalidate the original AME point. No E>0 example or existence premise is silently supplied.

## 6. Direct reconstruction: finite jets and all six callers

Fix arbitrary real h. For each a!=a' combine the AC/AD coefficients in a direct sum,

C_b=(M_ab M_a'b^*, M_ab^T conjugate(M_a'b)),

with frequency omega_b=h_ab-h_a'b. The off-diagonal pair of actual blocks is d^-2 sum_b exp(it omega_b) C_b.

Group equal frequencies **before** taking a Vandermonde matrix: distinct values lambda_1,...,lambda_r have r<=d, with A_j the full matrix-coefficient sum of that class. The original AME point gives sum_j A_j=0 (order0). The printed derivatives1,...,d-1 include the needed1,...,r-1 equations sum_j lambda_j^p A_j=0 after removing the common nonzero i^p factor.

The Vandermonde determinant is nonzero because these r values are distinct, even if one is0 or arbitrarily close to another. Applying its inverse coordinatewise in the direct-sum matrix space gives every A_j=0. For r=1 the order0 equation alone does so; there is no illegal equal-frequency division. Coefficient matrices may themselves vanish; they were never presumed independent.

Those zero class sums make AC and AD fixed for every real t. AB/CD already stay fixed. For each same pure psi(t), flatten across AC|BD into its actual square d^2-by-d^2 coefficient matrix N. NN^*=I/d^2 implies dN is unitary, hence N^*N=I/d^2, so the transposed BD reduction is also I/d^2. AD|BC pays BC the same way. Unit-modulus phases preserve normalization throughout.

Thus F2=>F3=>F1. F1 gives every derivative and hence F2, closing the equivalence. This works for all real frequencies/times, not merely a periodic/rational flow or a finite time sample. It neither asserts that first-order tangency for one h integrates nor that the derivative order bound is sharp. The distinction from A's quantifier **every h** is essential and correctly made.

## 7. Direct reconstruction: finite rational-space union and resonance

For a fixed row pair, an admissible partition has each **full direct-sum matrix** block sum zero. There is at least one such partition: the one-block partition uses the original order-zero identity. No trace-only substitute is permitted.

For any admissible partition collection P, L_P imposes equality of omega_b within each chosen block. These are the printed homogeneous integer-coefficient mixed-difference equations, so L_P is a rational linear subspace of the **real** h-space. The actual amplitudes determine which partitions are allowed, not the coefficient field of their linear equations.

- **Forward:** a complete AME flow has zero sums on its actual frequency classes by §6, so these classes are an admissible collection and h lies in its L_P.
- **Converse:** h in L_P may merge distinct proposed blocks, but cannot split one. Every actual frequency class is a union of whole admissible blocks, hence has zero coefficient sum. Section6 then pays the entire six-marginal flow. Extra collision hyperplanes are included, not removed as generic exceptions.
- **Finiteness:** finitely many partitions of a finite alphabet and finitely many external row pairs give a finite union, without any computational classification or enumeration.

All additive h_ab=alpha_a+beta_b lie in every L_P. The linear parameter map has only the one-dimensional kernel (all alpha shifted equally and beta oppositely), so its image has dimension2d-1. These are genuine local phase operations.

If all conditional ranks are1, §4 gives full h-space. If some rank exceeds1, no L_P can be the full space, because then all h and, at t=1, every independent theta would preserve AME, contradicting §4. Every L_P is proper. Choose a nonzero real linear form vanishing on each proper space; the finite product is a nonzero polynomial and cannot vanish on an open set. Thus the finite closed union has empty interior and open dense complement. Nothing implies closure under sums of generators from different L_P.

For nonresonant h, every mixed difference with a!=a', b!=b' is nonzero. Thus the omega_b are distinct at **every** row pair. An admitted full flow has singleton coefficient sums C_b=0; in particular M_ab M_a'b^*=0 for all fixed b and unequal a. The same nonzero-orthogonal-subspace dimension argument of §4 forces every conditional rank1. The contrapositive gives at least one rectangle resonance for each admitted full flow if any block is entangled. No actual generator/state is chosen, no resonance is imposed WLOG on the original AME point, and no existence of an additional nonlocal flow is assumed.

## 8. Original-target and assurance limits

These derivations provide the four packets' claimed universal coupling/defect/flow theorems at the **same actual tensor and all six marginals**. The field is complex throughout; AD/BD transposes were explicitly paid. All coordinate zeros, rank/gauge degeneracies, collisions, constant/local phases, zero E and arbitrary physical product bases are included. No missing non-elementary mathematical dependency was needed under these claims.

The auxiliary AB diagonal operation is generally not four-party product-local. Its support pattern is unchanged and its generic point can leave the AME locus. An arbitrary original AME point need not have any extra nonlocal complete-flow direction. Therefore the existence of the unavoidable local2d-1 phase space, the rational-space classification, E/Jacobian values, or a nonresonant-flow obstruction supplies **no strict support delta**. The author states this limitation correctly. A support-to-additional-necessary-flow/conditional-rank theorem or an eligible explicit witness is still missing.

Original minimum, improved actual lower bound and improved actual witness remain OPEN. Historical I48/J49/J50, native/catalogue and external-status claims are not premises and receive no new credit. All original STOP/HOLD/ZERO and process findings, N4 UNKNOWN/historical exit unestablished and auxiliary214 STOP remain. This verdict is only same-harness WRITTEN review of the frozen scope, not formal/kernel/human/configured-family/executable/independent-model or novelty acceptance.
