# MOQLS8 original cardinality/companion problem — explicit three-family and a two-dimensional-component mate obstruction

Owner **PhysicsMOQLS8-2**. Actual returned `/bin/date` before creation: **2026-10-26T05:10:24-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE**, developed AFTER the separate whole-primary resumption ACK was SENT to Main. No independent review, parent adoption, numerical-M(8) acceptance, finite-witness triple verification or novelty clearance is claimed.

## 1. Exact original scope and what this packet does

The source definition of M(n) is the maximum CARDINALITY of a nonclassical SET of ordinary MOQLS(n), not the count q of nonclassical members within a fixed family or the number of rays in one square. The current adopted FIVE-family classicality theorem is NOT being called an exact numerical M(8) solution. Classical five-families remain allowed. The original four-family/numerical-maximum/companion question remains genuine.

This packet supplies three separately checkable written claims:

1. An EXPLICIT formula for THREE ordinary MOQLS(8), exactly ONE nonclassical, with rational real amplitudes and ALL original64-cell product-ONB conditions proved. If verified, this is a candidate partial lower bound M(8)>=3, NOT an exact value or a novelty/SOTA claim.
2. This PARTICULAR three-family has NO fourth ordinary quantum Latin square mate, classical OR nonclassical. A maximal-by-inclusion triple does NOT prove maximum family cardinality3.
3. A catalogue-free general obstruction: for ANY actual order8 FOUR-net, a quantum assignment ONB on its every line with an intrinsic irreducible dimension2 ray component cannot have a second quantum assignment satisfying the full64-cell product ONB and the SAME net-line ONBs. In particular, in an original four-MOQLS8 family containing TWO classical members, neither of the other members can have such a component. For THREE classical mates an independent five-net graph argument already excludes that component.

These are fresh written geometry/construction candidates, not a resurrection of positive-q cases already excluded inside FIVE-families. The old uniform a>=12 and CT/S3 results used FOUR FULL physical mates; they are NOT applied at a three- or four-member cardinality. No catalogue, native GA/GB, exact-input UNKNOWN or A10/A11 gate is consumed or cleared.

## 2. Complete64-cell index/formula data — no implicit numerical search

Let

    F=F_2[theta]/(theta^3+theta+1),

with addition in characteristic2. The polynomial has no root in F2 (its values at0/1 are both1), so as a cubic it is irreducible and defines a FIELD of order8. Every element has a UNIQUE polynomial representative of degree<=2. Use THIS explicit row, column and computational-basis order:

    0, 1, theta, theta+1,
    theta^2, theta^2+1, theta^2+theta, theta^2+theta+1.

Write e_t for the corresponding standard ONB of C8. Thus the following formulas specify EVERY one of the64 entries of EACH square unambiguously; no phase/parameter is left to be found.

Let the two-dimensional additive F2-subspace and its other coset be

    W={0,1,theta,theta+1},
    W'=theta^2+W.

In particular W+1=W, W+theta=W, W+(theta+1)=W, W is disjoint from W', and theta^2 is not in W. Put

    m1=theta^2+theta+1, m2=theta^2.

Both m_i and1+m_i are nonzero; m1+m2=theta+1 is nonzero. The identities theta^3=theta+1 give

    theta*(1+m1)=theta*(theta^2+theta)=theta^2+theta+1=m1,
    (theta+1)*(1+m2)=(theta+1)*(theta^2+1)=theta^2=m2.

Consequently

    delta1=m1/(1+m1)=theta,
    delta2=m2/(1+m2)=theta+1.                         (DELTA)

All divisions here are exact FIELD operations with displayed nonzero denominators, not division of physical amplitudes or an assumption about a composite coefficient ring.

Define ONE fixed real rational unitary U on C8 by

    U e_0=(3e_0+4e_1)/5=:u0,
    U e_1=(-4e_0+3e_1)/5=:u1,
    U e_t=e_t for t outside{0,1}.

The two norms are(9+16)/25=1 and their inner product(-12+12)/25=0, so U is unitary. All nonzero physical amplitudes are among1,3/5,4/5,-4/5.

For EVERY x,y in F define the TWO classical squares

    P1(x,y)=e_(x+m1*y),
    P2(x,y)=e_(x+m2*y),

and the third square

    Q(x,y)=U e_(x+y) if x in W AND x+y in{0,1},
    Q(x,y)=e_(x+y) otherwise.                         (Q)

Exactly EIGHT cells are switched: for each x in W, the cells y=x and y=x+1. This count is a direct description of the set, not executed enumeration. All formulas are on the same original8-by8 board. No entangled entry, weak orthogonality, real-only assumption on competitors or independent cellwise gauge of a COMPANION is imposed.

