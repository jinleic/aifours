# Two-pair reference rays: a complete asymmetric-domination candidate

Before-creation clock observed: **2026-10-23T15:06:34-07:00**. Owner: physics-1 / PhysicsResearch96h. Assurance: **CANDIDATE written proof, not independently reconstructed, formally verified, novelty-cleared, or accepted**.

This packet closes the last88 charge-zero dimensions left by checkpoint007. Together with its explicitly pinned leaf proofs below, it is a complete candidate for a **scoped W4 reference-ray theorem**, not unrestricted three-copy ququart Werner undistillability. The new derivation is written algebra; no scientific program, CAS, finite replay or new GO was used. Earlier round assays and the parent's disclosed arithmetic cells are not mathematical premises and are not relabeled formal verification.

## 1. Exact statements and the unchanged full problem

Let `Lambda(X)=Tr(X)I_4-X/2`, `B=Lambda tensor Lambda`, and use the reversed-input co-Choi convention

`Jhat(E)=sum_(i,j) |j><i| tensor E(|i><j|)`.

For a nonzero two-ququart reference eta define

`A_eta=B(|eta><eta|)`, `L_i=B(|i><eta|)`,

`M_eta(|i><j|)=L_i A_eta^-1 L_j†`,

`C_B=Jhat(B)=(I-F_13/2)(I-F_24/2)`, `S_eta=Jhat(M_eta)`.

A_eta is invertible; it is at least `||eta||^2 I/4`. Multiplying eta by a nonzero scalar does not change S_eta.

### Candidate Theorem A — all two-equal-pair reference angles

For every finite t>=0, with

`eta_t=|00>+|11>+t|22>+t|33>`,

one has the full256-dimensional inequalities

**`C_B-S_eta>=0`, `3C_B+S_eta>=0`.**

For t>0, the second inequality is strict and

`ker(C_B-S_eta)=span{eta_t}_input tensor (C^4 tensor C^4)_output`.

No endpoint equality/kernel classification at t=0 is asserted. The nonstrict inequalities there suffice for the following consequence. Local unitaries and scaling transport the result to every reference whose Schmidt coefficients have the form `(a,a,b,b)`, a,b>=0 and not both zero.

### Candidate Theorem B — the resulting rank-two partial-trace class

For `H=H1 tensor C^4 tensor C^4`, with H1 any finite-dimensional complex space, set

`q3(C)=||C||_HS^2-(1/2)sum_i||Tr_i C||_HS^2+(1/4)sum_(i<j)||Tr_ij C||_HS^2-(1/8)|Tr C|^2`.

Every trace is the unnormalized partial trace of the coefficient operator itself. If rank C<=2 and its range contains a nonzero ray `a tensor eta`, where eta has Schmidt coefficients `(a0,a0,b0,b0)`, then **q3(C)>=0**. The same holds for the adjoint co-range class. The other range vector and both covectors are arbitrary complex vectors; no normality, Hermiticity, positivity or block-product condition on them is imposed. No equality classification is added.

For H1=C^4 this is a scoped class of the frozen64x64 W4 target. **The unrestricted statement for every complex rank<=2 C remains NOT PROVED here.** The book's Quantum Channel article is a motivating source, not a claim that this theorem solves all its capacity/resource questions.

## 2. Dependency closure and complete sector accounting

All files below are in this owned slot and remain immutable evidence snapshots. None has yet been promoted by a distinct reconstruction of the complete new candidate.

| Leaf | SHA256 | Exact role |
|---|---|---|
| checkpoint002, eight-dimensional angular compression | `47a24185bbf5f1a1de7fbe64f4ec585feda2b488b1e68b53c11fe35c7ad21ecf` | Full fixed8 physical table, full inverse and exact reference kernel |
| checkpoint003, fixed minus sign | `761e04717ce22a786352ab75b1faf6ff3c4b865e13714a8da81a290def169a5e` | Upper bound on fixed8 for t>0, exact two kernels |
| checkpoint004, extremal charges | `fc210c46216932b4846d7cad6c1754538d4d66ff597c951d57533ff4b7e6eaf4` | Both symmetric signs on32 charge±2 dimensions |
| checkpoint005, higher charge-one sectors | `a7432f7d2d417f60f5bc64d3eea042ca8556b7fe936081afdf25bba4394f5147` | Both symmetric signs on64 higher charge±1 dimensions |
| checkpoint006, fixed threshold and asymmetric bridge | `cc8e1ed4830e728cd4f168d3ee3b9657f7aa684908842385a4ac719d0b281399` | Explicit fixed Schur matrices; independently derived one-site spectrum |
| checkpoint007, nonzero-charge and fixed asymmetric closure | `4299d5a8e3259f7d7c0911abe6a34a830c62318ad598476450dcf99daf9600b3` | Completes all160 nonzero-charge dimensions and fixed8 for the asymmetric signs |

