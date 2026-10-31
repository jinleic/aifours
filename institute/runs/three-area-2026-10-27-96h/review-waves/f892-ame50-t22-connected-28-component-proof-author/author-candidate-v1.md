# Actual AME(4,6), N=50/t=22: no connected 28-word E agreement component at any of the 13 profiles

**Status.** NONBLIND, same-harness GENERAL AUTHOR written candidate (f892, AuthorF892AME22Connected). Not reviewed, not adopted; parent disposition is separate. Native clock observed immediately before this exclusive creation: **2026-10-31T04:12:27Z** (an observation before the write, not a certified creation time). No code was prepared or run; there is no code hash.

## 0. Exact statements

**Setting (unchanged actual interface).** ONE normalized complex AME(4,6) state psi in ONE fixed local orthonormal product basis, `U=6 psi`, all three balanced 36x36 flattenings unitary; exactly 50 nonzero entries, exactly 22 of modulus one (the set P), the other 28 nonzero words form E. All amplitudes are arbitrary nonzero complex numbers. The agreement graph joins two distinct E words sharing at least two coordinates. "Connected case" means that E is ONE agreement component. Parties are physical; every pair system, cut and phase refers to this one tensor.

**Theorem A (author claim).** In this setting the E agreement graph is never connected. Equivalently, no such tensor has a connected 28-word residual component, for each of the 13 necessary global E-alphabet profiles `3566, 3666, 4456, 4466, 4555, 4556, 4566, 4666, 5555, 5556, 5566, 5666, 6666`.

**Corollary B (composition with the adopted S5 split exclusions).** No such tensor has global E profile `3566`, `3666` or `4456`. Any tensor of the setting must have `E = C12 ⊔ C16` (two agreement components of sizes 12 and 16, C12 the canonical 2333 gadget by S5) with global profile among the ten profiles `4466, 4555, 4556, 4566, 4666, 5555, 5556, 5566, 5666, 6666`. That 12+16 split is the **exact residual** of the t22 branch; it is NOT decided here.

**Not claimed.** No exclusion of the 12+16 split for those ten profiles; no global support-50 impossibility; no minimum 51; no existence/witness; no novelty, priority, human, independent-family or formal assurance. The conditional t-range imports of S1/S2 are untouched.

The proof uses only actual pair incidence of the same E, the actual seven-K2,2 cut structure, and the four-qubit binary-box bound (whose proof covers arbitrary complex phases). It uses no phase ansatz, no modulus assumption, no independent cut completion, no global t bound, and no finite enumeration. The integral phase criterion is recorded (Section 9) but not needed.

## 1. Imports (named, with packet source)

* **I1 (common incidence).** S6 §1, S7 §1, S8 §1, S10 §1: in each cut the 28 E entries form seven full 2x2 unitary blocks; in each physical pair, 14 E values each with exactly two E extensions and 22 P values, disjoint, covering all 36 values; the pair-mate maps are fixed-point-free involutions; agreement edges are exactly mate relations (two E words sharing a pair value are its two extensions). Elementary and reconstructed in those sources; I re-checked them.
* **I2 (binary box).** Adopted in S4; proofs S6 §4, S8 §2, S10 §2: any 2x2x2x2 box (two symbols per party) contains at most seven E words (eight would close a common 4x4 unitary block in all three cuts, i.e. a four-qubit AME state, excluded by the Pauli argument for arbitrary complex phases).
* **I3 (degrees, profiles).** S4, S6 §§4-5, S8 §§3-4, S10 §1: for an E-used symbol x of party i its number of distinct E partners at party j is the same for every j != i (call it d(x)); x occurs in 2d(x) E words; d(x)>=2; `sum_x d(x)=14` at each party; `3<=q_i<=6`; and trivially `d(x)<=q_j` for every j != i. The necessary profiles are the 13 listed (adopted in S4). In the connected case the component alphabets and component degrees are the global ones.
* **I4 (phase interface, adopted S3).** Flat representative and integral left-kernel even-sum criterion. Recorded only; not used by Theorem A.
* **I5 (adopted S5).** The 12+16 split is impossible at 3566, 3666, 4456. Used ONLY in Corollary B.

