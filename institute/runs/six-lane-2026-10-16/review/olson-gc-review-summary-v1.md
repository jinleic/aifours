# proof-GC.md review desk: Lemma GEN, Lemma GC and Theorem NMH-iii

Desk OlsonGCReviewDesk. Recorded after 2026-10-18 00:49 PDT (host clock). This file reports two independent static reviews and one desk smoke test. **It is not a parent theorem or gate verdict.**

## 1. Target and pinned inputs

**Target.** `mathematics/evidence/six-lane-20261016/olson/inverse-run-count/mixdef-high/c6/proof-GC.md`, SHA-256 `f968a396facf396854662cbcb566c614e7e1e1dac415ca23ae70309878998425`. This hash equals the task pin and `c6/out/freeze.txt` LF330.

**Snapshot.** `olson-gc-review-inputs-v1/` holds 30 files. Its `manifest.json` has SHA-256 `aeabac14f819ed437e54e095bd6ea889ac9f3ab0550e67dec446803675a0a22f`.

**Direct imports and their status:**

| Import | SHA-256 | Status |
|---|---|---|
| `c6/proof-SEEDG-r2.md` (TS, Definition/QS, actual-empty alternative, NW, GS (a)/(b), SL, SCW-G, SEED-G) | `353b0e95…30b7` | parent-accepted |
| `c6/proof-A0-r1.md` (A0, C0-all, Corollary (a)/(b)) | `fba51b12…81a0` | parent-accepted |
| `c6/proof-C0WB-r2.md` (DF, C0W) | `7900f468…36f1` | parent-accepted |
| `c3/proof-C-r1.md` (Sec. 0 setting, Kill lemma, Sec. 2 identities) | `b5eb9fa7…b65b` | Codex ACCEPT |
| `c6/c5-fixes/proof-Cplus-r2.md` ((B1+), (B2+), C4) | `00e850cf…8bd3` | r1 reviewed; C4 delta parent-verified |
| `../../inverse-parity/proof-PAR-K0.md` (Lemma H with its 07:39 correction; the BC Claim) | `4b107fff…9a38` | Codex ACCEPT |

The DF and C0W text is byte-identical across C0WB r0, r1 and r2; the desk checked this.

**Also in the snapshot:**
- Definition files: `README.md`, `c3/README.md`, `proof-MH.md`.
- The producer's control script `gc_controls.py` and its receipt. These are aids only.
- The c6 producer log.
- The two parent verdicts: `olson-c6-uniform-parent-verdict.md` (`e5ac31d9…61ce`) and `olson-par-mixlow-parent-verdict.md` (`c0ee2c46…42a1`).
- 13 earlier review notes.

**Withheld from reviewers.** `olson-gc-parent-math-spot-v1.md` was left out of the snapshot, the manifest and both prompts. The desk read it only after both notes were final, and it agrees with them.

## 2. Reviews (static; reviewer identities from the receipts)

| Reviewer | Identity per receipt | Wall time | Disposition | FATAL/MAJOR/MINOR |
|---|---|---|---|---|
| `olson-gc-review-codex-v1` | gpt-6.1-sol, openai, read-only sandbox, effort max | 531 s | **ACCEPT-WITH-FIXES** | 0/0/2 |
| `olson-gc-review-claude-v1` | claude-opus-5-5 (firstParty), no tools, effort max | 1008 s | **ACCEPT-WITH-FIXES** | 0/0/8 |

Codex ran 17 commands, all `cat -n` or `shasum -a 256` on paths inside the snapshot. One `cat` named a file that does not exist in the snapshot. Codex ran no program and opened nothing outside the snapshot. Claude had no tools. No retry was needed.

## 3. Consolidated findings

All findings are MINOR wording, scope or path issues. None changes a proof step.

1. **LF109–110: the ZSI-B parenthetical overreaches** (Codex 1, Claude m5).
   - Problem: "every ZSI-B word" is not contained in R ≤ 2p−3.
   - Counterexample (Codex): p=5, k=6, κ=2, B=1, d=(3,−1,1,1,1,1), reflection lengths (5,1,1,1,1,1). This word satisfies (4.1) but has R=8>7. The desk re-checked it by hand.
   - Fix: "every ZSI-B word with R ≤ 2p−3".
   - LF118 says "its ZSI-B part". Claude reads this as already restricted by item (iii); Codex suggests adding the same qualifier for clarity.
2. **LF118: path.** Under the stated convention, `../proof-MH.md` resolves to a nonexistent file; it should be `proof-MH.md` (both reviewers; desk confirmed).
3. **LF16–17: verdict reference** (both reviewers).
   - The parent-verdict path is relative to the repository root, not to `mixdef-high/`.
   - "not re-read by this worker" is stale: the c6 README, LF652–655, records that it was read after freezing (Claude).
   - Fix: mark the path as root-relative, or give its SHA `e5ac31d9…` and rows LF11, 14, 17, 21.
