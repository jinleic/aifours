# Addendum: the exact bound holds for half-unit hidden-root splitting

Status: **WRITTEN-checked-in-kernel using exact rational algebra**, pending independent review. This additive successor widens the `|h|<=1/4` hypothesis of `frontier-20261029-ph7-critical-near-equal-hidden-root-bound-v1.md` (SHA256 `ecd97a65517447de61d4e129ad2da7b24f6b86378d66699d05796247ace6f19c`) to **`|h|<=1/2`**. All other definitions, the exact root `r_*`, and all scope/nonclaims are unchanged.

If the real hidden decay rates of a critical seven-state Metzler spectrum are `r+h,r-h>0` with `|h|<=1/2`, then `r>=r_*`, where `r_*` is the unique root of the pinned degree-six polynomial `F` in `[27/8,7/2]` and `r_*>3437/1000`.

The proof is the same centered-trace argument, with these exact widened-interval checks:

1. Trace-square positivity forces `r>2`. Indeed for `0<=r<=2` and `h^2<=1/4`, the convex quadratic `45r^2-72r-58+63h^2` is maximized at an interval endpoint, where its values are at most `-169/4` at 0 and `-25/4` at 2.
2. The cubic in the centered `tau3` formula from the parent manuscript is positive for `r>=2`: at 2 it equals 94, its derivative at `r=2+t` is `135t^2+324t+368>0`, and the additional term `h^2*(315r-252)` is nonnegative. Thus `tau3<0`.
3. On `[2,27/8]`, the seven Bernstein coefficients of `-F` after affine conversion to `[0,1]` are `24626`, `109543/2`, `5101165/32`, `1839116671/5120`, `12744303589/20480`, `12398944103/16384`, `47222523911/262144`; all are positive.
4. On `[2,7/2]`, the five Bernstein coefficients of `-C` are `305748`, `2210193/2`, `4426353/2`, `13634217/4`, `67088061/16`; thus `-C>=305748`. Since `h^4<=1/16` and `305748>127575/16`, the sum `C*h^2+127575*h^6` is nonpositive. The separate `D*h^4` term is nonpositive exactly as in the parent source.

Hence the necessary centered-moment expression is at most `2F(r)`. It is strictly negative for every `2<r<r_*`: item 3 covers through `27/8`, and the earlier exact monotonicity proof covers the interval from `27/8` to `r_*`. This contradiction proves the widened theorem. The finite rational coefficient lists were checked in the owner's SymPy kernel and are explicitly presented for independent reconstruction; they are not a formal proof or scientific-review gate.

No claim is made for half-gap above `1/2`, complex hidden roots, a PH7 or PH8 existence/exclusion verdict, novelty, or parent adoption.
