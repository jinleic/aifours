# Referee report: `proof-REFLHI-arcs-v5.md` (4e463746…cff1c), read under errata 1 (512e1d9e…), 2 (b4451461…) and 3 (380106c9…)

**Scope.** This review covers only the frozen scope:
- §1 Lemma W and Facts 2.1–2.2.
- §2 arc systems, Lemma 2.1, ARC+ and Lemma SEG.
- §3 labels, Lemmas 3.1, 3.2, BAL and the realisation rule as replaced by e5.
- §4 R = p data, Theorem FP, and v3 Corollary FP-1 with its supporting v3 L94–137.
- §5 K2P+ and IIIb-X.
- §7 ETA.

**Method.** The imports H0, P0, AR, RED, SMALLK, FEW and CD are taken at their parent-accepted scopes and not re-proved. Every check below was done by hand from the written text. I used no tools, no computation and made no edits.

## A. Disposition

**Overall: 0 FATAL / 0 MAJOR / 11 MINOR. No REJECT.**

Every in-scope claim is correct at the scope stated in §C. Each ACCEPT-WITH-FIXES rests on a step that the source asserts but does not write out. I verified each such step (§E), and the acceptance covers the text with the §B lines added. A proof outline alone is not accepted.

| Claim | Disposition | Findings |
|---|---|---|
| Lemma W | ACCEPT | — |
| Fact 2.1 | ACCEPT | — |
| Fact 2.2 | ACCEPT | — |
| Lemma 2.1 | ACCEPT | — |
| Lemma ARC+ (incl. ARC) | ACCEPT-WITH-FIXES | F1, F2 MINOR |
| Lemma SEG (+e1) | ACCEPT-WITH-FIXES | F3 MINOR |
| Lemma 3.1 | ACCEPT-WITH-FIXES | F4 MINOR |
| Lemma 3.2 (balanced kill) | ACCEPT-WITH-FIXES | F5 MINOR |
| Lemma BAL | ACCEPT-WITH-FIXES | F6 MINOR |
| Realisation rule (e5 text) | ACCEPT | F7 MINOR (printed L107–108 superseded) |
| §4 data + Theorem FP (v5) | ACCEPT-WITH-FIXES | F8 MINOR |
| v3 Fact 4.2, Thm FP, Lemma 4.3, Cor. FP-1, L137 | ACCEPT | — |
| Theorem K2P+ (+e2) | ACCEPT-WITH-FIXES | F9 MINOR |
| Corollary IIIb-X | ACCEPT-WITH-FIXES | F10 MINOR |
| Theorem ETA | ACCEPT-WITH-FIXES | F11 MINOR |

## B. MINOR findings and minimal repairs

**F1 (ARC+ (i)/(ii): several segments in one gap).** The phrase "the same argument applies to each" does not say why ε_j is the base label. Add:

> A later segment Σ′ in the same base gap is consecutive and disjoint from Σ. So it lies before c_1 or after c_(2t′) of Σ, that is, in an outer sub-gap, which keeps the base label. Hence (i) and the ±W formula of (ii) apply to Σ′ with the same ε.

**F2 (ARC+ (iii)).** Add three facts:
- m_b ≥ 1.
- Each U_j ∋ 0 (take t′_j = 0), so every CD summand is nonempty.
- The window is nonempty since E± ≥ 0. If either count is clipped at p, the other count being ≥ 1 already gives a meeting point.

**F3 (SEG).** Erratum e1 is in force.
- U″ is defined as a set of sums (2W-values), but the induction hypothesis is about W-sets. Write 2U″ := {∑_(J″) δ_j}; halving is a bijection, so the sizes agree.
- Apply the hypothesis to blocks 3..b′. That segment has b′−2 ≥ 1 blocks, deltas δ_3..δ_(b′−1), and t−1 intervals.
- Note that J′ = {2} and J′ = {1,2} are realised by c = (2,3) and c = (1,3), which need block 3; it exists since b′ ≥ 3.

**F4 (3.1).**
- An arc choice must have ∑c_i ≥ 2; otherwise it is not an arc system.
- The symbol b_i (blocks of M_i) clashes with b_t (the ρ_−1 count of R_t). Rename one of them.

**F5 (3.2).** Add:

> Segments insert an even number of single-block arcs inside one M_i. So every parity of c_i, and hence z and T, is unchanged. Both range conditions are monotone in m, so it suffices to check them at m_b and at m_b + ∑t_j.

