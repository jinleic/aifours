# Olson uniform review desk: RZ-wide, S2-wide, A0/C0-all

Written 2026-10-17T23:16:37.398666-07:00 by the delegated review desk (subagent OlsonUniformReviewDesk). This is a correctness review only. It does not certify novelty or significance, and the parent makes the final call. The lane files were only read. No lane fixes, commits, pushes, network requests, external contacts or paid APIs were used. Claimant code was not run by the desk or by either reviewer.

## Targets (hashes verified; they match the task pins and c6/out/freeze.txt lines 187, 194 and 206)

| ID | lane file (L = .../olson/inverse-run-count/mixdef-high/c6) | sha256 |
|---|---|---|
| T1 | L/proof-RZwide.md | f6aff2e2a6cf5eb84419302e4d28c1323c10569b1aff854fa1028413980962a9 |
| T2 | L/proof-S2wide.md | bf697c7967982f354100fdadd05a2381c750f90a62c1ca14422709741cf20451 |
| T3 | L/proof-A0.md | 5c4a0dda2b1d03439ab728d8f787a0785024c87699621fce71df28a3860e413e |

## Result

| Reviewer | overall | T1 | T2 | T3 | FATAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|---|
| Codex gpt-6.1-sol (static; read/sha only) | ACCEPT-WITH-FIXES | ACCEPT | ACCEPT | ACCEPT-WITH-FIXES | 0 | 0 | 1, plus 1 optional uncounted remark |
| Claude claude-opus-5-5 (no tools) | ACCEPT-WITH-FIXES | ACCEPT-WITH-FIXES | ACCEPT-WITH-FIXES | ACCEPT-WITH-FIXES | 0 | 0 | 12 (T1 2, T2 5, T3 5) |

- **FATAL: none (both reviewers). MAJOR: none (both reviewers).**
- Neither reviewer found a mathematical error. Neither found an integer solution of (L) or an import used outside its hypotheses. Every finding is about the record or wording, or offers an optional simplification.
- Both runners exited 0 with status NOTE_RETURNED_UNVERIFIED. I read both notes in full and re-checked their central computations (see Verification below).

### Findings both reviewers made independently
1. **T3 dependency status (task question).** Theorem C0-all (proof-A0.md:40-41) and its Corollary (proof-A0.md:66-70) are stated unconditionally. The only qualifier is "(under review)" in the Dependencies line (proof-A0.md:5).
   - Codex M1 says to state them as conditional, using this wording: "Theorem C0-all, conditional on Lemma C0W. Assuming Lemma C0W of c6/proof-C0WB.md in its stated NMH setting, for every NMH word with R<=2p-3, the integer system (L) has no solution". It gives a matching corollary wording.
   - Claude T3-m1 says no qualifier is mathematically required: C0W was re-verified, it was reviewed in r0, and it is byte-identical in r1. Claude still asks for the record to be corrected and supplies conditional wording in case r1 governs.
   - **Desk recommendation, following the task instruction:** label C0-all and its Corollary as conditional on Lemma C0W until the parent accepts C0W's status. Lemma A0 itself is unconditional; both reviewers agree.
2. **T2's parity rule is unnecessary (optional; not an error).** proof-S2wide.md:30-36. Both reviewers note that c = 1 throughout also works; the exceptional set then shrinks to (Delta,h) = (3,0), (3,2), (4,1).
   - Both checked (p,g,B) = (11,6,2) by hand: j2 = 3, j1 = 1, footprint 11 = n-B-4. Claude also checked (11,3,3).
   - The desk's own arithmetic agrees: S_mut_c1 below, every class with p <= 401, 0 failures, with exactly those 3 exceptional families.
   - The five-family proof as written remains correct.

### MINOR map (reviewers' findings; not applied)
Codex (1):
- M1, proof-A0.md:5, :40, :66: state C0-all and the Corollary as conditional on C0W, as above. Codex verified that the DF/C0W passages of r0 (L27-29, L33-49) and r1 (L39-41, L45-61) have the same sha256, ead66341...7175. It also re-checked the C0W argument directly.
- Uncounted optional remark: the T2 parity rule (above).

