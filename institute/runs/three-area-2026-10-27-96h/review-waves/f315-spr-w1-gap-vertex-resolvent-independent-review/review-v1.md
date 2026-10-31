# Independent written review — f315 W1 gap-vertex resolvent identity

## 1. Verdict and delivery

**Mathematical disposition: SUPPORTED at the explicit normalized-model scope.**

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR in the f310 candidate’s stated mathematical claims.**

The full gap \((0,c,e)\) identity, its stronger coupled inequality, and its stated boundary corrections are correct. The proof retains the node and leading-scale factors, replaces the inadmissible node-2 baseline contribution correctly, and evaluates the entire sum at the same universally quantified node configuration.

This is **not** an actual-member reduction, six-node exclusion or certificate, unrestricted common-numerator synthesis, or \(m7/m8\) result.

The working-tree ACK write was refused. No bypass was attempted; this complete body is returned for parent materialization as the wave’s `review-v1.md`.

## 2. Binding, complete reading and process qualifications

Live metadata hashing matched:

- **Manifest:** `f73af928baccd1a0c65935c281614c68a0b999f8ef52daa173aa7b692c59a439`
- **Freeze receipt:** `fea3cb45f60871c3108f2615de355ec8619b95f28f912f9745107cf124192e28`
- **Literal packet:** `32d3cdfb1764b746b674d03f88efa652ab15e04b05a62f24e3cbac40ed4aae31`

All five source hashes and all six original status-control hashes also matched the manifest.

Before opening the mathematical packet, I read the complete manifest, freeze receipt and six status-only controls. Following the fresh native-clock observation **2026-10-30T07:37:08-0700 PDT**, I attempted the authorized wave ACK write; the tool refused that path. I then recorded an explicit PRE-BODY ACK in `local://f315-reviewer-prebody-ack-v1.md`, before all mathematical packet reads.

**Actual direct parent receipt occurred later, after packet reading and reconstruction.** It is not backdated as a delivered pre-body ACK. The parent’s subsequent reconciliation record, SHA `6591e467a575705f56cce1cbaa23e393c07474436218fc9a11d1d9463e7dbe79`, was read completely and its live hash matched. It classifies this as an administrative ACK-transport qualification, not by itself contamination or proof invalidity. That record supplied no mathematical premise.

After the local ACK, I read the complete packet sequentially in raw windows of at most 20 LF: \(1\!-\!20,\ldots,881\!-\!900\), followed by \(901\!-\!907\), displaying the final `S5|43` ending. Coverage was:

| Frozen source | Complete displayed coverage | Live source SHA-256 |
|---|---:|---|
| S1 — f310 author candidate | Logical lines 1–292; 291 LF | `7353391511acea69436e8e76f5999e2d73d95ddf46999e88f0e826669cae7a34` |
| S2 — adopted corrected f308 disposition | LF 1–38 | `ab7debb56facd94151e8d696da8c28d6c4410b79806f244ce4567508e75d91c2` |
| S3 — full f308 written review | Logical lines 1–504; 503 LF | `198880d97e1ff03fc8e4c2cdb274d04c2a26c06b0ab14cf91cb64065b0c50ee3` |
| S4 — node-order/scale erratum | LF 1–27 | `1b2802e2aa65bdb3100c7ee5697a280c3089b555851de9709ddb9661089b243b` |
| S5 — original consolidated table | LF 1–43 | `5187883349994d17b06f0d74e773026ef45edcc08998cfbaa7f2eaa1054f04a2` |

No elision occurred. The packet was not independently regenerated; byte-roundtrip assertions remain receipt assertions.

A scratch checkpoint incorrectly described an additional “non-LF logical line907.” That wording was promptly withdrawn by `local://f315-reviewer-checkpoint-addendum-v1.md`; the accurate statement is complete displayed coverage through the final `S5|43` ending. Source bytes were not changed.

Fresh observations:

- Completed packet-read observation: **2026-10-30T07:42:30-0700 PDT**.
- Substantive reconstruction checkpoint: **2026-10-30T07:44:36-0700 PDT**.
- Completed-review clock: **2026-10-30T07:46:40-0700 PDT**.

