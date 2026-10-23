**Packet.** I read SOURCE00–08 as inlined. I did not recompute the SHA256 values, because no tools were available. Citations are SOURCE:LF.

**Result: 0 FATAL, 0 MAJOR, 8 MINOR.**

| Claim | Verdict |
|---|---|
| Lemma S1(c), SOURCE00:27-48 | **ACCEPT** (M2 is editorial only) |
| Corollary S1+, SOURCE00:50-51 | **ACCEPT-WITH-FIXES** (M1) |
| ROT-ZX+ terminal, SOURCE00:58-61 | **ACCEPT-WITH-FIXES** (M3, M5) |
| ROT-ZX+/INV*-ZX+ uniform, SOURCE00:63-72 | **ACCEPT-WITH-FIXES** (M4, M5) |
| OLSON-ZX+ uniform, SOURCE00:74-82 | **ACCEPT-WITH-FIXES** (M5, M6) |
| Sec. 3 ranges and residual, SOURCE00:84-109 | **ACCEPT-WITH-FIXES** (M7, M8) |

Sections 2–3 have the same status as proof-ROT-ZX-v1.md (SOURCE01), which is still unaccepted.

## S1(c), step by step

Here κ=(p+1)/2, the (ZP) window is [p+3, 2p], and the target is that every zero-sum has length ≤ p+1.

- **Choice of T.** If (S1) fails, some zero-sum has even length > p+1. Since p+2 is odd, that length is ≥ p+3, so a shortest such T exists.
- **Step (i).**
  - N is even and not in [p+3, 2p], so N ≥ 2p+2.
  - Removing one term leaves ≥ 2p+1 ≥ D(Z_2p) terms. So there is a nonempty zero-sum missing that term, and it is proper.
  - Take any proper nonempty zero-sum T′. Both T′ and T−T′ are zero-sums of Y shorter than N, so each has length ≤ p+2, hence ≤ p+1 by parity.
  - Therefore N = 2p+2, and |T′| ≥ (2p+2)−(p+1) gives |T′| = p+1. Correct.
- **Step (ii).** Since 2p+2 ≥ 2p−1, EGZ gives T_1 with |T_1| = p and x-sum 0. As p is odd, s(T_1) = (1,0), and |M| = p+2. (s(M) is never used.)
- **Step (iii).**
  - If |V| is even, V is a proper zero-sum of length ≤ p < p+1. Impossible.
  - If |V| is odd, then V ≤ T−T_1, so T_1V uses distinct occurrences and has sum 0. Its length is p+|V| ≤ 2p < N, so it equals p+1. Hence V is one term with x = 0. Correct.
- **Step (iv).**
  - The prefix-sum Davenport argument (proved in-file at SOURCE00:16-17; audited) on any p terms of M gives a nonempty V with |V| ≤ p. So M contains u_1 = (1,0).
  - M−{u_1}, with one occurrence removed, still has p+1 ≥ p terms. This gives a second occurrence u_2 = (1,0).
  - u_1u_2 is a proper zero-sum of length 2 ≠ p+1. Correct.
- **Edge cases.**
  - p=5 (N=12, |M|=7) and p=7 (N=16, |M|=9) go through verbatim.
  - T can contain (1,0) at most once, by (i). If that occurrence lies in T_1, (iv) already gives a contradiction at u_1. If it lies in M, (iv) still forces u_2.
  - Y itself may contain many copies of (1,0); a pair has length 2 ≤ p+1, which (S1) allows.
  - All operations act on occurrences, consistent with SOURCE01:43-44.
  - If |Y| < 2p+2, the claim is trivial.
- **Optional simplification.** (D) can be dropped.
  - Minimality alone gives "every proper nonempty zero-sub-sum has length ≤ p+1", which is all that (iii) uses.
  - In (iv), the complement of u_1u_2 has length N−2 ≥ 2p > p+1, which closes the argument.

## Consequences

- **S1+.** For integer κ ≤ (p+1)/2, either κ ≤ (p−1)/2 (equivalently 4κ ≤ 2p−2, so S1(a) applies; I re-derived it) or κ = (p+1)/2 (S1(c)).
- **Terminal form.**
  - Lemma ZX and Theorem ROT-ZX use κ only through (S1), 0 ≤ κ ≤ k−1 and κ < p (SOURCE01:130,144,150,176-179), and through (H) 2H ≥ 2p−2k ≥ k−1 (SOURCE01:227).
  - κ ≤ (p−1)/2 is used only to obtain (S1) (SOURCE01:219). So (S1) from S1+ at κ̂ = (p+1)/2 is enough.
  - Newly covered terminal pairs: (5,4) at p=7; (7,6) at p=11; (8,7) and (9,7) at p=13; (10,9) and (11,9) at p=17.
- **Uniform corollaries.**
  - k ≤ o (SOURCE05:37), so 3k ≤ 2p+1.
  - Branch o ≤ (p+3)/2 (an integer): κ̂ ≤ k−1 ≤ o−1 ≤ (p+1)/2.
  - Branch F ≥ o+p−3: this is equivalent to κ(w) ≤ (p+1)/2, and κ̂ = κ(w)−(o−k)/2 ≤ κ(w).
  - REFL-few-odd (d) holds because o ≤ (2p+1)/3 ≤ p. Correct.
- **OLSON deletion ledger.**
  - Case 2: (o,F) → (o−1, F−1), so F′−o′ = F−o.
  - Case 3: (o,F) → (o or o−2, F), so F_i−o_i ≥ F−o and o_i ≤ o.
  - Both branches and 3o′ ≤ 2p+1 survive the deletions.
  - Case 1: (F−o)/2 ≥ (4p−3−(2p−3))/2 = p. Correct.
