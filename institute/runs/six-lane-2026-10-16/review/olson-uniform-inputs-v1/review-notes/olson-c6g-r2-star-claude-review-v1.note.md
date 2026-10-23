DISPOSITION: ACCEPT-WITH-FIXES

Audit of T1 `c6/proof-SEEDGstar.md` (476e9a28…5b22) and T2 `c6/proof-SEEDG-cls.md` (5a5038e4…02ba), with `c6/seedX2.py`, `c6/seedXstar2.py`, the six receipts, base r2 and the r1→r2 diff. Paths are relative to mixdef-high/. Review date 2026-10-17 (PDT).

Summary:
- Every written step re-derives.
- I found no place where the code is weaker than the written hypotheses.
- Every table row, total and control figure agrees with the receipts.
- The fixes concern wording, one superfluous hypothesis, citations, the 'allowed' definition, and evidence and provenance.

## FATAL
none

## MAJOR
none

## MINOR

**m1. SEED-G* hypothesis is ill-formed** (`c6/proof-SEEDGstar.md:50-52`)
- The hypothesis is a per-run "either/or" followed by "these seeds satisfy (P2) and (PIN)".
- That quantifies over seeds that need not exist: a run with an empty actual intersection has no seed.
- Corrected statement: "Suppose that either some run t has seeds obtained by Lemma GS (a) from actual configurations with empty intersection, or every run t has a seed [a_t, b_t] satisfying (QS*) and these seeds satisfy (P2)."
- With that statement, the proof at :53-54 holds verbatim.
- Correctly, an empty (QS) or (QS*) window is never used as an exclusion anywhere in T1 or T2.

**m2. Wrong comparison wording** (`c6/proof-SEEDGstar.md:42-43`)
- "an integer >= each of the nine displayed bounds" is false as written. The sum can lie below, for example, Delta0 + E + 2.
- Corrected: "the sum equals min_{i,j}(U_i + T_j). Each term sum is >= its displayed bound, so the sum is >= L_A(d), and as an integer it is >= ceil(L_A(d)) >= 1 - a_t."
- The same correction applies to (B^s).

