# Erratum 1 to proof-P7L-v1.md (sha256 7e8bee08dacb10a9b4dd373dc9e57e526a21bd4bc77e91a41091b8e88cacb7e8)

Owner OlsonThirdCutWindow. Written after /bin/date 2026-10-20T06:19:35-0700, from the author's own re-read of the created
file. The v1 text is not edited. No statement, lemma, case or conclusion of v1 changes.

1. Process disclosure (proof LF379-381). The text says "one rewording replacement (Lemma 2.1(ii)) before creation". The
   correct count is TWO plain in-memory string replacements before the single exclusive creation: the Lemma 2.1(ii)
   sentence ("this proves the case m(P) = 2") and the closing machine-step sentence itself. No assertion of any kind was
   executed and no check over mathematical objects was made (also recorded in checkpoints/cp-05.md).
2. Clarification (proof LF180-181, Lemma 9(e)). theta_e != 0 already follows from theta_e = tau_e != 0 (mod 7); the bound
   |theta_e| <= 6 is recorded but not needed for this. No change.
3. Clarification (proof LF155-158, Lemma 8). a and b have the parity of sigma(P), so a+2j > b means a+2j >= b+2; in all
   uses b-a = B*-x-y >= 8-2 > 0. No change.
