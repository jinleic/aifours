# Every weak-E regular Rees source over the five-element base has a local-band lift

**NEW AUTHOR WRITTEN CANDIDATE with exact finite checks; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 18:51:47 PDT 2026**. This strictly removes the row-code and triangular-tag restrictions of the two preceding Rees families, but only for ONE specified five-element base A. It is not a theorem for all original sources, a printed-question equivalence, an independently reviewed result or a novelty claim.

## 1. Exact theorem

Let A have identity4 and multiplication table

```text
0 1 2 3 0
3 2 1 0 1
0 1 2 3 2
3 2 1 0 3
0 1 2 3 4
```

Write θ=(0,1,0,1,0):A→C2. Equivalently `A=(R⋊C2)^1`, where R={0,1} is right-zero and the nontrivial group element swaps R; its nonidentity `(r,g)` is table label `2r+g`. Let I,Λ be arbitrary nonempty sets and let P be ANY Λ×I matrix over A.

**Theorem.** If every P entry is in `{4,1,3}`, then the full Rees semigroup S=M[A;I,Λ;P] has an explicit faithful physical host over its natural CS actor `r(i,a,λ)=(i,θ(a),λ)`, with a locally regular band and C2 action. No other restriction on P, its entries' placement, I or Λ is imposed. If S is regular, this host makes S weakly E-unitary and locally r-orthodox, and the actual-q conclusion in §5 gives canonical κ_q injectivity.

Conversely, if S is regular and weakly E-unitary, every entry of P must be in `{4,1,3}`. Therefore **every regular weak-E full Rees source over this particular base A** lies in the displayed faithful-host family; local r-orthodoxy follows rather than being assumed. Source regularity is not automatic; all rows and columns having a4 is one sufficient condition.

This covers P rows with arbitrarily many occurrences of distinct 1 and3 at the same group label, including patterns violating both earlier sufficient families. The target band below may be infinite if I or Λ is infinite. Nothing says an arbitrary weakly E-unitary locally r-orthodox source is a Rees semigroup over this A.

## 2. An evaluation band for an arbitrary sandwich matrix

For each λ choose a function `f_λ:I→{0,1}` with

`f_λ(i)=1` when P_(λ,i)=1; `f_λ(i)=0` when P_(λ,i)=3;

on positions where P_(λ,i)=4 choose either value, for example0. This is possible for any allowed P, without a factorization, colouring or same-row uniqueness assumption.

Form a disjoint union

`T={U_i:i∈I} ⊔ {V_λ:λ∈Λ} ⊔ {W_0,W_1}`.

Put `N={V_λ}∪{W_0,W_1}`. Define multiplication on T by

- `x y=y` for every x∈T and y∈N;
- `U_i U_j=U_i`;
- `W_r U_j=W_r`;
- `V_λ U_j=W_(f_λ(j))`.

These four clauses cover every product. T is a band and is associative: idempotence is immediate. For associativity, if the rightmost factor lies in N, both bracketings equal it. If the two rightmost factors are U_j,U_k, their product is U_j, while `x U_j` is always either a U or a W and is unchanged by right-multiplication by U_k. Finally, if the middle factor lies in N and the rightmost factor is U_k, both bracketings equal that middle factor multiplied by U_k, which lies in N. No finiteness is used.

Each `U_i T U_i={U_i,W_0,W_1}`: U_i is an identity on the two-element right-zero band of W's. For every e∈N, `e T e={e}`, because every element times e equals e. Hence all local corners are regular bands. Let

`B=T×T`,      `α_1(x,y)=(y,x)`.

B is locally regular, and the coordinate swap is a C2 action. In contrast to the false simultaneously-tight A-model route, this band explicitly remembers BOTH a source column λ and an arbitrary source row selector i.

## 3. Faithful host and a symbolic proof of ALL products

For a nonidentity middle value a=(r,g), r,g∈{0,1}, define a band coordinate

`C(i,(r,0),λ)=(W_r,V_λ)`,
`C(i,(r,1),λ)=(V_λ,W_(1-r))`,
`C(i,4,λ)=(U_i,V_λ)`.

The actor is `r(i,a,λ)=(i,θ(a),λ)`. If actor coordinates and C coincide, i,λ,g are fixed. For g=0, `(W_0,V_λ)`, `(W_1,V_λ)` and `(U_i,V_λ)` are distinct, distinguishing 0,2,4. For g=1, the second coordinates W_1,W_0 distinguish1,3. Thus `j(s)=(C(s),r(s))` is injective.

For arbitrary `s=(i,a,λ)`, `t=(j,b,μ)` set `p=P_(λ,j)`, `q=θ(p)`, `g=θ(a)`, and `w=g+q` mod2. The full physical law is

`C(st)=C(s) · α_w(C(t))`.                                 (1)

We prove it without an index-size or P-pattern enumeration.

