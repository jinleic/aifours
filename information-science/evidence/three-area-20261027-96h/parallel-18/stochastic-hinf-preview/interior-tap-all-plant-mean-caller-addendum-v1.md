# The interior-tap obstruction holds for every actual bound linear plant/controller

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:33:06 PDT 2026**. Append-only continuation of `two-endpoint-kernel-class-interior-tap-obstruction-v1.md`, SHA `4181508388f1d87614db22302ae48ead68f9d5056bb10373e8cf9dfe1ecd0851`, paying its previously qualified state-feedback caller. No new source, controller class, scientific evaluation or performance substitution.

## 1. Exact claim and relevance to the original controller-domain bridge

Fix ANY original full matrix plant of the released finite-horizon class, finite T>h>0, zero state/history, the canonical progressive E2 domain and the same deterministic stationary linear preview law class. Let 0<d<h and J be any nonzero real m-by-p matrix.

For each candidate law define its ACTUAL deterministic-input mean-control operator `U_mean:v->E u_v`, from L2([0,T-h];R^p) to L2([0,T];R^m). The theorem concerns the ability of this precise parameterized class to emulate the control functional `Jv(t-d)` on ALL inputs. It is not a new synthesis objective or a claim about the original optimal gain.

**Theorem.** For EVERY plant and EVERY law in the bound class,

`||J D_d-U_mean|| >= ||J||`.

Moreover the infimum of this distance over the bound law class for that plant is exactly ||J|| (the law u=0 attains that benchmark distance). Thus no finite-dimensional state feedback within this released class restores exact or uniform mean-control emulation of an interior tap. In particular no such law has actual control `u=Jw(t-d)` for every deterministic/admitted input.

This extends the earlier feedforward obstruction to actual physical state feedback for ALL original matrices, rather than relying only on its zero-state structural caller. It does not preclude emulation on selected inputs, weaker topologies, a different controller class or the source's full abstract window functional.

## 2. Paid mean and compact state contribution

For every deterministic v, finite-horizon linear-SDE theory gives E2 state/control for the original closed loop. Put `P=A+BK` and retain the original feedforward R. The actual mean state is

`x_bar(t)=integral_0^t exp(P(t-s))[B Rv(s)+C v(s-h)]ds`.

This identity is justified by the zero mean of the actual square-integrable Itô term; it is not extended to an arbitrary local-only control. The actual mean control is

`U_mean v=K x_bar+R v`.

The finite-horizon state Volterra kernel is square-integrable, so its operator is compact; its composition with the bounded forcing operator B R+C S_h is compact. The R kernel part is compact too. Consequently

`U_mean=L0 E0+Lh Eh+K_compact`.

Every original matrix/noise coupling remains in the physical equation and well-posedness proof. Noise does not contribute to this justified first moment, but is not asserted absent from the actual control/state distribution.

## 3. All-input actual-state obstruction

Choose any small interval I inside (0,T-h) of length less than min(d,h-d), so I, I+d and I+h are disjoint. Restrict deterministic inputs to I and project the compared control means onto I+d. Both endpoint terms vanish there, whereas `J D_d` is the translated matrix isometry. The remaining restricted state/kernel term is compact.

Take a unit maximizing vector e of J and any orthonormal sequence phi_k in L2(I). The actual deterministic inputs v_k=e phi_k have norm one and are weakly null. The restricted compact contribution tends strongly to zero, while the interior-tap output has constant norm ||J||. The norm lower bound follows for every law. For u=0, U_mean=0 whatever the plant state does, and the norm of J D_d on these intervals is exactly ||J||. This proves the infimum and its benchmark attainment.

If a bound law actually implemented u=Jv(t-d) almost surely for every deterministic v, its mean would implement it too, contradicting the positive lower bound. This pays the original actual-control caller without a controller realization argument, an invertible state reconstruction or a modified physical output.

## 4. Original-output version and limits

For the ORIGINAL output of any bound law the same paid mean calculation yields

`Z_mean = (D1L0)E0+(D1Lh)Eh+K_compact`.

Therefore a proposed universal emulation of an interior direct output functional `J_out v(t-d)` with J_out!=0 also has deterministic mean-operator error at least ||J_out||. This is a representation obstruction only; no error functional is installed as the original performance criterion, and no gain or feasibility comparison is inferred merely from the operator error. In particular the original synthesis optimum could still be feasible for other reasons.

The exact failed original-domain implication remains `abstract full window information -> this particular two-endpoint/L2-kernel parameterization represents all those laws (perhaps using the finite plant state)`. It does not. Thus no N&S theorem proved only for this subclass automatically answers the original full-information F task, unless a separate lawful sufficiency reduction is supplied.

At J=0 the obstruction is zero; at d=0 or d=h the target is already an allowed endpoint tap, so the claimed positive bound is not asserted. h=0 has no interior tap, and T>h is retained. All original matrix ranks, state/noise degeneracies and finite dimensions are covered; the proof is not a scalar or selected-trajectory diagnostic.

Only current admitted definitions, classical linear-SDE/isometry well-posedness/zero mean, finite-kernel compactness and elementary L2 weak-null facts are used. No old guide, new source, scientific execution, selected numeric/control probe, storage or stopped realization route is used. Full original synthesis, source-book equivalence, infinite horizon and broader nonlinear/local-only controls remain unresolved. All old STOP/HOLD/ZERO, process findings including late-ACK MINOR, N4 UNKNOWN and aux214 STOP persist; no review/adoption or stronger assurance/novelty is claimed.
