# f649: exact physical matrices, conditional-route failure, and two sufficient regions

**Status: independent same-harness AUTHOR reconstruction and proposed finite source; source NOT RUN.** The exact equalities below are written calculations/expected checker values, not observed execution output or a parent disposition. If checked, the first example disproves the previously **conditional sufficient CORE-GRAM premise** on actual doubly orthonormal frames. It does **not** violate Q or the physical T2 target. The original unrestricted Q/T2 remains open within this packet. Nothing here claims a family-wide computational check, independent-model/family, human, kernel, novelty, or publication acceptance.

## 1. Definitions and genuinely physical frame

Use basis `|ij>` with zero-based indices and linear index `4i+j`. For an operator `R` on `C^4 tensor C^4`, define

`F(R) = ((Tr_B R)_0, (Tr_A R)_0)`,
`q(R) = ||Tr_B R||_F^2 + ||Tr_A R||_F^2 - |Tr R|^2/2`,
`G(R) = ||R||_F^2 + |Tr R|^2 - ||Tr_B R||_F^2 - ||Tr_A R||_F^2`.

The inner product is conjugate-linear in its first argument. The imported original **double-universal** equivalence is `q(R) <= 2||R||_F^2` for all rank-at-most-two `R` iff `S_2(A tensor I + I tensor B) <= 2L` for all traceless complex `4x4` pairs, with `L=||A||_F^2+||B||_F^2` and `S_2` the sum of the two largest squared singular values. This is not a fixed-pair equivalence.

Put `b=(4,2,2,1)`, `a=(4|00>+2|11>+2|22>+|33>)/5`,

`u1=|01>`, `v1=-(6|01>+8|02>+|10>)/sqrt(101)`, `u2=v2=a`,
`x1=|u1><v1|`, `x2=|a><a|`, and `R=x1+x2/sqrt(101)`.

The norms of `u1,u2,v1,v2` are one, and the two `u` vectors and the two `v` vectors are respectively orthogonal. Thus these are actual singular-vector frames. The first normalized right vector must include the `sqrt(101)` denominator; no auxiliary Gram matrix is substituted for an actual frame.

### Complete 16-by-16 matrices

The following row lists specify **all entries**, not merely a selected principal block. `Z` denotes the zero row of length 16, and all columns are ordered `00,01,02,03,10,11,12,13,20,21,22,23,30,31,32,33`. Define

```
s = (0,-6,-8,0,-1,0,0,0,0,0,0,0,0,0,0,0)
p0  = (16,0,0,0,0,8,0,0,0,0,8,0,0,0,0,4)
p5  = ( 8,0,0,0,0,4,0,0,0,0,4,0,0,0,0,2)
p10 = ( 8,0,0,0,0,4,0,0,0,0,4,0,0,0,0,2)
p15 = ( 4,0,0,0,0,2,0,0,0,0,2,0,0,0,0,1)
S = rows(Z,s,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z)
T = rows(p0,Z,Z,Z,Z,p5,Z,Z,Z,Z,p10,Z,Z,Z,Z,p15)
```

Then `x1=S/sqrt(101)`, `x2=T/25`, and **the complete actual rank-two operator** is `R=(25S+T)/(25sqrt(101))`. The proposed checker independently forms `S` from the two vectors, `T/25` as both an outer product and the explicit coefficient table, and `sqrt(101)R` a second time by adding its three prescribed row entries. It checks the projector equation, rank, and both left/right SVD actions. Thus the singular values of `R` are `1` and `1/sqrt(101)`; in particular `||R||_F^2=102/101`.

Direct contraction of the actual 16-by-16 matrices gives

```
Tr_B x1 = -6 E00/sqrt(101),  Tr_A x1 = -(6 E11+8 E12)/sqrt(101)
Tr_B x2 = Tr_A x2 = rho = diag(16,4,4,1)/25
c1 = Tr x1 = -6/sqrt(101),  c2=1,  Tr(rho^2)=289/625
```

