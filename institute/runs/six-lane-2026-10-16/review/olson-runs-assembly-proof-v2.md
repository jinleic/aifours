# RUNS(p) after Lemma GC: exact dependency/quantifier map and conditional citation assembly (v1)

Author: OlsonRunsAssembly (sub-agent; math-2 ordered-Olson slot).  Written after host clock 2026-10-18T00:34:20-0700.
Status: [W] assembly by the assembler; NOT independently reviewed; NOT a parent, theorem or gate verdict.  Lane O was only read.
Version v2 (same session): = v1 (R/olson-runs-assembly-proof-v1.md, sha256 153dff8a82786d04f8a9184f1f42cedee6dc6517b606593d91e1c90cb01b7bef,
never sent to a reviewer) with Remark (2) after Theorem C corrected (v1 misattributed the o_F <= p / o_F >= p + 1 split of the
branches) and the no-census sentence added to Sec. 0.  No other change.
Paths are relative to O := mathematics/evidence/six-lane-20261016/olson/ unless prefixed R/ (R := institute/runs/six-lane-2026-10-16/
review/).  "Ln" = 1-based index in text.split('\n') of the cited file; SHA-256 pins in Sec. 7.  "Solvable" = has an identity
2p-subword (2p letters in increasing index order whose ordered product is 1).

## 0. Result

Fix a prime p >= 5.  Assume
 (GC)  Theorem NMH-iii of inverse-run-count/mixdef-high/c6/proof-GC.md (L109-110): every NMH word with R <= 2p - 3 is solvable;
 (IMP) the load-bearing imports U2-U10 of Sec. 6, which have not been reviewed by both model families.
