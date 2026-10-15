# Finite residuals modulo a left-divisible semifilter

Date: 2026-10-14 PT. Scope: the exact independently stated Questions 2 and 3 on book page 62 (PDF page 78). This is the audited and revised written proof, not an assumption supplied to the formalization. Novelty and Lean coverage are separate gates. The notation below is deliberately different from the book's overloaded `R`.

## 1. Exact definitions and conventions

Let X be any finite alphabet, including the empty alphabet, and M = X* its free monoid. Its identity is the empty word ε. A language is an arbitrary subset of M. For u in M, put D_u A = {v in M : uv in A}. In particular D_ε A = A and D_v(D_u A) = D_(uv) A.

A left-divisible semifilter L is a family of languages satisfying:

1. M belongs to L.
2. If A,B belong to L, then (A Δ B)^c belongs to L.
3. If A belongs to L and u belongs to M, then D_u A belongs to L.

Complements are in M. There is no upward-closure axiom for a semifilter and no properness axiom in the source. A left-divisible filter has nonemptiness, intersection, upward closure, and all the same left quotients, in place of the semifilter closure axiom. Nonemptiness and upward closure give M in L. Intersection and upward closure imply axiom 2 because A intersection B is a subset of (A Delta B)^c.

For T subset M, the book's right congruence is

    u R(T,L) v  iff  {w in M : uw in T iff vw in T} belongs to L.

Write R_L for the class of T for which this equivalence relation has finitely many classes. Write Reg for the regular languages, equivalently languages with finitely many distinct left residuals.

Let V = {A^c : A belongs to L}. Regard a language as its characteristic series M -> F₂, and use + for symmetric difference. Then V contains 0, is closed under addition, and is closed under every D_u. Indeed, if B=A^c and C=H^c, then B+C=A+H, whose complement is in L; and D_u(A^c)=(D_u A)^c. The converse construction also holds. For the converse, from such a V define L={B^c:B in V}. Zero gives M in L; if A=B^c and H=C^c with B,C in V, then (A+H)^c=(B+C)^c belongs to L; and D_u(B^c)=(D_u B)^c belongs to L for **every** word u. Scalars in F₂ are 0 and 1, so additive closure and zero are precisely vector-subspace closure. Thus V is exactly a derivative-invariant F₂-vector subspace of all series. Moreover

    u R(T,L) v  iff  D_u T + D_v T belongs to V.                 (1)

This follows because the displayed agreement set is (D_u T + D_v T)^c. Relation (1) is reflexive, symmetric and transitive by the vector-space axioms. It is a right congruence because D_z(D_u T + D_v T)=D_(uz)T+D_(vz)T lies in V.

For such V, define C(V) to be the languages T whose residual cosets D_u T+V, u in M, form a finite set. Equation (1) proves R_L=C(V), not merely an analogy with it. More explicitly, for all T subset M and all u,v in M,

    {w in M : (uw in T iff vw in T)}
       = {w in M : 1_T(uw)+1_T(vw)=0}
       = (D_u T+D_v T)^c.

Complementation is an involution, so a language H belongs to L if and only if H^c belongs to V; this proves both directions of (1). The map u |-> D_u T+V is surjective onto its range, and its fibers are exactly the equivalence classes in (1). These classes are therefore in bijection with that range; finite index is **equivalent** to its finiteness. Derivative invariance makes the induced map D_z on the ambient quotient space well-defined: changing a representative by an element of V changes its derivative by an element of V.

The word u=ε contributes the coset T+V. The context w=ε is included in the agreement set: it belongs to that set exactly when u in T iff v in T. Membership of the entire agreement set in L need not force it to contain ε. Thus this congruence need not respect the accepting status of representatives; the error values at ε below account for that. D_ε is the identity, so the quotient axiom at ε adds no hidden nonemptiness restriction. Right invariance holds for every z, including ε.

## 2. Elementary closure facts

The following use actual finite sets of residual cosets, not a presumed automaton for T.

