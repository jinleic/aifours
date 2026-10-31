# Independent scientific review: two PPT-grid kernel planes and phase charts

**Native clock observed immediately before this file was created:** 2026-10-28T19:02:19-0700 PDT  
**Binding assignment:** `manifest-v3.json`, SHA-256 `211781d48b70a8abcd1c4d6ea484d8cce9a38e31994dec978414ec56ab3a453b`.  
**Method:** same-harness reviewer, own exact Gaussian-rational and sparse-polynomial computations; no author checker executed, no author contact, no external model.

## Verdicts and findings

| Object | Verdict | Fatal / major / minor |
|---|---|---:|
| Entire plane `P(span{0,2,3})` | Mathematical assertion supported, including its projective boundary, using the independent boundary argument below; its cited boundary source is wrong. | 0 / 0 / 1 |
| Entire reflected plane `P(span{0,2,4})` | Mathematical assertion supported by independently checked local symmetry and the same boundary argument. | 0 / 0 / 1 shared |
| 4/5-phase interpolation | No mathematical defect found within the stated sufficient domain, including singular boundaries. | 0 / 0 / 0 |
| Optimal interpolation / existence of PSD `H_p` | No mathematical defect found in the stated iff criterion or its `3<=T<6` specialization. This is **not** an iff for Schmidt number. | 0 / 0 / 0 |
| Manifest process | One redundant digest field is only a prefix; the separately stated full SHA-256 matches the bytes. | 0 / 0 / 1 |

There are **two distinct minor findings**; the plane citation finding is shared rather than double-counted.

1. **MINOR, wrong boundary citation.** `frontier-20261028-grid-two-entire-kernel-planes-v1.json:12` says the boundary `P(span{0,2})` was proved in `frontier-20261028-grid-all-two-column-compressions-v1.json`. That cited file, at lines 6, 9 and 23, proves the different family `P(span{3,4})`. It does not establish the asserted `0,2` boundary. This is an evidence/provenance defect, not a counterexample: if `ker K` lies in `span{0,2}`, then `K|0>` and `K|2>` are dependent, so the Bob support of `A'=(I⊗K)A` has dimension at most two. All other eight original generators already have Schmidt rank at most two, and local maps cannot increase it. The original nine-term sum itself is therefore an SR<=2 decomposition, for every such kernel, including both endpoints. An additive correction should supply this proof or a genuinely applicable pinned citation.
2. **MINOR process finding, literal mismatch in an auxiliary digest field.** `manifest-v3.json:58-64` gives the optimal checker's full `sha256` as `9af3335b714c7100adad5bf46e9e843dfed7085da62e12a245e8a48943b53f7f`, exactly matching the file, but its `expected` is only `9af3335b714c`. This is a matching 12-hex prefix, not a literal equality to a full SHA-256, despite `match: true`. The independent full digest verifies the input's identity; no changed input was found. An additive manifest correction can record the complete expected value and clarify the prefix comparison. Do not silently call the two strings equal.

## Pinned inputs and imports

All six primary inputs were completely read in the manifest's order in raw windows. Bytes, LF counts and the complete `sha256` values match as follows; the last row has the separate `expected`-field issue above. Paths in this table are relative to `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/`.

| Input, in order | SHA-256 | bytes / LF |
|---|---|---:|
| `frontier-20261028-grid-two-entire-kernel-planes-v1.json` | `0ba59dc04b2041605fff18acffb9eb6c072f36d03ba356863dc51cd09e9392c8` | 5521 / 21 |
| `frontier-20261028-grid-complementary-plane-check.py` | `ef12e7177a6eaea92fe39187d744131a89340ed1f5d4162b5426ad1f1fb3d336` | 3441 / 83 |
| `frontier-20261028-grid-phase-interpolation-v1.json` | `e1f92daf6dca9ae2a2196bc205ee48c690531ae654a8d4614774dbd185e4dd1e` | 5421 / 23 |
| `frontier-20261028-grid-phase-interpolation-check.py` | `d5955daf860ccb7de7858c25d444b926ba5835505883f3ac1709f1709fdbb96a` | 4092 / 97 |
| `frontier-20261028-grid-optimal-interpolation-v1.json` | `31370ff4b90de6c8073098a49f318d962d4fc9cb0efd59adf233c911294f62d3` | 4060 / 19 |
| `frontier-20261028-grid-optimal-interpolation-check.py` | `9af3335b714c7100adad5bf46e9e843dfed7085da62e12a245e8a48943b53f7f` | 2658 / 53 |

