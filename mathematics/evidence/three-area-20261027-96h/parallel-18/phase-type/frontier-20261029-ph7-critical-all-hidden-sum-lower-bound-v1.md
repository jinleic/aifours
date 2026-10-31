# A universal lower bound on the hidden-pole sum at 8/9

Status: **WRITTEN-checked with exact stdlib Fraction/Bernstein arithmetic**, pending disjoint scientific review. This is a topology-independent necessary condition on the actual hidden quadratic, including both real and complex roots. It is not a PH7 existence/exclusion verdict.

## 1. Theorem

Let a real seven-state Metzler generator have spectrum `0` and the critical pair `-1 +/- i*sqrt(8/9)` each twice, together with two other eigenvalues forming a real quadratic `Q(y)=y^2+p*y+q`. If those hidden eigenvalues lie strictly in the left half-plane, then

`p > 49/10`.

The stronger bound `p>3437/500` holds when both hidden eigenvalues are real, by `frontier-20261029-ph7-critical-all-real-hidden-roots-bound-v1.md` (SHA256 `f8f60590ff771dfde36c2693af8b1816208c5ba83ae700f45f8c88e128ec3512`). The present theorem proves the weaker `49/10` bound without assuming their reality. A critical PH7 representation supplies strict hidden stability through the previously supported irreducibility/Perron normalization. No claim is made that any hidden spectrum satisfying the bound is Metzler- or PH-realizable.

## 2. Complex hidden pair

It remains to consider hidden eigenvalues `-r +/- i*h` with `r>0`, `h>0`; then `p=2r`. Put `v=h^2`. Center `G` by adding `(4+2r)/7` times the identity. The exact centered traces are

`tau2=2*(45r^2-72r-63v-58)/63`,

`tau3=-2*[45r^3-108r^2+260r-354-(315r-252)*v]/147`.

The Metzler trace-square inequality gives `tau2>=0`, hence

`45r^2-72r-58>=0` and `0<=v<=V(r):=(45r^2-72r-58)/63`.

The quadratic is strictly negative for `0<=r<=43/20` (endpoint values `-58,-383/80`), so `r>43/20`.

Suppose for contradiction `r<=49/20`. Since `315r-252>0`, the square bracket in `tau3` is bounded below by its value at `v=V(r)`, namely

`-2*(90r^3-216r^2-131r+293)`.

Its Bernstein coefficients on `[43/20,49/20]` are exactly `2965/16`, `59063/400`, `35253/400`, `751/400`, all strictly positive. Therefore `tau3<0` on the entire admissible strip.

Metzler geometric-mean symmetrization and the seven-dimensional traceless-symmetric trace extremum then give

`(25/42)*tau2^3-tau3^2 >=0`.

With `F,C,D` defined in the all-real source, exact expansion yields

`(107163/4)*[(25/42)*tau2^3-tau3^2] = 2F(r)-C(r)*v+D(r)*v^2-127575*v^3`.

The stdlib `Fraction` checker `frontier-20261029-ph7-complex-hidden-low-mean-fraction-check.py` (SHA256 `dfb544ef599781ad4a3f47fc546a8d28e3d232ec6f406cb68e4ad1abfb439da3`) substitutes `r=43/20+(3/10)*s`, `v=t*V(r)`, `0<=s,t<=1`, reconstructs the exact degree-`(6,3)` polynomial, and verifies that **all 28 Bernstein coefficients of its negative are strictly positive**. It returned PASS, with scaled minimum `394710459840`. Hence the moment expression is strictly negative throughout the admissible strip, a contradiction. Therefore `r>49/20`, so `p=2r>49/10`.

The checker is independently written exact code by the same owner, not a disjoint scientific review or formal proof. The stated hidden-root stability is essential; nonreal hidden roots with arbitrary positive real part are outside scope. No actual PH witness, PH8 result, minimum-state claim, novelty, parent adoption, or complete `8/9` verdict follows.