* V is contained in C(V): all residuals of B in V have the single coset V.
* Reg is contained in C(V): a finite residual set has a finite image modulo V.
* C(V) is closed under addition: residual cosets of S+T are sums of one residual coset of S and one of T, a subset of a finite Cartesian product's image.
* C(V) is closed under D_z: D_u(D_z T)=D_(zu)T, so its residual cosets are a subset of those of T.
* If V is contained in W, then C(V) is contained in C(W), by mapping cosets to coarser cosets.

Thus C(V) itself is a derivative-invariant F₂-vector subspace. Since the all-words language M is regular, C(V) is also closed under complement. We do NOT assert closure under intersection for arbitrary semifilters.

## 3. Parity concatenation and the derivative split

For languages A,B, define their parity product A ⊙ B by

    1_(A ⊙ B)(w) = sum_(w=uv) 1_A(u) 1_B(v) in F₂.

There are exactly |w|+1 cuts, so this definition involves only a finite sum even for infinite languages. Products are associative and bilinear: expanding either association yields the same finite sum over triples z=u v t for each fixed word z, and finite sums distribute in F₂. Thus a coefficient of A a B counts the positions of a distinguished occurrence of a, with prefix in A and suffix in B. For a letter a, write A a B for A ⊙ {a} ⊙ B. This is NOT ordinary existential concatenation: two accepting cuts cancel. All sums of languages below are in F₂.

For every word x, regular or nonregular languages A,B, and letter a, one has

    D_x(A a B) = (D_x A) a B + sum_(x=uav, u in A) D_v B.      (2)

Proof: fix arbitrary x,y in M and a in X. Index the coefficient on the left by all triples (r,a,b) with xy=rab, weighted by 1_A(r)1_B(b). The index has at most |xy| elements; cuts with weight zero may be discarded. Exactly one of the following disjoint alternatives holds:

* |r| >= |x|: the common-prefix property for lists gives a unique r' with r=xr'. Cancellation of x gives y=r'ab. Conversely every cut y=r'ab gives the unique cut xy=(xr')ab of this type. Its weight is 1_(D_x A)(r')1_B(b). In particular |r|=|x| belongs here: the distinguished a is the first letter of y.
* |r| < |x|: since lengths are integers, |r|+1 <= |x|. The distinguished a is inside x, and the common-prefix property gives a unique v with x=rav and b=vy. Conversely each cut x=rav together with the fixed y gives exactly one cut xy=ra(vy). Its weight is 1_A(r)1_B(vy), the coefficient of D_v B at y when r belongs to A. The boundary v=ε, where a is the last letter of x, is included.

Every factorization is counted once, with its multiplicity retained modulo 2. This proves (2) coefficientwise. For x=ε the second sum is empty and the first term is A a B.

If A is regular and B belongs to V, the second sum in (2) belongs to V. There are finitely many D_x A. Hence A a B belongs to C(V).

More generally, if A is regular and B belongs to C(V), then A a B belongs to C(V). To see this without assuming what is to be proved, choose representatives b₁,...,b_m for the finitely many residual cosets of B modulo V. Every finite sum of residuals D_v B is congruent modulo V to one of the at most 2^m subset sums of these representatives. The first term in (2) takes only finitely many values, one for each residual of A. Consequently (2) puts all residual cosets of A a B into a set of cardinality at most

    (number of residuals of A) × 2^m.                         (3)

This argument also proves closure for **unmarked** regular-left parity products A ⊙ B. Its derivative identity is

    D_x(A ⊙ B) = (D_x A) ⊙ B
                  + sum_(x=uv, |u|<|x|, u in A) D_v B.     (2u)

To prove it, partition the cuts xy=rb at |r| >= |x| versus |r| < |x|. In the first case r=xr' and y=r'b uniquely; in the second x=rv and b=vy uniquely, with v nonempty. The strict inequality prevents counting the cut r=x twice. Conversely both constructions recover exactly their respective original cuts. For x=ε the second sum is empty. This proves (2u) coefficientwise with multiplicities. The first term again has at most as many values as A has residuals, and the correction has at most 2^m cosets. Therefore A ⊙ B belongs to C(V) whenever A is regular and B belongs to C(V).

