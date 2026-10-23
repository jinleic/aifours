# Sun M3(1,1): R1 and R2 residual instances are excluded

Recorded at 2026-10-19T13:38:03-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Written/model-reviewed relative to original-scope accepted R0, L0.1/Lagrange, E1, LFC/INV/E6/E7, VFC, L1 triangle rules and E3-a (Z11(a) only in the valid both-family (1,1) setting). Computer-assisted Sun(5)/Sun(6) remain transitive imports through the declared packages and class reduction. **M3(1,1) emptiness is not accepted here except as the stated conditional implication.**

## Exact class and conclusions

M3(1,1): K6.2*, V={d,i*} union O, |O|=5, e_d>=4,e*=2; the3-marker t lies in O with f_t>=2 and f*=1; every admissible5-marker placement and unbounded exponents/w-parts; (alpha_(d i*),alpha*_(d i*))=(1,1). Arbitrary groups with finite-index subgroups are covered by R0, including the explicit product-equality descent in erratumv2.

- **R2X:** no family y has its four entries y_tu (u in O minus {t}) all in {1,2}.
- **Theorem7, weaker RR:** an R1-instance (x;a,b), with distinct a,b in O minus {t}, x_ta=x_tb=4, Pi_t^x Pi_a^x=Pi_t^x Pi_b^x and x'_ta=x'_tb=2, would force x'_tu=2 for all four u in O minus {t}. Nothing about x'_(t i*)=2 is supplied by this theorem.
- **R1X:** no R1-instance exists, by Theorem7 and R2X.
- **NR:** every configuration of this exact class has neither R1 nor R2. This is a definition-level conjunction, not a new imported theorem.
- **M3E, CONDITIONAL:** IF the pending MK-v2 TheoremM3R proves every M3(1,1) configuration has an R1 or R2 instance, THEN M3(1,1) is empty. That classification is still pending; it is not discharged by this record.
- Supporting Lemmas1-4, Proposition5 and Lemma6 accepted at their printed scopes, narrowed re-proof labels and mandatory corrections. Proposition5(a) is an implication, not an existence assertion about its hypothesis.

## Evidence and reviews

[Proof](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/K62-R2MIX-v2.md) `b75e6dc7e72b8c0b1cd5388e8845a3bcd23854b0fbd83292fa6ff7c22ade0806`; original freeze `b9416d526dd2a7a4f3e260d9cbe5a7c54d9ab59f08403b074379d40439a6ebec`; corrected second-family freeze `897e23bb011a18038864eb041502050a201ee446a1e4f3cdc68d3e73f7964732`. Read [parent erratumv1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-R2MIX-parent-erratum-v1.md) `c8528a68d7923ddc677457354b177167c3f2f038571816ebe2195bb33cc5badf`, then [v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-R2MIX-parent-erratum-v2.md) `0626c5c5a94927ad0ef6b5fe2706a5e1cb61a150961b252a3b82417b9c9e4f97`.

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-R2MIX-codex-v1.prompt.stdout.txt) `e89a76f1c9bbbd7a419d9d48506aa952206b6d667fca31a6b5ff1dcf20309427`: gpt-6.1-sol/max/read-only, all principal derivations ACCEPT, packet0F/0M/3MINOR, disposed by v1.
- [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-R2MIX-claude-v2.prompt.note.md) `0fa4eb33e2fcec461eac9c4286ed7ff5214fa9f8f4292e3888800397410f355a`: claude-opus-5-5/max/no tools, principal derivations accepted,0F/0M/6MINOR, disposed by v2. No model review is a premise of the mathematics.

## Parent checks

The original freeze records the parent's whole-proof read and24source/hash-range checks. The parent re-derived the ordered product separation pa=qb^-1, translated/inverted family assignments, d-label gcd3 and cap3 for allmarkers, pair lower bounds n_d/4, the missing-own-fibre deficit1, tau/3 product cardinality, chain gcd6, and the certificate11/12>5/6. For the quotient addendum, pi(XY)=pi(X)pi(Y) preserves the R1 equality since N lies in both families; no normality of the original subgroups is assumed. These are written checks, not a finite computational or Lean replay.

## Remaining

The classification premise, M3(1,1) emptiness, M13/fullK6.2* candidates, fullK7 and Sun(7) are not accepted by this record. Pending M3R's stronger RR and R2N statements remain pending. No novelty, priority, human-referee or Lean claim. The new fullK6.2* packet has its own independent review and may later supersede this restricted status, never by automatic promotion.
