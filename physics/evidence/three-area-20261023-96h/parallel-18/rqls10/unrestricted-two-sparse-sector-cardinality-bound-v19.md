# RQLS10 v19 — arbitrary two-sparse sector mechanisms have sharp-scope ray-multiplicity bounds

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 06:58:55 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite-dimensional/context/counting reasoning only; no interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no private decimal/approximate scout or discarded-probe backconversion. No machine/kernel/formal/human/configured-family/novelty acceptance.

The original unrestricted maximal1-RQLS10 remains UNKNOWN, with the parent-supported necessary intrinsic branches{10},{4,6},{5,5}. This closes a different whole sparse-coordinate mechanism inside ANY of those branches. It neither assumes nor proves that arbitrary sector rays are two-sparse.

## 1. Exact hypotheses and bounds

Let E be ANY rankd common sector of an actual1-RQLS(n), so each original row, column and designated transversal contains exactlyd of its cells, forming an ONB there. Suppose EVERY sector cell vector is supported on at mostTWO coordinates in ONE fixed orthonormal basis of that sector. The basis is arbitrary and need not be an actual row; phases and nonzero amplitudes are arbitrary complex numbers. Exact zero support is required, not numerical smallness.

Let A be the number of sector CELLS supported on one coordinate, and let a be the number of DISTINCT coordinate rays that occur. There are nd sector cells, and0<=a<=d,A>=a.

**Theorem A (exact multiplicity bound).** The number K of distinct sector rays satisfies

    K <= a+2*floor((nd-A)/6).                        (COUNT)

Consequently

    K <= floor((nd+2d)/3).                          (UNIFORM)

If d is ODD then every actual row-sector basis has at leastONE coordinate ray, so A>=n. When n>=d, this gives the stronger bound

    K <= d+2*floor((nd-n)/6).                        (ODD)

**Theorem B (original order10 consequences).**

- If all100 entries are two-sparse in any fixed basis of C^10, the full cardinality is at most40.
- If a common4-sector is entirely two-sparse in any sector basis, it has at most16 distinct rays among40 cells. The full original array then has cardinality at most76.
- If a common5-sector is entirely two-sparse in any sector basis, it has at most17 distinct rays among50 cells. The full original array then has cardinality at most67.

These are bounds, NOT claims that an array attaining them exists. In particular no maximal100-ray solution in any surviving intrinsic branch can be produced by keeping ALL of that sector's rays in a coordinate-root/two-sparse alphabet, even with arbitrary complex phases/amplitudes, arbitrary resolution and irreducible support graph.

## 2. Every two-sparse ONB consists of coordinate singletons and orthogonal two-coordinate pairs

Take a genuine two-support vector

    q=alpha*e_r+beta*e_s, alpha*beta!=0.

A vector with support<=2 orthogonal to q cannot overlap its support in exactlyONE coordinate: the inner product would have a single nonzero term. Thus every other vector of a two-sparse ONB is either supported on the SAME pair{r,s}, or entirely disjoint from it.

An ONB spanning the whole sector must therefore contain EXACTLYONE other vector on{r,s}, the unique perpendicular ray

    q_perp=-conj(beta)*e_r+conj(alpha)*e_s.

The vectors outside that pair span its coordinate complement; nothing with mixed one-coordinate overlap is allowed. Iterating across the basis partitions its coordinate directions into singletons (coordinate axes) and2-blocks, each2-block occupied by one orthogonal pair. This proves the asserted structure for arbitrary unequal complex amplitudes. A zero amplitude is a singleton and is counted in A instead, not divided away.

In particular if d is odd there is at leastONE singleton in every row-sector ONB. Since the n rows partition the cells, A>=n. This is an exact row-count statement, not a claim that the coordinate rays are themselves common reducing1-sectors.

## 3. Three ACTUAL contexts force at leastSIX cells per noncoordinate ray pair

Fix a sector cell v carrying a genuine two-support ray L. Its row, column and designated-transversal sector ONBs EACH contain the unique ray L_perp within the same coordinate pair, by Section2.

