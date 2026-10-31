# Exact physical complex mixed-filter finite author candidate

**Status: AUTHOR CANDIDATE; verifier UNRUN.** This is a proposed written derivation and a new, stand-alone exact finite verifier, not an observed verifier result, independent review, family/human/formal acceptance, literature-priority claim, or global PPT44 theorem. The parent must read the entire source and this narrative, then separately issue a one-shot GO before any execution. The source's own cooperative limit is 40 seconds and the parent's external limit must be at most 55 seconds. An internal timeout, a failed invariant, or a wrong/accepted mutant is a nonzero terminal failure. No scientific code was run by this author.

## 1. Objects, quantifiers, and import boundary

Write `[v]=vv†`, `ij=|i>_A|j>_B`, and use zero-based indices. For real `s,r>1` with `(s−1)(r−1)>=4`, let the actual 20×20 positive operator be

```
Q = [00+11+22]+[01+12]+[10−21]
    +s([02+34]+[32]+[04])
    +r([20+33]+[23]+[30]).
```

For all finite complex `alpha,beta,gamma`, let `w=(alpha,beta,gamma,0)^T`, `K=[I4 | w]`, `R=(I4⊗K)Q(I4⊗K)†`, and `n=|alpha|²+|beta|²+|gamma|²`. The coefficient in a ket is *not* conjugated by applying `K`. This candidate's explicit character construction additionally assumes `beta != 0`. Define

```
A=00+11+22, B=01+12, D=10−21,
F=02+3w, H=0w, G=32, P=30, J=20+33.
R=[A]+[B]+[D]+s([F]+[H]+[G])+r([P]+[J]+[23]).
```

The finite fixtures below all satisfy the actual admissibility condition, `beta gamma != 0`, and `|beta|²/s+|gamma|²/(s−1)>1`; they are outside the displayed ellipsoid and both displayed coordinate lines. The six-character and range identities below are algebraic statements for the displayed objects, not a claim that the displayed sufficient condition exhausts all filters. The assertion that the parent `Q` has Schmidt number 3 depends on the prior original-source/range proof linked inside S2; that linked proof is not in this packet and was not opened. Therefore any SN3-to-SN2 *transition* remains a named conditional import. The physical filtered-state conclusions below do not require that import.

## 2. Actual character vectors and all 3×3 minors

Let `kappa=r/(r+s)`, `eta=s/(r+s)` and `C=(F,H,G,P)` be the 16×4 matrix of actual columns. For `beta != 0`, define

```
t1=(-gamma,1,gamma²,alpha gamma)^T/beta,
t2=(0,0,gamma,kappa alpha)^T,
t3=alpha(1,0,−gamma,−alpha)^T/beta,
t4=(0,0,−eta alpha,0)^T,
Xj=C tj.
```

Direct cancellation in the actual filtered kets gives `X1=(alpha/beta)00+01−gamma31` and `X3=(alpha/beta)02+alpha31`. For every sixth root `z`, put

```
Vz=A+zD+z^−1 X1+z^−2 X2+z^−3 X3+z^−4 X4.
```

The four rows of its 4×4 coefficient matrix are

```
(1+(alpha/beta)z^−1, z^−1, (alpha/beta)z^−3, 0)
(z,                    1,    0,                    0)
(0,                   −z,    1,                    0)
(kappa alpha z^−2, alpha z^−3−gamma z^−1,
 gamma z^−2−eta alpha z^−4, 0).
```

The first row is `(z^−1+(alpha/beta)z^−2)` times the second plus `(alpha/beta)z^−3` times the third. The fourth is `kappa alpha z^−3` times the second plus `(gamma z^−2−eta alpha z^−4)` times the third; use `kappa+eta=1`. The second and third rows are independent, so every `Vz` has rank exactly 2, including `z=1`. In particular *all* 16 choices of 3 rows and 3 columns have zero determinant. The six exponents `(0,1,−1,−2,−3,−4)` are pairwise distinct modulo six, so exact character orthogonality yields

```
(1/6) Σ_(z^6=1) [Vz] = [A]+[D]+Σ_(j=1)^4 [Xj].   (I)
```

The unrun source is designed to check every one of the 16 symbolic minors in the ring `Q(i)[z]/(z^6−1)` for each fixture, and independently all 16 minors at each of the six roots in the exact field `Q(i)[zeta]/(zeta²−zeta+1)`. In that field `zeta^6=1` and conjugation sends both `i` to `−i` and `zeta` to `1−zeta`; it explicitly forms the six actual outer products and checks (I) entry by entry. No floating root or tolerance occurs.

## 3. Residual, scalar criterion, and exact positive decomposition

Put

```
Lambda=diag(s,s,s,r),   M=Lambda−Σ_j tj tj†,
a=|alpha|², x=|gamma|², y=|beta|²,
q=x/s+a/(r+s)+{[1+x+x²+a(1+x)]/s+a(x+a)/r}/y.
```

