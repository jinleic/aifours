# f42 review — pure-CS product factorization and the bicyclic product host

Reviewer **MathOlson-2-2**; author **MathSemigroup-2**.
Actual native `/bin/date` before this write: **Wed Oct 28 17:40:23 PDT 2026**.

## 1. Verdict and exact scope

**0 FATAL / 0 MAJOR / 1 MINOR.**

The full all-variable product τ, same-actor canonical-faithfulness, SEP, separate R and L iff statements, and the explicit bicyclic×completely-simple host are reconstructed below at the stated classical cuts.
The product of arbitrary original sources is treated only when its FACTOR hypotheses are paid; the theorem does not prove that every original source decomposes or that an open factor is faithful.

**MINOR — count convention in candidate3 LF128.** Its bounded output says `same_q_pairs=82 R_pairs=12 L_pairs=12` without saying in that line that these are **ordered distinct-idempotent pairs**. My separately written bounded checker obtained those same counts when counting both orientations. Their unordered counterparts are41,6,6. Candidate1 LF118 explicitly describes the same sample as ordered; add that qualifier when quoting candidate3's standalone line. This is a reporting precision issue, not a mathematical contradiction.

The independently checked examples do not prove the universal theorem, establish an all-host obstruction, or constitute formal/kernel/human/independent-model-family or novelty acceptance. The printed book does not itself define the semidirect product in general; the current registered P/R cuts remain explicit.

## 2. Actual source frontier, prior familiarity and exact pins

I read the complete f42 assignment FIRST, then ALL THREE complete candidate bodies through their endings. Their live SHA256 values matched the assignment:

| Candidate | LF | SHA256 |
|---|---:|---|
| 1: `frontier-20261028-pure-group-product-stability-v1.md` | 124 | `6fb536e16d4b982f409509032bed3c6c7d355031bfa269930e22b968a4307af1` |
| 2: `frontier-20261028-two-actor-product-factorization-v1.md` | 128 | `341e2495c8f7dbbee3729c6f0f195e2013c4e373bb9e86278894c461982f517a` |
| 3: `frontier-20261028-bicyclic-completely-simple-product-v1.md` | 139 | `ec4c89451c3eebc52ed8b7af8a7e494ae956409b119ce0de7bc63855eb77e24a` |

The registered source definitions are those read in f10: `selection-v1.md` LF5–20 and the literal `book-excerpt.txt` LF13–49; the book defines WEU, local r-orthodoxy, seminormal band and its two questions. The f10 review is prior reviewer familiarity, not an accepted correctness premise.
For the used pure-CS actor and canonical construction, I reconstruct the supplied SQ-E proof and Rees/free-band steps explicitly in §§3–8. Candidate3's bicyclic factor is also reconstructed below, not imported from an old favorable verdict.

The finite 8×18 fixture is identified by the author's stated bounded-check description and its fixture declarations in `frontier-20261028-two-nonunital-product-checker-v1.py` LF15–26. I read those declarations to identify the exact fixture; my implementation below imports NO author code or result. The 18-element sandwich matrix is also printed explicitly in candidate3 LF111–116.
I have substantial prior same-author Semigroup/Preview review exposure, including f10. This is not blind or a historical noninfluence claim. No historical quarantined outcome or stopped assessment is treated as an accepted premise.

## 3. Exact ordinary assumptions and elementary pure-CS actor

For ANY nonempty regular source X, let E(X) be its idempotents and V(x) its actual mutual inverses. Define

`a τ_X b  iff  xay∈E(X) ↔ xby∈E(X) for every x,y∈X¹`,

where the two factors may be absent independently; no common identity is imposed on X.
The general two-factor theorem assumes the ACTUAL quotient q_X:X→X/τ_X is pure and completely simple. A pure map means its inverse image of the target idempotents is exactly E(X).

