# Shor ACTUAL arbitrary Y — exact boundary moments, positive rational realization and all-parameter return tails

Owner MathShor / MathShor-2. Actual `/bin/date` before writing: **Sun Oct 25 19:30:21 PDT 2026**. WRITTEN CANDIDATE, unreviewed. No scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/build/test/CLI/nestedagent/new GO. This is a generalization of the positive-potential representation to the ACTUAL arbitrary one-b set, not merely the selected row normal form. It is not a Shor completion witness or a general noncompletion theorem.

This derivation is AFTER the actual v105-G return19:14:25 and separate prospective primary-resumption ACK19:15:35, SHA256 `71fd5544d6b4896df794f3f9b60bc84ef468f0fe91678fd4bcf961e09d67e797`. No new review duty was inferred from the parent's complete-read notification.

## 0. Data, exact local dependencies and what is NO LONGER assumed

Fix n, actual subsets A,B of Z_n with0inA,B and A+B=Z_n direct. Let Y be ANY actual one-b residue set satisfying the ALL-t border bijection

    B x Y^t x A -> Z_n^(t+1),
    (d,(i1,j1),...,(it,jt),s)
      ->(d+i1,j1+i2,...,jt+s)                             (BT)

for EVERYt>=0. All residues are canonical0,...,n-1. The original Shor application requires Y contain all sixteen literalC pairs and n>14. No actual such candidate has been found here.

There is NO requirement that Y's first coordinates lie in A, that its rows be complements of A, that it have the existence-normal form, or that unknown actual representatives be replaced. There are no independent row normalizations. The graph is the SAME fully defined cyclic graph: every a-edge v->v+1, and every b-edge i->-j for(i,j)inY. Call its unnormalized weighted adjacency matrices P for a and Q for b, and

    M(t)=tP+(1-t)Q,            0<t<1.

P is the actual cyclic permutation matrix; Q may branch and is not assumed stochastic, diagonalizable or symmetric. Multiple different labels with the same endpoints contribute separately.

The previous exact arbitrary-Y border packet is `shor-actual-Y-complement-automaton-and-finite-linear-border-test-v1.md`, SHA256 `ebf60e3d3db9450bad5d8274adb39fe307930dad24bdf78465c8a07ba641ac96`. The prior explicit first-return-code/rawUD/completeness/finiteness proof is `shor-cyclic-one-b-automaton-regular-completion-and-finiteness-v1.md`, SHA256 `17da5c435b348966f1097a79a0c1a9c0c7d7aa43e62dfce74f9cef4ef675af3a`. Both are local WRITTEN/unreviewed interfaces, not new accepted imports.

The immediately preceding positive-potential packet, SHA256 `692154b4563d4d8ca70a8d054a376611881e5ad9ee52866921e0775e67aee0bb`, gave an ELEMENTARY explicit polynomial h for the common-mate row normal form. That original restricted theorem remains immutable. Here a general finite positive-rational construction is obtained from BT itself and one stated standard Perron-Frobenius theorem.

## 1. EXACTLY ONE boundary path for EVERY literal binary word

Let u be the0/1 column indicator of start states -B, and v the0/1 column indicator of terminal states A. For a binary word w, let M_w be the ordered product of its UNWEIGHTED label matrices P/Q.

Write w with t b's and actual a-run lengths l0,...,lt. Graph paths with start -d for d inB, terminal s inA, and b-edges(i_r,-j_r) satisfy exactly

    d+i1=l0, j1+i2=l1,...,jt+s=lt modn.

The border bijection says there is EXACTLY ONE such tuple, hence exactly ONE such graph path, for EVERY w. Conversely every such path gives that tuple. For a pure-a word the same conclusion is the t0 tiling B+A=Z_n. Therefore

    u^T M_w v = 1 for EVERY finite binary wordw,           (1)

including the empty word. In particular u^Tv=1; this counts the actual intersection -B with A, not alln endpoints. No expected-length argument or formal-language theorem is being substituted for the exact path count.

## 2. Unambiguity extends to EVERY pair of graph endpoints

For any two states r,s and any word w, there is AT MOST ONE path r->s labelledw. To prove this, use0in-B and0inA. Prepend the fixed a-path0->r of lengthr and append the fixed a-paths->0 of length[-s]_n. Two distinct r->s paths would then give TWO distinct boundary0->0 paths with the SAME extended word, contradicting(1).

