# PH7 at 8/9: a necessary directed short cycle

**Disposition: ACCEPT, computer-assisted at the exact certificate and caller boundaries below.** Native clock observed before composing: **2026-10-28T19:48:11-0700 PDT**. This is same-harness written mathematics and exact standard-library arithmetic, not a human, independent-model-family, formal/kernel or novelty certification. It neither constructs nor excludes all PH7 realizations at `z=8/9`.

## Exact statement

Let `D(y)=y[(y+1)²+8/9]²`. There is **no** irreducible real 7×7 Metzler matrix G with spectral bound zero, `D|χ_G`, and off-diagonal directed graph having no cycle of length 2, 3 or 4.

For the registered PH transform `H(s)=c(a²+b²)²/[(s+c)((s+a)²+b²)²]`, with `a=c+d`, `c,d,b>0`, `z=b²/d²=8/9`, every actual PH representation using at most seven states therefore has a directed **2-, 3- or 4-cycle**, conditional on the named [irreducibility/normalization result](math-1-ph7-global-irreducibility-eight-edges-parent-v1.md). This includes arbitrary rates/topology, cancellations, repeated hidden roots and any number of positive edges. The separate new author candidate requiring a 2- or 3-cycle is **not** adopted or used here.

## Reconstructed proof and exact finite obligation

Perron theory gives seven positive diagonal rates `u_i=−G_ii`. In the characteristic-polynomial permutation expansion, every nonidentity term requires an off-diagonal directed cycle. If the girth is at least five, those terms have degree at most two, so coefficients of `y⁶,y⁵,y⁴,y³` equal the first four elementary symmetric functions of all seven rates.

Choose any five rates, with elementary functions `s₁,…,s₄`, and write the remaining two real rates as v₁,v₂, `t=v₁+v₂`, `r=v₁v₂`. Since `D|χ_G`, write `χ_G=D(y)(y²+py+q)`. Matching the top two coefficients eliminates p,q. The next two equations are affine in t,r:

`(s₂−4s₁+74/9)t+(s₁−4)r+s₃−4s₂+(74/9)s₁−28/3=0`,

`(s₃−(70/9)s₁+212/9)t+(s₂−70/9)r+s₄−(70/9)s₂+(212/9)s₁−1007/27=0`.

Let `den` be this 2×2 determinant and `tn,rn` its Cramer numerators. The reconstructed integer polynomials `Dpol=81den` and `Npol=−19683(tn²−4rn·den)` have 96/1,753 nonzero monomials and individual degrees 2/4. The coefficient and certificate reviews independently reconstructed their complete arrays, not just point evaluations. The exact dyadic Bernstein covers establish both strictly positive on the positive five-rate orthant. Hence

`t²−4r=−Npol/(3Dpol²)<0`,

contradicting `t²−4r=(v₁−v₂)²≥0`. Only the four top matched coefficients are used; hidden-root coincidences and arbitrary edge weights do not bypass the contradiction. The actual PH caller obtains `D|χ_G` from the reduced denominator and `G=(T+cI)/d`; positive rescaling preserves the support and uses the named import to give irreducibility and spectral bound zero.

### Certificate coverage and the three expository minor findings

Compactify each rate by `u=x/(1−x)` and clear the positive denominators. The complete binary tries have **513/657 leaves**, every coordinate split at least once. All **124,659/2,053,125** computed tensor Bernstein coefficients are nonnegative. Every leaf corner lying in the global open cube is strictly positive. For a point on an internal subdivision face, choose the incident leaf corner matching any endpoint coordinates and an interior endpoint in every remaining coordinate; its Bernstein basis weight is positive. This pays strict positivity throughout the open cube, not at the compactified infinite-rate boundary, where zero coefficients are allowed.

The written reviewer reported **0 FATAL / 0 MAJOR / 3 MINOR**: spell out that corner argument; make clear irreducibility/spectral bound are used to obtain positive rates; and do not transfer the `8/9` certificate to every `z>1/2`. These qualifications are adopted explicitly here. The coefficient/certificate reviewer reported **0/0/0** in its assigned scope. At `z=1/2` a determinant-zero control exists, so no endpoint or all-z extension follows.

## Bound evidence and actual parent replay

- [Candidate, 92 LF](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-ph7-critical-short-cycle-theorem-v1.md): SHA-256 `8f31703fe765d1380431b719d4b4f16d5ec53cd4fd61a25699e7c00d38a9421b`.
- [Frozen manifest](../review-waves/f109-ph7-critical-short-cycle/manifest-v1.json): `8f1fa208bdb84a0fbbb44c12c9a1ce22af20a9076ec5ec650babb09db0cb4f75`.
- [Written proof/caller review, 118 LF](../review-waves/f109-ph7-critical-short-cycle/proof-review-v1.md): `8db18f9876baeccaf56e8e6a7b3557025d890556f995115187539a1518de8fdf`; parent read completely. Its separate direct and Padé coefficient derivations agree; the short-cycle PH caller has no separate defect, subject to the named import.
- [Coefficient/certificate review](../review-waves/f109-ph7-critical-short-cycle/certificate-review-v1.md): `b10ad38b3ea36638bddc54e1ca593b57af18f77a7693b550aff6d52fede8d3a4`; parent read completely. Its [independently written engine](../review-waves/f109-ph7-critical-short-cycle/certificate-replay-v1.py), SHA `7142f9c6f2ef2b5efd1d9b54e301c6f05a7b4ee5d6595e18f82e2bfd5e44902f`, imports or executes no author checker.
- Parent inspected that entire engine and actually replayed it from verified in-memory bytes on **2026-10-28 19:47:08–19:47:11 PDT**. [Parent result](../review-waves/f109-ph7-critical-short-cycle/parent-shared-certificate-result-v1.json): `feb55d4e2633a0690b62300851021f024df7317bd550e11cc36b0f413f0b2188`. [Execution binding](../review-waves/f109-ph7-critical-short-cycle/parent-shared-certificate-binding-v1.json): `44a53507acf2d68452aebc8cae40bfab47cee1a813bfb09091e79ee1cb8c5a03`. Both complete covers, array hashes, coefficient reconstruction and all corruption controls passed; controls reject missing/duplicate/prefix leaves, altered coefficients, sign flips and an invalid demand for strictness at the infinite-rate corner. This is a **shared-engine parent replay, not a third independent implementation**.

Trusted computation includes Python 3.14.3 integers/Fraction/JSON/SHA, the inspected sparse polynomial and Bernstein implementations, and the machine/runtime. Ordinary Perron/adjugate/characteristic and Bernstein facts and the named prior normalization theorem remain written mathematical inputs, not proof-assistant axioms audited here. No exact minimum order, PH7 existence/nonexistence, stronger girth-four obstruction, public priority or original-target closure is claimed.
