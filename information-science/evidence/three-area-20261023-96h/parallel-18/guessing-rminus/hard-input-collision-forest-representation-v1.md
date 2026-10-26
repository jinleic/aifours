# R-minus arbitrary five labels: the global hard-input collision forest

Owner `InfoGuessingRminus-2`, info-5. Actual checkpoint clock receipt: `/bin/date` returned **Sun Oct 25 13:58:33 PDT 2026** before this body.

**NEW WRITTEN representation of the ENTIRE no-common-pivot five-label residual**, not another selected-family assumption. Allm>=2, composite/nonlinear interfaces retained. This paper gives necessary GLOBAL structure, NOT an actual guessing-number improvement or a universal section/Hall proof. No scientific interpreter/program, symbolic kernel, enumeration, replay, CLI or nested agent. Every deduction is written graph/equality reasoning, not machine-checked.

## 1. Exact input and why this is the whole hard residual

Take ANY five distinct actual syndrome rows eta0=0,eta1,...,eta4 on the original ten triangles

`T1=123,T2=145,T3=167,T4=239,T5=(2,7,10),`

`T6=389,T7=(4,5,10),T8=(4,8,10),T9=569,T10=678`.

Use A,...,J for these column labels only. Actual physical words retain all thirty incident Z_m slots and the complete26-edge R-minus neighbourhoods. No syndrome coefficient may be normalized by a field operation or arbitrary per-column relabeling.

If ANY vertex admits a common-pivot confusion section for these rows, that actual section already gives an injection of arbitrary outside FD subsets into their ACTUAL R(A). The remaining section problem is therefore exactly the case in which NO original vertex admits such a section. We reduce that entire case below; this is not a theorem that no global section exists.

The ordinary actual SECTION/removal interface is from the complete literal triangle-code proof. The common-pivot criterion has the full written proof in `five-label-common-pivot-obstruction-and-bucket-hall-v1.md`, SHA256 `742b96fa2c5bb954134d9d8ebeef1ecc643d53f2b31d5f8bc21a9ad5548e1030`; it is a named WRITTEN input, not a newly accepted formal/family gate. The needed logic is reconstructed next so this representation does not depend on a headline.

## 2. Exact bad-pair extraction, including multi-label local buckets

Fix original v and partition the five rows by equal full d_v. Put U_v=V\(N(v) union{v}). The literal induced graph on U_v is complete bipartite, with parts and singleton-trace profiles

|v|L_v|R_v|J_L|J_R|
|---|---|---|---|---|
|1|{8}|{9,10}|{J}|{D,E,G,I}|
|2|{4,6}|{5,8}|{C}|{F}|
|3|{5,7}|{6,10}|{B}|{H}|
|4|{2,6}|{7,9}|{A}|{F}|
|5|{2,8}|{3,7}|{H}|{C}|
|6|{2,4}|{3,10}|{B}|{F}|
|7|{3,5}|{4,9}|{A}|{H}|
|8|{1}|{2,5}|{C}|{D,E,G,I}|
|9|{1,10}|{4,7}|{A}|{J}|
|10|{1,9}|{3,6}|{B}|{J}|

Here J_L/J_R list precisely triangles with a singleton U_v trace in the indicated shore. Other chosen triangles avoiding v have an EDGE trace, one vertex on each shore; triangles through v have their other two corners in N(v). No chosen triangle lies entirely in N(v).

A same-bucket representative difference zero on N(v) is also zero at v, by the actual decoder. Its support is inside U_v. It is confusing IFF its changed physical support lies entirely in ONE shore: if both shores have changes, every changed vertex has a changed neighbour; if just one shore changes, any changed vertex witnesses confusion.

A difference syndrome has a representative on L_v precisely when its J_R profile is0: necessity follows from the opposite singleton traces, sufficiency by assigning each required triangle sum to its L corner. All slots are independent, and all through-v differences are0. The R version is symmetric. This uses only additions in Z_m, no division.

For a WHOLE bucket, a pairwise-confusing family supported on L union R must choose ONE shore globally. The two-shore rook lemma proves it: if two points differ on L, they agree on R; any point differing on R would have to match both L values, impossible. Conversely, if one opposite singleton profile is constant on the bucket, choose one representative for its base row zero on N(v), and construct ALL relative rows on the compatible shore. Different buckets then compare at v itself. Representatives for each base exist because no triangle is fully inside N(v).

