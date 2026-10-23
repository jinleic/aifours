# Erratum 1 (consolidated) to evidence/proof-LSplus-partials-v2.md and its addendum evidence/proof-LSplus-partials-v2-addendum-MAX-v2.md

Owner ContinueOlson (review-errata ownership only).  Written after /bin/date 2026-10-19T04:53:08-0700.
Texts concerned (NOT edited):
- P := evidence/proof-LSplus-partials-v2.md, sha256 eedfa0f16572f1636bfa4f387e3a1566b87864ae4ced6fddcf063cddaedcb6b2
- A := evidence/proof-LSplus-partials-v2-addendum-MAX-v2.md, sha256 4b0be3e304199cc61180e2b5bdad7eb63acb8b2c6e5ada6e95cfb0e099a451c7
Reviews answered in this ONE round:
- run review/olson-LSplus-partials-codex-v1.prompt.stdout.txt, sha256 89ba12944b2edd1ab585bcd3968afc8008fe0e4889b8c41badae9ec487bfceb1: 0 FATAL / 0 MAJOR / 3 MINOR (M1-M3).
- run review/olson-LSplus-partials-claude-v1.prompt.note.md, sha256 f4a4557649936daa81fff270aa6fff7f2ca036c8ea236cee47432579b02d7ac3: 0 FATAL / 0 MAJOR / 9 MINOR (m1-m9; repairs 1-8).
No statement changes.  No statement of Lemma TV, Lemma RED+ (a)/(b), Lemma SHIFT, Corollary SHIFT-C (incl. its LS version), Lemma
MAX or the Proposition 'STAB implies LS+' changes; every item below is a proof repair, a citation, a wording correction or a
status label.  The former side observation of A is relabelled (item 7) as a SEPARATE UNREVIEWED candidate with status HOLD; it is
not granted and is used nowhere.
Disposition map: Codex M1 = Claude m2 -> item 2; Codex M2 = Claude m1 + m9 -> item 1; Codex M3 = Claude m7 -> item 7; Claude m3 ->
item 3; m4 -> item 4; m5 -> item 5; m6 -> item 6; m8 -> item 8.  Line numbers 'P n' / 'A n' refer to the frozen files; quoted 'Old'
blocks are their verbatim whole lines; each 'New' block replaces exactly the quoted lines.

## Item 1 (Codex M2; Claude m1, m9): Lemma MAX -- integer witness, c = 1, e >= 1
1a. Old (A 13-14):
    | Proof.  Write y = c h, c odd in [1, 2p - 1].  For c in {1, 3} the sequence is h^a (3h)^b with a + b = 3kappa + 2 and still has
    | a long zero-sum, so Lemma TV forces a violation of (ZP_kappa).  Let c >= 5 (indeed c >= 3 suffices below).
New:
    | Proof.  Every odd y equals c h for a unique odd c in [1, 2p - 1] (h is a generator); this includes the involution y = p
    | (c = p).  For c in {1, 3} the sequence is h^a (3h)^b with a + b = 3kappa + 2 and still has a long zero-sum (that of E2,
    | resp. E3), so Lemma TV forces a violation of (ZP_kappa).  For c = 1, Lemma TV is load-bearing: the level argument below
    | fails there (w1 = p > p - 1 >= j2 for E2; w1 = 2p > 2p - 1 >= j2 for E3).  Let now 3 <= c <= 2p - 1 (c = 3 is covered twice).
1b. Old (A 18):
    | w2 := (2p + 2e - 1 - c)/2 (integers; w2 - w1 = e - 1 >= 1).  The two intervals meet: w1 <= p - 1 (c >= 3) and
New:
    | w2 := (2p + 2e - 1 - c)/2 (integers, c being odd; w2 - w1 = e - 1 >= 0, for which e >= 1 suffices).  The two intervals
    | meet: w1 <= p - 1 (c >= 3) and
1c. Old (A 20):
    | (2p + 3e - 2 - c)/3 <= p - 1 (c >= 3e + 1 - p, true as 3e <= p - 1) and <= (4p - c)/3 (3e - 2 <= 2p), so j1 <= j2; w1 <= w2.
