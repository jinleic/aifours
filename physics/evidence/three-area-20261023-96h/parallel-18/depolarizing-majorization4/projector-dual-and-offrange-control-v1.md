# Exact U3 projector dual and an actual-projector off-range obstruction

Observed attempt/freeze clock: **2026-10-23T16:07:28-0700**. PhysicsDepol4. This is the parent's next bounded written attempt on the **same** low-noise physics-2 residual. No scientific executable, numerical eigenvalue calculation, code, solver, CLI or nested agent was used.

**Status:** the exact dual is derived, but equivalence alone is not scientific progress or acceptance. A concrete method obstruction below is proved for each required projector rank: compressing to Ran(P), or asserting an optimizer always lies there, is false. The actual uniform projector inequality is **not proved or refuted** here. The first unproved coupled-block step is frozen explicitly. Central/high-noise acceptance remains at the parent's named boundary; Zhang prior-claim ambiguity and NOVELTY_UNCLEAR remain mandatory.

## 1. Tensor placements and exact self-adjointness

The physical Hilbert space is `(C^2)_1 tensor (C^2)_2 tensor (C^2)_3 tensor (C^2)_4`, in that order. For an operator A define

`T_i(A)=Insert_i[I_2 tensor Tr_i(A)]`,

where insertion puts the identity back on the physical qubit that was traced out, without reordering the other three qubits. Equivalently, in bit-string coordinates x,y,

`(T_i(A))_(x,y)=delta_(x_i,y_i) sum_(b=0,1) A_(x with bit i replaced by b, y with bit i replaced by b)`.

There is no factor 1/2: the identity and partial trace are unnormalized. Thus

`Phi_3(A)=sum_(i=1)^4 T_i(A)`, and `X_3(rho)=Phi_3(rho)`.

For arbitrary operators A,B, the partial-trace identity gives

`Tr[A T_i(B)]=Tr_(rest)[(Tr_i A)(Tr_i B)]=Tr[T_i(A) B]`.

Summing proves exact trace self-adjointness of Phi_3, including complex off-diagonal entries. If P>=0, then Phi_3(P)>=0; for a rank-k projector, `Tr Phi_3(P)=8k`.

For any state rho, the Ky-Fan variational formula uses actual rank-k **orthogonal** projectors:

`K_k(Phi_3(rho))=max_(P=P^dagger=P^2, Tr P=k) Tr[P Phi_3(rho)]`

`                =max_P Tr[rho Phi_3(P)]`.

Taking the maximum over states, the compact product domain allows exchanging the two maxima (there is no minimax interchange):

`max_rho K_k(Phi_3(rho))=max_P lambda_max(Phi_3(P))=max_P ||Phi_3(P)||_op`.

Therefore the missing sufficient U3 inequality is **exactly equivalent**, rank by rank, to

`Phi_3(P)<=(k+3)I_16` for EVERY complex rank-k orthogonal projector P, k=2,3,4.    (D)

Purity of a maximizing rho follows by choosing an eigenvector of Phi_3(P). This does **not** imply that eigenvector belongs to Ran(P). Section 3 gives exact countercontrols to that latter assertion.

## 2. Known normalization and sharpness controls

For the pure product input rho0=P_(0000), `Phi_3(rho0)` has spectrum `(4,1,1,1,1,0,...,0)` and trace eight, as required.

For each k=2,3,4, choose any k-1 distinct single-excitation strings e_j and the actual diagonal projector

`P_k^star=P_(0000)+sum_(j=1)^(k-1) P_(e_j)`.

Its diagonal under Phi_3 is the occupied-vertex value four plus the number of occupied one-bit neighbors, or only that neighbor count at an unoccupied vertex. At 0000 the value is `4+(k-1)=k+3`; at any chosen single-excitation vertex it is five, and at any other vertex it is at most k. Thus `||Phi_3(P_k^star)||=k+3`. The proposed universal constant cannot be lowered.

