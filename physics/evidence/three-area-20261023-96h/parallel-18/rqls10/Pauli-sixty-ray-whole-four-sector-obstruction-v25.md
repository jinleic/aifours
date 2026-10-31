# RQLS10 v25 — ENTIRE standard two-qubit Pauli60-ray model cannot supply an ACTUAL common4-sector

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 07:43:43 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite symplectic/Pauli/orthogonality/coloring/Hall proofs only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty or full-witness acceptance. No executable finite-witness gate has been performed.

## 1. Exact whole-model theorem, not a rank4-WLOG claim

Let S_60 be the sixty standard two-qubit Pauli stabilizer rays, defined canonically in section2. The following covers ALL forty-ray subsets, ALL actual orthogonal4-tuples, ALL choices of three ten-basis partitions, ALL cycle orientations and ALL allowed full resolutions, together with arbitrary common unitary/phase/label changes of this fixed60-ray model.

**Theorem.** No maximal1-RQLS10 can have an actual common4-dimensional sector whose forty distinct rays belong to a common unitary image of S_60.

This is a complete model-specific obstruction, NOT a classification of arbitrary C4 rays, not an unrestricted4+6 impossibility, and not a solution to the original maximal100-ray problem. The irreducible10/proper4+6/proper5+5 branches remain OPEN. Unlike a dimension count or an enumeration stopping at one coloring, the proof classifies every case needed for this finite-model theorem and retains the ORIGINAL full-resolution requirement.

Whole v23+v24 are named literal construction/Hall dependencies, with the operative algebra/incidence reduction also reconstructed below. Neither earlier partial object nor its honestly open completion was previously a100-ray witness.

## 2. Complete literal60-ray model and all its commuting triples

Use the exact I,X,Y,Z matrices from v23; two-letter labels are tensor products. There are fifteen nonidentity Hermitian Pauli labels, with signs ignored only when naming labels. The maximal commuting triples are EXACTLY:

- nine product triples {aI,Ib,ab}, with a,b in{X,Y,Z};
- six entangled triples {XX,YY,ZZ}, {XY,YX,ZZ}, {XX,YZ,ZY}, {XZ,YY,ZX}, {XY,YZ,ZX}, {XZ,YX,ZY}.

Here is a complete derivation rather than a supplied catalogue. A commuting triple containing a local label aI must have the other factor's local label Ib and their product ab. If no local label occurs, choose two distinct weight-two labels. For them to commute, BOTH coordinates must differ; their product uses the remaining axis in each coordinate. Hence the triples pair the three first-qubit axes bijectively with the three second-qubit axes, giving the six permutations printed above. No other triple exists.

For each triple A, choose any independent commuting P,Q in it. Its four rays are the rank-one projectors

    Pi_A(s,t)=(I4+sP)(I4+tQ)/4,     s,t in{+1,-1}.

The projector proof in v23 section2 gives Hermitian rank-one, four mutually orthogonal rays, and different A give different rays. Thus this literally defines sixty distinct rays, partitioned into fifteen four-ray pure Pauli bases. No unseen file or classification result is a premise.

For different A,B the Pauli expansion gives the exact overlap:

    tr(Pi_A Pi_B)=1/4                         if A,B share no label;
    tr(Pi_A Pi_B)=(1+lambda_A(P)lambda_B(P))/4 if A intersect B={P}.

Distinct triples share at mostONE label, since two labels force their product. Thus two rays from different pure bases are orthogonal IFF the triples share a Pauli P and the two rays have OPPOSITE eigenvalues for P.

We will also use the elementary binary symplectic formulation, justified directly by Pauli commutation. Assign each nonidentity two-qubit label its nonzero vector in F2^4; commutation is the nondegenerate alternating form, and a triple is the three nonzero vectors of a totally isotropic2-space. Each point lies on THREE such triples. For a triple L and a point p outside it, the functional x-><p,x> is nonzero on L (otherwise p would lie in L-perp=L). Its kernel is exactlyONE nonzero point of L. Consequently there is a unique point on L commuting with p. These statements supply all small-geometry facts used below.

## 3. ALL orthogonal4-tuples are pure or hybrid; no ACTUAL pure context is allowed

### 3.1 Exhaustive basis classification

If an ONB contains two rays from the same pure basis A, they have exactlyONE common Pauli eigenvalue lambda(P). Their2-space is E_lambda(P). The complementary2-space is E_-lambda(P). Any stabilizer ray lying there must have P in its Pauli triple, since its expectation of P is -lambda, not zero. Any two orthogonal stabilizer rays in that eigenspace must come from the SAME pure basis B: different triples sharing P and the SAME eigenvalue have overlap1/2, not0. Thus the four-ray ONB is either all of A, or two rays from A in one P eigenspace and two rays from a DIFFERENT B in the opposite P eigenspace. Call the latter a HYBRID basis.

