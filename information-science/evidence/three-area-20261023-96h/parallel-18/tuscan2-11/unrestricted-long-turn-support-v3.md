# Actual unrestricted Tuscan11 turn support: the regimes m=3,4,5 are impossible

Owner `InfoRecursiveMDS18-2`. NEW WRITTEN CANDIDATE, frozen with the actual clock and SHA256 in checkpoint010 before the temporary v81-B review. This is a consolidated proof of the next actual-core obstruction, not a full Tuscan-2(11) settlement.

**Main new candidate theorem.** In any eleven Hamilton rows with exact LINEAR ordered-adjacency coverage, the total number m of arrows in completed center cycles of length>=3 satisfies **m>=6**. Consequently every unrestricted Tuscan-2(11) square would have m>=6 as well.

All proofs below are written. No interpreter/eval, enumeration, arithmetic/symbolic program, native scientific child, replay, external CLI, nested agent or scientific GO. All arbitrary asymmetric rows are retained. The order11 table/unrestricted-obstruction target is STILL OPEN at m>=6.

## 1. Actual data, baseline and assurance boundary

The definitions are those of the complete current191LF `unrestricted-boundary-turn-coupling-v1.md`, SHA256 `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275`. Its actual complete151LF reconstruction has SHA256 `acaa6029b30eee6c51f64ff6ff99a900c7b6aaf41d865f51ed4771634ddf7ee5`; its complete25LF parent boundary has SHA256 `57f88518207f60db578f2fc2892969c133527304aba00d76a711a7a62fdebc0e`. All were read for this push. V11 withdraws the parent's invented10:04 header clock; no chronological credit is imported. The OLD interface review does NOT cover the NEW theorem here.

The earlier consolidated `unrestricted-boundary-turn-core-v2.md` was frozen and sent for fresh review. Its m4 stratum was still open. This successor closes that entire stratum and also excludes m5 by a stronger boundary-leaf argument. It does not silently edit v2, transfer its future review verdict, or import the unreviewed global-asymmetry candidate.

Let X have eleven symbols. Each actual row is a permutation of X. Exact adjacent-pair coverage gives one start and one end at every symbol; tau is the fixed-point-free endpoint permutation. Define f(v),p(v) from the second symbol in the row starting v and the penultimate symbol in the row ending v.

The actual internal-triple map at v is completed by its boundary turn p(v)->f(v) and diagonal v->v to a permutation K_v. On X\{v}, the only possible fixed point is the boundary p(v)=f(v). Let beta=#such boundary loops. Let m count all arrows in all cycles of length>=3 on these ten neighbors, across all eleven centers.

The arc-successor map is `T(a,v)=(v,K_v(a))`. It follows whole actual ten-edge rows, then splices at their endpoints. Its cycles are precisely tau-cycles stretched by10. A T-cycle containing r rows has length10r and, among its arc TAILS, visits each original symbol a exactly

`r-1_(a in its row-start set)`.                           (1)

This follows by omitting the unique end from each Hamilton row's tail list. Different T-cycles have disjoint nonempty start sets.

Make the split graph by one vertex for each cycle of K_v on X\{v}, with degree equal to that cycle's length. The unordered original edge{a,b} joins its two copies at a,b. There is exactly one edge for each unordered pair, so this graph has55 edges, no loop or parallel edge, and its projected edges are globally UNORDERED-EDGE-SIMPLE. Distinct split copies may carry the same original symbol. The cyclic orders realize T as oriented-edge walks.

The original Tuscan-2 interface remains `sum K_v=J+GF-M`, with ACTUAL f,p, simple zero-diagonal M, disjoint ten-step first-arc layers and Hamilton11 segments. No GF=M/regularity/Latin-column shortcut is introduced. The proof below uses only the adjacency/Hamilton subset of these exact requirements, so discards NO candidate Tuscan-2 array.

## 2. Two elementary genuine-row controls

### 2.1 No separate all-degree2 component