Claude (12):
- **T1-m1, proof-RZwide.md:7-8.** The import list omits Lemma H (used at L38). It does not say that the "actually empty interval" alternative (L62) comes from the SEEDG r2 delta, which a parent desk accepted without CLI re-review. Corrected import text is supplied.
- **T1-m2, proof-RZwide.md:32.** The no-wrap reason covers only one side of the cycle. Correct reason: the path ends t±2 are at cyclic distance min(4,k-4) >= 2 (k >= 10). The conclusion is true.
- **T2-m1 (optional), proof-S2wide.md:30-32, :36.** The parity rule is unnecessary, as above.
- **T2-m2, proof-S2wide.md:6-8.** The import list omits NW, GS(a), Lemma H, W-ALL, SEED and RZ-wide (used at L73-74, L15-17, L86-89). It also gives no delta/review status. Corrected list supplied.
- **T2-m3, proof-S2wide.md:21-26.** The packing-lemma proof omits no-wrap (k >= 11) and the properness of Q+t. The conclusion is true.
- **T2-m4, proof-S2wide.md:90 (title L1).** The scope sentence "closes ONLY the all-single-letter NMH subcase" overreaches. NMH allows k = 2p-2. Counterexample to the scope: p=7, g=1, B=4 gives k = R = 12 = 2p-2, an all-single-letter NMH word outside the Corollary (R <= 2p-3) and outside the c3 setting. "Closes" is also too strong for unreviewed [W] work. Corrected sentence supplied. The desk checked the NMH membership: 8 <= k=12 <= 12, 1 <= B=4 <= kappa-1=4, A=8 <= 13.
- **T2-m5 (cosmetic), proof-S2wide.md:59.** The table is arithmetic in the free integer g (with B = g-h >= 2 and p = 2g-h+Delta prime), not in B.
- **T3-m1, proof-A0.md:4-6, :40-41, :56-57.** C0W status, as above. Exact replacement wording is supplied for L5, after L41, and L56-57.
- **T3-m2, proof-A0.md:4-6 vs :66-70.** The Corollary's imports are unlisted: the SEEDG-r2 lifts with P0, TS, GS, NW, SL and SCW-G, and the SEEDGstar-r1 lemmas SCW-G*, QQ and SEED-G*. No version is named for SCW-G*. (PIN) is stale (automatic in r1) but harmless.
- **T3-m3, proof-A0.md:66-70.** The Corollary's quantifiers are unstated. Corrected version: (a) some run has an empty intersection of seeds from actual GS(a) configurations; (b) every run has a quality seed; or (c) every run has a nonempty (QS*) seed and the seeds satisfy (P2). Under (b) and (c), singletons come from the canonical lifts. Corrected statement and proof are supplied.
- **T3-m4, proof-A0.md:71.** "Universal seed existence remains open for words with excess" implies that seed existence is settled for E = 0. W-ALL and SEED (B = 1) are not SEED-G quality-seed certificates. Corrected sentence supplied.
- **T3-m5, proof-A0.md:17.** The Kill criterion is stated without "proper" and without a source (c3/proof-C-r1.md:43-46; Lemma H). There is no gap, since P at L32 is proper.

## Verification of the reviewers' central evidence (desk)
- Codex static compliance: its stderr shows 30 shell executions, all read-only: nl 23, sed piped to shasum 2, shasum 2, rg 2, cat 1. All ran with cwd inside the snapshot. It ran no python, solver, network or write.
- Claude's receipt: model claude-opus-5-5, tools [], 1060.6 s. The usage outputTokens (128,748) is slightly above maxOutputTokens (128,000), but the note is complete: it has the counts table and the closing paragraph. One cosmetic chunk-join artifact appears ("proof-LB" / "-r1.md" split by a blank line).
- Hand re-checks by the desk:
  - Claude's T2-m1 arcs for (11,6,2) with c=1 give Q(7,4) = [5,5], Q+t+ = [6,6], Q+t- = [5,5], seeds [1,1] and [0,0] inside the QS windows [0,1] and [-1,0]. For (11,3,3) with c=1, the seeds are [0,2] and [-1,1] inside [-1,2] and [-2,1].
  - Codex's and Claude's kappa=3, p=7 arcs: [3,3], [3,4], [2,3]. Raw seeds are [0,1] and [-1,0]; clipped to the canonical ranges, [1,1] and [-1,0].
  - Both reviewers' smallest exceptional instances are (7,2,2), (11,5,3), (11,6,2), (11,4,3) and (11,3,3). They equal the first rows of the desk's no-split mutation failures.
  - Claude's T3.6 spot checks: W(5,1) forces x_al = 1 and x_an = -1, and the anti run plus an isolated aligned run kills (0 < 1). W(11,3) with x_an = -3 gives Case B with Delta = 0 and kill -2 < -1. W(11,3) with three isolated aligned zeros gives an A0 kill, 0 < 1.

