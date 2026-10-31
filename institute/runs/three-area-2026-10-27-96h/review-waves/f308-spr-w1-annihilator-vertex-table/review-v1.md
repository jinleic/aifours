# Independent written review — f308 W1 annihilator and vertex table

## 1. Binding, process and verdict

**Manifest:** `9699f35d0890571979afcce07e4e237199ad2eca00ece12c3ac26705cafa0ecb`  
**Freeze receipt:** `4ba147f689d8f2459c5fc763441037cc0a578fa68390e5431e21552ce000bfb2`  
**Literal packet:** `cff24f20f843af3b5cea5ee88d6b04aed5c25d84cf4b330a5bdcc322fbc9741c`

Live metadata hashes matched these pins, all five input bindings, and the three control bindings. I did not independently regenerate the literal packet; its byte-roundtrip flags remain receipt assertions.

The complete manifest, receipt and status-only controls preceded the administrative PRE-BODY ACK delivered to Main, following the fresh native-clock observation **2026-10-30T06:55:40-0700 PDT**. No mathematical packet body or derivation preceded that ACK.

I subsequently read every packet LF 1–141, sequentially in raw windows of at most 20 LF, including the final line. Coverage was:

- **S1 LF 1–27 first**, complete erratum;
- **S2 LF 1–43**, complete candidate;
- **S3 LF 1–34**, complete adopted disposition;
- **S4 LF 172–192**, selected moment definitions;
- **S5 LF 232–245**, selected four-node normalization.

No elision occurred. No excluded links, held payload, author code, or prior reviewer body outside the selected adopted ranges was read. Only an administrative peer ACK arrived. No scientific execution, CAS, solver, chosen mathematical instance, or external-model review was used. Shell operations were limited to metadata hashing and native date observations.

Fresh substantive checkpoint: **2026-10-30T06:59:01-0700 PDT**. Completed-audit clock: **2026-10-30T07:01:57-0700 PDT**. These observations are not a continuous-supervision certificate.

### Disposition

**Core normalization/table and the five limited positivity claims: SUPPORTED.**

**Findings: 0 FATAL / 0 MAJOR / 4 MINOR.**

There is **no missing node factor** in the five-node weights or Lemma A’s nine term formulas. The first literal normalization omission occurs earlier, **S2 LF 7**: the individual terms omit \(1/\lambda_-\) outside the monic case. Their ratio remains correct.

Unproved RI conditions and full sums are not promoted to theorems. No six-node exclusion, synthesis, support-reduction, or novelty claim is accepted.

## 2. Findings

### F1 — Restore the leading-scale factor in the correction’s individual terms

**Severity:** MINOR  
**Priority:** P2  
**Confidence:** 1.00  
**File:** `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261030-annihilator-w1-consolidated-vertex-table-v1.md`  
**Lines:** 7–7

In the general positive-leading setting explicitly retained by S1 LF 15 and S2 LF 13, the terms at \((a,b,e)\) are
\[
|T_1|=\frac{(b-u_1)^2(e-u_1)}
{\lambda_-(d-u_1)D_1},
\qquad
T_2=\frac{(b-u_2)^2(e-u_2)}
{\lambda_-(d-u_2)D_2}.
\]
LF 7 omits \(1/\lambda_-\), so its individual equalities are valid only in the monic specialization \(\lambda_-=1\). This makes those magnitudes inconsistent with Lemma A, although the common factor cancels from LF 8’s ratio. Insert the factor in both terms or expressly restrict that paragraph to monic boxes. This is **not** an error in Lemma A LF 15–23.

### F2 — Do not assert separation from zero for the band \(u_4\) sign range

**Severity:** MINOR  
**Priority:** P2  
**Confidence:** 1.00  
**File:** Same candidate file  
**Lines:** 25–25

When \(c<u_4<d\), one has \(O_-(u_4)<0<O_+(u_4)\). Consequently the admissible negative odd values fill \([O_-(u_4),0)\), not a range bounded away from zero. Positive atom weights do not exclude odd values arbitrarily close to zero. Nevertheless \(K_4<0\), so \(K_4/O_4\) tends to **positive** infinity and its finite minimum remains at \(O_-\). Replace the separation-from-zero assertion for band \(u_4\) with this sign argument. The incorrect auxiliary sentence does not invalidate the lower bound or create an unbounded-negative direction.

