# info-6 frontier: rank-six phase obstruction at peak/unit weight 212

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T19:39:59-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**, depending on the explicitly pinned preceding written results. No global no-go, Boolean witness, novelty or formal-verification claim is made.

## Statement and consequence

For any actual balanced f:F₂⁹→{0,1} with full Walsh peak≤28, use the even-half polar B, odd-half quadratic Q, `P=1_{|W|∈{4,28}}`, and scaled signed counts A_t from the preceding rank-six results. If

    rank(B)=6,       wt(P)=212,       wt(Q)=112,

then

    A₃+A₋₅ = #{P=0,Q=1} ≥ 16.                                              (1)

This excludes the entire formal histogram in `frontier-20261028-four-zero-post-simplex-result.json`, SHA-256 `4a3b0d9c0f4bbc8e48d030ea9936a24e202bcfd3a3f7244dab9d39d01d9c95ae`, 287 LF: its Z=4, Z+F=112 forces rank six, and it has wt(P)=212, wt(Q)=112, but A₃+A₋₅=12. The exclusion is independent of how that histogram is placed. It does **not** exclude other four-zero histograms or settle the original problem.

## Reduction to two affine-flat exchanges

Put h=1+P, so wt(h)=44. The forced quartic form and radical slicing from `frontier-20261028-rank-bound-sharpening-v1.md`, SHA-256 `f741e11a0cc0a73e8c094f6c2c74a09f3f902db58100e3dc9e76bf059c109aab`, 60 LF, apply: four six-variable slice weights are even and at least eight; two slices differ by a quadratic; their mixed radical derivative is affine; weight-eight slices are identical and cannot coexist with weight ten or twelve; weight-ten slices are identical to each other.

The sorted partitions of 44 remaining after these restrictions are

    (8,8,8,20), (8,8,14,14), (10,10,10,14), (10,10,12,12).

In the first and third patterns the three small slices coincide. Their difference from the fourth is the mixed radical derivative, supported on at most 28 or 24 points, respectively. A nonzero affine Boolean function on six variables has weight 32 or 64, so that derivative vanishes and the fourth slice would coincide too, a contradiction.

In either remaining pattern, the two smaller slices are one support S. The mixed derivative is the difference of the other two slices, supported on at most 28 or 24 points, hence vanishes; their common support is T. The nonzero quadratic `1_S+1_T` has weight at most 22 and therefore weight 16, the indicator of an affine 4-flat H. Thus `T=S△H`, and either

- `|S|=8`, `|T|=14`, `|S∩H|=5`; S is a symplectic simplex; or
- `|S|=10`, `|T|=12`, `|S∩H|=7`; S has the rank-six quartic moment matrix from the pinned predecessor.

Since Q has rank-six polar and weight 112 on the eight-dimensional half, it is independent of the two radical coordinates and has weight 28 on the six-dimensional quotient. Consequently

    A₃+A₋₅ = 2(t_S+t_T),    t_S=|S∩{Q=1}|,    t_T=|T∩{Q=1}|.               (2)

Both t_S and t_T are odd: the parity of each support's product with Q is the full-degree coefficient of its Boolean indicator times Q, and the three complementary quartic–quadratic symplectic pairings contribute 1+1+1=1.

## The simplex exchange

For |S|=8, the exact phase classification in `frontier-20261028-rank6-simplex-phase-v1.md`, SHA-256 `8aaa61f80a25cf0a2fae3b5b8d908e1a088b0bab107a5b814aa7eeadcf8d1054`, 48 LF, gives `t_S∈{3,7}` when Q has quotient weight 28. Also t_T is odd because T has the same forced quartic form, so its dot product with Q has parity one.

Any five simplex points affinely span H, and the four difference directions have all-one-off-diagonal alternating Gram matrix, hence H is nondegenerate. Thus the restriction Q|H has weight 6 or 10. If `t_S+t_T<8`, then t_S=3 and t_T is 1 or 3. Write `j=|S∩H∩{Q=1}|`; since `T=S△H`, `t_T=t_S+wt(Q|H)−2j`. The case t_T=1 requires j≥4, impossible. For t_T=3 it would require `wt(Q|H)=6` and j=3. But for a five-point affine symplectic simplex, a quadratic taking value one at exactly three of its five points has weight **10**, not 6, on its 4-flat. Contradiction.

