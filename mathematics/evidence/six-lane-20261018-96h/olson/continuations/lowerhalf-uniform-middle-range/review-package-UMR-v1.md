# Review package UMR v1 (uniform middle range, terminal k = p+1, kappa_hat = kappa)

Owner OlsonThirdCutWindow (same math2 slot). Written after /bin/date 2026-10-20T08:39:28-0700.
Status: CANDIDATE_UNVERIFIED written mathematics; no model review has been run by this owner (the parent runs all reviews
and verdicts). No novelty, priority, "first", Lean, human-referee or runtime claim. FQW (not accepted), TCW and P7L
(accepted only at their own scopes) are not premises.

## 1. Outcome and claims under review

OUTCOME: the ENTIRE target is NOT proved. The EXACT FIRST FAILING UNIFORM LEMMA is Lemma FC (proof Sec. 5): for every
frame of every NF word (terminal k = p+1, kappa_hat = kappa, (kappa,p) in T), Xi(S_ev)+Xi(S_od) <= -1. FC would prove the
whole target (Lemma 14); it is proved outside the residual class RES (Theorem UMR-P) and is OPEN on RES.
Target range T: p >= 17 prime, floor((p+7)/4) < kappa <= (p-3)/2. Claims under review (all uniform on T):
- Theorem UMR-F (proof Sec. 0, Secs. 1-3): in every frame, U'(P) = Theta(P) for every set of runs P with central level
  g/2 <= m(P) <= kappa+1 (g = p+1-2kappa); every empty run has a nonzero even theta; Theta(all runs) = B*-2nu0-2p.
  Components: (SR) from NF+GRX (Lemma 1); windows (Lemma 2); frame through SC0/Y'z and ZSTRUCT/FB at (p-1,kappa-1)
  (Lemma 3); label counts with the reservoir u1 >= |b_l|+2kappa-1 (Lemma 4); density, Neg(P) = L(P) symdiff A,
  |A^c| >= (p+kappa+1)/2 (Lemma 5); margins M0 >= 2kappa-1+E/2, >= 4kappa-2+e*-|A|, >= |A^c|-g+e* (Lemma 6); two-sided
  realisation with offsets x = max(eps, ell-q, M-q'), y = max(eps, M-q, ell-q') at every central level (Lemma 7);
  representatives (Lemma 8); theta pair-independence inside every block of two consecutive central levels (Lemma 9,
  offset sums <= 2delta+8) and chaining over the whole central range (Lemma 10); complements (Lemma 11); an interleaved
  additive triple at m_T = max(g/2, ceil(kappa/4), ceil((kappa-g-1)/2)) (Lemma 12); connectivity and f0 = 0 (Lemma 13).
- Theorem UMR-P (Sec. 4): no avoider has such an NF with a frame satisfying UB(S_ev) and UB(S_od). Components: identity
  Xi(S_ev)+Xi(S_od) = e* (Lemma 14); half-certificates (U) through supersets of N_S and (L) through supersets of P_S
  (Lemma 15); goodness (Lemma 16); exact cases (Lemma 17); the no-jump lemma (Lemma 18); Lemma 19.
