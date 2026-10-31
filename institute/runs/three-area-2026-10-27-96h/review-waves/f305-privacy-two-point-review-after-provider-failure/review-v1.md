# f305 written review — complete return

**Delivery observation:** `/bin/date -u` returned `2026-10-30T13:49:33Z`.

**Materialization:** The permitted own-wave process-record write was refused by the mounted write tool. No alternate filesystem or scratch-file write route was attempted. This is the full review text for parent materialization as this wave’s `review-v1.md`.

## 1. Binding, coverage, and assumptions

The manifest, freeze receipt, and all four status-only controls were read before the administrative **PRE-BODY ACK**, delivered at the observed time `2026-10-30T13:43:03Z`. No mathematical packet had been read or derivation performed before that ACK.

Live metadata hashing matched:

- Manifest: `daef2f7e51613735935f9c3b00430386e7baaa885439f0e434bee11406562b50`
- Freeze receipt: `3e739f04a171294628d645ed0c419d136349ddc28b1c6d3359876e299a0729c6`
- Literal packet: `507486774f3133870bdd3c79908b0d7439f001cf97cabdb64bff94ec380f8470`

After the ACK, **all 308 LF of the literal packet were read in order, raw, in windows of at most 20 LF, including its ending, before derivation**. No elision remained. This covers all sixteen declared inputs: S1–S14 at their complete declared bodies, S15 at LF16–23, and S16 at LF13–38. Individual source-file hashes were read from the frozen receipt, not independently recomputed.

The following are conditional imports, not newly certified original-problem results:

- The actual-cutoff-two standing hypothesis, including \(1/2<V\le2\), and \(\lambda=V\).
- The functional, boxes, and CPL constraints in S16|13–38.
- The corrected fixed-scalar profile rule, with S13|8 overriding S15|23’s false biconditional and nonuniqueness wording.
- The attained variational reduction at exactly S13|9’s imported scope.
- The necessary geometric conditions at S14|7–24’s stated scope, without any rejected Clarke equality or sufficiency assertion.

All slack conditions below are **weak and pointwise on the declared closed core interval**. In particular, \(y=0\) remains part of the definition when \(a=0\).

## 2. Exact two-point stratum: SUPPORTED

Write
\[
u=a+\tfrac12,\qquad
p_0(y)=\operatorname{clip}(R_0(y),[a,2a-y]),
\]
and
\[
p_d(y)=\operatorname{clip}(R_1(y),[d,2d-y]),\qquad d\ge u.
\]

The clipping conventions are precisely those in S16|37–38. Since \(m,v>0\),
\[
R_0(y)>R_1(y)
\]
also in the clipped-root cases.

### Necessity from edge core slack alone

At \(y=0\), edge core slack gives
\[
\min(2u,\max(u,R_1(0)))\ge p_0(0)+1.
\]
But
\[
p_0(0)+1\ge a+1>u,
\]
so
\[
R_1(0)\ge p_0(0)+1.
\]
Consequently \(R_0(0)>p_0(0)\). Projection onto \([a,2a]\) can have this property only at its upper endpoint:
\[
p_0(0)=2a.
\]
This also covers the collapsed box at \(a=0\). Therefore
\[
R_1(0)\ge2a+1.
\]
The right side is positive, so the clipped branch cannot satisfy this inequality. Thus it is equivalent to
\[
\boxed{\lambda\ge v+(2a+1+m)^2.}\tag{E}
\]

No corner-interval assumption was needed for this necessity.

### Sufficiency, including clipping and weak equality

For \(0\le y\le u\), put
\[
q(y)=y^2+(2u-y+m)^2.
\]
This is convex, and
\[
q(0)-q(u)=2u(u+m)>0.
\]
Hence its maximum on \([0,u]\) is \(q(0)=(2u+m)^2\). Under (E),
\[
\lambda-v-y^2\ge(2u-y+m)^2>0,
\]
so the root is real throughout this interval and
\[
R_1(y)\ge2u-y.
\]
Moreover, the inequality is strict for \(y>0\), even when (E) is tight.

Since \(R_0>R_1\), the core projection is
\[
p_0(y)=2a-y,\qquad 0\le y\le a.
\]
At the edge,
\[
p_u(y)=2u-y,\qquad 0\le y\le u.
\]
This satisfies the core coupling with equality and satisfies the corner floor, including the joins \(y=a\) and \(y=u\).

