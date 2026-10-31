# A finite exact initial-state compatibility condition for the literal ratio

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:42:43 PDT 2026**. This is an explicit comparison of initial-state interpretations in the same bound finite-horizon linear controller class, not a claim that the book requires arbitrary initial states. The separate page audit found no explicit initial-state convention IN THE THREE INSPECTED PAGES; their surrounding method discussion is not a proof input. All previous timing/process/STOP/HOLD/ZERO qualifications persist.

## 1. Full matrix scope and exact theorem

Use all original compatible real matrices and the bound deterministic stationary linear preview law, finite T>h>=0, zero disturbance history/zero extension and canonical progressive E2 inputs. Replace the earlier adopted x(0)=0 only for THIS EXPLICIT COMPARISON by a specified deterministic vector x0. Do not silently promote this alternative into the supported zero-initial problem.

Write

`P=A+BK`, `Q=A0+B0K`, `N=D0+D1K`,

and retain the exact endpoint/kernel operator R. Define the finite subspace

`M_(n-1)(x0)=span{W x0: W is any word in P,Q of length at most n-1}`,

including the identity word of length zero. This quantifies ALL words; it does not select an order, invariant rank or tested state.

**Theorem.** The fixed-law literal gain with this initial state is finite iff

**N W x0=0 for every P/Q word of length at most n-1.**          (I)

If (I) holds, its entire actual input/output map equals that of the same law at zero initial state, hence its literal progressive and deterministic gains equal the respective zero-initial gains. If (I) fails, BOTH literal gains are infinity, witnessed by an analytic small-amplitude family of actual deterministic inputs. The criterion is all-variable, includes every matrix degeneracy, and is finite algebraic data rather than an uncomputed infinite-word assertion.

The finite zero-initial gain used for the sufficiency assertion is the current author theorem `general-linear-preview-literal-bound-and-continuity-v1.md`, SHA `48a51780b14540091b369e6d5f964f38a40c90c580699debd85e45f0a45e3302` (UNREVIEWED). The initial-output obstruction and finite-word equivalence below are separately reconstructed rather than inherited from that bound.

## 2. Separate the actual homogeneous initial response

Finite-horizon linear-SDE existence/uniqueness/linearity gives, at the SAME input and Brownian motion,

`X_(x0,w)=X_(x0,0)+X_(0,w)`,

`z_(x0,w)=z_(x0,0)+z_(0,w)`.

The zero-input initial state solves the ACTUAL equation

`dY=P Y dt+Q Y dW`, `Y_0=x0`, `z_(x0,0)=N Y`.

It has continuous paths and finite second moments on this compact horizon. No feedforward term is hidden at zero input; R0=0. All states/controls/outputs remain E2 for each specified E2 input and deterministic finite x0.

If `c0:=E||N Y||_[0,T]>0`, fix ANY nonzero deterministic v in the admitted L2 interval and use the whole symbolic family w=epsilon v, epsilon>0. Linearity and the reverse triangle inequality give

`E||z_(x0,epsilon v)||/(epsilon||v||)`

`>= c0/(epsilon||v||) - E||z_(0,v)||/||v||`.

The second term is finite by ordinary finite-horizon E2 well-posedness. The first is unbounded as epsilon decreases to zero. Every input is actual deterministic E2 with positive denominator; no zero-disturbance ratio is evaluated, no numerical amplitude or state is selected. This proves both infinite-gain conclusions whenever the homogeneous output is not identically zero.

If c0=0, the continuous process N Y is zero at every time almost surely. The actual output maps are then identical for all inputs; in particular their gains equal their zero-initial counterparts. Thus it remains to characterize this exact zero-output event.

## 3. A zero-process differentiation lemma derived from the allowed facts

For ANY constant matrix L, suppose the actual continuous process L Y is identically zero. Its increment equation gives

`0=integral_s^(s+epsilon) L P Y_r dr + integral_s^(s+epsilon) L Q Y_r dW_r`.

The actual Itô integral is E2, hence has conditionally zero increments, proved from simple-predictable integrals and L2 approximation. Conditional expectation on F_s and division by epsilon show

