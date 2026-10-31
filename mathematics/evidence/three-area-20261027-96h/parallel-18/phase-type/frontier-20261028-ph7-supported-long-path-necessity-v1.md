# Any PH7 realization above z=1/5 needs a supported simple path of length at least five

**NEW ALL-TOPOLOGY WRITTEN THEOREM CANDIDATE; independent review/novelty clearance pending.** MathResearch96h-2, original math-1. It is an input/exit-route necessary condition, not an exclusion of all seven-state realizations.

## 1. The theorem

For the original H, suppose `z=b²/(a-c)²>1/5` and there is an actual PH representation with exactly seven transient states. Then its directed transition graph contains a **simple path of length5 or6** from a state with positive initial probability to a state with positive exit rate.

In particular, at z=8/9 no PH7 candidate can have every supported simple input-to-exit path of length<=4. The condition permits arbitrary graph topology, arbitrarily many input/exit states, repeated or nonreal hidden roots, and arbitrary cycle/diagonal coincidences. It does not claim that such a long path is sufficient, nor does it exclude all PH7 realizations at8/9.

The proof below does not use the old PH6 theorem; its threshold 1/5 is derived independently from the actual seven-state determinant and principal-submatrix paths. It is not claimed as a new PH6 result.

## 2. Relative degree and a complete simple-path expansion

Shift/scale `G=(T+cI)/(a-c)` and use the corresponding actual nonnegative input beta and exit gamma. The scalar transfer is `K/D_z(y)`, with K>0 and `D_z=y[(y+1)^2+z]^2`, so its relative degree is5.

For a Metzler matrix, the minimum directed distance from a positive-input state to a positive-exit state is exactly4: if it were d, the first nonzero coefficient in the expansion of `beta(yI-G)^(-1)gamma` at infinity would be at order `y^(-d-1)` and is a sum of strictly positive length-d off-diagonal walk products. A diagonal step cannot appear in a walk of exactly the minimum distance. Hence all supported simple paths have length>=4, and at least one has length4.

The actual cofactor/path identity is

    beta adj(yI-G) gamma
      = sum_(supported simple paths P) weight(P) det(yI-G_(complement P)),  (PATH)

where `weight(P)` is the nonnegative product of the input, all path-edge rates, and the exit. It follows by expanding the adjugate determinant and grouping the unique nonrepeating input-to-exit chain; the remaining permutation cycles give precisely the principal-complement determinant. The path sign and off-diagonal signs cancel. This formula retains the actual SAME matrix; it does not replace cycles by independent poles.

Assume no supported simple path has length5 or6. Since there are only seven vertices and all supported paths have length>=4, every supported simple path has length EXACTLY4 and uses five vertices. Its complement is a two-element principal set S. Because the actual characteristic polynomial equals `D_z Q` for a monic quadratic Q, the target numerator is `K Q`; the leading coefficient of each complement determinant in(PATH) is1. Dividing by the positive sum of path weights gives

    Q(y)=sum_S lambda_S det(yI-G_S),
    lambda_S>=0,     sum_S lambda_S=1.              (MIX)

Repeated paths or repeated S sets simply add weights. Every two-state complement, including one with a 2-cycle, is allowed. This identity is the critical input/exit restriction.

## 3. A topology-free trace-square contradiction

Write `G_ii=-u_i`; write `Q=y²+p y+q` and `det(yI-G_S)=y²+p_S y+q_S`. From(MIX),

    p=sum_S lambda_S p_S,       q=sum_S lambda_S q_S,
    p_S=sum_(i in S) u_i.

Newton traces of the actual seven-by-seven characteristic polynomial give

    tr G=-(4+p),
    tr G²=4(1-z)+(p²-2q).                          (TRACE)

For each two-state principal block, `tr G_S²=p_S²-2q_S`. Convexity of the square gives

    p²-2q <= sum_S lambda_S tr(G_S²).

Since G is Metzler, every pair product `G_ij G_ji` is nonnegative. Therefore

    tr G²-tr G_S² >= sum_(i outside S) u_i²
                  >= (sum_(i outside S)u_i)²/5.

The trace identity implies `sum_i u_i=4+p`; averaging over S yields

    sum_S lambda_S sum_(i outside S)u_i
      =4+p-sum_S lambda_S p_S=4.

A second Jensen inequality therefore gives

    4(1-z)
      =tr G²-(p²-2q)
      >= sum_S lambda_S [tr G²-tr G_S²]
      >= (1/5) sum_S lambda_S (sum_(i outside S)u_i)²
      >= 16/5.

Thus `z<=1/5`, contradicting the hypothesis. The proof remains valid for negative shifted diagonals, zero rates, nonminimal/unobservable states, repeated hidden roots, and nonzero 2-cycle weights, because only Metzler pair-product signs and real Cauchy/Jensen are used. The actual PH normalization ensures beta,gamma>=0 and the correct target numerator. □

## 4. Concrete complete graph cut: three triangles sharing one vertex

As an application, take the 9-edge graph consisting of THREE directed 3-cycles sharing exactly one hub and otherwise vertex-disjoint, covering all seven states. Every simple path between two vertices lies within at most two triangles: leaving one triangle and entering another passes through the hub, and visiting a third would revisit the hub. Each of the two portions has length at most2, so EVERY simple path has length<=4. Therefore, for z>1/5 this entire graph is impossible for PH7 **for arbitrary nonnegative initial and exit supports**, not just a sampled single input/exit. This is a proof of the graph cut, independent of a numerical optimizer.

The conclusion also explains why single-source/single-exit numerical trials on any strongly connected 7-vertex graph whose supported simple input-to-exit path is unique and of length4 cannot be exact PH witnesses for z>1/5. Unlike that narrower observation, the theorem permits many length4 paths and arbitrary 2-cycles in their two-state complements.

## 5. Boundaries

Named ordinary imports: determinant/adjugate path expansion, Metzler nonnegativity, Cauchy/Jensen and elementary trace identities. No numerical program, external classification theorem, old held proof or public-source characterization is used as a premise. Independent review should reconstruct all path signs, the handling of multiple input/exit supports and complement 2-cycles, and both Jensen steps.

The theorem leaves graphs with supported simple paths of length5 or6 entirely open. It does not settle the 8/9 PH7 question, PH8 minimum, novelty, formal/Lean/kernel or cross-vendor review, and it does not repair any earlier process finding.

END — every PH7 realization above1/5 must admit a simple supported input-to-exit path of length5 or6.
