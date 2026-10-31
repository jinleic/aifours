# Full Rees sources over an identity-adjoined band-by-group base

**NEW AUTHOR WRITTEN CANDIDATE with exact finite checks; unreviewed/unadopted.** Native check-start observations **Wed Oct 28 19:10:21 PDT 2026** and **19:11:06 PDT 2026**. This extends the earlier rectangular-base-with-new-identity theorem to arbitrary globally regular band bases, and gives an exact characterization for the full Rees sources in the original class. It remains a SPECIAL Rees family, not an all-original-source solution or novelty claim. The actual-q/canonical clause depends on the named pure-CS actor pushforward.

## 1. Exact source characterization and host

Let B be ANY nonempty band and G ANY group acting on B by automorphisms. Let `A=(B⋊G)^1` denote B⋊G with a **new external identity** 1_A, even if B⋊G already had one. Thus B⋊G is the proper ideal of nonunits of A. Write `θ(1_A)=1_G` and `θ(b,g)=g`, and put

`K(B)={p∈B : b p b=b for every b∈B}`.

Let I,Λ be nonempty and P any full Λ×I matrix over A. For S=M[A;I,Λ;P]:

1. S is regular **iff** each P row and each P column contains 1_A.
2. S is weakly E-unitary **iff** each P entry is either 1_A or `(p,q)` with q≠1_G and p∈K(B).
3. If S is regular and locally r-orthodox then B is globally a regular band.
4. Conversely, if B is globally regular and the matrix satisfies item2, S has an explicit faithful physical model over its natural CS actor `r(i,a,λ)=(i,θ(a),λ)`. Whenever additionally item1 holds, S is a regular weak-E locally r-orthodox source. Under the explicit pure-CS actor pushforward in §7, that model yields faithful actual-q and canonical κ_q, with both same-q R/L obligations.

Thus items1–3 are NECESSARY, and together with global regularity and the matrix form they are SUFFICIENT, for this full Rees source to lie in the declared original class. No claim is made that arbitrary original sources admit this special form. K can be empty; §4 treats the resulting all-unit case separately.

## 2. Prove regularity and the original-class base constraint

B⋊G is regular: `(b,g)` has mutual inverse `(g^(-1)·b,g^(-1))`; 1_A is its own inverse. If every P row and column contains 1_A, pick appropriate unit sandwiches and any inverse in A to obtain an inverse of each Rees source element.

Conversely, suppose S is regular. For each i,λ, the source `(i,1_A,λ)` has some x=(j,a,μ) with sxs=s. Its middle equation is

`P_(λ,j) a P_(μ,i) = 1_A`.

Any factor in the proper ideal B⋊G makes the whole product nonunit, so all three factors are 1_A. Hence row λ and column i each contain a unit. This proves item1, without assuming weak E or local regularity.

If S is additionally locally r-orthodox, choose a cell with `P_(λ,i)=1_A` (such a cell exists). Its idempotent `(i,1_A,λ)` has local monoid isomorphic to A. The idempotents of A are exactly `1_A` and `(b,1_G)` for b∈B, so their band is B with a new identity adjoined. Local r-orthodoxy requires this band globally regular, and then its subband B is globally regular. This is item3.

## 3. Exact weak-E matrix form

If the matrix has the form in item2, the natural CS actor is pure. At a diagonal 1_A sandwich, an idempotent actor has θ(a)=1_G, and both 1_A and all `(b,1_G)` are idempotent. At a diagonal `(p,q≠1_G)` with p∈K(B), the source middle element has form `(b,q^(-1))`, and its square returns it because `b(q^(-1)·p)b=b`. Equality of natural order in the CS actor then gives weak E-unitarity.

Conversely, if P contains a nonunit `(p,1_G)`, its corresponding `s=(i,1_A,λ)` has `s³=s²≠s` with s² idempotent, a weak-E violation. If P contains `(p,q≠1_G)` with p∉K(B), choose b with `b(q^(-1)·p)b≠b` (K is automorphism invariant) and set `s=(i,(b,q^(-1)),λ)`. The band law `(bt)^2=bt` gives `s³=s²≠s`. Again s² is idempotent and below s. This establishes item2 without relying on a finite test.

## 4. Evaluation band: the nonunit-sandwich branch

Assume B globally regular, item2 holds, and at least one P entry is nonunit. Its band part supplies `z∈K(B)`. Adjoin a formal identity 1 to B, giving the regular band B^1; G acts on it by fixing 1. Define a full Rees semigroup over B^1 with rows I×G, columns Λ×G, and sandwich

`H_((λ,t),(j,u)) = 1` if t=u;

`H_((λ,t),(j,u)) = t^(-1)·p` if t≠u and `P_(λ,j)=(p,t u^(-1))`;

`H_((λ,t),(j,u)) = z` in all remaining cases.             (4)

All off-diagonal H values lie in K(B). Let T be the subset containing

- ALL Rees cells with middle b∈B; and
- cells with middle1 only when the group indices in the row and column agree.

T is closed: any product containing a B-middle factor or off-diagonal H has B-middle. If both middle factors and H are1, the left and right group indices agree at their junction; the output unit-middle cell is again aligned. Associativity is inherited from the ambient Rees semigroup. Every B-middle element squares to itself because its diagonal H is either1 or a K element; every aligned 1-middle element has diagonal H=1. Thus T is a band.

