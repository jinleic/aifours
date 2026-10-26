# Candidate v1 — two entirely thin axes force forbidden product officers

Observed before creation: `2026-10-23T14:26:12-0700`. PhysicsAME46, physics-6. Immutable WRITTEN CANDIDATE / PARTIAL. No scientific execution or independent reconstruction. This is a stronger family exclusion than `three-thin-axes-exclusion-v1.md`; old snapshots remain intact.

## 1. Literal theorem, import and novelty boundary

Let ψ∈(C^6)^⊗4 be AME, with arbitrary complex amplitudes in any product orthonormal basis. Put A_x=6ψ_x, T={x:|A_x|=1}, N=supp A\T, t=|T|, h=36−t, e=|supp A|−(72−t), and d_(i,a)=6−|{x∈T:x_i=a}|. A coordinate is entirely thin when all its positive deficits are2, allowing zero deficits.

**Candidate theorem.** If e=0 and N is nonempty, at most one coordinate is entirely thin. Equivalently, every such AME tensor has at least three coordinates each containing a local value of deficit≥3.

This is a theorem about a necessary support structure across arbitrary complex amplitudes, not an assumption that an unrestricted support minimizer has e=0. It does not exclude the remaining e=0 profiles with three/four thick axes, nor any e>0 stratum. Thus the unrestricted documented range remains48≤s_min≤60; no stronger numeric lower bound or new state is claimed.

The written proof uses:

- the exact-two-line/closed2×2 facts in the pinned `thin-slice-obstruction-v1.md`, SHA256 `ba269009d0f352e9b9fed1967cead86b5594b9ddee6d822cd8190fc67c2bce4f`;
- that file's Theorem A: at e=0, a doubled fiber in coordinate i closes into a cubic bipartite qubit module with at least6 vertices, hence both values of coordinate i have deficit≥3. In particular a Hamming-distance-one support pair cannot involve a deficit2 value in its varying coordinate;
- the standard no-AME(4,2) theorem (elementary proof supplied in the pinned file §4);
- **Ball–Simoens, arXiv:2603.02334v1, Theorem6:** “There does not exist a pair of orthogonal quantum Latin squares of order six.” Definitions1–3 and Theorem6 were read directly at https://arxiv.org/html/2603.02334v1 . The latest arXiv API entry read still identifies v1. A raw source snapshot is `ball-simoens-2603.02334v1.html`.

Ball–Simoens is an explicit external theorem import, not reproved or formally verified here. The equivalence needed to use it is proved in §5, rather than inferred from the paper's title. Its result forbids a pair of ordinary vector-valued QLS with tensor-product orthogonality; it does not forbid entangled-officer AME(4,6) states, which do exist. Novelty of the new-to-this-slot thin-axis reduction is not cleared.

## 2. Classifying a thin slice by balanced binary planes

Assume coordinates3 and4 are entirely thin. Their active values form sets C,D of the same size k=h/2≤6. For each c∈C, the non-officer slice x3=c has exactly4 points. In each of the other coordinates1,2,4 it takes exactly two values, each exactly twice. Assign binary labels to those two values temporarily.

### Four-point plane lemma

Four distinct binary triples with each coordinate taking0 and1 twice form either a parity plane x⊕y⊕z=ε, or a plane in which two coordinates have a fixed XOR and the third is free.

**Written proof.** Each coordinate partitions the four points into two pairs. There are exactly three such unordered2+2 partitions of a four-element set. If two coordinate partitions coincide, those bits agree or disagree everywhere; the third partition must differ (otherwise there would be only two distinct triples), and all four triples of the stated free-coordinate plane occur. If no two partitions coincide, they are the three different partitions; after labeling points by the first two bits, the third is their XOR or its complement. These exhaust the cases without enumerating candidate tensors. ∎

In slice c, use bits u for coordinate1, v for coordinate2 and w for coordinate4. The free-w plane u⊕v=ε cannot occur: it contains support pairs differing only in coordinate4, whose involved values are thin, contradicting Theorem A's deficit consequence. The remaining forms are:

- **Type E:** u⊕v⊕w=ε. For a fixed coordinate4 value, its two entries differ in both coordinates1 and2; the corresponding two-term vector in C^6⊗C^6 is entangled.
- **Type P1:** v⊕w=ε, u free. For a fixed coordinate4 value, its two entries differ only in coordinate1 and form a product vector.
- **Type P2:** u⊕w=ε, v free. The two entries differ only in coordinate2 and also form a product vector.

Exactly the same classification applies to each thin slice x4=d, with the roles of coordinates3 and4 interchanged. All assertions concern support and exact nonzero coefficients; complex phases and unequal moduli have not been discarded.

## 3. An entangled edge would propagate around a thin-axis cycle

Let H be the bipartite graph on C∪D with an edge(c,d) when that pair-line meets N. Each c has exactly two d-neighbors and each d has exactly two c-neighbors, because its deficit is2. Thus each component is a simple even cycle of length2r with r≥2. Every edge contains exactly two non-officer coefficients in coordinates1,2.

The edge's difference pattern in coordinates1,2 uniquely determines whether it is of type E,P1 or P2. At either endpoint, both incident edges have the slice's same type. Therefore an entire connected cycle has one type.

Suppose a cycle has type E. At each of its vertices the same two coordinate1 values and same two coordinate2 values occur on both incident edges. Along the connected cycle these sets are constant; denote them{a0,a1} and{b0,b1}. The two entries at an edge use either the diagonal pair{(a0,b0),(a1,b1)} or the opposite diagonal{(a0,b1),(a1,b0)}. The parity-plane form makes the two incident edges at every vertex use opposite diagonals. Hence the diagonal choice alternates around the2r-cycle, with r edges of each choice.