`0=epsilon^(-1) E[ integral_s^(s+epsilon) L P Y_r dr | F_s ]`.

The state is L2-continuous in time by the linear-SDE/isometry estimate. Conditional expectation is an L2 contraction, so the right side converges in L2 to L P Y_s as epsilon decreases to zero. Explicitly, its difference norm is bounded by

`||LP|| epsilon^(-1) integral_s^(s+epsilon) ||Y_r-Y_s||_L2(Omega) dr ->0`.

Therefore L P Y_s=0 for every s<T, and continuity/one countable dense time set gives the process identity L P Y=0 through T. Returning to the increment equation leaves the Itô integral of L Q Y identically zero; isometry gives `E integral_0^T |L Q Y_r|^2 dr=0`, and time continuity gives L Q Y=0 identically too.

Thus

**L Y identically zero -> L P Y and L Q Y identically zero.**  (Z)

No quadratic-variation uniqueness, support theorem, stochastic-flow transformation, optional stopping, storage/Gramian or external source is imported. The argument uses only admitted linear-SDE/isometry facts, conditional expectation and ordinary L2 continuity.

## 4. Necessity and finite closure, including x0=0

Apply (Z) first to L=N and then recursively to all appended P/Q words. If N Y is zero, every N W Y is zero and evaluation at time zero gives N W x0=0 for ALL finite words, hence (I).

Conversely define `M_0=span{x0}` and `M_(j+1)=M_j+P M_j+Q M_j`. If a step has no dimension increase, that space is invariant under P and Q and later steps do not grow. If x0!=0, the sequence starts in dimension one and can increase strictly at most n-1 times. Hence M_(n-1) is already invariant; if x0=0 it is the invariant zero space from the start. It is exactly the span of the words in (I).

Under (I), N annihilates this invariant space. The homogeneous linear SDE started at x0 has a solution entirely inside it: solve the restricted finite-dimensional equation and embed it into the original state space. Original strong uniqueness identifies it with Y. Thus N Y is identically zero, proving sufficiency. This finite algebraic restriction is only a proof of an actual invariant subspace, not a modified plant/controller or replaced performance output.

If (I) fails, necessity contraposition says N Y is not the zero process. Its continuous finite-E2 paths then have positive expected pathwise L2 norm, so the small-input obstruction in section 2 applies. This proves the complete iff assertion.

## 5. Precise initial-state and strictness consequences

For n=1, the word list has length zero only and (I) reduces to N x0=0, as it should. Singular N, P or Q, zero x0 and invariant hidden initial-state components are all included. No inverse, stability or nonzero matrix entry is assumed.

If a proposed interpretation requires finite gain for EVERY deterministic initial state without any initial-energy term in the denominator, (I)'s length-zero condition forces N=0. Conversely N=0 makes the original output `z=D1 Rw` independent of the state, so it has finite literal gain and the property does hold. This is an exact conditional interpretation statement, not a claim that the inspected book imposed that initial-state quantifier.

When (I) holds, ALL actual ratio/strictness questions are literally the same as the corresponding zero-initial law. When it fails, no finite prescribed gamma can satisfy even pointwise strictness on all nonzero deterministic inputs, not merely a uniform-margin convention. This addresses the actual homogeneous-ratio obstruction rather than computing a ratio at w=0.

The result does not settle the zero-initial prescribed-gamma synthesis task, choose K, prove feasibility for arbitrary initial data in the original source, extend to nonlinear/non-E2 unknown controllers or treat infinite horizon. Its purpose is to pay an exact initial-state compatibility premise that cannot be erased by a transcription agreement or an RMS reformulation.

All reasoning is written, symbolic and all-variable. Named facts and their uses are stated above; no selected numeric/state/control probe, program, model CLI, old proof/guide or new source was used. All NR-SOURCE/source-domain qualifications, STOP/HOLD/ZERO/findings including the late-ACK MINOR, N4 UNKNOWN and aux214 STOP persist. No parent/peer, formal/kernel, executable, human/configured-family or novelty acceptance is claimed.