For this last elementary phase fact, take one of the five points as p and the other differences v₁,…,v₄; their Gram has off-diagonal entries one. Expanding the quadratic Gauss sum over subsets of these four basis vectors gives

    G_H=(−1)^{Q(p)} Re[(1−i) Π_{j=1}⁴(1+i(−1)^{Q(p+v_j)+Q(p)})].

If exactly three of the five values are one, direct evaluation gives G_H=−4, hence weight `(16−G_H)/2=10`.

## The ten-point exchange

For |S|=10, the rank-six quartic moment matrix M and ⊕S=0 are established in the pinned predecessor. H contains seven points of S. Translate H to a linear 4-space U; M is translation-invariant because |S| is even and ⊕S=0. The three outside points have distinct nonzero images in the two-dimensional quotient V/U, since their sum is zero there. Their three outer products sum to the nondegenerate alternating 2×2 form. Thus the restriction of M to the annihilator of U is nondegenerate, and U itself is a nondegenerate symplectic 4-space. In particular `wt(Q|U)∈{6,10}`.

Let `t_out=|S\U∩{Q=1}|`. Since T=S△U,

    t_S+t_T = wt(Q|U)+2t_out.                                               (3)

If the left side were below eight, (3) forces `wt(Q|U)=6` and t_out=0. Write the symplectic orthogonal direct sum as V=U⊕R, dim R=2. The three outside points project to the three nonzero elements of R. In a symplectic basis adapted to U⊕R, M is block diagonal; its zero cross block forces all three outside points to have the **same** U component u. Indeed, if the R components are r₁,r₂,r₁+r₂, the cross block is `(u₁+u₃)r₁ᵀ+(u₂+u₃)r₂ᵀ`, so u₁=u₂=u₃=u.

Define the normalized quadratic `Q_R(r)=Q(r)+Q(0)`. For u∈U, r∈R, polarization gives `Q(u+r)=Q(u)+Q_R(r)`. All three outside points have Q=0, so Q_R is constant Q(u) on the three nonzero r. It cannot be zero there because its rank-two polar is nondegenerate; therefore Q(u)=1 and Q_R has weight three. Its Gauss sum is −2. Meanwhile Q|U has weight six and Gauss sum +4, so the product formula on U⊕R gives the quotient Gauss sum −8, i.e. quotient Q has weight 36—not the required 28. Contradiction.

Both exchange types have `t_S+t_T≥8`; equation (2) proves (1). ∎

## Finite controls and pins

The separate finite checker tests the simplex argument on all 56 affine 4-flats meeting an explicit simplex in five points and all affine shifts of a rank-six quadratic, verifies the five-point phase rule, and checks the three 7-point flats of an explicit rank-six weight-ten slice. In both example types the minimum `t_S+t_T` for quotient Q weight 28 is eight. These are finite controls, not a substitute for the all-variable proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-rank6-boundary44-check.py` | `396850f9634c1fe48356d6d4ff548414985a46fdec7e4a12b0539cd11b3ac3ce` | 49 |
| `frontier-20261028-rank6-boundary44-check-result.json` | `d6a3343e62d9d6f614724f62795ef653d96483ae0523aef64ebafc0be6c1fc1b` | 26 |
| `frontier-20261028-rank-bound-sharpening-v1.md` | `f741e11a0cc0a73e8c094f6c2c74a09f3f902db58100e3dc9e76bf059c109aab` | 60 |
| `frontier-20261028-rank6-simplex-phase-v1.md` | `8aaa61f80a25cf0a2fae3b5b8d908e1a088b0bab107a5b814aa7eeadcf8d1054` | 48 |
| `frontier-20261028-four-zero-post-simplex-result.json` | `4a3b0d9c0f4bbc8e48d030ea9936a24e202bcfd3a3f7244dab9d39d01d9c95ae` | 287 |

The actual four-zero target and the unrestricted witness-or-exclusion gap remain open in this work. **END.**
