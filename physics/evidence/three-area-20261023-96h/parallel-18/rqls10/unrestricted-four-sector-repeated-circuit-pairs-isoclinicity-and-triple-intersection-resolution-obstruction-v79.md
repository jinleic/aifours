# RQLS10 v79 — ALL repeated actual circuit pairs: forced isoclinicity, partial-transversal capacity, no triple intersection

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 17:25:59 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written two-projection/actual-ray/matching/cardinality arguments only; no scientific Eval/interpreter/arithmetic/CAS/enumeration/native program/solver/replay/private approximate scout/chosen angle/state/control/probe.

**SEPARATE FUTURE ONLY:** Main's frozen v17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 are UNCHANGED. This is outside those gates; no admission/read/adoption or old-verdict inheritance.

## 1. Entire actual all-SPARSE family and circuit-intersection representation

Use the COMPLETE v76 five-row-type true common E4 graph and v77 actual sparse local frames, not a chosen graph or freely chosen Eulerian decomposition. The five vertices are the actual pairs of original rows. The ten edges are actual original columns. Every vertex has four incident edges; its eight E4 rays occupy its TWO original rows and those FOUR actual columns. The graph is connected, loopless and 4-regular with parallel edges retained.

At EVERY SPARSE vertex, v77's complement pairing is unique and comes from the actual zero-diagonal unitary. Following these pairings produces actual projection circuits. Each circuit is vertex-simple, has length 2 through 5, and carries ONE fixed unordered rank2 projection pair {P_C,I-P_C}. Every original graph vertex lies on EXACTLY TWO DISTINCT such circuits: one circuit cannot visit it through both local pairs. The four local incident edge planes are precisely the two pairs of those two circuits.

Define H with one vertex per actual circuit and one edge per original graph vertex. Its edge v joins the TWO circuits meeting at v. Thus H has EXACTLY FIVE edges, no loops, and degree at C equal to that actual circuit's length, hence between 2 and 5. It is connected: a disconnected circuit-incidence graph would separate all original graph edges and vertices into disconnected original components. H is a multigraph; NO parallel intersection is discarded and no cycle or projection angle is selected.

For an unordered pair {C,D}, let m_CD be its edge multiplicity in H, equivalently the number of actual original row-pair vertices where precisely C,D meet. The sector-cell set A_CD consists of EIGHT actual cells per such vertex and therefore has 8m_CD cells. These sets partition all forty E4 cells.

The claims below quantify over ALL actual all-SPARSE arrays with these data, all circuit counts, all complex frames, all endpoint/interior principal angles, and arbitrary geometry in the E6 complement.

## 2. Repeated intersections force isoclinicity already for ordinary 100-ray maximality

Fix any C,D with m_CD at least TWO. Set P=P_C and Q=P_D, choosing either orientation of each pair once. At every vertex of A_CD, v78 section2 gives an ACTUAL rank2 projection R_v commuting with P,Q, with rank(P|R_v)=rank(Q|R_v)=1 and the same ranks on R_v-perp. All eight local cell rays lie in R_v or its complement. Relabeling an oriented edge pair changes none of these statements.

Use the COMPLETE two-projection CS decomposition proved in v78 sections3-5. Its two eigenvalues lambda1,lambda2 of PQP on rangeP lie in [0,1], and ALL endpoints are included. If lambda1 differs from lambda2, the same local commutant/rank argument gives R_v equal to one of the FIXED central CS planes H1,H2 at EVERY C,D intersection. This is a statement about this fixed pair P,Q only, not all other circuits.

Each CS plane has a ONE-dimensional intersection with rangeP and a ONE-dimensional intersection with kerP. At each C,D vertex, the two actual rays in its P edge plane are exactly those two rangeP lines, one in each central plane; likewise its I-P edge supplies the two fixed kerP lines. These FOUR actual P-pair rays are therefore the SAME four projective rays at EVERY C,D vertex. This includes the unequal endpoint case 0/1: the four common eigenlines are fixed, and the two local rank restrictions exclude mixing one line from each endpoint block.

