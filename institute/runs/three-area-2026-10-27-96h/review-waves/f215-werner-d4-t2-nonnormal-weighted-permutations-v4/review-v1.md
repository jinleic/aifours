# f215 — independent same-harness review of the frozen Werner v4 packet

**Disposition: 0 FATAL / 0 MAJOR / 1 MINOR; INCONCLUSIVE: the remaining general two-copy obligation, the unrestricted both-squares-nonnormal region, T3, Z2, original-target closure, and novelty.** At the stated scopes, I independently reconstruct the weighted-partial-permutation operator bound, cyclic grade/equality result, rank-one-B result and gap, restricted 4×2 lemma, square-normal result, and tail/variance tests. This is written mathematical support, not parent adoption. The square-normal proof **does depend** on the previously unadmitted 4×2 lemma in its nonnormal two-block case; I reconstruct that lemma below with **both** trace-zero hypotheses, and the structural decomposition supplies exactly those hypotheses for each block. The normal subcase is separate. The arbitrary-T extension is false and is not used.

Native clock observed before composing this report: **2026-10-29T13:31:37-0700 PDT**. This is not a claimed file-creation time.

## Frozen inputs and actual sequence

The first research artifact opened was `manifest-v1.json` in this wave. Its measured SHA-256 was `4bfd67422734409c8689e6bb9cc34a240ed4501443d5f4ae05f9d6eb70524ed6`, matching the required prefix `4bfd67422734`. Before opening any input body, I measured SHA-256, byte count, and LF count for **all four** inputs and compared each to the manifest; all matched. The initial manifest display truncated the long scope and requirements lines 9 and 43; I read those two lines raw after the four input bodies and before any mathematical reconstruction or control. The displayed input list and identity fields were complete at the initial read. No mathematical body outside these four inputs was opened or used.