Thus a common-pivot section exists IFF EVERY equal-d_v bucket has at least ONE of its two singleton profiles constant.

If no common-pivot section exists, some bucket has BOTH profiles nonconstant. The same rook lemma on the TWO PROFILE VALUES shows there must be a PAIR whose two profiles BOTH differ; otherwise all profile pairs would be rook-adjacent and one entire profile would be constant. This handles arbitrary bucket sizes, not merely one equal pair.

Therefore for EACH v choose ONE such actual pair p_v of class labels. Bind all ten choices simultaneously, with the SAME global five labels. Then

`d_v(eta_i)=d_v(eta_j)` for p_v=ij,

but BOTH opposed singleton profiles differ. At peripheral vertices those are scalar inequalities. At the two hubs, the four-coordinate profile differs in AT LEAST ONE of D,E,G,I, and the other profile is the scalar J or C.

This is an actual obstruction-pair cover extracted from the given data, not arbitrary independent local partitions.

## 3. Six shared equal/separate columns

For every triangle column T let K_T be the graph on the SAME five labels containing the three edges p_v at its physical corners. Actual eta_T is constant on every connected component of K_T, because its scalar values agree along all three declared local-pair edges.

In particular, if some pair has different eta_T values, its endpoints CANNOT be connected in K_T. This is elementary graph-path propagation of equality, valid for every m; it is not substituting a prime-field rank for the actual modular equations.

The extracted bad-pair cover forces this entire table:

|column|three equal-pair edges in K_T|three pairs separated by actual scalar values|
|---|---|---|
|A=T1|p1,p2,p3|p4,p7,p9|
|B=T2|p1,p4,p5|p3,p6,p10|
|C=T3|p1,p6,p7|p2,p5,p8|
|F=T6|p3,p8,p9|p2,p4,p6|
|H=T8|p4,p8,p10|p3,p5,p7|
|J=T10|p6,p7,p8|p1,p9,p10|

For example p2 differs at C and F, p6 at B and F, p7 at A and H; the hub8 pair differs at C and hub1 pair at J. All equal and separated edges in this table refer to the SAME fixed p_v and original rows, not different local normalizations.

Two additional hub constraints must remain:

- p1 differs in at least one of columns D,E,G,I;
- p8 differs in at least one of D,E,G,I.

No choice of WHICH one is fixed here, and neither disjunction may be dropped in a future converse or case classification.

## 4. Exact allowed-repeat graph: only a four-cycle and one edge

An equal edge and a separated edge in the same column cannot be the SAME label pair. Applying this to all six rows of the table yields

|physical v|ONLY other vertices at which p_v may possibly repeat|
|---|---|
|1|none|
|2|5,10|
|3|none|
|4|none|
|5|2,9|
|6|7|
|7|6|
|8|none|
|9|5,10|
|10|2,9|

This can be checked directly by cross-reading the equal and separated lists: e.g. p2 is excluded from p1,p3,p4,p6,p7,p8,p9, leaving only5and10; p3 is excluded from ALL nine other positions. The complete possible-repeat graph is exactly

`2--5--9--10--2`, together with `6--7`,

and isolated physical1,3,4,8.

This is an UPPER bound on possible equalities, not a claim that every allowed repeat is realizable. All four isolated positions have globally unique collision-pair colours. No colour can occur at THREE positions because the allowed-repeat graph has no triangle. Doubles are disjoint edges of this graph; at most two occur in its four-cycle and one on67. Thus there are at least seven distinct LABEL-pair colours among the ten p_v.

Do NOT confuse this with the separate witness-palette theorem. Here p maps PHYSICAL VERTICES to local COLLIDING LABEL PAIRS. A confusion-section witness assignment f instead maps LABEL PAIRS to PHYSICAL VERTICES with NONZERO own defects. The directions and meanings are opposite; p_v itself CANNOT be witnessed at v. There is no conflict between seven-or-more distinct p colours and at-most-eight physical f colours.

## 5. The decisive collision forest on five label vertices

All following edges are edges of K5 on the ACTUAL global labels0,...,4, not edges of the physical graph. Label0 remains the distinguished baseline in any future classification.

### 5.1 Distinct p6,p7 force a spanning tree

Suppose p6!=p7. They are two distinct simple edges, hence form an acyclic graph H with three components.

