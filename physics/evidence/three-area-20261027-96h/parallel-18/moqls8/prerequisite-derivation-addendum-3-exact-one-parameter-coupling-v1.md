# Addendum3 — finite all-order criterion and exact joint one-parameter coupling

Actual preceding native clock: **Tue Oct 27 15:08:20 PDT 2026**.
Owner PhysicsMOQLS8-2 / physics-4. **WRITTEN / UNREVIEWED** all-variable conditional theorem. No numeric state, chosen control, finite time sample, interpreter, calculator, CAS, solver or replay.

The15:08:03 parent standing direction keeps S1 in force and requires continued admissible work without requesting approval for each internal step. It does not admit new sources, held methods, numerical execution or stronger claims. This packet continues the actual-family coupling question; it does not silently restrict the original four-family target to deformation-connected families.

## 1. Exact original-object hypotheses

Let (A1,A2,A3,A4) be ANY actual ordinary complex four-MOQLS(n) tuple (n=8 included). All row/column and pair-product ONB conditions hold. No member is assumed classical; all phases and separate member frames remain free.

For every a choose a nonzero subspace S_a, an active cell set Omega_a with A_a(x)∈S_a for its active cells, and ANY skew-Hermitian linear operator X_a on S_a. Put r_a=dim S_a. Its proposed one-parameter move is

    A_a(u;x)=exp(u X_a) A_a(x) if x∈Omega_a,
    A_a(u;x)=A_a(x) otherwise,             u∈R.

The parameter origin is the identity of this universally quantified operator group, not a selected physical test state. No numerical operator, angle, point or curve is instantiated. Skew-Hermiticity makes exp(uX_a) unitary for real u by the ordinary convergent exponential series.

The following theorems distinguish THREE obligations:

1. one member's whole path is legal against the three ORIGINAL fixed mates;
2. local directions have all higher-order compatibility, not merely a first derivative;
3. all four individually legal paths can be combined simultaneously.

## 2. Permission subspaces from the SAME original family

For one selected member A=A_a, suppress a in notation. Let S,Omega be its data. For every active x define

    R_x=span{A_y:y∈Omega, same row as x},
    C_x=span{A_y:y∈Omega, same column as x},
    F_x^b=sum_(y∈Omega)|<A_b(x),A_b(y)>|² P_(A_y),  b≠a,
    M_x=R_x∩C_x∩intersection_(b≠a) E1(F_x^b).

These are exactly the conditional faces of addendum2, but the full load-bearing argument is repeated here: product-basis completeness gives

    sum_y |<A_b(x),A_b(y)>|² P_(A_y)=I.

After compression to S, I_S−F_x^b is the positive sum over inactive y of the corresponding projected rank-one operators. Its kernel is the set of vectors orthogonal to EVERY inactive projection whose mate overlap is nonzero. The original row/column resolutions give the analogous orthogonal complements of R_x/C_x.

Consequently a common unitary U on the active cells produces an actual four-family with the original mates fixed **iff** U A_x∈M_x for every active x. Both-active and both-inactive inner products are preserved; at a mixed pair the indicated row/column or nonzero-mate constraint is exactly what remains. Unit norms, all row/column ONBs and n²-vector product completeness are retained. This is an exact physical iff, not an imported old channel/local-span theorem.

## 3. Exact single-member ALL-order criterion

> The one-member path is an actual four-family with its three original mates fixed for EVERY real u iff
>
>     X^j A_x∈M_x for every x∈Omega and j=0,…,r−1.      (K)
>
> Legality on any open parameter neighborhood of the identity is already equivalent to the same condition and hence to legality for all real u.

**Necessity.** If exp(uX)A_x lies in the fixed linear space M_x on an open neighborhood, every derivative at the identity lies there. Those derivatives are X^j A_x. This includes all indicated orders; the original j0 condition already holds because the family is actual.

