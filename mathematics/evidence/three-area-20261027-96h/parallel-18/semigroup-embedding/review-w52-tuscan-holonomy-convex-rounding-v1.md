# Review w52 — Tuscan holonomy, whole-row convex obstruction and high-purity rounding

**Reviewer:** MathSemigroup-2, math-4. **Author:** InfoRecursiveMDS18-2, info-4.

Actual first wake: **Tue Oct 27 16:17:37 PDT 2026**. Actual pre-body ACK observation: **16:18:01**. Actual native observation immediately before writing this review: **Tue Oct 27 16:22:46 PDT 2026**.

## 1. Verdict and counts

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** for each of the three full candidate bodies S6/v5, S7/v6 and S8/v7.

| Candidate | FATAL | MAJOR | MINOR | Exact result supported by this written reconstruction |
|---|---:|---:|---:|---|
| S6 / multirow holonomy v5 | 0 | 0 | 0 | Weighted defect inequality and its redundancy at order11; all stated maximal-overlap block signs; triangle/cycle sign necessity, not forced existence of such a configuration. |
| S7 / convex obstruction v6 | 0 | 0 | 0 | Whole-row integer equivalence, universal fractional feasible point and weighted PSD/cut identities; obstruction to infeasibility of this relaxation, not refutation of existential integral realizability. |
| S8 / high-purity rounding v7 | 0 | 0 | 0 | Heavy-row compatibility, strict and closed purity threshold, exact unit-row boundary completion, original actual-row extraction and the stated existence equivalences. No high-purity point is supplied. |
| **Total** | **0** | **0** | **0** | Original T2(11) remains OPEN. |

The convex point does not satisfy an original **integer** missing-graph realization, and the source explicitly distinguishes this. The high-purity theorem selects a new actual heavy-row array; it does not assert that arbitrary fractional input weights become integral. These distinctions are essential to the verdict.

## 2. Mandatory order, exposure and actual coverage

S0 and the complete manifest (`e2b40390782c44b45cb18d33c06d01a81c9f7788639f66b4cc44561ac1c42db7`) were read first. Before any packet body or mathematical reasoning I wrote the specified pre-body ACK, SHA `e13412a39671909d4a18a81c8ced7c9b91a18c12bc76e3db47fe328bef287994`.

I then read **every line and ending** of the frozen **859-LF / 80999-byte** packet, SHA `ac8090e533e799b1e3b064a4daf62b6fd767cff7fcc9dc1773fcffa41ea76ea2`, in raw windows1–60,61–120,121–180,181–240,241–300,301–360,361–420,421–480,481–540,541–600,601–660,661–720,721–780,781–840,841–859. No long-line omission was left unresolved.

| Label / role | Complete source LF | SHA-256 |
|---|---:|---|
| S1, literal definitions | 37 | `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c` |
| S2, v1 dependency | 146 | `5c7e2c40f979b41c30608da7d75de7039ae458bfce949a50bc259f3d7a6b0b76` |
| S3, v3 dependency | 95 | `0cbe329eaf589fe0a4aa8ed7465355676c7eed37c616e45ad741776b9b51279a` |
| S4, v4 dependency | 84 | `94ec05b2ac521136ac08c633513afe5ee9143f957669d2767b15c346f5b5036c` |
| S5, v2 dependency | 144 | `8dec8f35e53114009c9e2f10f2e37f54ec078af002133e6779d324fa3f2c1b97` |
| S6, candidate v5 | 96 | `2f181fe57febc7fd9854cb7ac148e0e42740392e7883b3a2a55761858ab7bc03` |
| S7, candidate v6 | 129 | `91167935f66f07302d365fb8b3b971e2a1b1637f4c3abb957228b5b319ccf7f3` |
| S8, candidate v7 | 96 | `fe8d68e5363663e1ac4d83eb8740b0562d3ca220086cd191006367402c1dac00` |

This is **serial continuation** of my w1 Tuscan review, not blind work. Prior v106-related exposure/findings also survive. The earlier favorable verdict is not transferred: the actual dependency steps used here are reconstructed below from this packet. My own semigroup method STOP, QOA source-display MINOR, and all inherited findings remain; they supply no Tuscan premise.

