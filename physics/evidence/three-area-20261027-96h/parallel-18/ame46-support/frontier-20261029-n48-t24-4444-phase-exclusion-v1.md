# Candidate support48/t24 exclusion of residual alphabet (4,4,4,4): actual cross-cut phase contradictions

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Thu Oct 29 10:42:49 PDT 2026`; not an exact completion time. **WRITTEN normal form plus exact finite coverage and integer phase certificates**, not independently reviewed, adopted, formally verified or novelty-cleared. This is one residual profile of the open support48 case, not a global lower-bound theorem.

## 1. Scope and the one load-bearing candidate prerequisite

Assume a normalized complex AME(4,6) state has `N=48`, exactly `t=24` modulus-1/6 coefficients P, and other support E of size24. Assume all four E alphabets have size4.

The candidate result is that this branch is impossible. It uses the **separately unreviewed** no-distance-one conclusion for this exact N48/t24 case in `frontier-20261029-n48-t24-noh1-and-six-alphabets-v1.md`, SHA-256 `6bbe85a8b1bec38ef5984d32408c52479ec58edeb3502398d87ab1f7e04a7c96`. That prerequisite re-derives its component/complement argument at n12; the recorded f127 N46 lemma is not applied outside its scope. The prerequisite inherits the named classical no-OLS(6) theorem. No held material or solver UNSAT result is used.

The identity support below is rejected by the same classical no-OLS(6) import. All other surviving support patterns are rejected by explicit integer contradictions among the **actual phase equations in three cuts**, for arbitrary nonzero complex amplitudes. Equal moduli and real signs are not assumed.

## 2. The degree and fiber normal form

In each cut, `U=6ψ` is unitary. Removing the24 singleton maximal entries leaves a12×12 residual unitary with24 entries, so every residual row and column has degree2. Each of the six pair projections of E therefore has12 values, each with exactly two E extensions.

Call a P coordinate active when its value is in the four-symbol E alphabet. The P/E pair partition gives12 P words active at each party and4 active at each party pair. Therefore `Σ_P k=48`, `Σ_P C(k,2)=24`, and `Σ_P[k−C(k,2)]=24=|P|`. Every P word has k=1 or2, and Σk=2|P| then forces **every** P word to have exactly2 active coordinates.

For a residual symbol a at party i, partner degree d_i(a) is j-independent and its P occurrence count is `6−d_i(a)`. The number of P words using a and active at another party j is `4−d_i(a)`. Since each P word using a has exactly one other active party,

`6−d_i(a)=3(4−d_i(a))`, hence `d_i(a)=3`.

Each E symbol fiber consequently has6 entries, takes3 values twice at each other party, and is pair-injective in those three coordinates: two fiber words sharing another coordinate pair would differ in only the fourth coordinate, forbidden by the prerequisite.

Thus each global E pair projection is a4×4 graph of degree3; its complement is a perfect matching. Relabel B,C,D so the missing A–B, A–C and A–D matchings are identity. In A fiber a, the other three alphabets are then all `V={0,1,2,3}\{a}`. The remaining three missing matchings, on BC,BD,CD, are arbitrary permutations f,g,h∈S4. All `24³=13,824` choices must be kept; no orientation is discarded.

## 3. Deleting a symbol from a forbidden matching

Within A fiber a, each other pair projection has6 distinct values, row and column degree2 on the local3×3 grid. Its complement is one perfect matching and must contain every restriction of the global forbidden matching F to V×V.

If F(a)=a, those restrictions already have three edges. Otherwise exactly two edges survive and their matching has a unique completion. Explicitly its local map is

`F_a(b)=F(b)` when `F(b)≠a`, and `F_a(b)=F(a)` when `F(b)=a`, for b≠a.

This is cycle deletion (shortcutting through a). It is not an extra ansatz. A local six-point fiber must have exactly the complement of F_a for each of its three pair projections. These projections uniquely determine any possible six-point pair-injective fiber; that uniqueness and existence are independently exhausted in the two programs below rather than assumed without checking.

## 4. Complete finite support coverage

Two separate standard-library implementations enumerate the complete normal form:

- The producer builds all balanced, pair-injective six-subsets of a3×3×3 cube: exactly144. It maps their three projection signatures to fibers and enumerates every f,g,h∈S4.
- The replay does **not** read producer code or import the phase engine. It extends the two or three local forbidden edges to each of the six possible3×3 matchings, then enumerates the six-triangle covers of the three allowed local pair graphs by exact recursion.

Both obtain:

| gate | count |
|---|---:|
| all global matching triples | 13,824 |
| all four local fibers exist | 3,054 |
| all six global pair projections have12 values of multiplicity2 | 382 |
| every cut is a disjoint union of full2×2 blocks | 10 |

The replay checks that every local cover has multiplicity at most1, all ten residual supports are covered once, and the supplied matching triple binds to that support.

For the ten survivors, f=g=h and this common permutation is an involution: identity, one of six transpositions, or one of three double transpositions. This is an **output of the finite coverage**, not an input restriction. No global matching triple with a3-cycle or4-cycle, or three unequal involutions, is silently omitted.

## 5. Actual phase contradiction for the nine nonidentity cases

Every nonzero2×2 unitary block imposes

`φ_11−φ_12−φ_21+φ_22 ≡ π (mod2π)`.                              (P)

This follows from its two-term row orthogonality; it is valid for arbitrary nonzero complex moduli. There are6 blocks per cut,18 equations in all. For each nonidentity survivor the producer emits an integer vector λ on these18 actual equations with

`Σ λ_j (coefficient row of equation j)=0`,  `Σ λ_j odd`.         (C)

Summing (P) with those integer coefficients gives `0≡π (mod2π)`, impossible. The replay reconstructs every actual block from the support, checks coverage of all18 serialized equations up to harmless sign orientation, checks every coefficient cancellation directly, and verifies the odd sum. It imports no integer-elimination or phase-solving code.

Examples, in the producer's frozen block order:

- Transposition F=(0,1,3,2) has
  `λ=(1,−1,1,0,0,0,0,0,0,1,−1,−1,−1,−1,1,0,0,0)`, sum−1.
- Double transposition F=(1,0,3,2) has
  `λ=(0,1,0,0,0,0,0,−1,0,0,0,0,0,1,0,0,0,0)`, sum1.

The latter is the literal three-equation contradiction A−B+C:

`A = φ_0212−φ_0221−φ_3112+φ_3121 ≡ π`,

`B = φ_0122−φ_0221−φ_3112+φ_3211 ≡ π`,

`C = φ_0122−φ_0212−φ_3121+φ_3211 ≡ π`.

Their left sides cancel exactly, while `π−π+π=π`. The certificate records provide the corresponding supports and all18 actual blocks; the cancellation is a common-three-cut statement about the **same coefficients**, not separate phase assignments for each cut.

## 6. Identity case: classical selection, not a false phase obstruction

For f=g=h=identity, E is all24 permutations of four symbols. Its even-permutation subset has12 words and is pair-injective: fix any ordered two-coordinate value pair; the two completions differ by swapping the remaining two symbols, so exactly one is even.

This selector shares no pair with the24 P words, since P pair rows are isolated from E. Together the36 words form OA(36,4,6,2), equivalent to two orthogonal Latin squares of order6, forbidden by the named no-OLS(6) theorem. The identity case is not falsely rejected by a phase inconsistency; it is explicitly the **classical-selection** branch.

Thus all ten finite support cases are excluded, conditional on the prerequisite and exact finite coverage/certificate checks.

## 7. Pinned evidence, mutations and limits

Producer `frontier-20261029-n48-t24-4444-enum-v1.py`, SHA-256 `7a6a4430a91c38eac78021e539bd3c30fe8a4ba96f794ab0f0a576d67571b68c`; candidate/certificate record `frontier-20261029-n48-t24-4444-enum-v1.json`, SHA-256 `fe55fefb173a152b0cc86c3280618e01fe645bb63b757b4513b0c50616f415d0` (8,817LF,125,529bytes). It includes every survivor, every block equation, nine integer odd relations and the remaining12-word selector.

Independent triangle-cover/certificate replay `frontier-20261029-n48-t24-4444-replay-v1.py`, SHA-256 `8a5bbc878f4e45bc3409098d041499d1a7b9e98cf99c59f99b4fe72f33c1b1f5`; receipt SHA-256 `bcdb0102feb5da0ae410b1ae58ccfad55004b46f7e17611cdc39e18164e38e37`. It rebuilds all13,824 matching cases (864 cached local triangle signatures), obtains identical counts, directly checks nine relations and one selector, and rejects four intended corruptions: a changed relation coefficient, a missing block equation, a duplicated selector word and a duplicated support word.

Both implementations are same-harness exact finite checks, not independent-model-family review, human proof, formal verification or novelty clearance. Independent review should attack the activity/d=3 step, use of the exact-scope n12 no-distance-one prerequisite, unique local missing-matching extension, complete matching enumeration, full2×2 support necessity, literal phase certificates and the identity selector/no-OLS composition.

Other residual profiles at N48/t24 remain open. This packet does not compose any global support bound or claim a smaller-support AME tensor.
