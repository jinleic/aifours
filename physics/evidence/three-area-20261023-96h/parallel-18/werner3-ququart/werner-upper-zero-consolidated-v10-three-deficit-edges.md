# Werner upper zero — GLOBAL gF>dij, intersecting deficit edges, and an exact at-most-three-dimensional sign gate

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE, not parent-read/reviewed/adopted.** Immediately preceding actual `/bin/date`: **Sun Oct 25 17:09:45 PDT 2026**, precreation observation only. Same ENTIRE all-positive-spectrum full complex p12/q6 operator problem; no new problem/slot/GO/deadline. All mathematics below is WRITTEN, NOT checked-in-kernel.

No scientific interpreter, calculator/eval, symbolic/numerical program, enumeration, solver/replay, test/build, scientific CLI or nested agent. HOLD v2/v9-v11/additive process history remains. The serial privacy review was actually returned before checkpoint019 and before this primary continuation. No related review upgrades these new physics candidates.

## 1. Exact named inputs

Consume the actual full-raw GFR1-GFR14 identities in `werner-upper-zero-consolidated-v7-full-raw-ground-state.md`, SHA256 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`, and the NEW global row-budget decomposition in the complete233LF `werner-upper-zero-consolidated-v9-signless-row-budget.md`, SHA256 `1a41695f8bbde665338e4daca4fdba41713472cdb20d9490ac78add2a277b616`.

Their full operative union is unchanged: generic G1–G12 `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`; FALSE-G13 correction `1b0e9a523810b5fb29cfa3c53ad287112d19803dc8110913d1b1f975817e6eb5`; ENTIRE Qraw/commutator addendum `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`; physical K_full and Schur P4/P10 `1a814168eec30b5a8698b669fceae33145862f58c1b380d0f6b679caecf8fe98`, NOT P11; literal four residuals `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`; original v24 limited identity support `55d24c07c592c8e2e3d5bdd06aa0ca2c6c1ce9d9d2a3a527398251c5b8d29248`. No region theorem, unadmitted arithmetic, or external result supplies the new mass argument. Ordinary imports: positive-factor algebra, elementary four-vertex graph reasoning, Hermitian square completion and finite-dimensional Gram/Schur equivalence.

Assume ALL ci>0, sum ci^2=1, xi=ci^2, di=1-xi, dij=(di+dj)/2, r=(sum1/di)^(-1), W=e3(d). All Z are COMPLEX with Zc=0. Off-diagonal entries Zij are twelve free complex coordinates; the four diagonals are fixed by that constraint. No real/symmetric/output-c restriction is made.

## 2. NEW stronger GLOBAL mass inequality

Fix edge ij with complement kl. Put

```
S=di+dj, T=xi+xj=2-S, L=1-T=S-1,
delta=di-dj,
R=sum_(t!=i,j) xt/[(di+dt)(dj+dt)].
```

Every pair da+db=2-xa-xb is at least1. Therefore EACH denominator in R is at least1, and

```
0<=R<=L,  delta^2<=T^2.                                 (TD1)
```

This pair-sum bound is stronger than the denominator>=di*dj bound used for the earlier v7 mass comparison. Subtract dij=S/2, rather than the weaker base g, in the EXACT v7 GFR4 identity:

```
gF_ij-dij = S^2/(8W)[2W-S(3-S)]-(S delta^2/4)R.          (TD2)
```

All signed commutator row sums remain. For h=xi*xj and v=xk*xl, normalization gives

```
W=1+2T L+(1+T)h+S v,
2W-S(3-S)=3T L+2(1+T)h+2S v>=3T L,
W<=3/2+3T L/4.                                         (TD3)
```

Using(TD1)-(TD3), with T,L in(0,1),

```
gF_ij-dij >= 3S^2 T L/(8W)-S T^2 L/4
          = S T L/(8W)[3S-2WT].
```

The final bracket is positive by an elementary exact bound:

```
3S-2WT >=3(2-T)-2T[3/2+3T L/4]
         = (3/2)L(4-T^2)>0.
