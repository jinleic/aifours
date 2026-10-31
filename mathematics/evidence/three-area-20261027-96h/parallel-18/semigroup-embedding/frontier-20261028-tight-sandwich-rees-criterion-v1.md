# Exact band-lift criterion for nonunit Rees sandwiches

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 17:57:45 PDT 2026**. This strictly extends the sufficient unit-sandwich construction in `frontier-20261028-unit-sandwich-rees-lift-v1.md`, SHA `8822d5ac2eeb8e50ee2e0d655b1a3619aa0f1ea43112caabb2083fb67b463747`: its added assumption `b_p=b_1` is unnecessary for units, and suitable NONUNIT sandwich elements can also be used. That earlier file remains frozen, correct at its stronger hypotheses, and is not edited. No original all-source solution or novelty is claimed.

## 1. An exact criterion, not a guessed unit normalization

Let A be ANY nonempty regular monoid with an onto group homomorphism θ:A→G and a faithful homomorphism

`ι_A(a)=(b_a,θ(a)):A→B⋊G`,

where B is a band in the actual local-regular-band variety V and G acts on B by automorphisms α. Write `e=b_(1_A)`; e is an idempotent of B but B need not have a global identity. The source identity yields, for EVERY a∈A,

`e b_a=b_a`,      `b_a α_(θ(a))(e)=b_a`.                     (1)

Call p∈A **tight for this given representation** when

`b_p=e α_(θ(p))(e)`.                                        (2)

**Exact equivalence.** For a fixed p∈A, the unchanged-band-coefficient lift identity

`b_(a p c)=b_a α_(θ(a)θ(p))(b_c)` for ALL a,c∈A              (3)

holds **iff** p is tight. Necessity is (3) with a=c=1_A. For sufficiency, expand the actual homomorphism and use (1):

`b_(a p c)=b_a α_(θ(a))(e α_(θ(p))(e)) α_(θ(a)θ(p))(b_c)`
`=b_a α_(θ(a)θ(p))(e b_c)`
`=b_a α_(θ(a)θ(p))(b_c)`.

Associativity and α's homomorphism property are the only manipulations. This is a necessary-and-sufficient criterion for THIS particular unmodified coefficient lift, **not** a claim that a nontight p forbids all other host constructions.

## 2. Every unit is automatically tight, but its coefficient need not equal e

If u is a unit of A, write `ι_A(u)=(b,g)` and `ι_A(u^(-1))=(c,g^(-1))`. The actual identity products give

`e=b α_g(c)=c α_(g^(-1))(b)`,  and `e b=b`.

Applying α_g to the second equality yields `α_g(e)=α_g(c)b`. Because B is a band,

`e α_g(e)=(b α_g(c))(α_g(c)b)`
`=b α_g(c) b=e b=b`.

Hence `b_u=e α_(θ(u))(e)`: **every unit is tight**. There is no general equality `b_u=e` unless extra action conditions hold, and none is used in (3).

The explicit finite experiment in §6 has an actual faithful A model with `b_(1_A)≠b_u` for a unit u. Thus a universal proof that simply normalizes all unit band coordinates to e would make an unsupported assumption; (2) is the correct general expression. It is a representation-dependent equality, not an assertion that every faithful model admits a global band identity.

## 3. Regular tight-sandwich Rees sources have explicit faithful hosts

Let I,Λ be arbitrary nonempty index sets and P=(p_(λ,i)) an A-valued matrix whose entries are **all tight** for the fixed representation. Form the FULL Rees matrix semigroup `S=M[A;I,Λ;P]`. Assume S is regular; a concrete sufficient condition, allowing nonunit entries, is proved in §4.

Its actor

`D=M[G;I,Λ;θ(P)]`

is completely simple, and the onto homomorphism `r(i,a,λ)=(i,θ(a),λ)` has an explicit physical source host

`j(i,a,λ)=(b_a,(i,θ(a),λ)) ∈ P(B,D)`.

