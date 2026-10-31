# S1 continuation: a finite exact jet certifies an entire physical phase flow

Owner **PhysicsAME46-2**. Native prewrite observation **`Tue Oct 27 15:00:16 PDT 2026`**, not exact write/completion/runtime. **WRITTEN only**, same-harness and unreviewed. This is a new append-only derivation from the same S1/S2 definitions and the elementary identities in the preceding two packets. No scientific execution, chosen generator/state/control, source expansion or old proof input.

## 1. Full original-object caller and theorem

Fix ANY normalized arbitrary-complex AME(4,6) tensor and ANY physical product basis; `d=6`, `M_ab=(d psi_abkl)_(k,l)`. Let `h=(h_ab)` be ANY real array, with no rationality, nondegeneracy or genericity restriction. The auxiliary phase flow is

`psi(t)_abkl = exp(i t h_ab) psi_abkl`,  `t` any real number.

The following three conditions are equivalent:

**(F1)** `psi(t)` is AME for EVERY real t, with all SIX marginals of this same tensor equal to `I/d^2`.

**(F2)** For EACH of the TWO crossed marginals AC and AD, every derivative at zero of order `p=1,...,d-1` is the zero MATRIX.

**(F3)** For each `a!=a'`, partition the b labels according to equal real frequencies

`omega_b=h_ab-h_a'b`.

For EVERY block B of this actual equal-frequency partition, BOTH matrix sums vanish:

`sum_(b in B) M_ab M_a'b^* = 0`,

`sum_(b in B) M_ab^T conjugate(M_a'b) = 0`.                                              (11)

All variables and phase collisions are included. This is an exact infinite-time/all-six-marginal certificate from a finite jet of TWO actual marginal matrices. No sampling, numerical tolerance or assumption that first-order tangency integrates is used. No sharpness of the order bound is claimed under the physical constraints.

## 2. Full proof: (F2) implies (F3)

AB and CD stay maximally mixed for every t as in the preceding packets. Diagonal A blocks of both AC and AD are also fixed for every t by the original same-tensor marginal identities. For a fixed off-diagonal A block `a!=a'`, put the TWO matrix coefficients in a direct-sum vector space:

`C_b = ( M_ab M_a'b^*, M_ab^T conjugate(M_a'b) )`.

The actual off-diagonal pair of marginal blocks is

`d^(-2) sum_b exp(i t omega_b) C_b`.                                                     (12)

Let `lambda_1,...,lambda_r` be its DISTINCT frequencies, and `A_j=sum_(b:omega_b=lambda_j) C_b`. There are `r<=d` frequencies. The original AME point gives `sum_j A_j=0`, the order-zero equation. Condition (F2) supplies, for all `p=1,...,r-1`,

`sum_j lambda_j^p A_j=0`.

Together these are the square Vandermonde system for powers `p=0,...,r-1`. Its determinant is the product of all pairwise differences of the DISTINCT lambda values, so it is nonzero. Applying the inverse to each coordinate in the finite-dimensional direct-sum matrix space gives EVERY `A_j=0`, exactly (11).

This is a symbolic theorem for arbitrary real frequencies, not a computation of frequencies for a selected h. If frequencies coincide, they are grouped BEFORE the Vandermonde step. If r=1, the original order-zero equation alone already gives its sole A_j=0; no nonzero difference or higher derivative is demanded in that case.

## 3. (F3) implies (F1), paying all six marginals

Grouping (12) by its actual frequencies and using (11) shows that EVERY off-diagonal A block of AC and AD vanishes for every real t. Their diagonal blocks are already fixed, so AC and AD equal `I/d^2` for every t. AB and CD also remain fixed as noted above.

For completeness, the other crossed pair is not independent data: flatten the SAME pure `psi(t)` across AC|BD into the square coefficient matrix N. `rho_AC=NN^* = I/d^2` implies the square matrix `dN` is unitary, hence `N^*N=I/d^2`. The BD reduced matrix is its transpose under the explicit coefficient convention, so BD also equals `I/d^2`. Applying the identical square-isometry argument to AD|BC gives BC. This proves all SIX actual marginals without independently choosing a complementary reduction or eigenbasis.

No invertibility away from the AME locus is presumed: `NN^*=I/d^2` itself proves the required invertibility and unitary identity at each t. The flow is normalized for every t because every coefficient was multiplied by a unit-modulus phase.

Finally (F1) trivially gives every derivative in (F2), completing the equivalence. Alternatively (F1) gives (F3) by finite-exponential linear independence; that is already proved by the Vandermonde argument and needs no additional analytic import.

## 4. Forward/converse boundary and exact failure to avoid

The forward caller takes an original eligible tensor and any specified h. It computes no new tensor and assumes no phase robustness. Conditions (F2) or (F3), if established WRITTEN for its actual conditional matrices, are sufficient to certify the entire flow. The converse is necessary: a claimed full AME flow must satisfy the same matrix conditions. No support pattern or rank condition is substituted for those matrices.

Merely having the original AME point gives only the order-zero frequency-sum identity. A first derivative for ONE h supplies only its first frequency moment, not (11). The Vandermonde proof needs the complete listed moments or an independently paid smaller-frequency case. I do not claim a physically realized counterexample to a lower jet order, nor that the dimension bound is optimal; I identify precisely the unpaid higher-moment implication. In contrast, the earlier first-order theorem quantified over ALL h, which is a stronger condition and is not being silently substituted here.

All coordinate zeros, coincident frequencies, constant/local phases and rank degeneracies are covered. No division by a tensor coordinate, frequency difference between equal values or derivative is used. Matrix-valued cancellations must be proved in full; entrywise diagonal tests do not suffice.

## 5. What this does and does not advance

This is a genuine finite certificate reduction: infinitely many times and six physical marginals reduce to finitely many exact derivatives of two actual crossed matrices, with a converse and an explicit degeneracy rule. It is not a coordinate restatement of one AME point or an assumption of phase separability. Together with (11), it gives a precise all-variable coupling obstruction to an alleged phase family.

Every phase on this auxiliary orbit preserves the original coefficient zero pattern. Therefore this theorem ALONE cannot improve the support minimum, exhibit a sub-benchmark object, or justify restricting original tensors to any phase-robust subclass. The original minimum and actual lower/upper witness gates stay OPEN. No numerical ledger, I48/J49/J50 union, native result or priority/source status changes.

The next admitted structural question is the shape of the set of ALL real generators h satisfying (F1), not a selected h test. Equation (11) suggests a finite union of linear spaces specified by exact frequency-collision equalities and actual zero-sum matrix blocks. That claim will need its own proof, including possible mergers of frequency classes; it is not assumed here.

Imports: finite-dimensional matrix algebra and partial traces as displayed; derivatives of finite exponentials; Vandermonde determinant/invertibility; square isometry equals unitary. These are ordinary elementary facts, not old science/source imports. Main's model/public-book equivalence, full parent reads, actual frozen peer returns, stronger verification and novelty remain unpaid. All STOP/HOLD/ZERO/history controls, N4 UNKNOWN/historical-exit UNESTABLISHED and auxiliary214 STOP persist; no new GO or scientific execution.
