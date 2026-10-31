# Review v1: wave f160-ph7-threshold-shift-and-above-0p85

Reviewer: **ReviewF160Threshold** (same-harness subagent). Manifest `manifest-v1.json` SHA-256 `25c12576efb95998889f4f94374cf37202d8aeaebe1b99315c5c71cd99de220b`, verified. Clock: `/bin/date` printed **2026-10-29T07:53:58-0700** immediately before this file was written.

**What this review is.** It is an independent scientific review run in the same harness as the author. It is **not** a human review, **not** a review by an independent model family, **not** a formal/kernel (Lean) verification, and **not** a novelty or priority assessment. I did not treat author "PASS" lines as evidence. I read and hashed the author scripts but never imported or executed them. This review does not adopt any PH7 threshold.

**Counts: FATAL 0 / MAJOR 0 / MINOR 3.**

## 0. Inputs (read completely, in the declared order)

At 2026-10-29T06:54:37-0700 all ten inputs matched the manifest in SHA-256, bytes and LF. At 2026-10-29T07:50:29-0700 they were re-verified and were unchanged. The manifest lists no mandatory errata, overlays or withdrawals.

| # | file (…/parallel-18/phase-type/) | role | SHA-256 | bytes | LF |
|---|---|---|---|---|---|
| 1 | frontier-20261029-ph7-eight-ninths-impossibility-v1.md | 8/9 candidate (f159; context only) | 599feaa589a6281316786cdd4d19050a88ba2945a12ce253d5f04678e862b2d4 | 10157 | 86 |
| 2 | frontier-20261029-ph7-shift-monotonicity-corollary-v1.md | Lemma S and corollary | dde16615ea1cfcc0dcac77ca5f3329cc947e58287e4c126b13979468b7a390e1 | 3746 | 37 |
| 3 | frontier-20261029-ph7-impossibility-above-0p8765-v1.md | z≥1753/2000 packet | 8084804cabea6159bf5bebe588c593d87abcf43090313a07483ef278a86cc7ff | 6711 | 62 |
| 4 | frontier-20261029-ph7-threshold-z1-certificate-v1.json | z1 certificate | 62b279a132f0f7663dfefa2c0b2fd05591884f2a47928800decc58f39f6ba9af | 523925 | 22880 |
| 5 | frontier-20261029-ph7-threshold-z1-check.py | author generator (read/hash only) | 586e1bc96ad4b2d89b026615790bd6e0144b390f33d3f2fd6d8dc6ae8f7be5a8 | 9336 | 158 |
| 6 | frontier-20261029-ph7-threshold-z1-integer-replay.py | author replay (read/hash only) | 7ae13e57436a8d47bfdc1e846f3bac81a332369b3516231f06a1697f31b849ee | 10036 | 175 |
| 7 | frontier-20261029-ph7-impossibility-above-0p85-v1.md | z≥17/20 packet | a624b358c71e838963c8250bfb82af2e54b06f3bc886332abcc3891a3e24f133 | 7453 | 75 |
| 8 | frontier-20261029-ph7-threshold-z2-certificate-v1.json | z2 certificate | 3824b33dffd55abb03e5174c65fec1d9a353c72c1403c7b3356e9f20603fc6df | 1593287 | 144650 |
| 9 | frontier-20261029-ph7-threshold-z2-check.py | author generator (read/hash only) | ff919031860c7583547dbd09d58271bbf333f2eeee880cfe4822a096f940fbc7 | 17559 | 302 |
| 10 | frontier-20261029-ph7-threshold-z2-integer-replay.py | author replay (read/hash only) | c9c3164fa281b2422ebaab77238723532255b79173487f9923c313bd3ca2e6a5 | 15941 | 277 |

My own code parsed both certificate JSON files in full: `json.loads` of the hash-verified bytes, consuming every leaf of every list. The z2 certificate was never displayed.

## 1. Verdicts