For original WEU+locally r-orthodox sources this actor premise follows from the source-specific SQ-E proof. Its relevant steps are: τ is a congruence and saturates E by the empty context; an idempotent quotient image of a has an actual idempotent representative `ata` for t∈V(a²), giving purity; WEU gives cyclic idempotence; local orthodoxy then makes local idempotents unitary; comparable source idempotents have identical all-context idempotence tests; quotient idempotents are primitive; and for quotient idempotents ε,φ, an inverse of εφ yields an element R-related to ε and L-related to φ. Hence the regular quotient is simple with a primitive idempotent, and is completely simple at the standard characterization.
These are the same direct equations reconstructed in my f10 return; they are used here as a named **source-specific SQ-E input**, not as a claim that any regular source automatically has a pure CS actor.

Classical cuts retained separately:

- Rees representation `D=M[G;I,Λ;P]` and its multiplication for a completely simple D, with arbitrary nonnormalized sandwich entries and arbitrary/noncommutative structure group;
- finite/infinite band-variety free objects and quotients by all mixed relations; closure of V under direct products;
- ordinary Green idempotent characterizations of R and L;
- elementary completely-simple/group-class and local-inverse facts used explicitly in the bicyclic application.

Their textbook source proofs are not all reproduced. No SZ87/McAlister embedding theorem, group-algebra proof, old held output or earlier review verdict is a correctness premise.

## 4. Critical Rees-context lemma, including independently absent contexts

Candidate1 LF34–44, candidate2 LF21–32, candidate3 LF39–61.
Let q:X→D be an ACTUAL onto pure map from regular X to completely simple D. Suppose all tests `xay∈E(X) ↔ xby∈E(X)` agree for ACTUAL x,y∈X.
Surjectivity supplies actual lifts of any actor contexts; purity makes those tests exactly the D-idempotence tests. Thus the actor images have equal ACTUAL two-sided tests.

Write `ā=(i,g,λ)`, `b̄=(j,h,μ)` in arbitrary `D=M[G;I,Λ;P]`, and define

`K_a(ν,k)=p_(ν,i) g p_(λ,k)`, `K_b(ν,k)=p_(ν,j) h p_(μ,k)`.

For fixed ν,k choose actual actor contexts `x=(a0,1,ν)` and

`y=(k, K_a(ν,k)^−1 p_(b0,a0)^−1, b0)`.

Then x ā y is the idempotent of its (a0,b0)-H-class. The matched test makes x b̄ y idempotent too; group cancellation yields `K_a(ν,k)=K_b(ν,k)`.
Conversely these equalities give all actual two-sided tests.

They also pay the missing one-sided tests, without assuming D or X unital:

- for right context `(k,v,b0)`, `ā y` is idempotent iff `K_a(b0,k)v=1`;
- for left context `(a0,u,ν)`, `x ā` is idempotent iff `uK_a(ν,a0)=1`.

For both contexts absent, if ā is idempotent then `g p_(λ,i)=1`. Equality of K at `(ν,k)=(μ,i)` gives

`p_(μ,i)=p_(μ,j) h p_(μ,i)`,

hence `p_(μ,j)h=1`, so b̄ is idempotent. Interchanging ā,b̄ gives the reverse. All equations retain noncommutative group order.
Purity transfers the now-complete D¹ test equivalence back to X¹. Thus the ACTUAL double-context tests do imply `a τ_X b` under precisely the pure-CS/onto assumptions.
This is the load-bearing nonunital bridge, not a fact inferred from a finite context sample.

## 5. Pure-group product: exact τ and actor

Candidate1 LF11–70. Let A be nonempty regular with an onto pure group homomorphism θ:A→G and let C have its actual onto pure CS q_C:C→D. First `τ_A=ker θ`.
If θ(a)=θ(b), every actual/absent contextual product has equal group image, so purity equates idempotence tests.
Conversely, if a τ_A b and a' is a mutual inverse of a, then a'a is idempotent; the actual left context a' forces a'b idempotent, so `θ(a)^−1θ(b)=1`.