The group is U(2)_A x U(2)_B, A={0,1}, B={2,3}, with conjugate action on negative slots2,4. Eta_t is invariant. The central charges2,1,0,-1,-2 have dimensions16,64,96,64,16. Charge zero decomposes as

- fixed subspace, dimension8;
- spin-two A and B, dimension5 each;
- product of the two adjoint representations, multiplicity4, dimension36;
- adjoint A, multiplicity7, dimension21;
- adjoint B, multiplicity7, dimension21.

These exhaust96 dimensions: `8+5+5+36+21+21=96`. The earlier packet closes the first8 and all nonzero charges. Sections3-6 below close the other88, with explicit physical matrices rather than a symmetry-based positivity guess.

Use throughout

`s=t^2`, `a=1+2s`, `b=2+s`, `c=3(1+s)/2`,

`k=1/a`, `l=s/b`, `p=kl`, `L=k+l=1-3p`,

`r=1/[4+2L]=1/[6(1-p)]`, `delta=(l-k)/2`.

The full inverse is `A_eta^-1=D^-1-r|H><H|`, H=D^-1 eta; D has values a,b,c on AA,BB,mixed pairs. It is never replaced by a truncated inverse.

## 3. The two spin-two sectors: exact constant scalar

The unique highest-weight vector of spin-two A is `w_A=|0,1,0,1>`. Its full diagonal-phase weight cannot occur in any other group pattern, so the corresponding weight space is one-dimensional. The group orbit spans the five-dimensional symmetric spin-two representation (identify each negative SU(2) leg with a positive leg using the invariant alternating form). Covariance therefore extends the scalar calculation to the full reducing5-dimensional sector.

Both physical swaps fix w_A, hence C_B has scalar1/4. Directly,

`L_01†|01>=-(1/2)Omega_A+(1/4)eta`.

Its D^-1 norm squared is L/8, and its H inner product is delta. Thus

`S_eta(w_A,w_A)=L/8-r delta^2=1/12`,

because `(k-l)^2=(1-p)(1-9p)`. This is an exact identity for every angle. The B highest-weight vector `|2,3,2,3>` gives the same scalar. Consequently both spin-two sectors have

`C_B-S_eta=I/6`, `C_B+S_eta=I/3`.

They are strictly positive also for the asymmetric lower sign. Total dimension closed:10.

## 4. The36-dimensional product-adjoint sector

Take the highest-weight traceless matrices E_01 on A and E_23 on B. Their complete highest-weight space consists of the four orthonormal coordinate vectors

`P1=|0,1,2,3>`, `P2=|2,3,0,1>`,

`P3=|0,3,2,1>`, `P4=|2,1,0,3>`.

The diagonal-phase weight forces exactly these four placements. Each is annihilated by both raising operators, so their group orbits give four copies of the3x3-dimensional product-adjoint representation. No other representation has this highest weight. The full36-dimensional restriction is therefore the following4x4 form tensored with its9-dimensional irrep identity.

The physical swap formula gives

`C4=[[1,1/4,-1/2,-1/2],`

`    [1/4,1,-1/2,-1/2],`

`    [-1/2,-1/2,1,1/4],`

`    [-1/2,-1/2,1/4,1]]`.

The exact co-Choi form is

`S4=[[0,-1/12,u,u],`

`    [-1/12,0,v,v],`

`    [u,v,0,-L/8],`

`    [u,v,-L/8,0]]`,

where `u=1/(4c)`, `v=s/(4c)`, `u+v=1/6`.

For a direct physical reconstruction, every Bell contraction between positive and negative indices vanishes on these four distinct-label vectors. The two negative matrix-unit terms give the F_13 and F_24 edges with coefficients u or v. The negative/eta and eta/eta terms give `-L F_13F_24/8`. The full inverse correction is zero on the two mixed-input patterns; on P1,P2 it has off-diagonal `-delta^2`, so the full corrected edge is

`-L/8+r delta^2=-1/12`.

This explains the constant edge and retains the inverse correction's sign.

The P3-P4 direction decouples and is strictly positive for both signs. On the remaining three dimensions use Z=(P3+P4)/sqrt(2).