```

Consequently, for EVERY positive four-spectrum and EVERY edge,

```
gF_ij-dij >=3 S T L^2(4-T^2)/(16W)>0.                   (TD4)
```

This strengthens gF>=g=dij-(di-dj)^2/4 to **gF>dij**. It does not assert entrywise positivity of the full raw correction or its inverse difference. It uses the ACTUAL mass after all row sums, not a correction diagonal. No program or sampled spectrum is used.

## 3. Negative edge coefficients cannot be disjoint

Retain the v9 exact coefficients

```
q_ij=di*dj/(4gF_ij), kappa_ij=r-q_ij.
```

Define vertex weights hj=1/dj, and for complementary pairs let

```
A=h_i+h_j, B=h_k+h_l, so r=1/(A+B).
```

The new mass bound gives

```
q_ij <di*dj/(4dij)=1/(2A).                              (TD5)
```

If A>=B, then r>=1/(2A)>q_ij and hence kappa_ij>0. Contrapositively,

```
kappa_ij<=0 ==> A<B.                                   (TD6)
```

In particular its complementary edge kl has B>A and kappa_kl>0. Thus two disjoint edges can NEVER both have negative (or nonpositive) kappa in the full positive interior. This is not a numerically observed pattern.

Let E_- be the edges with kappa<0. The four-vertex graph E_- is an intersecting edge family. It has at most THREE edges and is contained in a STAR or a TRIANGLE. An elementary proof: after two distinct edges ab,ac, a third edge intersecting both either contains a or is bc. If bc occurs, no edge through the fourth vertex can intersect all three. Otherwise every edge shares a. Empty, one-edge and two-edge cases are included. No spectrum/set enumeration was performed.

The three-edge triangle genuinely can occur: v9's exact interior x=(7/10,1/10,1/10,1/10) has kappa=-6/185 on each edge among the three small coordinates. This is ONLY a coefficient-pattern control, NOT a negative E_full witness. No universality of that triangle pattern is asserted; stars remain in the mathematical gate unless separately excluded.

## 4. Exact original target as a positive operator minus rank at most3

Let N be the positive direct sum of the FOUR actual three-dimensional row matrices N_i proved in v9 SR9-SR10. Each N_i includes all complex row variance and the row common-direction metric; it is not the false bare diagonal. Define the six linear pair forms

```
s_ij(Z)=sqrt(di/dj)Zij+sqrt(dj/di)Zji.
```

Let C_comp be the Hermitian operator whose quadratic form is the minimum of BOTH actual compatibility-square sums in v7 GFR11, over ONE common complex symmetric z6. Its pivot is the actual positive K_full/mass metric, so this minimum is attained, is a quadratic form in the twelve free off-diagonal coordinates, and C_comp>=0. No independent attainment of the varying centers is asserted.

The exact v9 full-target identity is

```
E_full =N +C_comp
       +sum_(kappa_e>0) kappa_e s_e^dagger s_e
       -sum_(kappa_e<0) (-kappa_e) s_e^dagger s_e.         (TD7)
```

Set

```
L_+=N+C_comp+sum_(kappa_e>0) kappa_e s_e^dagger s_e >0.
m=|E_-|<=3,
S_-:Z ->(s_e(Z))_(e in E_-),
D_-=diag_(e in E_-)(-kappa_e)>0.
```

Then the ENTIRE original problem, not merely a dropped-q sufficient residual, is

```
E_full =L_+-S_-^dagger D_- S_-.                         (TD8)
```

All twelve p coordinates and the ENTIRE q6 correction are retained in L_+. The negative update has rank m because each distinct s_e uses its own unordered pair of free directed coordinates; only the bound<=3 is needed below. The physical Zc=0 chart is invertible, so inertia statements in these coordinates are statements about the actual operator form, not a projected test family.

Whiten by the proved positive L_+ and use equality of the nonzero spectra of A^dagger A and AA^dagger. This gives an EXACT at-most-three-dimensional sign gate:

```
E_full>=0
  iff I_m-D_-^(1/2) S_- L_+^(-1) S_-^dagger D_-^(1/2)>=0. (TD9)
```

For m=0 the target is already strictly positive. For m>0, (TD9) is still UNPROVED. Its inverse is of the displayed fully positive operator, not a signed row metric or the false bare dual lift. Keeping C_comp here is mandatory for equivalence; dropping it gives only a sufficient test, not the original target.

Two NEW unconditional-within-the-written-imports consequences are

```
number of negative eigenvalues of E_full,c <=m<=3,
E_full,c(Z)>0 for every nonzero Z in ker(S_-),
dim_complex ker(S_-)=12-m>=9.                           (TD10)
```

They follow from(TD8), not from assumptions about the remaining Gram sign. They do NOT imply E_full>=0. The possible bad directions are confined to a star/triangle deficit interface; coupling of that interface to its positive complement remains in L_+^(-1).

## 5. Exact remaining task and nonclaims

NEW GLOBAL WRITTEN progress: actual gF>dij with quantitative lower bound(TD4); an analytic complementary-edge exclusion(TD6); at most3 intersecting negative edge coefficients; and an exact original-target gate(TD9) of dimension at most3, with the positive codimension<=3 statement(TD10). This is a new representation/reduction of the full remaining problem, not another inconsequential spectrum enumeration or a claim that positive components alone settle it.

Remaining: prove the actual star/triangle deficit Gram in(TD9) is <=I for ALL positive spectra, or produce a genuine exact separating E_full spectrum/test within authorized evidence rules. Standalone Praw may be attacked by dropping C_comp only as an explicitly sufficient problem. Full E_full/generic Z_up is NOT yet globally proved. Other three final signs F_up/F_low/Z_low, the whole asymmetric co-Choi route, and unrestricted rank<=2 W4 remain NOT_PROVED. No negative full-target spectrum or physical witness has been delivered.

This successor does not edit pinned/reviewed sources and does not resurrect FALSE G13/bare dual lift. All new assertions require complete-source reconstruction and parent disposition. No formal/kernel/configured-family/human/executable/triple-witness/novelty gate or scientific GO/park follows. Original science cutoff2026-10-27T11:05:38-07:00 and delivery deadline12:35:38-07:00 unchanged.