## Desk arithmetic spot-check (own code; no lane imports; [F] aid only, not a premise)
olson-uniform-desk-check-v1/desk_check.py (sha256 96184e605291af1b93e69acbe1f63baa8a832c7ca66d70e9bd00fbd77d7e204a) and desk-check-result.json (sha256 229402359cda8d536917128b189d36ed12b2e24df7a4481491423df2f4e34924). One process, 55 s, exact integers.
- **R (RZ-wide classes, 7 <= p <= 401):** 906,860 classes and 1,813,720 target signs (the same counts as the producer's receipt). The checks cover the recipe, availability inequalities, genericity of the four arcs, GS(b) QS bounds and NW. 0 failures. 37 class-signs have an actually empty class-level GS(a) interval, which is a direct exclusion. Mutation c := 1: 899,872 failures.
- **S (S2-wide classes, p <= 401):** 899,911 classes: 899,535 default and 376 exceptional (76/75/75/75/75). There were 0 failures and no mismatch with the T2 Sec. 3 table. No-split mutation: 376 failures. c := 1 everywhere: 0 failures, with exceptional families (3,0), (3,2), (4,1) only.
- **K (literal proof constructions on explicit cyclic words):** random placements give 3,360 RZ words / 140,280 targets and 3,030 S2 words / 128,880 targets. Adversarial layouts (one block, alternating, block straddling 0) give 9,000 words / 522,300 targets, for p <= 43. All produced 0 failures in non-adjacency, block counts, mass and properness.
- **C (C0-all chain on random NMH run structures; random integer vectors in the singleton windows with sum p):**
  - The plain generator gave 6,050 vectors (Case A 4,904, Case B 1,146) and the parametric generator 9,360. The Case-B-biased run gave 15,480 vectors, of which 1,029 are Case B: (i) 400, (ii) 569, (iii) 60.
  - Checks:
    - A0 first-prefix kill;
    - exact identity (2.2), the bound (3.1) and (B1+) |X_o| >= 2Delta+s0;
    - the (B2+) kill in cases (i)/(iii) and the C0W kill in case (ii), each checked against lam(D_Q, m(Q)).
  - Result: 0 failures. Mutation (A0 target g instead of g+1): 4,050 and 5,162 failures.
- These controls are the desk's own. They are not the producer's controls (seedRZwide2, seedS2wide, defect_prefix), which were not replayed.

## Import manifest and status (snapshot olson-uniform-inputs-v1/manifest.json, sha256 4b1a9119283df624ecc020fbadba0431367f524d3523d164f5f23ae99e98776c; 39 pinned files + manifest)
- c6/proof-SEEDG-r2.md 353b0e95...30b7: r1 Codex and Claude ACCEPT-WITH-FIXES; r2 DELTA-ACCEPT-WITH-NOTES (olson-c6g-r2-review-summary-v1.md).
- c6/c5-fixes/proof-Cplus-r2.md 00e850cf...48bd3: r1 Codex ACCEPT and Claude ACCEPT-WITH-FIXES; r2 C4 delta parent-verified.
- c3/proof-C-r1.md b5eb9fa7...b65b: Codex ACCEPT.
- c3/proof-WALL.md 4808abcf...9442: Codex ACCEPT.
- c6/c5-fixes/proof-SEED-r3.md 474396f2...936e: r2 Codex ACCEPT and Claude ACCEPT-WITH-FIXES; r3 wording-only delta accepted.
- c6/proof-C0WB.md ac52d85f...de77 (r0, cited by T3): Codex 0/0/5 and Claude 0/0/6, both ACCEPT-WITH-FIXES; DF, C0W and C0B judged correct.
- c6/proof-C0WB-r1.md 7a387300...4084:
  - At snapshot time (22:53 PT) this was an unreviewed repair; DF and C0W were byte-identical to r0, which the desk confirmed by diff.
  - **Update (23:1x PT, IRC from OlsonRepairDeltaDesk):** REVIEW/olson-repair-delta-v1/delta-check-v2.md (sha256 573c62e59a41a240b2aaeee05b7c23265cd732a495d22de4de8b40cdcdd1c04c) gives C0WB-r1 DELTA-ACCEPT-WITH-NOTES (desk) and DELTA-ACCEPT (Codex delta). It confirms that DF/C0W/C0B at r1:39-81 equal r0:27-69. That record is advisory; the parent decides.
- c6/proof-SEEDGstar.md 476e9a28...5b22 (r0 ACCEPT-WITH-FIXES) and -r1.md 8d4c8449...0806: r1 repairs were unreviewed at snapshot time; per the same repair desk, now DELTA-ACCEPT-WITH-NOTES.
- inverse-parity/proof-PAR-K0.md 4b107fff...9a38: Lemma H and the Claim; Codex ACCEPT.
- Definitions: mixdef-high/README.md Secs. 1-2 (91ca3716...) and c6/README.md Secs. 1, 3 and logs 22-25 (50751f25..., equal to freeze line 316).
- Context only: c6/proof-LB-r1.md (cc337fc8..., unreviewed; both reviewers found no silent reliance), plus the producer's control code and receipts.

## What the reviews support (subject to the listed fixes; parent decides)
- **T1 Theorem RZ-wide [W]:** every all-single-letter NMH word with g = kB >= 1, B >= g+1 and kappa <= p-3 (p >= 7) has an identity 2p-subword, for every anti placement.
- **T2 Theorem S2-wide [W]:** the same for g >= B >= 2.
- **T2 Corollary:** with W-ALL and SEED for B = 1, every all-single-letter NMH word with R = k <= 2p-3, for every prime p >= 5, has an identity 2p-subword.
  - It uses no finite or computer-assisted premise.
  - It rests on T1, T2, SEEDG-r2 (whose r2 is delta-accepted), W-ALL and SEED-r3.
  - It does NOT cover all-single-letter NMH words with k = 2p-2 (Claude T2-m4).
- **T3 Lemma A0 [W]:** unconditional.
- **T3 Theorem C0-all [W]:** the integer system (L) is infeasible for every NMH word with R <= 2p-3, **conditional on Lemma C0W**.
- **T3 Corollary [W]:** count-free seed certification, conditional on C0W. Per both reviewers, it removes the C0+ count condition from the seed-certified implications of SEED-G and SEED-G*. It does not establish seed existence, which stays open in general (in particular with excess).
- Not claimed by the targets and not supported: NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, ordered Olson. No novelty or priority search was done, and no firstness claim is made.

## Artifacts
| artifact | sha256 |
|---|---|
| olson-uniform-inputs-v1/manifest.json | 4b1a9119283df624ecc020fbadba0431367f524d3523d164f5f23ae99e98776c |
| olson-uniform-codex-review-v1.prompt.txt | 3ed105d92fcc663d5144e6ae02cff4b329f28e6a6ef562650f8b409936a93fb0 |
| olson-uniform-codex-review-v1.note.md | 17e7792f574f7a22f1cb768eb5d2cc4558ccb3eae8f8b120b841b62a48e882ac |
| olson-uniform-codex-review-v1.receipt.json | 0286f05d1501cd4060825a317b9f253d44af5445ad3df97503acfdb3dd533ea0 |
| olson-uniform-codex-review-v1.stdout.txt | 3d825ff3cd866640d992272a4fb9a94422998cf7d84bf265d566ceb2b5924532 |
| olson-uniform-codex-review-v1.stderr.txt | 91525719f193c94a708c405182d3fb55bbffa8581f98a9bfe6d247f865425bad |
| olson-uniform-claude-review-v1.prompt.txt | 37b634a95d8eaa1b8e0e1a6718a00d74ad3866f83916eb1a19913802cf43dd92 |
| olson-uniform-claude-review-v1.note.md | 5fd44d740bd752f988057542d3eb269e005da2c299c292e5186c7f36258d5409 |
| olson-uniform-claude-review-v1.receipt.json | e0443d6876a69432a9755dabd91a34dc82a9802c16186de62c74e2985b9dc439 |
| olson-uniform-claude-review-v1.stdout.json | b8d0f729be36f568481a88455407f680ea41e8c16dec39ce767f764f413467f3 |
| olson-uniform-claude-review-v1.stderr.txt (empty) | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| olson-uniform-desk-check-v1/desk_check.py | 96184e605291af1b93e69acbe1f63baa8a832c7ca66d70e9bd00fbd77d7e204a |
| olson-uniform-desk-check-v1/desk-check-result.json | 229402359cda8d536917128b189d36ed12b2e24df7a4481491423df2f4e34924 |
Paths are relative to /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review. The machine receipt is olson-uniform-review-result-v1.json.

## Deviations and own errors (preserved, not hidden)
- The manifest's desk_observations[2] says the C0WB r0-to-r1 Sec. 0-2 change is at "r1 LF 34-36". The correct range is r1 LF 34-35, and both prompts state 34-35. The manifest was created exclusively and was not edited.
- The desk ran its own arithmetic script for about 55 s on one CPU, writing only into olson-uniform-desk-check-v1/. It was pre-tested in the desk's in-memory kernel. This is a desk aid, not a review premise.
- Codex hashed DF/C0W excerpts that it piped through sed (read-only). This is within the read-and-verify-sha allowance, but beyond the three target hashes.
- Claude's packet omitted SEEDG-r2 Secs. 5-7, C-r1 Sec. 3, Cplus-r2 Secs. 3-4, C0WB r0 Secs. 3-4 and r1 beyond its header, LB-r1, and the controls. These were omitted for size (prompt 129,488 bytes). Codex had the full files.
- The C0WB-r1 and SEEDGstar-r1 statuses changed after the snapshot and prompts were frozen. The reviewers saw "unreviewed"; the update above comes from the repair desk's IRC message and file, not from these reviews.
- The snapshot root and its subdirectories were created with mkdir(exist_ok=False), and all files with mode x/xb. No pre-existing file was touched.
- For read-only inspection the desk used shell ls/grep/head/diff/cat/wc/shasum and bash cd in places, rather than only the specialised tools. No file mutation resulted.
