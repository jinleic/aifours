# Addendum 3: the exact algebraic repeated-hidden-root threshold

Status: **WRITTEN-checked-in-kernel using exact rational symbolic expansion**, pending independent scientific review. This is an additive sharpening of `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1-addendum-2.md` (SHA256 `8a8e858e11f49e69c7db16f152de2ea578d4b3b048203bec3ada7bd0c44acd35`).

Let

`F(r)=18225r^6-87480r^5+1701r^4+410670r^3-471474r^2+271080r-360506`.

The repeated-hidden-root hypotheses of the preceding addendum imply the **exact necessary bound**

`r >= r_*`,

where `r_*` is the unique real zero of `F` in `[27/8,7/2]`. In particular `r_*>3437/1000`. This is a bound on the repeated hidden decay rate, not a PH7 existence/exclusion verdict.

## Proof

The preceding addendum establishes that any such `r` obeys `r>27/8`, that its centered third trace `tau3<0`, and that `F(r)>=0` is necessary. Put `r=13/4+t` with `t>=0`. Exact expansion gives

`F'(r)=109350t^5+(2679075/2)t^4+(23482791/4)t^3+(177854859/16)t^2+(1052052975/128)t+667306647/512 >0`.

Thus `F` is strictly increasing on `[13/4,infinity)`. At the two rational endpoints,

`F(27/8)=-47222523911/262144 <0`,

`F(7/2)=14829109/64 >0`.

The intermediate value theorem and strict monotonicity give the unique `r_*` in the stated interval and make `F(r)>=0` equivalent to `r>=r_*` there. Finally

`F(3437/1000)=-54167280737148221039/40000000000000000 <0`,

so `r_*>3437/1000`. All polynomial/rational identities were computed with exact SymPy arithmetic in the owner's kernel; the displayed algebra is independently checkable. The bound permits equality at `r_*`; this addendum does not claim a realization at equality or a stricter root condition.

The previously noted relevant independent-review, Perron-normalization, formal-proof, novelty, and parent-adoption boundaries remain unchanged. Coincidence of the hidden roots is an explicit hypothesis, not a conclusion; PH7 at `8/9` remains open.
