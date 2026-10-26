# x1111 additive replacement: a 37-term Schmidt-two decomposition with small positive weights

Actual `/bin/date` observation before writing: **Sun Oct 25 04:46:27 PDT 2026**. Owner PhysicsPPT44-2. **WRITTEN CANDIDATE, strictly written repair of the outstanding upper-bound gate.** No scientific eval, interpreter, arithmetic program, enumeration, certificate replay or solver was used. Metadata clock/hash calls only. Global HOLD and parent erratum v7 remain binding.

## 1. What this replaces, and what it does not assert

The v30-B review `peer-review-ppt-x1111-schmidt-two-v1.md`, SHA-256 `d04c1e340cd861900177ecafae226456f3855670bda5075571df689670f18d05`, fully reconstructs the eight-vector average, all individual rank conditions, PPT and entanglement. Its **MAJOR NOT_RECONSTRUCTED** gate is the old large21-pair weighted residual identity. The parent correctly did not accept SN<=2 or retire the N4 input from that review.

This successor **replaces that residual table as a proof premise**. It gives one finite sixteen-phase identity, five two-dimensional-support projectors and six positive single-generator projectors. Their complete six-dimensional coefficient sum is reconstructed below with a diagonal table and all six off-diagonal entries. There are no large unexplained rational sums.

The old21-pair table remains frozen and NOT_RECONSTRUCTED by this note. No claim that its literal coefficients have now been hand-summed is made. The new decomposition is an alternative proof of the same proposed upper bound, not retroactive verification/admission of the old computation. Parent acceptance of this new written proof is separate.

The diagonal-Bell/Grassmannian packet is unrelated and is not an input. Neither this note nor a positive disposition would resolve unrestricted P44 or recover the old native N4 result/child exit.

## 2. Literal state and notation

Use unnormalized `P(v)=v v*` and kets ij in C4 tensor C4. Put `x=|0>+|1>+|2>+|3>` and

```
a=00+11+22, b=01+12, c=10-21,
d=02+|3> tensor x, e=20+33,
f=30, g=32, h=|0> tensor x, j=23.
```

The unchanged target is

```
R=P(a)+P(b)+P(c)+3[P(d)+P(e)+P(f)+P(g)+P(h)+P(j)],
rho=R/49.                                                   (1)
```

Every entry of rho is rational with denominator dividing49. Its positive Gram sum proves positivity, and its trace is49. The exact direct PPT Gram is

```
R^Gamma=P(02+11-20)+2P(02+20)
        +P(01+10)+P(12+21)+P(00)+P(22)
        +3P(32+h)+3P(30+23)+3P(|3> tensor x)+3P(33).
```

This is the same identity already reconstructed at v30-B boundary B0; no execution result is used here.

## 3. The eight rank-two vectors and their already-reconstructed average

Let delta run over `+2i/3,-2i/3`. For the positive sign let

```
gamma=sqrt(30)(1-i)/12;
```

for the negative sign use its conjugate. Independently beta=+gamma or -gamma and chi=+gamma or -gamma. For all eight choices define

```
psi=a+beta b+chi c+delta(d-e-f-g)+delta chi f+delta beta g.    (2)
```

Its coefficient matrix has rows

```
(1,beta,delta,0), (chi,1,beta,0),
(-delta,-chi,1,0), delta(chi,1,beta,0).
```

The first three rows/columns have determinant

```
1-delta(beta^2+chi^2)+delta^2=0,
```

because beta²+chi²=delta+delta^(-1). The fourth row is delta times the second, so every psi has Schmidt rank at most two. This is an identity over complex numbers, not a real-only rank test.

Write `v=d-e-f-g`. Independent beta/chi signs and conjugate delta signs remove all cross groups in (2). The variances are1 on a,5/12 on b,c,4/9 on v and5/27 on f,g. Thus

```
A=(1/8)sum_eight P(psi)
 =P(a)+(5/12)[P(b)+P(c)]+(4/9)P(v)+(5/27)[P(f)+P(g)].       (3)
```

