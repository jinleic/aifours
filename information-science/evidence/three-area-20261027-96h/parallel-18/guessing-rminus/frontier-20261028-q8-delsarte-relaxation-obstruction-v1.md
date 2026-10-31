# A support-orbit Delsarte relaxation is too weak for the q=8 target

**Status: WRITTEN with an exact checked fractional LP point; scientific review pending.** A natural q=8 Fourier/Delsarte relaxation of the original graph-confusability code contains a rational feasible point of objective

\[
\frac{2256535552}{1181}>\frac32\,2^{20}.
\]

Thus this specified relaxation **cannot prove** the desired q=8 triangle-code bound `|W|<=2^20`, and is even weaker than the inherited entropy bound on q=8 cardinality. The rational point is not an actual code, entropy law, or proof of the relaxation's optimum. This is a documented obstruction to this particular representation, not a new guessing-number upper or lower bound.

## The relaxation

Identify each q=8 alphabet with `F_2^3`. For an FD-consistent set `W`, define `a_S` as the average number of ordered partners whose bitwise difference from a word has vertex support `S`. Then `a_empty=1`, `a_S>=0`, and `sum_S a_S=|W|`. A nonempty difference support is allowed only if the induced R-minus subgraph has no isolated vertex; otherwise the two words conflict at an isolated vertex. Exactly 911 of the 1,024 support masks, including the empty mask, are allowed.

Average the difference distribution over independent invertible linear alphabet maps at each vertex and over the eight checked graph automorphisms. For each character-support mask `T`, Fourier nonnegativity gives

\[
\sum_{\mathcal O}\frac{a_{\mathcal O}}{|\mathcal O|}
\sum_{S\in\mathcal O}\left(-\frac17\right)^{|S\cap T|}\ge0,\tag{16}
\]

where `O` runs over graph-automorphism orbits of allowed supports and `a_O` is their total mass. Indeed, the Fourier transform of the ordered difference distribution is the squared modulus of the Fourier transform of the word indicator; for a nonzero character on `F_2^3`, the average over the seven nonzero alphabet differences is `-1/7`. The LP maximizes `sum_O a_O` subject only to nonnegativity, normalization and (16). Graph symmetry reduces it to 162 support orbits and 186 character-support orbits.

The pinned fractional point has denominator 4,724, nonnegative orbit masses, correct normalization and all 186 exact Fourier inequalities. Its objective is the rational above. It need not be realizable by any word set.

## Comparison with the inherited upper bound

The source upper bound `gn(R-minus)<=1847/276` would give `|W|<=8^(1847/276)=2^(20+7/92)`. Because `7/92<1/2` and `sqrt(2)<3/2`, this is strictly below `(3/2)2^20`, while the feasible relaxation point is strictly above that quantity. The corrected publisher reference must be read before the frozen f110 source packet: `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`.

## Exact evidence

Candidate `frontier-20261028-q8-delsarte-primal-v1.json` SHA-256 `9608294d56bcaa625fe4f59d113e1adda279b22fc5e8cd05d4d4587193b21fbf`; checker `frontier-20261028-q8-delsarte-primal-check.py` SHA-256 `bf68002219e64199f8b93bc3208e25f54d05acd747299c7cd1ec7fda385f9e50`, receipt SHA-256 `13af8650aa2233cc9a66549220229220bb05eb67968363f0a6b64642e70fd355`. The checker rebuilds all support/character orbits, evaluates the 186 Fourier rows using integer arithmetic, verifies the exact objective and rejects normalization, negative-mass and Fourier-violation mutations. The LP solver only proposed this point; no floating status is used as proof, and no dual-optimality claim is made. The Fourier/relaxation correspondence is written mathematics and has not received independent scientific review.
