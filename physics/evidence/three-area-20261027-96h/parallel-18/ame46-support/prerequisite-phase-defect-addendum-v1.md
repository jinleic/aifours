# S1 continuation: exact mean phase defect equals conditional linear entropy

Owner **PhysicsAME46-2**. Actual native prewrite observation **`Tue Oct 27 14:58:40 PDT 2026`**, not exact write/completion/runtime. **WRITTEN only**, no scientific execution or numerical/selected-state probes. Append-only continuation of `prerequisite-derivation-v1.md`; no changed earlier proof or premise. Full original quantifiers and controls remain.

## 1. Statement for the same arbitrary physical tensor

Fix ANY normalized arbitrary-complex AME(4,6) tensor and ANY physical product basis. Retain `d=6`, `M_ab=(d psi_abkl)_(k,l)` and all actual-object identities (1)–(2) of the first derivation. For an arbitrary independent phase array let `psi(theta)_abkl=exp(i theta_ab) psi_abkl` and define

`Q_ab=M_ab^* M_ab`, `P_ab=M_ab M_ab^*`, `p_ab=tr(Q_ab^2)=tr(P_ab^2)`.

Each `Q_ab` is positive semidefinite of trace one. Thus `p_ab` is exactly the purity of a normalized conditional two-party pure state's one-body reduced matrix; it is not an independent free parameter. Set

`E = sum_(a,b) (1-p_ab)`.

Let `<f>` mean normalized averaging over the FULL independent phase torus, equivalently constant-coefficient extraction for the finite Laurent polynomials used below. This is a WRITTEN character identity, not sampled phases or an interpreter integration. For EACH of the four crossed pairs `X` in `{AC, AD, BC, BD}`,

`< || rho_X(psi(theta)) - I/d^2 ||_F^2 > = E/d^4`.                                      (9)

AB and CD have zero defect identically for every phase array. Consequently the full six-marginal mean squared defect is `4 E/d^4`. In particular the FOUR crossed means agree, despite being built from different actual flattenings.

For the actual differential at the original AME point define

`J_X^2 = sum_(x,y) || partial rho_X(psi(theta))/partial theta_xy at theta=0 ||_F^2`.

Then for EACH crossed pair,

`J_X^2 = 2 E/d^4`.                                                                      (10)

No physical two-party phase robustness, rank restriction or support pattern is assumed. Equations (9)–(10) quantify the missing coupling for EVERY original eligible tensor/basis.

## 2. Complete derivation for AC

Write `C_(a,a',b)=M_ab M_a'b^*`. For `a=a'`, the AC marginal block is `I/d^2` for all phases by the original fixed-a identity. For `a!=a'`, it is

`d^(-2) sum_b exp(i(theta_ab-theta_a'b)) C_(a,a',b)`.

Distinct b values give distinct characters of the independent phase torus. On expanding the squared Frobenius norm, the normalized character mean is zero unless the b labels agree. There is no assumed orthogonality of the coefficient MATRICES. Therefore

`<defect_AC^2> = d^(-4) sum_b sum_(a!=a') ||M_ab M_a'b^*||_F^2`

`= d^(-4) sum_b sum_(a!=a') tr(Q_ab Q_a'b)`.

The second identity is cyclicity of trace, with the conjugate transpose in the correct order. For each fixed b, the ACTUAL BD marginal supplies `sum_a Q_ab=I`. Hence

`sum_(a!=a') tr(Q_ab Q_a'b) = tr((sum_a Q_ab)^2) - sum_a tr(Q_ab^2)`

`= d - sum_a p_ab`.

Summing all b gives `d^2-sum_(a,b) p_ab=E`, proving (9) for AC. This uses BD's identity from the SAME tensor: replacing the individual blocks by independently selected AC data would leave this step unpaid.

For (10), each summand in an off-diagonal AC block has two opposite phase-coordinate derivatives, for `theta_ab` and `theta_a'b`. For a fixed ordered pair `a!=a'`, all these coordinate labels are distinct as b varies. Summing the squared derivative norms across ALL coordinates thus gives exactly twice the sum of the coefficient-matrix squared norms. Diagonal A blocks have zero derivative. The preceding trace calculation proves (10). This is an exact universal Jacobian identity, not a selected coordinate test.

