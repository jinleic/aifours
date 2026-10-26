# Candidate v1 — doubled-fiber modules and a pointwise thin-slice obstruction

Observed before creation: `2026-10-23T14:08:26-0700`. PhysicsAME46, physics-6. Immutable written candidate; no scientific execution. **PARTIAL / CANDIDATE, not independently reviewed, not a stronger numerical support bound, not a discovery/novelty claim.** The documented unrestricted range remains48≤s_min≤60.

## 1. Exact scope and baseline imports

Let ψ be any AME(4,6) pure state, with arbitrary complex amplitudes, expressed in any product orthonormal basis. Put A_x=6ψ_x, S=supp A, T={x:|A_x|=1}, N=S\T, t=|T|, h=36−t and e=|S|−(72−t). For coordinate i and value a, set t_(i,a)=|{x∈T:x_i=a}| and d_(i,a)=6−t_(i,a).

**Throughout the structural theorems below assume e=0.** This is an explicit restriction on a support stratum, not an inference that every minimum-support AME has e=0. The e>0 strata remain necessary for an unrestricted numerical lower bound.

Previously established elementary facts (re-derived here as needed; not new contributions) are in the frozen six-lane `SUPPORT_LOWER42.r2.md` §§0–1 and `SUPPORT_LOWER46.r2.md` Lemma15:

- For every fixed two-coordinate line L, Σ_(x∈L)|A_x|²=1.
- An officer is alone in every such line through it. Distinct officers agree in at most one coordinate.
- Every line without an officer has at least two non-officer entries.
- At e=0 it has exactly two: the sum over the36 rows in any flattening is exactly t+2h. Apply this to all six choices of fixed coordinate pair.
- In any flattening, non-officer components are closed2×2 unitary blocks. To see this directly, every non-officer row/column has degree2. If two rows share a column they must share a second, because a one-term nonzero inner product cannot vanish. Their two-column supports coincide; they and these columns form a closed2×2 block.
- Consequently the non-officer slice x_i=a has exactly2d_(i,a) points: in each partner coordinate there are6−t_(i,a)=d_(i,a) lines without an officer, each with two entries. Every partner coordinate takes exactly d_(i,a) values in that slice, each exactly twice. The officer entries in the slice number6−d_(i,a). Thus |{x∈S:x_i=a}|=6+d_(i,a).

All marginal conditions used here are genuinely two-party conditions. For a cut P|Pᶜ, M_P is the flattening of A. Direct tracing gives

    ρ_P = M_P M_P†/36,
    ρ_Pᶜ = (M_P† M_P)^T/36.

The three cuts12|34,13|24,14|23 therefore account for all six required marginals, including off-diagonal coherences. No one-body or approximate substitute is used.

## 2. Doubled fibers form cubic bipartite qubit modules

Fix one coordinate i and two distinct local values a,b. Write z for a triple in the other coordinates j,k,l. Define

    D = {z : A_(a;z) ≠0 and A_(b;z) ≠0}.

A member of D is a doubled fiber. Its two entries are necessarily non-officers. Join z,z′ in D by a color-j edge if z_j=z′_j. The following statement in particular proves that this rule never creates a clique larger than an edge.

### Theorem A

If D is nonempty:

1. Every used value in each of the three coordinates occurs at exactly two vertices of D. Every vertex has one neighbor of each color; these three neighbors are distinct. Distinct vertices agree in at most one coordinate. Thus the graph is simple cubic, properly3-edge-colored, each color a perfect matching.
2. Every connected component C is bipartite, has equally many vertices in its two parts, and has at least6 vertices.
3. Put v_z=(A_(a;z),A_(b;z))ᵀ. Each v_z has norm1. On a component C, the vectors in one bipartition class are proportional to one unit vector u_C and those in the other to its orthogonal complement w_C. Hence one2×2 unitary acting only on the local span{|a⟩,|b⟩} makes **every doubled fiber in C a singleton**. This is an actual local-unitary operation, not independently chosen row rotations.
4. For every component C,

    |C| ≤ 2d_(i,a) and |C| ≤ 2d_(i,b).

In particular d_(i,a),d_(i,b)≥3. There cannot be two support points differing in just one coordinate if either of their values in that coordinate has deficit2.

**Proof.** Fix z∈D and a partner coordinate j, with {j,k,l} the other three. In the flattening ij|kl, the column(z_k,z_l) has the two nonzeros in rows(a,z_j),(b,z_j) and nothing else, by the exact-two-line property. These rows lie in one closed2×2 block. Its other column supplies a unique z′∈D with z′_j=z_j.

Both other coordinates of z′ differ from those of z. If, for example, z′_k=z_k, then the four block entries would all lie on the line fixing j and k, contradicting its exact two entries. This also shows that two D vertices cannot share two coordinates. For any fixed j-value, row(a,z_j) already contains its two nonzeros, so no third D vertex has that j-value. This proves assertion1, including closure rather than merely an assumed graph pattern.

