# v54-B — exact written reconstruction of the unadorned leaf-cycle operator

Reviewer MathShor-2, math-5. Observed clock before creation: **Sun Oct 25 08:13:27 PDT 2026** (`/bin/date`). Output exclusively in the assigned reviewer root.

## 1. Verdict and exact scope

**0 FATAL / 0 MAJOR / 1 MINOR.** The MINOR is an explicit finite-domain/zero-remainder convention needed in LC4 at the single-gap boundary; the balanced-gap proof supplies the immediate correction, detailed in Section10. With that convention, the exact bare-cycle table, placement attainment and stated construction bounds are WRITTEN-SUPPORTED by the full derivation below.

This verdict concerns v6 Section5 and its limitations ONLY: ONE UNADORNED leaf cycle, every ell>=3, every local budget, both portal flags and all original shortest-path ties. It does not accept the separately assigned portal-swap theorem, a decorated-cycle/general-cactus polynomial algorithm, a hardness conclusion, executable verification or novelty.

### Frozen sources and full coverage

- **S1:** `parent-evidence-erratum-v9.md`, SHA-256 `b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`, LF1–35, read FIRST and in full.
- **S2:** `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/replacement-information-primary-screen-v6-cactus-portal-swap-v1.md`, SHA-256 `9359694947945528ed5bf0b1bd60687468c63bbc8643abf67ccd0b162a7e2cf5`, LF1–387. Primary reconstructed scope LF249–358 and limitations LF364–369; the whole source was read for interfaces.
- **S3:** same author root, `replacement-information-primary-screen-v5-cactus-hardness-sketch-v1.md`, SHA-256 `5c961bb5115861285dec23a6519ad04e348e725657fd287e5d00f4a58d2459b8`, LF1–300, fully read again as the named portal/objective import.
- **S4:** `institute/runs/three-area-2026-10-23-96h/cactus-interface-ph7-new-cone-parent-v1.md`, SHA-256 `bac4507df174d8533de37e6315a203f77a1e0ac806d2d96e33a6b09bd65e13b6`, LF1–33, fully read; only its cactus interface boundary is relevant.

Single literal part `peer-review-wave-v54-v54-B-part1-v1.md`, SHA-256 `961a3f76f6bf093a9e6faacc3c20872688d54552c2f96b245aef0f64f9d8cda9`,65,469 bytes. ALL packet LF1–778 were read consecutively in displayed windows1–143,144–293,294–443,444–583,584–778. Every declared LF, including all endings and the contextual portal-swap body, was actually read.

Long primary proof passages were reread raw at packet LF299,303,311,318,319,324,326,331,332,333,336,342,345,346,349,356,357,360,363,366,370,374,376,379,381,384,387,392,393,394,397,400,401,404,406,414,415,417. The manifest's truncated v54-B scope LF127 was recovered raw. No unresolved load-bearing truncation remains.

Manifest SHA-256 `6ff977cddc325cf5baa06d73f62e8407a8e680c5a48813916dd12a73cf760981`; exact v54-B entry and full packet-byte-equality receipt read before ACK/body. Actual manifest/part/source hashes were observed and match the pins. Receipt equality did not substitute for source reading.

Exposure ACK BEFORE proof body: `peer-review-cactus-leaf-cycle-operator-ack-v1.json`, SHA-256 `da98562a670f4c9955b71dbe1df54fff5cbd93a89aae2f609cd6de810a192da3`. It discloses the prior v47-A reconstruction and the disjoint reviewer assignment. The actual preceding cactus review is pinned at `d8d8c6343dcdf27ca820506701f9f22a271db2c99507d8972c0eaf1615c32e3e`; its verdict does not automatically prove the new leaf-cycle theorem.

No scientific interpreter/eval/program/enumeration/symbolic computation/replay/solver, implementation/test run, nested agent or external CLI was used. This is written mathematical/algorithmic reconstruction, not an executed algorithm.

