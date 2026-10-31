# Same-harness scientific review: f200, all-density depolarizing window 1/142

**Disposition: 0 FATAL / 0 MAJOR / 1 MINOR; INCONCLUSIVE items: none within the stated 1/142 theorem.** The candidate inequality is supported by the independent written reconstruction below for all four-qubit densities, all complex rank-three projectors, and `|1-p| <= 1/142`. This conclusion does **not** rely on substituting `1/142` into the previously adopted `1/200` theorem: the interval-dependent far bound, Hessian margin, Parseval/gap estimates, conjugation remainder and block budget are re-established here on the larger interval. The one minor is a prospective source-order conflict in the frozen manifest, not a demonstrated mathematical defect; see P1 below. No opinion is asserted outside this window or the exact previously adopted regional scopes.

Native clock observed before composing this review: **2026-10-29T13:20:56-0700 PDT**. This is an observation, not a claim of a file-creation time.

## Frozen inputs, measurements, and actual read sequence

The manifest was the first research artifact opened. Its SHA-256 was measured as `eea5b85084e326e673237636ce5d317bd162c6f07924c9390824db2bc67c76b1`, agreeing with the assigned `eea5b85084e3` prefix. Before any declared input body was read, all 12 input byte strings were independently measured; SHA-256, bytes and LF **all matched** the manifest. The following rows are in the actual manifest/body-read order. Basenames are unambiguous within the manifest; no linked body was opened.

| # | Frozen input, identifying basename | SHA-256 | Bytes | LF |
|---:|---|---|---:|---:|
|1|`frontier-20261028-125-121-source-clock-erratum-v1.json`|`1922f5bdcf9ce6ca8203445362853bcc0ae1f5bfce81503e144dd92012580c8c`|2692|33|
|2|`frontier-20261028-127-121-fixed-Q-equality-erratum-v1.json`|`a19cf2acdd3004cc2a21d02537366af0b5ca6543b09f885eec8b9dcbce4de9c6`|2699|21|
|3|`frontier-20261028-128-121-prior-prefix-scope-erratum-v1.json`|`873390c306531f1bf69efbdcfdac26b315a7051ad2ccccabaa92ecf964daf285`|2839|25|
|4|`frontier-20261028-130-121-exclusion-source-bindings-v1.json`|`e1b3c3a3a16ab27da1e0568a8d8d181ce9511d9c1fbde66624d8ae5e9456b001`|2342|28|
|5|`frontier-20261028-133-121-weight3-conjugation-erratum-v1.json`|`237a9e74881881c5117654b99efd47471693cb961f560f371d8daa0ca341c453`|2403|14|
|6|`parent-reflection-scope-note-v1.json`|`c87955405f104a439fba5dfefb1d51142bbd658d3da230ed2199a5067329f958`|1392|11|
|7|`physics-2-depolarizing-balanced-rank-prefix-parent-v1.md`|`cdda493b043002b208d8f92b7da352d2f165f6e03c07481a439b596be7b8b38d`|5579|37|
|8|`physics-2-depolarizing-k3-regional-classes-and-near-identity-all-density-parent-v1.md`|`774cbb0f053c2b5c6400320a6c3bfdb919ec1e3df09ddf5884508e54cccb3f6c`|7514|22|
|9|`physics-2-depolarizing-k3-class-H-scope-erratum-v1.json`|`c9b5632e8285298a6b8438842498fc5a35695a889efcee0245836c2cbf038db2`|2444|27|
|10|`frontier-20261028-121-consolidated-physical-k3.md`|`91643ea8965e0e423f2b5010a18e967ddfaeb4c0f78a175ba6509dd9f2e5c36b`|25795|427|
|11|`frontier-20261029-177-f172-presentation-and-reflection-addendum-v1.md`|`a092c605b188cadafa5784eee5ab794524d7fee934f400b7964bde48f4511b70`|7899|107|
|12|`frontier-20261029-180-all-density-window-one-over142-v1.md`|`03618f679ca4570c752e693f69464b55faa898a6d3345beee6d11d3fc05bb8e9`|10413|205|

Every body above was displayed completely, in the table's order, in the following actual `:raw` windows; endpoints include the final lines:

