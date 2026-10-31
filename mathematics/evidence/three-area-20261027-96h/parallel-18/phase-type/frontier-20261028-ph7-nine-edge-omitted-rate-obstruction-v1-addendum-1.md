# Addendum 1: a sharper two-omission rate cutoff

Status: **WRITTEN-checked with stdlib Fraction coefficient replay; not independently audited**. This is an immutable successor to `frontier-20261028-ph7-nine-edge-omitted-rate-obstruction-v1.md` (SHA256 `0660efa2450da347f5f74a45d55ff4af6127254c899ae6c6ecc3ce867db745cf`), not an edit to that file. All notation and the exact full-/one-block determinant argument in that manuscript are retained.

## Improvement

In the two-omitted-vertex block of §4 of the original manuscript, the sufficient cutoff `t,u>=3` can be sharpened to `t,u>=21/8`, still at `z=8/9`. Consequently every repeated critical eigenvalue on the nine-edge disjoint-triangle connector graph forces at least one of:

* a one-omission triangle with its omitted normalized rate `<2`; or
* a two-omission triangle with at least one omitted normalized rate `<21/8`.

With unnormalized eigenvalue `-d+ib`, multiply these thresholds by `d`. This strengthens the exact necessary condition, but does not close any remaining non-Hamiltonian connector shape or decide PH7.

## Proof of the stronger block lemma

Use `M_theta=N*v_t*v_u-|C|^2*(v_t+v_u)` and its exact concavity decomposition in §4 of the original manuscript. It suffices to prove `M_1>0` since `M_0=v_t^2*v_u^2>0` and the concavity remainder is nonnegative. Put

`t=21/8+T`, `u=21/8+U`, `T,U>=0`,

and expand in the visited normalized rate `r`:

`M_1 = A(T,U) + r*B(T,U) + r^2*C(T,U)`.

A direct coefficient calculation gives each of `A(T,U)-a`, `B(T,U)-b`, and `C(T,U)-c` nonnegative coefficients in the ordinary power basis of `T,U`, where

`a = 17082424681921/110075314176`,

`b = -34168631/524288`,

`c = 4084297/589824`.

Thus for `r>0`, `M_1 >= a+b*r+c*r^2`. The latter quadratic is strictly positive because `a,c>0` and

`4*a*c-b^2 = 51891455549006353/1014454095446016 > 0`.

The coefficient identities, every individual coefficient sign, and the displayed rational discriminant were checked by `frontier-20261028-ph7-nine-edge-21over8-fraction-check.py` (SHA256 `2e76071b2bcab760253c8c4399f1718050142dfbdca6aa9eb20b92c9e4d2f60d`); it returned PASS. That checker imports the pinned preceding stdlib `Fraction` coefficient-dictionary implementation, so it is a replay of the written identities, **not an independent implementation or mathematical review**. The proof uses the exact finite coefficient sign test, not any selected generator or numerical search.

## Scope and sharpness of this method

The one-omission threshold `2` cannot be uniformly lowered using only the corresponding block logarithmic-derivative sign. For any fixed `0<t<2`, choose `0<theta<1` satisfying `theta>2(t-1)/t` when `t>1` (any positive `theta<1` works when `t<=1`), and take the other two normalized rates equal to a variable `R`. The exact formula in §3 gives

`lim_{R->infinity} M_theta/R^4 = theta*t*[2(t-1)-theta*t] < 0`.

The relevant block polynomial is nonzero for all sufficiently large `R` because its leading complex factor has positive imaginary part. Its logarithmic derivative therefore has **positive** imaginary part. These are analytic block-level counterexamples to a uniform stronger derivative lemma, not PH7 witnesses and not complete generators.

Likewise, in the two-omission case at `z=8/9`, set both omitted rates equal to `q>1`, set the visited rate to `r`, and temporarily set `theta=1`. The coefficient of `r^2` in `M_1` is exactly

`2*q^2*(9*q^2-18*q+17)*(18*q^2-54*q+19)/81`.

It is negative for `1<q<(27+sqrt(387))/18`. By continuity one may take `theta<1` sufficiently close to 1 and then `r` sufficiently large, with nonzero block polynomial, giving a positive imaginary logarithmic derivative. Therefore no universal two-omission sign cutoff below `(27+sqrt(387))/18` is possible via this block lemma. This lower limit is not a PH realization, a proof of a sharp PH threshold, or permission to import selected controls into other held research.

The critical PH7 application remains conditional on the separate, as-yet-unadopted nine-edge graph template and its triangle-capacity/overlap-budget dependencies. The graph-specific spectral result remains independent of that template. No unrestricted graph exclusion, novelty, formal proof, or parent adoption is asserted.