4. **LF105, Remark (3): the walk bound.**
   - The stated bound (2m−1)(L−2) is true but quadratic in k.
   - Exact count: the walk has exactly L−2 = k−3 unit moves. b* = (2,…,2m−1,L−1) is componentwise above b = (1,…,2m−1), so the lowering pass is empty.
   - Codex calls the bound valid but loose; Claude calls the "linear" justification inconsistent.
   - Fix: state the exact count.
5. **LF103–104, Remark (1): incomplete list.** The remark should also list the NMH inputs it uses (Claude m2): Lemma H with β=0, (1.1), |d_s| ≤ e_s+1, e_s ≥ 0, E = Σ e_s.
6. **LF113–115: "empty seed intersection".**
   - Problem: an empty interval is not a seed under SEEDG-r2 LF74.
   - Fix: say that the canonical bound [λ({t}),U({t})] and the GS (a) bound [s_lo,s_hi] from the actual configuration are inconsistent.
   - This is the accepted actual-empty alternative (parent verdict LF21), not an empty (QS) window. Claude m8 counts it as a finding; Codex states the same point in Q4 without counting it.
7. **LF119–121: "It supersedes" is unconditional** (Claude m6). Fix: "If accepted, it subsumes, as a conclusion only, …".
8. **LF121–123: the [I] assembly conditions** (Claude m7). The sentence should also make acceptance of the README Sec. 1 reductions a condition: OR, M0, ALT, B0/C0-B'/A1 and the trivial cut.

**Not a target issue.** In the c6 README, LF622 and LF638 read "[k]-2026-10-18T…" where "[k]-{t}" was intended (Claude).

## 4. Audit items: what the two reviewers and the desk found

1. **GEN is an exact iff.** All three re-derived it, including the parity elimination for both parities, the centres and lengths, a1±a2 and complement symmetry.
   - Extra (Claude, Codex, desk): the left side |4m−(k+2)|+|2y−D| is always even, since D ≡ Δ0 ≡ k (mod 2).
   - So the bound is parity-tight: the right sides E+2Δ0 and E+2Δ0+1 are equivalent.
2. **GC holds for every k ≥ 7.**
   - m=⌊(k+4)/4⌋ gives c=2,1,0,1 for k≡0,1,2,3 (mod 4), with 2 ≤ m and 2m ≤ L−1.
   - Neighbours: r₁ and r_L are non-adjacent. The cyclic blocks of X and Y are their path blocks.
   - The second colouring χ* has blocks (2,1^{2m−3},L−2m,1).
   - Sum identity: (3.2) Σ = D−d+d_{t+1}−d_{t−1}.
   - Walk: strictly increasing, one recoloured position per move, endpoint colours preserved.
   - Q always contains t+1. TS and GS need no isolation of t.
3. **The window and crossing are sound.**
   - D±W′ is always even, so hi−lo+1 = W′−|d|+1.
   - (S), (M) and (3.3) hold for pure aligned, pure anti and pair targets.
   - The crossing argument cannot skip the window.
   - Both reviewers worked a nontrivial-crossing example: p=7, k=11, κ=4, B=3.
   - The tight E ≥ 4 case is p=11, k=12, d_t=7: it attains equality in (S) and (M) (Claude).
4. **The invocation is valid.**
   - GS (b)'s definition of generic matches the target's, and NW is exactly the hypothesis of GS (a).
   - In the empty case the actual configuration excludes the word directly. Codex example: p=7, k=9, d=(−2,2,1⁷), t=2, Q={3,5,7}. Then [s_lo,s_hi]=[1,1] while the canonical range is [2,3]; the desk re-checked this by hand.
   - Otherwise every run has a quality seed, which is Corollary case (b).
   - C0-all case (ii) is exactly C0W's accepted scope (B ≥ g+1, 3g+1 ≤ p).
   - No count condition and no defect bound is used.
   - Every NMH hypothesis holds: k ≥ p+1, β=0, pure or (1,1) runs, 1 ≤ B ≤ κ−1, B ≤ A ≤ 2p−1, Δ0 ≥ 3, and k=2κ+Δ0 ≥ 7.
5. **Scope.**
   - The theorem covers normalized NMH words with R ≤ 2p−3, for every prime p ≥ 5. These are the item (iii) words plus the ZSI-B words with R ≤ 2p−3.
   - It is not NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR, INV, INV* or ordered Olson.
   - No finite control, census or E2 315-row table is a premise.
   - The overreach is wording only (items 1, 7 and 8 above).

