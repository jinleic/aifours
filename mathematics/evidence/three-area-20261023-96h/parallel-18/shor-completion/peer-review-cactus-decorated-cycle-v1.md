# v61-A — complete written reconstruction of the decorated-cycle operator

Reviewer MathShor-2, math-5. Observed clock before creation: **Sun Oct 25 08:46:24 PDT 2026** (`/bin/date`). Output solely in the assigned reviewer root.

## 1. Verdict, scope and actual evidence coverage

**0 FATAL / 0 MAJOR / 0 MINOR at the exact written scope reconstructed below.** All new DG/CK/TF/IP/NS/CO/CA load-bearing identities, state-sufficiency steps, attainment directions and stated complexity bounds are reconstructed. No new load-bearing algorithmic step is left NOT_RECONSTRUCTED.

This supports a WRITTEN exact algorithm for every input cactus with parameterized arithmetic bound `O(N^12*2^(5c_e))`, and its stated odd-cycle/log-even-cycle polynomial cases. It does NOT establish polynomial input-bit time for unbounded c_e, hardness, implementation/test evidence, independent-family/formal acceptance or novelty.

### Frozen source binding

- **S1:** `parent-evidence-erratum-v9.md`, SHA-256 `b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`, LF1–35, read FIRST and in full.
- **S2:** `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/replacement-information-primary-screen-v7-decorated-cycle-operator-v1.md`, SHA-256 `9b89a528db5f2a7ab3ba149bd3de16dbf26951701aa442c3bbbcc11af2f3931e`, full LF1–368, the entire new proof.
- **S3:** same author root, `replacement-information-primary-screen-v6-cactus-portal-swap-v1.md`, SHA-256 `9359694947945528ed5bf0b1bd60687468c63bbc8643abf67ccd0b162a7e2cf5`, full LF1–387.
- **S4:** same author root, `cactus-leaf-cycle-zero-remainder-addendum-v1.md`, SHA-256 `d77e15ce516e0d63641cd0f0f2ae5ea62dc8de40c0c2922402d8e725a7ba7498`, full LF1–20.

Single mandatory part `peer-review-wave-v61-v61-A-part1-v1.md`, SHA-256 `a257aae3924afef817070c8aab56b5d0ff9a2c5b59f1e033a1ccc56fb69e71a5`,67,011 bytes. ALL literal packet LF1–833 were read consecutively in displayed windows1–163,164–323,324–473,474–633,634–833. Every declared source line and ending was actually read.

Load-bearing packet LF89,98,103,110,118,126,136,159,167,176,184,191,208,214,228,238,239,255,259,261,265,274,280,288,294,303,305,306,314,318,321,323,327,329,331,338,341,347,349,355,363,365,373,375,377,383,387,388,389,390,827,829,831 were reread raw. The manifest's truncated scope LF42 was recovered raw. No unresolved load-bearing truncation remains.

Manifest v61-A SHA-256 `754c22af0691a50929daefdb62dd5b7a69d072ddf45dce5093cc97f04d0e2850`; exact entry and complete byte-equality receipt read before ACK/body. Actual manifest/part/all author-source hashes were freshly observed and match. Byte-equality metadata was not substituted for body reading.

ACK before proof body: `peer-review-cactus-decorated-cycle-ack-v1.json`, SHA-256 `53270822554797e9758a09c4e7591ea368782382baf31f8a4b338bf51066be24`. Prior v47/v54 exposure is disclosed. This is a same-harness cross-domain supplied-proof reconstruction, not blind, cross-vendor, human, configured dual-family, formal or novelty acceptance.

No scientific interpreter/eval/program/enumeration/symbolic computation/replay/solver, implementation/test, external CLI or nested agent was used. Source reading, metadata clocks/hashes and writing only. All mathematical arithmetic/complexity reasoning below is WRITTEN.

## 2. Model and the exact inherited one-portal interface

