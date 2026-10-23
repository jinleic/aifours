VERDICT: **ACCEPT-WITH-FIXES**

Per-file: **W4 — ACCEPT-WITH-FIXES; NOBC — ACCEPT; NOLP — ACCEPT-WITH-FIXES.** All four SHA-256 values match.

No FATAL or MAJOR finding.

- **MINOR — [proof-W4.md:60](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c3-inputs-v1/inverse-run-count/mixdef-high/c2/proof-W4.md:60):** Explicitly require \(c\notin\{z_1,z_2\}\). Literally, “not adjacent to either” includes the zeros themselves. Fix: exclude both zeros and their neighbours; at most six aligned positions are excluded, giving the claimed \(p-2\).
- **MINOR — [proof-NOLP.md:45](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c3-inputs-v1/inverse-run-count/mixdef-high/c2/proof-NOLP.md:45):** Restrict “a phi-independent certificate … must use integrality” to certificates using this lifted constraint system. Real feasibility excludes contradictions from that relaxation; it does not classify every possible proof method.

## What is established

- **W4:** Every listed lambda value, including complements and interval endpoints, is correct. Conditions (A)/(B) hold throughout, including \(p=11,13\) and the overlapping boundary regimes. Lemma L applies; the stated total range forces \(X_{[k]}=p\). The bounds \(p+1\), \(p-2\), and \(p+2\), and all three final cases, are valid. The theorem’s prose matches \(W(p,4)\).
- **NOBC/AV:** Both per-part bounds and the extra \(1/5\) loss are correct. Thus every partition fails BC condition (a), covering every certificate shape in the quoted statement. AV’s induction, averaging, and \(p=11\) contradiction are correct.
- **CORE/NOLP:** Lifting and both directions of CORE are correct under the stated hypotheses. The real point satisfies every proper-pattern inequality: the two anti-run cases \(e=0,1\) cover all patterns, irrespective of block count.
- Independent computations checked W4 formulas/certification through \(p=199\) and 13,545,524 NOBC/NOLP pattern-type cases. The general conclusions follow from the written inequalities.

## What is imported/unchecked

The imported H representation is
\[
u_Q\notin[1-\lambda(Q^c),\,\lambda(Q)-1]\pmod p,
\]
with additive zero-sum half-jumps and the stated empty/full-pattern condition. Singleton-lift existence and the quoted BC Claim follow correctly from this interval exclusion.

NOBC imports BC’s requirement that certificates are ordered partitions with total lambda at least \(p+1\); its exclusion is correct **given that statement**.

`proof-PAR-K0.md` and `repr-WAS.md` are absent. Their upstream equivalence with ordered group products, the complete original BC statement, and the archived computational receipts were not independently certified.