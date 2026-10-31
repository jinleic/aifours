# f310 — A coupled resolvent identity pays the full gap \((0,c,e)\) vertex

**UNREVIEWED AUTHOR CANDIDATE — prospective written development, not independent review or acceptance.**

## 1. Binding and process

- **Manifest:** `98e56288c2dec746ab0f1e1dd19f34144f6e4984259e2f66f596989e77864992`
- **Freeze receipt:** `841c5263f6cec9ed52393412ea7f08cafaae5ecd55a1c57f981b00b239f1983e`
- **Literal packet:** `f81679c6ae0b67c6171e2674156f0da75b440eb1af991e97ad433459983a1244`

Live metadata hashing matched these three pins and all five admitted mathematical source pins. The receipt’s byte-roundtrip assertions were read; the packet was not independently regenerated.

The complete manifest, receipt and all five status-only controls preceded the administrative PRE-BODY ACK delivered to Main. The fresh pre-body clock was **2026-10-30T14:20:24Z**. An earlier attempt addressed the nonexistent agent `parent` and failed; successful delivery to Main still preceded every mathematical packet read.

After the ACK, I read every literal-packet LF **1–648**, in ordered raw windows of at most 20 LF, including the ending:

- S1 LF 1–38;
- S2 logical lines 1–504;
- S3 LF 1–27;
- S4 LF 1–43;
- S5 LF 1–34.

No output elision required recovery. S1’s adopted corrections and the complete corrected reconstruction preceded the original S4 table. No mathematical source outside the frozen packet was consulted. S5’s execution history was status only, not proof input. No held diagnostic payload or consumer was used.

Fresh post-read/start clock: **2026-10-30T14:21:57Z**. Fresh substantive completion/checkpoint clock: **2026-10-30T14:25:17Z**. The substantive result at that checkpoint was the full-sum identity below, including its boundary routing.

No scientific executable, CAS, solver, enumeration, replay, selected mathematical configuration or external-model CLI was used. Machine work comprised metadata hashing and native date observations only. No build, lint, test or formatter was run. These observations are not a continuous-supervision or independent-acceptance certificate.

## 2. Exact imports and scope

The following are imports, not reproved results:

1. **S1 LF 7–11 and S2 LF 97–159:** the five-node annihilator normalization, \(C>0\), and the even pairing
   \[
   P=C\sum_iT_i,
   \]
   retaining the node factor in the weight and its cancellation against \(F\).

2. **S1 LF 21–32, S2 LF 161–336 and S3 LF 7–23:** corrected node orders, positive leading scales, exact open-region endpoint formulas, and the actual-value versus continued-bound distinctions at \(u_4=c\) and \(u_5=e\).

3. The three adopted full positive vertices and two gap first-pair dominations retain their previous scope. They are not reproved or counted as new results here.

4. S5’s at-most-five-frequency exclusion remains an adopted theorem at its stated compact independent monic septic-box scope. It is not needed for the identity below and is not extended.

**The new theorem concerns the explicit normalized \(E/F\) model only. It does not establish actual-member certificate reduction to that model.**

## 3. New universally quantified result

Assume the corrected marker order
\[
a\le b<c\le d<e\le f
\]
and distinct positive nodes satisfying
\[
0<u_1<a<u_2<u_3<b<u_4<d<u_5<f.
\]

The new unpaid case is the entire gap
\[
b<u_4<c.
\]
The boundary \(u_4=c\) is treated below. The already-paid band \(c<u_4<d\) is recorded only to make the identity’s routing explicit. **No additional ordering between \(u_5\) and \(e\) is assumed.**

Let
\[
\lambda_-\ge\lambda_+>0,\qquad
H(t)=\prod_{j=1}^{5}(t-u_j),\qquad D_i=|H'(u_i)|,
\]
and
\[
O_-(t)=\lambda_-(a-t)(d-t)(e-t),\qquad
O_+(t)=\lambda_+(b-t)(c-t)(f-t).
\]

Use the adopted W1 odd signs \((+,-,+,-,+)\), nonzero odd values, and the corrected exact pointwise minima. Fix the previously unpaid gap vertex
\[
E(t)=(-t)(c-t)(e-t),\qquad F(t)=-t(b-t)(e-t),
\]
and write \(S=\sum_iT_i\) for its normalized worst-endpoint full sum.

