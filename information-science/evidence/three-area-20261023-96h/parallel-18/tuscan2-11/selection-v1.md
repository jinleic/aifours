# info-4 replacement — Tuscan-2 square of order11: selection v1

Clock observed immediately before creation: **2026-10-23T14:15:13-0700**. Same worker `InfoRecursiveMDS18`, info-4; exclusive root `information-science/evidence/three-area-20261023-96h/parallel-18/tuscan2-11/`. Parent authority: `institute/runs/three-area-2026-10-23-96h/info-4-replacement-v1.json`, with contract-v2 and both parent errata. Deadline remains **2026-10-27T12:35:38-07:00**. Only source and written work are admitted.

## Exact active claim and quantifiers

Determine whether there exists an array `A=(A[r,c])` with `r,c∈{0,...,10}` and entries in `X={0,...,10}` such that:

1. each row `(A[r,0],...,A[r,10])` is a permutation of `X`;
2. for each ordered pair `(a,b)∈X²` with `a≠b`, exactly one pair `(r,c)` with `0≤r≤10, 0≤c≤9` satisfies `A[r,c]=a, A[r,c+1]=b`;
3. for each ordered pair `(a,b)` with `a≠b`, at most one pair `(r,c)` with `0≤r≤10, 0≤c≤8` satisfies `A[r,c]=a, A[r,c+2]=b`.

**Positions are linear, not circular. There is no wraparound, no condition at distances≥3, and no Latin-column condition.** The uniqueness is separately at each specified distance, not across the union of distances1and2. Requiring columns to be permutations would restrict to Roman-2 squares and would not settle this unrestricted Tuscan-2 target. Requiring all distances would restrict to Florentine squares; requiring circular distances would be another problem again.

A full positive answer is a literal121-entry array with a complete exact check/proof. A full negative answer covers **all** such arrays, not one symmetry/Latin-column/terrace subclass. The at-most-one version of(2) is equivalent because all11 rows together have110 adjacent positions, exactly the110 ordered distinct pairs.

Allowed normalizations must be proved from genuine symmetries: simultaneous global symbol relabeling, arbitrary row permutation, and reversing **all** rows are safe. Independent column permutations, arbitrary independent row reversals, or assuming a cyclic development are not safe without separate justification. The initial first row can be made `(0,...,10)` by symbol relabeling. No further normal form is imposed until proved.

## Source relationship and actual matched baseline

### Current explicit open instance

