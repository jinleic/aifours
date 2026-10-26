# All-reference working checkpoint 015: the joint charge Q/R/T block closes by hand

Before-writing clock observed: `2026-10-23T18:46:48-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written proof**, within the same unfinished all-reference W4 route. No scientific program, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used. No output from the proposed charge-covariance-polynomial-002 assay was received or used; the author requested HOLD before freezing this proof.

**Delta:** after removing the actual Q reference kernel, the full joint `(Q_perp,R/T)` principal space is positive for **every reference spectrum**. Its physical R/T Schur matrix is strictly diagonally dominant with margin **1/18**. The entire upper nonzero-charge twelve-block therefore reduces to a **four-dimensional P Schur residual**, not the previous seven-dimensional residual. The P sign remains unproved.

## 1. Physical interface and notation

Use the full physical table of checkpoint 004, SHA256 `98e0d5f820e1b9aeabe9b88410afc6c3d1771feaffb2dfa7fe1798812c649d72`. The rational covariance derivation is checkpoint 013, SHA256 `cf4734d64a507777c28042cf2ec7ba39bd8181c59c29f164e025bbc61e4ef9a1`. They are unreviewed working sources; no inherited acceptance is claimed.

Fix charged labels `a!=b`, spectators `{j,k}`, and normalized nonnegative Schmidt amplitudes c. Write

```
A=x_a, B=x_b, J=x_j, K=x_k,
T=A+B, V=J+K=1-T,
m=AB, n=JK, w=sqrt(JK),
W=1+2TV+(1+T)m+(2-T)n,
beta=(1-2T+m-n)/(4W),
r_j=d_jb=(1+A+K)/2, r_k=d_kb=(1+A+J)/2,
t_j=d_aj=(1+B+K)/2, t_k=d_ak=(1+B+J)/2,
s=d_jk=(1+T)/2.
```

Every d above is at least `1/2`, and `1<=W<=2`. The lower W bound follows from the displayed positive expression; the upper follows from `W=1+2e2(x)-e3(x)`, `e2(x)<=1/2`, and `e3(x)>=0`.

The physical basis is

```
Q_i=|i,i,a,b>, P_i=|a,b,i,i>,
R_l=|a,l,l,b>, T_l=|l,b,a,l>, l=j,k.
```

The upper form is `D=C_B-S_eta`. Its full Q-reference kernel is `sum_i c_i Q_i`, with zero cross-form to every other coordinate. Only that true kernel is removed; the P4 directions are not set to zero in the final whole-block conclusion.

## 2. Exact Q pivot and the four-dimensional Schur entries

Put `Tau=diag(tau_i)` with `tau_a=tau_b=1/2`, `tau_j=tau_k=1`, `f=Tau c`, and `d=c^T Tau c=d_ab`. The physical Q principal block is

```
Q0=Tau-f f^T/d.
```

For `q orthogonal c`,

```
q^*Q0 q=min_z (q-zc)^*Tau(q-zc)
         >=(1/2)min_z ||q-zc||^2
         =(1/2)||q||^2.
```

Thus its three-dimensional complement is a genuine positive pivot for every normalized c. Its kernel is exactly c.

Let R be the physical four-dimensional R/T Schur matrix after this Q pivot is eliminated, in order `R_j,R_k,T_j,T_k`. Its entries are

```
R_Rj,Rj=3/4-J(4A-J)/(16r_j^2),
R_Tj,Tj=3/4-J(4B-J)/(16t_j^2),               (15.1)
```

and the analogous diagonal entries with `J,j` replaced by `K,k`. The same-family off-diagonals are

```
R_Rj,Rk=w(1-A-B/2)/(4r_j r_k),
R_Tj,Tk=w(1-B-A/2)/(4t_j t_k).               (15.2)
```

The same-spectator opposite-type entries are

```
R_Rj,Tj=-beta-J(T-J)/(16r_j t_j),
R_Rk,Tk=-beta-K(T-K)/(16r_k t_k),             (15.3)
```

and the different-spectator opposite-type entries are

```
R_Rj,Tk=(w/4)[s/(r_j t_k)-1/s],
R_Rk,Tj=(w/4)[s/(r_k t_j)-1/s].              (15.4)
```

These formulas retain beta and its **full** generic inverse correction. No paired-spectrum cancellation is used.

### Derivation of the Q subtractions

For positive amplitudes, apply checkpoint 013's amplitude congruence temporarily. If `h_i^(Rj)=-delta_ij/2+J tau_i^(jb)/(2r_j)`, the scaled Q-cross column is `g_i=x_i h_i`. The exact physical inverse pairing is the covariance pairing divided by the two R/T amplitude factors. The four weighted sums needed for expansion are

```
sum_i x_i (tau_i^(jb))^2/tau_i^(ab)
 =2A+B/2+J/4+K,