No scientific executable, code, CAS, interpreter, solver, enumeration, replay, selected mathematical instance or parameter, independent-model CLI, build, lint, test or formatter was used. Machine operations were metadata hashing and native-clock observations. Quarantines and historical execution records were status-only NONINPUT; no held payload or excluded transcript was opened. These statements are not a clean-cognition or continuous-supervision certificate.

## 3. Exact imports and acceptance boundary

The load-bearing framework is:

1. **S2 LF 7–11; S3 LF 97–159:** the five-node moment definition, annihilator normalization and explicit normalized even pairing.
2. **S4 LF 7–15:** the corrected class/node placements and positive-leading envelope convention.
3. **S2 LF 23, 27–32; S3 LF 161–336:** the corrected endpoint and boundary interface. These corrections govern the original S5 table.
4. **S5 LF 13–23:** the original formulas, used only under that corrected interface.

The classical interlacing/class/genericity framework underlying the placements is an import, not independently reconstructed from external sources here. The five-node linear algebra, the relevant endpoint formulas, rational division, interpolation identity, full coupled sum and required boundaries are reconstructed below.

The prior at-most-five-frequency exclusion is documentary background at its already adopted compact independent monic septic-box scope. It is neither needed nor reproved here. References to that theorem inside earlier packets do not constitute a new reading or extension of its original source.

## 4. Normalization and every \(H'\)-sign

Assume the candidate’s marker and node orders:
\[
a\le b<c\le d<e\le f,\qquad
0<u_1<a<u_2<u_3<b<u_4<d<u_5<f.
\]
The open gap additionally imposes \(u_4<c\).

Let
\[
H(t)=\prod_{j=1}^{5}(t-u_j),\qquad D_i=|H'(u_i)|>0.
\]
There are exactly \(5-i\) negative factors in
\[
H'(u_i)=\prod_{j\ne i}(u_i-u_j),
\]
so
\[
\operatorname{sgn}H'(u_i)=(+,-,+,-,+).
\]