**F6 (BAL).** The bound t ≤ q−1 is asserted without proof. Add:

> S(q−1) = T − z_i d(N_i) ≥ T − d > (T−d)/2, so t ≤ q−1. If q = 1 then |T| = d, and if d = 0 then T = 0. So T > d forces q ≥ 2. "Say T > d" is WLOG by z → −z.

**F7 (realisation).**
- The printed v5 L107–108 offers no move when M_j is covered by arcs of ≥ 3 blocks; for example, M_j is a single 3-block arc. Erratum e5 restricts to singletons and pairs and is correct.
- K2P+(f) adds a singleton on an unused block of M_i even if M_i already has a singleton. This departs from e5's priority order, but the move is itself valid: the parity flips, the count rises by 1, and no pair is lost.
- Repair e5's wording: "each of the three moves realises the change when applicable; the order given is one sufficient choice."

**F8 (§4, FP).**
- (a) State the hypothesis "w ∈ (S), R = p, w avoids".
- (b) Spell out the use of BAL: apply it at i = n to c^(n) (c_n = 0, all other c_j = 1, sum p−1 even). The result is c^(i′), i.e. the labelling z^(i′), with |T| ≤ 1. Since T is odd, |T| = 1.
- (c) For B = 0, add the one line T(n) = (p+1)/2 − (p−1)/2 = 1 (as in v3 L119–120).
- (d) The subsumption sentence and e8 are not audited here.

**F9 (K2P+).** Erratum e2 is in force; also directly, at p = 5, H ≤ (p−3)/2 = 1 contradicts H−δ ≥ 2. Write out the two inequalities of step (d):
- **Π\* ≤ N0.** From 2κ ≥ R+1 and 2⌈(R−d)/4⌉ ≤ (R+3)/2 we get N0 ≥ (R+7)/2. Also Π\* ≤ p+1−R/2. So N0 − Π\* ≥ R−p+5/2 > 0.
- **N0 + Π\* ≤ k−p+5+d/2.** Substituting 2κ = k−2p+R gives N0+Π\* = k−p+5+[R − 2⌈(R−d)/4⌉ − ⌈R/2⌉]. The bracket is ≤ R − (R−d)/2 − R/2 = d/2.

In step (f), the final arc count is N0 or N0+2. So m ∈ {m_lo+1, m_lo+2} ⊆ [m_lo, m_hi] by (a). The printed range [N0−2, N0+2] is a harmless superset.

**F10 (IIIb-X).**
- State the ambient hypotheses: length 4p−2 over D_(2p), all rotation letters ρ_x with x ≠ 0, all maximal constant reflection blocks odd.
- B = 0 is superfluous, since K2P+ holds for any B.
- k = 2p+1 is a consequence of (0.1), not an extra hypothesis.
- Write the check 2p+1 ≥ 3κ+3 ⇔ p ≥ 7.

**F11 (ETA).**
- (a) Notation and citation.
  - "G_(m\*)" is undefined; read it as γ_(m\*).
  - "Fact 2.1 gives" is a mis-citation. The evaluation is direct: γ_(m\*)(x) = min(H+⌊R/2⌋, x−⌊R/2⌋, ⌊x/2⌋), because x−κ+m\*−1 = x−⌊R/2⌋ and p−m\* = H+⌊R/2⌋.
- (b) Write both endpoints of I(P). With x = D_P:

  | Case | I(P) |
  |---|---|
  | R even, 0 ≤ x ≤ R | {x−R/2} |
  | R odd, 1 ≤ x ≤ R−1 | {x−⌈R/2⌉, x−⌊R/2⌋} |
  | R odd, x = 0 | {−⌊R/2⌋} |
  | R odd, x = R | {⌊R/2⌋} — misses x−⌊R/2⌋ |

  The last row is why R_1 must be nonempty with R_1 ∉ P when R is odd.
- (c) Put in the statement: (S), B = 0, and R ≤ 2κ+1 (equivalently m\* ≥ 1). Also require the indexing to start at a nonempty R_1 when R is odd, the parts Z_i to be nonempty, and η(Z) to mean the set of residues.

## C. Exact accepted scopes

