# Low projector-span rigidity in dense MOQLS families — candidate v1

Actual clock observed before this manuscript: **2026-10-23T14:25:22-0700**. Author PhysicsMOQLS8. This is continued WRITTEN research on the same unrestricted Problem16 n8 target. No scientific executable, solver, enumeration, numerical check, compilation, CLI or nested agent was used.

**Status: CANDIDATE, not independently reconstructed or parent-accepted.** The principal theorem below excludes a genuine low-span family, not just an encoding. Its n8 corollary would exclude K5 when combined with the previously derived covariance budget. A B3 consequence additionally needs the separate sector/rank14 candidate and, for full B3 coverage, the explicitly named OLD K1/K2/K3 imports. Those compositions are not promoted to acceptance by this author manuscript.

## 1. Statement and invariant

Let Q_1,...,Q_t be actual mutually orthogonal QLS(n), t>=2. The definitions are those of Ball–Simoens arXiv:2607.12933v2 §§2.2–2.3: every actual row/column is an ONB of C^n, and for s!=u and distinct cells x,y,

    <Q_s(x),Q_s(y)> <Q_u(x),Q_u(y)>=0.                     (T)

Let

    a_s=dim_R span_R {Q_s(x)Q_s(x)^*: all cells x}.

**Theorem LS.** If n<2(t+1), every nonclassical square in this family has

    a_s>=n+3.                                              (1)

Equivalently a_s<=n+2 forces that square to be classical. The entire family need not be classical; the assertion concerns the operator-span cost of each nonclassical member. All vector phases are arbitrary complex phases. No preferred support pattern or fixed coordinate field is assumed.

We prove it for square1. Any actual row or column may be chosen as the reference ONB and independently unitarily mapped to a coordinate basis in square1. This does not change a_1, classicality or the physical tensor identities. It does not change the other squares' physical vectors or identify their frames.

## 2. Two elementary dimension-saturation tools

### 2.1 Two-matchings bound

Suppose X and Y are disjoint cell matchings on the same m actual rows and m actual columns, and for each OTHER square s=2,...,t its entries on X and Y are ONBs of the SAME m-dimensional subspace K_s. Then

    m>=t+1.                                                (2)

Indeed fix x in X. Two different Y-cells share its row and its column. Every transition row from Q_s(x) to the Y-basis has zeros in those TWO positions and is nonempty elsewhere. The t-1 transition supports are disjoint by (T), so t-1<=m-2. This argument is the full content of (2); the subspaces K_s may differ across squares.

### 2.2 Isolated two-space

If all square1 cells lie either in a fixed two-space B or in B-perp, each actual line has exactly two B-vectors forming an ONB of B. Group B-cells by their unordered orthonormal ray-pair. A class on m_a rows is on m_a columns and has m_a occurrences of each ray, as two disjoint matchings. All cross overlaps between distinct ray-pairs in C^2 are nonzero.

For every other square, its spans from distinct classes are therefore orthogonal by (T); each class span has dimension at least m_a because each repeated ray forces m_a orthonormal vectors. The m_a sum to n, so all dimensions saturate: each class span has dimension m_a and both matchings are bases of it. Equation(2) gives m_a>=t+1 for EVERY class. Two different classes would require n>=2(t+1).

Thus, under the strict inequality in Theorem LS, an isolated two-space can use only one fixed ray-pair. In particular a globally isolated two-space containing a noncoordinate superposition of its two reference rays is impossible.

These arguments were proved independently of a_s in the earlier sector candidate; they are recalled here so that their hypotheses are explicit. They concern WHOLE vectors in selected subspaces, never merely projected parts.

## 3. One-channel lemma

This extension handles two overlapping coordinate edges and is essential; treating all low-span patterns as disjoint two-blocks would be false.

Let B be a two-space, choose unit b in B and unit c in B-perp, and put F=span(b,c). Assume every square1 cell is of one of three kinds:

- wholly in B;
- wholly in B-perp;
- in F, with nonzero components along both b and c.

Call the third kind mixed. Assume at least one mixed cell, and at least one B-pure cell whose ray does NOT belong to beta={b,b-perp}. Then

    n>=2(t+1).                                             (3)

