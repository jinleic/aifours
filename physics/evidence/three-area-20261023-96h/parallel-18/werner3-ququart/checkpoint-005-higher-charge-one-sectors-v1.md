# Checkpoint 005 — both signs have a uniform gap on the 64 higher charge-one dimensions

Before-creation clock observed: **2026-10-23T14:36:37-07:00**. Owner: physics-1 / PhysicsResearch96h. Status: **CANDIDATE written proof**, pending distinct reconstruction. No scientific program or new GO was used. This continues the same two-pair angular obligation, not a new problem slot.

## 1. Exact scope

For `eta_t=Omega_A+t Omega_B`, A={0,1}, B={2,3}, t>=0, there is an explicitly defined reducing subspace of dimension64, contained in central charges+1 and-1, on which

`C_B-S_eta >= I/12`,

`C_B+S_eta >= I/4`.

These are full operator inequalities on those64 dimensions for every t, not compressions at selected angles. Together with checkpoint004's32 extremal-charge dimensions, this removes96 dimensions from the possible angular obstruction. The remaining160 dimensions include the eight-dimensional fixed block. Its minus sign was closed in checkpoint003; its plus sign and the remaining152 nontrivial-complement dimensions are not closed by this result.

The unrestricted W4 rank-two inequality remains open. All new sector results retain CANDIDATE labels until actually reconstructed; they are not independent-discovery counts.

## 2. A concrete half of charge+1

Positive slots are1,3; negative slots are2,4. First take the32-dimensional part of charge+1 with exactly one A label in the positive slots and none in the negative slots. Use two orientations, with alpha in A and j,k,l in B:

`X_(alpha;j,k,l)=|alpha,j,k,l>`,

`Y_(alpha;j,k,l)=|k,j,alpha,l>`.

The common internal B triple is `B_positive tensor conjugate(B)_negative tensor conjugate(B)_negative`, with coordinates(j,k,l). Define two equivariant contraction embeddings from one negative B factor:

`U1(v)=sum_a |j=a,k=a,l=v>`,

`U2(v)=sum_a |j=v,k=a,l=a>`.

Their Gram blocks are

`U1†U1=U2†U2=2I`, `U1†U2=U2†U1=I`.

Hence their joint range has dimension4 and its orthogonal complement

`H_B=ker(U1†) intersect ker(U2†)`

has dimension4. Let T interchange the negative indices j,l. Then `T U1=U2`, `T U2=U1`, so H_B is T-invariant. In fact **T=+I on H_B**. To see this without assuming a spin decomposition, the entire T=-1 subspace has dimension `2 times dim wedge^2(conjugate B)=2`. The image of U1-U2 lies in it, has dimension2 because `(U1-U2)†(U1-U2)=2I`, and therefore exhausts it. H_B is orthogonal to that image and has no T=-1 part.

The subspace with alpha arbitrary, internal triple in H_B and both orientations therefore has dimension `2 times4 times2=16`.

## 3. Why the 16-dimensional subspace reduces the full operator

Covariance under `U_A direct_sum U_B`, with conjugate action on negative slots, preserves central charge. Within the displayed32-dimensional pattern, the raw formulas in Section4 preserve H_B exactly.

The other pattern of charge+1 has two positive A labels and one negative A label. Its B component is only a single negative B factor. Any U(2)_B-equivariant map from the internal B triple to that factor is a linear combination of U1† and U2†. Indeed, turning the dual legs identifies this intertwiner space with the commutant of `U tensor U` on `B tensor B`; the elementary two-label proof in checkpoint002 gives precisely span{I,F}, whose two contractions are U1† and U2†. Such a map annihilates H_B. Thus there is **no coupling** from this16-dimensional subspace into the other charge+1 pattern. Hermiticity excludes the reverse coupling too.

This proves a reducing subspace, not just positivity of one principal compression. It does not need an unproved assertion that all nontrivial representation sectors are positive.

## 4. Raw physical co-Choi calculation

Set s=t^2, `b=2+s`, `c=3(1+s)/2`, `l=s/b`. The exact physical maps are

`L_ab=delta_(ab)c_a I-[c_b E_ab tensor I+c_a I tensor E_ba]/2+|ab><eta|/4`,

where c_a is1 on A and t on B. The full inverse is `A_eta^-1=D^-1-r|H><H|`, as in checkpoints002/004.

