# PROJECTOR-INVARIANT v1 — all-object kernel, exact defect and a universal relaxation barrier

Clock actually observed before creation: **2026-10-23T14:10:00-07:00**. Author PhysicsRQLS10. Target and baseline are frozen in `selection-v1.md` and `baseline-dependency-freeze-v1.json`.

**CANDIDATE / PARTIAL, written only.** Every necessary statement below holds for every Latin B and arbitrary complex vectors satisfying the 30 exact bases, not only flat-coordinate or WH arrays. The explicit H₀ below is **not a physical witness**. The bounded attack closes the naive projector-Gram relaxation as an obstruction route, and isolates its missing complex rank-one lift. It does **not** decide maximal 1-RQLS(10). No scientific program, enumeration, numerical test or kernel ran. Novelty is not established; frame/Gram methods and projection constraints have substantial prior art.

## 1. A fixed 28-dimensional kernel for every possible resolution

For each cell p let `P_p=q_p q_p*` and `Q_p=P_p-I/10`. Work in the real Hilbert space of Hermitian 10×10 matrices, with inner product `tr(AB)`. Define two 100×100 real symmetric matrices

    H_pq = tr(P_p P_q) = |<q_p,q_q>|²,
    C_pq = tr(Q_p Q_q) = H_pq-1/10.

Thus H and C are positive semidefinite Gram matrices; C is the centered projector Gram matrix, **not** the ordinary complex vector Gram G of GRAM-CERT.

For a line L among the 30 rows, columns and B-classes let `l_L∈R^100` be its indicator column. Its ONB condition gives

    sum_(p∈L) P_p = I,
    sum_(p∈L) Q_p = 0.

Therefore

    C l_L=0,                    H l_L=1.                    (1)

Let S be the real span of these 30 indicators. Then **dim S=28**, independently of B.

**Proof of the dimension.** For each of the three parallel classes (rows, columns, symbols), its ten disjoint line indicators span a ten-dimensional space containing the all-ones vector 1. Their zero-sum contrasts have dimension nine. Contrast spaces from different parallel classes are mutually orthogonal: every line from one class meets every line from the other in exactly one cell, so for contrasts `l-l′` and `m-m′` the inner product is `1-1-1+1=0`. Every contrast is orthogonal to 1. Hence S is the orthogonal direct sum of span{1} and three nine-dimensional contrast spaces, with dimension `1+3*9=28`. QED.

Consequently

    C⪰0,   S⊆ker C,   rank C≤72,   tr C=100*(9/10)=90,
    H⪰0,   rank H≤73.                                      (2)

The rank-73 bound uses `H=C+J/10`, where `J=11ᵀ`, and C1=0. Equivalently, the 100 rank-one projectors cannot span more than 73 real operator directions; their centered versions cannot span more than 72. This is an **all-object** invariant. A hypothetical unrestricted proof cannot simply assume these 100 projectors are independent.

## 2. Exact fourth-moment defect, with equality fully characterized

Every cell shares its three lines with 27 distinct other cells, hence has exactly 72 cells sharing no line. Put `p⊥_B q` for a required line-orthogonality pair and `p~q` for a distinct pair sharing no line. Both notations here concern cells; `p~q` does not mean that its vectors have a nonzero inner product.

Summing the projector identity over all ten rows gives `sum_q P_q=10I`, so

    sum_q H_pq=10,       sum_(q~p) H_pq=9.                 (3)

There are 7200 ordered pairs p~q. Expanding squares using (3) gives the exact identity

    sum_(p,q) |<q_p,q_q>|⁴
       = 425/2 + sum_(p~q) ( H_pq-1/8 )².                 (4)

**Proof.** The 100 diagonal terms H_pp² contribute 100; all 2700 ordered required-edge terms contribute zero. For each p, the 72 remaining H-values sum to 9. Thus

    sum_(q~p) (H_pq-1/8)²
      = sum_(q~p) H_pq² - (1/4)*9 + 72/64
      = sum_(q~p) H_pq² - 9/8.