| Claim | Verdict | Conditional on |
|---|---|---|
| **Lemma S** (G_t=G+t(rl^T/(l^Tr)−I): irreducible, Metzler, s=0, char poly y·C(y+t)/(y+t), ratio z→z/(1+t)² after rescaling) | **WRITTEN_SUPPORTED** | nothing; standalone linear algebra, independent of f159 |
| Shift corollary: no PH≤7 for every z≥8/9 | WRITTEN_SUPPORTED, **conditional** | the whole 8/9 theorem (f159: Sections 3–4 and its imported algebraic core) plus the caller; its conclusion also follows from the z≥17/20 theorem, which needs less from f159 |
| z-symbolic identities (characteristic matching, seventh-rate splitting, residual decomposition, case (a), c2=S3·A) | **WRITTEN_SUPPORTED** (exact, z a polynomial variable) | – |
| Lemma C at z1 (four conditions infeasible for seven positive reals) | **WRITTEN_SUPPORTED**, unconditional algebra | z1 certificate (valid) |
| **z1 certificate** `62b279a1…` | **COMPLETE_VALID** | – |
| Theorem: no PH≤7 for z≥1753/2000 | WRITTEN_SUPPORTED, **conditional** | f159 Lemmas 1–4; caller 729926c5; Lemma S |
| **Lemma 5** (y² coefficient of the cover identity plus Cauchy interlacing ⇒ Y2b≥0) | **WRITTEN_SUPPORTED**, **conditional** | f159 Lemma 1 (A=−S symmetric with positive spectrum), Lemma 2 (cover identity; ω≥0; extra cycles have ≥3 states), Lemma 3 (W=E4, E3=T3+C4); Cauchy interlacing (standard) |
| Lemma C2 at z2 (five conditions infeasible) | **WRITTEN_SUPPORTED**, unconditional algebra | z2 certificate (valid) |
| **z2 certificate** `3824b33d…` | **COMPLETE_VALID** | – |
| Theorem: no PH≤7 for z≥17/20 | WRITTEN_SUPPORTED, **conditional** | f159 Lemmas 1–4 (including Lemma 2 down to the y² coefficient, via Lemma 5); caller; Lemma S |
| Bracket "threshold in about [0.8204, 0.85)"; "minimum order exactly 8 at 8/9" | INCONCLUSIVE here (outside this wave) | the lower end rests on owner seven-state constructions (not inputs); "exactly 8" rests on upper8 `e110dd1f…` (not an input); see m3 |

## 2. Lemma S: reconstruction

- P=rl^T/(l^Tr) satisfies P²=P, GP=0 (because Gr=0) and PG=0 (because l^TG=0).
- (G_t)_ij = G_ij + t·r_i l_j/(l^Tr) for i≠j. This is ≥ G_ij, and strictly positive when t>0. So G_t is Metzler, and it is irreducible: trivially for t=0, and because every off-diagonal entry is positive for t>0.
- C^n = span(r) ⊕ l^⊥ is a splitting into G-invariant complements (l^Tr≠0). G_t r=0, and on l^⊥ we have G_t=G−tI. So det(yI−G_t) = y·χ(y+t), where χ(w)=det(wI−G|_{l^⊥})=C(w)/w.
- Spectral bound: Re λ<0 for every non-Perron eigenvalue λ of an irreducible Metzler matrix with s=0, by Perron–Frobenius (strictly smaller real part). Hence Re(λ−t)<0 and s(G_t)=0.
- Rescaling by 1+t: if C=y[(y+1)²+z]²Q, then det(yI−G_t/(1+t)) ∝ y[(y+1)²+z/(1+t)²]²Q((1+t)y+t). The hidden roots (λ−t)/(1+t) still have negative real part, so the new p′,q′ are >0.
- Taking t=√(z/z0)−1≥0 maps ratio z to z0 whenever z≥z0.

All of this is verified exactly in control S+ (§12).

