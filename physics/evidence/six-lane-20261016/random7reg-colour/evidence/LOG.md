# Lane log (host clock, PDT)

Times are captured `date` outputs or file mtimes. No guessed times.

- 2026-10-17 06:04:34 lane assigned by parent IRC. Read the contract and the parent-pinned sources in place:
  KPW 0812.2937v1 §§1–4, and AN Annals §§3–5 (Theorem 7, (5), Theorem 9, Prop. 10, eqs. (9)–(12)). Also read the
  scout Colour7Screen report (agent://Colour7Screen), which is treated as untrusted.
- 06:04–06:14 priority kill-check (web search; dated misses):
  - Kemkes thesis: Semantic Scholar lists "Properties of random graphs" (2008, Waterloo). The full text was not
    opened (access hole).
  - KPW's own footnote says part of KPW appeared in that thesis, so it is presumably not stronger than KPW.
  - Shi–Wormald, Waterloo report 2004-24: fetched into sources/; it is image-only, one page. Its abstract, as
    returned by search, covers d = 4, 6 and "other d between…". KPW cite it for χ(G_{n,4}) = 3 and χ(G_{n,6}) = 4.
  - Achlioptas–Moore cond-mat/0407278v1, fetched into sources/:
    - its table gives χ(G_{n,d}) ∈ {4,5,6} for d = 7, 8, 9 (layout l.43–46);
    - §7 says "any improvement on the upper bound for E[Y²] given in [4] would immediately give an improved
      positive-probability k-colorability result for G_{n,d}" (l.532–534).
  - Erdős-problems page (UCSD): restates KPW only.
  - Searches for the (k−1)³log(k−1)/(k(k−2)) constant, for "random 7-regular 4-colourable", and for 2021–2026
    chromatic-number papers found no source determining χ for d = 7.
  - Access holes: the Kemkes thesis full text, the Shi–Wormald CPC body, and journal bodies beyond arXiv.
  - A miss is not novelty.
- 06:14:04 python-flint arb comparison semantics checked: comparisons are True only when certain.
- README §0 protocol written (README mtime) before any computation in this lane.
- 06:17:44 code/verify_rigorous.py run → evidence/verify_rigorous.json (mtime 06:17:48). all_required_true = true:
  - exact-rational and arb enclosures of every constant;
  - d = 8 control exact (13³² > 2⁵⁶·3³²·5⁵);
  - first-moment sup Φ_d < 0 on both KKT curves for d = 6, 7, 8 (3000 pieces each); d = 5 positive, as required;
  - mutation controls rejected.
  Wall time 3.7 s.
- 06:18:52 pinned-source SHA-256 values recomputed; they match the parent manifest. Also read ACG (1.1)–(1.7) and
  Table 1, and confirmed that KPW §2 (l.183–566) has no d-condition beyond d positive and k ≥ 3.
- 06:20:12 fetched W99 (Wormald, Models of random regular graphs, 1999; sha 987de47e…cb70) into sources/, to pin the
  exact statements of the small subgraph conditioning Theorem 4.1 (layout l.1561–1596) and of Theorem 2.6.
- 06:20–06:25:30 review/PROOF_CHI7.r1.md written. Proofreading corrected page numbers, restricted Theorem 2.2 to
  c ≥ 0, and softened one unverified bound into a float display. FROZEN at mtime 06:25:30, SHA-256
  8a79ba3c9858137fa698c5f962ac6fe4e1fba38f2b61ce919772893d74ea906c. Checkpoint 1.
- 06:26:05 lane SHA256SUMS written. Candidate-proof message sent to Main immediately after (r1 SHA 8a79ba3c…906c).
- 06:27:28 code/crosscheck.py → evidence/crosscheck.json (all_ok = true). These are independent second routes, not
  needed by r1:
  - X1 (arb): family-1 G ≥ 0 on [−1/3, 1], via G″ ≥ 0.7957 on ±1/20 neighbourhoods of the double zeros 0 and 2/3,
    plus 40000-piece subdivision elsewhere (smallest lower bound 0.0020);
  - X2: family 2 by convexity, H″ ≥ 1 − (3/4) ln 3 = 0.176 > 0;
  - X3: Lemma 5.1's count matches exhaustive enumeration of perfect matchings in 7 small cases;
  - X4 (sanity): the exact (1/n) ln E Z_3 at d = 7 is −0.391, −0.355, −0.338, −0.329, −0.325 for n = 20…320, tending
    to the balanced exponent −0.3205.
- 06:28 parent safety rule received (all lanes): cooperative stops only, never SIGKILL. Python
  subprocess.run(timeout=…) also sends SIGKILL, so it is not to be used. Timeouts count as UNKNOWN.
- 06:28:47 audit of this lane: no subprocess or kill calls in code/; every run (verify_rigorous 3.7 s, crosscheck
  7.4 s) finished normally; nothing was stopped. Any future long run will use native limits or
  Popen + wait(timeout) + terminate(), and will leave a survivor running and report it.

## Exploratory d = 8 screen (parent IRC; bound ≤ 90 min from 06:32:25; no target frozen, no claims)

- Parent: r1 pinned at institute/…/review/chi7-parent-inputs-v1/; the verifier replays byte-identically under the
  parent. Keep r1 frozen; one final r2 after all reviews.
- 06:32:25 start. Derived the exact exponent Ψ_d(M) of |T(M)|/|P_{n,d}| (KPW (3.4) without Lemma 5's relaxation)
  and its concave dual. Wrote code/explore_exact_exponent.py (single-threaded, finite loops, no subprocess).
- 06:34:14 sanity checks:
  - Ψ(J) matches the closed form;
  - the numerical Hessian coefficient at J is −0.1500, −0.1000 and −0.0500 for d = 7, 8, 9, matching the exact
    local coefficient −(k²−2k−d+2)/(2(k²−2k+2)) from KPW (3.11);
  - at M = (J+I)/2, Ψ_8 − Ψ_8(J) = −0.0290, whereas the relaxed value is +0.0074.
- 06:34:25–06:34:37 explore_exact_exponent.py → evidence/explore_exact_exponent.json:
  - Ψ ≤ relaxed at 900 random points;
  - at d = 8 the centre wins on all five one-parameter families. The minimum normalised margin is 0.0350, along
    M_t and its permuted copies.
  - multistart at d = 8: 160 of 160 SLSQP runs end at J;
  - at d = 9 there is a non-centre maximum, Ψ_9 − Ψ_9(J) = +0.01864, at the M_t-type point (diagonal 0.8156,
    off-diagonal 0.0615);
  - d = 10 fails on several families.
- 06:35 parent relayed the Codex CLI review of r1: ACCEPT-WITH-FIXES, one MINOR, no fatal or major issue
  (institute/…/review/chi7-codex-hostile-review-v1.note.md).
  - The minor: KPW Theorem 10 needs the endpoints of the 7 marked edges to induce a matching. Discard G if either
    deleted vertex lies in a triangle (probability O(1/n)); together with dist(v_1, v_2) ≥ 4 this makes the 14
    neighbours independent before rewiring. State uniformity via exactly binom(14,7) inverse endpoint assignments.
  - Codex also notes that the intermediate zero of L in Lemma 2.1(c) is exactly v* = 1/3.
  - Both are queued for the single final r2, once the Claude and priority reviews return; r1 is unchanged.
- 06:36 explore_d8_followup.py launched in the tool background (job bg_783; finite loops):
  - F1: minimum normalised margin over B_4;
  - F2: closed-form restricted-dual bounds B_β;
  - F3: volume fraction of B_4 in the 9-parameter cube.
- 06:37:10 follow-up finished (52 s) → evidence/explore_d8_followup.json:
  - F1: minimum normalised margin 0.035008 at M_{2/3}, where every row is (3/4, 1/12, 1/12, 1/12) on a permutation;
  - F2: B_β fails for every β ∈ [0, 1] (β = 1 is KPW: +0.0081);
  - F3: B_4 occupies 1.045·10⁻³ of the 9-parameter cube.
- 06:39:35–06:40:00 explore_d8_dualfamilies.py: g = β ln m + γ m with (1.25, −1.5) gives worst case ≈ 0 at J. The
  full Cauchy–Schwarz relaxation fails.
- 06:41:03–06:41:15 explore_d8_tune.py: Nelder–Mead gives (β, γ) = (1.3263, −1.4526); B_g's minimum normalised
  margin is 0.035008 (same as Ψ_8) and its Hessian coefficient at J is −0.082.
- 06:42:05–06:42:36 explore_d8_rowrelax.py: the row-only Cauchy–Schwarz R_g with retuned (1.2441, −1.1825) has
  minimum normalised margin 0.03501 on row-stochastic matrices (96 starts) and on B_4; the 60-grid one-free-row
  scan gives 0.0365.
- 06:43:23–06:43:30 explore_d8_separable.py: fully separable relaxations fail (−0.228 and −0.285).
- 06:44:31 d9_failure_enclosure.py, rigorous (arb plus exact rational primal and dual):
  - Ψ_9(M_{3/4}) − Ψ_9(J) = +0.0186292384986560592641… > 0, so the balanced second moment fails at d = 9;
  - Ψ_8 − Ψ_8(J) = −0.0609659 at t = 3/4 and −0.0466773 at t = 2/3.
- 06:46:19 probe_row_two_value.py: the per-coordinate first-order function F has up to 3 interior turning points
  in the sampled multiplier range, so route (b1)'s plain two-value lemma fails as stated (risk raised).
- 06:47 review/D8_SCREEN.md written (exploratory, no claims). Conclusion: d = 9 NO-GO (rigorous point enclosure);
  d = 8 conditional GO (numerics plus a closed-form dual bound with margin 0.035). The certification routes and cost
  estimates are in §4. Total screen time about 15 minutes, well inside the 90-minute bound. No processes left
  running; nothing was stopped.

## d = 8 analytic pilot (parent IRC ≈ 06:50–06:55; ≤ 2 h; no target frozen, no claims) — part 1

- 06:55:46–06:56:22 inline numerical check of the parent's x^{7/8} dual route; nothing saved, no error found
  (E(J) = 9/√2, U(J) = Ψ_8(J), per-row max ratio −0.0550, κ = (441/128)(a² − 1/9) ≈ 0.02344).
- 06:56:42 fetched Diaconis–Saloff-Coste 1996 (Ann. Appl. Probab. 6, 695–750) from the Duke course mirror:
  sources/diaconis-saloffcoste-1996-lsi.pdf (6a67ed86…db0c) + layout. Theorem A.1 (l.2727–2739) gives
  α = (1 − 2π_*)/log(1/π_* − 1) for K(x,y) = π(y); uniform on 4 points gives α = 1/(2 log 3). Theorem 3.5(ii)
  (l.1365–1371) gives ‖H_t‖_{2→q} ≤ 1 when e^{4αt} ≥ q − 1 (reversible). Duality is used the same way at l.2672–2676.
  The parent independently confirmed the normalisation by IRC.
- 06:59–07:00 code/verify_d8_pilot.py written; first runs failed on a Fraction/arb type error and on an
  over-crude monotone enclosure near x = 0.29. Fixed with centred-form fallback.
- 07:06:06–07:06:33 verify_d8_pilot.py → evidence/verify_d8_pilot.json (+ .stdout.txt): all_ok = true (details in
  the pilot note).

## χ7 frozen r2 (parent IRC after both reviews returned)

- Inputs read:
  - institute/…/review/chi7-claude-complete-review-v1.note.md: ACCEPT-WITH-FIXES, minors m1–m7;
  - chi7-claude-source-visibility-addendum.json: m1 is a parent prompt-numbering artefact; the LF citations are
    correct;
  - chi7-priority-audit.md: AN (12) and NPG are prior work on the constant;
  - chi7-codex-hostile-review-v1.note.md.
- 07:07:39 fetched NPG arXiv:2109.13347v1 into sources/: nir-perezgimenez-2109.13347v1.pdf (09161e92…5893),
  layout (c4bd2801…c5083). Its quotes were checked directly:
  - Theorem 1.2 at l.113–118;
  - "conceivable" at l.121–123;
  - non-contiguity at l.65–67;
  - (8) at l.524–527;
  - Theorem 3.1 at l.530–535;
  - c = d/2 at l.1778–1780.
- 07:12:31 review/PROOF_CHI7.r2.md frozen (mtime), SHA-256
  f157337d864cb122247d5c9ec3c73e2d12efb5786c837404efbeafa1b6afb6a5. r1 is unchanged (8a79ba3c…906c). Fixes, per r2
  §9:
  - induced matching, triangle exclusion, exact C(14,7) conditional uniformity and the a.a.s. transfer;
  - loop exclusion via the colouring definition and KPW l.184–194;
  - W99 Theorem 4.1 conclusion quoted (l.1584–1596);
  - Molloy–Reed (KPW l.67–68, l.175–178; W99 l.1102–1107) primary for χ ≥ 4, computer certificate as cross-check;
  - J = (1/4)J_4 unified;
  - prior work stated explicitly, and r1's §8 sentence corrected;
  - v* = 1/3.
  verify_rigorous.py was not rerun (r2 changes no computation). README §1 updated.

## d = 8 analytic pilot — part 2

- 07:13–07:18 verify_d8_pilot.py extended with two float items: a weak-duality sanity check (U ≥ Ψ_8) and a β-window
  control. One run failed on a tuple return from psi_exact; fixed.
- 07:18:26–07:18:56 verify_d8_pilot.py → evidence/verify_d8_pilot.json (+ .stdout.txt), all_ok = true:
  - sympy S1–S6 all true; arb R1–R4 all certain;
  - R4: 8000 + 8000 pieces, 113 needing the centred form; h″ upper bounds −0.2087 and −1.0331;
  - weak duality: min(U − Ψ_8) = +1.7e−5 over 300 random DS, and −8.9e−16 at J;
  - β-window: negative maxima for every tested β ∈ [0.80, 0.95].
- KPW l.596–800 and l.995–1036 re-read. (3.9) is used for the S_2 estimate (l.775–777, l.1021–1033); the S_1
  asymptotics improve (3.6)–(3.7) (l.778–779).
- 07:21:28 (mtime) review/D8_PILOT.md written (exploratory); a time-label fix followed at 07:22. GO recommendation for a frozen target
  χ(G_{n,8}) = 4. It corrects D8_SCREEN §3, whose β-grid {0, …, 0.75, 1} never tested 7/8, and D8_SCREEN §4's
  residue list (d = 8 needs r = 1, 2, 3). D8_SCREEN itself is unchanged.
- 07:22:23–07:24:04 bounded d = 8 priority search, read-only, 5 web queries:
  - queries:
    1. "random 8-regular" chromatic 4-colourable a.a.s.;
    2. G_{n,8} / χ(G_{n,8}) with 4-colorable and second moment;
    3. 4-colorability threshold d = 8, 9 with KPW and improvement;
    4. "8-regular" chromatic "{4,5}";
    5. a recent-year query on small-degree random regular colouring.
  - Hits were already-known sources only: Shi–Wormald 2004-24, AM04, KPW, Coja-Oghlan–Efthymiou–Hetterich
    1308.4287 (k ≥ k₀ only), Kang–McDiarmid survey, Wormald survey, Bykova REU. No statement of χ(G_{n,8}) = 4 for
    the uniform model was found.
  - Access holes: the same as the parent audit (Semantic Scholar, Google Scholar, dblp, ScienceDirect).
  - A miss is not novelty.
- KPW reference audit (pilot risk 2): a grep of the layout for Lemma 5/(3.7)/(3.8)/(3.9)/(3.15) finds them only at
  l.713–779, l.912 (S_1 improves (3.9) via (3.10) + Lemma 8), l.999–1033 (S_2) and l.1034–1138; none in §4.
  Recorded in D8_PILOT §8.