sum_i x_i tau_i^(jb)tau_i^(kb)/tau_i^(ab)
 =2A+B/2+(J+K)/2,

sum_i x_i tau_i^(jb)tau_i^(aj)/tau_i^(ab)
 =A+B+J/4+K,

sum_i x_i tau_i^(jb)tau_i^(ak)/tau_i^(ab)
 =A+B+(J+K)/2=d_ab.
```

Inserting these into `sum_i x_i h_i h'_i/tau_i` gives, in physical coordinates,

```
Gram_Rj,Rj=1/4+J(4A-J)/(16r_j^2),
Gram_Rj,Rk=-w(1-A-B/2)/(4r_j r_k),
Gram_Rj,Tj=1/4+J(T-J)/(16r_j t_j),
Gram_Rj,Tk=-w s/(4r_j t_k).
```

The raw R/T upper diagonals are one, same-family off-diagonals zero, same-spectator opposite entries `1/4-beta`, and different-spectator opposite entries `-w/(4s)`. Subtraction gives (15.1)-(15.4). The T analogues follow by interchanging A,B.

The Q complement has the uniform physical gap proved above, so its pseudoinverse and these Schur forms extend continuously to boundary references. All final denominators in (15.1)-(15.4) are bounded away from zero. No zero-amplitude division is used at the boundary.

## 3. Diagonal bound: every diagonal is at least 2/3

It suffices to prove

```
J(4A-J)/(16r_j^2)<=1/12.
```

Since `r_j=(1+A+K)/2`, it is enough to show

```
(1+A)^2-12AJ+3J^2>=0, 0<=J<=1-A.           (15.5)
```

For `A<=1/3`, the quadratic in J is minimized at `J=2A`, with value `1+2A-11A^2`. This is concave on `[0,1/3]`, so its minimum on that interval is the smaller endpoint value `4/9>0`.

For `A>=1/3`, the vertex `2A` lies at or beyond `1-A`; the quadratic decreases on the allowed J interval and its minimum is at `J=1-A`, with value

```
4(2A-1)^2>=0.
```

Adding `K>=0` only increases `(1+A+K)^2`. This proves (15.5), hence the claimed bound. Interchanging labels gives

```
R_rr>=2/3 for every diagonal r.             (15.6)
```

## 4. Same-family bound: each is at most 2/9

For the first entry of (15.2), write `U=1-A-B/2=V+B/2`. Its exact denominator is

```
4r_j r_k=(2-B)(1+A)+w^2.
```

As a function of `0<=w<=V/2`,

```
w U/[(2-B)(1+A)+w^2]
```

increases: the derivative has numerator `U[(2-B)(1+A)-w^2]>=0`, since the first product is at least one and `w^2<=1/4`. At `w=V/2`, substituting `A=1-V-B` gives the upper bound

```
V(2V+B)/(4-V-2B)^2.
```

For fixed V this increases with `0<=B<=1-V`: its numerator increases and its positive denominator decreases. Setting `B=1-V` therefore bounds it by

```
V(1+V)/(2+V)^2<=2/9,
```

whose derivative is `(3V+2)/(V+2)^3>0` on `[0,1]`. These entries are nonnegative. The T analogue is identical with A,B interchanged, proving

```
0<=R_Rj,Rk<=2/9, 0<=R_Tj,Tk<=2/9.           (15.7)
```

## 5. Same-spectator opposite-type bound: absolute value at most 1/4

Write `b0=1-2T+m-n`. The two exact numerator identities are

```
W-b0=2T(2-T)+T m+(3-T)n >=2T,
W+b0=2V(1+T)+(2+T)m+V n >=2V.               (15.8)
```

