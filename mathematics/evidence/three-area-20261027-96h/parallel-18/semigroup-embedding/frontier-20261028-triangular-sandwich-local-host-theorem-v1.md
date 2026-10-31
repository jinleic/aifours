# Triangular signed sandwiches: a general locally regular-band Rees lift

**NEW AUTHOR WRITTEN + COMPLETE FINITE-PARAMETER-CHECKED CANDIDATE; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 18:48:16 PDT 2026**. Unlike the previous row-coded theorem, a row in this family may contain TWO DISTINCT entries of the same θ-value. This is a theorem about a specified Rees family, not arbitrary original sources, not a solution of either printed question and not a novelty claim. Its 700-case universal coefficient lemma is exact same-author code, not a human/independent/formal verification.

## 1. The family

Let A be the fixed five-element monoid

```text
0 1 2 3 0
3 2 1 0 1
0 1 2 3 2
3 2 1 0 3
0 1 2 3 4
```

with identity4 and pure group map `θ=(0,1,0,1,0):A→C2`. Let I and Λ be arbitrary nonempty sets. Choose bits `c_i∈{0,1}` for each source row i and `r_λ∈{0,1}` for each source column λ. Let P be ANY Λ×I A-valued matrix whose entries obey

- P_(λ,i)=4; OR
- `c_i≤r_λ`, and P_(λ,i)=1 if `r_λ XOR c_i=0`, or P_(λ,i)=3 if `r_λ XOR c_i=1`.

Equivalently the permitted nonidentity pairs `(r_λ,c_i,P_(λ,i))` are `(0,0,1)`, `(1,0,3)`, `(1,1,1)`. There is no requirement that all possible such entries occur. In particular one row with r=1 may contain both1 and3 in different columns; this violates the single-valued same-θ row premise of `frontier-20261028-row-coded-right-zero-rees-theorem-v1.md`, SHA `559f94ab0d3d89c47fedacddec031db86da84fae28b8fc71692c3579652f8410`.

**Claim.** The FULL Rees semigroup `S=M[A;I,Λ;P]` has an explicit faithful physical model over its natural actor `D=M[C2;I,Λ;θ(P)]` with a25-element locally regular band. This holds without a regularity assumption. If S is regular, then S is weakly E-unitary and locally r-orthodox. A sufficient regularity hypothesis is that every row and column contains 4. Under regularity, the explicit pure-actor pushforward in §4 yields a faithful host over the ACTUAL source q_τ and hence canonical κ_q injectivity and both same-q R/L obligations.

The hypotheses are sufficient only. The forbidden tagged active quadrant does not imply source nonembedding: it only falls outside the displayed coefficient law.

## 2. Fixed band and coefficient formula

Let B0 have multiplication

```text
0 2 2 4 4
0 1 2 1 4
0 2 2 2 4
0 3 2 3 4
0 4 2 4 4
```

Its local corners are `{0}`, `{1,2,4}`, `{2}`, `{2,3,4}`, `{4}`, each a regular band. It is not globally regular. Let `B=B0×B0` and let the C2 generator swap the two coordinates. This B is locally regular and has25 elements; its construction and all corner/action checks are independently stated at exact same-author scope in `frontier-20261028-ambiguous-source-local-band-host-v1.md`, SHA `a96cb3eeae75bba72af2cc43ff548785c74224fb7ed3509303a0f177cfb2feba`.

Set `u_0=1,u_1=3` and `v_0=4,v_1=0`. For source `(i,a,λ)` with c=c_i and r=r_λ, define

```text
a = 0       C = (2,v_r)
a = 1       C = (v_r,4)
a = 2       C = (4,v_r)
a = 3       C = (v_r,2)
a = 4       C = (u_c,v_r).
```

The source actor coordinate retains i,λ,θ(a). Within any given group fibre, this C separates the A middle coordinate: when θ=0, the first coordinates for a=0,2,4 are 2,4,u_c∈{1,3}; when θ=1, the second coordinates for a=1,3 are 4,2. Hence the resulting physical model will be injective once its multiplication is established.

## 3. Complete parameter-level multiplication lemma

For `s=(i,a,λ)` and `t=(j,b,μ)`, put `c=c_i`, `d=c_j`, `r=r_λ`, `m=r_μ`, `p=P_(λ,j)`, and `w=θ(a)+θ(p)` in C2. The required physical law is

