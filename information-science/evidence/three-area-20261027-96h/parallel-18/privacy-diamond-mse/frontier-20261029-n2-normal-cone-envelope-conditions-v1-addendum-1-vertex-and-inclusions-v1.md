# Addendum 1: vertex-sign correction, inclusion-only subdifferential statements, master-integral limit

Owner: InfoResearch96h-2 / info-1. Native clock: `Thu Oct 29 20:36:30 PDT 2026`. **OWNER REPAIR of the frozen f280 source** `frontier-20261029-n2-normal-cone-envelope-conditions-v1.md` SHA `df1224e15ac5723d2841f99c5c2d93626bad8d543b499bebfafe8f6886afe742` (bytes unchanged; read this first). Unreviewed, not adopted.

**(M1) Vertex corrected.** At (0,1/2) the active constraints a>=0 and c>=a+1/2 have outward normals (−1,0) and (1,−1), so N_K=cone{(−1,0),(1,−1)}. Smooth necessity is

    h_c >= 0   AND   h_a + h_c >= 0,

the SAME sign of h_c as (G2); my (G3) "h_c<=0" was a sign error (the feasible ray (0,1) forces h_c>=0 directly). Consequently NOTHING excludes the vertex branch by sign reversal; item-(c) preparation must not use the wrong sign.

**(M2) Inclusions only.** All Clarke statements are downgraded to NECESSARY INCLUSIONS: ∂_C rho ⊆ −{g_{ac}}·(∂_λh)^{-1} for g_{ac} in the projected Clarke subdifferential of h (Clarke's chain rule gives an inclusion without strict-differentiability assumptions); the pointwise-interchange formula for ∂_C h is asserted only as the containment of every measurable-selection integral of pointwise convex-hull elements; and (F) becomes 0 ∈ (that set) + N_K as a necessary condition only. No equality is claimed anywhere.

**(m1) Master form limit.** In (M), the block-0 integral runs to the limit a (its own moving limit), not a universal c; the boundary-term bracket carries the y-limit speeds of each block's own interval (block 0: [0,a]; tail: [0,c] with the corner subinterval [a,a+1/2] inside it). The speed coefficients themselves are unchanged.

(G1), (G2), (G4), (G5) stand as written modulo the M2 downgrade. No manuscript is issued from this repair; item (c) remains unlaunched pending your disposition.
