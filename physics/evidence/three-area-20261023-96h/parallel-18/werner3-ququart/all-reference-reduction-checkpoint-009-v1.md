# All-reference working checkpoint 009: hand closure of the full four-dimensional blocks

Clock observed before this written derivation was frozen: `2026-10-23T17:31:28-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written proof**. No scientific execution, numerical evaluation, import, compilation, polynomial program, model CLI, or proof assistant was used. This is one working leaf of the ongoing universal-reference W4 route, not a separate problem or an accepted theorem. The full universal-reference claim and unrestricted W4 are still unproved.

**New delta:** conditional on the previously printed physical four-block table, a real orthogonal Hadamard change of basis, a positive three-dimensional pivot, and a scalar estimate prove the **whole** four-dimensional upper form for every normalized nonnegative reference. The conditional trace argument then proves its asymmetric lower form. The earlier missing fourth determinant is no longer a gap in this written candidate. It is not being supplied by the pending coefficient-assay proposal.

## 1. Scope and source pins

The physical `C4,S4` are exactly those printed in checkpoint 001 (SHA256 `1e1e076bb8ec3b47853877c5cddd39dd37dc0915d8c9d87c4ef18596533a2326`) and repeated in checkpoint 008 (SHA256 `ba80e91294df7eb48ec1158a9ab5d4f8f2928d331131957c327a734e7151c828`). The regular inverse and `W` identities are in checkpoint 005 (SHA256 `6cfa523879ded76992804f916ba9afb00075b98b972199026512c298b2d7c00c`).

This proof does not require checkpoint 007's three-minor result or checkpoint 008's amplitude filter. Their sources remain preserved; no edit or inherited review is asserted. All source checkpoints are unreviewed working candidates.

The four phase labels `a,b,c,d` are distinct. Put `x_i=c_i^2`, where the Schmidt amplitudes `c_i` are nonnegative and `sum x_i=1`. The result below is matrix positivity on the entire four-dimensional complex sector, not only on real test vectors.

Use

```
T=x_a+x_b, V=1-T=x_c+x_d,
m=x_a x_b, n=x_c x_d, s=T V,
W=1+2s+(1+T)m+(2-T)n.
```

Thus `0<=m<=T^2/4`, `0<=n<=V^2/4`, and `W>=1`. Independent permutations within the two pairs permit `x_a>=x_b` and `x_c>=x_d` without loss of generality. Set

```
Delta=x_a-x_b >= 0, Gamma=x_c-x_d >= 0,
a=T/[4(2-T)], b=V/[4(1+T)],
p=Delta/[4(2-T)], q=Gamma/[4(1+T)],
h=[2+m+n+s/2]/(4W), z=Delta Gamma/(8W).
```

In particular `0<=p<=a<=1/4` and `0<=q<=b<=1/4`.

## 2. The elementary E bounds and regular identities

For completeness, the bound used below is reproduced rather than inferred from a finite point calculation. Let `Q_i=x_i/(1-x_i)` away from a product vertex, and for any complementary pair write `u=Q_i+Q_j`, `v=Q_k+Q_l`. Then

```
E_ij=(u+v+uv)/[4(4+u+v)].
```

If `t=x_i+x_j`, the pairwise Jensen bounds are

```
u >= 2t/(2-t),
v >= 2(1-t)/(1+t).
```

The increasing function `2u+2v+3uv` equals exactly `4` at those two lower bounds: after multiplying by `(2-t)(1+t)`, its numerator is `4(2-t)(1+t)`. Therefore `E_ij>=1/12`.

Also `u<=t/(1-t)` and `v<=(1-t)/t` when `0<t<1`, so `uv<=1`. This gives `E_ij<=1/4` (indeed a stronger strict inequality away from the relevant limiting vertices). All boundary values follow from the regular expression

```
E_ij = [2+(x_i+x_j)(x_k+x_l)]/(4W)-1/4,
```

where `W=1+2e_2(x)-e_3(x)>0`. The expression for `W` in Section 1 is the same polynomial, grouped by the two pairs. Thus no singular `Q_i` is substituted at a product vertex.

For `e=E_ac` and `f=E_ad`, direct multiplication gives

```
h=1/4+(e+f)/2,
f-e=Delta Gamma/(4W)=2z.
```

The useful consequences are

```
h >= 1/3,
h+z=1/4+f <= 1/2.                         (9.1)
```

There is also a sharper global bound on the small correlation entry:

```
0<=z <= s/[8(1+2s)] <= 1/48.              (9.2)
```

Here `Delta<=T`, `Gamma<=V`, `W>=1+2s`, and `s<=1/4`; the last rational function is increasing in `s`.

## 3. The full Hadamard matrix, including every off-diagonal sign

Reorder the original physical basis as `(P1,P3,P4,P2)` and regard it as the ordinary two-bit order `(00,01,10,11)`. In that order, using the Pauli matrices `X,Y,Z`,

```
C4=(I-X/2) tensor (I-X/2),
S4=a I tensor X + p Z tensor X
   +b X tensor I + q X tensor Z
   -(e+f) X tensor X/2 - z Y tensor Y.
