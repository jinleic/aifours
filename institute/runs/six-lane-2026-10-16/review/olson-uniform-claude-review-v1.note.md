DISPOSITION: ACCEPT-WITH-FIXES

T1 DISPOSITION: ACCEPT-WITH-FIXES

T2 DISPOSITION: ACCEPT-WITH-FIXES

T3 DISPOSITION: ACCEPT-WITH-FIXES

## FATAL

none

## MAJOR

none

## MINOR

**T1-m1. P/c6/proof-RZwide.md:L7-L8 (used at L38, L62). Imports and status record are incomplete.**
- Lemma H (beta = 0) is not listed as an import, but it produces the lam/U formulas at L38-L40.
- L62 uses the "actually empty interval" alternative of Theorem SEED-G. That alternative exists only in the r2 delta (change (4), P/c6/proof-SEEDG-r2.md:L17-L18, L77-L79, L168-L170). The r2 delta was accepted by the parent desk without re-review. The phrase "(review fixes submitted to the parent)" does not say this.
- No mathematical change is needed. By the GS(a) proof (SEEDG-r2:L96), an avoider's x_t lies in [max(lambda({t}),s_lo), min(U({t}),s_hi)].
- Corrected L7-L8: "Imports: Lemma H with beta = 0 (../../../inverse-parity/proof-PAR-K0.md Sec. 1, as in c6/proof-SEEDG-r2.md Sec. 0); the all-single-letter specialisation of c3/proof-C-r1.md Sec. 0; c6/proof-SEEDG-r2.md Lemmas GS, NW, SCW-G, SL, C0+ and Theorem SEED-G (r1 reviewed ACCEPT-WITH-FIXES by Codex and Claude; the r2 delta, including the actual-empty alternative used in Sec. 3, accepted by the parent desk without independent re-review)."

**T1-m2. P/c6/proof-RZwide.md:L32. The no-wrap argument covers only one side of the cycle.**
- The deleted triple separates the path ends t-2 and t+2 on one side only.
- Correct reason: their cyclic distance is min(4, k-4) >= 2, because k = p+kappa >= 10. This is the same correction made in SEEDG-r2:L12-L13 for Lemma CF.
- The conclusion is true.

**T2-m1 (optional simplification, not an error). P/c6/proof-S2wide.md:L30-L32, L36. The parity rule for c is unnecessary in T2.**
- There are no anti singles, so m-y need not be even.
- With c = 1 for every q:
  - j2 = q+1 >= 1 and j1 = B+[h odd]-1 >= 1 are integers.
  - Genericity holds; L44 already covers c = 1.
  - (2.1) becomes (m+y)-(n-B-4) = 5-Delta-q. This is positive only for (Delta,h) in {(3,0),(3,2),(4,1)}.
- So families (3,4) and (5,0) disappear. Hand checks:
  - (p,g,B) = (11,6,2): m=4, y=7, j2=3, j1=1, footprint 11 = 17-2-4.
    - Arcs: Q(7,4): lam = min(8,5,5) = 5, U = max(3,5,5) = 5. Q+t+(8,5): [6,6]. Q+t-(6,5): [5,5].
    - Seeds [1,1] and [0,0] lie in the (QS) windows [0,1] and [-1,0] for Delta = 3.
  - (11,3,3): m=3, y=4, j2=1, j1=2, footprint 7 = 14-3-4.
    - Arcs: Q(4,3) = [4,5], Q+t+(5,4) = [5,6], Q+t-(3,4) = [4,5].
    - Seeds [0,2] and [-1,1] lie in the windows [-1,2] and [-2,1] for Delta = 5.

**T2-m2. P/c6/proof-S2wide.md:L6-L8. The import list is incomplete.**
- Used but not listed:
  - Lemma NW (L73) and GS(a) (L74).
  - Lemma H (L15-L17).
  - Theorem W-ALL (L86).
  - Theorem SEED of c6/c5-fixes/proof-SEED-r3.md (L86-L87).
  - Theorem RZ-wide (L88-L89), which was unreviewed when T2 was written.
- Status notes are also missing:
  - The actual-empty alternative (L51, L74, L81) comes from the SEEDG r2 delta, accepted by the parent desk only.
  - The r3 delta of SEED was also accepted by the parent desk only.