Status-only controls supplied no mathematics.

## 2. Lemma 1 (twin closure; no twins when connected)

*Statement.* If two E words differ in exactly one coordinate, the agreement component containing them uses exactly two symbols at that coordinate's party. Hence in the connected case (all `q_i>=3`) no two distinct E words agree in three coordinates; every E word has six distinct agreement neighbours, one per physical pair, each agreeing with it in exactly two coordinates.

*Proof.* Let `w=(a,b,c,d)`, `w'=(a,b,c,d')`, `d!=d'` (order A,B,C,D). The AB, AC, BC values of w each have exactly two E extensions (I1), so all three are `{w,w'}`. In cut AD|BC the column (b,c) contains exactly w (row (a,d)) and w' (row (a,d')); its K2,2 block has a second column (b2,c2) and the words `(a,b2,c2,d)`, `(a,b2,c2,d')`. Here `b2!=b` (else AB=(a,b) would have a third extension) and `c2!=c` (via AC). In cut AB|CD the row (a,b) contains exactly w (column (c,d)) and w' (column (c,d')); its block gives `(a3,b3,c,d)`, `(a3,b3,c,d')` with `a3!=a` (via AC) and `b3!=b` (via BC). In cut AC|BD similarly `(a4,b,c4,d)`, `(a4,b,c4,d')`, `a4!=a`, `c4!=c`. So every "D-twin triple" t has three D-twin triples sharing exactly A, exactly C, exactly B with it, all with the SAME D-pair `{d,d'}`. Let T be the closure and `W=T x {d,d'}`. For `(t,d) in W` its AB, AC, BC mates are `(t,d')`, and its AD, BD, CD mates are the corresponding `(t',d)` produced above; so W is closed under all six mate involutions, hence (I1) a union of agreement components, and it is connected. Thus W is the component of w and its D-alphabet is `{d,d'}`. By party symmetry the same holds for any coordinate. In the connected case this contradicts `q_D>=3`. Distinct mates of one word through different pairs would agree in three coordinates, so the six mates are distinct. ∎

## 3. Lemma 2 (degree-two symbols; forced flat moduli)

*Statement (connected case).* If x at party A has `d(x)=2`, then after naming its two partner symbols at B, C, D as 0,1 its four E words are exactly `(x,i,j,k)` with `i+j+k` even (a parity tetrahedron). Every one of the 13 profiles has a party with `q>=5`, which has a degree-two symbol; therefore the connected agreement graph has a triangle and **all 28 E moduli are forced to** `|U_w|^2=1/2`.

*Proof.* The four words give three balanced 2+2 partitions (by B, C, D). Two equal partitions would put two words agreeing in A and in two further coordinates (twins), excluded by Lemma 1; all three equal would repeat words. So the three partitions are the three distinct balanced partitions of a four-set, which is exactly the displayed parity pattern. Words `(x,0,0,0),(x,0,1,1),(x,1,0,1)` pairwise share A and one more coordinate: a triangle. Along every agreement edge `p_w+p_w'=1` (I1 line norms; S3/S6/S7), so a triangle forces 1/2 and connectivity propagates it. Five or six symbols each of degree at least three would have degree sum at least 15>14. ∎

(This forced flatness is consistent with I4 and is not used below.)

## 4. Lemma 3 (mate exit for a degree-two symbol)

*Statement (connected case).* Let x at party D have `d(x)=2`, with tetrahedron `(a_i,b_j,c_k,x)`, `i+j+k` even. For any x-word w and any pair `{P,Q}` of the parties A,B,C, the PQ-mate of w has D-symbol `y!=x`, and its symbol at the third party `R in {A,B,C}\{P,Q}` lies OUTSIDE x's R-pair.