For the only potentially surviving b/g and c/f cross terms, their coefficients are `(5/12)E(conj(delta))=0`. This supplies the full average, not a list of sampled entries. v30-B boundary B1 reconstructed precisely this identity.

## 4. One small finite phase identity handles the only problematic pair

Let

```
Z4={1,i,-1,-i},
chi_(z,w)=d+e+z h+z^(-1)g+w j+w^(-1)f, z,w in Z4.          (4)
```

The use of the name chi_(z,w) here is unrelated to the scalar chi in (2). Each vector in (4) has the **explicit two-product factorization**

```
chi_(z,w)
 =(z|0>+|3>) tensor (x+z^(-1)|2>)
  +(|2>+w^(-1)|3>) tensor (|0>+w|3>).                      (5)
```

The first product expands to `d+z h+z^(-1)g`; the second to `e+w j+w^(-1)f`. Thus every one of the sixteen literal complex vectors has Schmidt rank at most two, with no division by a possible zero: z,w are specified nonzero fourth roots of unity.

The five coefficient characters in (4) are

```
1, z, z^(-1), w, w^(-1).
```

Their exponent pairs `(0,0),(1,0),(3,0),(0,1),(0,3)` are distinct modulo(4,4). The finite geometric-series identity therefore removes every cross group except the retained d/e cross term inside their constant coefficient. Consequently

```
B=(1/16)sum_(z,w in Z4) P(chi_(z,w))
 =P(d+e)+P(f)+P(g)+P(h)+P(j).                              (6)
```

This is a complete symbolic identity: the sixteen points DEFINE an exact Fourier average; they are not an enumeration used to infer a universal statement. No finite computational check is needed or used.

## 5. Five remaining pairs are already rank at most two

Define

```
k1=d+f, k2=d+g, k3=e-f, k4=e-g, k5=f-g.                   (7)
```

k1,k2 are supported on Alice's span{|0>,|3>}; k3,k4 on her span{|2>,|3>}; k5 is the product vector `|3> tensor (|0>-|2>)`. Hence all five have Schmidt rank at most two. The individual d,e have Schmidt rank at most two, and f,g,h,j are product vectors.

This is the missing simplification in the earlier sampler. Simultaneously making BOTH auxiliary symmetric arrays rank one is a sufficient condition for a residual vector to be Schmidt-two, but not a necessary one. The pair projectors (7) can be certified directly from their two-dimensional Alice support; they need not belong to that overly restrictive simultaneous-Veronese subcone.

## 6. Complete small residual identity — all entries hand-accounted

Let F have columns `(d,e,f,g,h,j)` in that order and put lambda=4/9. Subtracting (3) from (1) leaves `(7/12)[P(b)+P(c)]` and `F M F*`, where

```
M=3I6-(4/9)q q^T-(5/27)(E_ff+E_gg),
q=(1,-1,-1,-1,0,0)^T.                                    (8)
```

The small replacement for the old21-pair identity is

```
F M F*
 = lambda B + lambda sum_(l=1)^5 P(k_l)
   +(11/9)[P(d)+P(e)]
   +(16/27)[P(f)+P(g)]
   +(23/9)[P(h)+P(j)].                                    (9)
```

Here is a complete human-readable verification. Work in the six-dimensional coefficient basis before applying F; this avoids any issue of overlaps between the physical generators. By (6), lambda B contributes the d/e pair projector plus one lambda on each of f,g,h,j. The five pair projectors in (7) contribute exactly the other five edges of the complete graph on d,e,f,g. There are no off-diagonal entries involving h or j.

The six diagonal totals are:

| Coordinate | lambda B | lambda sum P(k_l) | positive singleton remainder | Total |
|---|---:|---:|---:|---:|
| d | lambda | 2lambda | 11/9 | 23/9 |
| e | lambda | 2lambda | 11/9 | 23/9 |
| f | lambda | 3lambda | 16/27 | 64/27 |
| g | lambda | 3lambda | 16/27 | 64/27 |
| h | lambda | 0 | 23/9 | 3 |
| j | lambda | 0 | 23/9 | 3 |

