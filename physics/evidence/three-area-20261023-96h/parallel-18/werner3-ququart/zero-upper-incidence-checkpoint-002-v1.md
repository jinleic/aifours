# Upper zero-six: an exact raw-energy decomposition with nonnegative remainder

Actual clock observed before writing: **2026-10-24T03:56:21-07:00**, `/bin/date -Iseconds`. Author PhysicsResearch96h. Same single active target `Z_up(c)>=0`; no other final residual is attacked.

Status: **NEW CANDIDATE hand identity and sign of its raw-energy remainder**. This does not prove the p-Schur comparison or Z_up. No scientific program, arithmetic interpreter, import, compile, syntax/test execution, enumeration, solver, model CLI or nested agent was used.

Consume `zero-upper-incidence-checkpoint-001-v1.md`, SHA256 **`70bdec0140a9cbaf788cee074bd09dc43a467fe488fb8200b30ca7930a053372`**, for the declared edge variables, exact full H(q) coupling and retained incidence/cycle cross terms. The literal pinned residual source is `all-reference-four-residuals-v1.md`, SHA256 `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`; its actual scalar coefficient lines41–50 and full zero-six lines182–257 were read again for this derivation. Parent/component status and all historical corrections are unchanged.

## 1. A regular four-dimensional positive matrix

Use `x_i=c_i^2`, `sum x_i=1`, `D=diag(d_i)`, `d_i=1-x_i`, `d_ij=(d_i+d_j)/2`. Define the REAL symmetric matrix

```
L_ii=1/4,
L_ij=-c_i c_j/[2(d_i+d_j)] = -K_ij, i!=j.       (R1)
```

There is no singular denominator in (R1) on the closed physical simplex: `d_i+d_j>=1` for distinct indices. The exact Lyapunov identity is

```
D L+L D=Q/2, Q=I-cc^T.                        (R2)
```

Both the diagonal `d_i/2` and the off-diagonal `-c_i c_j/2` follow entrywise. On the positive interior D is strictly positive, and hence

```
L=(1/2) integral_0^infinity exp(-tD) Q exp(-tD) dt >=0.   (R3)
```

This is a mathematical integral proof, not an executed calculation. Formula (R1) is continuous on the full compact simplex. Therefore its PSD sign extends to every sparse reference by continuity. One must NOT substitute a singular boundary D into the integral and assert uniqueness there: for instance the product-reference active diagonal is fixed by the continuous formula (R1), not by a unique singular Lyapunov solution.

## 2. The exact raw q-plus energy

Let U be any complex symmetric zero-diagonal matrix, with `q_ij=d_ij U_ij` and `b=Uc`. Define

```
A=[D,U]=DU-UD,
R0(U)=(1/2)sum_(i<j)d_ij(1+d_ij)|U_ij|^2
      -(1/4)b^dagger D b.                     (R4)
```

R0 is a proposed comparison energy, not the already-established p-Schur cost.

The source coefficient simplifies exactly. For complementary pairs `{i,j}` and `{k,l}`,

```
E_ij=d_ij d_kl/W-1/4,
W=e3(d)=1+2e2(x)-e3(x)>0.                     (R5)
```

Indeed, with s=x_i+x_j, the source numerator is `2+s(1-s)=(2-s)(1+s)=4d_ij d_kl`.

The full raw q energy has the following exact decomposition:

```
Qraw(U):=q^dagger[(5/4)I6-Tq]q
 =R0(U)
  +sum_(i<j)d_ij^2[1/2-d_ij d_kl/W]|U_ij|^2
  +(1/4)Tr(A^dagger L A).                     (R6)
```

All edge adjacencies and complex cross terms of Tq are included; disjoint edge entries are zero exactly as in the literal source.

### Full derivation of the adjacency term

For the positive-interior derivation only, introduce

```
K_ij=c_i c_j/[2(d_i+d_j)] for ALL i,j,
K_ii=x_i/(4d_i),
D K+K D=P/2,
L=(1/4)D^(-1)-K.
```

Unlike (R1), K may diverge at a product face; it is only an auxiliary interior object and is absent from the final regular formula (R6).

Write `F=(DU+UD)/2`, so `F_ij=q_ij`, `F_ii=0`. Expansion of `Tr(F^dagger K F)` enumerates each pair of edges sharing a label with exactly the source coefficient K_at; its diagonal contribution on edge i,j is `(K_ii+K_jj)|q_ij|^2`. Therefore

