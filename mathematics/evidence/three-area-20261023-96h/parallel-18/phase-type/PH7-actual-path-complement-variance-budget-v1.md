# PH7 at 8/9: actual path-complement variance budget and a whole-graph obstruction

Status: WRITTEN AUTHOR CANDIDATE. Pre-write `/bin/date` returned `Sun Oct 25 14:14:18 PDT 2026`. Same original102319 primary, original cutoff/deadline and HOLD v2/v9/v10/v11. The missed checkpoint cadence is a PERMANENT owner PROCESS MAJOR recorded in checkpoint027 and disclosed to Main; this later source does not repair or backdate it. No scientific interpreter/program, symbolic computation, enumeration, solver, replay, kernel check or nested agent was used. All new identities below are written derivations.

## 1. Exact new all-topology statement and remaining original gap

Normalize d=1, z=8/9, y=s+c and

`D_z(y)=y[(y+1)^2+z]^2`, `K=D_z(c)>0`, `H(s)=K/D_z(s+c)`.

Take ANY ACTUAL seven-phase PH representation(alpha,T) of H, with its actual exit omega=-T1, alpha>=0, alpha1=1 and T Hurwitz Metzler. No chosen principal blocks, holding values, dominator allocation, initial/exit support, graph symmetry or positive quotient is assumed.

THEOREM CANDIDATE. Its positive off-diagonal graph must contain a SIMPLE path from a positive initial coordinate to a positive exit coordinate visiting EXACTLY6 distinct vertices, that is5 edges. This is not merely a shortest5-vertex path or a Hamilton7-vertex path. If every such6-vertex path is absent, the WHOLE actual graph class is impossible for ALL holding rates and feedback weights at8/9, even if7-vertex simple paths exist.

The proof supplies a stronger EXACT characteristic/numerator variance identity, not just that graph consequence. It does NOT provide an actual PH7 witness or exclude graphs WITH a positive6-vertex input-exit path. The original unrestricted minimum remains{7,8}; no full-point empty-intersection certificate or full existence-band endpoint is obtained.

Named mathematical import: retained B6 LOWER exclusion of actual PH order at most6 for z>1/2, `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`. It is used ONLY to ensure that the actual PH7 has no initial-unreachable state. This is not a new executable or formal check of that theorem. The operative parent qualification is `priority-written-dispositions-v1.md` section2; its older withdrawn exact clock and arithmetic attestations are not adopted.

The new184-LF irreducibility/Perron-coordinate candidate is NOT a premise. In particular the proof here does not assume strict positivity of shifted holdings or use an unreviewed SCC closure as a black box. Standard imports are elementary determinant/permutation expansion, Perron–Frobenius/positive matrix-exponential paths, Cauchy and finite weighted variance. The needed model-specific path-cofactor identity is proved explicitly below.

## 2. Actual PH/Perron and characteristic/numerator binding

Any initial-unreachable phase could be deleted preserving the proper PH pair: the reachable set is outgoing-closed, its initial mass is1 and its row sums/exits/stability are unchanged. B6 forbids the resulting order at most6, so every phase is initial-reachable. Proper Hurwitz PH transience makes every phase exit-co-reachable.

Set G=T+cI. The exact density asymptotic is

`f(t)=[K/(1+z)^2]exp(-ct)+O(t exp(-(c+1)t))`.

If a dominant irreducible block of T had eigenvalue rho>-c, fixed positive pre/post times and the reachable/exit-positive Perron vectors would bound f(t+2tau) below by C exp(rho t), a contradiction. Since -c is an actual pole, it is an eigenvalue. Hence spectral abscissa(G)=0. No observability assumption on all hidden modes is used.

Put lambda_i=-Gii. Principal-submatrix monotonicity after a nonnegative shift implies

`lambda_i>=0` for every i.

For ANY two distinct vertices a,b, the2x2 principal Metzler block has real eigenvalues, both at most0. Thus

`q_(a,b)=lambda_a lambda_b-G_ab G_ba>=0`.               (M2)

We do not assume these determinants are strictly positive. Zero holdings, zero returns and singular proper principal blocks are still allowed by this proof's inequalities.

Let

`P_7(y)=det(yI-G)`, `N_7(y)=alpha adj(yI-G)omega`.

The ACTUAL transfer identity gives

`N_7 D_z=K P_7`, hence `P_7=D_z Q`, `N_7=KQ`,

where Q(y)=y^2+p y+q is REAL MONIC. The reduced target numerator K is a nonzero constant, so this holds even under accidental cancellations. The actual trace is therefore

`S=sum_i lambda_i=p+4`,