For example `3lambda+11/9=(12+11)/9=23/9`, and `4lambda+16/27=(48+16)/27=64/27`. These are precisely the diagonal entries in (8).

All nonzero upper off-diagonal coefficients are listed here; their Hermitian conjugates supply the lower half:

| Pair | Only contributing projector | Coefficient |
|---|---|---:|
| d,e | lambda P(d+e) inside lambda B | +lambda |
| d,f | lambda P(k1) | +lambda |
| d,g | lambda P(k2) | +lambda |
| e,f | lambda P(k3) | -lambda |
| e,g | lambda P(k4) | -lambda |
| f,g | lambda P(k5) | -lambda |

The signs are exactly those of `-lambda q q^T` off the diagonal. All other off-diagonal coefficients vanish by (6) and the literal pair definitions. This accounts for **all six diagonal and all fifteen upper off-diagonal entries**, not just a checksum or some selected entries. It proves (9) over the rational coefficient space. Applying the linear congruence F preserves the exact operator identity, whether or not the physical columns overlap.

## 7. Final explicit37-term operator decomposition

Substitute (6) and (9) into (3). Since lambda/16=1/36, the complete formula is

```
R = (1/8)sum_eight P(psi)
    +(7/12)[P(b)+P(c)]
    +(1/36)sum_(z,w in Z4) P(chi_(z,w))
    +(4/9)sum_(l=1)^5 P(k_l)
    +(11/9)[P(d)+P(e)]
    +(16/27)[P(f)+P(g)]
    +(23/9)[P(h)+P(j)].                                   (10)
```

Every scalar coefficient is explicitly positive and small-denominator rational. All vector parameters are literal finite sets; no table, optimizer output, unspecified solution or search is hidden. The Schmidt-rank certificates are (2)–(3) for the eight vectors, the two-product identity (5) for the sixteen phase vectors, the Alice-support argument for the five k vectors, and the obvious one/two-product descriptions for the singles. There are8+2+16+5+6=37 terms before merging duplicates.

Divide (10) by49. For each nonzero vector u with displayed coefficient c, replace it by its unit normalization and assign weight `c ||u||^2/49`; zero vectors, if any, may be omitted. These weights are nonnegative and sum to one by the trace of the already-proved exact operator identity. Therefore (10) is a complete WRITTEN Schmidt-number-at-most-two certificate for the actual rho, with no old21-weight premise.

For the matching lower bound, project Alice onto levels0,1,2. The range matrices are

```
[ A+H  B+H  D+H H ]
[ C    A    B   0 ]
[ E   -C    A   J ].
```

A product vector with nonzero Bob3 column must have its whole middle row zero, hence A=0. With zero Bob3 column, H=J=0 and the two core minors give `A^2-BC=A^2+BC=0`, again A=0. All product vectors in this range thus have11 coefficient zero, whereas the projected positive state has11 diagonal entry1. It is entangled. This already-reconstructed lower-bound argument and (10) give the new candidate theorem **SN(rho)=2**.

## 8. Acceptance and non-claims

This note supplies the actual short symbolic replacement requested by the parent. The new load-bearing work is (5), the finite character identity (6), and the fully itemized coefficient proof of (9). It has no scientific-arithmetic premise and requires no withheld replay to be read as a written proof.

It does not assert that the old literal21-pair table has been reconstructed, that unadmitted computation acquired credit, that the historical N4 outcome changed, or that its child exit is recovered. The parent must disposition this exact new packet before calling the input retired. No new scientific launch or retry is authorized.

This is ONE input-specific result toward P44, not an unrestricted theorem: another rational PPT/SN3 state or an all-state no-go remains missing. Independent reconstruction of this successor, formal verification, outside-model/human review and novelty clearance are not claimed.