Sum over 100 p and add the diagonal contribution: `100+100*9/8=425/2`. QED.

In particular, the fourth moment is at least **425/2**, and equality holds exactly when every line-disjoint pair has squared overlap **1/8**. Also some line-disjoint pair has squared overlap at least 1/8. If the array has maximal cardinality and

    η = min_(p≠q) (1-H_pq),

then necessarily `0<η≤7/8`. The upper endpoint is a bound, not a claim of attainability.

The rank proof gives the same bound but additionally exposes the operator subspace: from (2), `tr(C²)≥(tr C)²/72=225/2`, and `tr(H²)=100+tr(C²)` because C1=0. The next section identifies the equality matrix exactly.

## 3. The necessary PSD/incidence relaxation is feasible for EVERY B

Let P₀=J/100. For each of the three parallel classes c define

    E_c = (1/10) sum_(L∈c) l_L l_Lᵀ.

Each E_c is the orthogonal projector onto that class's line-indicator space. For c≠d, `E_c E_d=P₀`, because every two lines intersect once. Hence

    R = I - E_row - E_col - E_symbol + 2P₀              (5)

is the orthogonal projector onto S⊥, of rank 72. Its entries are

    R_pp = 18/25,
    R_pq = -2/25       if p⊥_B q,
    R_pq = 1/50        if p~q.

For example the diagonal is `1-3/10+2/100=18/25`; a required-edge entry is `-1/10+2/100=-2/25`; a line-disjoint entry is `2/100=1/50`. No coordinates of the q_p have been used.

Define

    C₀=(5/4)R,           H₀=C₀+J/10.                    (6)

Then H₀ has the explicit entries

    H₀_pp=1,
    H₀_pq=0             on required edges,
    H₀_pq=1/8           on line-disjoint pairs.

Its exact spectral decomposition is:

- eigenvalue 10 on span{1};
- eigenvalue 0 on the 27-dimensional line-contrast space;
- eigenvalue 5/4 on the 72-dimensional space S⊥.

Thus H₀ is positive semidefinite, entrywise nonnegative, has diagonal 1 and rank 73, satisfies **every** equation (1)–(3), has strict off-diagonal entries below 1, and attains the lower bound (4), for every Latin square B of order ten. C₀ has the forced kernel, trace 90 and rank 72.

This is an exact feasible object for the **relaxation**, not a 100-ray state array. Its PSD factorization gives abstract real vectors representing centered projectors' pairwise inner products; it does not make them Hermitian rank-one matrices in C^10. Similarly, an entrywise square-root matrix is not automatically a valid complex Gram matrix. The missing lift is the science, not a rounding detail.

### Barrier conclusion

No contradiction can follow from only the following conditions: H⪰0, C=H-J/10⪰0, diagonal 1, all required edge zeros, all line-sum equations, the rank≤73/72 constraints, strict H_pq<1 for p≠q, and the fourth-moment lower bound (4). Their intersection contains the exact H₀ for every B.

Therefore repeating a PSD feasibility check at this level, or interpreting rank≤73 as near a no-go, cannot decide the target. The frozen redirect condition in `selection-v1.md` is triggered **for this relaxation route only**. The unrestricted Gram/rank-one certificate protocol in the companion is not discarded.

Equality in the rank proof additionally forces C=C₀: a PSD matrix supported on the 72-dimensional S⊥ with trace 90 has `tr(C²)=225/2` only if all 72 eigenvalues are 5/4. This agrees with the elementary entrywise equality characterization in (4).

## 4. Bounded analytic attack on the equality lift

This section does not impose the equality case on the target. It describes exactly what lifting the barrier point H₀ would require, and proves a scoped real obstruction. A nonuniform complex witness is entirely unaffected.

Write N for the adjacency matrix of the line-disjoint relation ~. An equality lift has a Hermitian matrix S with

    S_pp=0,
    S_pq=0             on required edges,
    |S_pq|=1           when p~q,
    G=I+S/sqrt(8).