The actual primary definition was read from [Rosin's CPro1 repository](https://raw.githubusercontent.com/Constructive-Codes/CPro1/827f02b4048fc96a6b79f0970c87ca5a54f31f40/CPro1/design_definitions/tuscan-2-square/problem_def.py), current main commit **`827f02b4048fc96a6b79f0970c87ca5a54f31f40`** (GitHub API date3June2026). It literally defines the above linear-distance condition and retains `OPEN_INSTANCES=[[11],[13]]`. The file itself last changed at commit `cfe6fda4ff32faed60dd48c5f42a6dc13d690ffd` dated28January2025; the June date is the repository snapshot, not a fabricated new theorem date. Retained source `sources/cpro1-tuscan-definition.txt`, SHA-256 **`80c4c529c3526971139ee7e0e361d2e27f59879a7cdbd22f526010c6e603f5d0`**. It was read as text, never imported/executed.

[Rosin, arXiv:2501.17725v1,29January2025](https://arxiv.org/html/2501.17725v1) includes Tuscan-2 among the16 Handbook families and reports no solved Tuscan-2 instance. [arXiv:2505.23881v1,29May2025](https://arxiv.org/html/2505.23881v1), §3.1 and Table2, again selects Tuscan-2 from the remaining open Handbook instances. Its positive results concern other families. The repository's December2025 workshop paper is behind an OpenReview browser challenge in this session; its full body is not an imported status theorem.

### Accessible mathematical primary literature

[Stoyan Kapralov, *The non-existence of Tuscan-2 squares of order9*, ACCT2012, pp.173–175](https://www.moi.math.bas.bg/moiuser/~ACCT2012/b30.pdf) was read in full. It states the exact unrestricted Tuscan-k definition, supplies an order8 example, and proves nonexistence9 by a compatibility-graph clique computation. Its table retains question marks at11and13. Its56459-vertex order9 graph/203140075-edge census and reported Cliquer outcome are **published baseline reports**, not replayed here. Retained PDF SHA-256 `98294178d6c923dbdcac0012e2e6745e69e15d570d4758d5902139d74437bd5b`.

[Jeff Dinitz's Handbook-update page](https://site.uvm.edu/jdinitz/?page_id=413), actual raw body read, was last edited18October2019 and records the order9 nonexistence at Handbook p.656/Table62.26. This does not decide11. The attribution there differs from the Kapralov conference note; neither is converted into a new computation by this slot.

[M.A.Ollis, *Roman and Vatican crossover designs*, Bulletin of the ICA92(2021),91–108](https://luca-giuzzi.unibs.it/ICA/Volumes/92/Reprints/BICA2020-33-Reprint.pdf), definitions through §3, was read for the precise distinction: Roman designs are column-uniform; Tuscan designs drop that condition. Its constructions with multiple subjects per treatment (`ℓ>1`) cannot be substituted for an11×11 Tuscan-2 square. The text extraction loses some Greek multipliers, so no exact multipler-dependent theorem is imported from an OCR guess. Its terrace/development machinery is classical baseline, not a fresh idea of this slot.

### Current-status qualification

The current live primary problem-definition repository still lists11, but the old open label is not a proof of present openness. Dedicated web searches,17 DataCite records returned for `Tuscan AND square`, and the local/current remote mathematical corpus screen located no matched order11 settlement. The relevant2026 DataCite hit is Kirtchakov's **circular Florentine5×25** construction, a different object/order, not an11×11 Tuscan-2 square. It is not ignored and is not confused with this target.

Status is **UNCERTIFIED-OPEN / NOVELTY_UNCLEAR**, supported by a literal primary open-instance list and bounded later search, not by a claim that no solution exists anywhere. The old q18 source-screen failure demonstrates why a later explicit claim, including a personal repository, must trigger a new scope check.

## Book relationship and exclusions

The information-science volume and actual code/distance article were read in the preceding source intake: *10000 Selected Problems in Sciences: Information Science* (2011; ISBN978-7-03-031911-1; PDF SHA-256 `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db`), printed pp.394–395/PDF415–416, *纠错码的译码问题*. This target is an **indirect combinatorial-design/sequence-design relative**, not a literal problem stated there and not a solution of its average-decoding-complexity question. The direct modern source is Handbook VI.62/CPro1. No fabricated book quotation or claimed decoding consequence is used to strengthen the bridge.

The parent collision check excludes overlap with all18 roster entries, including PA19, CFR21, MOLS39, recursive MDS18, MOQLS8 and RQLS10. It also lies outside completed CDF/CPCW/BTD/point-cyclic cases. Existing `information-science/evidence/six-lane-20261016/cfr33/sources/info2-killcheck-screen-v2.md` was read at its Tuscan rows: it screened11and13, noted the classical failure of odd cyclic development and warned that exhaustive nonexistence at11 would be costly. That screen contains **no solved Tuscan11 certificate or new claimed construction**. Its cyclic-ansatz obstruction is baseline, not this round's discovery.

The original order18 assignment is now **PRIOR-CLAIM**, not a concurrent active problem; its exact public table and scope disposition are preserved in the immutable old root. SkewW(30,25) remains merely a reserve screening proposal and is not attacked in parallel.

## Mandatory corpus screen

Local `/Users/jinleic/jinleic-workspace/math/lean/docs` and `math/preprints` were screened for `Tuscan` and weighing-matrix alternatives; the only broad skew-weight hit was unrelated. Remote openai/math lean/docs and preprints inventories were opened during this intake, and the complete fresh remote `CONTENTS.md` was screened for `Tuscan`, `weighing matrix`, `weighing matrices`: no matches. The retained catalog is in the immutable old root, SHA-256 `cc7c0b8a1cdedd845a777e77cf682657308503daf8346c1349e06e9259d063c2`. This is a corpus keyword/title/abstract check, not exhaustive semantic proof comparison.

## Missing ingredient, full delta and first bounded written attack

The missing ingredient is a way to couple an exact Hamilton-path decomposition of the complete directed graph with the noncollision condition on every same-row two-step path, **without** using the impossible regular odd cyclic starter or assuming Latin columns. The compatibility-graph restatement alone is already Kapralov's method; merely repeating it earns no discovery.

First derive exact endpoint/second-neighbor defect identities for the unrestricted array and the relation between missing distance2 arcs and row starts/ends. Seek a structural certificate that forces an obstruction at11 or a genuinely viable nonregular development/trade mechanism. Any structural lemma is explicitly partial unless it supplies a full construction or excludes all arrays. A finite model of necessary conditions is not an existence certificate for rows.

Chronology: conceptual endpoint/defect and nilpotent-path-matrix ideas were considered during source screening before this freeze. No completed candidate or executable result preceded the freeze. This is disclosed rather than backdated. Substantive proof development follows this snapshot.

## Verification and redirect

Complete candidate first, then parent and separate in-harness reconstruction on pinned bytes. A positive verifier must check exact row universes and exact110-pair coverage at distance1 plus99 distinct distance2 events, with bounds/range/duplicate/malformed controls. A negative proof must retain every non-Latin-column possibility and certify any enumeration. Python/Fraction arithmetic is not formal proof. No scientific execution is admitted; proposed solver/verification work needs exact source/input pins, named GO, resources, controls and graceful settlement before launch.

Redirect if a matched current primary source supplies the literal11 object or unrestricted nonexistence, or if parent authorizes another distinct target after this source gate. Failure of a symmetry/trade ansatz does not settle11. UNKNOWN is not UNSAT. No nested agents, modelCLI, paid fallback, account/config change, Git mutation, deletion, old runtime or scheduler.