*Proof.* Every row containing mixed cells has at least two, because the B/B-perp off-block part of its ONB resolution must sum to zero and a single mixed projector contributes a nonzero term. It has at most two, since those vectors are orthogonal in the two-space F. Hence it has exactly two, forming an ONB of F. Its remaining B-pure part consists of exactly one ray b-perp. The same holds in every mixed column. If k is the number of mixed rows, there are2k mixed cells and therefore also k mixed columns.

A nonmixed row has two B-pure vectors forming an ONB of B. Let m_beta count its rows whose ray-pair is beta; for each other ray-pair alpha, let m_alpha count its rows. Then

    k+m_beta+sum_alpha m_alpha=n.                          (4)

Among beta B-pure cells, b occurs m_beta times and b-perp occurs m_beta+k times. Each alpha has m_alpha occurrences of each ray. Its two occurrence sets are matchings on m_alpha rows and columns. A cell on alpha cannot be in a mixed row/column, since those have only the B-pure ray b-perp.

For each other square s, form spans K_{s,beta} and K_{s,alpha} from its entries on these pure-B classes. Different ray-pairs have all cross overlaps nonzero in square1, hence their spans are orthogonal. The repeated rays imply lower bounds m_beta+k and m_alpha. These add to n by (4), forcing every dimension bound to be tight and giving an orthogonal direct sum of C^n. Both alpha matchings are therefore ONBs of an m_alpha-space, and (2) gives

    m_alpha>=t+1.                                         (5)

There is at least one alpha by hypothesis.

At a mixed cell, square1 overlaps every alpha ray, so the other square's vector lies in K_{s,beta}. It also overlaps every pure-b cell. The latter entries are an orthonormal m_beta-set spanning L_s inside K_{s,beta}. Thus all mixed-cell entries of square s lie in

    W_s=K_{s,beta} intersect L_s-perp,      dim W_s=k.      (6)

The square1 mixed cells form a two-regular board on k rows/columns, with an ONB of F at its two selected cells per line. Group these cells by their orthonormal ray-pair in F. Class sizes ell_a sum to k. For the other square their repeated rays require dimensions at least ell_a, and different classes give orthogonal spans inside W_s. Saturation again gives the SAME ell_a-space for both matchings of each class. Equation(2) yields ell_a>=t+1 and therefore k>=t+1. With any alpha from (5), (4) proves (3). QED.

The complement B-perp may contain arbitrary vectors and arbitrary mixing internally. No hidden purity assumption on that complement was used.

## 4. Consequences of a small projector span in a line frame

Choose any actual line as reference basis e_1,...,e_n. Its projectors span the n-dimensional real diagonal algebra D. Since D is contained in S=span_R{Q_1(x)Q_1(x)^*}, the off-diagonal projection L of S has dimension

    dim L=a_1-n.                                          (7)

For any other actual line basis, let U be its transition matrix from the reference basis. If its bipartite support graph has c components, the span of the two bases' projectors has dimension2n-c. Indeed a Hermitian operator diagonal in both satisfies

    diag(d) U=U diag(lambda),
    (d_i-lambda_j)U[i,j]=0,

so intersection labels are arbitrary real constants on its c graph components. Thus that line's off-diagonal projector span has dimension n-c.

In particular, a connected component of transition size r costs at least r-1 off-diagonal dimensions. A component is square because its rows and columns are both orthonormal and supported inside it. If a_1<=n+2, every component has size at most3; a size3 component is the only nontrivial component of its line. If a cell vector has three nonzero coordinates T, its containing actual line therefore has exactly a connected size3 component on T and its off-diagonal projector span has dimension2. In that case a_1=n+2 and

    L equals that line's two-dimensional off-diagonal span,
    all matrices in L are supported inside T.              (8)

This uses dimensions of ACTUAL ONBs, not just their zero/nonzero graphs. No sparse-unitary catalogue is imported.

If a_1=n, S equals D and every rank-one cell projector is diagonal, so the square is classical. This also proves a_1>=n and its equality characterization.

## 5. Surplus one is impossible for a nonclassical square

Suppose a_1=n+1. No transition can have a component of size3 or more by §4; every cell therefore has weight1 or2 in the chosen line frame. There is a weight2 cell, otherwise the square is classical. Its off-diagonal projector has just one Hermitian edge, on coordinates a,b, and spans the one-dimensional L.