- 1: `1-15, 16-30, 31-33`; 2: `1-15, 16-21`; 3: `1-15, 16-25`; 4: `1-15, 16-28`; 5: `1-14`; 6: `1-11`.
- 7: `1-15, 16-30, 31-37`; 8: `1-15, 16-22`; 9: `1-15, 16-27`.
- 10: `1-15, 16-30, 31-45, 46-60, 61-75, 76-90, 91-105, 106-120, 121-135, 136-150, 151-165, 166-180, 181-195, 196-210, 211-225, 226-240, 241-255, 256-270, 271-285, 286-300, 301-315, 316-330, 331-345, 346-360, 361-375, 376-390, 391-405, 406-420, 421-427`.
- 11: `1-15, 16-30, 31-45, 46-60, 61-75, 76-90, 91-105, 106-107`.
- 12: `1-15, 16-30, 31-45, 46-60, 61-75, 76-90, 91-105, 106-120, 121-135, 136-150, 151-165, 166-180, 181-195, 196-205`.

The first request for input 11's `46-60` unexpectedly displayed the already-read input 10's `46-60`; I immediately repeated the exact input-11 request and displayed the correct input-11 window before proceeding. It did not cause reliance on an undeclared body. The input-9 class-H erratum itself says to read it before input 8, whereas this manifest expressly orders input 8 before input 9. I followed the mandatory manifest order, read the correction before all three author bodies and before reconstruction, and do **not** claim the class-H erratum preceded the disposition. This conflict is P1.

## Claim-by-claim verdicts

`0F/0M/0m` means independently reconstructed at the stated scope, not a claim of formal verification. Line citations to 121/177/180 refer to the frozen inputs 10/11/12.

| Claim | Verdict | Scope/reason |
|---|---|---|
| C1: physical reflection, product reference, fixed-Q comparison and Pauli certificate, 121:16-23, 76-80, 175-187 | 0F/0M/0m | Re-derived below, including the transformed actual Q and the `t=0` endpoint. |
| C2: maximizing-product gauge and zero weight-one amplitudes, 121:191-197 | 0F/0M/0m | Stationarity and compactness, independent of the old radius. |
| C3: far-region bound `S >= 4-2 delta`, monotonicity and strict margin, 180:30-63 | 0F/0M/0m | Re-established at `t=1/142`; explicit coefficient and gap below. |
| C4: raw complex Hessian formulas and all-weight decomposition, 121:205-256; 180:25-27 | 0F/0M/0m | Matrix-unit derivation and weight-share/phase argument below; valid throughout the new interval. |
| C5: strengthened Hessian margin `A+K2(M) <= -t/4`, 180:65-85 | 0F/0M/0m | All three normal weights bounded uniformly; no finite sampling supplies the universal step. |
| C6: normalized Parseval estimates, generator, off-block bound and constants, 180:87-126 | 0F/0M/0m | All bounds redone with explicit `t <= 1/142`, including off-block compression. |
| C7: bridge and exact conjugation/remainder, 177:31-59 and 180:128-145 | 0F/0M/0m | Half-double-commutator and scale `16/t` are derived below; `-eta^4 B` retained. |
| C8: two block separations, Ky Fan error budget and tube gap, 180:148-174 | 0F/0M/0m | Actual compressed-block separations and all three error terms accounted for at the new boundary. |
| C9: endpoint, common-Q mixture and reflection to the entire stated interval, 180:176-182 | 0F/0M/0m | Fixed-Q argument; not an all-density statement at `p=4/3`. |
| P1: class-H correction's consumer order versus manifest order | 0F/0M/**1m** | Input 9 calls for before input 8; the manifest mandates 8 then 9. Followed the manifest; corrected H is not used as a premise. Parent should preserve this factual qualification. |

## Written reconstruction

### 1. Reference, reflection, and all-state Pauli estimate

Let `0 < t <= c=1/142`, `a=(1+t)/2`, `b=(1-t)/2`, and first take `p=1-t`. A pure product input has output eigenvalues `lambda_h=a^(4-h)b^h` at weight h, hence its top-three sum is

`R3=lambda_0+2 lambda_1=a^4+2a^3b`, and `16R3=3+8t+6t^2-t^4`.

For a pure `rho`, diagonalize its single-qubit marginals, let `r_1 <= r_2 <= r_3 <= r_4` be their Bloch radii, and put `S=sum r_i^2`, `L=r_1+r_2+3r_3+3r_4`, `delta=8-L`. The weight-one Pauli operator has top-three sum `L`: its top diagonal value is `sum r_i`, followed by `sum r_i-2r_1` and `sum r_i-2r_2`, including ties. In the Pauli expansion, `sum_{P != I}(Tr QP)^2 = 16 Tr Q^2-(Tr Q)^2=39`; for pure rho the sum over weights 2--4 is `16-1-S=15-S`. Because `t^h <= t^2` for `h>=2`, Cauchy--Schwarz with the **same** actual Q gives