- Corrected list: "...c6/proof-SEEDG-r2.md Lemmas NW, GS(a),(b), (QS), Lemma C0+, Theorem SEED-G (r2 delta parent-accepted); Lemma H (beta = 0, PAR-K0 Sec. 1); for the Corollary only: Theorem W-ALL (c3/proof-WALL.md), Theorem SEED (c6/c5-fixes/proof-SEED-r3.md), Theorem RZ-wide (c6/proof-RZwide.md)."

**T2-m3. P/c6/proof-S2wide.md:L21-L26. The packing-lemma proof omits no-wrap and the properness of Q+t.**
- Add: "the path ends t±2 are at cyclic distance min(4,k-4) >= 2 (k = p+kappa >= 11 as kappa >= 4); Q+t is proper since both neighbours of t are omitted."
- The bound 2m+2 <= k is already at L42.
- The conclusion is true.

**T2-m4. P/c6/proof-S2wide.md:L90 (also title L1). The scope sentence overreaches.**
- "This corollary closes ONLY the all-single-letter NMH subcase" is too broad. NMH (P/README.md:L25-L26) allows k = 2p-2.
- Counterexample to the stated scope: p=7, g=1, B=4.
  - Then kappa=5, k=12=2p-2, A=8 <= 13, 1 <= B=4 <= kappa-1, and R=12=2p-2.
  - This is an all-single-letter NMH word. It lies outside the corollary (R <= 2p-3) and outside the c3 setting (12 < 2kappa+3 = 13).
- "Closes" is also too strong for an unreviewed [W] result that rests on T1.
- Corrected: "This corollary settles, subject to review of Theorems RZ-wide and S2-wide, only the all-single-letter NMH words with R = k <= 2p-3 (all-single-letter item-(iii) words); all-single-letter words with k = 2p-2, words with excess, parity/inverse reductions and ordered Olson are not settled by it."

**T2-m5 (cosmetic). P/c6/proof-S2wide.md:L59.**
- "arithmetic in the free integer B>=2" should read "arithmetic in the free integer g (B = g-h >= 2, p = 2g-h+Delta prime)".

**T3-m1. P/c6/proof-A0.md:L4-L6, L40-L41, L56-L57 (desk question T3.4). Status of the C0W import.**
- The Dependencies line calls C0W "(under review)", yet L40-L41 and L66-L68 are stated unconditionally. By the file's own record, the statements overreach their declared dependency status.
- Judgment: no conditional qualifier is mathematically required.
  - C0W's hypotheses (B >= kB+1, 3kB+1 <= p, NMH with R <= 2p-3, (0.2) = (L)) match case (ii) verbatim.
  - C0W uses only:
    - Lemma DF (singleton inequalities, d_t <= E+1 <= p-3);
    - sum c = D-p (i.e. sum x = p);
    - A <= 2p-1, k >= 4, p >= kB+2;
    - (L) at the produced proper P.
  - I re-verified steps (1)-(4) at P/c6/proof-C0WB.md:L27-L49.
  - Both reviewers accepted r0 with no change to DF or C0W, and r1 is byte-identical there.
- The record must therefore be corrected. Exact wording:
  - **L5:** "c6/proof-C0WB.md (r0, sha256 ac52d85f...de77) Lemmas DF, C0W, reviewed ACCEPT-WITH-FIXES by Codex and Claude with no change to DF or C0W (byte-identical in the not-yet-re-reviewed repair c6/proof-C0WB-r1.md); case (iii) also uses refinement C4 of c6/c5-fixes/proof-Cplus-r2.md (s0 >= 1/2 suffices; parent-verified)."
  - **Append after L41:** "(Case (ii) imports Lemma C0W of c6/proof-C0WB.md r0; cases (i), (iii) import only c3/proof-C-r1.md Secs. 0-2 and steps (B1+), (B2+) of c6/c5-fixes/proof-Cplus-r2.md.)"
  - **L56-L57:** "Lemma C0W (c6/proof-C0WB.md r0) gives a contradiction: its construction of a proper P with (M), (Fl), (P) uses only the singleton inequalities, sum x = p and NMH scalars; the contradiction is (L) at P."
