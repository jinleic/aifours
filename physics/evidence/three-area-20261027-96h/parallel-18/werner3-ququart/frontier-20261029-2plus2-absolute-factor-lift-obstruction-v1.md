# Obstruction to a naive entrywise-factor lift of the 2+2 norm lemma

**WRITTEN symbolic diagnostic, UNREVIEWED; no physical q or numerical instance.** The original 2+2 proof bounds the actual operator `X=tI+C⊗I2+I2⊗D`. A tempting route to show its whole class is inside the f274 certificate region is first to assert the stronger bound

`|| |X| ||_op² ≤ 4|t|²+||C||_F²+2||D||_F²`,  (false),

where absolute values are entrywise in a Schur product basis. This assertion is **false**, even with both `C,D` traceless and `t=0`. This only rules out that unqualified factor-modulus step; it is NOT a counterexample to the actual norm lemma, T2, the compound certificate, η≤2L, or any physical statement.

For a free real symbolic `e` with `0<e²<1/3`, put `a=√((1−e²)/2)`, `x=ae`, `c=1−e²`, and

`C=[[x,c],[0,−x]]`, `D=[[−x/2,x],[0,x/2]]`, `t=0`.

Both matrices are 2×2 and traceless. Set `X=C⊗I2+I2⊗D` and unit nonnegative vectors

`u=(a,a,e,0)ᵀ`, `v=(0,e,a,a)ᵀ`.

Their norms are one because `2a²+e²=1`. In the standard product basis,

```
|X| = [[ x/2, x, c,  0],
       [   0, 3x/2, 0, c],
       [   0, 0, 3x/2, x],
       [   0, 0, 0, x/2]].
```

Direct multiplication gives

`uᵀ|X|v = c²+5a²e² =: S`,

and the purported right-hand side is exactly

`||C||_F²+2||D||_F² = c²+5a²e² = S`.

But

`S = (1−e²)² + (5/2)(1−e²)e² = 1+(e²/2)−(3e⁴/2) > 1`,

so `|| |X| ||_op² ≥ (uᵀ|X|v)²=S²>S`. No finite search or symbolic program was used.

The inequality `ρ(|X†X|)≤|| |X| ||_op²` goes in the direction of an upper bound: failure of the right-hand side to meet this *particular* scalar bound gives no lower bound on `ρ(|X†X|)`. Also the original f274 object is the second compound, with additional local-product-basis minimization; no f274 failure is established. Determining whether any general separately 2+2 pair lies outside `η≤2L` remains open, and the complete 2+2 theorem and the later witness-overlap addenda retain their recorded statuses.