Observations (not defects):
- **Brauer.** The identity holds for G+t(rw^T/(w^Tr)−I) with *any* w satisfying w^Tr≠0. Only Gr=0 is needed (matrix determinant lemma); the left vector adds the commuting/Jordan structure. My first negative control assumed otherwise and was ill-posed (§13).
- **t≥0 is essential.** With t<0 the Metzler pattern breaks at every zero off-diagonal entry (control S-b). So the shift only lowers z.

What is proved is **downward closure of the spectral problem**: if an irreducible 7×7 Metzler G with s(G)=0 and y[(y+1)²+z]² | det(yI−G) exists at z, one exists at every z′∈(0,z]. Via the caller, PH7-impossibility at z0 therefore propagates to every z≥z0 (with z>1/2). Lemma S does **not** show that the set of z admitting a PH7 representation is downward closed, since no initial or exit vectors are constructed. The Lemma S file words this correctly ("SPECTRAL problem"); the manifest's "downward closure of 7-state realizability" must be read in this spectral sense (m3).

## 3. Corollary z≥8/9

Take t=√(9z/8)−1≥0 and rescale; the shifted matrix meets the hypotheses that f159's Sections 3–4 use. Those hypotheses are irreducibility, Metzler sign pattern, s=0, the double factor at 8/9, and p,q>0 for the hidden quadratic (Perron–Frobenius, as above). The argument is correct, but it is **conditional on the entire 8/9 theorem** under f159 (including its imported algebraic core), plus the caller. Its conclusion is also implied by the z≥17/20 theorem, which depends on f159 only through Lemmas 1–4.

## 4. z-symbolic identities (my log lines A1–A6, exact sparse expansion, z a variable)

- **A1.** For y((y+1)²+z)²(y²+py+q):
  - [y^6] = p+4
  - [y^5] = q+4p+6+2z
  - [y^4] = 4q+(6+2z)p+4+4z
  - [y^3] = (6+2z)q+(4+4z)p+(1+z)²
  - [y^2] = (4+4z)q+(1+z)²p
- **A2.** Matching Lemma 3 ([y^6]=e1, [y^5]=e2, [y^4]=e3−W, [y^3]=e4−T3−C4) gives:
  - p = e1−4
  - q = e2−4e1+10−2z
  - W = E4(z) = e3−4e2+(10−2z)e1+12z−20
  - T3+C4 = E3(z) = e4−(6+2z)e2+(20+4z)e1+3z²+6z−45
  - E2 = e5−[(1+z)²p+(4+4z)q]

  At z=8/9 these reduce exactly to the 8/9 constants 74/9, −28/3, −70/9, 212/9, −1007/27.
- **A3.** With e_k=f_k+x·f_{k−1}, where x is the largest of the seven and S4=α1:
  - q = A+x(f1−4)
  - E4 = Ax+B
  - E3 = h0+x·h1
  - E3−E4·S4 = E+xD
  - EA−BD = h0A−h1B
- **A4.** D=K1+β1K2 (β2 cancels). Also Abar−A=(r5−r6)²/4 and Dbar−D=α1α2/6−α3. Each bound used in case (d) has an exact nonnegative form:
  - α1α2/6−α3 = (1/12)Σ_triples[a(b−c)²+b(a−c)²+c(a−b)²]
  - (3/8)α1²−α2 = (1/8)Σ(ri−rj)²
  - β1²/4−β2 = (r5−r6)²/4
  - β1−α1/2 = (1/4)Σ_{i≤4}[(r5−ri)+(r6−ri)] (needs sorting)
  - (5/12)f1²−f2 = (1/12)Σ(ri−rj)²
- **A5.** A−(4−f1)² = f2+4f1−f1²−6−2z ≤ 6/7−2z−(7/12)(f1−24/7)². This is negative for z>3/7, and both z1 and z2 exceed 3/7.
- **A6.** Y2b=E2−E4·m2−S3(E3−E4·L4) has degree exactly 2 in x=v7, and its leading coefficient is c2=S3·A.

