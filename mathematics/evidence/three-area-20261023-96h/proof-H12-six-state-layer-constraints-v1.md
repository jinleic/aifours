# H_{1,2}: all-topology necessary structure of a six-state representation

Before-creation clock observed: **2026-10-23T13:46:07-07:00**. Status: **CANDIDATE / NOVELTY_UNCLEAR**, written reasoning only. This develops the parent's explicit shortest-initial-to-exit-path lead; the lead is not retrospectively called an independently discovered six-state impossibility. No enumeration, scientific program or other new target is involved.

## 1. Exact scope and delivered structural lemma

Let a>c>0,b>0,d=a-c,beta=b/d and

    H(s)=K/D5(s), K=c(a^2+b^2)^2,
    D5(s)=(s+c)((s+a)^2+b^2)^2.

Suppose H has a PH representation(alpha,T) with exactly six transient states. Put w=-T1 and assume

    beta>1/sqrt3.

This includes the unresolved minimum6-versus7 band supplied by the new G7 construction.

**Candidate lemma L6.** Every such representation necessarily has all of the following properties:

1. T is irreducible and its characteristic polynomial is D5(s)(s+u) with u>c. No unreachable state, reducible parallel branch or reducible hidden-real-pole component can supply a residual six-state exception.
2. In its positive off-diagonal support graph, the shortest path from a positive initial state to a positive exit state has four edges. After ordering by distance from the initial support, the graph has one state in each layer0,1,2,3,4 and a single extra state in one layer ell in{0,1,2,3,4,5}. Thus it has either six singleton layers or exactly one doubled layer. Every edge advances at most one layer; backward and within-layer edges remain allowed.
3. Let lambda_i=-T_ii>c. For each omitted vertex m, let W_m be the total positive weight of all simple four-edge initial-to-exit paths omitting m, with weight alpha_(start) w_(end) times the product of off-diagonal rates. Let R5 be the corresponding total weight of all simple five-edge paths. Then

       sum_m W_m=K>0,
       K u=sum_m W_m lambda_m+R5.

   Thus the canceled real pole is not a free spectral parameter: it satisfies an exact positive-path identity.
4. Writing v=u-c and x_i=lambda_i-c>0, the standard trace constraints and the path identity become

       sum_i x_i=4d+v,
       sum_i x_i^2 <= 4(d^2-b^2)+v^2,
       v=sum_m (W_m/K)x_m+R5/K.

These are necessary all-topology restrictions, not a converse and not a universal six-state exclusion. The fixed new G7 band still has minimum6or7; no minimum7 claim follows from this lemma alone.

## 2. Binding the hidden eigenvalue and excluding untrimmed states

A six-state transform's reduced denominator D5 divides its monic characteristic polynomial, so

    det(sI-T)=D5(s)(s+u)

for some real u. Hurwitz stability gives u>0. Since beta>1/sqrt3>1/sqrt5, the already written-checked universal five-state trace obstruction rules out every representation of order at most5. If any state were unreachable from the positive initial support, deleting all unreachable states would preserve H and leave at most5 states, a contradiction. Hence every state is reachable.

Every transient PH state can reach a positive exit: otherwise its reachable set would contain a final communicating class with no absorption and row sums zero, giving an eigenvalue0, contrary to Hurwitz stability. Thus the representation is also co-reachable to w.

For completeness, positivity excludes a canceled dominant real mode. Let T_j be an irreducible diagonal block whose spectral abscissa rho equals that of T. Since the block is reachable and co-reachable, for any fixed t0>0 the restrictions to that block of alpha exp(Tt0) and exp(Tt0)w are nonnegative and not zero. The Metzler semigroup restricted to trajectories remaining within the block dominates exp(T_j t) entrywise. Perron–Frobenius for an irreducible Metzler matrix then gives

    f(t+2t0)>=C exp(rho t) for all sufficiently large t,

with some C>0. But the exact inverse H has asymptotic C' exp(-ct), with C'=K/(d^2+b^2)^2>0; its other terms are polynomial times exp(-at). Hence rho<=-c. Since -c is an eigenvalue, rho=-c and u>=c. This argument uses positivity/accessibility, not an unsupported assumption that every eigenvalue must be an observable pole.

## 3. Reducible six-state spectra cannot occur in this residual region

Every irreducible Metzler block has a real algebraically simple Perron eigenvalue, and the only real spectral values available are -c and -u. If T were reducible, it would have exactly two diagonal blocks, each containing one real eigenvalue. When u=c, algebraic simplicity likewise forces exactly two blocks. Their sizes must be(1,5),(3,3) or(5,1), since each remaining eigenvalue belongs to one of the two repeated conjugate pairs.

For a block with one real eigenvalue-r and ell conjugate pairs, irreducible Perron theory gives r<a, and shifting by r yields the same trace inequality as the exact-degree proof:

    b^2 <= (a-r)^2/(2ell+1).

Here r is c or u, and u>=c, so a-r<=d. For a5block, ell2 and beta^2<=1/5 follows. For two3blocks, ell1 in each and beta^2<=1/3 follows. Both contradict the present beta>1/sqrt3 assumption. Therefore T is irreducible. Its real Perron eigenvalue-c is algebraically simple, so u=c is impossible and u>c.