`16 Tr(Q Lambda_(1-t)(rho)) <= 3+tL+t^2 sqrt(39(15-S))`.

Subtract the exact reference. Since `6t^2-t^4 >= 5t^2`,

`16(R3-Tr Q Lambda(rho)) >= t[delta-t(sqrt(39(15-S))-5)]`.  (1)

For one qubit `Y X^T Y=Tr(X)I-X`. Applying this to every tensor factor gives `Lambda_(1+t)(X)=Y^tensor4 Lambda_(1-t)(X)^T Y^tensor4`. In a trace this maps the actual projector to `Q'=Y^tensor4 Q^T Y^tensor4`, an actual rank-three projector, while the input and t are unchanged. The reference spectrum is also unchanged. This does not assume equality for a nonmaximizing fixed Q.

### 2. Closest-product gauge and the far region

The set of normalized product vectors is compact and has a positive maximum overlap squared `m` with a nonzero pure state. Rotate a maximizer to `|0>=|0000>` and fix its phase. A first variation of each local factor in an arbitrary complex tangent direction forces all four weight-one amplitudes to vanish. Thus

`psi=sqrt(1-eta^2)|0>+eta v`, `eta^2=1-m`, `||v||=1`, with v supported in weights 2, 3 and 4, whenever `eta>0`. No nondegeneracy of the maximizer is needed.

For the local majority eigenvectors, the commuting-projector union bound gives a product overlap at least `1-(1/2)sum(1-r_i)`. Hence `eta^2 <= (1/2)sum d_i <= delta/2`, where `d_i=1-r_i`, because `delta=d_1+d_2+3d_3+3d_4 >= sum d_i`. Moreover

`S=sum(1-d_i)^2=4-2 sum d_i+sum d_i^2 >= 4-2delta`.

Consequently the bracket in (1) is at least `f_t(delta)=delta-t(sqrt(429+78delta)-5)`. Set `r=19/80` and `delta_0=2r^2=361/3200`. If `eta>=r`, then `delta>=delta_0`. For `d>=delta_0`, rationalizing the square-root difference gives

`f_t(d)-f_t(delta_0)=(d-delta_0)[1-78t/(sqrt(429+78d)+sqrt(429+78delta_0))] >= 0`,

since both roots exceed 20 and the square bracket is at least `1-39c/20=2801/2840>0`. Also `429+78delta_0=441-5121/1600<441` and `delta_0-16c=31/227200>0`. Thus `f_t(delta_0)>delta_0-16c`, and for every far pure state and actual rank-three Q,

`R3-Tr Q Lambda(rho) > 31t/3635200`.  (2)

This includes the tube boundary. The independent control's `1/141` negative is only a failure of this particular boundary certificate; it is not a counterexample to the theorem at that larger radius.

### 3. All-variable raw Hessian and its stronger margin

For the gauge above let

`V=Lambda(|v><0|+|0><v|)`, `W=Lambda(|v><v|-|0><0|)`,

`A=W_00+sum_{|k|>=2}|V_{k0}|^2/(lambda_0-lambda_|k|)`,

`M_ij=W_(e_i,e_j)+sum_{|k|>=2} V_(e_i,k)V_(k,e_j)/(lambda_1-lambda_|k|)`.

All denominators are positive for `0<t<1`. The local rules `|0><0| -> diag(a,b)`, `|1><1| -> diag(b,a)`, `|0><1| -> t|0><1|` give the following, without assuming real amplitudes. In a single normalized weight-h component, the `00` entry of `W` is `a^(4-h)b^h-a^4`, and `V_(C,0)=a^(4-h)t^h v_C` for each h-word C. This yields the scalar terms below. The weight-one entries follow from the same rules: a weight-h component has virtual weight h+1 in the `M` correction, where that sector exists.