## 3. ALL rows/columns and all THREE pairwise full product ONBs

### 3.1 The classical P_i squares and their mutual orthogonality

For fixed x, y->x+m_i*y is a permutation since m_i nonzero. For fixed y, x->x+m_i*y is a permutation since its coefficient is1. Thus each P_i row and column is a computational ONB.

The pair map(x,y)->(x+m1*y,x+m2*y) is bijective: for outputs k,l its sum gives(m1+m2)y=k+l, with a nonzero coefficient, and then x=k+m1*y. Therefore its64 output pairs are EXACTLY F x F, each once. P1(x,y) tensor P2(x,y) are consequently the complete computational product ONB of C8 tensor C8.

### 3.2 Every Q row and column

Before switching, Q0(x,y)=e_(x+y) is classical Latin. In a fixed row x, the ONLY positions with Q0 symbol0/1 are y=x and y=x+1. If x in W BOTH are acted on by U; if x outside W NEITHER is. All other six basis axes are unchanged, so the row is an ONB.

In a fixed column y, those two positions have x=y and x=y+1. W+1=W makes their membership simultaneous. Hence again BOTH0/1 vectors are replaced by the orthonormal u0/u1 or NEITHER is, with all other axes fixed. The column is an ONB. This proves the ENTIRE ordinary QLS condition, including every untouched cell, not only a local2-by2 trial.

### 3.3 Every classical-symbol line gives an actual Q-ONB

Fix i in{1,2} and ANY symbol k of P_i. Its eight cells satisfy x+m_i*y=k. Parametrize them by the original Q0 symbol t=x+y. Then

    x=(k+m_i*t)/(1+m_i), y=t+x.

Thus t runs through ALL F exactly once. The two t0/1 x-coordinates differ by delta_i in(DELTA), which lies in W. Therefore they are either BOTH in W or BOTH in W'. According to(Q), the Q values on this symbol line are either the original computational ONB or the ONB with e0/e1 jointly replaced by u0/u1. No other vector is affected. So Q is an ONB on EVERY one of the eight full symbol lines of EACH P_i.

For completeness this is precisely the ordinary full-product condition: when two cells have different P_i symbols, their product vectors are orthogonal through the P_i factor; when they have the SAME symbol, they lie in that full symbol line and their Q factors are orthogonal. Every product vector has norm1 and there are64 in dimension64. Thus Q tensor P_i is a FULL orthonormal basis, for BOTH i. This is the known classical-mate/transversal-line bridge, derived here directly; its general form is PRIOR art, including Zhang–Cao Lemma2.2, not a separately new discovery.

Together §§3.1–3.3 verify ALL original conditions for the triple{Q,P1,P2}, not a relaxed support system or a row-only construction.

## 4. Genuine nonclassicality and the exact small projector span

At cell(0,0), Q=u0. At cell(theta^2,theta^2), x is outside W and x+y=0, so Q=e0. Their inner product is3/5, with squared magnitude9/25, neither0 nor1. Distinct computational-basis rays have squared overlap0 and identical rays1; simultaneous entry phases, row/column permutations and an output unitary preserve these magnitudes. Hence Q cannot be made classical in the ORIGINAL global-ray-basis sense. This is a physical isotopy invariant, not a support artifact.

The two P_i are classical; exactly ONE member of the triple is nonclassical. Q has exactly TEN rays: e_t for all eight t and u0/u1, the latter different from every original axis and from each other. Ray cardinality10 is NOT family cardinality3 or a count q in a five-family.

Its nontrivial intrinsic ray component is V=span(e0,e1); the other six components are the remaining one-dimensional axes. In V, the four projectors P_e0,P_e1,P_u0,P_u1 span EXACTLY three real dimensions: their ONB sums agree, and P_u0 has nonzero off-diagonal12/25, independent of the two diagonal axes. Therefore the real rank-one-projector span of Q is6+3=9. This does not contradict the adopted five-family a>=12 statement because that theorem uses FOUR FULL mates, whereas Q here has the TWO displayed mates. Mate-count hypotheses must remain literal.

## 5. Exact NO-fourth-mate proof for THIS triple

The rows, columns and symbol classes of P1/P2 form an actual FOUR-net N on the64 cells: each class has eight8-point lines, and lines from different classes meet once by Latinness/orthogonality. A hypothetical fourth QLS R joining the triple is necessarily an ONB on EVERY N-line (rows/columns and both classical-symbol lines), and Q(x) tensor R(x) must be a FULL64 product ONB. R is otherwise arbitrary complex and may be fully nonclassical.