`C(c,m; a p b) = C(c,r;a) · α_w(C(d,m;b))`.              (1)

All dependencies on possibly infinite I and Λ have disappeared: (1) only depends on `a,b∈A`, four bits c,d,r,m, and whether p is the identity or an allowed tagged nonidentity. There are exactly these seven `(r,d,p)` configurations:

```text
(0,0,4)  (0,1,4)  (1,0,4)  (1,1,4)
(0,0,1)  (1,0,3)  (1,1,1)
```

For each, c and m independently range over both bits and a,b over all5 elements. The literal A/B0/coefficient tables give **7×2×2×5×5=700** equations; the checker in §5 exhausts exactly those700 without floats, randomness or external packages, and all hold. This exhaustive finite parameter lemma proves (1) for ANY I,Λ and ANY P satisfying §1; it is not merely a test of a single selected source. The parent/source-dependent transition from (1) to the complete product formula uses no further enumeration.

The checker also evaluates the100 tagged cases with a nonidentity in the excluded quadrant `(r,d)=(0,1)`. Twenty of those100 violate (1). This negative control demonstrates the actual boundary of this coefficient table; it makes no universal claim about other B or coefficient choices.

Therefore `j(i,a,λ)=(C(i,a,λ),(i,θ(a),λ))` is a homomorphism to the physical whole host P(B,D), and the fibre argument in §2 proves it is injective.

## 4. Original source hypotheses and ACTUAL actor

Both nonidentity P entries1 and3 satisfy the reverse-fibre condition `a p a=a` for every a with `θ(a)=θ(p)^(-1)`; entry4 does too. Thus the natural actor is onto and pure. When S is regular, its weak E-unitarity follows by reflecting idempotence from the CS actor. The source is locally r-orthodox: in any local source monoid eSe, every idempotent maps into the identity of the local actor group, and its band coordinate lies in a regular local corner of B; faithfulness transfers idempotent closure and the regular-band identity. If each row and column has4, choose those unit sandwiches and a mutual inverse in A to obtain source regularity directly.

Do NOT assume the natural D is already the actual syntactic quotient. Since r is onto and pure, `τ_S=r^(-1)(τ_D)`. Its actual q is the pure quotient `D→D/τ_D` composed with r. The pure onto-CS actor pushforward in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, transports the faithful D-host to a faithful q-host, adding a rectangular-band factor `I×Λ` and transporting the group action via the local-group isomorphism. The new band remains locally regular. By the actual canonical free-band universal property, its κ_q is faithful, so the declared family has both R- and L-idempotent separation.

This actual-q conclusion names the preceding WRITTEN actor-transport input. If it fails review, retain the directly proved faithful natural-D host, and mark actual-q/canonical results **NR-PUSHFORWARD**; do not identify the actors by assertion.

## 5. Exact check and nonseparated-actor control

`frontier-20261028-triangular-sandwich-checker-v1.py`, SHA `1d6d3a117727846dfcfa5abb5e6a5bba3580c57910a5a046ec014a2aa79099c7`, ran at **Wed Oct 28 18:48:16 PDT 2026**, `/opt/homebrew/opt/python@3.14/bin/python3.14 -B`, exit0. It checks all700 permitted parameter equations and the excluded quadrant; its actual output is

```text
tag-law valid=700 excluded=100 excluded law failures=20
source=60 preliminary_actor=24 actual_actor=18
PASS all3600 source/r/q products, source-host laws, injection, retained rectangle
PASS actual tau, 61^2 contexts/source; actor pure
```

Its second case has four source rows, three source columns, column tags `(0,1,0,1)`, row tags `(0,1,0)`, and

`P=((4,4,4,4),(4,1,3,1),(4,4,1,4))`.

It is a full regular Rees source (every row/column contains4), with a row containing both1 and3. The preliminary 24-element actor merges two indistinguishable actor rows, giving the true 18-element q found by all61² contexts per source. A retained-rectangle q-host is checked directly on all60² products and same-q pairs. This is not a global claim that such P always yields separated rows or columns.

The earlier 45-element ambiguous-row source is another instance, with tags `(c_0,c_1,c_2)=(0,1,0)` and `(r_0,r_1,r_2)=(0,1,0)`; its explicit target has25 elements and its actual actor is already separated, as in the pinned source-host note. Neither finite example establishes novelty or settles arbitrary original sources.