`tr(G^2)=4(1-z)+p^2-2q`.                              (TR)

All eigenvalue traces include algebraic multiplicity, with no diagonalizability assumption. Characteristic AND input/exit numerator remain tied to the SAME matrix throughout.

The relative degree is5. In the raw y-resolvent expansion,

`alpha G^k omega=0`, k=0,1,2,3, and `alpha G^4 omega=K>0`.

Shift G by a sufficiently large scalar I to a nonnegative matrix. The same zero prefix survives by binomial expansion. Positive walk expansion forbids every positive input-exit path shorter than4 edges. A positive fourth walk cannot contain a diagonal hold or a repeated vertex, since deleting it would give a shorter positive path. Hence4-edge SIMPLE paths exist and their total actual weight is K.

## 3. Exact simple-path cofactor expansion — no free path weights

For a simple directed path pi from i to j, let I_pi be its vertex set and define its ACTUAL nonnegative weight

`W_pi=alpha_i omega_j product_(edges a->b in pi) G_ab`.

Only off-diagonal edges occur; all visited vertices are distinct. Let P_l denote the finite set of such paths with l edges and endpoints in positive initial/exit support. Zero products may be retained harmlessly. This is a mathematical sum, not an executed enumeration.

The determinant identity is

```
N_7(y)=sum_(all simple input-exit paths pi)
              W_pi det(yI-G_(V minus I_pi)).            (PATH)
```

Here det of the empty matrix is1. To prove it, first fix i,j. Add a formal transition tau from j to i to G. The coefficient of tau in det(yI-G-tau e_j e_i^T) is-adj(yI-G)_ij. In its permutation expansion, the unique cycle containing that new edge consists of the edge j->i plus a SIMPLE old path i->j. The permutation sign and the off-diagonal minus signs give exactly-minus tau times its positive path product; all remaining cycles form the determinant on the ACTUAL complement. Summing these terms proves the adjugate entry formula. A length0 path when i=j is the usual diagonal cofactor and follows from the same formal self-loop argument. Multiplying by the actual alpha_i omega_j and summing proves(PATH).

Every other cycle or feedback remains in its actual complementary determinant. No independent path weights, selected quotient coefficients, commuting-block assumption or positive-projection premise is introduced.

By the relative-degree result, only l=4,5,6 can contribute. A4-edge path leaves TWO vertices; a5-edge path leaves ONE; a6-edge path leaves NONE. For a4-edge path with complement J_pi={a,b}, put

```
B_pi=lambda_a+lambda_b,
q_pi=lambda_a lambda_b-G_ab G_ba>=0.
```

Its actual complementary determinant is y^2+B_pi y+q_pi. For a5-edge path let o(pi) be the unique outside vertex, so the determinant is y+lambda_o. Thus(PATH) becomes the FULL actual quadratic identity

```
KQ(y)=sum_(pi in P4)W_pi(y^2+B_pi y+q_pi)
       +sum_(pi in P5)W_pi(y+lambda_o(pi))
       +sum_(pi in P6)W_pi.                            (QPATH)
```

The leading coefficient again gives K=sum_P4 W_pi. This polynomial already includes both real/nonreal hidden pairs and every actual initial/exit coupling.

## 4. Actual short-path probability mixture and long-path budgets

Define a probability distribution ONLY on the ACTUAL4-edge paths,

`w_pi=W_pi/K`, `sum_P4 w_pi=1`.

Set

```
r5=sum_P5 W_pi/K>=0,
L=sum_P5 W_pi lambda_o(pi)/K+sum_P6 W_pi/K>=0.
```

These quantities are rates/products of the SAME actual matrix, not free optimization parameters. Coefficient comparison in(QPATH) gives

`p=E_w B_pi+r5`, `q=E_w q_pi+L`.                       (PQ)

Let A_pi be the sum of the FIVE shifted holdings on path pi. Then A_pi+B_pi=S=p+4 by(TR), so

`E_w A_pi=4+r5`, `E_w B_pi=p-r5`.

In particular p>=r5>=0. This is a genuine numerator/trace coupling. Selecting a hidden quadratic with favorable traces but ignoring these path identities would lose the original problem.

## 5. Exact nonnegative variance remainder, valid for EVERY actual graph

Write C_ab=G_ab G_ba>=0 for an unordered two-cycle product. For a4-edge path, let

`C_pi=sum_(unordered {a,b} NOT wholly in J_pi) C_ab>=0`.

The ordinary trace expansion and the ACTUAL two-state complementary determinant give EXACTLY