The outer products in `M` require Hermitian conjugation, even for complex inputs. By the actual filtered `Q` and (I),

```
R=(1/6)Σ_(z^6=1)[Vz]+[B]+r[J]+r[23]+C M C†.       (II)
```

For every admissible `s,r`, every finite complex filter with `beta != 0`, and `M>=0`, this is a finite positive decomposition into Schmidt-rank-at-most-2 kets: all columns of `C` have Alice support only on rows 0 and 3, and `B,J,23` have respective ranks 2, 2, 1. A zero-pivot-capable exact positive rank-one elimination gives `M=Σ_l (1/d_l)[u_l]` with `d_l>0` (skip a zero diagonal only when its remaining row/column is zero). Then `C M C†=Σ_l (1/d_l)[C u_l]`. This also covers singular `M` and needs no numerical square root. The source intends to construct this factorization and compare the resulting actual 16×16 positive residual to `C M C†` entry by entry whenever all 15 principal minors are nonnegative.

To see the advertised scalar criterion, set `W=Lambda^−1/2(t1 t2 t3 t4)`. Explicitly

```
tr(W W†)=Σ_j tj† Lambda^−1 tj=q,
kappa²/r+eta²/s=1/(r+s).
```

For every vector `v`, Cauchy–Schwarz gives `v†Mv >= (1−q)v†Lambda v`. Thus `q<=1` is sufficient for `M>=0`, including equality; it is not asserted necessary. Equivalently, the code tests the actual Hermitian `M` by *all* 15 nonempty principal minors, not merely leading minors. A negative `M` minor only invalidates this residual certificate; it does **not** prove SN3, non-PPT, or impossibility of another decomposition.

## 4. Physical partial transpose, traces, and actual range

`Q` is positive by its displayed sum. Direct Bob partial transpose yields scalar blocks `1,1,s,r`, all-ones 2×2 blocks with coefficients `1,1,s,r`, five zeros, and the block

```
N = [[1,1,−1],[1,s,1],[−1,1,r]].
```

The Schur complement of its upper-left entry is `[[s−1,2],[2,r−1]]`, PSD under the stated admissibility condition. Hence `Q^Gamma_B>=0`. The *physical complex* filter identity is

```
R^Gamma_B=(I⊗conjugate(K)) Q^Gamma_B (I⊗conjugate(K))†,
```

not the same congruence with unconjugated `K`. Let `T=tr Q=7+4(s+r)` and `Z=tr R=7+2s(1+n)+4r`. Since `K K†=I+ww†` has largest eigenvalue `1+n`, the actual contraction is `K/sqrt(1+n)` and, on normalized input `Q/T`, `rho=R/Z` succeeds with probability `Z/((1+n)T)`. The numerator and denominator are positive and `(1+n)T−Z=2s+(7+2s+4r)n>0`. Thus `rho` is well-defined and PPT. The source separately constructs and compares the actual 20×20 `Q`, 16×16 `R`, partial transposes, traces, marginals and conjugated-filter congruence; it also checks exact positive elimination on `Q^Gamma_B` and `R^Gamma_B`.

Because all nine weights in the actual output sum are strictly positive, `range(R)` is exactly the span of its nine displayed kets. In coefficient-matrix form each vector in the range is, for complex `a0,b,c,d,e,f,g,h,k`,

```
(a0+alpha h, b+beta h, c+gamma h, 0)
(d,          a0,       b,         0)
(e,         −d,        a0,        k)
(f+alpha c,  beta c,   g+gamma c, e).
```

The minors using `(rows 1,2; cols 1,2)`, `(rows 1,2; cols 0,2)`, and `(rows 1,3; cols 1,3)` are `m1=a0²+bd`, `m2=a0d−be`, `m3=a0e`, and the formal identity

```
a0² m1 − a0 b m2 − b² m3 = a0^4
```

holds over the complex polynomial ring. All three minors vanish for a product vector, forcing `a0=0`; thus every product vector in the range has zero `11` coefficient. On the other hand `R_(11,11)=1`. Every vector in any positive separable decomposition lies in `range(R)`, so `R` is entangled. Consequently, on `M>=0`, the positive decomposition above proves exact Schmidt number 2. The source intends both to check the formal polynomial identity from the displayed range matrix and to compare the rank of the actual `R` with that of the nine actual ket columns. The product ket `H=0w` with `alpha != 0` demonstrates why replacing the zero `11` coordinate by zero `00` is wrong.

## 5. Finite fixture specifications and analytically derived classifications

All entries below are exact Gaussian rationals, all `s,r` are rational and admissible, and `i²=−1`. These are author-derived expected values, **not executed source results**. `E` is the ellipsoid left side `y/s+x/(s−1)` and `p` is the physical success probability.

