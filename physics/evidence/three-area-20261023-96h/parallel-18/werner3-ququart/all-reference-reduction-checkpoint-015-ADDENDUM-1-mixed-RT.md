# Operative correction candidate to checkpoint015: mixed R/T entry and explicit charge composition

Actual clock observed before writing: **2026-10-24T03:17:00-07:00**, returned by `/bin/date -Iseconds`.

Author: **PhysicsResearch96h**. This is a **NEW immutable CANDIDATE correction/composition**, prompted by an actual MAJOR source-identity finding during MathKacMoody's assigned wave-v10 reconstruction. The old015/016, interface and manifests remain byte-unchanged. This document has **not yet received an actual reviewer return or parent acceptance**. No scientific program, arithmetic code, import, compile/syntax check, test, enumeration, native launch, external-model CLI or nested agent was used.

## 1. Exact defect and affected frozen inputs

The finding is accepted as a **MAJOR displayed-identity/proof defect**, not merely cosmetic notation and not a negative route direction. The following source snapshots must be read with this additive correction:

| Frozen source | SHA256 |
|---|---|
| `all-reference-reduction-checkpoint-004-v1.md` — actual raw physical table | `98e0d5f820e1b9aeabe9b88410afc6c3d1771feaffb2dfa7fe1798812c649d72` |
| `all-reference-reduction-checkpoint-013-v1.md` — covariance representation | `cf4734d64a507777c28042cf2ec7ba39bd8181c59c29f164e025bbc61e4ef9a1` |
| `all-reference-reduction-checkpoint-015-v1.md` — erroneous displayed mixed identity | `c3f90d9adb871bfdf866f68764412e99b04a6c7e9b3a11c182053a44711e8ba5` |
| `all-reference-reduction-checkpoint-016-v1.md` — dependent lower composition | `3acd6132e58ed850df1b29751dda1b84768980392ecf5e1c176b5b43c8cb646e` |
| `all-reference-four-residuals-v1.md` — raw-matrix residual interface | `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277` |
| `all-reference-working-manifest-v2.json` — historical then-current dependency record | `4aad56bdfc55160c5684f7551af1ce371545ea079fbc1cedad5f9e790a20d6cc` |

In015's weighted-sum display, source line100 labels

```
A+B+(J+K)/2
```

as `d_ab`. That label is false: its value is **s=d_jk**, not d=d_ab. The mistake propagates to the physical inverse pairing at line109, the two entries in (15.4), and the argument of §6 used to bound those entries. The old §6 bounds a different scalar function and is **withdrawn as a proof for the actual physical mixed entry**. A uniform-point calibration cannot repair this identity.

The rest of this file derives the actual entry directly from the printed raw columns and supplies a new bound. It then explicitly recomposes the upper pivot, the exported norm bound and016's lower pivot. It does not silently mark the original proof correct or transfer a numerical/peer verdict.

## 2. Notation: keep d and s distinct

Fix distinct charged labels a,b and distinct spectators j,k. Put

```
A=x_a, B=x_b, J=x_j, K=x_k,
A+B+J+K=1, all four nonnegative,
T=A+B, V=J+K=1-T, w=sqrt(JK),
d=d_ab=(2-T)/2=(1+V)/2,
s=d_jk=(1+T)/2,
d+s=3/2,
r_j=d_jb=(1+A+K)/2,
t_k=d_ak=(1+B+J)/2,
u=r_j t_k.
```

Each d,s,r_j,t_k is at least1/2. Also `r_j+t_k=3/2`, so `u>=1/2`.

Use `Tau=diag(1/2 on a,b;1 on j,k)`, `f=Tau c`, and `Q0=Tau-f f^T/d`. The actual physical upper Q-cross columns from004 are

```
G_Rj=-e_j/2+c_j Tau^(jb)c/(2r_j),
G_Tk=-e_k/2+c_k Tau^(ak)c/(2t_k).
```

They are orthogonal to c. On such columns the actual Q-complement inverse pairing is exactly `g^*Q0^+h=g^*Tau^(-1)h`: `Tau^(-1)h+constant*c` solves Q0q=h, and the constant vanishes against g. This is the same physical inverse rule as the canonical interface, with no numerical pseudoinverse.

## 3. Direct physical reconstruction of the corrected entry

The four contributions to the weighted product are respectively

```
i=a: A,
i=b: B,
i=j: J/2,
i=k: K/2.
```

Indeed the ratios `tau_i^(jb)tau_i^(ak)/tau_i^(ab)` are1,1,1/2,1/2 on those four labels. Therefore

```
sum_i x_i tau_i^(jb)tau_i^(ak)/tau_i^(ab)
=T+V/2=(1+T)/2=s,                          (A1)
```

not d.

Expanding the raw cross columns gives the two negative cross terms `-w/(4t_k)`, `-w/(4r_j)` and the positive term `w s/(4r_jt_k)`. Since j!=k the delta/delta term is zero. Hence the corrected physical Gram entry is

```
G_Rj^*Q0^+G_Tk
= [w/(4r_jt_k)](s-r_j-t_k)
= -w d/(4r_jt_k).                          (A2)
```

The raw upper R_j/T_k entry is `-w/(4s)`. Its **actual** Q Schur entry is consequently

```
R_Rj,Tk=(w/4)[d/(r_jt_k)-1/s].              (A3)
```

For the other mixed pair, replace j,k throughout:

```
R_Rk,Tj=(w/4)[d/(r_kt_j)-1/s].              (A4)
```

