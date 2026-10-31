# A third gluing inequality from the reoptimized star point

**Status: WRITTEN with independent exact identity and Shannon-cone checks; scientific review and novelty clearance pending.** This is a separate successor to `frontier-20261028-second-gluing-inequality-v1.md` (SHA-256 `fac5ba03c3b65e022990e3f379d0e6f51e91180b6edb007657725e1404a3adcf`). It neither changes the f110 review inputs nor improves the original R-minus numerical bound.

## Universal 18-term inequality

For arbitrary finite `X=(a,b,c,d,e,f,g,h,i,j)` and additional variables `D,F`, define

\[
\begin{aligned}
L_3={}&-H(abcehi)-H(acefghi)+2H(abcdefghij)\\
&+H(abcefhiD)+H(acefghiD)-H(acefhijD)+H(abcefhijD)-2H(abcdefghijD)\\
&+H(abcehiF)-H(acefhiF)+H(acefghiF)-H(abcefghiF)\\
&-H(abcdfhjF)+H(abcdfghjF)+H(acefhijF)-H(abcefhijF)\\
&+H(abcdefhijF)-H(abcdefghijF).
\end{aligned}
\]

Every finite law satisfies `L_3>=0`, and the inequality extends to the almost-entropic cone. The independently checked entropy identity is

\[
L_3=\sum_{k=1}^{12}I_k-2I(D;F\mid X),
\]

with the positive CMI terms listed below. The left side uses only `(X,D)` and `(X,F)` marginal entropies. Replacing the joint conditional law of `(D,F)` given `X` by `P(D|X)P(F|X)` preserves all terms in `L_3`, makes the negative CMI zero, and proves the inequality from the twelve nonnegative CMIs. No graph FD or initial independence is assumed.

| Row | CMI | Conditioning variables |
|---:|---|---|
| 1 | `I(b;g | ...)` | `a,c,e,f,h,i,D,F` |
| 2 | `I(b;F | ...)` | `a,c,e,f,h,i,j,D` |
| 3 | `I(d;D | ...)` | `a,b,c,e,f,h,i,j,F` |
| 4 | `I(d;D | ...)` | `a,b,c,e,f,g,h,i,F` |
| 5 | `I(e;g | ...)` | `a,b,c,d,f,h,j,D,F` |
| 6 | `I(f;F | ...)` | `a,b,c,e,h,i,D` |
| 7 | `I(g;i | ...)` | `a,b,c,d,e,f,h,j,D,F` |
| 8 | `I(g;D | ...)` | `a,b,c,d,f,h,j,F` |
| 9 | `I(j;D | ...)` | `a,b,c,d,e,f,g,h,i,F` |
| 10 | `I(j;D | ...)` | `a,c,e,f,h,i,F` |
| 11 | `I(D;F | ...)` | `a,c,e,f,g,h,i` |
| 12 | `I(D;F | ...)` | `a,b,c,e,h,i` |

## Exact separation and reoptimization boundary

The independently checked two-family star primal has `L_3=-7123/3450000` at `D=g'2`, `F=f'3`. Thus those **particular** auxiliary marginals lie outside the projection of the almost-entropic cone. The primal passed all 45,360 tested substitutions of the first gluing inequality and, by two separately structured exact scans, all 272,160 active-role/per-pair substitutions of the second. Hence this specific `L_3` is not implied by that explicitly restricted star relaxation plus those tested first/second families. This does not rule out known inequalities or auxiliary derivations outside that relaxation.

Adding the one displayed `L_3` cut and reoptimizing the second star branch while holding the other branch and original profile fixed yields another exact candidate for which `L_3=5021/3450000>0`. A separate checker verifies its `372,750` Shannon rows, `1,539` copy equalities, seven cross-independence equalities, source rows, all 45,360 first-family cuts, 72 second-family cuts, and this third cut. Therefore the old fixed-point violation does **not** exclude even that fixed first-branch profile with a different third-branch assignment. No unrestricted graph upper improvement follows.

All terms of `L_3` contain the common background `(a,c,h)` and the coefficient sum is zero. Contracting that background gives a nine-variable valid inequality on `(b,d,e,f,g,i,j,D,F)`. An independently checked 12-variable Shannon polymatroid **without** conditional independence contracts to a nine-variable Shannon polymatroid satisfying all `4,617` elemental rows but with `L_3=-7123/3450000`. The contracted inequality is therefore non-Shannon-type on the nine-variable Shannon cone. This is a cone classification, not a novelty claim.

## Evidence

* Ray producer `frontier-20261028-cross-pair-round3-farkas.py` SHA-256 `ac27cf91a89c4759be237fc4f14a6b4d918c7148524b943a6e42a46d504a28be`; exact ray receipt SHA-256 `fc526f677044caff71bd12724acf4e47a7c0080573f83e828d2743e718976e76`.
* Independent identity verifier `frontier-20261028-cross-pair-round3-farkas-independent.py` SHA-256 `f346fb1459102d9919db1f40c2c96d5c82e49b02be8485462ddba04298750888`; receipt SHA-256 `b2e4e3d31006c40774601f0e91bd4ba6651aba1de9b4de3c75f87d64fd1904ac` reconstructs all 12 CMIs and `-2` independence, cancels the mixed terms, checks the exact constant and rejects five mutations.
* Nine-variable separation checker `frontier-20261028-nine-variable-gluing-separation-check.py` SHA-256 `33b781bf15aa9e8b352bb820ad12d5c7c2fb9e12eea224dcc22d0809b185e398`; receipt SHA-256 `486fe82f61fe70bef56027897f08422f8812115265bd5443c75cb524b6aea60c` includes all 512 exact nine-variable values and checks all 67,596 original 12-variable elemental rows and 4,617 contracted rows.
* Reoptimized third-cut candidate `frontier-20261028-crossbranch13-threefamilies-exact-candidate.json` SHA-256 `e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474`; separate checker `frontier-20261028-crossbranch13-threefamilies-independent-check.py` SHA-256 `93171f8cdd4b8be9d2b431390da3dfcace0e147ced774fe38d45b1a8000bc717`, receipt SHA-256 `cbbdb5f81e4c566eac413bc2b342737b6be556637fa765a171699b2d096616c5`.

No cross-model review, proof-assistant verification or comprehensive prior-art audit has been performed.
