# Exact band-size optimum for the 68-source over its actual actor

**Status: NEW AUTHOR WRITTEN + replayable exact finite certificate; UNREVIEWED / UNADOPTED.** For the specific 68-element source S and its actual eight-element pure-CS actor q pinned in `frontier-20261028-quotient68-sixband-host-and-obstruction-v1.md`, SHA `b24ce079030e75e6f1d5dfaa2a88696f4531eb53963f507c0876d4b0ad9f599c`, the minimum cardinality of a band B supporting a faithful physical host **over q** is exactly **10**. The lower bound applies to arbitrary bands, not just seminormal ones; the exhibited ten-element band is seminormal and locally regular. This is a fixed-source, fixed-actor optimum, not the minimum over arbitrary CS actors or a universal Q1 result.

## 1. Reduction of a 9-band host to two actions

The q-fibre at idempotent actor `(0,0,1)` has exactly nine elements, with source indices

`F=[1,9,17,25,32,37,45,53,61]`.

Every member is idempotent. The fibre is a band because q is pure and its actor is idempotent. In any faithful q-host, the band coordinates of these nine elements are distinct, so `|B|≥9`. If `|B|=9`, they exhaust B and the fibre multiplication table identifies B isomorphically with the explicitly pinned 9-element fibre band. Thus, after uniquely relabelling B by the order in F, the images of these nine source elements are fixed as 0,…,8; there is no choice of a different nine-element target band.

An action of the q actor's group C₂ on B is an involutory automorphism. The exact replay enumerates all `9!` permutations of the fibre table and checks every multiplication pair. There are exactly TWO automorphisms, both involutory:

`id=(0,1,2,3,4,5,6,7,8)`,
`τ=(0,1,6,7,4,8,2,3,5)`.

Hence every candidate 9-band q-host uses one of these two actions, up to the fixed fibre relabelling.

## 2. Replayable no-9 certificate

For each source element s maintain the current set `D_s⊆{0,…,8}` of possible band coefficients, initially the whole set except the nine fixed fibre values. For each source product `st=r`, and for the candidate action ρ, form all triples

`(x,y,z)` with `x∈D_s`, `y∈D_t`, `z∈D_r`, `z=x·ρ^w(y)`,

where `w=g_s+λ_s i_t` is the actual q group weight. Intersect D_s,D_t,D_r with the corresponding projections of this allowed-triple set. Every genuine solution survives every such pruning, including when two of the variable indices coincide; the projections are a sound necessary condition, not an assumption that the roles are independent.

The pinned literal trace file `frontier-20261028-quotient68-no9-arc-traces-v1.json`, SHA-256 `1df6c7fadc87c5279977c135cceadc4d152fb85d69df9e52a4bd1736045d936d`, gives each narrowing step. The independent-from-Z3 replay recomputes the projections against the current domains, verifies the old/new sets exactly and stops at an empty domain. The identity action has 143 narrowing steps ending with source variable24 empty; τ has 156 steps ending with variable32 empty. Thus neither possible action admits even a homomorphism with the fixed fibre embedding; no faithful 9-band host exists. The solver's earlier UNSAT response is NOT the proof: the complete no-9 argument is the finite automorphism enumeration plus the replayed sound pruning trace.

## 3. A ten-element SN-band host

`frontier-20261028-quotient68-10band-host-data-v1.json`, SHA-256 `a421753f77c853716e1bea0f49c10509c8947289c0a5a31abfbdb8f7b4f8e80b`, contains the 10×10 band table, its involution and 68 band-coordinate values. The exact verifier checks all 1,000 associativity triples, all 10,000 seminormal substitutions, all 100 action-preservation equations, all 4,624 source product equations, and all 256 distinct same-actor injectivity comparisons. It uses no Z3. Each band element is actually used; combining with the actual eight-element actor gives an 80-element physical host.

The ten-element host was found by a bounded same-author Z3 4.15.4 search and is verified from literal tables. A separate intermediate 12-element subband of C6³, with its own data and checker, is `frontier-20261028-quotient68-12band-host-data-v1.json` (SHA `0b71d1b41ac2cf117636485b0cd3662322de979d9ef8d368dbe1b915231335fa`) and `frontier-20261028-quotient68-12band-host-checker-v1.py` (SHA `d5780fb9e9bfe922a9eff822d83d2bbd0f1ada4c39a9e46a91e54249a46b254b`). The optimum uses the ten-element witness, not the earlier 12/7,776-element hosts.

## 4. Replay and limits

`frontier-20261028-quotient68-minimum-band-replay-v1.py`, SHA-256 `910dfe50d781d3c2791aa12790bdf57122318fcc47d3f31e7e9849c51fc659ce`, completed in the Python eval kernel before Wed Oct 28 22:06:37 PDT 2026, reading the source data, both arc traces and the ten-band witness. Its observed output:

```text
PASS 9-band arc trace action=[0,1,2,3,4,5,6,7,8] steps=143 empty variable=24
PASS 9-band arc trace action=[0,1,6,7,4,8,2,3,5] steps=156 empty variable=32
PASS exhaustive 9! automorphisms: exactly two C2 actions, both arc-inconsistent
PASS 10-band: 1000 associativity, 10000 SN identities, all 4624 source products, 256 injectivity pairs
RESULT: exact minimum actual-q band size=10, contingent on pinned source/actor verification
```

The replay is independent of Z3 but shares this author's pinned source and trace generation; the source quotient and actual q were checked separately in `frontier-20261028-quotient68-faithful-host-checker-v1.py`, SHA `694d037f52e02a0c9cf00eb426bdaa04043930bb035e3877f19a11e395807f25`. Independent source/trace/witness review remains required. No inference is made that a different CS actor cannot use a smaller band; the full original Q1 and all-actor optimality remain open.
