# Exact idempotent-fibre representation of the original source class

**Status: NEW AUTHOR WRITTEN universal representation; UNREVIEWED / UNADOPTED.** This supplies a different exact input formulation for the original universal embedding problem, not a proof of that embedding. It keeps DIRECT morphism extensions separate from cover/divisor Malcev products and Q2.

## 1. Exact corner formula at any pure-CS quotient

Let r:S→D be an onto idempotent-pure homomorphism, D completely simple. No source regularity is required in this paragraph. For d∈E(D), write `F_d=r⁻¹(d)`. Every F_d is a BAND: it is closed and purity makes every element idempotent.

For EVERY e∈E(S), d=r(e), the exact equality is

`E(eSe) = e F_d e`.                                      (1)

Indeed, if f∈E(eSe), then r(f) is an idempotent in `dDd`, a GROUP, so r(f)=d, and f=efe lies on the right. Conversely eae for a∈F_d has image d, so purity makes it idempotent, and it belongs to eSe. This proves both containments. It also shows E(eSe) is a band, hence pure-CS sources are automatically locally orthodox when they are regular.

Let V be ANY variety of bands, and define `W(V)` as the bands B for which every local monoid bBb belongs to V. Then (1) gives the exact equivalence

`all F_d∈W(V)  iff  all E(eSe)∈V`.                       (2)

No global closure of E(S) is assumed or inferred: distinct F_d may multiply to nonidempotent source elements. Conversely, if all source corners satisfy V, then each F_d is locallyV because for any e∈F_d its local monoid eF_de is exactly the source E-corner in (1).

## 2. Original and one-sided source classes, with dependencies explicit

Define `K_onto(W,CS)` to be the class of REGULAR semigroups admitting an ACTUAL ONTO morphism to a CS semigroup whose idempotent fibres are bands in W. This fibre condition itself implies idempotent purity. The notation K_onto is intentional and is NOT an unqualified standard Malcev-product claim.

Import the reconstructed source bridge from `frontier-20261028-weakE-localorth-pure-cs-proof-v1.md`, SHA `d339b3165ef3dce4a3b85bc3c74db447a504275aaa41195028f58c58008a7fe9`: regular WEU+localorth iff there is a pure-CS quotient. Import also the written band identity equivalences at their author-unreviewed scopes: localREGband iff SN; localRRB iff RIGHTSN; localLRB iff LEFTSN. The localREG equivalence requires the mandatory content-proof erratum `frontier-20261028-local-seminormal-band-content-rationale-erratum-v1.md`, SHA `dfedbf04821a2e60259e2d34631f336178ed73f867e79373d888926f4cb1262a`.

Then (2) gives the exact source descriptions

- Original regular WEU/local-r sources = `K_onto(SN,CS)`.
- Regular WEU/locallyRRB sources = `K_onto(RIGHTSN,CS)`.
- Regular WEU/locallyLRB sources = `K_onto(LEFTSN,CS)`.

For the forward implication use the named source bridge to get the pure quotient, then (2). Reverse: a morphism with band fibres is pure, so regularity and CS's primitive idempotents imply WEU by mapping every FULL natural-order witness; (2) supplies the precise local band identity. This is a universal representation of the actual source class, including nonorthodox fibres over different actor idempotents. The embedding gap is now explicitly DIRECT pure-CS extensions of SN bands versus faithful physical SN hosts, not an unspecified weaker local test.

## 3. A concrete cover trap: standard Malcev closure is strictly larger

Standard finite-semigroup Malcev products can be defined using a COVER: M belongs to V m W if some finite T has onto maps `α:T→M`, `β:T→N∈W`, with each idempotent β-fibre in V. This is the convention explicitly given in Kufleitner–Weil, *On the lattice of sub-pseudovarieties of DA*, §1.2, <https://arxiv.org/pdf/0904.2893>. It is not the direct K_onto definition above.

The distinction persists even for REGULAR sources and IDEMPOTENT-SEPARATING covers. Let `T=P({1,2})⋊C₂`, the eight-element inverse host, where C₂ swaps the atoms. Map `(A,g)` to the partial bijection x↦g(x) whose RANGE is restricted to A. This gives an onto idempotent-separating homomorphism to the seven-element symmetric inverse monoid I₂. Projection β:T→C₂ is pure and its identity fibre is the four-element semilattice. Thus I₂ is in the cover-defined `SL m G`, hence also in cover-defined `SN m CS`. But I₂ is NOT WEU: its zero is below its nonidempotent full swap, using zero on both sides. Therefore I₂ is NOT in K_onto(SN,CS), despite being inverse and locally a semilattice.

`frontier-20261029-direct-cover-kernel-boundary-checker-v1.py`, SHA `230f91486631d8ed42c231ef44febb2a475be5d23c150e2c2b543a891fecb709`, completed before ThuOct29 01:57:24 PDT2026. It checks all64 cover multiplication equations, onto7, allfour idempotents distinct under the cover, the direct C₂ purity/SLkernel, FULL source WEU, I₂'s unique inverses and all local E-corners semilattice, and the literal zero-below-swap violation. The kernel/class statement (1)–(2) is a universal written proof, not a finite replay conclusion.

Hence a theorem about ordinary cover/divisor Malcev closure cannot by itself solve the actual Q1 DIRECT-source-to-faithful-host problem; it may merely supply an idempotent-separating image of a host, the DIFFERENT type of statement in Q2. Nor does closure under such images preserve WEU. All named universal inputs, source convention equivalences and the new proof still require independent review. No original universal separation, formal verification, or novelty is asserted.
