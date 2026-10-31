# Level-six type125: the entire (2,2,6) map is injective for EVERY r,s>=6 — a two-minor resultant candidate

**MathKacMoody-2 / math-3.** Native `/bin/date` observed immediately before this additive write: **Wed Oct 28 20:47:38 PDT 2026** (precreation observation). New exact-computation-assisted written argument, **UNREVIEWED**: not parent adoption, formal/kernel, human, independent-model, priority or novelty acceptance.

## 1. Exact claim

For EVERY pair of integers `r,s>=6` and every allowed FULL complex Cartan realization C of A(r,s), let `S=G_C/J` be the original Serre quotient and `P_(2,2,6)=ker f1 ∩ ker f2` in degree (2,2,6). At exactly the named UNREVIEWED full-Cartan/free-Levi/PBW source-identification inputs already used by the pinned strip candidate `frontier-20261028-level6-226-gap41-strip-candidate-v1.md` (SHA `a9d70a2b7da3b93056999cff6771997593e78d2d4cc12a3ac46a33d094f75f40`), which identify `P_(2,2,6)` with the 34-dimensional free-Levi joint horizontal kernel and the actual target with the 235 affine target rows:

> **Candidate theorem.** The ENTIRE original map `D3: P_(2,2,6) -> S_(2,2,5)` is injective for all integers `r,s>=6`.

This is **effective and complete on the quadrant** for this one primitive type: no exceptional pair remains, no Faltings/Siegel or Hilbert-irreducibility import is used, and no density or finite-residue restriction is needed. The earlier strip, ratio-cone, modular-row, density-one and cofinite candidates for this type become special cases but remain separate pinned routes. Nothing is claimed for the other six level-six primitive types, the small-row regime `min(r,s)<=5`, F6/B6, arbitrary-GCM/all-level Serre, a non-Serre witness, novelty or priority.

## 2. Two actual maximal minors

Put `x=r-6,y=s-6`. The full affine 235×34 matrix `M(x,y)` of D3 on the 34 kernel vectors is taken byte-pinned from `frontier-20261028-level6-226-ratio-cone-certificate-v1.json` (SHA `ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b`), whose rows were rebuilt by the separate tree-Jacobi engine in `frontier-20261028-level6-226-ratio-cone-independent-replay-v1.json` (SHA `3eb7f2f9ee8211b3510715eddc72f56bb5cc85d1c2aab67b63b1225033437879`). Every entry is affine in x,y, so each 34×34 minor has total degree ≤34.

- `P1` = the previously pinned selected minor: `P1=393216(x+5)^4(y+5)^7(2x+2y+19)^2 R`, R of total degree 21, `[y^21]R=2107392`.
- `P2` = the same rows with slot 0 replaced by target word `00601`: exactly
  \[ P2=-3145728\,(x+5)^3(y+5)^7(2x+2y+19)^2\,R_2, \]
  where `R2 in Z[x,y]` is primitive, has 276 terms, total degree 22 and constant leading coefficient `[y^22]R2=44255232`.

All displayed linear factors are strictly positive on `x,y>=0`. If `M(x0,y0)` had rank <34 at an integer point of the quadrant, both minors would vanish, hence `R(x0,y0)=R2(x0,y0)=0`.

## 3. The resultant excludes every integer fibre x0>=0

Let `H(x)=Res_y(R,R2)` with formal y-degrees 21,22. Both leading y-coefficients are nonzero constants, so for every complex x0 the specialization identity `H(x0)=Res(R(x0,·),R2(x0,·))` holds, and `H(x0)=0` iff `R(x0,·)` and `R2(x0,·)` have a common complex root. The total-degree bound gives `deg H<=21·22=462`. The exact computation gives `deg H=462` and

\[ H=(x+5)^{11}(x+6)^{18}(x+4)^{18}(x+3)^{3}(x+2)^{2}(x+1)(4x+19)^{16}\,H_2,\qquad \deg H_2=393, \]

with every listed multiplicity exact. Every listed linear factor is positive for `x>=0`.

`H2` has **no integer root**: every complex root obeys the Cauchy bound `|z|<=B=1+⌈max_{i<393}|h_i|/|h_393|⌉`. Modulo the prime 1009, `H2` keeps its degree and is squarefree, so each of its 15 roots mod 1009 is simple; by Hensel uniqueness (Stacks [06RR](https://stacks.math.columbia.edu/tag/06RR), complete rings henselian [04GM](https://stacks.math.columbia.edu/tag/04GM)) an integer root z would equal the symmetric residue of the unique 1009-adic lift of `z mod 1009` modulo a power `1009^k>2B`. All 15 symmetric lifts exceed B in absolute value. The independent replay repeats this at the different prime 5003 (8 roots, no lift within the bound).

Therefore `H(x0)!=0` for every integer `x0>=0`; for every integer point of the quadrant, P1 or P2 is nonzero; `M` has rank 34; and D3 is injective on the whole 34-dimensional `P_(2,2,6)`. This proves the candidate theorem at the stated inputs.

The vanishing of H at x=-6,-5,-4,-3,-2,-1 and -19/4 (r=0,1,2,3,4,5 and r=5/4) concerns parameters outside the quadrant and is not interpreted as a kernel of any actual algebra.

## 4. Exact evidence

- Producer `frontier-20261028-level6-226-two-minor-resultant.py`, 229LF SHA `fa8be638bacacf9c8910af6b42168fd204bf2962a95abdd2cb877b1e9423246e`: recomputes P1 and P2 by total-degree interpolation on the pinned rows, checks P1 against the pinned R, divides P2 exactly, evaluates H by exact univariate resultants at x=0..470, interpolates on 463 points and checks the other 8, divides out all linear factors with exact multiplicity checks, and builds the p=1009 certificate. Output `frontier-20261028-level6-226-two-minor-resultant-v1.json`, 5024LF SHA `e410b55d3e4252c1bc7d88db77d16cf85ced36b5069b9bdf47bb51edcda81bba`, PASS at **Wed Oct 28 20:45:36 PDT 2026**.
- Separately authored replay `frontier-20261028-level6-226-two-minor-independent-replay.py`, 245LF SHA `55861cb4502064104b656217927e9790e079e5c00795c10a030635cd7db0400e`, imports no producer code: 630 own fraction-free determinants on a SHIFTED unisolvent triangular grid reproduce P2; own integer convolution rebuilds the P2 factorization; own Gaussian Sylvester eliminations match H at 463 points modulo each of two 60-bit primes (926 checks) plus 5 exact integer Sylvester determinants; own division checks every linear factor and multiplicity; own Hensel lifting at p=5003 excludes integer roots. Output SHA `b62c6543cf32144a28bd1caeb246fdb89bdffd7a10d5198ca14aea9c731165f7`, PASS at **Wed Oct 28 20:47:06 PDT 2026**.

The two programs share the pinned matrix and R data and were written by the same owner; this is exact computation, not independent-model, human or formal verification.

## 5. Gates and history

Required before adoption: full scientific review of the source identification inputs (unchanged from the strip candidate), the two-minor reduction, the resultant specialization and Hensel argument, and a source/code audit of both programs and their pinned inputs. All earlier ZERO/STOP/HOLD/process findings, the incidental older cone-status exposure, and the separate pending F5 audit remain unchanged; no held guide is a premise.

**END — all-parameter (2,2,6) injectivity candidate at named source inputs; independent review pending.**
