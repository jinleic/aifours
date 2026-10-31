# Slice B review — f283-spr-six-frequency-consolidated (K1/K2 finite-claim independent replay)

Reviewer agent: `CheckF283SprKernels` (slice B). Wave dir: `review-waves/f283-spr-six-frequency-consolidated/`.
Manifest `manifest-v1.json` SHA-256 `6af2c6c24c3f9493ac3fec94256599e38f33a5d09c810411a66e061f361c0131` (5958 B, 94 LF); packet `literal-packet-v1.md` SHA-256 `0132ac8c0eb77a4bc6a161020b754fe5a098a800dcc51c93ade482e5dacd95b9` (32992 B, 255 LF) — both verified before reading. Scope: independent, definition-first exact replay of the two pinned kernel claims K1 (S1|38, S2) and K2 (S1|71, S3) from S1's written definitions only. This is **not** a review of the manuscript's continuous arguments (§§1–2, 5–9, Lemma proofs — slice A scope) and **not** a verdict on the Theorem (S1|5) or the original target.

## 1. Read and execution receipts (complete)

Reads (unelided, raw):
- `manifest-v1.json` 94/94 LF, raw, in full — inputs, metadata-only pins, slice contract.
- `literal-packet-v1.md` 255/255 LF, raw, in full — S1 (S1|1–101), S2 (S2|1–16), S3 (S3|1–129).
- Author kernels `frontier-…-five-node-phase-independent-kernel-v1.py` (SHA `ac13abaa…`) and `frontier-…-phase-c-gap-positive-polynomials-kernel-v1.py` (SHA `e01dc6d4…`): **metadata only, never opened/imported/executed** (manifest pins; no read of file contents occurred).
- No other file was read; slice A output and any prior review were not read. No network, Git, deletion, or unrelated build/lint/test runs.

Development phase (disclosed): before freezing, the polynomial engine and K1 predicate logic were benchmarked/validated in scratch cells (same mathematics, not the frozen artifacts). Hand-verification at all-gaps-equal-1 reproduced all eight S3 coefficient sums (e.g. 369600 = 180·1225·(56/15), 48384000 = 180·1225·(1536/7), 8640 = 180·35·(48/35)) before any checker run.

Frozen artifacts and their one bounded runs (native clocks, PDT; single core; standard library only; exact integer/`Fraction` arithmetic):

| checker | SHA-256 at freeze/run | run window | exit | wall |
|---|---|---|---|---|
| `slice-b-k1-checker.py` | `cb33a69230044bf876bd6c633a83974b87dcdf0c16e70aa5ff5aab990a8b7f8f` | 2026-10-29T21:11:17→21:11:38 | 0 | 0.22 s |
| `slice-b-k2-checker.py` | `6ec1984a2bc9b4a742206d2b2eeb07dbb043bda3120fdabc374d47b4ce27e681` | same window | **1** (diagnosed: manuscript sign typo, §4 below; all mathematical checks passed) | 21.0 s |
| `slice-b-erratum-check.py` | run 1 `3ecb603b…` (crash: `Fraction` not JSON-serializable, math complete), run 2 `8b7e6044…` (crash: lost `ok` line), final `fae5b10052fdee741a859f98f30d48f7d3530c557c1148f9f1bcaaa97d6a615d` | 21:14:01 / 21:14:18 / 21:14:27 | 0 | <1 s |

The K2 checker's exit 1 is its designed behavior when an internal exact assertion fails; the failing assertion is the manuscript's own parenthetical identity (Finding 1). No checker was rerun after its recorded bounded run; the erratum verifier is a separately scoped new checker. Admission estimate: well under 2 GiB (largest object 89,883 monomials; observed peak RSS 127,631,360 B ≈ 121.8 MiB — macOS `ru_maxrss` is bytes; the receipt field name `peak_rss_kb_observed` is mislabeled). Per-process and total limits (≤120 s / ≤600 s) respected with large margin.