For C4-S4, the upper2x2 block is `[[1,1/3],[1/3,1]]`; its Schur subtraction from the Z diagonal is `17/16-6uv`. The final scalar is

`5/4+L/8-(17/16-6uv)=3/16+L/8+6uv>0`.

For C4+S4 the upper block is `[[1,1/6],[1/6,1]]`. The coupling sum is5/6 and its difference has absolute value at most1/6, so the Schur subtraction is at most

`(6/7)*(25/36)+(6/5)*(1/36)=22/35`.

Its Z diagonal is at least9/8. Thus the final scalar is at least `139/280>0`. This proves **both symmetric signs**, and hence the asymmetric signs, on all36 dimensions at every angle.

## 5. Complete seven-dimensional adjoint-A matrix from the physical maps

Let X=E_01. In the all-A pattern define

`P=X_12 Omega_A,34`, `Q=Omega_A,12 X_34`, `R=X_14 Omega_A,32`.

The fourth contraction `Omega_A,14 X_32` equals P+Q-R in dimension2. Their Gram matrix is

`[[2,0,1],[0,2,1],[1,1,2]]`.

The four mixed patterns are

`B1=X_12 Omega_B,34`, `B2=Omega_B,12 X_34`,

`B3=X_14 Omega_B,32`, `B4=Omega_B,14 X_32`.

Each has norm squared2, and they are mutually orthogonal and orthogonal to the all-A pattern. The three all-A vectors and four mixed vectors are the complete seven-dimensional highest-weight space. One can see completeness directly: the all-A weight-one space has four coordinate states, of which one belongs to spin two, leaving three adjoint highest weights; each mixed pattern supplies one more. Their group orbits give exactly21 dimensions.

For a concise physical table put

`theta=4r delta=(s-1)/[3(1+s)]`,

`B0=k/2-1/(2c)+1/12`, `E0=(3l-k)/4`.

The C_B form on(P,Q,R) is

`[[1,-1/2,1/4],[-1/2,1,1/4],[1/4,1/4,1]]`;

on(B1,B2,B3,B4) it is

`[[2,1/2,-1,-1],[1/2,2,-1,-1],[-1,-1,2,1/2],[-1,-1,1/2,2]]`.

Its cross block is zero by group pattern. The full S_eta form on(P,Q,R) is

`[[k,2B0-k,B0],[2B0-k,k,B0],[B0,B0,B0-1/12]]`.

On the four mixed patterns it is

`[[0,1/2-1/c,1/(2c),1/(2c)],`

` [1/2-1/c,4s k,-3s/(2c),-3s/(2c)],`

` [1/(2c),-3s/(2c),0,E0],`

` [1/(2c),-3s/(2c),E0,0]]`.

The entire3x4 cross block is

`[[0,-t/c,t/(2c),t/(2c)],`

` [t/c,2t k,-3t/(2c),-3t/(2c)],`

` [t/(2c),t*(k-1/(2c)),-t/c,0]]`.

These are form matrices, including the full inverse term.

### Raw derivation and a constant cancellation

The universal vector formula is

`L_rs†|uv>=delta_(rs)c_r|uv>-(c_s/2)delta_(ru)|sv>-(c_r/2)delta_(sv)|ur>+(1/4)delta_(ru)delta_(sv)eta`.

For the all-A block its D^-1 part is k times the following dimension-two raw form, plus l/8 times the input/output swap form:

`H2=[[1,-3/4,1/8],[-3/4,1,1/8],[1/8,1/8,0]]`,

`F2=[[0,2,1],[2,0,1],[1,1,0]]`.

They follow by substituting the two coordinate terms of P,Q,R in the displayed vector formula. The restricted rank-one map has `V_AA=delta I+k|Omega_A><Omega_A|`. With `u0=3k+l`, its co-Choi form is

`[[0,delta u0,delta u0/2],[delta u0,0,delta u0/2],[delta u0/2,delta u0/2,2delta k]]`.

Subtract r times this form. The identities `k(1+theta)=1/c`, `l(1-theta)=s/c`, and `theta k=1/c-k` give the all-A matrix above and the angle-independent last diagonal difference `-1/12` after the basis change below.

