# The fixed star-LP primal is not jointly entropically realizable

**Status: WRITTEN with a separately checked exact nine-row Shannon identity.** This is an additive correction to `frontier-20261028-crossbranch-star-optimum-v1.md` (SHA-256 `1fb4cb0a74fd288e7fd96aaa2aba50b21901cd4385fa845ba28aa4a1656a54bf`). The exact star-LP optimum `1847/276` and its verified primal/dual are unchanged. The new statement concerns **that particular fixed star primal**, not its original-variable base profile with different auxiliary assignments.

## Exact cross-pair identity

Use the two pinned star candidates from the predecessor, let `X=(a,b,c,d,e,f,g,h,i,j)`, `U=b'0`, `D=d'1` and `F=f'3`. In the following table, all conditional mutual informations are Shannon-nonnegative, with the displayed conditioning variables:

| Row | CMI | Conditioning variables |
|---:|---|---|
| 1 | `I(b;d | ...)` | `a,c,e,f,g,h,i,j,D,F` |
| 2 | `I(c;d | ...)` | `a,b,e,f,g,i,j,D,F` |
| 3 | `I(c;F | ...)` | `a,b,e,f,g,h,i,j,D` |
| 4 | `I(d;D | ...)` | `a,c,e,f,g,h,i,j,F` |
| 5 | `I(h;D | ...)` | `a,b,e,f,g,i,j,F` |
| 6 | `I(h;F | ...)` | `a,b,c,d,e,f,g,i,j,D` |
| 7 | `I(D;F | ...)` | `a,b,d,e,f,g,i,j` |
| 8 | `I(D;F | ...)` | `a,b,c,e,f,g,i,j` |

As an entropy-vector identity, the sum of these eight CMIs minus `2 I(D;F|X)` cancels **every** entropy involving both `D` and `F`. The remaining 16 entropy terms involve only `X`, `(X,D)` or `(X,F)`. On the two **fixed** rational star marginals they evaluate exactly to

\[
\sum_{k=1}^8 I_k-2I(D;F\mid X)
=-\frac{12637}{1725000}.
\]

Thus any Shannon-polymatroid joint extension of these two fixed marginals must have

\[
I(D;F\mid X)\ge \frac{12637}{3450000}>0.
\]

In particular they have no Shannon joint extension with `I(D;F|X)=0`. This statement is stronger than the earlier floating infeasibility observation, but does **not** rule out an extension after changing either auxiliary marginal.

## Why the specific full star point cannot be entropic

Suppose a finite joint law realized both fixed star systems on a common `(X,U)` distribution. The star constraints include `I(U;V|X)=0` and `I(U;W|X)=0`, where `V=(d'1,e'1,g'2)` and `W=(f'3,g'3,h'4)`. Hence its two checked marginals factor respectively as

\[
P(X)P(U\mid X)P(V\mid X),\qquad
P(X)P(U\mid X)P(W\mid X).
\]

Replace the joint conditional kernel by their product `P(U|X)P(V|X)P(W|X)`. This preserves both full `(X,U,V)` and `(X,U,W)` distributions, hence all fixed `X,D` and `X,F` entropy values, while making `D` and `F` conditionally independent given `X`. The exact identity then contradicts Shannon nonnegativity. Therefore the particular star primal is not the marginal entropy profile of any single finite joint law, even up to positive entropy scaling.

This does **not** prove that the original 1,023-coordinate base profile is non-entropic: another choice of copies might work. It does not establish separation from the almost-entropic closure, nor does it show that the star LP optimum or the full all-cross-branch LP optimum is lower than `1847/276`.

The same argument yields a valid **new existential extension constraint** for original laws: when the three copy branches are sampled independently conditional on the original `X`, the 16-term known-marginal expression above must be nonnegative. It cuts this chosen star primal, but its effect after the auxiliary coordinates are reoptimized is not yet known.

## Evidence

* Source candidate/dual-ray producer `frontier-20261028-cross-pair-farkas.py` SHA-256 `b7abbc2f507c07534b44b6ff695469dd36441b16954113eeebaf20288f116a39`; ray receipt SHA-256 `5c28724b56f54b6f38d1b8828e449a1f9140f373e480e7dcb523c06b715088e3`. A floating solver only proposed the ray; its eight `+1` and one `-2` weights, cancellation and constant are exact.
* Independent verifier `frontier-20261028-cross-pair-farkas-independent-check.py` SHA-256 `b69af7b6bf2dad9726c8311c1d34e5ef9707a56218b2f3e38f50041e36245c51`; receipt SHA-256 `199a7471622c6c3085a669e2b43e7235676e680ee7e8cb3fa8f636449a1aff45`. It rebuilds every CMI and the independence expression from named masks, checks all signs, verifies cancellation of all mixed-auxiliary terms and the exact negative constant, binds the two independently checked star candidate hashes, and rejects five intended mutations.
* The other two tested cross pairs had floating infeasibility statuses only, and six further pairs had producer-exact candidates without independent checks. No conclusion about those pairs is adopted here.

No cross-model review, proof-assistant formalization, or novelty clearance was performed.