### F3 — Clear the actual RI-2 rather than a stronger sufficient condition

**Severity:** MINOR  
**Priority:** P2  
**Confidence:** 1.00  
**File:** Same candidate file  
**Lines:** 39–39

LF 39’s three-factor inequality is equivalent to
\[
\psi(b)>\psi(u_4)\psi(u_5),
\]
not RI-2,
\[
\psi(b)^2>\psi(u_3)\psi(u_4)\psi(u_5).
\]
The exact clearing of RI-2 retains the squared \(b\)-factors and the \(u_3\)-factors, as derived below. The shorter inequality is sufficient because \(\psi(b)>\psi(u_3)\), so it does not produce a false positivity certificate; it misidentifies the announced residual inequality and can unnecessarily discard cases. Replace the asserted clearing or label it a stronger sufficient condition.

### F4 — Account for all six unclosed band vertices

**Severity:** MINOR  
**Priority:** P2  
**Confidence:** 0.99  
**File:** Same candidate file  
**Lines:** 43–43

Only two of the eight band vertices are proved positive, and neither proved partial domination is a band claim. Six band vertices still lack an unconditional full-sum proof:
\[
(0,b,d),\ (0,c,d),\ (a,b,e),\ (a,b,d),\ (a,c,e),\ (a,c,d).
\]
The phrase “3 band vertices” does not account for LF 38’s obligations, and no equivalence closing three additional vertices is supplied. State six unclosed band vertices. On the gap side, seven full vertices remain unclosed: five other vertices plus the two vertices with only a proved partial domination. “5 gap … beyond the proven dominations” is acceptable only with that distinction explicit.

## 3. Five-node reconstruction without importing four-node weights

Throughout, \(u_i\) denotes the positive squared-frequency variable called \(t_i\) in the adopted moment definition. Let
\[
0<u_1<\cdots<u_5,\qquad
H(t)=\prod_{j=1}^{5}(t-u_j),\qquad
D_i=|H'(u_i)|.
\]
The derivative signs are
\[
\operatorname{sgn}H'(u_i)=(+,-,+,-,+).
\]

The four zero odd moments are
\[
\sum_i u_i^r y_i=0,\qquad r=0,1,2,3,
\qquad y_i=\mu_i u_iO_i.
\]