Representative mixed contractions expose the remaining entries: B1 has zero diagonal because `L_01†|bb>=0` for b in B; B2 has diagonal4s k because every BB input trace contributes tX; the corrected B1,B2 edge is `(3l-k)/4-r delta(k+3l)=1/2-1/c`; the B3,B4 edge has no mixed-input inverse correction and equals E0. In the cross block the D^-1 terms for P,B2 and Q,B1 acquire their respective rank-one corrections, giving `-t k(1+theta)=-t/c` and `(t/b)(1-theta)=t/c`. The displayed vector formula determines every other entry by the same two-label sums. No numerical interpolation or assumption of the desired kernel is used to obtain the table.

## 6. Exact2+5 split and both signs on the adjoint sector

Use normalized all-A directions

`U=(P+Q)/2`, `V=(P-Q)/2`, `W=R-(P+Q)/2`,

and normalized `Z_±=(B3±B4)/2`. U,V,W,Z_± all have norm1; B1,B2 retain norm squared2. The form splits into a2x2 block(W,Z_-) and a5x5 block(U,V,B1,B2,Z_+), with no coupling between them.

### 6.1 The2x2 block is even symmetrically dominated

On(W,Z_-),

`C2=(3/4)I`,

`S2=[[-1/12,-t/(2c)],[-t/(2c),(k-3l)/8]]`.

Since `|t/(2c)|<=1/6` and `(k-3l)/8` lies in[-3/8,1/8], the minus determinant is at least `71/144>0`; the plus determinant is at least `2/9>0`, with positive diagonals. This closes both symmetric signs on the two multiplicity dimensions, hence six physical dimensions.

### 6.2 The5x5 form and its exact persistent kernel

Write `h=k+1/(2c)>0`, `j=k-1/(2c)=b/[3a(1+s)]>0`. In the order(U,V,B1,B2,Z_+),

`C5=diag(1/4,3/4) direct_sum [[2,1/2,-1],[1/2,2,-1],[-1,-1,5/4]]`,

and

`S5=[[B0,0,t/(2c),t j,-t/(2c)],`

`    [0,k-B0,-t/(2c),-t h,t/c],`

`    [t/(2c),-t/(2c),0,1/2-1/c,1/(2c)],`

`    [t j,-t h,1/2-1/c,4s k,-3s/(2c)],`

`    [-t/(2c),t/c,1/(2c),-3s/(2c),E0/2]]`.

The persistent kernel is `K=U-V+t B2=eta_input tensor X_output`. It can also be checked directly in every row of this full table.

### 6.3 Upper bound by a complete square and one positive2x2 remainder

For arbitrary complex coefficients on the five vectors, introduce the linear combinations

`X0=t U-B2`, `Y0=t V+B2`.

In the C5-S5 form the entire(U,V,B2) principal form is exactly

`j|X0|^2+h|Y0|^2`.

The B1 couplings to(X0,Y0) are `(-1,1)/(2c)`, and the Z_+ couplings are `(1/(2c),-1/c)`. Completing these two squares leaves a2x2 remainder on(B1,Z_+). With

`D=b(4+5s)`

its entries are

`R11=2-2a/D`,

`R12=-1+3s/D`,

`R22=5/4+(k-3l)/8-a(4+3s)/[(1+s)D]`.

For all s>=0,

`R11>5/3`, since `3D*(R11-5/3)=2+2s+5s^2>0`.

Also `|R12|<=1`, because `0<=3s/D<=3/14<1`. Finally R22>3/4: after multiplying R22-3/4 by its positive denominator `4ab(1+s)(4+5s)`, the numerator is

`4+5s-2s^2+6s^3+5s^4`

`=(s^2-1)^2+4s^4+6s^3+5s+3>0`.

Hence `det R>1/4`, so R is positive definite. This proves C5-S5>=0 **also at t=0**, without dividing by t. For t>0, vanishing of the two completed squares and of the positive remainder forces B1=Z_+=0, X0=Y0=0, leaving precisely span K. The t=0 upper kernel is larger here and is intentionally not conflated with the full-rank kernel statement.

### 6.4 The asymmetric lower bound from a uniform generalized trace

This step uses the just-proved upper positivity, not an unproved symmetric plus inequality. The inverse of C5 has first diagonal entries4,4/3 and mixed block

`[[8/9,2/9,8/9],[2/9,8/9,8/9],[8/9,8/9,20/9]]`.

Direct multiplication with the displayed S5 gives the exact trace identity

`Tr(C5^-1 S5)=[4+(11/2)k+(15/2)l+32/(3(1+s))]/9`.

This generalized trace is unchanged by the nonorthogonal form basis; no Gram matrix is being omitted from an ordinary action trace.