## 5. Lemma C at z1: case logic (reconstructed)

I did not open the core manuscript (46659f60); this reconstruction is built from the packet text alone.

- **(a) f1<4.** p>0 gives x>4−f1>0. q>0 gives A>x(4−f1)>(4−f1)², which contradicts A5.
- **(b) f1≥4, A≤0.** q>0 gives x(f1−4)>−A≥0, so f1>4. E4≥0 gives (f1−4)B ≥ (−A)·x(f1−4) ≥ A². So A²−(f1−4)B≤0, which contradicts Qpol(z1)>0.
- **(c) f1≥4, A>0, D≤0.** E3−E4S4≥0 gives E≥−xD. With A>0, EA−BD ≥ −D(Ax+B) = (−D)E4 ≥ 0. This contradicts Hpol(z1)=−L_H(h0A−h1B)>0 (A3).
- **(d) f1≥4, A>0, D>0.** Let α be the elementary sums of the four smallest of the six numbers and β those of the two largest. Then A≤Abar and D≤Dbar (A4). Use the chart y=α1>0, γ=β1−α1/2≥0, τ=α2/((3/8)α1²)∈(0,1].
  - Under this chart Abar, Dbar and f1−4 are exactly the certificate polynomials. At z1 the multiples are 18000·, 18000· and 2·: for example Abar = 18000[(3/8)τy²+(9/16)y²+(5/4)yγ+γ²/4−6y−4γ+10−2z1].
  - The residual cover shows that everywhere on the chart Abar≤0, Dbar≤0 or f1−4<0 holds, a contradiction.
  - x is not needed in this case.

The four cases exhaust all possibilities.

**Leaf-rule soundness (I supply the argument; see m2).**
- Nonnegative Bernstein coefficients give P≥0 on the box.
- Take a point in box∩(0,1)^6 and let F be the face of the box containing it in its relative interior.
  - Its fixed coordinates lie in (0,1).
  - Depth≥6 with split axis = depth mod 6 makes every axis interval a proper dyadic subinterval, so every free coordinate has an endpoint in (0,1).
- So F has a vertex inside the open cube. Its coefficient is >0 by the leaf rule, and every Bernstein basis function of F is positive at the point, so P>0 there.
- The compactification factor Π(1−x_j)² is >0 on (0,1)^6, so Qpol and Hpol are >0 on the open orthant.
- Residual leaves: a maximum coefficient ≤0 (resp. <0) gives ≤0 (resp. <0) on the closed box, and the factors (1−s)^d(1−g)^d are >0 for s,g<1.

## 6. z1 certificate replay: COMPLETE_VALID

`rf160-replay.py` builds Qpol(z1) and Hpol(z1) from the written A, B, h0, h1:
- It checks scale lcms 10^6 and 4·10^9, term counts 168 and 435, individual degree 2, and digests equal to the certificate (`40dfd7ca…`, `5b15a0d0…`).
- **Coverage.** Every leaf list uses only the alphabet {0,1}, is prefix-free, and has Kraft sum exactly 1, so it is a complete partition:

  | cover | leaves | max depth |
  |---|---|---|
  | Q | 9942 | 45 |
  | H | 5952 | 24 |
  | residual | 1736 | 22 |

- **Leaves.** Every leaf was verified by a **direct per-leaf** method: an exact integer Taylor shift to the leaf box followed by monomial→Bernstein conversion. No subdivision tree and no author algorithm is used.
  - Q 9942/9942 and H 5952/5952 pass the rule: depth≥6, all coefficients ≥0, every interior-domain vertex coefficient >0.
  - Residual labels all pass: {f1-4<0: 64, Abar<=0: 844, Dbar<=0: 828}.
- **Machinery positive control.** On random leaves, vertex coefficients and the Bernstein form at random interior rationals equal direct exact evaluation: 531 vertices, and 155 interior points across Q, H and the three residual polynomials.

