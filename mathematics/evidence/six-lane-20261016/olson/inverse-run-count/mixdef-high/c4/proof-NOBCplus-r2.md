# Lemma NOBC+ and Lemma NOLIFT (revision r2): ERRATUM to the DOB(p) obstruction claim, corrected statement

REVISION r2 (c4/proof-NOBCplus-r2.md), written after host clock 2026-10-17T13:30:35-0700.  It supersedes
c3/proof-NOBCplus.md (frozen, unchanged; sha256 48f75d4eb1e0a68895961241854d63eb723f439fe78ecc42b166f4de8bda81fc) and
answers the parent's Codex review institute/runs/six-lane-2026-10-16/review/olson-c3-codex-review-v1.note.md
(proof-NOBCplus.md: REJECT as written; Lemma NOBC+ and Lemma NOLIFT themselves correct; MAJOR finding at
proof-NOBCplus.md:54, :56, :61 and README.md:227, :262).  c3/ is not edited.
Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only).  Imported unchanged:
Lemma H (corrected), Lemma BC, Lemma L, the family W(p, kB) and formula (0.1) of c3/proof-WALL.md (ACCEPT).

## 0. Erratum (what was wrong)

(E1) c3/proof-NOBCplus.md Sec. 3 (lines 54-62) states that for the words of DOB(p) "neither a Lemma BC certificate
... nor a Lemma L/CORE lifting argument starting from singleton extension exists" and that DOB(p) is "out of reach of
both certificate types used so far in this lane".  The second half is FALSE.  Lemma NOLIFT(a) (no certified 2-run
pattern containing the anti run when 3kB >= p + 5) only shows that (H) fails; it does not stop the certification of
larger patterns that contain the anti run by other routes (adjoining the anti singleton to a certified ALIGNED pair),
nor a pin by another certified complementary pair.  Counterexample (reviewer): W(19, 8), which lies in DOB(19), is
excluded by a Lemma L argument; c4/proof-KB0.md (Theorem KB0) writes this argument out for every prime p = 1 (mod 6),
p >= 13, at kB = (p + 5)/3.
(E2) The same claim is withdrawn wherever it was repeated: c3/README.md Sec. 9 lines 226-231 ("so no lifting argument
of the Lemma L type starts ... is beyond BOTH current techniques"), Sec. 11 lines 261-264 ("the explicit sub-family
DOB(p) ..., on which BOTH certificate types of this lane provably fail") and Sec. 12 lines 284-285 ("in particular
DOB(p) for every prime p >= 17, where both certificate types of the lane provably fail").  Each is replaced by the
statement of Sec. 3 below (DOB(p): no Lemma BC certificate and (H) fails; the stronger lifting obstruction only on
DOB*(p)).  The exact computations quoted there (nobcplus.py, famdfs, map3x) are unaffected.
(E3) c3/README.md line 257 states NOLIFT(b) as "for 3kB > p + 6 nothing beyond singletons is certified"; that is a
correct sufficient condition.  The exact condition (c3/proof-NOBCplus.md Sec. 2(b), confirmed below) is 3kB >= p + 7
for odd kB and 3kB >= p + 6 for even kB.

## 1. Lemma NOBC+ (unchanged; reviewed correct)

Statement and proof as in c3/proof-NOBCplus.md Sec. 1 (no Lemma BC certificate for W(p, kB) when
rho(p + kB) - sigma < p + 1; explicit sufficient condition p > kB + 7 + 18/(kB - 3) for kB >= 4).

## 2. Lemma NOLIFT (unchanged; reviewed correct) and the exact pair-certification threshold

Lemma NOLIFT as in c3/proof-NOBCplus.md Sec. 2: (a) if 3kB >= p + 5, no 2-run pattern containing the anti run is
certified; (b) if 3kB >= p + 7 (kB odd) or 3kB >= p + 6 (kB even), no 2-run pattern is certified, hence no proper
pattern with >= 2 runs is certified (also under extended certification).
**Lemma D (aligned pairs beyond W-ALL).**  Let p >= 5 be prime and 1 <= kB <= p - 4 with 3kB >= p + 5.  Then the
aligned pairs of W(p, kB) are certified (by singleton extension) if and only if p = 1 (mod 6) and kB = (p + 5)/3.
Proof.  For aligned s, t the only certification step is {s} -> {s, t}.  With m := m({s, t}) in {1, 2}, (0.1)/(0.2)
of c3/proof-WALL.md give lambda({s}) = lambda({t}) = 2 - kB, lambda({s, t}^c) = min(p - m + 1, p - 3 + m,
floor((p + kB - 2)/2) + 1) = floor((p + kB - 2)/2) + 1 (the floor term is <= p - 2 because kB <= p - 4), and
lambda({s}^c) = Lambda1 = floor((p + kB - 1)/2) + 1.  Condition (A) reads floor((p + kB - 2)/2) >= 2kB - 4, i.e.
3kB <= p + 6 for odd kB and 3kB <= p + 5 for even kB.  Condition (B) holds whenever (A) does:
lambda({s, t}) + 2 Lambda1 >= (3 - kB) + (p + kB - 2) + 2 = p + 3.  Together with 3kB >= p + 5: for odd kB we would
need 3kB in {p + 5, p + 6}, impossible (p + 5 is even while 3kB is odd, and 3 does not divide p + 6 since 3 does not
divide p); for even kB, exactly 3kB = p + 5, which needs p = 1 (mod 3), and kB = (p + 5)/3 is even iff p = 1 (mod 6).  []
[F] review_check.py (out/review_check.txt): the exact (A)/(B) evaluation of aligned and anti pairs agrees with the
closed forms of NOLIFT(a), (b) and Lemma D for every prime 11 <= p <= 199 and every 1 <= kB <= p - 4 (0 mismatches).

## 3. Corrected statement for the doubly obstructed family

DOB(p) := { kB : 1 <= kB <= p - 4, 3kB >= p + 5 and rho(p + kB) - sigma < p + 1 } (definition unchanged).
DOB*(p) := { kB in DOB(p) : NOLIFT(b) applies } = DOB(p) minus {(p + 5)/3}.
**Proposition DOB (corrected).**  Let p >= 5 be prime.
(i) For kB in DOB(p): no word of W(p, kB) has a Lemma BC certificate (Lemma NOBC+), and (H) fails (Lemma NOLIFT(a):
    the anti pairs are not certified).  NOTHING is claimed about other uses of Lemma L.
(ii) For kB in DOB*(p): moreover no proper pattern with >= 2 runs is certified by singleton extension or by extended
    certification (Lemma NOLIFT(b)); so the lifted constraints of Lemma L / Lemma CORE reduce to the singleton
    constraints, and no argument that uses only those lifted constraints and their consequences can exclude these words.
(iii) DOB(p) - DOB*(p) = {(p + 5)/3} if p = 1 (mod 6) and (p + 5)/3 is in DOB(p), and is empty otherwise (Lemma D).
    These words (and W(13, 6), which is beyond Theorem W-ALL but not in DOB(13) = empty) are excluded by
    c4/proof-KB0.md (Theorem KB0).
[F] out/review_check.txt (primes 11..199): DOB(17) = {8, 9, 10} = DOB*(17); DOB(19) = {8, ..., 11}, DOB*(19) = {9, 10, 11};
DOB(23) = DOB*(23) = {10, ..., 16}; DOB(29) = DOB*(29) = {12, ..., 22}; DOB(31) - DOB*(31) = {12}; DOB(37) - DOB*(37) = {14};
DOB(43) - DOB*(43) = {16}; in general DOB(p) - DOB*(p) = {(p + 5)/3} exactly for the primes p = 1 (mod 6) in the range
(19, 31, 37, 43, 61, ..., 199), and the beyond-W-ALL values with certified aligned pairs are exactly kB = (p + 5)/3
(also at p = 13).
Status of DOB*(p) after the review: not excluded by any lifting argument of the Lemma L type (by (ii)); whether other
arguments exclude it is the subject of c4 target T3 (independent-set systems; c4/README.md).  It is NOT claimed that
DOB*(p) is out of reach of every method.

## 4. Exact computations [F] (aids)

* review_check.py / out/review_check.txt: DOB(p), DOB*(p), DOB(p) - DOB*(p), NOLIFT(a)/(b) and Lemma D closed forms
  versus exact lambda evaluation, primes 11..199; plus the type-level certification steps of Theorem KB0 for every prime
  p = 1 (mod 6), 13 <= p <= 199 (0 failures).
* certk.cpp / out/certk_kb0.txt: exact singleton-extension DP on W(13, 6) (all sizes: every proper pattern certified
  except the 19 anti pairs and {0}^c) and on W(19, 8) (sizes <= 9: exactly the 27 anti pairs uncertified; every
  aligned pair, anti triple and pattern of size 3..9 certified); the pin pair P = {0, 2, 4}, P^c certified in both
  (lambda(P) + lambda(P^c) = 8, resp. 10).