Every other off-diagonal cell projector is a real multiple of it, so it too is supported only on that same edge. A rank-one projector cannot have a nonzero coordinate outside {a,b} together with a coordinate inside or another coordinate outside; that would create an off-diagonal entry elsewhere. Thus every cell is either wholly in B=span(e_a,e_b) or is a singleton coordinate ray outside B. B is globally isolated and contains its reference coordinate pair and a genuinely mixed weight2 vector. This supplies two ray-pairs and contradicts §2.2. Hence a nonclassical square cannot have a_1=n+1.

## 6. Surplus two, with a weight2 cell in SOME actual line frame

Suppose a_1=n+2 and choose a reference line/frame in which a cell v has weight2 on {a,b}. Its off-diagonal projector E is supported on that ONE edge. Put B=span(e_a,e_b).

### Case A: some cell z has weight3 in this same frame

By (8), its containing line has a connected component on a three-coordinate set T and its two-dimensional off-diagonal span equals L. Since E belongs to L, both a and b belong to T. Write T={a,b,d}. Then

    L=span_R{E, offdiag(zz*)},

and all cell off-diagonal projectors are supported within T. Consequently every cell is either inside span(e_a,e_b,e_d) or a singleton outside T.

Across the B / span(e_d) split, E contributes zero and the other generator contributes z_B conjugate(z_d), which is nonzero. Every mixed cell w has w_B conjugate(w_d) equal to a real nonzero multiple of this vector, so w_B is parallel to the fixed direction u=z_B/||z_B||. Hence every cell is either B-pure, B-perp, or lies in F=span(u,e_d) with both components nonzero. There is at least one mixed cell z.

There is also a B-pure ray outside beta={u,u-perp}. If beta is not the reference pair {e_a,e_b}, at least one of those reference rays lies outside beta. If beta IS that pair, the original weight2 vector v lies outside beta. Thus the one-channel lemma applies and contradicts n<2(t+1).

### Case B: no cell has weight3 in this frame

All noncoordinate cell projectors have support on a single coordinate edge. Each distinct edge gives a nonzero vector in L whose coordinate support is disjoint from that of every other edge, so at most TWO distinct edges occur.

If only one edge occurs, its two-space is globally isolated and nonclassical, ruled out by §2.2. This remains true if its projectors use two independent complex phases on that one edge; no real-only restriction is imposed.

If two disjoint edges occur, each two-space is globally isolated and a noncoordinate vector on either edge contradicts §2.2.

If two overlapping edges occur, name them {a,b} and {b,d}. Every mixed cell is supported on one of these edges, because no weight3 cell exists. Take B=span(e_a,e_b), u=e_b and c=e_d. All cells are B-pure, B-perp or mixed in span(u,c). The second edge supplies a mixed cell; a noncoordinate vector on the first edge is a B-pure ray outside beta={e_a,e_b}. The one-channel lemma again contradicts the strict size inequality.

Thus a nonclassical square of surplus two cannot have ANY weight2 cell relative to ANY actual line frame.

## 7. Surplus two, with NO weight2 cell in ANY line frame

Continue to suppose a_1=n+2 and that square1 is nonclassical. In a chosen reference line frame some cell is noncoordinate; by the no-weight2 assumption and §4 it has weight3. Its containing line has exactly one connected three-component on a coordinate set A. By (8), L is supported on A. Therefore every cell vector is either entirely in the three-space V_A or a singleton coordinate outside A. V_A is globally isolated, and each actual line contains exactly three V_A-vectors forming an ONB of V_A.

For any two actual line bases, their V_A transitions have no column of weight2. A three-by-three unitary with this property is either monomial or has all entries nonzero: a non-full column must be a singleton; removing its isolated row/column leaves a two-by-two unitary, which is either monomial or has forbidden weight2 columns. This proves the assertion directly.

In particular, if an actual row and actual column meet at an A-cell, their A-bases share that cell's ray. Their transition cannot be full, so it is monomial: the two unordered A-bases coincide. Group all A-cells by these unordered A-bases. Each row belongs to one class; each column meeting it at an A-cell has the same class. A class on m_a rows has3m_a cells on m_a columns and exactly m_a occurrences of each of its three orthogonal rays. Each ray occurrence set is a matching on the same m_a rows/columns. The sizes m_a sum to n.

