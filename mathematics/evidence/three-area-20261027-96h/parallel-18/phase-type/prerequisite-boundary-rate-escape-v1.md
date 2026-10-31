# Definition-first continuation: fixed-order bounded-rate PH cannot approach the touching boundary

MathResearch96h-2 / math-1. Actual native observation before writing: **Tue Oct 27 14:56:01 PDT 2026**. **WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** This is the next genuinely admitted all-variable step after the density theorem, not a selected parameter experiment or an order-divergence claim.

## Exact current inputs and scope

Current S1 controls/43LF packet and its literal H definition remain the authority. The ONLY specialized new proof input is the complete195LF current candidate `prerequisite-derivation-v1.md`, SHA256 `a763a08228625177d05f98cbc18f0deddba9cdfa609c83eb983e7f5a588d0adb`, whose full density-threshold proof is required for a joint review. Its r_star is the unique implicit threshold there. It is not already parent-adopted. No old compactness, critical-generator, hidden-factor, comparison or held guide is an input.

Ordinary elementary facts used below: compactness of a bounded closed finite-dimensional cube/probability simplex and finite-subsequence selection; matrix-exponential and convergent geometric series; continuity of matrix inversion at invertible matrices; uniqueness of Laplace transforms of bounded continuous functions. The actual applications are supplied, including a potentially singular limiting subgenerator. No general PH-closure theorem is imported.

Fix ARBITRARY symbolic `c,b,M>0` and a positive integer n. Let `d=r b`, `a=c+r b`, and H_r be the exact supplied rational transform. No numerical values are chosen.

**Theorem.** There is an epsilon>0 such that no `r` with `r_star<r<r_star+epsilon` has a PH representation of dimension at most n whose EVERY holding `-T_ii` is at most M.

Equivalently, any sequence of exact PH representations with a fixed finite order ceiling, approaching the density-touching boundary from above, must have unbounded maximum holding rates. This conclusion does NOT assert existence of such a sequence or divergence of its minimum orders.

## 1. Compact limits preserve row ties, not necessarily Hurwitz stability

Suppose the theorem were false. Its negation supplies a sequence r_j tending down to r_star from above, and actual PH pairs `(alpha_j,T_j)` of dimensions at most n, all holdings bounded by M, with transfer exactly H_(r_j). This is an existential contradiction sequence, not a sampled calculation/enumeration. A subsequence has one constant dimension m<=n.

Because each T_j is Metzler with `T_j1<=0`, its off-diagonal row sum is at most `-T_j,ii<=M`. Thus all its entries lie in fixed bounded intervals and alpha_j lies in the m-dimensional probability simplex. Finite-dimensional compactness gives a further subsequence

    alpha_j -> alpha_0,
    T_j -> T_0,
    omega_j=-T_j1 -> omega_0=-T_01.

The limit has alpha_0>=0, alpha_01=1, T_0 Metzler, T_01<=0, and omega_0>=0. It may have zero eigenvalues, inaccessible closed classes or zero exit coordinates. **No Hurwitz property or PH status of T_0 is assumed.** That unsupported implication would be an error.

## 2. All positive-real resolvents nevertheless converge

Put `P_0=I+T_0/M`. It is nonnegative with row sums<=1. For EVERY real s>0,

    (sI-T_0)^(-1)
      =1/(s+M) * sum_(k>=0) [M/(s+M)]^k P_0^k.

The geometric series converges because the row norm of P_0 is at most1 and `M/(s+M)<1`. It proves positive-real invertibility even when T_0 is singular at zero. The same formula holds for every T_j, and continuity of inversion at each positive s gives

    alpha_0(sI-T_0)^(-1)omega_0
      =lim_j alpha_j(sI-T_j)^(-1)omega_j
      =lim_j H_(r_j)(s)=H_(r_star)(s).

The last equality follows directly from the supplied rational formula and `a=c+r b`, with positive denominators at every s>0. The ONE subsequence of matrices converges, so this conclusion is valid for ALL s>0; no different limiting physical data are chosen for different s.

## 3. A singular row-tied limit still cannot have an interior density zero

Let `g_0(t)=alpha_0 exp(T_0 t)omega_0`. Since P_0 is substochastic,

    exp(T_0 t)=exp(-Mt) sum_(k>=0) (Mt)^k P_0^k/k!

is nonnegative and has row sums<=1. Also `0<=omega_0,i<=M`, so g_0 is continuous and bounded between0 and M. Its Laplace transform at s>0 is exactly the positive-real resolvent above.

The target H_(r_star)(s) is nonzero. Thus g_0 is not identically zero. In the equivalent nonnegative expansion

    g_0(t)=exp(-Mt) sum_(k>=0) t^k
                         alpha_0(T_0+MI)^k omega_0/k!,

at least one coefficient is strictly positive. Hence g_0(t)>0 for EVERY t>0, even though T_0 need not be Hurwitz. This uses no unjustified closure of the PH class.

But the first packet gives a bounded continuous inverse f_star for H_(r_star), with

    f_star(xi/b)=0,      xi/b>0.

Uniqueness of Laplace transforms for continuous functions of exponential order identifies g_0 with f_star, contradicting strict positivity. Therefore the assumed bounded-rate sequence cannot exist, proving the theorem.

## 4. Exact original-object caller and failed next implication

This theorem quantifies over ALL PH topologies, reducible cases, input/exit supports, nonuniform holding rates and canceled modes. The ONLY extra restriction is the explicitly stated arbitrary finite holding ceiling M and order ceiling n. It is a genuine actual-object coupling lemma near the universal non-PH boundary, not a matrix ansatz or a selected fitted state.

It does **not** imply that minimum PH orders tend to infinity as r approaches r_star. That further conclusion would need a valid normalization/closure theorem controlling arbitrarily large rates at fixed order, or an independent proof that their singular fast-state limits cannot evade finite PH realization. The present compactness proof deliberately does not cover unbounded generator entries. No old compactness/hidden-factor result supplies that missing premise.

Nor does this theorem prove existence of finite PH representations on the strictly-positive-density side. The exact missing positive-realization/PH-characterization input from §10 of the first packet remains. Neither unbounded rates nor an order ceiling by itself provides actual alpha,T data.

## Limits and continuation

All proofs are exact WRITTEN, no scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker or selected numeric/control/boundary/decimal probe. The sequence and arbitrary M are quantified in a universal contradiction proof, not instantiated test inputs. Prior exposure is not denied; all old STOP/HOLD/ZERO/v260 consumers and every process finding remain. This document does not reconstruct or consume a legacy compactness guide, and makes no private-independence/noninfluence census.

A full review requires this COMPLETE proof AND the entire195LF first packet and literal definition/control inputs, mathematics plus dependency/application. No original critical8/9 decision, finite minimum order, novelty, formal/kernel/human/configured-family/executable or parent adoption is claimed. Same18/exclusive new root/HOLD/N4UNKNOWN historical exit unestablished/aux214STOP; research deadline2026-10-31T21:23:27.000Z; truthful20min-target/30min-max substantive cadence, no heartbeat/timer/poll/earlypark. No Git/delete/contact/publication/infrastructure or new GO.

**END — universal bounded-rate/fixed-order boundary obstruction; unbounded-rate closure and positive-density PH existence remain exact unproved next inputs.**
