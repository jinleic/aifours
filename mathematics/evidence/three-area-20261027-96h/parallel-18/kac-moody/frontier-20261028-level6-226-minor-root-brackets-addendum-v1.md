# Exact real-root brackets for the selected level-six 125-type minor

**MathKacMoody-2 / math-3.** Native observation before this write: **Wed Oct 28 18:54:01 PDT 2026**. Additive to the UNREVIEWED strip candidate `frontier-20261028-level6-226-gap41-strip-candidate-v1.md`, 74LF SHA `a9d70a2b7da3b93056999cff6771997593e78d2d4cc12a3ac46a33d094f75f40`; no frozen file is edited. This is exact symbolic/rational algebra for one selected determinant, not a full-map or integer-parameter counterexample.

Let `P(x,y)` be the ACTUAL selected 34×34 minor polynomial of that source, with `x=r-6,y=s-6`, whose entire bivariate determinant identity has a separate exact 630-grid replay. Direct exact rational evaluation gives

\[
P(11,0)<0<P(23/2,0),\qquad
P(0,41)<0<P(0,83/2).
\]

By continuity, there is at least one real zero of `P(x,0)` in `(11,23/2)` and at least one real zero of `P(0,y)` in `(41,83/2)`. These intervals contain no integer. No uniqueness of either zero or statement about any other zeros is proved.

This sharpens the old existence-only axis observation and makes TWO limitations concrete:

1. The **same selected polynomial P** has a real zero in the first axis inside `|x-y|<41`. Therefore the symmetric strip theorem must use its expressly supplied whole-algebra node exchange in the `r>s` chamber; it must NOT claim that this original selected P is nonzero throughout both chambers.
2. The direct `s>=r` coefficient-sign certificate cannot be uniformly extended beyond `83/2` for this fixed P, since its second-axis root lies before that bound. This is NOT a statement that the true full map's maximal strip is 41, or that other target minors fail.

The exact 32LF checker `frontier-20261028-level6-226-minor-root-brackets.py`, SHA `634a670e3568bc483f287ae86f923ed0f0b230bb2bfa503a09521ceabae7875f`, reads the separately replayed mixed polynomial SHA `874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8` and evaluates all four endpoint values using Fraction. Its 26LF output `frontier-20261028-level6-226-minor-root-brackets-v1.json`, SHA `5c7de0bf6f4bcf635e0743500d81a7b3ccd2468e80a7202cad32ce832df2aa95`, records all exact rationals and returned `PASS exact IVT signs: selected-minor real roots x in (11,23/2), y in (41,83/2)` at **Wed Oct 28 18:54:01 PDT 2026**. The earlier methodology/exposure and unreviewed source limitations remain unchanged.

A zero of one square minor is NOT a kernel of the full map, a non-Serre element, an integer-parameter counterexample, an all-minor obstruction or a novelty result. Full mathematical/source/code review and parent disposition remain pending.

**END — exact brackets for two zeros of one selected determinant only.**
