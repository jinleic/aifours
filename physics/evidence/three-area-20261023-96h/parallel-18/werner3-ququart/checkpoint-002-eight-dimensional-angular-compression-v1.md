# Checkpoint 002 — the full invariant angular block reduces to two explicit five-dimensional forms

Before-creation clock observed: **2026-10-23T14:14:56-07:00**. Owner: physics-1 / PhysicsResearch96h. Status: **CANDIDATE written matrix identities**, pending distinct reconstruction. No scientific program, symbolic engine or new executable replay has been used. The main W4 target and all other slots are unchanged.

## 1. Delivered representation and exact limit

For `eta_t=Omega_A+t Omega_B`, with `Omega_A=|00>+|11>`, `Omega_B=|22>+|33>`, t>0, this checkpoint reconstructs **every entry of the full eight-dimensional fixed subspace** of the correlated U(2)×U(2) action. On that subspace, symmetric co-Choi domination is equivalent to two explicit5×5 rational matrix inequalities. The exact reference zero modes and the positive remaining scalar are separated, rather than perturbed or dropped.

This is not yet a full256-dimensional GS characterization: the nontrivial representation sectors outside this fixed subspace still require their own proof. It does improve the next obligation from unspecified eight-way contractions to fully displayed matrices suitable for written Schur/determinant analysis. The stronger principal quartic of checkpoint001 is recovered as a submatrix test, not assumed sufficient.

## 2. Parameters and the full reference inverse

Let s=t^2, and define

`a=1+2s`, `b=2+s`, `c=3(1+s)/2`,

`k=1/a`, `l=s/b`, `r=1/[4+2(k+l)]`,

`u=3k+l`, `v=k+3l`,

`g=-2t/(1+s)`, `h=3(k+l)/2`.

The symbol r here is an inverse coefficient, not a Schmidt rank or a switch mass. All parameters are explicit rational functions of t. Useful exact identities are

`k+l+3kl=1`, `0<k+l<=1`, `g^2=8kl/(1-kl)`.

For eta=(1,1,t,t), its compression is `A_eta=D+|eta><eta|/4`. The diagonal D equals a on A⊗A, b on B⊗B and c on mixed-group pairs. With H=D^-1 eta,

`A_eta^-1=D^-1-r|H><H|`, `||eta||^2=2+2s`, `<eta,H>=2(k+l)`.

Every coefficient below retains this full inverse. No unsupported rank truncation occurs.

## 3. The complete fixed subspace and its basis

On the first physical ququart, act by U_A⊕U_B; on the second act by its coefficientwise conjugate. The reference eta is invariant. Covariance gives the same paired action on co-Choi input/output slots, so C_B and S_eta preserve the fixed subspace and its orthogonal complement.

There are two invariant contractions when all four slots are in A, two when all are in B, and one in each of four balanced mixed-group patterns. Unbalanced patterns cannot be invariant because independent central phases of U_A,U_B would act nontrivially. The two-contraction fact for a two-dimensional group is elementary: an operator commuting with every U⊗U is, by diagonal-phase and permutation symmetry, diagonal on |00>,|11> with one common value and of the form [[b,c],[c,b]] on |01>,|10>. Commuting with a Hadamard rotation forces the first value to be b+c. Thus the commutant is span{I,F}, giving exactly the two pairings. This proves the dimension eight, not merely the existence of eight invariant vectors.

Use the following eight vectors, with four slots grouped input12/output34:

`p_A=Omega_A,12 Omega_A,34`, `q_A=Omega_A,14 Omega_A,32`,

`p_B=Omega_B,12 Omega_B,34`, `q_B=Omega_B,14 Omega_B,32`,

`p_AB=Omega_A,12 Omega_B,34`, `p_BA=Omega_B,12 Omega_A,34`,

`q_AB=Omega_A,14 Omega_B,32`, `q_BA=Omega_B,14 Omega_A,32`.

All have squared norm four. The only nonzero overlaps between distinct displayed vectors are `<p_A,q_A>=<p_B,q_B>=2`; all mixed patterns are mutually orthogonal and orthogonal to the two all-group blocks. Hence they form a genuine basis. Matrix entries below are **quadratic-form entries**, not uncorrected action matrices in this nonorthogonal basis.

## 4. Raw S entries before eliminating the known reference kernel

It suffices first to compute S on