Here `E12` is not replaced by `E21`. Let `C12=<Tr_B x1,Tr_B x2>+<Tr_A x1,Tr_A x2>` and

`4 p_i = 1+|c_i|^2-||Tr_B xi||_F^2-||Tr_A xi||_F^2`.

Writing `t=sqrt(101)`, the expected exact values are

```
p1 = 1/404,            p2 = 168/625,
t*C12 = -24/5,         t*(conj(c1)c2 - C12) = -6/5.
```

Both `p_i` are positive. The mixed term is strictly negative, and **positive squares**, not a sign-ambiguous squaring, give

```
|conj(c1)c2-C12|^2 = 900/63125 > 672/63125 = 16 p1 p2.
```

Consequently `Re(conj(c1)c2-C12) < -4 sqrt(p1 p2)`: the proposed universal CORE-GRAM premise fails on this actual frame. Equivalently its `G`-matrix has determinant `-228/63125`. For this real frame the imported displayed convention `c1 conj(c2)` happens to agree; in general the mixed coefficient used with `z1* z2` is **`conj(c1)c2-C12`**. The checker uses an actual `u1 -> i u1` phase change to test conjugation: the corresponding `h` becomes `-i h`, not `+i h`.

The physical marginals of `R` are

```
Tr_B R = diag(-134,4,4,1)/(25 sqrt(101))
Tr_A R = (diag(16,-146,4,1)-200 E12)/(25 sqrt(101)).
```

Their squared Frobenius norms are respectively `17989/63125` and `61589/63125`, and `Tr R=-5/sqrt(101)`. Substitution yields the following **expected exact values**, which the proposed source recomputes entry-by-entry:

```
G(R) = -203/63125 < 0,
q(R) = 143531/126250 < 255000/126250 = 2||R||_F^2,
2||R||_F^2-q(R) = 111469/126250 > 0.
```

Thus the sufficient route fails but Q holds for this operator. No `A,B` are fabricated to claim a physical Q/T2 violation. Its trace and `C12` are nonzero; the range `span{|01>,a}` differs from its adjoint range `span{v1,a}`, and since `a` has Schmidt rank four both common local supports have dimension four. These classifications refer to the actual operator, not an unrelated compression.

## 2. Entire actual-frame span: uniform region and exact residual

For any actual frame put `q_i=q(x_i)`, `h=<F(x1),F(x2)>=C12-conj(c1)c2/2`, `alpha_i=2-q_i`. For arbitrary complex coefficients,

```
q(z1 x1+z2 x2) <= (|z1| sqrt(q1)+|z2| sqrt(q2))^2
                <= (q1+q2)(|z1|^2+|z2|^2).
```

The first step is the triangle inequality in the direct sum of the traceless-marginal spaces, the second Cauchy–Schwarz; frame orthogonality gives the norm on the right. Therefore `q1+q2<=2` is a sufficient condition for Q on the **entire actual complex two-plane**, including all phases and singular-value ratios. Using the imported rank-one swap identity this is equivalently `4(p1+p2)>=(|c1|^2+|c2|^2)/2`. It is sufficient, not necessary. The example has

```
q1=118/101, q2=531/1250, h=-9/(5 sqrt(101)),
q1+q2=201131/126250 < 2.
```

The actual span Gram matrix `[[q1,h],[conj(h),q2]]` has positive diagonal principal minors and determinant `29304/63125>0`. The residual matrix `[[2-q1,-h],[-conj(h),2-q2]]` has diagonal entries `84/101` and `1969/1250` and determinant `80673/63125>0`. Hence the written PSD check directly confirms Q for every complex combination of these **actual** dyads, including the example where `G<0`.

Generally the rank-one identity gives `q_i<=3/2` and hence `alpha_i>=1/2`. On any actual frame, Q for all complex coefficients is **equivalent** to the exact residual

`|C12-conj(c1)c2/2|^2 <= (1-|c1|^2/2+4p1)(1-|c2|^2/2+4p2)`.