Then NMH(p), MIX_DEF_HIGH(p), MIX_DEF(p), RUNS(p) and INV_Res(p) hold, every inherited avoider in RGR_(4p-2)(p) has B = kappa = 0
after normalisation, and by Theorem DR-Res every word of RGR_(4p-1)(p) is solvable (Theorems A-C, Corollaries B', D, E below).
This is NOT ordered Olson for D_(2p).  Corollary DR' (proof-DR.md L42-58) additionally needs INV*(p) (proof-DR.md L44): (a) the
rotation values of every avoider of length 4p-2 lie in one set {rho_x, rho_-x}, x != 0, and (b) every maximal cyclic reflection
run of such an avoider is constant (inverse-parity/mixdef-low/c2/obligations-after-PAR.md L54-57).  Both halves are open
(inverse-parity/mixdef-low/c2/invstar/results.md L67-71); every statement below assumes an RGR word.
Closing item (iii) alone does not close RUNS(p): RUNS(p) also rests on C2 (R >= 2p - 2), Theorem ALT (k = 2p - 1), the B = 0
lemmas, the k >= p+1 extension of Theorem K0, Theorems KB, KBH and M, and the OR/M0 transfers.  All are mapped below.
No finite computation, census or certificate table is a premise of any step (the cited files label theirs as aids).

## 1. Words, parameters, statements

1.1 RGR_N(p) (proof-DR.md L11-14): words of length N over D_(2p) whose rotation letters lie in one set {rho_x, rho_-x}, x != 0
(normalised x = 1), and whose maximal cyclic reflection runs are constant.  With F, R >= 1 the word is a cyclic alternation
R_1 S_1 ... R_k S_k of k nonempty rotation runs and k nonempty constant reflection runs S_j = sigma_(y_j)^(l_j).  Notation
(inverse-run-count/proof-RUNS.md L11-15): a_t, b_t = numbers of rho_1, rho_(-1) in R_t; r_t = a_t + b_t; d_t = a_t - b_t; A, B,
R = A + B, D = A - B; F = sum l_j; H = sum floor(l_j/2); o_F = #{j : l_j odd}; kappa := p - 1 - H.  A run is pure if a_t b_t = 0
and a (1,1)-pair if a_t = b_t = 1; the word is all-odd if every l_j is odd.  An avoider has no identity 2p-subword.  For every
word of length 4p - 2 with F, R >= 1:
   F = o_F + 2H,    R = 2p - o_F + 2 kappa,    o_F <= k <= min(R, F),    k <= 2p - 1.                                   (1.1)
(l_j = 2 floor(l_j/2) + [l_j odd]; R = 4p - 2 - F; every run is nonempty, so 2k <= F + R = 4p - 2.)
1.2 Normalisation N (inverse-parity/proof-PAR-K0.md L48-50): rho_v -> rho_(-v), sigma_v -> sigma_(-v) preserves avoidance, RGR,
k, every l_j (hence o_F, H, kappa) and the five inherited conditions, and swaps A and B.  WLOG A >= B.
1.3 Inherited (proof-INV-reduction.md L14-16): (E) R <= 3p - 2; (P) F + sum_i floor(r_i/2) <= 3p - 2; (V) R + H <= 3p - 2;
(Pairs) H <= p - 1; (D0) a_i, b_i <= p - 1 for every rotation run.  Equivalently (proof-PAR-K0.md L52-53): (Pairs) <=> kappa >= 0;
(V) <=> kappa <= o_F - 1; (P) <=> R + o_R >= 2p (o_R = number of odd rotation runs).
1.4 Windows: Lemma HW (inverse-run-count/README.md L17-36) = Lemma H (proof-PAR-K0.md L18-44).  Only the direction "phi(P) is
congruent mod p to an element of I(P) for ONE pattern P => solvable" is used; in particular a full window (|I(P)| >= p) makes
the word solvable (R/olson-kbh-codex-review-v1.note.md L12-37).
1.5 Statements (p a fixed prime >= 5).
 NMH(p) (inverse-run-count/mixdef-high/README.md L25-26): every all-odd RGR word of length 4p - 2 with p + 1 <= k <= 2p - 2,
   every run pure or a (1,1)-pair, 1 <= B <= kappa - 1 and B <= A <= 2p - 1 is solvable.
 NMH-iii(p) (mixdef-high/c6/proof-GC.md L109-110): every NMH word with R <= 2p - 3 is solvable.                [hypothesis (GC)]
 MIX_DEF_HIGH(p) (mixdef-high/README.md L13-14): every RGR word of length 4p - 2 with F, R >= 1, A >= B, 1 <= B < kappa and
   o_F >= p + 1 is solvable; no inherited hypothesis.
 MIX_low(p) (inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md L61-64): every RGR word of length 4p - 2 with all k reflection
   runs odd, k <= p, A >= B >= 1 and B < kappa <= k - 1 is solvable.                                     [Theorem M, accepted]
 MIX_DEF(p) (inverse-run-count/mixdef/README.md L10-11): every RGR word of length 4p - 2 with all reflection runs odd,
   1 <= B < kappa and B <= A is solvable (any k, no inherited hypothesis).
 RUNS(p) (proof-INV-reduction.md L41-43; inverse-run-count/README.md L10-13): every inherited avoider w' in RGR_(4p-2)(p) with
   F, R >= 1 has k <= p.
 PAR(p) (proof-INV-reduction.md L42): every inherited avoider in RGR_(4p-2)(p) with k <= p has all 2k runs odd.
   [Theorem P, accepted: proof-R4-closure-r1.md L84-94]
 INV_Res(p) (proof-INV-reduction.md L17, L44): every inherited avoider in RGR_(4p-2)(p) has all runs odd and k <= p.
 RGR-LONG(p): every word of RGR_(4p-1)(p) is solvable.  Theorem DR-Res (proof-INV-reduction.md L19-37): INV_Res(p) => RGR-LONG(p).
 INV*(p) (proof-DR.md L44): every avoider of length 4p - 2 over D_(2p) lies in RGR_(4p-2)(p).
 OO(p): ordered Olson for D_(2p) (no avoider of length 4p - 1).  Corollary DR' (proof-DR.md L42-58): INV*(p) + RGR-LONG(p) =>
   OO(p) (DR' uses INV(p) only through the conclusion of Theorem DR; obligations-after-PAR.md L14-18).

## 2. Three elementary facts (proved here)

**Fact Z (avoiders of length 4p - 2).**  Let w in RGR_(4p-2)(p), F, R >= 1, A >= B, be an avoider.  Then (i) A, B <= 2p - 1;
(ii) B <= kappa; (iii) o_F >= 2 kappa - B + 1 >= kappa + 1 >= 1, in particular (V) holds; (iv) if B <= kappa - 1, o_F >= kappa + 2.
Proof.  (i) 2p letters rho_1 (resp. rho_(-1)) in increasing order have product rho_(2p) = 1 (resp. rho_(-2p) = 1).  (ii) The
empty pattern has I(empty) = [-min(p, A - kappa - 1, floor(A/2)), min(p, B - kappa - 1, floor(B/2))] and phi(empty) = 0
(proof-PAR-K0.md L22-23; proof-RUNS.md L59-60); if A, B >= kappa + 1 both minima are >= 0, so 0 is in I(empty) and w is
solvable.  Hence B = min(A, B) <= kappa.  (iii) By (1.1) and (i), 2p - o_F + 2 kappa = A + B <= 2p - 1 + B, so
o_F >= 2 kappa - B + 1 >= kappa + 1 by (ii), and kappa >= B >= 0.  (iv) 2 kappa - B + 1 >= kappa + 2 iff B <= kappa - 1.  []

**Fact T (transfer audit of the two reductions).**
 (OR) Lemma OR (inverse-parity/proof-PAR-Kplus-partial-r2.md L24-35; proof-RUNS.md L366-375) needs o_F >= 1 (Fact Z(iii)).  The
   merged word w~ has k~ = o_F reflection runs, all odd, nonempty runs, the same R, F, A, B, H, kappa (hence the same o_F and D),
   and if w avoids then w~ avoids.  Since R and H are unchanged, (E), (V), (Pairs) hold for w~ whenever they hold for w.  (P) and
   (D0) can FAIL for w~ (Kplus-r2 L37-42: a segment may contain >= p equal rotations), and k~ <= k may be < p + 1.  Below, no
   statement applied to a merged word uses (P), (D0), or any inherited condition except through parameters that OR keeps.
 (M0) Lemma M0 (proof-RUNS.md L402-414; independently re-derived in both PAR-closure reviews, R/olson-par-mixlow-parent-verdict.md
   L16, L26), applied to a run with a_t, b_t >= 1 and r_t >= 3, keeps k, every d_t, every reflection parity and phi, maps
   (A, B, R, H, kappa) to (A - 1, B - 1, R - 2, H + 1, kappa - 1), keeps kB := kappa - B and D, keeps every run nonempty, and
   preserves avoidance.  (P) may fail (proof-RUNS.md L413); no inherited condition is used after M0 below.  Iteration stops
   with every run pure or a (1,1)-pair (a run with a_t, b_t >= 1 and r_t <= 2 is a (1,1)-pair); it stops because B drops.
 (N) as in 1.2.

**Fact K (MIX_low's hypothesis kappa <= k - 1 is automatic after the trivial cut).**  If v is an all-odd RGR word of length
4p - 2 with A >= B, B <= kappa - 1 and A <= 2p - 1, then kappa <= k - 2.
Proof.  o_F = k, so R = 2p - k + 2 kappa by (1.1); A = R - B <= 2p - 1 gives 2 kappa - B <= k - 1, and B <= kappa - 1 gives
2 kappa - B >= kappa + 1.  []  (Theorem M's Step 0 records the same inequality 2g + B <= k - 1, g = kappa - B:
proof-R4-closure-r1.md L66-67.)

## 3. Dependency and quantifier map

Each row lists the input class (only the listed hypotheses), the imported statement with its exact hypotheses, and the word it
is applied to.

3.1 NMH(p).  Input: all-odd; p + 1 <= k <= 2p - 2; every run pure or a (1,1)-pair; 1 <= B <= kappa - 1 (kB >= 1);
B <= A <= 2p - 1; no inherited condition.  Delta0 := 2p - R = k - 2 kappa (by (1.1)).
 N1  R >= 2p - 2.  Theorem FW+ (mixdef-high/c2/proof-C2.md L119-123).  Hypotheses: all-odd, k >= p + 1, pure/(1,1) runs,
     R >= 2p - 2, A, B <= 2p - 1, min(A, B) <= kappa (here min(A, B) = B <= kappa - 1).  Inside: R = 2p - 2 Lemma R2 (C2 L17-18:
     all-odd, k >= p + 1, any letters, any B); R in {2p - 1, 2p} Theorem FWH (a), (b) (mixdef-high/proof-MH.md L56-59: all-odd,
     any letters, any B, k >= 3 resp. k >= 6; here k >= p + 1 >= 6); R >= 2p + 1: FWH (c) (MH L60: k >= 6, every
     |d_u| <= 2p - k + 1) or, in the integer complement |d_u| >= 2p - k + 2 for some u, Lemma BR (C2 L61-63: k >= p + 1, pure/(1,1),
     R >= 2p + 1, A, B <= 2p - 1, min(A, B) <= kappa).  Conclusion: a full window; solvable by 1.4.
 N2  R <= 2p - 3.  Theorem NMH-iii (GC L109-116).  Its setting is mixdef-high/c3/proof-C-r1.md L19-21 (all-odd, k >= p + 1,
     pure/(1,1) runs, 1 <= B <= kappa - 1, B <= A <= 2p - 1, R <= 2p - 3), identical to N2's input; it contains the k = p + 1
     (ZSI-B) words and uses no region, count condition or finite certificate.  Lemma GC uses only Delta0 >= 3 and k >= 7 (GC
     L103-104); here Delta0 >= 3 and k = 2 kappa + Delta0 >= 2(B + 1) + 3 >= 7.  Chain inside (GC L111-116): Lemma GC ->
     Lemma GS (b) with Lemma NW (mixdef-high/c6/proof-SEEDG-r2.md L80-99; accepted) -> Corollary (a)/(b) of
     mixdef-high/c6/proof-A0-r1.md L92-103, through Theorem C0-all (L63-64), whose import Lemma C0W is accepted
     (R/olson-c6-uniform-parent-verdict.md L17).
     Coverage of 3.1: R >= 2p - 2 or R <= 2p - 3.
3.2 MIX_DEF_HIGH(p).  Input: F, R >= 1; A >= B; 1 <= B < kappa; o_F >= p + 1; no inherited condition.  Route: trivial cut
(A >= 2p; proof-RUNS.md L364); else Lemma OR -> w~ with k~ = o_F in [p + 1, 2p - 1] (by (1.1)); if k~ = 2p - 1 Theorem ALT
(proof-RUNS.md L36-37: every RGR word of length 4p - 2 with k = 2p - 1; nothing else assumed); else iterate M0 -> w^ with
k^ = k~ in [p + 1, 2p - 2], all-odd, pure/(1,1) runs, kappa^ - B^ = kappa - B >= 1, A^ - B^ = A - B >= 0, A^ <= A <= 2p - 1.
If B^ >= 1, w^ is an NMH word: 3.1.  If B^ = 0 (all letters rho_1, kappa^ = kappa - B >= 1, R^ = A^): R^ <= 2p - 2 Theorem C0-B'
(proof-RUNS.md L318-320: ANY RGR word of length 4p - 2, all letters rho_1, all-odd, R <= 2p - 2, kappa >= 1); R^ = 2p - 1
Lemma A1 (L348-350: same with R = 2p - 1; a full window); R^ >= 2p the trivial cut.  (Alternatives with other review status:
R^ = 2p - 2 Lemma R2; R^ = 2p - 1 FWH (a).  C0-B' is load-bearing for R^ <= 2p - 3.)  Source of this reduction:
mixdef-high/README.md L18-23 and proof-MH.md L12-13, re-proved as Theorem B.
3.3 MIX_low(p): Theorem M (accepted).  By Fact K its hypothesis kappa <= k - 1 is automatic when A <= 2p - 1.
3.4 MIX_DEF(p): trivial cut; all-odd gives o_F = k; k <= p Theorem M (Fact K); k >= p + 1 MIX_DEF_HIGH(p).
3.5 RUNS(p): Theorem C, branches C1-C6; table and inherited-condition audit in Sec. 5.
3.6 INV_Res(p) = RUNS(p) + PAR(p) (Theorem P).   3.7 RGR-LONG(p) <= INV_Res(p) (DR-Res).
3.8 OO(p) <= INV*(p) + RGR-LONG(p) (DR'); INV*(p) is open.

## 4. Conditional theorems and proofs

Throughout p >= 5 is prime and (GC), (IMP) are assumed; every step names the import it uses.

**Theorem A (NMH(p)).**  Every NMH word is solvable.
Proof.  Let w be an NMH word.  If R >= 2p - 2, row N1: FW+ gives a full window.  If R <= 2p - 3, row N2: w is in the setting of
c3/proof-C-r1.md L19-21, so Theorem NMH-iii applies.  []

**Theorem B (MIX_DEF_HIGH(p)).**
Proof.  Let w satisfy the hypotheses and suppose it avoids.  By Fact Z(i), A <= 2p - 1; o_F >= p + 1 >= 1, so Lemma OR gives an
avoider w~ (Fact T) with k~ = o_F in [p + 1, 2p - 1], all reflection runs odd, F, R >= 1 and the same A, B, kappa (1 <= B < kappa,
A >= B, A <= 2p - 1).  If k~ = 2p - 1, Theorem ALT makes w~ solvable: contradiction.  Otherwise p + 1 <= k~ <= 2p - 2; iterating
Lemma M0 (Fact T) gives an avoider w^ with k^ = k~, all-odd, every run pure or a (1,1)-pair, kappa^ - B^ = kappa - B >= 1,
A^ - B^ = A - B >= 0 and A^ <= 2p - 1.  If B^ >= 1, w^ satisfies every hypothesis of NMH(p) (p + 1 <= k^ <= 2p - 2,
1 <= B^ <= kappa^ - 1, B^ <= A^ <= 2p - 1) and Theorem A contradicts avoidance.  If B^ = 0, every letter is rho_1,
kappa^ = kappa - B >= 1 and R^ = A^; Theorem C0-B' (R^ <= 2p - 2), Lemma A1 (R^ = 2p - 1) or the trivial cut (R^ >= 2p)
contradicts avoidance.  []

**Corollary B' (MIX_DEF(p), and kappa > B for every RGR word).**  (a) MIX_DEF(p) holds.  (b) Every RGR word of length 4p - 2 with
F, R >= 1, A >= B and 1 <= B < kappa is solvable (any k, any reflection parities, no inherited hypothesis).
Proof.  (b) Suppose w avoids.  By Fact Z, A <= 2p - 1 and o_F >= kappa + 2 >= 1.  If o_F >= p + 1, Theorem B.  If o_F <= p,
Lemma OR gives an avoider w~ whose k~ = o_F <= p reflection runs are all odd, with A >= B >= 1, B < kappa and kappa <= k~ - 2
(Fact K, or Fact Z(iv)); Theorem M makes w~ solvable: contradiction.  (a) is the all-odd case of (b).  []

**Theorem C (RUNS(p)).**  Every inherited avoider w' in RGR_(4p-2)(p) with F, R >= 1 has k <= p.
Proof.  Suppose k >= p + 1.  Apply N (avoidance, the five inherited conditions, k, o_F and kappa unchanged; A >= B).  By Fact Z,
A, B <= 2p - 1, B <= kappa and o_F >= 2 kappa - B + 1 >= 1.  Since B <= kappa, exactly one of C1-C6 holds.
 C1  B = 0 < kappa.  Corollary B0 (proof-RUNS.md L377-381).  Explicitly: Lemma OR gives an avoider w~ with every letter rho_1,
     all k~ = o_F reflection runs odd, the same R and kappa >= 1.  If o_F <= p: Proposition S1' (Kplus-r2 L164-166: all-odd, all
     rho_1, k <= p, kappa >= 1, R <= 2p - 2), Lemma A1' (L207-208: R = 2p - 1) or the trivial cut (R >= 2p; A = R) applies to w~
     (Kplus-r2 L231-234).  If o_F >= p + 1: Theorem C0-B' (R <= 2p - 2), Lemma A1 (R = 2p - 1) or the trivial cut applies to w~.
     None of them uses an inherited condition of w~.  So w~ is solvable: contradiction.
 C2  B = 0 = kappa.  Theorem K0 (proof-PAR-K0.md L94-96) applied to w' itself, with the extension of proof-RUNS.md L383-389:
     K0 uses k <= p only to get R >= p (L101-102) and o_F <= p (L141); here R = 2p - o_F by (1.1) and R >= k >= p + 1 give
     o_F <= p - 1 and R >= p + 1 >= 6 (K0 needs R >= 5); o_F <= p - 1 < k gives an even reflection run (K0's "even run"); K0's
     remaining hypotheses (L145-147: (V) only as o_F >= 1, (P) as e_R <= e_F, the zero condition, kappa = 0) hold for the
     inherited unmerged word w'; Lemma BC (L57-65) has no hypothesis on k.  So w' is solvable: contradiction.
 C3  B = kappa >= 1, o_F <= p.  Theorem KB (Kplus-r2 L238-241) applied to w' itself: F, R >= 1, A >= B, B = kappa >= 1, (V),
     o_F <= p, any k, any parities; in its capped case (D0) of w', the original unmerged word (L240, L276-279).  All hold because
     w' is inherited.  Contradiction.
 C4  B = kappa >= 1, o_F >= p + 1.  Theorem KBH (kappaB-high/proof-KBH.md L10-14) applied to w': F, R >= 1, A >= B, B = kappa,
     o_F >= p + 1; no inherited hypothesis.  Contradiction.
 C5  1 <= B < kappa, o_F <= p.  Corollary RL (obligations-after-PAR.md L40-48), re-proved: Lemma OR gives an avoider w~ whose
     k~ = o_F <= p reflection runs are all odd, with A >= B >= 1 and B < kappa; (V) gives kappa <= o_F - 1 = k~ - 1 (Fact Z(iv)
     even gives kappa <= k~ - 2).  Theorem M (MIX_low(p)) makes w~ solvable: contradiction.
 C6  1 <= B < kappa, o_F >= p + 1.  w' satisfies the hypotheses of MIX_DEF_HIGH(p); Theorem B: contradiction.
Exhaustiveness: B = 0 splits into kappa >= 1 (C1) and kappa = 0 (C2); B >= 1 forces kappa >= B >= 1 and splits into B = kappa
(C3, C4) and B < kappa (C5, C6), each by o_F <= p or o_F >= p + 1.  []
Remarks.  (1) Theorem C uses no PAR statement: Theorem M is MIX_low, an ingredient of Theorem P, not a consequence of it.
Theorem P is used only in Corollary D, after RUNS (order of use: proof-INV-reduction.md L44-48).  (2) The hypothesis k >= p + 1
is used only in C2.  C1 and C3-C6 apply to every k, so every inherited avoider has B = kappa = 0 after normalisation; C2 then
excludes k >= p + 1, and Theorem K0 (k <= p) excludes an even run.  This is Theorem P's chain (proof-PAR-assembly-r2.md L48-54,
there with k <= p) extended to k >= p + 1: C1a, C3, C5 are its o_F <= p steps, C1b, C4, C6 treat o_F >= p + 1, C2 treats kappa = 0.

**Corollary D (INV_Res(p)).**  Every inherited avoider in RGR_(4p-2)(p) with F, R >= 1 has k <= p (Theorem C) and hence, by
Theorem P, all 2k runs odd.  []
**Corollary E (RGR-LONG(p)).**  By Corollary D and Theorem DR-Res (proof-INV-reduction.md L19-37), every word of RGR_(4p-1)(p) is
solvable.  []
**Non-conclusion F (OO(p)).**  Corollary DR' needs INV*(p) besides RGR-LONG(p).  INV*(p) concerns arbitrary words of length
4p - 2 (rotation values; constancy of reflection runs) and is addressed by none of the statements above, all of which assume an
RGR word.  Its only written partial results (invstar/results.md L9-18: Lemma GR0, reductions toward half (b) with rigid
rotations; unreviewed) leave both halves open.  So OO(p) is NOT established by this assembly for any prime p >= 5.

## 5. RUNS(p): branch table and inherited-condition audit

| br | B, kappa | o_F | uses k >= p+1 | result (file:L) | applied to | inherited conditions used | review status |
|---|---|---|---|---|---|---|---|
| C1a | B = 0 < kappa | <= p | no | OR + S1' / A1' / cut (Kplus-r2 L24-35, L164-234) | w~ | none on w~; o_F >= 1 (Fact Z) | Codex AWF; parent-accepted as PAR imports |
| C1b | B = 0 < kappa | >= p+1 | no | OR + C0-B' / A1 / cut (proof-RUNS L318-364) | w~ | none | no target review (U6) |
| C2 | B = 0 = kappa | <= p-1 (forced) | yes | K0 + extension (K0 L94-147; RUNS L383-389) | w' | (P) as e_R <= e_F; (V) as o_F >= 1 | K0 Codex ACCEPT; extension unreviewed |
| C3 | B = kappa >= 1 | <= p | no | KB (Kplus-r2 L238-295) | w' (w~ inside) | (V); (D0) of w' in the capped case | Codex AWF |
| C4 | B = kappa >= 1 | >= p+1 | no | KBH (KBH L10-108) | w' | none | Codex AWF |
| C5 | 1 <= B < kappa | <= p | no | OR + Theorem M (Corollary RL) | w~ | (V) (automatic, Fact Z) | M accepted; RL unreviewed |
| C6 | 1 <= B < kappa | >= p+1 | no | Theorem B: cut, OR, ALT, M0, C0-B'/A1/cut, FW+, NMH-iii | w', w~, w^ | none | U1-U6, U10 |

Inherited audit: (E) is never used; (P) only in C2, on the unmerged w'; (V) in C1 (as o_F >= 1), C2, C3, C5, and it is automatic
for avoiders (Fact Z(iii)); (Pairs) is never needed beyond kappa >= B >= 0 (Fact Z(ii)); (D0) only in C3's capped case, on the
unmerged w'.  After OR or M0 no inherited inequality is used.  Normalisation N precedes every branch.

## 6. Status of every load-bearing import; exact unresolved list

Accepted at parent level after two-family review: Theorems M and P with their chain, including Lemma M0
(R/olson-par-mixlow-parent-verdict.md L7-8, L16); canonical lifts and Lemmas TS, NW, GS of mixdef-high/c6/proof-SEEDG-r2.md, and
Theorem C0-all with its Corollary in mixdef-high/c6/proof-A0-r1.md with Lemma C0W (R/olson-c6-uniform-parent-verdict.md L11, L17).
Load-bearing and NOT reviewed by both families (each must be accepted for Sec. 0):
 U1  (GC) mixdef-high/c6/proof-GC.md: Lemma GEN, Lemma GC, Theorem NMH-iii [W]; unreviewed (a separate review desk; a parent spot
     derivation exists and is not acceptance).
 U2  mixdef-high/proof-MH.md Sec. 3, Theorem FWH (a)-(c) (L56-85): no review as a target; the C2 Codex review used it as context
     (R/olson-c2-codex-review-v1.note.md L67-68).  Hand re-derivation in the Appendix.
 U3  mixdef-high/c2/proof-C2.md, Lemma R2, Lemma BR, Theorem FW+: Codex ACCEPT only (R/olson-c2-codex-review-v1.note.md).
 U4  kappaB-high/proof-KBH.md, Theorem KBH: Codex ACCEPT-WITH-FIXES only; its fix concerned Lemma H's auxiliary statement
     (R/olson-kbh-codex-review-v1.note.md L1-10).
 U5  Corollary RL (obligations-after-PAR.md L40-48): unreviewed; re-proved as C5 from Lemma OR and Theorem M.
 U6  proof-RUNS.md: Theorem ALT (L34-52); Lemmas TL, KW (L65-100); Theorem S1 Steps 0-2 (L188-222) as used in Sec. 10; Split
     Lemma, Depth Lemma, Theorem C0-B (L250-310); Theorem C0-B' (L318-339); Lemma A1 (L348-362); Corollary B0 (L377-381); the
     kappa = 0 extension of K0 (L383-389).  Never target-reviewed: the KBH Codex review checked the bookkeeping only (its note
     L60-72).  Lemma M0 (L402-414) is accepted.
 U7  inverse-parity/proof-PAR-Kplus-partial-r2.md (Lemma OR, Proposition S1', Lemma A1', Theorem KB) and inverse-parity/
     proof-PAR-K0.md (Lemma H, Lemma BC, Theorem K0): Codex review (R/olson-parity-k0-kplus-codex-review-v1.note.md) plus a parent
     delta check; read by Claude only as reviewed imports of the PAR closure packet; no Claude target review.
 U8  inverse-run-count/README.md Sec. 2 (Lemma HW): Codex only (KBH review, item 2).
 U9  Foundations with Claude review only: proof-GR.md (Lemma GR), repr-WAS.md (Lemma WAS), proof-INV-reduction.md Sec. 1
     (Theorem DR-Res), proof-DR.md (Theorem DR, Corollary DR').
 U10 The reduction NMH(p) => MIX_DEF_HIGH(p) (mixdef-high/README.md L18-23; proof-MH.md L12-13): unreviewed as written;
     re-proved here as Theorem B.
Also used: mixdef-high/c3/proof-C-r1.md Sec. 0 (the NMH setting; Codex ACCEPT; read as an import in both uniform reviews).
Open and not addressed: INV*(p) (both halves), hence OO(p).  Not claimed: the non-inherited INV(p) of proof-DR.md L18-19 and
MIX_RUNS(p) of proof-RUNS.md L444-445 (C2 needs (P); C3's capped case needs (D0)); p = 3; formal verification; novelty or
priority.

## 7. Pins (SHA-256 at assembly time)

| file (O-relative unless R/) | sha256 | role |
|---|---|---|
| inverse-run-count/mixdef-high/c6/proof-GC.md | f968a396facf396854662cbcb566c614e7e1e1dac415ca23ae70309878998425 | (GC), U1 |
| inverse-run-count/mixdef-high/c2/proof-C2.md | 67690a03c911595df57b9a67d588eb81731c01735832cddeefa00d2c93342ab0 | FW+, R2, BR (U3) |
| inverse-run-count/mixdef-high/proof-MH.md | d742605f286d4b3e6e90c4a1d79e053a46c844bc393ee3dfc2daec728fe77012 | FWH (U2), Sec. 1 |
| inverse-run-count/mixdef-high/README.md | 91ca37169af72cc273a6d524e95e8e0e93b00780d6f01d89b65b51df369069c1 | NMH, MIX_DEF_HIGH, reduction (U10) |
| inverse-run-count/kappaB-high/proof-KBH.md | 76e32fe558f012fb9b109ebecfa72960bbb8bff9dac728391f2e899efa5df81e | KBH (U4) |
| inverse-run-count/proof-RUNS.md | e3682f4d02ab0062cddfda8d4199f4307860936581cf75b843a93e91dec40661 | ALT, TL, KW, S1, C0-B, C0-B', A1, B0, K0 ext., M0 (U6) |
| inverse-run-count/README.md | c5897ac71ecc5d400be0b1e62c48bf6f5c8e187b37c3c3b3393a5b5e0dbec3ef | RUNS target, Lemma HW (U8) |
| inverse-run-count/mixdef/README.md | a3db75defc2156b3dd580f6d9a9e46cbe4b8f7d90846d0b75c2f97740e6ae6b1 | MIX_DEF statement |
| inverse-run-count/mixdef-high/c3/proof-C-r1.md | b5eb9fa7d511447d06b9d7b8abb406fff187f186bf5ae81a72e3f1ea9077b65b | NMH setting (R <= 2p-3) |
| inverse-run-count/mixdef-high/c6/proof-SEEDG-r2.md | 353b0e95c4e58d874038a11b5864514f4049753853d355015e27ebf7330130b7 | GS, NW (accepted) |
| inverse-run-count/mixdef-high/c6/proof-A0-r1.md | fba51b126e05e865c0af50de1d2572f569e46e0a941d6b3f88d796332eb781a0 | C0-all, Corollary (accepted) |
| inverse-run-count/mixdef-high/c6/proof-C0WB-r2.md | 7900f468c3f0cb10a1c586972b784e4184bc737ce6ad9caa6710f7a6b0d036f1 | C0W (accepted) |
| inverse-parity/proof-PAR-Kplus-partial-r2.md | 8a13d98291a4514cd982a2059a9b9fd05653d190166b70c22e7f7558b8fefd04 | OR, S1', A1', KB (U7) |
| inverse-parity/proof-PAR-K0.md | 4b107fffb766855d82a1c421707d426dc7fdc0a0ece77864a73d8db1ad5f9a38 | Lemma H, BC, K0 (U7) |
| inverse-parity/mixdef-low/c2/obligations-after-PAR.md | e90342017b885d0c730ce5fb359336fa51c2a17365d8d731c77e7542ccd3ee3f | Corollary RL (U5), INV* halves |
| inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md | 4432a2d840a2651540e38d4c2b2ad102d3ba7ad21fc25f74606b1d5c9f9f8837 | Theorems M, P (accepted) |
| inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md | 0bb78d1f948e4646665ec89fbfe8048f81aa138bbd4d66af1328acbf82276648 | PAR chain, statuses |
| inverse-parity/mixdef-low/c2/invstar/results.md | 2273f4fe29c8c72cf808dfc940d1c12f1626b752838b14cca242c3fd172431d8 | INV* status |
| proof-INV-reduction.md | f11c9de18974993b1a291f7f0cb5029299d88a3902cffb531d5f59e31bd01c29 | inherited, RUNS, PAR, INV_Res, DR-Res (U9) |
| proof-DR.md | dbaa48bbd96e6d0e9c21e2a01cb5f1dbb78e5cdead550157113bd2a7cb84308d | RGR_N, INV*, DR' (U9) |
| proof-GR.md | 33621e9e51e2f4f38ad68cff2a3a467c5277a2c6dc5317e591e35600f945fc08 | Lemma GR (U9) |
| repr-WAS.md | 87d7cade40e69c11e11200ae4034c0265c98d0618f715c67fccb43b43c1f6806 | Lemma WAS (U9) |
| R/olson-par-mixlow-parent-verdict.md | c0ee2c467726abafaf50208b0c4c7b2881760fec714410bbfe59d97d6f7e42a1 | M, P accepted |
| R/olson-c6-uniform-parent-verdict.md | e5ac31d9f83ab71cda8af6c024f25d22f03f30b820089863b2a13dcde61c61ce | SEED-G r2, A0/C0-all accepted |
| R/olson-kbh-codex-review-v1.note.md | 92d0a4a5d90ecf5e80ee8a338a1e65199cd21726b505bc6b3dfeecc7e2e014ae | KBH, HW review |
| R/olson-c2-codex-review-v1.note.md | c231b4e70aac2d296d14738ca9d4e67a68797acb083ce1964e4011dd12bdb8e1 | C2 review |
| R/olson-parity-k0-kplus-codex-review-v1.note.md | 91ab54b53227acaf8be0abe59a2e79bc3efa5e50c8bff55bbbeaad33076e13d4 | K0, OR, KB review |

## Appendix: the assembler's own hand checks (aids for reviewers, not acceptance)

* Facts Z, T, K and Theorems A, B, C: proved above from the cited statements; every hypothesis match is written out.
* FWH Claim 1 (proof-MH.md L63-75): with y = R - x and kappa <= x, y: (p - m) + (p - m) >= p - 1 iff m <= (p + 1)/2, true as
  m <= m* = floor(kappa/2) + 1 <= (p + 1)/2; (p - m) + (y + m - 1 - kappa) >= p - 1 iff y >= kappa; (p - m) + floor(y/2) >= p - 1
  as y >= kappa >= 2(m* - 1) >= 2m - 2; the two linear terms sum to R + 2m - 2 - 2 kappa = 2p - k + 2m - 2 >= p - 1 as
  2m >= k + 1 - kappa >= k - p + 2; linear + floor >= (x + 2m - 3 - 2 kappa + R)/2 >= p - 1 iff x >= k + 1 - 2m, true as
  x >= kappa >= k + 1 - 2m; floor + floor >= (R - 2)/2 >= p - 1 for R >= 2p; for R = 2p - 1 and m = m* the floor terms are the
  minima and sum to (R - 1)/2 = p - 1.  Claim 2 (L76-85): (a) k = 2 kappa + 1 >= 2m* + 1, steps <= 2p - k; (b) k = 2 kappa >=
  2m* + 1 iff kappa >= 3 (k >= 6), steps <= 2p - k + 1; (c) 2 kappa >= k + 1 gives 2 m_lo <= max(2, (k + 3)/2) <= k - 1 and
  m_lo <= m*; in each case the step bound is at most the size 2p - k + 1 of [kappa, R - kappa], so the path from P_0 to P_0^c
  (x(P_0^c) = R - x(P_0)) meets it.  m* >= m_lo holds for R = 2p (both equal ceil((kappa + 1)/2)).
* Theorem ALT (L36-52): with p + 1 particles among 2p - 1 positions, the cyclic shift path keeps p + 1 boundaries, toggles one
  single-letter run per move (Dl changes by +-2), and ends at P_0^c with Dl(P_0^c) = -Dl(P_0); Dl is odd, so some pattern has
  {E+, E-} = {p - 1, p}, and Lemma FW (L25-32: m = (p + 1)/2, E+, E- >= p - 1, h = 0) gives a full window.
* Lemma A1 (L348-362): as FWH Claim 1 at R = 2p - 1 with x = R_P; the vacancy construction gives a path to P^c with steps
  r_u <= 2p - k, shorter than the 2p - k + 1 integers of [kappa, R - kappa].
* K0's dependence on k: located at L101-102 (R >= p, used as R >= 5 in Step 4) and L141 (o_F <= p); plus its even-run hypothesis.
* Not re-derived in full by the assembler: Theorem C0-B' with the Depth Lemma, Lemmas R2 and BR, Theorems KBH, KB, S1' and Lemma
  GC.  Their acceptance is part of (IMP) and (GC).
