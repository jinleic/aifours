# Canonical R/L separation and faithfulness factorize over products of pure-CS sources

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 17:32:57 PDT 2026**. This strengthens `frontier-20261028-pure-group-product-stability-v1.md` from one pure-group factor to **two arbitrary pure completely-simple syntactic actors**, and removes the earlier premise that either factor's canonical host is already faithful. It does not edit or retroactively adopt that earlier note. No novelty or original all-source solution is claimed.

## 1. Exact theorem

Let S and T be ANY nonempty finite or infinite regular semigroups. For each factor, let τ be its source-defined congruence

`a τ b` iff for every `x,y∈S¹`, `xay∈E(S)` exactly when `xby∈E(S)`,

and analogously for T. Assume the ACTUAL quotient maps `q_S:S→D_S=S/τ_S` and `q_T:T→D_T=T/τ_T` are idempotent pure and D_S,D_T completely simple. These hypotheses hold for every original weakly E-unitary locally r-orthodox source by the exact SQ-E argument recalled in §8. Let `B_S,β_S,κ_S` and `B_T,β_T,κ_T` be their actual canonical V-band constructions; let U=S×T have its own actual τ_U, q_U and canonical `(β_U,κ_U)`.

**Theorem — product factorization.**

1. `τ_U=τ_S×τ_T`, and the actual pure completely-simple actor is `q_U=(q_S,q_T):U→D_S×D_T`.
2. `κ_U` is injective **iff** `κ_S` and `κ_T` are both injective.
3. For the full same-q-fibre idempotent SEP condition, U satisfies SEP **iff** both factors do. The same equivalence holds separately for the same-q **R-idempotent** condition and separately for the same-q **L-idempotent** condition.
4. If S and T satisfy the original weak-E-unitary locally-r-orthodox hypotheses, so does U. Hence this is an exact reduction for genuine original-class products, including nonunital/nonorthodox/infinite factors.

There is NO assumed faithful factor host and neither implication is a finite-sample inference. The theorem reduces a decomposable source to its actual factors; it does not assert that every original source decomposes, prove either factor's obligations or furnish an all-host counterexample.

## 2. Actual two-sided contexts detect the whole syntactic quotient

We first prove a lemma used in the product τ calculation. Let R be any nonempty regular semigroup with an onto idempotent-pure q:R→D, where D is completely simple. If two elements c,d∈R have matching idempotence tests `xcy` versus `xdy` for all **actual** x,y∈R, then they have matching tests for all x,y∈R¹, including independently absent factors.

Purity and surjectivity transfer the actual two-sided tests to all actual x,y in D. Choose arbitrary Rees coordinates `D=M[H;I,Λ;P]`, c-bar=(i,g,λ), d-bar=(j,h,μ), and define

`K_c(ν,k)=p_(ν,i)g p_(λ,k)`, `K_d(ν,k)=p_(ν,j)h p_(μ,k)`.

For every ν,k choose actual x,y with group coefficients making `x c-bar y` the idempotent in any fixed H-class. The matching test forces `K_c(ν,k)=K_d(ν,k)` by group cancellation. Conversely these equalities give all actual two-sided tests. They also give each left- or right-absent test: for y=(k,v,η), c-bar y is idempotent iff `K_c(η,k)v=1`; for x=(a,u,ν), x c-bar is idempotent iff `u K_c(ν,a)=1`.

For both factors absent, if c-bar is idempotent then `g p_(λ,i)=1`. K equality at `(ν,k)=(μ,i)` gives `p_(μ,i)=p_(μ,j)h p_(μ,i)`, hence d-bar is idempotent; the reverse interchanges c-bar,d-bar. Thus the two actor elements have identical D¹ tests. Purity carries every such test back to R¹, proving c τ_R d. This covers arbitrary noncommutative H, nonnormalized P and nonunital R; no common identity is inserted into the source.

## 3. Prove τ_(S×T)=τ_S×τ_T

The reverse inclusion is immediate: if a τ_S b and c τ_T d, then for any actual product contexts, or either whole factor absent, the idempotence test in each component agrees; a pair is idempotent iff both components are idempotent.

Conversely suppose `(a,c) τ_U (b,d)`. Pick actual mutual inverses a'∈V_S(a), c'∈V_T(c). The ACTUAL product contexts

`x=(a',c')`,     `y=(a'a,c'c)`