A degree2 cycle component with e edges has two opposite T-cycles of length e. Their row counts r=e/10 are equal. Their raw original-symbol counts are equal because reversing this undirected cycle visits the same split vertices once. Equation(1) then gives identical nonempty row-start sets for the two different T-cycles, contrary to unique starts. Thus no such component exists.

This remains true with repeated original labels on different split copies. It is not a Latin/symbol automorphism argument.

### 2.2 An actual reverse-row pair forces TWO boundary loops

If actual row(a,...,b) and its exact reverse(b,...,a) both occur, the unique row ending b has penultimate symbol equal to the second symbol of the unique row starting b. Hence p(b)=f(b). The same holds at a; a!=b. Thus beta>=2.

More geometrically, their internal opposite turns are local two-cycles and their endpoints are local fixed boundary turns, so these edges form an isolated path component. This is a consequence of actual occurrence, not a license to reverse a row independently.

## 3. Every regime with exactly one ODD long cycle is impossible

Suppose the ONLY long cycle is one odd cycle at center v. At that center its odd support inside ten neighbors leaves an odd remainder. There is at most one off-v fixed point, so it MUST be present; it is p(v)=f(v). At every other center all cycles are two-cycles, with no fixed point because ten is even. Thus beta=1.

The split graph has one odd-degree branch at the copy of v and ONE leaf, also labelled v; all other vertices have degree2. Starting at that leaf and following the degree2 chain must reach the branch: another leaf does not exist, and a degree2 chain cannot enter a cycle without a branch. Let d be the leaf-to-branch distance.

The leaf reflection is the actual row boundary at v.

- If d<=10, the actual row ENDING at this leaf contains the branch's original symbol v within its previous ten edges, and then ends at v again. This contradicts that row being a permutation.
- If d>10, the row ending at the leaf and the row starting there both remain on the degree2 chain for ten edges. They are exact reverses. Section2.2 forces beta>=2, contradicting beta=1.

Therefore this entire regime is impossible. In particular **m=3 and m=5 are both impossible**: with total support3 or5, there can be only the single3-cycle or single5-cycle, respectively, since every long cycle has length at least3. No finite list of candidate arrays is being checked here.

The same argument works at every odd order for any one odd long cycle; it does not depend on T2, on a regular missing graph or on a lollipop face enumeration.

## 4. Exact shape if m=4 were to occur

Then exactly one K_v has one4-cycle; all other off-diagonal cycles are two-cycles. Ten minus four is even, so there is no extra fixed point at this center or any other. Thus beta=0.

The split graph has exactly one degree4 vertex and all other vertices degree2. Section2.1 prohibits any separate cycle component, so it is connected: two edge-disjoint cycles meeting at this degree4 vertex, a figure-eight. Write their lengths a,b; then a+b=55.

The degree4 cyclic order has either three T-faces of lengths a,b,a+b, or one T-face of length2(a+b). To see the two possibilities, pair the ends of the two loops as(12),(34). Composing their return involution with a cyclic order(1234) gives two fixed visits and one2-cycle, hence faces a,b,a+b; an interlacing order(1324) gives one4-cycle and the single110-edge face. End relabeling and inversion preserve these alternatives.

The three-face case is impossible because a+b=55 is not a multiple of10. So the one-face case is forced. Orient and name the loop words A,B so that the actual T-face has the form

`A B A^{-1} B^{-1}`.                                     (2)

Every loop individually is an unordered-edge-simple TRAIL in the original labels, even though its original vertices may repeat. Its reverse in(2) is an ACTUAL portion of the same T-face, not an independently reversed new row.

Because this one face consists of eleven actual rows, its boundary positions form ONE residue class theta modulo10. Let its vertex-coordinate0 be the start of A; the four appearances of the branch occur at0,a,55,55+a. Complete row windows have ten edges and eleven vertices.

We next prove that no theta or loop lengths a,b can work.

## 5. Window lemmas for one unordered-edge-simple trail

Consider any trail `(x_0,...,x_L)` in the original complete graph with no repeated UNORDERED edge. A complete window starting s is the eleven vertices x_s,...,x_(s+10). All windows used below must be permutations of X; these are exactly actual whole rows viewed either forwards or backwards along this same trail.