## 2. Objective and the exact one-portal contract

The target uses q from the ORIGINAL unweighted graph's shortest paths, including selected endpoints. For distinct vertices the contribution to GBC is1-q; undirected reversal gives

```text
GBC=n(n-1)-2*beta,
```

where beta is the unordered missed mass. Selecting vertices does not delete them, lengthen a shortest path or promote a surviving longer path to a new geodesic.

The imported portal state is(a,epsilon,alpha,beta), where a counts selected internal vertices excluding the portal and alpha sums avoidance to that portal over internal vertices. For a compatible outside rooted component K, shortest cross-side paths factor at the single shared articulation; beta_total=beta_H+beta_K+alpha_H*alpha_K. Thus fixed outside mass z contributes z*alpha_H. For equal a/epsilon/alpha, retaining only the smallest beta is exact for ALL z>=0. No new portal-swap theorem is needed for this fact.

The leaf cycle may have arbitrary outside cactus only at v. A purported internal geodesic leaving H through v must return to v and incur positive extra length, so outside attachments do not alter its original two-arc geometry. There are NO nontrivial child attachments at other cycle vertices. This is the essential restriction enabling length-only gap costs.

## 3. LC1 from original geodesics and exact LC2 gap cost

Assume first that at least one cycle vertex is selected. The remaining vertices split into cyclic gaps between consecutive selected separators; consecutive selected vertices create an empty gap. Endpoints in different gaps have a selected vertex on BOTH cycle arcs, so q=0. Endpoints in the same gap have a unique within-gap arc of length d; its complement contains the nonempty selected set and is blocked.

There are then exactly three original-distance cases:

- d<ell/2: the within-gap arc is the unique shortest path and avoids C, so q=1;
- d=ell/2 for even ell: BOTH equal arcs are shortest and exactly one avoids C, so q=1/2;
- d>ell/2: the shorter ORIGINAL arc is the blocked complement, so q=0, even though the longer gap arc remains unselected.

This proves LC1 without deleting selected vertices or dropping an antipodal tie. The case k=0 must be handled separately; otherwise the complement need not be blocked.

For a gap of r vertices there are exactly r-d unordered pairs at gap-distance d. For ell=2h+1 the surviving distances are1,...,min(r-1,h). For ell=2h they are1,...,min(r-1,h-1), with half of the max(r-h,0) antipodal pairs. Hence the stated LC2:

```text
f_ell(r)=sum_(d=1)^min(r-1,h0) (r-d)
```

plus `max(r-ell/2,0)/2` only in the even case, h0=floor((ell-1)/2). Empty sums give f(0)=f(1)=0. Its physical domain0<=r<=ell-1 is correct because k>=1. Summing gap costs gives the ENTIRE beta: selected-endpoint pairs and different-gap pairs contribute0, and all other pairs are accounted for exactly once.

## 4. LC3/LC4: discrete convexity, balanced attainment and zero-gap-count cases

Adding a new endpoint to a gap adds precisely one pair of every distance1,...,r. Thus, wherever both f(r),f(r+1) are in the domain,

```text
ell=2h+1: Delta f(r)=min(r,h);
ell=2h:   Delta f(r)=min(r,h-1)+(1/2)*1_(r>=h).
```

These are exactly the two even branches in LC3: r for0<=r<=h-1 and h-1/2 for r>=h. Both sequences are nondecreasing. The use in the proof needs only0<=r<=ell-2.

If p>=q+2, move one unselected vertex from a length-p residual gap to a length-q gap. The cost change is Delta f(q)-Delta f(p-1)<=0. The total remains s and all lengths stay in the physical domain. Repetition terminates, for example because the sum of squared lengths strictly decreases, at gaps differing by at most1.

For j>=1 let q=floor(s/j) and rho=s-jq. A balanced allocation has j-rho gaps of length q and rho of length q+1. Its exact minimum is

