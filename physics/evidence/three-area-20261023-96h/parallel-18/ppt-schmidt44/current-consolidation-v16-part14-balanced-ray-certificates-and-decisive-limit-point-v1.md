# CURRENT P44 CONSOLIDATION v16 — PART14/14: exact SN2 certificates on the balanced ray, the decisive limit point (1,1,-1,0), and a universal failure of the Alice-3 peel route

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 22:52:09 PDT 2026**. Exact WRITTEN mathematics only, using exact rationals and radicals. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## B0. Scope and union rule

NEW claims C33.1–C33.4 continue the ORIGINAL compression chart R_x (Part10 H1.1). They:
- extend Part13's e-including mechanism to a general lemma (C33.1);
- give exact certificates at further balanced points (C33.2);
- identify the decisive remaining point by an exact closedness argument (C33.3);
- prove that one natural peel-off route fails at EVERY chart point (C33.4).

No P44 solution and no SN3 claim. The complete current union is ALL FOURTEEN parts and endings:
- the thirteen parts bound in `checkpoint-088-complete-current-v15-thirteen-part-manifest-x1111-SN2-v1.json` (SHA256 c0738969ad1a4f2d0d1cb3497ad5ce92cbae0528e748c4082b2c74228a940d0b);
- THIS part;
- every mandatory overlay named there.

Process records cp083/cp085/cp089 (cadence miss and repeated private decimal-heuristic exactness occurrences, ZERO credit) are permanent. Nothing here relies on approximate reasoning. Parts 9–14 are LATER UNREVIEWED; nothing is inherited.

## B1. C33.1 — the e-including core lemma for any chart point with v!=0

Let x=(u,v,w,z), v!=0. Choose a complex delta!=0 and beta0, chi0 with

`z beta0^2 + chi0^2 = 1/delta + delta z`.                                   (B1.1)

Average uniformly over the eight members:
- branch delta: beta in {+-beta0}, chi in {+-chi0};
- branch -delta: beta in {+-i beta0}, chi in {+-i chi0}.

The squares in the second branch are negated, so (B1.1) holds there with -delta. Each member is

`psi = a + beta b + chi c + delta d_x - delta z e + delta(v chi-u) f + delta(v beta-w) g`.

**Rank.** In (H1.2) the rows are:
- row0 = [1, beta, delta, 0];
- row1 = [chi, 1, beta, 0];
- row2 = [-delta z, -chi, 1, 0];
- row3 = [delta v chi, delta v, delta v beta, 0], which is delta v times row1.

The 3x3 determinant of rows 0–2 is 1-delta(z beta^2+chi^2)+delta^2 z=0 by (B1.1). The minor 1-beta chi is nonzero whenever |beta0 chi0|<1, so the rank is exactly two.

**Moments.** Sign averaging kills all means and every b/c cross. The b-g and c-f crosses vanish because E[conj(delta)]=0 within the branch average. The average is

```
P(a) + |beta0|^2 P(b) + |chi0|^2 P(c)
  + |delta|^2 [ P(d_x - z e - u f - w g) + |v|^2(|chi0|^2 P(f) + |beta0|^2 P(g)) ].   (B1.2)
```

Here the cross covariances are the entries of |delta|^2 n n*, with n=(1,-z,-u,-w) on (d_x,e,f,g).