```

The signs of the last term matter: `Y tensor Y` has opposite corner entries `-1,+1`, and the original opposite entries of `S4` are `-e,-f`, with `f-e=2z`.

Apply the real orthogonal one-qubit Hadamard on both bits. Since it interchanges `X,Z` and sends `Y` to `-Y`, the resulting `M=C4-S4` is

```
M' = [[d1, -q, -p, -z],
      [-q, d2,  z,  p],
      [-p,  z, d3,  q],
      [-z,  p,  q, d4]],

d1=h-a-b,
d2=1+a-b-h,
d3=1-a+b-h,
d4=2+a+b+h.                               (9.3)
```

This is a full orthogonal transformation, not a compression or a discarded coupling. Positivity of `M'` is exactly positivity of the original four-dimensional physical form.

## 4. A positive three-dimensional pivot and a scalar sufficient inequality

Let `B` be the lower-right three-dimensional principal block of (9.3), and `v=(q,p,z)^T`. All three off-diagonal entries of `B` are nonnegative. Its exact edge decomposition is

```
B=diag(d2-z-p, d3-z-q, d4-p-q)
  +z (e1+e2)(e1+e2)^T
  +p (e1+e3)(e1+e3)^T
  +q (e2+e3)(e2+e3)^T.
```

By (9.1), `a>=p`, and `b>=q`,

```
d2-z-p >= 1/2-b,
d3-z-q >= 1/2-a,
d4-p-q >= 2+h.
```

Consequently

```
B >= D0=diag(1/2-b,1/2-a,2+h)>0.
```

Inverse order and the Schur complement imply

```
d1-v^T B^(-1)v
>= h-a-b-q^2/(1/2-b)-p^2/(1/2-a)-z^2/(2+h)
>= F,

F=h-a-b-p^2/(1/2-a)-q^2/(1/2-b)-(3/7)z^2. (9.4)
```

The last step uses `h>=1/3`. Thus it suffices to prove `F>=0` over the full domain in Section 1. No sign of the inverse entries of `B` is assumed.

Define

```
A(T)=(2-T)(4-3T),
B(T)=(1+T)(1+3T),
R(T)=T/[2(4-3T)]+V/[2(1+3T)]
    =(2-3s)/(4+9s).
```

Expanding the squares of `p,q` gives exactly

```
a+p^2/(1/2-a)=T/[2(4-3T)]-m/A(T),
b+q^2/(1/2-b)=V/[2(1+3T)]-n/B(T).
```

Therefore the scalar to be proved is

```
F=h-R(T)+m/A(T)+n/B(T)-(3/7)z^2,
z^2=(T^2-4m)(V^2-4n)/(64W^2).             (9.5)
```

The formula is invariant under `(T,m,n) -> (1-T,n,m)`.

## 5. Central interval: 1/6 <= T <= 5/6

Here `s>=5/36`. The rational function `(2-3s)/(4+9s)` decreases with derivative `-30/(4+9s)^2`, so

```
R(T) <= R(5/36)=19/63.
```

Using `h>=1/3`, the nonnegative `m,n` terms, and (9.2),

```
F >= 1/3-19/63-(3/7)(1/48)^2
  = 2/63-1/5376 > 0.                       (9.6)
```

This proves the entire central interval, with no restriction on the two within-pair angles.

## 6. Left edge: 0 <= T <= 1/6

The following argument controls the full rectangle `0<=m<=T^2/4`, `0<=n<=V^2/4`. It does not merely inspect its corners.

### 6.1 F is increasing in n

Write `W0=1+2T-2T^2`, so `W>=W0`. Direct differentiation of the rational expression for `h` yields

```
partial_n h
=[-3+2T+s(1+T/2)+(2T-1)m]/(4W^2)
>= -3/(4W0^2).                              (9.7)
```

Indeed `(2T-1)m>=-m>=-T^2/4`, and `2T-T^2/4>=0` on this interval. Moreover `partial_n(z^2)<=0`, because its nonnegative numerator factor `V^2-4n` decreases while `W` increases. Hence

```
partial_n F >= 1/B(T)-3/(4W0^2) > 0.         (9.8)
```

The strict final sign has the explicit polynomial certificate

```
4W0^2-3B(T)
=1+4T-9T^2-32T^3+16T^4
=1+T(4-9T-32T^2)+16T^4
>=1+(29/18)T+16T^4>0,
```

