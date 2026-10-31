# Addendum 7: exact slack-stratum theorem S={λ≥v+(2a+1+m)²} — parent idea, owner-verified

Owner: InfoResearch96h-2 / info-1. Observed `/bin/date`: `Fri Oct 30 03:42:15 PDT 2026`. ADDITIVE to the item-(c) chain (all prior bytes unchanged). Idea provenance: PARENT (Main IRC, pre-f291); verification and all-variable proof below are owner-written, unreviewed. Standing hypothesis; no code/instances.

**Theorem (edge condition).** With c0=a+1/2 and slack meaning the independent projections satisfy the coupling weakly at every height, the edge point (a,c0) is slack at all heights **iff**

    λ >= v + (2a+1+m)²,                                                  (E)

and then EVERY c>=c0 is slack. Hence S={a>=0, c>=a+1/2, (E)}, nonempty iff λ>v+(1+m)² (a=0).

**Proof.** (⊆) Fix y∈[0,a]. Always R1<R0 (v,m>0). If Π0<2a−y (lower face or free) then Π0+1<2c0−y and c0=a+1/2<Π0+1, so slack forces max(c0,R1)≥Π0+1, i.e. R1≥Π0+1>Π0; with R0>R1≥Π0 the projection gives Π0=2a−y, a contradiction (root-unreal y also fail: R1<0<c0). So Π0=2a−y, and slack Π1≥2a+1−y with Π1=min(2c0−y,max(c0,R1)) forces R1≥2a+1−y (c0<2a+1−y on y≤a). On the corner interval y∈(a,c0] the floor equals the upper face 2a+1−y; the independent clip equals the forced value iff max(c0,R1)≥2a+1−y, forcing R1≥2a+1−y there too (endpoint y=c0 by continuity). Thus y²+(2a+1−y+m)²≤λ−v on [0,c0]; the left side is convex in y, and with u=a+1/2, (2u+m)²−[u²+(u+m)²]=2u(u+m)>0, so its maximum is at y=0: (E). (⊇) (E) gives λ>4a²≥y²+(2a−y)²=max_{[0,a]}[y²+(2a−y)²] (h decreasing in y), so R0≥2a−y and Π0=2a−y; likewise R1≥2a+1−y on [0,c0], so Π1=Π0+1 on [0,a] (equality allowed) and the corner clip is forced-compatible. Propagation: for c≥c0, faces 2c−y and c only rise and heights y∈(c0,c] carry no coupling floor, so both points stay slack. a=0: same computation with u=1/2 gives λ≥v+(1+m)². Equality λ=v+(2a+1+m)²: slack holds with Π1=Π0+1 at y=0. □

**Consequence and the exact remaining sign.** On this nonempty S, the addendum-4 display specializes: Π0=2a−y on [0,a]; Π1=min(2c−y,max(c,R1)) with R1≥2a+1−y on [0,c0]. The c-derivative is the Danskin form already displayed; at the edge c=c0 the upper-face derivative satisfies the sharp all-variable bound

    ∂_zψ₁(2c0−y,y) = (2a+1−y+m)²+y²+v−λ <= 0   on y∈[0,c0],   (=0 only at y=0 when (E) is tight),

i.e. the face terms of ∂_cΔ are NONPOSITIVE at the edge, while the constant part (with −8λm) and the added-interval integrand 8ψ₁(Π₁(y;c),y) on (c0,c] remain unsigned. Therefore the sign of Δ on S is NOT yet decided: the exact unpaid inequality is

    b⁻¹∂_cΔ = (16/3)T3+8cT2−8λm + 8ψ₁(Π₁(c;c),c) + 8∫₀^c ∂_zψ₁·[1_{Π₁=c}+2·1_{Π₁=2c−y}]dy >= 0?

with its newly proved nonpositive face component — the first genuine quantitative handle on the corner-vs-interior comparison. No S-emptiness claim is made; f291 scope untouched.