- If the desk treats the unreviewed r1 as governing, use instead: "Theorem C0-all (conditional on Lemma C0W of c6/proof-C0WB.md)" and "Corollary (conditional on Lemma C0W, via Theorem C0-all)".

**T3-m2. P/c6/proof-A0.md:L4-L6 vs L66-L70. The Corollary's imports are not listed.**
- Not listed:
  - From SEEDG-r2: the canonical lifts and Lemma P0 (L59-L67), Lemmas TS, GS, NW, SL, SCW-G, and the r2 actual-empty alternative.
  - From c6/proof-SEEDGstar(-r1).md: Lemmas SCW-G*, QQ and Theorem SEED-G*.
- No version is named for SCW-G*. In r1, (PIN) is automatic (SEEDGstar-r1:L60-L61), so listing it as a hypothesis is stale but harmless. The r1 repairs are not re-reviewed.
- I re-checked r1's SCW-G*:
  - s >= 3: min_i U_i + min_j T_j = min_(i,j)(U_i+T_j) >= L_A(d). The left side is an integer, so it is >= ceil(L_A) >= 1-a_t.
  - s = 2: this is exactly (P2).
  - Pin: a_a+lambda({a}^c) >= 1, and b_a+p-lambda({a}) <= 2p-1 by P0.
- Add: "for the Corollary only: c6/proof-SEEDG-r2.md (canonical lifts, Lemmas P0, TS, GS, NW, SL, SCW-G; r2 delta parent-accepted) and c6/proof-SEEDGstar-r1.md (Lemmas SCW-G*, QQ, Theorem SEED-G*; r0 reviewed ACCEPT-WITH-FIXES, r1 repairs not re-reviewed)."

**T3-m3. P/c6/proof-A0.md:L66-L70. The Corollary's quantifiers are unstated.**
- The text does not say "every run" for the seed routes or "some run" for the empty alternative.
- "Actual-empty" must mean configuration-derived GS(a) seeds; an empty (QS)/(QS*) window alone excludes nothing (SEEDG-r2:L77-L79).
- In L69-L70 the singletons of (L) come from the lifts, not from "the certification lemma".
- Corrected statement: "Let w be NMH with R <= 2p-3. Suppose (a) some run t has GS(a) seeds from actual configurations with empty intersection; or (b) every run has a quality seed from actual configurations; or (c) every run has a nonempty seed satisfying (QS*) and these seeds satisfy (P2) (SCW-G*, c6/proof-SEEDGstar-r1.md). Then w has an identity 2p-subword; no n_ev,al or (A*) condition is needed."
- Corrected proof: "(a) excludes directly. In (b)/(c), if w avoids, the canonical lifts give lambda({t}) <= x_t; SCW-G (resp. SCW-G*) gives certification and X_[k] = p; SL gives X_Q >= lambda(Q) for |Q| >= 2; so x satisfies (L), contradicting C0-all."

**T3-m4. P/c6/proof-A0.md:L71. Unsupported implicature.**
- "Universal seed existence remains open for words with excess" implies that seed existence is settled for E = 0.
- T3 proves nothing about seeds. For B = 1, the cited exclusions (W-ALL, SEED) are not SEED-G quality-seed certificates.
- Corrected: "This does not prove that any NMH word has such seeds. Quality seeds (or actual-empty intervals) are established uniformly only in the regions of c6/proof-SEEDG-r2.md and, subject to review, for all-single-letter words with B >= 2 (c6/proof-RZwide.md, c6/proof-S2wide.md); seed existence is open in general, in particular with excess."

**T3-m5. P/c6/proof-A0.md:L17. The Kill criterion is stated without "proper" and without a source.**
- Corrected: "For a proper Q and integer x: X_Q < lambda(Q) iff (M), (Fl), (P) (Kill lemma, P/c3/proof-C-r1.md:L43-L46; Lemma H with beta = 0, c3:L27)."
- Its use at L32 has P proper, so there is no gap.

## Answers to the review questions

### T1

**T1.1 (L17-L19). Correct.**
- m >= ceil((2g+1)/2) = g+1, so r >= 1.
- c ≡ r (mod 2) and c <= r, so i = (r-c)/2 is a nonnegative integer.
- j = i+y, hence i+j = m and j-i = y.