For s=(i,a,λ), t=(j,c,μ), the actual source product is `(i,a p_(λ,j)c,μ)`. Its band coordinate is exactly (3), and its actor coordinate is the Rees product in D. Therefore j respects EVERY source product. If two images coincide, their Rees actor coordinates give the same row, column and θ-value, while the band coordinates agree; faithfulness of ι_A makes the middle A-elements equal. Thus j is injective.

The actor r is idempotent pure: in a physical band-by-CS host, an idempotent actor has self-weight1, so every element over it is idempotent; injectivity reflects idempotence to S. Therefore S is weakly E-unitary because natural order in D is equality. For any e∈E(S), the local monoid eSe is regular (e x' e is a mutual inverse of x whenever x∈eSe and x'∈V_S(x)). Each local idempotent maps to the single idempotent in the local actor group and to an element of the actual corner b_e B b_e. Products of these elements stay idempotent, and b_e B b_e is a regular band by B∈V. Injectivity transfers closure and the regular-band identity to E(eSe). Hence S is locally r-orthodox, not merely a formal source with an abstract actor.

Thus the ORIGINAL physical embedding for this declared subclass is explicit. Its source may be globally nonorthodox and need not be locally inverse. Nothing here identifies the entire registered presentation criterion with the whole printed problem.

## 4. Regularity is essential; row/column units suffice but not all-unit P

The tight criterion does **not** make a full Rees source automatically regular. If every row of P contains at least one unit of A and every column contains at least one unit, then S is regular: for s=(i,a,λ), choose an actual a'∈V_A(a), a column j with p_(λ,j) a unit and a row μ with p_(μ,i) a unit. The actual source element

`t=(j,p_(λ,j)^(-1) a' p_(μ,i)^(-1),μ)`

satisfies sts=s and tst=t by direct cancellation of only those two units. All other entries of P may be nonunits, provided they are tight. This is a SUFFICIENT condition, not a necessary classification of regular Rees matrices.

The counterexample in §6 has a tight nonunit p. If **all** sandwich entries are p, the corresponding finite60-element Rees semigroup contains s=(0,1_A,0) with no inverse: every middle product p a p has empty set-coordinate, while 1_A has a nonempty set-coordinate. Thus tightness alone cannot supply the original regular-source hypothesis. This is a precise failed inference about this proposed method, not an original-class nonembedding example.

## 5. The ACTUAL syntactic actor and both R/L obligations

The actor r in §3 is onto and pure, so for all s,t∈S,

`s τ_S t  iff  r(s) τ_D r(t)`,

by lifting actual actor contexts and using purity in both directions; absent source factors are handled as absent factors. Thus the true q_τ actor is the quotient map `f:D→D/τ_D` composed with r. No assumption that D's τ is equality is made.