For a physical Bell-pair product `rho_Bell=P_(Phi+12) tensor P_(Phi+34)`, direct single-qubit tracing gives

`Phi_3(rho_Bell)=I_12 tensor P_(Phi+34)+P_(Phi+12) tensor I_34`,

with spectrum `(2,1 repeated6,0 repeated9)`. Its leading k sums at k2,3,4 are3,4,5, below5,6,7. This checks the normalization without importing any Werner/co-Choi candidate.

All subsequent projectors are in the original physical qubit coordinates, not arbitrary marginal tuples or a two-ququart Schmidt reduction.

## 3. A rank-k family where the maximizer is outside Ran(P)

Write `P_v=|v><v|` for a normalized vector. Define

`v0=|0000>`,

`v1=|1+00>=(|1000>+|1100>)/sqrt(2)`,

`xi1=|0010>`, `xi2=|0001>`.

These four vectors are pairwise orthonormal. For each k=2,3,4 put

`P_k=P_(v0)+P_(v1)+sum_(j=1)^(k-2) P_(xi_j)`.

Consequently `P_k=P_k^dagger=P_k^2`, `Tr P_k=k`, and every matrix entry is real rational. No projection feasibility is inferred from a relaxation.

**Claim.** For each of these three k,

`||P_k Phi_3(P_k) P_k||=k+5/2`,                                  (3a)

`||Phi_3(P_k)||=[k+4+sqrt((k+1)^2+1)]/2`,                          (3b)

and the quantity in (3b) is strictly between the compression norm and k+3. Every maximizing eigenvector lies outside Ran(P_k).

### 3.1 Exact block matrix before adding xi1,xi2

On physical qubits1,2 set

`A=P_(00)+P_(1+)`.

Then `P_2=A tensor P_(0)_3 tensor P_(0)_4`. Since

`Tr_1 A=P_(0)+P_(+)=[[3/2,1/2],[1/2,1/2]]`, `Tr_2 A=I_2`,

the sector where qubits3,4 are00 has the exact four-by-four block

`H=T_1^(12)(A)+T_2^(12)(A)+2A`

` =[[9/2,1/2,0,0],`

`   [1/2,3/2,0,0],`

`   [0,0,7/2,3/2],`

`   [0,0,3/2,5/2]]`                                               (4)

in the ordered 12 basis00,01,10,11. The 34 sectors10 and01 each have block A; sector11 is zero. These follow directly by inserting the erased qubit identity into the four terms of Phi_3, not by a numerical block diagonalization.

### 3.2 Effect of the additional actual projector vectors

Each `Phi_3(P_(xi_j))` is diagonal: it equals four on xi_j, one on each of its four one-bit neighbors, and zero elsewhere. In the 34=00 sector, its only contribution is one at12=00. Therefore the k-th main sector is

`H_k=H+(k-2)P_(00)`.

Its q1=0 block is

`[[k+5/2,1/2],[1/2,3/2]]`,

with eigenvalues

`[k+4 plus_or_minus sqrt((k+1)^2+1)]/2`.                           (5)

Its q1=1 block is unchanged, with eigenvalues `3 plus_or_minus sqrt(10)/2`.

For k=2 the other two sectors have norm one. For k=3,4 the sectors34=10 or01 have norm at most five: each contains A, of norm one, and at most one added diagonal single-product contribution, of norm at most four. The other added xi contributes zero on that sector. Sector34=11 has norm k-2, at most two. Since the upper eigenvalue in (5) is greater than k+5/2, it exceeds all those other-sector bounds for k=3,4. At k=2 it equals the upper eigenvalue of the unchanged q1=1 block and still exceeds the other sectors. This proves the full operator norm (3b).

### 3.3 Compression, strict discrepancy and no optimizer in the projector range

In the orthonormal range basis `(v0,v1,xi1,xi2)` truncated to k vectors, the compressed diagonal entries are respectively

