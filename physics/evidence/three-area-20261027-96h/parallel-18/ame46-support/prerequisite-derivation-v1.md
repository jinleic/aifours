# S1 prerequisite derivation: one-crossed-marginal tangent rigidity

Owner **PhysicsAME46-2**. Native prewrite observation: **`Tue Oct 27 14:55:37 PDT 2026`**; not an exact write/completion/runtime clock. **WRITTEN, same-harness, not kernel/formal/executable checked or novelty-cleared.** No scientific interpreter, arithmetic program, selected-state/control probe or external source was used.

## 1. Scope, input and provenance

Input is ONLY the complete S1/S2 packet `07d0ecd8964839862d06c09fda5e444ad5713501438d3c0e04d4e42522c03b01` (all33LF, read after the saved pre-body ACK), its controls, permitted safe intake and ordinary elementary facts named below. No I48/J49/J50 result or historical bound is a premise. Main authored S2 from the registered target; no verbatim-book/public-source equivalence is certified. Prior exposure and all process/ZERO findings persist. A proof's displayed dependencies are not a clean-cognition or independent-reconstruction certificate.

The original target quantifies over **every normalized arbitrary-complex AME(4,6) state and every physical product orthonormal basis**, requiring all six marginals of the SAME tensor. Fix any such state/basis. Write `d=6`, retain `d` symbolically, and set

`T_abkl = d psi_abkl`,  `M_ab = (T_abkl)_(k,l)`.

Every index ranges independently over the full physical local alphabet. No support pattern, symmetry, equal-amplitude premise, rank restriction or nonzero-entry assumption is added. The theorem concerns all such states/bases; it does NOT assert that its equivalent extra robustness conditions hold for every AME tensor.

Introduce an AUXILIARY two-party diagonal unitary, with arbitrary real independent parameters `h_ab`:

`psi(h,t)_abkl = exp(i t h_ab) psi_abkl`.

This is generally NOT a product of four local unitaries. It is not a legal WLOG product-basis move and is not assumed to preserve AME. Its support is unchanged, but that fact supplies no existence, minimum or lower-bound conclusion. The question is whether the original AME point is first-order flat along every such direction for ONE crossed marginal.

## 2. Universal coupling theorem

For the fixed arbitrary AME tensor/basis the following are equivalent:

**(A)** For EVERY real array `h`, the derivative at `t=0` of the actual reduced matrix `rho_AC(psi(h,t))` is the zero matrix.

**(B)** EVERY actual conditional `CD` coefficient matrix `M_ab` has rank one.

**(C)** For EVERY real phase array `theta_ab`, the tensor `exp(i theta_ab) psi_abkl` is AME: all SIX actual marginals equal `I/d^2`.

Thus first-order flatness of ONE crossed marginal in all two-party diagonal directions already forces global nonlinear flatness of ALL six. Conversely, any conditional `CD` Schmidt rank above one obstructs this first-order flatness. This is a universal same-tensor coupling lemma, not a numerical support bound.

### Step 1: actual-object identities

From `rho_AB=I/d^2`:

`tr(M_ab M_a'b'^*) = delta_aa' delta_bb'`.                                                   (1)

Here `*` is the conjugate transpose. In particular EACH `M_ab` has Frobenius norm one; no conditional block vanishes. The four other pair marginals give

`sum_b M_ab M_ab^* = I` for each `a`  (AC),

`sum_b M_ab^* M_ab = I` for each `a`  (AD),

`sum_a M_ab M_ab^* = I` for each `b`  (BC),

`sum_a M_ab^* M_ab = I` for each `b`  (BD).                                               (2)

For AD/BD the directly indexed marginal is the transpose of the displayed sum; its equality to the identity is equivalent to (2). This transpose must not be silently interpreted as complex conjugation of the physical tensor.

For the AUXILIARY phase family the full AC entry is exactly

`rho_AC(h,t)[(a,k),(a',k')] = d^(-2) sum_b exp(i t(h_ab-h_a'b)) (M_ab M_a'b^*)[k,k']`.        (3)

Equation (3) is computed from this ONE tensor, not from independently chosen flattenings. When `a=a'`, phases cancel and (2) gives the required diagonal block for every `t`.

### Step 2: (A) forces (B)

For `a != a'`, differentiating (3) at zero gives

`i d^(-2) sum_b (h_ab-h_a'b) M_ab M_a'b^*`.                                                (4)

The entries of `h` are independent real variables. If (4) vanishes for EVERY `h`, its coefficient of each `h_ab` vanishes. Therefore

`M_ab M_a'b^* = 0` for every `b` and every `a != a'`.                                     (5)

This is coefficient comparison in a universal finite linear identity, not a selected numerical direction or executed probe. For fixed `b`, (5) says that the row spaces `range(M_ab^*)`, as `a` varies, are pairwise orthogonal subspaces of the SAME `d`-dimensional D-space. Consequently

`sum_a rank(M_ab) <= d`.

There are exactly `d` such blocks and each is nonzero by (1), so each rank is at least one. Equality of the dimension budget forces every rank to be one. This holds for every `b`, proving (B). No support-count census or old rank lemma is imported.

### Step 3: (B) supplies actual compatible product arrays

Since every block has rank one and Frobenius norm one, choose unit vectors `u_ab` in C-space and `v_ab` in D-space with

`M_ab = u_ab v_ab^T`.                                                                    (6)

The choice is nonunique up to reciprocal phases; no proof depends on a choice of gauge. Substituting (6) in (2) gives:

