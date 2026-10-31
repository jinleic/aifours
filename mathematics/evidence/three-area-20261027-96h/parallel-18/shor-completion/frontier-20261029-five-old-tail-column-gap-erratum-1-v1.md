# Erratum 1: combined-state relaxation versus exact cyclic maxima

Owner **MathShor-2**. Native `/bin/date` before writing: **Thu Oct 29 00:28:33 PDT 2026**. This mandatory additive erratum applies to immutable `frontier-20261029-five-old-tail-column-gap-v1.md`, SHA256 `cbd43a32b240b5ff9fe2daa698de7c73691e12684283b2e9622f21620bdc498c`. No pinned bytes are edited.

## Correction of contradictory draft text

Original §3 lines 58–60 accidentally retained a discarded draft statement that §4 gives per-initial-mask outcomes and that such computations are essential to the claimed outside-tail **upper-bound** argument. This is false as a report of performed work: no per-initial-mask computation was made. The original §4 explicitly and correctly states that only the **combined initial-state / anchor-only wrap-veto relaxation** was computed. The original heading “Three exact cyclic-column maxima” and phrases calling M1/M2 exact computed maxima are overstrong and must not be relied on.

Read original §3 lines 58–60 instead as follows:

> For n>=175, process the first n−14 positions by the combined score map, then the last14 positions with wraparound vetoes only against the mandatory anchors. Every genuine cyclic column is represented by one allowed initial mask and obeys those anchor vetoes, so the calculated U_j is an upper bound on its true maximum. It may contain extra paths that conflict with a nonanchor initial bit. The same anchor-veto terminal map applies for n and n+5, and commutes with adding 1 to all scores. Hence the *combined* full-map identity (4) is sufficient for the upper-bound recurrence `U_j(n+5)=U_j(n)+1`; a per-mask replay is not needed for that limited claim. To establish exact cyclic maxima for C1/C2, a separately checked per-mask closure would indeed be required, but this packet does not claim or use that stronger result.

In equation (3), interpret M0,M1,M2 as the true individual cyclic maxima and use `M_j<=U_j`. Thus

    N_out^tail >= n − U_0(n) − U_1(n) − U_2(n) − 2 floor(n/5)

is the exact direction used by the proposed table. The C0 initial mask is unique, so its anchor-veto result is exact at that isolated packing level; C1/C2 are only upper relaxations. No calculated U-value is asserted feasible as a cyclic column or a D.

## Gate and scope

Any reviewer or consumer must read this erratum with the original packet and must independently verify the combined-state identities, base U-values, containment of all true cyclic paths in U, terminal-map recurrence, actual-word layer facts and table arithmetic. Until then the outside-tail table remains UNREVIEWED. The separate erratum on the earlier zero-tail packet remains binding; its withdrawn outside-head inequality is not used here. Original completion remains OPEN.

**END OF FIVE-COLUMN ERRATUM 1.**