## 7. Lemma 5: reconstruction

**Where the y² coefficient comes from.** In the cover identity:
- L=∅ gives e5(v).
- A single extra cycle C with |C|=3, 4, 5 leaves det(yI+A_U) of degree 4, 3, 2, with y² coefficient e2(A_U) (the sum of principal 2×2 minors, equal to e2 of the eigenvalues), tr(A_U), and 1. Each comes with factor −ω_C.
- |C|≥6, and any two disjoint extra cycles (≥6 states), reach only y¹ and y⁰.

The target's y² coefficient is (1+z)²p+(4+4z)q (A1). Hence E2 = Σ_{|C|=3}ω·e2(A_U) + Σ_{|C|=4}ω·tr(A_U) + C5.

**The inequality.** Cauchy interlacing for an m-state principal submatrix of the symmetric 7×7 A gives v_k ≤ μ_k ≤ v_{k+7−m}:
- m=4: e2(A_U) ≥ m2 (monotone, since all eigenvalues are positive by Lemma 1), and tr(A_U) ≤ L4.
- m=3: tr(A_U) ≥ S3.

So E2 ≥ W·m2 + S3·C4 + C5 ≥ E4·m2 + S3·max(0, E3−E4·L4). This uses W=E4, E3=T3+C4, T3≤W·L4, C4≥0, C5≥0, S3>0 and ω≥0, and it gives Y2b≥0. The interlacing directions, the max(0,·) step and the sign of ω are all correct.

**Exact control L5+.** Eight seeded 7×7 rational Metzler matrices whose bidirected pairs have square products (up to 68 extra cycles, up to 6 of them virtual). The y⁶…y² coefficients **and** the full cover identity are equal exactly. Dropping C5, or using tr in place of e2, breaks the identity on every non-trivial trial (L5−). Three of the eight trials had no extra cycles and are trivial.

**Floating diagnostics.** The interlacing inequalities and the Lemma 5 inequality hold on these matrices, and the reversed direction tr(A_U)≥L4 fails. This is regression evidence for Lemma 2 (f159 scope), not a proof.

## 8. Lemma C2 at z2: reconstruction

Cases (a), (c) and (d) are as in §5 with z2 constants: z2>3/7, and Hpol(z2) and the z2 residual are certified.

Case (b) (f1≥4, A≤0) splits on where the six rates lie:

- **Not all six in N=[3/5,9/7].** In compactified coordinates the point lies only in "pos" leaves of the outer cover, because an N-leaf box lies inside [3/8,9/16]^6, the image of N^6. So Qpol(z2)>0 there and the case-(b) argument of §5 applies.
- **All six in N.** Map s=(v−3/5)/(24/35) with v1≤…≤v6≤x. The leaf containing s is not "unsorted", because lo_i>hi_j for some i<j excludes every sorted point. The leaf's label then gives a contradiction:

  | label | certified on the box | contradiction |
  |---|---|---|
  | F | f1<4 | case hypothesis f1≥4 |
  | A | A>0 | case hypothesis A≤0 |
  | Q | Qpol>0 | §5 case (b) argument |
  | E4v6 | A<0 and E4(v6)<0 | E4=Ax+B is decreasing, so E4(x)<0 for x≥v6 |
  | Y2v6 | A<0, Y2b(v6)<0, Y2b′(v6)≤0 | c2=S3A<0 (concave), so Y2b(x) ≤ Y2b(v6)+Y2b′(v6)(x−v6) < 0 for x≥v6 |
  | Disc | A<0 and c1²−4c2c0<0 | Y2b<0 everywhere |

  These contradict q>0, E4≥0 or Y2b≥0. The proof is complete.

Diagnostic D1 shows the split is genuinely needed: Qpol(z2) at six equal rates 447/500 is exactly negative.

## 9. z2 certificate replay: COMPLETE_VALID

