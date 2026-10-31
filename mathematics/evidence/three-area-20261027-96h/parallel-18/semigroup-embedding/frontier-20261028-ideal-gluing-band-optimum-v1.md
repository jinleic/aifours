# Exact band minima for glued semilattice ideals: an unbounded fibre-bound gap

**Status: NEW AUTHOR WRITTEN FAMILY with exact finite controls; UNREVIEWED / UNADOPTED.** This is a general family of simple positive original-class examples, not a proof for arbitrary weakly-E locally-r semigroups. Unlike the general finest-actor theorem, the all-actor lower bound below is proved directly, with no actor-transport import.

## 1. Source family and exact result

Let L be a finite meet semilattice, and let `A_i` for i in a finite nonempty index set I be nonempty lower ideals of L. Put `U=⋃_(i∈I) A_i`, a meet subsemilattice, and define

`S={ (i,x): i∈I, x∈A_i }`,
`(i,x)(j,y)=(i,x∧y)`.

The multiplication is well-defined because x∧y lies below x and hence in A_i; associativity is inherited from the product of the left-zero band I and L. S is a globally regular band, hence regular, weakly E-unitary, locally r-orthodox and seminormal. The exact minimum cardinality of the band factor of any faithful physical band-by-CS host of S, over **all** CS actors and all bands, is

`min |B| = |U|`.                                           (1)

A semilattice band U and a left-zero actor I achieve the bound via `(i,x)↦(x,i)`. The all-actor lower bound below does not assume the actor is I or that B is a semilattice.

Since every S element is idempotent, its actual idempotence-context quotient is the one-element semigroup. Over that fixed actor any faithful host must inject all of S into its band, so the fixed-actual-actor minimum is `|S|=Σ_i|A_i|`, attained by B=S. The minimum **whole-host** size over all actors is also |S|, by injectivity and this trivial-actor host. These are statements for this concrete family, not general formulas for arbitrary S.

## 2. All-actor lower bound, including arbitrary gauges

Let `S→P(B,D)` be any faithful physical host, with completely simple Rees actor D and arbitrary group action α. Within each fibre `{i}×A_i`, all source idempotents commute. Their actor images are commuting idempotents in a CS semigroup; their product is idempotent and lies below both, so primitivity forces them equal. Call this common actor `d_i`.

For any i,j, choose x∈A_i and y∈A_j. Since both ideals contain x∧y, the source product gives `d_i d_j=d_i`; similarly `d_j d_i=d_j`. Thus the actor idempotents form a left-zero band and share a common Rees column λ. Write

`d_i=(r_i,g_i,λ)` with `g_i=P_(λ,r_i)⁻¹`.

Let `c_i(x)` be the host's band coefficient of `(i,x)`, and define the normalized coefficient `b_i(x)=α_(g_i⁻¹)(c_i(x))`. The physical weight from d_i to d_j is `g_i P_(λ,r_j)=g_i g_j⁻¹`; applying α_(g_i⁻¹) to the host product gives

`b_i(x) b_j(y) = b_i(x∧y)`.                             (2)

Each b_i is injective, because all source elements in fibre i have the same actor and the original host is faithful. If `b_i(x)=b_j(y)=z`, then idempotence of z and (2) in both orders give

`z=b_i(x∧y)=b_j(x∧y)`.

Injectivity in the two source fibres forces `x=x∧y=y`. Thus **coefficients associated to different underlying semilattice elements never collide**, even if their actor values coincide. For each x∈U select any i with x∈A_i; these selected b_i(x) are all distinct, proving `|B|≥|U|`. Together with §1 this proves (1), including infinite ambient actors and arbitrary noncommuting group actions. □

The finest pure actor of this band source is the left-zero band I: source row equivalences are exactly the fibre indices (meet joins any two elements of a fibre), all source column equivalences are connected through cross-meets, and the actual q has trivial group. This observation is not needed for the direct lower proof.

## 3. An unbounded gap from the largest actor fibre

Take k≥2 disjoint chains of m≥2 elements glued only at their common bottom 0; their union U is a meet semilattice and each chain A_i is a lower ideal. Then

`|S|=km`,  `max_i |A_i|=m`,  `min_(all CS actors)|B|=|U|=1+k(m−1)`.

The ratio `(1+k(m−1))/m` is unbounded as k increases. Thus the largest-idempotent-fibre lower bound from `frontier-20261028-fibre-saturation-host-test-v1.md`, SHA `0c71bd9e76e3eedb03cb8a4fe0d67cab342e32f187c738055022b45430811781`, need not be close to the all-actor optimum: cross-fibre consistency can force arbitrarily many more band elements. The fixed actual-q minimum remains km, and the left-zero-k actor realizes the sharp smaller band.

`frontier-20261028-ideal-gluing-band-bound-checker-v1.py`, SHA `34fe31d0f39e3695c987b5560d7bc51d2dc32d8ca11ee0ad8f7251b22ca9c84b`, ran in the Python eval kernel before Wed Oct 28 22:55:44 PDT 2026 and exactly checks source associativity, band and regular identities, semilattice laws and product host equations for (k,m)=(2,2),(2,3),(3,3),(4,4). The universal lower bound is the written gauge/overlap argument, not the samples. All results remain same-author unreviewed candidates; no formal proof, novelty or all-source Q1 conclusion is claimed.