This is the determinant condition for the residual matrix, not the false CORE-GRAM premise. Because every rank-two operator admits such a doubly orthonormal SVD, the unpaid part is this residual for all remaining actual frames with `q1+q2>2`; its universal proof would settle Q/T2 via the imported double-universal equivalence. Conversely an actual frame with strict residual failure supplies a genuine rank-two Q violation, but **no such frame is claimed here**.

A second sufficient consequence, valid for actual SVD weights `s1>=s2>=0`, is `(s1 sqrt(q1)+s2 sqrt(q2))^2 <= 2(s1^2+s2^2)`. In particular `s2/s1<=3-2sqrt(2)` suffices by the rank-one `q_i<=3/2` bound. This does not claim unrestricted Q.

## 3. A separate physical-pair region and actual irreducible example

For a traceless pair write `X=A tensor I+I tensor B`, let `sigma_1>=sigma_2` be its two largest singular values, and take `L=||A||_F^2+||B||_F^2`. Pairing a normalized top singular dyad against `X`, the rank-one swap inequality and Cauchy–Schwarz give `sigma_1^2<=3L/2`. Consequently the physical-pair condition `sigma_2/sigma_1<=1/sqrt(3)` (with the zero case immediate) gives `S_2(X)<=2L`. It is a sufficient class of **pairs**, not a class of dual frames or a global proof.

Now take the actual traceless matrices

```
D = diag(3,-1,-1,-1),
N = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]],
A=B=M=D+N/10.
```

Both have squared Frobenius norm `1203/100`; therefore the actual pair has `L=1203/50`. The complete actual physical 16-by-16 matrices can be displayed without omitted entries in 4-by-4 block form:

```
K = [[60,1,0,0],[0,20,1,0],[0,0,20,1],[0,0,0,20]]
J = [[20,1,0,0],[0,-20,1,0],[0,0,-20,1],[0,0,0,-20]]
10 X = [[K,I4,0,0], [0,J,I4,0], [0,0,J,I4], [0,0,0,J]]
X0 = diag(6,2,2,2, 2,-2,-2,-2, 2,-2,-2,-2, 2,-2,-2,-2).
```

Indeed `X0=D tensor I+I tensor D` and `X-X0=(N tensor I+I tensor N)/10`. Direct multiplication gives `N^dagger N=diag(0,1,1,1)`, a nonzero orthogonal projection, so `||N||_op=1` and `||X-X0||_op<=1/5`. The exact **eigenvalue** multiplicities of `X0` are `6:1`, `2:6`, `-2:9`; its singular-value multiplicities are `6:1`, `2:15`. Singular-value perturbation yields **bounds**, not an asserted exact spectrum of `X`:

```
29/5 <= sigma_1(X) <= 31/5,     sigma_2(X) <= 11/5,
sigma_2/sigma_1 <= 11/29 < 1/sqrt(3),
S_2(X) <= (1443/841)L < 2L.
```

The same Weyl bounds give the independently useful direct estimate `S_2(X)<=1082/25 < 1203/25=2L`, a strict gap of at least `121/25`. Neither bound purports to calculate the exact singular values of `X`.

The pair is outside the separately `2+2` reducing class: a projection `P=P^dagger=P^2` commuting with `M` also commutes with `M^dagger`. The `3`-eigenspace of `M` is exactly `span{e0}`; thus `P e0=lambda e0` with `lambda` either zero or one. The actual identities

```
(M^dagger-3I)e0=e1/10,
(M^dagger+I)e1=e2/10,
(M^dagger+I)e2=e3/10
```

force `P e_j=lambda e_j` for every `j`, so `P` is `0` or `I`. The checker separately constructs the complete `32 x 16` real-coefficient system `[Z,M]=[Z,M^dagger]=0` and requires rank 15 over `Q`, equivalently over `C`, hence a scalar commutant. These are projection and linear-system descriptions of the same exact irreducibility, not a numerical eigenvector test. Also `M^2[0,1]=1/5` and `[M^2,(M^2)^dagger]_{00}=401/10000`, so both `A^2` and `B^2` are genuinely nonnormal.

