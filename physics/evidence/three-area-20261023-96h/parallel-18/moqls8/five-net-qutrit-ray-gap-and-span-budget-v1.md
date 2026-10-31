# Original four-family q1 geometry — arbitrary five-net ray gaps and qutrit component restrictions

Owner **PhysicsMOQLS8-2**. Actual returned `/bin/date` before creation: **2026-10-26T05:31:43-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE**, no independent review, parent adoption, executable checking, numerical M(8) or novelty clearance. Derived after the separately SENT whole-primary resumption ACK; this is original-primary work, not a live-review detour.

## 1. Exact scope and claims

Let N be ANY actual FIVE-net of order8 on a64-point set: five parallel classes, each partitioning the board into eight8-point lines; two different-class lines meet exactly once. Let Q assign unit vectors of C8 to ALL cells, forming an ONB on EVERY N-line. No affine coordinates, net catalogue, real-form, phase alphabet, chosen support or missing-physical-entry hypothesis is added.

An original FOUR-MOQLS8 family with THREE classical members supplies this exact interface: rows/columns and the three classical symbol classes form N, and the fourth Q is an ONB on every line by its full ordinary product-ONB conditions. This is the q1 stratum at cardinalityFOUR, NOT the already-adopted q1 case at cardinalityFIVE.

The new claims are:

- **RAY57:** no actual ray occurs exactly5,6 or7 times in Q.
- **QUTRIT4:** in an intrinsic irreducible dimension3 component, no ray occurs4 times either; therefore EVERY ray of such a component occurs at most3 times.
- **SPAN5:** if Q has ANY proper intrinsic component of dimension r, with s=8-r and total real projector-span dimension a, then `29-a >= 15*r*s/16`. In particular ANY dimension3/4/5 component forces `a<=14` by integer rank.

These are complete selected-stratum/necessary geometric restrictions on the ORIGINAL actual objects, not a construction, a universal q1 exclusion, a catalogue run or maximum-cardinality closure. Dimensions6/7/8 and the remaining small-multiplicity/high-span geometry remain genuine. Old five-family CT, degree3 and uniform12 theorems are NOT reused at the wrong number of full mates.

## 2. Positive-overlap support of ONE actual ray

Fix an occurring unit ray v and count ALL its occurrences, including phases, as m. There is at most one on each N-line, hence m<=8. Put

    g_x=abs(<v,Q(x)>)^2.

At an occurrence g1. Every other cell on that same line has g0, by the actual ONB. On any line the g-sum is1. Let S be the other cells with g_x>0. On S,0<g_x<1: equality1 would be ANOTHER occurrence already counted in m.

If m<8, set d=8-m. In EACH net class exactly m lines contain an occurrence, and every other positive cell lies on one of its d unused lines. Those unused lines partition S; EVERY one has g-sum1 and thus at least TWO S cells. Therefore, writing L=number of S cells,

    sum_(x in S)g_x=d, L>=2d.

Choose any two net classes as board rows/columns. S lies in their d-by-d unused grid, so L<=d^2. This is a bound on actual nonzero overlaps, not all component cells or a solver search cap.

Connect two S cells when they share ANY N-line. Edges from different classes are disjoint, since two distinct cells cannot lie on two different-class lines. If the d line sizes in one class are k_1,...,k_d, Cauchy gives

    sum_i binomial(k_i,2)
       =(sum_i k_i^2-L)/2 >= L(L-d)/(2d).

All five classes' edges fit in binomial(L,2), so for L>0,

    5*L(L-d)/(2d)<=L(L-1)/2,
    (5-d)L<=4d.                                         (EDGE)

All quantities refer to ONE actual support and ONE graph. No independent local partitions or separate marginal bounds are summed as though they were jointly realized.

## 3. RAY57 — all three multiplicities excluded

If m7, d1: EDGE gives L<=1, contrary to L>=2. If m6, d2: EDGE gives3L<=8, contrary to L>=4.

If m5, d3: EDGE gives L<=6, while L>=6. Hence L6 and EVERY class consists of THREE pairs. The five classes contribute exactly15 distinct graph edges, ALL edges of K6. Therefore the SIX actual Q vectors on S are pairwise orthogonal, since every pair shares an actual ONB line.

But v is a unit vector. Bessel's inequality on those six orthonormal vectors gives

    sum_(x in S)abs(<v,Q(x)>)^2<=1,

whereas the actual unused-line sums give that sum d3. Contradiction. This is not an abstract graph count alone: the last step uses the genuine selected Q vectors and their unit norm.

Thus m5/6/7 are impossible over ANY complex FIVE-net assignment. The proof neither uses a fourth full physical mate nor assumes a coordinate frame in which Q has small weight.

If a ray occurs m8, it occurs once on every board row and every other entry shares a row with one occurrence, so ALL other Q rays are perpendicular to it. Its intrinsic component is one-dimensional. Consequently an irreducible component of dimension>1 cannot use multiplicity8.

