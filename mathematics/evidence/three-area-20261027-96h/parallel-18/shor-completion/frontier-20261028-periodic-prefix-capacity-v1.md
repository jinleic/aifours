# A computer-assisted all-order periodic prefix-capacity bound for Shor completions

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 17:32:03 PDT 2026**.
**Finite-state/computer-assisted mathematical candidate; two separately implemented exact checkers, not formal/kernel/human review or a completion.**

## 1. Exact original-object implication

Let D be ANY finite uniquely decipherable (UD), factor-complete extension of the literal 16-word Shor code S. Let a^n be its actual unique pure-a atom, B its actual one-b layer, and N_out the number of its actual B-atoms whose initial a-run is NOT congruent modulo n to one of `A={0,3,8,11}`. The earlier raw-word argument in `frontier-20261028-prefix-layer-obstruction-v1.md`, SHA256 **ef0d973f52ece5365613a8280475e240992ab53d47bca55dd13ea62f573ab0dc**, proves |B|=n and the common-row packing caller used below.

**Theorem — exact certified row relaxation, all n>=140.** The following necessary lower bounds apply to N_out according to the ACTUAL n mod16:

| n mod16 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N_out at least | 2 | 6 | 5 | 5 | 6 | 8 | 7 | 8 | 10 | 10 | 7 | 11 | 6 | 8 | 5 | 8 |

For illustration only, at n=660 the bound is6, at n=1320 it is10, and at n=2640 it is2. These are conditional on a hypothetical completion with that same order, not claims that any order is realizable. No historical FACT import is needed.

**Scope:** the table is an EXACT maximum for each of the four original prefix rows when considered separately under the necessary A-packing constraints, and therefore an actual-completion lower bound. The maxima of distinct rows are NOT asserted simultaneously attainable, and full-list UD/multi-b/factor-completeness are NOT established by these row optima. Finite computation certifies a 98-state transfer periodicity; the all-order extension is the written induction in §4. This is not a theorem prover or an unrestricted noncompletion proof.

## 2. Reduce each actual row to a cyclic independent-set problem

The same D contains the four old suffix-zero words `a^v b`, v in A. For any actual prefix row i, let J_i be its set of suffix residues. If j,j' in J_i and a,a' in A satisfy `j+a==j'+a' mod n` with the pairs different, then the two actual two-atom lists have equal outer residues and internal residue. Nonnegative powers of the ACTUAL atom a^n align the three a-runs, giving distinct equal raw parses. Thus J_i+A is direct.

For n>=140 the distinct nonzero cyclic differences of A have positive representatives

    Q={3,5,8,11}.

Consequently J_i is exactly an independent subset of the cyclic graph on Z_n with forbidden differences `±3,±5,±8,±11`. Conversely, any set of residues avoiding these differences satisfies the isolated row's A-packing condition. This converse is ONLY for the row relaxation, not for UD or a completion.

The actual old S requires the SAME four rows to contain

    row 0:  {0,1,7,13,14},
    row 3:  {0,2,4,6},
    row 8:  {0,2,4,6},
    row 11: {0,1,2}.

Different actual one-b atoms cannot repeat the same endpoint residue pair, since pure-a endpoint padding would give an ambiguity. Therefore their numbers in these rows equal the corresponding |J_i|. The row0, row3/8 and row11 maxima are computed below; two rows share the middle anchor set but are still separately counted. Since |B|=n, subtracting their individual maxima is a valid lower bound on N_out even if the maximizing sets cannot coexist.

## 3. Exact width-11 transfer and cyclic closure

Let x_j in{0,1} indicate that tail residue j is selected. For a linear prefix `0,...,t−1`, a state records the ages 1,...,11 of selected positions relative to the NEXT position t, together with the maximum number selected among all legal prefixes with that state. When processing t:

- selecting0 shifts each age up by1 and discards ages>11;
- selecting1 is legal exactly when none of ages3,5,8,11 occurs; it makes the same shift and inserts age1, adding1 to the score;
- keep the maximum score for each resulting state.

This recursion is EXACT: every allowed prefix has one predecessor and one bit, and future compatibility depends only on its most recent11 bits. The three initial anchor patterns force a UNIQUE legal mask on positions0..10, respectively `{0,1,7}`, `{0,2,4,6}`, `{0,1,2}`. Every other position among0..10 differs from one of those anchors by one of the forbidden gaps. Row0 additionally forces positions13 and14. No forced anchor occurs after14.

For a cyclic row of length n>=140, process the first n−11 positions linearly and then the last11 with a wrap veto: a position i in that suffix may not be selected if its circular distance to one of the forced selected positions in0..10 is in Q. There can be no other wrap collision: if both indices are >=11, their wrap distance is at least12, above the largest forbidden gap11. All first-eleven nonanchors are proved absent, so the veto covers EVERY remaining boundary interaction. Its pattern depends only on the relative suffix offset and the row's fixed initial anchors, not on the absolute value of n. Taking the maximum final score therefore gives the exact cyclic row-packing optimum.

## 4. Finite 98-state period certificate implies ALL later orders

