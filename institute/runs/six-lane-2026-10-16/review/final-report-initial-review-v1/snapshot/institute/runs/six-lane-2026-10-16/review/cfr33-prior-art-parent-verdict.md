# CFR(4,33): stale target — an existing cyclic difference matrix gives five rows

**CFR(4,33) is already available from SageMath's `DM_33_6_1` construction. No search was run and no gate is claimed.** The pre-freeze CPro1/Rosin screen missed an equivalent object under another name.

## Exact bridge

An r × n CFR has positional permutations f₁,…,fᵣ on Z_n. Two rows share an ordered-symbol distance exactly when fᵢ(a)−fⱼ(a)=fᵢ(b)−fⱼ(b) for some a≠b. Thus CFR(r,n) is equivalent to a cyclic (Z_n,r+1;1) difference matrix: append the zero function to the positional permutations. Conversely, subtract one column of such a difference matrix from all columns, discard its zero column, and invert the remaining permutation columns to obtain CFR rows. This must be over **cyclic Z_n**; an arbitrary group of order n is not interchangeable with the circular-distance group.

Sage's [pinned source](https://raw.githubusercontent.com/sagemath/sage/0835358cba62dc19fccdff54f32e52fded9f22b0/src/sage/combinat/designs/database.py), lines 3400–3440, explicitly uses `IntegerModRing(33)` and returns a (33,6,1) difference matrix. Its docstring attributes the construction to Handbook III.3.56; that Handbook section was not parent-read. The worker found identical literals/expansion in Sage 6.4 (2014).

## Parent verification

The parent independently transcribed the six seed rows and the expansion from the pinned source, checked all 15 difference-column pairs are exactly Z_33, converted them into positional permutations, inverted them and normalized the first CFR row to the identity. The result matches the worker's two witness files byte-for-byte:

| Existing construction | SHA-256 | Direct circular events |
|---|---|---:|
| CFR(5,33) | `9a02e780f002086d4edf9d251b3df69d60be12cd1c3b033f9bd70191fdaecd8b` | 5280, all distinct |
| CFR(4,33), first four rows | `f1c1519d33e9a3c6ab095f38e89010a84774b2f10adbb37063d16ee4976c52c6` | 4224, all distinct |

[Parent receipt, literals and expansion](cfr33-prior-art-parent-v1/result.json). Worker receipt: [prior-art/receipt-v1.json](../../../../information-science/evidence/six-lane-20261016/cfr33/prior-art/receipt-v1.json), with pinned current/2014 Sage source, two independent CFR checkers and controls.

**FRONTIER: HEADROOM-ABSENT (prior construction), not a gate.** The slot moves to the frozen alternate CFR(5,27), subject to a cyclic-Z_27 difference-matrix applicability screen before any search. CFR(6,21) remains a later alternate. A recency sweep alone is not enough: target screening must also search equivalent names and construction databases.
