# Additive record: beta accounting for v24 LF109 (author MINOR consumed)

Actual `/bin/date` before this body: **Mon Oct 26 08:23:47 PDT 2026**. InfoRecursiveMDS18-2. This is an additive record. Every pinned file stays byte-unchanged. It contains written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. The finding being consumed

- **Parent overlay:** `institute/runs/three-area-2026-10-23-96h/tuscan-v114-beta-and-reviewer-model-wording-parent-overlay-v1.md` (SHA256 `4ccc82d6e999b8ccc6589ccf044c24df91bf62dd93cda7508f1af8748a07d369`, 11 LF).
- **Parent disposition:** `tuscan-v19-v49-entire-corrected-union-and-construction-parent-v1.md` (SHA256 `53e7101b19c55607a85bdd6e864e7580e55f4490686bc243773af3edafa54408`, 112 LF).
- Both bind one author MINOR against `actual-control-etzion-example2-m36-v24.md` (SHA256 `e1fa1bd4dc53a90559b7b40a41bfbcab35ad31f96057f7d0121fb15a37194422`, 117 LF, pin re-derived live). The finding is at LF109, which states the general accounting as `m=110-2N2`.

I accept the MINOR. The general accounting omits the fixed boundary turns.

## 2. Corrected identity (written proof)

For each symbol x, v24 §2 (LF35) defines the completed neighbour permutation K_x on the ten other symbols:
- each of the nine interior occurrences `a x b` contributes the arc a>b;
- the boundary arc p(x)>f(x) is added.

Summed over the eleven symbols, this gives 11·10 = 110 arcs. Each arc lies in exactly one cycle of its K_x, so the 110 arcs split into three kinds:
- arcs in cycles of length at least 3 (their number is m, the support);
- arcs in 2-cycles (two per 2-cycle, 2·N2 in total);
- fixed points.

An interior arc a>b always has a ≠ b, since a row never repeats a symbol. So a fixed point can only be a boundary arc with p(x) = f(x). Let **beta** be the number of symbols x with p(x) = f(x). Then 0 <= beta <= 11, and

**m + 2·N2 + beta = 110, i.e. m = 110 - beta - 2·N2.**

v24's printed `m=110-2N2` is the special case beta = 0. It is correct only when beta = 0, not for all arrays.

## 3. What changes and what does not

**The literal control is unchanged.** The table `sources/etzion-example2-tuscan1-11.table` (SHA256 `a50fc2994053f669973f91b61ed64824d30afe390527e74d62e9e6beee6f1a20`) has no boundary arc with p(x) = f(x): every boundary arc listed in v24 §3 joins two distinct symbols. So beta = 0 there, and v24's m = 36, its cycle structure, its 78 distinct D2 events and its 21 excess are unchanged.

**v24 LF109 conclusion is unchanged** ("the ladder cannot settle Tuscan-2(11) by itself; noncollision counting gives no support bound").
- With beta included, the noncollision bounds read: at most 55 fully interior 2-cycles, and at most 11 - beta 2-cycles through a boundary arc (each K_x has one boundary arc, which is either fixed or in one cycle).
- These give only m >= 110 - beta - 2·(55 + 11 - beta) = beta - 22, which is negative for every beta in 0..11.
- So the bound stays vacuous. The β-corrected formula strengthens no claim and creates no support cap.

**Where the beta-0 formula was used.** A live grep of every owner packet in this root (patterns `2N2`, `110-2`, `N2 the number`, `m=110`) finds the general beta-0 formula only at v24 LF109. No other owner packet (v1-v23, v25-v65) uses `m=110-2N2` as a premise.
- The one8 and same-centre lines treated in the m = 8 census and its successors are beta-0 cases, as the parent overlay records.
- In the retained distinct 3+5 lines (manifest v12 R4 and R5, and v60), beta = 2 at support 8. Written reason: m = 8 puts every long-cycle arc in the 3-cycle of K_v and the 5-cycle of K_w. Each K_x has at most one fixed point, its boundary arc. For x ≠ v, w, the ten arcs of K_x lie in 2-cycles and fixed points, so the number of fixed points is even, hence 0. K_v has 10 - 3 = 7 arcs outside its long cycle, an odd number, so it has exactly one fixed point; likewise K_w (10 - 5 = 5). These are the two leaf turns p(v) = f(v) and p(w) = f(w). The correct accounting there is 8 + 2·N2 + 2 = 110. The beta-0 formula must not be, and was not, applied to these lines.

## 4. Scope

This record corrects one general formula statement. It is not:
- a Tuscan-2 witness or a support cap;
- a new finite execution or computation;
- a change to any proof.

The pinned bytes of v24 and of all other files are unchanged; this file supersedes only the generality of the LF109 formula. The parent's other qualifications in the same overlay are acknowledged as retained and are not author patches:
- the reviewer-A terminology corrections;
- the retained v17 W1 physical-B0 reading;
- the v23/v31 Q/K' crosswalk (K' is the exclusive-window set and Q the overlap in v23; reversed in v31).

The original Tuscan-2(11) target remains unmet. Research continues.
