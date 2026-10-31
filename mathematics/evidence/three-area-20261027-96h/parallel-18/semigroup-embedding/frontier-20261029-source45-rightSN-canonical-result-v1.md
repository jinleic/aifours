# Exact 306-element canonical right-seminormal band for the 45-source

**Status: NEW AUTHOR COMPUTATION with separate literal-table recheck; UNREVIEWED / UNADOPTED.** This computes an ACTUAL one-sided canonical source quotient, not just a proposed model or a timeout. It is one finite source already known to have a faithful host, not an all-source theorem. The canonical interpretation depends on the new universal rightSN normal form; the exported faithful host can be independently checked without trusting that interpretation or the congruence engine.

## 1. Source and six-generator free representation

Use the exact 45-source `S=M[A;{0,1,2},{0,1,2};P]`, with

```text
A:
0 1 2 3 0
3 2 1 0 1
0 1 2 3 2
3 2 1 0 3
0 1 2 3 4

P:
4 4 4
4 1 3
4 4 1
```

The actual pure CS actor is `q(i,a,λ)=(i,θ(a),λ)`, `θ=(0,1,0,1,0)`, with group C₂. The source hypotheses, nonorthodox/non-locally-inverse witnesses and actual-q test were pinned earlier; the explicit local-band host is `frontier-20261028-ambiguous-source-local-band-host-v1.md`, SHA `a96cb3eeae75bba72af2cc43ff548785c74224fb7ed3509303a0f177cfb2feba`. This computation does not replace those source checks.

The three source generators are `(2,4,2)`, `(1,4,1)`, `(0,4,0)`, numbered44,28,12 in lexicographic45-order. Their right-generated closure is the entire source. Acting by both C₂ elements gives SIX formal band generators `X_(u,j)`, u∈C₂,j∈{0,1,2}. By `frontier-20261029-right-seminormal-normal-form-v1.md`, SHA `c2a5f4d9de295deed8e28282b2456f6d274886856224dccd68208bae0c2fe6be`, the free rightSN band on6 letters has exactly614,226 elements, represented by head/critical-letter/tail signatures.

Fix one right-generator source word for each s using BFS. Expand its coefficient recursively using the actual Rees weights; these define formal coefficients c_(u,s) in the six-generator free band. Impose the270 equations

`c_(u,s·g_j)=c_(u,s) X_(u+w(s,g_j),j)`,

for u∈C₂, s∈S and the three generators g_j. Close them under left/right multiplication by all six band generators. Both u values make the relation set C₂-stable, so the least generated congruence is action-invariant.

## 2. Why these are the complete canonical source relations

Relations against the source generators imply the full mixed law by induction on a generator word for t. If `t=t' g_j`, then its first Rees row is that of t', so `w(s,t)=w(s,t')`, while

`w(st',g_j)=w(s,t') w(t',g_j)`.

The induction hypothesis and the generator relation give

`c(st)=c(st') α_(w(st',g_j))c(g_j)`
`      =c(s) α_(w(s,t'))[c(t') α_(w(t',g_j))c(g_j)]`
`      =c(s) α_(w(s,t))c(t)`.

Conversely all270 equations are instances of the full physical source law. In any physical host, the six formal generators evaluate to the C₂-translates of the three source-generator coefficients; expanding the fixed BFS words gives the actual coefficient of every source element. Thus this six-generator quotient has the full canonical universal property in the **rightSN variety**, not merely a selected-source-word consistency property. Left/right congruence closure under generators suffices for closure under arbitrary words; no omitted outer context is assumed inert.

## 3. Actual computation and exported witness

The C++ producer `frontier-20261029-source45-rightSN-canonical-v1.cpp`, SHA `908d242077600f7d47ee833a0bbcfce64303ce684192d9d14ec2db89e6e7787d`, compiled with clang++ -O2 -std=c++20 and ran successfully. Its observed combined compile/run wall time was1.65s. It enumerated all614,226 signatures, precomputed their12 left/right generator translations and C₂ action, then generated613,920 congruence merges, leaving **306 canonical band classes**. The full source map over actual q is injective: all36 distinct same-actor source pairs survive. It checks action consistency and every12 generator transition throughout all614,226 free states.

The export successor `frontier-20261029-source45-rightSN-canonical-data-v2.cpp`, SHA `7d5e22ced129d653ba4cfb2a97002c98a35ee882fb27546a160d50d8b511172b`, rederives that result, constructs the complete306×306 quotient multiplication table, and checks all full45×45 source product equations for both C₂ translates. Its literal output is `frontier-20261029-source45-rightSN-canonical-host-data-v1.json`, SHA `9cf94b6a16eeea101f02c6ba5ff36b50a5045a5f94f44c7e68d36bb9c511953c`, containing the93,636 band entries, action and45 source coefficients. The whole physical host has306×18=5,508 elements.

The Python verifier `frontier-20261029-source45-rightSN-host-checker-v1.py`, SHA `2ee3ffb4742201570d83835120cd2374f1200de43c7d754f8ce4e7e5f261a169`, completed before Thu Oct29 00:18:45 PDT2026. It does NOT import the C++ signature or congruence code. From the literal exported table it checks all28,652,616 associativity triples, all28,652,616 rightSN identity substitutions, the complete C₂ action, all2,025 source products, all same-actor injectivity comparisons, and generation of all306 band elements by action-translated source coefficients. Thus the exported faithful rightSN/SN host is separately checked even if the canonical-count proof fails review.

## 4. Scientific scope

The306-band canonical object is not claimed to be a minimum-size host; the previously exhibited25-band host is smaller. The new result is an exact noncommutative canonical quotient at the full mixed-relation/outer-context scope, enabled by a614,226-state one-sided normal form rather than the astronomical unrestricted free band on six symbols. It exercises the genuine same-q R-idempotent example, not only comparable support.

Both C++ and Python are same-author artifacts. Independent finite-witness/canonical-proof review is required, including the source, actual actor, rightSN normal form, generator reduction and full congruence saturation. The general matching one-sided original source problem remains open; no novelty, formal verification or all-source Q1 conclusion is claimed.