An ONB cannot instead have four rays from four different pure bases. Pairwise orthogonality would make their four triples pairwise intersect. Three distinct isotropic lines that meet pairwise must be concurrent: otherwise their intersection points would span a3-dimensional totally isotropic subspace, impossible in a nondegenerate symplectic4-space; if dependent, the three lines would coincide rather than form a triangle. Only THREE lines pass through one point. Thus four distinct lines cannot be pairwise intersecting. This proves the exhaustive classification, including the2+1+1 and3+1 multiplicity cases already settled by the two-same-A argument.

### 3.2 Any chosen pure Pauli basis sees only supports1,2,4

The Clifford transitivity required here has a short constructive proof. A product triple maps to {ZI,IZ,ZZ} using single-qubit H/S axis permutations. An entangled triple maps by local axis permutations/signs to {XX,YY,ZZ}; the Bell Clifford CNOT*(H tensor I) maps the computational basis to its joint eigenspaces. Hence any pure Pauli basis can be made computational by a unitary that permutes Pauli labels up to sign. On the standard computational diagonal, a stabilizer projector has uniform diagonal support on an affine subset of F2^2: its commuting triple intersects the diagonal Pauli subgroup in binary dimension0,1 or2, and the diagonal expansion is the corresponding sum of0,1 or2 independent binary-character conditions. Its nonzero diagonal count is therefore4,2 or1. There is NO three-support stabilizer ray in coordinates of ANY pure Pauli basis.

Suppose an ACTUAL sector context were pure. Its four rays become the coordinate axes and already occupy distinct cells in that context. Take either of the other actual contexts through one axis. Its other three sector rays form an ONB of that axis's coordinate complement C3 and cannot be other coordinate axes, since those already occur in the chosen context and two contexts meet at most once. All three would therefore have to be genuine two-support rays: support4 is not orthogonal to the chosen axis and support3 does not occur in S_60. But a3-dimensional coordinate space has no no-axis ONB made solely of two-support vectors: orthogonal support pairs cannot overlap in one coordinate, so a complete basis decomposes into disjoint two-coordinate blocks and would have even size. Contradiction.

Thus EVERY one of the thirty ACTUAL sector contexts must be HYBRID. No arbitrary-row-basis or rank3-to-rank4 assumption was made.

## 4. The forty rays force ten whole pure bases and a rainbow coloring of their Pauli triples

Fix an actual ray q from pure basis A. In each of its THREE actual contexts, the hybrid classification pairs it with another ray from A. No partner can be reused in two contexts, since two actual cells would then share two contexts. There are exactlyTHREE possible A partners. Therefore all three are used, so the entire pure basis A is in the forty-ray roster.

The forty rays are consequently the union of TEN selected pure bases. Denote their triple set T; the five excluded triples are C.

For each selected A, its six internal ray pairs each occur in one actual hybrid context. These are the six edges of K4. Color a context according to its original ROW/COLUMN/TRANSVERSAL partition. Each ray has one edge of each color, so this is a proper three-edge-coloring of K4. Its opposite edges have the same color: each color is one perfect matching. The three perfect matchings are exactly the plus/minus eigenpairs for the three Paulis in A. Hence each Pauli P of A has a well-defined color c_A(P), and A's three Paulis get three DIFFERENT colors.

Let d_T(P) be the number of selected triples containing P. It cannot be1: the corresponding internal P-pair in A must be in a hybrid context with an opposite-eigenvalue pair from ANOTHER selected triple containing P. When d_T(P)=2, both pairs in both triples force the two opposite-sign hybrid bases between them. When d_T(P)=3, write the three selected triples A,B,D. Each has one positive and one negative P-pair. The actual hybrids match positive pairs bijectively to negative pairs, with no fixed point (a fixed point would be pure). A derangement on three letters is one of the two directed3-cycles. Thus the hybrid contexts connect ALL selected triples through P in either case.

Their common actual context color forces c_A(P) to be the SAME at all selected A containing P. We obtain a global coloring c(P) of points with d_T(P)>0, such that EACH of the ten selected triples has ALL THREE colors. Conversely the only hybrid choices at each P are exactly the two-cycle or directed3-cycle rules just described. This is a full structural reduction, not a selected construction assumed WLOG.

Since every point lies on three triples and d_T(P)!=1, the five excluded triples C have point multiplicities only0,1 or3—NEVER2.

