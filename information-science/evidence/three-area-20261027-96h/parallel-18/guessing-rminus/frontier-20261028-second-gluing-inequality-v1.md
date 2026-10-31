# A second universal gluing inequality cutting the reoptimized star point

**Status: WRITTEN with separately checked rational identity and Shannon-cone witness; independent scientific review and novelty clearance pending.** This is separate from the f110 publisher-LP review and does not modify its inputs. The result does not establish a new original-graph numerical upper bound.

## Universal 18-term inequality

For arbitrary finite variables `X=(a,b,c,d,e,f,g,h,i,j)` and additional variables `D,F`, define

\[
\begin{aligned}
L_2={}&-H(abcdeghj)-H(abcghij)+2H(abcdefghij)\\
&+H(abcdeghjD)-H(abcfghjD)+H(abcghijD)+H(abcfghijD)-2H(abcdefghijD)\\
&-H(abcghjF)+H(abcdeghjF)+H(abcfghjF)+H(abcghijF)\\
&-H(acdeghijF)-H(abcfghijF)-H(acefghijF)+H(abcefghijF)\\
&+2H(acdefghijF)-2H(abcdefghijF).
\end{aligned}
\]

Every finite joint law satisfies **`L_2>=0`**, and the inequality extends to the almost-entropic cone. The exact coefficient identity is

\[
L_2=\sum_{k=1}^{11}I_k-2I(D;F\mid X),
\]

where the 11 positive CMIs are listed below. All mixed `D,F` entropy terms cancel from the left side. Given any law, replace its conditional distribution of `(D,F)` given `X` by `P(D|X)P(F|X)`. This preserves every entropy in `L_2`, makes the last CMI zero, and leaves the 11 positive CMIs nonnegative. This proves the inequality without any graph FD or initial independence assumption.

| Row | CMI | Conditioning variables |
|---:|---|---|
| 1 | `I(b;d | ...)` | `a,c,e,f,g,h,i,j,D,F` |
| 2 | `I(b;f | ...)` | `a,c,d,e,g,h,i,j,D,F` |
| 3 | `I(d;i | ...)` | `a,b,c,e,g,h,j,D,F` |
| 4 | `I(d;D | ...)` | `a,c,e,f,g,h,i,j,F` |
| 5 | `I(e;i | ...)` | `a,b,c,g,h,j,D,F` |
| 6 | `I(e;D | ...)` | `a,b,c,f,g,h,i,j,F` |
| 7 | `I(f;D | ...)` | `a,c,d,e,g,h,i,j,F` |
| 8 | `I(f;D | ...)` | `a,b,c,g,h,j,F` |
| 9 | `I(i;F | ...)` | `a,b,c,f,g,h,j,D` |
| 10 | `I(D;F | ...)` | `a,b,c,g,h,i,j` |
| 11 | `I(D;F | ...)` | `a,b,c,d,e,g,h,j` |

## Exact separation and scope

The independently checked all-45,360-first-cut star primal has `L_2=-867/460000` when `D=d'1` and `F=g'3`. Therefore those **fixed** auxiliary marginals are outside the projection of the almost-entropic cone. The original profile can still be entropic or almost-entropic with other auxiliary values. Since this same star primal satisfies the full stated 45,360-instance first gluing family, `L_2` is not implied by that specified star LP plus those first-family instances; this does not rule out other known inequalities or establish novelty.

The five variables `(a,c,g,h,j)` occur in every term and the coefficients sum to zero. Contracting this background yields a seven-variable inequality on `(b,d,e,f,i,D,F)`. A separate exact 12-variable Shannon polymatroid extension **without** imposing `I(D;F|X)=0` contracts to a seven-variable polymatroid satisfying all `7+21*2^5=679` elemental Shannon rows but with `L_2=-867/460000`. Thus the contracted inequality is non-Shannon-type on seven variables. It may still follow from known non-Shannon inequalities; no novelty is claimed.

The source upper bound `1847/276` and the no-improvement statements for previously defined LPs remain unchanged. Whether adding this second cut and reoptimizing all relevant copy marginals improves the original-graph bound is open.

## Evidence

* Ray producer `frontier-20261028-cross-pair-round2-farkas.py` SHA-256 `9ab9b45acf9c0962d03e7f44b4fa2a5811704ebaab5b7586df6f82aeb16f9aba`; exact ray receipt SHA-256 `a10333eff083b493edff9e791e2def45f3a5a55309310f643cc01113bc7369da`.
* Independent exact identity checker `frontier-20261028-cross-pair-round2-farkas-independent.py` SHA-256 `8c69e573d9396ac9e27b0cadf9c08305c49d3f74cb59d0241ac0eb76cf61eb89`; receipt SHA-256 `29341b5eb23bcfaecf7bc350514ff38f76b17b3de4d88326b4561778a897dff9`. It rebuilds all 11 CMIs and the `-2` conditional independence, checks cancellation to the 18 known terms and exact negative fixed value, and rejects five intended mutations.
* Independent Shannon-separation checker `frontier-20261028-seven-variable-gluing-separation-check.py` SHA-256 `4fe43776427161cd4a9a92c42ca384df45256ce74afc72d43fbc318187eae207`; receipt SHA-256 `e57660795859960adf42a055068773ae2218380ef2a560f902fe5fba87d2ed4d`. It checks all `67,596` 12-variable and 679 contracted seven-variable elemental Shannon rows; the receipt includes all 128 exact seven-variable values and the 18-term coefficient map.
* The source 12-variable Shannon-only candidate is `frontier-20261028-crosspair-round2-noind-candidate.json`, SHA-256 `558e3cfb52d5090beeac4362bff5a6a429cc27a64b285b5722d55043a26fcc92`. The all-first-family-cuts star primal and its independent 45,360-cut receipt are cited in `frontier-20261028-crossbranch-allcuts-optimum-v1.md` (SHA-256 `a298d0b9098613179f09883b9f28f4db9ff0e33c3e2b345781b1809ce84a3d6f`).

No cross-model review, proof-assistant verification, or comprehensive literature/novelty audit has been performed.