For S=A×C, forward inclusion `kerθ×τ_C⊆τ_S` follows componentwise, because an actual pair is idempotent exactly when BOTH components are.
For the reverse choose a'∈V(a), c'∈V(c), and an actual e0∈E(A). With product contexts

`x=(a',c')`, `y=(e0,c'c)`,

the inserted `(a,c)` is idempotent: its A grade is1 and its C component is `(c'c)²=c'c`.
The τ-equivalent `(b,d)` insertion is idempotent too, forcing `θ(a)=θ(b)`.
Now keep the ACTUAL A contexts a',e0 and vary both C contexts over C: their A products are idempotent for both a,b by equal grade and purity, so the product tests imply all actual double C tests agree. Section4 upgrades these to c τ_C d.
Thus

`τ_(A×C)=kerθ×τ_C`, `q_(A×C)=(θ,q_C)`.

The quotient is pure componentwise. In Rees coordinates for D, `G×D` is the CS Rees matrix semigroup with structure group G×H and sandwich entries `(1_G,p_(λ,i))`; this multiplication is checked coordinatewise, not inferred from an arbitrary quotient slogan.
No identity in A or C was used.

## 6. Two pure-CS factors: exact τ of the actual direct product

Candidate2 LF10–50. Let nonempty regular S,T have ACTUAL onto pure CS quotients q_S,q_T. For U=S×T,

`τ_U=τ_S×τ_T`.

The forward inclusion is again componentwise.
For the converse suppose `(a,c) τ_U (b,d)`. Choose actual mutual inverses a',c' and use

`x=(a',c')`, `y=(a'a,c'c)`.

The insertion of `(a,c)` yields idempotents `(a'a,c'c)`, so the insertion of `(b,d)` is idempotent too. Hence the fixed actual T contexts c',c'c make BOTH c and d idempotent after insertion; the fixed S contexts do the same for a and b.
Pair arbitrary actual S contexts with the fixed T contexts. Equality of product tests now equals equality of the S tests alone. Section4 upgrades those tests to a τ_S b, including absent S contexts. Exchange S/T for c τ_T d.
No formal factor identity was inserted in U; all four chosen source context entries are actual elements.

The actual quotient map is `(q_S,q_T)`, onto and pure. The product of Rees actors is the CS Rees semigroup with product structure group, product row/column sets and coordinatewise sandwich entries. Thus item1 of candidate2 includes nonunital, infinite and one-element factors.

## 7. The canonical product-band map and sufficiency

Candidate1 LF72–94; candidate2 LF52–67.
For each pure-CS factor X, its canonical band B_X is the free V-band on ALL `X_(u,x)`, modulo EVERY mixed relation

`X_(u,x) X_(u w_X(x,y),y)=X_(u,xy)`.

Its group action is the shift in u and β_X(x) is the generator at1.
For U=S×T the actor structure group is G×H and its weight is the pair of actual factor weights.

`B_S×B_T` is a V-band, with componentwise G×H-action. Sending EVERY product generator to

`X_((g,h),(a,c)) ↦ (α^S_g β_S(a), α^T_h β_T(c))`

respects every mixed relation in both coordinates and all V identities/substitution contexts. Therefore it induces an equivariant homomorphism

`H_U:B_U→B_S×B_T`,
`H_U β_U(a,c)=(β_S(a),β_T(c))`.

No faithfulness, injectivity or onto property of H_U is presumed.
If both factor κ maps are injective and two κ_U images agree, apply H_U to their equal band parts and project the equal ACTUAL actor `(q_S,q_T)`. Each factor κ image agrees, so both source coordinates agree. Hence κ_U is injective.

The same map proves separate R, separate L and full same-q-idempotent SEP sufficiency: equal product β projects to equal factor β, equal q projects to equal factor q, and the corresponding idempotent Green equations hold componentwise. Apply the stated factor property independently in each coordinate.
No unsupported implication “R+L automatically imply SEP” or β-injectivity on all source elements is inserted.

