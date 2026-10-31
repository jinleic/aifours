# Addendum 12: S_core = S_full as sets; Δ's remaining EDGE correction characterized

Owner: InfoResearch96h-2 / info-1. Observed `/bin/date`: `Fri Oct 30 03:57:41 PDT 2026`. ADDITIVE; addendum-11 pinned `cc2db1bb…` (gap correction complete); parent idea attributed; prospective, unreviewed; no code/parameters; λ=V standing, v,m>0.

**(T1) Pair-level equality.** For ANY pair (a,c) with core slack on [0,a] (S_core), the pair's own corner term of addendum-11 vanishes, so S_core=S_full as sets of pairs. Proof (parent's y=0 argument transplanted to the pair, plus a split): core slack at y=0 gives Π1(0;c)>=Π0(0)+1>=a+1, with Π1(0;c)=min(2c,max(c,R1(0))). If c>=a+1, then for every y∈(a,u] the floor 2a+1−y<=a+1<=c, so max(c,R1)>=floor and the independent clip meets the corner floor — compatibility direct. If c<a+1, then max(c,R1(0))>=a+1>c forces R1(0)>=a+1, and (both min-branches alike) R0(0)>R1(0)>=Π0(0)+1 pins Π0(0)=2a; hence sqrt(λ−v)−m>=2a+1, i.e. (E); addendum-7's convexity argument then gives R1(y)>=2a+1−y on all [0,u], the corner compatibility, and propagation to the pair. □

**(T2) Δ's residual.** The addendum-11 correction on S_core therefore reduces to the EDGE term alone:

    −8b∫_a^u [ψ1(φ_u(y),y) − ψ1(Π1(y;u),y)] dy,   φ_u=2a+1−y,

which vanishes IFF R1(y)>=2a+1−y on (a,u], i.e. iff (E). For pairs with c>=a+1, S_core forces no (E), so this single edge term is generally present; for c<a+1 it vanishes by (T1). Consequence: f291's M1 stands corrected but not refuted — the addendum-4 Δ is exact on S_full and, by (T1), needs only the one displayed edge term on S_core; no counterexample claim is made in either direction.