```
Qraw=sum_(i<j)[1-d_ij d_kl/W+(1/4)(1/d_i+1/d_j)]
                  d_ij^2 |U_ij|^2
     -Tr(F^dagger K F).                        (R7)
```

For S=DU+UD and A=DU-UD, direct expansion gives

```
Tr(S^dagger K S)-Tr(A^dagger K A)
 =2Tr[U^dagger(DK+KD)UD]
 =Tr(U^dagger P U D)
 =b^dagger D b.
```

The last equality uses U^T=U and real c; it does not assume U is Hermitian or real. Thus

```
Tr(F^dagger K F)
 =(1/4)Tr(A^dagger K A)+(1/4)b^dagger D b.
```

Finally,

```
(d_ij^2/4)(1/d_i+1/d_j)-d_ij/2
 =[(d_i-d_j)^2/16](1/d_i+1/d_j),
Tr(A^dagger D^(-1)A)
 =sum_(i<j)(d_i-d_j)^2(1/d_i+1/d_j)|U_ij|^2.
```

Insert these equalities into (R7) and use `L=D^(-1)/4-K`; the result is (R6). The final identity has only the regular physical denominators `d_ij>=1/2` and W>0, so it extends to every closed-simplex reference, even though the auxiliary interior K did not.

## 3. Every term of the remainder is nonnegative

Fix an edge i,j; put

```
s=x_i+x_j, p=x_i x_j, z=x_k x_l.
```

The two pair sums of d are `2-s` and `1+s`, and their two pair products are `1-s+p` and `s+z`. Consequently

```
W=(1-s+p)(1+s)+(s+z)(2-s),
W-2d_ij d_kl
 =(3/2)s(1-s)+(1+s)p+(2-s)z >=0.              (R8)
```

This prints the complete sign certificate, with the inequality direction unchanged. Hence

```
1/2-d_ij d_kl/W=(W-2d_ij d_kl)/(2W)>=0.
```

The last term of (R6) is nonnegative by L>=0, including for complex A. Therefore the exact full raw energy satisfies the new bound

```
Qraw(U)>=R0(U)                               (R9)
```

on the entire closed normalized reference simplex.

If the reference has at least two nonzero Schmidt coefficients, the right side of (R8) is strictly positive for **every** edge. To check the endpoints: if s=0 then all active support lies in the complementary pair and z>0; if s=1 then p>0; otherwise the first term is positive. Thus the diagonal part of `Qraw-R0` is strictly positive at every nonproduct reference. This does not say anything about the currently unproved p-Schur subtraction.

R0 itself is positive for a nonzero U. Indeed row Cauchy-Schwarz gives

```
b^dagger D b<=sum_(i<j)(d_i^2+d_j^2)|U_ij|^2.
```

Hence

```
R0(U)>=sum_(i<j)[2(d_i+d_j)-(d_i-d_j)^2]|U_ij|^2/8>0,
```

because `0<=d_i,d_j<=1` and `d_i+d_j>=1`. This is merely positivity of a comparison energy; it does not bound the inverse p cost.

## 4. The exact remaining logical obligation — no silent substitution

The actual p inverse cost is the full quantity from checkpoint001:

```
Cost_p(U)=(1/r)eta(U)^dagger N^(-1)eta(U)
          +zeta(U)^dagger A8^(-1)zeta(U)
```

on the positive interior. Equivalently it is `Hq q` paired with the inverse of the true positive p quotient; on a face one uses the separately supported range/Moore-Penrose definition, never a divergent frame formula.

A possible sufficient next bound is

```
Cost_p(U)<=R0(U) for every complex symmetric zero-diagonal U.   (R10)
```

**R10 is UNPROVED.** The exact target remains `Cost_p(U)<=Qraw(U)`, not the stronger R10. If R10 fails, its failure must not be reported as a negative Z_up or Werner witness; one must return to the exact remainder in (R6). The new nonnegative remainder is not discarded as irrelevant and gives room for a weaker valid estimate.

If R10 were proved, R6 would prove the whole upper zero-six sign, with strict positivity at every nonproduct spectrum, and only the physical continuous boundary argument thereafter. This conditional implication is not acceptance of the premise. No result about the other three final residuals, the unrestricted all-reference route, the full book W4 question, priority or formal verification is claimed.