The J column has equal graph `{p6,p7,p8}` and SEPARATES p1. Therefore p1's endpoints are not connected even after p8 is added, and in particular not connected in H. Adding p1 to H reduces the component count from3to2 without a cycle.

The C column has equal graph `{p1,p6,p7}` and SEPARATES p8. Therefore p8's endpoints are still not connected after p1, and adding it reduces components from2to1 without a cycle.

All four edges are distinct (p1,p8 are globally unique by Section4). Thus

`{p1,p6,p7,p8}`

is a SPANNING TREE on the five global labels. No scientific modular field was introduced; this is a literal forest/path argument.

The underlying unlabeled tree is one of the three five-vertex tree shapes: the four-leaf star, the five-vertex path, or the degree-three fork with one extended arm. Future work MUST also retain which tree edges are p1,p6,p7,p8, all placements of the distinguished baseline0, the other SIX actual p_v, both hub disjunctions and all actual syndrome coefficients. A tree shape alone does not settle them.

### 5.2 Equal p6,p7 force a two-component forest

If p6=p7=e, the same two separation arguments say p1 is not closed by `{e,p8}` and p8 is not closed by `{e,p1}`. Thus e,p1,p8 are three distinct acyclic edges on the five labels. Their two components have sizes

`4+1` OR `3+2`.

The previously studied law p1=01,p6=p7=23,p8=04 is ONE3+2 example. Its additional choices p2=12,p3=02,p4=03,p5=13,p9=24,p10=34 give the specific sixteen-parameter stratum with known transport. Nothing here proves that all3+2 covers are that law, nor that4+1 or the spanning-tree branch is empty.

## 6. Every actual scalar column has at most three values — but values cannot be normalized away

Each chosen triangle's three p edges include at least TWO distinct edges. For A,B,F,H this follows from the globally unique corner positions1,3,4,8. C,J may repeat6/7 but have the unique hub edge. D=T4 has the unique3 edge; E=T5 has p7 distinct from p2,p10; G=T7 has unique4; I=T9 has p6 distinct from p5,p9. Thus no K_T is only one repeated edge.

Two distinct simple edges have rank at least2 as a forest/path relation on five vertices, so K_T has at mostTHREE connected components. Actual eta_T is constant on each; hence ANY hard input has at most THREE ACTUAL VALUES in EACH of its ten scalar syndrome columns, no matter how large or composite m is.

This is NOT permission to rename those values0,1,2. They can be arbitrary elements/nonunits of Z_m, and changing scalar values independently need not preserve original triangle sums or a section construction. Keep one actual Z_m parameter per K_T component, zero on the component containing baseline0, and retain all declared nonzero inequalities/disjunctions. At m2 additional value identifications can occur and must be retained. No field-rank or scalar-normalization shortcut has been authorized.

## 7. Exact remaining representation and scientific ceiling

The ENTIRE no-common-pivot arbitrary-four-syndrome input is now represented by

1. ONE obstruction cover p_v on the actual five labels;
2. the exact repeat-exclusion graph of Section4;
3. either the Section5 spanning tree or its two-component forest, with all distinguished labels/edge roles retained;
4. ALL ten K_T built from that SAME cover and ALL actual modular component values;
5. ALL scalar separation constraints in Section3 and BOTH hub disjunctions.

Every actual hard input supplies such data; no independent local partition or selected five-label family replaces it. The data are necessary only. This paper does not assert every abstract cover is realizable with distinct global syndrome rows, or that proper-colouring the columns supplies original FD outside words. The actual rows must stay pairwise distinct, and genuine winning-trade claims still require ALL original FD subsets and their actual removal union.

**Next missing proof:** construct a globally shared actual confusion section or a more general actual-removal Hall map for EVERY resulting tree/forest coefficient family, or produce exact original FD outside data with positive actual gain. The known sixteen-parameter law and its all-modulus family completion cover real subcases but cannot be silently substituted for the other covers or degeneracies. The universal at-most-eight-witness reduction is a separate necessary condition on f, not a solution of this p problem.

Thus this is a NEW exact barrier/next-representation record and a global hard-case reduction, NOT numerical gn progress. Certified20/3..1847/276 and the unmet T300 stronger gate remain unchanged. No formal/kernel/configured-family/human/executable/novelty assurance or round completion; all v9/v10/v11/HOLD, exclusive-root, cutoff/deadline and continuation rules remain binding.
