# Privacy v241 parent checkpoint — Markdown delimiter correction

Actual clock immediately before writing: **2026-10-27T08:47:33-0700 PDT**. The frozen [parent written checkpoint](privacy-v241-parent-separated-proof-checkpoint-v1.md) has SHA-256 `75e33e850fc83ac03f7a6a30107b014f89f29c95718c3ca43ddc3870e9f5bdc3`. Several inline-code closing delimiters in its sections A and B were accidentally typed as closing parentheses, producing misleading Markdown rendering. The source remains immutable. Read its argument with these literal replacements; this is a documentary MINOR, not a new computation or a change of scope.

- In section A, the constrained derivative is nonpositive for every `0 <= y <= q_*/2`.
- In section B set `d=1-12v`, `N=36m²+48m+11`, `w=2m+1`. In the regime `d>0`, the positive remainder zero is `q_c=mN/d`. One has `q_c>11m>2m` and, for the entire range `0<m<=1/4`, `P(2m)=m²(256m³-8m²-22m-1)<0`; hence `q_c>q_a`.
- The displayed equivalence is `Q(q_*)>=0 iff q_*<=q_c iff P(q_c)>=0 iff Q(q_c)<=0`.
- Set `x=q+m`. Then `Q=-x³+3vx+2vw`, `x_c=12vw/d`, and `d³Q(q_c)=vw[2-36v-1728v²-5184v³]=vwK(v)`.
- `s³K(1/(4s))=2s³-9s²-108s-81`. When `d<=0`, one has `s<=3`, so `2s³<=6s²` holds over the whole stated range. There is a unique positive cubic root `s_t`, and `s=sinh²(epsilon/2)` is strictly increasing. The candidate diamond criterion is `epsilon<=2 arcsinh(sqrt(s_t))`.

The proof is still only the parent pre-review written checkpoint. Both v241 reviews remain pending, v227 is binding, all selected-check consumers are ZERO and the threshold/regime claims are HELD until a separate disposition. No hidden source read, selected probe or stronger verification is claimed.