Let `delta=-beta-J(T-J)/(16r_j t_j)`. To prove `delta>=-1/4`, multiply `1/4+delta` by the positive `16W r_j t_j`. The result is

```
4r_j t_j(W-b0)-W J(T-J).
```

If `T<=J`, both terms in this expression are nonnegative in the indicated sign. If `T>J`, the first is at least `2T` by (15.8) and `4r_j t_j>=1`, while the subtracted quantity is at most `2JT<=2T`. Thus the result is nonnegative.

For `delta<=1/4`, multiplying `1/4-delta` gives

```
4r_j t_j(W+b0)+W J(T-J).
```

This is immediate when `T>=J`. Otherwise the first term is at least `2V`, while the possible negative magnitude is at most `2J^2<=2V`, because `J<=V<=1`. Therefore

```
|R_Rj,Tj|<=1/4, |R_Rk,Tk|<=1/4.             (15.9)
```

## 6. Different-spectator opposite-type bound: absolute value at most 5/36

For `R_Rj,Tk`, put `u=r_j t_k`. Since `r_j+t_k=3/2` and each lies in `[1/2,1]`,

```
1/2<=u<=9/16, 1/2<=s<=1, w<=1-s.
```

The entry is `(w/4)(s/u-1/s)`.

If `s^2<=u`, the entry is nonpositive and

```
absolute value
<=(1-s)(1/s-16s/9)/4<=5/36.
```

Here `s<=3/4`; both nonnegative factors decrease on `[1/2,3/4]`, so their product is maximized at `s=1/2`, where it is `5/36` after division by four.

If `s^2>=u`, the entry is nonnegative. Then `s>=1/sqrt(2)>2/3`, `1-s<=1/3`, and `s/u-1/s<=2s-1/s<=1`. Its value is at most `1/12<5/36`. This proves, also for the other mixed pair,

```
|R_Rj,Tk|<=5/36, |R_Rk,Tj|<=5/36.           (15.10)
```

## 7. Full four-dimensional Schur positivity and the new residual

Each row has exactly one off-diagonal of each type (15.7), (15.9), and (15.10). Their total absolute value is at most

```
2/9+1/4+5/36=11/18.
```

By (15.6) every diagonal is at least `2/3=12/18`. For an arbitrary complex test vector z, the elementary Hermitian diagonal-dominance estimate therefore gives

```
z^*R z >=sum_r[R_rr-sum_(s!=r)|R_rs|]|z_r|^2
        >=(1/18)||z||^2.                   (15.11)
```

Thus the **whole physical R/T Schur matrix**, not merely its diagonal or two-dimensional sectors, is positive for every reference spectrum.

The Q complement is positive and its reference cross-form vanishes, so the joint `(Q_perp,R/T)` principal block has dimension seven and is strictly positive. Eliminate that entire block in the actual twelve-dimensional upper matrix after removing its one true reference kernel. The remaining P space has dimension **four**. Full upper positivity is equivalent to the sign of its exact four-dimensional Schur complement, with every P cross term retained. That sign is not proved here.

The bound `R>=I/18` is for the Schur matrix, **not** an asserted numerical lower eigenvalue bound on the complete joint seven-dimensional pivot. The latter is positive by its two actual Schur pivots; no cross-term-free bound is substituted.

## 8. Evidence and literal frontier

The same universal-reference route now has these unproved forms:

1. **upper nonzero-charge four-dimensional P residual** after the joint pivot above;
2. lower nonzero-charge five-dimensional residual from checkpoint 012;
3. both zero-charge nine-dimensional residuals from checkpoint 010 and its rational chart in checkpoint 013.

Every reference is still included; the claimed component closure is not a paired-spectrum or small-neighborhood result. No full universal-reference theorem, unrestricted W4 theorem, exact asymmetric route failure, rank-two Werner witness, novelty certification, independent acceptance, or formal/kernel proof is claimed.

The author requested HOLD on `charge-covariance-polynomial-002` after deriving this hand closure; its source/request remain preserved and no GO or execution output was received or used by this proof. The older four-polynomial request remains separately HOLD. Those requests are not permissions to execute extra controls or retry. Any later execution decision belongs to the parent and must be recorded separately.