## 2. K1 — finite phase classification (S1|22, S1|33–38; S2)

Definition-first predicates (derived from S1 text, not from author code):
- (α) S1|34/Lemma 4: both parity sign words must fail the four-block pattern `+*−*+*−*`, i.e. contain the oriented subsequence (−,+,−,+) (applied to both parities per S1|38 "each parity sign word"). Internal control C0: over **all** 2^L sign words, L=0..7, `contains(−,+,−,+) ⇔ not fits(+*−*+*−*)` — passed, so the two readings of Lemma 4 coincide.
- (β) S1|22: for every pair i<j: (i) q_j ≥ q_i−1; (ii) if E- and O-signs both differ, q_j ≥ q_i+2. Class→(E,O) sign table taken verbatim from S1|22.
- Full universes enumerated: 7^3=343, 7^4=2401, 7^5=16807 words; complete retained **sets** compared, not counts.

Results (slice-b-k1-receipt.json):
- (α)-pass: m=3: **0**; m=4: **16** — exactly the set {2,6}×{0,4}×{2,6}×{0,4} predicted by the written m≥5 argument (S1|36, both parity words forced to exactly (−,+,−,+)); m=5: **676** (full list in receipt).
- Retained after (α)∧(β): m=4: **∅**; m=5: **exactly {(2,1,3,2,4), (2,1,3,5,4), (2,4,3,5,4)}** = words A, B, C.
- S2 comparison: all four count fields reproduced (`ordered_m4=0`, `ordered_m5=3`, `phase_order_removed_m4=16`, `phase_order_removed_m5=676`) and the three `cases` class triples match as sets. S2's `backward_band_intervals` labels were **not compared**: their encoding convention is not derivable from S1 alone.
- Mutations (must fail for intended reason): M1 orientation flip (−,+,−,+)→(+,−,+,−): 24 retained, not a superset — discriminating. M3 drop (β)(i): 11 retained ⊋ 3 — discriminating. M5 (α) on E-word only: 153 retained ⊋ 3 — discriminating. M2 drop (β)(ii), M4 advance +2→+1, M6 slack −1→−2: each retains the same 3 words — **non-discriminating** (honest limitation: on this universe (β)(ii) and the exact slack are implied once (α),(β)(i) hold).

