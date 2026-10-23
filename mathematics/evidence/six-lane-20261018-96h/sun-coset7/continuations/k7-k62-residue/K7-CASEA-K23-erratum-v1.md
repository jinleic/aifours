# K7-CASEA-K23-erratum-v1: R3' displayed t-weight is 1/2, not 1

Written: 2026-10-19T08:11:18-0700 (`/bin/date` immediately before exclusive create). Owner: Sun7K62Successor.
Overlay: `D/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`. Self-found arithmetic typo in a displayed weight vector; no theorem conclusion is changed.
This overlay must accompany the parent-owned R2 review, and the R3 transfer audit must use its corrected row.

## Item K23.1 (verbatim Old -> New)

Old, section 1 rigid-row list:

```text
  - R3 (K7-TC) and **R3'** (y = (o 1, f 1/2, s 1/2, s' 1/2) and (o 1, s 1/2, s' 1/2, t 1); {f,s,s'}, {t,s,s'}, {z,s,s'} have
    all gcds 2; {f,t,s}, {z,t,s}, {z,f,s}, {z,f,t,s} are allowed of weight 1 (E >= 2)): **L_f = L_t and L_z subset L_t**.
```

New:

```text
  - R3 (K7-TC) and **R3' = (1,2,2,4 | 4)**: for R3' use y1 = (o 1, f 1/2, s 1/2, s' 1/2) and
    y2 = (o 1, t 1/2, s 1/2, s' 1/2), all unlisted weights 0. Both have value 5. The one o is coprime to every
    other label (Sun(2)); two twos cannot share a fibre with f or with t (all gcds 2, Sun(3)), so both vectors
    are feasible. Equality of the two fibre weights gives 1_(f in S_C)=1_(t in S_C), hence L_f=L_t. If z is
    in S_C, o is not; without f,t the two value-1 conditions would force both s,s', forbidden with z by Sun(3).
    Thus L_z subset L_t. These containments are asserted under the full equality clause in setting (a1).
```

The old second vector had value 7, and was not feasible (t and a two can share a fibre), so it cannot serve as the
advertised value-5 vector. The corrected t weight 1/2 gives value 1+2+1+1=5 and the displayed feasibility proof.
For a fibre without o, subtracting the two weight-1 equations gives membership f iff membership t. For a fibre
with o, both f and t are absent by Sun(2), so the same conclusion holds. In the full setting, a fibre with z cannot
hold o (gcd 1), nor both twos (all pairwise gcds 2, Sun(3)); its weight-1 equation therefore forces f and then t.

No source byte is overwritten. This is a corrected proof display, still pending review. In the (a2-zt5) audit one
must continue to justify any z-containment separately through the available zero-weight/omitted-vertex clause;
no blanket full-FG conclusion is imported. The uses of R3' in K2 need L_f=L_t, whose corrected vectors vanish on z.