Two distinct intersection vertices consist of distinct original rows and distinct cells. Consequently m_CD at least two and unequal lambdas produce actual duplicated cell rays, contradicting ordinary 100-ray maximality ALREADY, without any quantum-transversal or full-resolution assumption. No extension of a local projector to all100 rays is invoked here.

If both lambdas equal 0 or both equal 1, Q=I-P or Q=P, respectively. These are impossible at even ONE actual sparse intersection, because v77's cross-pair traces are strictly between 0 and 2.

Thus EVERY repeated circuit pair in an ordinary MAX100 array is isoclinic with one unrestricted lambda_CD in (0,1):

    P Q P = lambda_CD P,    Q P Q = lambda_CD Q.

Equivalently its rank2 reflections A=2P-I and B=2Q-I obey

    A B + B A = 2(2 lambda_CD-1) I4.

These are written matrix identities from the complete CS form, not computed tests. Different repeated pairs may have DIFFERENT lambdas and DIFFERENT identifications. No simultaneous global tensor representation is assumed.

## 3. Exact local product coordinates for ONE repeated pair, without global WLOG

For this fixed isoclinic pair, v78 section6 supplies a physical identification H4=C2_first tensor C2_second with P=|p+><p+| tensor I and Q=|q+><q+| tensor I. The four first-factor rays p+,p-,q+,q- are distinct; every cross-basis overlap is nonzero, since 0<lambda_CD<1.

At each C,D intersection v, its commuting R_v is I tensor |u_v><u_v|. The EIGHT actual local rays are EXACTLY

    {p+,p-,q+,q-} tensor {u_v,u_v-perp}.

Each first-factor ray belongs to EXACTLY ONE of that vertex's four actual incident columns, with its two second-factor rays in the two original rows of that column. This is actual row/column incidence, not an arbitrary Cartesian relabeling of cells.

Global ray distinctness forces all 2m_CD second-factor rays to be distinct: a coincidence between vertices would repeat the actual product ray with first factor p+. For distinct vertices v,w, EVERY second-factor overlap between their two bases is therefore NONZERO, because the orthogonal partner of a qubit ray is unique.

These coordinates and the distinctness implication apply to the ENTIRE set A_CD. They say nothing about rays at other circuit-pair classes; those other frames need not share this first/second-factor identification.

## 4. Strong partial-transversal lemma: at most TWO cells from any repeated-pair class

Let S be ANY subset of cells in A_CD with mutually orthogonal rays and with distinct original rows AND distinct original columns. We prove |S| at most TWO, not merely the absence of a four-ray ONB.

Group S by its original row-pair vertex. Distinct vertex groups have all second-factor overlaps nonzero. Orthogonality of every selected ray across groups therefore makes their FIRST-factor spans pairwise orthogonal in C2. Hence at most TWO vertex groups can be nonempty.

One vertex group can contain at most TWO selected cells, because it has only TWO original rows. If |S| were at least three, at least two groups would be present and one would contain TWO selected cells. The two nonzero first-factor spans must both have dimension ONE. Thus those two cells at the same vertex have the SAME first-factor ray.

But the two actual cells with that first-factor ray at that vertex occupy the SAME incident edge column, as established in section3. This contradicts distinct columns. Three or more groups are independently impossible because C2 cannot contain three nonzero mutually orthogonal subspaces. This proves the bound in all cases.

For a pair class with m_CD=ONE, the SAME numerical bound at most two holds trivially from its two original rows, whether or not its pair is isoclinic. Thus every circuit-pair class A_CD contributes at most TWO cells to ANY quantum transversal in an ordinary MAX100 all-SPARSE array.

The repeated-pair bound uses only ordinary MAX distinctness and actual sparse frames; it does NOT use a full resolution, any true common global rank2 sector, or any classifier import.

## 5. TEN-class resolution excludes EVERY triple intersection

An original maximal1-RQLS10 requires ONE FULL resolution into TEN disjoint quantum transversals covering ALL100 cells. Each full quantum transversal contains exactly FOUR E4 rays, because the rays lie in the true E4/E6 decomposition and form an ONB of H10. Its selected cells in each A_CD are an orthogonal distinct-row/distinct-column subset, so section4 bounds their number by TWO.

