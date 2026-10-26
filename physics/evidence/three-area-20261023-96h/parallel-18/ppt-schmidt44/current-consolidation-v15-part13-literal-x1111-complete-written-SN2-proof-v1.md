# CURRENT P44 CONSOLIDATION v15 — PART13/13: complete WRITTEN Schmidt-number-two proof of the literal original input x=(1,1,1,1), with no computed table

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 22:39:46 PDT 2026**. Exact WRITTEN mathematics only. Every identity below is checked by hand with exact rationals and radicals. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## X0. What this part settles, and its exact relation to old21

NEW claim C32: **the literal original N4 assay input R=R_(1,1,1,1) (rho=R/49) has Schmidt number EXACTLY two**, by a complete written operator decomposition. The original constructive target is therefore retired against EVERY witness, if reconstructed. This is not a solution of P44.

Relation to old work (additive, no edit):
- The older owner packet `rational-x1111-schmidt-two-certificate-v1.md` (October 25 04:13) proposed the same eight-vector core ensemble (its (1)–(2)) and the same six-generator residual M (its (5)).
- It then relied on a 21-pair conic table obtained by withdrawn pre-correction kernel arithmetic. That table is the permanent **old21 NOT_RECONSTRUCTED** item.
- **This part does NOT replay, validate, use or credit that table.** The JSON table was not opened while preparing this part; earlier session history is not re-attested. The older markdown, which quotes one example row, was read before writing, and that row is not used. This part replaces the table by a NEW three-piece written decomposition of M (X4). The eight-vector identity and rank proof are re-derived here by hand (X2).

**Correction of scope in Parts 10 and 11 (additive).** Part10 H6 and Part11 V3 said the literal input's Schmidt number was UNKNOWN and that it lay outside every proved region. That was accurate at their writing: no admissible complete proof existed, and old21 was not reconstructed. It was incomplete because it did not name the old21 candidate. With C32, the literal input is now covered by a complete written proof. The remaining open balanced core of the chart (Part11 V3) EXCLUDES this point; other balanced points remain open. The frozen Part10/11 bytes are unchanged; this paragraph is the additive successor note.

The complete current union is ALL THIRTEEN parts and endings:
- the twelve parts bound in `checkpoint-087-complete-current-v14-twelve-part-manifest-rank-five-v1.json` (SHA256 378712c3c1fe27586214ad276521891f694e7d924b6fd0c97692ac84d3baec6d);
- THIS part;
- every mandatory overlay named there.

All process findings remain permanent, including cp083 and cp085.

## X1. The input and its generators

With kets ij=|i>_A|j>_B, P(y)=yy*, x=|0>+|1>+|2>+|3>:

```
a=00+11+22, b=01+12, c=10-21, d=02+30+31+32+33, e=20+33,
f=30, g=32, h=00+01+02+03, j=23,
R=P(a)+P(b)+P(c)+3[P(d)+P(e)+P(f)+P(g)+P(h)+P(j)],  Tr R=49.      (X1.1)
```

This is the Part10 chart (H1.1) at x=(1,1,1,1), i.e. the literal published-source compression used by the original N4 proposal. Its PPT property is the earlier written Gram identity; the SN statement below does not need it.

## X2. Eight-vector core ensemble — exact identity and rank

Let gamma=sqrt(30)(1-i)/12, so gamma^2=30(-2i)/144=-5i/12 and |gamma|^2=5/12. The eight choices are:
- delta=+2i/3 with beta,chi each independently in {+gamma,-gamma};
- delta=-2i/3 with beta,chi each independently in {+conj(gamma),-conj(gamma)}.

For each choice put

```
psi = a + beta b + chi c + delta d - delta e + delta(chi-1) f + delta(beta-1) g.   (X2.1)
```

**Rank exactly two.** The coefficient matrix has rows:
- [1, beta, delta, 0];
- [chi, 1, beta, 0];
- [-delta, -chi, 1, 0];
- [delta chi, delta, delta beta, 0], which is delta times row1.