Different class bases have all cross overlaps nonzero: comparing any actual lines from the two classes, a non-monomial transition must be full by the preceding three-by-three argument. For every other square, different class spans are therefore orthogonal by (T). Each repeated ray forces dimension at least m_a; the lower bounds sum to n, so saturation makes every class span exactly m_a-dimensional and EACH of its three ray-occurrence matchings an ONB of it.

Apply (2) to any two of its three matchings: m_a>=t+1 for every class. There are at least two classes, because a single A-basis together with the fixed singleton complement would make the square classical. Thus n>=2(t+1), the last contradiction.

Sections5–7 exhaust a_1=n+1,n+2; §4 handles equality n. This proves Theorem LS.

## 8. Conditional n8 consequences and precise remaining target

### 8.1 Global K5 exclusion, using the separately written covariance budget

The earlier complete candidate `proof-global-gram-defect-v1.md`, read with its wording erratum1, proves

    sum_{s=1}^5(a_s-8)<=14.                                (9)

Its actual separate written reconstruction reported0F/0M/1wordingMINOR; parent acceptance is separate. Equation(9) is re-stated as an explicit dependency, not newly certified by this manuscript.

At n8,t5, Theorem LS gives a_s>=11 for EVERY nonclassical square. If all five were nonclassical, their surplus sum would be at least5*3=15, contradicting(9). Thus the composition of the two candidate proofs excludes K5, the class with all five squares nonclassical. It neither proves that a family with four nonclassical squares exists nor excludes K4.

### 8.2 B3 K4/K5 exclusion, using the separate sector/rank14 proof

`proof-isolated-sector-exclusion-v1.md` proves, under literal B3 axes, a_1>=14. Square1 is nonclassical already from its two distinct B-axis bases. If a B3 family had at least four nonclassical squares, the other three nonclassical squares would each have a_s>=11 by Theorem LS; the last square has a_s>=8. Therefore its total surplus would be at least

    (14-8)+3*(11-8)=6+9=15>14,

again contrary to(9). This excludes B3 K4/K5 at the stated candidate-composition boundary.

The OLD accepted internal records `moqls8-k1k2-parent-verdict.md` and `moqls8-k3-parent-verdict.md` exclude exactly one, two or three nonclassical squares, respectively. IF those computational/classification-based imports are consumed at their literal existing trust boundaries, the new B3 K4/K5 exclusion completes a genuine B3 exclusion. Those older results are not this round's discoveries; their retained source, compiler/checker, catalogue, proof-retention and review qualifications are not erased.

This is a physical-configuration exclusion, NOT Boolean UNSAT of GB_B3 or GB_B3 AND M2. GB B3.M2 remains UNKNOWN as an exact Boolean-input fact. The remaining B2 inputs B2.M2/B2.M4 also remain UNKNOWN. No GA/GB count or final composition gate is silently raised.

### 8.3 Full Problem16 n8 remains unresolved here

Without importing the old K1/K2/K3 exclusions, the new global result only rules out K5. With them, the unrestricted nonclassical family would have exactly four nonclassical squares, each with projector-span at least11. Other normalized support classes, notably the still-open genuine B2 frontier, are not covered by the new B3 argument. U/T16/WMAN/NF and final A10/A11 acceptance remain separate. No full unrestricted D=0 theorem or exact D>0 point is delivered.

## 9. Trust and novelty boundaries

- Core Theorem LS uses only the physical definitions, actual ONB span dimensions, the two-matchings bound, two-space ray geometry and the one-channel saturation proof displayed here. No finite search, old K closure, Gram CNF, T16 cover or prior scalar bound is a premise.
- The separately written covariance budget and B3 rank14 proof enter ONLY §8 compositions, at their still-candidate boundaries. The first has an actual peer reconstruction plus a minor wording erratum; the second still needs its own complete reconstruction. Shared author derivation is not independent checking.
- Old K1/K2/K3, their Egan–Wanless classification imports and native certificates enter ONLY the explicitly conditional full-B3 consequence. They do not prove Theorem LS or remove the GB Boolean UNKNOWNs.
- No formal/kernel/human acceptance, priority, novelty or SOTA comparison is asserted. The rank/frame and Gram principles themselves are established tools. The concrete branch exclusions need actual written checking and primary prior-art comparison before stronger labels.
- All files are new immutable snapshots in the owned root. No runtime was restarted or repaired; no certificate replay or scientific execution was attempted. All HOLD, preservation and older process obligations survive.