```text
D_j(s)=(j-rho)f(q)+rho f(q+1),
```

with the zero-multiplicity convention in Section10. The proof establishes that this balanced allocation attains a minimum, not a unique placement or enumeration of all minimizers. Permutations/rotations can give multiple actual selections even when the length multiset is fixed. No unsupported claim about all equality cases on a linear plateau is needed.

For j=0, there is one empty allocation at s0 with cost0 and no allocation at s>0, hence D_0(0)=0 and D_0(s>0)=infinity. It is essential not to divide by j in this case. All LC7 calls have0<=s<=ell-1, so the lemma's total-range hypothesis is retained.

## 5. LC5/LC6: portal mass and the even antipode

If v is selected, alpha=0 by the endpoint convention. If it is unselected, let its gap have length r and let t be the number of its vertices on one side of v, so the other side has r-1-t. A vertex at distance d on either side contributes precisely the LC1 weight, with no contribution from other gaps or selected vertices. Therefore the one-sided sum is

```text
A_ell(u)=min(u,h0)
```

plus `(1/2)*1_(u>=ell/2)` for even ell, and alpha=A_ell(t)+A_ell(r-1-t). This excludes v itself exactly as required by the original state.

A possible even-cycle antipode is counted with weight1/2, never1. It cannot appear on BOTH sides of a feasible portal gap: that would require t and r-1-t both at least ell/2, hence r>=ell+1, contradicting r<=ell-1. Thus the sum has no hidden duplicate antipodal vertex.

These formulas include r1, giving alpha0, and arbitrarily long feasible gaps beyond the half-cycle, whose far vertices correctly contribute0 rather than being assigned a recomputed unselected-path distance.

## 6. Complete LC7/LC8/LC9 table with actual placement attainment

### Portal unselected:1<=k<=ell-1

Any actual selection has exactly k cyclic gaps. The designated portal gap has r>=1 and offset0<=t<r. Its length is at most ell-k, and its other k-1 gaps total s=ell-k-r. The exact cost is at least f(r)+D_(k-1)(s), with alpha fixed by LC6. This gives the lower-bound direction of LC7.

Conversely choose a candidate r,t with FINITE D_(k-1)(s), and choose the balanced residual lengths from LC4. Place the k selected separators around the cycle with those gaps. Concretely, put the separator immediately preceding the designated gap at clockwise position v-(t+1), then place its r unselected vertices followed by the next separator, and continue with the residual gaps. The total number of positions is k+(r+s)=ell, so it closes consistently. Empty residual gaps simply make selected vertices adjacent. The portal occupies its specified unselected offset. This realizes exactly the candidate beta and alpha in the ORIGINAL graph.

For k1 the residual gap count is0, so only s0 is finite, forcing r=ell-1. The preceding/next selected separator is the SAME one vertex after wrapping, not two charged copies. Thus LC7 inserts no fictitious abstract state. Taking the minimum over its actual candidates is exact for every alpha; empty candidate sets have value infinity.

### Portal selected:1<=k<=ell

There are k gaps totaling ell-k, and v can be fixed as one selected separator. The same balanced placement realizes cost D_k(ell-k). Alpha is0 because its endpoint is selected. Every alpha!=0 is impossible. This proves LC8 including k1 and kell, with no change to the vertex budget.

### Boundary and impossible rows

- k0,epsilon0: no selected vertex, so ALL original shortest paths avoid C. Thus alpha=ell-1 and beta=ell(ell-1)/2. Every other alpha is impossible.
- k0,epsilon1: impossible.
- kell,epsilon0: impossible.
- kell,epsilon1: all vertices selected, alpha=beta=0, exactly D_ell(0).
- k=ell-1,epsilon0: v is the only unselected vertex, so LC7 permits r1 and gives alpha=beta=0, correctly retaining the unselected portal flag.

The old internal budget is exactly a=k-epsilon. Thus epsilon0 uses k=a, and epsilon1 uses k=a+1, charging the shared portal once rather than once per local representation.