For fixed \(y\le u\), both faces in
\[
p_c(y)=\min(2c-y,\max(c,R_1(y)))
\]
are nondecreasing in \(c\). Therefore \(p_c(y)\ge p_u(y)\) for every \(c\ge u\). Above \(u\), no CPL corner floor remains.

It follows that, for every \(c\ge a+1/2\),
\[
\boxed{
S_{\rm both}
=
\{(a,c):a\ge0,\ c\ge a+\tfrac12,\
\lambda\ge v+(2a+1+m)^2\}.
}
\]

This proves the central claim in **S2|7 and S8|5–11**, with the nonemptiness correction in S7 applied.

### Boundary and nonemptiness consequences

For fixed \(m,\lambda\), this formal conditional stratum is empty unless
\[
\lambda\ge v+(1+m)^2.
\]
When this holds, its projection onto the \(a\)-axis is exactly
\[
0\le a\le
\frac{\sqrt{\lambda-v}-1-m}{2},
\]
with every \(c\ge a+1/2\) allowed.

Thus:

- Nonemptiness uses **\(\ge\)**.
- Positive \(a\) occurs iff the inequality is strict.
- At tight (E), the \(y=0\) coupling equality is allowed.
- The empty-substratum result remains valid:
  \[
  S_{\rm both}\cap\{u\ge\sqrt\lambda-m\}=\varnothing.
  \]

These are conditional stratum statements, not a proof that the original problem realizes the actual-cutoff-two regime.

## 3. Pair-only slack and corner compatibility: SUPPORTED, with a naming qualification

The pair-only condition is
\[
S_{\rm pair}:\quad p_c(y)\ge p_0(y)+1
\quad(0\le y\le a).
\]

### A pair in \(S_{\rm pair}\) satisfies its own corner floor

If \(c\ge a+1\), then for \(a\le y\le u\),
\[
2a+1-y\le a+1\le c\le p_c(y).
\]

If \(c<a+1\), the \(y=0\) pair slack test gives
\[
p_c(0)\ge p_0(0)+1\ge a+1>c.
\]
Therefore \(R_1(0)\ge p_0(0)+1\). The same root-dominance projection argument pins \(p_0(0)=2a\), yielding (E). Section 2 then supplies corner compatibility.

Hence **S3|5’s pair-level result is supported**: a pair satisfying its core slack test also has its own independent tail projection compatible with its corner floor.

However, pair-only slack does not imply edge core slack. In particular, for the entire algebraic region \(c\ge2a+1\), the pair core test is automatic from \(p_0\le2a-y\) and \(p_c\ge c\), whereas (E) still bounds \(a\).

Thus:
\[
S_{\rm both}\subseteq S_{\rm pair},
\]
and an \(S_{\rm pair}\) point outside \(S_{\rm both}\) must have \(c\ge a+1\).

### “\(S_{\rm full}\)” must not replace quantified definitions

The older corner-only strengthening should not be silently identified with edge core slack.

For the edge corner interval alone, compatibility is equivalent to
\[
R_1(y)\ge2u-y\quad(a<y<u).
\]
Continuity extends this to the endpoints. Since
\[
q'(y)=4y-4u-2m<0\quad(0\le y\le u),
\]
this corner-only condition is exactly
\[
\boxed{\lambda\ge v+a^2+(a+1+m)^2.}\tag{H}
\]
For \(a>0\), its threshold is strictly below the threshold in (E), by
\[
(2a+1+m)^2-\bigl[a^2+(a+1+m)^2\bigr]
=2a(a+1+m)>0.
\]

Consequently:

- If “\(S_{\rm full}\)” is explicitly redefined to mean full **two-point core slack**, its identification with \(S_{\rm both}\) is supported.
- If it retains S5|5’s meaning “\(S_{\rm pair}\) plus both corner checks,” its precise characterization is \(S_{\rm pair}\cap\{(H)\}\), not automatically \(S_{\rm both}\).

The bare alias is therefore not an additional accepted theorem. The explicit \(S_{\rm both}\) characterization above is unambiguous.

## 4. Original displayed \(\Delta\): exact on the original two-point \(S\)

