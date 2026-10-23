## UPAR3-v1 hostile review: 0 FATAL / 0 MAJOR / 11 MINOR

I re-derived UPAR3-Z, UPAR3-P and R3 at full scope. None of the eleven repairs changes a theorem, an inequality, a cell outcome or a residual test. No claim is rejected.

**What this review rests on.** Only the pasted text. Imports were used only at their verdict scope:
- UPAR2-P/R
- UPAR threshold, Lemma 1, cap and QQ
- UMR-F/P and Lemma 20
- UFC E0/ENV

**What it did not check:**
- hashes and byte counts
- UPAR2 LF124–193
- UPAR LF216–275 (literal R_PAR)
- the disposition and authority JSONs

**No unit narrowing.** The proof never sets ν=a except where e=0 is first derived: in Sec. 4 via Lemma 3 at κ=3b*+2d, and in Sec. 5 via Sec. 2.

### Per-claim verdicts

| Claim | LF | Math | Text |
|---|---|---|---|
| Sec. 1 contract: (W), ID, (Defect), parity, (Order), Q/I counts, (Cap) | 25–67 | PASS | FIX m1 m2 m3 |
| UPAR3-Z: F=e impossible, every orientation, e>0 nonunit | 69–99 | PASS | FIX m4 m5 m6 |
| (Gap) F−e≥2 | 100–103 | PASS | clean |
| One-run (Charge), table, two-run extension | 105–123 | PASS | FIX m8 |
| Minimal t=0,1,2, all orientations | 125–145 | PASS | clean |
| Nonminimal s=4,6, all orientations | 147–172 | PASS | FIX m6 |
| Sec. 6 necessity list, prime gaps, UPAR3-P on T3 | 174–183 | PASS | FIX m7 |
| Eight named cells | 185–196 | PASS | clean |
| R3 completeness and POSITIVE-BUDGET-COVER | 198–239 | PASS | FIX m10 |
| Residual rows | 241–253 | PASS | clean |
| Header, navigation, provenance | 1–23, 255–272 | n/a | FIX m9 m11 |

### Re-derivation record

**Contract (Sec. 1)**
- **(Defect).** Put the endpoint expressions for Θ(K) and Θ(Q) and the tail sums into ID, using |X|+|Y|=2h−2r−1. This gives e = F − (zP+z−l(X)−l(Y)) − sP − sQ − D.
- **Letter count.** zP+z = l(X)+l(Y)+2β′(K)+2β(Q). This gives (Defect) and β(X)+β(Y)=zP−W.
- **Parity.** ν+zP+Θ(K) ≡ a+(l(K)+a)+l(K) ≡ 0, so sP is even; sQ and D follow the same way.
- **(Order).** Θ(K)=Θ(I)+θ_u ≤ (A0−ν−z0)+θ_u, and θ_u ≤ t_r(S).
- **Q-count.** Uses 2r−3l(Q) ≤ Θ(Q) and l(Q)=a−z+2w.
- **I-count.** Uses l(I)=β′(I)+β(I) and z0=a−β′(I)+β(I).

**UPAR3-Z (Sec. 2).** Only ν≥a and the label-excess form of (Cap) are used.
- **Observation.** q(Q∪v)=z+1. The upper-window entries are:
  - eps ≤ 1;
  - near-A entry A0−z−1 ≥ (3κ−3)/4 > 1;
  - P entry ≤ (−11κ−16d+19)/4 < 0.

  So the bound is A0−ν−z−3, below the actual A0−ν−z−1. ν cancels.
- **Both weak.**
  - From zP ≥ 5b+4z−2d+1 and zP ≤ κ+b−2d: 4z ≤ κ−4b−1, so β(Y)=0 and zP ≤ |X|.
  - This gives 4a ≤ κ+6d−7b−4. The margin to δ+1 is (7κ−14d+7b+8)/4.
  - Y has at most z nonempty runs, so (Cap) gives κ ≤ 2a < κ/2, a contradiction.
  - At F=0 this reads κ ≤ 3−8d, which subsumes UPAR2's κ≥16d−7 branch.
- **I strong / Q weak.**
  - z0+z ≤ (κ−5b+6d−4)/2, hence κ ≥ 7b−6d+4 and z ≤ (κ−7b+6d−4)/6.
  - The gap to (κ−4b−1)/4 is (κ+2b−12d+5)/12 ≥ 9(b−2d+1)/12 ≥ 0, so the observation applies.
  - X is empty, but zP ≥ 2d > 0 and those letters have nowhere to go.
- **I weak / Q strong.**
  - 4a ≤ κ−7b+6d−4.
  - Y is all empty and negative, so (Cap) gives κ−b ≤ a.
  - Together: 3κ+3b ≤ 6d−4, impossible.
- **Both strong** is excluded by R2. The case split is complete.

**Charges (Sec. 3)**
- **One-run.** The needed entry is x ≥ A0−z−F+1, i.e. ≥ 6d−t−2 (minimal) or ≥ 6d+s−5 (nonminimal).
  - The P entry is ≤ −26d−5t+8 or −26d−3s+11, both < 0.
  - So only the near-A entry can carry the sum, which gives (Charge).
- **Two-run** at level r+2 ≤ κ−d+1:
  - the actual sum is A0−ν−4 but the near-A bound is A0−ν−6;
  - eps=0;
  - the P entry is M_{r+1}−R+4 < 0.

**Minimal families (Sec. 4)**
- **Both weak.** t+2α+sQ/2 ≤ w ≤ W ≤ t+1.
  - w=t: Y is positive and nonempty, so 2l(Y) ≤ 2, but l(Y) ≥ 4d+t.
  - w=t+1: Y is empty; also E(Y)=4d+t > 2d directly.