This argument retains actual full paths/cuts. It does not cancel a^n in a raw word or assume that all graph transitions are deterministic. It also proves that loop labels and first-return labels have no hidden path multiplicity.

## 3. Whole weighted boundary moments and the Perron root

Sum(1) over all binary words of fixed lengthL with their ordinary weights t^(#a)(1-t)^(#b). Their weights sum(t+1-t)^L=1, so

    u^T M(t)^L v = 1 for EVERY integerL>=0.              (2)

Meanwhile §2 implies every entry of M(t)^L is AT MOST1: for each possible word of lengthL, at most one path contributes to that ordered endpoint pair, and the TOTAL weight of all words is1. All entries are nonnegative. Thus

    0 <= [M(t)^L]_(r,s) <= 1,
    ||M(t)^L||_infinity <= n.                            (3)

For a fixed finite matrix, uniformly bounded powers imply spectral radius<=1; this also follows directly by applying the powers to an eigenvector. If its spectral radius were<1, ordinary finite-dimensional Jordan theory would give M(t)^L->0, contradicting the nonvanishing boundary moment(2). Hence

    spectral_radius(M(t))=1.                             (4)

For every0<t<1 the positive a-cycle makes M(t) irreducible. The standard finite-dimensional **PERRON-FROBENIUS** theorem therefore supplies a STRICTLY positive right eigenvector h(t) with M(t)h=h at the real eigenvalue1. This exact standard theorem, not a numerical eigensolver or a cycle-enumeration guess, is the named additional classical input here.

The usual irreducible Perron conclusion being used is only existence of positive left/right eigenvectors and their simple Perron eigenspace. I do not claim a new proof of the entire theorem. No primitive/aperiodic hypothesis is required for this conclusion; irreducibility supplied by the a-cycle is enough.

## 4. EXPLICIT positive rational h(t), not an existential controller oracle

Normalize h_0=1 and let F={1,...,n-1}. Write N(t)=M(t)_(F,F), c(t)=M(t)_(F,0). Then an explicit finite formula is

    h_F(t)=(I-N(t))^(-1)c(t),        h_0(t)=1.            (5)

Here is a direct proof that the inverse in(5) exists and is positive, rather than an untested inverse assertion. From ANY positive Perron h, define the diagonally similar finite transition matrix

    K_(r,s)=M_(r,s) h_s/h_r.

Its rows sum1. Following a-edges reaches0 from every nonzero state in at mostn-1 steps with strictly positive probability. Since finitely many states are involved, at each fixedt a positive minimum hitting probability exists. Thus the nonbase subtransition matrix K_FF has powers whose row sums decrease geometrically on n-step blocks; its geometric series converges. Consequently I-K_FF, and by similarity I-N, are invertible. The inverse is the nonnegative series sumN^k.

The vector in(5) equals the already-positive eigenvector normalized at0, so the missing row0 equation also holds. Every component is a RATIONAL FUNCTION of t, by the finite adjugate/determinant formula for a matrix whose entries are polynomial in t. Its denominator is NONZERO throughout0<t<1, and its values are strictly positive there. This is a fully specified finite-dimensional symbolic formula for EACH given actual candidate, not an executed matrix inverse, an unknown realization oracle or a claim of positive monomial coefficients.

The normal-form polynomial h from the preceding packet is a special more explicit realization of this same positive eigenvector after scaling. No normal-form hypothesis is used in(1)–(5).

## 5. ALL-t pointwise potential ratios give quantitative uniform return tails

The a-edge part of M h=h gives h_r>=t h_(r+1). Iterating along the a-cycle from ANY r to ANY s in at mostn-1 steps yields

    min_r h_r / max_s h_s >= t^(n-1).                    (6)

This is independent of the detailed Q rows and their unknown degrees. It avoids estimating a rational-function condition number or a stationary distribution.

For a nonzero state r, the all-a route to0 has lengthd=n-r<=n-1 and probability t^d h_0/h_r>=t^(2n-1) under K. At state0 the first positive all-a return has probability t^n>=t^(2n-1). Thus from EVERY state a visit to0 occurs within n steps with probability at least

    delta(t)=t^(2n-1)>0.

The same deterministic-block conditioning proof gives, for first positive return time tau from0,

    P(tau>kn) <= (1-delta(t))^k,
    E tau <= n/delta(t).                                 (7)

An exponential moment follows whenever exp(theta*n)(1-delta(t))<1. On ANY compactt interval[epsilon,1-epsilon],0<epsilon<=1/2, use the ONE constantdelta_epsilon=epsilon^(2n-1). These are exact algebraic/finite-chain estimates, not calculations made by a program or numerical sampler.

For a0->0 path, all h ratios telescope and its probability is the ORDINARY Bernoulli weight of its literal word. Endpoint unambiguity makes the corresponding first-return code X satisfy

    sum_(w inX) t^(|w|_a)(1-t)^(|w|_b)=1                 (8)

at EVERY0<t<1. No path multiplicity is absorbed into a word or hidden normalization.

## 6. Entire raw realization and the finite versus infinite split remain exact

The first-return code X is regular, RAW UD and factor-complete, by the explicit prior graph proof; it contains canonical M0 and the originalC if Y does. The same proof establishes the EXACT finiteness criterion for this graph:

    X finite  IFF  EVERY canonicalYpair(i,j)has i+j<n.     (9)

If all sums are short, the induced graph on nonbase vertices is acyclic because every internal edge strictly increases its canonical state. The first-return code has length<=n and is an ACTUAL finite complete positive realization. No such Shor candidate was supplied. If any i+j>=n, the corresponding backward/self b-edge and the intervening a-path form a nonbase cycle and X is infinite.

For finite truncations X_L, all the normalization/tail conclusions are valid for the ACTUAL arbitraryY:

    0 <= 1 - sum_(w inX_L)t^(|w|_a)(1-t)^(|w|_b)
      <= (1-delta_epsilon)^(floor(L/n)).                  (10)

They contain allM0 onceL>=2n-1 and are finite RAW UD. In the INFINITE side of(9), the deficit is STRICTLY positive for EVERY finiteL/every0<t<1, so no finite truncation is complete. In the FINITE side it becomes zero once all ofX is included, and that really IS a finite completion, not a numerical approximation.

Therefore the positive-Perron/exponential-tail/near-unit-Kraft conclusions are NOT artifacts of a selected common-mate normal form. They hold for EVERY actual border candidate. What varies is its exact wrapped-pair/finiteness status and, beyond this fixed cyclic construction, whether an infinite version can be replaced by a different finite history-split realization. The earlier n2 prefix control demonstrates why that latter question is not decided by the presence of an infinite cyclic first-return code.

## 7. Exact original target, named trust and nonclaims

This is a genuine change from a selected-mate analytic representation to the ACTUAL arbitraryone-b interface. Nevertheless it is still a REALIZATION CONTROL, not a solution of the original finite raw problem. No common-mate/actualY witness containingC, finite shortY graph, actual finite PR-saturated extension or uniform raw noncompletion invariant is supplied.

Original remaining gaps are ALL actual orders/endpoints/Y, the k7/Phi_n-divisible and ALL larger trades, exact isolated-word lifts, genuine multi-b bridge histories, arbitrarywordlength/bcount/heterogeneousdelay/arity and raw STAB. A hypothetical completion's actualY is retained, not replaced. Conditions(4)/(5)/(7)/(8)/(10) alone cannot replace FINITENESS(9) or prove that every alternative finite realization fails.

Named nontrivial ordinary input beyond the stated exact BT/rawgraph interface is finite irreducible Perron-Frobenius existence at its standard classical scope. Spectral-radius bounds, boundary-word moments, fullendpointunambiguity, the finite rational formula and every actual graph/Markov/tail application are supplied above. These are WRITTEN/unreviewed, not a formal/kernel/human/configured-family/executable/triple-witness certificate or a claim to have independently reconstructed every proof of general Perron-Frobenius/Jordan theory.

Hstar remains FALSE/WITHDRAWN; no known-construction classification or Sun8/PPT/Rminus review theorem is a premise. FACT660 versus additionalfull-code1320 scope and all older process corrections remain. No decimal scout, spectral-radius evaluation, matrix solve, probability simulation, source/shared/frozen edit, git/deletion/publication or new GO. No novelty/SOTA/discovery count or full-book acceptance. Same originaleighteenowners, exclusiveShorroot, cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; no roundcloseout.
