# CONFERENCE-GLUING rank8 v1 — no one-dimensional complex phase kernel, in every cyclic orientation

Observed before creation: **2026-10-23T14:53:38-07:00**. PhysicsRQLS10. Actual written advance on the noncommuting Schur obligation. Read with `candidate-CONFERENCE-GLUING-v1.md`; the later noncommuting note's basis metric correction remains mandatory for its own Schur formulas, but is not needed for the proof here.

**CANDIDATE WRITTEN PARTIAL.** This excludes **all arbitrary complex compatibility phases** when the fixed coefficient matrix has rank8 (rank9 was already impossible), with no phase-field assumption. It covers **every orientation of cyclic10's `1+2^4` matching relative to the first conference core**, not just the queued assay's central-negation orientation. It still assumes the two specified Et-Taoui conference-core monomial classes. It is not an H0-wide or unrestricted QLS10 no-go. No scientific program, finite enumeration, numerical arithmetic, solver, formal kernel or outside-model CLI ran.

## 1. Retain arbitrary relative permutations, phases, and zero matchings

Normalize the first core to C and the second to `C'=PCP^T`, with arbitrary P. The actual third basis has arbitrary diagonal compatibility phases, as in the main manuscript. For an arbitrary zero-matching permutation rho of nine labels, the necessary zero equations are

    M delta=0,               |delta_j|=1,
    M_(i,t)=conjugate(C_(t,i)) C'_(t,rho(i)).

Put s=i sqrt7, K=Q(s), and R=Z[1/2,s]. Every coefficient of M is zero,1,`(-3+s)/4` or`(-3-s)/4`, so M has entries in K. Under the ring homomorphism `phi:R→F7`, s↦0 and1/2↦4,

    phi(M)=N_rho=J-I-P_rho+Fix(rho).

This holds independently of P and does not require rho to be an automorphism of either core.

## 2. Every fixed coordinate of the reduced kernel vanishes

### Lemma F7

Suppose rho has f fixed points, with f positive and not divisible by7. If `N_rho z=0` over F7, then z_a=0 at every fixed point a.

**Proof.** Write S=sum_j z_j. At a fixed point a, its equation is `S-z_a=0`, hence z_a=S. At a nonfixed point i,

    z_i+z_(rho(i))=S.

On an odd cycle this recurrence forces every coordinate to be S/2. On an even cycle the coordinates alternate between u and S-u, so their sum is again the cycle length times S/2. Summing all nine coordinates therefore gives

    S=fS+(9-f)S/2,
    0=(7+f)S=fS   in F7.

Since f is nonzero modulo7, S=0, and each fixed coordinate is zero. QED.

For cyclic10's local matching f=1, so this conclusion applies in **every** orientation, without choosing a Paley-compatible labeling.

## 3. A quadratic-field equal-norm kernel vector is impossible, of any kernel dimension

For a+b s in K, its actual complex norm is

    N(a+b s)=a²+7b² in Q.

### Lemma K

Under Lemma F7's hypothesis, there is **no** vector `v∈K^9` satisfying

    Mv=0,
    N(v_0)=...=N(v_8)>0.                                  (E)

**Proof.** Clear the rational denominators of all a_j,b_j simultaneously. This preserves Mv=0 and multiplies all nine norms by the same positive rational square. Thus one may start with every v_j=a_j+b_j s in Z[s] and with their common norm c a positive integer.

If7 divides c, then

    a_j²+7b_j²=c  ⇒  7 divides a_j

for every j, since a_j² is zero modulo7. Divide the entire vector by s. Its coordinates remain in Z[s], because

    (a_j+b_j s)/s = b_j-(a_j/7)s.

Their common norm becomes c/7. Repeating this step finitely many times removes all powers of7 from the positive integer c. We obtain a vector u∈Z[s]^9 still in ker M, all of whose norms equal an integer c0 **not divisible by7**.