- **Mixed.** b ≤ n ≤ l ≤ z0+z ≤ b, so α(J)=0 and Θ(J)=b+2d.
  - I weak: negative empties ≥ 4d−t−2+2a > d+a/2.
  - Q weak: zP+sP ≤ F−z against ≥ 3b−2d+2−z, a gap of b+2d.

**Nonminimal families (Sec. 5)**
- **Both weak.**
  - W=1: zP ≤ 2b+s/2 against ≥ 4b−1 (w=1) or ≥ 4b−2 (wA=1).
  - W=0, sQ=0: zP+sP ≤ 2b+s/2+1 against ≥ 4b+1.
  - W=0, sQ=2: z=0, so the two-run extension applies.
- **Mixed.**
  - I weak: a ≤ 5, and y−2 ≥ 4d > d+5/2.
  - Q weak: 3z ≤ 6.
    - sQ=0: zP+sP ≤ 2 against ≥ b+2.
    - sQ=2: z=0, so the two-run extension applies.

**Sec. 6.** Constraints: b*≡κ (mod 2), b*≥2d−1, and Lemma 3. The surviving tuples (b*, F, e) are:

| κ | Tuples |
|---|---|
| 8d | (2d, 2, 0) |
| 8d+3 | (2d+1, 4, 0); see m7 for (2d−1, 0, 0) |
| 8d+4 | (2d, 2, 0 or 2) |
| 8d+6 | (2d, 2, 0 or 2) and (2d+2, 6, 0) |

The skipped values have composite p:
- κ=8d+2 gives p=3(6d+1);
- κ=8d+5 gives p=9(2d+1).

Also, κ ≤ 8d+6 ⟺ 9κ ≤ 4p+10. (24,53) is newly excluded too (κ=8d, d=3), though it is not one of the eight named cells.

**Cells.**

| Cell | d | κ−8d | (b*, r, F) | Family | Outcome |
|---|---|---|---|---|---|
| (19,41) | 2 | 3 | (5, 12, 4) | t1 | PROVED |
| (20,43) | 2 | 4 | (4, 12, 2) | s4 | PROVED |
| (22,47) | 2 | 6 | (4, 13, 2) and (6, 14, 6) | s6, t2 | PROVED |
| (27,59) | 3 | 3 | (7, 17, 4) | t1 | PROVED |
| (28,61) | 3 | 4 | (6, 17, 2) | s4 | PROVED |
| (25,53) | 2 | 9 | — | — | OPEN |
| (28,59) | 2 | 12 | — | — | OPEN |
| (29,61) | 2 | 13 | — | — | OPEN |

I recomputed every entry of the three residual rows:
- N, h, R, δ;
- the a′ minimum, max|c|, reservoir and |θ| bound;
- lo/hi, p+3, δ−2, δ;
- the (b*, r, F) tuples and the e lists (with F−e≥2).

All match.

### MINOR findings and minimal repairs

- **m1 (LF38).** "m is their size" holds only for 1≤|U|≤h−1 (UMR LF252–253). Add that qualifier.
- **m2 (LF64).** The Q-count and I-count also use the threshold floor Θ≥2r−3n (UPAR LF71–72) and n≤l, not just (W). Cite both.
- **m3 (LF56–121).** Bare b stands for b* before LF127 declares it, contrary to UPAR2 erratum v2 item 2. Declare b:=b* at LF45.
- **m4 (LF69).** The heading says "on ALL T", but the LJ data exists only off T2; on T2 the claim is vacuous. Write "on T\T2 (vacuous on T2)".
- **m5 (LF22–23).** "Both mixed orientations already excluded by UPAR2" is true only at F=0; Sec. 2 re-proves the mixed cases for every F=e. Insert "at F=0".
- **m6 (LF90, LF150).**
  - "T:=" collides with the target set T.
  - "x=y−1" collides with the window entry x.

  Rename both.
- **m7 (LF176–179).** The stated basis ("Lemma 3, F≥e, parity") does not exclude the tuple (κ=8d+3, b*=2d−1, F=e=0). Only (Gap) excludes it. The even rows list e=F explicitly but this odd row omits it. The conclusion is unchanged. Add "(b*=2d−1, F=0) removed by (Gap)".
- **m8 (LF121).** "Smaller by the same table bounds" is too terse for level r+2. Display eps=0 and P=M_{r+1}−R+4<0.
- **m9 (LF20).** "Complete residual of Sec. 6" should read Sec. 7.
- **m10 (LF200–237).** R3 paraphrases R2 instead of citing it.
  - "(Cost)" at LF236 is never defined in UPAR3.
  - "other new type Q or G" and "all type caps" at LF224 paraphrase UPAR2's "only one P exit".
  - Neither UPAR LF216–275 nor UPAR2 LF124–193 is in the packet, so "No old test is deleted" (LF201) cannot be checked here.

  Necessity holds as long as each paraphrase is read as the corresponding R2 test. Repair:
  - define R3 := literal R2 (UPAR2 LF194–218 with errata v1–v3) ∩ {F−e≥2}, restricted to T\T3;
  - treat (a)–(e) as a non-exhaustive gloss;
  - replace "(Cost)" with a reference to LF32–34 / UPAR Lemma 1.
- **m11 (LF255–267).** The packet I received lacks `olson-UPAR2-parent-disposition-v1.json` (pinned at scope LF28) and the authority JSON, so any governing content in them is unreviewed. This is a process issue only.

### Not claimed

This review makes no claim about:
- full T, or POSITIVE-BUDGET-COVER;
- existence or converse statements;
- full ordered Olson, or other k;
- novelty or priority;
- human, Lean or runtime certification.

It is a written/model review only.
