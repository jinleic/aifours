# Fractional reconstruction cannot resolve the 41 residual four-factor planes

**Status: WRITTEN with exact independently checked rational primal/dual certificates; scientific review pending.** In `frontier-20261028-fourfactor-plane-color-theorem-v1.md` SHA-256 `09cb78a5bcd1d811f45d087dad567a49ce4f9f9ca898a0fcde3ef96efa0bb4ca`, 206 of the 247 four-varying-factor covering planes have universal 3-color reconstruction. For each of the other 41, define a vertex set `I` to be safe when it contains no allowed nonconfusable active difference mask from the entire syndrome plane; then its complement reconstructs every possible FD support in that plane. The fractional universal-reconstruction-cover optimum is

* `10/3` for **37** planes;
* `7/2` for **4** planes.

Both exceed 3. Therefore **no** nonnegative fractional combination of these universal safe-set reconstructions can yield the required two-thirds entropy bound for any of the 41. In particular no universal three-color reconstruction exists, because it would give a cover of total weight 3. This is an exact boundary of this **specific universal reconstruction method**, not proof that a residual plane supports a strict gain, that another support-dependent entropy inequality fails, or that the original guessing number is larger.

`frontier-20261028-fourfactor-plane-fractional-certificates-v1.json` SHA-256 `863f74fe993c7b6adbd867b97fa0b83de54fe8c65f4c699e66b41ebb8a8db4f4` gives rational primal and dual witnesses. The separate checker `frontier-20261028-fourfactor-plane-fractional-check.py` SHA-256 `31d39f784474152899999fb47eded5bd235b3bff6a12fa300be07340a00e5773`, receipt SHA-256 `a7fe6d5a76a804d6f853ee97c07fde10a6358d39fa852b6846335835c15ce9d5`, checks every safe subset of the ten vertices, all primal coverage and dual packing inequalities, equality of the exact objective, the independently replayed active-mask input SHA-256 `87b6d473e68795c3c6710d642d9a7de4fd03f9fed2378aecb2db216d878e1ea9`, and a modified-dual negative control.

The partition `206 color-certifiable + 41 fractional-method-obstructed = 247` is complete only for the stated four-factor full-plane difference model. Scientific review, novelty clearance and proof-assistant formalization remain open.
