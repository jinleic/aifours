# Dependency list and exact statements for proof-ROT-ZX-v1.md (companion note, v1)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T11:44:02-07:00.  Requested by the parent for the
review packet.  This note does not change proof-ROT-ZX-v1.md (ad2460b2...815b, frozen); it only lists its imports and
restates its corollaries with explicit quantifiers.  No novelty claim.  Where a statement is not covered, that means
not covered by this route; it is never a claim that the statement fails.

Paths: R = institute/runs/six-lane-2026-10-16/review/; files without a directory are in rotation/.

## A. Imports, with the exact hypothesis used at each call

Lemma ZX and Lemma S1 (statements about sequences only) use:
1. (D) D(Z_(2p)) = 2p, i.e. every zero-sum-free sequence over Z_(2p) has length <= 2p - 1.
   Source: R/olson-rotation-lowodd-parent-verdict-v2.md (0853f4ac...ba29).
   Used in ZX Step A (L <= 2p - 1) and in S1 (a), (b) (a minimal zero-sum has length <= 2p).
2. Lemma MULT, proof-ROT-few-v4.md (abd3973c...b521) L61-81, accepted with ROT-FEW
   (R/olson-fewodd-parent-verdict-v1-addendum-1.md, 279d89d2...a62a, L11).
   Setting: Y' is a zero-sum-free sequence of odd elements of Z_(2p), L := |Y'|, e := 2p - 1 - L, and m is the
   largest multiplicity, attained by g.
   - (i) m >= L - e; no further hypothesis.  Not used by ZX.
   - (ii) If m >= max(2, e + 1), then g is a generator and Y' = g^m (d_1 g) ... (d_q g) with odd d_j >= 3 and
     sum_j (d_j - 1) <= e.
   - (iii) If 2p >= 3e + 2, then m >= max(2, e + 1).
   How ZX meets these hypotheses (Step A):
   - Y' := Y - Z is zero-sum-free because Z is a longest zero-sum.
   - |Z| <= 2kappa by (S1), so L >= 2p - k and e <= k - 1.
   - Hence 3e + 2 <= 3k - 1 <= 2p by 3k <= 2p + 1, so (iii) holds, and then (ii) holds.
   Derived inequalities, which are not separate imports:
   - 3e <= 2p - 1 (Step E): 3e <= 3(k - 1) <= 2p - 2, from e <= k - 1 and 3k <= 2p + 1.
   - m >= L - e'/2 (A1): from the form in (ii), L = m + q.  Each d_j >= 3 gives e' = sum_j (d_j - 1) >= 2q, so
     m = L - q >= L - e'/2.
   - d_j <= e' + 1 <= e + 1 <= m (A2): e' <= e by (ii), and m >= e + 1 by (iii).
   - COMP (a)-(c) and (A3), (A4) are proved in the file from the form in (ii) and (D).

Theorem ROT-ZX additionally uses:
3. The normal form: proof-ROT-few-E-v4.md (ac560eb8...ea8f) Sec. 0, L28-43.
   - From any avoider w of length 4p - 2 it produces an avoider w^ with the same length, rotation multiset and F.
   - w^ has a cyclic representation with 1 <= k <= o all-odd blocks (k = o mod 2), and every empty run lies between
     blocks of different values.
   - The ending with one even block is impossible (L39-41).
   - Its proof uses PM*, K1 and the fusion rule.
   - The statements in Sec. B quantify over any normal form produced by this process.
4. Lemma PM*: R/olson-rotation-lowodd-parent-verdict-v2.md.  It merges across even blocks, empty runs allowed, and
   preserves avoidance, rotation multiset, length, F, the number of odd blocks and H.  Used only inside item 3.
5. Proposition K1: same verdict.  Terminal k = 1 makes all rotations equal (then F = 2p - 1 and kappa^ = 0).
6. GRX: same verdict, in the form of proof-SHgen-v3.md (fcbd5a97...eb5e) L29-33; empty runs allowed.
   - z = all +: (ZP) for the rotation sequence of w^ at kappa^ (L33; proof-ROT-few-E-v4.md L42-43).
   - kappa^ >= 0: if H >= p, the all-plus pattern with m = 0 selected rotations is an identity selection (L37).
7. Lemma DAV / (V): kappa^ <= k - 1, proof-ROT-few-E-v4.md L42-43, which quotes Lemma DAV of proof-ROT-o3-v4.md (any
   constant-block representation; boundary gaps are not in I).