* **Weight 2.** Put `v_2=sum_{i<j} c_ij|ij>`, `T_ii=0`, `T_ij=T_ji=c_ij`, `Gamma=TT^dagger`, `n_i=Gamma_ii`. Then `Gamma>=0`, `Tr Gamma=2`, and
  `A_2=-a^2 t(1-t^2)`,
  `(M_2)_ii=-ab t(1-t^2)(1-n_i)`, `(M_2)_ij=ab t^2(1+t) Gamma_ij` for `i!=j`.
  For example the virtual weight-three contribution has denominator `ab t`, and its coefficient is `ab t^3`; this combines with the direct off-diagonal `ab t^2 Gamma_ij`. Rewrite
  `M_2=ab t(1+t)[-(1-t)I+K]`, `K=t Gamma+(1-2t)diag(n)`.
  For `t<=1/142<1/2`, `K>=0` and `Tr K=2(1-t)`, so `K2(K)<=Tr K` and `K2(M_2)<=0`. Also
  `a^2(1-t^2)-1/4=t(2-2t^2-t^3)/4>=0`; hence `A_2+K2(M_2)<=-t/4`.
* **Weight 3.** Write `v_3=sum_i g_i|bar i>`, `sum |g_i|^2=1`, and `D_3=1-ab=(3+t^2)/4`. The scalar virtual gap is `a t D_3`; the weight-one virtual gap is `b t D_3`. The local rules give
  `A_3=-a t D_3+a t^5/D_3`,
  `M_3=-a^2bt I-b^2t(1+t)diag(|g_i|^2)+(t^2b^2+t^5b/D_3) conjugate(g) conjugate(g)^dagger`.
  In particular `V_(e_i,1111)=b t^3 conjugate(g_i)`: the opposite conjugation is not interchangeable for complex g. Dropping the negative diagonal and bounding the positive rank-one contribution by its trace,
  `A_3+K2(M_3) <= -a t D_3+a t^5/D_3-2a^2bt+b^2t^2+bt^5/D_3`.
  Multiplication by `32D_3` and expansion gives `-t(1-t)(15+24t+38t^2+32t^3+3t^4)` (equivalently `-15t-9t^2-14t^3+6t^4+29t^5+3t^6`). Because `D_3<=1` and the polynomial is at least 15, this is at most `-(15/32)(1-c)t<-t/4`; the coefficient slack is `979/4544`.
* **Weight 4.** With `D_4=a^2+b^2=(1+t^2)/2`, `A_4=-tD_4+t^7/D_4` and `M_4=-ab t I`; since `D_4+2ab=1`, their combined top-two bound is `-t+t^7/D_4 <= -t(1-2c^6)<-t/4`. The slack relative to `t/4` is `3074406814103/4099209085472`.

For a general v, write `v=sum v_h`, `w_h=||v_h||^2`, `sum w_h=1`. A simultaneous local excitation-phase rotation multiplies weight h by `e^{ih theta}`; the 00 and weight-one/weight-one blocks are invariant, so all cross-weight quadratic terms vanish. The reference subtraction splits using `sum w_h=1`. Thus `A=sum w_h A_h`, `M=sum w_h M_h` for normalized nonzero components. Ky Fan subadditivity yields the all-direction, all-complex bound

`A+K2(M) <= -t/4`.  (3)

The local matrix-unit derivation and (3) are valid at `1/142` in their own right, not because the 1/200 acceptance was enlarged.

### 4. Normalization, all-variable norms, and bridge

For `t>0` define `H_t(X)=[16 Lambda_(1-t)(X)-Tr(X)I]/t`. With `h=eta sqrt(1-eta^2)`, set `D=H_t(|0><0|)`, `V_H=H_t(|v><0|+|0><v|)`, `W_H=H_t(|v><v|-|0><0|)`; then `H=H_t(|psi><psi|)=D+hV_H+eta^2 W_H`.

The eigenvalue of D at weight j is `d_j=(16lambda_j-1)/t`. The relevant separations are

`d_0-d_1=2(1+t)^3>=2`, `d_1-d_2=2(1+t)^2(1-t)>=2`,

because `1-t-t^2>0` at `t<=1/142`. The extreme eigenvalues imply `||D||<=4+6c+4c^2+c^3<81/20`; the exact slack is `108057/14316440`.

Both input operators defining V_H and W_H are traceless with squared Hilbert--Schmidt norm 2. The degree-one Pauli component of the first vanishes by the weight restriction, while that of the second is

`W_0=sum_i (r_i(v)-z_hat) dot sigma_i`.

