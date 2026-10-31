# Addendum 3: the bound holds for unit hidden-root half-gap

Status: **WRITTEN-checked with exact stdlib Fraction Bernstein arithmetic**, pending independent scientific review. This additive successor extends `frontier-20261029-ph7-critical-near-equal-hidden-root-bound-v1-addendum-2.md` (SHA256 `c0dc02a1d4831f1cbc2ceb5cfd381a95b176bce0107e9026434a93032dbc5fe2`) from `|h|<=3/4` to **`|h|<=1`**.

If a real seven-state Metzler generator has the critical double pair and hidden real decay rates `r+h,r-h>0` with `|h|<=1`, then

`r>=r_*`,

where `r_*` is the unique zero in `[27/8,7/2]` of the pinned polynomial `F` from `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1-addendum-3.md` (SHA256 `fa840d0d89681381968887d9ceedc73c284dc9c22ed903098fd5d2499e7e3f2b`). In particular `r_*>3437/1000`.

## Exact proof

Use the exact centered moments and `E=(107163/4)*[(25/42)tau2^3-tau3^2]=2F(r)+C(r)q+D(r)q^2+127575q^3`, `q=h^2`, from the original near-equal manuscript (SHA256 `ecd97a65517447de61d4e129ad2da7b24f6b86378d66699d05796247ace6f19c`). The previous source establishes the symmetric centered third-moment necessity `E>=0` whenever `tau2>=0` and `tau3<0`.

**First, `r>3/2`.** The `tau2` defining convex quadratic `45r^2-72r-58+63q` is strictly negative for `0<=r<=3/2` and `0<=q<=1`: its endpoint maxima are 5 at `r=0` and `-7/4` at `r=3/2`, so convexity alone is insufficient at `r=0`. However, because the hidden decay rates are positive, `q=h^2<r^2`; use `q<=min(1,r^2)`. For `0<=r<=1`, the quadratic is at most `108r^2-72r-58`, whose convex endpoint maximum is `-22`; for `1<=r<=3/2`, it is at most `45r^2-72r+5`, whose convex endpoint maximum is `-7/4`. Thus `tau2<0` there, a contradiction.

**For `3/2<=r<=37/20`, `tau3<0`.** The coefficient of `q` in its positive bracket is `315r-252>0`; `tau2>=0` forces `q >= (-45r^2+72r+58)/63`. Substituting that lower bound in the bracket yields `-2*(90r^3-216r^2-131r+293)`. Its Bernstein coefficients on this interval are `343/2`, `12691/60`, `141659/600`, `95011/400`, all positive. Hence the bracket is positive and `tau3<0`.

On the same low-mean rectangle `r in [3/2,37/20]`, `q in [0,1]`, the exact bivariate polynomial `-E` is strictly positive. The independently implemented stdlib `Fraction` checker `frontier-20261029-ph7-hidden-unit-gap-low-mean-fraction-check.py` (SHA256 `a03f93766c63230954c19c7aa812d00ecb276a19895a978cd0da8e0f4e981e53`) converts to degree `(6,3)` Bernstein form, subdivides once in each axis, and verifies strictly positive integer coefficients on all four quadrants. It actually returned PASS; the four scaled minima were `2920638800701440`, `3990144614400000`, `2444343710772096`, `10096997624108640`. Therefore `E<0`, contradicting the necessary inequality.

**For `37/20<=r<=7/2`, `tau3<0`** by the positive-cubic argument of addendum 2. On this interval `C<0`, and `C+D+127575<0`; the five Bernstein coefficients of the negatives are respectively

`34499493/6400`, `2482526907/3200`, `3151986669/1600`, `532817487/160`, `67088061/16`,

`4135950693/6400`, `5139488907/3200`, `4942362069/1600`, `773922087/160`, `98992989/16`.

For fixed `r`, `C+Dq+127575q^2` is convex in `q`; both endpoint values at `q=0,1` are negative, so it is negative throughout. The `h`-dependent correction to `E` is nonpositive. The parent source's exact Bernstein proof that `F<0` on `[37/20,27/8]`, followed by its monotone-root proof, gives `F<0` for all `r<r_*`; hence `E<0` there, again a contradiction. This proves `r>=r_*`.

The low-mean checker is independent code by the same owner, not a disjoint scientific review or formal proof. No statement is made for half-gap above one, complex hidden roots, PH7/PH8 existence, novelty, or parent adoption.
