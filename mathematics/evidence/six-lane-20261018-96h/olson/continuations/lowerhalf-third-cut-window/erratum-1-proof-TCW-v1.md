# Erratum 1 to proof-TCW-v1.md (sha256 62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713)

Owner OlsonThirdCutWindow. Written after /bin/date 2026-10-20T05:31:21-0700, from the author's own re-read of the created
file. The v1 text is not edited. No statement, lemma, case or conclusion of v1 changes; items 1-3 are citation and
process corrections only.

1. Process disclosure (proof LF509-511). The text says "one in-memory sentence replacement before creation". The correct
   count is SIX plain in-memory string replacements, all rewording of drafted text before the single exclusive creation:
   Lemma 7(b) proof sentence; the Lemma 13 citation "(by (F5) and Lemma 9(a))"; the closing "Which inputs carry the
   weight" sentence on the all-rotations-equal sub-case; the Sec. 6 (4,11) (F4) bullet; the Sec. 6 sentence on
   all-rotations-equal configurations; the Sec. 7 (M3) paragraph. No assertion of any kind was executed, and no check
   over mathematical objects was made (also recorded in checkpoints/cp-06.md).
2. Citation (proof LF154-155, Lemma 6(b)). "J contains at least u1-4 >= 5 of them (Lemma 3(v))": the bound u1 >= 9 is
   Lemma 3(iii) (u1 >= m1 >= 9); Lemma 3(v) supplies u1 >= b+4 used in the next sentence. Only u1-4 >= b >= 3 is needed
   for the argument (it also shows that J contains letters with |c| = 1).
3. Interface table (proof LF499). PL's Lemma LT and the exchange remark are at PL LF100-106, so the "used" PL lines read
   40-50, 61-83, 93-106 (all inside the pinned range 40-129).
4. Scope file typo (TCW-scope-v1.md Sec. 2, proof-ROT-few-E-v4.md line): the hash is printed inside single quotes; it is
   the correct whole-file sha256 ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f (as in checkpoints/cp-01.md).