**T1.2 (L24-L34). Correct, apart from T1-m2.**
- kappa = 3 forces (g,B) = (1,2), m=2, c=1, i=0.
- kappa >= 4 gives floor(kappa/2) >= 2, so m <= kappa-2 and 2i <= B-3.
  - Hence i >= 1 forces B >= 5, and B in {2,3,4} gives i = 0.
- Worst case t, t±1 all anti: beta = B-3 >= 2i, and every-other selection gives sum ceil(L/2) >= beta/2 >= i.
- Worst case t, t±1 all aligned: alpha = n-3 >= 2m, because 2m <= kappa+1 <= p-2 <= n-3 (g >= 1). After removing at most 2i aligned neighbours, (alpha-2i)/2 >= m-i = j.
- At p = 7 the classes are (1,2) and (1,3): i=0, j=2, alpha >= 5.
- Q and Q+t are proper (t±1 are omitted) with m and m+1 blocks, and D_Q = j-i = y.

**T1.3 (L38-L55). Correct; no off-by-one error.**
- Formulas: SEEDG-r2:L52-L53 with E=0 gives A-kappa = p-B, hence U = max(b-1, v+B-b, ceil((p-g+v)/2)-1), matching L39-L40.
- L41 equals GS(b)'s definition (SEEDG-r2:L93).
- The comparisons use only kappa <= 2m and 2m <= p-3 (p-3 is even):
  - lam(Q): first term p-m+1 >= m+4; second term m+c; floor term floor((kappa+c)/2)+1 <= m+c.
  - lam(Q+t): first term p-m >= m+3 > m+2; second term m+c+d+1 >= m+floor((c+d)/2)+1.
  - U(Q): third term C(c) = s or s+1; first term m-1 <= s-2; second term kappa+c-m <= s-1+c (tie possible).
  - U(Q+t): second term <= s+c+d-2 ∈ {s-2,s-1,s,s+1} <= C(c+d); ties at c+d = 3 are admissible.

**T1.4. Correct.**
- GS(b) gives (QS) bounds on [s_lo,s_hi]. NW then gives the hypothesis of GS(a).
- The resulting interval is a quality seed, or it is empty and is an actual exclusion (SEEDG-r2 r2 fix (4)).
- n_ev,al = 0 gives C0+ (i).
- Lemma R1 holds for every placement of the anti runs.

**T1.5. p = 7, (g,B) = (1,2).**
- Parameters: n=8, k=10, A=8, s=3, delta=6, Delta0=4; m=2, c=1, y=2, i=0, j=2.
- Arcs:
  - Q(2,2): lam = min(6,3,3) = 3; lamc = min(6,5,4) = 4, so U = 3. Arc [3,3].
  - Q+t+(3,3): lam = min(5,5,3) = 3; lamc = min(5,5,3) = 3, so U = 4. Arc [3,4].
  - Q+t-(1,3): lam = min(5,3,2) = 2; lamc = min(5,7,4) = 4, so U = 3. Arc [2,3].
- All four arcs attain their floor terms (some with ties).
- Seed windows: + gives [0,1] and - gives [-1,0]. The (QS) windows are [0,1] and [-1,0].
- Canonical singleton ranges: aligned [1,3], giving seed [1,1]; anti [-1,2], giving seed [-1,0].
- Consistency check: with x_al = 1, two non-adjacent aligned runs give X = 2 < lam(2,2) = 3.

### T2

**T2.1. Correct, apart from T2-m3.**
- A path containing at most B anti runs has at most B+1 aligned intervals.
- Blocks fit in an interval of length l iff sum(s_e+1) <= l+1.
- Pairs: sum floor((l+1)/3) >= (alpha-r)/3 >= (n-B-4)/3 >= j2.
- Singles: sum floor(C_l/2) >= (alpha+r-3j2-r)/2 = (alpha-3j2)/2 >= j1, since alpha >= n-3 > n-B-4.
- Intervals are separated by anti runs, pairs are adjacent aligned runs, y = 2j2+j1, and m = j1+j2.

**T2.2. Correct.**
- m-g = -q, so the stated equivalence holds.
- j2 = q+c and j1 = B+[h odd]-c; the footprint is m+y.
- (2.1) evaluates to 2B+ceil(h/2)+c+4-p = c+4-Delta-q, using p = 2B+h+Delta.
- The case split at L38-L41 is verified.
- The parity rule is not needed (T2-m1).