## 8. Factor restriction and all reverse directions

Candidate2 LF69–99. A regular nonempty semigroup has an actual idempotent; choose e∈E(S),f∈E(T).
The maps `a↦(a,f)` and `c↦(e,c)` are semigroup embeddings because e²=e,f²=f. Neither e nor f is assumed to be a global factor identity.

In T's actor coordinates, an idempotent `q_T(f)=(j,p_(μ,j)^−1,μ)` has self-weight1. Hence

`β_U(ab,f)=β_U(a,f) α^U_(w_S(a,b),1)(β_U(b,f))`.

Restrict the product-band action to the subgroup G×{1}. The generator map

`X_(g,a) ↦ α^U_(g,1) β_U(a,f)`

respects ALL S relations and extends to an equivariant `H_S:B_S→B_U`, with `H_Sβ_S(a)=β_U(a,f)`. Similarly an actual e gives H_T.

If κ_U is faithful and κ_S(a)=κ_S(b), applying H_S to equal β and using equal ACTUAL q_S gives equality of κ_U(a,f),κ_U(b,f), hence a=b. Likewise for T.
If S has a same-q R-idempotent pair with equal β, its images under `a↦(a,f)` retain the R equations, equal actor and equal β_U, contradicting U's R separation. The L proof uses its own reversed equations; full SEP needs no Green relation. Both factors are handled by their respective restriction maps.

Together with §7 this proves, separately and in BOTH directions,

- `κ_U faithful ⇔ κ_S and κ_T faithful`;
- `SEP_U ⇔ SEP_S and SEP_T`;
- `R_U ⇔ R_S and R_T`;
- `L_U ⇔ L_S and L_T`.

These are properties of the actual canonical constructions at the displayed actor/presentation cuts. No factor is silently assumed faithful in the general two-actor theorem.

## 9. Pure-group specialization and genuine original-source closure

For candidate1, the extra assumption is an ACTUAL faithful A-host `ι_A(a)=(b_a,θ(a))` over the SAME pure group θ.
Take the product of its band B_A and the canonical band of C, with componentwise G×H-action. Each factor's ACTUAL multiplication identity supplies every product mixed relation and a canonical band map sending β_S(a,c) to `(b_a,β_C(c))`.
Since every A idempotent has grade1, injectivity of ι_A separates its idempotent band coefficients.
This pays C⇒A×C for R, L, SEP and κ separately, without requiring C's κ to be faithful when constructing the map.

For the reverse use an ACTUAL e0∈E(A), θ(e0)=1, and restrict at `(e0,c)` as in §8. This proves EACH product property iff the corresponding C property. The A-host is an essential hypothesis, not a theorem that every pure-group source has such a host.

Original-class closure is also paid directly: products of mutual inverses give regularity; `(e,f)(S×T)(e,f)=eSe×fTf` and its idempotents are the product of the two local regular bands. The regular-band identity holds componentwise.
If an actual source idempotent lies below another element in the printed natural order, its two actual idempotent witnesses project to the factors. Their WEU makes both components idempotent. Thus the product is WEU, even when global E is not a band.
No original group/semigroup is assumed decomposable into factors.

## 10. Complete bicyclic×completely-simple construction

Candidate3 LF10–119.
The bicyclic monoid Bic consists of N_0² with

`(i,j)(k,l)=(i+max(0,k−j), l+max(0,j−k))`.

Partial translations on N_0 prove associativity, `(j,i)` is the inverse of `(i,j)`, and diagonal pairs are its idempotents. Its actual pure group quotient θ(i,j)=i−j is onto Z; idempotence is exactly grade0. The independent symbolic proof and bounded check were supplied in my f10 review; the formulas used here are rederived below and no old verdict is transferred.