No selected row, small case, numerical/group/graph/state/frequency instance or sanity probe was constructed or checked. Every case below is quantified in the original variables or is the source's literal original-order specialization. No mathematical interpreter, calculator/Eval/CAS, permutation generation/enumeration, solver, replay, test, model CLI, nested task, author contact, external source or old/held proof was used. Only the required ACK and this review were written.

**Service disclosure:** the ACK records previous substantive prewrite15:48:02 to this first wake16:17:37 as29m35, and to ACK observation16:18:01 as29m59; the earlier source return pin was15:50:04. No intervening substantive file/live checkpoint existed. The20-minute target was exceeded; no exact file-save/turn-end, fabricated heartbeat, continuous service or cadence-pass claim is inferred from those observation bounds.

## 3. Original caller and used dependency reconstruction

The literal target is S1:31–33: n actual linear permutation rows on n common symbols, each distinct directed pair exactly once at distance1 and at most once at distance2. The two distances are separate. No wraparound, Latin columns, support stratum, row symmetry or missing-graph regularity is imposed. The original order is11.

### 3.1 v1 actual-row holonomy and event caller (S2:24–98)

For actual rows a_r and their inverse position maps p_r, F_rs=p_s a_r. A repeated directed distance-d event is exactly F_rs(i+d)=F_rs(i)+d; the images lying in the position set automatically pay the second row's endpoint guard. Within-row repetition at one fixed distance is impossible. Noncollision of n(n-1) adjacent events therefore gives exact coverage by counting, not an additional Latin assumption.

F_st F_rs=p_t a_s p_s a_r=p_t a_r=F_rt, with F_rr=id and reciprocity. Thus every ordered cycle has identity product. Conversely choose an anchor o and common symbol labelling lambda; a_r=lambda F_or^-1 realizes every F_rs simultaneously by the triangle law. This is the actual-object equivalence, not a construction of such an admissible system. It pays the holonomy caller used by S6.

### 3.2 Endpoint uniqueness and maximal-overlap block structure (S3:25–53; S4:53–69)

Each symbol has n occurrences and n-1 outgoing adjacencies, hence is last once; the incoming count makes it first once. These are global array statements.

D2(s) consists of two directed parity paths O and E in the arbitrary named order s=(x1,...,x_n). If one other row contained all n-2 of those edges as adjacencies, both paths would be contiguous blocks. At odd order O contains both endpoints of s, so either O E repeats its start or E O repeats its end. Thus C_rs<=n-3.

If C_rs=n-3, exactly one of D2(s)'s edges is absent. Removing it splits the two parity paths into exactly three nonempty blocks; retained adjacency edges force every block contiguous in r. If the cut is in E, global endpoint ownership forces O into the middle, leaving exactly E1 O E2 or E2 O E1. If the cut is in O, O1 cannot be first and O2 cannot be last, leaving O2 E O1, O2 O1 E or E O2 O1. This is the whole block-order input needed by S6.

No stronger converse or source array existence is imported from these cases. S3's separate pair-sharpness construction and S4's additional numerical reciprocal capacities are not load-bearing premises of the candidate sign proof and are not promoted by this review merely because their files were read.

### 3.3 Common-middle identity and its exact graph/cut boundaries (S5)

For each actual consecutive triple (a,b,c),

2(f(a)-f(b))(f(c)-f(b))=(f(a)-f(b))²+(f(b)-f(c))²-(f(a)-f(c))².

Summing, an interior adjacency occurs in two triples, each boundary edge in one, and each distance2 event in one. Thus2Q=2E1-EB-E2. Exact adjacent coverage and distance2 noncollision give E2=E1-EM, hence2Q=EI+EM (S5:44–67). The missing graph is not assumed regular.