## 3. All four actual crossed callers

The same finite-character proof applies with the following coefficient matrices and the explicitly indicated SAME-tensor sum identity:

| Marginal | Off-diagonal external labels | Matrix coefficient before the phase | Cross-norm trace | Sum identity paying the mean |
| --- | --- | --- | --- | --- |
| AC | `a!=a'`, sum over b | `M_ab M_a'b^*` | `tr(Q_ab Q_a'b)` | `sum_a Q_ab=I` from BD |
| AD | `a!=a'`, sum over b | `M_ab^T conjugate(M_a'b)` | `tr(P_ab P_a'b)` | `sum_a P_ab=I` from BC |
| BC | `b!=b'`, sum over a | `M_ab M_ab'^*` | `tr(Q_ab Q_ab')` | `sum_b Q_ab=I` from AD |
| BD | `b!=b'`, sum over a | `M_ab^T conjugate(M_ab')` | `tr(P_ab P_ab')` | `sum_b P_ab=I` from AC |

For AD/BD, transposition of the opposite-ordered Gram product leaves its Frobenius norm unchanged. Diagonal external blocks are fixed by their corresponding original marginal identity. The squared norms reduce to exactly the trace in the fourth column, and each final sum is `E`. This proves all four versions of (9)–(10). AB remains `I/d^2` by conjugation with the AB diagonal unitary; tracing AB cancels phases and keeps CD fixed.

## 4. Positivity, exact obstruction and converse

The eigenvalues of `Q_ab` are nonnegative and sum to one. Therefore `p_ab<=1`, with equality precisely when `Q_ab` has rank one. All terms in E are nonnegative. It follows that

`E=0 <=> every M_ab has rank one <=> every crossed mean defect is zero <=> every crossed J_X is zero`.

Together with the first derivation this is also equivalent to preservation of all six marginals for EVERY independent AB phase array. If E is positive, each crossed mean defect and each crossed Jacobian norm is positive. Therefore some auxiliary phase and some infinitesimal direction disrupt each crossed marginal. This is an obstruction to the EXTRA phase-flatness property, not an obstruction to the original AME point. No eligible tensor with E positive or zero is constructed or assumed to exist beyond the universally quantified input.

All zero coordinates and all phase/factor gauge ambiguities are allowed. No division by an entry or by E occurs, so E=0 is included rather than removed as a generic case. No eigenvalue simplicity is needed. These identities concern actual coefficient matrices, not arbitrary assigned purities; the AB norms and all four physical sums are essential.

## 5. Scope of progress and exact outstanding bridge

This supplies a quantitative universal same-tensor coupling identity beyond the first-order equivalence: conditional entanglement determines the ENTIRE mean crossed-marginal defect and the differential size for every crossed pair. It does not merely list the original polynomial constraints. It also shows exactly where the complementary marginal pays the identity.

It does NOT improve the original minimum, force E to vanish, supply a tensor or change support: the auxiliary phase orbit preserves the zero pattern and generally leaves the AME locus. A lower-bound argument would need a separate theorem relating these quantities to an admissible strict support delta for the original all-variable class; none is supplied or inferred. Individual phase completions cannot be freely varied without this coupling.

The next admitted all-variable step is to characterize an arbitrary specified one-parameter phase flow exactly, including coincident frequencies, rather than infer full-flow validity from one first derivative. The finite number of characters permits a finite exact derivative certificate. No actual generator, tensor or numerical boundary will be selected or tested.

Imports: elementary spectral theorem for a positive matrix; trace/Frobenius identities; and the normalized integral of a nontrivial integer torus character is zero (equivalently finite Laurent constant-coefficient extraction). The required character cancellation is displayed above. No old theorem, source/native catalogue, I48/J49/J50 union, modelCLI or scientific execution is an input. Original source STOP, every inherited STOP/HOLD/ZERO/process finding, N4 UNKNOWN/historical-exit UNESTABLISHED and auxiliary214 STOP remain. Parent complete reads, frozen peer review and all stronger assurance/novelty gates are outstanding.
