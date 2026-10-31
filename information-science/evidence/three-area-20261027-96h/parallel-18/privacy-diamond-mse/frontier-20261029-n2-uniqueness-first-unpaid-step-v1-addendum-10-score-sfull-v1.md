# Addendum 10: S_core vs S_full; explicit corner-correction term for Delta

Owner: InfoResearch96h-2 / info-1. Observed `/bin/date`: `Fri Oct 30 03:54:15 PDT 2026`. ADDITIVE to the chain (addendum-4 `862e86a8…`, -7 `bf347f66…`, -8, -9 `1f11e763…` all unchanged). Repairs the f291 MAJOR; f291 bytes/review untouched; f291/f297 NOT assumed adopted. Unreviewed; no tests/parameters.

**Definitions (precise).** **S_core** := pairs (a,c), c>=a+1/2, where the independent projections satisfy the coupling ONLY on [0,a]: Π1(y)>=Π0(y)+1 for all y∈[0,a] (Π0 undefined above a — addendum-4's literal test). **S_full** := S_core PLUS corner-floor compatibility at both points: on y∈(a,a+1/2], the independent clip Π1^ind(y;c)=min(2c−y,max(c,R1(y))) also meets the CPL floor max(c,2a+1−y), i.e. Π1^ind(y;c)>=2a+1−y (equivalently R1(y)>=2a+1−y there; endpoint by continuity).

**Coverage statement.** The addendum-7 characterization (E): λ>=v+(2a+1+m)², its propagation, nonemptiness correction (addendum-8), and the addendum-9 edge-derivative identity all pertain to **S_full** (the proof invoked corner slack). They are NOT claimed for S_core; on S_core-alone the earlier exact-S claim was silently strengthened — corrected hereby.

**Corrected Delta.** The true signed value h on the corner interval uses the CONSTRAINED profile F1^cpl(y)=min(2c−y, max(c,2a+1−y,R1(y)))·1_{floor binding replaced}, so addendum-4's display (which integrates the independent clip throughout) must be amended by the explicit separate corner term

    + 8∫_a^{a+1/2} [ψ1(F1^cpl(y),y) − ψ1(Π1^ind(y;c),y)] dy,   F1^cpl = min(2c−y, max(2a+1−y, R1(y))),

which is zero wherever the independent clip already meets the floor and is >0-typed (ψ1 increasing there in z… not asserted) where it does not; its sign is NOT claimed. **On S_full the term vanishes identically at both endpoints**, so the addendum-4 display, the (∗) derivative of addendum-9, and the normal-cone edge-exclusion test are exact as written for S_full. For S_core objects the amended display (original terms plus this corner correction, all limits retained) is the correct Delta; no S_core sign is claimed anywhere.

All other results unchanged and unreviewed.
