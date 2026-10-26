# Written closure for the rank-three uniform reference embedded in two ququarts

Before-creation clock observed: **2026-10-23T13:29:20-07:00**. Status: **CANDIDATE written proof**. No new scientific program or certificate replay was performed. The earlier r=3 assay is corroborating one-encoding evidence only; it is not a premise of this proof.

## 1. Exact statement

Let each physical factor be C^4, let `o=3`, let `P=span{|0>,|1>,|2>}`, and set

`eta=Omega3=|00>+|11>+|22>`.

Define Lambda_B, A_eta, L_i, M_eta and the co-Choi matrices C_B,S_eta exactly as in the frozen reference-ray proofs. The claim is

**`C_B-S_eta>=0`, `C_B+S_eta>0`, and `ker(C_B-S_eta)=span{eta}_input⊗(C^4⊗C^4)_output`.**

By local-unitary covariance this covers every two-ququart reference having three equal nonzero Schmidt coefficients and one zero coefficient. It does not cover arbitrary Schmidt-rank-three references: the separate exact angle obstruction has already ruled that out.

The switched-complement bridge then gives rank-two endpoint nonnegativity whenever a range or co-range contains a ray `a⊗eta`, with arbitrary first-site dimension. The same kernel argument as the equality addendum yields its strictness/equality classification. These consequences are conditional on this newly written closure until it is independently reconstructed.

## 2. Exact inverse and a complete sector decomposition

Use positions 1,2 for the two-site input and 3,4 for the output. The raw coefficient formula is

`(S_eta)_((i,p),(j,q))=<L_j†p,A_eta^(-1)L_i†q>`.

Let `F_A=F_13`, `F_B=F_24`; then `C_B=(I-F_A/2)(I-F_B/2)`.

The reference inverse is block diagonal according to whether each local index is in P or at o:

- on `P⊗P`, `A_eta^(-1)=I/2-|Omega3><Omega3|/22`;
- on `P⊗o` and `o⊗P`, `A_eta^(-1)=2I/5`;
- on `o⊗o`, `A_eta^(-1)=1/3`.

In particular `A_eta^(-1)Omega3=(4/11)Omega3`.

The relevant L operators are

`L_ij=delta_(ij)I-(E_ij⊗I+I⊗E_ji)/2+|ij><Omega3|/4`, i,j in P,

`L_oi=-(E_oi⊗I)/2+|oi><Omega3|/4`,

`L_io=-(I⊗E_oi)/2+|io><Omega3|/4`,

`L_oo=|oo><Omega3|/4`.

Independent phase rotations at the outside level of each physical site leave eta fixed. The covariance of M_eta implies that both co-Choi matrices conserve the number n_A of outside labels among positions 1,3 and the number n_B among positions 2,4. Thus there are nine **orthogonal exact reducing sectors**, with dimensions

| (n_A,n_B) | Dimension |
|---|---:|
| (0,0) | 81 |
| (1,0),(0,1) | 54 each |
| (2,0),(0,2) | 9 each |
| (1,1) | 36 |
| (2,1),(1,2) | 6 each |
| (2,2) | 1 |

Their dimensions sum to 256. Physical interchange of the two ququart factors identifies the paired sectors. No unverified sparsity or discarded matrix entry is assumed.

## 3. The simple sectors

### 3.1 All four labels inside P: (0,0)

The inverse and L contractions restrict to exactly the two-qutrit uniform-reference matrices C_3,S_3. The dimension-universal GSd proof at d=3 therefore gives both signs, strict positivity of the plus sign, and a nine-dimensional minus kernel `Omega3_input⊗(P⊗P)_output`. This is an explicit written-theorem dependency, not an inference from the r=3 assay.

### 3.2 All four labels outside: (2,2)

Here `C_B=1/4` and `S_eta=3/44`. The two signs are `2/11` and `7/22`, both positive.

### 3.3 Both first-site labels outside: (2,0)

Use the basis `|o,b,o,d>`, b,d in P, and let T swap b,d. Direct contraction of the displayed L_oi gives

`C_B=I/2-T/4`, `S_eta=I/8-3T/88`.

For T=+1 the minus/plus eigenvalues are `7/44,15/44`; for T=-1 they are `13/22,10/11`. Hence both signs are strictly positive. Sector (0,2) is identical by physical factor interchange.

For example `L_ob†|od>=-|bd>/2+delta_(bd)Omega3/4`; its inner products with the P⊗P inverse yield the identity coefficient 1/8 and swap coefficient -3/88 above.

### 3.4 Three outside labels: (2,1)

For each i in P use the two orientations

`A_i=|o,o,o,i>`, `B_i=|o,i,o,o>`.