Let \(D_0\) denote S11|9–14’s displayed expression:
\[
\begin{aligned}
D_0(a,c)=b\Bigl\{&
\tfrac{16}{3}T_3(c-u)+4T_2(c^2-u^2)-8\lambda m(c-u)\\
&+8\int_u^c\psi_1(p_c(y),y)\,dy\\
&+8\int_0^u
[\psi_1(p_c(y),y)-\psi_1(p_u(y),y)]\,dy
\Bigr\}.
\end{aligned}
\]

On \(S_{\rm both}\):

1. Both core profiles equal \(p_0\), so their \(C_0\) blocks cancel.
2. Both endpoints’ tail profiles equal their independent projections, including the corner interval.
3. The constant terms \((2/3)T_4-2\lambda T_2\) cancel.
4. The constant difference, added interval, unchanged interval, and outer factor \(b\) are exactly those displayed.

Therefore
\[
\boxed{\Delta(a,c)=D_0(a,c)\quad\text{on the original }S=S_{\rm both}.}
\]

### Finding M1 — Withdraw f291 M1 at the original two-point scope

**Severity:** MAJOR.  
**Source:** `review-waves/f291-privacy-pure-slack-delta-and-empty-substratum/review-v1.md`, **LF17–24**; further reasoning at LF27 and LF52. These are S12 in this packet.

The f291 conclusion that a nonzero corner discrepancy remains on the original two-point core-slack \(S\) is **REFUTED**. Edge core slack already forces (E), and (E) supplies the allegedly missing corner compatibility at both endpoints. The discrepancy described at S12|21 uses the regime \(u\ge\sqrt\lambda-m\), which the same review correctly proves disjoint from \(S\). The possible pair-corner discrepancy in S12|22 also cannot occur for an \(S_{\rm pair}\) point with \(c<a+1\), because that case already forces (E).

The general corner-rule formulas in f291 remain useful. Its assertion that their correction is nonzero on the original \(S\) does not.

This does not invalidate f291’s standalone face-speed calculation, empty-substratum proof, or endpoint cubic-cancellation correction.

## 5. Full \(\Delta\) reconstruction off \(S_{\rm both}\)

Define
\[
\psi_0(z,y)=
\frac{z^3}{3}+y^2z-\frac{4y^3}{3}-\lambda(z-y),
\]
and let \(F_0^d,F_1^d\) be the corrected constrained two-line profiles at \((a,d)\), on \(0\le y\le a\).

For \(d\in\{c,u\}\), define the corner profile
\[
\phi_d(y)=
\min(2d-y,\max(d,2a+1-y,R_1(y))),
\quad a\le y\le u.
\]
In particular,
\[
\phi_u(y)=2u-y.
\]

Direct subtraction of the full functional gives the following identity at every feasible pair, conditional on the imported corrected-profile reduction:
\[
\boxed{\Delta=D_0+C_0^{\rm diff}+C_{1,\rm core}^{\rm diff}
+C_{1,\rm corner}^{\rm diff},}
\]
where
\[
C_0^{\rm diff}
=
8(1-b)\int_0^a
[\psi_0(F_0^c(y),y)-\psi_0(F_0^u(y),y)]\,dy,
\]
\[
\begin{aligned}
C_{1,\rm core}^{\rm diff}
=8b\int_0^a\Bigl\{&
[\psi_1(F_1^c(y),y)-\psi_1(p_c(y),y)]\\
&-[\psi_1(F_1^u(y),y)-\psi_1(p_u(y),y)]
\Bigr\}\,dy,
\end{aligned}
\]
and
\[
\begin{aligned}
C_{1,\rm corner}^{\rm diff}
=8b\int_a^u\Bigl\{&
[\psi_1(\phi_c(y),y)-\psi_1(p_c(y),y)]\\
&-[\psi_1(\phi_u(y),y)-\psi_1(p_u(y),y)]
\Bigr\}\,dy.
\end{aligned}
\]

This retains:

- Both endpoint corner corrections.
- The outer factors \(b\) and \(1-b\).
- The true \(C_0\)-block difference.
- The additional **tail-block correction on the two-line interval**.
- Every moving limit already present in \(D_0\).

### Specialization to \(S_{\rm pair}\)