- **Table.** All rows are correct.
  - p=5: o ≤ 3.
  - p=7: (p+3)/2 = 5 = ⌊(2p+1)/3⌋.
  - p=11: both bounds are 7.
  - p=13: o ≤ 8, and o=9 with F ≥ 19.
  - p=17: o ≤ 10, and o=11 with F ≥ 25.
  - p=19: as listed.
- **Residual.**
  - κ̂ ≥ (p+3)/2 together with κ̂ ≤ k−1 and 3k ≤ 2p+1 gives k ≥ (p+5)/2, hence p ≥ 13.
  - The listed pairs for p = 13, 17, 19 are correct and complete; the residual is empty at p = 5, 7, 11.
  - SOURCE00:101-109 make no failure or necessity claim; L107 says so explicitly.

## Findings (all MINOR)

- **M1 — SOURCE00:50.** "every κ with 0 ≤ κ ≤ (p+1)/2" is false for non-integer κ.
  - Counterexample: p=5, κ=1/2, Y = (1,1)(1,4) (that is, 1·9 in Z_10). The window [3,10] contains no zero-sum, but the length-2 zero-sum violates (S1), which requires length ≤ 1.
  - The dichotomy at L51 also needs integer κ.
  - Fix: write "every integer κ" (compare SOURCE08:15-19). S1(c) is unaffected, since (p+1)/2 is an integer.
- **M2 (editorial) — SOURCE00:31, 37, 40, 46.**
  - State the two parity steps (> p+1 ⇒ ≥ p+3; < p+3 ⇒ ≤ p+1).
  - Define s(·) as the sum in Z_(2p); it clashes with the integer s(U) of SOURCE01:110.
  - Cite SOURCE01:43-44 for the multiset/occurrence conventions.
- **M3 — SOURCE00:55-56, 61.** S1+ needs κ̂ to be an integer with κ̂ ≥ 0. Cite:
  - F ≡ k (mod 2), from SOURCE01:48-52;
  - κ̂ ≥ 0 for k ≥ 2 by GRX, from SOURCE01:214-215.
  - Both are obtained without using (S1).
- **M4 — SOURCE00:68.** "κ̂ ≤ k−1 (DAV)" holds only for k ≥ 2. Add: "if k = 1, ROT-ZX+ applies by K1".
- **M5 — SOURCE00:11-18, 58-82.**
  - Mark Sec. 2–3 as conditional on acceptance of SOURCE01, including SOURCE08's MINORs 1–2.
  - List the transitive imports: GRX, PM*, K1, normal form/DAV, MULT, SHgen, SHgen-E, REFL-few-odd, RGR-LONG, and OLSON-few L28-47.
- **M6 — SOURCE00:79.** Case 1 is more than "no INV* call": it needs o ≤ 2p−3 (SOURCE01:258). This holds because o ≤ (2p+1)/3; add the clause.
- **M7 — SOURCE00:98-99, 101.**
  - Change "whose normal form" to "some normal form of which" (SOURCE08:21).
  - Reword L101 roughly as: "S1+ does not supply (S1) at terminal pairs with κ̂ ≥ (p+3)/2. An avoider is outside this route only if no normal form has k=1 or (3k ≤ 2p+1 and κ̂ ≤ (p+1)/2), and its rotation sequence violates (S1); otherwise ROT-ZX applies (SOURCE01:294)."
- **M8 — SOURCE00:88-97.**
  - Change "every avoider" to "every avoider with o_F ≤ 5 (resp. 7), i.e. the whole range 3o_F ≤ 2p+1"; for OLSON, say "every word of length 4p−1".
  - Add "existence of words in the new ranges is not claimed", as in SOURCE04:20.

## Informational (not a finding): S1+ is sharp at p = 5, 7 as a statement about (ZP) alone

At κ = (p+3)/2, (ZP) does **not** imply (S1):

- **p=5, κ=4:** Y = (1,1)^8(1,3)^4. Its zero-sum lengths are {4, 6, 8, 12}. The window [10,10] is empty, but 12 > 8.
- **p=7, κ=5:** Y = (1,1)^10(1,3)^6. Its zero-sum lengths are {6, 8, 10, 16}. The window [12,14] is empty, but 16 > 10. The S1(b) pair is (1,1)^8(1,3)^2 and (1,1)^2(1,3)^4.

Neither κ value occurs as a terminal κ̂ at those primes, since κ̂ ≤ k−1 ≤ (2p−2)/3. So no claim in the addendum is affected, and the non-claim wording at L105-107 is appropriate. I did not examine p ≥ 13.

## Audited vs imported

**Audited by hand:**
- S1(c) in full, including the in-file proof of Davenport for Z_p;
- S1(a) and the S1+ dichotomy;
- how κ is used in ZX and ROT-ZX;
- all branch inequalities and the OLSON ledger;
- the table, the terminal pairs and the residual arithmetic;
- the non-necessity wording.

**Imported (hypotheses checked, not re-proved):**
- EGZ for Z_p (classical) and D(Z_2p) = 2p;
- MULT (used inside ZX);
- GRX, PM*, K1, and the normal form with DAV;
- SHgen and SHgen-E;
- REFL-few-odd and RGR-LONG;
- the OLSON-few case structure;
- Lemma ZX, S1(b) and Theorem ROT-ZX as written in SOURCE01 (also audited in SOURCE08).

No computation was run.