For the four zero odd moments,
\[
\sum_i u_i^r y_i=0,\qquad r=0,1,2,3,\qquad y_i=\mu_i u_iO_i,
\]
comparison of the \(t^4\) coefficient in Lagrange interpolation gives
\[
\sum_i\frac{p(u_i)}{H'(u_i)}=0
\quad(\deg p\le3).
\]
The four-row Vandermonde matrix has rank four. Therefore
\[
y_i=\frac{C}{H'(u_i)},\qquad
\mu_i=\frac{C}{u_iO_iH'(u_i)}.
\]
With the required nonzero odd signs \((+,-,+,-,+)\), positive weights give \(C>0\).

For
\[
E(t)=(-t)(c-t)(e-t),\qquad F(t)=-t(b-t)(e-t),
\]
the pairing is
\[
P=C\sum_i
\frac{-E(u_i)(b-u_i)(e-u_i)}{O_iH'(u_i)}.
\]
The node factor in the weight cancels against \(F\), but the remaining factor from \(E\) does not disappear. Writing
\[
K_i=\frac{E(u_i)F(u_i)}{u_iH'(u_i)}
=\frac{u_i(c-u_i)(b-u_i)(e-u_i)^2}{H'(u_i)},
\]
the normalized contribution is \(K_i/O_i\).

This confirms the normalization used in S1 LF 126–151 without importing four-node weights or losing a node factor.

## 5. Actual worst endpoints at \((0,c,e)\)

Use
\[
O_-(t)=\lambda_-(a-t)(d-t)(e-t),\qquad
O_+(t)=\lambda_+(b-t)(c-t)(f-t),
\]
with \(\lambda_-\ge\lambda_+>0\), under the imported envelope interpretation.

For \(K/O\), the derivative in \(O\) is \(-K/O^2\). Endpoint selection therefore depends on \(K\), together with the required sign of \(O\).

In the open gap, the relevant signs and minimizing endpoints are:

| Node | Sign of \(K_i\) | Required sign of \(O_i\) | Minimizing endpoint |
|---|---:|---:|---|
| \(u_1\) | \(+\) | \(+\) | \(O_+\) |
| \(u_2\) | \(-\) | \(-\) | \(O_-\) |
| \(u_3\) | \(+\) | \(+\) | \(O_+\) |
| \(u_4\) | \(+\) | \(-\) | \(O_+\), which is strictly negative here |
| \(u_5\ne e\) | \(+\) | \(+\) | \(O_+\) |

At \(u_5=e\), \(K_5=0\), and the term is zero for every admissible nonzero \(O_5\).

Define
\[
g(t)=\frac{t(e-t)^2}{\lambda_+(f-t)}.
\]
Direct substitution gives
\[
T_1=\frac{g(u_1)}{D_1},\qquad
T_3=\frac{g(u_3)}{D_3},\qquad
T_4=-\frac{g(u_4)}{D_4},\qquad
T_5=\frac{g(u_5)}{D_5},
\]
and
\[
T_2=
\frac{u_2(c-u_2)(e-u_2)(b-u_2)}
{\lambda_-(u_2-a)(d-u_2)D_2}>0.
\]
All displayed factors determining this last positivity have the required strict signs.

These are exactly S1 LF 126–142, including the different leading scales.

### The node-2 baseline is not physically admissible

At \(u_2\), \(O_+(u_2)>0\), whereas W1 requires \(O_2<0\). Thus the formal contribution
\[
\frac{g(u_2)}{H'(u_2)}=-\frac{g(u_2)}{D_2}
\]
must not be treated as an admissible odd endpoint or positive-weight atom.

S1 LF 146–151 correctly uses it only as an algebraic baseline, then removes and replaces it:
\[
S=\sum_i\frac{g(u_i)}{H'(u_i)}
+T_2+\frac{g(u_2)}{D_2}.
\]
The correction has the correct positive sign.

## 6. Rational division, interpolation and full coupled positivity

Put
\[
R=\frac{f(f-e)^2}{\lambda_+}\ge0.
\]
The exact polynomial factorization is
\[
t(e-t)^2-f(f-e)^2
=(t-f)\bigl[t^2+(f-2e)t+(f-e)^2\bigr].
\]
Consequently
\[
g(t)=Q(t)+\frac{R}{f-t},
\qquad
Q(t)=-\frac{t^2+(f-2e)t+(f-e)^2}{\lambda_+}.
\]
Thus the rational term has the **plus** sign claimed in S1 LF 153–164. Its residue is strictly positive when \(f>e\), and zero when \(f=e\).

Because \(\deg Q\le2\),
\[
\sum_i\frac{Q(u_i)}{H'(u_i)}=0.
\]
The interpolation formula for the constant polynomial, evaluated at \(f\), is
\[
1=\sum_i\frac{H(f)}{(f-u_i)H'(u_i)}.
\]
Since \(f>u_5\), neither this evaluation nor its division by \(H(f)\) is singular, and
\[
\sum_i\frac{1}{(f-u_i)H'(u_i)}=\frac1{H(f)}.
\]
Therefore
\[
\sum_i\frac{g(u_i)}{H'(u_i)}
=\frac{f(f-e)^2}{\lambda_+H(f)}.
\]

Combining this with the actual node-2 replacement proves
\[
\boxed{
S=
\frac{f(f-e)^2}{\lambda_+H(f)}
+\frac{u_2(c-u_2)(e-u_2)(b-u_2)}
{\lambda_-(u_2-a)(d-u_2)D_2}
+\frac{u_2(e-u_2)^2}
{\lambda_+(f-u_2)D_2}>0.
}
\]

Every factor of \(H(f)\) is positive. The residue term is nonnegative, and both node-2 replacement terms are strictly positive.

Moreover, throughout the open gap \(T_4<0\), so
\[
\boxed{
T_1+T_3+T_5-|T_4|
=
\frac{f(f-e)^2}{\lambda_+H(f)}
+\frac{u_2(e-u_2)^2}
{\lambda_+(f-u_2)D_2}>0.
}
\]
This is the stronger coupled statement in S1 LF 99–112. It pays the negative fourth contribution before adding \(T_2\); it is not merely a first-pair comparison.

For each admissible configuration,
\[
P/C\ge S>0,\qquad C>0.
\]
This establishes \(P>0\). It does not require \(C\) to be fixed while odd values vary, or assert a configuration-independent minimum for the unnormalized pairing.

## 7. Admissibility, boundaries and open endpoints

### 7.1 \(u_4=c\): actual zero versus continued bound

This boundary requires \(c<d\), because the standing node order requires \(u_4<d\).

Here
\[
E(c)=0,
\]
so the actual fourth contribution is exactly zero for every admissible nonzero negative \(O_4\). One must not substitute the inadmissible endpoint \(O_+(c)=0\) into the original quotient.

The rational baseline still contributes
\[
\frac{g(c)}{H'(c)}=-\frac{g(c)}{D_4}<0.
\]
Hence the actual boundary minimum is the displayed full-sum formula **plus**
\[
\frac{g(c)}{D_4}>0.
\]
S1 LF 206–223 makes this distinction correctly. The canceled negative gap expression is a continued lower bound, not the exact boundary value.

### 7.2 \(u_5=e\)

This boundary is possible only if \(e<f\). Since \(F(e)=0\), the actual fifth contribution is zero. For this vertex, \(E(e)=0\) as well, and
\[
g(e)=0.
\]
Thus the exact fifth term agrees with the baseline without any replacement correction. The positive endpoint \(O_+(e)\) is nonzero when this boundary is admissible.

### 7.3 \(e<u_5<f\)

Here
\[
E(u_5)<0,\qquad F(u_5)<0,\qquad H'(u_5)>0,
\]
so \(K_5>0\). Also
\[
O_-(u_5)<0<O_+(u_5).
\]
Over the required positive odd values, the minimum remains at \(O_+\), giving exactly
\[
T_5=\frac{g(u_5)}{D_5}>0.
\]

The complete interpolation identity uses the actual \(H\) and \(H'\) of these same nodes. No inequality is transported from a different \(u_5\) configuration. The old negative \(z=d\) expression is neither used nor mistaken for the exact minimum.

### 7.4 \(f=e\)

At the formal boundary \(f=e\), the node order forces \(u_5<e\); neither \(u_5=e\) nor \(u_5>e\) is then admissible. The rational function simplifies to
\[
g(t)=\frac{t(e-t)}{\lambda_+},
\]
a quadratic, and the residue vanishes. Therefore its complete five-node interpolation sum is zero. Nevertheless
\[
\frac{g(u_2)}{D_2}>0,\qquad T_2>0,
\]
so both claimed strict inequalities survive.

This algebraic boundary is not an assertion that a corresponding actual independent coefficient box exists. Under S4 LF 15’s literal coefficient-envelope convention,
\[
O_+(t)-O_-(t)
=\Delta_1+\Delta_3t+\Delta_5t^2+\Delta_7t^3,
\qquad \Delta_j\ge0.
\]
If both envelopes vanish at the common positive root \(f=e\), all these widths vanish. The envelopes coincide, forcing their ordered roots to coincide, including \(a=b\), which is incompatible with \(a<u_2<u_3<b\). Thus the formal equality-case calculation does not manufacture an actual-member W1 configuration. This does not invalidate the algebraic identity.

### 7.5 Leading scales and other marker equalities

The calculation retains \(1/\lambda_-\) in the actual node-2 term and \(1/\lambda_+\) in the baseline and its correction. It does not assume monicity. Indeed, the identity itself uses positivity of the individual scales, not a comparison between them; their ordering remains part of the adopted envelope convention.

The strict node chain already forces \(a<b\). If \(c=d\), the open gap can still be read algebraically, but \(u_4=c\) and the open band are excluded by \(u_4<d\). No forbidden zero denominator is introduced by these interpretations.

### 7.6 Odd values approaching zero

At fixed admissible nodes:

- At \(u_2\), \(K_2<0\), and \(O_2\to0^-\) produces **positive** divergence.
- At \(u_3\), \(K_3>0\), and \(O_3\to0^+\) likewise produces positive divergence.
- For \(u_5>e\), the positive odd range touches zero, but \(K_5/O_5\to+\infty\).
- At \(u_4=c\), \(K_4=0\), and the actual term is identically zero for every allowed nonzero \(O_4\).
- In the open band \(c<u_4<d\), \(K_4<0\), so its allowed negative odd values approaching zero also produce positive divergence.

Thus no hidden negative singular direction invalidates the finite lower bounds. In the open gap, \(O_+(u_4)<0\) is separated from zero at each fixed configuration.

The proof is pointwise. It asserts no uniform lower bound under node coalescence, endpoint approach or scale variation. The excluded limit \(u_1=0\) is not silently incorporated as an additional zero-frequency atom.

### 7.7 Previously paid band

For \(c<u_4<d\), the actual fourth term is positive, whereas the formal baseline fourth term remains \(-g(u_4)/D_4\). Hence
\[
S=\text{displayed gap right-hand side}
+T_4^{\mathrm{band}}+\frac{g(u_4)}{D_4}.
\]
This confirms S1 LF 234–245. It records the correct replacement but does not count the already adopted band vertex as a new result.

## 8. Per-claim disposition

| Candidate claim | Exact S1 lines | Disposition |
|---|---:|---|
| Full open-gap \((0,c,e)\) identity and strict positivity | 81–97 | **SUPPORTED** |
| Stronger coupled inequality before adding \(T_2\) | 99–112 | **SUPPORTED** |
| \(H'\)-signs and actual endpoint terms | 121–142 | **SUPPORTED** |
| Removal and positive replacement of the fictitious node-2 baseline | 144–151 | **SUPPORTED** |
| Rational division, residue sign and Lagrange evaluation | 153–190 | **SUPPORTED** |
| Strict positivity when \(f=e\) | 192–196 | **SUPPORTED algebraically**, without actual-member realization |
| Exact boundary replacement at \(u_4=c\) | 206–223 | **SUPPORTED** |
| Exact routing at \(u_5=e\) and \(e<u_5<f\) | 225–232 | **SUPPORTED** |
| Already-paid-band replacement identity | 234–245 | **SUPPORTED**, not a new frontier closure |
| No uniform lower bound under degeneration | 247 | Correct limitation |
| Other unpaid vertices, actual-member reduction, six-node/global synthesis and \(m7/m8\) | 257–282 | **INCONCLUSIVE / unchanged** |

**REFUTED candidate claims: none at the stated scope.** The earlier source’s corrected scale, zero-separation, RI-clearing and residual-count errors remain historical findings; they are not reintroduced by f310.

## 9. Preserved residual and assurance ceiling

If the parent subsequently adopts this result, precisely the previously unpaid **gap \((0,c,e)\)** vertex can be removed from the existing inventory. This review does not itself change the ledger.

The other six previously unclosed gap full vertices remain:
\[
(0,b,d),\ (0,c,d),\ (a,b,d),\ (a,b,e),\ (a,c,d),\ (a,c,e).
\]
The six previously unclosed band full vertices remain the corresponding six listed in S1 LF 265–268. Previously adopted all-positive vertices and the two partial dominations retain only their earlier exact scopes.

No proof is supplied here of:

- actual-member certificate reduction to normalized vertices;
- closure of another unpaid full vertex;
- RI1–RI4 universally;
- a six-node exclusion, existence theorem or certificate;
- another annihilator word or placement;
- unrestricted common-numerator synthesis;
- any \(m7/m8\) theorem.

This is a same-harness written reconstruction using the expressly admitted earlier f308 return. It is not a blind, independent-model-family, human, formal/kernel, novelty or worldwide-status gate.

**Overall correctness: correct at the explicit normalized-model scope.**

The full coupled identity and all requested boundary distinctions are supported; no patch-introduced mathematical flaw was found. The administrative ACK-transport and scratch-ending-description qualifications remain disclosed without being converted into claims of mathematical contamination or clean provenance.

**Confidence: 0.99.**