### Complete profile

Every alpha is a half-integer between0 and ell-1; there are at most2ell-1 grid values, not a claim that all are attainable. For each fixed a/epsilon/alpha, a larger beta can never help against any nonnegative outside mass. Hence the entire exact leaf profile is the minimum of its finite lines

```text
B_(ell,a+epsilon,epsilon)(alpha)+z*alpha,
```

for ALL z>=0. Its representation as at most O(ell) lines per budget/flag is complete even if some lines are dominated. No sampling of outside z, unique-path restriction, fixed-k hypothesis or unattainable state is used. This proves LC9 at its exact one-portal import.

## 7. Exact written storage/time/bit proof, including witnesses

The following explicit construction realizes the claimed bounds; it is a mathematical algorithm description, NOT executed code.

1. Precompute f(r),0<=r<=ell-1, directly from its finite sums. At most O(ell) summands per r gives O(ell²) exact operations. A(u) can be queried by LC5 in constant time or precomputed in O(ell) more operations.
2. Maintain one table slot for each(k,epsilon,2alpha). There are O(ell) budgets, two flags and2ell-1 mass indices, hence O(ell²) TOTAL slots. Initialize unattainable slots to infinity and add the explicit boundary rows.
3. For epsilon0 process each triple(k,r,t) in LC7 one at a time. The total number is at most

   ```text
   sum_(k=1)^(ell-1) sum_(r=1)^(ell-k) r=O(ell³).
   ```

   Compute s,j, the D_j query with its j0 guard and zero-remainder guard, alpha and candidate cost in constant many exact arithmetic operations. Update that alpha's minimum, retaining ONE argmin descriptor. No full candidate list is stored.
4. For epsilon1 compute each LC8 row with a constant-operation D_k query. Its all-selected row is included. This adds O(ell) work.
5. For a finite epsilon0 slot store r,t as the witness, with j,s already determined by its key/r; the residual q,rho are computed in constant time. For epsilon1 store or recompute q,rho. These are CONSTANT-SIZE integer descriptors, not a separately stored vector or a complete selected set for each slot. Ties need only one chosen argmin.

A requested optimum is reconstructed by choosing a canonical ordering of rho residual gaps of q+1 and the remaining gaps q, then walking around the cycle as in Section6. This takes O(ell) time and O(ell) transient output/storage. Even if an explicit witness is emitted for EVERY O(ell²) finite slot, streaming them costs O(ell³) total operations/output length and preserves O(ell²) internal table storage. Storing all explicit witness vertex sets simultaneously is NOT the claimed O(ell²) storage bound.

All f,alpha,beta and finite D values are half-integers. A pair contributes at most1, so beta and every partial gap sum are at most binomial(ell,2); alpha<=ell-1. Multiplying the table values by2 gives nonnegative integers O(ell²). Indices, quotients, remainders and constant-size descriptors also have O(log ell) bits. LC4's nonnegative terms represent actual balanced gap costs and stay within the same O(ell²) bound. Exact comparisons therefore need no numerical tolerance.

Consequently construction uses O(ell³) exact arithmetic operations on O(log ell)-bit numbers, including f preprocessing and compact witness bookkeeping. Standard integer arithmetic makes total BIT time polynomial as well; this is not merely a unit-cost claim on exponentially large integers. The table and backpointer bit storage is O(ell² log ell).

The O(log ell) coefficient bound concerns TABLE CONSTRUCTION, not a numerical query at an arbitrary outside rational z of large bit length. LC9 is already an exact symbolic min-of-lines representation; evaluating it at such a z must additionally account for z's own bit length. No claim of constant-bit arbitrary-z evaluation is inferred.

## 8. All-length/tie and nonuniqueness boundaries

