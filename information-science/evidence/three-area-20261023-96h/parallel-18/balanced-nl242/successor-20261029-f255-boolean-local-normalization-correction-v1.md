# f255 additive correction: Boolean-to-local Walsh normalization

**MANDATORY ADDITIVE AUTHOR CANDIDATE.** Native clock observed before writing: **2026-10-29T15:33:27-0700**. This correction addresses f255 M1 and m1 for the unchanged cross-fibre candidate `successor-20261029-f244-residual-cross-fibre-placement-v1.md`, SHA-256 `686dd9177d6ff8788b6463d8d4e444e8bda4231ce7060a76ad0cfdea5f39144c`, 183 LF. The base and review bytes remain unchanged.

**Status.** The original Boolean necessity of the base candidate is **not yet parent-adopted**. This is a new written bridge and clarification requiring a separately scoped disjoint review and parent disposition. It does not prove a witness, a complete `(0,4,8)` exclusion, a rank-two/global exclusion, novelty or formal verification.

**Review exposure.** After Main explicitly instructed me to read f255, I read the complete 140-LF `f255 .../review-v1.md` in raw ranges LF1–50, LF51–100 and LF101–140, including the ending, before preparing this correction. Whole-file SHA-256 `38a15d7d39cb26d2aa0277546318023e09249135a1fd9f0993830e19d7920958`; the frozen 30-LF manifest, SHA-256 `ccd41880d913a0ae12913dcde161533e41ddf6234dff7f3acab1432e81aa4fd6`, was also displayed. The review reports 0 FATAL / 1 MAJOR / 1 MINOR. Its conditional geometric, XOR, sign-mismatch and all-translation reconstructions are review findings, not a parent adoption of the original-object bridge.

The reviewer's own exact-control results are not re-executed or treated as an original-Boolean witness. No scientific computation, solver, test, nested agent, model CLI, Git, deletion or publication was performed for this correction. The old P1 profile roster, f239/CR7, and held or withdrawn sources/episodes remain **NONINPUT**.

## 1. Exact correction to the base candidate's input claim

In base §2, do **not** say that the 24-LF f244 disposition explicitly supplies the full identity

`16U_s(c)=3 Walsh_R(σ_s)(c)−2t_s(c)`.

It does not explicitly state the underlying caller, inverse, local transform or this normalization. Instead, derive them from the original Boolean object as in §§2–4 below. The f244 disposition is used only for its stated rank-two/eight-zero m=116 fibre scope, `T≠0`, `q⁻¹(0)=R`, the 4/8 atom and 23-position/affine-relation facts, and the specified `(G₃,H)=(1,0)` residual. The separately adopted original-object caller is an explicitly named prerequisite; the derivation below does not depend on unlisted linked author files.

## 2. Derive the common ternary inverse from the Boolean object

Let `f:F₂⁹→{0,1}` be balanced with `max|W_f|≤28`. Write `s(x)=(-1)^{f(x)}`, `k=W_f/4`, and `T=⊕{x:f(x)=1}`. The accepted scope gives `T≠0`, so `K=T^⊥` has dimension 8.

Choose `a₀∈F₂⁹` with `a₀·T=1`, and define the **linear** hyperplane `V=a₀^⊥`. Then `F₂⁹=V⊕⟨T⟩`. Restriction identifies K with V*: every `a∈K` has a unique character on V. Define, for y∈V,

`u(y)=[s(y)+s(y+T)]/2`.

The numerator is −2, 0 or 2, so `u∈{−1,0,1}`. Moreover `u(y)≠0` exactly when the unordered pair `{y,y+T}` agrees. Consequently the original f's agreeing-pair count is

`m=Σ_{y∈V}u(y)²=|supp u|`.

Since f is balanced, `Σ_y u(y)=(1/2)Σ_x s(x)=0`. Use the unnormalized transform `Walsh_V(u)(a)=Σ_{y∈V}u(y)(−1)^{a·y}` for `a∈K`. Since a·T=0,

`W_f(a)=Σ_{y∈V}[s(y)+s(y+T)](-1)^{a·y}=2 Walsh_V(u)(a)`.

Therefore

`Walsh_V(u)(a)=W_f(a)/2=2k(a)` for **every** a∈K.            (B1)

This identity, rather than an assumed inverse array, is the common Boolean-to-even-half bridge.

## 3. Derive the shared fibre/block coordinates and equation (1)

At the frozen f244 target scope, `rank B=2`, its radical R has dimension 6, and the even quadratic q vanishes exactly on R. Choose a **linear** complement P so that `K=R⊕P`, `dim P=2`. Since R is the radical and q vanishes on R, q is constant along R-cosets; the rank-two quotient is anisotropic. Label the four P elements by `s=0,1,2,3`, where q=0 exactly at s=0.