`Z=(p_A,p_B,q_A,q_B,q_AB,q_BA)`.

The four entries involving p_AB,p_BA will then be recovered by an exact reference-kernel identity, not an unsupported zero-mode assumption.

The following table gives `S_entry = D_inverse_part - r·rank_one_part`. Entries are real; symmetric counterparts are understood.

| Entry | D-inverse contribution | Rank-one contribution |
|---|---|---|
| p_A,p_A | `(9k+l)/2` | `u^2` |
| p_B,p_B | `(k+9l)/2` | `v^2` |
| p_A,p_B | 0 | `16kl` |
| p_A,q_A | `(-3k+l)/4` | `u^2/2` |
| p_B,q_B | `(k-3l)/4` | `v^2/2` |
| p_A,q_B and p_B,q_A | 0 | `8kl` |
| q_A,q_A | `(-3k+l)/2` | `3k^2+l^2` |
| q_B,q_B | `(k-3l)/2` | `k^2+3l^2` |
| q_A,q_B | 0 | `4kl` |
| p_A,q_AB and p_A,q_BA | g | 0 |
| p_B,q_AB and p_B,q_BA | g | 0 |
| q_A,q_AB; q_A,q_BA; q_B,q_AB; q_B,q_BA | 0 | 0 |
| q_AB,q_AB and q_BA,q_BA | 0 | 0 |
| q_AB,q_BA | h | 0 |

### Raw reconstruction of the table

For coefficients c_i equal to1 in A and t in B,

`L_ab=delta_(ab)c_a I-[c_b E_ab⊗I+c_a I⊗E_ba]/2+|ab><eta|/4`.

The entry convention is `<L_j†p,A_eta^-1 L_i†q>`. The all-A p/q entries reduce to the previously retained full-inverse contractions with `z=2(k+l)`; group interchange gives the all-B ones. Their listed D and rank-one parts are the same identities, not interpolation from parameter values.

For an independent rank-one calculation define V by columns `V|i>=L_i H`. Since c_a H_a is k in A and l in B,

`L_ab H=delta_(ab)c_a H+[<eta,H>/4-(c_a H_a+c_b H_b)/2]|ab>`.

The square bracket is `(l-k)/2` on A⊗A, `(k-l)/2` on B⊗B and **zero on mixed input pairs**. Thus the inverse correction has no q_AB/q_BA row. On the normalized Omega_A/Omega_B directions, V has matrix

`[[u/2,2t/a],[2t/b,v/2]]`.

On the three-dimensional orthogonal part of A⊗A it is `(l-k)I/2`, and on the corresponding B⊗B part its negative. For real coefficient matrices R_X of the displayed vectors, the rank-one co-Choi bilinear is `tr(R_X V R_Y V)`. This gives all rank-one entries in the table; e.g. p_A,p_B gives16kl, and q_A,q_A gives `u^2/4+3(k-l)^2/4=3k^2+l^2`.

For mixed entries, `p_A,q_AB` uses four mixed D-inverse contractions, each contributing -3t/4 before multiplication by1/c, giving `-3t/c=g`. The q_A,q_AB terms split into -2t/c and +2t/c and cancel. The q_AB diagonal contractions vanish. For q_AB,q_BA, the two single-matching-index classes contribute k and l; the double-matching class contributes k/2+l/2, while its H projection vanishes. Their sum is h=3(k+l)/2. These counts use two labels in each group and the full mixed inverse1/c.

This reconstructs every independent table entry from the physical map; the remaining eight-dimensional entries are fixed below by exact algebra.

## 5. Reference kernel and a complete eight-dimensional basis change

For this real eta, and in fact for every complex reference, linearity and adjoint preservation give

`Σ_i eta_i L_i=A_eta`,

`S_eta(eta⊗z)=Σ_j|j>⊗L_j†z=C_B(eta⊗z)`.

This five-line contraction is used locally here as an explicitly proved identity. It does not promote the separate pending quantitative open-region packet.

Consequently D_eta=C_B-S_eta annihilates

`K_A=p_A+t p_BA=eta_input⊗Omega_A,output`,

`K_B=p_AB+t p_B=eta_input⊗Omega_B,output`.

D_eta is Hermitian, so their cross-form entries with every vector also vanish. For t>0,

`p_BA=(K_A-p_A)/t`, `p_AB=K_B-t p_B`.

