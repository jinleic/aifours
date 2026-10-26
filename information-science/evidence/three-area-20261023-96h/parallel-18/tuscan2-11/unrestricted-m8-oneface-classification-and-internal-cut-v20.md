# Actual Tuscan11 one8/ONE face — complete face-word classification and UNIVERSAL internal-cut exclusion

Actual `/bin/date` before this body: **Sun Oct 25 21:36:24 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed/adopted/formal/executable/novelty cleared. Every finite permutation/chord/case statement below is written by hand, not by an interpreter, program, enumeration tool or replay. No scientific GO.

## 1. Scope and boundary

Current accepted boundary: m>=8 for eleven arbitrary Hamilton rows covering all110 LINEAR ordered adjacencies; v12/v13 and only the partial v14 classes are parent-supported at their stated scope (`RUN/tuscan-v12-v14-entire-m8-and-partial-selfdual-parent-v1.md`, SHA256 `4465171ac189cb5fcbcfdb4f9e10cd982b715b7972650815a06f5b0d06285e27`). V15–v19 are later unreviewed candidates; this paper does not use them as premises except that §5 records how its results relate to v19. Current whole-source manifest: v3 SHA256 `ebd91c88d902d26b496402ec08db34aaa2771439d6983164138aac7e06e1bc68`.

Hypothesis of this paper: EXACT one8-cycle support (one local8-cycle at original v, all other off-centre cycles2), beta0, and the T-faces form ONE110-edge face. All original eleven K_x/fpGF/simpleM/ten-step layers/Hamilton segments remain. Only actual Tuscan1 consequences are used, hence the results apply to Tuscan2 candidates. No Latin/regular/cyclic row family, GF=M, independent row reversal or support cap is assumed.

The split graph is a bouquet of four physical loops at the degree8 branch v; ONE degree2 physical copy of v (the short copy) lies inside one loop Lambda; every ordinary symbol has five degree2 copies. The single face traverses every loop once in each direction.

## 2. COMPLETE classification of the one-face words

Write the face as a cyclic word of its eight branch-to-branch traversals; each loop X occurs once as X and once as X^-. Mark the eight occurrences at positions0..7 and let alpha pair the two positions of each loop. Duality of the one-vertex/one-face map says: the branch rotation is ONE8-cycle iff the permutation phi(i)=alpha(i)+1 (mod8) of the position chord diagram is ONE8-cycle. (Direct verification: for a face successor relation the branch rotation is obtained by sending the terminal half-edge of each traversal to the initial half-edge of the next traversal; this is conjugate to phi above.)

**Span1 chords are impossible.** If alpha(i)=i+1 then phi(i+1)=alpha(i+1)+1=i+1 is fixed.

**No chord of span<=2.** Suppose all spans are3 or4. If all are4 we get the all-diameter diagram. If some chord has span3, rotate it to(0,3). Points1,2 cannot pair together; the span>=3 rule forces partner(1) in{4,5,6}, partner(2) in{5,6,7}, and the remaining two of{4,5,6,7} must be the only span>=3 pair(4,7). Hence{partner1,partner2}={5,6}. Both resulting diagrams have alpha(0)=3,alpha(4)=7 and phi contains the2-cycle(0 4). Thus ONLY the all-diameter diagram survives.

**Some chord of span2.** Rotate it to(0,2); let y=alpha(1) in{3,...,7}, and match the other four points in their three possible ways. Writing phi(i)=alpha(i)+1 explicitly, the fifteen cases give:

|y|matching of remaining points|phi verdict|
|---|---|---|
|3|45,67 / 46,57 / 47,56|fixed5 / ONE8-cycle / 5-cycle(0 3 2 1 4)|
|4|35,67 / 36,57 / 37,56|fixed7 / ONE8-cycle / fixed6|
|5|34,67 / 36,47 / 37,46|fixed4 / ONE8-cycle / 2-cycle(0 3)|
|6|34,57 / 35,47 / 37,45|fixed4 / ONE8-cycle / 2-cycle(0 3)|
|7|34,56 / 35,46 / 36,45|fixed4 / ONE8-cycle / 5-cycle(0 3 7 2 1)|

The five surviving diagrams are, respectively, XYXYZWZW, XYXZYWZW, XYXZWYZW, XYXZWZYW, XYXZWZWY. The fourth is a rotation of the second and the fifth a rotation of the first. Including the all-diameter case, every one-face one8 word is, up to choosing the face origin and naming loop directions, exactly one of

- W1 `A B C D A^- B^- C^- D^-` (all four chords interlaced),
- W2 `A B A^- B^- C D C^- D^-`,
- W3 `A B A^- C B^- D C^- D^-`,
- W4 `A B A^- C D B^- C^- D^-`.

For each, following face successors gives one8 branch rotation (for example W2 gives a-,b+,c+,d-,c-,d+,a+,b-). The four classes have rotation orbit sizes1,4,8,8, total21. Each class is also invariant under reflection, so global row reversal never produces a fifth class. This is a complete WRITTEN classification, not an imported genus table and not a sampled search.

## 3. Exact one-face band structure

Put the unique v-cut at face coordinate0. Every row contains v exactly once. Rows0 and10 contain v only at their endpoint0/110; each row m=1..9 contains exactly ONE non-endpoint v. Hence the other nine v-visits are

`P_m=10m+e_m`, `e_m in{1,...,9}`, m=1..9;

write e_0=0,e_10=10. Consecutive v-visits bound ten v-free gaps; gap m has length `10+e_(m+1)-e_m`, and its unique interior cut is at10(m+1). Row m is literally

`TAIL(m-1)  v  HEAD(m)`,

