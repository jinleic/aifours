# Gate-I RMS value: parent written check before v244 returns

Actual clock immediately before writing: **2026-10-27T08:52:43-0700 PDT**. This is a prospective parent check, not a disposition or independent proof of unseen material. Main read the complete [129-LF v55 source](../../../information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v55-gate-I-value-independent-proof.md), live SHA-256 `c51562e845a609bc00d46f1e4f65eec77e10355bdbf81db63e7b8a680004c43a`, before [v243](preview-v55-single-source-review-exception-v243.json). Both v244 reviews are pending. The original v21 proof and v54 corollary are not supplied or newly accepted. No numerical parameter, decimal, scientific program, calculation engine or chosen-control diagnostic is used.

## Exact scoped setup

For symbolic positive `a,c,d,sigma`, let `q0=2a-sigma²>0). The zero-state uncontrolled plant is `dX=(-aX+c w(t-h))dt+sigma X dW), with `z=dX) meaning the output coefficient d times the state, not the Itô differential of X. Inputs are original progressively measurable E2 disturbances on the canonical Brownian filtration, with zero extension to negative time. All gains below are infinite-horizon RMS gains. This is an adversarial-input value result, not a physical controller synthesis.

## Upper bound and energy identity

The positive fundamental flow satisfies `E[Phi(s+u,s)² | F_s]=exp(-q0 u)). Variation of constants and Minkowski in the joint time/probability L2 space give `||X||_2 <= c integral_0^infinity exp(-q0 u/2)du ||w(.-h)||_2 = (2c/q0)||w||_2). Thus `G2(h)<=2cd/q0) for every h>=0.

For the squared response, symmetrize the two input times. Conditional on the later time s, independence of future Brownian increments and the flow cocycle yield `E[int_s^infinity Phi(t,s)Phi(t,s')dt | F_s]=Phi(s,s')/q0) for s'<s. This gives `E int X²=(2c/q0) E int w_tilde X), with `w_tilde(t)=w(t-h)). To justify Fubini even for signed inputs, apply the same Minkowski bound to `|w_tilde|): the positive flow integral has finite L2 norm, so its squared expansion is absolutely integrable; then Cauchy–Schwarz gives finite `E int |w_tilde X|). The identity is for eligible E2 inputs; no divergent infinity-minus-infinity interpretation is used.

## A direct all-variable lower-bound cross-check

Choose an arbitrary symbolic pulse duration `delta>0) and symbolic `0<lambda<q0/(2c)). At h=0 define the disturbance `w=1_[0,delta]+lambda X 1_(delta,infinity)). This is a progressive adversarial input, not a controller. Linear-SDE strong existence gives the unique process on every finite horizon. Let `A=E X_delta²) and `Q0=E int_0^delta X²). On the pulse, `X_delta=c int_0^delta Phi(delta,s)ds>0) almost surely; the preceding upper bound gives finite Q0, and standard finite-time flow bounds give `0<A<infinity). Neither depends on lambda.

After delta, the state is autonomous with drift `-a+c lambda). Its second moment therefore obeys `E X_t²=A exp(-(q0-2c lambda)(t-delta))). Put `T_lambda=A/(q0-2c lambda)). For each admissible lambda this is finite, so the disturbance is truly E2; as lambda increases to the critical value it diverges. The actual gain quotient squared is

`d²(Q0+T_lambda)/(delta+lambda² T_lambda)),

which tends to `d²/(q0/(2c))²=(2cd/q0)²). Thus the lower bound matches the upper bound at h=0. This cross-check avoids relying on a zero-energy branch or the source's extra small-pulse inequality. It is a symbolic family and limit, not a selected numeric experiment. Each admissible lambda is a legal input; no controller, hidden state reset or compactly supported final input is asserted.

## Remaining gates

This check does not supply the exact value of `G2(h)) for positive finite h, any equality for the literal gain `G1), a controller or synthesis. The v55 long-preview corollary consumes unreviewed v54 and remains outside v244. The historical v21 source remains not reconstructed by this check. Two actual v244 review returns, their complete reads, and a separate prospective parent disposition remain required before changing v220's conditional value cut. Same 18 slots, HOLD v2, N4 UNKNOWN with historical child exit unestablished, aux214 STOP, all ZERO findings, original cutoff/deadline; no stronger or novelty claim.
