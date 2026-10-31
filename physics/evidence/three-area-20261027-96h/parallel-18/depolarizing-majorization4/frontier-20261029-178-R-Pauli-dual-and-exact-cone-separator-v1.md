# R positivity as a low-weight interpolation certificate; exact obstruction to decomposable-map proofs

Owner PhysicsDepol4-2 / physics-2. Actual native clock before composition: **Thu Oct 29 09:34:56 PDT 2026**. New additive packet; every earlier pinned packet remains unchanged.

**AUTHOR-WRITTEN exact linear algebra, with an eleven-dot-product Fraction check specified in §3.** Positivity of R is still **UNPROVED**. This packet does not prove unrestricted original k3. The two shortcut counterexamples below concern stronger auxiliary assertions, not the original channel or the R conjecture. No independent/formal/kernel/novelty certification is claimed. Zhang's matched clipping claim and its unresolved exact uniform-support/priority boundary remain binding.

## 1. An exact low-weight Pauli interpolation criterion

Use the conventions of packet 174: `R=M_2-M_3=4T_2-2T_1`, and for Pauli strings P without phase put

`F_j(X)=sum_(wt P=j) P X P`.

The single-site identity `sum_(a=x,y,z) sigma_a X sigma_a=4E(X)-X` gives

`F_1=4T_1-4 id`, `F_2=16T_2-12T_1+6 id`.

For the second identity, expand `(4E_i-id)(4E_j-id)` and sum over the six pairs; every E_i occurs three times. Therefore, as maps on every operator,

`4R = F_1+F_2-2 id`. (1)

For a normalized pure psi define the 16-by-66 matrix V with columns `P psi`, one for each of the 12 weight-one and 54 weight-two strings. Then

`4R(psi psi^dag)=VV^dag-2 psi psi^dag`.

The following statements are equivalent for this fixed psi:

1. `R(psi psi^dag)>=0`.
2. `psi` lies in `range(V)` and `psi^dag (VV^dag)^+ psi <=1/2`.
3. There exist complex numbers c_P with `sum_(wt P=1,2) c_P P psi=psi` and `sum |c_P|^2<=1/2`.
4. There exists an operator O supported only on Pauli weights one and two such that `O psi=psi` and `||O||_F^2<=8`.

**Proof.** For any PSD G, `G>=2 psi psi^dag` first requires psi to be orthogonal to ker(G). On range(G), conjugation by `G^{-1/2}` reduces the condition to `I>=2 zz^dag`, `z=G^{-1/2}psi`, equivalently `||z||^2<=1/2`. Take G=VV^dag and extend the inverse by zero on its kernel. The minimum squared norm of a solution of Vc=psi is `psi^dag(VV^dag)^+psi`, proving 2⇔3. Pauli orthogonality gives `||sum c_P P||_F^2=16 sum|c_P|^2`, proving 3⇔4.

No universal construction of O is supplied. The numerical pseudoinverse values observed earlier are not substitutes for such a construction or another proof.

For comparison, a pure permutation-symmetric psi does have a literal certificate:

`O=(1/6)sum_(i<j)sum_(a=x,y,z) sigma_i^a sigma_j^a`.

Each transposition acts as +1 on psi, and `swap_ij=(I+sum_a sigma_i^a sigma_j^a)/2`. The sum of the 18 Paulis therefore has eigenvalue six on psi, so O psi=psi and its coefficient norm squared is `18/36=1/2`. Thus R is positive on this class and its local-unitary images/convex hull. This is only an illustrative exact certificate; equal-radii classes were already part of the earlier regional work. It is not offered as a new original-k3 region or a global solution.

## 2. Two exact physical obstructions to dropping positive terms

### 2.1 The weight-two frame need not be bounded by 6I

Let

`psi=(|0000>+|1111>+i|0011>+i|1100>)/2`,

`phi=psi~=(|0000>+|1111>-i|0011>-i|1100>)/2`.

Both vectors are normalized and orthogonal. Every one-qubit marginal of psi is I/2: its support has no Hamming-distance-one pairs and each bit is balanced. Thus D=0 and packet 174's exact inverter identity gives

`R(psi psi^dag)=I+phi phi^dag-psi psi^dag`.

Every weight-one Pauli P has `<phi,P psi>=0`, by the antisymmetry of `Y^tensor4 P` (or directly from these four amplitudes). Hence `F_1(psi psi^dag)phi=0`. Apply (1) to phi to obtain

`F_2(psi psi^dag)phi=8 phi`.