**Sufficiency, including the finite order bound.** For any nonzero vector v in an r-dimensional space, the span of v,Xv,…,X^(r−1)v is X-invariant. If the r vectors are independent they span the space. Otherwise choose the first dependence X^ell v in the span of its predecessors; multiplication by X propagates that same finite span to all later powers. Thus all X^j v lie in the displayed span.

Under(K) that entire span lies in M_x. Every partial sum of exp(uX)A_x lies there, and the space is closed, so the actual exponential lies there for every real u. The exact permission iff in §2 then proves all QLS/product conditions. This uses no evaluated matrix power or enumeration.

This identifies the missing integrability test: verifying only X A_x∈M_x is not a proof of(K) or of a legal whole path. If an indicated higher power leaves M_x, this constant-generator path is impossible. It does **not** rule out a different nonconstant-generator path having the same first-order motion; that stronger assertion is not made.

## 4. Exact activation signature of an originally common-zero pair

Let

    Z0={e={x,y}: all FOUR original member overlaps vanish at e}.

Assume(K) holds for each of the four proposed paths separately against its original mates.
For e∈Z0 and member a:

- if both or neither endpoint is active in that member, its updated overlap is constant0;
- if exactly one endpoint x is active, put v=A_a(x)∈S_a and w=P_(S_a) A_a(y). The overlap, up to complex conjugation from exchanging endpoints, is

       f_a(u)=<exp(uX_a)v,w>.

Its Taylor coefficients are <X_a^j v,w>/j!. The coefficient at j0 is0 because e was originally common-zero.
Define the **activation set** T_a by including e exactly when it is mixed-active and

    <X_a^j v,w>≠0 for at least one j∈{1,…,r_a−1}.        (A)

For r_a=1 the index set is empty and there is no activation.

> e∈T_a iff the updated overlap is NOT identically zero as a function of u.

**Proof.** If all r_a initial coefficients including j0 vanish, the invariant-span argument of §3 makes every later coefficient vanish as well. The exponential overlap is identically0. Otherwise the least nonzero coefficient occurs among those finite orders. Its convergent Taylor series has a genuine first nonzero term, so the overlap is nonzero for all sufficiently small nonzero u. No sampled value of u is evaluated or needed. ∎

The signature uses exact original vectors, projections and a common generator. It is not a support-only pattern or an approximate residual, and no numeric coefficients are supplied by a program.

## 5. ALL-four-path theorem — finite signatures decide full simultaneous legality

> Subject to each path's exact single-member condition(K), the following are equivalent:
>
> (i) the simultaneous tuple is actual for EVERY real u;
> (ii) it is actual on SOME open neighborhood of the identity;
> (iii) T1,T2,T3,T4 are PAIRWISE DISJOINT.                (J)

### (iii) implies(i): every original pair case

Fix a cell pair e. If one original member a had nonzero overlap, single-member path legality for each b≠a against that original member forces the entire updated b overlap identically0. At most the updated a overlap can be nonzero.

If all original overlaps were zero, the only members that can develop a nonzero overlap belong to their activation sets. Disjointness allows at most one. Thus every updated member pair has product overlap0 at every cell pair for every u.
Each updated member was already an actual QLS by(K). Norm1 and n²-vector completeness give an ONB for every updated member pair. The simultaneous family is actual for every u.

### (ii) implies(iii): no cancellation of the first mixed activation term

If e belonged to both T_a and T_b, their two overlap functions have first nonzero Taylor terms c_a u^p and c_b u^q, with c_a,c_b nonzero. Their product has first term c_a c_b u^(p+q), nonzero over C. Hence the product cannot vanish on an open neighborhood, contrary to actual pair-product orthogonality. Different orders p,q do not avoid the collision. No chosen point or finite check proves this; it is an identity of convergent local series.

Finally(i) implies(ii) trivially. This proves the full forward/converse theorem and all complex-phase cases. ∎

