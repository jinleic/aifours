# No hidden-factor/rate escape to infinity: compact PH7 solution set at a symbolic reference shift

Owner MathResearch96h-2 / math-1. Actual `/bin/date` BEFORE this NEW manuscript write: **Mon Oct 26 07:22:06 PDT 2026**. **WRITTEN AUTHOR-CANDIDATE, UNREVIEWED.** No scientific interpreter/calculator/eval/CAS/program/enumeration/solver/LP/replay/checker/test/build/CLI/nested agent/new GO. All proofs are conventional exact symbolic matrix/polynomial/finite-probability arguments, not machine/kernel checks.

## 1. Exact theorem and original open point

Fix the original z=b²/d²=8/9 target. Rescale time by d>0 and rename the dimensionless parameters so d=1,a=c+1,b²=8/9. This is an exact time change, not a chosen numerical parameter trial. Put

    D_c(s)=(s+c)((s+c+1)²+b²)²,
    K_c=D_c(0), H_c(s)=K_c/D_c(s), c>0.

Let S_c be ALL actual seven-state PH pairs(alpha,T) with T Hurwitz Metzler, omega=−T1>=0, alpha>=0,alpha1=1 and transform H_c. For every such pair the SAME characteristic/numerator equations give

    det(sI−T)=D_c(s)Q(s),
    alpha adj(sI−T)omega=K_c Q(s),
    Q(s)=s²+p s+q, p,q>0.

The hidden quadratic may have real, repeated OR nonreal roots. No topology/boundary/support/holding pattern is fixed.

**Theorem candidate.** For EVERY FIXED c>0:

1. The coefficients p,q of ALL actual pairs in S_c are bounded above by some finite constant depending on c, unless S_c is empty (when the statement is vacuous).
2. The ENTIRE physical solution set S_c in the original alpha/T coordinates is compact, or empty. Thus neither hidden cancellation roots nor physical holdings/off-diagonal/exit rates can escape to infinity within actual target PH7 solutions.
3. Actual PH7 existence is independent of c>0: existence at ANY symbolic reference c_* is equivalent to existence at EVERY c>0, via the explicit proper PH normalization in §8. Therefore ONE compact reference S_(c_*) represents the whole original c/d family, without choosing a numerical parameter instance/probe.

This closes an unbounded-realization escape mechanism and gives a compact EXISTENCE domain, not its emptiness, a computable bound, actual PH7 witness or minimum8 theorem. Arbitrary ordered-A/TEN and balanced-B intersections remain OPEN/minimum{7,8}.

## 2. Precise input and current global assurance

The only model-specific correctness input needed for the compactness proof is **no actual PH representation of H_c with at most SIX states** at8/9. Its complete needed proof is now supplied in AppendixA of the266LF `PH7-standalone-global-ordered-A-or-balanced-B-equivalence-v1.md`, SHA256 `3815c4d699735797090dbd974f522828363c02931b604d8f36af438f00d7ffc6`. Current parent `PH7-standalone-global-equivalence-entire-parent-v1.md`, SHA256 `934d16b85347c025690aba9344b2d7ad8bb742e4ad222074bed0fc8fb6976ba0`, has ACTUALLY been read COMPLETE: it adopts the FULL266 body after both301/207LF returns. The CURRENT NR-DOM/NR-SHARED operative coverage gap is discharged PROSPECTIVELY; no old missing source read/gate is retroactively repaired.

A fresh gate for this NEW compactness proof must still supply/reconstruct its consumed lower<=6 input or state that exact named ordinary-written boundary. The existing266 review is not a verdict on the new proof below. The later141LF renewal/contact and174LF four-simplex packets are SEPARATE UNREVIEWED and NOT correctness premises here. Old I/O/raw Perron coordinates motivate §8, but no old global-stability assertion is silently used instead of the explicit argument.

Classical background is finite polynomial/real compactness, finite CTMC nonnegative semigroup/resolvent identities, ordinary finite stochastic-matrix Perron/recurrent-class structure, Laurent expansion and finite linear algebra. The specialized rank-loss/absorption argument below is proved; no external phase-type-closure theorem is imported by name alone. No novelty/priority clearance for this general compactness mechanism is claimed.

## 3. Assume unbounded hidden quadratics and take a DEGREE-DROPPING limit

