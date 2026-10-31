# UNREVIEWED AUTHOR CANDIDATE — full W1 gap vertex \((a,c,e)\)

**Result:** a new universal coupled identity proves positivity of the entire previously unpaid gap \((a,c,e)\) normalized vertex. This is not another proof of the paid \((0,c,e)\) vertex or merely a first-pair comparison.

The own-wave filesystem write was refused. No bypass was attempted; this is the complete proposed `review-v1.md` body for parent materialization. **No ledger promotion or independent review is claimed.**

## 1. Exact assumptions and scope

Retain the adopted f308 interlacing/class/genericity and odd-envelope admissibility hypotheses. In particular,
\[
a\le b<c\le d<e\le f,\qquad
0<u_1<a<u_2<u_3<b<u_4<d<u_5<f,
\]
with the **open-gap placement**
\[
u_4<c.
\]
The fifth node may lie below, at, or above \(e\).

Let
\[
H(t)=\prod_{j=1}^{5}(t-u_j),\qquad D_i=|H'(u_i)|,
\]
so
\[
\operatorname{sgn}H'(u_i)=(+,-,+,-,+).
\]
Retain both leading scales:
\[
\lambda_-\ge\lambda_+>0,
\]
and the adopted envelopes
\[
O_-(t)=\lambda_-(a-t)(d-t)(e-t),\qquad
O_+(t)=\lambda_+(b-t)(c-t)(f-t).
\]
These marker and scale inequalities are **not** asserted to establish envelope realization by themselves; the adopted envelope/admissibility hypotheses remain an additional import.