**Ambient conditions (every claim):**
- p ≥ 5 prime.
- Cyclic w of length 4p−2 over D_(2p).
- All rotation letters in one pair {ρ_x, ρ_−x}, x ≠ 0, normalised to x = 1 and A ≥ B.
- Every maximal cyclic constant reflection block odd, so o_F = k and β ≡ 0.
- F ≥ 1 and R ≥ 1.
- The maximal decomposition, so empty runs are genuine.
- No purity condition, no B < κ, and no restriction on reflection values.

**Per claim:**
- **W, 2.1, 2.2, 2.1-Lemma, ARC+, SEG, 3.1, 3.2, BAL:** words in (S). Facts 2.2 and 3.2 apply under avoidance. The e5 rule applies only to arc choices made of singletons and pairs.
- **FP (v5 and v3):** avoiders in (S) with R = p, for arc choices with m_0 ≤ m ≤ m_1 and |T| = 1.
- **FP-1 (v3):** the ambient conditions plus:
  - exactly R = p rotation letters;
  - (K) κ ≤ (p−3)/2 + ⌈(p−1)/4⌉;
  - either ∑(ν_i−1) − max(ν_i−1) ≥ (p−1)/2, or [B = 0 and ∑(ν_i−1) − min(ν_i−1) ≥ (p−1)/2].

  The L137 consequence requires B = 0, (K), and at least (p−1)/2 non-constant maximal reflection runs.
- **K2P+:** the ambient conditions (any B, purity or values) plus k ≥ 2p+1 and k ≥ 3κ+3. It is vacuous at p = 5. For avoiders it is equivalent to 2κ ≥ R+1 and H−(R−p) ≥ 2.
- **IIIb-X:** p ≥ 7, R = p, κ = (p+1)/2, so k = 2p+1. It holds for any B.
- **ETA:** (S), B = 0, R ≤ 2κ+1. It is a necessary condition on avoiders and excludes nothing by itself.

## D. Not audited; open

**Not audited:**
- Lemma 1.1.
- Theorem SEG, SEG-p, SEG-num, MID, TOP.
- The §4 subsumption sentence (e8), the §6 closing statement (e7), §8, and errata e3, e4 and e6.
- e5's claims about how SEG and MID use the rule.

No in-scope claim uses any of these as a premise. No novelty or priority assessment is made.

**OPEN:** REFL(p), REFL-HI(p), RES-HI(p), the reflection half of INV\*(p), rotation rigidity, INV\*(p), and ordered Olson for D_(2p). The one-pair and all-odd restrictions are essential to every claim here.

## E. Verification record

**E1. Lemma W.**
- In H0, E+(P) = D_P + B = A_P + B_(P^c) and E+(P^c) = E−(P).
- Also m(P^c) = m(P) and β(P^c) = β(P). Boundary blocks are maximal constant blocks, hence odd, so β = 0.
- Therefore I(P) = [−γ_m(E−), γ_m(E+)].
- Only the "if" direction is claimed. ✓

**E2. Fact 2.1.** γ_m(E) = ⌊E/2⌋ iff ⌊E/2⌋ ≤ p−m and ⌊E/2⌋ ≤ E−κ+m−1. The second inequality is equivalent to ⌈E/2⌉ ≥ κ+1−m. ✓

**E3. Fact 2.2.**
- (0.1) with o_F = k gives R = 2p−k+2κ.
- P0 with e_F = 0 gives o_R ≥ k−2κ = 2p−R. Odd runs are nonempty, so R ≥ 2p−R.
- An odd run has at most R−(2p−R−1) letters. An even or empty run has at most R−(2p−R).
- Consequences: d ≤ 2δ+1 and q ≥ 2p−R. ✓

**E4. Lemma 2.1 (independent endpoints, exact interval count).**
- For arbitrary, independent a_i ∈ X_i and b_i ∈ Y_i, the run interval (a_i, b_i] contains the IN gap. The interval (b_i, a_(i+1)] contains the run after Y_i.
- So the m intervals are nonempty and separated by at least one run of [k]. Empty runs count as elements, so m(P) = m exactly, and ∅ ≠ P ≠ [k].
- The non-gap runs in P are empty arc-internal runs, so E+(P) = E+.
- The boundary blocks are S_(a_i) and S_(b_i), and θ telescopes. ✓

**E5. ARC+.**

