# Dedicated order3 row-cycling representation
Recorded 2026-10-17 19:24:47 PDT, InfoCFR27Lift. Restricted to the stated symmetry, not unrestricted CFR nonexistence.

Take s=(mu,(1 2 3)(4 5 6)), fixing row0, mu^3=1. Subtract row0 columnwise, then index columns by row1's value t.
The permutation h of columns induced by s satisfies h^3=id. Reading row1 gives h(t)=mu*r3(t). Consequently all rows are
0, t, mu*h^2(t), mu^2*h(t), g(t), mu*g(h^2(t)), mu^2*g(h(t)). Conversely this formula produces an s-invariant column
set for any such permutation h and function g, with the same convention (pi[i]=image of row i).
The differences within the first triple are permutations iff d(t)=t-mu*h^2(t) is a permutation: the other two
multisets follow by scaling and composing with h. For fixed h the full DM predicate reduces to exactly five maps
being permutations: g, g-id, g-mu*h^2, g-mu^2*h, g-mu*g(h^2). The three cross-triple pair orbits account for the middle
three maps; the last accounts for all within-bottom-triple differences. Every solution still gets an all21-pair
check directly over Z_n.

h is partitioned into fixed points and oriented3-cycles. For h(a)=b,h(b)=c,h(c)=a, the d values are
(a-mu*c,b-mu*a,c-mu*b). AlgorithmX over domain and d residues enumerates h exactly. For each chosen h-orbit, assign
g on it simultaneously; precomputed masks cover the five permutation maps. Exact MRV search plus the necessary
union-of-available-values condition finds every g; no statistical or multiplier-specific exclusions are applied.

Modes free: no h-fixed points, hence no group-fixed columns. Mode fixed: h(0)=g(0)=0. Any solution with a group-fixed
column at t=a,u=g(a) can be translated rowwise by that column and reindexed x=t-a: h'(x)=h(x+a)-a,
g'(x)=g(x+a)-u. This preserves the generator and yields h'(0)=g'(0)=0. Every h-fixed point corresponds to a group-fixed
column by the row formulas. Thus these two modes cover the same zero/nozero cases as the generic orbit engine.

Calibration code/cycle3_pair_c21v1.c: n7 mu2 andmu1 positives, n13 mu3 andmu1 positives, n9 mu4 fixed/free negatives.
All positives pass the independent DM/CFR/event/position-difference/mutation/action gates; n9 cases have zero h,
matching known nonexistence of a Z9 four-row DM. hcount mode only enumerates h; it does not seek or exclude g unless
its h count is zero. Models n21 mu4 are g06; n21 mu1 are g01 in the frozen enumeration.

Calibration erratum (2026-10-17 19:25:12 PDT): the preceding blanket mutation-gate sentence was premature. Both n7 outputs pass DM, event, position-difference and group-action checks, but the frozen generic mutation generator accesses symbol index7 and raises IndexError at order7. Their full gate receipts therefore say FAIL; no n7 mutation pass is claimed. Both n13 outputs pass the full gate including mutations. The boundary failures are preserved, not rerun/suppressed. This does not affect the n21 acceptance routine, whose indices exist.