The trace is uniformly at least131/126. For s>=5 use `l>=5/7`. For0<=s<=5 use `k+l>=2/3` and `32/[3(1+s)]>=16/9`, giving the stronger bound85/81. Thus

`Tr(C5^-1 S5)>=131/126>1`.

The Hermitian matrix

`D5=C5^-1/2(C5-S5)C5^-1/2`

is positive semidefinite and has dimension5. Therefore every eigenvalue is at most its trace, which is at most `5-131/126=499/126`. It follows that

`C5^-1/2(3C5+S5)C5^-1/2=4I-D5>=(5/126)I`.

In particular3C5+S5 is strictly positive for every angle. This is the decisive use of the **asymmetric** criterion; no symmetric-GS statement for this5x5 block is needed.

Sections6.1-6.4 close the entire21-dimensional adjoint-A sector. Group interchange sends the adjoint-B sector to the adjoint-A calculation at1/t, with a harmless scalar change of reference. The bounds prove all t>0; continuity, including the uniform relative lower bound just obtained, supplies t=0. This closes the other21 dimensions.

## 7. Assembly and the W4 switched-complement bridge

The sector dimensions sum to256 and each decomposition is reducing by the displayed group representation and raw matrices. Checkpoint007 closes160 nonzero-charge dimensions plus fixed8. Section3 closes10, Section4 closes36, and Sections5-6 close42. Therefore both full asymmetric inequalities in Theorem A hold. For t>0 the upper kernels have dimensions8 from nonzero charges,2 from fixed8, and6 from the two adjoint blocks: total16. The explicit reference identity already places `eta_input tensor B_output` in the kernel, so this is exactly the asserted kernel, with no uncounted mode.

For clarity the sharp sufficient bridge is repeated. For the first-site reference |0>, let C0,S0 be the one-site co-Choi pair. On each span{|0a>,|a0>},

`C0=[[1,-1/2],[-1/2,1]]`, `S0=[[1,-1/2],[-1/2,0]]`.

Its generalized eigenvalues are1 and-1/3. On |00> the eigenvalue is1; on the symmetric/antisymmetric Q tensor Q sectors they are again1 and-1/3. Hence `T0=C0^-1/2 S0 C0^-1/2` has exactly that spectrum when dim H1>=2; only1 occurs for dim H1=1.

For `T_B=C_B^-1/2 S_eta C_B^-1/2`, Theorem A places its spectrum in[-3,1]. Consequently

`I-T0 tensor T_B>=0`.

Positive congruence says the switched-complement map `Lambda_1 tensor B-M0 tensor M_eta` is completely copositive, hence positive. This is a sufficient map property; it is not asserted necessary for W4.

If the range of a rank<=2 C contains `u=|0> tensor eta`, write `C=|u><v|+|x><y|`. Expanding the local swaps gives

`q3(C)=<v,Av>+<y,Dy>+2 Re<y,Lv>`

and the correctly oriented square completion

`q3(C)=||A^(1/2)(v+A^-1 L†y)||^2+<y,(D-L A^-1 L†)y>`.

The factored reference inverse makes the last switched complement exactly the positive map above evaluated on|x><x|. Both terms are nonnegative. Local-unitary covariance and adjoint invariance give all transports stated in Theorem B. The other ray is never assumed factorizable, and no rank-under-partial-trace shortcut is used.

## 8. Scientific delta, acceptance and remaining problem

At t=1 the candidate contains the earlier maximally entangled reference result; that point is not a new discovery. The new relative-to-local-baseline coverage is the entire two-equal-pairs family, including ratios where C_B+S_eta has an exact negative co-Choi form. For example the earlier eta=(1,1,1/4,1/4) symmetric obstruction does not obstruct this asymmetric sufficient route. No negative rank-two Werner witness is produced or reinterpreted.

This is a complete **written candidate** for the stated reference class and its rank-two consequence. It awaits a distinct full raw-matrix/proof reconstruction and parent disposition. The immutable checkpoints are a dependency closure, not seven independent accepted results. No human review, kernel proof, independent-model review or new exact computation is claimed.

Novelty remains **UNCLEARED**. The frozen selection's Wu-Zou, Ulam, EulerSolve/openai/math and qutrit-claim boundaries must be compared against this exact new reference class before any priority/publication assertion. The full64x64 rank<=2 W4 target, all-copy NPT bound entanglement, and the full book article remain open in this dossier. New candidate generation should pause for reconstruction of this complete packet rather than accumulating unchecked corollaries.
