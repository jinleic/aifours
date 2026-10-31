# The original source class as a pure-CS actor condition

**Status: WRITTEN CONDITIONAL INTERFACE; UNREVIEWED / UNADOPTED.** This is a source-class reformulation, not an embedding theorem. Its forward implication depends on the named SQ-E source reconstruction and is not newly claimed proved here.

For a regular locally r-orthodox semigroup S, the following are equivalent **provided the named SQ-E input is correct**:

1. S is weakly E-unitary in the full printed natural order (`a=eb=bf` with possibly different idempotent witnesses).
2. The actual idempotence-context syntactic quotient `S/τ` is completely simple.
3. S has an onto idempotent-pure homomorphism to some completely simple semigroup.

1⇒2 is the exact SQ-E input reconstructed in `frontier-20261028-cryptogroup-band-retraction-v1.md`, SHA `28432c0960893c0c79dda307288c975795489678b9ab4e2eb2e48aef688bbb0d`, §2.1; its acceptance is a separate review obligation. For all regular S, 2⇔3 and 2⇒1 follow from `frontier-20261028-syntactic-purity-all-regular-v1.md`, SHA `20b839e181bc4fff3655cc22cf07675357c0e4ddedb2998fdd1949642d1c1714`, without the local-r assumption: actual q is automatically pure; any pure CS map induces q as a CS image; and CS natural order is equality.

Thus, after the original local-r hypothesis is fixed, the user-facing source-class input to the finest-actor/SEP interface can be stated as the single condition `S/τ is CS`. The remaining problem is still whether its canonical seminormal-band coordinates separate all intrinsically actor-indistinguishable idempotents; no separation or embedding is inferred here. The erroneous four-element weak-E false alarm was withdrawn; the mandatory natural-order correction is `frontier-20261028-natural-order-weu-audit-erratum-v1.md`, SHA `801f699bb640bd1e58eed095779c05b882e7d9eddd0ea1c470b522ecbc345c28`.
