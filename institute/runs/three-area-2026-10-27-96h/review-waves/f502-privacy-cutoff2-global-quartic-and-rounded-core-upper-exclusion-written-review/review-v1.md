# F502 WRITTEN review: global quartic and rounded-core upper exclusion

## Verdict

**SUPPORTED at the exact assigned conditional scope.**

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.** The candidate proves the necessary upper bound \(m\le\beta\), including the full rounded-core exclusion and the conditional upper-endpoint classification, under the named actual-attainment and canonical-reduction imports. It does not prove that any parameter actually belongs to the cutoff-two regime.

**Overall correctness:** correct at the F502 scope.  
**Confidence:** 0.98.

The lower exclusion \(m>\alpha\) is outside this gate’s substantive audit and receives no additional acceptance from this return. The historical penalty-sign **1 MAJOR** remains unchanged.

## 1. Read coverage, provenance, and methods

Before opening the mathematical packet, I completely read:

- `manifest-v1.json`, lines 1–120;
- `freeze-receipt-v1.json`, lines 1–60;
- `parent-live-metadata-supply-v1.json`, lines 1–105;
- all ten manifest-listed status-only controls, including their endings.

I then sent Main a direct administrative pre-body ACK. Only afterward did I read `literal-packet-v1.md` completely, in the ordered raw windows \(1\!-\!20,21\!-\!40,\ldots,541\!-\!560,561\!-\!573\). Every window contained at most 20 lines. No mathematical derivation for this assignment preceded completion of that packet read.

The packet supplied:

- **S1:** the complete F486 candidate, logical lines 1–471, including its ending; SHA `fc4423b5a7cb6fb9a1ba19ae35cf70145b9fab9034daf9da78af4e26aa3c1b11`.
- **S2:** the scalar-edge/uniqueness/full-value disposition, lines 1–61; SHA `4179e3691a8050e64432044bfb928c273086537a3755fbd5b5d4f9c790af3330`.
- **S3:** the binding-core/corrected-penalty disposition, lines 1–39; SHA `4880cff7e5d64e615aad22c013a591f6fd8b835f7d7991fa8e3ac34cb2a54b06`.

The manifest pin `1c7e4458605e333ae75a1e1e7ea8ad78cb77a5671ad5108b4b0b24dc9ba64cae`, receipt pin `955768014130a1b39179e3af51ce67c08c13f7e91c73a083ec75f67ccbfeecfa`, packet pin `c92029922f6d85d79b7376be5b6346bd47bd45ff1858afe5bb91cc9f9becde9c`, and matching byte/LF observations are **parent-supplied metadata**, not my own hash execution. The clock `2026-10-30T12:27:04-0700 PDT` is likewise a parent observation, not my native start or completion time.

**Scientific execution: NOTRUN.** This review used written algebra in formal variables and only the numerical endpoints/instances already supplied by the candidate. No new chosen private instance, code, CAS, interpreter, solver, enumeration, numerical integration, build, test, lint, or formatter was used. No linked scientific body, sibling review, new mathematical source, author code, or held payload was opened.

All quarantined episodes and their proof, verification, selection, confidence, planning, and reporting consumers remain **HELD/ZERO/NONINPUT**. Status-control reading is not mathematical rehabilitation or a clean-cognition certificate.

The available write tool does not support repository-file materialization, and no bypass was attempted. This is the complete review body for Main’s materialization.

## 2. Exact imports retained

The conclusion is conditional on the following supplied imports, not an independent reconstruction of the original unreduced problem:

1. The corrected canonical fixed-scalar reduction, its full signed functional \(H_\lambda=N-\lambda Z\), and \(Z>0\).
2. An **actually attained** cutoff-two optimum with \(1/2<V\le2\), together with actual-optimizer positivity and pruning.
3. The adopted actual-optimizer conclusions
   \[
   a>0,\qquad c=a+\frac12,\qquad
   D(a)=2a^2+2ma+T_2<V,\qquad m<\frac12,
   \]
   from S2 lines 7–16.
4. The binding-core mechanism and complete geometric-tail/cubic calibration in S3 lines 7–19, and the complete edge value in S2 lines 49–53.

In particular, the fixed-\(\lambda=2\) argument below is justified by checking its own strict tail margin and clipping feasibility. It is not justified merely by pretending \(2=V\).

The erroneous unsigned penalty-difference assertion is not used. S3 lines 23–31 retain the corrected sign and the distinction between that penalty difference and the full endpoint comparison.