Fixing k,l through z gives exactly the two entries of v_z, so ||v_z||²=1. If z and z′ are a color-j edge, the2×2 block just constructed has columns v_z,v_z′. They are orthonormal, so v_z′ spans the unique orthogonal-complement ray of v_z in C². Along any graph walk the rays alternate between a ray and its orthogonal ray. An odd closed walk would make a nonzero vector orthogonal to itself, impossible. Thus every component is bipartite. Cubic degree implies its two parts have equal size, since both count the same edges as3 times their size. Simplicity forces each part to have at least3 vertices, so |C|≥6. The walk argument also proves the common pair of orthogonal rays on C, and the unitary taking these rays to the two coordinate axes proves assertion3.

Each vertex of C contributes one distinct non-officer coefficient to slice(i,a), which has exactly2d_(i,a) points; likewise for(i,b). This proves assertion4 and its deficit consequence. ∎

**Relation to the previous triangle lemma.** The old ENGINE_V4 Lemma20 excludes one doubled triangle. Theorem A excludes every odd cycle and gives the full qubit-ray transport and basis-change mechanism; it does not claim that triangle-free implies phase-consistent. Pandya's2×2 phase-linearization lemma is a prior ingredient/mechanism, not this slot's invention.

## 3. Exact support cost of the module rotation

Let D_tot=|D|. Let Q be the number of triples z for which exactly one of A_(a;z),A_(b;z) is nonzero, counting officer as well as non-officer singletons. All other local levels are unchanged by the unitary from Theorem A.

### Theorem B

For each component C, there is a locally equivalent AME state with support s′ satisfying

    s′ ≤ s + Q − |C|,
    Q+2D_tot = 12+d_(i,a)+d_(i,b) ≤24.

If the present basis minimizes support in ψ's local-unitary orbit, then |C|≤Q. Consequently for each coordinate/value pair either D is empty, or exactly one of these two possibilities holds:

- D has6 vertices, its graph is K_(3,3), d_(i,a),d_(i,b)≥3, and Q=d_(i,a)+d_(i,b)≥6;
- D has8 vertices, its graph is K_(4,4) with a perfect matching removed (the cube graph), d_(i,a)=d_(i,b)=6, and Q=8.

The same classification applies to **any e=0 AME tensor of support48**, without assuming an orbit-minimizing basis, if one imports the existing unrestricted lower bound48.

**Proof.** Each fiber in C had two nonzeros and after the unitary has one. Other doubled fibers can have at most two. Each singleton can have at most two, so support increases by at most Q there. This proves the inequality. In fact the chosen unitary is nonmonomial, since u_C and w_C each initially have two nonzero coordinates; every singleton therefore becomes exactly double, but only the upper bound is needed.

The second equation counts all entries on levels a,b using the final slice count in §1. If the basis is orbit-minimizing, s′≥s, giving |C|≤Q. Every component has at least6 vertices. Two components would give D_tot≥12 and Q≥6, contradicting2D_tot+Q≤24. There is therefore one component, D_tot=|C|. It is even and at least6, and3D_tot≤2D_tot+Q≤24, hence D_tot∈{6,8}. A simple cubic bipartite graph with parts of size3 is K_(3,3). With parts of size4 it is K_(4,4) minus a perfect matching. If D_tot=8 then Q≥8 forces equality throughout, giving d_(i,a)+d_(i,b)=12, hence both equal6 and Q=8. If D_tot=6 the equation gives Q=d_(i,a)+d_(i,b), and Theorem A supplies each deficit≥3.

For s=48, the existing theorem s′≥48 under every product basis supplies s′≥s even without asserting that the state is globally or orbit-minimal. The old48 theorem is used only for this last corollary; no old certificates are rerun or recounted as a new bound. ∎

## 4. A pointwise obstruction from four thin values

Call a local value thin if its deficit is2. This definition refers to the officer set of the current basis, not to local Hilbert-space dimension.

### Theorem C

In any e=0 AME(4,6) tensor there is **no** x∈N satisfying

    d_(1,x1)=d_(2,x2)=d_(3,x3)=d_(4,x4)=2.

This conclusion does not require support minimization or the numerical lower bound48.

**Proof.** Suppose x=(a,b,c,d) has four thin values. Its closed2×2 block in cut12|34 contains

    x=(a,b,c,d),        y=(a,b,c′,d′),
    z=(a′,b′,c,d),      w=(a′,b′,c′,d′).

Here a′≠a,b′≠b,c′≠c,d′≠d. For instance, if c′=c, x and y would differ only in coordinate4 whose value d is thin, contradicting Theorem A. The other inequalities follow in the same way. All four points are in N.

The non-officer slice x1=a has exactly4 points. Its coordinate3 and4 value sets are exactly{c,c′} and{d,d′}. Its coordinate2 value set is{b,b₀} for some b₀≠b. Since x,y exhaust the line(a,b), the other two points have coordinate2=b₀. Exact twice-per-value counts in coordinates3,4 leave two possibilities. The uncrossed possibility includes(a,b₀,c,d), which differs from x only in coordinate2 at the thin value b, impossible by Theorem A. Hence the slice's other points are

    p=(a,b₀,c,d′),     q=(a,b₀,c′,d).

