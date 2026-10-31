# Divisibility sharpens the uniform coset-state barrier to 180

**Status: WRITTEN, conditional on the pinned proper-subgraph and linear-rank certificates through the preceding packet; scientific review and novelty clearance pending.** Let a uniform group-coset R-minus FD law have positive balance gap, and write `m=[G:intersection_i H_i]`, `d_i=[G:H_i]`. Then

\[
\boxed{m\ge180.}
\]

More precisely:

* If `m` is odd, then `m>=1517`.
* If `m` is even but `3` does not divide `m`, then `m>=258`.
* If `m` is divisible by 6, then `m>=180`.

The previous result `frontier-20261028-uniform-coset-175-barrier-v1.md` SHA-256 `cdad7de637944f98771200a18d802108c9faa7dc90478a89a3f4021c3fdacdcc` proves that all ten `d_i>=2`, at least two `d_i>=3`, and strict balance implies `m^3>product_i d_i^2`. Also, every `d_i` divides `m`, since `K=intersection_i H_i` is a subgroup of each `H_i`.

If `m` is odd, every `d_i` is an odd divisor larger than 1, so `m^3>3^20=3486784401`; because `1516^3=3484156096 < 3^20 < 1517^3=3491055413`, `m>=1517`. If `m` is even and not divisible by 3, each of the two nonbinary indices is at least 4, so `m^3>2^16*4^4=256^3`; since `m` is even, `m>=258`. If `m` is divisible by 6, the previous lower bound `m>=175` rounds up to `m>=180`.

Therefore no uniform group-coset law on any group of order at most 179 can be a strict R-minus witness. This is a restricted-class obstruction; it says nothing about nonuniform group laws or general finite FD laws, and is not a numerical guessing-number upper bound.