The residual in coordinates (p,q,t,u',r,s) for (d_x,e,f,g,h_x,j) is

`M(x) = 3I - |delta|^2 n n* - |delta|^2|v|^2(|chi0|^2 E_tt + |beta0|^2 E_u'u')`,

plus (1-|beta0|^2)P(b) and (1-|chi0|^2)P(c). The three SR2 families of Part13 X3 (Phi1, Phi2, mixed) hold for ANY complex x. So **R_x is SN<=2 whenever |beta0|,|chi0|<=1 and M(x) lies in the cone they generate.** This is a checkable sufficient criterion. Part13 is the case x=(1,1,1,1), delta=2i/3.

## B2. C33.2 — exact certificates at x=(s,s,s,s), s=2,3,5

Take delta=i theta, beta0=chi0=gamma with gamma^2=(1+s delta^2)/(delta(s+1)), n=(1,-s,-s,-s). Use the Part13 mixed piece with tau=theta s and R0=S0=2 theta. It contributes:
- diagonal (2theta^2 s, 2theta^2 s, theta^2 s^2, theta^2 s^2, 4theta^2, 4theta^2);
- pq = theta^2 s;
- tu = -theta^2 s^2;
- no r/s crosses.

M-M3 is then supported on the two free cliques. Split its t and u diagonals equally between them.

| s | theta | |gamma|^2 | (pp,qq,tt=uu,rr) of M-M3 | Schur at p | Schur at q |
|---|---|---|---|---|---|
| 2 | 2/5 | 17/30 | (11/5, 43/25, 509/375, 59/25) | 4831/2545 | 6527/12725 |
| 3 | 1/4 | 13/16 | (41/16, 33/16, 363/256, 11/4) | 41/16-12/121 | 2265/1936 |
| 5 | 4/25 | 109/120 | (1699/625, 263/125, 427/375, 3-64/625) | positive (pp>2, deficit <1) | 35501/53375 |

Each entry is an exact rational computation from (B1.2), M(s) and the M3 data. Two checks for s=5:
- M(5)_tt = 3-(16/25)(229/120) = 667/375;
- minus tau^2 = 16/25 gives 427/375.

Every Schur complement above is positive, so M1 and M2 are PSD. The b/c residuals 1-|gamma|^2 are nonnegative. **Hence R_(s,s,s,s) is SN<=2 for s=2,3,5** (together with s=1 from Part13). Points with 4s^2<=2 lie in the Part6 ball. No interval theorem between these points is claimed.

By the unitary torus of Part10/Part6, all torus images of these points inherit SN<=2. So do their source-involution images, by invertible local filters.

## B3. C33.3 — the decisive limit point x0=(1,1,-1,0)

The Part6 source involution gives R_(s,s,s,s) ~ R_(1,1,-1,1/s) by an invertible local filter, so the Schmidt numbers are equal. R_x depends continuously on x, and the set {SN<=2} is closed. Therefore:
- if R_(1,1,-1,z') is SN<=2 for all sufficiently small z'!=0, then R_x0 is SN<=2;
- if R_x0 has Schmidt number 3 (an open condition), then R_(s,s,s,s) has Schmidt number 3 for all sufficiently large s.

So **x0 controls the far balanced ray**, and a P44 solution inside this chart is most plausibly located near x0.

Exact method limitations at x0 (not SN3 evidence):
1. Here z=0, so (B1.1) reads chi0^2=1/delta and the e-coefficient vanishes. Budget |chi0|<=1 forces |delta|>=1. With n=(1,-1,1) on (d,f,g):
   `n^T(3I-|delta|^2 n n^T)n = 9-9|delta|^2 <= 0`.
   The added positive f-diagonal load |delta|^2|v|^2|chi0|^2 then makes M(x0) fail to be PSD. C33.1 cannot certify x0 with uniform |beta0|,|chi0|.
2. x0 lies outside the Part6 ball (normx^2=3) and outside Theorems A (v!=0), C (u not dominant) and D (w!=0).

## B4. C33.4 — the Alice-3 peel-off route fails at EVERY chart point

Compress Alice onto span{|0>,|1>,|2>}. For every x the result is

`S_x = P(a)+P(b)+P(c)+3P(02)+3P(20)+3P(23)+3P(|0> tensor x)`.

**Claim: S_x is entangled for every complex x.** Consequently Part12 Lemma P can never be applied through this compression.

Proof. A product vector in range(S_x) with nonzero Alice-1 component has its Alice-1 and Alice-2 rows proportional:
- row1 = (c3, c1, c2, 0);
- row2 = (c5, -c3, c1, c7).

So c7=0, c2!=0, alpha2:=c1/c2, and row1 = c2(-alpha2^2, alpha2, 1, 0) (zero Bob-3 entry). Any other product in the range has zero Alice-1 row.

The Alice-1 diagonal block of S_x is I_3 on Bob{0,1,2}, contributed by a, b and c only. If S_x were separable, a decomposition through range products would give

`sum |c2|^2(|alpha2|^4, |alpha2|^2, 1) = (1,1,1)`.

Then sum |c2|^2(|alpha2|^2-1)^2 = 0, so |alpha2|=1 on every term.

Now take the Alice-0/Alice-1 block. It equals e0 e1^T + e1 e2^T, from a and b; the h_x, 02, 20 and 23 terms do not touch Alice1. In a range-product decomposition it is

`sum |c2|^2 alpha0 (-alpha2^2, alpha2, 1)(-alpha2^2, alpha2, 1)*`,

where alpha0 is the Alice-0 amplitude. With |alpha2|=1 its (0,1) entry is -sum|c2|^2 alpha0 alpha2 and its (1,2) entry is +sum|c2|^2 alpha0 alpha2. They cannot both equal 1. Contradiction. QED.

This is a whole-chart METHOD barrier for one compression, not a statement about SN(R_x).

## B5. Updated chart map and gap

Proved SN<=2 points and regions:
- the Part6 ball and projective region;
- the axes;
- Part10 Theorems A/C (and the involution w-dominant region);
- Part11 Theorems D/D';
- Part13 x=(1,1,1,1);
- this part: x=(s,s,s,s) for s=2,3,5 and all torus/involution images of the listed points.

OPEN: the comparable-component core, including x0=(1,1,-1,0), which controls the far balanced ray.

**Original physics-3/P44 remains UNMET.** These are author-WRITTEN candidates pending fresh complete reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v16 PART14/14.**
