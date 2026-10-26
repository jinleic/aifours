# Written closure of the pinned one-three-switch neighborhood v1

Clock actually observed before creation: **2026-10-23T15:32:08-0700**. Status **CANDIDATE / WRITTEN ONLY / PARTIAL FOR T2(11) / NOVELTY_UNCLEAR**. No program, scientific arithmetic cell, solver, import, compilation, CNF generation or executable control/check ran. The permutation tables below are written finite derivations and need actual independent and parent reconstruction.

## 1. Exact scope and why the proposed assay is now unnecessary

This closes the EXACT neighborhood proposed in `admission-request-three-switch-v1.json`: start from the twelve-symbol Hamilton-cycle decomposition obtained by appending11 to each row of the pinned Etzion1991 Tuscan-1(11); choose any two of its11 Hamilton rows; exchange successors on ONE length3 cycle of their relative permutation; retain only switches preserving both Hamilton rows; try every add-zero root.

**None yields T2(11).** This is NOT unrestricted Tuscan11 nonexistence. Longer relative cycles, unions of cycles, a second switch, other decompositions, and other construction mechanisms remain outside this claim.

Source table: `sources/etzion-example2-tuscan1-11.table`, SHA-256 `a50fc2994053f669973f91b61ed64824d30afe390527e74d62e9e6beee6f1a20`. Its full primary image/cutting proof are in `unrestricted-defect-orbit-candidate-v1.md` (`18dc11903db8b217cfb4b8517cbda600a5e4cbd5d8892bc36ddc1c40859779ae`). The printed star is0. Row labels here are **one-based printed row numbers1,...,11**; symbol11 is the new adjoined root.

The exact switch criterion is `three-edge-switch-criterion-v1.md`, SHA-256 `121c44c5d14613e336f2e39b0ccdfbd26cd5b9cc669bcf51a5e4ede6b9c903d8`. Actual successor exchanges are also expanded below, so the conclusion does not depend on using the orientation criterion as an unexplained black box.

The assay request and unexecuted source are superseded and should remain permanently HOLD. The parent's static graceful-settlement findings in `three-switch-neighborhood-v1.py` are accepted: signal handling before the protected region and throwing handlers during final receipt can interrupt settlement. Those defects were not repaired or tested; **no runtime PASS is claimed**. Since the exact mathematical neighborhood is closed in writing, no unused runtimev2 is needed for this scientific question.

## 2. Unchanged-fault support forces either row2 or row5 to change

In the original twelve-symbol cycles, these four paths share endpoints11→2:

- `(11,10,2)` in row3;
- `(11,8,2)` in row5;
- `(11,6,2)` in row7;
- `(11,3,2)` in row10.

These three share endpoints1→5:

- `(1,3,5)` in row2;
- `(1,6,5)` in row5;
- `(1,11,5)` in row4.

Centers in each list are distinct. The root-fault theorem says three unchanged paths force a good root to be an endpoint; two unchanged paths force it into the four-element endpoint-plus-centers set. Creating extra paths cannot remove a constraint supported by unchanged paths.

**Lemma1 (all two-row changes, not only3-switches).** A modified Hamilton decomposition differing from the source in at most two rows can have a good root only if the changed row pair contains row2 or row5.

*Proof.* Suppose neither row2 nor row5 changes.

- If row4 also does not change, all three1→5 paths remain. A good root must be1or5. At most two of the four11→2 paths can have changed, leaving at least two whose centers belong to `{10,8,6,3}`. Their four-element fault set contains neither1nor5. Contradiction.
- If row4 changes, only one other row can change. At least three11→2 paths remain, forcing a good root to be11or2. The two unchanged1→5 paths centered at3and6 force it into `{1,5,3,6}`, disjoint from `{11,2}`. Contradiction.

Thus every other pair is ruled out by preserved witnesses, irrespective of how its outgoing edges are reassigned. ∎

There are only19 unordered pairs touching row2or5. This is a necessary-support reduction, not an assumption that other rows cannot be changed in a larger-radius construction.

## 3. Raw successor data for reproducibility of the written table

Let P_r be the successor permutation of printed rowr after appending11. The entries below are `P_r(0),...,P_r(11)`:

|r|Successor vector|
|---:|---|
|1|6,2,3,4,5,0,7,8,11,10,1,9|
|2|1,3,11,5,6,7,8,9,10,2,0,4|
|3|7,4,5,6,0,8,9,11,3,1,2,10|
|4|2,11,6,7,8,9,10,4,1,0,3,5|
|5|11,6,7,0,9,10,5,1,2,3,4,8|
|6|3,7,8,9,10,6,11,2,0,4,5,1|
|7|9,8,0,10,7,1,2,3,4,5,11,6|
|8|4,9,10,8,1,11,3,0,5,6,7,2|
|9|10,0,9,1,2,3,4,5,6,11,8,7|
|10|5,10,1,2,11,4,0,6,7,8,9,3|
|11|8,5,4,11,3,2,1,10,9,7,6,0|

In particular

`P_2^(−1)=(10,0,9,1,11,3,4,5,6,7,8,2)`,

`P_5^(−1)=(3,7,8,9,10,6,1,2,11,4,5,0)`.

These give the relative permutations by a direct lookup, fixing the composition order and avoiding any hidden numerical convention.

## 4. Complete nineteen-case relative-cycle table

For pairs involving row2, the table lists `P_2^(−1)∘P_j`. For the remaining pairs involving row5 it lists `P_5^(−1)∘P_j`. Reversing the order of the two rows inverts this relative permutation and leaves its cycle supports unchanged; exchanging successors on a support is the same physical switch in either convention.