Therefore the tempting sufficient inequality `F_2(psi psi^dag)<=6I` is **false** at an exact Gaussian-rational physical state. This is not a counterexample to R: here its spectrum is `0,1 (multiplicity 14),2`, so R is PSD exactly.

### 2.2 The single-weight frame cannot simply be dropped on null states

Let `xi=|0> tensor (|000>+|111>)/sqrt2` and `u=|0> tensor (|000>-|111>)/sqrt2`. The full four-qubit spin flip sends xi to an orthogonal vector, so C(xi)=0.

For each of the last three sites, Z_i xi=u. Every other weight-one Pauli image is orthogonal to u, and `<u,xi>=0`. Therefore

`<u,[F_1(xi xi^dag)/2-xi xi^dag]u>=3/2>1`.

This disproves the contemplated sufficient inequality `F_1(xi xi^dag)/2-xi xi^dag<=I`, even under the null-state reduction. It does not disprove R, whose positive spin-flipped-frame term cannot be discarded this way.

## 3. Exact Farkas separator: R is not CP + co-CP

This replaces the need to rely on a 252-basis enumeration for the nondecomposability assertion in packet 174. It does not assume that R is positive.

On Pauli strings of weight w, R has multipliers

`f=(16,6,0,-2,0)`.

Suppose R could be written as a sum of a completely positive map and a completely positive map composed with the full transpose. Write the latter instead as C composed with the full spin flip Gamma; conjugation by `Y^tensor4` is CP, so C is still CP. Gamma commutes with local SU(2)^4 conjugations and with site permutations, as does R. Averaging this decomposition over the compact local-unitary group and permutations preserves complete positivity and gives

`R=A_cov+C_cov composed with Gamma`.

The Choi representation of a locally covariant CP map has, at each site, the two inequivalent irreducible sectors of `U tensor conjugate(U)`: the maximally entangled line and its three-dimensional orthogonal complement. Their tensor products are multiplicity-free. After permutation averaging, positivity of the Choi matrix is exactly nonnegativity of its five coefficients indexed by the number k of complementary sectors.

The corresponding map rays are the symmetrized products of k copies of `W(X)=Tr(X)I-X/2` and 4-k identity maps. Their Pauli-weight multipliers are

`E_k(w)=sum_j binom(w,j)binom(4-w,k-j)(-1/2)^j(3/2)^(k-j)`.

Using the sum over the orbit instead of its average changes a ray only by a positive scalar. Composing with Gamma multiplies the weight-w coordinate by `(-1)^w`. Thus the supposed decomposition would force f into the cone generated by the ten vectors `E_k` and `((-1)^w E_k(w))_w`, k=0,...,4.

Define the integer linear functional

`L(v)=3v_0-8v_1+18v_2+8v_3+11v_4`.

Its exact values on those ten rays are:

| k | L(E_k) | L(Gamma E_k) |
|---|---:|---:|
| 0 | 32 | 32 |
| 1 | 0 | 64 |
| 2 | 0 | 96 |
| 3 | 16 | 0 |
| 4 | 38 | 14 |

All are nonnegative. But

`L(f)=3*16-8*6+18*0+8*(-2)+11*0=-16<0`.

This is an explicit exact cone-separation certificate. Therefore **R cannot be a sum of a CP map and a CP map composed with transpose**. If R is eventually proved positive, it is a genuinely nondecomposable positive map. The cone separation alone proves no positivity and no original-channel majorization theorem.

**Finite arithmetic actually exercised.** In the retained Python eval kernel I used `fractions.Fraction`, the exact binomial expression for E_k, and z=(3,-8,18,8,11). It returned exactly the ten table values and `L(f)=-16`. No floating arithmetic was used for these eleven dot products. The short integer/rational certificate above is the proof object; no numerical LP status is needed to check it.

## 4. Present gap and consequence boundary

The global R conjecture is equivalent to finding the interpolation certificate of §1 for every psi, or to the magic-basis operator contraction in packet 174. Its positivity remains unproved. Together with the separate bound `K3(T_1(psi psi^dag))<=3`, it would imply the original k3 inequality for every density, every complex rank-three projector and every physical p, by packet 174's nonnegative layer comparison and the parameter mirror.

The present packet supplies an exact reformulation, two exact failed-shortcut witnesses, and an exact obstruction to CP/co-CP-only proofs. It does not supply either missing universal bound. The f172-adopted regional and near-complete-depolarization window are separate and unchanged; prior findings and quarantined outputs are not rehabilitated.