The original graph is finite, simple, connected, unweighted and a cactus. Sites remain unrestricted and k is arbitrary. Selected vertices are not deleted and distances are not recomputed. q is the fraction of ORIGINAL shortest paths avoiding the selection, including endpoints. Undirected reversal gives `GBC=N(N-1)-2beta`, beta the unordered missed mass.

For two rooted components sharing only v, internal geodesics cannot use a positive outside detour returning to v. A cross-side geodesic is uniquely a shortest path to v followed by a shortest path from v; all combinations occur and path counts multiply. Thus its avoiding fraction factors. At matching portal flags this gives the inherited exact law

```text
alpha_union=alpha_H+alpha_J,
beta_union=beta_H+beta_J+alpha_H*alpha_J.
```

The current k-values INCLUDE each component root, so `k_union=k_H+k_J-epsilon`, not simply their sum. This convention is retained throughout S2.

The named v5 I2 source is the earlier frozen300-LF source at SHA-256 `5c961bb5115861285dec23a6519ad04e348e725657fd287e5d00f4a58d2459b8`; its portal mathematics was actually read/reconstructed in the earlier serial cactus review. It is a named import here, not a newly certified complexity theorem. The geodesic product argument above supplies the exact interface required by the new proof.

The v6 portal-swap result is contextual and unnecessary for DG through CA; this review does not transfer another review's verdict to it. The new cycle algorithm is reconstructed from actual variable child profiles, not the bare-cycle equal-weight theorem.

## 3. DG: EVEN blocks alone control denominators and table size

A vertex pair has one block-cut route. In an edge or an odd cycle the shortest passage is unique. In an even cycle the passage is unique unless its two terminals are antipodal, when exactly two arcs tie. Each such block's fraction is0,1/2 or1. Avoidance of selected vertices is a LOCAL condition in each traversed block; an articulation selected anywhere on the route makes the product zero. Therefore all total and avoiding counts factor, so every positive q is exactly2^-t for some t no larger than the number c_e of EVEN blocks in the whole cactus.

With D=2^c_e, D*alpha and D*beta are integers. The actual ranges are0<=alpha<=|H|-1 and0<=beta<=binomial(|H|,2). This strictly refines the earlier all-cycle denominator upper bound; it does not pretend odd cycles have no geometric effect.

For fixed(k,epsilon,alpha), replacing beta by the minimum is safe at a single portal because all outside dependence uses beta+zalpha, and safe in a cycle because beta_i enters additively while all other dependence uses only k_i,epsilon_i,alpha_i. The replacement also has an actual attaining witness; no unattainable mass is introduced.

There are N+1 possible k indices, two flags, and at most ND+1 possible masses on the1/D grid. Hence

```text
S<=2(N+1)(ND+1)=O(NM),   M=ND.
```

This count is polynomial in D, NOT in log D. Selected-root entries automatically have alpha0; the uniform two-flag bound is deliberately loose.

## 4. CK: genuine variable-child weighted geometry

The child sets H_i are disjoint and include their DISTINCT cycle roots v_i. For an actual child entry,

```text
w_i=(1-epsilon_i)+alpha_i
```

sums avoidance from ALL of H_i to its root, including the zero-length root path. If the root is selected, w_i=0 even if some internal descendant pairs remain missed. Its beta_i is still needed and is NOT dropped.

For different children every geodesic combines child-to-root paths with a shortest cycle arc. Thus CK1 is exactly

```text
beta=sum beta_i+sum_(i<j)h_ij*w_i*w_j,
alpha=alpha_0+sum_(i!=0)h_i0*w_i,
k=sum k_i.
```

There is no budget subtraction here because the H_i roots are distinct. Only later articulation merges have a shared root.

When at least one cycle vertex is selected, different unselected gaps have h_ij0. In one gap, its within-gap arc avoids all selected cycle vertices while its complement contains a selected vertex. The ORIGINAL shorter arc therefore contributes1 when2d<ell, half when2d=ell, and0 when2d>ell. This is the weighted kernel K_ell, including the antipodal half. No surviving longer arc is promoted to a recomputed geodesic.