make `x(a,c)y=(a'a,c'c)` idempotent. Thus `x(b,d)y` is also idempotent; in particular the SAME T-contexts c',c'c make both c and d idempotent after insertion, and the SAME S-contexts a',a'a do so for a and b.

Now pair arbitrary actual S-contexts x_S,y_S with the fixed common T-contexts: the product tests imply `x_S a y_S∈E(S) iff x_S b y_S∈E(S)`. Section 2 upgrades this to a τ_S b. Interchange the factors to get c τ_T d. This proves τ_U equality without multiplying by a formal unit or assuming a common identity for either factor.

Both q_S and q_T are onto; therefore q_U=(q_S,q_T) is onto D_S×D_T and its kernel is τ_U. It is pure because a product pair is idempotent exactly when both components are, and each q_i is pure. If `D_S=M[G;I,Λ;P]` and `D_T=M[H;J,M;Q]`, then D_S×D_T is the completely simple Rees semigroup

`M[G×H; I×J, Λ×M; ((p_(λ,i),q_(μ,j)))]`.

The isomorphism and multiplication are coordinatewise. Rees representation is an explicitly named ordinary structural import; no embedding theorem is imported.

## 4. A universal product-band homomorphism

Let the canonical action on B_S be α^S:G and that on B_T be α^T:H. Because V is defined by band identities, `B_S×B_T∈V`; let `(g,h)` act componentwise. The actual actor weight for `(a,c),(b,d)` is precisely the pair of the two actor weights.

For every product generator define

`X_((g,h),(a,c)) ↦ (α^S_g β_S(a), α^T_h β_T(c))`.

The canonical M relation in each factor proves all product M relations. The target is a V-band, so all its identity substitutions and all outer contexts hold. This gives an equivariant homomorphism

`H_U:B_U→B_S×B_T`,
`H_U β_U(a,c)=(β_S(a),β_T(c))`.                           (3)

This is an all-derivation quotient invariant. It is well-defined whether or not either κ is injective, and no claim is made that H_U itself is injective or onto.

If κ_S and κ_T are injective and κ_U(a,c)=κ_U(b,d), applying H_U to the band coordinate and using q_U=(q_S,q_T) yields κ_S(a)=κ_S(b) and κ_T(c)=κ_T(d). Both factors are equal, so κ_U is injective. This proves the forward half of item 2.

## 5. Reverse factor maps without a global identity

Choose actual idempotents e∈E(S), f∈E(T), which exist by regularity. The maps `a↦(a,f)` and `c↦(e,c)` are semigroup embeddings into U. Write `q_T(f)=ε=(j,p_(μ,j)^(-1),μ)` in the T-actor's chosen Rees coordinates. Its self-weight is `p_(μ,j)^(-1)p_(μ,j)=1_H`.

The full canonical multiplication for `(a,f)(b,f)=(ab,f)` therefore reads

`β_U(ab,f)=β_U(a,f) α^U_(w_S(a,b),1_H)(β_U(b,f))`.

Restrict the product band action to `G×{1_H}`. Mapping every S-generator by

`X_(g,a) ↦ α^U_(g,1_H)(β_U(a,f))`

respects every S mixed relation and every V identity. It gives an equivariant homomorphism `H_S:B_S→B_U` with `H_Sβ_S(a)=β_U(a,f)`. There is no claim that f is a source identity; f²=f is exactly what this construction requires.

Similarly, with q_S(e) an idempotent of D_S, its Rees self-weight is1_G. Restricting to `{1_G}×H` gives `H_T:B_T→B_U` and `H_Tβ_T(c)=β_U(e,c)`. Both maps use the SAME actual actor coordinates, not a quotient fabricated after testing equality.

If κ_U is injective and κ_S(a)=κ_S(b), H_S gives equal product band coordinates, while the product actor values `(q_S(a),q_T(f))` are equal. Hence κ_U(a,f)=κ_U(b,f), so a=b. Thus κ_S is injective. The same argument using H_T proves κ_T injective. Combined with §4, this proves both directions of item 2.

## 6. R and L separation, and full SEP, separately

For idempotents use the source conventions

- `e R f` iff `ef=f` and `fe=e`;
- `e L f` iff `ef=e` and `fe=f`.

In a direct product these equations hold iff they hold in both components. Suppose BOTH factors have their same-q R-separation property. If two same-q_U R-idempotents `(e1,e2),(f1,f2)` have equal β_U, apply (3): their β_S components are equal and their β_T components are equal. Actor equality gives q_S(e1)=q_S(f1) and q_T(e2)=q_T(f2). Applying the two factor R-properties forces both components equal. Thus U has R-separation. The SAME proof with the L equations proves L-separation; no R/L symmetry is imposed without changing the product equations.