A collision therefore forbids ANY simultaneous interval of these otherwise singly legal constant-generator paths. It is not enough that they are independently legal or that their first-order mixed-product equations happen to vanish.

## 6. General smooth two-jet obstruction, without the constant-generator assumption

There is also a necessary obstruction for ANY C² actual four-family path, not only the paths above. Let g_a(u)=<A_a(u;x),A_a(u;y)> for a fixed cell pair. Actuality gives

    g_a(u) g_b(u)=0 for every a≠b and every u.

At ANY parameter value tau with g_a(tau)=g_b(tau)=0, differentiating twice gives

    2 g_a'(tau) g_b'(tau)=0.                            (JET2)

Thus two prescribed nonzero overlap derivatives at a common-zero pair cannot be integrated to a C² actual coupled path. The first derivative of the product equation at that pair is identically0 and by itself misses this constraint.

This is a universally quantified obstruction, not an asserted example of feasible first-order data with a failed lift. Nor does satisfying(JET2) guarantee integrability: further derivatives, all vector/ONB equations and actual path existence still matter. For constant-generator proposals §5 gives the complete finite higher-order activation criterion, not merely this necessary two-jet filter.

Entry rephasings multiply g_a by a nonzero phase function. At a zero of g_a its first derivative is only multiplied by the base phase, so(JET2)'s zero/nonzero condition is invariant. Separate time-dependent output unitaries preserve the actual member overlap exactly. No common frame or fixed entry phase is assumed.

## 7. Degenerate, isotopy and actual-target limits

- Empty active sets, zero projected w, one-dimensional S, or all zero activation coefficients produce empty activation sets and no collision. No nonclassical family is thereby constructed.
- If the whole cell set is active in a whole output space, the path is a global output isotopy; its member Gram is constant and its activation set is empty. Even nontrivial generators do not then change classicality.
- If all permission spaces are the original rays, condition(K) allows only phase changes on active entries. This is not an escape from the original classicality question.
- All finite order bounds are symbolic dimension statements; no operator, cell list or numeric parameter was enumerated/evaluated. Different member dimensions, active sets and separate output frames are allowed.
- Real-analyticity needed for the activation argument is supplied by these exact exponentials. The C² statement §6 is separately limited to its necessary jet conclusion. No arbitrary smooth path is promoted to an analytic constant-generator path.
- **Unpaid reachability premise:** nothing here proves that every potential nonclassical four-family can be connected to a classical tuple by these moves, or even that such a family admits a non-isotopic legal motion. Isolated or differently connected components are not excluded. “No legal move” does not imply “classical.”

Thus this route now has exact single-member all-order and simultaneous all-member gluing tests, but cannot by itself settle the unrestricted existence/no-go problem without an original-object reachability or static obstruction. That is a documented route barrier, not a claim that the original problem or all research methods are exhausted.

## 8. Input and assurance ledger

All claims use only S1/S2's admitted actual QLS/pair-product definitions and ordinary finite-dimensional facts: tensor inner-product/ONB completeness, positive rank-one sums/kernel identities, linear dependence in finite dimension, convergent matrix exponentials and their derivatives, and the elementary product/Taylor rules. Every model-specific permission, activation and synchronization step is proved here.

No legacy proof/review/park/checkpoint, old channel/local/commutant/candidate theorem, held guide or bibliography link supplies an input. No independent-reconstruction/private-cognition/novelty certificate is asserted. The packets remain author-written unreviewed candidates; Main must freeze a full scope and read whole sources/returns before adoption.

No full four-family theorem, physical nonclassical witness, numerical M(8)/maximum-three/A10/A11/native result, formal/kernel/human/configured-family/executable/novelty gate changes. Only the new owner root was written. Original STOP outside S1, HOLDv2/N4 UNKNOWN historical exit UNESTABLISHED/aux214STOP and every old finding/ZERO consumer persist. No scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/decimal/boundary probe, nested agent/model CLI, Git/delete/contact/infrastructure action.