| label | `(s,r)` | `(alpha,beta,gamma)` | `q` | `E` | `M` | `p` |
|---|---|---|---|---|---|---|
| equal-complex | `(3,3)` | `(i,3,i)` | `41/54` | `7/2` | positive definite | `91/372` |
| unequal-complex | `(2,5)` | `(i,4+i,i)` | `484/595` | `19/2` | positive definite | `107/700` |
| q-boundary | `(5/2,4)` | `(0,1+i,i)` | `1` | `22/15` | positive definite | `43/132` |
| M-boundary-q-outside | `(2,5)` | `(0,1+i,i)` | `5/4` | `2` | PSD singular | `43/140` |
| M-nonPSD-q-outside | `(2,5)` | `(0,i,i)` | `2` | `3/2` | not PSD | `13/35` |

For the first two, `q<1` makes `M` positive definite by the bound in §3. For `q-boundary`, `q=1` and `W` has at least two independent nonzero columns (the first has a nonzero H coordinate whereas the second has only a nonzero G coordinate); a PSD `W†W` of trace 1 and rank at least 2 has largest eigenvalue strictly below 1, so `M` is positive definite. For the last two, `alpha=0`, `gamma=i`, `s=2`, `r=5`; subtracting `t2t2†` first gives `D0=diag(2,2,1,5)` and `M=D0−t1t1†` with `t1=(-i,1,-1,0)^T/beta`. For `beta=1+i`, `t1†D0^−1t1=1`, so `M` is PSD singular and `det M=0`; for `beta=i`, the same quantity is 2, so `det M=det(D0)(1−2)=−20` and `M` is not PSD. The equality `(s−1)(r−1)=4` is present in the first, second, fourth and fifth rows; the third source is strictly inside the PPT source region. The fourth row witnesses why failure of `q<=1` alone does not imply failure of `M>=0`.

## 6. Source, intended controls, and unobserved execution

New source: `finite-ppt44-mixed-exact-v1.py`, 22,759 bytes, 643 LF; SHA-256 `1be5ad786ffde98241a686572ef38179eb7ee4293602bb86641515bbe7b55df7`, supplied by Main as an administrative metadata-only pin. I did not execute, import, compile, test, lint, or independently hash it. The pin is not an execution GO or correctness judgment.

The source uses only the Python standard library, exact Gaussian rationals and the exact cyclotomic field/ring above; it makes no data-file writes, network calls, subprocesses, floats, random choices or tolerance comparisons. It is designed to emit per-case exact summaries and one terminal `STATUS: PASS` only after all checks, otherwise terminal `STATUS: FAIL` and nonzero exit. Its named, intended-reason rejection controls are: wrong partial-transpose filter conjugation; transpose in place of Hermitian conjugation for `M`; a coefficient change producing a nonzero rank-3 minor; repeated Fourier character and its surviving cross term; the wrong `q` denominator in an unequal-`s,r` complex case; an incorrect sign in the formal range identity; and the false zero-`00` range obstruction. Each requires the precise named failure, not an arbitrary exception. These checks and their performance remain **unobserved** until parent-authorized execution; 40 seconds is an enforced cooperative limit, not a claim that the work has completed in that time.

## 7. Complete read and process declaration

Before any mathematical-body read or reasoning, I read the complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual dispatch receipt and all 22 manifest-listed controls. Initial automatically elided administrative displays were recovered with complete raw reads. Controls were used only for status and permissions. I exclusively created `prebody-ack-v1.md` and sent Main a direct prebody acknowledgment before opening the packet.

The sole literal part, `literal-packet-part-01-v1.md`, was read in order with raw windows LF `1–20`, `21–40`, `41–60`, `61–80`, `81–100`, `101–120`, `121–140`, `141–160`, `161–180`, `181–200`, `201–220`, `221–240`, `241–250`, including both source endings. The complete part is 25,182 bytes, so every display was below 30,000 bytes. No body clipping occurred. It contains complete S1 logical lines 1–191 and S2 logical lines 1–49. Parent-supplied part SHA-256 is `113313a395f04d445919344cebf5da0ef74e7005bef656445a5bcd1d514f6101`; S1 is `c5843b30d17031648d961d78c3da96f5c8fbf4509cdc7b8ca58bf9b97db4d352`; S2 is `3f15a273f2c1d64aa1b54ff296c24133fb4c0b7245ec456e484f765f164eccf3`. These packet pins were supplied by the parent, not independently recomputed here. No packet link or unlisted mathematical source was opened.

All genuine held episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers are NONINPUT. Memory and procedural skills were read as instructions, not mathematical premises. No scientific execution, solver, external model, network, child subprocess, build, test, compilation, code import, scientific eval or old-code read was used. No process deviation is known beyond the recovered, initially elided administrative displays; no clean-cognition certificate is asserted. The source and this candidate remain subject to parent full read, independent GO, observed execution and separate disposition; no family, human, formal/kernel, novelty, publication, all-filter, arbitrary-fourth-component, or global PPT44 acceptance is claimed.