In this basis the two matrices, tensored with I on the i label, are

`C_B=[[1/2,-1/4],[-1/4,1/2]]`,

`S_eta=[[0,1/44],[1/44,1/10]]`.

The minus matrix has positive leading entry and determinant `76/605`; the plus matrix has positive leading entry and determinant `601/2420`. Both are positive definite. Sector (1,2) is the physical interchange.

The 1/44 cross entry follows from pairing `-|ii>/2+Omega3/4` with `Omega3/4` under the P⊗P inverse. The 1/10 diagonal comes from a one-outside vector with inverse 2/5.

## 4. One outside label at each site: (1,1)

For each i,j in P, order the four orientations as

`A_ij=|o,o,i,j>`,

`B_ij=|o,j,i,o>`,

`C_ij=|i,o,o,j>`,

`D_ij=|i,j,o,o>`.

Within these orientations F_A swaps A with C and B with D; F_B swaps A with B and C with D. Thus the C_B matrix is

`[[1,-1/2,-1/2,1/4],`

` [-1/2,1,1/4,-1/2],`

` [-1/2,1/4,1,-1/2],`

` [1/4,-1/2,-1/2,1]]`,

tensored with the identity on the internal pair (i,j). Let `Pi=|Omega3><Omega3|` on that internal pair; its eigenvalues are three on Omega3 and zero on its orthogonal complement. The raw contractions give

`S_eta=[[0,0,0,Pi/11-I/44],`

`       [0,0,Pi/8-3I/88,I/10-Pi/5],`

`       [0,Pi/8-3I/88,0,I/10-Pi/5],`

`       [Pi/11-I/44,I/10-Pi/5,I/10-Pi/5,Pi/3]]`.

For example the A-D block contracts a general inside L_kl† against Omega3/4, giving `delta_(ij)delta_(kl)/11-delta_(ik)delta_(jl)/44`. The B-C block pairs `-|ik>/2+delta_(ik)Omega3/4` with its companion, giving `Pi/8-3I/88`. The B-D block uses the one-outside inverse 2/5 and gives `I/10-Pi/5`. These explicit checks fix the co-Choi orientation and all coefficients.

### 4.1 Internal Omega3 direction

Substitute Pi=3. The B-C antisymmetric orientation has minus/plus eigenvalues `12/11,9/22`. On the remaining A,(B+C)/sqrt(2),D directions:

- C_B-S_eta has a zero D row/column and the positive 2×2 block

  `[[1,-1/sqrt(2)],[-1/sqrt(2),10/11]]`, with determinant 9/22;

- C_B+S_eta has matrix

  `[[1,-1/sqrt(2),1/2],`

  ` [-1/sqrt(2),35/22,-sqrt(2)],`

  ` [1/2,-sqrt(2),2]]`.

After eliminating the first pivot one, the latter Schur block has diagonals `12/11,7/4`, off-diagonal `-3/(2sqrt(2))`, and determinant `69/88>0`. Hence the plus sign is positive definite and the minus sign has exactly the one-dimensional D⊗Omega3 kernel.

### 4.2 Internal traceless directions

Substitute Pi=0. For each of the eight internal traceless directions, the B-C antisymmetric orientation has minus/plus eigenvalues `63/88,69/88`. The remaining three-dimensional matrices are

`Minus=[[1,-1/sqrt(2),3/11],`

`       [-1/sqrt(2),113/88,-3sqrt(2)/5],`

`       [3/11,-3sqrt(2)/5,1]]`,

`Plus =[[1,-1/sqrt(2),5/22],`

`       [-1/sqrt(2),107/88,-2sqrt(2)/5],`

`       [5/22,-2sqrt(2)/5,1]]`.

After eliminating their first pivots, the minus Schur block has positive diagonals `69/88,112/121` and off-diagonal `-51sqrt(2)/110`. Its determinant is `19689/66550>0`. The plus Schur block has positive diagonals `63/88,459/484` and off-diagonal `-63sqrt(2)/220`; its determinant is `548289/1064800>0`. Both signs are therefore strictly positive on all these directions.

This accounts for all 36 dimensions of sector (1,1).

## 5. One outside label at the first site only: (1,0)

There are two orientations for each triple i,j,k in P:

`X_ijk=|o,j,i,k>`, `Y_ijk=|i,j,o,k>`.

Let T swap the internal j,k indices. F_A exchanges X,Y and F_B acts as T, so

`C_B=(I-J/2)(I-T/2)`,

where J exchanges the two orientations.

On the 27-dimensional internal space define

`U1(v)=Σ_a |a,a,v>`, `U2(v)=Σ_a |a,v,a>`,

