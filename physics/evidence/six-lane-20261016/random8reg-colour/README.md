# Six-lane phys-2 (third target): chromatic number of the random 8-regular graph

## 0. Frozen protocol

Written 2026-10-17 at about 07:35 PDT (host clock), before the proof and verifier in this lane.

### 0.1 Authority and lane separation
- **Contract:** `institute/runs/six-lane-2026-10-16/screening/phys-2-random8reg-colour-contract-r2.json`, SHA-256
  dc451d82e266db8e6b9f166bdc1e7a647570dfa47f12a1ec2c2b864d1d6d46aa. It supersedes only the lane path of the v1
  contract (9e123a12…0e49); the target and acceptance criteria are unchanged.
- **Target:** prove that the uniformly random 8-regular graph G_{n,8} has χ = 4 a.a.s., or isolate the exact
  failing dependency of the proposed route.
- **Where files go:** all χ8 files live in this lane.
- **Read-only prior input:** `physics/evidence/six-lane-20261016/random7reg-colour/`. That lane holds:
  - χ7 r2 (accepted);
  - `review/D8_PILOT.md` (exploratory);
  - the D–SC, NPG, W99 and AM04 sources.
- **Superseded draft, left unchanged:** `random7reg-colour/code/verify_chi8.py`, SHA-256
  9a400a5502acf312519efc5afbd9a039a14422bb0b9e83134a5bf8aa6ecd0cdc, mtime 07:34:11. It was written there before the
  r2 contract arrived and is not used.

### 0.2 Route (fixed before writing)
1. **Upper bound.** Use KPW's balanced-colouring second moment and small subgraph conditioning at (k, d) = (4, 8).
   Only the S_2 estimate changes:
   - Lemma A replaces KPW's Lemma 5 → (3.7) → (3.9) + (3.15). It combines the exact count (3.4) with pointwise weak
     duality, using multipliers μ_u = c + (7/8) ln m_u.
   - Theorem C proves global quadratic decay of U(M) = −10 ln 2 + 4 ln E(M), via a row reduction and a row
     inequality. The row inequality gets two independent proofs: hypercontractivity on K_4 (Diaconis–Saloff-Coste
     1996), and an elementary two-value lemma plus arb.
2. **Residues.** n mod 4 is handled by KPW Theorem 10 with r ∈ {1, 2, 3} and ℓ = 4r distinguished edges whose
   endpoints induce a perfect matching. Conditional uniformity must be exact.
3. **Lower bound.** Molloy–Reed.

### 0.3 Representation
- k = 4 colours. Cells u = (p, q) carry the entries of a doubly stochastic overlap matrix M.
- Allowed pairs form K_4 × K_4 (72 unordered pairs). J = (1/4)J_4.
- The only symmetry used is coordinate-permutation invariance of the row function on Δ_4, which gives the
  two-value families.

### 0.4 Acceptance
Contract items (1)–(7), verbatim in the contract:
1. imports with exact hypotheses;
2. Lemma A at finite n;
3. Theorem C with both proofs, the primary-source normalisation, and exact or arb constants;
4. the audit row: Lemma 5, (3.7) and (3.9) enter only S_2 and Theorem 10's restriction, and S_1 needs only
   (H1) = 2;
5. small subgraph conditioning at (4, 8);
6. residues r = 1, 2, 3, with ℓ = 4r and exact conditional uniformity;
7. Molloy–Reed: 16/27 < 1.

### 0.5 Controls
- Reproduce the pilot's arb constants.
- Show the route's condition fails at d = 9 (ln 8 > 2), with no d = 9 claim.
- Mutation controls.
- An exact-count check of Lemma A's exponent at M = I.
- Float sanity of U − Ψ_8, which is not evidence.

### 0.6 Stop rules
- A rigorous counterexample to Lemma A or Theorem C, or a KPW dependency that genuinely needs Lemma 5 outside S_2,
  means stop and report a refutation of the route. It is not a refutation of the target.
- If any required verifier item is not certain, do not freeze.
- The proof is frozen once (r1). Corrections go to r2.

### 0.7 Evidence rules
- Exact rationals, big integers, sympy and arb only. Floats are not evidence.
- No novelty or priority claim; record priority misses with their dates.

