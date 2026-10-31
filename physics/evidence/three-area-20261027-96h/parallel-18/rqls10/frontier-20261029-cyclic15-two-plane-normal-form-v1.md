# A two-plane normal form for the remaining cyclic 6D problem

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 03:01:59 PDT 2026. This is a reduction of the *cyclic-equivariant* G6 problem to finite spectra and continuous low-dimensional equations, not an existence or universal no-go result.

## Gauge and three population variables

Use the cyclic hypotheses and simple-spectrum/full-v5-support conclusion in `frontier-20261029-cyclic15-no-five-spectral-support-v1.md` SHA-256 `595b702ae059ef2d94e7f98cf3d111ede1dd134f39a6daced541cd4cc50d75cc`. Rephase U so `U^15=I`, put its six distinct eigenvalues `lambda_j=zeta_15^(a_j)`, and use a diagonal unitary commuting with U to make the six v5 coordinates `sqrt(p_j)>0`. Because `v5 ⟂ U^(-5)v5`,

`sum_(j:a_j≡r mod 3) p_j = 1/3` for r=0,1,2.

The six populations therefore have three independent real degrees of freedom. No rationality or other field condition is assumed.

Let `c=v5`, `Q=U^(-5)`, `A=U^(-2)`, and let `K=span{c,Qc}^perp`, a 4D space. The four other basis rays are `x=v2`, `Ax`, `y=v7`, and `AQy`. Necessarily

`x ∈ L := K ∩ A^(-1)K`, and `y ∈ M := K ∩ (AQ)^(-1)K`.

## Both L and M have dimension exactly two

For d=2 or 7, the defining four rows of the intersection, after removing the invertible diagonal factor `diag(sqrt(p_j))`, are

`(1)`, `(lambda_j^5)`, `(lambda_j^(-d))`, `(lambda_j^(5-d))`.

They have row rank 4 for **every** six distinct 15th-root eigenvalues meeting all three U^5 classes. To see this, suppose a relation

`a+b lambda^5+c lambda^(-d)+e lambda^(5-d)=0`

holds at all six roots. Within a fixed U^5 class q it is `(a+bq)+(c+eq) lambda^(-d)=0`. Since d=2,7 is coprime to 15, the lambda^(-d) values are distinct. Any class containing at least two roots forces both coefficients to zero. If two classes do, all a,b,c,e vanish. Otherwise the multiplicities are `(4,1,1)`; the two singleton roots in the other classes give two distinct equations `b+e lambda^(-d)=0`, again forcing b=e=0 and then a=c=0. Thus `dim(L)=dim(M)=2` without a numerical rank assumption.

## Explicit remaining equations

Take any basis matrices `B_L,B_M` of L,M and write `x=B_L z`, `y=B_M w`, with projective coordinates z,w∈CP1. Cross-orthogonality of the four rays is exactly

`z† C_i w=0`, i=0,1,2,3,

with `C_i=B_L† U^(e_i) B_M` and exponents `e=(0,-7,2,-5)`. In addition the paired rays must satisfy

`z† B_L† U^(-2) B_L z=0`,

`w† B_M† U^(-7) B_M w=0`.

Normalization of x,y can be imposed afterwards. Thus, for each of the 78 residual spectral classes in `frontier-20261029-cyclic15-78-residual-spectra-v1.md` SHA-256 `d709af376455f106e4312f56a29b54b1a6d15ccf025aa85d01f76f337de692b2`, the unresolved problem has three real positive population variables and two complex projective line variables, with the explicit two self-orthogonality and four cross-orthogonality equations above.

In particular, a necessary condition is that the four 2×2 matrices C_i fail to span the full 4D complex matrix space: otherwise a nonzero bilinear functional `C -> z†Cw` cannot vanish on all four. This condition is not sufficient; a vanishing determinant does not provide suitable z,w, let alone a full QLS10.

The rank proof, imported simple-spectrum result and all Gram-equation callers require independent written review. Symmetry-breaking 6D complements and the remaining 25 QLS cells are not addressed; no formal-kernel or novelty claim is made.