Thus `(K_A,K_B,Z)` is an invertible basis change of the entire eight-dimensional fixed space. No other vector or coupling is omitted. It follows that the full minus form has a2×2 zero block and the explicitly computed form on Z.

## 6. Positive scalar split and the two five-dimensional criteria

Physical interchange of the two ququart factors exchanges q_AB and q_BA and fixes the other relevant vectors. Set

`z_plus=q_AB+q_BA`, `z_minus=q_AB-q_BA`.

The z_minus direction is completely decoupled. Its minus/plus quadratic values are respectively `6+2h` and `6-2h`, both positive because `k+l<=1` implies h<=3/2. This split is exact, not an approximate parity guess.

Use the remaining five-vector basis

`Z5=(p_A,p_B,q_A,q_B,z_plus)`.

The C_B form is

`C5=[[3,0,-3/2,0,0],`

`    [0,3,0,-3/2,0],`

`    [-3/2,0,3,0,0],`

`    [0,-3/2,0,3,0],`

`    [0,0,0,0,10]]`.

The complete S_eta form is the symmetric matrix

`S5_11=(9k+l)/2-r u^2`,

`S5_22=(k+9l)/2-r v^2`,

`S5_12=-16rkl`,

`S5_13=(-3k+l)/4-r u^2/2`,

`S5_24=(k-3l)/4-r v^2/2`,

`S5_14=S5_23=-8rkl`,

`S5_33=(-3k+l)/2-r(3k^2+l^2)`,

`S5_44=(k-3l)/2-r(k^2+3l^2)`,

`S5_34=-4rkl`,

`S5_15=S5_25=2g`, `S5_35=S5_45=0`, `S5_55=2h`.

These entries specify every element of S5, not a partially defined matrix.

The C_B form on `(K_A,K_B)` and its cross-form to Z5 are

`K2=[[3+4s,t],[t,4+3s]]`,

`R=[[3,0,-3/2,0,-4t],`

`   [0,3t,0,-3t/2,-4]]`.

The determinant of K2 is exactly `12(1+s)^2>0`, and its leading diagonal is positive. As an independent compression check, K2 is the A_eta form on outputOmega_A,Omega_B, giving diagonals3+4s,4+3s and cross t directly.

In the `(K_A,K_B,Z5)` basis,

`Form(C_B-S_eta) = 0_2 direct_sum (C5-S5)`,

while `C_B+S_eta=2C_B-(C_B-S_eta)` has upper block2K2, cross block2R and lower blockC5+S5. Its Schur complement is therefore

`C5+S5-2R^T K2^-1 R`.

**Exact invariant-sector criterion:** on the full eight-dimensional fixed space, symmetric GS holds if and only if BOTH

**`M_minus(t)=C5-S5>=0`,**

**`M_plus(t)=C5+S5-2R^T K2^-1R>=0`.**

The eliminated z_minus scalar is already positive and the K2 block is positive definite. These are exact rational matrix functions for every t>0. Treating C5+S5 alone as sufficient would be wrong: it would omit the two reference-direction couplings captured by the Schur term.

## 7. Checks, obstruction and the next one-problem action

The p_A,q_A principal submatrix of the full plus form recovers checkpoint001's explicit polynomial matrix and its necessary quartic. The positive uniform point t=1 is consistent with the already written-checked full GS4 theorem, but this is a consistency boundary, not a substitute for checking the new formulas independently.

For further simplification, p=kl satisfies `0<p<=1/9`, `k+l=1-3p`, `(k-l)^2=(1-p)(1-9p)` and `g^2=8p/(1-p)`. The two-to-one t↔1/t group interchange is explicit, so parameter reduction does not discard an angular branch. These identities may reduce the determinant factorization to polynomials in one symmetry parameter without running an unadmitted symbolic engine.

The exact remaining blockers are:

1. resolve the signs of these five-dimensional forms over the full parameter interval, rather than over selected t;
2. reconstruct all nontrivial U(2)×U(2) representation sectors in the remaining248-dimensional complement before calling any resulting interval a **full** GS criterion;
3. keep the co-Choi conclusion separate from unrestricted W4 and from rank-two negative witnesses.

This is one continuing angular obligation in physics-1, not another problem slot or an independent-discovery count. Legacy evidence and all sibling write roots remain unchanged; no new scientific GO has been used.