Column 3 vanishes. The 3x3 determinant of rows 0–2 is 1-delta(beta^2+chi^2)+delta^2.
- For delta=2i/3: beta^2+chi^2=2gamma^2=-5i/6, so delta(beta^2+chi^2)=(2i/3)(-5i/6)=5/9 and delta^2=-4/9. The determinant is 1-5/9-4/9=0.
- The conjugate branch is identical: (-2i/3)(5i/6)=5/9, and delta^2=-4/9.

The minor [[1,beta],[chi,1]] equals 1-beta chi with |beta chi|=5/12, so it is nonzero and the rank is exactly 2.

**Exact average.** Let v=d-e-f-g, and average uniformly over the eight choices.
- Means of beta, chi, delta, delta(chi-1)=delta chi-delta and delta(beta-1) all vanish. Within each delta-branch the beta/chi signs average to zero, and E[delta]=0.
- Second moments:
  - E|beta|^2=E|chi|^2=5/12, and E[beta conj chi]=0;
  - |delta|^2=4/9;
  - E|delta(chi-1)|^2=(4/9)(5/12+1)=17/27, and the same for g;
  - d-e: -4/9; d-f, d-g: -4/9; e-f, e-g: +4/9; f-g: (4/9)E[(chi-1)(conj beta-1)]=4/9.
- Every cross with b or c vanishes. For example, b-g is E[conj(delta)(|beta|^2-beta)]=(5/12)E[conj delta]-E[conj(delta) beta]=0, using the branchwise sign average.

Hence

```
A := (1/8) sum P(psi) = P(a)+(5/12)[P(b)+P(c)]+(4/9)P(v)+(5/27)[P(f)+P(g)],      (X2.2)
```

since the f diagonal is 4/9+5/27=17/27 and every v-entry matches the listed covariances.

## X3. The six-generator residual

Subtracting (X2.2) from (X1.1) gives exactly

```
R = A + (7/12)[P(b)+P(c)] + F M F*,                                      (X3.1)
```

Here F has columns (d,e,f,g,h,j), and in coordinates y=(p,q,t,u,r,s) for p d+q e+t f+u g+r h+s j,

```
M = 3I - (4/9) z z^T - (5/27)(E_tt+E_uu),   z=(1,-1,-1,-1,0,0).
```

Explicitly:
- diagonal: pp=qq=23/9, tt=uu=64/27, rr=ss=3;
- off-diagonal: pq=pt=pu=4/9 and qt=qu=tu=-4/9;
- every entry involving r or s off the diagonal is 0.

The vector F y has Alice rows:
- Alice0: r x+p|2>;
- Alice2: q|0>+s|3>;
- Alice3: p x+t|0>+u|2>+q|3>.

Three exact Schmidt-rank-two families (valid for any complex x):
- **Phi2 (q=s=0):** the Alice2 row vanishes. Only Alice levels 0,3 occur, so SR<=2 for ANY (p,t,u,r).
- **Phi1 (p=r=0):** the Alice0 row vanishes. Only Alice levels 2,3 occur, so SR<=2 for ANY (q,t,u,s).
- **Mixed (r u=p^2 and t s=q^2):** write (r,p,u)=(alpha^2, alpha b0, b0^2) and (t,q,s)=(g0^2, g0 d0, d0^2) with complex square roots. Then
  `F y = (alpha|0>+b0|3>) tensor (alpha x+b0|2>) + (g0|3>+d0|2>) tensor (g0|0>+d0|3>)`.
  This is a sum of two products, so SR<=2. Each Alice row checks entrywise.

## X4. NEW written decomposition of M — no computed table

**Mixed piece M3.** Take tau=2/3 and R0=S0=4/3, so R0 tau=8/9. Let beta' be uniform on the circle, d' uniform on {0, pi/2} (independent), and alpha'=beta'+d'. Put

