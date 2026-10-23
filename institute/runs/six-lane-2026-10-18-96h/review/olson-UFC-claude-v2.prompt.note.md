**UFC v1 written review** (proof `2d03076c…`, package `6f2262d1…`, read under the governing fixed-parameter finiteness clarification)

**Counts: FATAL 0 / MAJOR 0 / MINOR 1.** Every step was re-derived by hand from the pasted literal UMR interfaces. No computation or enumeration was used.

## Claim-wise verdicts

| Claim | Source LF (proof unless noted) | Verdict |
|---|---|---|
| (D1)–(D4), F1/Couple, F2, F3 | 35–68 | Correct; literal UMR inputs |
| Parameterisation; T0 ⇔ j≥2v−1 | 72–81 | Correct; exact linear equivalence, no rounding |
| U0, p≡1 mod 4 (I1–I3) | 23–27, 85–120 | Correct for every frame |
| U0, p≡3 mod 4 (A1–A5) | 122–191 | Correct for every frame |
| U0 ⇒ no target NF in T0 | 25–26, 119–120, 190–191 | Correct: frame exists (UMR LF111–112); identity Xi_ev+Xi_od=e≥0 (verdict LF10) |
| E0 | 200–205 | Correct on all of T |
| rho / ENV | 209–226 | Correct on all of T |
| U1 / R_U | 28–31, 228–263 | Correct as a one-way necessary relaxation; finite only per fixed (kappa,p), per the correction |
| HIGH-COVER | 265–271 | Correctly marked UNPROVED. It is the first unproved step of this method, not shown false, necessary or nonempty |
| (8,23) | 285 | EXCLUDED (Sec.4, j=6≥3) |
| (9,23) | 286 | EXCLUDED (Sec.4, j=6=2v) |
| (10,29) | 288 | EXCLUDED (Sec.3, j=8≥5) |
| (10,23) | 287, 294–322 | OPEN; R23 is a faithful specialisation of R_U |
| Sec.5.4 limitation remark | 273–278 | MINOR-1 (scope/wording) |

**Answer to TARGET:** yes. On T0 the count covers every frame of every admissible NF under the full existential antecedent. U0 uses none of these premises: extra-pair placement, nonempty-run, o_F, rotation-pair, rigidity, UB, saturation, Lemma 15–20, FC717/FC19 or FCW/balfull.

## Re-derivation of load-bearing steps

**Interface**
- **(W_r) windows.** UMR Lemma 8 (LF163–165) gives low=Pi0+2−y−2p and up=−2−nu+x. Since Pi0=e+R−nu, low=e−g+2−nu−y.
- **Scope of the windows.** UMR-F (verdict LF9) includes level kappa+1. So the windows hold for every r-subset of S_ev/S_od with d≤r≤kappa+1. These subsets are proper because kappa+1≤h−1 ⇔ d≥2.
- **(1).** e=(nu−a)+(Pi0−a′), and nu≡a mod 2 because each |c_l| is odd.
- **Couple.** Every use places Q1 and Q2 in different alternating sets. So B1∪B2 lies outside L(Q1)∪L(Q2), and the outside letters are ≤ alpha′(Q1)+alpha(Q2).
- **F3.** R−(ell+M)=2p−2−2kappa>0, so the three cases are disjoint and exhaustive.

**Parameters**
- **p=4j−3:** h=2j−1, R=6j+2v−6, delta=4v−2, ell_j=M_j=2v, 3≤v≤j−2. The bound (3p+5)/8=(3j−1)/2 is equivalent to j≥2v−1.
- **p=4j−1:** h=2j, R=6j+2v−2, delta=4v; (ell,M)=(2v+2,2v) at level j and (2v,2v+2) at level j+1; 2≤v≤j−2. The bound (3p+7)/8=(3j+1)/2 is equivalent to j≥2v−1.
- The a′ bounds, the balance level m=(p+3)/4, and every row of the LF283–289 table are correct.