**T2.3. Correct.**
- Lemma H sees only (D_Q, m) = (g+c, m), so the T1.3 computation applies verbatim.

**T2.4. Every table entry recomputed (values minus g, as (lam terms → value; U terms → value)). All match L63-L67.**

| Family | Q | Q+t+ | Q+t- | Seeds (+, -) | Smallest (p,g,B) |
|---|---|---|---|---|---|
| (3,0): p=2g+3, B=g | lam (4,0,1)→0; U (-1,0,1)→1 | (3,2,1)→1; (0,0,1)→1 | (3,0,0)→0; (0,-2,0)→0 | [0,1], [-1,0] | (7,2,2) |
| (3,2): p=2g+1, B=g-2 | (2,0,0)→0; (-1,-2,0)→0 | (1,2,0)→0; (0,-2,0)→0 | (1,0,-1)→-1; (0,-4,-1)→0 | [0,0], [-1,0] | (11,5,3) |
| (3,4): p=2g-1, B=g-4, m=g-1 | (1,-1,-1)→-1; (-2,-3,-1)→-1 | (0,1,-1)→-1; (-1,-3,-1)→-1 | (0,-1,-2)→-2; (-1,-5,-2)→-1 | [0,0], [-1,0] | (11,6,2) |
| (4,1): p=2g+3, B=g-1 | (4,0,0)→0; (-1,-1,1)→1 | (3,2,1)→1; (0,-1,1)→1 | (3,0,0)→0; (0,-3,0)→0 | [0,1], [-1,0] | (11,4,3) |
| (5,0): p=2g+5, B=g | (6,0,1)→0; (-1,0,2)→2 | (5,2,1)→1; (0,0,2)→2 | (5,0,0)→0; (0,-2,1)→1 | [-1,2], [-2,1] | (11,3,3) |

- (QS) integer windows:
  - Delta=3: [0,1] and [-1,0].
  - Delta=4: [0,1] and [-1,0].
  - Delta=5: [-1,2] and [-2,1] (equality).
  - All seeds above satisfy them.
- Availability:
  - Singles families: 2g <= n-3 iff g <= p-3 (true, since g <= p-5).
  - (3,4): 3+2(g-2) = 2g-1 = p = n-B-4, so the packing lemma applies at equality (its hypothesis is non-strict).
- NW then GS(a) gives a quality seed or an actual exclusion.

**T2.5. Correctly assembled.**
- B=1: the all-single-letter NMH words with R <= 2p-3 are exactly W(p,g), 1 <= g <= p-4 (H = p-2-g; P/c3/proof-WALL.md:L15-L24).
  - p=5: g=1. p=7: g <= 3 = floor(11/3). Both lie in W-ALL's range.
  - p >= 11: W-ALL and SEED split the range at 3g = p+4 / p+5.
- B >= 2 forces kappa >= 3, hence p >= 7. Then T1 (B >= g+1) or T2 (g >= B) applies.
- Nothing finite or computer-assisted is used.
- The corollary rests on T1 and T2 (unreviewed at writing) and on the parent-accepted SEEDG r2 and SEED r3 deltas. C0+ (i) does not need C4.

### T3

**T3.1. Correct.**
- Z is nonempty and proper because sum bh = k-2g ∈ (0,k).
- The Kill criterion needs:
  - integral x;
  - Lemma H with beta=0, lambda(Q) = min(p-m+1, D_Q+m-kB, floor((D_Q+B)/2)+1) (c3:L27);
  - proper meaning Q ≠ ∅, [k] (inverse-parity/proof-PAR-K0.md:L13), with m = number of cyclic blocks (L15).

