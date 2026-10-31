# f346 — Binary-sector obstruction and physical exclusions for cyclic 4+6 supports

**GENERAL AUTHOR CANDIDATE — UNREVIEWED.** This is research development, not a no-selected-case written review. It supplies two necessary-condition results for the original 100 pairwise nonparallel rays in C^10 with all 10 row, 10 column and 10 resolution-transversal ONBs. It does not supply a 100-ray witness or an unrestricted no-go.

Own native start observation: **2026-10-30T08:39:44-0700 PDT**, executed after initial document reads, not a timestamp for those earlier reads. Own native observation before candidate preparation: **2026-10-30T08:59:27-0700 PDT**. A substantive checkpoint was recorded separately at that observation. Same-harness author work only; no independent-family, human, formal/kernel, novelty or scientific-acceptance claim.

**Transport:** A direct write of the full candidate to the assigned wave's `author-candidate-v1.md` was refused because this role's write transport accepts only `local://` scratch and `xd://` devices. No shell or alternate working-tree write was attempted. This file supplies the complete candidate for Main materialization; the four full source files named in Section 8 are companion deliverables, already present in the same session scratch. The transport refusal does not qualify or stop the mathematics.

## 1. Results and exact scopes

**Theorem A (entire 5+5 family excluded by a resolution invariant).** Let B be the 30-by-100 zero-one incidence matrix of the row, column and symbol contexts of the resolution Latin square L. Over F2, rank B is either 28 or 27. Rank 27 occurs exactly when L has an index-two quotient: there are balanced maps a,b,c from its rows, columns and symbols to F2, each taking each value five times, with c(L(r,j))=a(r)+b(j). If rank B=27, every orthogonal ray sector has even dimension. Consequently the complete 5+5 physical branch is impossible for every such resolution, including the cyclic square, the explicit dihedral square below, and all their isotopes. A 5+5 candidate at order 10 must have rank_F2 B=28. This imposes no covariance or symmetry on the rays.

**Theorem B (physical rank-four obstruction, not just incidence).** Two ONBs of C^4 sharing exactly one ray, with all other rays pairwise nonparallel, can have at most one additional cross-orthogonal pair after the common ray is removed. This is a universal necessary condition for any four-dimensional sector of the original problem, for any resolution Latin square.

**Theorem C (80 entire cyclic-support families excluded).** Specialize only the resolution to L(r,c)=r+c mod 10 and the support of the four-dimensional sector to H_S={(r,c): c-r in S}, where S is any 4-subset of Z10. The incidence counts are correct exactly when S contains two even and two odd elements; there are 100 such supports. No physical nonparallel four-dimensional realization exists if S contains a nondegenerate three-term arithmetic progression. Nor does one exist if S is an affine image of {0,1,3,8}. Together these eliminate **80 of the 100** balanced circulant supports, with arbitrary complex phases and no covariance assumption on the vectors. The 20 not excluded here are precisely the affine orbits of {0,1,3,4} and {0,1,5,6}, ten supports each. Survival is not feasibility. In particular the formally regular support S={0,1,2,3}, together with its regular six-dimensional complement, is not a physical 4+6 solution.

These are restrictions on specified previously surviving families, not another proof of the irreducible/4+6/5+5 trichotomy. Theorem A removes a full branch for an invariantly defined class of resolutions. Theorems B/C separate regular three-context incidence from exact dimension-four realization.

## 2. Original hypotheses and sector reduction

Use unit representatives q_{r,c} in C^10, with distinct cells having nonparallel rays. Rows, columns and the ten classes L(r,c)=s of a Latin square L are ONBs. Thus a resolution class contains exactly one cell in every row and column. Let H be an orthogonal sector: every ray lies in H or H-perpendicular; write d=dim H. Restricting any of the 30 ONBs to H gives a d-element ONB of H. If x_{r,c}=1 for the H-cells and zero otherwise, then, over the integers,

    B x = d 1_30.                                      (1)

There are 10d selected cells. For a 4+6 branch the selected 40 rays really lie in C^4; for a 5+5 branch the selected 50 really lie in C^5. Merely finding an integer x satisfying (1) does not produce these rays. This elementary sector reduction follows directly from the ONBs and does not use any held Gram or calibration material.

## 3. Proof of Theorem A