Suppose S_c contains a sequence(alpha_n,T_n) with p_n+q_n→infinity. Both coefficients are positive because Q_n is real monic Hurwitz quadratic. Set

    ell_n(s)=Q_n(s)/(1+p_n+q_n).

After a subsequence, the two nonnegative normalized coefficients converge. The s² coefficient tends0, while the s/constant coefficients sum to1 in the limit. Thus

    ell_n(s) -> ell(s)=a1*s+a0,
    a1,a0>=0, a1+a0=1.                            (DROP)

In particular ell is nonzero, degree0 or1, and ell(s)>0 for every real s>0. This covers BOTH real and nonreal/colliding hidden roots, without assigning individual roots or using a magnitude trial. It is precisely the loss of at least ONE finite hidden mode that will produce a smaller positive realization.

Adjoin an ACTUAL absorbing eighth state to each proper PH pair:

    C_n=[ T_n omega_n
           0     0 ],       omega_n=−T_n1,
    R_n(s)=(sI−C_n)^−1.

C_n is a conservative finite CTMC generator, not a free raw positive realization. For EVERY real s>0 the semigroup integral gives

    R_n(s)>=0, R_n(s)1=(1/s)1,
    0<=each entry<=1/s.                            (BOUND)

The characteristic is `s D_c(s)Q_n(s)`. Each entry is therefore a polynomial of degree<=7 divided by `s D_c(s)ell_n(s)`, after scaling its adjugate numerator by1+p_n+q_n. The denominators converge to the nonzero `sD_c(s)ell(s)` at every positive s.

Choose EIGHT arbitrary distinct symbolic positive real arguments. At those points (BOUND) and denominator convergence bound the values of each numerator polynomial. The fixed invertible Vandermonde map then bounds all its coefficients. This is a mathematical compactness proof, not a numerical parameter probe or a tool evaluation at selected arguments. There are only finitely many matrix entries/coefficients, so pass to ONE common subsequence with every numerator coefficient convergent. Hence for ALL real s>0

    R_n(s) -> R(s),

where R is a REAL rational8×8 matrix, entrywise nonnegative, with row sums1/s. It inherits the entry bound1/s. Its possible finite poles come from sD_c(s)ell(s); cancelled coincidences cause no problem. The inherited large-positive-s bound forces every entry to be O(1/s), even if a preliminary numerator had the same/higher degree than the limiting denominator.

## 4. The limiting resolvent has a stochastic IDEMPOTENT projection of rank<=7

For any s,t>0 the ordinary resolvent identity passes to the common limit:

    R(s)−R(t)=(t−s)R(s)R(t),
    R(s)R(t)=R(t)R(s).                             (RES)

Since R is rational and O(1/s), the coefficient limit

    Pi=lim_(s→infinity) sR(s)

exists. Pi is nonnegative and row-stochastic. Letting s→infinity in(RES) gives `Pi R(t)=R(t)=R(t)Pi`; then letting t→infinity gives `Pi²=Pi`. It is a genuine stochastic projection, not an arbitrary singular matrix.

The exact trace formula retains algebraic multiplicities, including Jordan blocks:

    tr R_n(s)=1/s+D_c'(s)/D_c(s)+ell_n'(s)/ell_n(s).

Thus

    tr R(s)=1/s+D_c'/D_c+ell'/ell,
    tr Pi=1+5+degell in{6,7}.                      (RANK)

An idempotent has eigenvalues0/1, so k=rankPi=trPi<=7. At least ONE of the original EIGHT augmented CTMC states has genuinely been lost. No inference from a numerator title/zero or an unobserved rate cancellation substitutes for this exact trace/rank calculation.

The eighth absorbing row survives explicitly: `e8^T R_n(s)=e8^T/s`, hence `e8^T R(s)=e8^T/s` and `e8^T Pi=e8^T`.

## 5. FULL positive factorization of the projection, with the absorbing class retained

For completeness factor a finite stochastic idempotent Pi as

    Pi=C D,       D C=I_k,
    C>=0,D>=0, C1=1,D1=1,                         (PROJECT)

with k=rankPi. Here is the finite proof. Put Pi in its transient/recurrent-class form as a discrete-time stochastic matrix. Every irreducible recurrent block is itself idempotent. Its Perron eigenvalue1 is simple and idempotence permits only eigenvalues0/1, with no Jordan blocks; it therefore has rank1, all rows equal to its positive stationary probability row. The transient block B satisfies B²=B but has spectral radius<1, so B=0. Each remaining transient row is a convex mixture of those class-stationary rows, since multiplication by the recurrent blocks leaves it fixed. Take D rows to be the stationary rows supported on each recurrent class, and C entries to be the corresponding class weights (class indicator values on recurrent states). They are nonnegative row-stochastic, DC=I and CD=Pi. This proves(PROJECT), not a hidden nonnegative-inverse assertion.

