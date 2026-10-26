# Operative algebra correction for the reverse-separation candidate

Observed before creation: **2026-10-23T14:29:39-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. Original snapshot preserved unchanged:

`proof-reverse-feasibility-separation-v1.md`, SHA256 **33a3e60e43ef8e83f4351824fc708467728243a54846fda349350cabae10bb0f**.

The last displayed expansion in §7, immediately after equation(24), has a non-load-bearing coefficient error. The **correct identity** is

\[
\begin{aligned}
 &(1-\delta/2)-(1+\delta/4)(1-\delta)(1+\delta/8)\\
 &\qquad=\delta/8+11\delta^2/32+\delta^3/32>0.
\end{aligned}
\]

Indeed `(1-delta)(1+delta/8)=1-7delta/8-delta^2/8`; multiplying by `(1+delta/4)` gives `1-5delta/8-11delta^2/32-delta^3/32`. Subtraction gives the displayed corrected expression. The original coefficient `3/16` was not equal to `11/32`. Its sign was positive in either case, but the original equality must not be quoted as valid.

An even shorter inequality avoiding the expansion is:

`(1-delta)(1+delta/8)<1-7delta/8`,

`(1+delta/4)(1-7delta/8)=1-5delta/8-7delta^2/32<1-delta/2`.

Thus the strict controller lower bound at gamma16386 remains unchanged. No parameter, stochastic argument, norm, source, controller quantifier, horizon or claimed implication changes. This correction was found by the author's written self-check before requesting review; no executable arithmetic was used. Review the original snapshot **together with this additive correction**, not by silently substituting edited source bytes.