A vector z=(a,b,c) in the left kernel of B over F2 is exactly a solution of

    a_r + b_j + c_{L(r,j)} = 0       for every cell.    (2)

The constant solutions, with constant values A,B,C and A+B+C=0, form a two-dimensional space T. If a is constant, fixing a column and varying the row in (2) shows that c is constant, then b is constant. The same argument applies to either other coordinate family. Thus every solution outside T is nonconstant in all three families.

For a nonconstant a, choose a row with a_r=0 and a row with a_r=1. Each row sees every symbol exactly once. Equation (2) therefore says both wt(b)=wt(c) and wt(b)=10-wt(c), so both weights are five. Applying the identical argument to columns gives wt(a)=5. Every nontrivial solution consequently has total weight 15 and defines balanced bit maps satisfying the asserted index-two quotient rule. Conversely such maps give a solution outside T.

There is at most one nontrivial coset modulo T. Indeed if z,z' lie outside T, their a-parts both have weight five, so a+a' has even weight. If z+z' were outside T its a-part would have weight five by the preceding argument, a contradiction. Hence z+z' lies in T. The left-kernel dimension is therefore two or three, and rank B is 28 or 27, respectively. This also proves the exact quotient characterization.

If rank B=27, take a nontrivial z. Reducing (1) modulo two and multiplying by z gives

    0 = z^T B x = d z^T 1_30 = 15 d = d  (mod 2).

So d is even. In particular d=5 is impossible, independently of rank, phase, or nonparallel realization questions downstream. This proves Theorem A.

For L(r,c)=r+c mod 10 use a_r=r mod 2, b_c=c mod 2, c_s=s mod 2. The selected context classes have 5+5+5=15 members, while each cell is incident to an even number of them; an odd-d sector would count an odd total in two incompatible ways. A second explicit family is the Latin square on Z5 x Z2

    L((a,u),(b,v)) = (a+(-1)^u b mod 5, u+v mod 2).

Its second coordinate is the same balanced binary quotient, so the theorem excludes its 5+5 branch too. Independent relabelings of rows, columns and symbols preserve the conclusion. No group-classification theorem is needed for these examples.

When rank B=28, every left-kernel vector is in T and has even weight. Standard finite-dimensional linear algebra then says 1_30 belongs to the column space of B over F2. This is only the absence of this *binary linear* obstruction: it does not supply a zero-one integer selector with d=5, and certainly not physical rays.

## 4. Proof of Theorem B

For two disjoint three-element ONBs of C^3, let U be their unitary change-of-basis matrix. Pairwise nonparallel rays imply that no entry has modulus one, hence every row and every column of U has at least two nonzero entries. U cannot have two zero entries. Two zeros in one row or column violate that degree condition. If the zeros are in different rows and columns, reorder them to U_11=U_22=0. The first two rows must then each be nonzero at their two remaining positions; their inner product has exactly one nonzero summand, at column 3, contrary to unitarity. Thus U has at most one zero.

For two four-element ONBs sharing exactly one ray, remove the common ray and work in its three-dimensional orthogonal complement. The remaining rays are disjoint and pairwise nonparallel, so the preceding fact applies. This proves Theorem B for arbitrary complex vectors and phases.

Operationally, any two sector contexts meeting in one cell must have at most one forced orthogonality between their remaining three cells. The test uses the actual dimension-four ONBs; an abstract incidence or PSD relaxation alone does not justify it.

## 5. Cyclic support balance and the arithmetic-progression obstruction

For L(r,c)=r+c, take H_S defined above. Every row and column contains |S|=4 cells. In the resolution class r+c=l, membership is l-2r in S. For each s with the same parity as l, the equation 2r=l-s has exactly two solutions modulo 10; for the opposite parity it has none. Thus every resolution class contains four H_S cells exactly when S has two elements of each parity. There are binom(5,2)^2=100 such masks.

Suppose distinct a,b,c in S satisfy a+c=2b mod 10. The row-zero sector basis contains the rays at (0,a),(0,b),(0,c). The column-b sector basis contains the rays at (b-a,b),(0,b),(b-c,b), because their differences are a,b,c, respectively. These two bases share only the cell (0,b). Besides this common ray, there are two cross-orthogonalities:

    (0,a) is orthogonal to (b-c,b), because both labels are a;
    (0,c) is orthogonal to (b-a,b), because both labels are c.