## 3. Claim-by-claim disposition

| Claim | Status in this gate | Principal source |
|---|---|---|
| Quartic identity, critical-point classification, and strict parameter monotonicity | **SUPPORTED** | S1 lines 83–104, 184–225 |
| Unique \(\beta\in(13/40,33/100)\) and global positivity for every \(m>\beta,\ t\ge0\) | **SUPPORTED** | S1 lines 227–294 |
| Global admissible fixed-scalar projection at \(\lambda=2\), including the rounded branch | **SUPPORTED**, conditional on the named canonical reduction | S1 lines 302–370 |
| Strict increase of the rounded branch and positivity at its joining point | **SUPPORTED** | S1 lines 379–414 |
| Exclusion of every actually attained optimizer with \(m>\beta\) | **SUPPORTED** | S1 lines 418–435 |
| If actual attainment occurs at \(m=\beta\), then \(V=2\), \(a=s(\beta)/2\), and the core is strictly all-upper | **SUPPORTED as a necessary implication only** | S1 lines 438–448 |
| Lower exclusion \(m>\alpha\) | **INCONCLUSIVE in this gate: outside the assigned substantive audit**, not refuted | S1 lines 133–179 |
| Existence or sufficiency anywhere in the necessary band | **INCONCLUSIVE / not established**, consistently with the candidate’s stated limitations | S1 lines 461–469 |

## 4. Written reconstruction of the quartic certificate

### 4.1 The quartic retains the full all-upper objective

From the supplied moments,
\[
M_2(t)=t^2+2mt+T_2,\qquad
M_4(t)=t^4+4mt^3+6T_2t^2+4T_3t+T_4.
\]
Consequently,
\[
P_m(t)=M_4(t)-6M_2(t),
\]
which gives exactly S1 lines 86–89. Thus the complete all-upper value at \(\lambda=2\) is
\[
\frac23M_4(2a)-4M_2(2a)=\frac23P_m(2a).
\]
There is no discarded tail constant or additional external factor \(1-b\).

### 4.2 Critical-point count and the competing boundary value