Suppose two arithmetic grids of window starts have period10. Windows from one grid are actual forward rows, and those from the other grid are actual backward rows. Let d be the smaller distance between their residues, so0<=d<=5. Choose the grid order so a nearest pair starts s,s+d.

### 5.1 d=0: actual reverse partners

One forward and one backward row occupy the identical eleven-vertex window and are exact reverses. In the m4 setting this contradicts beta=0 by section2.2.

A common window exists automatically if L>=19: the first nonnegative common-grid start has s<=9 and s+10<=19.

### 5.2 d=1: duplicate actual endpoint

Both windows s..s+10 and s+1..s+11 are permutations of the SAME X, so x_s=x_(s+11). If the first window is the forward row and the second the backward row, both actual rows START at that symbol. If the grid order is opposite, both actual rows END at that symbol. Either violates unique endpoints.

Such a pair exists automatically if L>=20, because s<=9 and s+11<=20.

### 5.3 d=2 or3: one repeated unordered edge

Since both whole windows are permutations of X, the removed d-vertex prefix at s..s+d-1 and the added d-vertex suffix at s+11..s+10+d have the same vertex SET.

For d2 their two paths each use the same single edge. For d3 each is a two-edge Hamilton path on the same three vertices; two2-subsets of the three edges of K3 intersect. These blocks occupy disjoint position intervals, so either case repeats an unordered edge of the trail.

The needed pair exists whenever L>=19+d, in particular at L>=21 for d2 or L>=22 for d3.

### 5.4 d=4 or5: two neighboring pairs force a repeated edge

Assume that all four windows at starts

`s, s+d, s+10, s+10+d`

are complete. The first pair says that its d-vertex blocks

`P0=[s,...,s+d-1]`, `Q0=[s+11,...,s+10+d]`

have the same d-set S. Each block is a Hamilton path of d-1 edges on S. Their position intervals are disjoint, so together they use2d-2 distinct edges on S.

The next pair similarly gives two paths

`P1=[s+10,...,s+9+d]`, `Q1=[s+21,...,s+20+d]`

on a common d-set S'. The first vertex of P1, x_(s+10), is outside S because the first whole Hamilton window contains S and that endpoint. Its other d-1 vertices are the FIRST d-1 vertices of Q0. Thus H=S intersect S' has EXACTLY d-1 vertices.

The omitted vertex of S is the LAST vertex of Q0. It has degree1 in Q0 and degree at most2 in P0. Hence the first pair uses at least `(2d-2)-3=2d-5` distinct edges INSIDE H. The new vertex of S' is the FIRST vertex of P1; the second pair likewise uses at least2d-5 edges inside H.

There is an important overlap control: Q0 and P1 share d-2 edge POSITIONS. These are allowed to be the same physical edges and MUST NOT be counted as repetitions. They are the ONLY overlapping positions between the first pair's two paths and the second pair's two paths, since d<=5. If no unordered edge repeats at different positions, the two edge families can therefore share at most d-2 edges.

But H spans only binomial(d-1,2) edges. Inclusion-exclusion forces their common edge count to be at least

`2(2d-5)-binomial(d-1,2)`.

For d4 this is3, strictly greater than the2 allowed common positions. For d5 it is4, strictly greater than the3 allowed common positions. At least one common edge must therefore occur at DIFFERENT positions, contradicting the unordered-edge-simple trail.

This is a complete small-graph counting proof; it is not a check by code or an assumption that overlapping subpaths are disjoint.

The two consecutive pairs exist automatically at L>=29+d: choose the first start0<=s<=9, and their last window ends s+20+d<=29+d. Thus L>=33 suffices for d4, and L>=34 for d5.

## 6. The actual two loop grids have offsets separated by5

In the figure-eight face(2), the four loop intervals in global coordinates are

- A:0..a;
- B:a..55;
- A^{-1}:55..55+a;
- B^{-1}:55+a..110.

Actual forward-row starts in A have residue theta modulo10. An actual reverse-A row starting at global coordinate t=theta modulo10 maps to the FORWARD-A window starting `55+a-10-t=45+a-t`. Hence the two window-start residues in A differ by