The proof applies uniformly to ell3 and every larger odd/even length: odd ell uses h0=(ell-1)/2 with no tie term; even ell uses h0=ell/2-1 and exactly one-half at distance ell/2. The r0/1 and j0 cases are explicit, and k0 is deliberately outside the selected-gap geodesic argument.

Attainment does not mean uniqueness. For example, distinct cyclic placements/permutations of balanced gaps can yield the same minimum and portal mass. The table stores one witness, not every optimizer. No uniqueness or exponential enumeration of all minimizers is required for the operator.

There is no need to call a graph package, enumerate selected subsets or run the algorithm to establish these finite symbolic bounds. No such implementation/test evidence is claimed here.

## 9. Decorated cycles and other claims are outside this gate

S2:366–369 correctly preserves the obstruction to promoting this result. With child subcacti at other cycle vertices, the weights are `w_i=(1-epsilon_i)+alpha_i` and child beta values/budgets vary. The interaction is the genuine weighted sum of h_ij*w_i*w_j. The unit-pair count r-d and the length-only convex exchange no longer justify optimizing those choices. Replacing all w_i by1 would narrow the original problem.

Thus this review establishes no polynomial envelope bound for decorated cycles, no arbitrary-cactus polynomial algorithm, no NP-hardness, no unrestricted forcing theorem, no new primary-slot cutover and no novelty. The exact predecessor portal state is only its named interface import.

Although read completely for context, the NEW S2 Sections2–4 portal-swap/LF/CAL theorems are separately assigned v54-A and are NOT_RECONSTRUCTED/accepted by this verdict. LC does not need their correctness. S4's PH7 section and its other gate are likewise outside this mathematical reconstruction. Public-search/book/corpus ancestry claims are read as bounded reports, not independently re-audited openness or novelty evidence.

## 10. MINOR1 — explicit zero-remainder/domain convention for LC4

**Locations:** S2:267,283–285,294–298 and its use at333–339.

f_ell is declared only for0<=r<=ell-1. In LC4, j1,s=ell-1 gives q=ell-1 and rho0. The printed expression `(j-rho)f(q)+rho f(q+1)` then contains a zero-weight f(ell), outside the declared domain. This case actually occurs at k1,epsilon1, so an exact all-budget construction should not perform that query. The balanced-allocation proof already shows its intended value is simply f(ell-1).

**Minimal additive repair:** state explicitly that when rho=0 the second term is OMITTED, i.e. D_j(s)=j*f(q), and f(q+1) is queried only if rho>0. In that case q+1<=s<=ell-1, so it is in domain. Keep the separate j0 rules. Also read LC3 only where both f arguments are defined (0<=r<=ell-2), or explicitly declare an algebraic extension if a larger domain is wanted; the proof itself needs no extension.

This is a MINOR finite-domain/convention issue, not a failure of the gap minimization theorem or complexity bound. The complete written reconstruction above uses the zero-weight omission and gives actual placements for the boundary row. No source/pinned file was edited; an additive author clarification is appropriate.

## 11. Final disposition and assurance

- **FATAL:0.** No mathematical counterexample to the stated unadorned leaf-cycle theorem found.
- **MAJOR:0.** LC1 through LC9, both placement directions and all construction bounds have been reconstructed, not supplied by an unreconstructed table.
- **MINOR:1**, the explicit finite-domain convention above. With that convention, the intended operator is exact for all stated lengths/budgets/flags/ties.

No new load-bearing identity within this primary scope is left NOT_RECONSTRUCTED. Contextual swap, PH7, public-source ancestry and stronger general-cactus/classification claims are deliberately excluded rather than silently inheriting a verdict. This is a same-harness supplied-proof cross-domain WRITTEN algorithmic proof, not an implemented run, executable certificate, formal/kernel proof, human/external-family review, novelty clearance or publication acceptance.

All author/shared/pinned files remain unchanged. Only the specified reviewer-root ACK and review were created. No scientific execution, new GO, additional agent/CLI, deadline/cutoff change or round closeout occurred.
