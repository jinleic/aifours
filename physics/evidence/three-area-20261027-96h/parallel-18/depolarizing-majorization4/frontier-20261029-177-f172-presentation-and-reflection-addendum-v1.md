# Additive clarification of the f172-reviewed composite: bridge, constants and exact reflection interval

Owner PhysicsDepol4-2, physics-2. Actual native clock observed before composing: **Thu Oct 29 09:31:09 PDT 2026**. This is a later additive record, not an edit of candidate 121, its five errata, either review, or any parent disposition.

## Scope and immutable inputs

This note supplies the omitted presentation behind f172 MINORs M4/M5 and explicitly withdraws 121's incorrect all-density endpoint sentence (M1). It restates, rather than enlarges, the proof reconstructed by f172. The derivations below are **AUTHOR-WRITTEN**; they receive no new independent-review, formal/kernel or novelty status merely by appearing here.

- Candidate: `frontier-20261028-121-consolidated-physical-k3.md`, 427 LF, SHA256 `91643ea8965e0e423f2b5010a18e967ddfaeb4c0f78a175ba6509dd9f2e5c36b`, with the mandatory errata 125/127/128/130/133 and the parent reflection-scope note.
- Fresh review: `institute/runs/three-area-2026-10-27-96h/review-waves/f172-depolarizing-corrected-composite/review-v1.md`, 271 LF, SHA256 `f34242e40d0b649851fbead9981b1e805ecbdd061c6ae31d9b83f86edeaf1b8f`. I read every line 1–90,91–181,182–271 before this note. It reports 0 FATAL, 0 MAJOR, 5 MINOR at its exact scope. This is same-harness supplied-proof reconstruction, not independent-model-family review.
- Parent scope correction: `institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-depolarizing-k3-class-H-scope-erratum-v1.json`, SHA256 `c9b5632e8285298a6b8438842498fc5a35695a889efcee0245836c2cbf038db2`, read completely before this note. **H requires both** `4S+8C<=64/9` and the stated spin-flip alternatives. P/U/D_p/H are pure-input classes before taking the fixed-p finite convex hull.

The all-density theorem is for **199/200 <= p <= 201/200**, a neighbourhood of **complete depolarization**, not of the identity channel. The identity channel is p=0. Zhang's matched clipping mechanism and the unresolved priority/full-weight-support qualification remain explicit; no novelty claim is made.

## 1. Explicit weight-share normalization

In 121's closest-product gauge write

`psi = sqrt(1-eta^2)|0000> + eta v`, `||v||=1`, with v supported on excitation weights 2,3,4.

Let v_h be its orthogonal weight-h components and w_h=||v_h||^2. For w_h>0 define u_h=v_h/sqrt(w_h); omit w_h=0 components. Then

`w_2+w_3+w_4=1`, `A = sum_h w_h A(u_h)`, `M = sum_h w_h M(u_h)`.

The scalar terms quadratic in v and the subtraction of the reference matrix scale with w_h. The latter subtraction splits because the weights sum to one. Excitation-phase covariance removes cross-weight products in the weight-0 and weight-1 diagonal blocks, including the virtual products in (16). Consequently Ky Fan subadditivity gives

`A+K2(M) <= sum_h w_h (A(u_h)+K2(M(u_h))) <= -15t/64`.

This makes the normalization implicit after 121 Eq.(16) explicit; it does not replace or extend the already reconstructed component identities.

## 2. Complete bridge from raw Hessian blocks to normalized conjugation blocks

Take `0<t<=1/200` and put c=16/t. In the normalized frame of 121 §8, `V_H=c V`, `W_H=c W`, and every divided gap is

`d_l-d_k = c(lambda_l-lambda_|k|)`.

Partition into excitation weights {0}, {1}, and {2,3,4}. Let S be the anti-Hermitian matrix with zero diagonal blocks and

`S_ij = -(V_H)_ij/(d_i-d_j)` across distinct blocks.

Then `[D,S]=-V_off`. Decompose V_H=V_diag+V_off. Thus

`B = [V_H,S] + (1/2)[[D,S],S] = [V_diag,S] + (1/2)[V_off,S]`.

The diagonal blocks of `[V_diag,S]` vanish. Within either leading block l (l=0 or 1), the product reference has the same diagonal value d_l at each index, so for i,j in that block,

`B_ij = sum_(k outside that block) (V_H)_ik (V_H)_kj/(d_l-d_k)`.

To verify the sign and the factor, use `S_kj=(V_H)_kj/(d_l-d_k)` and `S_ik=-(V_H)_ik/(d_l-d_k)` inside the half-commutator. The two terms coincide, cancelling its factor 1/2. There is no weight-0/weight-1 coupling; the virtual indices are precisely the rest indices in (16). Therefore