Take V={0}. A regular B has m actual residuals, so the same bound proves that A ⊙ B and A a B are regular when both A and B are regular. This is a finite-residual proof of parity-product regularity. It never replaces parity products by existential language products. Finite F₂ sums of regular languages are regular because the residual of a sum is the sum of the residuals, so the residual set is contained in the finite Cartesian-product image. Complements are regular as well: D_x(H^c)=(D_x H)^c.

## 4. Finite-state elimination / normal form

**Theorem 1 (normal form).** For every finite alphabet X and every derivative-invariant F₂-vector subspace V,

    C(V) = { K + sum_(i=1..n) A_i a_i B_i :
             n >= 0, K,A_i in Reg, a_i in X, B_i in V }.       (4)

If X is empty, n must be zero; then M={ε}, and all languages are regular.

The right-to-left inclusion follows from Section 2 and the first consequence of (2). For the other inclusion, let T belong to C(V). Let Q be the finite set of equivalence classes of (1), let q(w) be the class of w, and let q₀=q(ε). Right invariance gives the deterministic transition δ(q(w),a)=q(wa). Choose one representative r_q for each class, specifically r_(q₀)=ε. This is possible even when the initial class contains other words. Put

    S_q = D_(r_q)T,
    E_(q,a) = D_a S_q + S_(δ(q,a)),
    c(q) = 1_(S_q)(ε).

Since r_q a and r_(δ(q,a)) are equivalent in (1), E_(q,a) belongs to V. No regularity of E_(q,a) is presumed; it follows only under the extra hypothesis V subset Reg in Question 2.

For every q,a and suffix v the exact recurrence is

    S_q(av) = S_(δ(q,a))(v) + E_(q,a)(v).                     (5)

We eliminate (5) by the following strengthened induction, simultaneously for **every** starting state p. For w=a₁...a_k set p_0=p and p_i=δ(p_(i-1),a_i). The assertion is

    S_p(w) = c(p_k)
             + sum_(i=1..k) E_(p_(i-1),a_i)(a_(i+1)...a_k).  (6p)

Base k=0: w=ε, the sum is empty, p_k=p, and the identity is the definition S_p(ε)=c(p). For the induction step, write w=av with |v|=k and put p'=δ(p,a). Equation (5) gives S_p(av)=S_(p')(v)+E_(p,a)(v). Apply the induction hypothesis at the state p' to v. Its terminal state is p_(k+1), and its error terms are exactly positions 2,...,k+1 of w. Adding E_(p,a)(v) supplies position 1. This proves (6p) for all states and length k+1. Every sum is finite, so reordering is legitimate.

Now take p=q₀, noting that the enforced choice r_(q₀)=ε gives S_(q₀)=T. With q_i=δ*(q₀,a₁...a_i) we obtain

    T(w) = c(q_k) + sum_(i=1..k) E_(q_(i-1),a_i)(a_(i+1)...a_k). (6)

This eliminates the recurrence for every word; it does not assume an infinite-series inverse or any convergence. The simultaneous-state induction is essential because the first step changes the starting state.

For each q, let A_q={u:δ*(q₀,u)=q}; this is regular, recognized by the finite deterministic automaton (Q,δ,q₀,{q}). Let K={w:c(δ*(q₀,w))=1}; it is recognized by the same automaton with final states {q:c(q)=1}. Group the sum in (6) by the state immediately before its distinguished letter and by that letter. The result is the series identity

    T = K + sum_(q in Q, a in X) A_q a E_(q,a).               (7)

Indeed the coefficient at w of A_q a E_(q,a) sums exactly the positions i in (6) having q_(i-1)=q and a_i=a. The sets Q and X are finite, so (7) has finitely many terms. Its value at ε is K(ε)=c(q₀)=T(ε), while every error product vanishes at ε. This proves (4) for every word, not just a finite prefix. Different choices of noninitial representatives can change K and the errors but cannot change identity (7).

## 5. Exact answer to Question 2

**Theorem 2 (all semifilters).** For every finite alphabet X and every left-divisible semifilter L on X*,

    R_L = Reg  iff  every member of L is regular.             (8)

Equivalently the condition is V subset Reg.

Necessity: V subset C(V)=R_L, so R_L=Reg forces V subset Reg. Complements of regular languages are regular, so this is equivalent to L subset Reg.

