# Cactus portal swaps: the literal hardness family fails, and one exact polynomial cycle-profile operator

Owner: InfoResearch96h-2, original slot info-1. Additive successor to replacement-information-primary-screen-v5-cactus-hardness-sketch-v1.md; no frozen predecessor is changed.

**Assurance: WRITTEN candidates, not executed mathematics.** No new formula below was evaluated by an interpreter, graph program, enumeration, symbolic package, solver or replay. No kernel check is claimed. The written counts, symbolic identities and algorithmic bounds are given explicitly. Metadata clocks/hashes, source reading and public-primary searches are the only tool execution in this continuation. Parent evidence erratum v9 was read completely before these new claims were recorded. The earlier withdrawn arithmetic receives no verification credit.

## 1. Target, imports and exact change of direction

The unchanged frozen target is every finite simple connected UNWEIGHTED cactus, every integer 0<=k<=n, unrestricted selectable vertices, and the endpoint-inclusive ordered objective

```
GBC_G(C)=sum_(ordered s!=t) sigma_st(C)/sigma_st, |C|=k.
```

Every shortest path is retained, including both arcs of an even-cycle tie. Equivalently, minimize the unordered missed mass

```
beta_G(C)=sum_(unordered {s,t}, s!=t) q_G,C(s,t),
GBC_G(C)=n(n-1)-2 beta_G(C),
```

where q is the fraction of the ORIGINAL graph's shortest paths avoiding C. Selecting a vertex DOES NOT delete it from the graph or recompute shortest-path distances.

Named imports used below:

