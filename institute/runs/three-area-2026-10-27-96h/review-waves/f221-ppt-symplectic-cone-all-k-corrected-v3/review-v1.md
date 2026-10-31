# f221 — corrected symplectic-cone obstruction: independent written review

## Disposition and findings

**Mathematical disposition:** the stated obstruction is supported at the explicitly conditional elementary-linear-algebra level below, for every even `d >= 4`, integer `k >= 2`, and skew-unitary `J_0`, including zero maps, both filter sides, and arbitrary finite local-CP images and sums. **0 FATAL / 0 MAJOR / 1 MINOR.** The extra odd-`l` vertex is globally completely copositive but is in fact *not* `l`-positive; the polygon is strictly larger than the `l`-positive region in every odd case. This does not invalidate the enclosure or the obstruction.

**MINOR 1 — boundary notation** (target line 9): the phrase “consecutive equalities `u=v, v=w, w=x, x=u`” should say **`u=v=0`, `v=w=0`, `w=x=0`, `x=u=0`**. Mere equality of two functions does not determine a vertex: for example `(p,q)=(0,0)` has `u=v=1/d` but is not vertex A. Interpreting the intended equalities as simultaneous active halfplane boundaries gives exactly the stated vertices and the proof below. An additive wording correction is sufficient; this is not a failure of the vertex values or cone argument.

**INCONCLUSIVE — external attribution and priority:** the literal attribution to Park, arXiv:2602.09860v1, its named theorems and any priority/novelty statement are not established by the frozen inputs. The formula below is checked as an algebraically defined map, not identified with that external work. Author-script execution and external results were not independently verified or used.

**INCONCLUSIVE — qualitative curvature:** target line 9 calls the actual odd-`l` region “generally curved,” but neither its exact boundary nor its curvature is established here. The strict odd-case enclosure and an independently derived nonlinear *necessary* inequality are established below; they do not by themselves prove curvature of the actual boundary.

**Scope:** the `k >= d/2` decomposability conclusion concerns only the displayed map family (and decomposable/local-CP images and sums derived from it). The rank-four result is likewise a family/generated-cone filter obstruction. Nothing here establishes a global `4 x 4` PPT/Schmidt-number no-go, or resolves that target. Same-harness review is not human, independent-model-family, formal/kernel, or novelty verification.

### Per-claim verdicts

| Claim | Verdict and qualification |
|---|---|
| Normalization, local Choi rotation, and distinct original `J_0` versus rotated `K_0 = conjugate(J_0)` | SUPPORTED; zero map handled separately; MINOR 1 is unrelated. |
| Four necessary rank tests, bounded quadrilateral, stated vertices | SUPPORTED with MINOR 1 wording correction. |
| Vertex `C` completely copositive; even-`l` exact `l`-positive polygon; odd-`l` necessary enclosure | SUPPORTED; moreover odd enclosure is strictly larger. Exact odd boundary/curvature is INCONCLUSIVE. |
| `BH_l` is `l`-positive | SUPPORTED by the rank and nuclear-norm argument. |
| All `2l`-input compressions and their PSD-plus-partial-transpose identities, including zero and unit singular values | SUPPORTED by the general construction; its skew-congruence step is independently reconstructed below. |
| Smaller input compressions, output compressions, both arbitrary local filters and PPT-dual equivalence | SUPPORTED, including rank-zero filters and boundary `2l=d`. |
| Arbitrary finite local-CP images and sums; addition of decomposable witnesses | SUPPORTED for the no-PPT-negative-pairing property. `k`-positivity of an added witness must be separately required. |
| PPT source, indecomposable examples, mixture threshold including endpoints | SUPPORTED for `d>2k`; the threshold endpoint has zero pairing, not a negative one. |
| Park attribution, external theorem identification, novelty and author-code execution | INCONCLUSIVE; no such fact is used as a premise. |
| General/global `4 x 4` PPT/SN3 no-go | NOT ESTABLISHED and not implied by this review. |

## Input freeze and complete-read receipt