`k+5/2`, `9/2`, and5 for each included xi_j.

The off-diagonal entries vanish: Phi_3(P_k) respects the 34 sectors and the q1 blocks of (4), and the added product terms are diagonal. Hence the compression norm is (3a).

Their difference is the exact positive number

`[sqrt((k+1)^2+1)-(k+1)]/2>0`.

For k=3,4 the maximal eigenspace is the upper eigenvector of (5); its 01 component is nonzero because the off-diagonal entry is1/2. Ran(P_k) in that q1=0,34=00 sector contains only00, so no maximizing vector is in Ran(P_k). At k=2 there are two maximal eigenvectors, one in each q1 block. The first has nonzero01 component and the second is not proportional to1+=(10+11)/sqrt(2), because its two diagonal entries differ. Their two-dimensional span has zero intersection with span(v0,v1). Thus no maximizing eigenvector is in Ran(P_2), either.

Finally,

`[k+4+sqrt((k+1)^2+1)]/2 < k+3`,

since `(k+1)^2+1 < (k+2)^2` for k=2,3,4. These are **not counterexamples to (D)**. They refute the universal method assertion that its largest eigenvalue can always be computed inside Ran(P), or that bounding only that compression proves (D).

## 4. Retaining the actual projector blocks: first unproved uniform step

For an arbitrary complex orthogonal rank-k P, let Q=I-P and write

`A=P Phi_3(P)P`, `B=P Phi_3(P)Q`, `C=Q Phi_3(P)Q`.

Here B^dagger, not an unconjugated transpose, is the opposite block. With c=k+3, the desired operator inequality is exactly

`[[cP-A,-B],[-B^dagger,cQ-C]]>=0`.                                (6)

The identity `P^2=P` is retained, and these are coupled blocks of one actual projector. No replacement by independently selected marginals has been made.

If `D=cQ-C` is positive definite on Ran(Q), (6) is equivalent to

`cP-A >=B D^(-1) B^dagger` on Ran(P).                             (7)

At a semidefinite endpoint, the exact version requires all three conditions:

1. D>=0;
2. `Ran(B^dagger) subset Ran(D)`;
3. `cP-A-B D^(+) B^dagger>=0`, with D^(+) its Moore–Penrose inverse on Ran(Q).

Neither a uniform proof of these conditions nor the preceding separate compression bounds for arbitrary P is supplied here. The first attempted shortcut—replacing (6) by the P-compression alone—is false by Section 3. After retaining B, the **first unproved algebraic obligation** is a genuine all-projector bound on its Schur correction together with the D/range conditions. Merely rewriting it as (6)/(7) is not progress or a certificate.

For the exact controls, B is already nonzero: its matrix entry from v0 to0100 is1/2 for all k. This is why it cannot be discarded on the basis of P^2=P or orthogonality. More detailed projector identities might still control the correction, but no such all-complex estimate is inferred from these controls.

## 5. Scope, imports and settlement of the bounded attempt

The exact dual covers every mixed or pure rho because it maximizes over all actual complex rank-k projectors and all states. The obstruction uses real rational projectors, a valid subclass for disproving a universal complex-projector shortcut. Product sharpness and Bell controls have been checked analytically in their physical tensor placements. The two-ququart Schmidt-spectrum shortcut from the preceding attempt is not revived, and the sibling Werner candidate is not imported.

This bounded attempt establishes an exact **method obstruction** at every required rank, not a negative answer to the original channel problem and not exhaustion of its full target. The missing uniform inequality remains `Phi_3(P)<=(k+3)I`. A different argument that uses the full P^2=P coupling may still prove it; a violation of this sufficient U3 route would still need the exact noise/projector eligibility test before becoming a channel counterexample.

No mathematical execution, formal/kernel verification, human or outside-model review occurred. The supplied proof is ready for a separate reconstruction if the parent considers this route qualification worth reviewing, but no new discovery, globally closed low-noise index or novelty claim is made.