- **I1, frozen target:** cactus-exact-target-and-state-freeze-v1.json, SHA-256 ed3b93ac9b102a4f3f828b9b6ca8ebfdb872484d577fb9add491b6cc98644983. Its disclosed freeze was not a pre-exploration preregistration.
- **I2, preceding mathematics:** replacement-information-primary-screen-v5-cactus-hardness-sketch-v1.md, 300 LF, SHA-256 5c961bb5115861285dec23a6519ad04e348e725657fd287e5d00f4a58d2459b8. Import its objective/state definitions, one-articulation factorization, literal Claim T graph, and conditional nature of the proposed reduction. No hardness theorem is imported.
- **I3, parent boundary:** run-root cactus-interface-ph7-new-cone-parent-v1.md, cactus portion only: the written compositional pieces were accepted at their named scope, not a complexity classification. In particular a fixture's z_F*s term is NOT a constant; its calibration correction must be retained.
- **I4, primary model ancestry:** [Fink–Spoerhase, Maximum Betweenness Centrality: Approximability and Tractable Cases, 2010](https://arxiv.org/html/1008.3503v1), problem definition and the shortest-path coverage representation in Section 2. Its Section 5 tree theorem is prior, not a theorem about the cycle operator proved here.

Every result below specifies its scope and imports. The general swap identity is elementary finite coverage algebra, not a novelty claim. The new substantive conclusions are the exact legal defeat of the literal X/Y family and an exact polynomial profile operator for ONE UNADORNED LEAF CYCLE. Neither result classifies arbitrary cacti. The hardness route using the literal branches is abandoned; the full target is NOT_SOLVED and remains an UNBOUND derived lead rather than a primary slot cutover.

## 2. Exact portal-swap identity, with both kinds of fixture contribution

**Claim SW — WRITTEN; imports I1/I2/I4. Scope:** a cactus formed by item branches H_1,...,H_r and an optional fixture F meeting pairwise ONLY at one common vertex v. The selection C does not contain v. Every item/fixture internal selection is kept except for one explicitly removed selected vertex u in one item. No site is forbidden, no guard promise is added, and k is unchanged.

For each item put C_i=C intersect V(H_i) and define

```
alpha_i=sum_(x in V(H_i) minus {v}) q_Hi,Ci(x,v),
beta_i=beta_Hi(C_i),
gamma_i=beta_Hi(C_i)-beta_Hi(C_i union {v}).              (SW1)
```

Thus gamma_i is exactly the mass of currently missed shortest paths INSIDE H_i that contain v, including endpoint pairs touching v. It is nonnegative and gamma_i>=alpha_i. Equality need not hold: some internal pairs can also use v. For the fixture write its corresponding alpha as z_F and its portal-hit loss as gamma_F. If F is absent, all its values are zero. Do NOT replace gamma_F by z_F without a separate graph-specific proof.

Let

```
S=sum_i alpha_i,
Q=sum_(i<j) alpha_i alpha_j,
Gamma=gamma_F+sum_i gamma_i.
```

The one-articulation shortest-path product law gives the ORIGINAL missed mass

```
beta_G(C)=beta_F+sum_i beta_i+Q+z_F*S.                  (SW2)
```

The beta_i and beta_F include their pairs touching v. Such pairs belong to exactly one branch and are not duplicated. Q and z_F*S count distinct-branch pairs; all shortest paths of such a pair pass through v, and their avoidance fractions factor.

Choose u in C_i and define its FULL internal loss when undone AFTER the portal is selected:

```
L_i^v(u)=beta_Hi((C_i minus {u}) union {v})
         -beta_Hi(C_i union {v}) >=0.                 (SW3)
```

First adding v reduces the missed mass by Gamma+Q+z_F*S. Then removing u restores L_i^v(u), and nothing outside H_i: all cross-branch paths still contain selected v. Therefore the LEGAL equal-budget swap C'=(C minus {u}) union {v} satisfies the exact identity

```
beta_G(C')-beta_G(C)=L_i^v(u)-Gamma-Q-z_F*S.            (SW4)
```

The portal is counted once globally: before the swap |C|=sum_i |C_i|+|C_F|, and afterwards one internal selection is removed and the single shared portal is added. Changing the portal flag in several local descriptions does not charge several vertices.

### 2.1 Why the cost of undoing u cannot be suppressed

**Claim SW-U — WRITTEN; imports SW and its definitions. Scope:** the same actual graph and actual selections, not an arbitrary assignable state pair.

If one instead undoes u FIRST while leaving v unselected, put

```
D_i=beta_Hi(C_i minus {u})-beta_i,
delta_i=alpha_Hi(C_i minus {u})-alpha_i,
gamma_i^-=beta_Hi(C_i minus {u})
          -beta_Hi((C_i minus {u}) union {v}).
```

Then D_i,delta_i are nonnegative. The undo-first cost in the WHOLE graph is

```
D_i+delta_i*(S-alpha_i+z_F).
```

When v is subsequently selected its removal of cross mass includes

```
Q+delta_i*(S-alpha_i)+z_F*(S+delta_i),
```

and its internal removal is Gamma-gamma_i+gamma_i^-. Subtracting gives

```
D_i-(gamma_i^--gamma_i)-Gamma-Q-z_F*S.
```

The first two terms are exactly L_i^v(u), by expanding their definitions. Thus (SW4) has retained the undo loss, not set it to zero. The delta_i*z_F terms cancel only because the final selected portal kills ALL fixture-to-item paths. The original z_F*S remains in (SW4).

If alpha_i=A_i+a_i*b_i and s=sum_i a_i*b_i, this fixture contribution is

```
z_F*S=z_F*sum_i A_i+z_F*s.
```

Only the first summand is constant over the Boolean choices. The second is selection-dependent.

## 3. The literal branch: exact losses, and a legal portal swap in BOTH states

**Claim LT — WRITTEN; imports I2 Claim T and SW. Scope:** precisely the following literal unweighted branch H_m, m>=2; no unmentioned private payload/forcing attachments are present. Any unchanged external cactus may be glued ONLY at its portal.

Vertices are ports v_0,...,v_m, two arms a_j,b_j per square, a terminal leaf l at x=v_m, and a dummy leaf d at v=v_0. Square j has edges v_(j-1)-a_j-v_j and v_(j-1)-b_j-v_j. There are 3m+3 vertices. The two actual size-(m+1) selections from the preceding packet are

```
X={a_1,...,a_m,x},
Y={a_1,...,a_m,d}.
```

Both leave v unselected. The word “guard” denotes vertices in these particular candidate sets; it is NOT an input restriction. The competitors below are legal in the completely unrestricted vertex set.

Put e=2^(-m). For a bare t-square chain with its a-arms selected, its portal mass P_t obeys

```
P_0=0,
P_t=3/2+(1/2)P_(t-1),
P_t=3(1-2^(-t)).                                     (LT1)
```

The first square contributes b_1 with mass 1 and v_1 with mass 1/2, and multiplies every deeper contribution by 1/2. The terminal port has mass 2^(-t). Selecting that port removes its portal contribution and blocks the attached terminal leaf. Thus, as in I2,

```
alpha_X=4-4e,
alpha_Y=3-2e.                                        (LT2)
```

### 3.1 Portal-hit mass gamma must distinguish X from Y

In X the dummy d is UNSELECTED. Every positive internal avoiding path through v either has endpoint d or, if neither endpoint is d or v, would have to use both first-square arms a_1,b_1 and hence selected a_1. The latter paths have zero avoidance. Endpoint-v pairs contribute alpha_X. Dummy-to-other pairs contribute alpha_X-1, since q(d,v)=1. Consequently

```
gamma_X=2 alpha_X-1=7-8e.                             (LT3)
```

In Y the dummy d is SELECTED. Its pairs already have zero avoidance. The same selected a_1 excludes every other positive internal path through v, so only endpoint-v pairs remain:

```
gamma_Y=alpha_Y=3-2e.                                (LT4)
```

In particular gamma_Y is NOT 2 alpha_Y-1. Treating the dummy as unselected in both candidates would give a wrong swap conclusion.

### 3.2 X: undo the FIRST ARM, retaining its positive beta loss

Add v to X, then undo a_1. This preserves the original cardinality m+1 after the swap. With v selected, any restored path containing a_1 must have a_1 as an endpoint, since the other neighbor of a_1 besides v_1 is selected v.

- Its pair with b_1 has TWO original length-two shortest paths. Only the path through unselected v_1 avoids v, so its restored fraction is 1/2.
- Its pairs to the lower chain rooted at v_1 use the direct edge a_1-v_1 on every shortest path. Including endpoint v_1, their restored mass is 1+alpha_lower.
- Its pairs with v or d have zero avoidance because they contain selected v. Every other remaining selected arm and selected x also contributes zero.

The lower chain has m-1 squares, all its a-arms and terminal x selected. Its attached leaf l is blocked by x. By (LT1),

```
alpha_lower=3(1-2^(-(m-1)))-2^(-(m-1))=3-8e.
```

Hence the EXACT, NONZERO undo loss is

```
L_X^v(a_1)=1/2+1+alpha_lower=9/2-8e.                  (LT5)
```

Subtracting (LT3), not discarding (LT5), gives

```
L_X^v(a_1)-gamma_X=-5/2.                             (LT6)
```

For completeness the uncancelled undo-first quantities are also exact. Undoing a_1 with v unselected changes the portal mass by 3-4e, leaving alpha^-=7-8e. Now both a_1 and b_1 are unselected; their pair has an additional root-containing fraction 1/2. Dummy pairs still contribute alpha^--1. Therefore gamma^-=2 alpha^--1+1/2=27/2-16e, and SW-U gives D=L+(gamma^--gamma)=11-16e.

### 3.3 Y: replace the selected dummy leaf by its neighbor v

For Y use u=d, not a_1. After selecting v, undoing d restores NO path: every shortest path containing the leaf d and another endpoint contains its neighbor v. Thus

```
L_Y^v(d)=0,
L_Y^v(d)-gamma_Y=-(3-2e).                             (LT7)
```

Undoing d FIRST is not costless. It has D=4-2e, delta=1, and gamma^-=7-4e, so D-(gamma^--gamma_Y)=0, exactly as SW-U requires.

The full local table is therefore:

| actual state | vertex undone | alpha | gamma | raw undo loss D, v unselected | delta | gamma^- | loss L after selecting v | L-gamma |
|---|---|---|---|---|---|---|---|---|
| X | a_1 | 4-4e | 7-8e | 11-16e | 3-4e | 27/2-16e | 9/2-8e | -5/2 |
| Y | d | 3-2e | 3-2e | 4-2e | 1 | 7-4e | 0 | -(3-2e) |

This table is a written symbolic derivation, not an executed check or finite enumeration.

### 3.4 Full star-of-items domination, retaining the fixture

**Corollary LF — WRITTEN; imports SW, LT and nonnegativity of path masses. Scope:** any nonempty collection of literal H_(m_i) branches, m_i>=2, sharing v; any fixed internal selection in any additional fixture glued only at v; any normalized mixture C_i in {X_i,Y_i}, with v unselected.

Choose any one item i and perform the legal swap specified in the table. All other vertices remain selected or unselected exactly as before. The exact WHOLE-GRAPH changes are

```
X_i: Delta beta=-5/2-sum_(j!=i) gamma_j-gamma_F-Q-z_F*S,
Y_i: Delta beta=-(3-2e_i)-sum_(j!=i) gamma_j-gamma_F-Q-z_F*S.
                                                               (LF1)
```

Every displayed outside term is nonnegative before its minus sign. Since e_i<=1/4, 3-2e_i>=5/2. Each normalized mixture is therefore strictly beaten by a legal same-k selection, with beta decreased by at least 5/2 and ordered GBC increased by at least 5. The positive loss from undoing a_1 in an X item was explicitly retained; every fixture cross term z_F*S and internal portal-hit term gamma_F is included.

No such normalized mixture can be a global optimizer. A lossless optimum-preserving normalization of this literal family to these states with v unselected is impossible. Adding ANY fixture only at v cannot rescue it: that fixture can only add the nonnegative quantities in (LF1).

This is a negative result about the literal proposed family, NOT a theorem that every imaginable cactus item is portal-dominated. An attachment inside a branch, or an entirely different selectable item, changes its gamma and L and needs a new proof. In particular private payloads cannot be declared harmless calibration devices.

The two-line crossover in I2 remains true at fixed unselected-portal interface. The swap changes the portal flag and decreases the internal selection count by one. Therefore LF does NOT prove either line is absent from the restricted F_(a,0) envelope. It defeats their use for unrestricted-site optimum forcing, not all fixed-row boundary complexity.

## 4. Corrected calibration identity and why the literal hardness route stops

**Claim CAL — WRITTEN CONDITIONAL ALGEBRA; imports SW2 and I2 Section 6 only. Scope:** actual two-choice branches, IF realized, with alpha_i=A_i+a_i*b_i and beta_i=B_i+c_i*b_i, b_i in {0,1}; one fixed fixture with unselected-portal mass z_F. No graph realization or forcing is asserted.

To obtain beta_total=K_F+(s-tau)^2/2, s=sum_i a_i*b_i, the necessary coefficient in this template is

```
c_i=a_i^2/2-tau*a_i-a_i*sum_(j!=i) A_j-z_F*a_i,        (CAL1)
K_F=beta_F+sum_i B_i+sum_(i<j) A_i*A_j
    +z_F*sum_i A_i-tau^2/2.                           (CAL2)
```

Indeed expansion of SW2 gives the Boolean linear coefficient c_i+a_i*sum_(j!=i)A_j+z_F*a_i and the cross coefficient a_i*a_j. Substitution of CAL1 leaves a_i^2/2-tau*a_i as the linear coefficient; using b_i^2=b_i yields the square. This explicitly corrects the fixture omission in the earlier conditional template. It does not silently edit that frozen source.

In the preceding SUBSET-SUM scale, s and tau lie in [0,delta*W] with delta*W<1. Thus a calibrated normalized candidate would satisfy beta<K_F+1/2. If it were also one of the literal mixtures in LF, its legal portal alternative would satisfy beta<K_F-2. Hence a threshold at K_F could not implement the intended Boolean test: that alternative lies strictly below threshold irrespective of equality. This is a CONDITIONAL incompatibility check, not a claim that CAL1 was ever realized by the literal branches.

**Route disposition:** the literal many-tie X/Y star is a DEAD END for the intended unrestricted-site optimum-forcing/hardness route. No NP-hardness conclusion is made. The next work below attacks an exact polynomial cycle-profile operator instead of inventing another raw dyadic-mass family or promising fixed guards.

## 5. Exact polynomial operator for one unadorned leaf cycle

**Theorem LC — WRITTEN; imports I1/I2 for the one-portal objective/state convention, plus the elementary two-arc geometry of a simple unweighted cycle proved below. Scope:** H is EXACTLY a simple cycle of length ell>=3, rooted at portal v, with NO child subcacti or nontrivial attached masses at its other vertices. It may be attached to an arbitrary outside cactus only at v. Every k from 0 to ell and both portal flags are handled. This is a complete operator for this leaf block, NOT for a general decorated cycle or arbitrary cactus.

Here k counts ALL selected cycle vertices, including v if selected. Convert to the old internal-budget convention by a=k-epsilon, epsilon=1_(v selected); the portal is never charged twice.

For a selection containing at least one cycle vertex, the unselected vertices form cyclic gaps of consecutive unselected vertices between selected vertices. A gap may be empty. For two unselected vertices in DIFFERENT gaps both cycle arcs encounter a selected vertex, so q=0. For two in the SAME gap let d be their distance along that gap. Then

```
q=1    if d<ell/2,
q=1/2  if ell is even and d=ell/2,
q=0    if d>ell/2.                                   (LC1)
```

This keeps the ORIGINAL shortest paths: a longer unselected arc is not counted when the shorter arc contains a selected vertex. At a tie precisely one arc avoids the nonempty selected set, so the fraction is exactly 1/2. No one-arc surrogate is used.

### 5.1 Exact gap cost and balanced residual gaps

Put h0=floor((ell-1)/2). For 0<=r<=ell-1 define

```
f_ell(r)=sum_(d=1)^(min(r-1,h0)) (r-d)
         + (1/2)*max(r-ell/2,0)  if ell is even,
f_ell(r)=sum_(d=1)^(min(r-1,h0)) (r-d)
                                           if ell is odd.      (LC2)
```

An empty sum is zero, including r=0,1. This is the EXACT missed mass of one length-r gap. There are r-d unordered pairs at within-gap distance d, which proves (LC2) from (LC1). The graph's missed mass is the sum of its gap costs.

**Lemma LC-B — WRITTEN; imports LC1/LC2 only. Scope:** minimum cost of j nonnegative integer gap lengths summing to s, with 0<=s<=ell-1.

The forward differences of f are nondecreasing. More explicitly,

```
ell=2h+1: f(r+1)-f(r)=min(r,h),
ell=2h:   f(r+1)-f(r)=r             for 0<=r<=h-1,
                              =h-1/2         for r>=h.         (LC3)
```

These follow by adding one endpoint to the finite sums in LC2. If two gaps have lengths p>=q+2, shifting one vertex from p to q changes the cost by

```
[f(q+1)-f(q)]-[f(p)-f(p-1)]<=0.
```

Repeating this exchange reaches a balanced composition and never increases cost. Thus, with q=floor(s/j) and t=s-j*q,

```
D_j(s)=(j-t)*f_ell(q)+t*f_ell(q+1),  j>=1.             (LC4)
D_0(0)=0; D_0(s)=+infinity for s>0.
```

This supplies an exact closed-form residual-gap minimum, not an exponential search. It asserts existence of a balanced optimum, NOT uniqueness or that every optimum is balanced when the differences have a linear plateau.

### 5.2 Exact portal mass in its gap

For u>=0 put

```
A_ell(u)=min(u,h0)+(1/2)*1_(u>=ell/2) if ell is even,
A_ell(u)=min(u,h0)                    if ell is odd.   (LC5)
```

If v is unselected and lies at offset t, 0<=t<r, in its length-r gap, its exact portal mass is

```
alpha=A_ell(t)+A_ell(r-1-t).                          (LC6)
```

Vertices outside this gap have zero avoidance to v; vertices to its two sides are counted by their within-gap distances according to LC1. Formula LC6 includes neither v itself nor any selected vertex.

### 5.3 Complete profile table, attainment and complexity

For fixed k,epsilon let B_(ell,k,epsilon)(alpha) be the minimum beta among selections of that budget/flag and exactly that alpha; an unattainable entry is +infinity. For 1<=k<=ell-1 and epsilon=0 the exact table is

```
B_(ell,k,0)(alpha)
 =min { f_ell(r)+D_(k-1)(ell-k-r):
          1<=r<=ell-k, 0<=t<r,
          A_ell(t)+A_ell(r-1-t)=alpha }.               (LC7)
```

Every selection supplies its portal gap r,t, with k-1 other gaps summing to ell-k-r. LC4 lower-bounds their cost, proving one direction. Conversely take any r,t in LC7 and balanced other gaps realizing LC4. Place the k selected vertices successively around the cycle between these gaps, with v at offset t in its designated gap. This realizes a legal selection with exactly the stated beta and alpha. For k=1, D_0 forces r=ell-1, as required. Thus no unattained abstract state is inserted.

For epsilon=1 and 1<=k<=ell, the only alpha is zero and

```
B_(ell,k,1)(0)=D_k(ell-k).                            (LC8)
```

Fix v as one of the selected gap separators and realize balanced gap lengths around it. Their sum is ell-k, so this also gives an actual selection. All other alpha entries are impossible.

The remaining boundary rows are exact:

```
k=0, epsilon=0: alpha=ell-1, beta=ell*(ell-1)/2;
k=0, epsilon=1: impossible;
k=ell, epsilon=0: impossible.
```

Every beta and alpha is a half-integer. For a fixed k,epsilon there are at most 2ell-1 possible alpha values in [0,ell-1]. Keeping only the smallest beta at each alpha is valid for EVERY nonnegative outside mass z, since the outside contribution is z*alpha. Hence the COMPLETE leaf-cycle affine profile is exactly

```
F_(a,epsilon)(z)
 =min_alpha [B_(ell,a+epsilon,epsilon)(alpha)+z*alpha]. (LC9)
```

The table has O(ell^2) entries over all budgets/flags and at most O(ell) candidate lines at each budget/flag. The finite sums for all f_ell values need at most O(ell^2) rational operations; LC4 then needs constant many integer/rational operations per query. Enumerating the triples k,r,t in LC7 and taking exact minima costs O(ell^3) operations in total. All numbers have denominator dividing 2 and numerator O(ell^2), so bit lengths are O(log ell). Retaining each minimizing r,t and balanced residual lengths reconstructs an actual optimum for every finite profile entry.

These are WRITTEN algorithmic bounds and an attainment proof. No implementation was run or supplied as verification. The polynomial bound is for THIS EXACT leaf-cycle operator, not an announced full-cactus algorithm.

## 6. What the polynomial front now contains, and the genuine remaining obstruction

**Claim PF — WRITTEN scope statement; imports LF and LC, with I2's accepted articulation/cycle formulas.**

1. The literal hardness item family is rigorously pruned ACROSS portal-flag/internal-budget rows in an unrestricted global optimization. Its raw dyadic precision and two-line crossover do not survive as an optimum-forcing argument.
2. Every unadorned leaf-cycle profile is computed exactly by LC7–LC9, uniformly in its length, budget and even-cycle ties. This is an actual polynomial compression/attainment theorem for that block, not another count of raw states.
3. General cactus blocks can have nontrivial child-state masses w_i and child beta costs. Their cycle interaction is the accepted sum of h_ij*w_i*w_j; replacing these varying masses by 1 would be an invalid narrowing. LC2's length-only gap cost and LC4's exchange proof do not apply to arbitrarily varying child choices.
4. Across many even cycles the global interface alpha can have fine dyadic denominators. Neither LC nor the swap certificate bounds the COMPLETE fixed-row envelope for all decorated subcacti. The accepted exact composition remains potentially exponential.

The next exact gap is a polynomial optimization/compression theorem for the decorated-cycle operator with its genuine child-state choices, OR a different unrestricted selectable hardness construction that passes SW before calibration. There is no full-target classification, unrestricted forcing theorem for another family, exponential exposed-envelope construction, formal/kernel/human/cross-vendor acceptance, or novelty clearance here.

## 7. Dated primary search boundary and cumulative selection status

Actual owner clock bounds for the fresh queries/read window were **Sun Oct 25 07:53:07 PDT 2026** and **Sun Oct 25 07:55:21 PDT 2026**, verbatim /bin/date observations. Individual query timestamps are not invented. Queries actually submitted were:

- `"maximum group betweenness" "cycle" exact algorithm`;
- `"group betweenness" "cactus" "dynamic programming"`;
- `"maximum betweenness centrality" "swap" "tree"`.

These returned the 2010 primary paper and ordinary/library centrality or unrelated cactus-group results; no matched exact arbitrary-cactus classification was located. That is a bounded search report, NOT a proof of openness. Library endpoint conventions and their code were not imported as this objective.

The primary paper's actual problem definition, Section 2 path-coverage ancestry and selected Section 5 tree-DP body were reread. Its result is a polynomial algorithm on TREES; its integer top-node state is not a proof of the decorated-cycle operator. The new leaf-cycle argument has standard gap decomposition/discrete-convex ancestry and receives NO priority claim.

The cumulative [Das 2014 cactus source](https://arxiv.org/pdf/1408.4005), [Camur–Vogiatzis 2024 survey](https://arxiv.org/html/2401.05235v3), 2026 approximation metadata/body-access limitation, and OpenAI/math local/current-remote nonmatches remain exactly the scoped records in v4/v5. They were not reclassified as an exhaustive new corpus audit. **Target: UNCERTIFIED_OPEN; NOVELTY_UNCLEAR.**

The nine earlier original entry screens and rejection log remain cumulative, not nine fresh problems. Privacy keeps its separately accepted scoped written deliverable. Cactus is still an unbound derived lead with no primary cutover, new owner/slot, new GO or executable task. Global HOLD, parent errata, the unchanged deadline and the new-science cutoff remain binding.

Delivered new written result: exact full-loss/full-fixture portal-swap identity; strict same-k portal defeat of every normalized literal X/Y mixture; corrected fixture calibration; and a complete polynomial exact leaf-cycle profile operator with attainment for all budgets/flags/ties. All stronger acceptance and general-cactus complexity claims remain explicitly unmade.