First research artifact was the assigned manifest. Before displaying any input body, the manifest's entire SHA-256 was measured as `52ba3f0bd3b3f46a26a5f80c77cd33cdbd6e5db855c436e1740214524a99af17`, matching the assignment. Its size was 3,606 bytes / 37 LF. The manifest was displayed in raw windows 1–15, 16–30, 31–37. Before displaying any of its input bodies, **all three** input SHA-256, byte and LF counts were independently measured and matched the manifest; each ends with LF. Full paths and actual subsequent raw display order/windows:

1. `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261029-symplectic-cone-orientation-correction-v1.json` — `f95145b7c497708e4edf855609310c5a25bf4461903de1523a7395001de9f32e`; 2,154 bytes; 12 LF; window **1–12**.
2. `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-3-ppt-skew-unitary-pair-family-rank-2k-filter-obstruction-parent-v1.md` — `b3f1ed152cfb80a3f558695e40e0f6a9c00d036956e71464ef8c2706d688a8fa`; 3,300 bytes; 15 LF; window **1–15**.
3. `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261029-symplectic-cone-general-obstruction-v3.json` — `671b898e418369a0be2dbdcf36bc056eaf0fb1e1388b03eacf7f7925d7869939`; 9,794 bytes; 17 LF; windows **1–15, 16–17**.

The orientation correction was displayed first; the final line of each body was displayed. Mathematical reconstruction began only after the target's final window. The f216 disposition was read for its explicitly adopted context; the argument below is reconstructed rather than imported from its linked bodies. No other author body, earlier v1/v2, held/f161/f162 content, sibling result, web or model/API result was read or used. No author code was imported, compiled or executed. No author PASS or solver/search result is a premise.

**Explicit elementary imports/assurance:** the argument uses ordinary finite-dimensional Hermitian spectral decomposition (hence SVD), Cauchy–Schwarz, and finite-dimensional compactness as elementary mathematical facts. The specifically named complex skew-congruence step is reconstructed below rather than assumed from a paper. The external Park identification remains conditional/unverified as stated above.

## Written reconstruction

### 1. Normalization and orientation

Use `vec(Y) = sum_ij Y_ij |i,j>`, `Omega = sum_i |i,i>`, swap `F`, and `[v] = |v><v|`. For a positive map in the stated real three-parameter family, `Phi(I) = s I`, where `s = ad+b+c`. If `s=0`, positivity and `-||H||I <= H <= ||H||I` for Hermitian `H` imply `Phi(H)=0`, hence the map is zero. Otherwise `s>0`; put `t=a/s`, `p=b/s`, `q=c/s`, obtaining `dt+p+q=1`. The zero map already has zero compression and zero pairing.

Direct expansion on matrix units gives

`C = t I + p[Omega] + q (I tensor J_0) F (I tensor J_0^*)`.

Let `K_0 = conjugate(J_0)` and `j=vec(K_0)`. Because `(I tensor M)vec(Y)=vec(Y M^T)`, `(I tensor J_0^*)Omega=vec((J_0^*)^T)=j`. Thus conjugation by `I tensor J_0^*` sends `C` to

`C_hat = t I + p[j] + q F`.

`K_0` is skew-unitary, so `Fj=-j` and `<j,j>=d`. The original co-CP map term must still use `J_0`; the rotated vector, canonical forms and source use `K_0`. Local unitaries preserve decomposability, PPT and filter ranks. In particular, for `E=ld-l-1`, the point `(p,q)=(-1/E,-l/E)` has `t=l/E` and rotated Choi matrix `(lI-lF-[j])/E`. This algebraic identity does not establish any external name or attribution.

For completeness, the k-positivity/block-positivity equivalence used below follows directly as follows. Write `v=sum_a |a> tensor x_a`, `z=sum_a |a> tensor z_a`, with `a=1,...,k`, and put `eta=sum_i |i> tensor (sum_a conjugate((x_a)_i) z_a)`. Expanding matrix units yields `<z|(id_k tensor Phi)([v])|z> = <eta|C|eta>`. The coefficient matrix of `eta` has rank at most `k`; conversely any rank-at-most-`k` coefficient matrix admits such a factorization. Testing rank-one PSD inputs and all `z` proves the equivalence.

