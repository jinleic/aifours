# Entire stratum A: either another actual prefix separator or a single-initial 2-by-2 braid

Actual `/bin/date` observation before this manuscript: **Mon Oct 26 00:17:37 PDT 2026**. MathResearch96h-2, math-1. WRITTEN AUTHOR CANDIDATE, no independent reconstruction or parent acceptance claimed. No interpreter, calculator, eval, CAS, arithmetic program, scientific program, enumeration, solver or replay was used.

All prior process findings and approximate-ZERO-credit quarantines remain. The original PH7 question at 8/9 is NOT_PROVED/minimum {7,8}.

## 1. Scope, imports and actual graph

Use the ENTIRE physical stratum A in §9 of `PH7-eight-ninths-two-complete-dominator-strata-v1.md`, SHA256 `18d5a13896f3cd6491e34c1e166f6e9ed7edf2dff8c9c7812447cababbee7489`:

    T=[ A5     b       0
        r^T   −lambda  t
        D      f      −v ],
    alpha=(alpha_A,0,0), omega=(0,0,omega7)^T.

A5 is arbitrary, b=−A5 1>=0, alpha_A is a probability row, and the shortest positive initial-to-middle path has EXACTLY three edges. This includes multiple upstream exits, multiple initial phases, arbitrary backward feedback, and valid noncanonical partitions whose A5 contains phases reachable only after an earlier middle visit.

The preceding ordered-tail result may be applied without changing A5,b,alpha_A or r: `PH7-case-A-ordered-tail-and-ten-generator-fiber-v1.md`, SHA256 `f25b7d8623a4b393dcbb6f42eca2768eb847711db01026ffbbb914ceb7df48f6`. Hence all graph statements below also apply in its full f=0, lambda>=v class. The graph proof itself does not need that normalization.

Let I=supp(alpha_A), let o be the middle state, and use the positive directed graph on the FIVE actual A5 states and o. An internal prefix separator means a vertex in R\I on every I-to-o path. Only first arrival at o is considered; r,D,f are not suppressed from the physical matrix.

## 2. Exhaustive separator-or-braid theorem

**Theorem.** Either there is an actual internal prefix separator, or I is a SINGLE phase i and, after an actual permutation, the five upstream phases are exactly

    {i} union L union M,       |L|=|M|=2,

with positive paths i→L1→M1→o and i→L2→M2→o, possibly with M relabeled. The actual upstream matrix and exit have the full shape

    A5=[ −a0    u^T    0
           v     B      C
           w     E      F ],
    b=(0,0_L,b_M)^T,       alpha_A=e_i^T,           (BRAID)

where u1,u2>0, both entries of b_M are positive, C>=0 has a positive perfect matching, all permitted off-diagonal entries are nonnegative, and

    a0=u^T1,
    v+B1+C1=0,
    w+E1+F1+b_M=0.                                  (ROWS)

All backward and within-layer entries v,w,E and the off-diagonal entries of B,F remain arbitrary subject to these actual PH row/stability constraints. In particular the 2-by-2 C is not assumed diagonal, symmetric, rank one or regular.

*Proof.* Split every noninitial upstream vertex into an in/out pair with capacity one. Give every transition, every supersource-to-I arc, and the unsplit initial/sink vertices capacity eight. An I-to-o path exists. If a residual augmenting path after one unit of flow fails, the residual cut has capacity one and must be a single noninitial split vertex: this is the desired separator. This is the ordinary integral augmenting-path argument, not a solver run.

If no such separator exists, obtain two unit paths and discard circulation cycles. Trim each to its LAST I vertex. They have disjoint noninitial upstream vertices. Each remaining path has at least three edges because the actual shortest I-to-o distance is three. Therefore each uses at least TWO noninitial upstream vertices. Thus

    5−|I|>=4,

so |I|=1. Both paths must use exactly two internal vertices; all four noninitial upstream vertices are used. Label their first internal vertices L1,L2 and their second internal vertices M1,M2. This gives the two stated positive paths.

A direct i→Mj edge would give a two-edge I-to-o path; an Lj→o edge would do the same; an i→o edge would give an even shorter path. All are forbidden. Consequently the row from i has positive transitions only to L, and b has positive entries only on M. The chosen paths make BOTH u entries and BOTH b_M entries positive and give a positive perfect matching in C. Every other location in (BRAID) is allowed and remains actual. The row equations are precisely b=−A5 1, not a freely reselected diagonal. This proves necessity without assuming canonical reachability; in the nonseparator case all five states happen to lie on the two exhibited first-hit paths.