New:
    | j1 <= j2: put x := (2p + 3e - 2 - c)/3 and x' := (4p - c)/3.  Then x' - x = a/3 >= (p + 3)/3 > 1 (a = 2p - 3e + 2 >= p + 3
    | as 3e <= p - 1), so ceil(x) < x + 1 <= x' and hence ceil(x) <= floor(x'); x <= p - 1 (c >= 3e + 1 - p, true as
    | 3e <= p - 1), so ceil(x) <= p - 1; 0 <= floor(x') as 4p - c >= 2p + 1; and 0 <= p - 1.  So max(0, ceil(x)) <=
    | min(p - 1, floor(x')), i.e. j1 <= j2 (in particular 0 <= j2).  w1 <= w2 (e >= 1).  Integer witness: j1 <= j2, w1 <= w2,
    | w1 <= j2 and j1 <= w2 are inequalities between integers, so j* := max(j1, w1) <= min(j2, w2); with i := 4p - c - 3j* in
    | [0, a] and j* in [0, p - 1], y h^i (3h)^(j*) is a zero-sum subsequence of E2 y of length 1 + 4p - c - 2j* in
    | [2kappa + 2, 2p].
1d. Old (A 24):
    | (5p + 3e - 2 - c)/3 <= w2 (c <= 2p + 1); (5p + 3e - 2 - c)/3 <= 2p - 1 (c >= 3e + 1 - p) and <= (6p - c)/3 (3e - 2 <= p).
New:
    | j1 <= w2: (5p + 3e - 2 - c)/3 <= w2 (c <= 2p + 1) and w2 >= p + e > 0 (c <= 2p - 1).  j1 <= j2: put
    | x := (5p + 3e - 2 - c)/3 and x' := (6p - c)/3; x' - x = a/3 >= 1 (a = 3kappa - 2p + 2 >= 3 as 3kappa >= 2p + 1; the
    | margin is exactly 1 when a = 3), so ceil(x) <= floor(x'); x <= 2p - 1 (c >= 3e + 1 - p); 0 <= floor(x') (6p - c >= 4p + 1);
    | hence j1 <= j2.  w1 <= w2 (e >= 1).  Integer witness j* := max(j1, w1) <= min(j2, w2): with i := 6p - c - 3j* in [0, a]
    | and j* in [0, 2p - 1], y h^i (3h)^(j*) is a zero-sum subsequence of E3 y of length 1 + 6p - c - 2j* in [2kappa + 2, 2p].

## Item 2 (Codex M1; Claude m2): Corollary SHIFT-C, sigma(Y) != 0 via a SHORTEST long zero-sum and odd-kappa parity
Old (P 63-64):
    |   (|X| <= 3kappa - 2p <= 2e + 1, so a zero-sum in X would have length <= 2e and miss T); in particular sigma(Y) != 0 (else X,
    |   nonempty by SLZ3, would be a zero-sum).
New:
    |   (|X| <= 3kappa - 2p <= 2e + 1, so a nonempty zero-sum in X would have even length in [2, 2e] and miss T, against the
    |   first bullet; for T = Y, X is empty and the claim is vacuous); in particular sigma(Y) != 0: for kappa odd, |Y| = 3kappa + 2
    |   is odd and a sum of an odd number of odd elements is odd; for kappa even (indeed for every kappa), if sigma(Y) = 0, choose
    |   T to be a SHORTEST long zero-sum of Y: SLZ3 gives |T| <= 3kappa + 1 < |Y|, so X = Y - T is nonempty with
    |   sigma(X) = sigma(Y) - sigma(T) = 0, a nonempty zero-sum in the zero-sum-free X: contradiction.
(For an arbitrary long T the complement may be empty -- T = Y when sigma(Y) = 0 -- which is why the shortest T is chosen.)

## Item 3 (Claude m3): Fact S range, z even, kappa' >= delta >= 3, occurrence notions
3a. Old (P 14):
    | Fact S (S1-sharp): for kappa' <= kappa0, (ZP_kappa') implies (S1_kappa'), so a (ZP_kappa') sequence has no long zero-sum.
New (citations per item 5):
    | Fact S (Lemma S1-sharp: evidence/proof-S1-sharp-v1.md 992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c, mandatory erratum 1
    | evidence/proof-S1-sharp-v1-erratum-1.md bf504cdf8b8cfd3e96a26609d00162d365415b3481ca3a7dcbd7112af82f9507, parent verdict run
    | review/olson-s1sharp-parent-verdict-v1.md bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41): for every INTEGER kappa' with
    | 0 <= kappa' <= kappa0, (ZP_kappa') implies (S1_kappa'), so a (ZP_kappa') sequence has no kappa'-long zero-sum.
    | Sequences are families of odd elements indexed by occurrences; a subsequence is a set of occurrences; 'Z meets T' means that
    | Z and T share an occurrence, 'misses' is its negation, and Y - Z, Y - T, Y - y, Y - z - z' remove occurrences.  Every
    | nonempty zero-sum of odd elements has even length.
3b. Old (P 59):
    | makes it fail (S1_kappa').  Fact S excludes kappa' <= kappa0.  LS+(p, kappa') gives |Y| - z <= 3kappa' + 1.  []
New:
    | makes it fail (S1_kappa').  As z is even, kappa' is an integer, and z <= 2e gives kappa' >= kappa - e = 2kappa - p = delta >= 3
    | (delta is odd and > p/3 > 1; SLZ3 erratum 1, M1); so if kappa' <= kappa0, Fact S (range 0 <= kappa' <= kappa0) applies and
    | excludes this configuration.  Otherwise kappa0 < kappa' <= kappa - 1 <= p - 3 lies in the LS+ range, and LS+(p, kappa')
    | gives |Y| - z <= 3kappa' + 1.  (Each zero-sum W of Y - Z is disjoint from Z by occurrence, so W u Z is a subsequence of
    | Y.)  []

## Item 4 (Claude m4): Lemma RED+ -- explicit cut-down; H(kappa) only for (b)
4a. Old (P 42):
    | ## 2. Lemma RED+ (inductive structure; conditional on H(kappa))
New:
    | ## 2. Lemma RED+ (inductive structure; (a) uses only the accepted SLZ3, not H(kappa); (b) is conditional on H(kappa))
4b. Old (P 44-45):
    | (a) If LS+(p, kappa) fails, it fails for a sequence of length exactly 3kappa + 2 (cut a counterexample down around a shortest
    |     long zero-sum, which has length <= 3kappa + 1 by SLZ3).
New:
    | (a) If LS+(p, kappa) fails, it fails for a sequence of length exactly 3kappa + 2.
    |     Proof: let Y be a counterexample ((ZP_kappa), not (S1_kappa), |Y| >= 3kappa + 2) and T a shortest long zero-sum of Y;
    |     |T| <= 3kappa + 1 by SLZ3.  Let Y' := T together with any 3kappa + 2 - |T| (>= 1) occurrences of Y - T.  Y' satisfies
    |     (ZP_kappa) ((ZP) is hereditary), fails (S1_kappa) (witnessed by T, a subsequence of Y'; failure of (S1) is not assumed
    |     hereditary) and |Y'| = 3kappa + 2.  No H(kappa) is used.

## Item 5 (Claude m5): citations
5a. SLZ3.  Every reference to SLZ3 in P and A -- P 5-6 ('Lemma RED+ (a) uses the candidate SLZ3'), P 12, P 45, P 64, A 6-7
('the candidate SLZ3 (evidence/proof-SLZ3-v1.md ...)') and A 30 -- denotes the ACCEPTED Theorem SLZ3: evidence/proof-SLZ3-v1.md
(sha256 0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c) with mandatory erratum 1 evidence/proof-SLZ3-v1-erratum-1.md (sha256
483d9d1b70a895215a68654d329b73d8d8ab5221382fda290a933a937f5dda59), parent verdict run review/olson-SLZ3-parent-verdict-v1.md (sha256
2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24): for prime p >= 5 and kappa0 + 1 <= kappa <= p - 1, under (ZP_kappa) every shortest
kappa-long zero-sum has length <= 3kappa + 1.  It bounds |T|, not |Y|; the verdict's qualification on comparisons with Lemma SLZ
(common range kappa0 + 1 <= kappa <= p - 2 only) applies.  The word 'candidate' in P 6 and A 6 is deleted.
5b. Fact S: as in item 3a (S1-sharp text, erratum 1 and parent verdict with full hashes; range 0 <= kappa' <= kappa0).

## Item 6 (Claude m6): Corollary SHIFT-C, LS version -- LS quoted with its range
Old (P 65):
    | LS version.  With LS in place of LS+ (H'(kappa): LS(p, kappa') for kappa0 < kappa' < kappa; Fact S covers kappa' <= kappa0):
New:
    | LS version.  LS(p, kappa) is quoted from evidence/LS-scope-v1.md (sha256 80ae8041118d68f4c1417a67a2891ceaceeba181a375b29dfd73820957cfddfa),
    | Sec. 'Statement under test': 'LS(p, kappa): p >= 5 prime, 0 <= kappa <= p - 2 integer; every sequence Y of odd elements of
    | C_(2p) with |Y| >= p + 2kappa + 1 satisfying (ZP_kappa) (no zero-sum of length in [2kappa + 2, 2p]) satisfies (S1_kappa) (no
    | zero-sum of length > 2kappa, equivalently none of length >= 2p + 2).'  It is a conjecture, not assumed.  Let
    | kappa0 + 1 <= kappa <= p - 2 and assume H'(kappa): LS(p, kappa') for every integer kappa' with kappa0 < kappa' < kappa (each
    | such kappa' <= p - 3 lies in LS's range); Fact S covers 0 <= kappa' <= kappa0.  Then:
