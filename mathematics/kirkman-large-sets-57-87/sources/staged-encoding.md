# Exact staged encoding and its search restrictions

Date:2026-10-14. Implementation: `work/search_staged.py`; exact native-CNF replay: `work/replay_staged_cnf.py`. This is a constructive search for one cyclic-transversal resolved base, not a proof of the book-wide conjecture.

## 1. Infinity matchings

Put n=v−2, with gcd(n,6)=1, and pointsZ_n∪{u,w}. Translation normalizes the unique block containing{u,w} to{0,u,w}. The remaining blocks throughu pair all nonzero finite points exactly once, and likewise forw. An orbit of a block{u,a,b} is determined by the unsigned difference±(b−a); because the base is a translation-orbit transversal, every nonzero unsigned difference occurs once in each matching. The matchings cannot share an edge, since that finite pair would be covered twice in the STS.

These conditions are imposed exactly by Stage1: point/side and difference/side exactly-one constraints, with shared-edge at-most-one constraints. The seeded random linear objective only samples feasible matchings; no objective optimum is required for correctness. A five-second matching timeout does not certify infeasibility. The optional patterned first matching{x,−x} is an explicit restriction, not a symmetry normalization.

## 2. The finite triple cover

Freeze the two matchings M_u,M_w and let L=K_n−M_u−M_w. Every remaining block is a finite triangle ofL. Its choice must cover every edge ofL exactly once and every finite translation orbit exactly once. Thus the exact-cover columns are E(L) and the finite triple-orbits; a row is a triangle ofL and meets its three pair columns plus its orbit column.

There are `(n−1)(n−2)/6` finite triple-orbits and `3·(n−1)(n−2)/6` remaining finite edges. Any exact cover supplies exactly the required number of finite blocks. Together with the two infinity-matchings and{0,u,w}, it is a transversal STS(v). The driver additionally checks all concrete unordered pairs and all complete triple-orbit keys directly before attempting a resolution.

No class variables enter Stage2. At a frozen matching pair it is an exact STS-completion model, not merely a relaxation. The portfolio as a whole is incomplete because only finitely many matching pairs and candidate STSs are sampled.

## 3. Native CNF

Every exact-cover column with literalsx1,…,xk receives an at-least-one clause. For k≤3 the at-most-one condition is pairwise. Otherwise introduce prefix variabless1,…,s(k−1) and clauses:

- `¬x1∨s1`;
- for2≤i≤k−1: `¬xi∨si`, `¬s(i−1)∨si`, `¬xi∨¬s(i−1)`;
- `¬xk∨¬s(k−1)`.

Two selectedx values would force the prefix at the earlier index true and contradict the later negative-prefix clause. Conversely, with at most one selectedx, choose each prefix true exactly after that selected index; all clauses hold. Thus this is an existentially exact at-most-one encoding. Empty columns become empty clauses. The implementation writes a fixed-width DIMACS header, avoiding retention of all clauses in Python memory.

A sampled STS is subsequently blocked with the clause consisting of the negations of all its selected primary variables. This excludes exactly that candidate block set among exact covers. If its resolution timed out, the block is a **portfolio diversification decision**, not a logical inference that the STS is nonresolvable; the ledger explicitly counts these skipped unresolved candidates.

`replay_staged_cnf.py` reconstructs exact primary-row order from the saved matching seed, then replays preceding candidate-blocking clauses in order. The resulting SHA256 was exercised on both an initial9-point CNF and a15-point CNF with sequential auxiliaries and two blocked candidates; both hashes matched the corresponding solver receipts (`evidence/extended-cnf-replay-checks.json`).

## 4. Unrestricted resolution of the frozen STS

Each block is assigned to exactly one of `(v−1)/2` classes. Every point/class incidence is covered exactly once. The unique u-block of each class canonically labels that class by its unsigned difference; class0 contains{0,u,w}. This relabelling is lossless because each u-block has a different unsigned difference. No multiplier or reflection action is imposed on the chosen resolution.

The implementation can discard placements intersecting the already fixed u-block of a class, except for that anchor itself. This removes precisely impossible placements. The block-exactly-one and point/class-exactly-one constraints then define an actual resolution, not merely the correct class sizes.

On success, translating every class by every element ofZ_n gives the full LKTS. The standalone checker validates the expanded certificate without consulting any orbit keys, matchings, SAT assignment, or construction theorem.

## 5. Exercised validations and epistemic limits

- Native Kissat4.0.4 reproduced a fullLKTS(9) from frozen valid infinity matchings.
- Native CaDiCaL3.0.1 and CP-SAT9.15.6755 each reproduced a fullLKTS(15), rejecting two nonresolvable candidate STSs before finding a resolvable one.
- The independent checker passed all three expanded certificates.
- Exact CNF regeneration, including blocked-candidate clauses, matched recorded hashes.
- These checks establish exercised behavior on known cases, not complete correctness of every target search. A focused independent code/mathematical review is required for new claims; any target success requires independent certificate review.
- Solver INFEASIBLE/UNSAT is restricted to the encoded frozen instance and its explicitly blocked candidates. UNKNOWN and the final `UNKNOWN_PORTFOLIO_COMPLETE` are not nonexistence conclusions. Native logs retain statistics/status, raw-output hashes, and selected primary-row witnesses rather than redundant auxiliary-variable lines.

## 6. Joint modular model without frozen infinity matchings

`work/search_modular.py` replaces Stage1+Stage2 by one exact integer model. For each unsigned differenced∈{1,…,(n−1)/2}, an edge of that difference has a unique orientation `{a,a+d}`, a∈Z_n, because n is odd. Introduce start variables `a[u,d]`, `a[w,d]`. Their modular endpoints `a[s,d]+d modn` and starts are all constrained to{1,…,n−1}; for eachs the n−1 endpoints are all different. Thus each infinity gets exactly a rainbow perfect matching of the nonzero finite points.

For each finite triple-orbit choose a fixed representativeB and one shiftc_B∈Z_n. For each pair{x,y}⊂B, orient its unsigned differenced by choosing offsetp so that the pair is{p,p+d}. Its concrete position after translation is `c_B+p modn`. For everyd put all these finite-block pair positions, together with `a[u,d]` and `a[w,d]`, in one all-different constraint.

There are exactlyn entries in each such constraint: every finite pair of differenced belongs ton−2 finite triples, and quotienting their incidence count by the free n-point translation action gives n−2 finite-orbit pair incidences, plus the two infinity edges. Hence all-different is equivalent to covering each of the n concrete pairs of differenced exactly once. Repeated differences within an AP representative are retained as separate incidences with different offsets; they must not be dropped.

Together with{0,u,w}, the selected blocks therefore form a cyclic-transversal STS(v). Conversely every normalized cyclic-transversal STS(v) determines all these variables. The only extra symmetry break orders the two distinct infinity start positions for d=1; exchanging the namesu,w always satisfies one ordering, so this is lossless. It does not require an infinity-swapping automorphism of the design.

The primary variable count is `(n−1)+(n−1)(n−2)/6`, namely531 at57 and1246 at87. Modular endpoint/pair-position variables are additional; the solver may introduce further internal encodings. Every resulting concrete STS is checked directly, then passed to the same unrestricted resolution model and final independent LKTS checker. This removes the frozen-matching restriction of the six staged configurations, but its bounded run and skipped unresolved candidate resolutions still do not exhaust all cyclic KTSs.