**Verdict K1: SUPPORTED** (finite claim, exact scope: enumeration under the written predicates over the full 7^4, 7^5 universes; reproduces S1|38's "exactly A, B, C; 676 pass (α) alone; none with m=4 [retained]" and all S2 counts/sets). This verifies the finite classification only; the continuous input (Hermite–Biehler phase monotonicity producing (i)/(ii), Lemma 3 moment signs) is written mathematics in slice A scope.

## 3. K2 — eight cleared-denominator polynomials (S1|42–44, S1|63, S1|71; S3)

Independent derivation (documented in the checker header, proved by exact zero-polynomial checks): the §4 ray weights w_i^{(k)}=e_{3−k}(û_i)/(u_i O_i(u_i) H′(u_i)) give ray F-pairings Σ_i e_m(û_i)·E(u_i)F(u_i)/(u_i O_i(u_i)H′(u_i)); substituting F=−t(b−t)(e−t), E=(x−t)(c−t)(d−t), unit envelopes O₊⁰=(b−t)(c−t)(f−t) (nodes 1,2), O₋⁰=(a−t)(d−t)(e−t) (nodes 3,4), a=1, each term reduces exactly (cancellation verified symbolically: `E·F·Gden − t·O⁰·Gnum = 0` in ℤ[B,U,V,X,Y,Z,P,W,R,t], both σ, both x) to e_m(û_i)·g_{σ_i}(u_i)/H′(u_i) with precisely the manuscript's displayed g's (S1|71). Denominator clearing rests on the factor identity Vdm = (−1)^{4−i}H′(u_i)·Vdm(û_i) (verified as an exact zero-polynomial test for each i) and D_x absorbing (f−u₁)(f−u₂) resp. (u₃−1)(u₄−1). Hence N_{x,m} := Vdm·D_x·J_{3−m} (the primary, unambiguous definition in S1|71) is a polynomial, constructed term-by-term and validated pointwise.

Results (slice-b-k2-receipt.json; full expansions in `slice-b-k2-poly-xX-mM.txt`, 26 KB–1.9 MB each):

| case | monomials | coeff sum | min | max | all coeff > 0 | N=Vdm·D_x·J at 4 rational pts | J>0 at pts | S3 stats | S3 digest |
|---|---|---|---|---|---|---|---|---|---|
| x=0,m=0 | 11357 | 369600 | 1 | 837 | yes | yes | yes | match | match |
| x=0,m=1 | 27170 | 6384000 | 1 | 7983 | yes | yes | yes | match | match |
| x=0,m=2 | 53462 | 32709600 | 1 | 28620 | yes | yes | yes | match | match |
| x=0,m=3 | 89883 | 48384000 | 1 | 34968 | yes | yes | yes | match | match |
| x=1,m=0 | 1292 | 8640 | 1 | 78 | yes | yes | yes | match | match* |
| x=1,m=1 | 4969 | 150720 | 1 | 534 | yes | yes | yes | match | match* |
| x=1,m=2 | 12719 | 780960 | 1 | 1269 | yes | yes | yes | match | match |
| x=1,m=3 | 24167 | 1176480 | 1 | 1320 | yes | yes | yes | match | match |

Digest convention: S3 specifies only variable order (S3|114–124). My pre-declared canonical convention (lines `e_B,…,e_R:c`, exponent-tuple-lex ascending, LF-terminated, SHA-256) **reproduces the author's digest for 8/8 polynomials** — the two asterisked cases flagged False in the receipt only because I typo-copied two S3 constants into the frozen checker; byte-diff against the packet shows my independently computed digests equal S3's exactly (evidence: `slice-b-s3-digest-reconciliation.json`; e.g. packet `…1be43d1f73cdaa21` vs my typo `…1be43f1f73cdaa21`). All eight coefficient sums were additionally hand-verified at all-gaps=1 before any run.

Positivity ⇒ J^{unit}_{3−m}>0 for all positive gaps (all coefficients strictly positive, monomial count > 0, Vdm·D_x > 0) — a parametric statement, not a sample. Auxiliary finite checks: e_m(û_i) nonincreasing in i at 20 deterministic rational points (S1|44 note, corroborated); S₊ closed form `S₊=[q₂(u₂−x)h(u₂)−q₁(u₁−x)h(u₁)]/(u₂−u₁)` equals the direct partial ray sum and is >0 at 4 points for all eight (x,m) — see Finding 1 for the manuscript's adjacent identity.

Mutations (each fails for its intended reason — the definitional identity N=Vdm·D_x·J breaks): flip of the H′(u₁) orientation sign at (0,0) and (1,3); e_m→e_{m±1} at (0,0); node-4 term omitted at (0,3); denominator-clearing factors (u₃−1),(u₄−1) omitted at (0,3) (fails against both D₀ and D₁ scalings). Note honestly: the sign and term mutants still happen to have all-positive coefficients — **coefficient positivity alone would not catch them**; the identity to the definition is the discriminating check, which all mutants fail.

**Verdict K2: SUPPORTED** (finite claim, exact scope: the eight integer polynomials N_{x,m}, x∈{0,1}, m=0..3, defined by S1|71 from the Lagrange ray formula, have every nonzero coefficient a strictly positive integer; statistics and canonical digests reproduce S3 exactly; denominator clearing and sign orientation proved by exact polynomial identities, not sampling). The surrounding scale decomposition S = J^{unit}/λ₋ + (1/λ₊−1/λ₋)S₊ (S1|71) is algebraically consistent and S₊>0 at all tested points, but its general monotonicity argument is written mathematics (slice A), with one erratum below.

## 4. Findings

**FATAL: none. MAJOR: none.**

1. **MINOR (erratum, S1|71):** the parenthetical identity `q₂(u₂−x)−q₁(u₁−x)=(u₂−u₁)(e_m(u₃,u₄)−x·e_{m−1}(u₃,u₄))` has a sign error. Exact polynomial verification: the true identity is with `+x·e_{m−1}`; the manuscript's version is off by exactly `2x(u₂−u₁)e_{m−1}(u₃,u₄)` (nonzero iff x=1, m≥1 — precisely the cases my frozen checker flagged). The conclusion (difference > 0) remains valid and becomes trivial under the corrected identity (e_m ≥ 0, e_{m−1} ≥ 0, u₂>u₁). Verified by `slice-b-erratum-check.py` (E1–E3, exit 0).
2. **MINOR (justification flaw, S1|71):** "e_m/e_{m−1} is a mean of u₃,u₄" is false for m=2: e₂/e₁ = u₃u₄/(u₃+u₄) < min(u₃,u₄); exact counterexample u₃=u₄=3/2 gives 3/4 < 1 = x with both nodes > x. Under the corrected identity (Finding 1) this mean argument is unnecessary; S₊>0 itself was verified at all tested points.
3. **MINOR (ambiguity, S1|38):** "676 words pass (α) alone; none with m=4" — 16 words pass (α) at m=4 (=2⁴, structure verified); "none" means none retained after (β). S2|8's `phase_order_removed_m4_sequences: 16` disambiguates; the sentence alone does not.
4. **MINOR (presentation, S1|71):** the clearing description "Σᵢ(±)e_m(ûᵢ)·nᵢ·Vdm·D_x … signs (+,+,−,−)" admits a double-negative reading (nᵢ already carries the node-3,4 minus); the primary definition `N_{x,m}:=Vdm·D_x·J_{3−m}` is unambiguous and my reconstruction from it reproduces the author's digests 8/8.
5. **MINOR (not compared):** S2 `backward_band_intervals` labels ([1,"O1"],[3,"E2"]) etc. — encoding convention not derivable from S1; only the class triples were compared.
6. **MINOR (slice-B self-disclosure):** my frozen K2 checker embedded two typo'd S3 digest constants (x1_m0, x1_m1), producing two false mismatch flags in its receipt; corrected post-run by byte-diff (no scientific rerun; reconciliation artifact). Also `peak_rss_kb_observed` is bytes on macOS, not KB.

## 5. Scope and standing limits

- Same-harness, single-agent execution; **no human review, no independent-family model, no formal kernel (no Lean/proof assistant), no novelty or literature claim** (per manifest rules and S1|3/101).
- Finite verdicts only: K1/K2 finite claims verified exactly; the manuscript's continuous arguments (Hermite–Biehler inputs, moment cone completeness, envelope domination, §§5–9 case exclusions, reciprocity) were **not** audited here (slice A). Validity of the finite claims does **not** establish the Theorem (S1|5) or the original synthesis-or-obstruction target, which remain open as stated at S1|97.
- Intended-reason negatives recorded; non-discriminating mutations (K1 M2/M4/M6) disclosed as such.

## 6. Artifacts (this slice only)

`slice-b-k1-checker.py`, `slice-b-k2-checker.py`, `slice-b-erratum-check.py`, `slice-b-k1-receipt.json` (incl. full 676-word and 16-word lists), `slice-b-k2-receipt.json`, `slice-b-erratum-receipt.json`, `slice-b-s3-digest-reconciliation.json`, `slice-b-k2-poly-x{0,1}-m{0..3}.txt` (8 full coefficient expansions), and this `review-B-v1.md`. No inputs, manifests, ledgers, READMEs, or other slices' outputs were modified.

Post-run note: a `__pycache__/` directory (Python bytecode from my pre-freeze `py_compile` syntax check) remains in the wave directory; deletion was blocked by this harness's bash policy (`rm` pattern), so it is disclosed here rather than removed. It contains no data not derivable from the checkers above.