Because row8 of Pi is e8^T, one recurrent class is the SINGLETON eighth state. Denote its index by *. In this canonical factorization

    D_*row=e8^T, C_8row=e_*^T, D e8=e_*.

Other class-stationary rows have disjoint support from8. Thus the special absorbing state cannot be lost or relabeled as an unproved output vector.

## 6. Construct the smaller ACTUAL Markov generator directly from the limit

Set `R_eff(s)=D R(s) C`, a k×k rational matrix. It is nonnegative, has row sums1/s, and inherits(RES), because CD=Pi and PiR=R=RPi. Also

    R_eff(s)=I_k/s+G/s²+O(s^−3)

for a finite REAL matrix G, since DPiC=I. Compare the1/t coefficient in its resolvent identity as t→infinity. The left side is `R_eff(s)−I/t+...`; the right side is `R_eff(s)+[R_eff(s)G−sR_eff(s)]/t+...`. Hence

    R_eff(s)(sI−G)=I,
    R_eff(s)=(sI−G)^−1.                            (EFFECTIVE)

For i!=j, the nonnegative entry `(R_eff)ij=Gij/s²+O(s^−3)` forces Gij>=0. Row sums give G1=0. Thus G is a finite k-state CTMC generator, not a generalized inverse/pencil without a sign certificate. The special row obeys `e_*^T R_eff=e_*^T/s`, so the * row of G is0: it is ACTUALLY absorbing.

Furthermore `R(s)=C R_eff(s)D` because PiR Pi=R. All positivity/normalization/special-output data needed for an absorption-time representation have now been constructed, not inferred merely from a matrix rank.

## 7. The SAME target becomes PH of order<=6 — contradiction; then compactness

Pass to a subsequence of the original probability rows `alpha_ext,n=(alpha_n,0)` converging to alpha0. For an augmented PH generator the upper-right resolvent entry gives EXACTLY

    H_c(s)=s alpha_ext,n R_n(s)e8.

Taking the common limit and(PROJECT)/(EFFECTIVE) yields

    H_c(s)=s beta(sI−G)^−1 e_*,
    beta=alpha0 C>=0, beta1=1.                    (SAME-LAW)

This is the Laplace transform of the hitting/absorption time of the actual absorbing state * in the k-state CTMC, including a possible atom beta_* at time0. But the original proper target has `H_c(s)→0` as s→infinity, so beta_*=0. Also H_c(0)=1, so this hitting time is finite with probability1. Any other closed class is unreachable from the initial law; removing unreachable states and the distinguished absorbing state leaves a proper Hurwitz PH representation with at most `k−1<=6` transient states. All remaining reachable states must eventually reach *, otherwise a reachable nonabsorbing closed class would contradict probability1. This is the exact row/input/exit-positive smaller realization, not a mere lower McMillan degree.

The supplied lower<=6 theorem excludes it. Therefore an unbounded sequence p_n+q_n is impossible: **ALL actual hidden quadratic coefficients p,q are bounded for fixed c**. This argument never assumed their roots real or chose an asymptotic parameter instance.

Physical compactness now follows. The trace gives the sum of actual holdings

    sum_i(−T_ii)=c+4(c+1)+p.

In a substochastic Metzler PH matrix every off-diagonal and exit is bounded by its own nonnegative holding rate. Thus every entry of T/omega is bounded uniformly on S_c; alpha belongs to a compact simplex. S_c is also CLOSED. Indeed the lower<=6 barrier makes every actual PH7 initially reachable; transience gives exit co-reachability. The positive entrance/exit Perron comparison against the target's leading exp(−ct) term proves rho(T)=−c. Consequently every eigenvalue has real part<=−c. A finite matrix limit inherits that strict Hurwitz margin c>0 by eigenvalue continuity. Row/input/exit inequalities are closed, and its positive-s inverse/transfer converges to H_c. It is again an actual target PH7 pair. Therefore S_c is closed and bounded, hence **COMPACT (or EMPTY)**.