Let F_t be the vector of exact best prefix scores after t positions, indexed by the complete reachable 11-bit states. An absent state has score minus infinity. After position14, the same homogeneous max-plus transition T applies at EVERY subsequent interior position, and T commutes with adding a constant to every finite score.

The two independent exact implementations check the following WHOLE-vector identities, including identical reachable-state sets:

| Original row | Base prefix length t | Reachable states | Checked identity |
|---|---:|---:|---|
| 0 |129 |98 | `F_145=F_129+4` |
| 3 and 8 |29 |98 | `F_45=F_29+4` |
| 11 |69 |98 | `F_85=F_69+4` |

Because `T(F+c)=T(F)+c`, applying T repeatedly proves `F_(t+s+16)=F_(t+s)+4` for EVERY integer s>=0. This induction is an exact mathematical consequence of the finite checked equalities; it is not extrapolation from a numerical trend.

For n>=140, n−11>=129 for ALL three row types. The final11-position cyclic veto is the SAME offset-dependent map at n and n+16, so each exact cyclic optimum obeys

    M_i(n+16)=M_i(n)+4.

Since the four rows contribute `M_0+2M_3+M_11`, the lower bound `n−M_0−2M_3−M_11` is exactly periodic with period16 for every n>=140. Thus the 16 exact representative computations at n=140..155 prove the table in §1 for ALL n>=140, subject to the correctly implemented finite-state certificate.

## 5. Checked representative values

The independently computed representative row optima are:

| n | M_0 | M_3=M_8 | M_11 | n−M_0−2M_3−M_11 |
|---:|---:|---:|---:|---:|
|140|33|34|33|6|
|141|34|33|33|8|
|142|33|35|34|5|
|143|33|34|34|8|
|144|35|36|35|2|
|145|34|35|35|6|
|146|34|36|35|5|
|147|35|36|35|5|
|148|35|36|35|6|
|149|34|36|35|8|
|150|36|36|35|7|
|151|36|36|35|8|
|152|35|36|35|10|
|153|36|36|35|10|
|154|37|37|36|7|
|155|36|36|36|11|

Both implementations ALSO ran the full cyclic DP directly at n=660,1320,2640, returning respectively `(M_0,M_3,M_11,N_out lower bound)` equal to `(163,164,163,6)`, `(327,328,327,10)`, `(659,660,659,2)`. They agree with the period-representative calculation, but are not themselves a proof of the period.

## 6. Actual independent checks and reproducibility

After completing the code, the following bounded exact executions were performed:

1. `python3 -B frontier-20261028-row-transfer-certificate.py`: age-TUPLE state representation, computed all three full 98-state period equalities, all16 representatives and direct n=660/1320/2640 comparisons.
2. `python3 -B frontier-20261028-row-transfer-bitmask-check.py`: separately written BITMASK state representation, independently enumerated the initial legal masks, recomputed all 98-state equalities and the SAME16 representatives and direct orders. For EACH row it deliberately changed one score and separately deleted a state; both controls were rejected for the intended distinct score/state mismatch reasons.
3. `python3 -B frontier-20261028-all-rows-dp.py 28 44 60 76 92 108 124 140 330 660 1320 2640`: another full cyclic DP, reconstructing and directly validating each output row witness against anchors and all cyclic forbidden differences. Its 660/1320/2640 optima agree with both transfer checkers. These independently validated witnesses show the listed individual-row lower maxima; the transfer recursion supplies the upper side.

Native source pins observed Wed Oct28 17:32:03 PDT:

| Checker | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-row-transfer-certificate.py` | 33b96424dedd09c10f0056029119abe15616dfc91eb285f922eb8de1d97325e9 |99 /3869 |
| `frontier-20261028-row-transfer-bitmask-check.py` | 94929d8d3a622589d9830b85dda1c101e8351e1e9ac49d56a7fc27373707b50d |111 /3696 |
| `frontier-20261028-all-rows-dp.py` | a350647dab22aaf8ff5c17447b6584504255585433407d28783f495ef5d13e95 |78 /3323 |

The checkers are different implementations of the SAME elementary recurrence, not independent-model/cross-vendor formal verification. Their finite-vector equality and the mathematical reduction/induction require independent review. Recorded tests cannot turn separately feasible rows into one actual code.

## 7. Original problem and provenance limits

This refines the earlier all-variable prefix necessity and, at n congruent4 or8 mod16, strengthens its simple 2-adic lower bounds. It does not force an atom into a forbidden three-boundary rectangle, construct a full one-b layer, control multi-b atoms, prove factor-completeness, exhibit a finite complete D or rule out all finite D. The original Shor completion question therefore remains unresolved. Individual row witnesses are relaxation certificates, not candidate complete codes.

No held historical outcome is accepted as a premise merely by the new owner direction. This packet uses the supplied literal S, the explicitly identified raw one-b conservation proof, and elementary cyclic/finite-state arguments. All previous incidents remain historically recorded; no novelty/priority, human, formal, kernel or configured-independent-model acceptance is claimed.

**END OF COMPUTER-ASSISTED PERIODIC PREFIX CAPACITY CANDIDATE.**