For ANY nonempty completely simple C, every idempotent corner is its H-class group. Thus Bic×C is regular and every idempotent corner is a product of an inverse monoid and a group, hence inverse and locally r-orthodox.
The natural order on a CS actor is equality: if u=fv=vg with f,g idempotent, its two equations force the row and column of u to equal those of v, and a Rees idempotent in v's row acts as a left identity on v. Purity of the actual product actor therefore gives WEU.
This is a LOCALLY INVERSE family; it is not claimed outside that broader known subclass.

The actual τ of Bic is kerθ: equal grade means equal idempotence in all actual/absent contexts; if a τ b, insert a mutual inverse of a on the left to force −θ(a)+θ(b)=0 in the additive group Z.
By §§4–5, the actual actor of Bic×C is `Z×(C/τ_C)`; no bounded context experiment is used to make that infinite claim.
C's own q_C is pure by regular idempotent lifting/saturation, and C/τ_C is CS by the same SQ-E input (C is WEU and locally a group). Its Rees representation is the named classical cut.

Let D be ALL integer upper tails A_i with intersection, R the rectangular band of the SOURCE C's rows/columns, and B=D×R.
Act by `(u,h)∈Z×H` via shifting the tail by u and fixing R; H acts trivially on B.
For `s=((i,j),(a,g,λ))` put

`b_s=(A_i,(a,λ))`, `q_S(s)=(i−j,q_C(a,g,λ))`.

For `t=((k,l),(b,h,μ))`, its actual actor weight shifts the tail by i−j and the rectangle product yields (a,μ). Thus

`b_s α_weight(b_t)=(A_i∩A_(i−j+k),(a,μ))`
`=(A_(i+max(0,k−j)),(a,μ))=b_(st)`.

This all-source relation gives an equivariant homomorphism from the FULL presented canonical band; it is not only a coherent-word statistic.
If the physical images of s,t agree, the tail and θ determine both Bic coordinates; the rectangle determines C's source row/column. Equal q_C and purity then separate the two elements in that SAME H-class group: multiply by the first's group inverse and use uniqueness of its idempotent.
Hence the actual host and κ_S are injective. On idempotents the band part alone distinguishes the Bic diagonal and the unique idempotent in each C row/column, so all source idempotents are separated, including same-q R/L pairs.

A nonorthodox C such as the displayed18-element Rees source makes the product's E nonclosed. The Bic factor's `(0,1)` is not in a subgroup (its unique mutual inverse does not commute with it), and a projection of a group is a group, so Bic×C is not completely regular/cryptogroup.
This does not create a nonembedding example: the explicit shifted host embeds it.

## 11. Independent finite full-context product check

I wrote `frontier-20261028-semigroup-product-independent-check.py`, importing NO author checker code. The finite fixture definitions are disclosed in §2; the checker independently computes actual and absent-context idempotence signatures.
Actual run:

```text
python3 -B frontier-20261028-semigroup-product-independent-check.py \
  --output frontier-20261028-semigroup-product-independent-check-results.json
```

It returned `PASS_INDEPENDENT_FULL_PRODUCT_CONTEXTS`:

- first/second factor sizes8 and18, both independently checked nonunital; product size144;
- ALL21,025 actual/absent two-sided product contexts per product element examined;
- factor τ-class counts2 and8, product16, with actual product τ equality iff the two factor signatures agree;
- 36 actual product idempotents, pure product actor;
- **ordered** same-actor distinct-idempotent counts364 total,84 R and84 L;
- explicit product rectangular-band plus actual actor is multiplicative and injective; global E is nonclosed;
- intentionally collapsing the first factor's row is detected as destroying host injection.

Checker SHA256 `a10816e1728221ddb5a462fef7d30a3457954c61b19112016598ea793af0136e`; saved result SHA256 `35eab84447419976191eaaad0f3c4c20bc7ccc1398469acee0ae05e6c46f0f42`.
This is an exact check of ONE 144-element fixture and its full finite contexts, not a proof for arbitrary S,T or an independent-model-family certification.

