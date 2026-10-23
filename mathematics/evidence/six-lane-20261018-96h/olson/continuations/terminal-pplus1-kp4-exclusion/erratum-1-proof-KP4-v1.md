# Erratum 1 to proof-KP4-v1.md (author's line audit; wording only)

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T16:31:53-0700. Read after the immutable proof-KP4-v1.md, SHA256
a6308ea8e265869795028fcddbdfaaa5a01f0ec514b587da0a6c227af1efaacf (frozen 16:27:44). No statement, lemma, case split or
inequality changes; the proof file is not edited. Each Old span occurs exactly once in the proof.

## E1 (Sec. 7.3, |E|=1, profile (5,2,1^5)): the parenthetical names the wrong arc

Old:
````text
  to the 3-run: 4. (5,2,1^5): a neighbouring 1-run gives an arc of 6, so the 5-run sits between run 0 and the 2-run, and the
  arc through runs 7,0,1 (or 0,1,2 after reflection) holds 1+0+5=6.
````

New:
````text
  to the 3-run: 4. (5,2,1^5): a neighbouring 1-run gives an arc of 6, so the 5-run sits between run 0 and the 2-run. In both
  placements (5-run at 1 with the 2-run at 2, or 5-run at 7 with the 2-run at 6) the arc of runs 7,0,1 holds 6 letters
  (1+0+5, resp. 5+0+1).
````

## E2 (Sec. 3 heading): scope of Lemma MW

Old:
````text
## 3. Multi-length windows (p>=11) [RE-DERIVED for this cell]
````

New:
````text
## 3. Multi-length windows [RE-DERIVED for this cell]; Lemma MW holds for every prime p>=7, the instances MW2/MW34 need p>=11
````

Reason: Sec. 7.2(v) applies the general Lemma MW at p=7. Its statement and proof use only SR4, Lemma P/U, RS(b) and CD,
and the distinctness remark (calK in an integer interval of length <=6<p) holds for p=7. Only the listed instances
MW2 (p>=8) and MW34 (p>=10) need the stated bounds on p.