Pauli Parseval gives the all-variable estimates `||V_H||_F^2 <=512t^2` and `||W_H-W_0||_F^2 <=512t^2`. Since `(4/25)^2-512c^2=656/3150625>0`, both norms are `<v=4/25`. Let the anti-Hermitian divided-gap generator `S_1` have zero entries within the blocks `{weight 0}`, `{weight 1}`, `{weights 2,3,4}` and `S_1,ij=-(V_H)_ij/(d_i-d_j)` between blocks. Then `[D,S_1]=-(V_H)_off` and `||S_1||_F <s=2/25`.

Define `B=[V_H,S_1]+(1/2)[[D,S_1],S_1]`, `Qcal=W_H+B`. Writing `V_H=V_diag+V_off` gives `B=[V_diag,S_1]+(1/2)[V_off,S_1]`, so the commutator bound yields `||B||_F<3vs=24/625<1/25=:b_*`. Also `||W_0||<=8`, so `||W_H||<w=204/25` and `||Qcal||<w+3vs=5124/625<q=41/5`.

Only the transverse field `G=sum_i(r_ix(v)X_i+r_iy(v)Y_i)` contributes to `off W_0`. A single bit flip changes excitation weight by one, so the entire off-block part is exactly `P_{<=2} G P_{<=2}`, extended by zero. Hence `||off W_0||<=||G||<=sum_i sqrt(r_ix^2+r_iy^2)<=4`. Deleting blocks does not increase Frobenius norm, giving

`||off Qcal|| < 4+v+3vs=2624/625<o=21/5`.  (4)

For either leading block, the diagonal of `[V_diag,S_1]` vanishes and the diagonal block of `(1/2)[V_off,S_1]` is `sum_k (V_H)_ik(V_H)_kj/(d_l-d_k)`. The positive sign and the factor one follow from the two opposite entries of the anti-Hermitian S_1. There is no 0--1 coupling of V_H, so the virtual indices are exactly weights 2--4. Since `V_H=(16/t)V`, `W_H=(16/t)W`, and the denominators are `(16/t)` times the raw gaps,

`Qcal_00=(16/t)A`, `Qcal_weight1=(16/t)M`.  (5)

In particular (3) becomes the normalized leading-block margin `(16/t)(A+K2(M))<=-4` throughout the new interval.

### 5. Cubic remainder and two-block Ky Fan estimate

For `eta<=r`, `h<=eta` and `2h||S_1||<2rs=19/500`. Thus `exp(2h||S_1||) <= 500/481 <26/25`. In the exact unitary conjugation, truncate the D contribution after order two, `hV_H` after order one, and `eta^2 W_H` after order zero. The norm of the resulting remainder is bounded by `e eta^3`, where

`(26/25)[(81/20)(2s)^3/6+v(2s)^2/2+w(2s)] = 2661776/1953125 < e=137/100`.

Using `h^2=eta^2-eta^4`, this gives the exact identity

`exp(-hS_1) H exp(hS_1) = D+h V_diag+eta^2 Qcal-eta^4 B+R`, `||R||<e eta^3`.  (6)

The `-eta^4 B` term is not absorbed or dropped. Put `H_*=D+h V_diag+eta^2 Qcal`; then `||H_*-D||<rv+r^2q`. Let `g=199/200`. The exact calculation

`2-2(rv+r^2q)-g=63/16000>0`

shows both **compressed** block separations exceed g, without selecting eigenvectors in the degenerate weight-one block. The only off-block entries of H_* are `eta^2 off Qcal`, of norm `<eta^2 o`.

For Hermitian blocks with `lambda_min(A)-lambda_max(C)>=g`,

`[[A,B_0],[B_0^*,C]] <= diag(A+B_0 B_0^*/g,C+gI)`,

because the difference is the positive Gram matrix of `[B_0/sqrt(g); -sqrt(g)I]`. First compare weight 0 to the complement; its largest eigenvalue is at most the 00 diagonal plus `eta^4 o^2/g`. Cauchy interlacing bounds the next two eigenvalues by the top two of the complement. Apply the same comparison to weight 1 versus the remaining weights; its top-two sum costs at most another `2eta^4 o^2/g`. Using (5) and (3),

`K3(H_*) <= K3(D)-4eta^2+(3o^2/g)eta^4`.

The Ky Fan sum changes by at most three times the operator norm, so (6) adds at most `3e eta^3+3b_* eta^4`. For `eta<=r` the adverse coefficient divided by `eta^2` is bounded by

`3er+3b_* r^2+3o^2 r^2/g =126815937/31840000 < 4-16/2000`;

indeed the exact residual is `544063/31840000>16/2000`. Undoing normalization, for every `0<eta<=r` and `0<t<=1/142`,

