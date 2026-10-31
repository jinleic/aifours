# Werner upper zero — an explicit strict full-raw resolvent margin on EVERY complex p direction

Owner PhysicsResearch96h-2. Precreation `/bin/date`: **Mon Oct 26 08:23:24 PDT 2026**.

**WRITTEN OWNER-CANDIDATE, unreviewed/unadopted.** Written only after the complete `PH-Werner-post-review-qualified-original-direction-v50.json` was actually read. That direction prospectively clears v38 after actual cross-review RETURN and the already WRITTEN/SENT cp055 whole ACK (`74ccf26e41f0dca4997bc0d6bf054e493259f0546c1c61b38a68b6fc07ca09bc`). All previous findings, v46's full blocked-wait cadence gap, source/probe provenance and ZERO consuming-guidance boundaries remain. No withdrawn proposed bound or chosen-instance check is used.

This is an all-variable quantitative consequence of the existing exact raw-remainder identity, NOT an independent solution or a novelty claim. It makes the strict correction usable in an inequality rather than merely observing that it is PSD. The original universal sign remains unproved.

## 1. Quantified statement and exact ceiling

Let c_i>0, Sum_i c_i^2=1, x_i=c_i^2, d_i=1-x_i, d_ij=(d_i+d_j)/2 and W=e3(d). For each unordered edge e={i,j} let f={k,l} be its complement, and define

`kappa_e=1-2d_e d_f/W`,
`mu(c)=min_e kappa_e`.

For EVERY such spectrum, `0<mu(c)<1`, and

`K_full >= K_c + diag(kappa_e) >= K_c+mu(c)I`.                           (1)

Using the named base-kernel bound I<=K_c<=3I, the following hold for EVERY complex forcing j, in particular every original j(Z) with arbitrary complex Zc=0:

`j^dagger[K_c^-1-K_full^-1]j >= mu/[3(3+mu)] ||j||^2`,                  (2)

`j^dagger K_full^-1 j <= [3/(3+mu)] j^dagger K_c^-1 j`,                 (3)

`j^dagger K_full^-1 j <= ||j||^2/(1+mu)`.                              (4)

Put P(Z)=<Z,rho'Z>, `E_c=P-j^dagger K_c^-1j` and `E_full=P-j^dagger K_full^-1j`. Then, on the ENTIRE twelve-dimensional complex p space,

`E_full >= E_c + mu/[3(3+mu)] ||j||^2`,                                (5)

`E_full >= [3E_c+mu P]/(3+mu)`,                                       (6)

`E_full >= P-||j||^2/(1+mu)`.                                         (7)

No inequality asserting E_full>=0 for all Z follows merely from (5)–(7): the right sides have not been shown nonnegative. No chosen spectrum, boundary or limit evaluation, parameter viability check, region or threshold is used. No other canonical sign or W4 claim is made.

## 2. Named exact inputs

1. Generic base kernel and I<=K_c<=3I: `generic-upper-zero-operator-checkpoint-001-v1.md`, SHA `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`, G3–G4 at their existing written scope. FALSE G13 and the bare lift are not inputs.
2. COMPLETE exact raw-remainder identity: `generic-upper-zero-operator-checkpoint-001-ADDENDUM-2.md`, SHA `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`, §1/F1. For arbitrary symmetric zero-diagonal U, with F_ij=d_ij U_ij,

`(1/2)F^dagger(K_full-K_c)F = Sum_e d_e^2[1/2-d_e d_f/W]|U_e|^2 + (1/4)Tr([D,U]^dagger L[D,U])`,                         (8)

where D=diag(d_i), L_ii=1/4 and L_ij=-c_i c_j/(4d_ij). This retains the ENTIRE commutator Gram, not its diagonal.
3. Original forcing/domain/normalization: v1 (`b006646d85afb5b6f4428880d733a413f22f6a92c4320654e4d8dabbcafd553b`) and v20 (`b5c3d36c1b8594388b28c74a12e46de5adf4feb3d85a6d81d96d494a5a2c86ea`). No selected-reference example or frozen diagnostic is used.

Input2 is named rather than newly independently accepted. Its positive Gram can also be seen directly from `DL+LD=Q/2`, Q=I-cc^T:

