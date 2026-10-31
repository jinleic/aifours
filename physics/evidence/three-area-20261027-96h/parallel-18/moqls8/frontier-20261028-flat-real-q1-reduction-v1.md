# Real-flat four-MOQLS(8): at most ONE nonclassical member and an exact q1 net obstruction

**PhysicsMOQLS8-2 / physics-4. WRITTEN AUTHOR CANDIDATE; independent proof review and novelty clearance pending.** This is an additive strengthening of `frontier-20261028-flat-real-four-family-heavy-rigidity-v1.md`, SHA256 **c19176626318f4ad2da6b597b5f32013d34d99cf3e4b871b744a69b20fad7568**. No frozen file is changed.

## 1. Result and exact scope

For ANY ordinary actual four-MOQLS(8) family whose FOUR members each admit a (member-specific) real-flat ±1/sqrt8 frame, **AT MOST ONE member is nonclassical**. Thus the entire q2/q3/q4 mixed-classicality strata are excluded inside this explicit subclass. All members may have independent output bases/unitaries and arbitrary cell phases;all original row/column and pair-product ONBs are retained.

If a nonclassical member exists,it has at least24 support-4 cells in the frame of ANY actual chosen first row. Its three companions are necessarily actual classical Latin squares. Their actual q1 net must have at least24 cells satisfying an explicit four-label XOR condition (§4). The q1 case itself is NOT excluded. No statement for arbitrary non-real-flat four-families or a numerical M(8) follows.

## 2. Two exact inherited facts

The complete written predecessor independently proves,from actual QLS/MOQLS definitions:

1. In the frame of any chosen first row of a real-flat QLS(8),each entry has support size1 or4,with a support4 entry having four coordinates of magnitude1/2. Its support is an affine 2-plane after identifying the eight first-row basis labels with F2^3 by the explicit order8 Walsh/Hadamard reconstruction.
2. In an actual real-flat FOUR-family,heavy/support4 cells of distinct members are disjoint;in any row/column containing one heavy,that member has at least four heavy cells there;and an actual nonclassical member has at least24 heavy cells. The last fact uses the predecessor's full no-five-heavy-line and 16-cell 4+4 product-dimension obstruction,not a merely numerical count.

These facts are author-WRITTEN candidates,not presumed reviewed. The new argument below also states exactly the simpler 16-cell consequence it uses.

## 3. Heavy columns are pairwise disjoint; every nonclassical member needs five

Independently standardize the chosen common first row of every member to its own labelled ONB e_j,using separate output unitaries. The first row has no heavy cells in ANY member.

If distinct members Q,R both have at least one heavy cell in the same column j,then Q has at least4 heavy cells in that column and R also has at least4,by the actual column-ONB completeness bound. Their heavy cells are disjoint,so that column would contain at least8 heavy cells OUTSIDE its first-row cell. Only7 cells are available. Contradiction. Therefore the sets of heavy COLUMN labels of all members are pairwise disjoint.

Any nonclassical member has at least4 heavy columns. Suppose it had EXACTLY4,call their label set C. Every heavy row has at least4 heavy cells and has no other heavy column,so its heavy cells are exactly all four columns C. Its four support-4 vectors form an orthogonal part of a row ONB,therefore their support planes all coincide by the predecessor's h=4 line lemma. Call the common support S_i. Each j∈C is excluded by orthogonality to the actual first-row vector e_j in that column. Since |S_i|=|C^c|=4,this forces S_i=C^c for EVERY heavy row.

Thus every heavy column contains mutually orthogonal unit vectors all in the SAME four-dimensional space span(C^c),so there are at most4 heavy rows. The degree lower bound gives at least4. Hence the heavy set has exactly16 cells. The predecessor's §6 proves this ACTUAL 16-board is impossible in a four-family:all three mates are singleton in the complementary 4-space at those cells,and two mates then have32 orthogonal product vectors in a 16-dimensional subspace.

Therefore EVERY nonclassical member needs at least FIVE distinct heavy columns. Two nonclassical members would have disjoint heavy-column sets of total size at least10,but the board has only8 columns. Contradiction. This proves **at most one** nonclassical member,including every possible mixture of the other three. No 20–23 count,choice of a particular support plane,or classicality of the other members was assumed.

## 4. Exact q1 reduction to one actual 5-net

If Q is the sole nonclassical member,its three companions are classical individually. Their independently chosen first-row bases give ordinary Latin symbol maps L1,L2,L3 on the SAME grid,with `L_a(0,j)=j`. Their actual pair-product ONBs imply that every pair of maps is an ordinary pair of MOLS;rows,columns and the three symbol classes are therefore ONE actual 5-net. No affine or catalogue restriction is assumed.

Use the F2^3 labelling of Q's first-row basis obtained from its own real-flat frame in predecessor §2. For any nonfirst-row cell x=(i,j),the four labels

    j, L1(i,j), L2(i,j), L3(i,j)                                 (6)

are pairwise distinct. Indeed each companion excludes j by its own column ONB;the product orthogonality between companions and first-row cell (0,k) excludes two companions having the same k at x.

Orthogonality of Q to the first-row cell (0,j),and to each companion's first-row cell whose symbol equals its value at x,forces Q's support to avoid all four labels in (6). If x is heavy,its support has size4,so it is EXACTLY their complement. By the real-flat Walsh result,this support is an affine2-plane in F2^3. Its four-point complement is also an affine2-plane. Four distinct points of F2^3 form an affine2-plane iff their XOR is0. Therefore EVERY heavy cell obeys

    j + L1(i,j) + L2(i,j) + L3(i,j) = 0 in F2^3.                (7)

At least24 distinct cells of the SAME actual 5-net must satisfy (7). This is a necessary condition only:it does NOT assign phases,prove that the remaining supports form QLS/ONBs,or infer a physical nonclassical witness from a Latin net.

## 5. Exact affine 5-net subcase,not a WLOG net classification

Suppose in addition the F2^3 labels in §4 are identified with the additive group of F8,and the three actual classical mates have the special affine form

    L1(i,j)=j+a i,  L2(i,j)=j+b i,  L3(i,j)=j+c i,

with distinct nonzero a,b,c. These are actual classical MOLS under the usual field algebra. Equation (7) becomes `i(a+b+c)=0`. For every nonfirst row i≠0 this forces `a+b+c=0`.

Thus if `a+b+c≠0`,the q1 candidate has NO heavy cell and Q is classical. If `a+b+c=0`,every nonfirst cell passes THIS XOR screen;no physical Q,global no-go or completion is inferred. This is an exact conditional subcase and is not a claim that arbitrary 3-MOLS nets are affine or that arbitrary field labels preserve a given flat frame.

## 6. Assurance and next step

The predecessor proof and the current heavy-column/XOR arguments are ordinary written mathematics;the earlier complete64-ray/240-ONB census supplies only finite corroboration,not an enumeration of all 5-nets or a formal proof. No novelty/priority/human/configured-family acceptance is claimed. The original unrestricted four-family and even the real-flat q1 case remain open.

Next useful step: analyze actual FIVE-line ONB compatibility of the remaining affine `a+b+c=0` net,or a genuinely nonaffine 5-net,with actual 64 sign rays and exact orthogonality;a feasible support/XOR pattern alone is not a QLS witness. Independently check every row,column and pair-product ONB before promoting any constructed family.