The thin slice x3=c contains x,z,p. Its coordinate2 value set has size2 and already contains b,b′ from x,z; therefore b₀=b′. Its coordinate1 and4 value sets are{a,a′} and{d,d′}. The exact twice-per-value counts force its fourth point to be

    r=(a′,b,c,d′).

Similarly the thin slice x4=d contains x,z,q and forces

    u=(a′,b,c′,d).

Thus the following eight points all belong to N, with0/1 standing for unprimed/primed values:

    0000,0011,1100,1111,0101,0110,1001,1010.

They are the even-parity words in{0,1}⁴. For each choice of any two coordinates and their values, exactly two of these eight words have those values. Each corresponding pair-line is therefore already full: at e=0 a line containing N has exactly two entries. No entry outside these eight can meet any such pair-line.

For **each** of the three cuts12|34,13|24,14|23, take the4×4 submatrix B_P of M_P with row values from the two selected local values in each row coordinate and column values from the selected local values in each column coordinate. All four selected rows have their two nonzeros among these eight entries, so they have no outside entries. Their orthonormality in M_P gives B_P B_P†=I4. It follows that B_P is unitary and also B_P†B_P=I4. This is true independently for all three cuts.

Let ω=3 times the restriction of ψ to these eight entries, identified with a four-qubit vector. Its squared norm is9·(4/36)=1, since B_(12) has four unit rows. The flattening of2ω in cut P is exactly B_P, because2·3ψ=6ψ=A. Direct partial tracing now gives

    ρ^ω_12=B_12 B_12†/4=I4/4,
    ρ^ω_34=(B_12†B_12)^T/4=I4/4,
    ρ^ω_13=B_13 B_13†/4=I4/4,
    ρ^ω_24=(B_13†B_13)^T/4=I4/4,
    ρ^ω_14=B_14 B_14†/4=I4/4,
    ρ^ω_23=(B_14†B_14)^T/4=I4/4.

This would be an AME(4,2), impossible. For completeness, the standard elementary obstruction is: expand |ω⟩⟨ω| in Pauli strings and let A_k be the sum of squares of its weight-k expectations. The displayed pair marginals imply A0=1,A1=A2=0. Each three-qubit reduction has purity1/2, by its complementary one-qubit marginal I2/2, so the four triples contribute A3=4·3=12. Purity of ω gives A4=16−1−12=3. Spin flip multiplies each weight-k Pauli coefficient by(−1)^k; its overlap with the original positive state would consequently be(1−12+3)/16=−1/2, impossible for the trace of a product of positive semidefinite matrices. This is the standard no-AME(4,2) proof, not a new claim. ∎

## 5. Profile-level consequences and exact verification obligations

Write W_i={a:d_(i,a)≥3}. By Theorem C every point of N lies in at least one thick-value slice x_i∈W_i. Counting these incidences and using |N|=2h and |N∩{x_i=a}|=2d_(i,a) proves the necessary condition

    h ≤ Σ_i Σ_(a∈W_i) d_(i,a).

Equivalently, if m_i is the number of deficit2 values in coordinate i, then

    2Σ_i m_i ≤3h.

This is an analytic profile filter, not an enumeration. In particular no nontrivial e=0 AME tensor can have every positive deficit equal2 in all four coordinates: then the right side of the first inequality is0<h. The old finite proof already excluded some such profiles at larger t. The pointwise theorem and filter apply without enumerating any support, including new strata; they are not by themselves a complete exclusion of t=24,e=0 or s=48.

At t=24,e=0, h=12. Theorem C excludes every profile whose total thick deficit is below12. Theorem B further confines any doubled fibers to the K_(3,3)/cube alternatives in any support48 realization. The difficult profile{6,6}{2⁶}³ is **not** excluded in full by the thin-value inequality: its thick deficit equals12. Its remaining patterns can have no doubled fibers, one six-vertex module or one eight-vertex module; proving those alternatives incompatible with all officer placements is still open here. This is an exact remaining obligation, not UNKNOWN relabeled UNSAT.

A definition-level validation of this candidate needs only written reconstruction: check exact-two closure, the qubit-vector transport, the support-cost inequality and all six displayed qubit reductions. No graph enumeration, numerical tensor, source-independent solver or scientific program was run. A future executable application must separately pin an input support/officer list, verify the full exact-two incidence and all module edges, and obtain a named parent GO before running. Merely finding no module, passing these necessary tests, or satisfying squared-modulus equations does not construct an AME state.

## 6. Claims not made

- No s_min≥49 theorem, no support≤59 state, no resolution of the unrestricted gap.
- No assertion that an unrestricted minimizer has e=0, no exclusion from one convenient symmetry class alone presented as full nonexistence.
- No kernel/Lean proof, executable arithmetic check, independent reconstruction, outside-model or human review at this snapshot.
- Novelty and significance beyond the new-to-this-slot written structural mechanism remain unestablished. The old48 lower bound and Pandya/Bruzda60-term states remain baselines.
