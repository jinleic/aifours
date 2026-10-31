# v162-B working notes A — reviewer-owned written reconstructions completed so far

Reviewer **PhysicsPPT44-2**. Actual preceding `/bin/date`: **Mon Oct 26 18:30:19 PDT 2026**. These are interim WORKING NOTES inside the released v162-B review, not the review verdict file. Every item below was re-derived by hand in reasoning from the literal packet text (original LF labels). No interpreter, Eval, CAS, program, enumeration or solver was used; the live JS kernel was not touched.

## 0. Literal geometry (re-derived)

- N1={2,3,4,5,6,7}, N2={1,3,7,9,10}, N3={1,2,4,8,9}, N4={1,3,5,8,10}, N5={1,4,6,9,10}, N6={1,5,7,8,9}, N7={1,2,6,8,10}, N8={3,4,6,7,9,10}, N9={2,3,5,6,8}, N10={2,4,5,7,8}. Symmetric; degree sum 52, so 26 edges; no 9-10 edge; matches inputs-v1.json edge list.
- Triangles A=123,B=145,C=167,D=239,E=(2,7,10),F=389,G=(4,5,10),H=(4,8,10),I=569,J=678 are all graph triangles. Their 30 edge-slots cover exactly 25 distinct edges (2-3 in A,D; 3-9 in D,F; 4-5 in B,G; 6-7 in C,J; 4-10 in G,H); the unused edge is 3-4.
- Incidences 1:ABC 2:ADE 3:ADF 4:BGH 5:BGI 6:CIJ 7:CEJ 8:FHJ 9:DFI 10:EGH.
- U_v=V\(N(v)∪{v}) and singleton profiles (all ten rows re-derived): U1={8}|{9,10} star, J_L={J}, J_R={D,E,G,I}; U2={4,6}|{5,8} C4 4-5-6-8, {C}|{F}; U3={5,7}|{6,10}, {B}|{H}; U4={2,6}|{7,9}, {A}|{F}; U5={2,8}|{3,7}, {H}|{C}; U6={2,4}|{3,10}, {B}|{F}; U7={3,5}|{4,9}, {A}|{H}; U8={1}|{2,5} star, {C}|{D,E,G,I}; U9={1,10}|{4,7}, {A}|{J}; U10={1,9}|{3,6}, {B}|{J}. Every other avoiding triangle has an edge trace; none lies inside N(v).
- Automorphisms: pi=(2 5)(3 4)(6 7)(9 10) maps every N(v) to N(pi v) and permutes triangles (A B)(D G)(E I)(F H), fixing C,J. kappa=(1 8)(2 9)(5 10)(6 7) maps N1->N8, N2->N9, N3->N3, N4->N4, N5->N10, N6->N7 and triangles (A F)(B H)(C J)(E I), fixing D,G. Slot orders transform consistently (d3=(A,D,F)->d4=(B,G,H) under pi; d7=(C,E,J)<->d6=(C,I,J)).

## 1. Bodies reconstructed in full so far

RM-S021 (161, hard-input forest): six equal/separate column table; allowed-repeat graph 2-5-9-10-2 plus 6-7 (every exclusion re-derived from the A,B,C,F,H,J equal/separated lists); spanning tree when p6!=p7; 3-component forest {e,p1,p8} (4+1 or 3+2) when p6=p7; at most three values per column (two distinct p-edges in every K_T, including D,E,G,I). Rook lemma and bucket logic consistent with RM-S013. No defect.

RM-S036 (264, two syndromes): C4 trace table for all ten T0 rows (disjoint triangles and traces), Lemma TRACE (singleton or C4-edge; internal C4 neighbours non-adjacent), (FS)/(R1)/(R2) extension, Case I and Case II collision exclusion at the SAME vertex v. No defect.

RM-S028 (206, PATH p3=13): component table; twelve-parameter law; all ten triangle sums for all four rows of the 30-slot array (only cancellation c-c); comparisons 4:{01,03,12,13,23}, 6:{02,04,24}, 7:{14,34} with full N4,N6,N7 (edge 3-4 respected: physical3 nonzero only on label4, unused at 4); hard conditions a,b2,b3,c,f,h1,h2,j!=0,(d,e)!=0,(d,i)!=0 imply (NZ). No defect.

RM-S029 (191, PATH2 p3=02): component table, ten-parameter law, all row sums (cancellation -b+b), comparisons 3:{12,13,14,23,34}, 6:{02,04,24}, 7:{01,03}; hard conditions a,b,c,f,h,j!=0,(d,g,i)!=0 imply (d,e,g,i)!=0. p3=02 subcase forcing and kappa image (01,14,24,13,04,12,23,34,03,02) re-derived. No defect.

RM-S015 (199): FA and FQ iff theorems (E_u components, FA-EQ/FQ-EQ necessity, both sufficiency arrays with all ten sums per row, all comparisons). END-ROLE classification: all six chord values of p3 re-derived independently, giving exactly the eight rows; kappa+(0 4)(1 3) maps row1 to row2 and row7 to row8 exactly. FQ hypotheses for all three p3=04 covers; row-7 law; b2=b3 FA transfer (new rows, d3/d6/d7 inequalities) and e!=0,i12!=i3 pi-FA transfer with label map (3 4); repeated-67 reselections (local defects equal, both singleton profiles differ). No defect.

