# The same both-squares-nonnormal pair has a strict certificate in a second local basis

**WRITTEN, UNREVIEWED additive qualification of** `frontier-20261029-d4-t2-both-nonnormal-fixed-basis-obstruction-v1.md` (SHA-256 f3ef2ff62a3c59638dc46186422a071c6af3e55c2de9acd17271845f6102412f). The earlier proof claims failure only in its displayed basis and remains byte-unchanged. This addendum proves the stronger and deliberately opposite fact: the **same pair** has a second explicit local product basis with a strict f274 certificate. Thus it is **not** an η-counterexample and is in f274's certified region, conditional only on the explicitly named adopted f215/f274 written results. It does not decide whether other 2+2 pairs are certificate-covered.

## 1. Pair and hollow rotations

Use precisely the earlier pair and notation:

`Aδ=(δ I2+C)⊕(−δ I2)`, `Bδ=(δ I2+D)⊕(−δ I2+D)`,

`C=[[x,c],[0,−x]]`, `D=[[−x/2,x],[0,x/2]]`, `c,x>0`, `r=x/c`, `0<r²<8/29`,

`S=c²+5x²`, `g=c²(3r²−87r⁴/8)/(2+13r²/2)>0`, `M=2√(c²+6x²)`, `δ=g/[16(M+√g+g/x)]`.

For a real upper triangular traceless `T=[[a,b],[0,−a]]`, a real orthogonal 2×2 change of basis with first vector `(cosθ,sinθ)` has first diagonal entry `a cos(2θ)+(b/2)sin(2θ)`. Thus choose rotations `Q_C,Q_D` so that

`cos(2θ_C)=c/√(c²+4x²)`, `sin(2θ_C)=−2x/√(c²+4x²)`,

`cos(2θ_D)=sin(2θ_D)=1/√2`.

Then both diagonal entries vanish (the second is the negative of the first):

`Q_Cᵀ C Q_C=[[0,p],[q,0]]`, `Q_Dᵀ D Q_D=[[0,u],[v,0]]`.

The exact off-diagonal signs are immaterial; `|p|²+|q|²=||C||_F²`, `|u|²+|v|²=||D||_F²`. Use local unitaries `U=Q_C⊕I2` and `V=Q_D⊕Q_D`.

## 2. Strict entrywise-factor bound

At `δ=0` in these bases, `A0` is a weighted partial permutation with one 2-cycle and zero weights at the other two fixed points; `B0` is the direct sum of two identical weighted 2-cycles. Their diagonals vanish, so the supports of `A0⊗I4` and `I4⊗B0` are disjoint. Replacing their weights by absolute values therefore gives exactly `|X0|`, where `X0=A0⊗I4+I4⊗B0`.

The f215 weighted-partial-permutation operator bound, applied to these nonnegative weights, gives

`|| |X0| ||_op² ≤ m_A+m_B = ||C||_F²+||D||_F² = S−(3/2)x² =: P`.  (2.1)

Here the row/column weight sum on either vertex of a 2-cycle is its two squared weights; `||D||_F²=3x²/2`. This is the already-adopted f215 bound, not the false arbitrary-T estimate.

The block-diagonal rotations commute with `Z=I2⊕(−I2)`. The perturbation from the unperturbed global tensor-sum matrix is `δ(Z⊗I4+I4⊗Z)`, a diagonal matrix whose entrywise modulus has operator norm `2δ`. Entrywise `|Xδ|≤|X0|+|δ(Z⊗I4+I4⊗Z)|`; monotonicity of the operator norm on real nonnegative matrices yields

`|| |Xδ| ||_op ≤ √P+2δ`.  (2.2)

Also `Lδ=||Aδ||_F²+||Bδ||_F²=S+8δ²`.

For the exact `g,δ` above,

`g < (3/2)x²`,

`δ < g/(16M) < 3x²/[64√(c²+6x²)]`,

`4δ√P < (3x²/16)√((c²+(7/2)x²)/(c²+6x²)) < (3/2)x²`.

Consequently

`|| |Xδ| ||_op² ≤ (√P+2δ)² < S+4δ² < S+8δ²=Lδ`.  (2.3)

This is a strict finite-basis bound on the earlier entrywise-factor γ bridge, not a selected q value.

## 3. Consequence for the optimized compound and boundaries

The f274 domination of the compound certificate by the entrywise-factor bridge is `η≤2γ`, where `γ` minimizes `ρ(|X|ᵀ|X|)` over local product bases. The explicit bases above give `γ≤|| |Xδ| ||_op²<Lδ`; hence

**`η(Aδ,Bδ)<2Lδ`.**

Therefore the earlier fixed-basis obstruction and this strict alternate-basis certificate coexist for the **same original pair with both squares nonnormal**. The first basis was a valid method obstruction; it did not, and cannot, establish physical failure or optimized-certificate failure. The full 2+2-versus-f274 comparison is still open: this example resolves only its own membership. No chosen physical q, code, external source, Lean/kernel, novelty, T2-global/T3/Z2 or held input is asserted.