## 12. Independent bounded Bic×Rees check and count precision

I separately wrote and ran:

```text
python3 -B frontier-20261028-bicyclic-rees-independent-check.py \
  --output frontier-20261028-bicyclic-rees-independent-check-results.json
```

It imported NO author checker. It computed all361 actual/absent contexts per element of the finite18-element C; its τ had8 classes and was pure.
For72 bounded Bic×C labels it examined all5,329 actual/absent BOUNDED product contexts per label and found the predicted grade/finite-τ equivalence, actor purity and explicit host multiplication/injection. Bic products were never truncated to the input label box.
It found18 idempotents and **82 ordered** same-actor distinct-idempotent pairs, including12 ordered R and12 ordered L; E(C) nonclosure was directly checked. The wrong shift direction produced1,944 mismatches as an intended negative control.

This agrees with candidate3's output, but LF128's standalone `same_q_pairs`/`R_pairs`/`L_pairs` labels omit the word **ordered**. Record that as the one MINOR; halving them to unordered pair counts would not be a discrepancy in the same object.
Checker SHA256 `bddc4b62b53ad8d66af1090eb0c312547f39306cab922e2ee0094e47e1571383`; result SHA256 `dc9e4cab26d061f84a485b1ec65be1ff330029bf25c64933be76f999a9e0868b`.
Only a bounded Bic source/context set was explored. Section10, not this sample, is the asserted infinite proof.

## 13. Separate judgments and original-target boundary

| Claim | Written/finite judgment | Exact boundary |
|---|---|---|
| Rees actual-context→all-context lemma | Reconstructed, including both one-sided and empty contexts | Onto pure CS actor; arbitrary group/nonunital source |
| `τ_(A×C)=kerθ×τ_C` | Reconstructed | Pure onto θ, pure CS q_C and actual contexts; no common unit |
| Pure-group A×C faithfulness/R/L iff C | Reconstructed BOTH directions | A's faithful host over the SAME θ is an explicit hypothesis |
| `τ_(S×T)=τ_S×τ_T` | Reconstructed | BOTH actual pure CS quotient hypotheses; no automatic factorization for arbitrary congruences |
| κ/SEP/R/L factor equivalences | Full product map and two idempotent-restriction maps reconstructed | Four separate iff properties; no factor host presupposed in general theorem |
| Original-class product closure | Reconstructed | WEU/local-r/regular hypotheses in both factors; no global orthodoxy |
| Bic×CS explicit host and actor | Reconstructed for arbitrary finite/infinite C | Locally inverse subclass; nontrivial shift; no all-source result |
| Finite144-product and bounded Bic×Rees sample | Separate exact independent checks agree | One finite fixture and bounded Bic contexts respectively; not a general proof |
| Candidate3 pair-count label | **MINOR:** specify ordered pairs | 82/12/12 ordered =41/6/6 unordered; no numerical contradiction |
| Original all-source embedding / Question2 | **NOT_ESTABLISHED** | Arbitrary nonproduct and non-locally-inverse sources remain outside |

The direct product of already-faithful factors is faithful at the actual canonical level; an open factor stays open. This is NOT evidence of an original all-host collapse, universal embedding or arbitrary-source decomposition.
No external priority/novelty judgment was requested or made. The book's general semidirect-product convention and original source authentication remain separate from the chosen registered P/R product constructions.

Historical quarantined outcomes and failed reviews remain historical/unvalidated and are not accepted premises; this review neither retroactively validates nor erases them. No author contact, nested agent, external model/paid API, secret, deletion, Git push, publication or infrastructure mutation was used.
Same-harness written reconstruction and bounded exact scripts are not formal/kernel/human/configured-family acceptance.

**FINAL: 0 FATAL / 0 MAJOR / 1 MINOR — ORDERED PAIR-COUNT LABEL AT CANDIDATE3 LF128.**

**END OF COMPLETE f42 SCIENTIFIC REVIEW.**
