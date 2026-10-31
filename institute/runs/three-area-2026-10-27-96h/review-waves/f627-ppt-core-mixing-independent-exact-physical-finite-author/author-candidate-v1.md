# f627 independent exact physical finite-checker author candidate

**Status: SOURCE AUTHORED; SCIENTIFIC EXECUTION NOT RUN.** This is a nonblind, same-harness, independent implementation against the complete f605 author body and the frozen parent disposition. It is a proposed finite corroboration, not an executed verification, independent-model-family review, human review, formal proof, novelty determination, or parent acceptance. No check, control, time bound, or program output below is represented as having passed. The general SN2 result remains the separately reviewed written claim, not a conclusion inferred from a sample.

## 1. Provenance and execution chronology

I read the complete f627 manifest, freeze and dispatch receipts, parent-supplied metadata through its ending, and all 15 manifest-listed controls through their endings. I independently obtained the live manifest SHA256 `3c708102143e2f335613e432a635188cb5b73284182124a4142a0f7f33652d0a` and freeze-receipt SHA256 `e4225c63a8c5caed5b88f2a44786b70a244c040644c4b2d6e3ec85de7eced8f4`; both match the assignment. I then sent Main a direct pre-body ACK. Only afterwards did I read the complete literal packet in consecutive raw windows of at most 20 LF, lines 1–795 including the ending, and only after that did I derive the constructions and author the source. S1 was the 736-logical-line f605 author candidate; S2 was the complete 57-line parent disposition. The packet's SHA256 `38721105a35d39670fa2d95f659d4aa5728920ddaf68df44ab4edbaeada988ea` and input-source pins are parent-supplied metadata, not child-computed source or packet hashes.

All held episodes and their downstream consumers, including f586/f602/f596, were NONINPUT; quarantine controls were status/permission inputs only. The fresh selected cases below and the independent code design were developed prospectively under this FINITEAUTHOR duty. No scientific executable, selected-case computation, build, test, lint, external model, package installation, source follow, or paid/remote work was run. Hashing the proposed file and recording the clock were metadata operations only. No cognitive-isolation or independent-vendor certificate is claimed.

**Proposed source:** [independent-ppt-coremixing-physical-exact-v1.py](independent-ppt-coremixing-physical-exact-v1.py), SHA256 `361760d030fff86c55e1c4642628dbee915fce91cd7c24866427a9c85f608ddd`, 27,432 bytes, 764 LF; these metadata were observed after writing, and a subsequent native clock read reported `2026-10-30T14:51:10-0700 PDT`. The source file is the complete standalone source, not a pseudocode excerpt. It imports only `fractions` and `itertools`; it does not read or write files, access a network, launch children, install dependencies, or delete anything. Its only intended I/O is stdout. No runtime is claimed; a parent must first inspect it and, if authorized, execute it under its own bounded one-shot procedure. In particular, the requested ≤55-second budget has not been demonstrated.

## 2. Actual target and independently reconstructed interfaces

For `e_ab=|a>⊗|b>` write

`A=e00+e11+e22`, `B=e01+e12`, `D=e10−e21`, `E=e20+e33`,

`Q=[A]+[B]+[D]+s([e02+e34]+[e32]+[e04])+r([E]+[e23]+[e30])`,

where `[v]=vv†`; this is the actual 20×20 operator in Alice-major/Bob-minor order. For `w=(α,β,γ)`, the physical 4×5 matrix `K=[I4 | (α,β,γ,0)^T]` produces the actual 16×16 `R=(I⊗K)Q(I⊗K)†`. A separate direct-projector construction is compared at **all 256 entries**. The program also computes the physical Bob partial transpose entry by entry and checks

`R^Γ=(I⊗conj(K)) Q^Γ (I⊗conj(K))†`,

again at all 256 entries. It prints every output and partial-transpose entry, not a compressed surrogate. For the assigned member it also prints the entire 20×20 `Q` and 4×5 `K`.

The output-source trace and physical success probability are independently specified as

`T=7+4(s+r)`, `Z=7+2s(1+|α|²+|β|²+|γ|²)+4r`, `p=Z/((1+||w||²)T)`.

The `K K†` contraction defect is checked by exact Hermitian LDL. Partial traces are computed directly, and their positive definiteness is checked by exact LDL, rather than inferred from a trace alone. For the source-assigned `s=r=3`, `w=(1,1,1)`, the program requires `Z=43`, `T=31`, and `p=43/124`; here the actual contraction is `K/2`. It requires the **unnormalized** Alice and Bob marginals to equal respectively

```
[[14,0,0,3], [0,3,0,0], [0,0,8,0], [3,0,0,18]]
[[14,6,6,0], [6,9,6,0], [6,6,14,0], [0,0,0,6]]
```

(the normalized marginals divide each by 43). These are frozen-source targets, not recorded checker output.