For \(m\in[3/10,1/3]\),
\[
P_m''(t)=12\bigl(t^2+2mt+T_2-1\bigr).
\]
Here \(T_2<1\), while the expression is strictly increasing in \(t\ge0\). Therefore \(P_m'\) decreases up to one positive turning point and then increases.

The displayed signs in S1 lines 195–198 are correct:
\[
P_m'(0)\ge\frac{51}{125}>0,\qquad
P_m'(1/2)\le-\frac5{18}<0,\qquad
P_m'(1)\ge\frac{221}{125}>0.
\]
They imply exactly two positive critical points: a local maximum in \((0,1/2)\), followed by the unique local minimum \(s(m)\in(1/2,1)\). Since the leading coefficient is positive, the global minimum on \(t\ge0\) is indeed one of
\[
P_m(0),\qquad P_m(s(m)).
\]
The proof does not silently replace a global minimum by the favorable critical point.

### 4.3 Parameter monotonicity extends beyond the defining bracket

Differentiation gives
\[
\partial_mP_m(t)
=4t^3+(6+24m)t^2+(-8+48m+72m^2)t
 +96m^3+108m^2+4m-5.
\]
At \(m=3/10\), this is exactly
\[
4t^3+\frac{66}{5}t^2+\frac{322}{25}t+\frac{1064}{125}.
\]
Also,
\[
\partial_m^2P_m(t)
=24t^2+(48+144m)t+4+216m+288m^2>0
\]
for \(t\ge0,\ m\ge3/10\).

In particular, \(\partial_mP_m(t)\) has a strictly positive uniform lower bound on that entire domain. Thus
\[
f(m)=\min_{1/2\le t\le1}P_m(t)
\]
is continuous and strictly increasing on the defining compact parameter interval. More importantly, the pointwise strict increase remains valid for **every** \(m\ge3/10\), not only up to \(1/3\). This supplies the later all-parameter upper exclusion.

### 4.4 Expansion and Bernstein certificate

Writing \(u=m-1/3\) gives
\[
P_m(t)=\frac{W(t)}{27}+uJ(t)+u^2B(t)+u^3C(t)+24u^4
\]
with exactly the four polynomials displayed in S1 lines 236–239. In particular, the linear coefficient is
\[
J(t)=4t^3+14t^2+16t+\frac{107}{9};
\]
the constant \(107/9\) is correct.

For the two affine interval maps, direct formal expansion gives
\[
W(x/2)
=5+12x-18x^2+\frac92x^3+\frac{27}{16}x^4,
\]
and
\[
W((1+x)/2)
=\frac{83}{16}-\frac{15}{4}x+\frac{45}{8}x^2
 +\frac{45}{4}x^3+\frac{27}{16}x^4.
\]
Conversion to the degree-four Bernstein basis yields precisely the two listed coefficient rows. Their minimum is \(17/4\), so the bound
\[
W(t)\ge\frac{17}{4}\qquad(0\le t\le1)
\]
is valid.

At the candidate-supplied lower bracket, substitution into the same expansion gives
\[
P_{13/40}(2/3)=-\frac{1508857}{25920000}<0.
\]
Since \(2/3\in[1/2,1]\), this proves \(f(13/40)<0\).

At the supplied upper bracket, \(u=-1/300\). The bounds on \(J,B,C\) therefore have the stated directions, including the negative cubic term:
\[
P_{33/100}(t)
\ge\frac{17}{108}-\frac{413}{2700}
 -\frac{92}{27000000}
=\frac{29977}{6750000}>0.
\]
Hence \(f(33/100)>0\), and continuity and strict monotonicity prove the unique \(\beta\) in the claimed open bracket.

Finally,
\[
P_{13/40}(0)=\frac{28743}{320000}>0.
\]
Parameter monotonicity gives \(P_\beta(0)>0\). Together with the full critical-point count and \(f(\beta)=0\), this proves that \(P_\beta\) is nonnegative on the entire half-line and has exactly one zero, \(s(\beta)\). Strict parameter monotonicity then proves
\[
P_m(t)>0\qquad(t\ge0,\ m>\beta),
\]
including parameters above \(1/3\).

## 5. Written reconstruction of the complete fixed-scalar projection

Assume the actual-optimizer hypotheses and \(m\ge\beta\). Then
\[
\frac3{10}<m<\frac12,\qquad T_2<1,\qquad Q^*>2.
\]
Both \(R(a)=4a^2+4ma+T_2\) and \(D(a)\) increase strictly for \(a\ge0\). Their level-two roots satisfy
\[
a_R<a_D,
\]
because \(R(a)-D(a)=2a^2+2ma>0\) for \(a>0\). The candidate’s endpoint comparisons correctly give
\[
\frac14<a_R<\frac12.
\]
Every possible actual scalar satisfies \(a<a_D\).

### 5.1 Binding and clipping at \(\lambda=2\)

The strict tail margin is \(Q^*-2>0\). The supplied tail derivative argument therefore still removes slack at this fixed scalar. On the edge, the remaining corner is fixed and there is no far-tail interval beyond \(u=c=a+1/2\).

For \(0\le y\le a<a_D\),
\[
d(a,y)
=D(a)-2-(a^2-y^2)<0.
\]
Thus there is no positive-length lower-face branch. Moreover,
\[
2-v-y^2
=(a+m)^2+(2-D(a))+(a^2-y^2)>(a+m)^2,
\]
so the displayed square root is real throughout the shared core and its free root is strictly above the lower face.

Put \(w=a-y\). On the upper face,
\[
d(2a-y,y)=D(a)-2+2mw+2w^2.
\]
This expression increases strictly in \(w\ge0\). Its unique zero is the stated \(q>0\). Therefore:

- \(q\ge a\) gives the all-upper branch;
- \(0<q<a\) gives the free portion \(0\le y<a-q\), followed by the upper face.

At the rounded joining point,
\[
\sqrt{2-v-y^2}=a+q+m> a-q=y.
\]
The free segment consequently has slope in \([-1,0]\); it joins the upper segment continuously, and the binding tail joins the fixed edge corner. Together with the strictly convex pooled primitive, these facts establish an admissible **global fixed-scalar projection**, not merely independent-height stationarity.

The complete value from S2 lines 49–53 therefore applies:
\[
e_2(a)=\frac23M_4(2a)-4M_2(2a)
-8\int_0^{a-\tau}(U-r)^2
 \left(\frac{U+2r}{3}+m\right)\,dy.
\]
The cubic improvement is the exact primitive difference at its root. The geometric tails, normalization, and deterministic constant remain included.

## 6. Rounded-branch derivative and strict positivity

The rounded derivative can be reconstructed directly from that complete value. The moving-endpoint term vanishes because \(U=r\) at \(y=a-q\). Differentiating the integral therefore gives
\[
\frac{e_2'(a)}{16}
=G(a)-\int_0^{a-q}d(U,y)\,dy,
\]
where
\[
G(a)=\frac83a^3+4ma^2+(2T_2-2)a+m(\kappa-1).
\]

The full upper-face derivative integral is
\[
\int_0^a d(U,y)\,dy
=\frac83a^3+3ma^2+(T_2-2)a.
\]
Using \(2-D(a)=2mq+2q^2\), its negative portion has magnitude
\[
-\int_{a-q}^a d(U,y)\,dy=mq^2+\frac43q^3.
\]
Substitution gives exactly
\[
F_R(a)=\frac{e_2'(a)}{16}
=m\!\left[a^2+(1+2m)a+\kappa-1\right]
-mq^2-\frac43q^3.
\]

Implicit differentiation of the defining equation for \(q\) gives
\[
q_a=-\frac{2a+m}{m+2q}.
\]
Hence
\[
F_R'(a)=m(2a+1+2m)+2q(2a+m)>0.
\]

At \(a=a_R\), \(q=a_R\). Substitution of \(R(a_R)=2\) gives the candidate’s joining expression
\[
F_R(a_R)
=m\!\left(\frac13+\frac32m+m^2\right)
+ma_R-2ma_R^2-\frac43a_R^3.
\]
Since \(0<a_R<1/2\),
\[
ma_R-2ma_R^2\ge0,\qquad
-\frac43a_R^3\ge-\frac16.
\]
Using \(m>3/10\) then yields the valid positive lower bound
\[
F_R(a_R)\ge\frac{131}{500}-\frac16
=\frac{143}{1500}>0.
\]

Thus \(e_2'(a)>0\) throughout \(a_R<a<a_D\). The rounded branch cannot lower the value below its all-upper joining value. This conclusion follows from the complete objective and a strict derivative bound, not from stationarity implying global minimality.

The join \(q=a\) is covered by continuity and the vanishing integral. The boundary \(a_D\) is not a missing actual case: the imported inequality \(D(a)<V\le2\) excludes it strictly.

## 7. Actual-attainment contradiction and equality case

For the actual optimizing profile \(\sigma\),
\[
H_V(\sigma)=0,\qquad Z(\sigma)>0,
\]
so
\[
H_2(\sigma)=-(2-V)Z(\sigma)\le0.
\]
Because \(e_2(a)\) is the fixed-\(a\) minimum at \(\lambda=2\),
\[
e_2(a)\le H_2(\sigma)\le0.
\]
This comparison does not require the actual profile to minimize at \(\lambda=2\) in advance.

If \(m>\beta\), the global quartic certificate makes every all-upper value strictly positive. The rounded branch starts at a strictly positive joining value and increases strictly. These two branches cover every possible actual \(a<a_D\), contradicting \(e_2(a)\le0\). Therefore
\[
m\le\beta,\qquad
b\le\frac{\beta}{1+\beta}<\frac{33}{133}.
\]

At \(m=\beta\), matching the branch derivatives gives
\[
P_\beta'(2a_R)=12F_R(a_R)>0.
\]
Since \(2a_R>1/2\), the critical-point classification forces
\[
s(\beta)<2a_R.
\]
The quartic’s unique zero therefore lies strictly inside the all-upper branch. The rounded joining value is strictly positive, so \(e_2(a)\le0\) forces
\[
a=\frac{s(\beta)}2.
\]
The chain
\[
0=e_2(a)\le H_2(\sigma)\le0
\]
then forces \(H_2(\sigma)=0\), and \(Z(\sigma)>0\) gives \(V=2\). Finally \(a<a_R\) implies \(R(a)<2\), establishing the strict all-upper core classification.

## 8. Acceptance boundary

This gate supports the **necessary upper exclusion and conditional endpoint identification only**, under the exact named imports. It does not support:

- actual attainment at \(\beta\) or at any interior parameter;
- sufficiency or nonemptiness of the actual cutoff-two regime;
- the lower bound through an independent F502 audit;
- a global explicit value formula throughout the remaining band;
- unconditional attainment or pruning, unreduced-law uniqueness, or original-source/book equivalence;
- novelty, priority, human review, independent-family acceptance, or formal-kernel verification.

No correction is required for the assigned upper-bound proof. Parent disposition and the other disjoint gates remain separate obligations.