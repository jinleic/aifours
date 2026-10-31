# Definition-first common selection X: Hamilton cycle parity couples affine classes; exact dual certificates for safe cuts

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:25:04 PDT 2026**.

**NEW author-WRITTEN, unreviewed conditional completion result.** It adds a genuinely global cycle-sign equation to the two-row D2 affine system and identifies the precise cut-safety certificate after that higher-order coupling. It does not assume that pairwise affine classes stay independent once the new equation is imposed. No original row input, original witness or universal obstruction is supplied.

## 0. Inputs and setting

Only the current S1/S2 literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c` (complete LF1-37), controls/pre-body ACK, and elementary binary linear algebra/permutation signs are inputs.

Own input-clean proofs used:
- v8 `prerequisite-two-row-completion-v8.md`, SHA256 `a7414abf523c8d76c26dca66fae4cf25ba255dbe58245167090010fc9ecb1bcb`;
- v9 `prerequisite-affine-hamilton-cuts-v9.md`, SHA256 `141812a7a8eeebc90c3da035ae1d9b9f3612898d843fa861209ae6e528f55324`.

They concern ANY actual n−2-row partial system whose separate starts/ends are distinct. Its sentinel residual is a directed graph D on N=n+1 vertices with all indegrees/outdegrees2. Its bipartite representation has c cycle components of lengths2l_j, with Σl_j=N. Reference alternating arc colours τ and component variables x_j determine two cycle covers P(x),Q(x). The original distance2 restrictions give v8's exact D2-XOR equations; mandatory two-arc Hamilton cuts may also be added as in v9.

No old turn/Latin/sign/support theorem, stopped method/source, held/ZERO/review body or private type8 guide is input. Prior exposures persist; the Olson packet is review-only. No scientific execution, calculator/Eval/CAS, selected numeric/control/boundary probe, row/cut enumeration, solver, modelCLI or GO.

## 1. Individual Hamilton parity is an extra affine equation

Let P0=P(0) be the reference colour0 matching permutation. Define b∈{0,1} by

`(-1)^b = (-1)^(N−1) sgn(P0)`.

### Lemma 1

`sgn(P(x)) = sgn(P0) (-1)^(Σ_j (l_j−1)x_j)`.

Thus P(x) being a Hamilton cycle requires

`Σ_(j:l_j even) x_j = b` over F2.                                (HP1)

Both P(x),Q(x) can have Hamilton parity only if the number e of even l_j is even; when e is even the SAME equation (HP1) enforces the necessary sign for both covers.

**Proof.** Switching one component replaces one alternating matching by the other. Following one and reversing the other gives a single l_j-cycle on its left vertices, so the sign changes by (-1)^(l_j−1). Different components involve disjoint vertex sets, and their factors multiply, giving the formula. A Hamilton cycle has sign (-1)^(N−1), yielding HP1.

Q(x)=P(x xor1) as a matching choice; its sign differs by `(-1)^(Σ_j(l_j−1))=(-1)^e`. Hence if e is odd the two signs are opposite and cannot both equal the Hamilton sign. If e is even, enforcing HP1 pays the sign requirement for both. Also `Σ(l_j−1)=N−c`, so this includes v8's parity obstruction exactly. ∎

This is still only a NECESSARY cycle-sign equation. It is not a claim that a correctly signed cycle cover is Hamilton.

## 2. Exact interaction with D2 parity closure

Suppose the pairwise D2/two-arc-cut system is consistent. As in v9, write `x_j=y_(C(j)) xor d_j`, with one free bit per constraint class.

Let A be the set of classes containing an ODD number of even-l_j components, and put

`b' = b xor Σ_(j:l_j even) d_j`.

Then HP1 becomes exactly

`Σ_(C∈A) y_C = b'`.                                             (HP2)

Consequences, all without a chosen state:
- If A is empty and b'=1, no original two-row completion is possible, even if all D2-XOR equations are consistent.
- If A is empty and b'=0, this particular sign condition is automatic.
- Otherwise it is a new global affine relation among the indicated free class bits. It is not replaced by fictitious independent choices for those classes.

When the relation has two class variables it is a new pairwise parity edge and may merge classes. In general it is higher-arity. The all-solutions cut criterion of v9 was explicitly for a PAIRWISE-XOR system with independent class flips; it must not be used unchanged after an arbitrary higher-arity HP2 relation. The next section gives the correct general criterion.

