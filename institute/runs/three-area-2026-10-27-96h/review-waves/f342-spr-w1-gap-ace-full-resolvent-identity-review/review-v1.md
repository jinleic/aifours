# review-v1.md

## f342 — Written review of the full W1 gap \((a,c,e)\) resolvent identity

### 1. Verdict

**SUPPORTED at the explicit normalized five-node model scope.**

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR in the new candidate’s stated mathematical claims.**

The new full gap \((a,c,e)\) identity is correct under the retained interlacing/class/genericity and odd-envelope admissibility hypotheses. In particular, its cubic resolvent identity controls the genuinely coupled last three contributions, including the negative fourth contribution; combining that identity with the reconstructed first-pair comparison proves the entire vertex positive.

This is not a re-counting of gap \((0,c,e)\), nor merely another first-pair domination. If subsequently adopted, it pays **precisely one** of the twelve starting unpaid full vertices.

The role here is **DISJOINT SAME-HARNESS WRITTEN reviewer**, not author, independent-model-family reviewer, human referee, or kernel.

### 2. Exact frozen inputs and import boundary

Source labels refer to this wave’s complete literal packet:

| Label | Frozen source | Scope used |
|---|---|---|
| **S1** | f336 `review-v1.md`, logical lines 1–311 | Complete **UNREVIEWED author candidate** under review |
| **S2** | `info-2-w1-gap-0ce-full-coupled-resolvent-positivity-parent-v1.md`, lines 1–31 | Adopted gap \((0,c,e)\) result and corrected starting residual |
| **S3** | f315 `review-v1.md`, logical lines 1–388 | Expressly assigned prior written reconstruction, including normalization, interpolation, and realization qualifications |
| **S4** | `info-2-w1-five-node-annihilator-table-and-limited-positivity-parent-v1.md`, lines 1–38 | Adopted corrected table and limited-positivity interface |
| **S5** | f308 `review-v1.md`, logical lines 1–504 | Complete endpoint reconstruction, first-pair factors, boundary routing, and historical residuals |

The load-bearing adopted interface is S4 lines 7–11 and 23, together with S5 lines 97–159, 175–258, 287–336, and 340–379. The interlacing/class/genericity and envelope-realization framework is retained at its adopted provenance; it is not independently established from outside scientific sources here.

S2’s adoption supersedes the earlier seven-gap residual in S4/S5 by paying gap \((0,c,e)\). It does not pay the new candidate in advance.

The named quarantine and deviation controls provide **status exclusions only**. Neither their episodes nor their correctness, selection, or confidence consumers are premises in this review. No excluded link or unassigned reviewer body was followed.

### 3. Assumptions and normalization

Retain
\[
a\le b<c\le d<e\le f,
\qquad
0<u_1<a<u_2<u_3<b<u_4<d<u_5<f.
\]
For the open gap, additionally impose
\[
u_4<c.
\]
The strict node chain already forces \(a<b\).

Retain the individual positive leading scales
\[
\lambda_-\ge\lambda_+>0
\]
and the adopted envelopes
\[
O_-(t)=\lambda_-(a-t)(d-t)(e-t),
\qquad
O_+(t)=\lambda_+(b-t)(c-t)(f-t).
\]

These marker and scale inequalities do **not**, on their own, establish an actual coefficient-box realization. The imported envelope ordering, attainability, and admissibility hypotheses remain additional assumptions.