For a positive Perron vector h of irreducible T,

    -c=T_ii+sum_(j!=i)T_ij h_j/h_i.

Each row has a positive off-diagonal rate, so T_ii<-c, proving lambda_i>c for all six states.

## 4. Relative degree fixes the exact shortest path

The transform has expansion H(s)=K s^-5+O(s^-6). Its analytic density therefore satisfies

    f^(j)(0)=0 for j0,1,2,3,
    f^(4)(0)=K>0.

Choose a scalar Lambda large enough that B=T+Lambda I is entrywise nonnegative. Binomial expansion gives

    alpha B^j w=0 for j<4,
    alpha B^4 w=K,

because every term involving a lower T power vanishes. All summands of each B-walk expansion are nonnegative. Thus there is no positive walk from the initial support to the exit support with fewer than four steps, and there is one with exactly four. A diagonal step or a repeated vertex in such a walk would permit removal of that step/cycle and produce a shorter positive path, impossible. Therefore it is a simple four-edge path through five distinct states.

Let delta(i) be the shortest off-diagonal path distance from the positive initial support. Along a shortest initial-to-exit four-edge path, the distances are exactly0,1,2,3,4: any smaller intermediate distance would shorten the full exit path. Every reachable vertex has distance at most5 in a six-vertex graph. Only one vertex remains outside that chosen path. Hence its distance is one ell in{0,...,5}, producing exactly the layer alternatives in the statement.

For every positive edge i->j, delta(j)<=delta(i)+1. The initial support is exactly layer0, and positive exit vertices can occur only in layers4 or5. If a layer below4 is doubled, neither state in it can be an exit; if layer0 is doubled, both of its states are initially positive by definition. No acyclicity or forbidden backward edge has been smuggled into this reduction: strong connectivity requires backward routes and they remain in scope.

## 5. Positive simple-path numerator identity

For a real matrix T and off-diagonal graph weights, expansion of the resolvent cofactor gives the exact path identity

    alpha(sI-T)^-1w · det(sI-T)
      =sum_(simple paths P) alpha_(start) w_(end)
         (product of T edges along P)
         det[(sI-T) restricted to vertices outside P].

A direct permutation-expansion proof is available: a cofactor permutation consists of one open start/end path and disjoint cycles on the unused vertices. The open-path signs cancel its off-diagonal minus signs, leaving the positive product of path rates; the remaining signed cycles are exactly the complementary principal determinant. Paths of length0 are included in the general identity, but the preceding shortest-path argument excludes lengths below4 here.

In six states, a simple path has at most five edges. A four-edge path leaves one unused vertex m, whose complementary determinant is s+lambda_m. A five-edge path leaves the empty determinant1. Therefore the scalar numerator is exactly

    sum_m W_m(s+lambda_m)+R5.

On the other hand, the bound characteristic polynomial and exact target transform make that numerator

    H(s)det(sI-T)=K(s+u).

Comparing the two coefficients proves sum W_m=K and Ku=sum W_m lambda_m+R5. All W_m and R5 are nonnegative and K>0. This identity remains valid in the presence of feedback cycles; the complementary determinant already accounts for them. No invalid cycle-free transfer expansion is used.

## 6. Trace constraints and exact current obstruction

Set M=T+cI, whose eigenvalues are0,-v,-d+ib twice and-d-ib twice, with v=u-c>0. Its diagonal is-x_i, so

    tr M=-(4d+v), tr M^2=4(d^2-b^2)+v^2.

Nonnegative off-diagonal products give sum x_i^2<=tr M^2, and the trace gives sum x_i=4d+v. Dividing the path identity by K gives the final constraint in L6.

A further weak necessary condition is the Cauchy trace inequality

    6[4(d^2-b^2)+v^2]>=(4d+v)^2.

It alone does NOT exclude the residual region: the v^2 term can dominate at a large hidden pole. The new layer/path constraints also do not yet rule out every such v. This is the exact failed shortcut: treating the trace inequality or a companion coefficient sign as a six-state impossibility would be unjustified.

The next bounded proof obligation is a complete constraint/classification of the six layer placements, retaining arbitrary permitted backward/within-layer rates, the input/exit supports and the canceled-pole path identity. A finite graph/rate search would require a separate exact protocol and named GO; none is requested or launched here. A successful route must add a real all-topology inequality, not repeat the already closed constant-diagonal companion calculation.

## 7. Credit, review and novelty boundary

The shortest-path idea was supplied by the parent. The irreducibility threshold, six-layer alternatives and positive numerator identity were derived here in writing as a candidate bridge toward an actual residual lower bound. These classical graph/PH mechanisms are not asserted novel. The lemma still needs independent written reconstruction and parent disposition; it is not part of the previously accepted v2 or the G7 verdict.

The operative parent verification/timestamp qualifications remain in addendum002. This lane has run no scientific program. No full-book, exact-minimum7, formal/kernel or worldwide-priority claim is made.
