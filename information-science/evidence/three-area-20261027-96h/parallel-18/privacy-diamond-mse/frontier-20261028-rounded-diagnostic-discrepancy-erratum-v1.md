# Additive correction — source of the small-parameter diagnostic discrepancy is UNKNOWN

Native observation immediately before writing: `Wed Oct 28 17:49:16 PDT 2026`. This is an additive erratum to the frozen `frontier-20261028-euclidean-fourth-term-v1.md`, SHA `c95ed59c1d26fc0a1f2adbf514cc7645ca6a67a9446126d0af7b7f040207c7ab`; that predecessor remains unchanged and UNREVIEWED.

Its §6 described a difference between one earlier 70-digit run and the later 110-digit run as “a numerical-precision/bracketing sensitivity,” while also saying the exact origin was not isolated. The causal label is NOT established and should be read instead as **an unexplained transient diagnostic discrepancy**. I performed the following actual controlled follow-up at s=10^-8, recalculating all constants at each precision and varying bisection counts:

```text
precision= 70 bisections= 120 fourth_scaled= 1.636363542125
precision= 70 bisections= 160 fourth_scaled= 1.636363542125
precision= 90 bisections= 120 fourth_scaled= 1.636363542125
precision= 90 bisections= 160 fourth_scaled= 1.636363542125
precision= 110 bisections= 120 fourth_scaled= 1.636363542125
precision= 110 bisections= 160 fourth_scaled= 1.636363542125
```

I then recreated the originally stated 70-digit/120-bisection settings with its original pi literal and arctan stopping threshold; the actual output was again `1.636363542125`, NOT the earlier `1.638377523`. Thus changing precision or iteration count alone did not reproduce the earlier difference. The precise earlier cause remains UNKNOWN; I do not assume a clean runtime history or delete the anomalous output. The earlier number remains disclosed in the predecessor.

These are non-interval Decimal diagnostics only. They do not establish the value of the fourth coefficient, pay any original mathematical proof or source import, or certify absence of other numerical errors. The written fourth-term candidate and all of its unreviewed dependencies retain exactly their prior states.