At the pair endpoint, pair slack and Section 3 give
\[
F_0^c=p_0,\qquad F_1^c=p_c,\qquad \phi_c=p_c.
\]
Consequently,
\[
\begin{aligned}
\Delta=D_0
&+8(1-b)\int_0^a[\psi_0(p_0,y)-\psi_0(F_0^u,y)]\,dy\\
&-8b\int_0^a[\psi_1(F_1^u,y)-\psi_1(p_u,y)]\,dy\\
&-8b\int_a^u[\psi_1(2u-y,y)-\psi_1(p_u,y)]\,dy.
\end{aligned}\tag{P}
\]

The second line is not included in the \(C_0\)-block difference.

### Finding M2 — Include the active-edge tail-core correction

**Severity:** MAJOR completeness gap in the off-\(S_{\rm both}\) composite.  
**Source:** `frontier-20261029-n2-uniqueness-first-unpaid-step-v1-addendum-14-core-block-v1.md`, **LF5–9** — S1|5–9.

S1 correctly identifies a necessary additional \(C_0\)-block difference. However, adding that term to the two corner corrections does **not** complete the off-\(S_{\rm both}\) identity. When the edge core is active, its \(F_1\) on \([0,a]\) also generally differs from the independent \(p_u\); formula (P)’s second line must be retained.

This missing contribution is provably nonzero for \(a>0\) on \(S_{\rm pair}\setminus S_{\rm both}\). At an active edge height, the corrected rule gives
\[
F_0^u=\operatorname{clip}(R_1,[a,2a-y]),
\qquad F_1^u=F_0^u+1.
\]
Activity implies \(R_1<2u-y\), and these projection formulas give
\[
F_1^u>p_u.
\]
Because \(p_u\) is the unique tail-box minimizer and \(\psi_1\) is strictly convex there,
\[
\psi_1(F_1^u,y)>\psi_1(p_u,y).
\]
Failure of (E) makes the edge test fail at \(y=0\); for \(a>0\), continuity supplies an interval of positive length. Thus the omitted integral is strictly positive before its subtraction.

At \(a=0\), the core integrals vanish; the corner correction remains necessary. This boundary does not justify omitting the term for positive \(a\).

Accordingly, **S1’s additional term is supported as a component, but not as a complete off-stratum repair**. The boxed general identity and (P) supply the complete repair.

These comparisons concern correction terms relative to \(D_0\); they do not establish a global sign of \(\Delta\).

## 6. Edge right derivative: SUPPORTED

Under (E), \(p_u(y)=2u-y\) on \([0,u]\), and slack/corner compatibility persists to the right in \(c\). The core block is independent of \(c\). Hence the actual right derivative is obtained from the tail constant, moving endpoint, and face motion.

The tail constant derivative is
\[
\tfrac{16}{3}T_3+8uT_2-8\lambda m.
\]
The endpoint term is
\[
8\psi_1(u,u)=8(T_2u+2mu^2),
\]
because the cubic terms cancel exactly.

Using \(T_2=m^2+v\), the face integral is
\[
\begin{aligned}
\int_0^u\partial_z\psi_1(2u-y,y)\,dy
&=\int_0^u
[2y^2-(4u+2m)y+4u^2+4mu+T_2-\lambda]\,dy\\
&=\tfrac83u^3+3mu^2+(T_2-\lambda)u.
\end{aligned}
\]
Its multiplier is \(16\). Summation yields
\[
\boxed{
b^{-1}\partial_c^+h(a,u;\lambda)
=
\tfrac{16}{3}T_3+32uT_2+64mu^2
+\tfrac{128}{3}u^3-(16u+8m)\lambda.
}
\]

This verifies **S6|7–18**, including the tight weak-slack boundary.

### Ties

Under tight (E), equality with the upper-face root occurs only at \(y=0\); the integrand’s \(z\)-derivative vanishes there. The lower/upper box coincidence at \(y=u\) is another single-height event.

More generally, positive-face ties satisfy either a single level equation or
\[
y^2+(2c-y+m)^2=\lambda-v,
\]
so they cannot occupy an interval. The clipped value \(-m\) cannot tie either positive box face. Thus no positive-measure tie contribution or omitted switching-boundary residue enters this calculation.

This is an actual right derivative of the constrained value on the stated stratum, not an asserted global Clarke interchange identity.