The following named local imports were also read and their indicated SHA-256 values matched: `grid-state-five-projections-v1.json` (`9863760e2ca2331164d12e62300f3ad7db5b6a17a3ef424e360d504d541004a9`), `grid-unbounded-two-head-v1.json` (`67790038cc1fea96c22eef45c909a852f238132584acf21a397f42746420baa2`), `grid-all-two-column-compressions-v1.json` (`4076912f4e4197244483b47eaa7d6e5d09207386840929db1d04814332ff9406`), `grid-mixed-zero-three-compressions-v1.json` (`25278f1e460330954c54de872f9468b880fa3f3220dbab6c15954852cb139789`), and `grid-three-head-compressions-v1.json` (`6d27bfe9b5caef577097d1131094c853bae46b1b01bc630f09b14312b1d604b5`); each abbreviated name has the prefix `frontier-20261028-`. Only the portions actually reconstructed below are adopted, not all other claims of those imports. No held or withdrawn material is a premise.

**Named unverified imports:** the external Krebs–Gachechiladze arXiv:2509.07086v1 Eq. 11 attribution, historical priority, and the correspondence of its published formula with this explicit `R` were not checked. Nor were the imported authors' unrelated projection families, numerical replays, prior-review status, or novelty claims checked. None is needed for the arguments below: the explicit state, its PPT property, source SN=3, reflection, and the entanglement inequalities were reconstructed from the displayed formulas.

## Reconstruction and exact coverage

### Source and geometry

Use `[q]=|q><q|`, `A=|00>+|11>+|22>`, `B=|01>+|12>`, `D=|10>-|21>`, `C=|02>+|34>`, `E=|20>+|33>`, `F=|23>`, `G=|30>`, `I=|32>`, `H=|04>`, and `R=[A]+[B]+[D]+3([C]+[E]+[F]+[G]+[I]+[H])`. Direct exact computation confirms trace 31 and the ten-positive-projector partial-transpose identity in `grid-state-five-projections-v1.json:10` at all 400 entries. Hence `R` is PPT. The nine source vectors have disjoint supports and are independent. Independently expanding the 40 possible 3-by-3 range minors locates all five displayed source minors and verifies the polynomial identity at that import's line 11; therefore each SR<=2 vector in `range(R)` has coefficient `a=0`, whereas `A` has `a=1`. Positivity forces ensemble vectors into the range, giving SN>=3; the displayed generating vectors have SR<=3, giving SN=3.

For the first open chart put `K|j>=|j>` for `j=0,1,2`, `K|3>=v0|0>+v1|1>+v2|2>`, and `K|4>=|3>`. Thus its kernel is `|3>-v0|0>-v1|1>-v2|2>`. Every rank-four map with the same kernel differs by an invertible output filter, which preserves PPT and Schmidt number. Direct checking of the nine source-generator images and all 400 source-state entries confirms the imported symmetry `S_A: (0,1,2,3)->(-2,1,0,3)`, `S_B: (0,1,2,3,4)->(-2,1,0,-4,-3)`. It maps parameters to the `|4>`-tail chart `(w0,w1,w2)=(-v2,-v1,v0)`; all norm conditions below are invariant under this swap.

### Two complete kernel planes

For `v1=0`, let `U=|v0|^2`, `V=|v2|^2`, `A0=1+U+V`, `X=|20>`, `s=-A0 conjugate(v0)/(1+A0 U)`, and `W=-X+s(F'-v0 X)`. Directly, `W=-|20>+s v2|22>`. In `q_z=zA'+B'+z^2D'+z^3W`, the upper 3-by-3 determinant cancels identically and the fourth row/column vanish; distinct powers modulo four give `[A']+[B']+[D']+[W]` on averaging. In the basis `L=(E',G',I',F')`, `W` has the stated coefficient vector `t0`, and its residual Gram is `3I-t0 t0*`, PSD iff `||t0||²=A0/(1+A0 U)<=3`.

When `v2!=0`, `Z=|22>` has coefficient vector `t1=(-v0/v2,v0²/v2,v0,1/v2)` in `L`. For `beta=1+i`, `delta=1-i`, `beta delta=2`, the determinant of `z(A'+Z)+beta z² B'+delta D'` is `(2-beta delta)z³=0`. The displayed four-phase average plus `[A'-Z]/2` gives `[A']+[B']+[D']+[Z]`; its residual `3I-t1 t1*` is PSD iff `U+(1+U+U²)/V<=3`. Every residual `L`-combination has only Alice rows 2 and 3, hence SR<=2.

