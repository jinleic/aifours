# An exact both-squares-nonnormal obstruction to one fixed-basis compound certificate

**Status: WRITTEN, UNREVIEWED.** The result is a fully symbolic original-domain counterexample to the assertion that the f274 compound inequality must hold **in the displayed local product basis**. It is **not** a counterexample to `η≤2L`, T2, q3 or a physical assertion: `η` minimizes over all local unitaries and an unexamined basis may certify the pair. Nor does this show the pair lies outside f274's entire certified region or every prior sufficient test. The construction uses no selected numerical instance or physical q, execution, held input or the false f198 lemma.

## 1. Explicit traceless pair and exact statement

Let `c,x>0`, `r=x/c`, and `0<r²<8/29` be arbitrary symbolic variables. Set

`C=[[x,c],[0,−x]]`, `D=[[−x/2,x],[0,x/2]]`, `z=(r/2,5r/2,1,1)ᵀ`,

`S=||C||_F²+2||D||_F²=c²+5x²`,

`g=c²(3r²−87r⁴/8)/(2+13r²/2)>0`, `M=2√(c²+6x²)`,

`δ=g/[16(M+√g+g/x)]>0`.

The specified traceless 4×4 matrices and their standard 2+2 reducing bases are

`A=(δ I2+C)⊕(−δ I2)`,

`B=(δ I2+D)⊕(−δ I2+D)`.  (1.1)

For `X=A⊗I4+I4⊗B`, `H=X†X`, `L=||A||_F²+||B||_F²`, and `K=H^[2]`, the claimed exact inequality is

**`ρ(|K|)>2L` in this particular displayed product basis.**  (1.2)

Every hypothesis of the original traceless 4×4 pair domain holds. Both `A²` and `B²` are nonnormal. The new 2+2 T2 theorem, if accepted, establishes T2 for these pairs, so (1.2) would illustrate a sufficient certificate's basis dependence rather than contradict that theorem. The certificate-minimized quantity `η` and its comparison with `2L` are **not determined** here.

## 2. A positive four-dimensional Gram excess

Let `X0=C⊗I2+I2⊗D` and `H0=X0†X0`. In the same standard product basis,

```
X0 = [[ x/2, x, c, 0],
      [ 0, 3x/2, 0, c],
      [ 0, 0, −3x/2, x],
      [ 0, 0, 0, −x/2]],

|H0| = [[x²/4, x²/2, cx/2, 0],
        [x²/2, 13x²/4, cx, 3cx/2],
        [cx/2, cx, c²+9x²/4, 3x²/2],
        [0, 3cx/2, 3x²/2, c²+5x²/4]].
```

The following identities are by direct multiplication:

`||z||²=2+13r²/2`,

`zᵀ(|H0|−S I4)z=c²(3r²−87r⁴/8)=g ||z||²`,  (2.1)

`||X0+X0†||_F=2√(c²+6x²)=M`.  (2.2)

The condition on `r` gives `g>0`; no matrix eigenvalue or sampled parameter is needed.

## 3. A cross-sector compound Rayleigh witness

The four reducing sectors of `X` include

`X11=X0+2δ I4`, `X12=X0`.

Write `H+=X11†X11`, `H0=X12†X12`. The two-particle subspace containing one vector from each of these orthogonal sectors reduces `K`. After a signed permutation of its pair basis, the restriction of `|K|` is

`R=|H+|⊗I4+I4⊗|H0|`.  (3.1)

This uses that the diagonal entries of both Gram matrices are nonnegative and each off-diagonal compound entry in a cross sector comes from just one of the two factors. For the positive vector `w=z⊗z`,

`(wᵀRw)/(wᵀw) = (zᵀ|H+|z)/(zᵀz)+(zᵀ|H0|z)/(zᵀz)`.  (3.2)

From `H+−H0=2δ(X0+X0†)+4δ² I4`, the reverse triangle inequality entrywise and `|| |Y| ||_F=||Y||_F` imply

`|(zᵀ(|H+|−|H0|)z)/(zᵀz)| ≤ ||H+−H0||_F ≤ 2δ M+8δ²`.  (3.3)

By (2.1), `zᵀ|H0|z/(zᵀz)=S+g`. The block traces of `C,D` vanish, so `L=S+8δ²`. Consequently (3.2)–(3.3) give

`(wᵀRw)/(wᵀw)−2L ≥ 2g−2δM−24δ²`.  (3.4)

By the explicit definition of `δ`, `δM<g/16` and `δ²<g/256`; therefore

`2g−2δM−24δ² > 2g−g/8−3g/32 = 57g/32 > 0`.

Since the spectral radius of a real symmetric nonnegative matrix is at least any of its real Rayleigh quotients and `R` is a reducing block of `|K|`, (1.2) follows. This is a strict failure only of the fixed-basis sufficient test.

## 4. Structural scope and exact unpaid question

Because `C²=x² I2` and `D²=(x²/4)I2`,

`(δI2+C)²=(δ²+x²)I2+2δC`,

`(±δI2+D)²=(δ²+x²/4)I2±2δD`.

`C,D` are nonnormal (`c,x>0`) and `δ>0`, so the squares of both full factors in (1.1) are nonnormal. Both factors are also nonnormal. The denominator of `δ` exceeds `g/x`, hence `0<δ<x/16`; this makes the factors invertible. In particular neither factor is rank one.

`A` is not unitarily similar to an invertible weighted partial permutation: its spectrum `δ+x, δ−x, −δ, −δ` is real and has no nonzero opposite pair. Every cycle of length at least three in an invertible weighted permutation has a nonreal eigenvalue, and a two-cycle has a nonzero opposite pair; all cycles would therefore be singletons, making the matrix normal, contrary to `c>0`. This rules out the f215 weighted-pair structural class, as well as its rank-one and square-normal classes. It does not rule out other independently adopted sufficient tests.

The original all-bases question is precisely whether **some** local unitaries can still make `ρ(|H_{U,V}^[2]|)≤2L`; equivalently, whether `η(A,B)≤2L` for (1.1). This packet does not pay that premise. It gives neither an `η>2L` witness nor a physical counterexample, and makes no claim about general T2, T3, Z2, q3, external-source correctness or novelty. The f274/f281 dispositions, earlier false f198 estimate, all STOP/HOLD/ZERO restrictions, prior process histories, and all frozen reviews remain unchanged.