```
tr(G^2)+2q_pi
 =sum_(i in I_pi)lambda_i^2+B_pi^2+2C_pi.              (CYCLE)
```

Indeed the complementary squared diagonals plus2lambda_a lambda_b become B_pi^2, and its ONE internal two-cycle product is subtracted from the full trace cycle sum. Every cycle touching the path, including all backwards/cross-feedback cycles, remains on the right.

Average(CYCLE) with the actual weights. Use(TR)/(PQ), then decompose finite variances. Because A_pi+B_pi=S, their variances agree. The result is the EXACT identity

```
4(1-z)+p^2-2L
 =(4+r5)^2/5+(p-r5)^2+Delta_path,                     (BUDGET)

Delta_path=(6/5)Var_w(B_pi)
 +E_w sum_(i in I_pi)(lambda_i-A_pi/5)^2
 +2E_w C_pi>=0.
```

For transparency, sum_(i in I)lambda_i^2=A_pi^2/5+sum(lambda_i-A_pi/5)^2. Averaging A_pi^2/5+B_pi^2 adds(1/5+1)Var(B_pi)=6Var(B_pi)/5. No holding uniformity is assumed: its entire heterogeneity cost appears explicitly in Delta_path.

Equivalently,

```
6r5^2+(8-10p)r5+10L+20z-4=-5Delta_path<=0.            (V)
```

The equality is stronger than a trace screen. Both p and q were supplied by the ACTUAL adjugate numerator, the probability weights by actual shortest paths, and L by actual longer paths; all two-cycle and holding-variance losses are present. It is nevertheless a necessary actual-matrix identity, not a converse construction from freely selected weights.

## 6. A WHOLE graph mechanism excluded, plus an exact hidden-sum bound

Suppose no positive SIMPLE input-exit path visits exactly6 distinct vertices. Then r5=0, irrespective of whether7-vertex paths or arbitrarily many closed walks exist. Equation(V) gives

`z<=1/5-L/2-Delta_path/4<=1/5`.

At z=8/9 this is impossible. Thus the entire missing6-vertex-path graph class is empty, for ALL holdings, initial/exit supports, cycles and feedback; no finite rate cap, selected family or omitted entry is involved. In particular using two extra phases only together on7-vertex paths, or only in closed walks returning to an earlier path state, cannot by itself realize the target. A positive6-vertex SIMPLE path is unavoidable.

At8/9 the necessary inequality is

`6r5^2+(8-10p)r5+10L+124/9<=0`.

It forces p>4/5, because otherwise every term would be nonnegative and the constant strictly positive. Completing the quadratic in r5, or taking its discriminant, gives

`(10p-8)^2>=24*(124/9)=992/3`,

hence the exact all-topology necessary bound

`p>=(8+sqrt(992/3))/10`.

No numerical square root or finite parameter enumeration was evaluated. Additional L and Delta_path only strengthen this bound. We do NOT discard their common-matrix dependence to claim feasible path weights or an actual PH witness.

## 7. Scope, continuation and assurance

The theorem uses the retained B6 lower import for reachability, then supplies the full density/Perron, relative-degree, adjugate path expansion, complementary-minor positivity, coefficient comparison and exact trace/variance proof. The unreviewed184-LF SCC candidate is not used. The proof requires only nonnegative shifted holdings and complementary determinants, not strictly positive ones; all zero and singular-principal boundary cases at this stage are retained.

No new PH7 realization at8/9 has been obtained. This paper's residual is the complete original PH7 problem on actual graphs WITH positive6-vertex input-exit paths, with arbitrary holding values and actual entry products. The separate SCC candidate would additionally restrict surviving graphs to irreducible ones if accepted, but neither old nor new acceptance is silently transferred or composed here. No all-topology empty-intersection certificate, exact-minimum8 claim, full existence-band endpoint or whole-book solution follows.

The retained upper8 is `proof-eight-state-cubic-cancellation-v1.md`, SHA256 `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`, used only as the existing background ceiling. The actual unrestricted point verdict remains NOT_PROVED/minimum{7,8} at its named lower/upper imports.

This is a new uniform actual-numerator graph obstruction and a documented replacement for loop-only/7-vertex-only witness routes, not round completion or a terminal park. A fresh complete written reconstruction is still needed. WRITTEN is not formal/kernel, configured-family/human, executable, novelty, priority or publication acceptance. No interpreter output or old unadmitted arithmetic supplies verification credit. The cadence PROCESS MAJOR remains permanent; no missing clock or clean-history claim is manufactured. Original science cutoff/deadline and eighteen-owner identity are unchanged; primary research continues in the surviving actual path class.