## 7. Normal-cone consequence: necessary exclusion only

If the displayed right derivative is negative, the feasible vertical direction decreases \(h\). The point cannot be a constrained local minimum of \(h(\cdot;\lambda)\). Under the imported zero-level variational reduction, this excludes a candidate optimizer at its corresponding zero level.

If the derivative is nonnegative, it supplies only the vertical necessary test. It proves no existence, scalar-pair uniqueness, sufficiency, global sign, or behavior at other points.

At a differentiable point:

- Positive-\(a\) edge:
  \[
  h_c\ge0,\qquad h_a+h_c=0.
  \]
- Vertex \(a=0,\ c=1/2\):
  \[
  h_c\ge0,\qquad h_a+h_c\ge0.
  \]

At a kink, retain S14’s necessary condition with one and the same subgradient; no equivalence to ordinary directional nonnegativity is imported.

### Finding m1 — Restrict the edge equality to positive \(a\)

**Severity:** MINOR scope correction.  
**Source:** `frontier-20261029-n2-uniqueness-first-unpaid-step-v1-addendum-9-edge-derivative-v1.md`, **LF20–23** — S6|20–23.

The unqualified statement \(h_a+h_c=0\) is not the vertex condition. At \(a=0,c=1/2\), the necessary condition is \(h_a+h_c\ge0\), as already recorded in S14|19. The negative-\(h_c\) exclusion remains valid at both the edge and vertex, so this does not invalidate the exclusion actually established.

## 8. Per-claim disposition

| Claim | Disposition |
|---|---|
| \(S_{\rm both}\iff\lambda\ge v+(2a+1+m)^2\), uniformly for every \(c\ge u\) | **SUPPORTED**, including clipping, all named heights, and weak equality |
| \(S_{\rm pair}\) implies its own corner compatibility | **SUPPORTED** |
| \(S_{\rm pair}\) may be substituted for \(S_{\rm both}\) | **REFUTED** |
| Bare \(S_{\rm full}\) alias across the changing definitions | **INCONCLUSIVE without an explicit definition**; exact alternatives given in §3 |
| Original S11 displayed \(\Delta\) on its original two-point \(S\) | **SUPPORTED** |
| f291 M1 applies on that original \(S\) | **REFUTED — MAJOR** |
| S4’s two-endpoint corner correction | **SUPPORTED** as a component; its withdrawn upper-face parenthetical is not used |
| S1’s \(C_0\)-difference addition completes the off-stratum formula | **Not established; MAJOR completeness gap** — the tail-core difference is also required |
| Full general \(\Delta\) identity and pair-only specialization (P) above | **SUPPORTED**, conditional on the imported profile reduction |
| S6 edge right-derivative identity | **SUPPORTED** |
| Negative derivative excludes a candidate minimum at the imported scope | **SUPPORTED**, necessary exclusion only |
| Positive derivative establishes minimization or uniqueness | **NOT SUPPORTED** |
| Weak nonemptiness correction and empty-substratum result | **SUPPORTED**, as conditional stratum statements |

**Finding totals:** **0 FATAL, 2 MAJOR, 1 MINOR.** The \(S_{\rm full}\) naming ambiguity is exposed explicitly rather than counted as an additional independent finding.

## 9. Process and assurance boundary

Actual clock observations were `13:42:16Z`, `13:43:03Z`, `13:46:36Z`, `13:48:27Z`, and `13:49:33Z`; no active checkpoint gap exceeded thirty minutes.

No scientific code, interpreter, CAS, solver, enumeration, replay, selected mathematical instance, external-model CLI, account/configuration change, build, lint, test, or formatter was used. No f299 transcript or partial derivation, sibling mathematical output, held payload, or excluded link was read. Mandatory memory and skill guidance were administrative context only.

This is **same-harness written support**, not independent-model-family, human, formal/kernel, original-target, or novelty acceptance. No checklist is being promoted into a minimizer or uniqueness theorem.

**Overall correctness: incorrect as a complete composite.** The principal two-point stratum theorem, original two-point \(\Delta\) identity, and edge derivative are supported; f291’s adverse scope conclusion is wrong, and the latest off-stratum repair omits a tail-core contribution. The complete corrected identity and exact acceptance boundaries are supplied above.

**Confidence: 0.98.**