The predecessor `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, proves at the **onto pure CS** cut that f induces isomorphisms on all local groups. In Rees coordinates, it explicitly transports the whole host P(B,D) injectively to a whole host over D/τ_D with band `(I×Λ)×B`, using row gauges and the transported group action; it reconstructs the required Rees-coordinate multiplication. The proof does not need the target band to have an identity or any coinduced power of B.

Composing this injective pushforward with j gives a faithful physical model over the SAME ACTUAL q_τ. Mapping each generator X_(u,s) of the canonical free V-band to the transported action of the physical band coordinate of s respects all mixed products and all V relations. Hence equality of two κ_q images would give equality in the faithful physical model, so κ_q is injective. Both same-q R-idempotent and same-q L-idempotent separation follow.

**Dependency boundary:** this actual-q conclusion depends on the preceding WRITTEN/UNREVIEWED pure-actor pushforward and its named Rees representation/CS-image facts. Sections1–4 already prove the faithful source host over r without it. If the named pushforward failed, only the original-r host is established here, and the actual-q conclusion is **NR-PUSHFORWARD**; the original-r host must not be relabeled as a canonical-q host without that step.

## 6. Genuine finite nonunit example and exact negative controls

Let `R^1` be a 2×2 rectangular band with an identity adjoined. Let H=C2 act by swapping both rectangular row and column indices and fixing the identity. Let `P({0,1})` be the four-element intersection semilattice, and let H interchange 0 and1. Put

`B=R^1×P({0,1})`,  `e=(1_R,{0})`,

with the componentwise H-action. B is a regular band and hence in V. Consider the local monoid `A=e(B⋊H)e`. Explicitly its15 elements are `(v,U,h)` where v∈R^1, `U⊆{0}` when h=0, and U=∅ when h=1, with multiplication inherited from B⋊H. Its identity is `1_A=(1_R,{0},0)` and θ is the H-coordinate. It is regular because B⋊H is regular and a local monoid of a regular semigroup is regular. The inclusion is a faithful band-by-group model.

The element `p=(1_R,∅,1)` is **not a unit**: every product p a or a p has empty set-coordinate, whereas 1_A has set-coordinate {0}; in particular `p²=(1_R,∅,0)≠1_A`. It is tight because `e α_1(e)=(1_R,∅)=b_p`. Take the2×2 P matrix with p in the lower-right entry and 1_A in the other three. Every row and column has a unit, so §4 applies; the 60-element FULL source is regular. Its actor sandwich matrix is `[[0,0],[0,1]]` over C2 and its syntactic congruence is equality by the K-array criterion in the previous unit-Rees note. Therefore this example's actual actor has8 elements; the original-r and actual-q models coincide, but the general result above does not rely on that special coincidence.

A separate same-author finite check, `frontier-20261028-tight-nonunit-rees-checker-v1.py`, SHA `0398f9ed436b7fdbe2be250d4f6f07db134bded4ec77c6e58ff2945cf3c70bee`, ran at **Wed Oct 28 17:56:34 PDT 2026**, timeout60s, exit0,1.84s:

```text
A_size=15 S_size=60 idempotents=35 actor=8
nonunit_p=(None, 0, 1) identity=(None, 1, 0) p_squared=(None, 0, 0)
same_q_idempotent_pairs=290 R_pairs=28 L_pairs=28
PASS tight nonunit, row/column units, regularity, local-r, WEU, nonorthodox
PASS all3721 contexts/source, actual actor, full host law/injection, R/L
CONTROL nontight sandwich fails 1-p-1 coefficient equation
```

For the SAME A, `frontier-20261028-tight-rees-regularity-control-v1.py`, SHA `f2b87646317c519fb5ff4f197b8ecddfcd7c7e72becc715da2e8d26528248b9e`, ran at17:57:05, exit0, and directly checked that with all four sandwich entries p, the source element `(0,1_A,0)` has zero mutual inverses. That separate60-element source is not an original regular source; it is a targeted **negative regularity control**, not a counterexample to embedding.

The distinct-unit-coordinate witness in §2 is checked by `frontier-20261028-unit-gauge-automatic-checker-v1.py`, SHA `60c24df9477d1db08f751a28d262e43744ff6a7c2216537ce182094c1c257d89`, run at17:55:05, exit0: its source A has10 elements, the two unit coefficients are `((0,0),None)` and `((0,1),None)`, and a40-element unit-Rees lift has16 same-q R and16 L ordered pairs separated. Omitting the sandwich group action was rejected in400 product cases. All checkers are same-owner code; no independent implementation/triple-witness verification is claimed.

## 7. Remaining original problem and assurance

The theorem genuinely adds all tight nonunit sandwiches subject to **actual source regularity**, but it does not claim every original weakly E-unitary locally r-orthodox semigroup has such a representation. Tightness is tied to the particular faithful A model and does not prove that nontight matrices or non-Rees sources are unembeddable. A no-go would require an actual original-class canonical collapse or an unrestricted all-host obstruction, not failure of this chosen lift.

Named mathematical inputs: ordinary Rees representation/completely-simple local group facts, band identities and the predecessor onto-pure-actor pushforward at its explicit scope. The present tight iff, automatic unit formula, physical homomorphism, row/column unit regularity and finite examples are independently written/checked here. No peer/independent-model/human/formal/kernel review, full-source priority or novelty clearance has occurred. Both the printed first question beyond this family and the printed second question remain open at this record's scope; earlier held outcomes are not accepted premises.
