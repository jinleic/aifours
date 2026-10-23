# Disposition: overlap of Lemma S1-sharp's proof with Zeng-Yuan 2011 (k = 2), v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:16:48-0700, on parent instruction, after the priority audit (run
screening/olson-zero-sum-priority-audit-v1.json, sha256 28e9e5678e958d5339912b110ba2bfbe493bf7fdaaf36c0bc8d729d9cc64d93c, findings 7, 8, theorem_comparison 0, open question 3) and
the parent's note (run review/olson-priority-parent-note-v1.md, sha256 6e62cca7d56196792d2cf704eb7b82cd7cd7f3e791e1c33f30e76f21fc0604ed, item 2).  No frozen text is edited; the
accepted statement and correctness verdict of S1-sharp are unchanged.

## Texts concerned
- evidence/proof-S1-sharp-v1.md (992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c) + erratum 1 (bf504cdf8b8cfd3e96a26609d00162d365415b3481ca3a7dcbd7112af82f9507); parent verdict run
  review/olson-s1sharp-parent-verdict-v1.md (bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41).
- X. Zeng, P. Yuan, 'Indexes of long zero-sum sequences over cyclic groups', Eur. J. Combin. 32 (2011) 1213-1221, DOI
  10.1016/j.ejc.2011.06.007, Zbl 1262.11008.  Statement used (k = 2; from the abstract as recorded by the scout; the lane did
  not open the source; full text HTTP 403): 'let S be a zero-sum sequence over C_n of length |S| >= 2 floor(n/2) + 2.
  Suppose that S can be decomposed into a product of at most two minimal zero-sum sequences.  Then there exists some g
  such that S = (n_1 g) ... (n_|S| g), n_i in [1, n], n_1 + ... + n_|S| = 2n.'  The general-k form (Yuan, CANT 2016 slide 21)
  was reconstructed from lost glyphs and is not used.

## The overlap (lane check [W])
In S1-sharp Sec. 2, after Steps 1-3 the shortest long zero-sum T has |T| = N >= 2p + 2 = 2 floor(2p/2) + 2 and T = Q Q' with
Q, Q' minimal zero-sums (Steps 2-3).  Zeng-Yuan then gives g with total coefficient sum 4p.  g is a generator: the terms are
odd, so g is odd, and g = p would make T = p^N, whose minimal zero-sums have length 2, while |Q| = p + delta > 2.  Q and Q'
are zero-sums, so each coefficient sum is a positive multiple of 2p; they add to 4p, hence A_Q = A_Q' = 2p.
- This is the conclusion of Step 4 (a generator with A_Q = 2p; Step 4 obtains it from the index-one theorem, using
  |Q| >= p + 3) together with Step 7 (A_Q' = 2p).  Step 6 (coefficients of Q' are <= D + 1) is used only inside the proof of
  Step 7.
- The facts derived in Step 4 (m >= (p + 3delta)/2, S_Q nonempty, b_min <= p - delta + 1, the bound on the elements of S_Q)
  use only A_Q = 2p, |Q| = p + delta and odd least coefficients, so they hold for Zeng-Yuan's g; Steps 5, 8 and 9 use only
  these facts, A_Q = 0 (mod 2p) and A_Q' = 2p.

## Disposition
1. Credit: Steps 4 (existence of the common generator), 6 and 7 of S1-sharp are routine given Zeng-Yuan 2011 (k = 2).  The
   lane's own proofs of these steps (via the index-one theorem) stand as an alternative route; no step of the accepted text
   is replaced, and no statement changes.
2. Not located in the bounded screen (a search miss is NOT novelty evidence): the statement of S1-sharp (transfer of (ZP_kappa)
   to (S1_kappa) for kappa <= floor(2p/3), sharp), Steps 1-3 (shortest long zero-sum, minimality of all proper zero-sums, the
   induction giving a proper zero-sum of length exactly 2kappa), Step 5 (exchange inequality MC), Steps 8-9 (the b_min
   obstruction and the base >= 3 count) and the sharpness families F1/F2.
3. Significance wording for S1-sharp (lane summaries from now on): 'a sharp specialist lemma; modest extension; partially
   routine given Zeng-Yuan 2011'.  No novelty or priority claim.
4. Optional simplification NOT adopted: citing Zeng-Yuan would remove Step 4's use of |Q| >= p + 3 and Steps 6-7 (audit open
   question 3).  Adopting it would require reading Zeng-Yuan's primary text (exact hypotheses: generator requirement, n
   range); not pursued.
5. Related audit items recorded without change: FB has no located equivalent (bounded); no located primary result implies
   the ordered dihedral criteria; located dihedral E(G) results are unordered (parent note items 3-4).