Reduce Mu=0 via phi. Lemma F7 says that at a fixed index a the constant coefficient of u_a is zero modulo7. Therefore

    N(u_a)=a_a²+7b_a²=0 mod7,

contradicting N(u_a)=c0 with7 not dividing c0. QED.

This is a written integer-norm descent, not an executed p-adic assay. It imports no theorem about arbitrary extension fields or primes fixed by complex conjugation.

### Exact phase-field consequence

A valid phase vector delta cannot be projectively K-valued: there do not exist a common nonzero complex scalar lambda and v∈K^9 with delta=lambda v. Otherwise its unit moduli would force the equal positive norms in (E).

This statement **does not** assume that every complex phase solution is projectively K-valued. Larger kernels can have phase solutions involving extensions or transcendental coordinates; they remain allowed. For example, rational linear equations can have unit-phase solutions involving cube roots not in K. No false descent of arbitrary torus points to K is used.

## 4. All rank8 matrices are excluded for unrestricted complex phases

### Theorem R8

If f is positive and not divisible by7 and `rank_K M≥8`, then no unit complex vector delta satisfies M delta=0.

**Proof.** Rank9 has zero kernel. If rank is8, exact Gaussian elimination over K gives a nonzero basis vector v∈K^9 for its one-dimensional kernel. The rank and kernel dimension are unchanged on extending scalars from K to C, since the same nonzero minors and zero determinant apply. Hence any complex kernel vector is lambda v for a common complex scalar lambda.

If such a vector had every coordinate of modulus1, every N(v_j) would equal `1/|lambda|²>0`, contradicting Lemma K. This excludes arbitrary complex lambda and requires no assumption that lambda is algebraic. QED.

This strengthens the noncommuting note's proposed individual rank8 norm tests: their outcome is now ruled out **universally in writing**, using only the fixed-point property of rho and the actual coefficient field. No finite rank8 list or numerical norm comparison is needed.

## 5. Consequence for the remaining Schur problem and the prepared assay

For cyclic10 every matching orientation has cycle type `1+2+2+2+2` and f=1. Therefore any local triple from the two specified conference monomial classes would require

    rank M≤7,          dim_C ker M≥2,

and its unit phase vector cannot lie projectively in K^9.

In the central-negation orientation, the written mod7 even-block argument already gives rank M≥5. Its only possible survivors are now **rank5,6 or7**, equivalently Schur-kernel dimensions4,3 or2. A one-dimensional noncommuting Schur kernel is impossible for the actual unit-phase problem, regardless of whether it has full coordinate support. The symmetry-preserving cases remain excluded by the earlier independent-phase averaging theorem.

The prepared source remains unchanged and unexecuted. Its literal output still distinguishes row-certificate exclusions from surviving **linear** kernels. If it eventually returns a rank8 linear survivor, that is not an inconsistency and not a phase witness; R8 would exclude it by a separate written composition, once that finite rank claim and this proof have actually been checked. Its frozen request has not silently been broadened to other orientations or promoted to a physical certificate.

The precise remaining scientific obligation is narrower but still real: can any actual rank5–7 noncommuting coefficient matrix support the simultaneous unit-modulus equations and the other conference moduli? The present argument does not answer it. Unknown kernels are not UNSAT; K-valued phase exclusion is not unrestricted phase exclusion when the kernel has dimension at least2.

## 6. Trust and significance boundary

The coefficient field and mod7 map are derived from the actual Et-Taoui C9 construction already read, not a claimed classification of all conference9 matrices. Row/column/transversal definitions remain the original Zhang–Cao target. All kernel, norm-descent and scalar-extension steps are written above. No first-level PSD feasibility, real-only argument, old numerical output, new runtime or scientific executable is a premise.

This complete candidate requires an actual separate reconstruction and parent review on pinned bytes. Correctness, field/import trust, scoped significance, novelty and full-target resolution are separate. Novelty remains **UNCERTIFIED**. The eighteen-slot physics-5 primary target remains UNKNOWN.
