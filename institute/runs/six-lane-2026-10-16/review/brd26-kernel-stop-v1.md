# Brd26Kernel report (verbatim)

Recorded 2026-10-17 13:33:21 PDT. Agent output is untrusted until parent-bound.

I've stopped. No Lean process is running (`pgrep` found none at 13:02:07 PDT), so nothing had to be terminated; the last build finished at about 12:58:39 PDT. I deleted nothing and changed nothing after your message, so `progress.md` still has only its 12:48 entry.

**No proof exists.** I never assembled the root `exists_brd26_130`, never ran `#print axioms`, never ran `leanchecker --fresh`, and wrote no controls, replay driver or manifest.

**Builds that completed** (all one at a time, `lean -j 1 -M 7168`; highest memory use was 6.12 GB):
- **Real modules:**
  - `Brd26/Data` (3.5 s): the 26×130 matrix literal generated from the raw file. `gen_lean.py --check` regenerates it byte for byte.
  - `Brd26/Target` (1.3 s): the property definitions, nothing proved.
  - `Brd26/Witness` (0.35 s): the explicit matrix `brdM`, with a kernel check that the data has 26 rows of 130 entries each.
- **Scratch probes:** each part of the property was checked by `decide +kernel` in a separate scratch module, and each passed:
  - entries in {-1,0,1}
  - 25 nonzeros per row
  - 5 nonzeros per column
  - every distinct row pair has exactly 2 products of +1 and 2 of −1 (`scratch/Probe_pairsAll`: 20.5 s, 6.12 GB)

  These were cost probes, not the deliverable: the four checks were never combined into one theorem.
- **Failed builds:** first attempts of `Witness` and `Target` (both fixed and rebuilt), and `scratch/Probe_prof2` (a typo of mine; no output file written).
- **Not built:** `Brd26/CertPairs.lean` and `Brd26/CertStd.lean`. I generated them from an unsaved Python cell, not a script in the directory.

**SHA-256 of sources and scripts** (in `review/brd26-kernel-worker-v1/`):

| File | SHA-256 |
|---|---|
| `Brd26/Data.lean` | `8afe003e9177cecd21cec0b57dcc4fcadd1f427dcfec2f1f075f48795df1c38e` |
| `Brd26/Witness.lean` | `1c5b1b5fafbdd6b5846f583ad6c1b4f6819b55a8e17d50715170f4ca66b9bf21` |
| `Brd26/Target.lean` | `5800bf01adfc480f543ebfab3090632f92a9305d80ae2c6e789e397e77f878bd` |
| `Brd26/CertPairs.lean` | `3fe67aca40fc3e306fb034e7cbb90e4662516dcb4615fa089b46507e3c2fc32a` |
| `Brd26/CertStd.lean` | `f039a657b067d4ef304fd9898c41fe6bd6763caeab20cce412ae0e225d02c644` |
| `gen_lean.py` | `d26986051b1ddb448fce6792d17e73ccaf10ad5994dec49941676b15fd3b3e57` |
| `lean_env.sh` | `31335cbed7002be9b989dd61297a45dd2889651bf23edab467ccf256578377a4` |
| `build_module.sh` | `dc1c0e2e67b6d3078923de27642e0e507a6f05e16636d05cbd9b914f93ea7b03` |
| `lean_source_scan.py` (unchanged copy of the reviewed scanner) | `8e9eb834f6bafa282c42ad793d71d82539d206c941e6d72fe5c4c2c8c8baf5bb` |
| `progress.md` | `9fd9f8aa789d04148849f96708e8a12d9fda1e7fedd665e7b32e6df788e6460f` |
| `scratch/Probe_pairsAll.lean` | `821052faac5b22c6958f49d1e8f0362f5659c775c62a9feeb4489e05cc4afaf3` |
| `scratch/ProbeA.lean` | `2ec5c43367b3497b93f37c570ecfa4f77bc06275005c22bae7abda2853b96ce3` |
| `scratch/Probe_alphabet.lean` | `ebb679c3167ce1959ae986e2a5714ff7d28164c47333fbaea56f62bdb7d309ff` |
| `scratch/Probe_rows.lean` | `331c86400fc491861472f05ebc5a95eb62c66720902780bd0ba2734f08972e05` |
| `scratch/Probe_cols.lean` | `96383f5a41e5a07c536e248ffadf7631f33f2fec1cbb19a90026cf5d23784c0a` |
| `scratch/Probe_pair0.lean` | `be867e43bbaf8bf266f18ba0b595142d465ac3f2a240f3e55864397d6f2f489b` |
| `scratch/Probe_pairs4.lean` | `6b5f2dbda225f6befdc42d8cfc2bf34aabb87f29c49bbb945a6b3c32cd14f88c` |
| `scratch/Probe_prof.lean` | `c11a11a92efb1ddce7fddf9979c04e87eb1e313e8845babb725f27e9464869f0` |
| `scratch/Probe_prof2.lean` | `ef253ecc2e160756f27b0343ab0bc703cb7574996f09cc52b89f355a3b90a70f` |
| `scratch/Probe_idx.lean` | `e17326a48a5d80126c156f9e1a2d1e347547777d5be2d659cff1060786a41274` |
| `scratch/Probe_listRows.lean` | `82a6bb38f3aa7be7f8995251c395c9eaa90bbfc8c389d47d1bb8814b2eab1c94` |
| `scratch/Probe_nthD.lean` | `c8aa25e4ae354c4caaa77b0f6b15278cdeed4f8dd46282d3d8ebd9c117fa8c8c` |

**SHA-256 of the three real build outputs** (`scratch/build/Brd26/`):

| File | SHA-256 |
|---|---|
| `Data.olean` | `b243c04e5508d79ff54e2acd29c5cd10ba82d6be4f28d732a00f82d177688cbe` |
| `Target.olean` | `1d5324ad854350cc78e00a6ae5758da33bb2d28ee02a81eb1fae2f5947635f17` |
| `Witness.olean` | `6f33742b923fad914ee7b866ec45be089cd606ef61c0ef22bc18497cde04861a` |

The rest of `scratch/build/` (probe compiled files) and all of `scratch/logs/` (timing and memory logs) are throwaway build output, 56 files; the whole directory is 4.7 MB. Running `shasum -a 256` over the directory lists every hash.

Two other points:
- The raw witness still has the pinned SHA (`eb15cba1…71fe`); I only read it.
- If this work is ever resumed: each kernel check on this matrix costs about 6.5 s and 2.2 GB just to look up the 3,380 entries. Splitting the pair check into 7 blocks of first rows (what `CertPairs.lean` does) keeps memory near 4 GB.