The pairing between K and V is nondegenerate. Its dual decomposition identifies each y∈V uniquely with `(c,z)∈R*⊕P*`: `a=(r,s)` pairs with y by `r·c+s·z`. This is one **shared** choice for both s=2 and s=3, not two unrelated six-dimensional transforms.

For each c∈R* and s∈P define the four-point block transform

`U_s(c)=Σ_{z∈P*}u(c,z)(−1)^{s·z}`.                            (B2)

Every U_s(c) is an integer in [−4,4]. Its common eight-dimensional inverse is exactly the u from §2, and

`m=Σ_{c,z}u(c,z)²`, `Σ_s U_s(c)²=4Σ_z u(c,z)²`.               (B3)

Splitting the character sum in (B1) gives

`2k(r,s)=Σ_{c∈R*} U_s(c)(−1)^{r·c}`.                           (B4)

For s≠0, q=1. The caller's `|k|≤7`, evenness on K and `q=k/2 mod 2` imply `k(r,s)∈{±2,±6}`. Define

`v_s(r)=k(r,s)/2∈{±1,±3}`, `σ_s(r)=sign v_s(r)`,
`A_s={r∈R:|v_s(r)|=1}`, `τ_s(r)=σ_s(r)1_{A_s}(r)`.

Thus the original f's fibre cardinality is `e_s=|A_s|`, and pointwise

`2k(r,s)=4v_s(r)=12σ_s(r)−8τ_s(r)`.                             (B5)

Define unnormalized transforms over R, whose outputs are indexed by the **same** c∈R*:

`Walsh_R(σ_s)(c)=Σ_{r∈R}σ_s(r)(−1)^{r·c}`, `t_s(c)=Walsh_R(τ_s)(c)`.

Applying 64-point character inversion to (B4), then substituting (B5), yields

`U_s(c)=[12 Walsh_R(σ_s)(c)−8t_s(c)]/64`,

or, exactly as needed,

`16U_s(c)=3Walsh_R(σ_s)(c)−2t_s(c)`.                            (B6)

In particular `U_s(c)≡t_s(c) (mod 3)`. No solver, selected profile roster, separate-fibre placement assumption, or inverse normalization is needed.

## 4. Direct energy, local range, and the common-zero count

At f244 scope, there are 8 Walsh zeros and q vanishes exactly on R. Odd-half k is odd, so all zeros are in the s=0 fibre. On that fibre the 56 nonzero k-values are ±4; on nonzero s the values are ±2 or ±6. Six-dimensional Parseval applied to (B4) gives

`Σ_c U₀(c)²=56`, `Σ_c U_s(c)²=144−2e_s` for s=1,2,3.       (B7)

For `(e₁,e₂,e₃)=(0,4,8)` the three nonzero-fibre energies are 144,136,128. Since e₁=0, t₁=0; (B6) makes every integer U₁ divisible by 3. Its absolute value is at most 4, so U₁∈{0,±3}, with exactly 16 nonzero blocks by energy 144.

Each block with U₁=±3 contains exactly three ±1 entries, and its other three Walsh entries have magnitude 1. In every block, all four U_s are congruent modulo 2 because `−1≡1 (mod 2)`. Hence in the remaining 48 blocks U₀,U₂,U₃ are all even. There, a four-point ternary transform is either all zero, has exactly two ±2 entries among U₀,U₂,U₃, or has exactly one ±4 entry among those three. In particular **U₂ and U₃ are never ±3**, so (B6) implies

`U_s(c)=0  ⇔  t_s(c)≡0 (mod 3)` for s=2,3.                   (B8)

This is a direct original-object derivation of the equivalence needed for the common zero sets.

We also spell out the 17 common-zero count without importing an undefined class table. The four-atom fibre has the f244 zero count `#{U₂=0}=24`; its energy 136, the 16 magnitude-one values and the even local range force exactly two U₂ peaks of magnitude 4. The f244 eight-atom relation gives `#{U₃=0}=23`; its energy 128 similarly forces exactly one U₃ peak.

Among the 48 U₁=0 blocks, let a,b,c count pairs of ±2 at coordinates `(U₀,U₂)`, `(U₀,U₃)`, `(U₂,U₃)` respectively; let d count U₀ peaks and o zero blocks. Then the three energies and the total of 48 blocks give

`a+b+4d=10`, `a+c=22`, `b+c=24`, `a+b+c+d+o+2+1=48`,