For every polynomial \(p\) of degree at most three, compare the \(t^4\) coefficient in its degree-at-most-four Lagrange interpolation:
\[
\sum_i\frac{p(u_i)}{H'(u_i)}=0.
\]
The four-row Vandermonde matrix has rank four. Its nullspace is therefore precisely the span of \((1/H'(u_i))_i\). Hence
\[
y_i=\frac{C}{H'(u_i)},
\qquad
\boxed{\mu_i=\frac{C}{u_iO_iH'(u_i)}}.
\]

For the W1 odd signs \((+,-,+,-,+)\), positivity of all \(\mu_i\) is equivalent to \(C>0\).

This reconstructs S2 LF 13. In particular, the four-node \(e_{3-k}\) numerator in S5 is **not transferred** to this five-node nullspace.

For
\[
E(t)=(x-t)(y-t)(z-t),
\qquad F(t)=-t(b-t)(e-t),
\]
the even pairing is
\[
\begin{aligned}
P
&=\sum_i\mu_iE(u_i)F(u_i)\\
&=C\sum_i\frac{E(u_i)F(u_i)}
 {u_iO_iH'(u_i)}\\
&=C\sum_i
 \frac{-E(u_i)(b-u_i)(e-u_i)}
 {O_iH'(u_i)}.
\end{aligned}
\]

Thus the \(u_i\) in the atom weight is canceled by \(F\). No further node factor may be dropped. In particular, \(x=0\) gives
\[
E(u_i)=-u_i(y-u_i)(z-u_i),
\]
explaining the retained \(u_1\) in \(T_1(x=0)\) and the retained factors \(x-u_2=-u_2\), \(x-u_3=-u_3\) in the other formulas.

Also,
\[
F(t)=-be\,t+(b+e)t^2-t^3.
\]
Under the adopted strict even-moment signs, its pairing is strictly negative. The vertex calculations below concern the explicit normalized \(E/F\) model; they do not alone establish a new actual-member envelope reduction or support-exclusion theorem.

## 4. Exact substitution and worst-endpoint audit

Use S1’s corrected orders:

- **Gap:** \(0<u_1<a<u_2<u_3<b<u_4<c<d<u_5<e\).
- **Band:** \(0<u_1<a<u_2<u_3<b<c<u_4<d<u_5<e\).

Put
\[
K_i=\frac{E(u_i)F(u_i)}{u_iH'(u_i)},
\qquad T_i=\frac{K_i}{O_i}.
\]
The sign of \(K_i\), not merely that of \(O_i\), determines the minimizing endpoint.

### Term-by-term reconstruction

1. **\(u_1,\ x=0\).**  
   \(K_1>0,\ O_1>0\); minimize at \(O_+\). Cancellation gives
   \[
   T_1=
   \frac{u_1(y-u_1)(z-u_1)(e-u_1)}
   {\lambda_+(c-u_1)(f-u_1)D_1},
   \]
   exactly LF 15.

2. **\(u_1,\ x=a\).**  
   \(K_1<0,\ O_1>0\); minimize at \(O_-\). Cancellation gives
   \[
   T_1=
   -\frac{(y-u_1)(z-u_1)(b-u_1)}
   {\lambda_-(d-u_1)D_1},
   \]
   exactly LF 16.

3. **\(u_2\).**  
   \(K_2<0,\ O_2<0,\ H'(u_2)=-D_2\); minimize at \(O_-\):
   \[
   T_2=
   \frac{(x-u_2)(y-u_2)(z-u_2)(b-u_2)}
   {\lambda_-(a-u_2)(d-u_2)D_2}.
   \]
   At \(x=a\), the \(a-u_2\) factors cancel as stated in LF 17.

4. **\(u_3\).**  
   \(K_3>0,\ O_3>0,\ H'(u_3)=D_3\); minimize at \(O_+\):
   \[
   T_3=
   -\frac{(x-u_3)(y-u_3)(z-u_3)(e-u_3)}
   {\lambda_+(c-u_3)(f-u_3)D_3},
   \]
   exactly LF 18.

5. **Gap \(u_4,\ y=b\).**  
   \(E(u_4)>0,\ F(u_4)>0,\ H'(u_4)=-D_4\), hence \(K_4<0\). With \(O_4<0\), minimize at \(O_-\):
   \[
   T_4=
   \frac{(x-u_4)(z-u_4)(b-u_4)^2}
   {\lambda_-(a-u_4)(d-u_4)D_4},
   \]
   exactly LF 19.

6. **Gap \(u_4,\ y=c\).**  
   \(E(u_4)<0\), so \(K_4>0\). With \(O_4<0\), minimize at \(O_+\):
   \[
   T_4=
   \frac{(x-u_4)(z-u_4)(e-u_4)}
   {\lambda_+(f-u_4)D_4},
   \]
   exactly LF 20. Canceling \(c-u_4\) does not make this the exact value at \(u_4=c\).

7. **Band \(u_4\), either \(y\).**  
   \(E(u_4)>0,\ K_4<0\); minimize at \(O_-\):
   \[
   T_4=
   \frac{(x-u_4)(y-u_4)(z-u_4)(b-u_4)}
   {\lambda_-(a-u_4)(d-u_4)D_4},
   \]
   exactly LF 21. The allowed negative \(O_4\)-range touches zero, as addressed in F2.

8. **\(u_5<e,\ z=e\).**  
   \(E(u_5)>0,\ F(u_5)>0,\ H'(u_5)=D_5\), so \(K_5>0\). Minimize at \(O_+\):
   \[
   T_5=
   -\frac{(x-u_5)(y-u_5)(e-u_5)^2}
   {\lambda_+(c-u_5)(f-u_5)D_5},
   \]
   exactly LF 22.

9. **\(u_5<e,\ z=d\).**  
   \(E(u_5)<0,\ K_5<0,\ O_5>0\); minimize at \(O_-\):
   \[
   T_5=
   -\frac{(x-u_5)(y-u_5)(b-u_5)}
   {\lambda_-(a-u_5)D_5},
   \]
   exactly LF 23.

These calculations cover every \(x,y,z\) endpoint. **All nine Lemma A formulas are SUPPORTED in their stated open regions.**

The odd-envelope endpoints are attainable because odd coefficients vary independently and evaluation is affine. Whenever an allowed sign range touches zero, the corresponding divergent direction is positive. For negative terms, the relevant allowed odd values are separated from zero in the applicable open gap placement.

Therefore the pointwise lower bounds and absence of an unbounded-negative odd-denominator direction are supported, after F2’s correction. This is not a uniform boundedness claim as distinct nodes coalesce.

### Complete vertex sign table

Entries are ordered \(T_1,\ldots,T_5\).

| Vertex | Gap | Band |
|---|---|---|
| \((0,b,d)\) | \(+,+,+,+,-\) | \(+,+,+,+,-\) |
| \((0,b,e)\) | \(+,+,+,+,+\) | \(+,+,+,+,+\) |
| \((0,c,d)\) | \(+,+,+,-,-\) | \(+,+,+,+,-\) |
| \((0,c,e)\) | \(+,+,+,-,+\) | \(+,+,+,+,+\) |
| \((a,b,d)\) | \(-,+,+,+,-\) | \(-,+,+,+,-\) |
| \((a,b,e)\) | \(-,+,+,+,+\) | \(-,+,+,+,+\) |
| \((a,c,d)\) | \(-,+,+,-,-\) | \(-,+,+,+,-\) |
| \((a,c,e)\) | \(-,+,+,-,+\) | \(-,+,+,+,+\) |

This proves the three claimed all-positive vertices:

- Gap \((0,b,e)\);
- Band \((0,b,e)\);
- Band \((0,c,e)\).

No other full vertex follows from sign inspection in the open region.

## 5. Boundaries and the \(u_5\)-extension

### \(u_4=c\)

Because \(u_4<d\), this boundary entails \(c<d\).

For \(y=c\), \(E(c)=0\), so the actual term is exactly zero for every admissible nonzero \(O_4\). The continuously extended gap bound is
\[
\frac{(x-c)(z-c)(e-c)}
{\lambda_+(f-c)D_4}<0.
\]
It remains a lower bound, not the exact boundary minimum.

For \(y=b\), \(K_4<0\), \(O_-(c)<0\), and \(O_+(c)=0\). The admissible negative range is \([O_-(c),0)\), and the finite minimum remains at \(O_-(c)\), as in the band expression.

**S1 LF 19: SUPPORTED**, with the exact-value/lower-bound distinction retained.

### \(u_5=e\)

Since \(F(e)=0\), the actual \(T_5\) is exactly zero at both \(z\)-vertices.

The \(z=e\) formula is zero. The continued \(z=d\) expression from LF 23 is negative and remains only a lower bound. One must not substitute \(O_-(e)=0\) into the uncanceled quotient.

**S1’s zero-term statement: SUPPORTED.**

### \(e<u_5<f\)

At every vertex,
\[
E(u_5)<0,\qquad F(u_5)<0,\qquad K_5>0.
\]
Moreover,
\[
O_-(u_5)<0<O_+(u_5).
\]
The required positive \(O_5\) may approach zero, but the minimum is finite at \(O_+\):
\[
T_{5,\min}(z)=
-\frac{(x-u_5)(y-u_5)(z-u_5)(e-u_5)}
{\lambda_+(c-u_5)(f-u_5)D_5}>0,
\qquad z\in\{d,e\}.
\]

For \(z=e\), this remains LF 22. For \(z=d\), it replaces LF 23 as the **exact** minimum; LF 23 remains a negative conservative lower bound.

Terms 1–4 retain their derived formulas at the new ordered nodes. This establishes a termwise lower-bound extension, **not** a general license to transfer an inequality evaluated at a different \(u_5\). The partial dominations are separately extended below.

The three previously proved full vertices remain positive: their last term is zero at \(e\) and positive beyond \(e\). Unproved RI/full-sum obligations remain conditional.

**S1 LF 23 and LF 27: SUPPORTED in this limited lower-bound sense**, not as an exact continuation of the \(z=d\) worst-endpoint formula.

## 6. Ratios, partial dominations and RI status

For \(v>u_2\),
\[
0<\psi(v)=\frac{v-u_2}{v-u_1}<1,
\]
and \(\psi\) is strictly increasing by S2 LF 29’s identity.

At every \(x=a\) vertex, direct division of the reconstructed terms gives
\[
R(y,z)=\frac{T_2}{|T_1|}
=\frac{\psi(y)\psi(z)\psi(b)}
{\psi(d)\psi(u_3)\psi(u_4)\psi(u_5)}.
\]
Here
\[
\frac{D_1}{D_2}
=\frac1{\psi(u_3)\psi(u_4)\psi(u_5)},
\]
and the shared \(1/\lambda_-\) cancels. This reconstructs the general ratio and its \((a,b,e)\) specialization without transferring another vertex’s canceled expression.

### The two gap partial dominations

At \((a,c,d)\),
\[
R(c,d)=
\frac{\psi(c)}{\psi(u_4)}
\frac{\psi(b)}{\psi(u_3)}
\frac1{\psi(u_5)}>1.
\]

At \((a,c,e)\),
\[
R(c,e)=R(c,d)\frac{\psi(e)}{\psi(d)}
>R(c,d)>1.
\]

These prove the two literal partial dominations. They also extend them to **every \(u_5\in(d,f)\), including \(e\)**, without extending the old \(e\leftrightarrow u_5\) matching beyond its valid order.

They remain strict at \(u_4=c\), because the other factors remain strict.

They do **not** prove the associated full open-gap sums: negative \(T_4\), and for \(z=d,u_5<e\) negative \(T_5\), remain.

### RI-1 and RI-2

The exact first-pair criteria are:

\[
(a,b,e):\quad
\psi(b)^2\psi(e)>
\psi(d)\psi(u_3)\psi(u_4)\psi(u_5),
\]
and
\[
(a,b,d):\quad
\psi(b)^2>
\psi(u_3)\psi(u_4)\psi(u_5).
\]

The latter clears exactly to
\[
\boxed{
(b-u_2)^2(u_3-u_1)(u_4-u_1)(u_5-u_1)
>
(b-u_1)^2(u_3-u_2)(u_4-u_2)(u_5-u_2).
}
\]

LF 39 instead clears
\[
\psi(b)>\psi(u_4)\psi(u_5).
\]
Since \(\psi(b)>\psi(u_3)\), that stronger inequality implies RI-2, but it is not RI-2’s asserted algebraic form.

### RI-3 and RI-4

For band \((a,b,e)\),
\[
R(b,e)=
\frac{\psi(b)}{\psi(u_3)}
\frac{\psi(e)}{\psi(u_4)}
\frac{\psi(b)}{\psi(u_5)\psi(d)}.
\]
The first two factors exceed one, so RI-3 is sufficient.

Replacing the last numerator \(\psi(b)\) by \(\psi(c)\) gives the corresponding proof of RI-4 at \((a,c,e)\).

### RI-5 is a vacuous sufficient condition on band placements

For band \((a,c,d)\),
\[
R(c,d)=
\frac{\psi(b)}{\psi(u_3)}
\frac{\psi(d)}{\psi(u_4)}
\frac{\psi(c)}{\psi(u_5)\psi(d)}.
\]
Thus the stated RI-5,
\[
\psi(c)>\psi(u_5),
\]
is stronger than needed and would imply \(R>1\).

However, throughout the band placement,
\[
c<u_4<d<u_5,
\]
so strict monotonicity gives
\[
\psi(c)<\psi(u_5).
\]

Therefore **RI-5 is uniformly impossible in the band region**. Its sufficient implication is true but vacuous; it is not an open nonempty route and does not refute full-sum positivity.

### Sufficient is not necessary

All domination-plus-remainder routes are sufficient, as corrected by S1 LF 27, and none is necessary for a positive full sum.

The gap comparisons at \((0,b,d)\), \((0,c,e)\), \((0,c,d)\), and the \((a,c,d)\) comparison retaining \(T_2-|T_1|\), are exact rearrangements of their sign table. Discarding a positive first pair in other routes makes those conditions only sufficient.

Band
\[
T_3+T_4>|T_5^d|
\]
is sufficient after controlling an \(x=a\) first pair, or after discarding positive \(T_1,T_2\) when \(x=0\).

No universal validity of RI-1 through RI-4, or of any remaining full-sum inequality, is established by this packet or review.

## 7. Exact claim register

| Claim | Disposition |
|---|---|
| S1 LF 7–11: corrected node orders | **SUPPORTED**, conditional on the adopted interlacing/class and genericity framework. The garbled S2 LF 13 order is replaced, not retroactively validated. |
| S1 LF 15: leading scales and \(\lambda_-\ge\lambda_+>0\) | **SUPPORTED** algebraically for the stated positive-leading interval. Monic specialization gives both scales equal to one. |
| S2 LF 7: individual correction magnitudes | **REFUTED** as unrestricted positive-leading equalities; **SUPPORTED** in the monic specialization. |
| S2 LF 8: corrected \((a,b,e)\) ratio | **SUPPORTED**. |
| S2 LF 13: five-node annihilator and pairing | **SUPPORTED**, reconstructed above. |
| S2 LF 15–23: open-region endpoint table | **SUPPORTED** for the explicit normalized \(E/F\) model, retaining every node and leading-scale factor. |
| S2 LF 25: finite minimum/no unbounded-negative odd-denominator direction | **SUPPORTED**. Its band-\(u_4\) separation-from-zero subclaim is **REFUTED**. |
| S2 LF 29–31: ratio and two gap partial dominations | **SUPPORTED**; not complete vertex proofs. |
| S2 LF 33: three stated all-positive vertices | **SUPPORTED**, with the boundary/extensions interpreted as above. |
| S1 LF 19, 23: boundary/extension lower bounds | **SUPPORTED**. Reading the old negative \(T_5^d\) expression as the exact minimum for \(u_5\ge e\) would be **REFUTED**. |
| S2 LF 37–38; S1 LF 27: sufficient-route status | **SUPPORTED** as conditional implications, not necessity or proofs that the residual inequalities hold. |
| Universal RI-1 through RI-4 and unresolved full sums | **INCONCLUSIVE**. |
| RI-5 feasibility on band placements | **REFUTED uniformly**; its sufficient implication remains valid but vacuous. |
| S2 LF 39: exact clearing of RI-2 | **REFUTED**; stronger-condition sufficiency is **SUPPORTED**. |
| S2 LF 43: three-band residual inventory | **REFUTED** as the inventory of the supplied proofs. Six band vertices remain unclosed. |
| Other word counts/global residual censuses | **Not reconstructed**; no new acceptance here. |
| S3: adopted at-most-five positive-frequency exclusion | Retained as an **ADOPTED INPUT**, not newly proved by this review. |

## 8. Imports and final acceptance boundary

The classical/adopted boundary is the Hurwitz/interlacing/class perturbation framework and the prior lower-bound disposition. The five-node Vandermonde/Lagrange derivation, endpoint minimization, complete vertex sign table, and matching arguments above were reconstructed here.

The imported lower bound concerns **compact independent monic degree-seven strictly Hurwitz boxes**, including optional zero/infinity atoms. The algebraic positive-leading table does not silently extend that theorem to a different box class.

S3’s adverse historical findings remain intact. Its finite-execution summaries are history/status, not mathematical premises used in this derivation. The complete earlier review, finite checker, and author code were outside the read set.

The remaining full vertices are:

- **Seven gap vertices** other than \((0,b,e)\), including \((a,c,d)\) and \((a,c,e)\), for which only the first pair is proved controlled;
- **Six band vertices** other than \((0,b,e)\) and \((0,c,e)\).

The packet supplies sufficient routes, not their universal proofs. No six-node exclusion or certificate, \(m=7/m=8\) result, original synthesis theorem, formal proof, independent-family gate, worldwide-status verification, or novelty conclusion follows.

**Overall correctness: incorrect as a literally exact frozen package**, because of the four MINOR errors. The core five-node normalization, exact open-region endpoint table, two partial dominations, and three full positive vertices are supported; the findings do not reveal a FATAL or MAJOR defect in those five limited claims. No wider acceptance is granted.

**Confidence: 0.99.**