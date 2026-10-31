# Addendum: explicit vertex and triangle orbits

For the exact all-syndrome inequality `frontier-20261028-compact-full-syndrome-inequality-v1.md` SHA-256 `3d40fe8179a05b77f3688b31fea2cfbb3a831c218c2a24d3efa58ddf6d85eb17`, the three averaged terms can be written without automorphism notation:

\[
\begin{aligned}
12\Delta(X)\le{}&\sum_{v\in\{2,5,9,10\}}H(S\mid X_{N(v)})\\
&+2\sum_{v\in\{6,7\}}H(S\mid X_{N(v)})\\
&+\sum_{T\in\{123,145,389,4\,8\,10\}}H(S\mid X_T).
\end{aligned}\tag{42}
\]

The first vertex orbit has size four, the second size two with multiplicity two, and the triangle orbit has four elements; these are the images of the checked four-element group in certificate `frontier-20261028-common-syndrome-compact-dual-v1.json` SHA-256 `580416bde07e8009210f1e9cef3272c4a465f8693c35cfd67046e6bdbc6353a9`. This is only a notational expansion of (41), with all the same group-factor/full-syndrome assumptions and the same limitations; it is not a separate claim of a numerical upper bound.
