# Canonical additive global amalgam fails Shannon

**Status: WRITTEN, exact integer-checked for one explicit representation.** Let `X=(a,...,j)`, `U=b'0`, `V=(d'1,e'1,g'2)` and `W=(f'3,g'3,h'4)`. Form the canonical additive set function on all 17 variables from the unchanged rational star profiles:

\[
h_{\mathrm{add}}(S)=h_{XUV}(S\cap(X,U,V))+h_{XUW}(S\cap(X,U,W))-h_{XU}(S\cap(X,U)).
\]

It matches both star profiles on their respective blocks and has `I((U,V);W|X)=0`. Nevertheless it is **not** a Shannon polymatroid: exact computation gives the explicit violated elemental inequality

\[
I(e;f\mid a,c,d,g,h,i,e'1,f'3,g'3,h'4)
=-\frac{1233917}{2300000}.
\]

The checker computes all `17+binom(17,2)*2^15 = 4,456,465` elemental rows by scaled integer arithmetic; 90,351 are negative for this particular additive formula. Thus this obvious closed-form amalgamation cannot certify a full 17-variable extension of the chosen star point. This does **not** rule out any other Shannon amalgam, exclude the original base profile, or give a guessing-number bound.

Evidence: `frontier-20261028-global-parallel-sum-check.py` SHA-256 `863466c3001d0ee5405551a89fdf7d39e087d561068160164e9969e0c2a057e8`, receipt `frontier-20261028-global-parallel-sum-check-result.json` SHA-256 `cfba4f73209467d9c2ac8d6788ad60c0accee454b2c5fc942430d41766ff83a8`. The receipt pins original vector SHA-256 `aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651`, star 1 SHA-256 `1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739`, and star 2 SHA-256 `e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474`.