### Theorem — full gap \((0,c,e)\) positivity

Throughout \(b<u_4<c\),
\[
\boxed{
\begin{aligned}
S={}&\frac{f(f-e)^2}{\lambda_+H(f)}\\
&+\frac{u_2(c-u_2)(e-u_2)(b-u_2)}
{\lambda_-(u_2-a)(d-u_2)D_2}\\
&+\frac{u_2(e-u_2)^2}
{\lambda_+(f-u_2)D_2}
>0.
\end{aligned}}
\tag{1}
\]

Every variable is universally quantified over the stated region. In particular, (1) holds for **all \(u_5\in(d,f)\)**, including \(u_5=e\) when allowed. Both individual leading scales are retained; no monic specialization is used.

This is a full vertex proof, not another domination of \(T_1\) by \(T_2\). More precisely, the proof establishes the coupled inequality
\[
\boxed{
T_1+T_3+T_5-|T_4|
=
\frac{f(f-e)^2}{\lambda_+H(f)}
+\frac{u_2(e-u_2)^2}
{\lambda_+(f-u_2)D_2}
>0.
}
\tag{2}
\]

Thus the genuinely unpaid negative \(T_4\) is paid by the indicated three positive/nonnegative terms **before adding the strictly positive \(T_2\)**.

## 4. Proof of the coupled identity

Define
\[
g(t)=\frac{t(e-t)^2}{\lambda_+(f-t)}.
\]

The derivative signs at the ordered nodes are
\[
\operatorname{sgn}H'(u_i)=(+,-,+,-,+).
\]

At the gap vertex \((0,c,e)\), the imported exact table gives
\[
\begin{aligned}
T_1&=\frac{g(u_1)}{D_1},\\
T_2&=\frac{u_2(c-u_2)(e-u_2)(b-u_2)}
{\lambda_-(u_2-a)(d-u_2)D_2}>0,\\
T_3&=\frac{g(u_3)}{D_3},\\
T_4&=-\frac{g(u_4)}{D_4},\\
T_5&=\frac{g(u_5)}{D_5}.
\end{aligned}
\]

For \(T_1\) and \(T_3\), the \(c-u_i\) factors cancel from the corrected \(\lambda_+\) expressions. The gap \(T_4\) expression becomes
\[
-\frac{u_4(e-u_4)^2}{\lambda_+(f-u_4)D_4}.
\]
The exact \(z=e\) expression for \(T_5\) becomes \(g(u_5)/D_5\), both below and above \(e\), and vanishes at \(u_5=e\). These cancellations use the admitted nonzero open-region factors; \(u_4=c\) is treated separately.