For the claimed original strictness, the interior undirected multigraph is connected at n>=5: a cut with both sides of size at least2 would need at least4(n-2)>2n directed boundary events if no interior event crossed it. For a singleton, all2(n-1) adjacency incidences would have to be boundary, but the unique first/last occurrences give2 incidences and second/penultimate positions give at most n more; n+2<2(n-1) at n>=5. Both are contradictions. This is a universal cut proof, not a selected graph or subset.

Writing G=I plus M with directed events retained as undirected multiplicities gives Q=(1/2)f^T L_G f. Each symbol is the middle in n-2 triples, so Q's diagonal is n-2 and G's degree is2(n-2); multiplicity on {x,y} is2-b_xy+m_xy. For an arbitrary set A, the common-middle product on its indicator counts exactly alternating-middle triples. Hence2Alt(A)+Bcut(A)=2|A|(n-|A|)+Mcut(A), simultaneously for all A. This pays the used graph/PSD/cut claims without assuming graph sufficiency.

The weighted version in S7 needs only the per-row identity and linearity, which are also reconstructed directly in §5 below. It does **not** inherit integrality of G, M or event occurrences.

## 4. Candidate S6/v5: every claim reconstructed

### 4.1 Weighted defect inequality and exact redundancy (S6:19–37)

Take an arbitrary adjacent event of r. If not a D2(s) event, it is charged to one of a=n-1-C_rs bad r-edges. Otherwise it corresponds to a unique actual two-step s-path. If either of its edges is not D2(t), charge that edge: each bad s-edge lies in at most two such paths, so at most2b events are accounted for.

When both s-edges are good, their common middle is the same actual symbol in t; the t-positions increase successively by2, yielding a four-step t-path. A bad t-edge occurs in at most four such paths, giving at most4c events. If all four were D2(r), their actual r-positions would advance by8, contradicting that the original event advances by1. The endpoints of distinct r-events determine distinct paths, so these incidence bounds do not hide a many-to-one charge.

Every r-edge is charged, giving n-1<=a+2b+4c, equivalently C_rs+2C_st+4C_tr<=6(n-1). Linear endpoints only decrease the incidence caps; no wrapping path is added.

At the original order, the individual bound C<=8 makes the entire weighted left side at most(1+2+4)8=56<60. Thus the scalar inequality and its rotations genuinely exclude no triple already satisfying that one-entry bound. This is a universal upper-bound comparison for all permitted values, not evaluation of a chosen transport triple. No stronger consequence is asserted.

### 4.2 Full block-sign classification (S6:41–66)

Let n=2m+1 with m odd in the claimed range. The sign of F_rs is the inversion sign of the list of source indices appearing in r. For base O E the odd element at index2j+1 has j smaller even-block elements placed after it, giving epsilon=(-1)^(m(m+1)/2).

Apply the complete block classification from §3.2. Swapping blocks of lengths u,v contributes(-1)^(uv):

- **Cut in E:** E1 length k, E2 length m-k. E1 O E2 has relative exponent k(m+1), even. E2 O E1 has exponent(m-k)(m+1+k), with parity(1-k)k=0. Both signs are epsilon.
- **Cut in O, separated:** O2 E O1 moves the k-prefix O1 past n-k positions; k(n-k) is even because n is odd. Sign is epsilon.
- **Cut in O, adjacent:** O2 O1 E has exponent k(m+1-k), congruent to k modulo2. Moving E across the entire odd block contributes m(m+1), even, so E O2 O1 has the same sign epsilon(-1)^k.

Thus the exceptional indicator e_rs is exactly the stated odd-prefix adjacent-cut case. All cut lengths, nonempty blocks and source orders are covered algebraically. Additional same-distance restrictions may delete cases; none can change their computed signs. No case is asserted to extend to a full array.

### 4.3 Triangles and all cycles (S6:72–94)

On a directed maximal-overlap triangle, actual permutation holonomy gives sign product+1. The classification gives epsilon³(-1)^(sum e), hence(-1)^(sum e)=epsilon. The source's original-order odd-exception conclusion follows from its stated epsilon specialization. Maximal self-overlap cannot create an overlooked loop in this range because C_rr=0.