### 0.8 Resources
- ≤ 4 CPU processes, ≤ 8 GiB, checkpoints ≤ 30 min, chunks ≤ 3 h.
- No /tmp or other out-of-repo writes.
- Cooperative stopping only: never SIGKILL or `subprocess.run(timeout=...)`.

## 1. Status

**CANDIDATE PROOF, frozen r3 (r3 itself not re-reviewed).** File: `review/PROOF_CHI8.r3.md`, SHA-256
e7c506d0bcd75aad69ce004c4633ffa15e5a8ee64d90f53bf9c6867b95187e2d, mtime 2026-10-17T09:20:07-0700, 860 lines. It is
never to be edited.
- r3 is r2 plus exactly the three editorial fixes from the Codex delta review of r2 (r3 §11, items 14–16), plus the
  title, supersession and status lines.
- Unified diff: `evidence/r2-to-r3.diff` (SHA-256 f6d99375585428cd1646fe39ffd08764ba79bed67160c411c5f50307041fe054).

Superseded, kept unchanged:
- r2: `review/PROOF_CHI8.r2.md`, SHA-256 055d295258dfe294b701f6e461684f82b7f8a9435a68d49ab52634d247644cb1,
  mtime 09:01:28.
- r1: `review/PROOF_CHI8.r1.md`, SHA-256 7ed7f8c865468326b307b2ce8fd93048cc5ceed807eb98503e7b1c32248a4c8a,
  mtime 07:42:34.

Reviews, parent-held:
- Of r1:
  - Codex CLI hostile review: ACCEPT, no fix requested; one minor remark (KPW l.1251 at k = 3).
  - Claude CLI complete review v2: ACCEPT-WITH-FIXES, seven editorial minors, no fatal, major or gap finding (v1
    timed out with no verdict).
  - Parent priority audit: GSV/GSVY Φ precursors; AM04 §6 counterpoint.
  - Parent rational arithmetic receipt.
  r2 applies all of these (§11 items 1–13).
- Of r2: Codex delta review, ACCEPT-WITH-FIXES, three minor editorial findings and no fatal or major finding.
  The parent replayed `verify_chi8_r2.py` byte-identically. r3 applies the three fixes (§11 items 14–16).

Verifiers, unchanged for r3:
- `code/verify_chi8.py` → `evidence/verify_chi8.json` (unchanged from r1).
- `code/verify_chi8_r2.py` → `evidence/verify_chi8_r2.json`: the run at 09:00:44 returned all_required_true = true.

The working drafts were retired, unchanged, to `archive/PROOF_CHI8.r2.DRAFT-working-copy.md` and
`archive/PROOF_CHI8.r3.DRAFT-working-copy.md`. The empty `review/drafts/` directory is left in place (no deletion).

Claim: χ(G_{n,8}) = 4 a.a.s.
- Upper bound: KPW's second moment and small subgraph conditioning at (4, 8). KPW's S_2 estimate is replaced by
  Lemma A (exact count plus pointwise weak duality, with an explicit polynomial factor and empty cells handled) and
  Theorem C. Theorem C states U(M) ≤ U(J) − C_8‖M − J‖², with C_8 = (49√2/32)(a² − 1/9) = 0.01473…. It rests on
  the analytic hypercontractivity proof of the row inequality; an elementary interval check is supplementary.
- Audit rows A14 and A15: Lemma 5, (3.7) and (3.9) enter only S_2 and Theorem 10's restriction; S_1 needs only
  (H1) = 2.
- Residues r = 1, 2, 3, with ℓ = 4r and exact multinomial(8r; 8, …, 8) conditional uniformity.
- Lower bound: Molloy–Reed, 16/27 < 1.

Verifier: `code/verify_chi8.py` → `evidence/verify_chi8.json`. The run of 07:37:16–07:37:24 PDT returned
all_required_true = true.

Priority: dated misses are in the LOG and the proof's §9. No novelty claim.

Exploratory, not part of the frozen target: `explore/GENERAL_K_LEAD.md`, with `explore/check_general_k.py` →
`explore/check_general_k.json`. It is an [INFERENCE] general-k lead: the route reaches d ≤ 1 + e^{4−8/k}, which
includes (k, d) = (5, 12) with C_12 = 5.87·10⁻⁴ > 0. Nothing is claimed until the χ8 proof is accepted.