where HEAD(m) is the first10-e_m interior symbols of gap m (ending at its cut) and TAIL(m-1) the last e_m interior symbols of gap m-1 (starting at its cut). Since rows are Hamilton permutations,

`TAIL(m-1) disjoint-union HEAD(m) = O` (the ten ordinary symbols).

Gaps0 and9 have lengths11..19. Each ordinary loop traversal is one gap; each short-loop traversal is two gaps split by the short copy. These are restatements of actual row cuts, not added hypotheses.

## 4. UNIVERSAL theorem: the v-cut cannot be at the short copy (ALL four words)

Suppose the unique v-cut is at one visit of the short copy. Name Lambda's direction so that this visit is on Lambda's forward traversal; this is naming only. Let the short copy be at physical t on Lambda (length L). Then gap9 is Lambda[0,t] and gap0 is Lambda[t,L]; their lengths give

`t=20-e_9 in[11,19]`, `L-t=10+e_1 in[11,19]`.

Rows10 and0 are the WHOLE forward windows `W_10=Lambda[t-10,t]` and `W_0=Lambda[t,t+10]`. Lambda's backward traversal is two consecutive interior gaps j (Lambda[L,t]) and j+1 (Lambda[t,0]) of lengths10+e_1 and20-e_9. No word places Lambda^- immediately after or before Lambda (span1 chords are impossible), so 2<=j and j+2<=8; thus e_j,e_(j+2) lie in1..9 and gaps j-1,j+2 traverse loops OTHER than Lambda.

Let delta=e_(j+1). Row j+1 is the WHOLE backward window `B=Lambda[t-10+delta,t+delta]`. B against W_0 has start difference delta and against W_10 has10-delta. The supplied actual opposed-window module (reverse pair needs two fixed boundaries, beta=0 here; difference1 duplicates an actual row start; differences2/3 repeat an edge of K2/K3 at distinct physical positions) forces

`delta in{4,5,6}`.

Set subtraction of B with W_10 and W_0 gives the ordinary partition

`H=labels(Lambda_(t+1..t+delta))=labels(Lambda_(t-10..t-11+delta))`,
`K=labels(Lambda_(t+delta+1..t+10))=labels(Lambda_(t-10+delta..t-1))`,

|H|=delta,|K|=10-delta. Each side carries TWO physical paths at disjoint positions: H has2delta-2 edges, K has18-2delta. Put r0=Lambda_(t+delta) (an endpoint of H's first path) and s0=Lambda_(t-10+delta).

The SAME actual rows crossing Lambda's two endpoints give exact complements:

- Row j: HEAD(j)=Lambda[t+delta,L-1]={r0} union K union E_suf, E_suf=Lambda[t+11,L-1] of size e_1-1. Hence E_suf subset H minus{r0} and the path TAIL(j-1), on another loop, has label set `H minus({r0} union E_suf)` and e_j=delta-e_1>=1 vertices.
- Row j+2: TAIL(j+1)=Lambda[1,t-10+delta]={s0} union H union E_pre, E_pre=Lambda[1,t-11] of size9-e_9. Hence E_pre subset K minus{s0} and the path HEAD(j+2), on another loop, has label set `K minus({s0} union E_pre)` and e_9-delta>=1 vertices (because e_(j+2)=delta+10-e_9<=9).

All these new paths lie at physical positions disjoint from the four certificate paths.

- delta4: K4(H) is already exhausted. New H-edges number (3-e_1)+max(e_1-2,0)=2,1,1 at e_1=1,2,3. Repetition.
- delta6: K4(K) is already exhausted. New K-edges number (e_9-7)+max(8-e_9,0)=1,1,2 at e_9=7,8,9. Repetition.
- delta5: H's two P5 use8 of10 K5 edges. New H-edges number (4-e_1)+max(e_1-2,0)=3,2,2,2 at e_1=1..4. Three exceed the remaining two; with exactly two, a complete K5 would need degree4 at r0, but r0 has degree<=3 in the certificate paths (endpoint of one P5) and no new path touches r0.

Every possibility repeats an unordered edge. **Hence in EVERY one-face one8 system the unique v-cut lies at a BRANCH corner.** This holds for W1–W4 alike; its only word input is the absence of span1 chords. It is the uniform form of the internal-cut argument used in v19 Sections6–8, now proved directly for all four words.

## 5. Exact remaining one8/F1 residual and status

Combining §§2–4: an actual one8/ONE-face system must have one of W1–W4 and a BRANCH v-cut. V19 (unreviewed candidate) separately claims to close W1 completely; this paper re-closes W1's internal-cut part independently but does NOT reprove v19's W1 branch-cut part.

OPEN here: W2, W3 and W4 with a branch v-cut, for every short-copy loop and every branch corner (up to each word's proved symmetries: W2 acts transitively on its four loops; W3 has only the reversal symmetry A<->D,B<->C; W4 only the reversal fixing A,B and swapping C,D). Every actual length, cut, copy and ordinary-label condition remains, as do ALL other m8 placements and ALL m>=9.

**First unproved ORIGINAL step:** literal11x11 table with110 distinct LINEAR adjacencies and99 distinct LINEAR distance-two events, or contradiction for every remaining full eleven-K_x/fpGF/simpleM/layer/Hamilton system. Neither is supplied. No table, unrestricted Tuscan2(11) no-go, support cap or stronger assurance follows.

All cadence/private-written-exactness/admission/clock/source histories and the checkpoint045 mathematical withdrawal remain unchanged. This candidate needs its own complete source-bound gate; it is outside every earlier frozen wave and inherits no prior verdict.