- Lemma 20 (structure of RES): explicit necessary conditions (giant pair of runs with >= p+3 letters, or N_S
  'A^c-saturated'/n_S >= kappa+1, together with the analogous condition for P_(S')).
Cells (7,17), (7,19), (8,19): constants instantiated in proof Sec. 6; each is OPEN at Lemma FC (RES not excluded).
Not claimed: exclusion of any target cell; anything outside T; other kappa_hat, other k; rigidity; INV*; o_F assembly;
full ordered Olson; nonemptiness of RES; multiset-only statements.

## 2. Files (this directory)

| File | Bytes | SHA256 |
|---|---|---|
| UMR-scope-v1.md (frozen 2026-10-20T07:29:56-0700, before any derivation and before the parent route note) | 8604 | 2d0ef2fc8e7a5a94892a6b50a03ae55840931a36d5273734bce95e027728c4da |
| proof-UMR-v1.md | 40276 | c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9 |
| review-excerpts-UMR-v1.json (manifest, 14 entries) | 3261 | ec9a5c75d4fee9770f237cb376bb26a3a3b7484431a0ce9105e44b6d3f84419e |
| checkpoints/cp-01.md | 2040 | 6bff4b3b479721c9bf63927d1def04942dc173f4ed2264244bb9c0f81bbe7df1 |
| checkpoints/cp-02.md | 1745 | b037799c424a1cdf10943d66cbc6e1fb6e5e1d87701fab5fb30b558c0c964ac4 |
| checkpoints/cp-03.md | 1513 | 877f63fa48173a35617cf910dc718e888fcad34620be160e25b031b3e9bdef6e |
| checkpoints/cp-04.md | 1586 | 95cb6d0a936479fdf81be99681c0da00813ab9f49996c754664b1fbb19cc02cb |
| checkpoints/cp-05.md | 900 | 11edc85ea6c9c82f38e7dbc895e553f4a8750371e35f216395bcc53d31dc0e2c |
| checkpoints/cp-06.md | 1058 | 14fac13b08cec6517aad01cc5bc435d6a3b848072799733632dc7d680a5eb4a6 |
This package and the closing checkpoint cp-07 are hashed in cp-07 and in the owner's final report.

## 3. Manifest

review-excerpts-UMR-v1.json (sha256 ec9a5c75d4fee9770f237cb376bb26a3a3b7484431a0ce9105e44b6d3f84419e): 14 entries
{path, sha256, start, end}, absolute paths, inclusive LF ranges: proof (1-406), scope (1-97), authority transition
(1-49), parent untrusted route note (1-21; exposure comparison only), NF (proof-ROT-few-E-v4.md 28-43), GRX (7-20),
SC0 (1-11), FB verdict (1-16), proof-FB (9-24), FB erratum 1 (1-7), balfull (S') extension (26-34), (S1) definition
(zx-s1c line 19), LOWER parent erratum (1-10), FCW parent erratum (1-14; derivation patterns only). Raw excerpt size
about 68.9 KB in 687 lines (whole-file entries from wc byte counts; the partial ranges reuse byte counts measured for
the identical files, hashes and ranges in the TCW packet). Every hash was re-checked with shasum -a 256 at
2026-10-20T08:39 and equals the scope/proof records.
Not in the manifest (context or untrusted; hashes in proof Sec. 8): USK, FCW, SCW, TCW, P7L, K0T and LOWER-K1 verdicts;
the FQW, TCW, P7L, FCW and SCW proof texts; PL.

## 4. Premises actually used (each at its accepted scope)

NF; GRX if-direction (Lemma 1); SC0 through Y'z (Lemma 3(c)); ZSTRUCT and Lemma FB in (S') at (p-1,kappa-1) for t >= 1
(Lemma 3(d)); the (S1) definition; the LOWER parent erratum conventions. NOT used: PL in its entirety, Theorem P,
B0S-CJ''', S1(a), the Setting fact, FB-E, and every USK, K3, FCW, SCW, TCW, P7L and FQW lemma.

## 5. Where a reviewer should look first

- Lemma 7 Cases U and L (the bridge argument; conditions (C1) u1 >= bmax+max(ell,M)+1 and (C2) R-delta-2 >= bmax+1).
- Lemma 4(iv), the -s_j branch (uses n+ + E/2 <= 2kappa-3+g/2 through t and n- >= 1).
- Lemma 9: the six-entry lists for X+2 and Y+2 and the 36 pairwise sums (all <= 2delta+8 < 4kappa+6); Lemma 10 chaining.
- Lemma 12: the 27-sum bounds with couplings (I1), (I2) and the choice of m_T (needs 2|A^c| >= 3kappa+g).
- Lemmas 17-18: the swapping argument for exact cases and the no-jump argument; Lemma 20 (the residual class).

## 6. Process disclosure

- Freeze: UMR-scope-v1.md created at 2026-10-20T07:29:56-0700 (date taken right after mkdir, before creation), before
  any derivation and before the parent route note was read. Pre-freeze exposure (scope Sec. 4): my TCW, P7L and FQW work
  and their inputs; the parent's earlier transition notes; the Main IRC message and the transition (which name only the
  route note's topics); unwritten target-reading arithmetic (the range at p = 17, 19; delta = 10, 8, 12 at the three
  cells; at kappa = (p-3)/2, delta = p-7 and R = 2p-4); metadata; memory summary.
- Post-freeze reading: parent route note, TCW and P7L parent verdicts (cp-01).
- Machine steps: /bin/date before every timestamp; shasum -a 256; wc -c -l; ls; mkdir of this directory and
  checkpoints/; reading files; exclusive creation of drafted text with Python open(path,'x'). The proof was drafted by
  hand in six in-memory parts with six rewording replacements before its single creation (cp-05, cp-06). No assert
  statement of any kind, no parsing or checking of mathematical objects, no script, enumeration, solver, test, Lean,
  model CLI, nested agent, network, /tmp, deletion, commit or push. No file was edited, overwritten, moved or deleted.
- Checkpoint cadence: freeze 07:29:56; cp-01 07:45:35 (939 s); cp-02 07:59:31 (836 s); cp-03 08:17:27 (1076 s);
  cp-04 08:25:54; cp-05 08:30:55; cp-06 08:37:00; all gaps below 1200 s; no output was lost.
- Exposure use: every parent suggestion was re-derived (proof Sec. 7 (M1)); the final count, which the parent note left
  open, is the first failing uniform lemma.
