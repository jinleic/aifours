# C19-invariant resolved LKTS(57): obstruction and staged search

Date: 2026-10-14 (PT). This note and `work/c19_search.py` concern the specified action on `Z_19 × {0,1,2}`, not arbitrary large sets. A point `(x,i)` is encoded as `19i+x`. Fixed constituents are required to have an invariant chosen resolution.

## 1. The 36-fixed pattern is impossible

A fixed KTS(57) has 28 classes. Under C19 their orbits have lengths 1 or 19, so there are either 9 or 28 fixed classes. A fixed class consists of one orbit of 19 triples. Each triple must meet all three layers, since its orbit must partition the 57 points. Thus 28 fixed classes would contain only ABC triples and could not cover within-layer pairs. There are exactly nine fixed classes and one free orbit of 19 classes.

Choose one class P from that free class orbit. All its 19 triples belong to distinct triple-orbits: two translated blocks in P would make the translated classes overlap, contrary to a resolution. Along with the nine fixed-class seed orbits, these are 28 distinct triple-orbits. Write u,w,z for the numbers of AAA, AAB, ABC blocks in P. All 27 within-layer pair-orbits must occur exactly once in P, so

`3u+w=27`, `u+w+z=19`, and hence `z=2u−8`, `u≥4`.

There are 51 AAA triple-orbits per layer, but **nine per layer cannot occur in any C19-fixed STS**, regardless of resolution. They are the arithmetic progression orbits represented by `{−d,0,d}`, with `d=1,…,9`. In such a block the two consecutive pairs belong to the same translation orbit; developing the block repeats pairs. Conversely, a three-element subset of Z19 has two pairs in the same unsigned difference orbit exactly when it is an arithmetic progression: after choosing their common endpoint, the other endpoints have opposite nonzero differences. The AP center is unique because 3 is invertible modulo 19, so these are exactly nine distinct orbits.

Consequently, only `3·(51−9)=126` AAA orbits are available to fixed STSs. Disjoint fixed resolved constituents each need at least four. In particular,

`36·4=144>126`.

This is a rigorous obstruction to the **entire 36-fixed + one free 19-orbit pattern**, not merely the staged search below. Together with the constituent orbit counts and the existing exclusion of 55 fixed constituents, only **17 fixed constituents plus two free 19-orbits** remain for this resolved C19 action. The bound does not exclude an automorphism of unresolved block systems whose chosen resolutions are not invariant.

The implementation exhaustively inventories all 1,540 triple-orbits and 84 pair-orbits, checks their lengths, identifies precisely the 27 AP orbits, and independently expands every triple-orbit to check whether its 57 pair incidences are distinct. The proof above does not rely on a negative solver answer.

## 2. Exact fixed-constituent model

For each admissible, non-forbidden triple-orbit and each of its 19 translates, a Boolean variable means that the translated block belongs to P. For each non-forbidden ABC orbit there is a second variable meaning that the full orbit is a fixed class. Exact-one constraints cover each of the 57 points of P and each of the 84 pair-orbits. They force 19 P blocks and nine fixed classes, and prevent repeated triple-orbits automatically. The generated constituent is expanded into 28 classes and all 1,596 concrete pairs are checked independently of the solver.

`--fixed-aaa` freezes u (default 4). Thus the default starter has four AAA, fifteen AAB and no ABC blocks. This is a search restriction, not a theorem that every possible constituent has this type.

Seventeen constituents are generated greedily, forbidding all previously used orbits. A failed candidate solve discards that greedy prefix and restarts with a new recorded seed. Each restart retains its final prefix in a separate packing file; every intermediate candidate and forbidden prefix is preserved in the phase receipts. The first complete packing is frozen. This does not enumerate all possible collections of 17 constituents.

## 3. Exact free-base completion of a frozen packing

Seventeen fixed constituents use 476 triple-orbits. The complement has 1,064 orbits. For each remaining orbit, each of its 19 blocks, each of two free bases, and each permitted class, a Boolean variable places that block in the base/class. Constraints require:

- exactly one placement overall for every remaining triple-orbit;
- exactly one occurrence of each concrete pair in each base;
- exactly one occurrence of each point in every class of each base.

Thus both bases are resolved KTS(57)s, each using 532 distinct triple-orbits. Their 38 translates and the 17 frozen constituents partition all triples. No additional automorphism of a free base is required.

Class-permutation symmetry is removed losslessly by sorting classes by the least other point in the block through point 0. In class c (zero-based), this least point lies between c+1 and 2c+1: the blocks through 0 form a perfect matching on points 1,…,56. The two bases are ordered by the third point of their block through pair {0,1}; those third points differ because their blocks cannot share an orbit. This removes only interchange of the two bases.

A completion INFEASIBLE would exclude only this particular frozen packing, not all C19-invariant large sets. UNKNOWN is never promoted to nonexistence. A positive result is expanded in the existing `LKTS/KTS/CLASS` text format and passed to `work/check_lkts.py`.

## 4. Reproduction and receipts

Run from the target directory; existing receipts are never overwritten:

```sh
python3 work/c19_search.py --fixed 36 --seconds 7200 --threads 2 --seed 193614 --output evidence/c19-36-obstruction
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --offline --with ortools==9.15.6755 python work/c19_search.py --fixed 17 --seconds 7200 --threads 2 --seed 191714 --fixed-aaa 4 --candidate-seconds 90 --output evidence/c19-17-staged
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --offline --with ortools==9.15.6755 python work/c19_search.py --fixed 17 --seconds 7200 --threads 2 --seed 191715 --fixed-aaa 5 --candidate-seconds 90 --output evidence/c19-17-staged-u5
```

