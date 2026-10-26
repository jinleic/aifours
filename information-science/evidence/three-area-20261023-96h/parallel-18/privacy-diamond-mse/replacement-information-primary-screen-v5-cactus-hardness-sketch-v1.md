# Cumulative v5 — exact cactus target, compositional state, and a many-tie hardness sketch

Actual metadata clock before creation: **Sun Oct 25 06:55:15 PDT 2026** (`/bin/date`). InfoResearch96h-2. **WRITTEN CANDIDATE / HARDNESS SKETCH, not an NP-hardness theorem or a polynomial algorithm.**

The exact target/state was frozen first in `cactus-exact-target-and-state-freeze-v1.json`, SHA256 `ed3b93ac9b102a4f3f828b9b6ca8ebfdb872484d577fb9add491b6cc98644983`, actual clock06:48:23 PDT. Its exposure record expressly discloses prior private written exploration; this is NOT preregistration. No scientific execution occurred.

This ONE cumulative successor binds v4, `replacement-information-primary-screen-v4.md`, SHA256 `68cf8f5a4ac3c0a2c5c777521ad4d85f7be3c86b4c2d46c6c24ffeaf36193782` (106LF), and retains all nine book-entry screens and earlier rejections. The graph problem is the explicit DERIVED NET439 subproblem, not the whole printed article and not a tenth book entry. Ownership/root/slot remain unchanged. The parent has authorized this written continuation, not a solver, numerical experiment or primary cutover.

## 1. ONE exact target — no fixed-k, odd-cycle or unique-path escape

Input: EVERY finite simple connected undirected UNWEIGHTED cactus graph G=(V,E), n>=2, and an arbitrary integer0<=k<=n. A cactus has each block an edge or simple cycle. Cycle lengths, number of cycles and positions of all selected vertices are unrestricted.

For distinct s,t let sigma_st count ALL shortest s-t paths and sigma_st(C) count those meeting C at least once, INCLUDING endpoints. The objective is

```
GBC_G(C)=sum_(ordered s!=t) sigma_st(C)/sigma_st.
```

Required output is an EXACT maximizing k-vertex set. A polynomial algorithm must have polynomial TOTAL bit time in the input, not merely a polynomial number of arithmetic operations on exponentially large tables. The corresponding decision input includes an explicitly binary-encoded rational threshold B and asks if some k-set has GBC>=B.

