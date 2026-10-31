# Addendum 4: Delta displayed on the pure-slack stratum, with every moving limit

Owner: InfoResearch96h-2 / info-1. Observed `/bin/date` immediately before this write: `Fri Oct 30 03:33:33 PDT 2026` (not an estimate). ADDITIVE to `c0fc76fe…`,`6bf0a034…`,`cb697d42…` (unchanged). Unreviewed; standing hypothesis (cutoff two, 1/2<V<=2) throughout; λ=V; ε-dependence enters only through m=b/(1−b), v, T2,T3,T4 and λ.

**Stratum.** S = {(a,c): a>=0, c>=a+1/2, and at BOTH points (a,c) and (a,a+1/2) the two-line rule is slack at every height}: Π₁(y)>=Π₀(y)+1 for all y. (Nonempty: at large a the upper box faces bind: Π₀=2a−y, Π₁=min(2c−y,R₁) and slack holds when max(t₁,R₁)… i.e. when 2c−y or R₁ exceeds 2a+1−y at every height; e.g. c>=a+1 with R₁>=2a−y.) On S the profiles are the independent projections; nothing depends on a inside the blocks.

**Displayed Delta (pure-slack stratum), δ:=c−a−1/2:**

    Δ(a,c) = b·{ (16/3)T3·δ + 4T2·(c²−(a+1/2)²) − 8λm·δ
               + 8∫_{a+1/2}^{c} ψ₁(Π₁(y;c),y) dy
               + 8∫_{0}^{a+1/2} [ψ₁(Π₁(y;c),y) − ψ₁(Π₁(y;a+1/2),y)] dy },

    ψ₁(z,y)=T2z+m(z²+y²)+z³/3+y²z−4y³/3−λ(z−y),
    Π₁(y;c)=min(2c−y, max(c, R₁(y))),  R₁(y)=sqrt(max(λ−v−y²,0))−m,

and by Danskin d/dc of the tail block on S:

    ∂_c[8∫₀^c ψ₁(Π₁(y;c),y)dy] = 8ψ₁(c,c) + 8∫₀^c ∂_zψ₁(Π₁(y;c),y)·[1_{Π₁=c}·1 + 1_{Π₁=2c−y}·2]dy.

Every moving limit is displayed: the constant part difference (16/3)cT3+4c²T2−λ8cm between c and a+1/2, the added y-range [a+1/2,c], and the projection-shift integral over the unchanged range [0,a+1/2].

**One nontrivial full-stratum sign.** The constant-part and added-range terms are jointly

    b·{δ[(16/3)T3 − 8λm + 4T2(a+1/2+c)] + 8∫_{a+1/2}^c ψ₁(Π₁(y;c),y)dy},

and on the sub-stratum S₊ where additionally Π₁(y;c)<=2c−y is the UPPER face or free with λ−v−y²>=0 (root real), ∂_zψ₁=(z+m)²+v+y²−λ can be signed where z>=… : at z=Π₁>=a+1/2 and λ<=2, if a+1/2>=√λ−m then ∂_zψ₁>=0, making BOTH the shift integrals and the face speeds nonnegative — hence Δ>=0 on S∩{a+1/2>=sqrt(λ)−m}. This is a genuine full-stratum sufficient condition, displayed with its hypothesis.

**Exact remaining term.** The unproved piece on general S is the projection-shift integral 8∫₀^{a+1/2}[ψ₁(Π₁(y;c),y)−ψ₁(Π₁(y;a+1/2),y)]dy with c>a+1/2: raising the lower box face c→Π₁ increases z where the lower face binds (∂_zψ₁ sign undecided there), and where Π₁ is free (R₁(y)∈(c,2c−y)) the integrand is UNCHANGED. The exact open inequality is the nonnegativity of that single displayed integral on S outside S₊; its derivation above shows it is the only term not covered by the constant-part and face-speed signs.

Withdrawn/kept per Main: Δ>=0 is sufficient-only, not an equivalence; Δ<0 at a point does not exhibit an interior minimizer since both h-values may stay positive at λ=V. No programs, no instances; old bytes preserved.