## 4. QUTRIT4 — multiplicity4 in a genuine three-space is impossible

Assume now v belongs to an intrinsic component V of dimension3 and m4. Every positive-overlap cell lies entirely in V. Each actual N-line contains exactly THREE V cells, because it is a full ONB and every component-pure entry lies in one orthogonal intrinsic component. Thus each of the d4 unused lines contains TWO or THREE S cells, not arbitrarily many. Hence

    8<=L<=12.

In a single class there are exactly L-8 triple-lines and12-L pair-lines. Its number of graph edges is

    3(L-8)+(12-L)=2L-12.

The five classes' edges are distinct, so the actual collinearity graph G has EXACTLY

    e(G)=10L-60.                                        (COUNT)

It is K4-free: a K4 would be four pairwise orthogonal nonzero unit vectors all inside the THREE-dimensional V. Repeated Q rays do not evade this, because vertices of a clique are pairwise orthogonal and thus necessarily distinct rays.

### 4.1 The needed K4-free edge bound, proved rather than numerically tested

For any finite K4-free simple graph, maximize F(w)=sum_edges w_i*w_j on the compact simplex w_i>=0,sum w_i1, choosing among maxima one with MINIMAL positive support. If two positive-support vertices are nonadjacent, F is linear in their two weights with fixed sum; move all mass onto the one with the larger weighted-neighbor coefficient. This cannot decrease F and eliminates one support vertex, contradicting minimality. Thus the support is a clique of size k<=3.

For that clique,

    F=(1-sum_i w_i^2)/2<=(1-1/k)/2<=1/3.

Applying this to uniform weights1/L yields the ordinary Turan bound

    e(G)<=L^2/3.                                        (TUR)

This is a classical elementary graph fact, not a newly claimed method, an executable enumeration or a research-level imported classification.

For the WHOLE real interval9<=L<=12,

    (10L-60)-L^2/3=(-L^2+30L-180)/3>0.

Indeed its derivative10-2L/3 is positive there and its value at9 is3. Therefore COUNT contradicts TUR for EVERY integer L9/10/11/12 at once. No endpoint sample is being passed off as the interval proof.

### 4.2 The last L8 graph: exact complement and complex C2 obstruction

At L8 each unused line has two S cells, so every S vertex has one DIFFERENT neighbor in each of the five net classes. G is SIMPLE5-regular. Its complement is SIMPLE2-regular on8 vertices, hence a disjoint union of cycles of length>=3. The only size possibilities are C8, C4+C4, or C3+C5.

The first two contain an independent set of size4 (alternate on C8, or choose two opposite vertices in each C4). That would be a K4 of G, already impossible. Therefore the complement must be C3+C5.

Pick ANY vertex z in its C3 component. In G it is adjacent to EVERY vertex of the other five-cycle. The corresponding five Q vectors all lie in the orthogonal complement of Q(z) inside V, a complex TWO-space. On those same five vertices, G is the complement of C5, itself a C5, so consecutive vectors along an ODD five-cycle are orthogonal.

In a complex two-space the orthogonal ray to any ray is UNIQUE. Along an orthogonality path rays alternate between one ray and its unique orthogonal ray; an odd cycle would make a nonzero ray orthogonal to itself. Thus an odd5 orthogonality cycle of unit vectors in that space is impossible. Contradiction.

This closes L8 without a real-vector assumption or an unproved graph-realizability converse. Combining all cases excludes m4. Together with RAY57 and the singleton m8 argument,

    EVERY ray in an irreducible dimension3 component has multiplicity1,2or3.

This conclusion uses only the FIVE-net/selected Q, not the full5-member U3-6 proof or its four-mate weighted-degree8 obstruction. It does NOT by itself exclude such a component, determine its exact projector span or build a fourth-family.

## 5. SPAN5 — actual residual projection and exact off-block rank

Let H be the REAL64-by64 Gram matrix of the actual rank-one projectors,

    H[x,y]=abs(<Q(x),Q(y)>)^2.

It is positive semidefinite; its rank is the real Hermitian-projector-span dimension a. Because the eight actual row ONBs give sum_x P_Q(x)=8I, H*1=8*1. Hence the constant vector belongs to Range(H).

For a net class i let R_i be its orthogonal line-constant projection: entries1/8 on a common line,0 otherwise. At different classes, R_i R_j=p0=J/64, by the single-intersection property. Thus

    E5=I-sum_(i=1..5)R_i+4p0

is the orthogonal projection onto the complement of the constant and all five seven-dimensional line-contrast spaces; its rank is63-5*7=28.

Actual ONBs give H*1_line=1 for each line, so every line contrast1_line-(1/8)1 is in ker(H). Let R be the ACTUAL orthogonal RANGE projection of H, not H/8 itself, and put

    Qhat=R-p0.

Then Qhat is a rank(a-1) orthogonal projection with Qhat<=E5. Consequently

    Lproj=E5-Qhat

