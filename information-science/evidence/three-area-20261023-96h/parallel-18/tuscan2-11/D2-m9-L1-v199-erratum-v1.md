# Erratum v1 to v199 (owner self-verification record)

Owner: InfoRecursiveMDS18-2, slot info-4, under parent direction v143. `/bin/date` before this record: **Tue Oct 27 05:21:34 PDT 2026**.

Applies to `D2-m9-L1-types12-2-r2eq3-alpha3-k1-closed-r2eq3-closed-v199.md` (SHA256 `b1832cc493277e538fdf38c0db39d6ddaaafeddb1e47d043e90d870b1c57b70f`, LF [1,108]). v199 is pinned and is not edited; this file is additive.

## 1. Self-verification

v199 was pinned at 05:00:52, after Main's metadata request arrived and before the owner's usual pre-pin re-read. That re-read has now been done line by line, against v196 §1, v188 §1, v190 §2 and v185 §2.

No mathematical error was found. Every numerical range used in §2 was re-derived by hand:
- (ℓ1, ℓ2) ∈ {(20,12), (20,13), (21,11), (21,12)};
- the t3V windows {8,9}, {9}, {7,8} and {8}.

## 2. Corrections (wording only)

**(a) v199 §3, the bullet "t3[ℓ3−1]" (LF80).**
- "f2's cut vertex" should read "the F2-cut vertex t3[20−x]". The name f2 is defined only in §2 (Case B1), as L(t1[18]).
- The argument is unchanged: since ℓ3 − 1 ≥ 20 − x, the vertex t3[ℓ3−1] is either the Q1/Q2 cut vertex, which carries an F2-cut label, or a vertex of Q2. c7's t3-vertex lies inside Q1.

**(b) v199 §1, LF13.**
- P1 = 30 is also excluded, because b3 never lies on a cut (v188 §1). Together with P1 ≥ 31 (DP★) and P1 ≥ 21 (t1[u+10] lies at 20), this gives P1 ∈ [21,29].

**(c) v199 §3, the grid bullet (LF64).**
- Q1 is a pure t3-row. Its F1 span therefore lies inside t3's F1 positions, P4+1..P5−1 ⊆ [52,68], so the F1-cut strictly inside it can only be 60.
- Neither end of Q1 lies on an F1-cut, because a label cannot be both F1-cut and F2-cut.
- The grid lemma (v184 §2) then needs at least 4 on each side, which gives ℓ2 + x ∈ [19,21].

## 3. Status

The v199 result is unchanged: WRITTEN, unreviewed. The support-9 statement is not made, and every m in 10..110 is unresolved. In metadata map v21, v199 stays outside the completed freeze.
