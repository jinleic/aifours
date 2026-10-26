# A two-front decorated-cycle operator and an exact even-cycle-parameter algorithm

Owner: InfoResearch96h-2, original slot info-1. Additive successor to the frozen cactus v5/v6 packets. Actual source-search window bounds are recorded in Section 10. This packet is **NEW WRITTEN, UNREVIEWED**; no execution, kernel checking, configured-family/human/formal acceptance or novelty clearance is claimed.

## 1. Unchanged target and named imports

The target remains all finite simple connected UNWEIGHTED cacti, all integers 0<=k<=N, unrestricted selectable vertices, and the endpoint-inclusive ordered all-shortest-path objective. Write

```
beta_G(C)=sum_(unordered distinct {x,y}) q_G,C(x,y),
GBC_G(C)=N(N-1)-2 beta_G(C), |C|=k,
```

where q is the fraction of the ORIGINAL graph's shortest paths avoiding C. Selecting a vertex neither deletes it nor recomputes distances. All even-cycle ties are retained. No child masses below are input vertex/edge weights: they are the exact boundary masses induced by ordinary unweighted subcacti.

Named imports:

- **I1:** cactus-exact-target-and-state-freeze-v1.json, the unchanged exact target and single-portal state convention. No new primary cutover or GO is implied.
- **I2:** replacement-information-primary-screen-v5-cactus-hardness-sketch-v1.md, Section 2, its accepted articulation/cycle shortest-path product identities. Its bit-length observation used the number of ALL cycles; Section 2 below explicitly refines that bound to the number of EVEN cycle blocks.
- **I3:** replacement-information-primary-screen-v6-cactus-portal-swap-v1.md, 387 LF, SHA-256 9359694947945528ed5bf0b1bd60687468c63bbc8643abf67ccd0b162a7e2cf5: the original-graph gap kernel, NOT its length-only equal-mass exchange as a decorated-cycle algorithm.
- **I4:** cactus-leaf-cycle-zero-remainder-addendum-v1.md, 20 LF, SHA-256 d77e15ce516e0d63641cd0f0f2ae5ea62dc8de40c0c2922402d8e725a7ba7498. It omits the unused f(q+1) term at zero remainder, handles j=0 separately and restricts forward differences to their declared domain. Frozen v6 is unchanged.
- **I5:** run-root cactus-portal-swap-leaf-cycle-parent-v1.md: scoped written acceptance of the portal-swap and bare leaf-cycle results, with I4's minor convention. Its acceptance does not extend automatically to this successor.
- **I6:** [Fink–Spoerhase 2010](https://arxiv.org/html/1008.3503v1), objective/path-coverage ancestry and the prior polynomial tree result. No cactus operator is imported from its tree theorem.

Parent erratum v9 was read in full first. Global HOLD is binding. ALL new mathematics here is written: no arithmetic interpreter, enumeration, graph package, symbolic program, native scientific process, solver or replay was used. Algorithmic recurrences below are descriptions and proofs, not executed programs.

**Delivered scope:** an exact polynomial-in-(N,D) operator for GENUINELY DECORATED cycle blocks with actual variable child states; then an exact algorithm on every cactus with arithmetic-operation bound O(N^12 * 2^(5 c_e)), where c_e is the number of EVEN cycle blocks. This yields polynomial cases c_e=0 and c_e=O(log N), and fixed-parameter tractability in c_e. It is NOT a bit-polynomial theorem for unbounded c_e and does not settle the unrestricted cactus complexity classification. The lead remains unbound and priority UNCLEAR.

## 2. Exact child profiles and the even-cycle denominator bound

**Lemma DG — WRITTEN; imports I1/I2 and the elementary block geometry below. Scope:** any rooted subcactus H of an N-vertex cactus having c_e even cycle blocks in total. Put D=2^(c_e).

For a selection C in H, let epsilon indicate whether its portal v is selected and set

```
a=|C minus {v}|, k_H=|C|=a+epsilon,
alpha=sum_(x in H minus {v}) q_H,C(x,v),
beta=beta_H(C).
```

The unique block-cut route between two vertices traverses edges and cycle blocks. In an odd cycle the shorter arc is unique. In an even cycle there is either a unique shorter arc or two antipodal shortest arcs. For an unblocked antipodal passage, the avoiding fraction in that block is 0, 1/2 or 1 according to how many of its two arcs avoid the selection. The accepted product identity multiplies these independent block fractions. Every positive q is therefore a power 2^(-t) with t<=c_e. Consequently

```
D*alpha and D*beta are integers,
0<=alpha<=|H|-1, 0<=beta<=|H|(|H|-1)/2.                (DG1)
```

This is a refinement of I2's all-cycle bound, not a claim that odd cycles have no effect on the objective. They have no factor-2 ambiguity but still have nontrivial shortest-arc geometry.

At each (k_H,epsilon,alpha), retain only the smallest beta and one attaining selection descriptor. For one-portal attachment every outside dependence is beta+z*alpha with fixed flag/budget and z>=0, by I2. Thus this pruning loses no profile optimum. It is also safe INSIDE a decorated cycle, where the child beta enters additively and all other dependence uses only alpha, epsilon and budget.

Put M=N*D. The number of retained entries in any child table, over all budgets and flags, is bounded by

```
S<=2(N+1)(M+1)=O(N*M).                               (DG2)
```

This count is not polynomial in log D. The remaining sections give the missing polynomial-in-D cycle-pattern operator, rather than mistaking DG2 alone for an algorithm.

## 3. The genuinely decorated cycle and its weighted gaps

**Claim CK — WRITTEN; imports I2/I3. Scope:** a cycle v_0,...,v_(ell-1), ell>=3, with actual rooted subcacti H_i at its vertices. The H_i are vertex-disjoint, allowing singleton children. The output portal is v_0. Each child input is its COMPLETE pruned table from DG, with actual attainment.

Choose one child entry (k_i,epsilon_i,alpha_i,beta_i) at each vertex and put

```
w_i=(1-epsilon_i)+alpha_i.
```

Thus epsilon_i=1 implies alpha_i=w_i=0, while epsilon_i=0 gives w_i=1+alpha_i>=1. The exact original-graph composition is

```
beta_total=sum_i beta_i+sum_(i<j) h_ij*w_i*w_j,
alpha_total=alpha_0+sum_(i!=0) h_i0*w_i,
k_total=sum_i k_i.                                  (CK1)
```

The child roots are distinct, so k_total here counts every vertex once. The old internal-budget index is a_total=k_total-epsilon_0.

Suppose at least one cycle vertex is selected. The other cycle vertices form unselected cyclic intervals, or gaps, between selected cycle vertices. Their lengths range from 0 to ell-1. Different gaps have h_ij=0. In one gap, renumber its positions 1,...,r in cyclic order and define

```
K_ell(d)=1   if 2d<ell,
       =1/2 if 2d=ell,
       =0   if 2d>ell.                               (CK2)
```

For distinct positions within this gap h_ij=K_ell(|i-j|): a shorter unselected arc survives, a longer one is not an original shortest path, and an antipodal tie has exactly one surviving arc. Its EXACT contribution, including child-internal pairs, is

```
J(I)=sum_(i in I) beta_i
     +sum_(1<=i<j<=r) K_ell(j-i)*w_i*w_j.             (CK3)
```

Unequal w_i and variable beta_i are retained. The bare-cycle length-only gap function and balancing exchange do NOT optimize CK3.

## 4. The new representation: a triangular two-front correction

**Lemma TF — WRITTEN; imports CK only. Scope:** one proper unselected interval I, all of its child portal flags zero, with arbitrary actual child-state choices. No equality of masses is assumed.

Let W=sum_i w_i and eta_i=beta_i-w_i^2/2. Then

```
J(I)=sum_i eta_i+W^2/2-E(I),                          (TF1)
```

where E subtracts the complete-pair interactions that fail, or partly fail, to be shortest surviving arcs. The possibly negative eta_i is algebraic bookkeeping, NOT a negative input graph weight or a new objective.

### 4.1 Odd cycle ell=2h+1

If r<=h+1, every within-gap distance is at most h, so E=0. Otherwise set p=r-h-1>0 and split the interval into

```
L_i=w_i,                    1<=i<=p;
R_t=w_(h+1+t),              1<=t<=p;
central positions p+1,...,h+1.
```

Since r<=2h, these groups are disjoint. A left/right pair has distance h+1+t-i. This is too long exactly when t>=i. All other pairs survive fully. Therefore

```
E=sum_(1<=i<=t<=p) L_i*R_t
 =sum_(t=1)^p (L_1+...+L_t)*R_t.                     (TF2)
```

### 4.2 Even cycle ell=2h

If r<=h, every distance is below h, so E=0. Otherwise set p=r-h>0 and split into

```
L_i=w_i,                    1<=i<=p;
R_t=w_(h+t),                1<=t<=p;
central positions p+1,...,h.
```

The distance is h+t-i. For t>i the complete-pair contribution must be removed; for t=i half must be removed; for t<i none is removed. Thus

```
E=sum_(1<=i<t<=p) L_i*R_t+(1/2)*sum_(i=1)^p L_i*R_i
 =sum_(t=1)^p (L_1+...+L_(t-1)+L_t/2)*R_t.           (TF3)
```

The last term is essential: dropping it would silently choose one antipodal geodesic. Again the groups are disjoint because r<=2h-1. Every central vertex has no removed or half-removed interaction. If the corresponding p is nonpositive, use no left/right pairs and regard all r vertices as central.

TF2/TF3 are exact triangular factorizations of the ORIGINAL gap kernel. They are not an assertion that arbitrary child masses are free realizable gadget parameters.

## 5. Exact interval dynamic program with two mass fronts

**Theorem IP — WRITTEN; imports DG, CK and TF. Scope:** compute the optimum CK3 over ALL genuine child-table choices on a specified proper interval I, for every exact budget and, when required, every output-portal mass. Complexity is polynomial in N,D and the input table bound S. This is a finite written recurrence, not a run.

### 5.1 Root-mass statistic

If I contains the output cycle vertex v_0, let t_0 be its position in the interval and set

```
c_i=K_ell(|i-t_0|), including c_(t_0)=1,
P=sum_(i in I) c_i*w_i.
```

Every other gap has zero avoidance to v_0. Because w_0=1+alpha_0, the full output portal mass contributed by this unique gap is exactly

```
alpha_out=P-1.                                      (IP1)
```

The unit subtracted is the cycle portal itself. This is boundary bookkeeping, not a diagonal pair in beta. Formula IP1 includes alpha_0 and every other child's correctly tied root interaction. Since w_0>=1, its completed P is at least 1. If I does not contain v_0, take every c_i=0 and do not emit a root mass.

### 5.2 State and recurrence

Process the paired positions (L_t,R_t) in increasing t, then the central positions in any fixed order. At each stage retain the smallest shifted cost g for each state

```
(K,W,U,P),
K = total chosen child selection count already processed,
W = sum of ALL processed masses,
U = sum of processed LEFT masses only,
P = sum of their processed c_i*w_i contributions.
```

The initial state is (0,0,0,0) with g=0. Every choice at a processed position is an actual child-table entry of flag epsilon_i=0, with its own k_i,w_i,beta_i and eta_i=beta_i-w_i^2/2.

At paired stage t choose one actual entry for each of its two distinct children. If their masses are L,R, child budgets k_L,k_R and local costs eta_L,eta_R, update

```
K'=K+k_L+k_R,
W'=W+L+R,
U'=U+L,
P'=P+c_L*L+c_R*R;

g'=g+eta_L+eta_R-(U+L)*R           in the ODD case;
g'=g+eta_L+eta_R-(U+L/2)*R         in the EVEN case.   (IP2)
```

For a central child entry of mass w, budget k_i and eta_i,

```
(K',W',U',P')=(K+k_i,W+w,U,P+c_i*w),
g'=g+eta_i.                                         (IP3)
```

Keep exact minima at identical state keys. At the final stage restore the complete-pair square:

```
beta_I=g+W^2/2.                                     (IP4)
```

If I is a root-containing interval, emit (K,alpha_out=P-1,beta_I), minimizing over W,U at fixed K,P. Otherwise emit (K,beta_I), minimizing over W,U. The empty interval emits only budget 0 and cost 0, and never contains the root.

### 5.3 Sufficiency, exactness and attainment

After paired stage t, every correction whose right endpoint has been processed has all its left endpoints already processed: in TF2 they have i<=t, and in TF3 they have i<=t with the displayed diagonal half factor. A future left index cannot contribute to an earlier right index. Hence g is exactly the sum of processed eta values minus all completed corrections. The next correction needs only U and the two chosen entries. Future square restoration needs only W; future budgets and portal statistics need only K,P. No unrecorded vector of earlier masses is needed. Central positions have no correction interaction by TF.

Induction proves that every generated state has an actual child-choice witness and the correct shifted cost. Conversely every child-choice tuple follows one of these transitions. Keeping only its minimum g at fixed stage,K,W,U,P is lossless because all future dependence uses precisely those keys. TF1 and IP1 then prove exactness of the emitted interval tables. Store one winning predecessor/entry pair at each finite state; following these pointers realizes every emitted minimum by actual selections, not an abstract state assignment.

### 5.4 Finite state and bit bounds

The disjoint child vertex sets imply sum_i w_i<=sum_i |H_i|<=N. Thus K<=N, W,U<=N, and 0<=P<=W<=N. Scale W,U by D and P by 2D; the latter permits its half coefficients. With M=ND there are at most

```
O(N*M^3) states per stage,
O(ell*N*M^3*S^2) operations per interval.             (IP5)
```

Pair stages choose at most S^2 actual entry pairs; single stages need at most S choices and fit the bound. There are O(ell) stages. For an ordinary nonroot interval P can be omitted, but IP5 is a uniform upper bound.

All shifted costs can be represented with common denominator 2D^2. Child beta values have denominator dividing D; local squares, products and half-products fit 2D^2. Their magnitudes are O(N^2), so numerators and mass indices have O(log N+log D) bits. Exact minima and products therefore have polynomial bit cost in those lengths. No rounding or approximate profile projection is used.

## 6. The separate case with NO selected cycle vertex

**Lemma NS — WRITTEN; imports CK1 and DG. Scope:** every epsilon_i=0, while internal child selections and their budgets remain unrestricted genuine table choices. This case is NOT a length-ell gap in CK2.

All cycle vertices are unselected, so BOTH shortest arcs avoid the selection at a tie: h_ij=1 for every pair. Put W=sum_i w_i. Then

```
beta_total=sum_i (beta_i-w_i^2/2)+W^2/2,
alpha_total=W-1,
k_total=sum_i k_i, epsilon_0=0.                     (NS1)
```

The output root's own unit is subtracted exactly once. Process children in any fixed order with state (K,W), accumulating sum eta_i. At each child choose ANY actual epsilon_i=0 entry. At the end apply NS1 and minimize beta at fixed K,W. This gives exact attained entries in O(ell*N*M*S) operations. It covers, in particular, budget 0; no cycle anchor or selected cycle vertex is invented. Using CK2 on a fictitious full unselected run would be wrong and is explicitly avoided.

## 7. Closing the cycle without enumerating selected subsets

**Theorem CO — WRITTEN; imports IP, NS, CK and DG. Scope:** the full decorated-cycle operator for all budgets and both output flags, with every genuine variable child state allowed.

Precompute IP's interval tables for all cyclic proper intervals, including the empty interval. There are O(ell^2) such intervals. A root-containing interval records alpha_out=P-1; a nonroot interval has no root mass and emits zero for its root-mass coordinate. Also form

```
Sel_i(k)=min beta_i among actual child entries
         with budget k and epsilon_i=1.
```

Here alpha_i=0 automatically. A selected cycle vertex has w_i=0, so its only contribution is this child cost and its budget.

For a nonempty selected cycle set choose one selected vertex as ANCHOR a and cut the cycle there. Use positions 0,...,ell in cyclic order from a, with position ell the SAME anchor again. Open intervals between successive selected positions are exactly the unselected gaps.

- For output flag epsilon_0=1 take anchor a=0. This loses no selection because v_0 is required selected in this conditional row; both flags will be optimized globally.
- For output flag epsilon_0=0 try all anchors a!=0, and forbid a selected arrival at v_0's interior position. It must instead belong to exactly one intervening unselected gap. This is a conditional DP flag, not a restriction on the final unrestricted optimization.

For one anchor retain F[t,K,A], the smallest cost of a partial sequence whose last selected position is t, with used budget K and accumulated scaled output mass A. Initialize

```
F[0,k,0]=Sel_a(k).
```

For a transition from selected position s to t>s, take the IP table for the open interval I=(s+1,...,t-1). Choose its budget g and cost b_I. If it contains v_0, let its emitted mass be alpha_I and A_I=2D*alpha_I; otherwise A_I=0. For t<ell choose an actual selected-child minimum Sel_(vertex at t)(b). Then update

```
F[t,K+g+b,A+A_I]
 =min(current, F[s,K,A]+b_I+Sel_(vertex at t)(b)).      (CO1)
```

At t=ell use b=0 and selected-child cost 0: the anchor's actual child state was already charged in the initialization. Do NOT add its budget or beta again. Closing after one selected anchor is permitted and uses the length-(ell-1) proper gap. Adjacent selected vertices use the empty interval. Entries whose target t is v_0 are forbidden only in the epsilon_0=0 row, as stated.

Read final F[ell,K,A] with alpha=A/(2D), minimizing over anchors and all paths. In the epsilon_0=1 row every interval excludes v_0 and A=0. Add NS's entries to the epsilon_0=0 row. Finally retain minimum beta at identical (K,epsilon_0,alpha), in the sense of DG.

### 7.1 Why the operator is complete and attainable

Every selection with at least one selected cycle vertex has an allowed anchor. Its chosen selected vertices define a path of CO1 transitions; each intermediate unselected gap has an IP entry of no larger cost with the same budget and, when relevant, the same root mass. Selected children use their Sel minima. Thus the recurrence cannot miss an optimal state.

Conversely every path in CO1 assigns exactly one actual child state to every cycle vertex: selected vertices at its transition endpoints, unselected vertices in its disjoint open intervals, and the anchor only at initialization. All root flags match their gap/selected roles. The attained child selections therefore assemble into a legal selection of total budget K. CK3 gives its beta as the sum of the emitted gap and selected-child costs. If v_0 is unselected it lies in exactly one gap; CK1/IP1 give precisely that gap's alpha. If it is selected all outside mass is zero. NS handles exactly the remaining selections. This proves equality, not merely an abstract lower relaxation.

Record the minimizing anchor, selected-position path, gap entries and child/interval predecessors. They reconstruct an attaining original-graph selection for every finite output entry. No vertex is assigned an artificial candidate restriction in the final union of both flag rows.

### 7.2 Complexity of this ACTUAL decorated-cycle operator

Using S=O(N*M), all interval tables together take at most

```
O(ell^3*N*M^3*S^2)=O(ell^3*N^3*M^5) operations.        (CO2)
```

For the closing recurrence one anchor has O(ell*N*M) state keys. From each, try O(ell) next positions, O(N) gap budgets, O(N) selected-child budgets and at most O(M) root-mass outputs. Thus all anchors together use at most O(ell^3*N^3*M^2) operations. NS is smaller. Since ell<=N and M=ND, CO2 is bounded by

```
O(N^11*D^5) exact arithmetic operations per cycle.    (CO3)
```

These are deliberately loose uniform bounds, not performance measurements. The finite stage/state/choice bounds give a polynomial-in-(N,D) construction and bounded predecessor storage; no hidden enumeration of the 2^ell selected cycle masks remains.

The output alpha and beta have actual selection witnesses, so DG1 places them back on the true 1/D grid. There is no rounding from the temporary 1/(2D) root coordinate. This is a structural consequence of attainment and the even-cycle count, not a numerical divisibility test used as a fallback.

## 8. Integration on the whole cactus

**Theorem CA — WRITTEN; imports DG, CO, NS, I2's articulation law and the edge rule proved here. Scope:** every N-vertex simple connected unweighted cactus, every exact cardinality k, all original shortest paths and unrestricted sites. Let c_e count its EVEN cycle blocks and D=2^(c_e).

Root its standard block-cut tree. A singleton portal has only (k,epsilon,alpha,beta)=(0,0,0,0) and (1,1,0,0). For an edge from a new parent portal v to a child's root u, take any actual child entry of budget k_u and define w=(1-epsilon_u)+alpha_u. The edge output is

```
k=k_u+epsilon_v,
alpha=(1-epsilon_v)*w,
beta=beta_u+(1-epsilon_v)*w.                         (CA1)
```

Indeed v is a new leaf relative to this child; all old child shortest paths are unchanged. If v is unselected, its missed endpoint interactions sum to w; if selected, all its endpoint interactions are hit. Both parent flags are used. This proves the edge rule and attainment directly.

At a cycle block use CO with complete child profiles at its distinct vertices; its parent-portal child may be the singleton. Other blocks hanging at the same parent portal are merged by I2. For two components meeting only at v and agreeing on epsilon, the actual-budget form of that law is

```
k=k_H+k_J-epsilon,
alpha=alpha_H+alpha_J,
beta=beta_H+beta_J+alpha_H*alpha_J.                    (CA2)
```

The subtraction counts the shared selected portal exactly once. Equivalently their old a-indices add. Generate all compatible entry pairs, retain only minimum beta at identical resulting k,epsilon,alpha, and store one union witness. The one-portal law proves both sufficiency and attainment. Every operation builds the actual subcactus, so induction gives its COMPLETE attained pruned profile table, not a table on arbitrary freely prescribed masses.

At the whole-graph root, outside mass is zero. For any requested k take the smallest beta over BOTH flags and ALL alpha at that budget; return N(N-1)-2 beta. Backpointers supply an attaining size-k vertex set. All k=0,...,N are already computed; impossible conditional flag rows simply have no entries. This ends the optimization in the original unrestricted model.

There are O(N) blocks/merges in a cactus. Each profile has S=O(N^2 D) entries by DG. Pairwise articulation merging uses O(S^2) operations per merge, the edge rule O(S), and CO is bounded by O(N^11 D^5) per cycle. A safe whole-graph bound is therefore

```
O(N^12*D^5)=O(N^12*2^(5 c_e)) arithmetic operations.   (CA3)
```

All arithmetic has O(log N+c_e) bits up to constant factors by IP5/DG. Multiplying CA3 by a polynomial in this bit length bounds bit time. Finite predecessor tables and their reconstruction obey the same parameterized bound; no unbounded real arithmetic oracle or numerical tolerance is assumed.

**Exact consequences at this written scope:**

- For arbitrary c_e the algorithm is fixed-parameter tractable in the number of EVEN cycle blocks, with arbitrary numbers/lengths of odd cycles allowed.
- For c_e=0, D=1: every odd-cycle cactus, including arbitrary decorated odd cycles and arbitrary k, has a polynomial exact algorithm here. This is not merely a tree or single-cycle special case.
- For any fixed constant B and c_e<=B*log_2 N, D<=N^B, so the algorithm is polynomial in N, with an exponent depending on B.
- For unbounded c_e, D can be exponential. CA3 is NOT a polynomial-in-input-bit-length algorithm for general cacti, not a proof of polynomial complete envelopes there, and not a hardness result.

These are written algorithm/attainment theorems awaiting review, not executed checks or established priority claims.

## 9. Difference from the failed hardness route and remaining exact gap

The literal X/Y portal-forcing family remains defeated by the accepted v6 legal swap. No attempt is made here to resurrect it, promise fixed guards, manufacture arbitrary beta coefficients, or provide another raw 2^m-mass construction.

The new bridge is a TRUE variable-child cycle operator: TF's triangular correction replaces a potentially long memory of child masses by the two scalar mass fronts W,U, plus budget and the one linear output-portal statistic. Every child choice remains an actual recursively attainable unweighted-cactus state. The interval and cyclic recurrences prove construction/attainment, not only a bit-length or state-count observation.

The unresolved unparameterized issue is now sharply located: the mass grids in those same exact recurrences can have D=2^(c_e) positions. A polynomial-in-log D compressed representation or another bit-polynomial operator would settle the tractability branch; a different genuine selectable construction with an actual forcing proof could settle hardness. Neither is supplied. No exponential COMPLETE exposed envelope is claimed from grid size alone. CA is a partial complexity theorem in the same model, not a silent replacement of the target by odd cacti or small c_e.

## 10. Dated primary screen and assurance

The fresh public-primary search/read window is bounded by actual verbatim owner clocks **Sun Oct 25 08:25:29 PDT 2026** and **Sun Oct 25 08:29:02 PDT 2026**. Submitted queries were:

- `"group betweenness" "unicyclic"`;
- `"maximum betweenness centrality" "cactus" OR "geodetic" OR "even cycles"`;
- `"group betweenness" "cycle" "dynamic programming"`.

No matching exact classification or even-cycle-parameter theorem was located in those results. This does NOT certify openness or priority. Hits on single-node centrality, generic library routines, dynamic graph updates and unrelated group-labelled unicyclic problems do not match this optimization target.

The directly read [Puzis–Elovici–Dolev 2007 primary abstract, DOI 10.1103/PhysRevE.76.056709](https://pubmed.ncbi.nlm.nih.gov/18233792/) reports rapid successive group-centrality computation after preprocessing and use in finding prominent groups. Only the abstract was read; no cactus complexity statement is inferred from it. I6's exact objective and tree-DP theorem remain the already read primary baseline. The earlier Das cactus source, Camur–Vogiatzis survey, 2026 approximation-paper metadata/unread-body limit and OpenAI/math corpus nonmatches keep precisely their previous bounded scopes; they were not rerun or relabelled exhaustive.

**Target openness: UNCERTIFIED. Novelty: UNCLEAR.** The complete written recurrences above are independently reviewable mathematics but not specialist literature clearance. The cumulative nine entry screens/rejection log remain intact. Privacy keeps its separately accepted scoped result; cactus remains an unbound derived lead, not a new slot or primary cutover.

No scientific execution, replay, kernel check, nested agent, external model CLI/contact/publication, Git/deletion, frozen-file edit or other-root write occurred in this continuation. Only owned-root additive text/JSON, metadata and public source reading/searching were used. Parent erratum v9, the global HOLD, the unchanged deadline 2026-10-27T12:35:38-07:00 and new-science cutoff 2026-10-27T11:05:38-07:00 remain binding.