Let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h` and `P=/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart`. Input bodies were then displayed completely, in the following order, in raw windows. Ranges with an upper endpoint past the last LF reached EOF; no nonexistent extra line is claimed.

| Order and input | Measured SHA-256 | Bytes | LF | Raw windows actually requested |
|---|---|---:|---:|---|
| 1. `P/frontier-20261029-f198-block-bound-trace-erratum-v1.json`, mandatory erratum first | `c00425bb6e64b322a251d07f03aa277dc8591c87d68c0e94ab7eacb54a544205` | 4521 | 14 | 1–7, 8–15 (EOF at 14) |
| 2. `R/dispositions/physics-1-werner-stratified-duals-and-support-ladder-parent-v1.md` | `adbc15fdcccb66519353a8288993f571d9e94931ffae23c77f7a01da3d8579bf` | 7488 | 41 | 1–11, 12–22, 23–33, 34–42 (EOF at 41) |
| 3. `R/dispositions/physics-1-werner-d4-t2-rank-one-reduction-and-safe-classes-parent-v1.md` | `1eebc50e0ec0a17e92294b548344edf271c1c1516e57956fdb2cf6cece2c8049` | 5100 | 22 | 1–11, 12–23 (EOF at 22) |
| 4. `P/frontier-20261029-d4-t2-nonnormal-weighted-permutations-unified-v4.md` | `fab0ed2a598dba3de737bb37d56439a76e7e784fb5095d0b9af84b725ac06199` | 12625 | 128 | 1–12, 13–24, 25–36, 37–48, 49–60, 61–72, 73–84, 85–96, 97–108, 109–120, 121–129 (EOF at 128) |

The erratum's report of an earlier counterexample and its dependency inventory were treated as warnings, not as a proof or as a review/adoption. The direct counterexample below was independently constructed. The linked source and review bodies mentioned in the dispositions and the v2/v3 bodies were not opened.

## Per-claim disposition

| Claim | Verdict | Basis and boundary |
|---|---|---|
| §1 dual target, normalization, and relation to T3 | **0F/0M/0m** | The exact f168 dual/ladder is an explicitly adopted import; the normalization is checked below. No T2 or T3 closure follows. |
| §2 arbitrary zero-diagonal weighted partial permutations, unequal sizes, unitary similarities, and strict-gap condition | **0F/0M/0m** | Rowwise complex Cauchy–Schwarz gives the stated sharper bound. The examples and nonnormal/spectral-test claims are also reconstructed below. |
| §3 cyclic weighted shifts, all d≥3, grade bound and iff equality | **0F/0M/0m** | Independent grade-block and no-four-cycle rank proof below, including zero matrices and arbitrary complex phases. The d≥3 hypothesis is essential to this equality classification. |
| §4 trace-zero lemma, all-variable (†) and explicit gap | **0F/0M/0m** | Weighted-Hilbert–Schmidt projection and singular-limit argument reconstructed, including complex inner products. |
| §4 all traceless rank≤1 B | **0F/0M/0m** | Mixed-pair completion, same-block supported-site case, and all-zero/rank-zero cases reconstructed; the (†) equivalence is also shown. |
| §5 4×2 bound with Tr A=Tr T=0 | **0F/0M/0m** | Independent swap and trace-removal proof below. This is only same-harness support of a previously unadmitted restricted claim; no unrestricted-T premise is allowed. |
| §6.1 one-supported-site lemma | **0F/0M/1m** | It follows from the adopted f168 ladder and dual. **Minor:** the proof's last sentence says “proving (5.1),” but the argument proves the displayed Lemma 6.1, not the §5 operator-norm inequality (5.1). Correct the cross-reference to “Lemma 6.1”; §5 has its own valid proof. |
| §6.2 A²- or B²-normal | **0F/0M/0m** | Dimension-four structure and block argument reconstructed. The nonnormal case uses §5 with separately traceless blocks; the normal case does not. |
| §7 tail and fourth-moment/variance sufficient tests, including strictness | **0F/0M/0m** | Exact expansion and the 16-eigenvalue mean-zero Cauchy–Schwarz calculation reconstructed. They are sufficient, not exhaustive. |
| §8 remaining general problem, both-squares-nonnormal outside covered classes, T2/T3/Z2/original, global equality, novelty | **INCONCLUSIVE** | The proven classes include some pairs with both squares nonnormal, but no general conclusion for that complement or the full target follows. No novelty assessment. |

The single minor is the cross-reference only, not an assertion that the supported-site lemma proves the distinct 4×2 estimate. No other F, M, or m is identified in the frozen mathematical claims.

## Reconstruction

Throughout, `||.||` without a subscript denotes the Frobenius/Hilbert–Schmidt norm when applied to a matrix; `||.||op` is the operator norm. Inner products are conjugate-linear in the first argument. For d=4 and traceless A,B, the cross trace in X†X vanishes, so `||X||²=4(||A||²+||B||²)`. The f168-adopted odd-sector Ky-Fan dual consequently asks for `σ1(X)²+σ2(X)²≤2(||A||²+||B||²)`. The f168 one-site ladder and f196 normal-matrix/one-supported-site scope are imports only as expressly adopted there.

### 1. Weighted partial permutations, and cyclic grade blocks

Let `A e_p=a_p e_{σ(p)}` and `B e_q=b_q e_{τ(q)}`, with zero weight at every fixed point. Any finite partial row/column matching can be completed to permutations by assigning the unused weights zero. For an input vector w, Cauchy–Schwarz at output `(i,j)` gives

```
|(Xw)ij|² ≤ (|a_{σ⁻¹i}|²+|b_{τ⁻¹j}|²)
             (|w_{σ⁻¹i,j}|²+|w_{i,τ⁻¹j}|²).