8. Theorem SHgen: proof-SHgen-v3.md L44-49, with its setting L20-28 and weights L39-42.
   - Setting: k >= 2 odd blocks, all runs nonempty.
   - Hypotheses: eta >= 1, (H) 2H >= E, (K) k <= 2p - eta - a_max - 1.
   - ROT-ZX establishes |b| <= k <= p - 2 before identifying b with the SHgen weight b_x.
9. Lemma SHgen-E: proof-ROT-few-E-v4.md Sec. 1, L45-70.
   - Same as item 8, but empty runs are allowed between blocks of different values.
   - It assumes REFL(p) for words with o_F <= k, and o_F <= k <= p holds throughout its induction.
10. Corollary REFL-few-odd: reflection/proof-REFL-fewodd-r4.md (1e447754...861d) L21-25, through its Sec. 4 interface
    (R/olson-refl-fewodd-parent-verdict-v1.md, 16436c07...f1ca, L6).
    - Hypotheses: (0) p >= 5 prime; (a) |w| = 4p - 2; (b) all rotations in one {rho_c, rho_-c} with c != 0;
      (d) o_F(w) <= p.
    - Conclusion: every maximal cyclic reflection run of w is constant.
    - Used for the SHgen-E descendants (o_F <= k <= p) and, in INV*-ZX, for w itself.
11. RGR-LONG(p): R/olson-runs-parent-verdict-v1.md (82adbddd...9237) L7.  Every RGR word of length 4p - 1 has an
    identity 2p-subword.  Used in OLSON-ZX.
12. The case structure of proof-OLSON-few-v3.md (ae151f9b...d66a) L28-47 (Cases 1-3) and the parent-accepted deletion
    argument (half-range verdict, overlay 5).  OLSON-ZX states its own deletion calculations.

## B. Exact statements, with quantifiers

Conventions.
- An avoider is a word over D_(2p) with no identity 2p-subword in increasing index order.
- o_F(w) is the number of odd blocks in the maximal cyclic constant reflection-block decomposition of w, and
  F(w) is the number of reflection letters.

**ROT-ZX (terminal form).**  For every prime p >= 5 and every avoider w of length 4p - 2, suppose SOME normal form w^
of w (item 3), with terminal k and kappa^ := p - 1 - (F(w) - k)/2, satisfies either
- k = 1, or
- 3k <= 2p + 1 and every zero-sum subsequence of its rotation sequence has length <= 2 kappa^.
Then there is c in Z_p \ {0} such that every rotation letter of w is rho_c or rho_-c.  The second alternative holds
in particular when 3k <= 2p + 1 and kappa^ <= (p - 1)/2.

**ROT-ZX (uniform).**  For every prime p >= 5 and every avoider w of length 4p - 2 with o := o_F(w) and F := F(w),
suppose 3o <= 2p + 1, and o <= (p + 1)/2 or F >= o + p - 1.  Then there is c in Z_p \ {0} such that every rotation
letter of w is rho_c or rho_-c.

**INV*-ZX (uniform).**  For every prime p >= 5 and every avoider w of length 4p - 2 with o := o_F(w) and F := F(w),
suppose 3o <= 2p + 1, and o <= (p + 1)/2 or F >= o + p - 1.  Then w is RGR: there is c in Z_p \ {0} such that every
rotation letter is rho_c or rho_-c, and every maximal cyclic reflection run of w is constant.
Terminal form: the same conclusion holds for every avoider covered by ROT-ZX (terminal form) with o_F(w) <= p.

**OLSON-ZX (uniform).**  For every prime p >= 5 and every word w of length 4p - 1 over D_(2p) with o := o_F(w) and
F := F(w), suppose 3o <= 2p + 1, and o <= (p + 1)/2 or F - o >= p - 1.  Then w has an identity 2p-subword in
increasing index order: there are indices i_1 < ... < i_(2p) with w_(i_1) ... w_(i_(2p)) = 1 in D_(2p).

**Not covered by this route.**
- Avoiders of length 4p - 2 for which no normal form meets the ROT-ZX (terminal) condition.  Inside 3k <= 2p + 1
  these have kappa^ >= (p + 1)/2, and by Lemma S1 (b) their rotation sequence contains two disjoint minimal zero-sums
  P, P' with 2p - 2kappa^ + 2 <= |P|, |P'| <= 2kappa^ and |P| + |P'| >= 2p + 2.
- Words of length 4p - 1 outside the uniform condition of OLSON-ZX.
- Neither is claimed to fail.
