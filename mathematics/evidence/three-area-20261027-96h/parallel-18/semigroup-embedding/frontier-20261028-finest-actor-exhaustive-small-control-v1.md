# Exhaustive order-1–3 control for the pure-CS actor theorem

**Status: SAME-AUTHOR EXACT FINITE CONTROL; UNREVIEWED / UNADOPTED.** This supplements the universal candidates `frontier-20261028-finest-pure-cs-actor-v1.md`, SHA `772cf39e2d5c6aab1c127ed73edaf3e7c2e617deda8f3113b8059df19f4c83ab`, and `frontier-20261028-pure-cs-quotient-lattice-v1.md`, SHA `21646707ddc27c5fe4a9e6ab2dc2ec118661ed123e5cd8e800fc8b800c0d59bf`. It is not a proof of either theorem.

`frontier-20261028-finest-actor-small-semigroups-checker-v1.py`, SHA-256 `a6cbc617d2e8c3ad42b9cd4bbc8fdeaef299b068f15d59f9b746af71096c87d7`, ran in the Python eval kernel before Wed Oct 28 22:28:51 PDT 2026. It enumerates every labelled multiplication table on 1,2,3 elements; checks associativity and regularity; derives the full idempotence-context congruence; filters only cases whose actual quotient is pure and CS; and exhausts all source set partitions as candidate congruences. For each filtered source it independently computes every pure CS quotient, the finest row/column relations and their q-fibre Bell-product count; verifies the constructed finest kernel is pure and CS and refines all the enumerated pure-CS kernels; and checks its Rees row×group×column size.

Observed cumulative counts:

```text
order≤1: associative=1, regular=1, pure-CS actual q=1, quotient lattices checked=1
order≤2: associative=9, regular=7, pure-CS actual q=7, quotient lattices checked=7
order≤3: associative=122, regular=57, pure-CS actual q=51, quotient lattices checked=51
```

The 51 cases include relabellings and all have orders at most3. This control can falsify errors in the finite statements at those orders; it does not cover arbitrary/infinite semigroups, reproduce the written general proof, certify the all-actor band lift, or establish novelty. The checker shares this author's implementation and needs independent review.
