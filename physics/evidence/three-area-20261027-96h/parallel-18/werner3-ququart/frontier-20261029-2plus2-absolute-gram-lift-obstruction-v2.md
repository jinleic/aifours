# Stronger obstruction: even the entrywise Gram modulus cannot use the weighted norm bound

**WRITTEN symbolic diagnostic, UNREVIEWED.** This is a successor to the separate entrywise-factor diagnostic `frontier-20261029-2plus2-absolute-factor-lift-obstruction-v1.md` (SHA-256 0a9486330fbc8c9b5b8eb050c17b27d960f25a4e096c4563341125f18498603d); all pinned bytes remain unchanged. It falsifies a proposed proof premise, not the original two-qubit norm lemma or T2. No code, selected numerical instance, selected physical q, or held input is used.

## False premise and all-variable counterfamily

A still stronger possible repair of the factor-modulus approach would claim, for traceless `C,D∈M2` and scalar `t`,

`ρ(|X†X|) ≤ 4|t|²+||C||_F²+2||D||_F²`, `X=tI4+C⊗I2+I2⊗D`.  (false)

It is false for `t=0` already. Let `c,x>0` be free symbolic variables with `r=x/c` and `0<r²<8/29`, and set

`C=[[x,c],[0,−x]]`, `D=[[−x/2,x],[0,x/2]]`.

Then both factors are traceless, and the proposed right-hand side is

`S=||C||_F²+2||D||_F² = c²+5x²`.

The actual two-qubit operator is

```
X = [[ x/2, x, c, 0],
     [   0, 3x/2, 0, c],
     [   0, 0, −3x/2, x],
     [   0, 0, 0, −x/2]],
```

so its entrywise Gram modulus is

```
|X†X| = [[x²/4, x²/2, cx/2, 0],
         [x²/2, 13x²/4, cx, 3cx/2],
         [cx/2, cx, c²+9x²/4, 3x²/2],
         [0, 3cx/2, 3x²/2, c²+5x²/4]].
```

With the positive vector `z=(r/2,5r/2,1,1)ᵀ`, direct expansion gives

`zᵀ(|X†X|−S I4)z = c² (3r²−87r⁴/8)>0`.

Thus its Rayleigh quotient is strictly larger than `S`, and `ρ(|X†X|)>S`. This is an exact inequality for every member of the displayed symbolic family.

## Exact limits

The actual `||X||_op²` still obeys the weighted bound proved in the main packet; the counterexample concerns only modulus entrywise **after** the Gram product. Since `|X†X|≤|X|ᵀ|X|` entrywise, this stronger obstruction also entails failure of the still stronger factor-modulus premise for the same family. It does not imply that an embedded traceless 4×4 pair fails f274: the latter concerns `|H^[2]|`, the full 16-dimensional `H`, the total `2L`, and a minimization over **all** local product bases. The chosen 2×2 factors here in fact have scalar squares; no both-squares-nonnormal complement witness is claimed. The wider comparison `η≤2L` for arbitrary 2+2 pairs remains unpaid.