*Proof.* Coordinate permutations of A,B,C and simultaneous flips of two of them preserve the tetrahedron and act transitively on its words and on the three pairs, so take `w=(a0,b0,c0,x)` and `{P,Q}={A,C}`, mate `u=(a0,beta,c0,y)`. Since w is x's only word with AC value (a0,c0), `y!=x`. If `beta=b0`, u and w are twins (Lemma 1). Suppose `beta=b1`. Then u shares AB value (a0,b1) with the x-word `w'=(a0,b1,c1,x)`. In cut AB|CD the row (a0,b1) is `{w' (column (c1,x)), u (column (c0,y))}`; column (c1,x) contains exactly x's two words with C=c1, namely w' and `(a1,b0,c1,x)`, so the block's other row is (a1,b0) and `(a1,b0,c0,y) in E`. In cut AC|BD the row (a0,c0) is `{w (column (b0,x)), u (column (b1,y))}`; column (b0,x) contains x's words with B=b0, namely w and `(a1,b0,c1,x)`, so `(a1,b1,c1,y) in E`. The row (a1,c0) is `{(a1,b1,c0,x) (column (b1,x)), (a1,b0,c0,y) (column (b0,y))}` (these are the two extensions of AC value (a1,c0)); column (b1,x) contains x's words `(a1,b1,c0,x)` and `(a0,b1,c1,x)`, so `(a0,b0,c1,y) in E`. Hence y has the four words `(a0,b1,c0),(a1,b0,c0),(a1,b1,c1),(a0,b0,c1)`, and together with x's four words the box `{a0,a1}x{b0,b1}x{c0,c1}x{x,y}` contains eight E words, contradicting I2. ∎

## 5. Lemma 4 (square shape and rectangle double covers)

Let X,Y be two parties and let Z,W be the other two. For a pair system let `E_XY` be the bipartite graph on E-used symbols whose 14 edges are the E pair values of XY; a vertex's degree there is its d (I3).

*(a) Square shape.* In the connected case every block of cut `XZ|YW`, with rows (x,z),(x',z') and columns (y,w),(y',w'), consists of the words (written X,Z,Y,W) `(x,z,y,w),(x,z,y',w'),(x',z',y,w),(x',z',y',w')` with `x!=x'`, `z!=z'`, `y!=y'`, `w!=w'`. Any equality makes two of these words twins.

*(b) Double cover.* The XY values of a block are the four distinct cells of the rectangle `{x,x'}x{y,y'}`, all in E_XY. Each E word lies in exactly one block of the cut and each E_XY edge has exactly two words, which lie in different blocks (a block's four cells are distinct). Hence the seven blocks of either cut separating X from Y give a multiset R of seven rectangles contained in E_XY that covers every edge **exactly twice**.

*(c) Links.* A vertex x of degree d lies in exactly d rectangles of R (its 2d words, two per block), each covering two of its d edges; so the Y-pairs of these rectangles form a 2-regular multigraph `L_x` on N(x). Degree 2: one double edge; degree 3: a triangle; degree 4: a 4-cycle or two double edges; degree 5: a 5-cycle or triangle plus double edge. **A link containing a double edge belongs to a vertex of degree 2 or at least 4.** A degree-4 link contains no triangle.

*(d) Degree-two alternative.* If `N(y)={u,u'}` then the two rectangles at y are `{u,u'}x{y,y*}` and `{u,u'}x{y,y**}`. Either `y*=y**` (the rectangle is **doubled** in R) or u and u' are both adjacent to the three distinct vertices y, y*, y**.

## 6. Lemma 5 (doubled rectangles) and Lemma 6 (degree-two neighbours)

**Lemma 5.** If some cut family R contains the same rectangle `{x,y}x{a,a'}` twice and one of its four vertices has degree 2, then both vertices on the other side have degree at least 4.

*Proof.* Name the separated parties D (side of x,y) and A, the cut DB|AC. The two blocks are, in order (D,B,A,C), `(x,b1,a,c1),(x,b1,a',c1'),(y,b1',a,c1),(y,b1',a',c1')` and `(x,b2,a,c2),(x,b2,a',c2'),(y,b2',a,c2),(y,b2',a',c2')`; rows (x,b1),(x,b2) lie in different blocks, so `b1!=b2`. Suppose `d(x)=2`. Then these four x-words are all of x's words, its B-pair is `{b1,b2}`, and `(y,b1',a,c1)` is the AC-mate of `(x,b1,a,c1)`; by Lemma 3, `b1'` lies outside `{b1,b2}`. So a has at least the three B-partners `b1,b2,b1'`, i.e. `d(a)>=3`; the doubled rectangle puts a double edge into `L_a`, so `d(a)>=4` by Lemma 4(c). The same for a'. The roles of the two sides are symmetric (transpose the cut), which covers a degree-two vertex on the A side. ∎

**Lemma 6 (N2).** In every pair graph E_XY of the connected case, every neighbour of a degree-two vertex has degree at least 3. Consequently no E_XY edge joins two degree-two vertices, and if `X_2,Y_2` denote the degree-two symbols, `2|X_2|+2|Y_2|<=14`.
Moreover (**6a**) if `N(y)={u,u'}`, `d(y)=2`, and `d(u)=3`, then y is in the non-doubled alternative, `N(u)={y,y*,y**}` is contained in `N(u')`; if also `d(u')=3` then `N(u)=N(u')`.

*Proof.* In Lemma 4(d), the doubled alternative gives `d(u),d(u')>=4` by Lemma 5; the other alternative gives three distinct neighbours. Edges at `X_2` go to vertices outside `Y_2` and edges at `Y_2` go to vertices outside `X_2`; these edge sets are disjoint. For 6a, degree 3 rules out the doubled alternative. ∎

## 7. Degree multisets used

By I3, a six-symbol party has degree multiset `H1=(2,2,2,2,3,3)` or `H2=(2,2,2,2,2,4)` (`|X_2|=4` or 5). A five-symbol party whose partners all have at most five symbols has one of `P1=(2,3,3,3,3)`, `P2=(2,2,3,3,4)`, `P3=(2,2,2,4,4)`, `P4=(2,2,2,3,5)`; with a four-symbol partner only P1,P2,P3 (degrees `<=4`). A four-symbol party with a four-symbol partner has `(2,4,4,4)` or `(3,3,4,4)`. Every party with `q>=5` has a degree-two symbol.

## 8. Pair lemmas and the profile closure

**Lemma 7 (two six-parties).** Impossible: `|X_2|,|Y_2|>=4` gives `16>14` in Lemma 6.

**Lemma 8 (six-party D beside a party X with a degree-two symbol).** (i) `D!=H2`: a degree-two X vertex needs two D-neighbours of degree at least 3, and H2 has one. (ii) If D=H1 with degree-three vertices t1,t2, then every degree-two X vertex a has `N(a)={t1,t2}`; its rectangles cannot be doubled (Lemma 5 would need `d(t)>=4`), so `N(t1)=N(t2)={a,a',a''}`, a 3-set containing all of `X_2`. (iii) If X is a five-party, then `X in {P1,P3}`. Indeed for **P4**, `X_2` (three vertices) equals `N(t1)`, so the degree-five vertex has all five neighbours among the four degree-two D vertices: impossible. For **P2**, `X_2={a1,a2}`, `N(t1)=N(t2)={a1,a2,a'}`; the rectangles of a1 and a2 are `{t1,t2}x{a1,a2}`, `{t1,t2}x{a1,a'}`, `{t1,t2}x{a2,a'}` (exactly t1's link triangle), so `L_{a'}` has the double edge {t1,t2}; hence `d(a')=4`, a' is the degree-four vertex f, and `L_f` has a second double edge {x,x'} with x,x' degree-two D vertices. Both rectangles of x have A-pair `N(x)={f,n_x}`, so `{x,x'}x{f,n_x}` is doubled, and Lemma 5 (x of degree 2) needs `d(n_x)>=4`; f is the only such vertex. Contradiction.

**Lemma 9 (two five-parties).** The pairs P1P1, P1P3, P3P3, P2P2, P4P4 are impossible. (X side, Y side; subscripts 2,3,4,5 denote degrees.)

* **P4P4.** By Lemma 6 each of `x1,x2,x3` has `N={r,G}` (r of degree 3, G of degree 5) and each of `y1,y2,y3` has `N={s,F}`. Then `N(s)⊇{y1,y2,y3}`, so `N(s)={y1,y2,y3}`, and `N(r)={x1,x2,x3}`. G needs two neighbours besides `x1,x2,x3`, from `{s,F}`, so `G~s`, giving s degree 4. Contradiction.
* **P3P3.** X: `x1,x2,x3` (2), `F1,F2` (4); Y: `y1,y2,y3` (2), `G1,G2` (4). Lemma 6 gives `N(xi)={G1,G2}`, `N(yj)={F1,F2}`; each F and G has exactly one further neighbour, so exactly two edges join `{F1,F2}` to `{G1,G2}`, say `F1G1`. A rectangle covering `F1G1` is `{F1,X'}x{G1,Y'}` with `Y' in N(F1)\{G1}={y1,y2,y3}` and `X' in N(G1)\{F1}={x1,x2,x3}`, needing the edge `X'Y'`, which joins two degree-two vertices. So `F1G1` is covered zero times, not twice.
* **P1P3.** X: `x0` (2), `u1..u4` (3); Y: `y1,y2,y3` (2), `f1,f2` (4). Lemma 6 gives `N(x0)={f1,f2}` and each `N(yj)` is a pair of degree-three vertices with, by 6a, equal neighbourhoods `{yj,·,·}`. A degree-two Y vertex lies in the common neighbourhood of every member of such a class, so these classes have exactly two members, are disjoint, and there are at most two of them. If one class `{u1,u2}` serves all three `yj`, then `N(u1)={y1,y2,y3}` and `u3,u4` have neighbours only in `{f1,f2}`. Otherwise `N(u1)=N(u2)={y1,y2,f}` and `N(u3)=N(u4)={y3,f1,f2}` (u3 cannot meet y1,y2), so f (f1 or f2) is adjacent to x0,u1,u2,u3,u4: degree 5. Contradiction either way.
* **P1P1.** X: `x0` (2), four of degree 3; Y: `y0` (2), four of degree 3. By Lemma 6/6a, `N(x0)={y,y'}` with `N(y)=N(y')={x0,x',x''}` and `N(y0)={u,u'}` with `N(u)=N(u')={y0,y*,y**}`. If `{u,u'}={x',x''}`, then `N(x')={y0,y,y'}=N(x'')`; the vertices `x0,x',x'',y,y',y0` are saturated and the remaining two degree-three X vertices see only the remaining two Y vertices. If exactly one of u,u' lies in `{x',x''}`, say `u=x'`, then `{y,y'}⊆N(x')={y0,y*,y**}` forces `N(u')={y0,y,y'}`, so `u' in N(y)={x0,x',x''}`, contradiction. If `{u,u'}` is disjoint from `{x',x''}`, then `y*,y**` are the two remaining Y vertices; x' and x'' each need one neighbour among them, and not the same one (degree overflow), say `x'~y*`; the link triangle of x' needs a rectangle on `{y,y*}`, i.e. a vertex of `N(y)∩N(y*)\{x'}={x0,x',x''}∩{u,u',x'}\{x'}`, which is empty.
* **P2P2.** X: `x1,x2` (2), `s1,s2` (3), F (4); Y: `y1,y2` (2), `r1,r2` (3), G (4). Each `N(xi)` is a 2-subset of `{r1,r2,G}`; doubling is impossible (Lemma 5 needs two neighbours of degree at least 4). *(A) `N(x1)={r1,r2}`.* By 6a `N(r1)=N(r2)={x1,x',x''}`; x1's rectangles are `{x1,x'}x{r1,r2}`, `{x1,x''}x{r1,r2}`, and r1, r2 need third rectangles `{x',x''}x{r1,rho}`, `{x',x''}x{r2,rho'}`. If `rho=r2`, then `L_{x'}`, `L_{x''}` contain the double edge {r1,r2}, so `{x',x''}={x2,F}`; `L_F` needs a second double edge {g,g'} from rectangles `{F,phi}x{g,g'}`, `{F,phi'}x{g,g'}`; if `phi=phi'` then phi has degree 2 or at least 4, but x1,x2 are saturated; if not, g,g' have degree at least 3, while r1,r2 are saturated and only G remains. If `rho!=r2`, then `rho=rho'` (otherwise x' and x'' both reach degree 4), so `d(x'),d(x'')>=3`, hence `x2` is not in `N(r1)` and can only use G. *(B) `N(x1)={r1,G}`* (the case `{r2,G}` is symmetric). By 6a `N(r1)={x1,x',x''}⊆N(G)` and x1's rectangles are `{x1,x'}x{r1,G}`, `{x1,x''}x{r1,G}`; so `L_G` is a 4-cycle `x1-x'-w-x''-x1`. By (A) for x2, `N(x2)={r_j,G}`, so `x2 in {x',x'',w}`. If `x2=x'` then `N(x2)={r1,G}` and its second rectangle `{x2,x''}x{r1,G}` adds the edge `x2-x''` to `L_G`, which then contains a triangle: impossible. So `x2=w`, `N(x2)={r2,G}`, `N(r2)={x2,x',x''}`, and `L_G` is `x1-x'-x2-x''-x1`. Now x', x'' meet r1,r2,G, and r1, r2 need third rectangles `{x',x''}x{r1,rho}`, `{x',x''}x{r2,rho'}`. If `d(x')=3`, its triangle forces `rho=r2` and then `d(x'')=3`; so `{x',x''}={s1,s2}` and F can only see y1,y2. If `d(x')=4` (x'=F), its 4-edge link `{r1,G},{r2,G},{r1,rho},{r2,rho'}` is 2-regular only if `rho=rho'=sigma` is a new vertex (`rho=G` would give `L_G` a fifth edge, `rho=r2` would give r2 link-degree 3), and then x'' has the same four link edges, so `d(x'')=4` as well: two degree-four X vertices. Contradiction in all cases.

(For contrast, a P1P2 rectangle double cover does exist, e.g. `{u,u'}x{y1,y2,f}` plus `{u3,u4,x0}x{f,s1,s2}` minus `x0f`; hence pairwise covers alone do not decide every mixed five-party pair.)

**Lemma 10 (4456 four-parties).** If D=H1 and A is a four-party with degrees at most 4, then A is not `(3,3,4,4)`. Write `alpha1,alpha2` (degree 3), `beta1,beta2` (degree 4), t1,t2 the degree-three D vertices, D2 the four degree-two D vertices. If some alpha has two D2 neighbours u,v (`N(alpha)={u,v,w}`), then both rectangles of u have A-pair `N(u)` and are among alpha's link rectangles, and likewise for v; so all three rectangles at alpha use the same second column a', `L_w` gets the double edge `{alpha,a'}` (so w is in D2), and `L_{a'}` contains a triangle, so `d(a')=3` and `N(a')=N(alpha)={u,v,w}`; then t1 can only meet `beta1,beta2`. Hence `N(alpha_i)={t1,t2,u_i}` with `u_i in D2`. If `u1=u2=u`, u's rectangles are `{u,t1}x{alpha1,alpha2}`, `{u,t2}x{alpha1,alpha2}` (doubling is excluded by Lemma 5); t1's triangle forces `{t1,t2}x{alpha1,beta}` and `{t1,t2}x{alpha2,beta}`, so `N(t1)=N(t2)={alpha1,alpha2,beta}` and the other beta can only meet three D2 vertices. If `u1!=u2`, then `N(u_i)={alpha_i,beta}` with beta the common third neighbour of t1,t2, so `N(beta)={t1,t2,u1,u2}` and the other beta can only meet two D vertices. Contradiction in all cases. ∎

**Closure (connected case).**

| profile | argument |
|---|---|
| 3566, 3666, 4466, 4566, 4666, 5566, 5666, 6666 | two six-parties: Lemma 7 |
| 4456 | D=H1 (Lemma 8(i), C has a degree-two symbol); A, B have degrees `<=4`; Lemma 10 gives `A=B=(2,4,4,4)`; then both P holes of the 4x4 E-used A-B grid (exactly `16-14=2`) would lie in the row of the degree-two A symbol and in the column of the degree-two B symbol: impossible for two distinct cells |
| 4556 | D=H1; B, C (five-parties, degrees `<=4`) are P1 or P3 by Lemma 8(iii); E_BC is P1P1, P1P3 or P3P3: Lemma 9 |
| 5556 | D=H1; A, B, C in {P1,P3}; any pair: Lemma 9 |
| 4555 | B, C, D in {P1,P2,P3}; equal profiles are impossible (Lemma 9), so they are P1,P2,P3 and the pair P1P3 occurs |
| 5555 | four parties in {P1,P2,P3,P4}; equal profiles are impossible, so all four occur, including P1P3 |

This proves Theorem A. Corollary B follows with I5. ∎

## 9. Cycle/phase conditions of the actual K2,2 agreement graph (deliverable; not load-bearing)

Every square in cut AB|CD is an alternating AB/CD 4-cycle of the agreement graph; in the connected case Lemma 4(a) makes it the antipodal pattern `0000,0011,1100,1111` of one binary box. With `U_w=sqrt(p_w)z_w`, (I1) gives `p_w+p_mate=1` on every edge, and orthogonality of each of the 21 cut-indexed squares `[[a,b],[c,d]]` is `z_a z_d+z_b z_c=0`. Writing `z_w=exp(2 pi i theta_w)` and A for the 21x28 matrix (+1 diagonal, -1 off-diagonal), the system `A theta=(1/2)1` in `(R/Z)^21` is soluble iff every INTEGRAL y with `A^T y=0` has even coordinate sum (I4; Smith normal form; a merely mod-2 relation is not sufficient). Each word lies in exactly three squares, one per cut, and the two words of a square's row have opposite signs; a ±1 odd dependency is therefore an odd set of squares covering each word 0 or 2 times with a balanced sign graph (the eight-word box relation r1+r2-r3 of S6/S8 is one). In the connected case Lemma 2 would additionally force all moduli flat. Theorem A does not evaluate this criterion: the connected case dies before phases are solved, and the arbitrary-phase content enters only through I2.

## 10. Exact local necessities derived (connected case, before the contradiction)

* Alphabet/degree: component alphabets equal the global ones; degree multisets as in Section 7; no twins (Lemma 1); every degree-two slice is a parity tetrahedron (Lemma 2); every degree-d slice induces a cubic three-edge-coloured graph on its 2d words.
* Pair cells: every pair graph E_XY carries two rectangle double covers (one per separating cut); no E_XY edge joins two degree-two symbols (Lemma 6). SAME-P22 incidence consequence: every cell of `X_2 x Y_2` is a P cell, so `|X_2||Y_2|<=q_X q_Y-14`; this inequality is not needed for the proof.
* P moments (from S4/S6/S8 and I3 identities): 3566 `(0,0,3,18,1)`, 3666 `(0,0,0,18,4)`, 4456 `(0,0,8,14,0)`. Recomputed here and NOT used: 4555 has `3n0+n1+n4=1`, forcing `(0,0,9,12,1)`; 4466 has `(0,0,4,16,2)`.

## 11. Boundary cases and limits

* Lemma 1 needs `q>=3` at the twin's party; in the 12+16 split, C12 is built from twins (S5), so Lemmas 2-6 are NOT asserted for the split. Whether a twin-free C16 obeys analogous constraints is not examined here.
* Lemma 4(c): a double edge allows degree 2 or at least 4, never 3. The pair lemmas use only this corrected rule (see Section 12).
* The P1P2 cover in Section 8 shows that pairwise covers do not exclude every mixed five-party pair; the 4555/5555 closures use the pigeonhole on equal profiles plus P1P3.
* Corollary B depends on the adopted scope of S5; Theorem A does not.

## 12. Disclosed process items

* **Self-found error (scratch only).** My scratch note `author-working-notes-02-v1.md` stated that a doubled rectangle forces an isolated K2,2. That is false when a vertex has degree at least 4. It was corrected in `author-working-notes-03-v1.md` and the subsequent notes before this candidate; every argument above avoids it. The six scratch notes (01-06) are exclusive working records in this wave directory, not candidates, and none was edited.
* **Discarded reasoning pass.** After the complete packet read, one reasoning pass was discarded by the runtime output limit before any tool call or file write from it took effect; work resumed from the packet and the notes.
* **Shell use.** Only `date -u` clock observations and `ls -la` of this wave directory (administrative). No scientific code, eval, solver, test, compile, network, external model, Git, deletion, installation or child process.

## 13. Read declarations

Administrative before any body: manifest (294 LF), freeze receipt (271 LF), final binding (223 LF), metadata (284 LF), actual dispatch receipt (62 LF). Initial structured displays of the first four elided nested lines; the elided ranges (manifest 8-291, receipt 10-271, binding 16-223, metadata 22-284, dispatch line 60) were re-read RAW before the ACK. Then all 22 status-only controls RAW through their endings, in manifest order. Parent IRC confirmed the dispatch receipt. I wrote `prebody-ack-v1.md` (3173 B) and sent Main a direct PREBODY ACK, both before any body.

Then part 01 (418 LF; S1-S7) RAW in windows 1-20, 21-40, 41-60, 61-80, 81-100, 101-120, 121-140, 141-160, 161-180, 181-200, 201-220, 221-240, 241-260, 261-280, 281-300, 301-320, 321-340, 341-360, 361-380, 381-400, 401-418 (ending S7|119). Then part 02 (416 LF; S8-S10) RAW in windows 1-20, ..., 381-400, 401-416 (ending S10|139). Every source's LF range was covered completely: S1 1-40, S2 1-15, S3 1-21, S4 1-16, S5 1-34, S6 1-143, S7 1-119, S8 1-141, S9 1-122, S10 1-139. Raw displays showed whole long lines with no truncation marker and consecutive source line numbers across windows; no clipping recovery was needed. Per-window byte sizes were not separately measured. All mathematics started after the part-02 ending.

Declared pins (from manifest/receipt, not recomputed): part01 `7e549ce2caedb45dced3b0d3c4ea73ecfb332bc6babaa107fe811c28d62bde96`; part02 `62f242306558acd9d19f577a0276c442de154f82fc539a7bc18d3fe32f51186a`; S1 `6e0e7704...`, S2 `4c201b80...`, S3 `85878560...`, S4 `4ae01f3c...`, S5 `876bf145...`, S6 `14c09bba...`, S7 `12d2e4c7...`, S8 `edbe988b...`, S9 `34689ded...`, S10 `c6189b12...` (full values in the manifest). No linked original, sibling return, old code, held episode or held consumer was opened; every genuine held episode and all of its consumers remain NONINPUT. Controls were status/permission only. All statements above are unreviewed author claims requiring independent scrutiny and a separate parent disposition; corrections must be additive.