`Q_00 = (W_H)_00 + sum_k |(V_H)_k0|^2/(d_0-d_k) = c A`,

`Q_(e_i,e_j) = (W_H)_(e_i,e_j) + sum_k (V_H)_(e_i,k)(V_H)_(k,e_j)/(d_1-d_k) = c M_ij`.

Each virtual term scales as c^2/c=c, not c^2 and not 1. These are the load-bearing identities `Q_00=(16/t)A` and `Q_wt1=(16/t)M` used in the leading-block Ky Fan estimate.

## 3. Constants with all terms retained

Use the source Parseval bounds `v_F=23/200`, `s_F=23/400`, so `||V_H||_F<v_F`, `||W_H-W_0||_F<v_F`, and `||S||_F<s_F`. The strict inequalities are uniform over the entire complex normal sphere and 0<t<=1/200; no sampled direction is a premise.

Since deleting blocks decreases Frobenius norm and `||[X,Y]||_F<=2||X||_F||Y||_F`, the decomposition in §2 gives

`||B||_F < 3 v_F s_F = 1587/80000 < 47/1000`.

Also `||W_0||<=8`, hence

`||W_H|| < 8+23/200 < 163/20`,

`||Q|| < 163/20+47/1000 = 8197/1000 < 41/5`.

Only the transverse part of W_0 is off-block. Its off-block part is its compression to weights at most two, extended by zero, and its norm is at most four. Thus

`||off Q|| < 4+23/200+47/1000 = 2081/500 < 21/5`.

For `h=eta sqrt(1-eta^2)<=eta<=9/40`, the three Taylor errors come respectively from D after order 2, h V_H after order 1, and eta^2 W_H after order 0. The common exponential bound is valid because

`2 h ||S|| < 2 eta s_F <=207/8000`,

`exp(207/8000) <= 1/(1-207/8000) = 8000/7793 < 103/100`.

The respective cubic coefficients are bounded by `5(2s_F)^3/6`, `v_F(2s_F)^2/2`, and `(163/20)(2s_F)`. Their total, with that tail factor, is

`(103/100)[5(2s_F)^3/6+v_F(2s_F)^2/2+(163/20)(2s_F)] = 580473701/600000000 <1`.

Consequently the remainder norm is less than eta^3. Substitution of `h^2=eta^2-eta^4` leaves the separate `-eta^4 B` term; it is not discarded.

For `H_* = D+h V_diag+eta^2 Q`,

`||H_*-D|| < (9/40)(23/200)+(9/40)^2(41/5)=441/1000`.

Each reference separation is at least two. Weyl on the compressed blocks leaves each actual separation greater than `2-2(441/1000)=559/500>11/10`. This does not require distinct eigenvalues within the weight-one block.

Use 121 Eq.(26) twice, first separating weight zero and then weight one. Its comparison uses the positive Gram difference for any g>0; here g=11/10 also puts the comparison's lower block below the upper block. The bridge in §2 and the normalized margin `(16/t)(A+K2(M))<=-15/4` give

`K3(H_*) <= K3(D)-(15/4)eta^2 + [3(21/5)^2/(11/10)] eta^4`.

Moving from H_* to the exact unitarily conjugated operator costs at most `3 eta^3+3(47/1000)eta^4`. After dividing by eta^2 (eta>0), the full adverse coefficient is at most

`3(9/40)+3(47/1000)(9/40)^2+[3(21/5)^2/(11/10)](9/40)^2 = 54870831/17600000 <13/4`.

Thus the normalized deficit is at least eta^2/2, and undoing the normalization gives the source bound `R3-K3(Lambda_(1-t)(rho)) >= t eta^2/32`. This supplies presentation only; it changes none of the source constants or intervals.

## 4. Explicit author withdrawal of the overbroad endpoint sentence

The last paragraph of 121 §9 says that reflection covers the negative-shrink physical half, "including p=4/3." **That sentence is withdrawn for the all-density branch.** The permitted reflection preserves t=|1-p|. Hence the all-density argument on `[199/200,1]` reflects only to `[1,201/200]`. At p=4/3, t=1/3>1/200, so this proof supplies no all-density statement there. Regional statements reach p=4/3 only under their own actual pure-input hypotheses, followed by the fixed-p convex hull.

M2/M3 remain addressed by the earlier errata 133/127; those immutable corrections are not replaced or backdated here. M4/M5 are expanded above. All old process findings, including the 84-minute owner checkpoint gap disclosed in 175, remain as process records, not mathematical claims. No unrestricted k3 proof, full majorization or novelty clearance follows from this addendum.
