# Paired-involution normal form INV1
Recorded 2026-10-17 19:44:07 PDT. Exact representation of the remaining order2 models, not an unrestricted exclusion.

Generator s=(mu,(1 2)(3 4)(5 6)), row0 fixed, mu^2=1. Set row0=0 and index columns by row1=t. The column involution
h(t)=mu*r2(t) obeys h^2=id. Rows are exactly 0,t,mu*h,g,mu*g(h),j,mu*j(h). Conversely these formulas are invariant.
Top-pair validity reduces to t-mu*h being a permutation. For fixed h let V contain the maps g for which g, g-id,
g-mu*h, g-mu*g(h) are permutations. A pair g,j extends iff g-j and g-mu*j(h) are permutations. The remaining pair
conditions are obtained by scaling mu and composing with h. The program nevertheless checks every output on all21
row pairs directly.

h is a partition into fixed points and2-cycles, enumerated by DLX covering domain values and d=t-mu*h values. Each
h-orbit is assigned its g-values simultaneously using exact4-family masks. Union-of-compatible-values pruning is a
necessary condition only. Store every g up to swapping its paired row Sg=mu*g(h), then test every stored pair by
the two cross conditions. A store cap or deadline is UNKNOWN, not exhaustion.

Existence reductions: unit conjugation sends h to u*h(u^-1 t), g,j similarly, preserving all conditions. Keep one
lexicographic h representative under this finite unit group. Independently replacing g by Sg or j by Sj preserves
both cross conditions (they are interchanged by scaling/composition), so twin-row lexicographic reduction is exact.
Any odd-order column involution has a fixed column. Translate rows by that column (whose coordinates are paired
by mu), reindex t-a, and get h0=g0=j0=0 without changing s. Thus only the fixed-column mode is needed; this is not
an assumption excluding no-fixed-column cases (those are impossible by parity).

Target n21 multipliers1,8,13 correspond exactly to frozen groups g00,g10,g16, respectively. mu=-1 on prime7/13 gives
positive calibration examples; on n9 it is negative as expected from the known four-row nonexistence. Controls and
independent permutation H counts are recorded under calib/involution-v1/. No target use until a dated README addendum.