since `9T<=3/2` and `32T^2<=8/9` for `T<=1/6`. All denominators in (9.8) are positive. Thus `F(T,m,n)>=F(T,m,0)`.

### 6.2 A lower bound uniform in m at n=0

At `n=0`,

```
partial_m h=[-1-2T+s(3-T)/2]/(4W^2)<0,
```

because `s<=T` makes the numerator at most `-1-T/2`. Therefore `h(T,m,0)>=h(T,T^2/4,0)`. Drop the nonnegative term `m/A(T)` from (9.5), and use `z^2<=T^2/64`. This gives

```
F(T,m,0) >= h_min(T)-R(T)-3T^2/448,

h_min(T)=(8+2T-T^2)/[4(4+8T-7T^2+T^3)].      (9.9)
```

A hand expansion, not a finite-point identity check, is

```
h_min(T)-R(T)
= T[64+46T-215T^2+105T^3-12T^4]
  /{4(4+8T-7T^2+T^3)(4+9T-9T^2)}.          (9.10)
```

For transparency, the two numerator products before subtraction are

```
(8+2T-T^2)(4+9T-9T^2)
 =32+80T-58T^2-27T^3+9T^4,

4(4+8T-7T^2+T^3)(2-3T+3T^2)
 =32+16T-104T^2+188T^3-96T^4+12T^5.
```

On `0<=T<=1/6`, the bracket in (9.10) is at least

```
64-215/36-1/108 = 3133/54 > 58.
```

Both positive factors `4+8T-7T^2+T^3` and `4+9T-9T^2` are below `6`, so the denominator in (9.10) is at most `144`. Thus, conservatively, `h_min(T)-R(T)>=T/4`. Finally `3T^2/448<=T/896`, and (9.9) proves

```
F(T,m,n) >= (223/896) T >= 0.                (9.11)
```

The bound is strict for `T>0`.

## 7. Right edge and the full upper conclusion

Apply the symmetry `(T,m,n)->(1-T,n,m)` to Section 6. On `5/6<=T<=1`,

```
F >= (223/896)(1-T) >= 0.
```

Together with (9.6), all `0<=T<=1` are covered. Equation (9.4), the strictly positive pivot `B`, and its Schur complement prove

```
C4-S4 >= 0
```

for every normalized nonnegative reference, and strict positivity when `0<T<1`. In particular strict positivity holds when all four Schmidt amplitudes are positive. There is no amplitude-filter singularity in this proof. The same formulas are regular at zero amplitudes and repeated amplitudes; alternatively all boundary nonnegativity follows by continuity of the original physical matrices with `W>=1`.

No complete kernel classification at `T=0,1` is claimed.

## 8. The asymmetric lower form follows, not the symmetric one

The inverse of `C4` is `(16/9)` times the original matrix with the four `-1/2` cycle entries replaced by `+1/2`; the opposite `1/4` entries remain positive. Let `Eavg=(e+f)/2`. Direct contraction gives

```
Tr(C4^(-1) S4)=(16/9)[2(a+b)-Eavg].
```

Also `a+b=(1-s)/[2(2+s)]>=1/6`, while `Eavg<=1/4`. Hence this trace is at least `4/27`.

For the Hermitian `T4=C4^(-1/2)S4 C4^(-1/2)`, the proved upper form says that every eigenvalue is at most one. Its trace is at least `4/27`, so its smallest eigenvalue is at least `4/27-3`. Therefore

```
3 C4+S4 >= (4/27) C4 > 0.                   (9.12)
```

This does not prove `C4+S4>=0` and does not use that stronger, potentially false, symmetric route.

## 9. Literal remaining universal-reference frontier and evidence labels

The working candidate now closes both required signs on every full four-dimensional phase block. This is a hand-written analytic claim pending a separate actual reconstruction, not an inherited acceptance or a new standalone-discovery count.

The remaining unproved blocks of the same all-reference target are:

1. **both seven-dimensional residuals** in each nonzero-charge twelve-dimensional block, with the previously specified kernel/reference Schur treatment;
2. **both twelve-dimensional residuals** in the zero-charge block, after the previously specified antisymmetric/symmetric eliminations.

The scalar and two-dimensional blocks retain their earlier working proofs. This checkpoint alone is not an all-reference theorem, a full W4 proof, an exact rank-two Werner witness, a novelty finding, or a kernel-verified result.

The proposed `all-reference-four-polynomial-001` coefficient assay is **not an input**. Before freezing this leaf the author asked the parent to HOLD that pending request as potentially unnecessary. Its source and proposal remain preserved; no execution, permission, success, or failure is inferred. The earlier seven fixed-reference assay passes remain finite evidence only.
