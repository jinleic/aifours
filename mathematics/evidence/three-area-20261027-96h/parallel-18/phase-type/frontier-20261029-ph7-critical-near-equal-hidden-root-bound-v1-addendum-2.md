# Addendum 2: the same bound holds for three-quarter-unit hidden-root splitting

Status: **WRITTEN-checked-in-kernel with exact rational algebra**, pending independent scientific review. This immutable additive successor widens `|h|<=1/2` in `frontier-20261029-ph7-critical-near-equal-hidden-root-bound-v1-addendum-1.md` (SHA256 `ed06fd7121b09940d6c801f335bc4383d2bcdcaeccd0e27baa5f4154112e078a`) to **`|h|<=3/4`**. All other notation and scope remain unchanged.

For a real seven-state Metzler generator with the critical pair repeated twice and two hidden real decay rates `r+h,r-h>0`, if `|h|<=3/4` then their mean satisfies `r>=r_*`, where the pinned degree-six `F` has its unique root `r_*` in `[27/8,7/2]` and `r_*>3437/1000`.

The centered second/third traces and polynomials `F,C,D` are those in `frontier-20261029-ph7-critical-near-equal-hidden-root-bound-v1.md` (SHA256 `ecd97a65517447de61d4e129ad2da7b24f6b86378d66699d05796247ace6f19c`). The wider proof uses the following exact checks:

1. `tau2>=0` forces `r>37/20`. On `0<=r<=37/20` and `h^2<=9/16`, the defining convex quadratic for `tau2` has maximal endpoint values `-359/16` at zero and `-7/4` at `37/20`, both negative.
2. `tau3<0` for `r>=37/20`: its cubic at that endpoint is `67669/1600>0`, its derivative at `r=37/20+t` is `(2160t^2+4536t+5159)/16>0`, and the `h^2*(315r-252)` term is nonnegative.
3. The Bernstein coefficients of `-F` on `[37/20,27/8]` are `44939243951/2560000`, `47733248437/5120000`, `3977724737347/51200000`, `5514642363421/20480000`, `4788010994899/8192000`, `537183377321/655360`, `47222523911/262144`; all are positive.
4. On `[37/20,7/2]`, the coefficients of `-C(r)` are `34499493/6400`, `2482526907/3200`, `3151986669/1600`, `532817487/160`, `67088061/16`, and the coefficients of `-[C(r)+(9/16)D(r)+(81/256)*127575]` are `1271248209/3200`, `8155066689/6400`, `16837221951/6400`, `5387696721/1280`, `1368590553/256`. All are strictly positive Bernstein coefficients.

For fixed `r`, the bracket `C+D*q+127575*q^2` is convex in `q=h^2`. Item 4 makes it negative at both endpoints `q=0,9/16`, hence throughout the interval. The `h`-dependent correction in the exact centered-moment polynomial is therefore nonpositive. Item 3 and the previously pinned monotonicity/root proof make `F(r)<0` on `[37/20,r_*)`, contradicting the necessary centered-third-moment inequality. This proves `r>=r_*`.

All rational lists were checked in the owner's SymPy kernel and are printed for independent reconstruction. There is no claim for larger half-gaps, complex hidden roots, formal proof, novelty, independent scientific review, parent adoption, or a complete PH7/PH8 verdict.