Sufficiency: if V subset Reg, all factors B_i in (4) are regular. Section 3 proves every parity product A_i a_i B_i regular, and finite sums remain regular. Thus C(V) subset Reg. The opposite inclusion always holds.

This is not a reformulation of finite index: the criterion examines only the members of the input family L and their ordinary regularity. It also gives the largest qualifying semifilter, namely L=Reg itself. Reg is a semifilter because it contains M and is closed under complement, symmetric difference and all left quotients. Therefore a language has finitely many residuals modulo regular languages if and only if it is regular.

**Theorem 3 (all filters).** For a left-divisible filter L,

    R_L = Reg  iff  every member of L is cofinite.            (9)

For filters V is an ideal of languages. To check this directly, if B=A^c belongs to V and H subset B, then H^c contains A, so upward closure gives H^c in L and hence H in V. If B,C belong to V, then B^c,C^c belong to L, their intersection belongs to L, and its complement B union C belongs to V. Conversely an ideal containing the empty language gives a nonempty upward-closed intersection-closed filter by these same identities. Derivative invariance is carried across complementation in either direction. If all its members are finite, they are regular: for a finite B, every nonempty residual is supported on the finite set of suffixes of words of B, so there are finitely many residuals. Thus (8) applies. If it contains an infinite language B, enumerate the regular languages as K₀,K₁,... (finite deterministic automata over a finite alphabet have a countable set of finite descriptions), and choose distinct b₀,b₁,... in B. Define H={b_i:b_i not in K_i}. Then H differs from K_i at b_i for every i, so H is nonregular. But H subset B implies H belongs to V, contradicting (8). This proves (9). If X is empty, no B can be infinite and the statement remains true, including the improper filter.

A concrete complete parametrization of the filters in (9) is useful. For any suffix-closed set U subset M (D_x U subset U for all x), set

    L_U = {A subset M : A^c is a finite subset of U}.          (10)

The complementary family V_U={F:F finite and F subset U} contains the empty language, is downward closed, and is closed under finite unions. For any word x and F in V_U, the map v |-> xv is injective by cancellation in the free monoid, so D_x F is finite; suffix closure gives D_x F subset U. Thus V_U is derivative-invariant, and its complementary family (10) satisfies every filter axiom, including quotients by ε. No regularity of the possibly infinite U is required. Every filter satisfying (9) has this form: let U be the union of V. Downward closure puts {u} in V for each u in U, and finite-union closure then puts every finite subset of U in V. Thus V is exactly the finite subsets of U; derivative invariance makes U suffix-closed: if xv belongs to U, downward closure gives {xv} in V, and D_x{xv}={v} belongs to V, so v belongs to U. This also proves uniqueness of U, since U can be recovered as {u:{u} in V}.

Examples answering the book's request for other L include U={words of length < n}, n>=1, giving the filter of all languages containing every word of length at least n. U=empty gives {M}; U=M gives the known cofinite filter. The semifilter Reg is generally not a filter: for a nonempty alphabet it contains the empty language but does not contain every language. For a unary alphabet {a}, suffix-closed U are exactly the empty set, {ε,a,...,a^(n-1)} for n>=1, and all of M: suffix closure makes the allowed lengths a downward-closed subset of the natural numbers. These give precisely the finite-threshold filters, {M}, and the cofinite filter in the unary filter case. The general semifilter argument makes no assumption of two distinct letters.

For the empty alphabet, M={ε}; all its languages are finite and regular. Its derivative-invariant subspaces are {0} and the entire one-dimensional F₂ space, so its semifilters are {M} and P(M), both filters. In (10) these correspond to U=empty and U=M. In particular the improper filter P(M) qualifies here. For any nonempty finite alphabet, M is infinite and has a nonregular subset by the diagonal construction above; the improper filter P(M) has V=P(M), has universal source congruence for every T, and recognizes all languages, so it does not qualify. Thus improper filters have not been silently excluded. None of these examples is claimed new.

## 6. Exact answer to Question 3

**Theorem 4 (saturation).** C(C(V))=C(V).