`Delta_A=a+5-2theta (mod10)`.

For B, use local coordinates with its forward start at a. The forward starts have residue theta-a. A reverse-B row starting at t maps to the local forward window starting100-t, with residue-theta. Thus its two residues differ by

`Delta_B=a-2theta (mod10)`.

These formulas describe ALL complete actual rows contained in those four loop intervals. No column-Latin or discretionary row-reversal assumption is used. In particular

`Delta_A-Delta_B=5 (mod10)`.

Their minimum circular distances are therefore, in some order, exactly one of

`(d_A,d_B)=(0,5),(1,4),(2,3)`.                           (3)

The arithmetic here is a written residue calculation, not an interpreter check.

## 7. Exhaustion of ALL loop lengths and boundary phases at m4

Write L_d for the length of the loop with distance d in(3).

- Pair(0,5): if L0>=19, section5.1 produces actual reverse partners, impossible since beta=0. Otherwise L0<=18, so L5=55-L0>=37; this exceeds34 and section5.4 forces a repeated unordered edge.
- Pair(1,4): if L1>=20, section5.2 duplicates an actual start/end. Otherwise L1<=19, so L4>=36; this exceeds33 and section5.4 forces a repeated edge.
- Pair(2,3): at least one loop has length>=28, since their lengths sum55. That loop exceeds both section5.3 thresholds21/22, forcing a repeated edge.

All possible a,b,theta are covered. The contradiction uses the ACTUAL Hamilton row windows and original endpoint uniqueness. Therefore **m=4 is impossible** for unrestricted Tuscan-1(11), and hence for the requested Tuscan-2(11). This is a full obstruction to the whole noninvolutive m4 stratum, not to a selected construction family.

## 8. Consequence, retained earlier core filters and EXACT residual

The existing written interface excludes all-involutive data at odd order, so m>=3. For clarity, at order11 every off-v involution on ten neighbors has no fixed point; the split graph would consist only of degree2 components, already impossible by section2.1. Values1 or2 cannot be a sum of long-cycle lengths. Section3 excludes3 and5; sections4–7 exclude4. Thus

`m>=6`.

Every original11x11 candidate remains covered: arbitrary row permutations, exact110 adjacent events,99 distinct distance-two events, ALL eleven K_v and actual f/p/GF, simple zero-diagonal M, disjoint ten-step layers and every Hamilton11 segment. GF=M is not assumed, nor cyclic development, regular M, middle-column Latinness, independent reversal or a finite cap. No global asymmetry/canonicalization theorem is used.

The earlier v2 actual-core filters — R>=5, reverse-pair/path correspondence, the seven branched row-count alternatives, beta>=11-R and the exact bad-turn identity `B_bad=m+11-beta-2delta` — are retained as NEW WRITTEN candidates pending their own fresh review. They are not required as unproved premises of the m4 window obstruction or of the m3/m5 boundary argument above.

**First unproved step is now m>=6, not m4.** At support6 there are three actual long-cycle placements: one6-cycle; two3-cycles at one center; or one3-cycle at each of two centers. NONE of those full systems is yet excluded or constructed here; all m>=7 remain as well. Their actual boundaries, Hamilton cuts and simpleM still must coexist. Counting these support types does not itself realize any of them.

No actual11x11 certificate and no contradiction covering all m>=6 is delivered. Therefore the ORIGINAL unrestricted Tuscan-2(11) completion criterion is NOT MET. This packet closes genuine low-support regimes and leaves the exact all-system residual, rather than replacing it by a regular/Latin/symmetric subproblem.

No formal/kernel, human, configured-family, executable or novelty acceptance is claimed. The new lemmas and their shared-position overlap control require a fresh actual written reconstruction before parent use. Old v1/v2 reviews do not transfer automatically. V9/v10/v11/HOLD and the original cutoff/deadline remain unchanged. Following the primary checkpoint, the owner temporarily performs the assigned serial v81-B review and then resumes the actual m>=6 boundary/turn/Hamilton/simpleM problem.