For source-region parameters `s>1`, `r>1`, `(s−1)(r−1)≥4`, the program independently assembles the physical PPT PSD sum, including complex conjugation of `w`. Its central block uses

`[e02+e11−e20]+(s−1)[e02+2e20/(s−1)]+(r−1−4/(s−1))[e20]`.

All weights and the entire matrix identity are checked exactly, including equality. The separate LDL check of the *actual* 16×16 partial transpose does not prove a universal characterization outside the source region. A case outside that region is a genuine `Q,K,R` calculation, not a fabricated state. As a written case-specific observation, the selected `s=r=2,w=0` has central partial-transpose principal minor `det([[2,1,1],[1,1,−1],[1,−1,2]])=−3`; if the program is run, it is designed to require NPT there. Neither this case nor the sufficient parent-region proof implies a filtered-output PPT iff statement.

## 3. Proposed exact Schmidt-rank checks

The source implements finite cyclic-character rings `Q(i)[C5]` and `Q(i)[C3]` with integer exponents modulo the respective group orders and Gaussian-rational coefficients. The coefficient of the identity character equals the exact average over all complex roots. It computes each outer-product entry in that ring and extracts this coefficient; no trigonometric values, numerical roots, floats, or positivity tolerances are used. Vanishing of a formal group-ring minor is stronger than evaluation at the individual roots, but this program applies it to the selected parameter cases only.

For the five-character vector

`V_z=zA+B−z²D+z⁻¹U+βz⁻²e32`, `U=e02+αe30+βe31`,

the code checks on the actual 4×4 coefficient matrix both `C2=z⁻¹ C1`, `C3=0` and **every** 3×3 minor. It independently computes the exact character mean and compares every entry with `[A]+[B]+[D]+[U]+|β|²[e32]`. For a selected case in the ellipsoid it builds and checks the actual positive identity

```
R = mean_z[V_z]
  + (s−1)[U + (sγ/(s−1))e32]
  + δ[e32] + r[E] + s[0w] + r[e23] + r[e30],
δ = s−|β|²−s|γ|²/(s−1) ≥ 0.
```

All scalar weights are exact and checked nonnegative; all residual coefficient matrices have every 3×3 minor checked. The source does not assume the formula as an already-checked result: it compares the constructed sum against the actual filtered matrix.

For the `β` line the code checks every 3×3 minor and the dependent-column identity for `T_ζ=A+ζD+ζ⁻¹e01`; it checks the exact three-root mean `[A]+[D]+[e01]` and the actual output decomposition when `s|β|²≥1`. It also tests both overlapping endpoints in the listed cases. The written coverage argument is `s>1 ⇒ 1/s<s`; hence `|β|²≤s` or `|β|²≥1/s` covers all finite complex `β`, but finite program cases do not themselves establish this quantified statement.

For the `γ` line, it constructs the `β=α=0` five-character mean and checks the complete-square identity with `x=|γ|²` and the vector `e32+conj(γ)e02/(1+x)`. The coefficients `s(1+x)` and `s−1+s x²/(1+x)` are required nonnegative. The input includes a large nonreal `γ` outside the ellipsoid; no infinite/projective endpoint is claimed.

## 4. Formal range, local-filter, and entanglement boundaries

The source has an independent sparse **formal monomial-dictionary** implementation over the 12 variables `a,b,c,d,e,f,g,h,k,α,β,γ`. It constructs the actual output range matrix

```
[a+αh, b+βh, c+γh, 0]
[d,    a,    b,    0]
[e,   −d,    a,    k]
[f+αc, βc,   g+γc, e]
```

and checks the explicitly indexed output 2×2 minors `m1=a²+bd`, `m2=ad−be`, `m3=ae` and the *formal polynomial identity* `a²m1−abm2−b²m3=a⁴`, as well as the `11` entry `a`. It also constructs the original 4×5 source range matrix, computes the five specified 3×3 minors directly by row/column indices, and checks the corrected formal source identity `2a(g5−g3−g4)−(cg1+eg2)=2a⁴`. The intended meaning of a successful formal check would be an exact polynomial identity, not an extrapolation from sampled SN3 states; execution and independent review are still unpaid.

The written lower-bound interface is separate from the finite upper decompositions: a rank-one range vector has all these 2×2 minors zero, so the displayed identity forces `a=0` over `C`. Positive separable decompositions require each product vector to lie in the output range, whereas `R_(11,11)=1`. The obstruction must use the `11` coordinate, not `00`: an actual product vector `|0w>` can have nonzero `00` when `α≠0`. This is an entanglement/SN≥2 obstruction, **not** an SN3 detector.

The code verifies the literal kernel vector `(-α,-β,-γ,0,1)^T`, the rank-four identity submatrix, and an explicit invertible nonreal output change