`L=(1/2) integral_(s=0)^infinity exp(-sD) Q exp(-sD) ds >=0`.

D>0 makes this a convergent ordinary matrix integral. The diagonal and off-diagonal entries give exactly the displayed L. No interpreter, numerical integration, CAS or other scientific execution occurs.

## 3. Every diagonal raw coefficient is STRICTLY positive

This proof uses all four variable coordinates and no special spectrum. For e={i,j}, put

`p=x_i+x_j`, `h=x_i x_j`, `v=x_k x_l`.

All are positive and 0<p<1. We have

`d_i d_j=1-p+h`, `d_k d_l=p+v`,
`d_i+d_j=2-p`, `d_k+d_l=1+p`.

Consequently, by grouping the elementary symmetric cubic in complementary pairs,

`W=(1-p+h)(1+p)+(p+v)(2-p)`
` =1+2p(1-p)+(1+p)h+(2-p)v`.

Since `4d_e d_f=(2-p)(1+p)=2+p(1-p)`,

`2W-4d_e d_f = 3p(1-p)+2(1+p)h+2(2-p)v >0`.

Therefore

`kappa_e = [3p(1-p)+2(1+p)h+2(2-p)v]/(2W) >0`.

Also kappa_e<1 because d_e,d_f,W>0. This holds for EVERY edge and every positive spectrum, so the finite minimum mu lies strictly between0 and1. Complementary edges have equal kappa; mu can equivalently be written as

`mu=1-(2/W)max{d_12 d_34,d_13 d_24,d_14 d_23}`.

This is an explicit permutation-invariant symbolic function, not a selected parameter search or an asserted uniform closed-simplex gap.

Multiply (8) by2 and use F_e=d_e U_e. The exact correction is

`F^dagger(K_full-K_c)F = Sum_e kappa_e|F_e|^2 + (1/2)Tr([D,U]^dagger L[D,U])`.

The final term is nonnegative. This proves (1) for arbitrary complex F with the full raw correction retained.

## 4. Exact inverse-order deductions

Set mu=mu(c)>0. Positive definite inverse order gives

`K_full^-1 <= (K_c+mu I)^-1`.

Because K_c<=3I,

`K_c+mu I >= (1+mu/3)K_c`,

which proves (3). Because K_c>=I, it also gives K_full>=(1+mu)I and proves (4).

For (2), functional calculus for the positive Hermitian K_c yields

`K_c^-1-(K_c+mu I)^-1=mu K_c^-1(K_c+mu I)^-1`.

Each eigenvalue is `mu/[lambda(lambda+mu)]` with0<lambda<=3. The denominator is at most3(3+mu), so this matrix is at least `mu/[3(3+mu)]I`. Combining with inverse order proves (2).

Subtracting these forcing bounds from the SAME P proves (5) and (7). Rewriting (3) gives

`P-[3/(3+mu)](P-E_c)=[3E_c+mu P]/(3+mu)`,

which is (6). No entrywise-inverse inequality, lost p direction, independent square center or assertion K_full<=3I is used. Only the named K_c upper bound is used.

## 5. Exact remaining universal obligation

The existing exact Lemma N_full (v20), or equivalently full potential inequality F4 (v22), still has to be proved on ALL positive spectra and ALL complex tests. The present margin shows quantitatively why a failed stronger-base certificate is not an original-target counterexample, but supplies no sign of an unbounded/unknown base residual.

A proof that `3E_c+mu P>=0` on the ENTIRE p space for every spectrum would now suffice for the ORIGINAL full sign; it is not asserted or proved here, and is not substituted for the exact obligation. No replay of an old selected scout is authorized by that observation.

F_up, F_low, Z_low, the co-Choi-to-W4 eligibility bridge and unrestricted rank<=2 W4 remain separate, unresolved obligations. No negative physical direction, numerical ledger, closed target, novel result count, formal/family/human/executable gate or deadline change follows.

## 6. Assurance

Exact written all-variable algebra and named input identities only. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/CLI/nested agent/new GO. All original findings and held-lead provenance remain, no counterfactual independence or clean-history claim. Same18/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; no early final park or round closeout.