Conversely, if S's R-property fails, take its distinct same-q_S R-idempotents e1,f1 with equal β_S. The induced H_S in §5 gives equal β_U(e1,f),β_U(f1,f), their product actor values coincide and the two product idempotents remain R-related. Thus U's R-property fails. The same argument treats failure in T via H_T, and separately treats L pairs. Hence U has each property iff BOTH factors have the corresponding one.

The identical proof without R/L equations gives the full same-q idempotent SEP equivalence. No claim is made that R and L separation alone imply SEP without whatever separate comparable-idempotent argument the application requires. Nor is β alone claimed injective on arbitrary source elements.

## 7. Closure of the original source class

If both factors are weakly E-unitary and locally r-orthodox, U is too. Regularity follows by taking componentwise mutual inverses. The local monoid of an idempotent `(e,f)` is `eSe×fTf`; its idempotents form the product of the two local idempotent bands, and orthodoxy and the regular-band identity are preserved by products. This proves local r-orthodoxy.

If an idempotent `(e,f)` lies below `(a,c)` in the printed natural order, its actual idempotent witnesses project to witnesses e≤a in S and f≤c in T. Weak E-unitarity of the two factors makes a,c idempotent. Thus U is weakly E-unitary, with no separate assumption that the product's global idempotents form a band. This argument does not use or equate the printed full target with the canonical criterion.

The theorem iterates over any FINITE number of original factors. A factor with an open R/L/canonical obligation remains exactly an open factor; one cannot count the product factorization itself as resolving it.

## 8. Exact bounded verification — two nonunital factors

The reviewer-owned scientific checker `frontier-20261028-two-nonunital-product-checker-v1.py`, SHA `e70ad49726584917a4b7cfecf5db6afa908cd54ffda81e67469561f944a8a11d`, independently executes the definitions on a nonunital8-element rectangular group A and a nonunital18-element nonorthodox Rees semigroup C. It computes the full τ equivalence by all actual and absent two-sided contexts for each factor and for their entire144-element product, and checks the actual τ-product identity, idempotent purity, explicit band-host multiplication/injectivity, both same-q R/L pair conditions and global idempotent nonclosure.

Actual command `/opt/homebrew/bin/python3 -B .../frontier-20261028-two-nonunital-product-checker-v1.py` at **Wed Oct 28 17:32:31 PDT 2026**, timeout60s, exit0, wall time2.48s:

```text
factor_sizes=8x18 product=144 product_contexts=21025
idempotents=36 actor_classes=16
ordered_same_q_pairs=364 R_pairs=84 L_pairs=84
PASS both nonunital, complete factor/product tau, purity, host map, R/L separation, E nonclosure
CONTROL homomorphic first-factor row collapse rejected by host injectivity
```

A second same-author checker `frontier-20261028-bicyclic-rees-checker-v1.py`, SHA `b29630a070182fda0807d5d7518919c449b48fbfc7fc8650a3b96ba442659510`, executed at17:19:14 and exercises a nontrivial infinite-bicyclic shift on bounded product labels, with a wrong-shift negative control. It checks all contexts of the finite18-element factor but only bounded Bic contexts. These programs are not independent mathematical proofs of the general theorem; the second is a separate example, not an independent verification of the144-element witness. Stronger independent review/mutation controls are required before witness promotion.

## 9. Named inputs and limits

The proof explicitly reconstructs τ factorization, both product/factor band maps, the Rees-context and idempotent self-weight calculations, all four logical directions and both Green conventions. Named standard inputs are: Rees representation of a completely simple semigroup; the elementary idempotent Green-relation characterization; and closure of band varieties under direct product. Their general textbook proofs are not reproduced here. For the application to **every** original source, the source-specific SQ-E result that τ gives a pure CS quotient is reconstructed in `frontier-20261028-cryptogroup-band-retraction-v1.md` §2.1 and remains an explicit prior-written/peer-review input. No SZ87 embedding theorem or historical held review is used.

The original printed Question 1 asks about arbitrary weakly E-unitary locally r-orthodox sources, not only products; no equivalence between that printed question and the entire canonical-host registration is silently assumed. Question 2, nonproduct sources and the general R/L/SEP problem remain open at this record's scope. This theorem could be classical; no novelty, independent review, formal/kernel or full-source priority clearance is claimed.