```
L     = [[1,i,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,2]],
L^(-1)= [[1,-i,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1/2]].
```

It compares all entries of the `LK` physical output with the congruence of the original output. This single selected `L` is only finite evidence. The general *written* interface is: equal kernels and rank four induce an isomorphism of the common four-dimensional quotient, hence `K'=LK` for some invertible complex `L`; applying `L` and its inverse to Schmidt-rank-at-most-two decompositions preserves the Schmidt number. Physical rescaling must be applied before interpreting a success probability. No sampled `L` is offered as a proof of the universal interface.

## 5. Frozen finite inputs and intended controls

The following are source inputs, not observed test results:

| case | `(s,r)` | `(α,β,γ)` | Intended coverage |
|---|---:|---|---|
| assigned | `(3,3)` | `(1,1,1)` | simultaneous core mixing; trace/marginals/`43/124` |
| zero | `(3,3)` | `(0,0,0)` | zero terms and both ellipsoid/γ-line construction |
| both-boundaries-complex | `(5,2)` | `(2+i, 1, 8/5+4i/5)` | PPT boundary and ellipsoid boundary, nonreal |
| huge-alpha-complex | `(5,2)` | `(100000+70001i, 1+i, 1−i)` | finite huge α, nonreal β and γ, interior |
| beta-outside-ellipse | `(3,3)` | `(0,2+i,0)` | `|β|²=5>s`, three-root line |
| beta-lower-endpoint | `(5,2)` | `(0,(1+2i)/5,0)` | `s|β|²=1`, zero line residual |
| beta-upper-endpoint | `(5,2)` | `(0,1+2i,0)` | `|β|²=s`, ellipsoid boundary and line |
| gamma-large-outside | `(3,3)` | `(0,0,40+30i)` | large nonreal γ outside ellipsoid, full line square |
| outside-source | `(2,2)` | `(0,0,0)` | actual finite NPT case, no universal iff claim |

The source includes negative controls that must fail for their named intended reason, with exact nonzero discrepancy signatures where appropriate:

1. `WRONG_KBAR`: replacing conjugated `K` by `K` in the partial-transpose congruence; the prescribed complex case checks the `(00,32)` discrepancy `−2si`.
2. `FOUR_ROOT_CROSS_TERM`: four rather than five roots; the `(10,32)` difference is `−conj(β)` from the unwanted `D`–`e32` cross term.
3. `DELTA_DENOMINATOR`: omitting the `s−1` denominator; its `(32,32)` discrepancy is `|γ|²/(s−1)`.
4. `ELLIPSOID_GAMMA_CONJUGATE`: wrong conjugation of γ in the ellipsoid square; its `(02,32)` discrepancy is `s(γ−conj(γ))`.
5. `BETA_COVERAGE_GAP`: a deliberately reversed pair of intervals misses a point in the true overlap. This is a rejected coverage rule, not an excluded physical state.
6. `GAMMA_LINE_CONJUGATE`: wrong conjugation in the whole-line square, with the same exact-signature form at a nonreal γ.
7. `WRONG_PRODUCT_VECTOR_00_INDEX`: the nonzero actual rank-one range vector `|0w>` disproves the incorrect `00`-entry obstruction, while the required `11` entry remains zero and the physical `R_(11,11)=1`.
8. `FILTERED_IFF_SCOPE_OVERCLAIM` and `FINITE_TO_UNIVERSAL_SCOPE_OVERCLAIM`: explicit scope-guard rejections. They are logic/claim guards, not fake counterexamples or physical states.

Controls catch only `CheckFailure` carrying their exact intended label; unexpected exceptions or a control that accepts do not count as intended rejection. An independent parent should inspect the source and failure sites rather than assuming these controls will work.

## 6. Parent handoff and unpaid steps

The parent may statically review and freeze the exact pinned source, then make its own bounded execution decision consistent with the run control. The prospective command is `python3 -B independent-ppt-coremixing-physical-exact-v1.py` in this wave directory. A valid execution receipt must report the actual source hash, interpreter/command, bounded runtime, exit status, stdout and stderr, complete output, all named intended-reason controls, and any failure; no result or ≤55-second runtime is pre-claimed here. If it fails, the failure is evidence, not a pass, and corrections require new additive files rather than overwriting this source or this report.

The proper-family SN2 continuum, complex range lower bound, PPT sufficiency and general same-kernel interface need the separately assigned written reviews and parent disposition. The selected exact finite checks, even if later successful, cannot prove quantified SN3 claims or universal detector block positivity. The unrestricted `4×4` PPT/SN3 existence problem, arbitrary filters (including the missing fourth component of `w`), filtered PPT necessity outside the parent region, exhaustive prior-art/novelty, and independent-family/human/kernel verification remain open or unpaid. The parent may attribute the published parent construction only to the prior source already identified in S2; no fresh literature comparison was performed.