On a directed cycle of length ell, telescoping the actual relative permutations gives identity, hence(-1)^(sum e)=epsilon^ell. Equivalently sgn(F_rs)=sigma_s^-1 sigma_r for the actual row permutation signs. This is only necessary. The source neither forces a maximal-overlap triangle in every array nor promotes sign consistency alone to row realization. Low-overlap transport remains outside this conditional exclusion.

## 5. Candidate S7/v6: whole-row relaxation and exact obstruction

### 5.1 IP is exactly the original object (S7:17–33)

Omega is the complete mathematical set of permutation rows. Integer nonnegative z with total n is exactly a list of n actual rows with their multiplicities. The adjacency equations and distance2 caps are the literal source requirements. Conversely any original array gives those weights. Every row has an adjacency, so z_pi<=1 follows from its nonnegative adjacency equation; repeated row types cannot remain hidden. The statement is up to permutation of row identities, not reordering symbols inside a row.

### 5.2 Barycentre, all event totals and boundaries (S7:39–79)

There are n! rows as a finite counting fact, not an enumerated list. Weight z*_pi=1/(n-1)! gives total n.

For each arbitrary directed pair, an adjacent ordered block plus the other symbols has(n-1)! permutations, giving weighted total1. A distance2 event has n-2 legal starts; after fixing its endpoint labels the remaining positions have(n-2)! fillings. Its total is(n-2)/(n-1)<1, with deficit1/(n-1). This is one uniform weight system satisfying every pair constraint simultaneously.

Each fixed directed first edge has(n-2)! completions, as does a last edge, so B*=2/(n-1). They are distinct positions for n>=3, and one directed pair cannot occupy both in a permutation. Therefore I*=(n-3)/(n-1) and M*=1/(n-1). These are fractional usages/deficits, not original sets or degree-regular missing graphs. All z*_pi are strictly between0 and1 in the stated range, so this same vector is not an integer occurrence vector.

### 5.3 Weighted common-middle matrix and cuts (S7:81–101)

The elementary triple identity is valid on every row and thus under these weights. Using E1 exact coverage and E2 weighted deficits gives

2Q*(f)=sum_(x!=y)(I*+M*)(f(x)-f(y))²
      =((n-2)/(n-1)) sum_(x!=y)(f(x)-f(y))².

For arbitrary f, expanding the full ordered-pair sum gives2n sum_x(f(x)-fbar)². Therefore

Q*(f)=n(n-2)/(n-1) sum_x(f(x)-fbar)²,

with matrix((n-2)/(n-1))(nI-J). Its diagonal is n-2, row sums0, off-diagonals nonpositive and kernel exactly the constants. The arbitrary indicator substitution in the same identity gives every weighted cut equality simultaneously. This is an algebraic identity for all f/A, not a selected test vector or cut.

It does **not** satisfy the discrete integer graph model as such, and the source explicitly says so. The result is feasibility after adding the stated PSD/cut identities in their weighted relaxed interpretation. No integrality-valid cut or other stronger semidefinite condition is asserted satisfied.

### 5.4 Exact failed implication, not an original no-go (S7:103–127)

The same fractional point cannot be an occurrence vector of n whole rows. Its distance2 data are also fractional rather than integer occurrence counts. Thus promoting **that same** relaxed solution/data to an actual occurrence-level array is unjustified.

Since an analytic feasible point exists for every n in scope, infeasibility of these particular relaxed constraints plus their stated PSD/cut consequences cannot prove original nonexistence. This does not refute `LP feasible => SOME integral feasible point` at the original order—that existential implication remains exactly an unsolved problem. Nor does it refute every convex/moment/integer-cut approach. These distinctions are correctly explicit in the candidate.

## 6. Candidate S8/v7: full closed-threshold rounding

### 6.1 Caps and compatibility (S8:19–35)

Each nonnegative z_pi<=1 follows from any adjacent event of that actual row. If two weights exceed1/2 and their rows share a same-distance1 or2 event, their two terms already exceed its cap1. Thus distinct heavy rows are compatible at each distance. Their disjoint adjacency sets each contain n-1 directed pairs, out of n(n-1), so h=|H|<=n.