### 2. Four tests, all parities, and the cone

Set `l=min(k,d/2)`, `r=2 floor(l/2)`; `2 <= l <= d/2`. In a symplectic basis of `K_0` write its `d/2` pairs `(e_i,f_i)`, so `j=sum_i (|e_i,f_i>-|f_i,e_i>)`. There are at least `l` such pairs. The following unit vectors have the indicated Schmidt rank and expectations `f=<F>`, `h=|<j,x>|^2`:

| Vector | Rank | `(f,h)` |
|---|---:|---:|
| `|e_1,e_1>` | 1 | `(1,0)` |
| `(|e_1,e_2>-|e_2,e_1>)/sqrt(2)` | 2 | `(-1,0)` |
| sum of `r/2` paired antisymmetric vectors, divided by `sqrt(r)` | `r` | `(-1,r)` |
| `sum_{i=1}^l |e_i,f_i>/sqrt(l)` | `l` | `(0,l)` |

All ranks are at most `l`, including odd `l`; the second vector uses two isotropic `e` vectors and has zero overlap with `j`. Thus every `k`-positive map, being `l`-positive, obeys

`u=t+q >= 0`, `v=t-q >= 0`, `w=t-q+rp >= 0`, `x=t+lp >= 0`.

With `dt+p+q=1`, solving simultaneous adjacent boundary equations gives

- `u=v=0`: `A=(1,0)`;
- `v=w=0`: `B=(0,1/(d+1))`;
- `w=x=0`: `C=(-1/D,(l-r)/D)`, `D=ld+l-r-1`;
- `x=u=0`: `H=(-1/E,-l/E)`, `E=ld-l-1`.

Both denominators are positive in the stated range. The other intersections are infeasible: `v=x=0` implies `p=-t/l`, `t=q>0`, hence `w=-rt/l<0`; `u=w=0` gives `q=-t`, `p=-2t/r`, `t>0`, and `x=t(1-2l/r)<0`. From `t>=|q|` and `p>=-t/l`, normalization yields `1 >= (d-1-1/l)t`, so the feasible set is bounded. It is therefore precisely the convex quadrilateral with these four vertices; this is an enclosure of the `l`-positive family, not automatically the actual positive region.

`A` is the identity map. At `B`, `C_hat=(I+F)/(d+1)>=0`. At `C`, the **original-basis** map numerator is `l Tr(Z)I-Z+(l-r)J_0 Z^T J_0^*`. Its Choi partial transpose is

`lI-F+(l-r)[vec(J_0^*)] = lI-F+(l-r)[j] >= 0`.

Here `J_0^*=-conjugate(J_0)=-K_0`; `l-r` is 0 or 1, and `lI-F>=0`. Thus C is globally co-CP for both parities. When `l` is even, `r=l`, and `C_hat=(lI-[j])/(ld-1)` is `l`-block positive because for rank-at-most-`l` `Y`, `|Tr(K_0^*Y)| <= ||Y||_* <= sqrt(l)||Y||_F`. The other vertices are CP or the `l`-positive H vertex proved below; convexity therefore gives **exactly** the `l`-positive polygon in every even case. If `k>l`, this does not assert that every polygon vertex is `k`-positive.

When `l` is odd, let `m=l-1=r` and take the rank-`l` coefficient vector

`Y = sum_{i=1}^{m/2} (|e_i,f_i>-|f_i,e_i>) + |e_{m/2+1},f_{m/2+1}>`.

It has squared norm `l`, unnormalized swap expectation `-m`, and `|<j,Y>|^2=l^2`. At C its unnormalized numerator is `l*l-m-l*l=-m<0`. Hence C is co-CP but not `l`-positive, and the odd polygon is **strictly** an enclosure for every allowed `d,l`.

More generally, putting coefficient `a` on the paired sum and `b` on the last product vector gives the quadratic form `m w |a|^2 + (t+p)|b|^2 + 2m p Re(a conjugate(b))`. Thus actual `l`-positivity also requires `w(t+p) >= m p^2`. This is a nonlinear necessary restriction; it does not establish that the actual boundary is curved or determine the full odd region.