Conversely, every actual physical matrix of shape (BRAID), with those positive path/matching conditions, has two internally disjoint three-edge paths to o and no shorter path. Hence no noninitial upstream vertex separates all of them. The shape is therefore an exact representation of the NONSEPARATOR branch, not only a support relaxation. ∎

## 3. Actual four-state cofactor representation of the braid

Put

    H4=[B C; E F],
    u_tilde=(u1,u2,0,0),
    k_tilde=(v^T,w^T)^T,
    b_tilde=(0,0,b_M1,b_M2)^T,
    g(s)=det(sI−H4).

Here k_tilde denotes the actual return COLUMN to i, not a free polynomial. Direct elimination of the initial state, followed by polynomial clearing, gives

    a(s):=det(sI−A5)
       =(s+a0)g(s)−u_tilde adj(sI−H4)k_tilde,
    N(s):=alpha_A adj(sI−A5)b
       =u_tilde adj(sI−H4)b_tilde.                   (COF)

They are identities at roots of g as well; no coprimality or diagonalizability is required. The second numerator has degree exactly two, with positive leading coefficient

    L0=u^T C b_M>0.

Its degree follows also from the actual three-edge initial-to-middle path. In particular (COF) is a smaller actual cofactor representation for the outer data in the ten-generator fiber, not a new independently chosen Q. Set Q=N/L0 only with all row ties and its required Hurwitz condition retained.

The returns to i do not occur as an additional independent numerator factor: they enter a through the first formula. But the PH equations link their values to H4 via

    H4 1=−k_tilde−b_tilde,
    a0=u^T1.

Thus one MUST NOT vary k_tilde while pretending H4/diagonals stay free and the physical rows unchanged. For example at s=0 these ties imply

    a(0)=N(0),

exactly the upstream probability normalization used in (TEN). No forgotten initial/exit scale is supplied by a formal polynomial factorization.

## 4. Entire lumpable braid mechanisms are excluded above z=1/2

The sole scientific import in this section is the unrestricted B6 lower bound, `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`: no actual PH representation with at most six states has the original target when z>1/2. Its ordinary written status is retained.

### 4.1 Merging only the two L states

If

    v1=v2,        C11=C21,        C12=C22,           (LUMP-L)

the two L states have equal total transition rates to EVERY other block of the partition

    {i}, L, {M1}, {M2}, {o}, {post}.

Their transition/exit rates to o/post are zero. Their total rate to L itself agrees by (ROWS); the individual within-L feedback entries and holdings need not be equal. All other partition blocks are singletons. Therefore this is strong CTMC lumpability to SIX states, regardless of r,D,f and all incoming rates to L.

### 4.2 Merging only the two M states

Similarly the conditions

    w1=w2,        E11=E21,        E12=E22,
    b_M1=b_M2                                      (LUMP-M)

give strong lumpability for the six-state partition which merges M only. All incoming rates to M remain arbitrary.

For completeness, if C_part is the zero-one block incidence matrix, these equal-row-sum conditions give

    T C_part=C_part T_bar,
    omega=C_part omega_bar,
    alpha_bar=alpha C_part.

The off-diagonal rates of T_bar are nonnegative block sums; its row/exit equations and probability initial law are literal. Since C_part is injective, its invariant range shows every eigenvalue of T_bar is an eigenvalue of Hurwitz T, so T_bar is Hurwitz. The exponential identity gives

    alpha exp(Tt)omega=alpha_bar exp(T_bar t)omega_bar.

Thus this is an ACTUAL smaller PH representation of the SAME target, not a spectral quotient with unproved signs. B6 excludes it for z>1/2.

Consequently an 8/9 witness in the braid branch must break at least one equality in (LUMP-L) AND at least one in (LUMP-M). This is stronger than merely forbidding an exact branch-swap automorphism: the forbidden lumpings allow unequal individual internal holdings/feedback. These are whole graph/rate mechanisms, not failed numerical trials.

## 5. Exact residual and assurance

The entire ordered-tail A outer problem now splits exhaustively into:

1. actual A5 with an additional prefix separator (which may be reblocked, but is NOT proved impossible here);
2. the fully actual asymmetric braid (BRAID)/(ROWS)/(COF), outside both six-state lumpability mechanisms, still subject to the complete ten-generator target fiber.

The full balanced stratum B is untouched. This does not say every remaining braid is feasible, or that missing these two lumpings is sufficient for minimality. No nonnegative witness at 8/9, all-topology no-go, minimum-eight conclusion or maximal band endpoint is obtained. Formal/kernel/configured-family/human/executable/novelty review and every new gate remain separate. All mathematics here is WRITTEN, machine checks NONE; original HOLD, root, science cutoff and deadline are unchanged.
