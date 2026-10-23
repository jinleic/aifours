<!-- Parent transcription 2026-10-17 18:23:34 PDT of subagent Cfr27ParentReproduce's final report (agent://Cfr27ParentReproduce), verbatim below. Its receipt is review/cfr27-parent-reproduce-v1/receipt-v1.json. -->

Both candidates reproduce exactly. A binary rebuilt from the frozen source regenerates both DM raws byte-for-byte equal to the parent pins, and my own independent audits of the group action and of the DM→CFR conversion pass too. I make no gate, novelty, priority or isomorphism claim.

**Where it is:** `institute/runs/six-lane-2026-10-16/review/cfr27-parent-reproduce-v1/`. The receipt is `receipt-v1.json` (sha256 `e8b1f77c8eb38ee993e37d6c36dad7dcac4878b35dca5efc726edd92085feb72`). It hashes all 55 files in the folder, re-hashes the lane originals and the parent pins (unchanged), and records the exact commands, limits and run results. Work ran 17:50–17:58 PDT, so no 30-minute checkpoint was needed.

**1. Rebuild and replay of the producer**
- **Pinned inputs:** 13 lane files were copied only after their hashes matched the freeze record: the freeze `c24cb110…`, the C source `8aea035d…`, `dm_to_cfr.py`, the model compiler, the T10/S3a spec and model files, the worker's output logs and DM raws, and the worker binary (kept as `.noexec`, never run). All 23 hash and group claims inside the freeze record check out.
- **Compile:** run in `build-savetemps/` with `TMPDIR=build-savetemps/tmp/`: `cc -O2 -march=native -Wall -Wextra -save-temps=obj -o bin/dmorbit_xc_v1 code/dmorbit_xc_v1.c`. The only change from the worker is `-save-temps=obj`. It exited 0 with no warnings, using Apple clang 17.0.0 (clang-1700.3.19.1).
- **Binary:** `b9ab685625436c942ee8a2214f321453d7ab01b131049664b2d707f7aa572158` is byte-identical to the worker's binary. The `.i`, `.bc`, `.s` and `.o` intermediates are kept and hashed. Because the binary already matched, I skipped the planned two-step build.

| Run | Arguments | Exit / status | Wall time | Max RSS | DM output |
|---|---|---|---|---|---|
| T10 | `T10.model 180 zero first` | 10, `s SATISFIABLE` | 9.18 s | 13.2 MB | `b8eec25f…` = `A-DM.raw` |
| S3a | `S3a.model 180 nozero first` | 10, `s SATISFIABLE` | 9.55 s | 20.0 MB | `3f45f8c3…` = `B-DM.raw` |

- Search node counts (3,296,253 and 6,082,255), option counts and root items match the worker's logs. The comparison ignores only the time limit, timings and output path.
- The printed base columns equal the ones in the freeze record. No SIGTERM was sent and no resource limit was hit.
- Recompiling both specs with the lane's model compiler gives model files byte-identical to the pinned ones.

**2. Independent group-action audit** (standard library only, no lane imports, group elements as matrices mod 27)
- **T10:** a cyclic group of order 6. Orbit sizes are [1,2,6,6,6,6]. The 5 base columns from the freeze plus the zero column expand to exactly the 27 columns of `A-DM.raw`. The DM is invariant under the generator and all 6 group elements.
- **S3a:** a non-abelian group of order 6 (S3). Orbit sizes are [3,6,6,6,6], with no column fixed by the whole group. The expansion matches `B-DM.raw` exactly, and the DM is invariant under both generators and all elements.
- The group listed in each model file equals the group stated in the freeze record. Each model lists exactly one representative row pair per orbit of row pairs.

**3. DM→CFR conversion** (written from the definitions, all arithmetic mod 27)
- Regenerating the CFRs gives files byte-identical to `A-CFR.raw` (`6ceed793…`) and `B-CFR.raw` (`a9faf3dd…`).
- Each CFR has 0 violations across all 3,510 (symbol pair, distance) checks, and all 15 DM row pairs pass.
- Rebuilding a DM from each CFR (row 0 all zeros; row j gives each symbol's position in CFR row j−1) gives back the original column multiset. A short proof of both directions is in the receipt.
- Row 0 of both pinned DMs is all zeros, so the conversion step itself involves no real subtraction here. The mod-27 arithmetic matters in the validity checks.

**Controls:** all 13 behaved as expected.
- The required invalid generator (mu=1, swap rows 0 and 1) breaks invariance for both DMs.
- Wrong multipliers break invariance: mu=1 and mu=19 with the 6-cycle for T10, and mu=10 for S3a.
- For T10, using the opposite action convention (c_{pi(x)} instead of c_{pi⁻¹(x)}) fails, so the freeze's convention is the one the DM satisfies. For S3a the swap produces the same group, so that control cannot discriminate there.
- A perturbed base column no longer expands to the DM.
- A mutated DM gives 4 bad row pairs and a different CFR with 16 violations.
- Under base-3 digit arithmetic (the additive group of GF(27)), 10 DM row pairs fail and the CFRs show 144 and 128 violations. These are cyclic Z_27 objects, not GF(27) ones.

**Things to know:**
- The producer's time limit was 180 s instead of the worker's 10800.
- The producer writes the `.dmraw` with exclusive create (`O_EXCL`, mode 0444) according to the source code. I also made sure each output path did not exist before the run.
- One side effect outside my folder: xcrun's per-user cache file (`/var/folders/…/T/xcrun_db`) grew from 2514 to 2670 bytes at 17:52:34. That is the same second as my toolchain-version queries (`cc --version`, `xcrun --find clang`, `ld -v`), so they most likely caused it, though that is inferred from timing. xcrun does not follow `TMPDIR` for this cache. The file did not change during the compile, and I left it as is.
- The "orbits" lists in the spec files are placeholders the producer ignores.

**Not claimed:** that A and B are non-isomorphic or isomorphic, or any CFR-level symmetry. The group invariance is only a property of the DM's columns, taken up to adding a constant. Witness validity rests on checks of the raw bytes, not on the producer or the symmetry model.

**Resources:** one busy CPU at a time, at most 20 MB RSS, 570 KB of new data, and 17.3 GB of free disk afterwards (above the 12 GB floor). The folder has no `__pycache__` and every temp folder ended empty. You don't need to run anything else for this audit.