The new vertex is
\[
E(t)=(a-t)(c-t)(e-t),\qquad F(t)=-t(b-t)(e-t).
\]
The five-node moment normalization gives
\[
\mu_i=\frac{C}{u_iO_iH'(u_i)},\qquad C>0,
\]
and hence
\[
\frac PC
=\sum_i\frac{-E(u_i)(b-u_i)(e-u_i)}
{O_iH'(u_i)}.
\]

Let \(S\) be the sum of the f308 **termwise odd-endpoint minima** at this explicit even vertex. This is an exact minimum in the nodewise odd-value relaxation and a lower bound for admissible odd-value choices in the explicit model:
\[
P/C\ge S.
\]
It is not a newly proved reduction of arbitrary actual box members to this vertex.

## 2. New full-vertex identity

Define
\[
A_1=
\frac{(c-u_1)(e-u_1)(b-u_1)}
{\lambda_-(d-u_1)D_1},\qquad
A_2=
\frac{(c-u_2)(e-u_2)(b-u_2)}
{\lambda_-(d-u_2)D_2},
\]
and
\[
\delta_{12}=A_2-A_1.
\]

**Candidate theorem.** For every admissible open-gap configuration above,
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

The first difference satisfies \(\delta_{12}>0\). The residue term is nonnegative, and the two remaining displayed terms are strictly positive.

The genuinely new coupled part is
\[
\boxed{
\begin{aligned}
T_3+T_5-|T_4|
={}&\frac{(f-a)(f-e)^2}{\lambda_+H(f)}\\
&+\frac{(a-u_1)(e-u_1)^2}
{\lambda_+(f-u_1)D_1}\\
&+\frac{(u_2-a)(e-u_2)^2}
{\lambda_+(f-u_2)D_2}
>0.
\end{aligned}}
\]
It pays the entire negative fourth term. Combining it with the already adopted—and reconstructed below—first-pair domination closes the **full** vertex.

## 3. Written proof

### 3.1 Exact endpoint contributions

The f308 endpoint table gives
\[
T_1=-A_1,\qquad T_2=A_2.
\]
Here \(T_1,T_2\) use \(O_-\), while \(T_3,T_4,T_5\) use \(O_+\), with the fifth contribution zero when \(u_5=e\).

Set
\[
g_a(t)=\frac{(t-a)(e-t)^2}{\lambda_+(f-t)}.
\]
Cancellation against \(O_+\) gives, throughout the open gap,
\[
T_3=\frac{g_a(u_3)}{D_3},\qquad
T_4=-\frac{g_a(u_4)}{D_4},\qquad
T_5=\frac{g_a(u_5)}{D_5}.
\]
All formulas use the same actual nodes and their actual \(H'\)-factors.

In particular,
\[
g_a(u_1)<0,\qquad g_a(u_2)>0.
\]

The formal \(O_+\) baseline at node 2 has the wrong odd sign and is not an admissible W1 atom. At node 1, the \(O_+\) baseline is not the minimizing endpoint. Both differences are accounted for explicitly below.

### 3.2 Five-node resolvent identity

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

The five-node Lagrange identity annihilates \(Q\):
\[
\sum_i\frac{Q(u_i)}{H'(u_i)}=0.
\]
Interpolation of the constant polynomial, evaluated at \(f>u_5\), gives
\[
\sum_i\frac{1}{(f-u_i)H'(u_i)}=\frac1{H(f)}.
\]
Consequently,
\[
\boxed{
\sum_i\frac{g_a(u_i)}{H'(u_i)}
=\frac{(f-a)(f-e)^2}{\lambda_+H(f)}.}
\]

### 3.3 Coupling the remaining three terms

Using the signs of \(H'\),
\[
\sum_i\frac{g_a(u_i)}{H'(u_i)}
=
\frac{g_a(u_1)}{D_1}
-\frac{g_a(u_2)}{D_2}
+T_3+T_4+T_5.
\]
Thus
\[
T_3+T_4+T_5
=
\frac{(f-a)(f-e)^2}{\lambda_+H(f)}
-\frac{g_a(u_1)}{D_1}
+\frac{g_a(u_2)}{D_2}.
\]
Both node corrections on the right are strictly positive. Since \(T_4<0\) in the open gap, this proves the displayed strict identity for
\[
T_3+T_5-|T_4|.
\]

This step does **not** treat either formal node-1 or node-2 baseline as its actual minimizing contribution.

### 3.4 The first pair remains strictly positive

For \(v>u_2\), define
\[
\psi(v)=\frac{v-u_2}{v-u_1}.
\]
Then \(0<\psi(v)<1\), and \(\psi\) is strictly increasing, because
\[
\psi'(v)=\frac{u_2-u_1}{(v-u_1)^2}>0.
\]
Direct division gives
\[
\frac{A_2}{A_1}
=
\frac{\psi(c)}{\psi(u_4)}
\frac{\psi(b)}{\psi(u_3)}
\frac{\psi(e)}{\psi(d)}
\frac1{\psi(u_5)}
>1.
\]
Every comparison follows from the standing node/marker order. No comparison between \(u_5\) and \(e\) is needed.

Therefore
\[
T_1+T_2=\delta_{12}>0.
\]
Adding this to the coupled three-term identity proves the full claimed formula and \(S>0\). Since \(C>0\), the explicit model consequently satisfies \(P>0\).

## 4. Boundaries and admissibility

### 4.1 \(u_4=c\)

This boundary requires \(c<d\). Since \(E(c)=0\), the actual fourth contribution is exactly zero for every admissible nonzero negative \(O_4\).

The canceled baseline instead contributes
\[
-\frac{g_a(c)}{D_4}.
\]
Accordingly, the **actual boundary endpoint sum** equals the boxed open-gap expression, evaluated at these boundary nodes, **plus**
\[
\frac{g_a(c)}{D_4}
=
\frac{(c-a)(e-c)^2}
{\lambda_+(f-c)D_4}>0.
\]
The first-pair comparison remains strict: its factor \(\psi(c)/\psi(u_4)\) becomes one, while the remaining factors still give a product greater than one.

Thus the full boundary vertex is positive. The continued negative gap term is only a lower bound, not its exact fourth contribution.

### 4.2 \(u_5=e\)

This requires \(e<f\). The actual fifth contribution and \(g_a(e)\) are both zero. The identity remains exact with \(H\) and \(D_i\) formed from the actual node \(u_5=e\). No correction is needed.

### 4.3 \(e<u_5<f\)

Here \(K_5>0\) and the required odd sign is positive. The minimizing endpoint remains \(O_+\), giving exactly \(g_a(u_5)/D_5>0\).

The entire interpolation identity is evaluated at these same nodes. No inequality is transferred from a configuration with another fifth node.

### 4.4 Marker equalities and excluded degenerations

- If \(c=d\), the open-gap proof remains algebraically valid. The boundary \(u_4=c\) is excluded by \(u_4<d\).
- The strict node chain excludes \(a=b\).
- At the formal equality \(f=e\), the residue vanishes, but \(\delta_{12}\) and both node corrections remain strictly positive. This algebraic observation does not manufacture an actual independent-box W1 realization; the earlier envelope-realization qualification remains.
- No node coalescence, zero-frequency node, vanishing scale, or configuration-independent positive margin is asserted.

At sign ranges touching zero, the nonzero relevant \(K_i/O_i\) diverges positively, not negatively. At \(u_4=c\), its actual fourth contribution is identically zero. Thus the boundary statements do not conceal a negative singular direction.

## 5. Exact imports and claim status

The source labels below are those of the f336 literal packet.

| Input | Exact scope used |
|---|---|
| **S3 LF 7–11; S4 LF 97–159** | Five-node moment normalization and explicit normalized pairing |
| **S4 LF 175–258** | Endpoint formulas, retaining both leading scales |
| **S3 LF 15–23; S4 LF 340–379** | The adopted \((a,c,e)\) first-pair comparison and its fifth-node extension; reconstructed above |
| **S4 LF 287–336** | Actual-zero versus continued-bound distinctions and fifth-node routing |
| **S1 LF 7–21; S2 LF 179–214** | Admitted f315 resolvent method; its paid \((0,c,e)\) conclusion is not counted again |

**Per-claim disposition, at author-candidate level only:**

- **SUPPORTED by the written derivation, UNREVIEWED:** the new \(g_a\) resolvent identity, strict coupled three-term inequality, full gap \((a,c,e)\) positivity, and stated boundary corrections.
- **REFUTED:** no new refutation is claimed.
- **INCONCLUSIVE / unchanged:** every other unpaid full vertex, other words, actual-member reduction, six-node/global synthesis, and \(m7/m8\).

## 6. Remaining obligations

The corrected adopted starting inventory is **six unpaid gap vertices plus six unpaid band vertices: twelve**. This return does not itself change that inventory.

The candidate addresses only **gap \((a,c,e)\)**. If separately accepted, the other five unpaid gap vertices remain:
\[
(0,b,d),\quad(0,c,d),\quad(a,b,d),\quad(a,b,e),\quad(a,c,d).
\]
All six unpaid band vertices remain:
\[
(0,b,d),\quad(0,c,d),\quad(a,b,d),\quad(a,b,e),\quad(a,c,d),\quad(a,c,e).
\]

No universal RI1–RI4 theorem is claimed. The impossible RI5 route is not used. No other word, actual-member certificate reduction, six-node exclusion/certificate, unrestricted synthesis, or \(m7/m8\) obligation is discharged.

## 7. Binding and process record

- Live manifest SHA matched `1133034b87c68464ecfc82a2fd2cec5382230347e51bd531c3f6f74cb2ee30c6`.
- Live receipt SHA matched `77e3744f0baaa395d92df0a775c40b7f5cf36a2d0471ad278291d35e7afe2ae2`.
- Live packet SHA matched `df762dd6cce54e2dcfc78f3b26b4d7af2bc08938707e8c4ac5d0c30f668a0f89`.
- All four source hashes and all five status-control hashes matched their frozen pins.
- The complete manifest, receipt, five status-only controls, and prospective twelve-vertex correction preceded the direct PRE-BODY ACK delivered to Main, following native observation **2026-10-30T08:01:01-0700 PDT**.
- Subsequently read the entire ordered packet sequentially in raw windows of at most 20 LF: lines 1–960, then 961–963, through the final `S4|504`. Coverage was complete: S1 logical lines 1–31; S2 1–388; S3 1–38; S4 1–504. No elision occurred.
- Completed-read observation: **2026-10-30T08:04:17-0700 PDT**.
- Substantive written checkpoint observation: **2026-10-30T08:05:53-0700 PDT**.
- Completed-candidate observation: **2026-10-30T08:06:49-0700 PDT**.
- The packet was not independently regenerated; byte-roundtrip assertions remain receipt assertions.
- No selected mathematical instance, scientific executable, CAS, solver, enumeration, replay, external-model CLI, build, test, lint, formatter, or new budget was used. Quarantine records were status-only; no held payload was opened.

**Assurance ceiling:** one universally quantified written AUTHOR CANDIDATE. It remains **UNREVIEWED**, without independent-family, human, formal/kernel, novelty, or worldwide-status verification.