**T3.2 (Lemma A0). Correct.**
- Phi(∅) = 0, so P exists and is nonempty. Phi(P') <= g by integrality.
- X+m = Phi+bh, and bh(P') <= 0.
- m(P) <= m(P')+1, including the merge cases (since P ≠ [k]).
- x_t <= floor(d_t/2) <= E/2.
- g+E/2+1 <= p-B-2 < p, so (M), (Fl), (P) hold and P is proper.
- Only the following are used:
  - (L) at the single pattern P;
  - sum x = p, only to get Z ≠ [k];
  - the NMH scalars (d_t <= E+1, Delta0 >= 3, B >= 1).
- Singletons are not used.

**T3.3. Correct.**
- (2.2) is valid in Case B.
- The extension from Z to all runs drops only terms of the right sign (aligned -f_t <= 0; pair and anti terms > 0).
- (3.1) follows from 2·(n_pr+n_ev,an+n_ev,al)/2 <= n_pr+B+n_an+n_ev,an-2.
- (B1+) (Cplus:L62-L76) uses only (1.1)-(1.3). (B2+) (L80-L88) uses only |X_o| >= 2Delta+1 and (L).
- Case (i): s0 >= k-g-3B+1+n_pr >= g-B+4 >= 4.
- Case (iii): 2g+B >= p+1 gives E <= p-B-7, so 2E <= 2p-2B-14 <= 2p-2B-1. With n_ev,al <= E this gives s0 >= 1/2.
- The cases (i)-(iii) are exhaustive.

**T3.4.**
- The hypotheses match, and C0W uses only (L) plus scalars (re-verified above).
- The status judgment and corrected wording are in T3-m1.

**T3.5.**
- Both routes supply all of (L):
  - singletons from the canonical lifts (SEEDG-r2:L66);
  - sum x = p from the pin (L152-L156; SEEDGstar-r1:L67-L69);
  - |Q| >= 2 from SL.
- The corollary does make SEED-G and SEED-G* count-free. This is consistent with the imports: in both reviewed proofs (SEEDG-r2:L170-L172; SEEDGstar-r1:L84-L86) the count condition enters only through C0+.
- The reviewed files themselves keep (i)/(ii+).
- Quantifier and import problems are covered in T3-m2 and T3-m3.

**T3.6. No (L)-solution was found.**
- Spot checks:
  - W(5,1): the singletons force x_al=1 and x_an=-1. Then {anti, non-adjacent aligned} has X = 0 < lam(0,2) = 1.
  - W(11,3) with x_an = -3: Phi(Z) = 3 = g, Delta = 0, and {anti, s} gives X = -2 < lam(0,2) = -1.
  - W(11,3) with three isolated zeros: A0 stops at P = two zeros, X = 0 < lam(2,2) = 1.
- C0-all is integral (L25), so it is consistent with Lemma NOLP's real feasibility (c3:L115-L117).

### Also reported

- No import is used outside its hypotheses.
- No arithmetic slip was found.
- Overreach: S2wide:L90, A0:L71, and A0's unconditional statements versus its "(under review)" label.
- No [F] receipt is used as a premise.
- No silent reliance on proof-LB

-r1.md. Lemma R1 (RZwide:L22-L34) and the packing lemma (S2wide:L19-L26) are self-contained re-proofs. S2wide:L100-L101 cites c6/out/replayLB.txt only as a control.

## Counts

| Target | FATAL | MAJOR | MINOR |
|---|---|---|---|
| T1 | 0 | 0 | 2 |
| T2 | 0 | 0 | 5 (includes optional T2-m1 and cosmetic T2-m5) |
| T3 | 0 | 0 | 5 |

## Correctness, novelty, significance

**Correctness.** I re-derived every displayed inequality of T1-T3 by hand. I also recomputed the full exceptional table of T2 and the p = 7 edge case of T1, and re-checked the imported steps the targets rely on: GS(b), NW, the SCW-G/SL route, (B1+)/(B2+), C0W, and r1's SCW-G*. I found no mathematical error, no integer solution of (L), and no import used outside its hypotheses. All findings concern the record, wording, or optional simplification.

**Novelty.** Not assessed; no literature or priority search was requested or performed, and no firstness claim is made. The arguments specialise the lane's own tools: genericity with Lemma GS, packing, and the Kill lemma. The one new device is A0's first-defect-prefix stopping rule, an elementary integrality observation.

**Significance (within this program only).** Subject to acceptance, T1 and T2, together with W-ALL and SEED, exclude every all-single-letter item-(iii) word uniformly in p. T3 removes all count hypotheses from the lifted-system contradiction. For item (iii), the remaining work is then establishing (L), via seeds or certification, for words with excess. None of the targets proves NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson, and none claims to.