*(i) Arc count and E+.*
- Σ is consecutive and disjoint from the base arcs, so it lies in one gap.
- In the role sequence Z, c_1, …, c_(2t′), Z′ the roles alternate. Since 2t′ is even, Z′ and all later arcs keep their roles.
- Sub-gap labels alternate, beginning and ending with the old label.
- Relabelled runs (IN→OUT or OUT→IN) lie in some (c_(2s−1), c_(2s)], which is internal to Σ, so they are empty. Hence E+ is preserved. Every gap still contains the run after its arc.

*(ii) Interval count and u-value.*
- In an IN gap, (a_i, c_1], (c_2, c_3], …, (c_(2t′), b_i] give t′+1 intervals and add W to u.
- In an OUT gap, (c_1, c_2], …, (c_(2t′−1), c_(2t′)] give t′ new intervals and add −W.
- Base endpoints stay free, and single-block arcs have forced endpoints. All choices are independent, so the u-set contains the full sumset.

*(iii) Uniform window.* For every realised m in [m_b, m_b+∑t_j], Fact 2.1 gives the same window [−⌊E−/2⌋, ⌊E+/2⌋]. The clipped CD count plus the window count is at least p+1 (see F2). The common residue is the u-value of an actual configuration whose window is that uniform one, so Lemma W applies. ✓

**E6. SEG.**
- 2W = ∑_(j∈J) δ_j, and the map J ↔ c is bijective onto sets J with at most t intervals.
- Base cases: t = 0 or b′ = 1 give {0}; b′ = 2 with t ≥ 1 (e1) gives {0, δ_1/2}.
- Induction step: |A| ≥ 3; when δ_1+δ_2 = 0 this uses that p is odd. Also J′ ∪ J″ has at most t intervals.
- Checked edge cases:
  - t = 1 (U″ = {0});
  - b′ = 3 (J″ ⊆ ∅);
  - a final singleton interval {b′−1}, realised by (b′−1, b′);
  - saturation: |U″| ≥ p gives |A+U″| = p.
- The remark after SEG is correct but weak. The guaranteed gain is min(p−1, 2t, b′−1), so each unit of t adds 2, except possibly the last, which adds 1. ✓

**E7. Lemma 3.1.**
- Passing M_j crosses c_j arcs with alternating roles, so labels follow z up to sign.
- E+ = ∑_IN a + ∑_OUT b = (R±T)/2.
- T ≡ R (mod 2), so these values are integers. ✓

**E8. Lemma 3.2.**
- The ceiling condition at E_min implies it at E_max, and the floor condition at E_max implies it at E_min.
- ⌊E+/2⌋+⌊E−/2⌋ ≥ ⌈R/2⌉−1: it equals (R−1)/2 for R odd and is R/2 or R/2−1 for R even.
- Adding Π_need gives ≥ p−1. ✓

**E9. BAL.**
- Flipping the parities of c_i and c_(i+t) flips z exactly on N_(i+1..i+t), so T becomes T−2S(t).
- For the least such t: S(t−1) < (T−d)/2 ≤ S(t) ≤ S(t−1)+d < (T+d)/2, so |T−2S(t)| ≤ d.
- t ≥ 1 because S(0) = 0 < (T−d)/2; t ≤ q−1 by F6. The cases q = 1 and d = 0 are trivial. ✓

**E10. e5.**
- An arc meeting M_j lies inside M_j.
- With no singleton and no unused block, every block of M_j lies in a pair, and there is at least one pair.
- Each move changes the count by ±1, costs at most one pair, and keeps the singleton/pair form. ✓

**E11. §4 data and FP.**
- Data: with δ = 0, every nonempty run has one letter, q = p, k = p+2κ, g_E = 2κ, d = 1, and T is odd.
- r = ⌈(p−1)/4⌉ = ⌊(p+1)/4⌋: both equal a for p = 4a+1 and a+1 for p = 4a+3. For E = (p±1)/2, the minimum of ⌈E/2⌉ and the maximum of ⌊E/2⌋ are both r.
- So Fact 2.1 holds for both E iff κ+1−r ≤ m ≤ p−r. The window sum is (p−1)/2 = Π_need.
- FP follows from 3.2.
- Balanced labelling: by F8(b). Independently, v3 L4.3 sets U(n) = (−1)^n T(n). Steps are ±2 through odd integers, and U(n+p) = −U(n), so U hits ±1. For B = 0, T(n) = 1. ✓

