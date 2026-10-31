# Addendum 2: a stronger exact repeated-hidden-root bound

Status: **WRITTEN-checked-in-kernel with exact rational symbolic expansion**, pending independent scientific review. This immutable successor strengthens the initial trace-square bound in `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1.md` (SHA256 `17924ce6bfa54fd9d78456d9a3aaacf3c4cbac46f2c4cc81126a9d65442ec622`) and its strictness addendum `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1-addendum-1.md` (SHA256 `81919e3af344b0414b17e8a61f19dd5b55db002de01e5a1b5fe24b7a299e77ef`).

## Theorem

If a real seven-state Metzler generator has `r>0` and the critical spectrum

`0, -r, -r, -1 +/- i*sqrt(8/9)` with the complex pair repeated twice,

then necessarily `r>27/8`. This is topology independent and needs no input/exit vectors. It is conditional on the two hidden roots actually coinciding; it does not imply that they do.

## Centered second and third moments

Let `h=(4+2r)/7` and `X=G+hI`, so `tr X=0`. Exact expansion gives

`tau2=tr X^2=2*(45r^2-72r-58)/63`,

`tau3=tr X^3=-2*(45r^3-108r^2+260r-354)/147`.

For any real Metzler matrix, symmetrize off-diagonal pairs by `S_ij=sqrt(X_ij*X_ji)` and keep diagonals. Then `tr S=0`, `tr S^2=tau2`, and `tau3>=tr S^3` by AM-GM on opposite oriented triangle products. For every traceless symmetric seven-by-seven matrix,

`tr S^3 >= -(5/sqrt(42))*(tr S^2)^(3/2)`.

This is the standard compact fixed-square-sum extremum: at the minimum six eigenvalues are equal positive and one is their negative sixfold multiple. Consequently if `tau3<0`, a necessary inequality is

`(25/42)*tau2^3-tau3^2 >=0`.

Here exact expansion is

`(25/42)*tau2^3-tau3^2 = (8/107163)*F(r)`,

`F(r)=18225r^6-87480r^5+1701r^4+410670r^3-471474r^2+271080r-360506`.

## Excluding the whole interval

The preceding source already gives `r>=4/5+sqrt(434)/15>21/10`. For `r>=21/10`, the cubic `45r^3-108r^2+260r-354` is strictly positive: at `21/10` it is `26493/200>0`, and after writing `r=21/10+t` its derivative is `(540t^2+1404t+1607)/4>0`. Thus `tau3<0` throughout the remaining range.

On the whole interval `[21/10,27/8]`, write `r=21/10+(27/8-21/10)t`, `0<=t<=1`. The degree-six Bernstein coefficients of `-F` are exactly

`1753050059/40000`, `15633558221/160000`, `701551117387/3200000`, `1060702289477/2560000`, `1306790852311/2048000`, `234237010993/327680`, `47222523911/262144`.

Every coefficient is strictly positive; hence `F<0` on the entire closed interval. This contradicts the centered-third-moment necessary inequality. The coefficient list and both trace identities were expanded in the owner's SymPy kernel using exact rational arithmetic; their displayed values are independently checkable with the usual power-to-Bernstein conversion. Therefore `r>27/8`. □

The exact algebraic threshold from the unique positive root of `F` lies above `27/8`, but no claim about its uniqueness or exact isolation is needed here. This repeated-hidden-root obstruction does not decide the hidden-root type, the existence of an actual PH7 representation, the minimum PH order, novelty, formal proof, independent scientific review, or parent adoption.
