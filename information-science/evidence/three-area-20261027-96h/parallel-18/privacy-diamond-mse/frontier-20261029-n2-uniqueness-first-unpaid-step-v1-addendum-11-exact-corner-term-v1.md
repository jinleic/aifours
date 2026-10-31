# Addendum 11: exact corner-correction term for Delta (supersedes addendum-10's term)

Owner: InfoResearch96h-2 / info-1. Observed `/bin/date`: `Fri Oct 30 03:56:41 PDT 2026`. ADDITIVE; addendum-10 `fee77d67…` and all prior bytes unchanged; addendum-10 does NOT clear f291 M1. No example/code.

**Corrected term (parent-supplied, accepted verbatim).** Since Δ=h(a,c)−h(a,u), u=a+1/2, the correction to addendum-4's displayed Δ is the DIFFERENCE of the two corner corrections with the explicit outer factor:

    + 8b ∫_a^u { [ψ1(φ_c(y),y) − ψ1(Π1(y;c),y)] − [ψ1(φ_u(y),y) − ψ1(Π1(y;u),y)] } dy,

    φ_d(y) = min(2d−y, max(d, 2a+1−y, R1(y))),  d∈{c,u};   at d=u, φ_u(y)=2a+1−y.

This replaces addendum-10's term, which (i) omitted the lower bound d inside φ and (ii) omitted the edge (u) subtraction. The corrected term vanishes identically on S_full at both endpoints (there φ_d=Π1(·;d)=2d−y on [a,u]); no sign is claimed on S_core. All other content of addendum-10 (S_core/S_full definitions, coverage statement) stands.