The algebra covers **all** `v0,v2 in C`: first Gram works if `U>=1/3`, and also if `U<1/3, V<=1`; if `U<1/3, V>1`, the second norm is `<1/3+13/9=16/9<3`. For `v2=0` the first certificate is used. Add the independently proved `P(span{0,2})` projective boundary, and the first result is all `P(span{0,2,3})`; the exact symmetry gives all `P(span{0,2,4})`, including its common boundary. Each conclusion holds for every complex rank-four `K` with such a kernel, not just the displayed output normal form. Within the first open chart, `3V<4` additionally proves entanglement, so SN=2 there; the reflected condition is `3|w0|²<4`.

The entanglement proof is not inferred from Gram positivity. In the local 3-by-3 core, a range vector has rows `[[a,b,c],[d,a,b],[e+v0 f,-d+v1 f,a+v2 f]]`; for `(v1,v2)!=(0,0)` the six source coordinates are unique. Its two rank-one minors imply `2a²=-(a v2-b v1)f`. In any separable decomposition, the exact core moments are `sum |a|²=1`, `sum |f|²=3`, and `sum |a v2-b v1|²=|v1|²+|v2|²`; Cauchy–Schwarz forces `4<=3(|v1|²+|v2|²)`. For `v1=v2=0` the two minors instead force `a=0`, contradicting the presence of `A`. This establishes the cited strict entanglement conditions, including the phase example below, without relying on the imported checker.

### 4/5-phase chart

Put `T=|v1|²`, `X=E'-v0G'-v2I'=|20>+v1|31>`, `t=(1,-v0,-v2)^T`, and `L=(E',G',I')`. The five-phase seed is `q5=zA'+B'-z²D'-z³X-z⁴v1G'`: its Alice rows satisfy row 2=`z` row 1 and row 3=`-z³v1` row 0. For `q4=zA'+B'-z²v1I'-z³X`, the rows satisfy row 2=`-z²` row 0+`z` row 1 and row 3=`-z²v1` row 1. Thus both have SR<=2; distinct powers modulo 5 and 4 respectively cancel cross terms. For any `p in [0,1]`, subtracting their averaged projectors leaves exactly

`(1-p)[D']+3([C']+[F']+[H']) + sum_jk (H_p)_jk |L_j><L_k|`,

where `H_p=diag(3,3-pT,3-(1-p)T)-tt*`. All residual vectors have SR<=2. Therefore `H_p>=0` is sufficient, and `p=1/2` covers exactly the stated closed sufficient subdomain `T+3(|v0|²+|v2|²)<=6`. In particular `T=6` forces `v0=v2=0` and gives `H=diag(2,0,0)`. For positive budgets the Schur test is `1/3+|v0|²/(3-pT)+|v2|²/(3-(1-p)T)<=1`; zero budgets require the corresponding head amplitude to vanish. The `|4>`-tail reflected chart has the same quadratic condition.

For `(45/46,1/2,45/46)`, exact endpoint Schur sums are `3037/3036>1` but the half-half sum is `36467/36501<1`; `3(T+|v2|²)=3831/1058<4` establishes entanglement and SN=2. Its normalized denominator is `40187/1058`. The second stated point `(1/2,2,1/2)` has `T=4`, half-half PSD, and neither endpoint Gram PSD; no entanglement conclusion is asserted there.

### Optimal iff-for-`H_p` chart

Write `a=|v0|`, `b=|v2|`, `x=3-pT`, `y=3-(1-p)T`, and `S=x+y=6-T`. For `0<T<6`, feasible `x` lie in `[ell,u]`, `ell=max(0,3-T)`, `u=min(3,S)`, and `y=S-x`. A rank-one Schur complement, including the zero-budget convention, gives `H_p>=0` iff `1/3+a²/x+b²/y<=1`. The convex function `a²/x+b²/(S-x)` is minimized at `S*a/(a+b)` when both amplitudes are positive and at the corresponding endpoint when one vanishes; clipping that point to `[ell,u]` handles all cases. If `a=b=0`, every feasible `x` works. This proves the exact iff for existence of a PSD **member of this seed family**. At `T=0` it reduces to `a²+b²<=2`; at `T=6` it is possible iff `a=b=0` and `p=1/2`; at `T>6` it is impossible.

For `3<=T<6`, `[ell,u]=[0,S]`, so the exact seed-family criterion is `(a+b)² <= (2/3)(6-T)`. This yields the stated sufficient SN<=2 domain and its reflected counterpart, not a necessary Schmidt-number criterion. At `(1,2,1/10)`, `x=20/11`, `y=2/11`, `p=13/44`, the exact Schur sum is `563/600`, and the half-half quadratic expression is `703/100>6`.

