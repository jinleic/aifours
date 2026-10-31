# Elementary polynomial proof of generic all-site support density

**PhysicsResearch96h-2 / physics-1.** This is an additive WRITTEN proof of the density step in `frontier-20261028-d4-generic-all-site-support-obstruction-v1.md`, SHA256 `cd63c97ef4590b3e3b2adafbc43b9853c4ad6abd4f71b39c230da2848cebdc73`. It avoids the earlier invocation of real-analytic continuation. It does not assert any q3 positivity, evaluate a chosen physical state/control, or create a new source/review/novelty claim.

Let f=f1 f2 f3 be the nonzero homogeneous degree-12 polynomial in the formal coordinates of u∈H=(C⁴)^tensor3, with fi a fixed 4×4 minor of the i-th site matricization. Each fi is nonzero and their product is nonzero in the complex polynomial ring, as already proved.

For an **arbitrary** unit u, the elementary fact that a nonzero polynomial over an infinite field has a nonvanishing point supplies an abstract w with f(w)≠0; no coordinates of w are specified or evaluated in q3. The one-variable polynomial

`P(t)=f(u+t w)`

has leading coefficient f(w), so it is not identically zero and has only finitely many roots. There are therefore real nonzero t arbitrarily close to0 with P(t)≠0. For such t, `u(t)=(u+t w)/||u+t w||` is well-defined near0, converges to u, and satisfies `f(u(t))≠0` by homogeneity. Thus full Schmidt rank at all three local sites is dense on the unit sphere; continuity makes it open.

For an arbitrary isometry V with columns (u,v), replace u by a sufficiently close u(t) in that dense set and Gram–Schmidt v against u(t). The resulting isometries converge to V. Each local reduction of their rank-two range projection dominates the corresponding full-rank reduction of `|u(t)><u(t)|`, so all three local supports are rank4. This proves relative density; openness follows from positivity of each local-reduction determinant.

The resulting full-original-domain continuity implication is in `frontier-20261028-d4-dense-local-support-boundary-extension-v1.md`, SHA256 `4e6fe20463ddba8ebf32fba9cfd9139d058837b05a618732cc0b85eb91bffff3`. No generic q3 nonnegativity is proved; a separate all-generic-input positivity argument and its exact boundary extension remain required. No unreviewed source result, held outcome, parent/f62 adoption, human/family/Lean, operational or novelty claim is implied.