The ordinary Gram equation `G²=10G` is equivalent, by direct expansion, to

    S² = 72I + 16 sqrt(2) S.                              (7)

**Proof.** Expanding gives `I+2S/sqrt8+S²/8=10I+10S/sqrt8`; multiply by eight and rearrange. The coefficient is `8*sqrt8=16sqrt2`. Conversely (7) gives G²=10G. Hermiticity, diagonal 1 and the edge conditions then imply positive semidefinite rank ten by Theorem G in the companion. Unit moduli give H₀. Thus (7) with the displayed support/modulus constraints is an exact necessary-and-sufficient complex phase-lift system for H₀.

For completeness its individual off-diagonal equations have fixed combinatorial sizes, for every B:

- if p⊥_B q, there are exactly 56 cells r line-disjoint from both; equation `(S²)_pq=0` is a sum of 56 unit complex terms equal to zero;
- if p~q, there are exactly 50 such r; equation `(S²)_pq=16sqrt2 S_pq` is a sum of 50 unit complex terms.

**Counting proof.** The required-edge graph has degree 27. Two adjacent cells have ten common required neighbors: the other eight on their common line, plus two intersections of the remaining coordinate classes. Two nonadjacent cells have six common required neighbors, from the six ordered choices of distinct coordinate classes (row/column/symbol). Distinctness of these intersections follows because no distinct cells agree in two coordinate classes. For an adjacent pair, 98 other cells minus the union of their other required neighbors gives `98-(26+26-10)=56`. For a nonadjacent pair it gives `98-(27+27-6)=50`. QED.

### Corollary R (scoped real no-lift)

There is **no real-vector lift** of H₀, even after a common unitary and independent ray phases.

**Proof.** Such a real realization would give a real G in the above normalization, hence S_pq∈{−1,+1} on every line-disjoint pair. For any one of those pairs, `(S²)_pq` is an integer (a sum of 50 signs), while the right side of (7) is `±16sqrt2`, an irrational number. Contradiction. A common unitary does not change G, and choosing real representatives after arbitrary ray phases yields exactly such a real Gram matrix. QED.

An independent dimension argument corroborates the scope without being a numerical check: real rank-one projectors lie in Sym(10,R), and their centered versions in its 54-dimensional traceless subspace. Therefore for any real realization `rank C≤54`, whereas H₀ has rank C₀=72. More generally a real 30-basis array satisfies `tr(H²)≥100+90²/54=250`, strictly above 425/2. This is only the real subclass, not an obstruction to arbitrary complex q.

For complex phases, neither the 56-term zero sums nor the 50-term equations above are contradicted by the triangle inequality. No existence or nonexistence of their complete simultaneous solution is established. Replacing phases by signs would silently shrink the problem; that is expressly not done.

## 5. Result, imports and verification boundary

Delivered actual written conclusions:

1. A resolution-independent 28-dimensional kernel and operator-span bounds, with an exact proof for all B and all complex arrays.
2. An exact fourth-moment defect identity and its fully characterized equality matrix.
3. An explicit feasible relaxation point for every B, proving that these first-level invariants alone have no exclusion headroom.
4. A complete phase-lift system for that equality point, and a real-subclass no-lift proof. The unrestricted target and complex equality lift remain unresolved.

Items 1–3 are elementary consequences of the source predicates and standard frame/linear algebra; no priority is claimed. Nechita–Pillet's [SudoQ §2](https://www.rintonpress.com/xxqic21/qic-21-910/0781-0799.pdf) already formulates general constraint lists as rank-one projectors with line sums equal to identity. The source target is Zhang–Cao [2608.29201v2](https://arxiv.org/html/2608.29201v2), Definition 1.1/Lemma 2.2. No E1/F-family/WH5C2 theorem, parity import or old numerical output is a premise here.

This complete candidate requires actual separate in-harness reconstruction and parent review at pinned bytes. It has no kernel/formal/human/novelty acceptance. No checker or control was executed. The right next mathematical obligation is a complex rank-one/phase lift or a genuinely stronger all-object invariant—not a larger run of the already feasible relaxation.
