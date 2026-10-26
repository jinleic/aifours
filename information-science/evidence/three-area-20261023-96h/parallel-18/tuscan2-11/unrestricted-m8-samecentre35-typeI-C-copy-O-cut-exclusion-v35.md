# Actual Tuscan11 same-centre 3+5, Type I, short copy on C, v-cut in O — impossible

Actual `/bin/date` before this body: **Mon Oct 26 01:12:40 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting (v18 §§1–3, SHA256 `66a010b502ca9647d3c1af37745cefd59f94ad71136c4a1243d21d37aeb962bb`)

Same-centre 3+5 support 8: branch copies v3 (degree 3) and v5 (degree 5) of v, theta paths A, B, C (each directed v5 to v3), loop D at v5, one short copy of v, two faces. Type I words: P = D A B^- (three branch visits) and O = D^- C A^- B C^- (five). Every row holds v exactly once, so a face with r rows has r = (its v-visits) + (its v-cuts), and its gap excesses sum to 0 without a v-cut and to 10 with one (band values e in [1,9] at interior visits). This packet treats the short copy on C (then r_P=3, r_O=8, both C traversals in O, C=Lambda with L=20+p+q) and the unique v-cut in O. v18 §§4–5 closed the v-cut in P.

P has no v-cut and consists of D, A, B^-, so x_D+x_A+x_B=0, hence the O-excess sum gives p+q=5.

## 2. Transfers (all arguments are row-local)

(F1) holds: v has degree 3+5+2=10 and each label meets v in exactly one physical edge, so the ten v-neighbours carry ten distinct labels. In O's cyclic word the traversals C and C^- are not adjacent.

- **Cut at the short copy.** v20 §4 (SHA256 `0a1249ba2d262010efaaba699e2beccb3e9b4142ade16e53ccf515cdd04c642f`) uses only Lambda's two traversals inside one face, the rows at Lambda's ends, band values in [1,9], non-adjacency of Lambda and Lambda^- in that face, the opposed-window module and (F2). All hold in O, so this cut is impossible.
- **Cut at an end of C.** v30 (SHA256 `16159aa53d6db5bf3b08a64a534a81190da9f3680ee325be24e645c45a41bddc`) with v22 (I) and v29 §2(a) uses the same row-local data plus (F1); reversal of all rows preserves the class (Type I is fixed by the arities 3 and 5; C stays self-dual; the cut stays in O). So these four corners (D^-|C, C|A^-, B|C^-, C^-|D^-) are impossible.

## 3. The only interior corner A^-|B

From the cut, O's gaps are B, C[L,t], C[t,0], D^-, C[0,t], C[t,L], A^- with excesses x_B, q, p, x_D, p, q, x_A, so e_1=x_B, e_2=x_B+q (=w), e_3=x_B+5, e_4=5-x_A, e_5=5-x_A+p (=u), e_6=10-x_A. Band ranges give 1<=x_B<=4 and 1<=x_A<=4. The window offset is D=10-u-w=x_A-x_B, so |D|<=3, against (T4) |D|>=4 (v21 §2). Impossible.

**Result.** Same-centre 3+5, Type I, short copy on C, v-cut in O is impossible. With v18 §§4–5, Type I with the short copy on C is closed for every v-cut. Remaining same-centre 3+5: Type I with the short copy on a cross path A/B/D and the v-cut in O; all of Type II.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