`P1=U1 U1†`, `K12=U1 U2†`, `K21=U2 U1†`.

Then direct L contraction gives the orientation blocks

`S_XX=0`,

`S_YY=(2/5)[P1-(K12+K21)/2+T/4]`,

`S_XY=I/8-P1/4+K12/8+5K21/44-T/11`,

`S_YX=S_XY†`.

For instance, in the X-Y contraction the P⊗P inverse sends

`-|jn>/2+delta_(jn)Omega3/4`

to

`-|jn>/4+(5/44)delta_(jn)Omega3`.

Pairing with the full inside L_lm† expression produces the identity, P1, K12, K21 and T coefficients shown. The Y-Y contraction instead uses the one-outside inverse 2/5. Thus the two inverse blocks have not been conflated.

### 5.1 Orthogonal complement of the two contraction ranges

Let `Kint=ran U1+ran U2`. Since `U1†U1=U2†U2=3I`, `U1†U2=I`, its dimension is six. T interchanges its two ranges. On its 21-dimensional orthogonal complement all P1,K12,K21 terms vanish. For each T eigenvalue epsilon=+1 or -1, the orientation matrices are

`C_B=(1-epsilon/2)[[1,-1/2],[-1/2,1]]`,

`S_eta=[[0,1/8-epsilon/11],[1/8-epsilon/11,epsilon/10]]`.

All four sign/epsilon combinations have positive diagonal leading pivots. Their determinants, in order epsilon=+1 minus/plus then epsilon=-1 minus/plus, are

`4619/38720`, `9811/38720`, `56803/38720`, `70267/38720`.

Thus both signs are strictly positive on this full complement, without a sampled spectral assertion.

### 5.2 The internal contraction ranges

For a fixed unit v, the basis U1(v),U2(v) has Gram matrix `G=[[3,1],[1,3]]`. The operator T swaps the two basis vectors. In the ordered basis XU1,XU2,YU1,YU2, multiplying the action matrices by the corresponding Gram metric gives the following **quadratic-form** matrices:

`Form(C_B-S_eta)=`

`[[5/2,-1/2,0,-1/11],`

` [-1/2,5/2,0,-2],`

` [0,0,0,0],`

` [-1/11,-2,0,16/5]]`,

`Form(C_B+S_eta)=`

`[[5/2,-1/2,-5/2,13/22],`

` [-1/2,5/2,1/2,-1/2],`

` [-5/2,1/2,5,-1],`

` [13/22,-1/2,-1,9/5]]`.

To check the metric multiplication explicitly, the common C_B diagonal form block is `D=[[5/2,-1/2],[-1/2,5/2]]`, its cross block is -D/2, and the S_XY form block is `[[ -5/4,15/44],[1/4,3/4]]`. The S_YY form block is `[[5/2,-1/2],[-1/2,-7/10]]`.

The upper-left D is positive definite, with inverse `[[5/12,1/12],[1/12,5/12]]`.

For the minus sign, the YU1 row/column is zero and the Schur complement on YU2 is `3629/2420>0`. Thus its kernel is exactly YU1.

For the plus sign, eliminating D gives the positive Schur matrix

`[[5/2,-9/22],[-9/22,3871/2420]]`,

whose determinant is `3709/968>0`. Therefore the plus sign is positive definite. The argument applies independently to each of the three basis vectors v, accounting for all 12 dimensions of this internal-range orientation sector.

Combining Sections 5.1–5.2 covers all 54 dimensions of (1,0). The physical factor interchange covers (0,1).

## 6. Assembly, exact kernel and limits

Every sector has now been treated by an explicit scalar or at-most-four-dimensional quadratic form, plus the written d=3 GSd import on the all-inside block. C_B+S_eta is strictly positive in every sector. The C_B-S_eta kernels are:

- dimension nine in (0,0), for both output labels inside P;
- dimension three in each of (1,0),(0,1), for one outside output label;
- dimension one in (1,1), for both outside output labels;
- no others.

These total sixteen dimensions and are exactly `Omega3_input⊗(C^4⊗C^4)_output`. This proves the stated kernel as well as the two signs.

This is a written universal reference-ray result, not a new finite scientific run or a claim that the earlier assay independently verified its physical modeling. The one-encoding assay agrees, but the present proof rests on the raw L contractions, exact sector symmetries, Gram metrics and positive Schur complements.

The angle-obstruction packet gives rank-three nonuniform rays for which symmetric GS fails; thus this positive uniform result cannot be generalized by dropping equality of the three nonzero Schmidt coefficients. No complete angular characterization, unrestricted W4 theorem, novelty clearance, human review or kernel verification follows automatically.
