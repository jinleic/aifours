# A simpler radius for the four-node-ratio neighborhood

**Status: WRITTEN bound; additive to `frontier-20261028-five-contact-four-node-neighborhood-v1.md`, not parent adoption.** In that theorem the four deviations from \((2,3,6,8)\) may each be as large as the explicit rational radius \(10^{-160}\), rather than the smaller tower-form radius. The shape rectangle, gain-1000 Cramer construction, all-member stability statement and displayed unnormalized ratio bound remain unchanged. This does not cover arbitrary contact-node ratios or arbitrary septic boxes.

At the unperturbed nodes, restriction of the independently replayed trivariate tensor certificate gives every parameter Bernstein coefficient at least
\[
m=2614056841543193314947/78125000000>1.
\]
The strict interior shape rectangle has minimum lower coefficient 1 and minimum interval width \(9481/2500000\), independently checked in the preceding packet.

On the auxiliary node box of radius \(1/10\), all roots appearing in the endpoint cubics are below 13, \(0<u<1\), and \(0<\lambda<2\). In a partial derivative with respect to any one of the four nodes, each moving node has derivative 1 and the shape parameters are fixed. The same product-rule overbounds as in `frontier-20261028-contact-node-radius-10minus160-v1.md` therefore give endpoint-cubic coefficient bounds \(5\cdot10^3\) and derivative bounds \(2\cdot10^4\); tangent-row entry bounds \(10^{11}\) and \(10^{12}\); and Cramer entry bounds \(10^{15}\) and \(10^{16}\), including the gain 1000. The 120-term Leibniz formula bounds each \(5\times5\) determinant and its partial derivative by \(10^{78}\) and \(10^{79}\), respectively.

Here there is no parameter-denominator clearing factor. The scaled Cramer numerator has coefficient bounds \(10^{81}\) and partial-derivative bounds \(10^{83}\); its boundary/center pairing coefficients are bounded by \(10^{86}\) and their partial derivatives by \(10^{88}\). At most four monic synthetic divisions amplify the combined bound by less than \(10^{36}\). Fixed frequency de Casteljau subdivision does not increase it. Three degree-3 inverse Bernstein parameter transforms have row-norm product less than \(6^3<10^3\), so every shape-tensor coefficient has each node partial derivative bounded by \(10^{127}<10^{150}\). The direct endpoint/width functions obey the same much looser \(10^{150}\) bound.

Moving four coordinates by at most \(10^{-160}\) therefore changes any tensor coefficient, endpoint or width by at most \(4\cdot10^{-10}\), less than half the positive base bounds. All numerator coefficients and all boundary/center tensor coefficients remain positive, all seven widths remain positive, and the root order and alternating marker signs persist. Boundary-to-center linearity and the original \(S<1000\) estimate then give the same strict SPR and ratio bound for every \(\rho<1\).

This is an analytic conservative estimate based on the exact base certificate and its independent replay; the universal derivative bounds are written mathematics, not a separate machine proof. No formal verification, cross-vendor review, novelty claim or unrestricted septic conclusion is made.