## 5. Complete classification of the five excluded triples

If no point has C-multiplicity3, the five excluded triples are pairwise disjoint and cover all fifteen points: C is a SPREAD.

Otherwise choose a point p of multiplicity3. All three triples through p belong to C; call the other two L,M. Each line not through p meets exactlyONE of the three p-lines, at the unique point commuting with p (section2). Let L meet one at q. To avoid forbidden C-multiplicity2 at q, M must also pass through q. Thus C is precisely the union of the three lines through p and the three through q, sharing line pq. The points p,q are distinct and commuting. This is a DOUBLE PENCIL. There is no third case.

### 5.1 All spread cases are Clifford equivalent to one literal case

Move one excluded triple to {ZI,IZ,ZZ}, using section3.2. Each of the other four spread triples is disjoint from it. The remaining local points XI,YI,IX,IY must be covered exactly once; only product triples contain them. Therefore exactlyTWO of the four triples are products, pairing X/Y on the first qubit with X/Y on the second. They must be the opposite corners {XI,IX,XX} and{YI,IY,YY}, OR {XI,IY,XY} and{YI,IX,YX}.

The two remaining excluded triples are then forced by disjointness to be, respectively, {XY,YZ,ZX} and{XZ,YX,ZY}, OR {XX,YZ,ZY} and{XZ,YY,ZX}. A single-qubit S axis swap X<->Y(up to signs) interchanges these two cases while preserving the Z triple. Hence every spread case is equivalent to the following explicit excluded five:

    {ZI,IZ,ZZ}, {XI,IX,XX}, {YI,IY,YY},
    {XY,YZ,ZX}, {XZ,YX,ZY}.

This exhaustiveness was derived from the printed fifteen triples, not an external transitivity claim.

### 5.2 All double pencils are Clifford equivalent to the literal v23 ten triples

The commuting independent pair p,q can be moved to ZI,IZ. Indeed first move their common pure basis to the computational one; its permutations of the three nonzero binary diagonal labels are generated by qubit swap and CNOT (GL(2,F2)), so choose p->ZI,q->IZ, with signs harmless. The excluded five are then EXACTLY

    {ZI,IZ,ZZ}, {ZI,IX,ZX}, {ZI,IY,ZY},
    {XI,IZ,XZ}, {YI,IZ,YZ}.

The selected ten are precisely the ten triples A1..A10 printed in v23. No arbitrary subset/coloring remains hidden after this reduction.

## 6. Spread case: literal Petersen obstruction to three actual partitions

For the canonical spread, the selected ten triples are

    C1={XI,IY,XY}, C2={XI,IZ,XZ},
    C3={YI,IX,YX}, C4={YI,IZ,YZ},
    C5={ZI,IX,ZX}, C6={ZI,IY,ZY},
    C7={XX,YY,ZZ}, C8={XY,YX,ZZ},
    C9={XX,YZ,ZY}, C10={XZ,YY,ZX}.

Each point belongs to exactlyTWO selected triples. Make a graph on the ten C nodes with one edge for each shared point. The rainbow coloring from section4 would be a proper three-edge-coloring of this cubic graph. Its exact outer/inner representation is

    (u0,u1,u2,u3,u4)=(C1,C2,C4,C3,C8),
    (v0,v1,v2,v3,v4)=(C6,C10,C9,C5,C7),

with outer edges u_i u_(i+1), inner edges v_i v_(i+2), spokes u_i v_i(indices mod5). Each displayed edge is checked directly against the listed triples. This is the literal Petersen graph; no name-only graph fact is needed below.

It has no cycles of length3 or4, by its outer/inner5-cycles and the spoke pattern: a cycle with two spokes would need equal step1 and step2 endpoint separations for a4-cycle; zero spokes gives length>=5; four spokes need at leastfour intervening same-side edges. Any proper three-edge-coloring would remove one color as a perfect matching, leaving an even-cycle2-factor. With ten vertices and girth5 such a2-factor must be a Hamilton10-cycle, since two5-cycles are odd.

There is NO Hamilton cycle, as follows. It must use a positive EVEN number of spokes, hence2 or4. With two spokes at indices a,b, its outer path must visit all five outer vertices, so a,b are adjacent modulo5; its inner path visits all five inner vertices, so a,b differ by2 modulo5. Contradiction. With four spokes, rotate the sole omitted index to0. The outer selected edges are u4-u0-u1 and u2-u3. The inner selected edges are v2-v0-v3 and v1-v4. Together with the four spokes they form TWO5-cycles, not one10-cycle. This exhausts the possibilities.