**Sec.3 (I1–I3)**
- **I1.** All constants check: −v−E(B), v−1−z−E(B), −d−z, and (IH) −d−z+2n(B).
  - P/Q have t≤0 because 2v−2−nu−z<j.
  - Q with t=0 gives 2j−2v+2≤nu+z≤2v−2, which contradicts j≥2v−1.
  - In the H case the outside letters number alpha+alpha′=a+z−2beta′≤nu+z.
- **I2.** All four pair types close.
  - Two P: impossible, since 5j>7v−5.
  - P with Q: sum ≤−2d.
  - Q/Q with both t=−1: summing gives z1+z2≥2d+2+nu, so the sum is ≤−2−nu.
  - Q/Q mixed: equality would force L(J1)=L(J2)=A, disjoint, so A=∅. Then J2 is empty and t2 is even, not −1.
- **I3, ordinary cases.** q′(J2)>2v−2, so J2 is G or Q. The G case gives ≤−2j+4v−3≤−1. Both Q cases give ≤−2d+m≤0; equality forces lam=0, so S2 is empty.
- **I3, bottom-j corner (LF115–117).** Equality forces d=v−1 (hence j=2v−1), m=2v−2, nu=a and a≤2v−2.
  - Let K be ranks j..2j−1 of S2. K is a j-subset, so its window is available even though it overlaps J2.
  - Every run of K is empty with theta≤−2, so Theta(K)≤−4v+2.
  - y_j(K)=2v−a, because 2v−a≥2>eps and ell−q′<0.
  - The lower window gives Theta(K)≥e−4v+4. This is a contradiction.
- **Coverage.** I2 and I3 together cover every pair of classes.

**Sec.4 (A1–A5)**
- **A1 constants:** −v−1−E(B), v−2−z−E(B), (AH), −v−E(C), and for Q+ (where t+≥0 is impossible because 2j−2v+4≤2v−2 fails) v−1−z−E(C) and −d−z. The six classes are exhaustive.
- **A2:** −2d−2, −4−nu, −2d, the parity contradiction in the mixed case, and ≤−v+(v−1) for pairs containing G/G+.
- **A3:** q′(Q)>2v for every Q⊂S2, which is equivalent to 5j>7v−4. The bounds are −5, −3, −2, −2.
- **A4:** z+=R−z0−beta(u)+beta′(u), a≤4v, o≤z0+z+, and q′(Q⊂S′)≥6d+2v−2>2v. The sums are 1−2d, 3−2d and 2−2d.
- **A5.1:** eliminating beta gives nu−a+2alpha≤2v−j. Both terms on the left are even and nonnegative, so at j∈{2v−1,2v} we get nu=a and alpha=0. The branch is vacuous for j≥2v+1.
- **A5.2:** u is nonempty, since beta(u)≥6j−2v−2>2v+2. Hence q(Q_w)>ell_j. If eps dominated, the window would give Theta≤−1−nu<0, which is impossible. Also q′(Q_w)=o+a+beta(w)−beta′(w). These give (A5.2) for every w∈J.
- **A5.3:** the identities Σbeta(w)=beta(J)≥2d−a, Σbeta′(w)=a and ΣE=(j−1)E(J) give the stated inequality.
  - The right side is j(2v−3)+1 or j(2v−3), so o+a≤2v−3.
  - The right side equals (2j−2)(v−1) exactly when j=2v−1, giving a≤v−1. It is smaller when j=2v, giving a≤v−2.
- **A5.4:** t′+≤−2 is refuted using ranks j+1..2j of S′: y_j≤2v−a, so Theta≥e−2j+2, against ≤−2j. Then the t′+=−1 bound gives lJ≥d+2+a.
- **A5.5:** t+≥1 forces j+1≤2v−2a−o, so a=o=0, contradicting lJ≥d+2. With t+=0 the sum is ≤2v−5d−7−6a−lB≤−3v−2. All constants hold uniformly in v.