## 3. Exact cut-safety dual for the full affine system

Collect D2-XOR, mandatory two-arc cut equations and HP1 into one affine system

`M x = q` over F2.                                               (AFF)

If it is inconsistent, the original completion is impossible. Assume it is consistent. No Gaussian elimination or state enumeration is performed; the following is an elementary theorem about every such system.

For a nonempty proper A⊂X∪{∞}, let its outgoing residual arcs be e. Each χ(e)=τ(e) xor x_(j(e)). Fix one outgoing arc e0 if the cut is nonempty. The condition that the cut is MONOCHROMATIC is precisely

`χ(e) xor χ(e0)=0` for all other outgoing e,

which is another linear system `L_A x=t_A`. It does not require deciding whether that common colour is0 or1. For an empty outgoing cut, the monochromatic obstruction is automatic.

### Theorem 2 — exact universal Hamilton-cut certificate

Every solution of (AFF) puts BOTH colours on a given nonempty cut iff the augmented system

`M x=q`, `L_A x=t_A`

is inconsistent. Equivalently there exist coefficient row vectors u,v over F2 such that

`u M + v L_A = 0`, but `u q + v t_A = 1`.                        (DUAL)

**Proof.** A solution of the augmented system is exactly an affine-feasible colouring with that cut monochromatic. Its absence is exactly the claimed universal cut safety.

Any certificate DUAL makes a solution impossible by taking that linear combination of its equations. Conversely, if the augmented right side lies outside the image of its linear map, choose a basis of the image, extend it by that right side and then to a full basis. Define a linear functional that vanishes on the image basis and is1 on that right side. It annihilates all coefficient columns but not the right side, producing u,v. This is elementary finite-dimensional linear algebra, not an executed solver. ∎

Thus universal safe-cut certificates need not be just a forced-opposite pair of arcs after HP2 couples several classes: a combination of several parity equations can certify that a monochromatic cut is impossible. Conversely the existence of ONE monochromatic affine-feasible colouring does NOT show that every colouring fails Hamiltonicity.

## 4. Full original realization and obstruction callers

**Robust positive caller.** If (AFF) is consistent and for EVERY nonempty proper vertex subset A the cut is nonempty and has a DUAL certificate, then EVERY solution of (AFF) supplies two Hamilton cycles. Deleting the sentinel gives the exact two original rows, with all D2 restrictions paid by the same affine vector. Together with the fixed n−2 rows this is an original array.

**Proof.** Theorem2 makes every cut bichromatic for each solution. A permutation cycle cover with an outgoing edge of each colour from every proper subset has one cycle in each colour. The v8 forward/converse then checks all original row, adjacency and internal-distance2 conditions without wraparound. ∎

**Negative callers.** Inconsistency of AFF (including the HP2 contradiction of §2), a zero outgoing cut, or a cut forced monochromatic in every affine solution excludes a completion. A DUAL certificate for cut safety is a POSITIVE ingredient for realizing rows, not a nonexistence certificate for the original array; the direction must not be reversed.

**Remaining non-robust case.** If some cuts have no universal safety certificate, the original problem may still have a solution: one common vector could satisfy ALL not-all-equal cut clauses even though other affine vectors fail individual cuts. No implication from per-cut existence to simultaneous existence is asserted. The exact general caller remains one vector satisfying both affine constraints and every HCUT.

## 5. Original scope and next gap

The result applies to every permissible n−2-row partial system; at original order11 that means every nine-row deletion of a hypothetical full array. No particular partial system, cut, sign or numeric coefficient was selected or evaluated. It sharpens the missing common-selection premise without assuming a maximal-overlap triangle or a special support class.

No admissible nine-row input meeting the positive caller is supplied, and no argument forces a negative caller for every possible input. Original Tuscan-2(11) remains OPEN. No construction, universal no-go, support promotion, book/current-openness or novelty certification is inferred.

**Next genuine mathematical obligation:** find an all-variable reason for one common affine/cut solution (or unavoidable contradictory cut), not independent favourable choices for cuts, cycle signs or D2 paths. The global row selection/purity gap from v6/v7 remains a separate upstream obligation. These conditional criteria are not silently substituted for its solution.

All exposure/STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. Author-written, unreviewed, no Main adoption or stronger verification gate. Full-window standing direction and original deadline unchanged.