Consequently one interval's exact contribution is

```text
J(I)=sum beta_i+sum_(i<j)K_ell(j-i)*w_i*w_j.
```

The w_i and beta_i are genuine variable child states, not unit weights, free gadget parameters or independently assigned real numbers. Length-only gap balancing is not used to optimize them.

## 5. TF: complete-pair square minus two-front corrections

The algebraic identity `sum_(i<j)w_i*w_j=(W²-sum w_i²)/2`, with W=sum w_i, gives

```text
J(I)=sum eta_i+W²/2-E(I),   eta_i=beta_i-w_i²/2.
```

Eta may be negative, but it is just an exact shift, not a negative graph input weight or altered objective.

### Odd ell=2h+1

For r<=h+1, every distance is at most h and E0. Otherwise p=r-h-1>0. Since r<=2h, p<=h-1. Left positions1..p, right positions h+2..h+1+p=r, and central positions p+1..h+1 are disjoint. All pairs except possibly left/right have distance at most h; in particular left-to-central and central-to-right maximum distances are exactly h.

For L_i and R_t the distance is h+1+t-i. It exceeds the shortest threshold precisely when t>=i. Thus

```text
E=sum_(i<=t)L_i*R_t=sum_t(L_1+...+L_t)*R_t.
```

This proves every term of TF2, including its full diagonal removal.

### Even ell=2h

For r<=h, all distances are below h, so E0. Otherwise p=r-h>0 and p<=h-1 because r<=2h-1. The left1..p, right h+1..h+p=r and central p+1..h groups are again disjoint. Every non-left/right pair has distance at most h-1.

The left/right distance is h+t-i. For t>i its interaction is removed entirely, for t=i exactly half is removed, and for t<i none is removed. Therefore

```text
E=sum_(i<t)L_i*R_t+(1/2)sum_i L_i*R_i
 =sum_t(L_1+...+L_(t-1)+L_t/2)*R_t.
```

This proves TF3 with its ESSENTIAL half-diagonal. Removing the whole diagonal or none would give the wrong antipodal contribution. When p<=0 the pair lists are empty and all positions are central. These formulas cover the shortest valid odd/even cycles and r0/1 without overlapping positions or charging a child twice.

## 6. IP: portal statistic, sufficient state and exact attainment

### Root mass is P-1, not P

When the proper unselected interval I contains v0, all its child portal flags are0. For each position take c_i=K_ell(|i-t0|) and c_t0=1. The complete weighted root interaction is P=sum c_i*w_i. The root child contributes w0=1+alpha0; the other terms are exactly its cycle interaction. Thus

```text
alpha_out=P-1=alpha0+sum_(i!=0)h_i0*w_i.
```

The1 removed is the portal vertex itself, not a diagonal beta term or a selected-site charge. P>=1 on completion because w0>=1. A nonroot interval has no root-mass emission; its c_i are0. An EMPTY interval has only cost/budget0 and cannot contain v0, so P-1 is never incorrectly applied to it.

### State invariant and paired/central transitions

At a FIXED interval and processing stage, retain minimum g at(K,W,U,P). W contains all processed masses, U only processed LEFT masses. Choose actual epsilon0 child entries, with their k,w,beta and eta. At pair t, the old U is the sum of L_1,...,L_(t-1). TF then gives exactly

```text
odd:  g'=g+eta_L+eta_R-(U+L)*R;
even: g'=g+eta_L+eta_R-(U+L/2)*R,
```

with simultaneous updates K+k_L+k_R,W+L+R,U+L,P+c_L L+c_R R. The even term is not half of the entire prefix product: only the current diagonal L*R has coefficient1/2. This distinction is reconstructed, not inferred from an odd-cycle recurrence.