Therefore no proper three-edge-coloring exists. The spread case fails even the three required actual context partitions, before considering full Latin completion.

## 7. Double-pencil case: ALL rainbow colorings and hybrid choices reduce to v24's Hall obstruction

Use the selected ten triples of v23. Let a,b be colors of XI,YI and c,d colors of IX,IY. The four product triples require a,b EACH different from c,d. Hence either a=b or c=d, since two two-element disjoint subsets of three colors cannot exist. If BOTH are equal, all of XX,XY,YX,YY have the same third color, contradicting the triple{XX,YY,ZZ}.

Thus exactlyONE pair is constant. Exchange the two physical qubits if needed and permute the three context colors, so

    c(XI)=c(YI)=0, c(IX)=1,c(IY)=2.

The product triples now force

    c(XX)=c(YX)=2, c(XY)=c(YY)=1,

and{XX,YY,ZZ} forces c(ZZ)=0. The remaining four entangled triples force uniquely

    c(XZ)=c(YZ)=0, c(ZX)=2,c(ZY)=1.

For completeness: {XX,YZ,ZY} requires c(YZ),c(ZY) to be0,1; {XY,YZ,ZX} requires c(YZ),c(ZX) to be0,2; hence c(YZ)=0,c(ZY)=1,c(ZX)=2. Then {XZ,YY,ZX} forces c(XZ)=0, and{XZ,YX,ZY} is rainbow as required. This is the ENTIRE coloring classification, not one found example.

It is EXACTLY v23's row/column/transversal coloring. At each point, section4 leaves only the forced two-cycle or one of two directed3-cycles. Thus all actual hybrid-basis choices are the cycle orientations explicitly covered by v24 section2. Coordinate-color permutations, basis labels and signs do not change completion existence.

Here is the full Hall certificate again in block form, to retain the original-model requirement. Label bases by the unordered A-node pairs as in v23/v24. For EVERY orientation:

- columns1,2 are occupied in rows1..4;
- both rows5,6 and both rows9,10 already have symbol4;
- column3 is occupied in rows1,2,5,6;
- both rows7,8 and both rows9,10 already have BOTH symbols9 and10.

Each is a literal consequence of v23's two-by-two A blocks, whose row-wise symbol SETS do not depend on cycle orientation. The first two facts force symbol4 in columns1 and2 into rows7,8, exhausting their4 occurrences. Then column3's three distinct symbols4,9,10 are ALL restricted to just rows3,4. Three symbols cannot occupy two cells. The partial Latin pattern cannot extend to a full order10 resolution.

Any ACTUAL original4-sector necessarily lives inside such a full resolution: the remaining sixty cells, whatever their6-dimensional rays, must supply the other six occurrences of each transversal symbol with exactlyone symbol per full row/column. This is impossible here. Thus the double-pencil case fails the full-resolution application gate, not the valid partial40-ray geometry.

## 8. Entire conclusion, named imports and remaining original gap

Sections2–7 exhaust ALL orthogonal contexts, ALL forty-ray subsets, ALL allowed three-partition choices and ALL orientation choices within the STANDARD60 Pauli-ray model. The spread case has no three-partition structure; the double-pencil case has the v23 partial structures but NONE extend to the original full Latin resolution. The theorem of section1 follows.

The operative dependencies are elementary exact Pauli/symplectic/Clifford facts proved here, the literal ten-triple projector/cycle/forty-cell construction in v23, and the full orientation-invariant Hall certificate in v24. An ENTIRE union review must read/reconstruct ALL of v23,v24,v25, not merely the Petersen argument, canonical case or a selected triple. In particular the Clifford normalizations, exhaustive basis/subset/coloring reductions and necessity of full resolution are part of the theorem, not assurance prose detachable from its statement.

No unprovided classification of the Pauli60 rays or graph database is a premise. No machine-generated finite-check output exists, and no finite-witness/checker/priority gate is claimed passed. The theorem is written/model-specific only. Arbitrary40 C4 rays outside this unitary60-ray model remain available, as do all original irreducible10/4+6/5+5 possibilities. No maximal100-ray construction or unrestricted exclusion is supplied. It would be false to treat absence from this finite stabilizer model as a rank4 no-go.

This is a documented replacement/closure of the failed literal v23 continuation at a genuinely larger exact model scope, not a repeated failed enumeration. Primary must now use a different4-sector geometry or a different surviving branch. All prior process/math findings, v9/v14 withdrawals and ZERO-credit quarantines remain permanent; no frozen source is edited or backdated. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 remain binding. No early pending-gate park.