The inclusion from right to left follows from V subset C(V) and monotonicity. For the reverse inclusion, C(V) satisfies all vector-space and derivative hypotheses by Section 2. Apply Theorem 1 with C(V) as the error space. Every resulting summand is A a B with A regular and B in C(V), so (3), not an unproved closure assertion, puts it in C(V). The regular term and finite sum also belong to C(V). This proves the reverse inclusion. The finite alphabet is used in (7), and finiteness of F₂ is used in the 2^m bound in (3).

**Theorem 5 (generator test).** Given any two left-divisible semifilters L₁,L₂, set V_j={A^c:A in L_j}. Then

    R_(L₁)=R_(L₂)
        iff V₁ subset C(V₂) and V₂ subset C(V₁).              (11)

Necessity follows from V_j subset C(V_j). If V₁ subset C(V₂), monotonicity and Theorem 4 give

    C(V₁) subset C(C(V₂)) = C(V₂).

Apply the symmetric condition for the opposite inclusion. This proves (11), without testing every possible recognized language.

To avoid a criterion stated in terms of the very classes being compared, expand (11) using (4). An equivalent answer with no generalized finite-index predicate at all is:

> For each ordered pair (j,k)=(1,2),(2,1), and every A in L_j, there exist an integer n>=0, regular languages K,A₁,...,A_n, letters a₁,...,a_n in X, and languages H₁,...,H_n in L_k, such that
>
>     A^c = K + sum_(i=1..n) A_i a_i H_i^c.                 (12)
>
> All products and sums in (12) are parity products and F₂ sums.

The finite length n may depend on the language and the direction (j,k); there is no uniform bound or restriction on n. All error tails H_i^c belong to the other complementary family, and need not be regular. For the empty alphabet no letters can be chosen, so the expressions have n=0, and every language is an eligible regular K; hence the equality test always holds, as it should.

This is a mutual finite-expression generation criterion on the two input families, not a restatement that all arbitrary T have the same finite-index behavior. It is not asserted to be a decidable algorithm for arbitrarily specified infinite families. If V_j is given by a generating set G_j under finite sums and left quotients, it suffices to check (12) for B in G_j rather than every B in V_j: C(V_k) is closed under precisely those operations. In particular finitely generated presentations reduce to finitely many finite-expression membership obligations.

Theorems 4 and 5 cover filters as well, with no extra hypothesis and without weakening the semifilter case. Question 3 does not require L₁=L₂; for example {M}, the cofinite filter, and the semifilter Reg all give the same class Reg.

## 7. Scope and prior-art boundary

The exact Q2 and Q3 have the written all-parameter answers (8)–(12), supported by the proofs above. Kernel verification covers only the expressly identified statements in Formal.lean and claims.json; it must not be read as formal certification of every step in this text. Questions 4 and 5, which concern general semigroups and two-sided contexts, are not claimed solved. General semifilter classes were not assumed Boolean algebras: the original Prodinger paper imposes filter hypotheses for its intersection proof in Section 5, and that distinction matters.

The 2010 Guo–Wang–Shum survey was recovered from the publisher. Its Theorems 3.3 and 3.4 give Q2/Q3-type answers for the specific suffix-generated filters; Theorem 2.7 records the already-known cofinite result. It does not supply the general-semifilter criterion (8) or (12) in its seven pages. This observation alone does not establish novelty. Full-text comparison with the 2017 Burnside application, the 2024 monograph, and any later paper on arbitrary semifilters remains required. A proof can be correct even if it is a reproduction; no discovery claim is made here.


## 8. Direct finite-span mechanism behind the formalization

This is an additional proof route for the regularity and saturation steps, not an assumption of normal form. Work first in a vector space H over F₂ with linear letter transitions d_a. For a word w, d_w means read its letters from left to right, so d_(uv)=d_v composed with d_u. A vector is locally finite if its actual orbit {d_w h:w in M} is finite.

Let Q and X be finite, S_q in H, and delta a deterministic transition. Suppose each of the finitely many transition errors e_(q,a)=d_a S_q-S_(delta(q,a)) has finite orbit. Form the finite set

    G={S_q:q in Q} union union_(q,a) {d_w e_(q,a):w in M}.