### 3. `BH_l` positivity and complete compression decomposition

For a rank-at-most-`l` coefficient matrix `Y`, let `S=(Y-Y^T)/2`. Then `rank(S)<=2l`, `Tr(K_0^*Y)=Tr(K_0^*S)`, and

`<vec Y|(lI-lF-[j])|vec Y> = 2l ||S||_F^2 - |Tr(K_0^*S)|^2 >= 0`.

Indeed an SVD and unitary `K_0` give `|Tr(K_0^*S)|<=||S||_*<=sqrt(2l)||S||_F`. Thus H is `l`-positive; the positive denominator `E` changes no sign.

Fix any isometry `U: C^(2l) -> C^d` and a complementary isometry `U_perp`. Define `G=U^* K_0 conjugate(U)` and `N=U^* K_0 conjugate(U_perp)`. The matrix `G` is skew and `GG^*+NN^*=I`. The following proves the needed skew-congruence normal form without importing the named theorem. For any skew `G`, let the antilinear operator `A z=G conjugate(z)` and `H=-A^2=GG^*`. Then `||Az||^2=<z,Hz>` and `<x,Ay>=-<y,Ax>`. Choose a unit eigenvector `x` of `H` with positive eigenvalue `lambda^2` and set `y=-Ax/lambda`. The vectors are orthonormal, `Ax=-lambda y`, `Ay=lambda x`, and their orthogonal complement is A-invariant by the displayed skew identity. Iterate; on the zero eigenspace `A=0`. Since `2l` is even, this gives `G=direct_sum_i lambda_i [[0,1],[-1,0]]` in a unitary basis, with `0<=lambda_i<=1` from `GG^*<=I`.

Write `s_i=sqrt(1-lambda_i^2)`. `NN^*` is diagonal with the two rows of pair i having squared norm `s_i^2`; distinct nonzero rows are orthogonal. Choosing a complement basis aligns each defective pair `s_i>0` with distinct output complement coordinates `p_i,q_i`. There is automatically enough complement dimension because `rank N=2#{i:s_i>0} <= d-2l`. In the resulting bases,

`j_U=(U^* tensor I)j = sum_i lambda_i a_i + sum_{s_i>0} s_i c_i`,

`a_i=|2i-1,2i>-|2i,2i-1>`, `c_i=|2i-1,p_i>-|2i,q_i>`, and `h_i=|2i-1,q_i>+|2i,p_i>`. The vectors `a_i,c_i` are mutually orthogonal with squared norm 2. List them as `u_alpha`, their nonnegative coefficients as `w_alpha`, so `sum w_alpha^2=l` and `j_U=sum w_alpha u_alpha`. This includes `lambda_i=0`, `lambda_i=1`, no defects, and any number of permitted defects.

Let `F_E` be swap on the input/output `E=ran(U)` block and zero on the output complement. The compressed unnormalized H witness is `C_U=lI-lF_E-[j_U]`. Let `A_other` be every unnormalized antisymmetric input/E basis vector except the `a_i`, and let `B_other` be each input/complement product basis vector outside the defective `2 x 2` blocks. Entrywise on the orthogonal sectors,

`l(I-F_E) - l sum_{s_i>0} [h_i]^{Gamma_in}`
`= l sum_alpha [u_alpha] + l sum_{v in A_other}[v] + l sum_{v in B_other}[v]`.

For each defective block this follows from `I_block-[h_i]^{Gamma_in}=[c_i]`: the partial transpose has eigenvalue `-1` on `c_i`, and `+1` on its symmetric companion and the two other block basis vectors. On the E block `I-F_E` is twice the antisymmetric projector; the symmetric block vanishes. The vector-valued Lagrange identity, valid for these real weights, gives

`l sum_alpha [u_alpha] - [j_U] = sum_{alpha<beta} [w_alpha u_beta-w_beta u_alpha]`.

Consequently

`C_U = P + Q^{Gamma_in}`,

`P = sum_{alpha<beta}[w_alpha u_beta-w_beta u_alpha] + l sum_{v in A_other}[v] + l sum_{v in B_other}[v] >= 0`,