Every correction with a processed right endpoint now has all its relevant left endpoints processed. A future LEFT index cannot interact with an earlier right endpoint in E. Therefore future corrections depend only on U, not an unrecorded vector of earlier masses. The final complete-pair restoration depends only on W, future exact budget on K, and outside root interaction on P. Central positions have no E interaction; their transition adds eta and updates K,W,P while leaving U unchanged. The final cost is g+W²/2.

Induction gives both directions: every child-choice tuple follows these transitions, and every generated finite state has exactly an actual tuple witness. At identical stage and keys, a smaller g can always replace a larger one because all future additions/restoration depend only on those keys. Minimizing W,U at fixed final K,P, or over them for a nonroot interval, is lossless for the emitted interface. This is an exact attained interval table, not a relaxation in which arbitrary masses are separately selected.

### IP5 grids and bit sizes

Child disjointness gives sum w_i<=sum|H_i|<=N. Thus0<=W,U,P<=N and K<=N. W,U are on the1/D grid and P may temporarily be on the1/(2D) grid. With M=ND this gives

```text
O((N+1)(M+1)^2(2M+1))=O(NM³)
```

state keys per stage. At most O(ell) stages and S² actual child-entry pairs per paired stage give O(ell*N*M³*S²) operations per interval; central S choices fit this bound. The P coordinate can be omitted for a nonroot interval, but the uniform bound is valid.

All eta, products and half-products have common denominator2D². Partial sum beta and complete-pair mass sums are bounded by O(N²), so both positive and negative shifted g have magnitude O(N²). Numerators/indices need O(log N+log D) bits. Exact minimum comparisons and products are polynomial-bit operations; no sampling, rounding, tolerance or real oracle is used.

Backpointers store one winning previous key and actual child entry/pair per finite state. The inductive witness yields each emitted minimum by actual child selections.

## 7. NS: the no-selected-cycle case is separate and necessary

Here EVERY epsilon_i=0, though descendants may still contain selected vertices. Each shortest cycle arc, including BOTH arcs at an antipodal tie, avoids the cycle selection. Therefore h_ij=1, not K_ell(d). The child leg avoidance remains in w_i.

The whole cycle interaction is complete-pair, giving exactly

```text
beta=sum(beta_i-w_i²/2)+W²/2,
alpha=W-1,
k=sum k_i, epsilon0=0.
```

The root's unit is subtracted once. State(K,W), accumulating sum eta_i over actual epsilon0 child entries, is sufficient. Final W restoration and pruning at fixed(K,W) preserve every attained interface. At most O(NM) keys, S choices per child and O(ell) children give O(ell*N*M*S) operations.

This covers budget0 and all patterns selecting only internal child vertices. Treating the entire unselected cycle as a fictitious proper gap would incorrectly block a complementary arc; NS explicitly avoids that error. For the empty global selection the formula reduces to alpha=|H|-1 and beta=binomial(|H|,2), as required.

## 8. CO: closing the decorated cycle without mask enumeration

Precompute IP for every cyclic PROPER interval, length0 through ell-1, at every starting position: O(ell²) intervals. Selected child tables Sel_i(k) keep beta minima among epsilon1 entries. Their alpha and w are0, but their INTERNAL beta may be positive and remains charged.

For epsilon0=1, anchoring at v0 loses no selection. For epsilon0=0, try all anchors a!=0 and forbid a selected arrival at the interior position representing v0. This is a conditional flag row, not a restriction on the final union of both flags. In any full path0..ell, v0 must then lie in exactly ONE open interval; no later gap can contain it again.

Initialize F[0,k,0]=Sel_a(k). A transition from selected position s to t>s chooses the actual IP entry for its open interval, its budget g/cost b_I/root-mass index A_I, and, if t<ell, a selected-child minimum of budget b at t. CO1 adds g+b to K, A_I to A, and b_I+Sel_t(b) to cost. Selected children have no cross-gap mass, so there is no omitted interaction with another gap.

