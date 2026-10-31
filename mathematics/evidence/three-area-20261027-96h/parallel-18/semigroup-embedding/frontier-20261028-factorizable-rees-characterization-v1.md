# Exact original-class characterization for Rees matrices over a factorizable pure-group monoid

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 18:04:37 PDT 2026**. The theorem proves a universal if-and-only-if about an entire source family and supplies a source-derived faithful host, not a finite-table conjecture. The bounded exact check in §7 is supplementary. No full original-target resolution or novelty claim is made.

## 1. The source family and theorem

Let A be ANY nonempty regular monoid with an onto **idempotent-pure** group homomorphism `θ:A→G`, and suppose the restriction `θ|_(U(A)):U(A)→G` is onto. Equivalently, every element of A has the form `e u` with e idempotent and u a unit (§2). Let I,Λ be arbitrary nonempty index sets and let P be an **arbitrary** A-valued sandwich matrix; no entry is assumed unit in advance. Let S=M[A;I,Λ;P] be the FULL Rees matrix semigroup.

**Theorem.** The following are equivalent:

1. S is an original-class regular, weakly E-unitary, locally r-orthodox semigroup.
2. E(A) is a regular band and **every entry of P is a unit of A**.

Moreover, if these conditions hold, S has an explicit faithful physical band-by-completely-simple host. Its actor can be transported to the SAME actual syntactic pure-CS quotient q_τ, giving injectivity of κ_q and both same-q R- and L-idempotent separation properties. The host over the displayed Rees actor is constructed completely in §§2–4; the final transport to q_τ explicitly invokes the independently written but as-yet-unreviewed pure-actor pushforward theorem identified in §5.

In particular, within this exact factorizable-base family, weak E-unitarity of the source forces the seemingly additional all-unit sandwich condition. The theorem is not a statement that every original source has such a Rees description or that every regular monoid admits an onto pure group quotient.

## 2. Source-defined factorization and a faithful band-by-group model

Purity gives `E(A)=θ^(-1)(1_G)`. Since a product of two such elements also maps to1, E(A) is a band. The restriction of θ to U(A) is injective: if θ(u)=θ(v), then uv^(-1) is a unit mapping to1, hence is both idempotent and a unit, so uv^(-1)=1_A. With the assumed surjectivity, θ|_U is a group isomorphism. Let its inverse be `g↦u_g`.

For any a∈A, the element `e_a=a u_(θ(a))^(-1)` maps to1 and is idempotent, so

`a=e_a u_(θ(a))`.

This factorization uses a unique u_g and its e_a is then uniquely determined. Conversely, if every a is e u, θ(a)=θ(u), so surjectivity of θ implies units map onto G. Thus the displayed assumption is exactly factorization `A=E(A)U(A)` under the pure-quotient hypothesis.

Conjugation `α_g(e)=u_g e u_g^(-1)` is a genuine automorphism action of G on E(A). For `a=e_a u_g`, `c=e_c u_h`,

`ac=e_a α_g(e_c) u_(gh)`.

Hence `a↦(e_a,θ(a))` is a homomorphism into the actual `E(A)⋊G`. It is injective by uniqueness of u_g and e_a. If E(A) is a regular band, it lies in V, so this is a faithful admissible band-by-group host. It sends `1_A` to `(1_A,1_G)` and every unit u_g to `(1_A,g)`, but these are proved properties of THIS model, not assumptions about arbitrary hosts.

## 3. Weak E-unitarity of S forces every sandwich to be a unit

In any weakly E-unitary semigroup, if x³=x² then x is idempotent: d=x² is idempotent and `d=dx=xd`, so d≤x by the printed natural-order witness; weak E-unitarity gives x∈E. This uses no general monotonicity/cancellation.

Assume S is weakly E-unitary. Fix ANY entry `p=p_(λ,i)` of P. Since θ(U(A))=G, choose a unit v with `θ(v)=θ(p)^(-1)`. Purity makes `v p` idempotent in A. For the actual source element `x=(i,v,λ)`,

`x²=(i,v p v,λ)`,
`x³=(i,v p v p v,λ)=(i,(v p)²v,λ)=x²`.

Therefore x is idempotent, so `v p v=v`. Multiplying by the actual inverse of the unit v on both sides gives `p=v^(-1)`, a unit. The argument covers every λ,i, including repeated/non-normalized entries, without requiring a finite matrix or testing the actor quotient.

This is not a claim that P must consist of units for arbitrary pure-group bases: the 60-element tight-nonunit source in `frontier-20261028-tight-sandwich-rees-criterion-v1.md` has a pure quotient whose unit group does NOT surject onto its C2 actor. The surjective-unit hypothesis is essential to the displayed proof and is not dropped.

## 4. Unit sandwiches give the original source and the explicit host

Suppose now E(A) is a regular band and every p_(λ,i) is a unit. First, S is regular: for s=(i,a,λ), choose a'∈V_A(a), any j,μ, and put

`t=(j,p_(λ,j)^(-1) a' p_(μ,i)^(-1),μ)`.

Direct multiplication gives sts=s and tst=t. This is valid in arbitrary cardinality and uses the actual two sandwich-unit inverses.

Define the onto Rees actor `D=M[G;I,Λ;θ(P)]` and

`r(i,a,λ)=(i,θ(a),λ)`,
`j(i,a,λ)=(e_a,r(i,a,λ)) ∈ P(E(A),D)`.

