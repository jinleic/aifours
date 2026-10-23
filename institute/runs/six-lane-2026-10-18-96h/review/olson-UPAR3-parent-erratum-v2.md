# UPAR3 — second-family precision erratum v2

Recorded 2026-10-21T10:33:34-0700 after `/bin/date`). Read after [erratum v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UPAR3-parent-erratum-v1.md). [Claude complete review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UPAR3-claude-v1.prompt.note.md) SHA256 `85548e4f7119b9d54cacede1aef50b6c67ab4567cf7ed5891a21bafcd8887456` reports 0 FATAL/0 MAJOR/11 MINOR after re-deriving UPAR3-Z, UPAR3-P and R3 at full quantified scope; it explicitly confirms no unit-label narrowing anywhere. All eleven repairs are wording/notation/citation-level; none changes a theorem, inequality, cell outcome or residual test. Note binding verified from the single complete7806-character assistant text segment.

1. **m1, proof LF38.** The alternating-set phrase reads “for 1≤|U|≤h−1, m(U)=|U| (UMR LF252–253)”.
2. **m2, proof LF64.** The Q-count and I-count also cite the threshold floor Θ≥2r−3n (UPAR LF71–72) and n≤l, beyond(W).
3. **m3, proof LF45 versus LF56–121.** Declare b:=b* once at LF45; bare b denotes the JUMP variable throughout, consistent with parent erratum v1/v2 conventions for UPAR2.
4. **m4, proof LF69.** Heading reads “F=e is impossible on T\T2 (vacuous on T2)”; the LJ inherited data exists only off T2.
5. **m5, proof LF22–23.** Same scope qualification as first-family item1: inherited mixed-orientation exclusions hold **at F=0**; §2 re-proves every mixed case for all F=e.
6. **m6, proof LF90/LF150.** Rename the local T:= bound variable (e.g. Tmix) and the x=y−1 tail-size symbol (e.g. xY); they collide with the target set T and the window entry x.
7. **m7, proof LF176–179.** Add “(b*=2d−1, F=0) removed by (Gap)”. Scalar inequalities, F≥e and parity alone do not exclude that odd row; the already-proved gap does. Same substance as first-family item2.
8. **m8, proof LF121.** Display eps=0 and P-entry M_(r+1)−R+4<0 for the two-run level r+2 explicitly.
9. **m9, proof LF20.** “Complete residual of Sec.7”, not Sec.6.
10. **m10, proof LF200–237.** R3 is DEFINED as literal accepted R2 (UPAR2 primary LF194–218 with mandatory errata v1–v3) ∩ {F−e≥2}, restricted to T\T3. Items(a)–(e) are a non-exhaustive gloss, not a replacement. “(Cost)” refers to LF32–34/UPAR Lemma1. “No old test is deleted” means no R2 test is deleted; the unpasted UPAR LF216–275/UPAR2 LF124–193 bodies remain the authority. R3 necessity holds with this literal definition; the paraphrase gaps are repaired, not waived.
11. **m11, packet scope.** The two pinned-not-pasted JSONs (authority and UPAR2 disposition) remain process metadata, never mathematical premises; their absence from the packet is a disclosed source limit, not an unreviewed governing input. Both families received the identical pasted mathematical sources.

New observation from the second family, NOT promoted beyond the theorem's own scope: (24,53) (κ=8d, d=3) is newly excluded by the proved region. It is a uniform-instance consequence of T3, bookkept in the frontier update, not an independent new theorem or claimed novelty.

UPAR3 remains candidate until the parent final gate: both families have now returned with only precision-level findings; verification chain = Codex 0F/0M/2m + Claude 0F/0M/11m + parent hand check, all through these two errata. Full T, POSITIVE-BUDGET-COVER, the three open named cells and ordered Olson remain unproved. No runtime/native/formal/human/novelty claim.
