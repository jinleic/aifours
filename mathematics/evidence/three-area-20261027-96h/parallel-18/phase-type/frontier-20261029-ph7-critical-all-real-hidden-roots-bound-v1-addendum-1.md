# Addendum: the all-real hidden-root mean bound is strict

Status: **WRITTEN-checked-in-kernel with exact rational polynomial arithmetic**, pending independent scientific review. This immutable successor strengthens `frontier-20261029-ph7-critical-all-real-hidden-roots-bound-v1.md` (SHA256 `f8f60590ff771dfde36c2693af8b1816208c5ba83ae700f45f8c88e128ec3512`) from `r>=r_*` to

`r>r_*`

for **any** two stable real hidden roots `-(r+h),-(r-h)`, `r>|h|`. The exact root `r_*` is the unique zero in `[27/8,7/2]` of the explicitly pinned degree-six polynomial `F` in that source. The result is a necessary spectral condition, not an existence/exclusion verdict for PH7.

## 1. Equality forces a rigid symmetrized matrix

The parent source proves `r>=r_*` through the centered moment polynomial

`E=2F(r)+C(r)h^2+D(r)h^4+127575h^6 >=0`.

On `[27/8,7/2]`, it proves the bracket `C(r)+D(r)v+127575v^2` strictly negative for every `0<=v<=r^2`. At `r=r_*`, `F(r_*)=0`, so `E>=0` forces `h=0`; the repeated-hidden spectrum then saturates

`tau3 = -(5/sqrt(42))*tau2^(3/2)`, `tau2>0`.

For the centered Metzler matrix `X=G+[(4+2r_*)/7]I`, let `S` have the same diagonal and off-diagonal entries `S_ij=sqrt(X_ij X_ji)`. Then `tr S^2=tau2` and `tr X^3>=tr S^3`. Equality in the seven-dimensional traceless symmetric minimum gives

`S=a*(I-7vv^T)`, `a>0`, `||v||=1`,

with eigenvalues `-6a,a,...,a`; it also forces `tr X^3=tr S^3`. Because `S_ij>=0` for `i!=j`, the coordinates of `v` have pairwise nonpositive products, so **at most two coordinates are nonzero**. Hence the bidirectional graph of `X` has at most one edge pair.

## 2. Triangle equality and fourth trace

In the trace-three symmetrization comparison, the discrepancy for each unordered triangle is three times the nonnegative difference between the two oriented products' arithmetic sum and twice their geometric mean. Since `S` has at most one bidirectional edge, every symmetric triangle product vanishes. Equality `tr X^3=tr S^3` therefore forces **every directed triangle product of X to vanish**.

Write `X=D+A` with zero-diagonal nonnegative off-diagonal `A`. The exact length-four walk expansion then contains no triangle/one-diagonal terms. All diagonal and two-cycle terms agree with those of `S`; the sole possible bidirectional pair contributes `2*(A_ij A_ji)^2` to both `tr(A^4)` and `tr(S_off^4)`. Every other length-four off-diagonal closed walk of `X` is nonnegative. Consequently

`tr X^4 >= tr S^4 = (13/14)*tau2^2`,

because the eigenvalues `-6a,a,...,a` have fourth sum `1302a^4` and square sum `42a^2`.

For the formal repeated-hidden spectrum at `r=r_*`, direct expansion instead gives

`tr X^4-(13/14)*tau2^2 = -4*H(r_*)/27783`,

`H(r)=9315r^4-29808r^3-5634r^2+26424r+23971`.

Here `H(27/8)=457296691/4096>0`, and putting `r=27/8+t` gives

`H'(r)=(9/128)*(529920t^3+4093632t^2+9363400t+5720161)>0` for `t>=0`.

Thus `H(r_*)>0` and the displayed fourth-trace difference is strictly negative, contradiction. Equality is impossible, proving `r>r_*`.

The fourth-trace algebra and rational polynomial signs were checked in the owner's SymPy kernel. The equality characterization, AM-GM termwise implication, and all closed-walk multiplicities are written arguments needing disjoint scientific audit; no formal proof or parent adoption is claimed. This result says nothing about nonreal hidden poles or actual PH7 existence at `8/9`.