The total wall deadline includes inventory, model construction, candidate solves and completion. Each solver receives only the remaining time, capped by `--candidate-seconds` for a candidate solve. Receipt phases record actual times, exact solver parameters, seeds, fixed restrictions, source and instance SHA256 hashes, logs and all found starter/fixed-class data. Each run preserves its executable source snapshot and full orbit inventory. Peak resident memory is recorded using macOS `ru_maxrss` (bytes). The two 17-fixed slices ran concurrently with two solver workers each, at most four in total; stages within a slice ran sequentially. Use fresh output prefixes, for example under `/tmp`, to replay without overwriting original receipts.

## 5. Actual bounded outcomes

All runs below terminated normally. No full LKTS(57) certificate was found.

| Pattern/slice | Total seconds | Observed stages and result | Receipt |
|---|---:|---|---|
| 36 fixed + one free orbit | 0.096 | Entire pattern **PROVED IMPOSSIBLE** by §1; exhaustive orbit arithmetic passed. The requested 7,200-second cap was not consumed because of the rigorous early obstruction. | `evidence/c19-36-obstruction.json` |
| 17 fixed, every starter u=4 | 7200.134 | All 17 disjoint fixed constituents found by 119.988 s, with no restart. Frozen-complement model built in 5.152 s; two-free-base completion ran 7074.986 solver seconds and returned **UNKNOWN**. | `evidence/c19-17-staged.json` |
| 17 fixed, every starter u=5 | 7200.028 | 288 candidate solves: 259 OPTIMAL and 29 UNKNOWN; 29 greedy restarts. Largest disjoint prefix had 15 constituents. No 17-packing was found, so free-base completion was **not reached**. | `evidence/c19-17-staged-u5.json` |

The u=4 frozen packing is a genuine positive auxiliary object: 17 pairwise block-disjoint, C19-invariant resolved KTS(57)s. Its 476 triple-orbits leave exactly 1,064. It is **not** a large set or evidence that the complement admits the two required free bases. The exact data are `evidence/c19-17-staged.frozen-packing.json`, SHA256 `6515e4041991d0c857df9c5d5752613f8d958d4ee76296cbbc24c024b807d714`.

The u=4 completion had 1,087,824 Boolean placements. It exercised 194,393,829 branches and 1,211,542 conflicts, so the timeout was not spent solely building or presolving the instance. Its model SHA256 is `22b64780769110e86923ba9ae93e760863b8a41ade4d2d080de06520a7f3db19`. The u=5 candidate solves used 7164.234 aggregate solver seconds, 273,269,109 branches and 7,812,431 conflicts. OPTIMAL here is CP-SAT's feasibility-success status, not an optimization claim.

The two search processes' peak resident sizes were 5,206,310,912 and 2,817,654,784 bytes. Their sum is 8,023,965,696 bytes, below the 12 GB assignment cap. Both owned search processes exited; no owned search service remains running.

### Independent executable replay

`work/c19_verify.py` is a standard-library-only implementation independent of the searcher's canonicalization and KTS checking routines. It enumerates all 19 group elements when forming orbit representatives; verifies the 27 arithmetic-progression exclusions by concrete pair multiplicities; expands every generated candidate; checks every class, pair, block and group action; and reconstructs all disjoint prefixes and the frozen complement.

The executed commands were:

```sh
python3 work/c19_verify.py evidence/c19-36-obstruction.json evidence/c19-17-staged.json --output evidence/c19-validation-initial.json
python3 work/c19_verify.py evidence/c19-17-staged-u5.json --output evidence/c19-validation-u5.json
```

Both returned **PASS**. They independently checked all 276 generated fixed-KTS candidate witnesses (17 in the u=4 run, 259 in the u=5 run), including all abandoned prefixes. This does not claim all those witnesses are distinct. The replay also checked that every pair-orbit has exactly 38 remaining incidences after the frozen 17-packing. It does not turn UNKNOWN into UNSAT, and no negative solver proof was generated.

All three runs bind search source SHA256 `84a908183e3a461b57f280ba52bbc567d045fcbc22ffc3b98dec73bb61768d1b` and inventory SHA256 `a6e07e3dd0940799826266c2ae4a7159c54c414fe5c10ffd7d5573ad6ba56454`; their source snapshots are preserved beside the receipts. The independent verifier SHA256 is `9f62024c7d9e6b7d2ca71cc9dc06797aaa4154df2188a70b2e05263b63a5938c`.

## 6. Precise remaining target and next action

Only the **17-fixed + two-free-orbits** pattern survives the whole-pattern C19 obstructions established here. These runs covered one frozen u=4 packing and a bounded greedy u=5 packing slice, not all such invariant large sets. They leave even the u=4 frozen-complement existence question unresolved.

The next useful construction experiment is to reuse the checked 476-orbit packing and first solve only the **two orbit-transversal STS pair covers**, postponing resolutions. That first exact model needs 40,432 placement variables (`1064·19·2`) instead of 1,087,824 class-indexed variables. For a positive pair-cover solution, separately color each 532-block system into 28 parallel classes, backtracking to a different pair cover when resolution fails. This is a proposed next experiment, not implemented or run here, and a nonresolvable first STS pair must not be treated as an obstruction to the frozen complement. Independently, the u=5 results motivate packing a pooled candidate family rather than throwing away a 15-system prefix at a 90-second timeout.