The rank-one inverse correction vanishes on every nonzero-charge sector: its columns are L_i H, which vanish on mixed input i, and otherwise have support only on A tensor A or B tensor B. Consequently its co-Choi entries have both input and output pure-group pairs and central charge zero. This is an exact support statement, not an inverse truncation.

On the B internal triple put

`P1=U1 U1†`, `K12=U1 U2†`, `K21=U2 U1†`.

The full D-inverse calculation on the two orientations gives the operator blocks

`S_XX=T/(4c)`,

`S_YY=(s/c)[P1-(K12+K21)/2+T/4]`,

`S_XY=S_YX=(s/(4b))[I-2P1+K12+K21-T]`.

The external alpha index is the identity. The formulas include the eta contributions; none is omitted.

For direct index reconstruction, let the column's internal indices be(n,m,o), and its external A index beta. The first two blocks follow from

`L_(beta,n)†|k,l>=-(1/2)delta_(nl)|k,beta>` when beta is in A and k,l,n in B,

and

`L_(m,n)†|alpha,l>=t[delta_(mn)|alpha,l>-(1/2)delta_(nl)|alpha,m>]`.

Their reversed contractions produce respectively T/(4c) and the four terms `P1,-K12/2,-K21/2,T/4`.

For the mixed orientation use instead

`L_(m,n)†|k,l>=t delta_(mn)|k,l>-(t/2)delta_(mk)|n,l>-(t/2)delta_(nl)|k,m>+(1/4)delta_(mk)delta_(nl)eta`,

`L_(alpha,j)†|beta,o>=-(t/2)delta_(alpha,beta)|j,o>-(1/2)delta_(jo)|beta,alpha>+(1/4)delta_(alpha,beta)delta_(jo)eta`.

The BB-versus-BB terms give `(s/b)[-P1/2+I/4+K12/4]`; the remaining BB-versus-eta term supplies `(s/b)K21/4`. The coefficient multiplying the double matching `delta_(jo)delta_(mk)delta_(nl)` is

`-l/4-l/8-k/8+(k+l)/8=-l/4`,

using the eta-eta contraction `<eta,D^-1eta>=2(k+l)`. This is the final `-(s/(4b))T` term. It shows explicitly why keeping the full eta contraction matters.

## 5. Reduction on H_B and the two signs

On H_B, `P1=K12=K21=0` and T=I. Hence

`S_eta|_(H_B orientations)=(1/(4c)) diag(1,s)`.

Let J swap X,Y. The two physical swaps act as J and T, so

`C_B=(I-J/2)(I-T/2)=(1/2)[[1,-1/2],[-1/2,1]]`

on this subspace, tensored with the identity on alpha and H_B. Thus `C_B>=I/4`. Since S_eta is positive semidefinite here, the plus sign is at least I/4.

For the minus sign, the diagonal entries are

`1/2-1/[6(1+s)]`, `1/2-s/[6(1+s)]`,

both at least1/3, and the only off-diagonal entry is-1/4. For arbitrary complex x,y,

`a|x|^2+b|y|^2-(1/2)Re(conjugate(x)y)`

`>= (a-1/4)|x|^2+(b-1/4)|y|^2`

`>= (|x|^2+|y|^2)/12`.

This proves the two asserted uniform gaps on the full16-dimensional higher-B part of charge+1.

## 6. The other 48 dimensions and rank-boundary endpoint

For t>0, interchange A and B and then interchange the two physical factors. This maps the preceding pattern to the other pattern of charge+1. The transformed reference is a nonzero scalar multiple of eta_(1/t). Scalar multiplication of the reference leaves S_eta unchanged, and the bounds above hold for every positive parameter. This gives another16-dimensional reducing subspace, the higher-A part.

Physical factor interchange alone maps charge+1 to charge-1 and leaves the symmetric diagonal reference eta_t unchanged. It supplies the corresponding two16-dimensional subspaces in charge-1. They are orthogonal by charge or inequivalent group pattern. Total dimension is64.

At t=0 the inverse still exists with the bound `A_eta>=||eta||^2 I/4`, and S_eta is continuous in the reference. The four group-defined higher subspaces do not depend on t. The same nonstrict uniform gap bounds therefore extend to t=0 by continuity; no singular 1/t substitution is applied at the endpoint itself.

The exact remaining task is the same single angular characterization: prove or refute the full plus/minus signs on the remaining160 dimensions, including the explicit fixed-sector plus Schur complement. The principal quartic of checkpoint001 is still only necessary. No negative rank-two Werner witness or full W4 theorem is claimed.