Thus simply fixing the label in(A1) while leaving (15.4) unchanged would not be a repair.

## 4. A new closed-simplex mixed bound

For the first pair, direct multiplication gives

```
4u=(1+A+K)(1+B+J)=2+(A+K)(B+J),
4sd=(1+T)(2-T)=2+TV,
4(u-sd)=(A-J)(B-K).
```

Equation(A3) therefore factors as

```
R_Rj,Tk=-w(A-J)(B-K)/(16us).                (A5)
```

The other pair has `u'=r_kt_j` and numerator `-w(A-K)(B-J)`. All denominators are strictly positive, including zero or repeated Schmidt amplitudes.

The complete nonnegative domain gives

```
w<=1/2,
|(A-J)(B-K)|<=(A+J)(B+K)<=1/4,
u>=1/2, s>=1/2.
```

The middle product bound is the elementary square inequality since its two nonnegative factors sum to1. Thus

```
|R_Rj,Tk|<=1/32,
|R_Rk,Tj|<=1/32.                            (A6)
```

This proves a bound for the **corrected** physical entries, rather than arguing that the old wrong function happened to satisfy a useful bound. No sample, coefficient assay or old finite-reference receipt is a premise.

## 5. Recompose015's actual upper principal pivot

The reported defect does not change the diagonal, same-family or same-spectator formulas in (15.1)-(15.3). Their existing arguments in015 §§3–5 remain explicit candidate dependencies to be checked by the actual reviewer; this author correction is not an independent endorsement of them. Their exports are

```
2/3<=R_rr<=1,
0<=R_Rj,Rk<=2/9, 0<=R_Tj,Tk<=2/9,
|R_Rj,Tj|<=1/4, |R_Rk,Tk|<=1/4.
```

The diagonal upper bound is the direct formula used in016: `R_Rl,Rl<=3/4+x_l^2/(16d_lb^2)<=1`, and the T analogue.

Together with(A6), each actual row has total absolute off-diagonal mass at most

```
2/9+1/4+1/32=145/288.
```

Consequently the actual physical upper R/T Schur matrix obeys

```
R >= (2/3-145/288)I=(47/288)I,
R <= (1+145/288)I=(433/288)I.                (A7)
```

In particular the two **coarser previously used numerical exports remain supported by this new composition**:

```
R>=I/18, R<=(29/18)I,                       (A8)
```

because `47/288>=16/288=1/18` and `433/288<=464/288=29/18`. The old scalar-function proof of those exports is not reinstated; (A1)-(A7) replace its defective link.

The actual Q complement has its unchanged positive bound `Q0>=I/2` on `c^perp`, with the actual reference kernel kept. Thus the corrected joint Q-perp3/R-T4 principal pivot is positive and still leaves an exact **upper P4** Schur sign, with all P cross terms retained. That P4 sign remains unproved.

## 6. Recompose016's lower pivot without dropping its reference correction

In016, d in the reference block and likelihood-ratio distribution is the genuine `d_ab`, not s. Its raw definitions, actual reference block4d, columns gC, and identity

```
L_RT_after_K,Q=3I-R-(4/3)(G-gC)^*Q0^+(G-gC)
```

are matrix identities using the **actual raw G**, not the erroneous simplified mixed entry. The likelihood-ratio argument bounds its positive Gram matrix by `9I/32`; it does not use the false (15.4) numerator. These remain explicit reviewer-check dependencies, not an assumed repaired verdict.

Insert the recomposed coarser norm export(A8) into that same lower argument:

```
L_RT_after_K,Q
>= [3-29/18-(4/3)(9/32)]I
=(73/72)I>0.                                (A9)
```

Thus no interface constant or reference-elimination rule needs to be silently changed. The true positive reference4d pivot, its Q-complement3Q0 pivot and(A9) still leave the **distinct lower P4** Schur sign. That sign also remains unproved.

This is a new candidate composition of015+this addendum+016, pending the reviewer's actual read of this addendum and its named dependencies. It is not a statement that a later repair retroactively made the original015 source correct.

## 7. Residual interface, unaffected gates, and execution boundary

The canonical four-residual specification defines its charge D8 directly from the full raw C/S/G matrices and the Tau-inverse Gram pairing, and defines L8 by the actual reference-corrected identity. It does **not** define R by substituting the wrong scalar numerator from (15.4). Therefore its literal F_up/F_low matrix definitions do not change; their claimed positive-pivot justification must now consume this additive correction before any composition is promoted. Frozen manifests/interfaces remain historical byte snapshots and require this operative overlay.

The actual charge reviewer has not yet accepted this correction. Parent charge/global promotion remains HOLD until its full correction/composition return. The separate zero017–019 return does not consume the defective mixed charge identity and supplies no repair endorsement; no verdict transfer is inferred. Checkpoint009's separate full-four phase proof is not repaired or independently accepted by this document.

All **four final signs remain UNPROVED**: charge F_up4, charge F_low4, zero Z_up6, zero Z_low6. This correction is not an all-reference theorem, W4 proof, route counterexample, admissible rank-two Werner witness, novelty finding or formal/proof-assistant verification.

The old and new symbolic coefficient sources remain preserved **HOLD/UNRUN by this worker**; no import, compile, control run, numeric-point check or replay was used to repair the source. In particular a calibration at the uniform reference has `d=s` and cannot distinguish the incorrect numerator from the correct one. No hypothetical calibration pass is an identity proof. No new scientific GO or changed execution authority is requested or implied. The parent evidence errata, including the withdrawn empty-child-handle exit attestation, remain operative.