```
y = ( sqrt(8/9) e^(i alpha'), i sqrt(8/9) e^(i beta'), -2/3, 2/3, (4/3) e^(2i alpha'), (4/3) e^(2i beta') ).
```

Then r u=(8/9)e^(2i alpha')=p^2 and t s=-(8/9)e^(2i beta')=q^2, so every member is in the mixed family. Since Re(y y*)=(P(y)+P(conj y))/2 and conj(y) is also mixed, M3 := E[Re(y y*)] is a positive combination of SR2 projector coefficients.

Its exact entries:
- **pq.** E[p conj q] = (8/9)(-i)E[e^(i d')] = (8/9)(-i)(1+i)/2 = (4/9)(1-i), so the real part is 4/9.
- **rs.** E[r conj s] = (16/9)E[e^(2i d')] = (16/9)(1-1)/2 = 0.
- **Other r/s crosses.** p-s, q-r, p-r, u-r, q-s, t-r, t-s and u-s all average a nonconstant phase in beta' or alpha', hence 0.
- **p-t, p-u, q-t, q-u.** Each averages e^(i alpha') or e^(i beta'), hence 0.
- **tu.** Re(t conj u)=-4/9.
- **Diagonal.** (8/9, 8/9, 4/9, 4/9, 16/9, 16/9).

**Free pieces.** Then M-M3 has:
- diagonal pp=qq=5/3, tt=uu=52/27, rr=ss=11/9;
- off-diagonal pt=pu=4/9, qt=qu=-4/9, and pq=tu=0;
- every other off-diagonal entry 0.

Split it as M1+M2:
- M2 on (p,t,u,r): [[5/3,4/9,4/9,0],[4/9,26/27,0,0],[4/9,0,26/27,0],[0,0,0,11/9]].
- M1 on (q,t,u,s): [[5/3,-4/9,-4/9,0],[-4/9,26/27,0,0],[-4/9,0,26/27,0],[0,0,0,11/9]].

Both are PSD. The (t,u) block (26/27)I is positive definite, and the Schur complement at p (or q) is

`5/3 - (27/26)(16/81+16/81) = 5/3 - 16/39 = 49/39 > 0`.

The r and s entries are decoupled positive diagonals. Spectral decomposition writes M2 as a positive sum of y y* with y supported on (p,t,u,r), i.e. Phi2, and M1 likewise with Phi1. Therefore

```
M = M3 + M1 + M2,                                                         (X4.1)
```

and F M F* is a positive combination (finite sums plus one circle average) of projectors onto Schmidt-rank-<=2 vectors. The closed SN<=2 cone contains it.

## X5. Conclusion and lower bound

(X3.1) and (X4.1) give an explicit decomposition of R into:
- the eight SR2 projectors of (X2.1);
- 7/12 [P(b)+P(c)];
- the three SR2 families of X4.

Hence **SN(rho)<=2**. Carathéodory turns the circle average into a finite decomposition if desired. The matching entanglement lower bound is elementary and independent of the old table. Project Alice onto {0,1,2}. Every rank-one matrix in the projected range has 11-coefficient zero: its Bob3 column forces the Alice1 row to vanish, and otherwise the minors A^2-BC and A^2+BC vanish. Yet the projected 11 diagonal is 1. So rho is entangled and **SN(rho)=2**.

Consequences:
1. The original N4 input can never be detected by any universally two-block-positive witness. The historical normalized-N4 attempt therefore could not have certified it, whatever its unknown child exit. That history remains UNKNOWN/incomplete/overrun and is not re-attested.
2. The decomposition uses the e generator in the core (delta d - delta e), which the earlier absorption families lacked. It is a candidate mechanism for further balanced chart points, but no general region is claimed here.
3. The rest of the chart's balanced core (Part11 V3) remains OPEN apart from this point.

**Original physics-3/P44 remains UNMET.** C32 is an author-WRITTEN candidate needing fresh complete reconstruction. It gives no old21 credit and no formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance. It is not a park and not a closeout.

**END OF COMPLETE CURRENT v15 PART13/13.**