The strict spectral-ratio condition is open. Irreducibility is open at this pair: injectivity of the commutator map on the compact unit sphere of traceless Hermitian matrices persists under small perturbations. Accordingly the new physical-pair class has a nonempty open portion outside the separately `2+2` class; no comparison to every other known physical class and no novelty claim is made.

## 4. Proposed exact source, controls, and what is not observed

The new self-contained source is `finite-checker-v1.py` in this same wave directory. It uses only standard-library `Fraction`, an exact Gaussian-rational pair, and a monotonic cooperative cutoff of 54 seconds. The `sqrt(101)` factors are kept symbolic as described above; no floating-point scientific arithmetic, dependency, file I/O, network, subprocess, deletion, or solver is used. It constructs and prints all entries of the actual `sqrt(101)x1`, `x2`, `sqrt(101)R`, `X0`, and `X`, recomputes the marginals and invariants, checks the full frame, real ranks, SVD actions, both Gram matrices' principal minors, the actual physical norm and exact commutator system, and performs named failure-reason controls. Its source contains no `assert`-based load-bearing checks.

The seven intended negative controls must each fail for its named mathematical reason, not by an arbitrary exception: sign-flipped core term (`CORE_SIGN`); wrong complex phase (`CONJUGATION`); swapped partial traces (`PARTIAL_TRACE`); nonorthogonal first frame (`FRAME_ORTHOGONALITY`); a false assertion that this real `R` violates Q (`FALSE_Q_COUNTEREXAMPLE`); a wrong physical `L` (`PHYSICAL_NORM`); and the actually reducible diagonal `D` substituted for `M` (`IRREDUCIBLE_COMMUTANT`). The phase check first constructs a legitimate complex-rephased physical frame. The false-Q control deliberately tests a false claim and is not a purported physical witness.

**No child scientific execution, source run, tests, CAS, solver, sampling, or observed output occurred.** The values, mutation outcomes, and `COMPLETE` line are expected only if a future execution succeeds. Before any actual execution the parent must read the entire proposed source, pin it, decide admission, and, if authorized, run it once under the parent protocol and report its actual settlement. A timeout, error, partial output, or wrong mutation reason is INCOMPLETE, not a scientific pass. The source's 54-second cooperative limit does not claim an OS-enforced memory ceiling or measured runtime.

## 5. Provenance and exact frontier

Before the packet body, this author read the complete assigned manifest, freeze receipt, parent pre-dispatch metadata, actual dispatch receipt, and all 15 listed status/permission controls through their endings, then sent a direct PREBODY ACK. The entire 243-LF literal packet was then read in ordered raw windows of at most 20 LF including its final line; no packet output was truncated. Afterwards a native-clock metadata observation was `2026-10-30T15:16:28-0700 PDT`. Own metadata-only SHA-256 checks matched manifest `a85241f04ed6d422dbc0e6422c36756c00323b14b0bf56a4fadb8d26ac2b1ebe`, freeze `c94141377f1242405a3793b4e7b48410949c4a20fab8b07a4dbd01edf4e9e27c`, and packet `fb308310fa2e844bc01cc624d76b87ad9feceb150f80860346e051c151ce3df8`. The packet supplies the unadopted f643 candidate and the clean conditional dual, corrected transpose, separately-2+2, and qubit-side scopes; no linked source, sibling review, old author code, or external source was followed. All held episodes and all their consumers, including held CORE, f285 and f289, are NONINPUT. No cognitive-isolation certificate is claimed.

A verified CORE-GRAM failure would refute only that **sufficient route**. Exact unrestricted original T2, Q on all remaining actual frames, higher-rank targets, broader physical claims, independent/third-party verification, kernel checking, and priority/novelty remain unpaid. The source and this report are proposed new artifacts; independent review and parent disposition have not occurred.