```

Reindexing the two sums, the coefficient of `|w_pq|²` is exactly `|a_p|²+|a_{σ⁻¹p}|²+|b_q|²+|b_{τ⁻¹q}|²`. Hence `||X||op²≤m_A+m_B`. The two a-indices are distinct unless p is fixed; in the fixed case the repeated weight is zero. Thus `m_A≤||A||²`, and similarly for B. This works for arbitrary complex weights, unequal local dimensions and permutation cycle structures. Independent local unitary similarities conjugate X unitarily and preserve all norms. At d=4, each of the top two squared singular values is at most `m_A+m_B`, so the claimed dual gap is at least `2[(||A||²−m_A)+(||B||²−m_B)]`; it is strictly positive if either term is positive.

For the cyclic subclass `S(a)e_i=a_i e_{i−1}` on `Z/dZ`, d≥3, grade the input by `k=i+j`. X sends the grade subspace H_k into H_{k−1}; the input and output grade decompositions are orthogonal. In corresponding bases, block X_k has entries `a_i` in row `i−1`, column i, and `b_{k−i}` in row i, column i. These locations are distinct and every weight occurs once, so

```
||X_k||² = L := ||S(a)||²+||S(b)||²,
||X||op² = max_k ||X_k||op² ≤ L.
```

This is the requested independent grade-block proof of the cyclic operator estimate. It implies the top-two bound for every d≥3, independently of the general partial-permutation proof.

For the iff equality, each column has at most the two allowed rows i and i−1; for d≥3 two different columns have at most one allowed row in common. Thus the support graph has no four-cycle. A rank-one matrix has Cartesian-product support: if it has nonzeros in at least two rows and two columns it contains a full nonzero 2×2 rectangle, which is impossible here. Its support must therefore lie in one row or one column, each of which has at most two allowed entries. Two nonzero weights from the same shift occupy distinct rows and columns in every block; three total nonzero weights also cannot fit in one row or column. In either case every block has rank at least two, hence `||X_k||op²<||X_k||²=L` and the top-two gap is strict.

If each shift has at most one nonzero weight, equality holds: for one `a_i` and one `b_j`, the entries share a column in grade `i+j` and a row in grade `i+j−1`, distinct modulo d. Those two blocks are rank one with squared singular value L, so the top two sum to 2L. With exactly one weight, every one of the d blocks has rank one and squared singular value L; with no weights both sides vanish. This proves the complete equality characterization, including complex phases and zero factors. For d=2 the graph can contain a rectangle: both shifts with weights (1,1) have two rank-one grade blocks of squared singular value 4, so equality occurs despite two weights per shift. Thus d=2 cannot be silently added to the iff statement.

The claimed genuinely nonnormal examples also exist. For `0<ε<1`, let A=B be the four-cycle shift with weights respectively `(1,ε,0,0)`, `(1,ε,ε²,0)`, or `(1,ε,ε²,ε³)`. These have ranks 2,3,4. Their squares are nonnormal: for rank 2 and 3 they are nonzero nilpotents; for rank 4 the 1↔3 two-cycle of A² has unequal opposite weights ε and ε⁵. As ε tends to zero they approach a rank-one shift. The tail test has left side tending to 0 and required right side tending to 2, while the variance test tends to `28≤18`, which fails. Thus both tests fail for sufficiently small ε; exact ε=1/4 instances are in the controls. These examples are covered by the weighted-permutation theorem, not an assertion about the whole both-squares-nonnormal region.

### 2. Trace-zero rank-one residual and its gap

Let `t=||u||²`, `q=||v||²=1−t`, `D=I−uu†−vv†`, and `d_A=Tr(A†AD)`. Since `uu†+vv†` is positive with trace 1, D is positive and `d_A≥0`. If u,v are independent, D is positive definite. Set `z=u†v`, `r=|z|²`, `Δ=tq−r>0`.

In the positive weighted inner product `<M,N>_D=Tr(M†ND)`, the functional `A↦v†Au` is represented by `R=v u†D⁻¹`, and `A↦Tr A` by `D⁻¹`. Project R orthogonally off the trace functional and apply Cauchy–Schwarz. For trace-zero A this gives

```
|v†Au|² ≤ N d_A,
N = q (u†D⁻¹u) − |v†D⁻¹u|² / Tr(D⁻¹).
```

For U=[u v], its Gram matrix G=U†U has trace 1 and determinant Δ. On span(U), `(I−G)⁻¹=G/Δ`, so `U†D⁻¹U=G²/Δ` and

```
u†D⁻¹u=(t²+r)/Δ,   |v†D⁻¹u|²=r/Δ²,   Tr(D⁻¹)=2+1/Δ.
```

Substitution yields

```
(1+t)−N = (1+2tq−4r)/(1+2Δ)
          = (1−2tq+4Δ)/(1+2Δ) ≥ 1−2tq.
