# An original-class 68-element quotient: exact SN host and B5-power obstruction

**Status: NEW AUTHOR-WRITTEN construction with same-author exact finite recheck; UNREVIEWED / UNADOPTED.** This solves one explicit nonorthodox, non-locally-inverse original-class instance at the physical-product convention. It does not settle general Q1, the arbitrary-band R/L gap, or source novelty. The all-actor strengthening in §4 has an explicitly separate unreviewed transport dependency.

## 1. Source, actor and actual quotient

Let B5 be the locally regular five-element band

```text
0 2 2 4 4
0 1 2 1 4
0 2 2 2 4
0 3 2 3 4
0 4 2 4 4
```

with automorphism `σ=(1 3)(2 4)` fixing 0, and let L2 be the two-element semilattice. Let `D=M[C₂;{0,1},{0,1};P]` with `P_(λ,i)=λi` in bits. Form the 80-element physical product `H=P(B5×L2,D)`, with C₂ acting as σ on B5 and trivially on L2. Generate a semigroup congruence α by the single actor-fibre pair

`((0,0),(0,0,0))  ~  ((2,0),(0,0,0))`.

Write `S=H/α`. The literal quotient partition, 68×68 multiplication table, eight-element actor map and five coordinate tables are pinned in `frontier-20261028-quotient68-faithful-host-data-v1.json`, SHA-256 `64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf`. Under its lexicographic source numbering S has 68 elements and 34 idempotents. It is regular, weakly E-unitary and locally r-orthodox; it is neither orthodox nor locally inverse. Exact witnesses by indices are `(0,7,3)` with idempotents 0,7 but product3 nonidempotent, and `(24,36,60)` with 36 and60 noncommuting idempotents in corner `24 S 24`.

The natural quotient actor map `q:S→D` is onto and pure, since α preserves actor and the pure physical actor projection is inherited. The literal checker verifies that all eight D elements have distinct idempotence-context signatures. Thus, by pulling back contexts through the onto pure map, q is the **actual idempotence-context quotient**, not merely a convenient auxiliary actor. This is an exact finite case, not a universal SQ-E proof.

## 2. A faithful product of a six-element SN band

Let C be the six-element band

```text
0 1 0 0 4 5
0 1 1 1 4 5
0 1 2 2 4 5
0 1 3 3 4 5
4 4 4 4 4 4
0 1 0 1 4 5
```

and let `ρ=(0 1)(2 3)` fix 4 and5. C is seminormal, each of its six local corners is a regular band, and ρ is an involutory band automorphism. It is **not** globally regular: the regular-band identity fails at `(x,y,z)=(2,5,3)`. On `C^5`, let C₂ act diagonally by ρ. The JSON file provides `c_s∈C^5` for each s∈S, and the checker verifies literally, for every `s,t`,

`c_(st) = c_s · ρ^(g_s+λ_s i_t)(c_t)` componentwise,

alongside `q(st)=q(s)q(t)`. The map `s↦(c_s,q(s))` is injective: all 256 distinct same-actor source pairs have unequal five-coordinate values. Therefore S embeds in `P(C^5,D)`, a concrete SN-band-by-CS host. The conceptual full band has 6⁵=7,776 elements and the host has 62,208; the certificate checks coordinates and products, not an enumeration of all host elements.

A nontrivial same-q R-pair is `e=37`, `f=61`: `ef=f`, `fe=e`, yet their band coordinates are `(4,2,1,1,4)` and `(4,2,1,0,4)` respectively. The coordinate tables were discovered by a bounded, same-author Z3 4.15.4 greedy finite-model search in the eval kernel (five successive satisfiable coordinate models); the literal verifier below does not import Z3 or depend on its verdicts. This is not a minimal-band claim.

## 3. Why powers of the previous five-band cannot suffice

The following quasiidentity Q holds in B5:

`ef=f, fe=e, eb=e, fb=f, ae=af  ⇒  e=f`.              (Q)

It holds by direct table inspection: the only nontrivial R-class is `{0,2,4}`. If e or f is 0 and they differ, `eb=e,fb=f` is impossible. If `{e,f}={2,4}`, then `a2=2` and `a4=4` for all a, so `ae=af` is impossible. It also holds in every rectangular band: R-related elements have the same row, and `eb=e,fb=f` force their columns both equal that of b. Thus Q holds in every direct product and subband of copies of B5 and rectangular bands.

In S, let `a=0`, `b=25`, `e=37`, `f=61` (all are source indices). The literal table gives `ef=f,fe=e,eb=e,fb=f,ae=af=32`. For each of these six products the actual physical action weight is the group identity. Hence in ANY physical host over the actual q, their band coordinates satisfy Q's hypotheses. If its band satisfies Q, e and f collapse; so there is **no faithful actual-q host** whose band is a direct product/subband of copies of B5 and rectangular bands, regardless of the C₂ action. This is a band-class obstruction only, not an all-SN-band obstruction.

Under the separately unreviewed pure-CS actor restriction/pushforward from `frontier-20261028-regular-source-any-actor-characterization-v1.md`, SHA `73d3951b03ecdbc6574a21753665e612c28aa0570158e7936a7228e36deade5d`, an arbitrary-actor host with band in `SP(B5)` would transport to an actual-q host with band B×R for a rectangular R, which also satisfies Q. Therefore the same nonexistence extends to arbitrary CS actors **conditional on that transport**. It does not extend to arbitrary seminormal bands: C above violates Q at `(a,b,e,f)=(4,3,1,0)`, and its C⁵ host is faithful. Thus this example exposes a genuine boundary of a tempting five-band-power strategy without being an original-Q1 counterexample.

## 4. Exact verification and provenance

`frontier-20261028-quotient68-faithful-host-checker-v1.py`, SHA-256 `694d037f52e02a0c9cf00eb426bdaa04043930bb035e3877f19a11e395807f25`, executed in the Python eval kernel before Wed Oct 28 21:54:03 PDT 2026, using only exact finite tables and no Z3. It checked all 512,000 associativity triples of H, generated the congruence from the displayed seed, rederived the complete quotient and actor tables, regularity/weak-E/local-r and the two negative-class witnesses, eight distinct actor context signatures, all six local corners of C, its 1,296 seminormal substitutions and automorphism, all 23,120 coordinate multiplication equations, all 256 same-actor injectivity pairs, all 625 substitutions of Q in B5, and every source equation/weight used above. The first version of the checker passed before the local-corner and Q assertions were added; the displayed counts refer to the successful final version.

The search `frontier-20261028-horn-layered-band-quotient-attack-v1.py`, SHA `2b025ea3527a8f6b6e1b2fcc6bf2629f8a344ac12c4f1862568c9acfd66a3b6e`, explored 120 selected actor-fibre congruence seeds, yielding 18 distinct quotient partitions. Its 68-source seed has 52 ordered comparable same-q idempotent pairs, all separated by Horn support; this is finite exploratory evidence, not a universal comparable proof. All finite artifacts are same-author. No independent finite-witness certification, cross-vendor/human/formal proof, full original-class conclusion or novelty clearance has been performed.