**m3. Incomplete list of facts used** (`c6/proof-SEEDGstar.md:20`)
- The nine bounds also use m - 1 <= m' <= m, m' >= 1 (r2:113, r2:134-137) and floor(a/2) >= (a-1)/2.
- They do not use (0.2'). That enters only in the comparison with the targets (r2:126, :133).
- Correct the list. The bounds themselves are valid on the full domain (Check 1).

**m4. Lemma LF: closed forms correct, proof incomplete** (`c6/proof-SEEDGstar.md:22-29`)
- (a) For d = -b <= -1, the L_A entry (R + b)/2 + 1 is never compared. It exceeds (Delta0 + E)/2 + 2 by (2kappa + b - 2)/2 > 0.
- (b) The case d = 0 is written out for one side only.
- (c) The second entries of the mins at :22 and :23 never attain. For |d| <= E + 1, the entry Delta0 + E - |d| + 1 exceeds (Delta0 + E - |d| + 3)/2 by (Delta0 + E - |d| - 1)/2 >= (Delta0 - 2)/2 > 0.
- Corrected statement:
  - L_A(d) = (Delta0 + E + 3 - max(d, -1))/2
  - L_B(d) = (Delta0 + E + 3 + min(d, 1))/2 = L_A(-d)
- The identity L_B(d) = L_A(-d) holds entrywise: the eight entries of L_B(d) are the eight entries of L_A(-d).

**m5. (PIN) is superfluous** (`c6/proof-SEEDGstar.md:40`, `:46`, `:63`)
- Every seed has b_a <= U({a}) (r2:74). So b_a - lambda({a}) <= p - lambda({a}^c) - lambda({a}) <= p - 1 by Lemma P0 (r2:59).
- Drop (PIN) from SCW-G*, SEED-G* and X*. The upper end of the pin becomes b_a + U({a}^c) <= 2p - (lambda({a}) + lambda({a}^c)) <= 2p - 1.
- Consequences:
  - `c6/seedXstar2.py:57` is vacuous in MODES 0 and 1, because sigma ⊆ [lambda({t}), U({t})] (`c6/seedX2.py:58-59`, `:73`).
  - This explains why the superseded seedXstar.py gave identical counts (:87).
  - r2:154-156 can be shortened the same way.

**m6. Wrong wrap reason in Lemma CF'** (`c6/proof-SEEDG-cls.md:35`)
- Replace "(k >= 12)" by "(the path ends t+2, t-2 have cyclic distance min(4, k-4) >= 2, as k >= 2kappa + 3 >= 7)".
- This is the same correction r2 made for Lemma CF (r2:13-15, r2:186-187).

**m7. T2 cites r1 "under review"** (`c6/proof-SEEDG-cls.md:6`, `:25`, `:54`, `:58`)
- Checked against the diff, nothing T2 uses has changed:
  - No hunk touches Lemma GS.
  - Lemma CF changed only its wrap reason (diff:61-63).
  - r1's Theorem SEED-G (diff:41-43, a quality seed for every run) suffices. T2 disposes of empty sigma itself (cls:56-57) via actual configurations. It does not rely on r1's withdrawn parenthetical (diff:33).
- T1's citation of r2, versus `c6/seedXstar2.py:6` citing r1, is equally immaterial. r2 Sec. 2 differs from r1 only at r2:150, and the downstream bound is unchanged.
- Fix: cite r2 (353b0e95…30b7) and update the status line.

**m8. 'allowed' definition does not match the code** (`c6/proof-SEEDG-cls.md:39-42` vs `c6/seedX2.py:38-50`)
- For a* = 1 the code also discards triples with:
  - b* <= 1 and E > n_pr;
  - b* >= 2 and E - n_pr < b* - 1;
  - b* >= 1 and E >= B.
- Each of these is a necessary condition for an actual word, so the code is sound. The written definition must still match it.
- Corrected definition: pi = (a*, b*, n_pr) is allowed iff
  - 1 <= a* <= E + 1, 0 <= b* <= min(B, E + 1), 0 <= n_pr <= min(B, E);
  - b* = 0 ⇒ n_pr = B, and b* >= 1 ⇒ n_pr + b* <= B;
  - if a* >= 2: (a* - 1) + (b* - 1)^+ + n_pr <= E, with e_an := (b* - 1)^+;
  - if a* = 1: e_an := E - n_pr, with e_an = 0 for b* <= 1, e_an >= b* - 1, and n_pr + e_an + 1 <= B for b* >= 1.
- The triple of every word is allowed (Lemma PR).

**m9. "class for class" is not what the receipt shows** (`c6/proof-SEEDGstar.md:84`)
- The receipts show only equal per-(label, verdict) counts. I checked all five rows of seedXstar2_mode1.txt:2-6 against seedX2_mode0.txt:2-6.
- Say "reproduces the per-label counts (p <= 23)". Class-wise equality follows from Lemma QQ and the shared code, not from the receipt. Alternatively, emit per-class lines.

**m10. The "additional" X* column needs nesting that Lemma QQ does not state** (`c6/proof-SEEDGstar.md:47-49` with `:70-80`)
- The X* column is computed as X*-pass - SA/PA - X. That needs X-pass ⇒ X*-pass, class by class.
- `c6/seedXstar2.py:52-56` also tests weight pairs that cannot co-occur:
  - equal weights;
  - two anti weights with b1 + b2 > B, i.e. y < -B.
- Both lie outside r2's range -B <= y <= E + 2 (r2:49).
- The nesting still holds. The uses of y >= -B in r2:139-151 need only:
  - y >= -2B - E - 4 (:140);
  - y >= -2kappa - E (:143);
  - y > -2B - 2E - 7 (:148);
  - d_v >= -B (:151).
- All four hold for y >= -2min(B, E+1).
- Add to Lemma QQ: "(P2) holds for any weights d1, d2 in [-min(B, E+1), E+1] with e(d1) + e(d2) <= E whose seeds satisfy (QS) and a >= lam(d, 1)".

**m11. Unverifiable "RA2" identification** (`c6/proof-SEEDGstar.md:81`, `c6/proof-SEEDG-cls.md:73-74`)
- The receipts show one OPEN0:written:pass class per p (seedX2_mode0.txt:7-8). By r2:290-291 this is an RA class.
- Whether it is RA2, RA3 (a) or RA3 (b) cannot be determined from the packet.
- Write "the RA class of r2 Sec. 6", or give (k, kappa, B).

**m12. No control is sensitive to X* on OPENE** (`c6/proof-SEEDGstar.md:84-86`)
- MODE 2 is insensitive, as the text says. MODE 1 only compares against X.
- Nothing shows that (P2) ever rejects a class, so a vacuous (P2) bug would be invisible. I checked :52-56 by hand and it is correct.
- Add a mode with (QS*) tightened by one: lower end 2 - ceil(L_A), upper end ceil(L_B) - 2.
- Add a per-class report of which test fails, including the p = 31 

failure (`seedXstar2_mode0.txt:8`, `OPENE:fail` 1).

**m13. Provenance** (`c6/seedXstar2.py:13`, `:64`; `c6/seedX2.py:111`)
- The receipts carry no hashes of the exec'ed sources: seedX2.py, map6.py, ../c4/ind_star3.py and ../c4/ind_star_ex.py.
- seedXstar2.py reads seedX2.py from the working directory at run time.
- The two runs are 28 min apart: `seedX2_mode0.txt:1` starts 17:38:26 and `seedXstar2_mode0.txt:1` starts 18:06:05.
- Fix: print the sha256 of every exec'ed file in each receipt header.

**m14. Interpretive overreach** (`c6/proof-SEEDGstar.md:82-83`)
- "The obstacle left ... is the COUNT condition of Theorem C+, not the certification" is an [F] observation, at p <= 31 and at class level only.
- C+'s class condition is only a worst-case sufficient condition for (i)/(ii+) (r2:179-180).
- Corrected: "[F, p <= 31] In 3,113 of the 3,114 OPENE classes, the seed and certification hypotheses of X* hold at class level. In 377 of them C+'s class condition fails. There, exactly the words violating both (i) and (ii+) of Lemma C0+ are not excluded by Theorem SEED-G* [W+F]."
- Check: 3,113 = 1,793 + 756 + 187 + 377.

**m15. Presentation**
- `c6/proof-SEEDGstar.md:78-80`: label the X and X* exclusions [W+F] in the totals sentence.
- Same table (:71-77): state that the OPEN0 'X*' column counts all passing classes (here the RA class), not additional ones.
- `c6/seedXstar2.py:2`: "c6/proof-SEEDG-star.md" → "c6/proof-SEEDGstar.md".
- `c6/seedX2.py:16` and `c6/seedXstar2.py:6`: cite r2.
- `c6/seedX2.py:6` says E >= 2, but :79 also processes E = 0. It does so with the correct single profile (p+kB, p+kB, 1, 1, False).
- `c6/proof-SEEDG-cls.md:30`: state properness explicitly. The neighbours of t lie outside Q + t, so Q and Q + t are proper and 2m + 2 <= k is automatic. Also state the S1 total, sum ceil(L_i/2) >= (n1 - 3)/2.
- `c6/proof-SEEDG-cls.md:78`: "(their generic seeds attain the (QS) bounds)" is an unproved gloss; mark it as such.

## Check 1 — SEED-G* derivation

**Notation.**
- mn = min(d, 0), mx = max(d, 0).
- p - kappa = Delta0 + E/2.
- A - kappa - kB = A - B - 2kB = A + B - 2kappa = Delta0 + E (r2:45-46).
- Domain: (2.1), 1 <= m' <= m <= m' + 1, 2m <= k.

**(A^s) term sums, re-derived.**
- U1+T1 = 2p - m - m' + 2 >= 2p - k + 2 = Delta0 + E + 2. Uses m' <= m and 2m <= k.
- U1+T2 >= p + 1 + A - kappa - y (m' <= m) >= Delta0 + E/2 + 1 - mn (y <= A + mn).
- U1+T3 and U3+T1 >= (Delta0 + E)/2 + 2. Uses (F1) for m' resp. m, T3 >= 1 (y <= A) and U3 >= 1 (y' >= -B).
- U2+T1 >= p + y' - kB (m' >= m - 1) >= Delta0 + E/2 - mn (y' >= -B - mn).
- U2+T2 = Delta0 + E - d + m + m'. This is even >= Delta0 + E - d + 2; r2's +1 is lossy but never binding.
- U2+T3 >= (y' + A - d + 1)/2 + m' - kB >= (Delta0 + E - d - mn + 3)/2. Uses m' >= 1 and y' >= -B - mn.
- U3+T2 >= A - kappa - d + 1 + (B + 1 - y')/2 (m >= 1) >= (Delta0 + E + 3)/2 - d + mx/2 (y' <= A - mx).
- U3+T3 >= (y' + B - 1)/2 + (A - y - 1)/2 + 2 = (R - d)/2 + 1.

**(B^s) term sums (mirror).**
- V1+S1: same as U1+T1.
- V1+S2 >= p + A - kappa - y' (m' >= m - 1) >= Delta0 + E/2 + mx (y' <= A - mx).
- V2+S1 >= p + 1 + y - kB (m' <= m) >= Delta0 + E/2 + mx + 1 (y >= -B + mx).
- V2+S2 = Delta0 + E + d + m + m'.
- V2+S3 >= (y + A + d + 1)/2 + m - kB >= (Delta0 + E + mx + d + 3)/2. Uses m >= 1 and y >= -B + mx.
- V3+S2 >= A - kappa + d + 1 + (B + 1 - y)/2 (m' >= 1) >= (Delta0 + E + 3)/2 + d - mn/2 (y <= A + mn).
- V3+S3 >= (R + d)/2 + 1.

**Conclusions for item 1.**
- L_A and L_B (T1:14-17) are exactly the minima of r2:122-125 and r2:129-132, so T1:18-19 is correct.
- The bounds hold for every (y', m, m') in the domain without (QS).
- Each (A^s)/(B^s) sum is the minimum of nine integer term sums, so it is >= ceil(L). This justifies the ceilings (with the m2 wording).
- Case s = 2 is exactly (P2):
  - Q' = {s'}, and lo/hi are the seed endpoints (r2:106).
  - m(Q) = m(Q^c) = 1 if s', t are adjacent, else 2, and D_Q = d_s' + d_t.
  - The condition is symmetric in (s', t), so one condition per unordered pair covers both decompositions in SL.
- The pin needs only one run, a_a >= lambda({a}) (seed definition), Lemma P0, and (PIN). (PIN) is itself implied (m5).
- Lemma QQ is correct:
  - (QS) ⇒ (QS*), since ceil(L_A) >= L_A >= (Delta0 - d)/2 >= 1 - a_t, and symmetrically for L_B.
  - r2:138-151 derives (P2) for any two distinct runs. It uses (QS) on both, a_u >= lambda({u}), and -B <= y <= E + 2 (r2:49).
  - r2:152-156 derives (PIN) for any run.
- SEED-G* combined with C0+ is correct once m1 is fixed:
  - If w avoids, no actual-configuration intersection is empty.
  - SCW-G* and SL give X_Q >= lambda(Q) for |Q| >= 2, the lifts give the singletons, and X_[k] = p.
  - C0+ then gives the contradiction.
  - The exclusion used is the actual-configuration one (r2:77-79), never an empty window.

## Check 2 — Lemma LF

Entries are numbered 1-8 in the order of T1:14-17. In every case, entries 6 and 7 coincide.

**Case d >= 1.**
- L_A = a := (Delta0 + E - d + 3)/2. The other entries exceed it:
  - entry 4 by (Delta0 + d - 3)/2 >= 1/2, and entry 2 = entry 4 + 1;
  - entry 3 by (d + 1)/2;
  - entry 8 by (2kappa - 1)/2;
  - entry 5 by (Delta0 + E - d - 1)/2 > 0 (for d <= E + 1);
  - entry 1 trivially.
- L_B = b := (Delta0 + E)/2 + 2. The other entries exceed it:
  - entry 2 by Delta0/2 + d - 2 >= 1/2, and entry 4 = entry 2 + 1;
  - entries 6 and 7 by d - 1/2;
  - entry 8 by (2kappa + d - 2)/2;
  - entry 5 by (Delta0 + E)/2 + d - 1.

**Case d = 0.**
- Both minima equal c := (Delta0 + E + 3)/2.
- Entry 4 (for L_A) resp. entry 2 (for L_B) exceeds c by (Delta0 - 3)/2 >= 0, a tie at Delta0 = 3.
- Entry 3 exceeds c by 1/2, entry 8 by (2kappa - 1)/2, entry 5 by (Delta0 + E - 1)/2.

**Case d <= -1.** Mirror image, via L_B(d) = L_A(-d).

**Setting facts used.**
- Used for the closed forms: Delta0 >= 3 (r2:45); R - Delta0 - E = 2kappa with kappa >= 1 (the setting gives kappa = kB + B >= 2); the sign of d.
- Not used for the closed forms: E even, E >= 0, |d| <= E + 1. The last only shows that entry 5 never attains.
- L_A >= (Delta0 - d)/2 needs d >= -(E + 4); L_B >= (Delta0 + d)/2 needs d <= E + 4.

**Relaxation in real units.**
- L_A - (Delta0 - d)/2 = (E + 3)/2 for d >= 0, and (E + d)/2 + 2 for d <= -1.
- L_B - (Delta0 + d)/2 = (E + 3)/2 for d <= 0, and (E - d)/2 + 2 for d >= 1.
- Each is >= 3/2 iff |d| <= E + 1. Equality holds at the far-side endpoint: d = E + 1 for L_B, and d = -(E + 1) for L_A (possible only if B >= E + 1).
- T1:30-31 is therefore correct; its second min entry never attains.

**Exact integer relaxation (E even, eps := Delta0 mod 2).** Define:
- lo_QS = ceil((d - Delta0)/2) + 1 and hi_QS = floor((d + Delta0)/2) - 1;
- lo* = 1 - ceil(L_A(d)) and hi* = ceil(L_B(d)) - 1.

Then:
- lo_QS - lo* = E/2 + 2 for d >= 0, and E/2 + 2 - floor((|d| - eps)/2) for d <= -1.
- hi* - hi_QS = E/2 + 2 for d <= 0, and E/2 + 2 - floor((d - eps)/2) for d >= 1.
- On the domain each value lies in [2, E/2 + 2].
- The value 2 occurs on the far side when floor((|d| - eps)/2) = E/2, i.e. at |d| = E + 1, and also at |d| = E when eps = 0.
- Example: Delta0 = 3, E = 0, d = 1 gives (QS) window [0, 1] and (QS*) window [-2, 3].

## Check 3 — Lemma PR and allowed triples

- The identities re-derive:
  - E = e_al + e_an + n_pr and B = n_an + e_an + n_pr.
  - n_al = k - B + e_an >= k - B > 0, so a* exists.
  - e_an >= (b* - 1)^+.
- For a* >= 2:
  - j = n_al - n1 >= 1 runs carry e_al >= (a* - 1) + (j - 1).
  - This gives cls:16.
- For a* = 1: n1 = n_al and e_an = E - n_pr exactly.
- Every filter in profiles() is a necessary condition (m8), so every word has an allowed pi.
- Lower bounds:
  - n_al and the n1 bound both increase with e_an.
  - Evaluating at the least admissible e_an therefore gives valid lower bounds for every word with that pi. That value is (b* - 1)^+ for a* >= 2, and the forced E - n_pr for a* = 1.
- The weight set {1..a*} ∪ {-b*..-1} ∪ ({0} if n_pr >= 1) is correct.
- The guaranteed weights a*, -b* (if b* >= 1) and 0 (if n_pr >= 1) are correct; in the setting, the weight determines the run type and length (r2:41-42).

## Check 4 — Lemma CF'

- Setup: the path has k - 3 runs. Of these, n1' >= n1 - 3 are single-letter aligned runs and o = k - 3 - n1' <= k - n1 are other runs. So there are at most o + 1 maximal intervals.
- S1: sum ceil(L_i/2) >= n1'/2 >= (n1 - 3)/2. Since the count is an integer, it is >= ceil((n1 - 3)/2). Correct.
- P1: sum floor((L_i + 1)/3) >= (n1' - o - 1)/3 = (2n1' - k + 2)/3 >= (2n1 - k - 4)/3. Since the count is an integer, the ceiling follows. Correct.
- Pairwise non-adjacency:
  - Members alternate within an interval.
  - Across intervals, a non-member path run separates them.
  - Across the wrap, the path ends are at cyclic distance min(4, k - 4) >= 2 (m6).
- No member is adjacent to t, since every path run is at distance >= 2 from t.
- Q has m blocks and Q + t has m + 1 blocks. Properness is automatic (m15).

## Check 5 — Corollaries X and X*

**Implications.** Each written implication holds.
- Every (family, m) term used corresponds to a configuration that exists in w, because n1(w) >= n1(pi) and n_al(w) >= n_al(pi).
  - Its actual y lies in the family's range.
  - No-wrap holds at that y, since it is tested for every y.
  - Its GS (a) seed lies inside [max(L1, min_y s_lo), min(U1, max_y s_hi)].
- Hence the actual intersection J_t lies inside sigma_pi(d_t), and if w avoids, x_t ∈ J_t.
  - The hull over the full y range is therefore enough.
  - The per-(family, m) no-wrap test over every y is sound: a failure only drops a term.
- An empty sigma implies an empty actual intersection. This is the r2-compliant exclusion, not an empty window.
  - For a guaranteed weight it excludes every word of pi.
  - For any other weight it excludes only the words containing that weight.
  - The code matches this through gempty.
- If w avoids, sigma_pi(d_t) is itself a seed of t. (QS), (QS*) and (P2) are monotone under shrinking, so checking endpoints suffices.
- Any two distinct runs have e_s + e_t <= E and m_st ∈ {1, 2}, so the (P2) check covers them. (PIN) needs one run and is vacuous anyway.
- C+'s class condition implies (i) or (ii+) for every word, because n_ev,al <= e_al <= E (r2:179-180).

**Labelling.** X and X* are correctly labelled [W+F]: a written implication plus a computed hypothesis. The tables are headed [F] (cls:60, T1:69); the totals sentence still needs the m15 fix.

**Receipts.**
- The T2 table (cls:65-71) matches `seedX2_mode0.txt:2-8` row by row:
  - SA/PA = OPENE:written:pass;
  - X = OPENE:notwritten:pass;
  - X,noC+ = pass-noC+;
  - rest = OPENE:notwritten:fail;
  - the OPEN0 columns likewise.
  - Totals: 3,114 = 1,793 + 756 + 207 + 358.
- The T1 table (T1:71-77) matches `seedXstar2_mode0.txt:2-8`:
  - SA/PA + X + X* = OPENE:pass = 24, 46, 128, 193, 392, 868, 1085;
  - noC+ = 0, 1, 9, 17, 46, 133, 171;
  - fail = 1 at p = 31, otherwise 0;
  - OPEN0 = 0, 0, 0, 0, 1, 4, 7, of which pass = 1 at p = 29 and 1 at p = 31.
  - Totals: 3,114 = 1,793 + 756 + 187 + 377 + 1.
- The cls:76-79 control figures all agree:
  - 2,154 classes.
  - MODE 1: 190 (+6) against 1,887 (+93).
  - OPENE: 3 (+6) against 743 (+49), and every OPENE written class fails.
  - MODE 2: 1,358 classes (OPENE 355).
- The T1:84-86 control figures also agree: p = 19 adds 1 IS failure; p = 23 adds 3 IE + 6 IS failures; OPENE is unchanged.
- Cross-check with r2:285-291: for p <= 31, seedX2's 'written' counts reproduce r2's OPENE SA/PA, IE SA/PA, IS SA/PA/RA and OPEN0 RA columns.

## Check 6 — Code carrying the class-level claims

**Functions that carry the claims.**
- seedX2.py:
  - cdiv (:20) and classes (:21-31);
  - profiles (:32-52) and exact_seed (:53-74);
  - class_pass (:75-96), MODE 0 path.
- seedXstar2.py:
  - the exec of seedX2.py minus its guard (:13-17), which imports cdiv, classes, profiles and exact_seed;
  - bounds (:19-27) and class_pass (:28-60).

**Code that only splits the counts.**
- region_SA (:97-101), region_PA (:102-107) and the 'written' flag (:120-121).
- map6.py classify (:31-37), plus the unincluded c4 code.
- The main loops, which only aggregate.

**Audit against the written statements.**
- `classes()`:
  - It is the same enumeration as map6.py:45-51.
  - kappa >= k - p follows from R >= k, and kappa <= (k - 3)/2 follows from k >= 2kappa + 3.
  - E is even automatically.
- `profiles()`:
  - Every filter is necessary (m8).
  - The a* = 1 branch is exact: e_an = E - n_pr and n1 = n_al.
  - b* = 0 occurs only with n_pr = B (<= E).
  - n_an >= 1 is enforced via n_pr + b* <= B.
  - In the a* >= 2 branch, eal = E - n_pr - (b* - 1)^+ is the largest possible e_al, and n1 = nal - (eal - a* + 2) is the PR bound.
- `exact_seed()` matches cls:44-48:
  - lam, lamc and U follow r2:52-53, using Python floor division, which is correct for negatives.
  - [L1, U1] is the canonical range, and e_d is computed as stated.
  - The y ranges are S1 {m}, P1 {2m}, SA [m, m + E - e_d] and PA [2m, 2m + E - e_d].
  - M equals the CF/CF' ceilings via cdiv, and 2m + 2 <= k is enforced.
  - Q + t has type (y + d, m + 1).
  - No-wrap is tested at every y, otherwise the term is dropped.
  - The hull is intersected with the canonical range.
- `class_pass()` in seedX2:
  - Weights and guaranteed weights follow PR.
  - (QS) is equivalent to a >= cdiv(d - D0, 2) + 1 and b <= (d + D0)//2 - 1, exact for integers.
  - An empty sigma is skipped (case (i)) or sets gempty (case (ii)).
  - It returns 'fail' iff bad and not gempty.
  - cplus matches r2 Remark (3), and the E = 0 single profile is correct.
- `bounds()`:
  - The eight expressions equal T1:14-17.
  - Every operand is an integer or half-integer of magnitude far below 2^53, so the float sums and mins and math.ceil are exact.
  - It returns 1 - ceil(L_A) and ceil(L_B) - 1; MODE 1 returns the (QS) bounds.
- `class_pass()` in seedXstar2:
  - gempty makes the profile pass.
  - (QS*) is checked on every live weight.
  - (P2) is checked on ordered live pairs, including equal weights, with e(d1) + e(d2) <= E and m ∈ {1, 2}, exactly as T1:61-62.
  - (PIN) is checked on every live weight (vacuous, m5), and cplus is applied.
- `region_SA` / `region_PA` against r2 (SA) :200-201 and (PA) :218-220:
  - They are identical, except that region_PA adds the term (p - floor((E+B)/2))//2. That term is (a1), which (b1) implies, so it is redundant.
  - The RA2/RA3 conditions match r2:244-256: p >= 11 through the loop start, and p >= 13 for RA3 (a).
  - SA/PA classes are counted only with cplus, as in r2:282-283.
  - None of this is part of any exclusion claim.

**Weaker than written (unsound):** none found.

**Stronger than written (conservative):**
1. profiles() keeps impossible triples; there is no e_an <= n_an(b* - 1) bound, among others.
2. n1 and n_al are taken at the least e_an.
3. The y ranges ignore the excess carried by the other runs.
4. No-wrap is demanded at every y, and one failing y drops the whole (family, m) term.
5. The hull over y is used instead of the actual y.
6. The CF and CF' counts use crude interval bounds: k - n1 other runs, and B non-aligned runs.
7. (P2) is checked over a superset of co-occurring weight pairs, in both orders (m10).
8. (PIN) is checked for every live weight (vacuous).
9. The 2m + 2 <= k break is redundant.
10. classes() includes the ZSI-B classes (k = p + 1, kB = 1), which affects counts only.

## Check 7 — Scope after fixes

**[W]** — correct after m1-m4 and m6-m8; not yet independently re-reviewed.
- Lemma LF, Lemma SCW-G*, and Lemma QQ with the m10 extension.
- Theorem SEED-G*, for any NMH word with R <= 2p - 3, p >= 5 prime, satisfying (i) or (ii+). (PIN) can be removed.
- Lemma PR and Lemma CF'.
- Corollaries X and X* as implications: class-level criteria valid for any p.

**[W+F]** — computer-assisted; the code was audited here by hand, not re-run.
- For p ∈ {11, 13, 17, 19, 23, 29, 31}: all words of 756 (X) + 187 (X*) OPENE classes, beyond the 1,793 SA/PA classes of r2.
- In the 377 X*,noC+ classes: every word satisfying (i) or (ii+).
- Re-exclusion of many IE/IS classes, which were already covered by IND* [W+F].

**[F] aids only.**
- All counts by label; the labels come from map6.py and the unincluded c4 code.
- The controls.
- The "obstacle" remark.

**Open.**
- At p <= 31:
  - 1 OPENE class (p = 31) fails X*.
  - In the 377 noC+ classes, the words violating both (i) and (ii+) remain.
  - OPEN0 classes: 1 at p = 23, 3 at p = 29, 6 at p = 31.
- There is no X/X* class-level data for p >= 37; only r2's SA/PA/RA and IND* apply there.
- r2's p = 7 gap remains.
- There is no uniform-in-p version of X or X*.
- NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* and ordered Olson are neither claimed nor implied.

## Correctness, novelty, significance (kept separate)

**Correctness:** as above. There is no counterexample; every fix is a wording, citation, definition, provenance or control item.

**Novelty:** internal to this program only; no literature comparison was made.
- SEED-G* replaces r2's uniform targets (Delta0 ∓ d)/2 by the exact minimum of r2's own term-sum bounds, plus integrality.
- It isolates the 2-run step as (P2).
- The window gain is at least 2 integers per side, and E/2 + 2 on the near side.
- Corollary X* is the matching class-level criterion.

**Significance:** finite and modest.
- +187 OPENE classes, about 6.0% of 3,114, at p <= 31.
- Nothing new for OPEN0, and no asymptotic or uniform consequence.
- At p <= 31 the class-level bottleneck for excess classes moves to C+'s class condition.
