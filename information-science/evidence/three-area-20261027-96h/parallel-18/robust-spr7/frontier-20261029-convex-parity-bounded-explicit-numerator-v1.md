# Explicit numerator for every bounded truncation of the convex septic family

**Status: WRITTEN candidate, not parent adoption.** In the convex fixed-odd family of `frontier-20261029-convex-septic-parity-compactness-addendum-v1.md`, define \(K_M\) by \(u,v\ge0\) and \(1\le u+v\le M\), for any real \(M\ge1\). Put
\[
\varepsilon_M=\frac{1}{2\,7^6M},\qquad
E_b=\varepsilon_M E_A,\quad O_b=O.
\]
Then this explicit monic septic \(b_M\) is strictly positive real against **every** member of \(K_M\). Thus the compact fixed-parity theorem's existence is realized here without searching or invoking a root-count algorithm.

Indeed
\[
P_{a_{u,v},b_M}(t)=tO(t)^2+
\varepsilon_M\bigl(uE_A(t)^2+vE_A(t)E_B(t)\bigr).
\]
The product \(E_AE_B\) is negative only on
\((1/2,3/4)\cup(2,3)\cup(6,7)\). On these intervals \(0<t<7\) and each of its six linear root factors has absolute value at most 7, hence \(|E_AE_B|\le7^6\). Meanwhile \(tO^2>1\): on the three intervals, lower bounds are respectively \(\tfrac12(429/64)^2\), \(2\cdot6^2\), and \(6\cdot20^2\). Since \(v\le M\), the potentially negative contribution has magnitude at most \(1/2\), and the pairing is positive.

Outside these intervals both displayed summands are nonnegative. They cannot vanish simultaneously: at \(t=0\) the even product is positive, and at the only positive zeros \(1,4,9\) of \(O\), both \(E_A,E_B\) have the same nonzero sign, with \(u+v\ge1\). The normalized infinity limit is 1. Thus the common SPR property follows on the entire half-line and for the whole convex family. The companion noncompact theorem proves **no fixed numerator** works uniformly for all \(M\); this does not contradict these parameter-dependent explicit numerators and does not decide any arbitrary original box.

All inequalities here are written elementary arithmetic, using the factorizations checked in the preceding septic compactness packet. No formal proof, cross-vendor review, novelty clearance or unrestricted original-box conclusion is claimed.