## 5. Desk smoke

**Run.** `olson-gc-review-smoke-v1/gc_smoke.py` (SHA `9158adb1…87ff`) is stdlib-only, written from the definitions, and imports no producer code.
- Output: `run-v1/smoke.jsonl` (SHA `a04d884a…5d990`); stderr empty.
- Limits: one process, RLIMIT_CPU soft 120 s, RLIMIT_FSIZE 8 MiB. User CPU 7.44 s; peak RSS 17,743,872 B.
- First attempt, 00:38: it failed the disk gate (free 12,199,751,680 < 12.203e9 B) and did not start. This was reported once to Main.
- Main cleared the gate at 00:44. The run started after a fresh passing gate (free 17,711,214,592 B).

**Sample.** Deterministic seed 20261018.

| p | Words | Classes covered |
|---|---|---|
| 5 | 7 | all 7 anti positions |
| 7 | 144 | all 9 classes |
| 11 | 210 | all 70 classes |
| 13 | 240 | 120 of 135 classes |
| 17 | 110 | E ≥ 4 classes |
| 19 | 70 | E ≥ 4 classes |
| 23 | 45 | E ≥ 4 classes |

Word styles: spread, concentrated, longest runs adjacent, anti/pair block.

**A. GEN against the floor-term definition.**
- Coverage: every proper pattern of the 246 words with k ≤ 14 (1,249,684 patterns), with λ(Q^c) taken from the explicit complement.
- Result: 0 mismatches, 0 complement-symmetry failures.
- Brute-force existence check: all 1,457 targets with k ≤ 11 have a generic configuration (minimum 40 each).
- Mutations:

| Mutation | Mismatches | Reading |
|---|---|---|
| bound −1 | 81,066 | detected |
| k+1 in place of k+2 | 12,706 | detected |
| bound +1 | 0 | expected, by the parity fact in §4 item 1 |

**B. The walk of Lemma GC, run literally.**
- Coverage: 14,630 targets, of which 7,869 have E ≥ 4, 804 are pair targets and 1,568 are anti targets.
- Result: 0 failures. All of these checks passed: (3.2), (S), (M), (3.3), the window, the crossing, slow-λ genericity of Q, Q+t and Y, the GS (b) bounds, NW, and the seed being a quality seed.
- Walk length: k−3 on every target. The lowering pass made 0 moves and the b* formula had 0 mismatches.
- Longest walk: 36 moves. The window was entered after at most 13 moves. Q contained t+1 on every target.
- Actual-empty: 447 GS (a) intervals were actually empty. In 360 of them the (QS) window still met the canonical range. So an empty actual interval and an empty (QS) window are different events.
- Mutations:

| Mutation | Effect |
|---|---|
| window widened by one | 1,682 non-generic picks |
| Y condition dropped | 247 picks with Q+t non-generic |
| Σ without the end terms | 5,833 targets wrong |

**Probe at Δ0 = 2** (R = 2p−2, outside the theorem's scope; 504 words, 8,904 targets).
- The written chain step E+3 ≤ W′ in (M) fails in 5,184 targets. Analytically it fails exactly when c = 2, i.e. k ≡ 0 (mod 4).
- Even so, (3.3), the crossing, genericity and GS (b)/NW held in every sampled probe target.
- Every probe target with k ≤ 11 had a generic configuration.
- So Δ0 ≥ 3 is used only by that written step. The probe found no failure of the conclusion; it claims nothing about Δ0 = 2.

**G. The theorem's conclusion checked directly in D₂ₚ (no lemma used).**
- The subsequence DP agrees with brute force on 250 random words (p=5).
- Controls for p=5, 7, 11, 13 behaved as expected: the avoider r^{2p−1}s^{2p−1} is reported as having no identity 2p-subword, and r^{2p}s^{2p−2} is reported as having one.
- **p=5, exhaustive** up to cyclic rotation and conjugation: 28 reflection-length patterns × 5⁶ reflection values = 437,500 words. All have an identity 10-subword; 0 avoiders.
- p=7, 11, 13: 594 random letterings, 155 of them with E ≥ 4. All have identity 2p-subwords.

**Scope of these checks.** They are [F] aids only. They do not repeat the producer's 1.39M-target census. The p=5 group-level check covers p=5 only.

## 6. Limits

- These are static reviews plus a desk smoke, not acceptance.
- The chain relies on parent-accepted imports at their exact scopes.
- MIX_DEF_HIGH(p) would additionally need c2/proof-C2.md and the README reductions to be accepted.
- RUNS(p) also needs Corollary RL, which is unreviewed; ordered Olson also needs INV*(p).
- There is no Lean formalization, no human peer review and no novelty search.
