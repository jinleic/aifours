# Addendum 1: nonmonic weak-polynomial notation and conic elimination

This additive clarification applies to `reconstruction-v1.md`; the original bytes are not changed. It makes two points in §§6–8 explicit and does not widen any claim or gate.

1. The definitions of §1 were written for a **monic** synthesis numerator. Whenever §§6–8 instead use a weak polynomial \(q(s)=\sum_{j=0}^7q_js^j\) of degree at most seven, \(q_7\) is arbitrary and may be zero. In those sections use
   \[
   F_q=q_0-q_2t+q_4t^2-q_6t^3,\qquad
   G_q=q_1-q_3t+q_5t^2-q_7t^3,\qquad P_{q,a}=F_qE_a+tG_qO_a=q\cdot r_a.
   \]
   In particular \(q/a\to q_7\ge0\) at infinity. Section 7's \(Q\), and the SDP of §4, remain monic and retain their \(-t^3\) term. This corrects the otherwise ambiguous carry-over of the monic notation into the weak-separation and buffer arguments.

2. In the conditional conic-Carathéodory step of §8, “deleting a positive linear dependence” means the following elementary elimination; no dependence with all coefficients of one sign is assumed. If more than eight current row vectors \(r_i\in\mathbb R^8\) have positive weights \(w_i\), choose a nonzero dependence \(\sum_i c_i r_i=0\) and flip its sign if necessary so that some \(c_i>0\). Set \(\theta=\min_{c_i>0}w_i/c_i>0\), then replace each weight by \(w_i-\theta c_i\). All weights remain nonnegative, at least one becomes zero, and the entire eight-coordinate aggregate is unchanged. Delete zero-weight terms and repeat. For rational rows and weights one may choose the dependence and every resulting weight rational. This proves the stated at-most-eight conclusion without adding a sign condition on the dependence.

The original author reconstruction and this addendum remain UNADOPTED pending complete parent read and separate disposition. No scientific code or verification was run for this clarification.
