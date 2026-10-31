# Invalid exploratory mixed-plane symmetry proposal

`frontier-20261028-three-syndrome-mixed-plane-equivariant-lp.py` used the wrong nontrivial graph permutation for the selected factor set `{3,4,7,10}` and its two parity-color classes. That permutation does not preserve the selected four-factor set, so its orbit-reduced model is **not a valid relaxation for all laws in the stated class**. Any numerical result produced by that script is NONINPUT and must not be interpreted as an entropy bound or feasibility result.

The corrected successor `frontier-20261028-three-syndrome-mixed-plane-corrected-lp.py` uses the factor automorphism taking the two selected colors to each other. Its output remains a numerical proposal only until independently checked exact identities are produced and the mathematical premises are reviewed. The error did not affect the earlier exact certificates, the 206-color theorem, the 41-plane fractional method boundary, or the factor-plane census.