No explicit value of a uniform coefficient/rate bound has been computed or supplied, and compactness does NOT identify an admissible solution. It does not admit a finite grid, LP campaign, scientific launch or interval certificate by itself.

## 8. Exact physical reference-shift map — ALL c>0 from one symbolic reference

Suppose an actual pair(alpha0,T0) exists at ANY symbolic c0>0. Write

    D_z(y)=y[(y+1)²+b²]²,
    G0=T0+c0 I, beta0=alpha0, eta0=omega0/D_z(c0).

The just-proved Perron comparison gives rho(G0)=0; eta0 is nonnegative and exit-co-reachable from every state. Rational equality gives

    beta0(yI−G0)^−1 eta0=1/D_z(y).

For ANY other c>0 set

    h_c=(cI−G0)^−1 eta0>0,
    S_c0=diag(h_c),
    T_c=S_c0^−1(G0−cI)S_c0,
    omega_c=S_c0^−1 eta0,
    alpha_c=D_z(c) beta0 S_c0.                     (SHIFT)

The inverse is an entrywise nonnegative Metzler resolvent and all h_c entries are strictly positive by exit paths. Also `beta0 h_c=1/D_z(c)`. Therefore alpha_c is a probability row, T_c is Hurwitz Metzler with rho=−c, and

    T_c1=−omega_c,
    alpha_c(sI−T_c)^−1 omega_c
       =D_z(c)/D_z(s+c)=H_c(s).

The graph/zero transition pattern and PH order are preserved by positive diagonal scaling and diagonal shifting. This proves existence at one c iff existence at EVERY c, rather than assuming an arbitrary similarity preserves row/exit ties. It does NOT claim the raw beta0/eta0 were already normalized for a different shift.

Consequently choose an ARBITRARY SYMBOLIC reference c_*>0. Its compact set S_(c_*) represents the ENTIRE original positive-c/d family via(SHIFT); no chosen numerical rate instance/probe is used or authorized. Bounds for the actual matrices at varying c need not be uniform as c→0 or c→infinity; the compact claim is in the fixed reference coordinates, with the exact physical map provided. Restoring d simply rescales time/rates, leaving existence/order unchanged.

## 9. What genuinely changed, first open gap and assurance

The new global mathematical consequence is that an actual PH7 solution CANNOT hide in an unbounded cancellation-root/holding-rate limit: the augmented-resolvent limit would yield an ACTUAL smaller PH law and contradict the now-supplied lower bound. The proof covers real/nonreal/repeated/coincident hidden quadratic cases, all original topologies/boundaries, zero limiting projection coordinates, possible instantaneous absorption (explicitly ruled out), and extra closed classes (trimmed only after their unreachability is proved). It is stronger than bounding a chosen uniformization rate or exploring selected trace tuples. The general compactness mechanism may be classical; no novelty credit is claimed.

**Still-open original science:** emptiness/nonemptiness of the compact actual reference S_(c_*), equivalently the full ordered-A/TEN OR balanced-B actual coefficient/row intersection. No explicit compact box value, separator valid over ALL outer data, PH7 witness, minimum8, maximal band, numerical frontier change or stronger certification is supplied. The real/complex-contact and four-simplex local B candidates remain independently unreviewed; neither their headlines nor this compactness statement proves B empty, and A remains.

This is a complete NEW proof needing its OWN ENTIRE mathematical AND dependency/application gate, with the needed lower<=6 source supplied. The parent266 adoption is not retroinserted acceptance. Old source/read/gate histories remain immutable. Compactness/proof success does not cure any process finding or make old leads post-ACK discoveries/preregistration.

All substantial derivation was saved in checkpoint077 before this manuscript. Work follows ACTUALv119RETURN→NEWwholeprimaryACKWRITTEN/SENT before primary sources/reasoning. NEWcadence071→072FULL33m29s/firstlate30m36s/parentv32, distinctprematureturnend/v21 and all older exactness/cadence/opaque/documentary/importpin/ZEROwithdrawnprobe-guidance histories remain permanent. No falseblind/cleanthought-runtime-access-countcensus/falsity-execution-from-process inference. Only exact WRITTEN/source/metadata operations; no machine/kernel/formal/human/configured-family/executable/novelty/SOTA/priority acceptance/newGO/owner/deadline reset. Same18/exclusiveOWN/HOLD/October27sciencecutoff11:05:38/deadline12:35:38/<=30minsubstantivecheckpoints/noearlyfinalpark/roundcloseout.