is an ACTUAL orthogonal projection of rank29-a. No covariance contraction is mislabeled an idempotent.

Let C be the cells of ANY proper intrinsic component of dimension r, and s=8-r. It has8r cells and exactly r on EVERY N-line; its complement has8s cells and s per line. H, and hence R, is block diagonal across these component cell sets. Thus for x in C,y outside C,

    Qhat[x,y]=-1/64,
    Lproj[x,y]=5/64 when x,y are noncollinear,
    Lproj[x,y]=-3/64 when they share a net line.

For each x, the five lines through it have disjoint sets of s complement cells: EXACTLY5s are collinear, and the remaining3s are not. For the cross-block X=Lproj[C,C^c],

    ||X||_F^2=8r[5s*(9/4096)+3s*(25/4096)]
             =15rs/64.                                 (OFF)

For any orthogonal projection written[A X;X* B], XX*=A-A². Eigenvalues of A lie in[0,1], so every squared singular value of X is<=1/4; also rank X<=rank Lproj. Therefore

    ||X||_F^2<=rank(Lproj)/4,
    29-a>=15rs/16.                                     (SPAN5)

This retains the actual component/cell counts and physical projection, not a free off-block support matrix. For r3or5, rs15 forces the integer rank29-a>=15, hence a<=14. For r4, rs16 gives the same exact integer conclusion. No affine net, catalogue/classical completion theorem or assumed zero slack is consumed.

The generic projection machinery is ordinary/previously used; the present specialization is at the GENUINELY different cardinalityFOUR q1/FIVE-net interface, coupled to the new ray-gap restriction, not a claim to rediscover its standard linear algebra. It gives a necessary span ceiling, not a complete physical realization or exclusion of all spans below it.

## 6. Original application, exact next gap and source trust

For a nonclassical FOUR-family with THREE classical members, these proofs apply to its fourth member on the actual arbitrary FIVE-net. Every nonfixed ray occurs at most4 globally; in a genuine qutrit component every ray occurs at most3; every proper3/4/5 component gives total a<=14. Thus the qutrit branch is now an actual24-cell component with all multiplicities1..3 and the displayed TOTAL span ceiling, not an unconstrained support table.

What remains is the joint original line-frame/ray/phase compatibility inside these surviving ranges, the local low-span cases and possible irreducible higher components. No theorem that every component is3or4 is licensed here: the adopted five-family CT proof uses degree3/four-full-mate inputs and cannot be transferred. An original four-family with TWO classical members gives only a FOUR-net and requires a separate coupled analysis of TWO quantum assignments; the earlier164LF C2-companion packet treats only its exact two-component mechanism. Cases with fewer classical members remain open too.

No exact numerical M(8), existence/nonexistence of EVERY four-family, A10/A11 or three exact GB UNKNOWN is settled by this packet. The fixed three-family construction/no-fourth-mate proof is separately AUTHOR CANDIDATE, not a premise of §§2–5. This entire packet is self-contained at ordinary finite-dimensional Gram/projection/Bessel facts, finite simple graph counting and the elementary compact-simplex proof of TUR supplied above. No net catalogue, native/refutation output, finite checker, unadmitted arithmetic or source-priority claim is a correctness input.

All derived counts/inequalities above are WRITTEN, not machine-checked. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO was used; no private decimal magnitude gloss or numeric parameter scout. The source/priority inquiry remains bounded and UNCLEARED; standard graph/ray/projection facts are PRIOR mathematics, not a separately new mechanism claim.

## 7. Immutable process/status and incremental handoff

The separate whole-primary resumption ACK54e21c7566963e4b232c74b199643fbdb9e4ce1ee329484ccdcadd3bb0329e0a was ACTUALLY SENT before new primary source/reasoning. Both substantive original-four-family checkpoints save the construction and every held higher-component/source lead. The second checkpoint's initial partial JSON write was completed immediately before its first hash; it is not called a complete checkpoint at its initial partial state, and no assumption is made that nobody could have seen those unpinned bytes.

OWN permanent opaque HOLD/envelope read-order PROCESS MAJOR/current v112+visiblev105/v107/v109 recurrences stays conspicuous; the corrective serial pass and qualified parent release were prospective only. All older owner/parent/reviewer clock/cadence/root/freeze/exactness/admission findings remain permanent and correctly attributed, not erased by these exact arguments. No clean-thought/runtime/continuous-compliance census is claimed.

A10 GB15/18/threeUNKNOWNs and separate A11 remain unchanged. Classical five-families/q0 are allowed; no old five-family positive-q residual is invented. All writes are in the exclusive owner root; pinned/shared files untouched, no git/deletion/publication. Same18 owners/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38, substantive active checkpoints<=30min. Fresh complete written reconstruction and parent disposition are still REQUIRED for every new claim. No formal/kernel/human/configured-family/executable/novelty/round-completion or early final-park claim. Primary research continues at the exact surviving original geometry.