The two pairs use distinct rays on each side, since a,b,c are distinct. Theorem B excludes this. Thus every balanced S with a nondegenerate three-term progression is physically impossible in dimension four.

This already eliminates the full affine orbits of {0,1,2,3} and {0,1,2,5}, of sizes 20 and 40. The proof is not a failure to find phases; it holds for all phases. In particular S={0,1,2,3} and its complement have all 30 context counts equal to 4 and 6 respectively, but the four-dimensional side cannot be realized by the required distinct rays.

## 6. A second physical obstruction: S={0,1,3,8}

The progression test does not exclude this S. Nevertheless a short two-plane propagation forces repeated rays. Write x_rc for its putative unit sector ray. Use the following row ONBs:

    R0 = {x00, x01, x03, x08},
    R5 = {x53, x55, x56, x58}.

Both x03 and x08 are orthogonal to both x53 and x58: the pairs (03,53) and (08,58) share columns, while (03,58) share label 3 and (08,53) share label 8. Consequently

    span(x03,x08) is perpendicular to span(x53,x58),
    span(x00,x01) = span(x53,x58).

Since R5 is an ONB, this implies x01 is orthogonal to x55.

The label-zero sector ONB is

    T0 = {x00, x19, x55, x64}.

The ray x01 is orthogonal to x00 (row zero) and to x55 (just proved), so x01 lies in span(x19,x64). It is not parallel to x19, hence its coefficient on x64 is nonzero. The ray x11 is orthogonal to x01 (column one) and to x19 (row one). Taking its inner product with that linear combination proves

    x11 is orthogonal to x64.

Now the row-one sector ONB is

    R1 = {x11, x12, x14, x19}.

The ray x64 is orthogonal to x11 by the previous paragraph, to x14 by column four, and to x19 by label zero. It must therefore be parallel to x12. These are distinct cells, contradicting global nonparallelness. All the displayed cells belong to H_S. This is an exact complex-vector proof, independent of a numerical solver or an enumeration of phases.

For every unit u in {1,3,7,9} and t in Z10, the cell relabeling

    (r,c) -> (u r, u c+t)

sends labels to u(r+c)+t and H_S to H_{uS+t}. Thus the contradiction covers the whole affine orbit of this S, of size 20. It does not assume that any physical ray is related to another by a unitary symmetry.

## 7. Exhaustive count for this particular support family

Here is also a direct count, so the 80/100 conclusion does not depend on a phase search. For a balanced S let E be its even pair and O its odd pair. Each same-parity endpoint pair has exactly one midpoint of the opposite parity. A nondegenerate progression within S can therefore arise only from the E pair with midpoint in O, or from the O pair with midpoint in E. Thus S has zero, one or two such progressions.

Normalize E by an even translation and an odd unit multiplier to {0,2}. If it is the E-pair that supplies a progression, O contains 1. Its other member is one of 3,5,7,9. There are two progressions precisely for O={1,3} or {1,9}; the other choices {1,5},{1,7} give exactly one. There are ten choices of the original E pair, hence 20 two-progression masks. There are 20 possible opposite-parity-center progression triples in total (ten for each endpoint parity), and each extends to a balanced S in four ways. Counting progression incidences gives 2*20 + N1 = 80, hence N1=40. Therefore 60 masks are excluded by Section 5 and 40 are progression-free.

An antipodal pair is {a,a+5}. Ten balanced masks have two such pairs: choose two of the five pairs. They are progression-free, since a nondegenerate progression would need three distinct residues modulo five. Exactly 60 masks have one antipodal pair: choose that pair in five ways, then an even element in four ways and an odd element in three ways excluding its antipode. The 40 one-progression masks all have one antipodal pair: after interchanging parities by an odd translation if necessary, they have the normalized forms {0,1,2,5} and {0,1,2,7}. The 20 two-progression masks have none. Thus among the 40 progression-free masks, 20 have one antipodal pair, ten have none, and ten have two.