Set
\[
H(t)=\prod_{j=1}^{5}(t-u_j),\qquad D_i=|H'(u_i)|>0.
\]
There are \(5-i\) negative factors in \(H'(u_i)\), so
\[
\operatorname{sgn}H'(u_i)=(+,-,+,-,+).
\]

For the four zero odd moments, write
\[
y_i=\mu_i u_iO_i,\qquad
\sum_i u_i^r y_i=0,\quad r=0,1,2,3.
\]
Lagrange interpolation gives
\[
\sum_i\frac{p(u_i)}{H'(u_i)}=0
\qquad(\deg p\le3).
\]
The four-row Vandermonde matrix has rank four, hence its nullspace is the span of \((1/H'(u_i))_i\). Therefore
\[
y_i=\frac{C}{H'(u_i)},\qquad
\mu_i=\frac{C}{u_iO_iH'(u_i)}.
\]
The W1 odd signs agree with the signs of \(H'\), so positive weights imply \(C>0\).

At the new vertex,
\[
E(t)=(a-t)(c-t)(e-t),\qquad
F(t)=-t(b-t)(e-t).
\]
Thus
\[
\frac PC
=\sum_i\frac{E(u_i)F(u_i)}
 {u_iO_iH'(u_i)}
=\sum_i
 \frac{-(a-u_i)(c-u_i)(b-u_i)(e-u_i)^2}
 {O_iH'(u_i)}.
\]
The node factor from the weights cancels against \(F\), with no additional factor discarded.

Let \(S\) denote the sum of the nodewise minimizing odd-endpoint contributions at this fixed explicit even vertex. Then
\[
P/C\ge S.
\]
This is the exact minimum in the stated nodewise odd-value relaxation, not a newly established reduction of arbitrary actual box members.

### 4. Exact f308 endpoints, retaining both scales

Define
\[
K_i=\frac{E(u_i)F(u_i)}{u_iH'(u_i)}.
\]
For a fixed nonzero \(K\),
\[
\frac{d}{dO}\frac KO=-\frac{K}{O^2}.
\]
Together with the required W1 odd sign, this determines the minimizing endpoint.

Throughout the open gap:

| Node | Sign of \(K_i\) | Required odd sign | Minimizing endpoint |
|---|---:|---:|---|
| \(u_1\) | \(-\) | \(+\) | \(O_-\) |
| \(u_2\) | \(-\) | \(-\) | \(O_-\) |
| \(u_3\) | \(+\) | \(+\) | \(O_+\) |
| \(u_4\) | \(+\) | \(-\) | \(O_+\), strictly negative here |
| \(u_5\ne e\) | \(+\) | \(+\) | \(O_+\) |

At \(u_5=e\), \(K_5=0\), so its contribution is zero for every admissible nonzero positive odd value.

Direct substitution gives
\[
T_1=-A_1,\qquad T_2=A_2,
\]
where
\[
A_1=
\frac{(c-u_1)(e-u_1)(b-u_1)}
 {\lambda_-(d-u_1)D_1},
\qquad
A_2=
\frac{(c-u_2)(e-u_2)(b-u_2)}
 {\lambda_-(d-u_2)D_2}.
\]
Both are strictly positive.

Define the new rational function
\[
g_a(t)=\frac{(t-a)(e-t)^2}{\lambda_+(f-t)}.
\]
Cancellation against \(O_+\), at the nodes where that endpoint is used, gives
\[
T_3=\frac{g_a(u_3)}{D_3},\qquad
T_4=-\frac{g_a(u_4)}{D_4},\qquad
T_5=\frac{g_a(u_5)}{D_5}.
\]
The last expression includes the zero value when \(u_5=e\).

Thus the negative first contribution and positive second contribution retain \(1/\lambda_-\), while the remaining three retain \(1/\lambda_+\). No monic specialization or equality of scales is used.

These formulas reconstruct S1 lines 111–134 from the assigned f308 interface, rather than transferring the old \((0,c,e)\) expressions.

### 5. Reconstructed strict first-pair comparison

For \(v>u_2\), put
\[
\psi(v)=\frac{v-u_2}{v-u_1}.
\]
Then
\[
0<\psi(v)<1,\qquad
\psi'(v)=\frac{u_2-u_1}{(v-u_1)^2}>0.
\]

The derivative factors give
\[
\frac{D_1}{D_2}
=\frac{1}{\psi(u_3)\psi(u_4)\psi(u_5)}.
\]
Consequently,
\[
\frac{A_2}{A_1}
=
\frac{\psi(c)}{\psi(u_4)}
\frac{\psi(b)}{\psi(u_3)}
\frac{\psi(e)}{\psi(d)}
\frac1{\psi(u_5)}
>1.
\]
Indeed, \(c>u_4\), \(b>u_3\), and \(e>d\); also \(0<\psi(u_5)<1\).

Therefore
\[
\delta_{12}:=A_2-A_1>0.
\]
No ordering between \(u_5\) and \(e\) is needed. The common \(1/\lambda_-\) cancels only in this ratio, not in the individual terms.

This supports S1 lines 196–222, but by itself does not pay the negative fourth term.

### 6. New cubic resolvent and the coupled last three terms

Let
\[
h(t)=(t-a)(e-t)^2.
\]
Since \(h\) is cubic,
\[
g_a(t)=Q(t)+\frac{R_a}{f-t},
\]
where
\[
Q(t)=\frac{h(t)-h(f)}{\lambda_+(f-t)}
\]
is a polynomial of degree at most two, and
\[
R_a=\frac{h(f)}{\lambda_+}
=\frac{(f-a)(f-e)^2}{\lambda_+}\ge0.
\]
The rational remainder has the **plus** sign.

The five-node interpolation identity annihilates \(Q\):
\[
\sum_i\frac{Q(u_i)}{H'(u_i)}=0.
\]
Interpolation of the constant polynomial at \(f\) gives
\[
1=\sum_i\frac{H(f)}{(f-u_i)H'(u_i)}.
\]
Because \(f>u_5\), all factors of \(H(f)\) are positive and no denominator vanishes. Hence
\[
\sum_i\frac{g_a(u_i)}{H'(u_i)}
=\frac{(f-a)(f-e)^2}{\lambda_+H(f)}.
\]

Using the actual \(H'\)-signs,
\[
\sum_i\frac{g_a(u_i)}{H'(u_i)}
=
\frac{g_a(u_1)}{D_1}
-\frac{g_a(u_2)}{D_2}
+T_3+T_4+T_5.
\]
It follows that
\[
\begin{aligned}
T_3+T_4+T_5
={}&\frac{(f-a)(f-e)^2}{\lambda_+H(f)}
-\frac{g_a(u_1)}{D_1}
+\frac{g_a(u_2)}{D_2}\\
={}&\frac{(f-a)(f-e)^2}{\lambda_+H(f)}
+\frac{(a-u_1)(e-u_1)^2}
 {\lambda_+(f-u_1)D_1}\\
&+\frac{(u_2-a)(e-u_2)^2}
 {\lambda_+(f-u_2)D_2}
>0.
\end{aligned}
\]
The residue term is nonnegative. Both displayed node corrections are strictly positive.

Since \(T_4<0\) in the open gap, this proves the genuinely coupled statement
\[
T_3+T_5-|T_4|>0.
\]

#### Both formal-baseline corrections are accounted for

At node 2, \(O_+(u_2)>0\) has the wrong W1 odd sign. Its formal baseline contribution
\[
-\frac{g_a(u_2)}{D_2}
\]
is not an admissible W1 atom.

At node 1, the \(O_+\) baseline is not the minimizing endpoint. Its formal contribution is \(g_a(u_1)/D_1\), not \(-A_1\).

The exact simultaneous replacement is
\[
S=
\sum_i\frac{g_a(u_i)}{H'(u_i)}
+\left(-A_1-\frac{g_a(u_1)}{D_1}\right)
+\left(A_2+\frac{g_a(u_2)}{D_2}\right).
\]
Regrouping yields the candidate’s identity. This does **not** require the individual node-1 replacement to be nonnegative; positivity is obtained from the proved first-pair difference and the two removed-baseline terms.

### 7. Full new vertex identity

Combining Sections 5 and 6 gives
\[
\boxed{
\begin{aligned}
S={}&\delta_{12}
+\frac{(f-a)(f-e)^2}{\lambda_+H(f)}\\
&+\frac{(a-u_1)(e-u_1)^2}
 {\lambda_+(f-u_1)D_1}\\
&+\frac{(u_2-a)(e-u_2)^2}
 {\lambda_+(f-u_2)D_2}
>0.
\end{aligned}}
\]

Therefore, pointwise for every configuration satisfying the stated assumptions,
\[
P/C\ge S>0,\qquad C>0,
\]
and hence \(P>0\).

This proves S1 lines 76–105 and 171–194 at their stated explicit-model scope. It asserts no configuration-independent margin under degeneration.

### 8. Required boundaries and realization qualifications

#### 8.1 Actual \(u_4=c\) contribution

This boundary requires \(c<d\), since \(u_4<d\).

Here \(E(c)=0\), so the actual fourth contribution is exactly zero for every admissible nonzero negative \(O_4\). One must not substitute \(O_+(c)=0\) into the original quotient.

The canceled baseline instead contributes
\[
-\frac{g_a(c)}{D_4}.
\]
Thus, with all \(H\), \(D_i\), and other expressions evaluated at these same boundary nodes,
\[
S_{\mathrm{actual},\,u_4=c}
=
S_{\mathrm{continued}}
+\frac{g_a(c)}{D_4},
\]
where
\[
\frac{g_a(c)}{D_4}
=
\frac{(c-a)(e-c)^2}
 {\lambda_+(f-c)D_4}>0.
\]

The first-pair ratio remains strict: \(\psi(c)/\psi(u_4)=1\), but its other factors still give a product greater than one.

Accordingly, the continued negative fourth expression is a lower bound, not the actual boundary contribution. S1 lines 226–243 make this distinction correctly.

#### 8.2 Fifth node below \(e\)

For \(d<u_5<e\), both \(E(u_5)\) and \(F(u_5)\) are positive. Thus \(K_5>0\), and the positive odd endpoint \(O_+\) minimizes the contribution:
\[
T_5=\frac{g_a(u_5)}{D_5}>0.
\]

#### 8.3 Fifth node at \(e\)

The equality \(u_5=e\) requires \(e<f\). Both the actual contribution and \(g_a(e)\) are zero. No fifth-node correction is needed.

The full interpolation identity uses the actual \(H\) and \(D_i\) with \(u_5=e\).

#### 8.4 Fifth node above \(e\)

For \(e<u_5<f\), both \(E(u_5)\) and \(F(u_5)\) are negative, so \(K_5>0\). Moreover,
\[
O_-(u_5)<0<O_+(u_5).
\]
Over the required positive odd values, the minimizing endpoint remains \(O_+\), yielding
\[
T_5=\frac{g_a(u_5)}{D_5}>0.
\]

Every term and derivative factor is evaluated at these same actual nodes. No inequality is inherited from a different fifth-node configuration.

These observations support S1 lines 245–253.

#### 8.5 Formal \(c=d\) and \(f=e\)

If \(c=d\), the open-gap algebra remains valid. The equality \(u_4=c\) is then excluded by \(u_4<d\).

If \(f=e\), the node order forces \(u_5<e\), excluding the fifth-node equality and above-\(e\) cases. The residue vanishes and
\[
g_a(t)=\frac{(t-a)(e-t)}{\lambda_+}
\]
is quadratic. Its complete interpolation sum is zero, while the two removed-baseline terms and \(\delta_{12}\) remain strictly positive.

These are algebraic statements, not actual-box existence claims.

In particular, the literal independent coefficient-envelope convention in S3 lines 307–313 supplies
\[
O_+(t)-O_-(t)
=\Delta_1+\Delta_3t+\Delta_5t^2+\Delta_7t^3,
\qquad \Delta_j\ge0.
\]
A common positive envelope root forces every width to vanish, so the envelopes coincide. Their ordered smallest roots must then coincide, contradicting \(a<b\).

This common-root obstruction applies to formal \(f=e\), and likewise to \(c=d\) when interpreted as a common envelope root. It does not invalidate the algebraic identities; it reinforces why marker order and scale order alone cannot manufacture an actual W1 box.

S1 lines 255–260 assert only the algebraic continuation and retain the realization qualification. No mathematical correction is required.

#### 8.6 Odd values approaching zero

At \(u_2\), \(K_2<0\), so \(O_2\to0^-\) produces positive divergence. At \(u_3\), and at \(u_5>e\), positive odd values approaching zero likewise produce positive divergence.

The open-gap negative fourth contribution has \(O_+(u_4)<0\), separated from zero at each fixed configuration. At \(u_4=c\), its actual contribution is identically zero for nonzero admissible odd values.

Thus no hidden negative singular direction invalidates the lower bounds. No uniform bound under node coalescence, scale degeneration, or zero-frequency limits is asserted.

### 9. Claim dispositions

| New candidate claim | S1 source lines | Disposition |
|---|---:|---|
| Exact endpoint contributions, with both scales | 109–134 | **SUPPORTED** |
| Cubic quotient degree and nonnegative rational remainder | 136–169 | **SUPPORTED** |
| Correct removal of both formal baseline terms | 171–194 | **SUPPORTED** |
| Strict first-pair comparison | 196–222 | **SUPPORTED** |
| Coupled last-three-term inequality paying negative \(T_4\) | 92–105, 171–194 | **SUPPORTED** |
| Full new gap \((a,c,e)\) identity and positivity | 76–90, 219–222 | **SUPPORTED** |
| Actual-zero \(u_4=c\) correction | 226–243 | **SUPPORTED** |
| Actual fifth-node routing below, at, and above \(e\) | 18, 123–125, 245–253 | **SUPPORTED** |
| Formal marker equalities without manufactured realization | 255–260 | **SUPPORTED with the retained realization hypotheses** |
| Twelve starting unpaid vertices and precisely one proposed payment | 284–295 | **SUPPORTED** |
| Other unpaid vertices and actual-member/six-node/global conclusions | 280, 284–295 | **INCONCLUSIVE / unchanged** |

**REFUTED new candidate claims: none at the stated scope.**

The earlier four MINOR f308 findings remain historical and governed by S4’s adopted corrections. They are not new defects in this candidate.

### 10. Exact prospective residual

The adopted starting inventory is
\[
6\text{ unpaid gap vertices}+6\text{ unpaid band vertices}=12.
\]

If this result is separately adopted, **only gap \((a,c,e)\)** is removed. The remaining five unpaid gap vertices are
\[
(0,b,d),\quad(0,c,d),\quad(a,b,d),\quad(a,b,e),\quad(a,c,d).
\]
All six unpaid band vertices remain:
\[
(0,b,d),\quad(0,c,d),\quad(a,b,d),\quad(a,b,e),\quad(a,c,d),\quad(a,c,e).
\]
The prospective inventory is therefore
\[
5+6=11.
\]

No ledger change is made by this review. Gap \((0,c,e)\) was already paid by S2 and is not counted again.

No actual eligible-box reduction to these explicit vertices, six-node exclusion or certificate, other-word result, unrestricted synthesis, universal RI1–RI4 theorem, or \(m7/m8\) obligation is discharged. The impossible RI5 route is not used.

### 11. Overall assessment

**Overall correctness: correct at the explicit normalized-model scope.**

The new full coupled identity, both leading scales, baseline-correction signs, required boundaries, and prospective one-vertex payment are supported by universal written reconstruction. The additional envelope-realization hypotheses and all unresolved actual-member, six-node, and global boundaries remain intact.

**Confidence: 0.99.**

This is same-harness written support only. It is not an independent-family, human, formal/kernel, novelty, priority, or worldwide-status gate.

---

# reviewer-process-v1.md

## f342 — Factual process chronology

### 1. Role and delivery qualification

Role: **DISJOINT SAME-HARNESS WRITTEN reviewer**.

An attempted write to the assigned wave’s `reviewer-process-v1.md` was refused because the available write tool accepts only device transport and session-local scratch paths. No shell or alternate-path bypass was attempted. Neither proposed output file is claimed to have been created. Their full bodies are returned for Main to materialize.

The administrative PRE-BODY ACK **was successfully delivered directly to Main before scientific packet reading**; the later filesystem refusal did not affect that sequence.

### 2. Observed chronology

1. Read the required memory summary and applicable written-review procedural skills. These supplied procedural context, not mathematical premises.

2. Read the complete frozen manifest, **128 LF**, and freeze receipt, **86 LF**, including endings, in sequential raw windows of at most 20 LF.

3. Read all seven named status-only controls completely, including endings:
   - Owner addendum 2: **14 LF**.
   - L1 quarantine: **23 LF**.
   - Duty execution/reporting deviations: **28 LF**.
   - f336 dispatch-count correction: **14 LF**.
   - Additive AME consumer quarantine: **8 LF**.
   - CORE-GRAM quarantine: **9 LF**.
   - Privacy-parameter quarantine: **11 LF**.

   No excluded payload or linked held body was followed.

4. Ran documentary metadata operations only: `shasum -a 256` and `wc -lc` on the manifest, receipt, seven controls, packet, and five live scientific source files. Every frozen hash, byte count, and LF count matched.

5. Actual native `/bin/date` observation:
   **2026-10-30T08:26:01-0700 PDT**.

   Subsequently sent an administrative PRE-BODY ACK directly to `agent://Main`; the tool reported **Delivered to Main**.

   Exact boundary at that delivery: administrative scope, bindings, controls, and procedural skills had been read; no literal scientific packet/body line had yet been opened or reconstructed in this assignment.

6. Read **every ordered packet line sequentially** in raw windows:
   \(1\!-\!20,21\!-\!40,\ldots,1241\!-\!1260\), then \(1261\!-\!1274\).

   Every call covered at most 20 LF. No elision occurred. Complete displayed source coverage was:
   - S1 logical lines **1–311**, **310 LF**.
   - S2 lines **1–31**.
   - S3 logical lines **1–388**, **387 LF**.
   - S4 lines **1–38**.
   - S5 logical lines **1–504**, **503 LF**.

   The final displayed source ending was `S5|504|**Confidence: 0.99.**`

   No mathematical reconstruction preceded this complete-read boundary.

7. Actual native complete-read observation:
   **2026-10-30T08:29:38-0700 PDT**.

8. Universal written reconstruction then covered:
   - Five-node normalization and every \(H'\)-sign.
   - All minimizing odd endpoints and both leading scales.
   - The exact \(A_2/A_1\) factorization.
   - Cubic rational division and its nonnegative remainder.
   - Removal of both formal baseline terms.
   - The coupled last-three-term inequality and full vertex identity.
   - Actual-zero \(u_4=c\) correction.
   - Fifth node below, at, and above \(e\).
   - Formal marker equalities versus coefficient-envelope realization.
   - The prospective twelve-to-eleven residual accounting.

9. Actual substantive written-checkpoint observation:
   **2026-10-30T08:31:03-0700 PDT**.

10. After that checkpoint, the own-wave process-artifact write was attempted and refused. No successful artifact creation or exact refusal timestamp is invented.

11. Rechecked the manifest, receipt, packet, and all five scientific source hashes. All remained equal to their frozen pins.

12. Actual final binding/checkpoint observation:
   **2026-10-30T08:32:18-0700 PDT**.

These observations are native clock readings, not backdated creation times or a continuous-supervision certificate. The observed work interval did not approach the 30-minute checkpoint limit.

### 3. Live bindings

All hashes below matched their frozen pins:

| Artifact | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| Manifest | `847a02eee831bb1ef16bd77220ff52bb3b2891e8d0da051fe0b42481a8a0eedc` | 7,005 | 128 |
| Freeze receipt | `cdc56027ca654e2565972bdc7a319a155b6672a2c4fc28ca3ba5d0a3337a7d46` | 3,299 | 86 |
| Literal packet | `5f0779677335920a2bd17ec6b983499151646a47ef52d7645fb266313188963c` | 67,407 | 1,274 |
| S1 | `6dfb3cdf79ccefa316dcec35c6c832cf840526131f167baadc2f87d2f1e461b7` | 11,015 | 310 |
| S2 | `d26858d6960f95d9f9f5fd6310a41ab4584ac65889920f577bb986bf24bcc1eb` | 4,821 | 31 |
| S3 | `59e784c14b60b709f11b3faa1529460f8731a8c3c10b516b3c1c0685c6849b1f` | 17,531 | 387 |
| S4 | `ab7debb56facd94151e8d696da8c28d6c4410b79806f244ce4567508e75d91c2` | 5,284 | 38 |
| S5 | `198880d97e1ff03fc8e4c2cdb274d04c2a26c06b0ab14cf91cb64065b0c50ee3` | 20,228 | 503 |

Control bindings:

| Control | SHA-256 |
|---|---|
| Owner addendum 2 | `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce` |
| L1 quarantine | `ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f` |
| Duty deviations | `12e118d84b8fd065d9c02bd29e2d030e6b1b4d4b26c84f1748eb2d72acd8416b` |
| f336 count correction | `3b6ffdf5dca9fb2667bd50ab058350effe359f958ccdd0c32e1c71c25c71be04` |
| AME quarantine | `c307e902eee5f3736aab0e2437738898382b3d3083f6c307118219b9a4c875b0` |
| CORE-GRAM quarantine | `23fa29449cef8e02d981efc021934e4cec16960ca6bfe8f6f2178bbd048c85b4` |
| Privacy quarantine | `e4d6f1e49cb18aced7735cf025dee54830400554c9adc08138250ae9f0523efc` |

The packet was not independently regenerated. Its selected-line byte-equality and roundtrip flags remain freeze-receipt assertions; they are not represented as a separately exercised regeneration check.

### 4. Process limits and preservation

No scientific executable, interpreter, CAS, solver, enumeration, replay, test, build, lint, formatter, author code, unassigned sibling return, outside scientific research, or external-model CLI was used.

No selected scientific instance or private diagnostic was used. The proof used arbitrary universally quantified variables and the required structural boundary cases only.

Historical controls supplied exclusions, not mathematical evidence. No source, frozen byte, historical hold, or ledger was changed. These statements describe the observable actions of this assignment, not a cognitive-isolation certificate.

**Scientific outcome:** same-harness written support for precisely the new full normalized gap \((a,c,e)\) vertex, with **0 FATAL / 0 MAJOR / 0 MINOR** new mathematical findings and all stated wider obligations preserved.