|Anchor, j|Full relative cycle decomposition|
|---|---|
|2,1|(0 4 3 11 7 6 5 10)(1 9 8 2)|
|2,3|(0 5 6 7 2 3 4 10 9)(1 11 8)|
|2,4|(0 9 10 1 2 4 6 8)(3 5 7 11)|
|2,5|(0 2 5 8 9 1 4 7)(3 10 11 6)|
|2,6|(0 1 5 4 8 10 3 7 9 11)(2 6)|
|2,7|(0 7 1 6 9 3 8 11 4 5)(2 10)|
|2,8|(0 11 9 4)(1 7 10 5 2 8 3 6)|
|2,9|(0 8 4 9 2 7 3)(1 10 6 11 5)|
|2,10|(0 3 9 6 10 7 4 2)(1 8 5 11)|
|2,11|(0 6)(1 3 2 11 10 4)(5 9)(7 8)|
|5,1|(0 1 8)(2 9 5 3 10 7 11 4 6)|
|5,3|(0 2 6 4 3 1 10 8 9 7)(5 11)|
|5,4|(0 8 7 10 9 3 2 1)(4 11 6 5)|
|5,6|(0 9 10 6)(1 2 11 7 8 3 4 5)|
|5,7|(0 4 2 3 5 7 9 6 8 10)(1 11)|
|5,8|(0 10 2 5)(1 4 7 3 11 8 6 9)|
|5,9|(0 5 9)(1 3 7 6 10 11 2 4 8)|
|5,10|(0 6 3 8 2 7 1 5 10 4)(9 11)|
|5,11|(0 11 3)(1 6 7 5 8 4 9 2 10)|

Each line covers all twelve tails. As a parity consistency check in writing, all these relative permutations are even, as required by composing two twelve-cycle successor permutations. The only length3 supports in the complete eligible table are

`{1,8,11}` at pair{2,3};

`{0,1,8}` at pair{1,5};

`{0,5,9}` at pair{5,9};

`{0,3,11}` at pair{5,11}.

No program produced this table. It is an explicit finite written case table, not a statement that a native enumeration or proof checker completed.

## 5. Expand the four actual switches

For each support, exchange the two rows' successors exactly at those three tails.

### Pair{2,3}, support{1,8,11}

The switched row3 splits as

`(0 7 11 4)(1 3 6 9)(2 5 8 10)`.

The switched row2 is the twelve-cycle

`(0 1 4 6 8 3 5 7 9 2 11 10)`.

Since row3 is not Hamilton, this switch cannot produce an admissible decomposition.

### Pair{1,5}, support{0,1,8}

The switched row1 is

`(0 11 9 10 1 6 7 8 2 3 4 5)`.

The switched row5 splits as

`(0 6 5 10 4 9 3)(1 2 7)(8 11)`.

Again the switch is not Hamilton on both rows.

### Pair{5,9}, support{0,5,9}

Both switched rows are Hamilton:

`P'_9=(0 11 7 5 10 8 6 4 2 9 3 1)`,

`P'_5=(0 10 4 9 11 8 2 7 1 6 5 3)`.

### Pair{5,11}, support{0,3,11}

Both switched rows are Hamilton:

`P'_(11)=(0 11 8 9 7 10 6 1 5 2 4 3)`,

`P'_5=(0 8 2 7 1 6 5 10 4 9 3 11)`.

This last case reproduces, when cut at11, exactly the already-derived nontrivial row5/row11 rotation state of the preceding defect-orbit packet. That independently derived identity is a useful self-consistency anchor for the composition/sign convention, not an independent model review or executable check.

## 6. Both Hamilton cases have no good root

For either remaining pair{5,9} or{5,11}, rows3,7and10 are unchanged. They retain the three11→2 paths centered at10,6and3, so every good root would lie in `{11,2}`.

Rows2and4 are also unchanged. The paths `(1,3,5)` and `(1,11,5)` force every good root into `{1,5,3,11}`. Intersecting leaves only **root11**.

Finally rows4and6 are unchanged and contain

`(7,4,8)` in row4,

`(7,2,8)` in row6.

Root11 is neither an endpoint nor either center, so both survive as repeated linear distance2 events7→8 after cutting at11. Thus root11 fails too.

This proves the claimed no-hit for ALL single-relative-3-cycle switches of the original pinned decomposition: pairs outside the nineteen eligible pairs are excluded by unchanged witnesses; the nineteen-case table has only four3-cycle supports; two fail Hamiltonicity and the other two fail every root. ∎

## 7. Scientific and operational disposition

This is a completed written radius1 route-closure candidate, not a full answer to the active Tuscan-2(11) problem and not a solver certificate. It needs actual separate in-harness plus parent reconstruction at these bytes. Novelty remains unclear; the original source and all standard graph/permutation ingredients are prior art.

`admission-request-three-switch-v1.json` and `three-switch-neighborhood-v1.py` are preserved as **superseded, never executed, permanently HOLD**. The static graceful-settlement gaps reported by the parent remain explicitly unfixed in that historical source; no compile/test/replay is used to confirm or deny them. The older deletion assays remain permanently HOLD and the unrestricted encoder remains PREPARE/not admitted. No scientific process needs settlement because none was launched.

The exact missing input for a full target result is now beyond this radius1 neighborhood: a different decomposition, a multi-switch/longer-cycle trade that breaks the preserved faults, or an unrestricted mathematical obstruction. This document does not authorize a larger search or silently change the primary target.
