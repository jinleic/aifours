# Finite CS actor image and same-band restriction: explicit payment

**NEW AUTHOR WRITTEN ADDENDUM; unreviewed/unadopted.** This is an additive clarification of `frontier-20261028-all-cs-globally-regular-band-obstruction-v1.md`, SHA `2f9f6a68a153449b61cda78305174c5b601e28fba49ec391bc1107aaba8e31af`, §5. It keeps that file frozen. The source, its exact finite checker and the universal actual-q globally-regular obstruction are imported at their displayed scopes from that file. The conclusion excludes **globally regular-band-by-CS physical hosts only**, not original locally regular bands.

## 1. Exactly the finite subsemigroup claim

Let `D0=M[K;I0,Λ0;P0]` be completely simple and let T be a **finite nonempty subsemigroup** of D0. No conclusion here is asserted for an infinite or arbitrary subsemigroup.

Write J⊆I0 and M⊆Λ0 for the rows and columns actually occupied by T. Every cross-cell `(j,μ)∈J×M` is occupied: take an element of T with row j and one with column μ; their product is in that cell. Each `T_(j,μ)=T∩H^D0_(j,μ)` is a finite nonempty subsemigroup of the ambient H-class group, since multiplying two elements in one cell stays in that cell. A finite nonempty subsemigroup of a group is a subgroup containing the ambient cell identity. Thus **every element of T belongs to a subgroup of T**, so T is completely regular.

For actual a∈T_(i,λ) and b∈T_(j,μ), let x be the cell-group identity in T_(i,μ), and y the cell-group identity in T_(j,λ). Their product xby lies in the subgroup T_(i,λ). If z is its inverse in that subgroup, then

`x b y z a = a`.

Hence `a∈T b T` for arbitrary a,b and T is simple. Any idempotent natural-order comparison in T is a comparison in D0; the latter has equality as its idempotent natural order, so T has primitive idempotents. By the standard Rees–Suschkewitsch characterization (simple with a primitive idempotent), T is completely simple. This proof does not claim that an infinite, nonregular or arbitrary subsemigroup of D0 must be completely simple.

Moreover, the R-classes of T are exactly the occupied ambient rows and its L-classes exactly the occupied ambient columns. Indeed, distinct ambient rows cannot be R-related in T, since right multiplication preserves the ambient row. If a,b∈T have the same ambient row i, write a' for a's inverse in its occupied ambient cell group. Then a(a'b)=b, because aa' is the ambient cell identity in a's cell; symmetrically b(b'a)=a. The column statement is dual. Thus Rees coordinates of T may use the actual sets J,M, and inclusion has the identity row/column maps.

## 2. Derive all row gauges on the occupied matrix

Choose Rees coordinates `T=M[H;J,M;Q]` with a base row j0 and column μ0 normalized by `Q_(μ0,j)=1_H=Q_(μ,j0)` for every occupied j,μ. This standard normalization is performed on T's own coordinates; the original D0 multiplication table and original band B are NOT modified. The only ambient sandwich entries used below are the restriction of P0 to occupied indices `M×J`.

Put

`E_j=(j,1,μ0)`, `F_μ=(j0,1,μ)`, `T_h=(j0,h,μ0)`.

Every `(j,h,μ)=E_j T_h F_μ`. Because inclusion preserves the actual ambient row and column, write

`ι(E_j)=(j,X_j,μ0)`, `ι(F_μ)=(j0,Y_μ,μ)`, `ι(T_h)=(j0,K_h,μ0)`.

Set `p*=P0_(μ0,j0)`, `u_j=X_j p*`, `v_μ=Y_μ`, and `φ(h)=K_h p*`. Multiplication of the three displayed elements proves

`ι(j,h,μ)=(j,u_j φ(h) v_μ,μ)`.                           (2)

Since `T_h T_k=T_(hk)`, φ is a group homomorphism, and it is injective because ι is. Also `F_μ E_k=T_(Q_(μ,k))`, so applying ι, multiplying the group coordinate by p* and cancelling the explicit definitions gives

`v_μ P0_(μ,k) u_k = φ(Q_(μ,k))`  for every μ∈M,k∈J.      (3)

Thus (2)–(3) are proved for the restricted, occupied gauge matrix; no rows or columns outside T are assumed to be represented, and φ need not be onto K.

## 3. Restrict a physical host using the SAME B

Suppose the concrete finite source S embeds in an arbitrary ambient physical host `P(B,D0)`, with B a globally regular band and K acting by automorphisms α. Let `t:S→T` be its actor map and c(s) its ambient band coefficient. The map t is pure: if its actor value is idempotent then its physical self-weight is 1_K, so `(c(s),t(s))` is idempotent; faithfulness reflects idempotence to S.

For `t(s)=(j,h,μ)` define

`c_T(s)=α_(u_j^(-1))(c(s))`,    `η_h=α_(φ(h))`.

This is a genuine H action on **the same globally regular band B**, since φ is a homomorphism and α an action. For `t(s)=(j,h,μ)`, `t(t')=(k,l,ν)`, the ambient action weight is, using (3),

`u_j φ(h) v_μ P0_(μ,k) = u_j φ(h Q_(μ,k)) u_k^(-1)`.

Therefore

`c_T(st') = α_(u_j^(-1))(c(s) α_(u_j φ(hQ)u_k^(-1))(c(t')))`
`           = c_T(s) η_(h Q_(μ,k))(c_T(t'))`.

This is the full physical product law over T. If t(s)=t(s') and c_T(s)=c_T(s'), their common T row is j, so applying α_(u_j) recovers c(s)=c(s'); their original D0 actors are also equal. Original-host injectivity gives s=s'. Thus `s↦(c_T(s),t(s))` is a faithful T-host with the SAME globally regular B and no coinduction, extension of scalars, quotient of B, or added band factor.

## 4. Actual-q transport and exact exclusion

The actor map t is onto T and pure. For each source pair, actual and absent idempotence contexts lift and reflect, giving `τ_S=t^(-1)(τ_T)`. The quotient map `f:T→T/τ_T` is onto, pure and between completely simple semigroups; the pure onto-CS pushforward, reconstructed at full row-gauge scope in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, changes the band only to `(J×M)×B`. Its target group action is transported through the local-group isomorphism. The rectangular band J×M is globally regular, and its direct product with B is globally regular. This yields a faithful physical host over the actual source q_τ with a globally regular band.

That contradicts the explicit same-q R-idempotent collapse in the parent note §4. Thus, conditional on the named standard Rees facts and on the stated pure-onto pushforward, the concrete source admits **no embedding in any globally regular-band-by-CS physical host, for any CS actor and any action**. The proof has not established nonembedding in the original larger locally regular band class, nor a global Q1/Q2 resolution. A distinct five-element locally regular non-globally-regular countermodel to the parent note's four-term lemma is `frontier-20261028-local-band-four-term-countermodel-v1.md`, SHA `7be9d26f0941fc37728b7305dc9451c1b3586e442e87a5c976be13f2ad8dd72f`; it is mandatory scope context and is not a host for this source.