If p is the unit u_h and a=e_a u_g, c=e_c u_k, then

`a p c=e_a α_(g h)(e_c) u_(g h k)`.

Therefore the actual band coordinate of j(st) is `e_a α_(g h)(e_c)`, exactly the physical host multiplication weight. Actor coordinates agree by construction. Equal j-images have equal source rows/columns and θ-values, and equal e_a; uniqueness of §2 gives equal A-elements. Thus j is a faithful homomorphism over the **actual specified** r.

The actor r is pure: if r(i,a,λ) is idempotent, then `θ(a)=θ(p_(λ,i))^(-1)`. With `p_(λ,i)=u_h`, write a=e_a u_(h^(-1)). Then `a p a=e_a²u_(h^(-1))=a`, so the source element is idempotent. The converse holds for every homomorphism. A completely simple Rees actor has equality natural order; hence purity makes S weakly E-unitary.

For local r-orthodoxy, each local source idempotent maps to an idempotent actor ε. The local actor corner εDε is a group, so every local source idempotent has actor ε and, in the faithful host, a band coordinate in the actual regular-band corner `e_a E(A) e_a`. Their products remain idempotent and inherit the regular-band identity. The source local monoids are regular by the ordinary e x' e inverse construction. Thus S is locally r-orthodox.

## 5. Necessity of E(A) regular, and the actual syntactic quotient

For ANY row i and column λ put p=p_(λ,i), now known to be a unit, and let `e=(i,p^(-1),λ)`. It is an actual source idempotent. Its local monoid eSe is isomorphic to A by

`(i,a,λ) ↦ a p`,

with inverse `z↦(i,z p^(-1),λ)`. Indeed eSe is exactly the full fixed-row/fixed-column subsemigroup and its product `a p c` becomes `(a p)(c p)`. The identity e maps to 1_A.

Therefore, if S is locally r-orthodox, A is an orthodox monoid whose entire idempotent set is a regular band. This completes the forward implication of §1. Conversely E(A) regular plus all-unit P gave every original hypothesis in §4, completing the iff. No false implication that an arbitrary local band is globally regular is used: this particular corner is explicitly all of A.

For the SAME source S, r is an onto idempotent-pure CS map, so `τ_S=r^(-1)(τ_D)` by full-context lifting/purity. Its quotient map `f:D→D/τ_D` is pure and onto. The separately written `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, proves an explicit whole-host embedding over f with band enlarged only by the original Rees rectangle. Composing with j provides a faithful host over the ACTUAL q_τ; the canonical free-V-band universal map then makes κ_q injective. Thus all same-q R and L pairs are separated.

**Dependency limit:** this last same-τ conclusion is conditional on the named unreviewed pure-actor pushforward proof and ordinary Rees/CS structural facts. Without it, §§2–4 still give the faithful original physical embedding over r. No earlier external review, CG/RU–LU argument or held outcome is a premise.

## 6. Exact scope and printed target

The theorem classifies full Rees sources over an explicitly factorizable pure-group monoid A. When E(A) is regular, the explicit host has regular-band base (therefore seminormal) and completely simple actor, so it supplies the printed first-question embedding for these sources under the standard product convention. It does not prove that arbitrary printed locally r-orthodox sources possess this form, or that the printed first question is equivalent to the registered all-host criterion. It does not address printed Question 2.

The negative direction is a true source-hypothesis constraint: under the stated unit-surjectivity premise, a nonunit sandwich gives an actual x³=x²≠x and therefore S cannot be weakly E-unitary. It is NOT an original-class counterexample and is not evidence that a nonunit sandwich fails for bases outside this assumption.

## 7. Exhaustive finite experiment

Checker `frontier-20261028-factorizable-sandwich-checker-v1.py`, SHA `cbf9a4273131352bffe01fb2c7246e37b26a6a337c25f3047adf1c7149aa4f45`, executed with `/opt/homebrew/bin/python3 -B` at **Wed Oct 28 18:04:11 PDT 2026**, timeout60s, exit0:

```text
base_size=10 unit_count=2 matrices=10000
all_unit_matrices=16 nonunit_matrices=9984
PASS all9984 nonunit matrices have explicit x^3=x^2!=x, violating WEU
PASS all16 unit matrices: full source regular/local-r/WEU, pure actor and faithful host
```

The base is `(2×2 rectangular band with identity)⋊C2` under the row/column-flip action. The program evaluates **every**2×2 sandwich matrix over that base. For each of the9984 nonunit cases it constructs the exact source element and idempotent natural-order witness; for each of the16 all-unit cases it exhausts the40-element source's regularity, local-r, weak E-unitarity, pure actor and host product/injection checks. It does not verify the infinite/all-base theorem by enumeration or certify the prior actor pushforward.

## 8. Remaining gaps and verification status

The primary proof steps above are written from the supplied definitions and elementary group/band/Rees arithmetic. Named imports for the actual-q extension are the recorded pure-onto CS actor pushforward and ordinary Rees representation/CS local-group facts; the former is a current unreviewed candidate, not an automatically accepted theorem. No independent implementation of this10,000-matrix experiment, external-model/human/formal/kernel review, full literature priority or novelty clearance has occurred.

Original sources lacking this factorizable pure-group monoid representation remain untreated. Previous source outcomes are historical, not automatically rehabilitated. The full printed first question, printed Question 2 and unrestricted registered same-quotient obligation remain open at this record's scope.