- for each fixed `a`, both families `(u_ab)_b` and `(v_ab)_b` are orthonormal bases;
- for each fixed `b`, both families `(u_ab)_a` and `(v_ab)_a` are orthonormal bases.

Indeed each is a square family of `d` unit vectors whose rank-one outer products sum to the identity. If its column matrix is `U`, then `UU^*=I`, hence `U` is unitary and its columns are orthonormal. For the v vectors, conjugating the relevant identity gives exactly the same conclusion.

Furthermore (1) gives the full, not merely row/column, compatibility identity

`<u_a'b',u_ab> <v_a'b',v_ab> = delta_aa' delta_bb'`.                                      (7)

Thus the `d^2` product vectors `u_ab tensor v_ab` are one orthonormal basis of the SAME CD-space. This global condition cannot be replaced by independent row/column frame choices.

### Step 4: (B) forces (C), checking all six callers

For arbitrary phases define

`phi = d^(-1) sum_(a,b) exp(i theta_ab) |a,b> tensor u_ab tensor v_ab`.                     (8)

- **AB:** tracing CD and using (7) gives `I/d^2`.
- **CD:** tracing AB gives `d^(-2) sum_(a,b) |u_ab tensor v_ab><u_ab tensor v_ab| = I/d^2` by the complete product basis (7).
- **AC:** an off-diagonal A block `a != a'` has, term by term in `b`, factor `<v_a'b,v_ab>=0` from the fixed-b D-basis. On the diagonal A block, summing the fixed-a C-basis gives `I/d^2`.
- **AD:** an off-diagonal A block has factor `<u_a'b,u_ab>=0` from the fixed-b C-basis. Its diagonal uses the fixed-a D-basis.
- **BC:** an off-diagonal B block `b != b'` has factor `<v_ab',v_ab>=0` from the fixed-a D-basis. Its diagonal uses the fixed-b C-basis.
- **BD:** an off-diagonal B block has factor `<u_ab',u_ab>=0` from the fixed-a C-basis. Its diagonal uses the fixed-b D-basis.

Every cancellation is inside (8), with identical phases, factors and tensor entries across all six checks. Thus (C) holds. Taking arbitrary `theta=t h` proves (C) implies (A), completing the equivalence.

## 3. Forward/converse certificate boundary, including degenerate cases

The forward caller is ANY original eligible tensor in ANY physical product basis. Its actual conditional matrices enter (1)–(5); a rank-above-one block is an exact obstruction to the proposed all-direction flatness, not an obstruction to AME itself.

For the converse caller, independently SUPPLIED unit-vector arrays satisfying ALL four row/column orthonormal-basis requirements AND the GLOBAL product orthogonality (7) produce by (8) a normalized AME tensor for every phase array: the preceding six checks are its proof. This is a genuinely sufficient same-object certificate interface. Mere existence of the arrays is not proved here. Omitting (7) is not an allowed converse, because AB and CD would then be unpaid.

Zero coordinates within the factors are allowed; no division by coordinates occurs. Individual conditional blocks cannot vanish because AB is maximally mixed. Rank-one phase/gauge ambiguity and repeated singular values elsewhere do not change the argument. Every phase array is allowed, including constant and locally factorized phases. No genericity, regular-value, perturbative remainder or nondegeneracy hypothesis is hidden.

## 4. What changes, what fails, and the next admitted step

**Established WRITTEN:** the all-variable equivalence (A)–(C), with full physical forward/converse callers. It converts an infinitesimal condition on ONE crossed marginal into an exact conditional-product characterization and all-six-marginal phase robustness. The failed implication to avoid is `an AME point at theta=0 => flat in every two-party diagonal direction`: the model supplies the pointwise marginal equalities, not the derivative identities (5). Claiming that implication without paying (5), or treating a two-party diagonal as a legal product-basis transformation, is unjustified. No example or unproved existence assertion is needed to identify that missing premise.

**Not changed:** original minimum OPEN; no new actual lower bound, actual tensor, upper witness, numerical48..60 reconciliation, actual48/noexact50/lower51 inference, or source/novelty claim. Extra robustness in (A)–(C) is NOT a WLOG restriction on the original problem. No implication that every eligible tensor has rank-one conditional blocks is claimed.

The next genuinely admitted all-variable step is to quantify the missing phase coupling from (3), rather than assume (A): compute, by a WRITTEN finite-character identity, the mean squared crossed-marginal defect over all independent phases in terms of the same conditional matrices. This uses no selected phases, states, arithmetic execution or new source, and is not an old support-family enumeration. It will be an append-only successor, not a silent edit of this packet.

## 5. Named imports and preserved controls

Only elementary finite-dimensional complex linear algebra is used: partial-trace expansion; rank-one matrix factorization/Schmidt rank; orthogonal-subspace dimension additivity; cyclic trace and Frobenius norm; square isometry equals unitary; and differentiation of a finite exponential expression/coefficient comparison. Each operative use is shown above. No historical science/source theorem is NR-imported. Main's model/book-source equivalence remains unverified; same-harness proof assessment, parent complete reads and any later frozen peer review remain outstanding. No formal/kernel, independent-family, native, executable or novelty/priority verification follows.

All inherited STOP/HOLD/ZERO, exposed-owner history and permanent process findings persist. Original source/public-status STOP remains outside the exact S1 release; old held material and guides were not opened or used as inputs. N4 UNKNOWN/incomplete, historical child exit UNESTABLISHED, auxiliary214 STOP. Metadata clock/hash/count tools only; no scientific execution or new GO.