This is the endpoint-counting objective of the directly read [Fink–Spoerhase primary](https://arxiv.org/html/1008.3503v1),20-Aug2010. The book link is 苏森、李勇辉、阎冬, **复杂网络中关键节点集合的确定**, printed439–441/PDF460–462, with the explicit group-betweenness specialization at440. Its images/pins are in v4. The prior general hardness, baseline approximation and exact TREE algorithm are not new results here.

Define the avoidance fraction

```
q_H,C(x,y)= #{shortest H paths x--y avoiding C}
            / #{ALL shortest H paths x--y}.
```

For a selected endpoint it is zero. When a zero-length boundary path is needed, define q(v,v)=1 if v is unselected and0 otherwise. Define the UNORDERED missed mass

```
Beta_G(C)=sum_({x,y} subset V, x!=y) q_G,C(x,y).
```

Then `GBC_G(C)=n(n-1)-2*Beta_G(C)`. Minimizing Beta with exact cardinality is therefore EXACTLY the frozen objective, not an approximation, connectivity surrogate or weighted input variant.

## 2. The precise state and exact merge theorem

**Claim S — NEW WRITTEN, imports only elementary shortest-path decomposition at an articulation and the standard bipartite block-cut tree. No machine check.**

Let H be an entire rooted subcactus attached to the rest ONLY at portal v. For a selection C in H retain

```
a=|C intersect(V(H) minus{v})|,
epsilon=1_(v in C),
alpha_H(C)=sum_(x in V(H) minus{v}) q_H,C(x,v),
beta_H(C)=Beta_H(C).
```

The graph size is known structural data, not a freely tunable state. Portal cost is counted once. The naive exact table is the achievable rational pairs `(alpha,beta)` at each `(a,epsilon)`. For a one-portal completion, the relevant affine profile is

```
F_H,a,epsilon(z)=min_C [beta_H(C)+z*alpha_H(C)], z>=0.    (S1)
```

Here z is outside avoidance mass, not a numeric sample chosen to suit a proof. In a finite N-vertex completion it is at most N. Lower-envelope compression for all nonnegative z is sufficient, but failure at an unattainable z alone would not establish computational hardness.

### 2.1 Articulation composition is exact

Suppose H and K meet only at v, their edges are disjoint, their selections agree on epsilon, and no other connection joins their interiors. A shortest path from x in H\{v} to y in K\{v} is a shortest x-v path in H followed by a shortest v-y path in K. All combinations occur, so both total and avoiding path counts multiply. A positive-length detour into the other side cannot improve an internal shortest path, because it must return to v.

Thus, with matching portal flags,

```
alpha_(H union K)=alpha_H+alpha_K,
beta_(H union K)=beta_H+beta_K+alpha_H*alpha_K.          (S2)
```

If v is selected, both masses alpha vanish and cross pairs are already hit, so the same equation applies. Repeating gives the analogous sum over all child pairs. Budgets add after counting the shared portal once. This proves that `(a,epsilon,alpha,beta)` contains EXACTLY the needed one-portal interaction information; it is not merely a heuristic state.

For fixed outside selection, beta_K is constant and the H-dependent objective is beta_H+alpha_K*alpha_H. Hence states dominated in both alpha and beta can be pruned. More generally only states exposed by attainable nonnegative outside mass need survive. An exponential number of raw masses is therefore NOT automatically an exponential lower envelope.

### 2.2 The full cycle-block operator, including ties

Let a cycle block have vertices v0,...,v_(ell-1), parent portal v0, and rooted attached subcacti H_i at v_i, allowing the trivial H_i={v_i}. Let epsilon_i record whether the cycle vertex is selected, and let alpha_i,beta_i be the attached states. Set

```
w_i=(1-epsilon_i)+alpha_i.
```

For distinct i,j let h_ij be the fraction of shortest v_i-v_j ARCS IN THE CYCLE that avoid selected cycle vertices. It is0,1/2 or1: an unweighted cycle has one shortest arc except at antipodal pairs in an even cycle, where there are exactly two. Endpoints are included.

All shortest paths between different attachments are Cartesian products of a child path, a shortest cycle arc and another child path. Therefore

```
beta_total=sum_i beta_i+sum_(i<j) h_ij*w_i*w_j,
alpha_total=alpha_0+sum_(i>=1) h_i0*w_i.                 (S3)
```

The selection count excluding v0 is `sum_i a_i + sum_(i>=1)epsilon_i`. The root flag is epsilon_0. No path through an unrelated descendant block shortens the cycle arc; otherwise the block-cut decomposition would not have the stated one-block attachments.

Equations(S2)–(S3) specify an exact, possibly exponential, dynamic program over ALL legal selections. They do not prove a polynomial number of states or polynomial cycle-pattern processing. Both obligations would be required for the requested compression branch. I choose the alternative HARDNESS-SKETCH branch below instead of asserting an unproved state-count theorem.

### 2.3 Exact bit lengths are not the same as state counts

For a cactus with c cycles, a selected-set avoidance fraction along any block route is either0 or a product of at most c factors1/2; unique surviving/blocked arcs contribute1/0. Hence alpha and beta are dyadic rationals with a common denominator dividing2^c and numerators bounded by the respective vertex/pair counts times2^c. Their individual bit lengths are polynomial in graph size.

This WRITTEN observation licenses exact rational notation in the state; it does NOT license enumerating every possible dyadic numerator. An exponentially fine denominator can still support exponentially many small-bit states.

## 3. An actual fixed-budget family with exponentially many raw portal masses

**Claim R — NEW WRITTEN exact family, not a Pareto/envelope or hardness theorem.**

For every m>=1 form a chain of m squares. Square i has opposite portals v_(i-1),v_i and arms a_i,b_i, with edges

```
v_(i-1)--a_i--v_i,  v_(i-1)--b_i--v_i.
```

Attach one leaf l_i to a_i. Consecutive squares share just their portal, so this is a simple unweighted cactus with4m+1 vertices. Root it at v0.

For epsilon in{0,1}^m select a_i if epsilon_i=0 and b_i if epsilon_i=1. Exactly m vertices are selected and v0 is unselected. These are ACTUAL legal selections, not virtual weights.

A shortest v_i-v0 path has one choice per earlier square. Exactly one choice at each square avoids its selected arm, so its avoidance fraction is2^(-i). The unselected arm at square i has avoidance fraction2^(-(i-1)): its shortest route goes to the upper portal, not around the other side of the square. The selected arm contributes zero. Leaf l_i contributes zero when a_i is selected and2^(-(i-1)) otherwise. Consequently

```
alpha(epsilon)=3*(1-2^(-m))
               +sum_(i=1)^m epsilon_i*2^(-(i-1)).        (R1)
```

Multiplying the variable part by2^(m-1) gives the distinct binary integers with digit weights2^(m-i). Thus there are EXACTLY2^m distinct raw alpha values at ONE fixed `(a=m,epsilon_portal=0)` budget/flag. An algorithm storing a separate entry for every feasible portal mass has exponentially many entries on this family.

No arithmetic interpreter, graph program or Boolean enumeration establishes this claim. The argument holds for every m by the displayed shortest-path bijection and binary uniqueness.

### 3.1 Essential negative control: this is NOT an exponential frontier

The family in ClaimR alone is NOT a hardness reduction. In fact its other states in this chosen family are dominated by its all-zero choice.

Remove the pendant leaves and call the resulting square chain the base graph. Its missed mass on base-base pairs is a constant beta_base independent of which arm is selected: independently swapping the two arms of each square is an automorphism fixing the portals. A leaf adjacent to a selected a_i has zero avoidance fraction to every other vertex. An active leaf (epsilon_i=1) has a positive summed interaction L_i with base vertices, independent of other arm choices after that base symmetry.

For active leaves i<j, the shortest path uses the unique own-square segments and the intermediate j-i-1 squares; hence their avoidance fraction is2^(-(j-i-1)). It follows EXACTLY that

```
beta(epsilon)=beta_base+sum_i L_i*epsilon_i
 +sum_(i<j)2^(-(j-i-1))*epsilon_i*epsilon_j,
L_i>0.                                                    (R2)
```

Every variable term is nonnegative and some linear term is positive if epsilon is nonzero. Both alpha and beta then exceed their all-zero values. So the raw2^m states can collapse to ONE state within this subfamily under dominance. This explicitly prevents the false inference “many tied paths => exponential relevant profile => NP-hard.”

The full legal selection space is even larger. No statement that the two-vector frontier or F in(S1) has exponentially many pieces follows from ClaimR.

## 4. Binary mass payloads with only linearly many vertices

**Claim B — NEW WRITTEN encoding fact under an explicitly fixed guard selection, not a guard-forcing theorem.**

Use the same bare square chain, select every a_i as a guard, and attach a leaf to the UNSELECTED b_i exactly when a prescribed binary digit d_i is1. The portal mass is

```
alpha=3*(1-2^(-m))+sum_i d_i*2^(-(i-1)).                 (B1)
```

For a binary integer w with m digits ordered most significant first, the payload is `2^(-(m-1))*w`. Relative to the otherwise identical no-payload chain, arbitrary dyadic payloads therefore have graph descriptions of size O(m), not O(w). Taking m=M+1 encodes2^(-M)w; a leading zero digit is allowed.

This is a useful ingredient for a binary-weight reduction. It is NOT a selection switch, does not make the guards compulsory, and does not tune beta for free. The internal pair terms caused by payload leaves must still be counted. Treating(B1) as an arbitrary freely assignable `(alpha,beta)` pair would invalidate the original graph model.

## 5. An actual many-tie tradeoff selector, with an exact outside crossover

**Claim T — NEW WRITTEN two-selection comparison. Neither selection is asserted globally optimal among all legal selections.**

Take a bare m-square chain as above with m>=2 and fixed selected guards a_1,...,a_m. Put x=v_m, attach ONE leaf l to x, and attach ONE dummy leaf d to root v0. There are3m+3 vertices. Compare two legal selections of the SAME size m+1:

```
X={all a_i} union{x},
Y={all a_i} union{d}.
```

In both, the portal v0 is unselected. Write e=2^(-m). The bare chain's portal mass is3(1-e); deleting the contribution of terminal x leaves prefix mass3-4e. Thus

```
alpha_X=4-4e, alpha_Y=3-2e,
alpha_X-alpha_Y=1-2e>0.                                 (T1)
```

Let B be beta when only the guards are selected, before selecting either x or d. The sum of avoidance fractions from x to the OTHER bare-chain vertices (including v0) is3(1-e), by reversing the chain's identical square factors. Selecting x removes:

- the x-prefix interactions and l-prefix interactions, two copies of that sum;
- the pairs x-d and l-d, each of fraction e;
- the pair x-l, of fraction1.

No other previously positive avoiding path is destroyed: an internal prefix-prefix path using x through the last square would already use selected a_m. Therefore its exact removed mass is7-4e.

Selecting d removes exactly its endpoint interactions. They have total1 plus the module portal mass, including x and l, namely4-2e. Hence

```
beta_X=B-(7-4e), beta_Y=B-(4-2e),
beta_Y-beta_X=3-2e>0.                                   (T2)
```

X has LOWER internal missed mass but HIGHER outside portal mass. The affine difference under completion mass z is

```
(beta_X+z*alpha_X)-(beta_Y+z*alpha_Y)
 =-(3-2e)+z*(1-2e).                                    (T3)
```

Its crossover is `(3-2e)/(1-2e)`, strictly above3 and at most5 for m>=2. Both sides of this comparison occur in genuine cactus completions: z=0 is the empty outside, and z=6 is six unselected leaves attached to v0. The preferred one of these TWO selections reverses between those completions.

This is an actual all-ties tradeoff, not the dominated switch in ClaimR. But a THIRD legal internal selection may beat both. The guards and the X/Y alternatives have not been forced in the full optimization. Thus(T3) is not a proof that both lines survive the COMPLETE envelope, still less that an exponential profile exists.

## 6. A precise conditional reduction template — the hardness SKETCH

This section states a logical reduction lemma conditional on an unproved GRAPH REALIZATION/FORCING specification. It does not assert that the specification has been achieved. Its purpose is to fix the exact equations a later many-tie construction must satisfy, rather than calling an abstract quadratic programme a graph reduction.

Start from SUBSET-SUM with positive binary integers w_1,...,w_r and target T in[0,W], W=sum w_i. Choose an integer M with2^M>W and set

```
delta=2^(-M), a_i=delta*w_i, tau=delta*T.
```

The scale is DYADIC, compatible with cactus avoidance probabilities, and has polynomial bit description. No numerical approximation is used.

### 6.1 Needed actual item and normalization specification

A later reduction would have to construct in polynomial size one cactus, with an ordinary exact cardinality budget, whose threshold-relevant selections normalize to one of TWO ACTUAL local choices b_i in{0,1} per item, with a common unselected portal. It must prove all of the following in the ORIGINAL unrestricted-site model:

1. Every fixed guard and exact per-item budget choice is enforced by the objective/cardinality or a proved lossless normalization; no “allowed candidate set” is added to the input.
2. A selection of the common portal or a different internal vertex cannot bypass the claimed threshold. The portal is not forbidden by definition.
3. At each item the actual rational state satisfies

```
alpha_i(b_i)=A_i+a_i*b_i,
beta_i(b_i)=B_i+c_i*b_i,
c_i=(a_i^2)/2-tau*a_i-a_i*sum_(j!=i)A_j.               (H1)
```

All A_i,B_i,c_i and threshold constants must come from ACTUAL shortest-path counts with polynomial descriptions. Beta remains nonnegative at each actual state; an abstract assignment of negative linear coefficients is not itself a gadget.

4. All extra fixture contributions are accounted for exactly, including all pairs touching the fixture, and the output is a simple unweighted cactus retaining every tied geodesic.

ClaimB supplies compact DYADIC MASS payloads under fixed guards. ClaimT supplies an ACTUAL direction of negative beta/positive alpha tradeoff under a fixed guard choice. Neither supplies(H1) or the forcing/normalization. Those are the literal unproved gadget steps, not minor wording repairs.

### 6.2 If that specification is achieved, the reduction algebra is exact

Let the item branches meet at the common portal. The articulation identity(S2) gives

```
beta_total=sum_i beta_i+sum_(i<j)alpha_i*alpha_j.
```

Using b_i^2=b_i only at Boolean choices, substitute(H1) and let s=sum_i a_i*b_i. All cross and linear terms combine into

```
beta_total=K+(s-tau)^2/2,                               (H2)
K=sum_i B_i+sum_(i<j)A_i*A_j-tau^2/2,
```

up to the EXACTLY declared constant fixture contribution. This is a written symbolic identity, not a program output. If a subset has sum T, then s=tau and beta=K. If not, the difference of the corresponding integer sums is nonzero, so |s-tau|>=delta and beta>=K+delta^2/2.

For an N-vertex output graph, the exact rational GBC threshold `N(N-1)-2K` would therefore distinguish equality from failure, with a gap at least delta^2 in the ordered objective. A complete binary reduction would also prove polynomial graph size and threshold bit length and, critically, the normalization conditions above.

**Current hardness status:** (H2) is proved CONDITIONAL algebra, while(H1) plus unrestricted-site/portal/guard forcing is NOT_PROVED. Thus this is a genuine many-tie hardness SKETCH with actual local mathematical core, not an announced reduction or NP-hardness theorem.

### 6.3 Why the obvious shortcuts are invalid

- Exponentially many raw masses from ClaimR are not exposed states; ClaimR's own dominance control refutes that shortcut.
- Polynomial bit lengths do not imply polynomially many distinct states; conversely a fine denominator does not by itself prove hardness.
- A fixed guard pattern is not an extra promise in the frozen target. It must be forced or normalized later.
- A root forbidden from selection, a marked candidate set, weighted vertices, one global item-consistency choice imposed from outside the graph, or a different value of k would change the problem.
- Crossover of two lines is not proof that either is on the full lower envelope.
- A purported reduction that first deletes one arc of every even cycle loses the very ties carrying its dyadic information.

The exact next mathematical gap is the ORIGINAL-model cost calibration and forcing, or a proof that these apparent tradeoffs always admit a polynomial compressed frontier. Neither branch is resolved by the present local constructions.

## 7. Dated public-primary search log and prior boundary

Search window is bounded by returned owner clocks **06:48:23–06:55:15 PDT,25-Oct2026**; no exact individual-query timestamp is invented. Queries actually submitted included:

- `"cactus" "group betweenness" "optimization"`;
- `"maximum betweenness centrality" "cactus" OR "tie" OR "treewidth"`;
- `"cactus graphs" "shortest path" "coverage" optimization hardness`.

No exact matching classification was located. Hits on ordinary single-node centrality, cactus plants/software, group estimation routines and graph-homomorphism hardness are not this target. A search miss does NOT certify openness or novelty.

Direct primary boundary retained:

- [Fink–Spoerhase2010](https://arxiv.org/html/1008.3503v1), exact GBC objective and the tree theorem. Its Section5 state definitions and unique-tree-path proof were freshly reread in this continuation. The tree's integer “top-node” count is prior; replacing it with alpha above and handling cycle ties are new candidate reasoning, not a claim that the tree theorem proves cactus compression.
- [Das2014 cactus paper](https://arxiv.org/pdf/1408.4005), actual full extracted contents read in v4: its listed shortest-path/domination/cover/colouring/tree/labelling tasks are not a k-group-betweenness optimizer. Its general graph decomposition ancestry is prior; no new invention of block-cut trees is claimed.
- [Camur–Vogiatzis2024 survey](https://arxiv.org/html/2401.05235v3), selected definitions/history/future-work scope read in v4. Its selective OR coverage is not proof of global absence.
- The June2026 approximation-paper metadata and unread publisher-body limitation from v4 remain explicit; no conjectured theorem is inferred from the title.

The v4 local/current-remote OpenAI/math checks found no matched group-betweenness/cactus optimizer. They are carried, not relabelled a new exhaustive corpus audit. No Lean/Comparator, graph code or finite certificate was replayed. **Target status remains UNCERTIFIED_OPEN; NOVELTY_UNCLEAR.**

## 8. Cumulative ownership and exact parkable result

Nine original entry screens remain cumulative: PG516, RC418, QPKE412, TEX533, HSP545, COV472, DH389, DEC394 and NET439; earlier PH/NIZK/DNA rejections and current-roster exclusions remain. No extra problem/owner count is created. The quasi-Hamiltonian lead is not promoted. The privacy result keeps its existing exact written support/assurance boundary; no scalar digits or old arithmetic are revisited.

Delivered NEW WRITTEN scope is:

1. one exact arbitrary-k/all-ties cactus target and precise state freeze;
2. exact articulation AND full cycle-block composition formulas;
3. an exponential raw-state family with a proved dominance negative control;
4. compact dyadic payload encoding under fixed guards;
5. an actual two-selection many-tie tradeoff with an exact completion crossover;
6. a conditional SUBSET-SUM square-gap reduction template and its complete literal realization/forcing obligations.

**Not delivered/claimed:** polynomial profile/state-count compression, an efficient cycle operator, exponential COMPLETE lower-envelope complexity, an unrestricted-site forcing theorem, exact cost calibration(H1), NP-hardness, a full optimizer, a finite search, formal/kernel/human/cross-vendor acceptance or novelty clearance. The remaining scientific gap is exact and substantial, not hidden under a numeric example.

All reasoning after the disclosed freeze is written. No scientific eval/interpreter, arithmetic program, enumeration, symbolic computation, graph package, solver, circuit, benchmark, replay, nested agent, external model CLI/contact/publication, Git, deletion or shared-root write occurred. Metadata clocks/hashes and public source reading/searching only. Global HOLD, parent errata and unchanged deadline remain binding.