Added after P 68:
    | (Details: if Z, of length z in [2, 2e], misses a long zero-sum, then Y - Z satisfies (ZP_kappa') as in Lemma SHIFT, has length
    | exactly p + 2kappa + 1 - z = p + 2kappa' + 1 (LS's threshold at kappa'), kappa' >= delta >= 3, and fails (S1_kappa'): Fact S
    | or LS(p, kappa') from H'(kappa) gives a contradiction.  Complements: |X| <= (p + 2kappa + 1) - (2p + 2) = delta - 1, which is
    | even, and delta - 1 <= 2e + 1 iff 4kappa <= 3p + 2; a nonempty zero-sum in X then has length in [2, 2e] and misses T.)

## Item 7 (Codex M3; Claude m7): the side observation of A -> SEPARATE UNREVIEWED candidate SO, status HOLD
The label of A 37 ('internal; not a claim beyond the SLZ3 text') is WITHDRAWN as false: the observation is strictly stronger
than the accepted SLZ3, and the same strengthening was not adopted in SLZ3 erratum 1 (M6) nor by the SLZ3 parent verdict.
Old (A 37-40):
    | ## Side observation on SLZ3 (internal; not a claim beyond the SLZ3 text)
    | Re-running SLZ3's Steps at N = 3kappa + 1 (kappa odd) gives base = (3kappa + 3 - 2p)/2 >= 3 whenever 3kappa >= 2p + 3 (3kappa + 3 - 2p is even), so
    | for kappa >= kappa0 + 2 the bound improves to N <= 3kappa; F1 shows N = 3kappa + 1 occurs at kappa = (2p + 1)/3.  In all
    | cases N <= max(3kappa, 2p + 2).
New:
    | ## Candidate SO (SEPARATE, UNREVIEWED; status HOLD; not granted, used nowhere)
    | Candidate SO.  Let p >= 5 be prime and kappa0 + 1 <= kappa <= p - 1.  Under (ZP_kappa), every shortest kappa-long zero-sum T of
    | a sequence of odd elements has length N <= max(3kappa, 2p + 2); equivalently N <= 3kappa unless 3kappa = 2p + 1 (then
    | p = 1 (mod 3), kappa = kappa0 + 1 and N <= 2p + 2 = 3kappa + 1, attained by F1).  No claim is made for kappa >= p (at
    | kappa = p, g^(4p) has shortest long zero-sum of length 4p > 3p + 1; SLZ3 erratum 1, M5), and no sharpness is claimed for
    | kappa >= kappa0 + 2.
    | Proof sketch and step map (recorded for a later review; not granted).  The accepted SLZ3 gives N <= 3kappa + 1; N is even.
    | (i) kappa even (includes kappa = p - 1, and kappa = kappa0 + 1 = (2p + 2)/3 when p = 2 (mod 3)): 3kappa + 1 is odd, so
    |     N <= 3kappa.
    | (ii) kappa odd and 3kappa = 2p + 1: max(3kappa, 2p + 2) = 3kappa + 1 and SLZ3 is the claim.
    | (iii) kappa odd and 3kappa >= 2p + 2: then 3kappa >= 2p + 3 (3kappa is odd), equivalently kappa >= kappa0 + 2 in the range.
    |     Suppose N = 3kappa + 1; with u := 2kappa: l := N - u = kappa + 1 (even), D := 2u - N = kappa - 1, delta := 2kappa - p
    |     (odd, 3 <= delta <= p - 2).  Re-run SLZ3's proof (S1-sharp Steps 1-9 with S1-sharp erratum 1 and SLZ3 erratum 1 as
    |     mandatory overlays) with SLZ3's hypothesis N >= 3kappa + 2 replaced by N = 3kappa + 1:
    |     - Step 1 (minimality of N only): proper nonempty zero-sums of T have length in [l, u]; N >= 2p + 4 gives D <= 2delta - 2
    |       and l >= p - delta + 2.
    |     - Step 2 needs N > 3kappa: holds.
    |     - Step 3 needs N > 3kappa - 2 and N > 2p: holds; as kappa - 1 >= kappa0 + 1, it uses the accepted SLZ3 at kappa - 1,
    |       whose bound 3(kappa - 1) + 1 = 3kappa - 2 suffices (no strengthened induction hypothesis); Step 1 applied to Q' gives
    |       D >= 0.
    |     - Step 4 needs |Q| = p + delta >= p + 3 and kappa <= p - 1 (S_Q nonempty): holds.  Steps 5 and 8 are independent of kappa.
    |     - Step 6 needs D <= 2delta - 2 and m >= (p + 3delta)/2 >= 2delta >= D + 2 (delta <= p): holds.
    |     - Step 7 needs D <= 2delta - 2 <= 2p - 6 (delta <= p - 2) and ends with l <= D, i.e. N <= 3kappa: contradiction.
    |     - Step 9 is the only step whose input changes: SLZ3's 'l >= kappa + 2 (base >= 4)' is replaced by l = kappa + 1 and
    |       base := (3l - 2p)/2 = (3kappa + 3 - 2p)/2, an integer with base >= 3 iff 3kappa >= 2p + 3 (true in case (iii));
    |       base >= 3 is all that S1-sharp's Step 9 with erratum A-m6 uses (t' <= 2 gives X < 0; t' >= 3 uses t' - 2 > t' - base),
    |       and l >= p - delta + 2 > b_min (Step 1) completes the contradiction.  (Claude's review records that base >= 4 in fact
    |       holds throughout case (iii); not needed.)
    |     Hence N <= 3kappa in case (iii).

## Item 8 (Claude m8): Lemma TV wording
8a. Old (P 21-22):
    | Proof.  If h = p (the involution), Y = p^(a+b) and (ZP_kappa) forces a + b <= 2kappa + 1 < 2p + 2, so no long zero-sum: so h
    | is a generator.  Zero-sums are h^i (3h)^j with i <= a, j <= b, i + 3j = 2pk (k >= 1), of length 2pk - 2j.  (ZP_kappa)
New:
    | Proof.  If h = p (the involution), Y = p^(a+b); since kappa <= p - 1, p^(2kappa+2) would be a zero-sum of length
    | 2kappa + 2 <= 2p, so (ZP_kappa) forces a + b <= 2kappa + 1, and Y has no zero-sum of length >= 2kappa + 2 (no long
    | zero-sum), contradicting the failure of (S1_kappa); as gcd(h, 2p) = gcd(h, p) for odd h, the only odd non-generator is p,
    | so h is a generator.  Zero-sums are h^i (3h)^j with i <= a, j <= b, i + 3j = 2pk (k >= 1), of length 2pk - 2j.  (ZP_kappa)
8b. Old (P 25):
    | [2kappa + 2, 2p] iff j in [p(k-1), pk - kappa - 1]; it is long iff j <= p(k-1) - 1.  Let k* be the least level with a long
New:
    | [2kappa + 2, 2p] iff j in [p(k-1), pk - kappa - 1]; under (ZP_kappa) a zero-sum is long iff its length is >= 2p + 2, i.e.
    | iff j <= p(k-1) - 1 (the (ZP_kappa)-relative criterion; in general 'long' means length >= 2kappa + 2).  Let k* be the
    | least level with a long

## Recorded observations (no repair; nothing changes)
- Claude: in E3, level 1 has j >= p - kappa + ceil((p - 2)/3) (P's 'j >= p - kappa' is true and weaker); the representation
  {h, 3h} is unambiguous (h' != h with {h', 3h'} = {h, 3h} forces 8h = 0, i.e. h = p); at p = 1 (mod 3) and
  kappa = (2p + 1)/3, E2 = F1 and E3 = F2 (h = ((2p + 1)/3) g), so F2 is no obstruction to STAB; the shortest zero-sum of E2
  and of E3 has length 2 ceil(p/3) > 2e (P Sec. 4 correct).
- Claude: the probe support for STAB consists of three complete cells, all with kappa <= kappa0 + 2 (aid, not a premise).
- Claude, out of review scope (the scope file evidence/LSplus-scope-v1.md, not a lemma): its remark 'LS+ implies ... S1-sharp'
  is vacuous within the LS+ range (S1-sharp, kappa <= kappa0, is the base of the induction, not a consequence); the LS+ range
  is empty at p = 5 (kappa0 + 1 = 4 > p - 2 = 3), the first nonempty cell being (p, kappa) = (7, 5).  No lemma statement
  depends on either.

## Scope after repair
Lemma TV, Lemma RED+, Lemma SHIFT, Corollary SHIFT-C (and its LS version) and Lemma MAX are scoped partials, with RED+ (b) and
SHIFT-C conditional on H(kappa) (the LS version on H'(kappa)) and SHIFT conditional on LS+(p, kappa') as stated; 'STAB implies
LS+' is a conditional reduction only; Candidate SO is HOLD (unreviewed, not granted).  LS+, STAB, LS, INV* and ordered Olson
remain OPEN.  No novelty claim; no Lean; no computation is a premise.