At t=ell the endpoint is the SAME anchor; adding cost0 and budget0 is essential. Its child was assigned only at initialization. One-anchor closure correctly uses the length-(ell-1) proper interval, and adjacent selected vertices use the actual empty interval. The only forbidden interior selected arrival is v0 in the epsilon0=0 row.

### Completeness and attainment, separately

Given any actual cycle selection with at least one selected cycle vertex, choose an allowed anchor. Its selected positions determine a CO path. Each of its unselected gaps can be replaced by an IP minimum with the same exact budget and, for the unique root gap, the same alpha; beta does not increase. A selected child can be replaced by Sel at the same budget because its w=0. Thus no optimum interface is missed.

Conversely, a finite CO path assigns every distinct cycle child EXACTLY once: selected endpoints, disjoint unselected intervals, and anchor only at initialization. The attained child witnesses assemble into one legal unweighted-graph selection, with total budget K. CK3 and the zero cross-gap interactions make its beta the stored sum. If v0 is unselected, its unique gap supplies exactly P-1; if selected its alpha is0. Thus every output is attained, not just a formal lower bound. NS covers exactly the remaining selections with no selected cycle vertex.

This also proves the output-grid statement. The temporary root coordinate uses1/(2D); it is NOT rounded or filtered by an unproved divisibility shortcut. Once CO's actual selection witness is established, DG applied to that REAL output subcactus proves that D*alpha and D*beta are integers. The final profile therefore lies on the true1/D grid and has the claimed DG entry count. Attainment comes logically BEFORE this reindexing; a finer temporary grid alone would not justify it.

The root mass is accumulated at most once, so A<=2DN=2M. In the selected-root row A0 throughout. Final minima over anchors at fixed(K,epsilon0,alpha) and adding NS to flag0 are exactly the complete pruned cycle profile. Stored anchor/path/gap/child predecessors reconstruct an attaining original selection.

## 9. Exact decorated-cycle operation bound

Using S=O(NM), all proper interval tables together cost

```text
O(ell²)*O(ell*N*M³*S²)
 =O(ell³*N*M³*S²)
 =O(ell³*N³*M⁵).
```

The geometric coefficients, pairing orders and interval endpoints can be formed within smaller polynomial work; no selected mask is materialized.

One anchor's closing table has O(ell*N*M) keys. Per key, O(ell) next positions, O(N) gap budgets, O(N) selected-child budgets and O(M) root-mass entries suffice. Times O(ell) anchors this gives O(ell³*N³*M²), smaller than the interval term. Sel preprocessing and NS are also smaller. Hence with ell<=N and M=ND, the cycle operator uses at most

```text
O(N^11*D^5)
```

exact arithmetic operations, as claimed. These counts include both flag rows, all budgets, all child states and one-anchor/empty-gap boundaries, not an unnoticed2^ell cycle-selection enumeration.

All state/choice loops are over finite integer-indexed grids and actual table entries. Per-stage backpointers and all stored interval/cycle tables have size bounded by the same loose operation bound. Keeping all winning records, or streaming outer loops with appropriate retained winners, remains within it. Witness reconstruction follows actual recorded choices; no additional exponential search is hidden there.

## 10. CA: edge and articulation integration on the whole cactus

The singleton entries are exactly(0,0,0,0) and(1,1,0,0). For an edge from new parent v to child u, w=(1-epsilon_u)+alpha_u sums the child's avoidance mass to u INCLUDING u. All old child geodesics are unchanged because v is a new leaf relative to that component. New missed pairs are precisely v-to-child, contributing(1-epsilon_v)w. Thus

```text
k=k_u+epsilon_v,
alpha=(1-epsilon_v)w,
beta=beta_u+(1-epsilon_v)w.
```

Both parent flags are used and each edge output has an actual witness.