Those THREE partner cells are DISTINCT. Two distinct original contexts through v have no other cell in common: a transversal meets each row/column once, rows/columns intersect once and the transversal classes are disjoint. Thus L_perp occurs in at leastTHREE actual cells. Choosing ANY one of those L_perp cells and applying the SAME argument shows that L itself also occurs in at leastTHREE cells.

Every noncoordinate ray is paired with its unique coordinate-pair perpendicular ray, which is noncoordinate too. The pairing is an involution without fixed points. Different such ray pairs have DISJOINT sets of carrying cells; two distinct pairs may use the same coordinate2-space, but their rays are different and their cell multiplicities cannot be reused. No connectedness assumption is made.

Therefore every DISTINCT unordered noncoordinate perpendicular pair consumes at leastSIX of the nd-A noncoordinate cells and contributes exactlyTWO distinct rays. Adding the a coordinate rays gives COUNT. This counts actual occurrences, not vectors up to selected phase representatives or a graph relaxation.

For comparison, row/column ONBs alone already force at leastTWO occurrences of each ray, because the two partner positions are distinct. The third resolution is what gives the factor3 and the six-cell bound here; no additional resolution is assumed.

## 4. Exact universal specializations and sector interpretation

From COUNT, K<=a+(nd-A)/3<=(nd+2a)/3<=(nd+2d)/3. Since K is an integer, this proves UNIFORM with no assumption that a floor expression is monotone.

For the order10 cases:

- d=10, nd=100: UNIFORM gives K<=floor(120/3)=40.
- d=4, nd=40: UNIFORM gives K<=floor(48/3)=16.
- d=5 ODD, nd=50: A>=10, so COUNT<=a+2floor(40/6)=a+12<=17.

The first bound is a bound on the full array. In the4-sector case the other60 cells contribute at most60 distinct rays, giving76 in total. In the5-sector case the other50 contribute at most50, giving67. Cross-sector rays are orthogonal and cannot collide; replacing the other cells by their count only weakens the upper bound. No attainable example or sharpness assertion is needed.

A common4-sector or5-sector need not have a further common2-sector merely because its rays are two-sparse. Different coordinate pairs can overlap across contexts and make its intrinsic support graph connected. The present argument still applies because it uses the basis-by-basis unique pair partner, not a falsely inferred global reducing projection.

Conversely, the proof does NOT apply to merely SOME two-sparse rays in a dense array. Their context partners could be genuinely three-/higher-support vectors; the full two-sparse ONB hypothesis in Section2 would then fail. Nor does a tensor C^2 tensor C^5 notation imply any coordinate-root support bound. These distinctions preserve the original unrestricted branches instead of silently narrowing them.

## 5. Original source identity and remaining geometry

Parent `rqls-unrestricted-sector-v15-v16-entire-parent-v1.md` adopts the ENTIRE small-sector/commutant union at the literal registered modern target, and `rqls-registered-modern-source-identity-parent-addendum-v1.md` separately binds the later actual two-way Zhang-Cao v2 definition bridge. Both were read completely before this manuscript. Their historical reviewer NR-BOOK-IDENTITY remains true; no verbatim Chinese book quote, current openness or novelty inference is introduced here.

The original surviving task remains an actual100-ray construction or exclusion of ALL irreducible10/proper4+6/proper5+5 branches. The new theorem says that all such maximal constructions must leave the fully two-sparse sector mechanism. The Witting40-ray4-sector model, which uses three-support vectors, required the separate v18 spread proof; it is NOT excluded by pretending it is two-sparse. Other genuinely dense4/5-sector configurations and all irreducible constructions remain open.

This is a fresh WRITTEN necessary theorem/quantitative restriction, not witness certification, a complete sector classification, a full no-go or a new scientific permission. All earlier findings/frozenbytes, v9 and v14 mathematical withdrawals, lexical clock qualification and ZERO-credit quarantines remain. Same original18/exclusive root/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and30min substantive actual-clock cadence. Primary continues the actual remaining geometry; pending gates are not a stopping condition.