In the unitary flattening M_(12|34), each of the two rows of one diagonal receives a nonzero coefficient from each of its r edges. It contains a non-officer, so its exact total degree is2. Thus r≤2. Combined with r≥2, we obtain r=2.

The cycle is therefore K_(2,2), on two values of coordinate3 and two of coordinate4, and its8 coefficients lie in the selected2×2×2×2 subcube. All selected rows in each of the three flattenings are full inside the subcube:

- for12|34, every selected first-pair row receives exactly the two same-diagonal edges, and every selected last-pair column has its two entries;
- for13|24, in each coordinate3 slice the parity plane gives two entries for each of the two coordinate1 values, filling each selected row; the selected columns are filled similarly by coordinate4 slices and coordinate2 values;
- for14|23 the same statement follows with coordinates3,4 interchanged.

Let B_12,B_13,B_14 be these4×4 submatrices. The rows have no outside entries and are orthonormal in the original unitaries, so every B_P is unitary. For ω=3ψ restricted to the8 entries, ||ω||²=9·4/36=1 and the flattening of2ω is B_P. The six actual two-qubit reductions are explicitly

    ρ^ω_12=B_12 B_12†/4=I4/4,     ρ^ω_34=(B_12†B_12)^T/4=I4/4,
    ρ^ω_13=B_13 B_13†/4=I4/4,     ρ^ω_24=(B_13†B_13)^T/4=I4/4,
    ρ^ω_14=B_14 B_14†/4=I4/4,     ρ^ω_23=(B_14†B_14)^T/4=I4/4.

This would be AME(4,2), impossible. **No type-E cycle exists.**

## 4. Therefore every officer in this cut is a product state

For every pair(c,d)∈[6]², define the normalized column officer

    w_cd = Σ_(a,b) A_abcd |a⟩⊗|b⟩  in C^6⊗C^6.

It has norm1 because M_(12|34) is unitary. If its column contains an officer coefficient, it is a computational product vector. Otherwise(c,d) is a hole edge of H. By §3 it has type P1 or P2, so its two terms differ in only one of a,b and it is again a product vector. There are no other columns: every column is nonempty, and a singleton column is an officer.

Consequently all36 vectors w_cd are product vectors. This is an exact statement about Schmidt rank1 in this cut, not a statement that the full four-party state is unentangled.

## 5. Checking the precise AME-to-QLS bridge

Choose unit vectors p_cd,q_cd∈C^6 with w_cd=p_cd⊗q_cd, absorbing any overall phase into p_cd. Since the36 columns of M_(12|34) are orthonormal,

    ⟨p_cd,p_c′d′⟩ ⟨q_cd,q_c′d′⟩ = δ_cc′ δ_dd′.

It remains to prove that each array p,q separately is a QLS, rather than assume this from product orthogonality.

The four cross-pair marginals of the original AME tensor give their diagonal blocks as follows:

    36 [ρ_13]_(c,c) = Σ_d Tr_2 |w_cd⟩⟨w_cd| = Σ_d |p_cd⟩⟨p_cd| = I6,
    36 [ρ_14]_(d,d) = Σ_c Tr_2 |w_cd⟩⟨w_cd| = Σ_c |p_cd⟩⟨p_cd| = I6,
    36 [ρ_23]_(c,c) = Σ_d Tr_1 |w_cd⟩⟨w_cd| = Σ_d |q_cd⟩⟨q_cd| = I6,
    36 [ρ_24]_(d,d) = Σ_c Tr_1 |w_cd⟩⟨w_cd| = Σ_c |q_cd⟩⟨q_cd| = I6.

Here a displayed diagonal block fixes the coordinate3 or4 index and leaves the coordinate1 or2 matrix indices free; [I36/36]_(c,c)=I6/36. These identities are exact consequences of the corresponding full two-party AME marginals. Each sum has six unit rank1 projectors in a six-dimensional space. Their6×6 synthesis matrix V therefore satisfies VV†=I6 and is unitary, so its columns are an orthonormal basis. Thus every row and every column of p is an ONB; the same holds for q. They satisfy Ball–Simoens Definition1.

The product inner-product identity above is exactly Ball–Simoens Definition2, so p and q are a pair of orthogonal QLS(6). The remaining complementary marginalρ_34 is already I36/36 by M_12†M_12=I; ρ_12 is I36/36 by M_12 M_12†=I. All six original marginal conditions have therefore been accounted for in the bridge.

Ball–Simoens Theorem6 rules out this pair. The assumed two entirely thin coordinates cannot exist. ∎

## Consequence, verification status and remaining problem

A permutation of parties carries the same proof to any pair of entirely thin coordinates. Hence an e=0 AME(4,6) with N≠∅ requires at least three coordinates with a deficit≥3 value. The earlier three-thin-axis and binary-full profile exclusions are special cases, though the earlier proof has the smaller external import set and remains preserved.

This candidate replaces neither the unrestricted target nor the true two-party AME conditions. It supplies a new analytic necessary condition and excludes whole profile families, not a lower49 proof. The remaining route must control profiles with at most one entirely thin coordinate, and all e>0 support48 cases. Proving an unrestricted stronger bound requires those additional cases, not just this family.

No scientific program, finite tensor search, numerical assay, solver, compilation or kernel replay was run. Source read, metadata hash and written reconstruction are distinct from independent verification. This snapshot still needs a separate agent's actual reconstruction and a parent check; no acceptance or novelty is claimed.