```

The last comparison has difference `2Δ(1+2tq)/(1+2Δ)≥0`. Therefore `N≤t(1+2q)≤t+1/2`, since `tq≤1/4`. Dependent nonzero u,v follow by a normalized independent approximation and continuity; if either vector is zero the left side vanishes. This proves the displayed lemma for **all** complex traceless A and normalized pairs.

Write `a=||A||²`, `s=||A||op²`, `k=v†Au`. Since `||Au||²+||Av||²=a−d_A`, the preceding estimate gives

```
2a − [||Au||²+||Av||²+|k|²/(1+t)+s]
  ≥ (a−s) + (1−2tq)d_A/(1+t) ≥ 0.
```

This is the all-variable (†) inequality and the claimed explicit gap; `a−s≥0` and `1−2tq≥1/2`.

For the rank-one-B conclusion, a nonzero traceless rank-one B is unitarily similar to `βE01`: its normalized range and co-range are orthogonal because its trace is zero. On the B-support X is `Γβ=[[A,βI],[0,A]]`, and the complementary space supplies two A blocks. By the supported-site lemma, two maximizing right singular vectors within Γβ are safe; two in the A blocks contribute at most `2s≤2(a+|β|²)`. For one from Γβ and one from an A block, with unit `(u,v)`,

```
2(a+|β|²) − [||Au+βv||²+||Av||²+s]
 = (a−s)+d_A−|k|²/(1+t)+(1+t)|β−k/(1+t)|²
 ≥ (a−s)+(1−2tq)d_A/(1+t)+(1+t)|β−k/(1+t)|² ≥ 0.
```

The cross term uses `k=v†Au`; complex phases are included. A top-two singular basis can be chosen blockwise even under ties, so these are all cases. B=0 is immediate. Conversely, if the dual bound holds for every traceless rank-one B, test it on any unit vector in Γβ and a top right singular vector of an A block; optimizing over complex β gives (†), with the β=0 optimum obtained by continuity if needed. Thus the f196 fixed-A equivalence is also reconstructed, not assumed from an author receipt.

### 3. Restricted 4×2 inequality and the one-supported-site lemma

For arbitrary unit ψ,φ in C⁴⊗C² define `c=φ†ψ`, `M=Tr₂|ψ><φ|`, `N=Tr₁|ψ><φ|`, `M0=M−cI4/4`, `N0=N−cI2/2`. Both traces are c. If **both** `Tr A=0` and `Tr T=0`, then

```
φ†(A⊗I₂+I₄⊗T)ψ = Tr(AM0)+Tr(TN0),
|...|² ≤ (||A||²+2||T||²)(||M0||²+||N0||²/2).
```

Let `s1=||N||²`, `s2=||M||²`. These are the overlaps of the corresponding one-site density reductions, hence each is at most 1. The local swaps F1,F2 commute and `(I−F1)(I−F2)` is positive; its expectation in ψ⊗φ is `1−s1−s2+|c|²`. Thus

```
||M0||²+||N0||²/2
 = s2/2 + (s1+s2−|c|²)/2 ≤ 1.
```

Supremizing over unit ψ,φ proves `||A⊗I₂+I₄⊗T||op²≤||A||²+2||T||²`. This is a complete reconstruction under the restricted hypotheses; the prior lack of admission is not silently converted into parent acceptance.

Both trace hypotheses matter for this proof and for the statement. For example, independently take `A=diag(3/4,−1/4,−1/4,−1/4)` and `T=diag(1/2,0)`. Then Tr A=0 but Tr T=1/2, the right side is 5/4, and the squared norm is 25/16. The omitted scalar is `c Tr T/2`. Conversely, `A=diag(1,0,0,0)`, `T=diag(1/4,−1/4)` violates the same bound if only Tr T=0 is imposed. These are intended-reason negatives, not evidence for any unrestricted lemma.

For Lemma 6.1, the f168 adopted ladder already gives q2(C)≥0 whenever rank C≤2 and a chosen leg at one site is supported on a 2-plane. To see the normalization, take `C=XP_F`, where F is a two-plane with its site-2 input leg contained in E. The compressed local factor has the positive product decomposition

```
I⊗P̄_E − |Ω_E><Ω_E|/2
 = 3∫ |u⊥><u⊥|⊗|ū><ū| dμ(u) + (I−P_E)⊗P̄_E.