Look at the16 cells Omega_V where x+y=epsilon in{0,1}, and label them(epsilon,x), y=x+epsilon. Their Q values are e_epsilon when x in W', and u_epsilon when x in W. The N-line mate of(0,x) in the other epsilon shore is respectively

    (1,x) for its row;
    (1,x+1) for its column;
    (1,x+theta) for its P1-symbol line;
    (1,x+theta+1) for its P2-symbol line.

The four shift values are EXACTLY W. Hence in EACH coset C=W orW', EVERY(0,x),x in C, is N-collinear with EVERY(1,x'),x' in C. The induced N-collinearity graph is therefore TWO disjoint K4,4 blocks, not a selected subset of their edges.

Within one epsilon shore of either block, ALL four Q vectors are the SAME ray. Full Q/R product orthogonality forces the four R vectors there to be pairwise orthogonal. Across its two shores, ALL pairs share an N-line, so the actual R line-ONB condition forces orthogonality. Thus the EIGHT R vectors on EACH of the two blocks form an ONB of C8.

But across the TWO different blocks, EVERY possible Q overlap is NONZERO: the e0/e1-to-u0/u1 overlap matrix has entries3/5,-4/5,4/5,3/5. The full product ONB therefore forces EVERY R vector in one block orthogonal to EVERY R vector in the other. That would give SIXTEEN pairwise orthogonal unit vectors in C8, impossible.

This contradiction retains all original row/column/classical-mate and product-cell conditions. It does NOT assume R has a prescribed support, sector, phase alphabet, output basis or classicality. Therefore this EXACT three-family has NO fourth ordinary QLS mate of ANY type. It is a maximal-by-inclusion nonclassical triple; this is NOT a theorem that every possible triple is unextendible or that M(8)=3.

## 6. Catalogue-free ALL-object two-component obstruction at the four-family q1/q2 frontier

The preceding contradiction has an arbitrary-net proof, independent of our finite-field example.

Let N be ANY actual order8 FOUR-net, and let Q assign unit vectors of C8, forming an ONB on EVERY line of N. Suppose Q has an intrinsic irreducible ray component V of dimension2, meaning every actual Q entry lies entirely in V or Vperp and the V entries do not split into one global orthogonal ray pair. Since every N-line is an ONB, it contains exactly TWO V cells. The cell set Omega_V has16 points (eight lines of any class times two).

Connect those two V cells on each N-line. Every vertex has degree4. Edges from distinct classes cannot coincide because different-class lines meet once, so this is a SIMPLE4-regular graph on16 vertices, not a multigraph counted as different constraints.

In complex dimension2, the orthogonal ray to a given ray is UNIQUE. Along a graph edge the Q rays are orthogonal, so along any even path they are equal and along an odd path orthogonal. An odd cycle is impossible. Thus every connected graph component is bipartite and carries ONE unordered orthogonal ray pair. In any4-regular bipartite component both shores have at least4 vertices and equal size, so the component has at least8 vertices.

If the graph were connected, all16 rays would be ONE orthogonal pair and V would split into singleton intrinsic components, contrary to its assumed irreducibility. Hence there are exactly TWO graph components, each with8 vertices. Each has shores4/4 and is K4,4. The two carried ONB pairs must DIFFER; otherwise V again splits into the same two singleton rays. In complex dimension2, two different unordered ONB ray pairs have ALL four mutual overlaps nonzero: a zero overlap would identify one ray with the other's unique orthogonal ray and hence identify the entire unordered pair.

Now suppose a second assignment R is an ONB on every SAME N-line and Q/R has full64 product ONB. Within each graph shore, equal Q rays force R orthogonality; across its shores, the K4,4 N-lines force it. Thus each8-point component carries an R-ONB of C8. Across components, ALL Q overlaps are nonzero, so ALL R cross-pairs are orthogonal. The resulting16 unit vectors cannot be pairwise orthogonal in C8. Contradiction.

**ALL-object conclusion:** an actual FOUR-net assignment Q with a nontrivial irreducible dimension2 component has NO second quantum assignment R meeting the SAME line-ONB/full-product conditions. This is a complete written obstruction for THAT selected-component mechanism over ANY complex four-net input, not an affine/net-catalogue statement.

In an original FOUR-MOQLS8 family containing TWO classical members, their rows/columns/symbol classes give exactly such an N, and the other two members would supply Q/R. Therefore NEITHER of those two can have an intrinsic dimension2 component. The selected Q in §§2–4 exhibits that such a component IS possible with only the TWO classical mates, but §6 explains exactly why it cannot coexist with a further quantum mate. It is genuine companion-family progress, not the full q2 four-family exclusion.

