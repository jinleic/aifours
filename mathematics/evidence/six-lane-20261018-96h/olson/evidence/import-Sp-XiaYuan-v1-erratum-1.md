# Erratum 1 to evidence/import-Sp-XiaYuan-v1.md (sha256 d4d515cd4ff7b848d703f9337a3e9b6f12f85bd99319173207014519961381d7)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:46:30-0700.
Reviews answered: run review/olson-kps-slz-codex-v1.prompt.stdout.txt (sha256 6ce69cb0eb1a2e23b9edff9d85868e17278adfbb1dd4943e9388380cef102408; 0 FATAL / 0 MAJOR / 3 MINOR, all
on SLZ-EXT) and run review/olson-kps-slz-claude-v1.prompt.note.md (sha256 c98dc2f491e739d374329d2489218a81837512e03b979714cdb57287f1bda3bd; 0 FATAL / 0 MAJOR / 8 required MINOR
M-1..M-8 + 2 editorial E-1, E-2 + optional O-1..O-5).  One coordinated round: this file and its two siblings
(import note, KPS v4, SLZ-EXT v2).  The frozen texts are not edited; no proof strategy or theorem statement changes.

## M-1 / M-2 (scope of Import S(p); the n-range)
The parent read Peng-Sun arXiv:1409.1970v1 Sec. 1 (IRC of 2026-10-19 ~03:40; run review/olson-priority-parent-note-v1.md):
Theorem 1.2 states I(C_n) = floor(n/2) + 2 for n >= 8, and Theorem 1.3 (the restatement of Xia-Yuan Thm 3.1) is stated for an
arbitrary cyclic group, with no further restriction on n in its even-n branch; its parameters t and l are positive (l >= 1).
At this SECONDARY-restatement trust level the classification applies at n = 2p for every prime p >= 5 (n >= 10).  Hence:
- Sec. 1 reads: 'Import S(p).  For every prime p >= 5, ... (at the trust level of Sec. 2: Xia-Yuan's primary text not read;
  hypotheses as restated by Peng-Sun Thm 1.2-1.3, parent-read)'.
- Sec. 2's sentences 'its exact hypotheses on n ... are not verified.  The use here is n = 2p, even, n >= 14 for the lane's
  applications (p >= 7); p = 5 (n = 10) is covered only if Thm 3.1 includes n = 10' are replaced by: 'Xia-Yuan's own
  hypotheses on n are not read; Peng-Sun's restatement (Thm 1.3, arbitrary cyclic G; Thm 1.2, I(C_n) = floor(n/2) + 2 for
  n >= 8) covers every n = 2p, p >= 5, at the secondary-statement trust level.'
- Sec. 5's '(n = 2p within the range of (I2))' is deleted accordingly.
## M-3 (trust items used from (I2))
'The only property of (I2) used' (Sec. 0, Sec. 2, heading of Sec. 4) is replaced by: Claim P uses (i) that the two displayed
families EXHAUST the unsplittable minimal zero-sum sequences of length floor(n/2) + 1 at n = 2p (Peng-Sun's restatement 'either
... or ...' and Yuan's slide 25 'determined all'), and (ii) that Xia-Yuan's 'unsplittable' coincides with the definition of
Sec. 0.  Source of (ii): the standard definition as stated in Peng-Sun Sec. 1 (read by the parent; the lane has not seen the
definition text); Xia-Yuan's own definition was not read.  Both are recorded trust items, not proved.
## M-4 (Lemma SPLIT)
Add the hypothesis 'M has no zero term' (automatic when |M| >= 2: a zero term would be a proper zero-sum); |x|_g is defined
only for x != 0.  Every use (Sec. 5: |M| = p + 1) satisfies it.
## O-1 (adopted): Claim P without the l = 0 case
With the exact text (t, l >= 1), every member of Family B contains (p + 1) g, and every member of Family A contains 2g, so NO
all-odd unsplittable minimal zero-sum of length p + 1 exists.  Independently, g^p (pg) is splittable (pg = g + (p - 1) g gives
the minimal zero-sum g^(p+1) ((p - 1) g)), so it is not in the classification.  Claim P is restated as 'no all-odd unsplittable
minimal zero-sum sequence of length p + 1 exists'; the v1 treatment of l = 0 remains valid and is now redundant.