- Qpol(z2)=100[A²−(f1−4)B] and Hpol(z2)=−4000[h0A−h1B] match the certificate digests `5de4b95f…` and `253b9934…`. The map u=x/(1−x) takes [3/8,9/16] onto N.
- The N-cover polynomials were rebuilt from the written Lemma 5 / Lemma C2 definitions: F=4−f1, A, Q, mA=−A, mE46=−E4(v6), mG6=−Y2b(v6), mD6=−Y2b′(v6), mDl=−(c1²−4c2c0).
  - Y2b comes from e1..e5 of seven variables; x→v6 is done by substitution and cross-checked against the c2, c1, c0 form.
  - All eight scale lcms (1, 10, 100, 10, 10, 400, 400, 160000) and digests match.
- **Coverage.** Every list is prefix-free with Kraft sum 1:

  | cover | leaves | max depth |
  |---|---|---|
  | H | 9179 | 39 |
  | outer | 9782 | 33 |
  | N | 22111 | 37 |
  | residual | 1949 | 22 |

- **Leaves.**
  - H: 9179/9179 pass.
  - Outer: 9470 pos leaves have Qpol>0, and 312 N leaves lie inside [3/8,9/16]^6.
  - N cover: {Q: 7873, Y2v6: 6707, unsorted: 6969, Disc: 521, E4v6: 41}. Positivity is strict everywhere except mD6≥0, and "unsorted" is checked exactly.
  - Residual: {f1-4<0: 65, Abar<=0: 950, Dbar<=0: 934}.
- Machinery controls on H, outer Q and N (Q, mG6, mDl, mE46) pass.

## 10. Dependencies (exact)