Consequently,
\[
S=\sum_{i=1}^{5}\frac{g(u_i)}{H'(u_i)}
+T_2+\frac{g(u_2)}{D_2}.
\tag{3}
\]

The final positive term removes the fictitious negative \(O_+\)-baseline contribution at node \(u_2\); its actual minimum uses \(O_-\) and is the displayed positive \(T_2\).

To evaluate the complete five-node baseline, put
\[
R=\frac{f(f-e)^2}{\lambda_+}\ge0.
\]
The polynomial
\[
t(e-t)^2-f(e-f)^2
\]
vanishes at \(t=f\). Therefore there is a polynomial \(Q\), of degree at most two, such that
\[
g(t)=Q(t)+\frac{R}{f-t}.
\]

The imported Lagrange coefficient identity annihilates \(Q\):
\[
\sum_i\frac{Q(u_i)}{H'(u_i)}=0.
\]

Evaluating the Lagrange interpolation of the constant polynomial at \(f\) also gives
\[
1=\sum_i\frac{H(f)}{(f-u_i)H'(u_i)},
\]
hence
\[
\sum_i\frac{1}{(f-u_i)H'(u_i)}=\frac1{H(f)}.
\]

It follows that
\[
\boxed{
\sum_i\frac{g(u_i)}{H'(u_i)}
=\frac{R}{H(f)}
=\frac{f(f-e)^2}{\lambda_+H(f)}.
}
\tag{4}
\]

Because \(f>u_5\), every factor of \(H(f)\) is positive. Combining (3) and (4) proves (1). Removing \(T_2\) from (3) proves (2).

The last term in (2) is strictly positive because
\[
0<u_2<b<c<e,\qquad f>u_2.
\]
The residue term is only required to be nonnegative. In the allowed equality \(f=e\), it vanishes, but the other displayed terms still provide strict positivity.

Finally, \(C>0\), so the original normalized pairing satisfies
\[
P=CS>0.
\]
Every admissible odd-value choice has pairing at least this pointwise minimum, within the explicit normalized model.

## 5. Boundary and extension routing

### Actual value at \(u_4=c\)

When \(u_4=c\) is admissible,
\[
E(u_4)=0,
\]
so the actual \(T_4\) minimum is exactly zero. The fictitious rational baseline contributes
\[
\frac{g(c)}{H'(c)}=-\frac{g(c)}{D_4}<0.
\]

The actual full minimum at the boundary is therefore the right-hand side of (1) **plus**
\[
\frac{g(c)}{D_4},
\]
and is strictly positive.

This is an actual zero-term replacement—not an assertion that the canceled negative gap expression remains exact at the boundary.

### Every \(u_5\in(d,f)\)

Identity (4) is established at the universally quantified nodes and requires only \(f>u_5\). It uses their actual \(H'\)-factors throughout the permitted region.

- At \(u_5=e\), the exact \(T_5\) is zero and \(g(e)=0\).
- For \(e<u_5<f\), the exact minimum uses \(O_+\) and equals the same positive \(g(u_5)/D_5\).

No inequality is transported from a different node configuration. The old \(z=d\) negative bound is never used.

### Already-paid band

For \(c<u_4<d\), retain the actual positive table term \(T_4^{\mathrm{band}}\) and define
\[
B_4=T_4^{\mathrm{band}}+\frac{g(u_4)}{D_4}>0.
\]
The exact full identity becomes
\[
S=\text{right-hand side of (1)}+B_4.
\]

At \(u_4=c\), the same statement holds with the actual zero value for \(T_4\). This records how the actual term replaces the negative rational-baseline term; it is **not counted as a new proof** of the previously paid band \((0,c,e)\) vertex.

No uniform positive lower bound as nodes coalesce is asserted. The result is pointwise strict positivity at every allowed distinct-node configuration.

## 6. Claim dispositions and preserved residual

### SUPPORTED by this written derivation — UNREVIEWED AUTHOR CANDIDATE

- The full gap \((0,c,e)\) positivity identity (1).
- Its stronger coupled inequality (2).
- Its actual-value routing at \(u_4=c\), \(u_5=e\), and \(u_5>e\).

### INCONCLUSIVE / unchanged here

The other six gap full vertices:
\[
(0,b,d),\quad(0,c,d),\quad
(a,b,d),\quad(a,b,e),\quad(a,c,d),\quad(a,c,e).
\]

All six previously unclosed band full vertices:
\[
(0,b,d),\quad(0,c,d),\quad
(a,b,d),\quad(a,b,e),\quad(a,c,d),\quad(a,c,e).
\]

The two adopted gap first-pair dominations remain partial comparisons where their other negative terms are unpaid. RI1–RI4 are not proved here. RI5 remains uniformly impossible in its stated band region and is not used.

No other placement, annihilator word, six-node case, or \(m7/m8\) case is eliminated. The adopted seven-gap/six-band frontier is **not administratively changed** by this author candidate. If the result is subsequently adopted, exactly this one gap vertex can be removed from that inventory.

### Not established

- Actual-member certificate reduction to normalized vertices.
- Any six-node exclusion or existence theorem.
- A six-node certificate.
- Unrestricted common-numerator synthesis.
- Any \(m7/m8\) theorem.
- Novelty, external-family, human or formal/kernel acceptance.

## 7. Self-findings and final disposition

**Self-findings: 0 FATAL / 0 MAJOR / 0 MINOR detected in the stated candidate.** This is a self-check, not independent review. Existing adverse source/process findings are not withdrawn or reassessed.

**Overall correctness:** correct at the explicitly stated normalized-model scope, as an **UNREVIEWED AUTHOR CANDIDATE**.

The resolvent identity couples the full node sum and pays one genuinely unpaid gap vertex uniformly over its complete node and leading-scale region. No wider mathematical or acceptance conclusion is claimed.

**Confidence in the written identity and stated scope: 0.99.**