**E12. v3 FP-1.**
- Normalisation preserves R = p, block parity, every ν_i, and "all rotation letters equal".
- Under avoidance there are exactly p maximal reflection runs M_i, each an arc with ν = ν_i. Setting c_i = 1 for i ≠ n and c_n = 0 gives 2m = p−1 and the labelling z^(n).
- m = (p−1)/2 ≥ κ+1−r ⇔ (K); also m ≥ 1 and m ≤ p−r.
- The max-version works with any balanced n. For B = 0 every n is balanced, so take n = argmin ν.
- L137: if some run has ν = 1 it is the argmin; otherwise ∑−min ≥ p−1.
- Edge cases: at p = 5, (K) reads κ ≤ 2 and m = 2 uses 4 arcs. At p = 7, (K) reads κ ≤ 4.
- Contradiction with FP. ✓

**E13. K2P+.**

*Setup.* For an avoider, δ = R−p ≥ 0 and d ≤ 2δ+1. From k = 2p−R+2κ:
- k ≥ 3κ+3 ⇔ H−δ ≥ 2;
- k ≥ 2p+1 ⇔ 2κ ≥ R+1;
- k ≡ R (mod 2).

*Steps.*
- (a) m_hi−m_lo = H − (⌊(R+d)/4⌋ − ⌈(R−d)/4⌉). The bracket is an integer ≤ d/2. So m_hi−m_lo ≥ H−⌊d/2⌋ ≥ H−δ ≥ 2.
- (b) m_lo ≥ (R+3)/4 > 0.
- (c) Pair supply: within each M_i the pairs (1,2), (3,4), … are arcs with ν = 2. Their number is ≥ g_E/2 ≥ (k−R)/2, using q ≤ R; this is an integer. Then (k−R)/2 ≥ Π\* ⇔ k ≥ 2p+2−[R odd], which holds by k ≥ 2p+1 together with parity.
- (d) κ ≥ (p+1)/2 gives H ≤ (p−3)/2. So d ≤ 2H−3 ≤ p−6 ≤ 2p−12. The inequalities are as in F9.
- (e) Block budget: N0+Π\* ≤ k−1 blocks are used, so a block stays unused.
- (f) Apply BAL at that i. The move at i is free, and the e5 move at i′ ≠ i costs at most one pair. So gain ≥ Π_need and m ∈ {m_lo+1, m_lo+2}.
- (g) ⌈E_min/2⌉ ≥ ⌈(R−d)/4⌉ = κ+1−m_lo, and ⌊E_max/2⌋ ≤ ⌊(R+d)/4⌋ = p−m_hi. Lemma 3.2 applies. The case R = 0 is covered by AR.

*Boundary instance.* At p = 7 the theorem forces δ = 0, κ = 4, k = 15. Then m_lo = 3, m_hi = 5, N0 = 8, Π\* = 4, and N0+Π\* = 12 ≤ 14. ✓

**E14. IIIb-X.** (0.1) gives k = 2p+1, and 2p+1 ≥ (3p+9)/2 ⇔ p ≥ 7. K2P+ then applies. ✓

**E15. ETA (offset, sign, R_1 exclusion).**
- m\* ≥ 1 ⇔ R ≤ 2κ+1. Also 2m\* ≤ k, since k−2m\* = 2p−2−[R odd].
- Take a_i ∈ Z_(2i−1) and b_i ∈ Z_(2i) in linear order from S_1. The intervals (a_i, b_i] are nonempty and separated, and the wrap-around gap (b_(m\*), a_1] contains R_1. So m(P) = m\* and P is proper.
- With B = 0, E+ = D_P = ∑_(i)(ρ_(b_i) − ρ_(a_i)), where ρ_j are the prefix sums of r.
- Sign check: u_P − D_P = ∑[y_(a_i)/2 + ρ_(a_i)] − ∑[y_(b_i)/2 + ρ_(b_i)] = ∑(η_(a_i) − η_(b_i)).
- By the F11(b) table, D_P − ⌊R/2⌋ ∈ I(P). For odd R this needs D_P ≤ R−r_1 ≤ R−1. So avoidance forbids the value −⌊R/2⌋ for this sumset.
- Clipped CD: if ∑|η(Z_i)| − 2m\* + 1 ≥ p the sumset is all of Z_p, a contradiction. Hence ∑|η(Z_i)| ≤ p+2m\*−2. ✓
