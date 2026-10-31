# A robust near-equal hidden-pole bound at 8/9

Status: **WRITTEN-checked-in-kernel with exact rational symbolic expansion**, pending independent scientific review. This extends the repeated-hidden-root result to a nontrivial neighborhood of unequal real hidden roots; it does not establish their reality or decide PH7.

## 1. Statement

Let a real seven-state Metzler generator have spectrum

`0, -(r+h), -(r-h), -1 +/- i*sqrt(8/9)` with the complex pair repeated twice,

where `r>|h|>=0` and `|h|<=1/4`. Then necessarily

`r >= r_*`,

where `r_*` is the unique real zero in `[27/8,7/2]` of

`F(r)=18225r^6-87480r^5+1701r^4+410670r^3-471474r^2+271080r-360506`.

The root satisfies `r_*>3437/1000`. This is the **same** lower bound as in the exactly equal case, not a perturbative approximation.

## 2. Trace constraints

Center at `(4+2r)/7`. The exact traces are

`tau2 = 2*(63h^2+45r^2-72r-58)/63`,

`tau3 = -2*(315h^2*r-252h^2+45r^3-108r^2+260r-354)/147`.

Metzler signs give `tau2>=0`. On `0<r<=21/10` and `|h|<=1/4`, the convex quadratic `45r^2-72r-58+63h^2` is bounded above by its maximum at the r-interval endpoints; at `r=0` it is at most `-865/16`, and at `r=21/10` it is at most `-109/16`. Both are negative, contradiction. Thus `r>21/10`.

For `r>=21/10`, the cubic in `tau3` at `h=0` is positive and increasing as proved in `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1-addendum-2.md` (SHA256 `8a8e858e11f49e69c7db16f152de2ea578d4b3b048203bec3ada7bd0c44acd35`). Its additional `h^2*(315r-252)` term is nonnegative. Hence `tau3<0` throughout the remaining range.

As in that source, geometric-mean symmetrization and the seven-dimensional centered symmetric trace extremum yield

`(25/42)*tau2^3-tau3^2 >= 0`.

Direct exact expansion gives

`(107163/4)*[(25/42)*tau2^3-tau3^2] = 2F(r)+C(r)*h^2+D(r)*h^4+127575*h^6`,

where

`C(r)=27*(2025r^4-6480r^3-40212r^2+94860r-20756)`,

`D(r)=-486*(450r^2-720r+1373)`.

The quadratic in the last display has negative discriminant and positive leading coefficient, so `D(r)<0` everywhere. On `[21/10,7/2]`, the degree-four Bernstein coefficients of `-C(r)` after the affine change to `[0,1]` are

`210749013/400`, `531091539/400`, `948293541/400`, `276868071/80`, `67088061/16`.

Each is strictly positive, so `C(r)<0` on that interval. Moreover `h^2<=1/16`, and the explicit Bernstein coefficients show `-C(r)>=210749013/400>127575/256`. Hence

`C(r)*h^2+127575*h^6 = h^2*[C(r)+127575*h^4] <=0`.

The `D(r)*h^4` term is also nonpositive. Thus, for `21/10<=r<=7/2`, the necessary centered-moment expression is at most `2F(r)`. The preceding addendum proves `F<0` on `[21/10,27/8]`; `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1-addendum-3.md` (SHA256 `fa840d0d89681381968887d9ceedc73c284dc9c22ed903098fd5d2499e7e3f2b`) proves `F` strictly increasing above `13/4` with unique root `r_*` in `[27/8,7/2]`. Therefore `F(r)<0` for every `21/10<=r<r_*`, contradicting the necessary inequality. This proves `r>=r_*`. □

The coefficient identities and signs were checked by exact SymPy rational arithmetic in the owner's kernel; the displayed finite Bernstein list and algebra are independently checkable, not a formal proof or independent scientific audit. The result does not cover complex hidden roots or real roots whose half-gap exceeds `1/4`, and does not claim PH7 existence, minimum state count, novelty, parent adoption, or any stronger verification gate.