`Q = l sum_{s_i>0}[h_i] >= 0`.

This is an identity on **all** coordinates, not merely on the span of `j_U`. An isometry of any smaller input subspace extends to a `2l`-isometry, and compression of `P+Q^{Gamma_in}` preserves this form: the Q factor is compressed with the conjugate isometry. `C_hat` is swap-invariant because `F[j]F=[j]`; swapping the two local systems gives output compression. Partial transpose on either side describes the same decomposable cone, since global transpose preserves PSD. If `2l=d`, there are no defects and the H matrix itself is PSD (`2l-d=0` on j and nonnegative on all other swap sectors). Thus at `k>=d/2`, all four enclosing vertices are globally decomposable and so is every member of **this family**.

### 4. Arbitrary PPT sources, both filter sides, and local CP closure

For a fixed Hermitian compression, the cone `D={P+Q^Gamma:P,Q>=0}` is closed: in any convergent sequence in D, the nonnegative traces of `P,Q` sum to the bounded trace of the sequence, so both PSD sequences have convergent subsequences. Its dual is the PPT cone: nonnegative pairing with all `P>=0` and all `Q^Gamma` is exactly `X>=0` and `X^Gamma>=0`. Conversely, if a matrix `C` is outside D, its closest point `D_0` in the closed cone gives `X=D_0-C` with `<X,Z> >= 0` for all `Z in D` and `<X,C> = -||C-D_0||_F^2 < 0`; hence `X` is a PPT separating source. This also proves the converse, rather than assuming an unproved cone-duality closure.

If `rank(A)<=2l`, choose an isometry spanning `ran(A)` (extend it if necessary). For any PPT `sigma`, compression of `(A tensor B)sigma(A tensor B)^*` to that range remains PPT, since partial transpose replaces A by its entrywise conjugate. The decomposable compression therefore pairs nonnegatively. The same argument holds with the sides interchanged. Conversely a negative PPT source for a compression embeds into the full local spaces and is selected by a projection filter of the corresponding rank. Rank-zero filters give zero; no normalization of a PPT source is needed, and nonzero sources may be normalized by their trace.

For arbitrary finite local CP maps with Kraus operators `M_i,N_j`, put

`C' = sum_ij (M_i tensor N_j) C (M_i tensor N_j)^*`.

For any filtered PPT source, cyclicity rewrites each summand's pairing with C using effective filters `M_i^* A` and `N_j^* B`. Their ranks are bounded by `rank(A)` and `rank(B)`, respectively, so **either** low-rank-side property survives each summand and hence the full image. This covers non-trace-preserving CP maps, both filter sides, repeated local CP images and finite sums. A decomposable witness also has nonnegative pairing with every PPT source after any local CP filter, so adding it is harmless. A decomposable witness need not itself be `k`-block positive for `k>=2`; the statement that the generated sum remains `k`-positive requires all added terms to be `k`-positive. The no-negative-PPT-pairing claim does not require that extra condition.

For the separate `k`-positivity assertion, each `(M_i^* tensor N_j^*)x` has Schmidt rank at most `k` whenever x does. Thus each local CP image of a `k`-block-positive Choi matrix is again `k`-block positive, as are finite sums of such images; adding an arbitrary decomposable term requires the additional `k`-block-positivity condition just stated.

### 5. PPT source, strict negative pairing, and mixture endpoint

For `d>2k`, take `l=k`, `W=kI-kF-[j]`, and `R=I+F+[j]`. `R>=0` since `I+F>=0`. Direct partial transposition, with the corrected complex orientation, gives

`R^{Gamma_B}=I+[Omega]+(I tensor conjugate(K_0)) F (I tensor conjugate(K_0)^*)`.

For the index check, the `((i,j),(k,l))` entry of `[vec(K_0)]^{Gamma_B}` is `(K_0)_{il} conjugate((K_0)_{kj})`. The same entry of the twisted swap is `conjugate((K_0)_{jk}) (K_0)_{li}`, which agrees because `K_0^T=-K_0`. Thus the conjugation and the partial-transpose side in this identity are fixed, not inferred from the finite control.

