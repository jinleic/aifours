# Erratum 1: reverse-inequality withdrawal for the zero-tail column packet

Owner **MathShor-2**. Native `/bin/date` before writing: **Thu Oct 29 00:26:04 PDT 2026**. This additive erratum applies to the immutable `frontier-20261029-zero-tail-column-gap-v1.md`, SHA256 `04c29222d328435797b095ae04ad68789538d7be2980f60641606f78dfa1f8a0`. Main was notified immediately before this record. No original bytes are edited.

## Finding and exact correction

The last inequality in original equation (2),

    n − 4 floor(n/c_0) >= n − 4 floor(n/M(n)),

is **false in general** under `c_0<=M(n)`: because `floor(n/c_0)>=floor(n/M(n))`, the inequality goes in the opposite direction. The claimed unconditional outside-head lower bound `N_out>=n−4 floor(n/M(n))` is hereby **WITHDRAWN**. In particular the inference of a large lower bound near n from an UPPER bound on `c_0` must not be accepted.

The first inequality

    N_out >= n − 4 floor(n/c_0)

is retained only as the separately written necessary row-packing implication, with actual SAME-D hypotheses; it is not strengthened using the upper bound on c0. A valid conditional consequence is: for any integer L with `L<=c_0`, `N_out>=n−4 floor(n/L)`; the trivial anchor lower bound `L=4` does not yield the withdrawn claim.

The candidate (1), namely the zero-tail-column necessary bound `c_0<=floor((n−12)/5)` for n>=175 and exactness for the isolated anchor-packing relaxation, is logically separate and **not withdrawn by this arithmetic finding**. Its 172-state identity, cyclic closure and actual-word packing remain entirely UNREVIEWED and require the originally requested disjoint scientific review. No independent correctness or adoption is implied by this erratum.

## Exact review and consumer boundary

All review packets and any downstream use must include the original frozen packet AND this erratum as a literal mandatory pair. No downstream result may use or quote the withdrawn outside-head inequality as established. The original packet's statement that (2) is a valid necessary consequence is false to the extent it includes the last inequality; its unaffected maximum and the first inequality must be assessed separately. Original unrestricted completion remains OPEN.

**END OF ERRATUM 1.**
