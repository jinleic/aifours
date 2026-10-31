# F828 additive correction: the four-variable bent-degree step

In §3 of `author-candidate-v1.md`, the observation that the Walsh transform of `(1-(-1)^h)/2` is divisible by 2 gives only the degree bound 3 via the stated divisibility lemma; it does **not** by itself establish degree at most 2. The base text names the standard S6 degree-2 fact as an import, but its word “equivalently” should not suggest that the preceding divisibility computation proves it. Replace that portion of the reasoning by the following complete written proof; the frozen base candidate is not edited.

Let `h:F₂⁴→F₂` be bent, so `hat((-1)^h)(a)=±4` for every `a`. For any nonzero `a` and either `ε∈F₂`, the character sum of `(-1)^h` on the affine three-flat `a·z=ε` is

`(hat((-1)^h)(0)+(-1)^ε hat((-1)^h)(a))/2 ∈ {0,±4}`.

That three-flat has eight points, so its number of `h=1` points is respectively `4`, `2`, or `6`: always even. In particular every degree-three ANF coefficient, obtained by summing `h` on the corresponding coordinate three-subspace modulo 2, vanishes. On all 16 points the weight is `(16-hat((-1)^h)(0))/2∈{6,10}`, so the degree-four ANF coefficient also vanishes. Thus `deg h≤2`. Applying this to `h=f+q` proves the quadraticity used in (9) without an additional source import. The rank argument and all conditional-import boundaries in the base candidate remain unchanged.

The separate `parent-acknowledgement-transport-process-note-v1.md` records Main's ONE PROCESS MINOR classification and the actual late direct acknowledgement; it does not alter the mathematical inputs or supply a no-go proof. No scientific execution was performed.