Across the TEN classes of that SAME resolution, all 8m_CD cells in A_CD must be covered. Consequently

    8 m_CD <= 10 times 2 = 20.

Since m_CD is an integer, EVERY actual circuit pair must satisfy m_CD at most TWO. In particular ANY intersection multiplicity at least THREE is excluded for original MAX1, regardless of other circuits, projection angles, complement60 geometry or ordering of original columns.

This excludes a full ORIGINAL resolution, not every single transversal for an otherwise admissible many-circuit array. It is not a selected-resolution enumeration: the capacity bound holds for EVERY allowed full resolution. For a repeated pair of multiplicity two, its sixteen cells additionally force at least SIX of the ten classes to contain TWO cells from that class, since five doubles plus five singles cover only fifteen. This is only a necessary capacity statement, not existence of those classes.

## 6. Exact three-circuit residual; stronger two-circuit consequence paid prospectively

If H has THREE circuit vertices, its five edges distribute over the three unordered pairs. Section5 bounds each multiplicity by two. Therefore ALL three pairs occur, and their multiplicities are EXACTLY 2,2,1, up to circuit names. Its circuit lengths are 4,3,3. Thus original MAX1 in the ENTIRE three-circuit all-SPARSE mechanism requires exactly this circuit-intersection triangle. The two repeated pairs are each interior-isoclinic, independently; no equal-angle or simultaneous-tensor condition is asserted for them or for the remaining singly intersecting pair.

This eliminates BOTH the 3+2 star and 3+1+1 triangle intersection patterns without choosing graphs or controls. The 2+2+1 triangle's actual frame gluing, any four/five-circuit mechanism, every dense-vertex mechanism, other sector placements and the SAME full Latin resolution remain unpaid.

For exactly TWO actual circuits, all FIVE original vertices belong to the SAME pair class A_CD. Ordinary MAX forces that pair to be isoclinic by section2; then section4 permits at most TWO orthogonal distinct-row/column E4 cells, while a quantum transversal would need FOUR. Hence this entire two-circuit MAX mechanism in fact has NO SINGLE quantum transversal. This is a NEW prospectively stronger consequence than v78's unequal-angle FULL-resolution route: the earlier v78 statement is not edited, backdated or silently widened. Its unequal branch is now excluded under ordinary MAX by the explicit duplicate-ray argument above.

## 7. Exact import union and remaining original gap

Imports are the ENTIRE v76 actual five-row-type multigraph/frame placement, v77 actual sparse pairing/circuit facts, v78 COMPLETE local commutant/CS/endpoints/isoclinic product construction, and the actual source-separated TEN-transversal/CLASSICAL-mate interface audit. The unequal-case duplicate-ray proof and the partial3/capacity arguments are new written arguments here. The v15 global rank2 ceiling is NOT needed by this manuscript's conclusions. No A5/Gaussian/code/NR/classifier/Butson premise, tensor ansatz or common eigenline extension is imported.

All these are author-WRITTEN necessary geometry/mechanism exclusions, not formal/kernel-checked results, original witness, global no-go, conditional family resolution or novelty clearance. The unrestricted irreducible10,4+6,5+5 branches remain OPEN. Dense local frames, all-sparse 2+2+1 three-circuit gluing and four/five-circuit cases, other placements/minimalrank3 physical and higher-rank families, actual100 distinct rays and the SAME allowed full TEN-class resolution are still unpaid.

Any incorporation is only into a NEW COMPLETE SEPARATE-FUTURE union retaining every older branch/S50/S33/E5/product/audit/NR+BOTHflatfactorizations/process characterization. Main frozenv17/S72/index/proofs and live151v2/S55 stay immutable. No automatic review admission/read/adoption/formal/family/vendor/human/checker/priority/current-openness/novelty claim.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. No109/110/newscope/proof/coauditorreport/159/140 access/read claim, extra GO/STOP/restart or continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
