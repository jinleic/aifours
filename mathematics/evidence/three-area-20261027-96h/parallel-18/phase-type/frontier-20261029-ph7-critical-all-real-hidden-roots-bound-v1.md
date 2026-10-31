# A global mean bound for any two real hidden poles at 8/9

Status: **WRITTEN-checked with separately implemented exact Fraction/Bernstein arithmetic**, awaiting disjoint scientific review and parent disposition. This removes the hidden-root gap restriction from the earlier near-equal theorem. It is a universal spectral necessary condition, not a proof that the hidden roots are real and not a PH7 existence/exclusion decision.

## 1. Theorem

Let a real seven-state Metzler generator have spectrum

`0, -(r+h), -(r-h), -1 +/- i*sqrt(8/9)` with the complex pair repeated twice,

where the two real hidden decay rates are positive: `r>|h|>=0`. Then, **with no upper bound on `|h|`**,

`r>=r_*`,

where `r_*` is the unique root in `[27/8,7/2]` of

`F(r)=18225r^6-87480r^5+1701r^4+410670r^3-471474r^2+271080r-360506`.

The previously pinned exact root analysis in `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1-addendum-3.md` (SHA256 `fa840d0d89681381968887d9ceedc73c284dc9c22ed903098fd5d2499e7e3f2b`) proves `r_*>3437/1000`. Equivalently, if the hidden quadratic is `y^2+p y+q` with two real negative roots, then `p>=2r_* >3437/500`.

## 2. Centered trace constraints

Put `v=h^2`. The exact centered traces from `frontier-20261029-ph7-critical-near-equal-hidden-root-bound-v1.md` (SHA256 `ecd97a65517447de61d4e129ad2da7b24f6b86378d66699d05796247ace6f19c`) are

`tau2=2*(63v+45r^2-72r-58)/63`,

`tau3=-2*[315vr-252v+45r^3-108r^2+260r-354]/147`.

The Metzler trace-square inequality gives `tau2>=0`; positivity of the real hidden decay rates gives `0<=v<r^2`. Hence

`108r^2-72r-58>0`,

and therefore `r>569/500`: the quadratic is convex, strictly negative on `[0,569/500]` (its endpoint values are `-58` and `-4453/62500`), and `r>0`.

The bracket in `tau3` is strictly positive for all `r>=569/500` allowed by `tau2>=0`. On `[569/500,21/10]`, its coefficient of `v` is positive and `v>=(-45r^2+72r+58)/63`; substituting gives

`-2*(90r^3-216r^2-131r+293)`.

The latter polynomial has positive Bernstein coefficients on that interval:

`39613719/6250000`, `68022289/375000`, `90043/300`, `10117/50`.

For `r>=21/10`, the bracket with `v=0` is already positive and increasing, and its coefficient of `v` is positive, as established in the repeated-root addendum `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1-addendum-2.md` (SHA256 `8a8e858e11f49e69c7db16f152de2ea578d4b3b048203bec3ada7bd0c44acd35`). Thus `tau3<0` in the entire feasible real-root domain.

Metzler geometric-mean symmetrization and the seven-dimensional traceless-symmetric trace extremum imply

`E(r,v):=(107163/4)*[(25/42)*tau2^3-tau3^2] >=0`.

The exact polynomial is

`E=2F(r)+C(r)*v+D(r)*v^2+127575*v^3`,

`C(r)=27*(2025r^4-6480r^3-40212r^2+94860r-20756)`,

`D(r)=-486*(450r^2-720r+1373)`.

## 3. Strict exclusion below 27/8

On `r in [569/500,27/8]`, write `v=r^2*t` with `0<=t<=1`. The separately implemented stdlib `Fraction` checker `frontier-20261029-ph7-hidden-all-real-low-mean-fraction-check.py` (SHA256 `c8621e51a9604b9cdd89986abb39c19be4d529954a9b11559154e91ba983faa8`) reconstructs `-E`, converts the exact degree-`(6,3)` polynomial to Bernstein form on the entire rectangle, and builds a complete binary cover with **47 strictly positive leaves**. It returned PASS. Therefore `E<0` on the entire feasible strip, contradicting the necessary moment inequality.

## 4. Exclusion from 27/8 to r-star

For `r in [27/8,7/2]`, both `C(r)` and `C(r)+D(r)*r^2+127575*r^4` are strictly negative. On that interval the degree-four Bernstein coefficients of their negatives are respectively

`16038045981/4096`, `4084345593/1024`, `1039208589/256`, `264168513/64`, `67088061/16`,

`20249163297/2048`, `5204656809/512`, `1337579919/128`, `343709919/32`, `88310277/8`.

For fixed `r`, the bracket `C+D*v+127575*v^2` is convex in `v`; its two endpoint values on `[0,r^2]` are negative, so the bracket is negative throughout. Thus the `v`-dependent correction to `E` is nonpositive and `E<=2F(r)`. The pinned root analysis proves `F(r)<0` on `[27/8,r_*)`, again contradicting `E>=0`. Therefore `r>=r_*`, proving the theorem.

The 47-leaf Fraction program is independent code by the same owner, not independent scientific review or formal verification. This result assumes **two real hidden roots** and does not cover a nonreal hidden conjugate pair; it establishes neither an actual PH realization nor minimum state count, novelty, parent adoption, or the full 8/9 decision.