RM-S008 (116, COMMON-OUTSIDE-NOGO): frame sums; T={1,9,10} independent, meets each non-J triangle in one corner; equivalence to one common C_m translate; exclusions at 1 (star 8-9), 9 (C4 shores 1|7), 10 (C4 shores 1|6); N1 single-service (four distinct d1 tuples); physical9 at most two equal tuples (only rows 3,4 when i=0). No defect.

RM-S013 (235, PIVOT): rook lemma; one-side extension; 1<=>2<=>3; explicit m>=3 family: all ten local defect tuples and all ten obstruction value pairs; (W0)-(W2) global interface. No defect.

RM-S034 (262, THREE): O table (J_L∪J_R) for peripheral and hub (H1)/(H8); monochrome rule; constant hub; both two-block (vertex 2,5,9,10 table rows re-derived); one three-block hub (6.1, 6.2); both three-block: C(e) lists, rows A-D, every cross-pair refinement, exceptional pair forcing (q,q), (Q), pi placement, §7.2 and §7.3 (D in {0,A}). No defect, conditional on the RM-S023 closure routes (to be re-verified from that body).

RM-S014 (213, three-witness m>=3): all ten row sums (T8 cancellations 2-1, 2-2), comparisons 6:S={0,1,3,4}, 3:{12,23}, 2:{02,24}. No defect.

RM-S012 (144, m=2): rows mod 2, d9 collision only 24, all row sums (row4 T2,T3 use 1+1=0), N9 comparisons, pair24 at 4 with (1,1,0) own and N4 zero. No defect.

RM-S035 (203, CRIT): E_u components, (EQ) necessity, (NEQ) via decoder (row-2 own3 = d3(eta_i)-d3(eta2)), all-solutions array with g,k, controls 6.1 (reproduces RM-S014 array exactly at g=k=0) and 6.2 tau family for all m>=2. No defect.

RM-S031 (205, STAR TYPE A): component table, ten-parameter law, all row sums (cancellations -b+b, i-i, -j+j), comparisons 3:S={0,2,3,4}, 6:{12,13,14}, 7:{01}; hard conditions a,b,c,f,h,j!=0,(d,g,i)!=0; affine covariance b_sigma(i)=r_i-r_k. No defect.

RM-S030 (233): star normalization; p2,p5 in {14,24,34}, p9,p10 in {12,13,14}; p3 not 13,24; p4 not 12,34; p3=12 unique cover (34,12,24,34,13,13) incl. failed p4=14 branch; p3=14 four covers; kappa TYPE B (24,34,13,24,12,12) with leaf perm (1 4)(2 3), verified against all tables; pi TYPE D with leaf perm (2 3); TYPE C coefficient law with epsilon/delta; transports A (needs a,c,f,j!=0 and (d,eps e)!=0) and B (needs e,i!=0) with all row sums and comparisons; kappa partner swap; exact complement (RES) with g!=0; G-supported family rows and complete bad-pair table (vertices 5 and 10 each with two choices). No defect.

RM-S032 (196, MIXED): all row sums of the mixed array (eps e+(1-eps)e=e, eps e-eps e=0), comparisons 3:{02,03,23,24,34}, 7:{01,04,14}, 6:{12,13}; needs only a,c,f,j!=0, hence all TYPE C hard inputs including (RES); TYPE D by pi with label perm fixing 0. No defect.

## 2. Packet-content checks already made (bodies still to be re-read in full)

- Kernel-intersection graph (RM-S003 claim, also in checkpoint 076): all 28 peripheral pairs and all hub pairs re-derived; positive pairs exactly 2-3(m),2-7(m^2),3-4(m^2),3-9(m),4-5(m),4-10(m),5-6(m^2),6-9(m^2),7-10(m^2); 6-7 zero because no chosen triangle contains 3 and 4; union of C5 3-4-5-6-9 and C5 3-4-10-7-2 sharing edge 3-4; girth 5; any four distinct selectors induce a forest. Row-mass/Bessel/total-relation/forest-selection logic re-derived.
- Gaussian collapse (RM-S024 claim): congruence diagonalization; |g_lambda|^2=Q via u=s-t,v=s+t (char!=2); centre and pair kernels nonzero; converse monomial; cubic centre zero when gcd(3,Q-1)=1; cofinal 3k-product bridge with Q<p s^k (p^40 for odd f).

## 3. Still required before any whole verdict

Read remaining literal parts 20-30 through their endings; re-read and reconstruct in full RM-S001,S002,S003,S004,S005,S006,S007,S009,S010,S011,S016,S017,S018,S019,S020,S022,S023,S024,S025,S026,S027,S033; then branch-level dependency/application/trust/noncircularity judgments for B00-B13.