## Independent Gaussian-rational checks

`independent-grid-verify-v1.py` implements its own `Q(i)` arithmetic, all principal minors of each Gram (15 for 4-by-4, 7 for 3-by-3), an independent exact Schur-PSD elimination, all 256 state entries, phase-vector 3-by-3 minors, and exact partial-transpose pivots. For the 5-phase polynomial, all 16 3-by-3 minors have degree at most 12, so checking them at 13 distinct rational values proves their vanishing for each sampled parameter point; distinct powers modulo 5 give the exact twirl. The universal complex-parameter claims above rest on the written row and inequality proofs, not on sample extrapolation.

Plane points: first and second columns are `||t0||²` and `||t1||²`; a norm exceeds 3 exactly when that individual Gram fails. Each available decomposition identity was checked even when its Gram failed, and each point had at least one PSD Gram. The final two points are mine.

| `(v0,v2)` | first norm | second norm |
|---|---:|---:|
| `(0,2)` | 5 | 1/4 |
| `(1/2,4)` | 276/85 | 85/256 |
| `(i/2,1+i)` | 52/29 | 29/32 |
| `(2,1)` | 6/25 | 25 |
| `((1+i)/4,1)` | 136/81 | 81/64 |
| **own** `((1+i)/2,0)` | 6/7 | undefined, correctly uses first Gram |
| **own** `(i/4,3+i)` | 2832/433 | 433/2560 |

The reflected points are also covered by the independently checked exact symmetry, with `(w0,w2)=(-v2,v0)`.

For phase/optimal points, all displayed Gram pivots are nonnegative and all state identities, 4-phase minors and partial-transpose checks pass; a missing final pivot denotes a zero Schur remainder. Two of my points exercise the half-half chart and two further points exercise the optimal chart, including a zero budget and a clipped optimizer.

| Point `(v0,v1,v2)` | `p` | exact Gram pivots |
|---|---:|---|
| author `(45/46,1/2,45/46)` | 1/2 | `2, 1523/1058, 391/48736` |
| author `(1/2,2,1/2)` | 1/2 | `2, 5/8, 2/5` |
| author's third checker point `(1+i/2,1,1/2)` | 1/2 | `2, 5/8, 1` |
| **own phase boundary** `(1,0,i)` | 1/2 | `2, 3/2` (singular) |
| **own phase complex** `((1+i)/4,1+i,(1-2i)/4)` | 1/2 | `2, 29/16, 43/29` |
| author optimal `(1,2,1/10)` | 13/44 | `2, 7/22, 37/385` |
| **own optimal zero budget** `(0,2,(1+i)/2)` | 3/4 | `2, 5/4` (singular; `x=0`) |
| **own optimal clipped** `(2/5,i,(1+i)/2)` | 1 | `2, 44/25, 189/88` |

For the last point, `T=1`, `ell=2`, `u=3`; `3a<2b` puts the unconstrained minimizer below 2, so `x*=2` and `p=1`. For the zero-budget point, `T=4`, `a=0`, and the optimum is `x*=0`, `y*=2`, `p=3/4`. Both are exact Gaussian-rational witnesses; square roots occur only in the analytic amplitude comparison.

## Reproducibility and limits

- `independent-grid-verify-v1.py`: SHA-256 `f7fc4adf77970625ac717559048efdb7a50a95216f0ddbd7396346bb14ccf9e6`; successful exit 0. Its `independent-grid-receipt-v1.json` SHA-256 is `f1aacac0020d3eb35cf2a3ebe3f706126782c257f8cfbe0d966f046ff7c97657`.
- `independent-source-minors-v1.py`: SHA-256 `cfa55b68b8ee0c349802701f04b011063f862fec66a425d093adf54bf3dc281f`; successful exit 0. Its `independent-source-minors-receipt-v1.json` SHA-256 is `9b95e3733e1a6104a3cc0d8b1665864c99ca6887f0f1111694cbec580018fc5f`.
- Replay from this directory with `python3 -B independent-grid-verify-v1.py` and `python3 -B independent-source-minors-v1.py`. The saved receipts were created exclusively and contain the complete exact outputs.
- These are proper, specific kernel families for the explicit `R`; no conclusion follows for generic kernels having both `|3>` and `|4>` coefficients, arbitrary 4-by-4 PPT states, existence of a 4-by-4 SN>=3 witness, or optimality among all possible SR2 decompositions. No external-family, human, formal, or novelty verification was performed. This review does not itself amend the pinned candidate or manifest.
