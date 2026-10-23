# InfoCFR33 final report (worker task output, saved by parent 2026-10-17 16:15:38 PDT)

I didn't construct anything new. CFR(4,33) was already known: a published SageMath table entry implies it, so no search was needed. On the CFR(5,27) alternate I found no witness, and nothing proves it doesn't exist, so it stays UNKNOWN. Nothing of mine is running now (checked 16:14:43 PDT), and 18.15 GB of disk was free at that point.

Everything is under `information-science/evidence/six-lane-20261016/cfr33/` (`MANIFEST.sha256` 207c1a3a…41f3, 579 files). Event counts were computed as r·n·(n−1): 4,224 for CFR(4,33), 3,510 for CFR(5,27), 5,280 for CFR(5,33).

### CFR(4,33): already known (prior art)
- **Why the target is dead:** a CFR with r rows of length n exists exactly when a cyclic difference matrix over Z_n with r+1 rows exists (proof in `notes/facts-v1.md` E2). SageMath's `DM_33_6_1` is such a matrix over Z_33 with 6 rows. Its docstring cites the Handbook III.3.56; I did not read the Handbook itself.
- **Source:** it sits in `src/sage/combinat/designs/database.py` at develop 0835358c (file sha 55a30e8a…23a9). The same entry, with identical literals and expansion, is in the 6.4 tag from 2014-11-14. The group is `IntegerModRing(33)`, so it is cyclic directly.
- **Re-check:** I rebuilt the matrix from the pinned literals without Sage. All 15 row pairs pass. Converted, it gives CFR(5,33) (5280/5280 events) and CFR(4,33) (4224/4224 events), and both pass the direct-event checker and the separately written position-difference checker.
- **Controls:** 62 mutation expectations all behaved as intended. Kirtchakov's CFR(5,25) passes both checkers.
- **Files:** the receipt is `prior-art/receipt-v1.json`. You have reproduced the result independently, byte for byte.

### CFR(5,27): UNKNOWN
**Literature screen:** I found no theorem that rules out a 6-row difference matrix over Z_27.
- Pan et al. (DCC 2022) show the 5-row version over Z_27 exists, which is CFR(4,27).
- The only relevant odd cyclic nonexistence result is the 4-row case over Z_9. The 2018 van Greevenbroek–Jedwab survey lists no general row bound for cyclic prime-power groups.
- I could not read the Handbook VI.17, Evans' books, or the bodies of the Ge 2005, Pan–Chang 2016 and Pan 2022 papers.
- Quotes are in `cfr27/notes/screen-cfr527-v2-nonexistence-theorems.md`.

**Restrictions I proved by hand** (notes facts-v2 to facts-v6). None of these says CFR(5,27) doesn't exist; each rules out one structured shape:
- **Multiplier models M2/M3:** impossible. Any symmetry that cycles rows while fixing two or more rows needs |Fix(mu)|² ≤ n, and 81 > 27.
- **Linear rows:** whenever 3 divides n, no normal form can contain a row c·x. The same idea forbids most linear relations among rows.
- **Per-row multiplier symmetry:** at n = 27 only the odd model (f(−x) = −f(x)) is possible.
- **Structured rows:** in any normal form, at most one row can belong to each of these families: maps preserving 3Z, maps ≡ −x mod 3, maps respecting the 9Z cosets, 10-equivariant maps.

**Restricted models searched to the end, no solution.** These were checked by my own exact search program, not by SAT with DRAT certificates; symmetry reductions are justified in facts-v4 R1:
- An f-row equivariant under the multiplier group <8>: all 96 representatives (1692 maps).
- An f-row ≡ c·x mod 9 for c ∈ {2, 5, 8}: 30 representatives.
- An f-row respecting the 9Z cosets with a non-linear induced map: 27 representatives.

An independent Python enumerator reproduced the search program's neighbour counts and pair counts exactly on 2 random inputs (4117/55 and 3997/54). The third input and the checks on the <8>-family representatives were stopped at wrap-up and not done.

**Sampled without success:**
- About 1,870 random odd first rows, 62 rows preserving 3Z, and 62 rows ≡ −x mod 3. Calibration: the same method found an odd CFR(5,25) after 72 random rows and CFR(4,27) in 1.9 s.
- kissat on the odd model, which I stopped at 1077 s because the custom search was far stronger.
- kissat on one row-cycling symmetric model (T6), which hit its 1800 s limit.

The contract's first-choice SAT approach was weak here: kissat could not find an odd CFR(4,27) in 600 s, while the custom search found one in under 2 s.

### Next representation
These are not started; details are in `cfr27/README.md` §4.3.
- An exact custom solver for the row-cycling symmetric models.
- Non-odd normal forms with a structured first row.
- A mod-9 then mod-27 lifting search (the top layer is 56 equations in 52 unknowns over GF(3)).
- SAT/DRAT certificates for the models listed above, if certified results are needed.

### Deviations
- **One SIGKILL despite the rule:** an eval-cell timeout made Python SIGKILL the wrapper of one control run (P21). The solver itself kept running and finished SAT, but that run has no record file. Since then everything has been launched detached; this is in `notes/deviations.log`.
- **Superseded search programs:** v1 had a bug and produced outputs that both checkers rejected, and v2 did not compile. Both are kept, not deleted.
- **Runs stopped early by SIGTERM:** the duplicate random runs on the 78-map mod-9 family, the n = 33 calibration and the P33 control.
- **Plan items dropped:**
  - M2 was settled by the written proof and never run on a solver.
  - A small survey job was prepared but never launched.
  - The README plan's 1-hour kissat passes were replaced by the custom search.

No commits, no deletions, no out-of-lane writes. Network access was read-only GETs, pinned in `sources/web/*.pin.json`. CFR(5,25) was used only as a control.