T is locally regular. For an idempotent e with B-middle a and diagonal sandwich p∈B^1, its local corner contains only B-middle cells because B is an ideal in B^1. Put d=ap∈B; then d²=d. The same map used in the predecessor, `(row,b,col)↦bp`, embeds eTe into dBd: e-locality gives `b=a p b p a`, yielding both `bp=d(bp)d` and injectivity. Since B is globally regular, dBd is a regular band.

If e has aligned 1-middle, its diagonal H is1, and its local corner is the band B^1 itself at that fixed row/column. Adjoining an identity preserves the regular-band identity, so this corner is regular. Therefore T is locally regular. The necessity of global regularity of B for these unit corners is explicit, not hidden by the proof.

## 5. Empty-K guard and all-unit branch

If ALL P entries are 1_A, K(B) may be empty even when B is a finite regular band. Do not choose z. Instead use the full Rees band over B^1 with the same row/column sets I×G,Λ×G and **every** H entry equal to1; allow every 1-middle cell. This is a rectangular band times B^1, hence globally regular and in the required local variety. The same coefficient formula in §6 works, since every actual sandwich has group label1_G and band part1.

A concrete three-element semilattice with incomparable maximal points has K=∅; the exact control in §8 verifies this all-unit branch and its nontrivial actual-actor quotient. If at least one admissible nonunit P entry exists, its band part lies in K and §4 applies. Thus the construction covers both cases without an unstated nonempty-K hypothesis.

## 6. Faithful physical host, with all source products

In either branch let the target band be `C=T^G`, with left shift `(α_wF)(k)=F(w^(-1)k)`. For source `s=(i,a,λ)`, write g=θ(a), and let `\bar a∈B^1` be1 if a=1_A, or its B component b if a=(b,g). Define

`β_s(k)=((i,k), k^(-1)·\bar a, (λ,g^(-1)k))`.           (6)

A source 1_A gives an aligned 1-middle cell, so β_s actually lies in T. For `t=(j,c,μ)`, set `q=θ(P_(λ,j))`, w=gq. In the product with shifted β_t, the two relevant group indices in (4) are `t0=g^(-1)k`, `u0=(gq)^(-1)k=q^(-1)t0`, so `t0 u0^(-1)=q`.

- If the actual P entry is 1_A, q=1_G, t0=u0 and the T sandwich is1.
- If the actual P entry is `(p,q≠1_G)`, t0≠u0 and the T sandwich is `(k^(-1)g)·p`.

The same identities hold in the all-unit branch. Hence the resulting T middle is exactly `k^(-1)` applied to the B^1 component of `a P_(λ,j) c`, and the resulting column is `(μ,θ(c)^(-1)q^(-1)g^(-1)k)`. Thus `β_(st)=β_s α_(gq)(β_t)` for EVERY source pair and arbitrary noncommutative G.

The natural Rees actor supplies i,λ,g. At k=1_G, the β middle supplies the B component or the distinct new identity. Therefore the physical homomorphism is injective. If source regularity holds, this faithful local-band/CS model makes every local E(eSe) a regular band, proving item4's original-class sufficiency.

## 7. ACTUAL q and explicit dependency

The natural actor is onto and pure by item2, so `τ_S=r^(-1)(τ_D)`. It need NOT be the actual quotient itself. The pure onto-CS actor pushforward in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, adds a rectangular band factor and transports the action via a local-group isomorphism, producing a faithful physical host over ACTUAL q_τ. The product band remains locally regular; the canonical free-V-band universal map then makes κ_q faithful and proves the two same-q R/L obligations.

If that named WRITTEN input fails independent review, retain the natural-actor host and source characterization in §§1–6, and mark actual-q/canonical **NR-PUSHFORWARD**. No inference about arbitrary original sources or equivalence to the entire printed target is made.

## 8. Exact checks for BOTH branches

`frontier-20261028-adjoined-identity-band-rees-checker-v1.py`, SHA `246c11ed7aadc066b9de179e4748e1c79d334c4dd7e7edb066d44798fc4feb74`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:10:21 PDT 2026**, exit0. Its B is a nonrectangular8-element regular band with K of size4, G=C2 acts nontrivially, and P has a row containing distinct nonunit labels at the same nonidentity group value. Source102, natural actor12, ACTUAL actor8; the aligned-unit evaluation band T has204 elements. The checker exhausts T closure/idempotence/all204³ associativity, all local corners, every102² source/host product and fibre comparison, WEU/regularity/local-r, and all103² contexts per source. It verifies both forbidden-sandwich WEU controls and a missing-unit-row nonregularity control.

`frontier-20261028-empty-K-unit-rees-checker-v1.py`, SHA `0ce8f1a4a2f65babf74d1da1d5598172786927b8a3e4500ccc2de0af9fabf49c`, ran at **Wed Oct 28 19:11:06 PDT 2026**, exit0. For a3-element semilattice with K=∅, new-unit A has7 elements and an all-unit P yields source28, natural actor8, ACTUAL actor2. It checks the full64-element all-unit evaluation band, all784 source/host laws, source τ and retained-rectangle actual-q injection. No nonexistent z is used.

Both verifiers are same-author finite evidence; the arbitrary-band/group proof is written above. No independent, cross-vendor, human or formal/kernel review, all-source conclusion or novelty clearance is claimed.
