# Three further three-syndrome q=8 classes

**Status: WRITTEN with exact rational multi-branch certificates; independent scientific review pending.** In the q=8 binary triangle-factor R-minus encoding, let the full syndrome support have at most three states, labelled `0,1,2`. Assume each of the ten binary factor-syndrome coordinates is a **nonconstant** function of those states. Every such coordinate, after an independent fixed bit translation, is the indicator of one of the three states. Suppose its factor-index color classes are one of the three following partitions, up to state relabeling:

\[
\begin{array}{c|c|c}
\text{class 0}&\text{class 1}&\text{class 2}\\\hline
\{1,2,6,8\}&\{3,4,7,10\}&\{5,9\}\\
\{1,2,5,6,8,9\}&\{3,10\}&\{4,7\}\\
\{1,2,6,8\}&\{3,10\}&\{4,5,7,9\}
\end{array}\tag{56}
\]

For every original-neighbour FD law on such a syndrome support, with arbitrary probabilities and correlations, `Delta<=0`; any uniform FD support has at most `2^20` words. The middle row's proof is **conditional on** the repaired two-syndrome theorem `frontier-20261028-two-syndrome-repaired-theorem-v1.md` SHA-256 `9feb6cd50a2b376b971c2091369b5c5ad7d50e18446ce4cd3293bfc718b776b1`. The first and third rows need only the full-syndrome conditional-factor gate and do not import the two-syndrome theorem. None of the four three-state color classes in (56) or the bipartition theorem covers all possible q=8 three-syndrome configurations.

## Proof and exact certificates

Each factor color `j` means its syndrome is the one-hot indicator `1{S=j}` after translation; all ten factor syndromes are nonconstant on the three-state support. Every vertex is incident to at least two colors in each row of (56). Original-neighbour graph FDs make the incident factor indicators functions of the neighbourhood, and any two distinct one-hot indicators determine the full state `S`; hence `S` is a function of every original neighbourhood. A factor triangle exposes its own one-hot indicator. Given `S` the factor parities are fixed, so each vertex block is determined by the other components of its incident triangles and `S`, including across the missing-edge issue recorded in required pre-source erratum `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f`.

Full-syndrome conditional triangle tensorization gives the nonpositive gate `3H(X_V)+17H(S)-2 sum_v H(X_v,S)<=0`. If an indicator `Y=1{S=j}` is used instead, the two fibers of `Y` contain one and at most two syndrome states respectively. The repaired two-syndrome theorem therefore supplies the same gate with `Y` in place of `S`; this extra import is used only for the middle row of (56). The one-hot KL/concavity inequalities and Shannon data-processing rows are as in `frontier-20261028-three-syndrome-bipartition-theorem-v1.md` SHA-256 `7217a2ebe34f1f7be40b61b1ddcd7ae90c62739f3d2fcc0f8d3a08e63f35ca0f`.

Three exact rational coefficient identities are pinned in order:

* `frontier-20261028-three-syndrome-color1-dual-v1.json` SHA-256 `2dcd1fc6a69d3a8f6d35b41c83a829b879db26590472adbfa69be7701be42ea6` (443 rows).
* `frontier-20261028-three-syndrome-color2-dual-v1.json` SHA-256 `61011d062f409e884371b64957748c228f1d5882a9c3d11a57201a516124310f` (661 rows; indicator-gate import).
* `frontier-20261028-three-syndrome-color3-dual-v1.json` SHA-256 `af8a2494c8c4e29076b99817c16ddb53a90344927900fe8b3bcca5a8c3e0c04a` (531 rows).

Each identity averages rows over the four factor-preserving graph automorphisms, expresses `Delta` as negative nonnegative terms, positive nonpositive terms and vanishing equalities, and therefore establishes the respective inequality under its stated assumptions. The independently written checker `frontier-20261028-three-syndrome-color123-dual-check.py` SHA-256 `559afd9857d7ba7fbfa3ba23217f56f35b9ba186a2b5c2514670f4a47a260e1c`, receipt SHA-256 `9185f8a4007c87281eccb3768d05055347e508123defc73aa0bb23978b30da10`, checks color-preserving automorphisms, each stated local/indicator incidence premise, all signs and all 5,119 branch coefficients per identity exactly, with altered-target and changed-CMI-sign controls.

All three claims, their indicator-gate import where used, and the one-hot entropy proofs await independent scientific review. They are not proof-assistant formalizations, novelty clearances, general three-state no-go results, or new numerical guessing-number bounds.