At an articulation merge the components share only v. The actual selected-set union has size `k_H+k_J-epsilon`, and the geodesic law in Section2 gives the claimed CA2 alpha/beta. Each component includes v once, so subtracting epsilon is essential; equivalently the old internal a indices add. Witnesses union consistently at the matching root flag.

Root the block-cut tree. At a cycle, the profiles attached to different cycle vertices are actual disjoint subcacti and are available bottom-up; the parent-portal child can be the singleton. Other blocks at the same portal merge by CA2. Induction over singleton/edge/cycle/articulation operations gives EVERY attainable profile optimum, not only freely prescribed masses. No unvisited ancestor state is used to create a circular dependency.

At the whole root z=0, minimizing beta over both flags and all alpha at the requested budget k is exactly unrestricted selection optimization; return N(N-1)-2beta and its witness. Conditional impossible rows have no finite entry. k0 is supplied by the empty selection and gives GBC0; k=N has the fully selected witness with beta0. No portal or other site is prohibited globally.

There are O(N) blocks and sequential articulation merges in a cactus. With S=O(N²D), an articulation merge costs O(S²), an edge O(S), and a cycle at most O(N^11D^5). Thus a safe total is

```text
O(N^12D^5)=O(N^12*2^(5c_e))
```

exact arithmetic operations. The lower-cost edge/merge operations fit this same bound. All numbers and indices have O(log N+c_e) bits up to constant factors, including the temporary2D² cost denominator. Multiplying by a polynomial in that bit length gives a genuine bit-time bound. Predecessor storage/reconstruction is within the same loose parameterized bound, not an unbounded-precision arithmetic oracle.

Consequently:

- the algorithm works for EVERY cactus and arbitrary k with fixed-parameter time in c_e (the polynomial bit factor in c_e may be absorbed into the parameter function);
- for c_e0, D1 gives a polynomial exact algorithm with arbitrarily many/long decorated ODD cycles, not merely trees or bare cycles;
- for fixed B and c_e<=B*log2N, D<=N^B yields polynomial time, with exponent depending on B;
- unbounded c_e may make D exponential, so this is NOT polynomial input-bit time for arbitrary cacti, not a complete-envelope polynomial theorem and not hardness.

## 11. Findings, old minor closure and assurance exclusions

**FATAL:0 / MAJOR:0 / MINOR:0 for the new reconstructed chain.** Every required DG/CK/TF/IP/NS/CO/CA step has the written derivation above; no new load-bearing identity or attainable-state claim is left NOT_RECONSTRUCTED.

The supplied S4 addendum explicitly omits the unused f(q+1) term at zero remainder, handles j0 separately and restricts old forward differences to0<=r<=ell-2. It correctly closes the v54-B finite-domain MINOR without changing the frozen v6 bytes. No old minor is transferred to v7 automatically.

Not newly accepted:

1. An unbounded-c_e polynomial-in-input-bit-time theorem, polynomial complete envelopes for all subcacti, NP-hardness or a full arbitrary-cactus complexity classification.
2. An implementation, benchmark, graph-program run, scientific replay, independently executed certificate or numerical performance/resource result. The stated operations are written algorithmic bounds only.
3. New correctness/novelty credit for the separately reviewed v6 portal-swap/hardness-route theorem. It is contextual and not a correctness premise for this new operator.
4. Public-search execution, external specialist priority, book/corpus screening or exhaustive openness/novelty. Those bounded ancestry statements are read as source reports, not independently authenticated here.
5. A primary-slot cutover, extra owner, new GO, external-family/human/formal acceptance, publication, deadline extension or round closeout.

The retained geodesic/block-cut interface is the named classical/previously reconstructed import; the actual new child-state and cycle recurrences have been reconstructed here rather than promoted from their headings. Source and parent/shared/pinned files were not edited. Only the specified ACK/review were created in the owned root. Parent v9, all prior admission qualifications, the original deadline/cutoff and scientific HOLD remain binding.