No compatibility of all positive weights is assumed. A weight exactly1/2 is not included in H and does not receive this strict argument.

### 6.2 Strict threshold (S8:39–51)

For H use z²<=z; outside H use z²<=z/2. Since total mass is n,

P<=sum_H z+(1/2)sum_notH z=n/2+(1/2)sum_H z<=(n+h)/2.

If h<=n-1 then P<=n-1/2. Hence P>n-1/2 forces h=n. Those n heavy rows themselves are actual permutations, have disjoint adjacency/distance2 events, and their adjacency count exhausts every directed pair. They form the original array. Their fractional weights need not be replaced by claims of integrality; the output is their actual set of rows.

### 6.3 Unit-row lemma and equality threshold (S8:57–75)

If n-1 rows have weight1, their disjoint adjacency sets cover(n-1)² pairs. Exactly n-1 pairs U remain. Every other positive row must avoid every already saturated adjacency; its n-1 adjacencies therefore equal U.

A directed Hamilton path is uniquely recovered from its full directed adjacency set: its start is the sole vertex without a predecessor, and successors determine the order. Thus there is at most one remaining row type. Total remaining mass1 forces it to have weight1. The distance2 caps also forbid it sharing any such event with a unit row. This proves the complete original-object unit-row lemma, not just adjacency completion.

Now let P=n-1/2 and suppose h<=n-1. The entire bound chain in §6.2 must be equality, giving h=n-1 and sum_H z=h, hence every heavy weight1. The unit-row lemma forces an indicator of n compatible rows, with purity n, a contradiction. Therefore h=n even at equality, and the same row-extraction argument applies.

This handles the boundary without declaring two half-weight rows compatible or silently using a generic scalar rounding theorem. All cases are symbolic in the actual variables.

### 6.4 Forward/converse and remaining optimization premise (S8:79–94)

An original array has indicator weights and purity n. Conversely any feasible point of purity at least n-1/2 yields the actual heavy-row array just proved. Also P<=sum z=n, and equality forces every z to be0 or1, so the source's purity-n/indicator wording is paid.

At the original order the three existence assertions listed in S8:83–86 are equivalent. No feasible point reaching the threshold is produced, and no upper bound excludes all such points. The uniform fractional point proves feasibility only, not this purity premise. The threshold is sufficient and is not claimed optimal. Thus the new conditional realization bridge is valid while original existence/nonexistence remains open.

## 7. Dependency, quantifier and assurance register

- **No load-bearing NR mathematical premise** was needed for the three candidate verdicts: actual-row collision/cocycle/count arguments, global endpoint ownership, maximal-overlap blocks, the common-middle identity and its relevant graph/cut statements were reconstructed from the supplied packet.
- Dependency files were not treated as globally adopted merely because supplied. In particular unused sharpness/other reciprocity consequences are not exported as review results here.
- All elementary imports were used explicitly: permutation inversion/composition/sign inversion counts, finite path incidence counting, nonnegative inequalities, and quadratic-form/multigraph identities. No old Latin sign, completed-turn, graph-splitting or support theorem was assumed.
- Boundary conditions remain those in the statements: v5 sign formulas require odd m in the stated odd-order range; actual endpoints and no wraparound are retained; v6/v7 quantify over all complete row types without generating them; half-weight is strictly excluded from the heavy set.
- The independent modern definition literal is supplied, not a new book-image, HTTP-byte, source-priority or current-openness certification.
- Scalar capacities, sign consistency, PSD/cuts and generic fractional feasibility are not sufficient original realization conditions. The high-purity theorem supplies its actual converse only when its additional premise holds.

All old/new process findings, own source-scope MINOR and method STOP, author exposure/STOP/HOLD/ZERO, N4 UNKNOWN with historical child exit unestablished and auxiliary214 STOP remain. There was no selected private sanity probe, scientific execution, extra source or author contact. This is same-harness WRITTEN review at the frozen scope only, not formal/kernel/human/configured-family/executable/independent-model or novelty acceptance. Main's own complete source/return reads and any later adoption are separate requirements.