Every progression-free mask with one antipodal pair is an affine image of the Section 6 example. To see this, translate the unique pair to {0,5}; normalize the other even element to 2. The other odd element cannot be 7 (a second antipodal pair), cannot be 1 (the progression 0,1,2), and cannot be 9 (the progression 9,2,5, since 9+5=2*2 modulo 10). It must be 3. The normalized set is {0,2,3,5}; multiplying by 9 and adding 3 sends it to {0,1,3,8}. Section 6 therefore excludes all 20 of them.

The total excluded is 60+20=80. The two surviving affine orbits have representatives {0,1,3,4} and {0,1,5,6}, ten elements each; the exact finite enumeration below also records the orbit sizes. For completeness, the first representative has at least ten distinct translates, and is stabilized by (u,t)=(1,0),(9,4),(3,1),(7,3), so its affine orbit has exactly ten elements. The second representative is any choice of two antipodal pairs, and affine transformations are transitive on those ten choices. This last partition asserts only which supports survive these necessary conditions. Neither surviving orbit, its dimension-six complement, nor any complete 100-ray array is constructed.

## 8. Reproducible calculations actually exercised

All four calculations used only Python standard-library integer arithmetic, finite bit masks and set operations, ran locally with a 60-second tool bound, and completed in well under one second. No optimizer, floating-point Gram/phase feasibility test, package install, heavy solver or remote campaign was used. The printed elapsed times are monotonic process durations, not wall-clock launch receipts. The only floating values in the outputs are those timing measurements.

Complete source bodies accompany this candidate as:

1. `f346-sector-obstructions.py` (scratch: local://f346-sector-obstructions.py). Executed command: `python3 local://f346-sector-obstructions.py`. Observed duration 0.06058229226619005 seconds. Output: cyclic incidence rank over F2 27; one-intercalate-traded Latin square rank 28; all thirty counts 4 for S={0,1,2,3}, all thirty counts 6 for its complement; 527 necessary 4x4 unitary supports; 100 balanced circulant masks, 20 excluded by the original *two-row-only* support test, 80 not excluded by that weaker test. The trade swaps columns 0 and 5 within rows 0 and 5. Both resulting row/column Latin conditions were checked by this finite calculation. Rank 28 is not a ray witness.
2. `f346-intersecting-bases.py` (local://f346-intersecting-bases.py). Executed command: `python3 local://f346-intersecting-bases.py`. Observed duration 0.023734459187835455 seconds. Checks only pairs of the original 30 contexts sharing one sector cell. Exactly 60 masks have at least two remaining forced cross-zeros; 40 survive this test. The script returns concrete context/cell certificates for each exclusion. This is not a phase search.
3. `f346-four-sector-closure.py` (local://f346-four-sector-closure.py). Executed command: `python3 local://f346-four-sector-closure.py`. Observed duration 0.17966004088521004 seconds. Exhaustively enumerated necessary support masks of sizes 2,3,4: respectively 1,10,527. These obey row/column support degree at least two and forbid exactly one common nonzero position for two distinct rows or columns. All actual disjoint nonparallel change-of-basis supports obey these rules, but the rules need not be sufficient. It examines every affine orbit of balanced S, all 4-cliques of forced orthogonality, and exact support consequences. Output orbits: {0,1,2,3}, size20, excluded; {0,1,2,5}, size40, excluded; {0,1,3,4}, size10, not excluded, 30 bases and 180 orthogonal edges; {0,1,3,8}, size20, excluded; {0,1,5,6}, size10, not excluded, 40 bases and 180 edges. No extra edges were forced in the two surviving representatives.
4. `f346-closure-proof-log.py` (local://f346-closure-proof-log.py). Executed command: `python3 local://f346-closure-proof-log.py`. Observed duration 0.19859412498772144 seconds. Extracts the proof consequences for S={0,1,3,8}, starting with 35 forced 4-cliques. First it compares R0 and R5: forbidden mask39234 has the sole necessary support26265, forcing (00,56) and (01,55) orthogonal. Next it compares label0 with column1: forbidden mask289 has candidate supports23130,38550,57054, all forcing (64,11) orthogonal. Finally label0 and row1 share19; the remaining3x3 forbidden mask320 admits no necessary support. Section 6 reconstructs these consequences directly in vector geometry and does not depend on accepting the enumeration as a proof of unitary sufficiency.

The difference between 20,60 and80 exclusions is intentional: they are increasingly strong necessary tests, not contradictory feasibility counts. A passed support test is never called a physical solution. The counts and exact code are author-owned evidence, not disjoint verification. Timings are reproduced literally above, not estimates.

## 9. Input/procedure receipt and chronology

The complete manifest, receipt and literal packet were read first, including all endings. The packet was initially read before the six controls; subsequently all six controls were read completely, followed by complete original S1/S2 bodies, before deriving this candidate. This order is disclosed rather than described as a cognition or provenance certificate. No links from held diagnostic records, the separately cited 95/90-ray candidates, or the held full-Gram/calibration episodes were followed. Status/permission controls supplied no scientific premises.

Own executed SHA-256 and `wc -cl` checks matched all manifest/receipt/packet/control/source pins. The later parent-supplied metadata file was also read; its 08:47:07 PDT observation is parent-supplied, not my own launch time or execution. Own additional native observations were 08:47:15, 08:53:44, 08:56:11 and 08:59:27 PDT. Exact wall-clock times of private algebra and individual calculation launches were not separately measured. The experiment order was the four scripts listed above, followed by the hand reconstruction and count in this candidate; no independent review or formal verification was performed.

Verified frozen metadata (SHA-256 / bytes / LF):

- manifest-v1.json: 2cab4719496a1a922b52727326de7b5f6f2330089eebecaec010ce970971f2bc / 5372 / 80.
- freeze-receipt-v1.json: 5a2e2ff4aab1e7c8806c02db9b06638ed8868cf274979ae003113458b953645f / 1891 / 47.
- literal-packet-v1.md: 01142327203616b38dbde6c9f2afc561d83a72dd6dc42539c0fed577c8b00a36 / 8557 / 68.
- prospective-author-method-scope-restoration-20261030-v1.json: 6ab69778c11dbfc4ac895f97b381cc70d0059a5723d6b02f62b9957c7e8dcd95 / 1884 / 15.
- contract-addendum-2-frontier-first-owner-direction-v1.json: 5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce / 3210 / 14.
- parent-L1-selected-diagnostic-release-quarantine-v1.json: ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f / 3103 / 23.
- parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json: e4d6f1e49cb18aced7735cf025dee54830400554c9adc08138250ae9f0523efc / 2356 / 11.
- parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json: 23fa29449cef8e02d981efc021934e4cec16960ca6bfe8f6f2178bbd048c85b4 / 1776 / 9.
- parent-ame-held-compression-claim-consumer-quarantine-v1.json: c307e902eee5f3736aab0e2437738898382b3d3083f6c307118219b9a4c875b0 / 1439 / 8.
- S1 `dispositions/physics-5-rqls10-maximal-commutant-trichotomy-parent-v1.md`, complete lines1-11: 4018563797c35eb283b407f4503903dd9850b30f7b9888373909d3faac062e3d / 2892 / 11.
- S2 `physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-20261029-maximal-1rqls10-commutant-trichotomy-v1.md`, complete lines1-55: 37b62f6eefc4b5d0e4ac57c91f9c521473b13deb0465468e24a3daad98c982bc / 5251 / 55.

S1 and S2 paths are those named by the frozen manifest; S1 supplies the explicit original transversal qualification, while S2 is the allowed mathematical structural source. No status claim of earlier acceptance is used as proof of the new results. No public source was used, so no public-source novelty comparison is claimed.

## 10. Unpaid boundaries and exact original-target relation

- The irreducible original branch is not decided.
- The general 5+5 branch for rank-28 resolution incidence is not decided. Its binary feasibility is not integer support feasibility or physical feasibility.
- The general 4+6 branch is not decided. Noncirculant supports, other resolutions, the 20 surviving cyclic masks, and all dimension-six complements remain unconstructed and unobstructed by this candidate except as specifically stated.
- No 100 vectors, 30 exact ONB checks, full dimension-ten rank certificate, global phase solution, or all-pairs nonparallel witness is supplied. No numeric failure is used as a no-go.
- No disjoint written check, parent adoption, human/formal check, independent-family assurance or novelty clearance has occurred. All claims here remain AUTHOR/UNREVIEWED.

The deliverable is the explicit branch-family obstructions above and their reproducible finite support evidence. It does not recast that limited progress as a solution of original 100-ray existence.