**If b=(v,h) is nonidentity**, both coordinates of C(t) lie in N. Because every x∈T satisfies x n=n for n∈N, the right factor of (1) overwrites the left. The middle product is `(v+w,h+w)` in R⋊C2, even if a or p is the new identity. If w=0, C(st)=C(t); if w=1, the displayed nonidentity formula gives C(st)=swap(C(t)). Thus (1) holds.

**If b=4 and p=4**, w=g and the middle product is a. If a=4, `(U_i,V_λ)(U_j,V_μ)=(U_i,V_μ)`. If a=(r,0), the product with `(U_j,V_μ)` is `(W_r,V_μ)`. If a=(r,1), the action swaps the right coefficient and `(V_λ,W_(1-r))(V_μ,U_j)=(V_μ,W_(1-r))`. Each is exactly C(st).

**If b=4 and p=(v,1)**, f_λ(j)=1−v. If g=0, the second coordinate of C(s) is V_λ whether a=4 or a=(r,0). The swapped right coefficient is `(V_μ,U_j)`, so the product is `(V_μ,W_(1-v))`, the coefficient of the middle product `(v,1)`. If g=1, a=(r,1), the action weight is0 and `(V_λ,W_(1-r))(U_j,V_μ)=(W_(1-v),V_μ)`, the coefficient of `(1−v,0)`. This proves (1) in every case, for arbitrary I,Λ and any placement of1/3/4.

The actor product is the Rees product in D=M[C2;I,Λ;θ(P)]. Thus j is a faithful physical homomorphism.

## 4. Weak-E classification and original class

For an allowed matrix P, the natural actor is pure. At source `(i,a,λ)`, its actor is idempotent exactly when `θ(a)+θ(P_(λ,i))=0`. If the sandwich is4, a has θ=0 and is one of the idempotents 0,2,4. If the sandwich is1 or3, a has θ=1 and the semidirect formula gives `a P_(λ,i) a=a`. A natural-order comparison with an idempotent transfers to the CS actor, whose natural order is equality; purity therefore gives weak E-unitarity.

Conversely suppose some `P_(λ,i)=p∈{0,2}`. Put `s=(i,4,λ)` and `e=s²=(i,p,λ)`. Since p²=p, `s³=s²=e`, e²=e, e≤s in the natural order, and s≠e is not idempotent. Thus weak E-unitarity fails. This proof covers every matrix position and does not assume the row/column unit regularity criterion.

Consequently, within regular full Rees sources over A, weak E-unitarity is equivalent to having P entries only 4,1,3. For a regular such S, the faithful local-band physical model makes every local eSe orthodox with regular idempotent band: the local actor is a group and its idempotents have the same actor identity, while the band coefficients lie in a regular corner of B. Thus S is locally r-orthodox. Row/column occurrence of4 guarantees regularity by inserting those identity sandwiches and a mutual inverse in A, but is not claimed necessary.

## 5. ACTUAL q and canonical obligations

The physical actor r is onto and pure. Therefore `τ_S=r^(-1)(τ_D)` by lifting actual contexts and reflecting idempotence; the actual source q is the composition with the pure quotient D→D/τ_D. The onto-pure-CS actor pushforward in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, gives a faithful physical model over that ACTUAL q by adding a rectangular-band factor I×Λ and transporting the action through a local-group isomorphism. The product band remains locally regular. Mapping the canonical free V-band generators to the translated physical coefficients then proves κ_q injective, including both same-q R and L idempotent separation.

This actual-q/canonical clause explicitly imports the named WRITTEN actor pushforward. If that input fails review, retain §§2–4's faithful natural-actor model and weak-E classification, and mark actual-q/canonical as **NR-PUSHFORWARD**. The proof does not assume the natural actor already has separated Rees rows or columns.

## 6. Exact finite evidence, including a genuinely new matrix

`frontier-20261028-unrestricted-five-base-rees-checker-v1.py`, SHA `346e118ef76b863d5c83e79cf5a619bd5f68c4ffc0771cb0aa62cf0a9231ef72`, executed `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 18:51:47 PDT 2026**, exit0:

```text
abstract local band: all16 selector tables, all12800 parameter laws, all corners regular
all81 2x2 allowed P matrices: 32400 source-product laws and actor-fibre injections
nontriangular/non-row-coded 45-source: natural actor=18 actual=8
PASS 2025 host products, retained-rectangle actual-q injection, 46^2 contexts/source
CONTROL forbidden entries 0,2 each yield explicit s^3=s^2!=s WEU violation
```

The last45-source uses

`P=((4,4,4),(4,1,1),(4,1,3))`.

It has a row containing1 and3, so is not row-coded. It also violates the previous triangular tag system: the two1 entries in row1 force the two nonzero columns to have the same tag, while row2's 1 and3 force those tags to differ. The checker exhausts all tag assignments, verifies this, checks all2025 source product equations, and directly establishes the natural18→actual8 actor collapse by every46² context per source. The retained-rectangle q-host is checked at that specific source.

All finite scripts are same-author; the general band/host argument in §§2–4 is written symbolically, not extrapolated from the finite matrices. No independent review, formal/kernel proof, all-original-source embedding, source-priority clearance or novelty conclusion is claimed.