`R3-K3(Lambda_(1-t)(|psi><psi|)) >= t eta^2/2000`.  (7)

Equations (2) and (7) cover every nonproduct pure input. When `eta=0` the input is a pure product and has the reference output spectrum. At `t=0` the output is exactly `I/16`, so all rank-three Q have trace `3/16`, without division by t. For a mixed input, fix the actual Q and average the pure inequalities over its finite spectral decomposition; then maximize over Q. The reflection in §1 extends this exact result from `p in [141/142,1]` to `p in [1,143/142]` and no farther.

## Independent bounded controls and receipts

The controls were authored in this wave from the definitions, using Python standard-library rational and Gaussian-rational arithmetic only; they do not import, execute, or compile an author script. The retained script is `reviewer-exact-controls-v1.py`, SHA-256 `8b4b94ee00e552cff6920d035eacbb2a0cfce24f8796c83894e958242a91b746`. The first observed native clock before writing the script was `2026-10-29T13:18:11-0700 PDT`.

| Run | Observed `/bin/date` start / end | SHA-256 measured before run | Exit | Result |
|---|---|---|---:|---|
| Initial | `2026-10-29T13:19:00-0700 PDT` / `2026-10-29T13:19:00-0700 PDT` | `29fa451b3edd89f171c367bedc68b0275159ae78d67974c12f767e7641fc1906` | 0 | Exact scalar budgets; eight matrix-unit/bridge instances; first intended negatives. |
| Phase-strengthened | `2026-10-29T13:19:49-0700 PDT` / `2026-10-29T13:19:50-0700 PDT` | `2ef334b5048eec57173dbd320b0c021022d1e71ad2d1a0e87211fb096cc7ea36` | 0 | As above, with an explicitly imaginary weight-three matrix-entry sign check. |
| Retained final | `2026-10-29T13:20:25-0700 PDT` / `2026-10-29T13:20:25-0700 PDT` | `8b4b94ee00e552cff6920d035eacbb2a0cfce24f8796c83894e958242a91b746` | 0 | As above, plus an actual complex density and complex rank-three Q at `t=1/142`, both signs of t, and the transformed-Q reflection. |

Each run had a 120-second tool deadline; none timed out. The earlier hashes identify actual earlier script versions; the retained file is the final version. Eight finite matrix controls covered complex weight 2, complex weight 3, weight 4 and mixed-weight directions at `t=1/142` and `t=1/2`, comparing independently channel-expanded raw blocks and the full commutator bridge to the displayed formulas. Exact scalar controls included all stated far, Hessian, gap and remainder slacks. Intended-reason negatives detected: the wrong complex rank-one conjugation and imaginary entry sign, omitting the half-double-commutator, leaving Q unchanged under reflection, replacing `1/142` by `1/141` in the same far certificate, and increasing the tube radius to `1/4` in the stated block-separation and remainder budgets. These mutations diagnose the respective proof steps only; they do not exclude a different proof or a larger true theorem. Finite controls are not the universal proof.

## Imports, remaining gap, and deviations

The pinned dispositions were read for their expressly adopted scopes only. The prefix disposition does not supply k3; the f172 disposition adopts the old all-density interval only at `1/200`, not at `1/142`. Its corrected H class requires **both** the moment hypothesis and the specified spin-flip alternative, and consists of pure inputs before taking a fixed-p convex hull; no regional H claim is used to prove the new interval. The written reconstruction uses the definitions, the elementary Pauli basis/trace identities, finite-dimensional spectral variational and interlacing principles, and the algebra displayed and re-derived above. It does not import linked packet bodies, author checker output or PASS claims, a solver status, floating-search failure, R-positivity, a one-erasure conjecture, held material, sibling reviews, outside literature, a web source or an external model/API. It did not run or import author code. The earlier `p=4/3` all-density reflection sentence is withdrawn; no such endpoint claim is made here.

Within the stated 1/142 claim, no mathematical step is left INCONCLUSIVE in this reconstruction. The unrestricted all-p k3 problem, larger windows, other prefixes, and novelty remain outside scope, not solved by this review. Contract deviation: **none from the manifest-mandated input order or the bounded-control protocol**. The input-8/input-9 consumer-order conflict and the corrected input-11 raw-window retry are disclosed above rather than retroactively represented as a different sequence.

This is **same-harness** review, not human review, independent-model-family review, formal/kernel verification, or novelty/priority verification.