**E0, ENV, residual**
- **E0.** At level d, y_d=0, so at most d−1 negative empty runs. That leaves kappa+1 positive empty runs, but x_{kappa+1}=0 bounds their sum by −2. Contradiction.
- **rho.** rho(0)=2 and rho(1)=3 are correct, and the empty-run bounds hold for every sign of the threshold.
- **ENV.** C_r and D_r are correct, and D_r uses (D4) as stated.
- **R1–R4.** These are literal: UMR LF64–68, 90–98, 201–209, 266–274, 300–302 and 315–324. Each test is necessary for actual frames, so U1 holds.
- **R23.** All numbers check: 24/42/4/2/16/12, ell_m=22−2m, M_m=2m−4, lower window e−2−nu−y, d−2=0, lo=11−r, hi=57−3r, run pair ≥26, threshold 14, |c|≤17, reservoir |c|+19, a′≥17, |theta|<46, Theta(all)=e−2nu−4.
- **(10,23) remarks.** A positive level-6 P threshold forces nu=q′=0, so S′ is empty, which violates E0. (HighQ) with right side 2 allows exactly (0,0), (0,1), (2,0). No exclusion or realisation is claimed.
- **Named-cell notes.** For (8,23), A5 is vacuous. For (9,23), Steps 3–4 are vacuous (d+2+a≤o≤3−a is impossible), but the bounds remain valid. For (10,29), the I3 corner is unreachable because d=5≠v−1.

## MINOR-1: Sec.5.4 limitation paragraph, proof LF273–277 (non-load-bearing)

**Step.** "For arbitrary high-strip parameters the same A5 derivation gives only (HighQ)…" The A5 hybrid exists only in the p≡3 mod 4 two-level setting.
- For p≡3 mod 4, (HighQ) is valid on all of T, and its right side is ≥2 in the high strip.
- For p≡1 mod 4 the analogous single-level Q-branch with t≥0 gives nu−a+2alpha≤2v−2−j. At j∈{2v−3,2v−2} this does force nu=a and alpha=0; (12,29) is an example.
- In that class, the j≥2v−1 uses in Sec.3 are I1's threshold controls (LF91–94) and the d≥v−1 margins (LF103–117).

LF277 ("No assertion … repairs these missing inequalities") also reads as an unproved no-go claim.

**Consequence.** None for U0, U1, E0, ENV, R_U, R23 or HIGH-COVER, because R_U retains the whole strip (LF278). A reader could, however, misplace the high-strip obstruction for p≡1 mod 4, or read LF277 against erratum v2.

**Minimal repair (wording only).**
- Restrict (HighQ) to p≡3 mod 4, and name the Sec.3 inequalities that fail for p≡1 mod 4.
- Replace LF277 with: "This packet substitutes no saturation assertion, selected UB failure or small-cell constant for these inequalities."

## Observations (no repair needed)

- **O1.** R2 follows from R1's retained windows together with (D2) and (D4). Actual frames always satisfy H_ev+H_od≥e≥0. So HIGH-COVER is equivalent to "every actual frame satisfies both UB", which is equivalent to nonexistence on T∖T0. This matches the packet's "equivalent exclusion target, not a reduction" (LF270–271).
- **O2.** The governing correction resolves "finite" at LF30 and LF231. Each fixed (kappa,p) has finitely many occurrence partitions, labels (|c_l|≤p−6) and theta values (|theta_i|<2p). No finiteness of the union over T∖T0 is asserted.
- **O3.** The I3 corner uses j=2v−1 implicitly, via d=v−1. The step is valid.

## Scope separation

- **Correctness.** U0, U1, E0, ENV, the R_U/R23 definitions, and the outcomes for (8,23), (9,23), (10,29) are correct as written. They depend only on accepted UMR at its literal scope, so no claim is left conditional.
- **Completeness.** Full UFC is not established. T∖T0 remains open at HIGH-COVER, and (10,23) is OPEN. R_U carries no converse, existence or inverse-NF content.
- **Process, priority, computation.** No FC717/FC19 lemma or constant enters any count. Process certification is not assessed here. No priority, novelty, Lean, human-referee or runtime claim is made or assessed.
- **Not approved:** the full research target and runtime.