```

Indeed on E⊗E, the elementary second moment is `∫P_u⊗P̄_u=(I+|Ω_E><Ω_E|)/6`; replacing `P_u` by `I−P_u` proves the first term. Each product contraction leaves a one-site Z of rank≤2, so `q1(Z)=||Z||²−|Tr Z|²/2≥0`. Equivalently one may use the adopted f168 result directly. The odd-sector reflection gives `q2(C)=||C||²−2||Podd C||²≥0`; X is in the odd sector and `<X,C>=||C||²`. Hence `||C||⁴≤||X||²||Podd C||²≤||X||²||C||²/2`, yielding `||XP_F||²≤||X||²/2`, with the zero case trivial. This proves Lemma 6.1, not the differently numbered §5 claim.

### 4. Square-normal structural classification and dependence

Suppose B is traceless and B² is normal. B commutes with B², so its spectral subspaces are B-invariant and, being mutually orthogonal and collectively spanning, reduce B. On the zero eigenspace B²=0; relative to `ker B⊕(ker B)⊥`, B has the form `[[0,C],[0,0]]`, and an SVD of C produces traceless nilpotent 2×2 blocks and scalar zeros.

On an eigenspace of B² with λ≠0, choose μ²=λ. The polynomial `(x−μ)(x+μ)` has distinct roots, so B is diagonalizable there. In `ker(B−μI)⊕ker(B−μI)⊥`, its upper triangular form has diagonal blocks μI and −μI: the latter follows from diagonalizability and the fact that all μ-eigenvectors already lie in the first subspace. An SVD of its off-diagonal block yields traceless 2×2 blocks `[[μ,c],[0,−μ]]` and scalar leftovers ±μ. If a nonnormal 2×2 block occurs in dimension four, the remaining dimension is either another 2×2 block or two scalars. Every 2×2 block has trace zero; global Tr B=0 forces the two remaining scalars to sum to zero, so together they form a second traceless 2×2 block. If no nonnormal block occurs, B is normal. Conversely a normal B has normal square, and a traceless 2×2 block squares to a scalar by Cayley–Hamilton; hence the classification is an iff.

If B is normal, diagonalize it and choose the top two right singular vectors of X within its one-dimensional B-eigenspace blocks, even in ties. Their B-leg support has dimension at most two, and Lemma 6.1 applies; this also lies in the expressly adopted f196 normal class. If B is nonnormal with `B=B1⊕B2` and `Tr B1=Tr B2=0`, write `Γj=A⊗I₂+I₄⊗Bj`. Two top singular vectors from one Γj are safe by Lemma 6.1. If one comes from each block, the **restricted** §5 estimate gives

```
σ1(Γ1)²+σ1(Γ2)²
 ≤ (||A||²+2||B1||²)+(||A||²+2||B2||²)
 = 2(||A||²+||B||²).