Its F₂ span P is a finite set (at most 2^|G| vectors). Each d_a maps every generator into P: a state vector maps to a state vector plus its error, and a derivative of an error maps to another derivative of that error. Linearity extends this to d_a P subset P. Induction on word length puts every d_w S_q in P. Hence every S_q has finite orbit. This argument also works over any finite ring for modules.

More generally let pi:H->J be a linear map commuting with the letter transitions. Suppose every vector in ker(pi) is locally finite and pi(t) has finite orbit. Choose one word r_q for each element q of that finite orbit, using ε for pi(t), and put S_q=d_(r_q)t. Set delta(q,a)=d_a q. Then pi(S_q)=q, every transition error lies in ker(pi), and S_initial=t. The preceding finite-span argument proves that t has finite orbit. Neither normal form nor saturation is a hypothesis.

Local finiteness is closed under sums and scalars, by finite Cartesian-product images, and under each letter transition, by taking a subset of the original orbit. Thus it forms an invariant subspace LF(H). For an invariant V in H, C_H(V) is the preimage of LF(H/V) under the quotient map; by intertwining this is exactly finiteness of {d_w t+V:w in M}. It is not defined by finite expressions.

The lifting theorem gives C_H(V)=LF(H) iff V subset LF(H). It also proves saturation directly: for W=C_H(V), apply the lifting theorem to H/V -> H/W. Every kernel vector is locally finite in H/V by the definition of W, while membership t in C_H(W) says its image in H/W has finite orbit. Therefore t belongs to W. The reverse inclusion follows from extensivity and monotonicity. The mutual-inclusion test then follows as in (11).

For H=(X*->F₂) and d_a f(v)=f(av), ordinary local finiteness is exactly ordinary language regularity. Formal.lean connects characteristic functions and actual residual orbits to Mathlib's Language.leftQuotient and its Myhill-Nerode theorem. The complement translation, parity normal form, and the original-family finite-expression version (12) retain precisely the written/formal distinction recorded in RESULT.md.


## 9. Source audit and dispositions

The following checks use the supplied lawful local copies and page images rather than OCR equations. The requested book wording is fixed by TASK.md; a separate scan of book page 62 is not present in this repository, so no claim of rechecking that scan is made.

| Source or issue | Image-checked evidence | Disposition |
| --- | --- | --- |
| [Prodinger 1980](sources/prodinger1980.pdf), pp.36-37 | The operation is (A Delta B)^c; Definition 2.2 has M in L and quotients by all words; Definition 2.3 uses the right-context agreement set. | Used as the source definition, with ε and no added upward closure or properness. |
| Prodinger 1980, pp.43-44 | The sentence imposing FD'/FD hypotheses precedes Lemmas 5.3/5.4 and Theorem 5.6. The intersection proof uses both intersection and upward closure. | Boolean closure is not imported for general semifilters. |
| [Guo-Wang-Shum 2010](sources/guo-wang-shum2010.pdf), pp.2-4 | Theorem 2.7 records the cofinite result; Theorems 3.3/3.4 treat suffix-generated special families. Theorem 2.4 states Boolean closure under semifilter hypotheses. | Special-case results are prior art; the broader Boolean assertion is not used. |
| Guo-Wang-Shum 2010, pp.5-7 | Further results concern product-monoid/ps-set special families; the conclusion describes difficulty with general semifilters. | No inference of novelty or mathematical impossibility is drawn from this wording. All seven pages were inspected. |
| Candidate recurrence elimination | The induction must quantify over every state, since a leading letter changes state. | Replaced the terse initial-state assertion with (6p) and its complete length induction. |
| Candidate parity closure | Sums of residuals of B in C(V) lie in their finite quotient span, not necessarily V. | Retained and justified the at-most-2^m coset bound; added the unmarked product proof (2u). |
| Candidate filter classification | Upward closure applies only to filters; infinite complements require an arbitrary-subset argument. | Supplied ideal duality, diagonal construction, full source-axiom checks for L_U, and explicit boundary cases. |
| DOI 10.1142/S1793557117500450 (2017) and DOI 10.1007/978-981-99-9171-6_3 (2024) | Primary full texts are not in this checkout and have not been compared here. | Novelty unresolved; external investigation belongs to the assigning agent. |