1. **Caller** `frontier-20261028-ph7-global-irreducibility-v1.md`, SHA-256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`. Not an input and not reviewed here; the parent reports f61. What the packets use: for z>1/2, a PH representation with ≤7 states has exactly 7 states and an irreducible T, and G=(T+cI)/d is irreducible Metzler with s=0 and y[(y+1)²+z]² | det(yI−G). All three theorems use this; the general-z range is taken from the packets' statement of the import.
2. **f159**, the 8/9 candidate `599feaa5…`.
   - Lemma 1: A=−S symmetric with positive eigenvalues. Its final step needs only that −1±i√z is non-real, which holds for all z>0.
   - Lemma 2: the cover identity; extra cycles have ≥3 states; ω≥0.
   - Lemma 3: coefficients y⁶–y³.
   - Lemma 4: Ky Fan.
   - The z≥8/9 corollary alone also uses f159's Section 4 and its imported core (46659f60…, girth-four b2674b82…, 1653-leaf certificate 45256245…). None of these was opened.
3. **Lemma S** `dde16615…`: reviewed here, sound.
4. **Standard facts:** Perron–Frobenius for irreducible Metzler matrices, Cauchy interlacing, Ky Fan, and positivity of the Bernstein basis.
5. **Bracket wording only:** owner constructions up to ≈0.82042 and upper8 `e110dd1f…`. Neither is an input.

No solver UNKNOWN or budget outcome enters any argument.

**Which claims depend on f159:**
- **No:** Lemma S, Lemma C(z1), Lemma C2(z2), both certificates, and all z-symbolic identities.
- **Yes:** Lemma 5 (Lemmas 1–3); the z≥1753/2000 and z≥17/20 theorems (Lemmas 1–4 only, not the 8/9 algebraic core); the shift corollary z≥8/9 (the whole 8/9 theorem).

## 11. Findings

- **m1 (MINOR, documentation).** The written packets do not state the certificate conventions.
  - The residual chart is not given: y=α1, γ=β1−α1/2, τ=α2/((3/8)α1²), split axes in the order (y, τ, γ), bit 0 = lower half. The packets defer to "as in the 8/9 core", which is not an input.
  - The N-cover axis j ↔ v_{j+1}, the bit convention and the digest serialization appear only in generator code or rule strings.

  I reconstructed all of these from the stated bounds. The reconstruction reproduces the certificate expressions exactly, and every leaf passes under it. There is no mathematical gap.
- **m2 (MINOR, compressed proof).** The z1/z2 packets state cases (b), (c) and the leaf-rule soundness ("giving strict positivity") without derivation and defer them to the core. The short derivations in §5 hold; they should be written into the packets.
- **m3 (MINOR, wording/scope).**
  - Lemma S yields downward closure of the *spectral* problem, and with the caller, upward closure of PH7-impossibility. It does not show that the PH7-realizable set is an initial segment.
  - "The seven-state threshold lies in about [0.8204, 0.85)" should therefore read: the supremum of PH7-realizable ratios lies in [≈0.82042, 0.85). The lower end rests on unreviewed owner constructions.
  - The manifest phrase "downward closure of 7-state realizability" must be read spectrally.

Notes that are not findings:
- The Lemma S file's own clock disclosure is a process matter for the parent.
- The packets' diagnostics agree with my unsaved kernel diagnostics:
  - z_Q≈0.8760934; my bisection gives 0.87609335….
  - Q(7/8)≈−0.0034 at 0.894; my unscaled value is −0.00343.
  - I also found that the equal-rate discriminant has degree 6 in z and is divisible exactly once by 128z³−149z²+38z−5.

  None of these is a premise.

## 12. Controls and receipts

All files are in this directory. Receipts are in `rf160-receipts-v1.json` (SHA-256 `17186cec9e4eab392710f0fb839c2f219ba5d4bbabf9aa8c2e63371a65d58095`).

| file | SHA-256 |
|---|---|
| rf160-replay.py (independent replay; modes all/neg) | d2643d0eb9ce10cb3427030d6387274bb9f2de480cc1d9aa4a6a344ca58eefa8 |
| rf160-replay-all-log.txt | 62f37612c8c3aae9159f1121dfecbd2042417d1b09e5db9326de657cb2879099 |
| rf160-replay-neg-log.txt | 1eeab658cde989f3b969ef9e5a127b8b87527aafb92ac828d146a5014f04c825 |
| rf160-lemma-controls.py (v1; exited 1, ill-posed negative) | 61fd0bbff2602bd919af3ca51accee578019fe617d6e5c63b630c8252461d71e |
| rf160-lemma-controls-log.txt (v1) | 3ae50a6d55c5a552b525c220cb578a28b3e1ade068b76dd732d5c99fa74d9744 |
| rf160-lemma-controls-v2.py | c053dbd9392ad70c137f65b223bd8771ae7d595a0e09851b51d505e9e98ff0ba |
| rf160-lemma-controls-v2-log.txt | 2af389c12ba2edf24ca8497df5687dd396520f0f22ec6d108539cdbaae29ec05 |

Runs, with `/bin/date` printed before and after each:

| run | before | after | exit |
|---|---|---|---|
| replay `all` | 07:27:57 | 07:28:51 | 0 ("ALL POSITIVE REPLAYS PASS (54.1s)") |
| replay `neg` | 07:30:56 | 07:31:22 | 0 |
| lemma controls v1 | 07:30:57 | 07:30:57 | 1 |
| lemma controls v2 | 07:46:11 | 07:46:12 | 0 |

All times are 2026-10-29, −0700.

**Positive cases (all pass, exact):**
- A1–A6.
- Both certificates in full, together with the machinery controls.
- **S+**, six trials. Each checks:
  - exact positive l, P²=P and GP=PG=0;
  - off-diag(G_t)>0, G_t r=0 and l^T G_t=0;
  - (y+t)C_t(y)=y·C(y+t).
- S+ also covers the Brauer variants and the ratio map.
- L5+.

**Negative cases (each fails for the intended reason):**
- **N1.** Qpol(7/8) is exactly <0 at six equal rates 447/500. The z1 Q leaves fail at 2311 of 9942 leaves, including the leaf containing that point (negative coefficient).
- **N2.** Dropping a leaf breaks the Kraft sum; adding a child or truncating a leaf breaks prefix-freeness.
- **N3.** Relabelling Dbar-leaf 001001001 as Abar fails.
- **N4.** The z2 N leaves checked against the polynomials at z=21/25 fail at 9874 of 22111 leaves (Q 7779, Y2v6 2014, Disc 81).
- **N5.** The wrong-sign H fails at leaf 000000.
- **S-a.** A rank-one term on the ones vector breaks the identity (6/6 trials).
- **S-b.** t=−1/10 breaks the Metzler pattern (6/6 trials).
- **L5−.** See §7.

## 13. Deviations and disclosures

1. **Author scripts.** I read them in full (read/hash only) to learn the digest serialization and the leaf conventions, and never imported or executed them. My polynomials are built from the packet text.
2. **Files not opened.** I did not open the caller, the no-two-cycle core, upper8, the girth-four certificate or any other non-input file. No web access, external model, Git, deletion or publication. Nothing was written outside this directory; I set PYTHONDONTWRITEBYTECODE=1 and no `__pycache__` was created.
3. **Tools.** numpy serves only as an object-dtype container for exact ints and Fractions. Floats appear only in labelled diagnostics. The eval kernel was used only for JSON structure inspection and the unsaved diagnostics listed in the receipts.
4. **v1 Lemma controls.** v1's negative control S− assumed the identity needs the left vector; by Brauer's theorem it does not. The run exited 1. The v1 script and log are retained unchanged, and v2 is a new file with valid negatives.
5. **Main's messages.** During the review Main sent two status-only safety-control messages (f162 and f161 holds). I accessed none of the affected materials, and none is used here.
6. **Edits after the first write.** The header clock (07:53:58) was observed before the first write of this file. Two presentational edits followed: the abbreviated hashes in the §0 table (one tail was mistyped) and the caller hash in §10 were replaced by the full values. `/bin/date` then printed 2026-10-29T07:58:49-0700, after those two edits and before this item was added. That time is therefore an upper bound for the two hash edits and a lower bound for this item and for the final content. No verdict, count or evidence changed.

## 14. Summary

Lemma S is correct, elementary and independent of f159. It proves downward closure of the spectral problem, and hence that PH7-impossibility at a ratio propagates to all larger ratios (with z>1/2). It does not prove downward closure of PH7 realizability itself.

Every z-symbolic identity was reconstructed exactly with z as a variable. The Lemma C case analysis at z1 and the Lemma 5 / Lemma C2 argument at z2 were reconstructed and are complete, with the interlacing directions and the max(0,·) step verified.

Both exact certificates were replayed leaf by leaf with independently written exact rational/integer code using a direct per-leaf Bernstein method. That code rebuilt every polynomial from the written definitions, and both certificates are COMPLETE_VALID: z1 has 9942+5952 six-cube and 1736 residual leaves; z2 has 9179 H, 9782 outer, 22111 N and 1949 residual leaves. Each comes with full coverage proofs, positive machinery controls, and negative controls that fail for the intended reasons.

The theorems "no PH≤7 for z≥1753/2000" and "no PH≤7 for z≥17/20" are therefore WRITTEN_SUPPORTED, conditional on:
- f159's Lemmas 1–4 (Lemma 5 also uses Lemma 2 at the y² level);
- the unreviewed irreducibility caller 729926c5.

They do not depend on the 8/9 algebraic core. The shift corollary for z≥8/9 depends on the whole f159 theorem, and the z2 result supersedes it.

There are no FATAL or MAJOR findings. The three MINOR findings concern certificate conventions missing from the written packets, compressed case/leaf-rule derivations, and "threshold" wording.

This same-harness review is not human, independent-model-family, formal/kernel or novelty verification.