```

The traceless restriction therefore **suffices exactly**: Tr A=0 is an ambient hypothesis and each Bj is separately traceless by the dimension-four structural argument. The proof as written does depend on this restricted lemma in the nonnormal split case; it does not require the false arbitrary-T assertion. Exchanging sites proves the A²-normal case. This establishes only the stated subclass at the present same-harness assurance level.

### 5. Tail and variance tests

Put `x=||A||op`, `y=||B||op`, `sA=||A||²−x²`, `sB=||B||²−y²`. The operator triangle inequality gives `σ1²+σ2²≤2(x+y)²`. Hence `sA+sB≥2xy` is sufficient for the dual bound; if strict, the lower bound on the gap `2(sA+sB−2xy)` is strictly positive.

For the second test, put `a=||A||²`, `b=||B||²`, `p=Tr[(A†A)²]`, `q=Tr[(B†B)²]`, `z=Re(overline{Tr A²} Tr B²)`. Expanding `H=X†X` and using Tr A=Tr B=0 removes all terms containing a single A or B, giving

```
Tr H = 4(a+b),
Tr H² = 4(p+q)+4ab+2z.
```

Its 16 nonnegative eigenvalues have mean `(a+b)/4` and centered square sum `V=4(p+q)+4ab+2z−(a+b)²`. The centered indicator of the top two positions has squared norm `2(7/8)²+14(1/8)²=7/4`. Thus Cauchy–Schwarz implies

```
λ1+λ2 ≤ (a+b)/2 + sqrt((7/4)V).
```

The right side is at most `2(a+b)` exactly under the sufficient condition `14(p+q)+7z≤8(a²+b²)+2ab`. If the displayed condition is strict and X is nonzero, the resulting dual inequality is strict. The argument establishes sufficiency and strictness only, not necessity; the weighted-shift examples above show both tests can fail in a covered class.

## Reviewer-owned exact controls and receipts

All controls below are reviewer-written, use only Python standard-library rational arithmetic (including explicitly implemented Gaussian rationals in the second script), and live in this wave directory. No author script was run, imported, or compiled. The exact finite controls are counterexample/consistency checks, not proofs of the universal claims; the written derivations above carry those claims. Both invocations had a 120-second cap; neither hit it.

1. `reviewer-f215-controls-v1.py`, SHA-256 `4cbb59e686e93e57267e7fb0365140e8e17639d90baa634715d066005089b944`. Native `/bin/date` start and end were both `2026-10-29T13:29:51-0700 PDT`, at one-second clock resolution; process exit **0**. It reported **39 positive and 7 intended-reason negative controls**. Examples: unequal-size rowwise bound `599/9 ≤ 281/3` with `m_A=5,m_B=4`; d=3,4,5 grades and exact ranks; the two restricted 4×2 block PSD certificates with bounds 11 and 19; direct centered partial-trace coefficients 1 and 53/81; moment trace `128=4(p+q)+4ab+2z`; and the three ε=1/4 rank 2/3/4 nonnormal-square examples. The negative controls actually exhibit, rather than merely seek, failure when incoming weights are omitted (4>2), when the d≥3 equality classification is extended to d=2, when trace zero is removed from §4, when either A or T trace hypothesis is removed from §5 (including 25/16>5/4), when the unrestricted 4×2 slack is asserted PSD, and when the z term is omitted from the fourth moment (128≠96).
2. `reviewer-f215-complex-controls-v1.py`, SHA-256 `44ecc911f7e89cdb26a644f575954e59fff3666e54b6967a86ed08f1bee35717`. Native `/bin/date` start and end were both `2026-10-29T13:31:11-0700 PDT`, at one-second resolution; process exit **0**. It reported **3 positive and 1 intended-reason negative controls**. Complex weights `1+i` and `2−i` give grade ranks `[1,1,2,2]` and norm squared 7 in every grade; a genuinely complex normalized pair has `z=−36i/125`, `k=48i/125`, and satisfies the lemma and mixed square completion. The negative replacing k with its conjugate makes the purported lower bound `2294613/2125000` exceed the actual mixed gap `2253/5000`, catching the phase error for that fixture.

## Imports, remaining gap, and deviations

The f168 disposition's odd-sector dual, one-site ladder and qualified support scope, and the f196 disposition's expressly adopted safe-class context and fixed-A rank-one reduction, are the only prior mathematical imports. The Böttcher–Wenzel conditional import in f196, other linked bodies, the erratum's status-only reviewer summary, author scripts/receipts, held material, external sources, solver results, sibling reviews, and model/API calls were not used as evidence. Standard finite-dimensional linear algebra, the elementary Haar second moment displayed above, and independently constructed exact controls were used directly.

The square-normal and rank-one-B conclusions do not settle arbitrary nonnormal A,B. In particular, examples with both squares nonnormal are covered by §2, but the general both-squares-nonnormal complement and general T2 remain open in this review; T3, Z2, the original target, a general equality classification, and novelty likewise remain unestablished. A reviewer-written proof of the restricted 4×2 lemma is not a parent disposition or a license to use the false arbitrary-T variant.

**Contract deviations:** none identified. The initial manifest-line truncation and subsequent complete raw reads are disclosed in the sequence above; all input identities were measured before any input body, the mandatory erratum was read first, and all four bodies were completely displayed before reconstruction and controls.

**Assurance:** this is a same-harness review, not human, independent-model-family, formal/kernel, or novelty verification.