The twisted swap is a Hermitian involution, so `I+twisted_swap>=0`; consequently `R` is PPT. Also `Tr R=d(d+2)`, `Tr(FR)=d^2`, and `Tr([j]R)=d^2`. Hence

`Tr(WR)=d(2k-d)<0`.

A decomposable witness cannot be negative on a PPT source, so this algebraically defined `k`-positive H example is indecomposable. This does not imply that any rank-at-most-`2k` local filter can reveal it: the compression proof says the opposite.

With `E=kd-k-1`, mixing normalized H with the identity map by weight `lambda` gives pairing

`(1-lambda) d(2k-d)/E + lambda d^2`.

For `0<=lambda<=1` it is strictly negative exactly when `0<=lambda<(d-2k)/(d-2k+dE)`. The endpoint pairs to zero; above it the chosen pairing is positive, which by itself proves neither decomposability nor indecomposability. At `d=6,k=2` the strict cutoff is `1/28`. At `d=2k` the unnormalized H/PPT pairing is zero, and the full H Choi matrix is PSD as above; the strict-negative example explicitly requires `d>2k`.

## Reviewer-owned bounded exact controls

A single independent control source was created only inside this wave: `reviewer-f221-exact-controls.py`, SHA-256 `da2aadb9524d8135da46f62b8789638719424ae696b0f597c61ec61bbd1848af`. It uses Python standard-library integer pairs for exact Gaussian-integer matrix entries and `fractions.Fraction` for rational scalars; no author code, floating-point criterion, solver or unpinned scientific source is used. Run via the kernel Python interpreter with `-B`, a 115-second subprocess timeout, and `PYTHONDONTWRITEBYTECODE=1`. Actual `/bin/date` start: `2026-10-29T13:46:27-0700 PDT`; actual `/bin/date` end: `2026-10-29T13:46:27-0700 PDT`; **actual exit 0**, no stderr; output ended `ALL CONTROLS PASS`. This is finite corroboration, not a general proof.

- For `J_0=diag(J_2,iJ_2)`, checked both rotated Choi basis terms and the complete corrected source partial-transpose identity. Intended-reason negatives: `[vec(J_0)] != [vec(conjugate(J_0))]`, and using the wrong source twist gives a different matrix. The PPT part is corroborated by the exact involution square identity. Replacing `I+F` by `I-F` yields a genuinely non-PPT negative: its partial transpose has Omega expectation `-16`.
- Checked the four vectors and all six boundary-pair intersections in `(d,l)=(4,2),(6,2),(6,3),(8,3),(8,4),(10,3),(12,5)`; in each case exactly two nonadjacent intersections violate the halfplanes. The odd-C rank-`l` vector is explicitly negative; the even-C test vector saturates.
- Checked the complete entrywise PSD-plus-coPSD identity, after clearing denominators by 25, for `(d,l)=(4,2),(6,2),(8,2),(6,3),(8,3),(10,3),(8,4),(10,4)`, including 0, 1 and 3/5 canonical values, 0/1/2 defects and full-space boundary. In every case an intentionally deleted nonzero Lagrange summand produced exactly that summand as residual; when defects exist, omitting partial transpose changes the matrix. The control also verifies the required `-1` partial-transpose eigenvalue on each `c_i`.
- For two arbitrary Kraus operators per side and a PPT source, exact CP-image/adjoint-filter trace identities were checked for each rank-one filter side. The correct pairings were 523 and 830; deliberately using Kraus operators instead of their adjoints gave 869 and 686 respectively, detecting the intended error.
- For `d=6,k=2`, checked the normalized mixture at `lambda=0`, `1/56`, `1/28`, and `1/14`: signs negative, negative, zero, positive respectively.

## Process deviations

None identified. Every declared input was pin-checked before the first input body and displayed in the required order and exact small windows; the author sources were not changed. No incomplete or timed-out control is being used as exclusion. No Git, deletion, publication, infrastructure mutation or author contact was performed. The only scientific claims adopted here are the written reconstructions and their explicitly stated elementary imports, at the family and filter scopes above.