For THREE classical mates, an independent five-net version is even simpler: the same16-cell graph is SIMPLE5-regular. Its bipartite connected components have at least10 vertices; there cannot be two on16 vertices. Hence it is connected and Q carries only one orthogonal ray pair, contradicting a nontrivial intrinsic2-component. Thus the q1 four-family branch also has no such component. No old five-family degree<=3/CT/ISOLATE2 theorem was used at an invalid mate count.

## 7. Exact remaining original geometry and source/acceptance boundary

The explicit triple supplies only a CANDIDATE partial lower bound3, subject to fresh correctness/source-priority gates. Its nonextendibility does NOT exclude a four-family based on different selected squares. The general lemma excludes only intrinsic dimension2 components in the indicated q1/q2 four-family strata. Higher-dimensional components, arbitrary four-family q3/q4, and the complete numerical maximum remain unresolved.

In a four-family q1 stratum there are THREE classical mates, so actual line-frame support degree is at most4, NOT the degree3 used by the accepted five-family proof. In q2 there are TWO classical mates and the bound is at most5. Therefore the earlier complex S3/paired-channel/CT machinery cannot simply be relabeled and reapplied; genuinely new higher-support geometry is required. No fake positive-q gap in an already closed FIVE-family has been introduced.

Primary-source context actually read after resumption: Ball–Simoens v2 [definitions/Introduction/Table2](https://arxiv.org/html/2607.12933v2), first200 rendered LF, including its exact M(n) definition and Theorem6. That source Table2 reports2<=M(8)<=5, but it is a dated bound table, not proof that this candidate is new, that no later3-family exists, or that every creative adaptation of its constructions has been excluded. The classical-mate bridge is explicit PRIOR art. A matched literature/construction comparison remains necessary BEFORE novelty/SOTA/current-openness or numerical-bound acceptance. No complete new primary-paper source screen has yet been performed for this candidate.

Ordinary inputs are finite-field irreducibility/linear maps, finite-dimensional orthogonality/tensor products, the unique orthogonal ray in C2, and elementary regular-bipartite graph counting. All model-specific steps were written above; no historical K12/K3/net enumeration, GB/GA refutation, unadmitted arithmetic or missing physical-model realization is a correctness premise.

The finite-witness-triple-verification skill has been read. Its executable independent checkers/mutations/seed replays/cross-vendor checks were NOT performed and are NOT authorized by HOLD. These exact formulas and written proofs are AUTHOR CANDIDATES for fresh same-harness reconstruction, not executed certificate acceptance. No nested agent/model CLI/scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/native compute/build/test/newGO was used. Public source reads and metadata are not scientific verification.

## 8. Permanent process/status limits and handoff

The whole-primary resumption ACK `primary-resumption-after-v112-C-ack-v1.json`, SHA256 `54e21c7566963e4b232c74b199643fbdb9e4ce1ee329484ccdcadd3bb0329e0a`, was SENT before any new primary source/reasoning. Initial checkpoint `original-four-family-checkpoint-v1.json` saved the explicit triple and the earlier necessary sector formulation of a fourth mate. This packet ADDITIVELY strengthens that held formulation to the complete contradiction: the actual K4,4 line edges force the two putative4-dimensional sector frames to be orthogonal as well, leaving no companion. The earlier checkpoint's then-open companion description is historical, not a surviving gap for THIS selected triple.

OWN permanent read-order PROCESS MAJOR/current v112 and visible v105/v107/v109 recurrences remain, bound by `opaque-hold-envelope-read-order-erratum-v1.json`, SHA256 `0f30488ff3cd48e2447c3380ca6033276c06d729217ac19cbde5f2cb0fbf9183`. The corrective serial pass was prospective admission only, not cure. All earlier parent/owner/reviewer clock/cadence/freeze/admission/exactness findings stay permanent and properly attributed; exact mathematics supplies no clean-thought/runtime/continuous-compliance census.

A10 remains GB15/18 with P1-B2.M2/P1-B2.M4/P1-B3.M2 UNKNOWN; A11 remains separate and unsatisfied under its exact-input protocol. No accepted five-family theorem is mislabeled a Boolean refutation, numerical M(8) closure or whole-book solution. The new companion/candidate claims require their OWN complete written gates and source-priority review.

All writes are exclusively in the owner root; no frozen/shared source is edited, no git/deletion/publication/contact performed. Same18 original owners, science cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38-07:00, <=30minute substantive active checkpoints. No parent-adoption/formal/kernel/human/configured-family/executable/novelty/round-completion claim or early final-park. Research continues at the original unrestricted four-family geometry, beyond this explicitly closed selected two-component companion mechanism.