so `a=4−2d`, `b=6−2d`, `c=18+2d`, `o=17+d`. Here d is exactly the H count. At the frozen residual H=0, the common zero set of U₂ and U₃ consists of the 17 zero blocks:

`|{c:U₂(c)=U₃(c)=0}|=17`.                                     (B9)

The remaining rank-three four-atom flat structure and rank-six eight-atom normal form are the explicitly scoped f244 facts reconstructed conditionally by f255. Combining (B8)–(B9) with those facts supplies the original-object input required by the base candidate's common-hyperplane and placement arguments. It does not itself re-adopt the reviewer's conditional conclusions.

## 5. The all-translation shear comes from one Boolean object

The shared R-coordinates in §3 can be changed without changing f. Let `L:P→R` be any linear map with `L(2)=t` and `L(3)=0`, possible because 2 and 3 are independent nonzero labels in P. Replace P by its graph `{s+L(s):s∈P}`.

In the new coordinates the actual same k has `k'(r,s)=k(r+L(s),s)`. Hence

`A'_2=A₂+t`, `A'_3=A₃`, `σ'_2(r)=σ₂(r+t)`, `σ'_3(r)=σ₃(r)`.

At fixed block character c, the dual z-coordinate changes by `c∘L`, and therefore

`U'_s(c)=(-1)^{L(s)·c}U_s(c)`.

Thus every absolute local shape, e_s, m, the `(G₃,H)` residual, and the zero and absolute-value conditions used in the base candidate are preserved. This supplies the quantifier bridge for all `t∈R`; it is an actual linear coordinate change of the single Boolean object, not a new independently chosen spectrum.

## 6. MINOR m1: state the correct general parity identity

In base equation (3), for an arbitrary **even** number e of signed atoms with n⁻ negative signs and XOR X, the correct expansion is

` t(c)/2 ≡ e/2 + n⁻ + X·c  (mod 2)`.                          (B10)

Indeed `(-1)^{a·c}=1−2(a·c)` modulo 4 and `Σ_a ε_a=e−2n⁻`; dividing by 2 and reducing modulo 2 gives (B10). The shorter formula `t/2≡n⁻+X·c` requires `e/2` even, not merely e even. At the present actual fibre sizes **e₂=4 and e₃=8**, e/2 is even in both cases, so the base candidate's displayed formula and its derived XOR/sign-product equality are unchanged at the frozen scope.

For an intended-reason negative example, two positive atoms have e=2 and `t(0)/2=1`, whereas the shortened expression gives 0. This is a hand arithmetic illustration, not a computational test.

## 7. What is and is not repaired

The displayed Boolean construction derives the definitions, ternary values, exact energy normalization, one shared local-Walsh system, the needed mod-3 zero equivalence, the 17 common-zero count, and the all-translation coordinate change from the original f under the expressly stated f244 hypotheses. It addresses M1's missing premise; (B10) addresses m1.

If this bridge is separately reviewed and accepted, the conditional f255 reconstructions can be reconsidered as necessary conditions on that original-object residual: equal atom XOR/sign product, the all-translation support-intersection bound, and the sign-mismatch constraints. **This sentence is a conditional review route, not a claim that Main has adopted those conclusions.** The formal placement in the base remains a non-witness, and the original Boolean residual, the six other f244 pairs, all other fibre patterns, rank two and the global balanced target remain OPEN.

This correction does not expand the f255 frozen scope, incorporate the reviewer's code as a proof, or alter historical STOP/HOLD/ZERO/NONINPUT boundaries. A successor review must receive both the immutable base and this full additive correction with exact source pins; its own scope and adoption are for Main to decide.

## 8. Exact inputs and provenance

`P=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`; `F=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f255-nl242-residual-cross-fibre-placement/`.

| Input | SHA-256 | LF | Role |
|---|---|---:|---|
| `P/info-6-nl242-rank2-eightzero-116-fibre-048-obstruction-parent-v1.md` | `18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912` | 24 | f244 adopted at its explicit scope |
| `P/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | explicitly named original-object caller |
| `successor-20261029-f244-residual-cross-fibre-placement-v1.md` | `686dd9177d6ff8788b6463d8d4e444e8bda4231ce7060a76ad0cfdea5f39144c` | 183 | immutable author base |
| `F/review-v1.md` | `38a15d7d39cb26d2aa0277546318023e09249135a1fd9f0993830e19d7920958` | 140 | full f255 review, exposure disclosed above |

Source hashes and LF counts were observed by metadata-only calls before this write. Same-harness review is not independent-model-family, human, formal/kernel or novelty verification.
