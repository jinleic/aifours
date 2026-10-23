# k62-followon checkpoint 013 (Sun63Successor) — withdrawal of an IRC claim

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:45:32-0700. Previous: `checkpoint-012-v1.md`
  (sha256 6e068573722df1772d4fe70a7cf671b1de2f4c4e4be7b8a7b9acb90d9550e58a).
- **State:** parked until the CAP/DT dual review returns (`RUN/review/sun7-K62-CAP-DT-review-freeze-v1.json`). No file of the
  frozen package changes; no enumeration; no computation.

## Withdrawal (recorded at the parent's request)
My IRC answer to the parent's CAP question Q2 claimed that DG's bound "sum <= 19/16 - 2/n_d" is *equivalent* to the
pattern-determined predicate "sum < 19/16" (i.e. sum <= 37/32) and that "nothing is lost". **That claim is false and is
withdrawn.** The 1/32 grid argument only absorbs the term 2/n_d when 2/n_d <= 1/32, i.e. n_d >= 64. Counterexamples to
equivalence: at n_d = 16, DG gives sum <= 17/16 while "sum < 19/16" admits 18/16 (for example eight terms 1/8 and two
terms 1/16); at n_d = 32, DG gives sum <= 36/32 while the grid test admits 37/32.
**Correct statement:** "sum < 19/16" (and likewise N(O)/n_d < 1/8 in place of N(O) <= n_d/8 - 1/2) is a **safe necessary
weakening** of DG, determined by the pattern, but it is lossy in general. Any rule built on CAP-62 must either keep the
explicit small-n_d dependence (for example by adding a capped n_d-class to the pattern) or use the weakened predicate
and accept the loss. Equivalence for n_d >= 64 would be a separate conditional statement; it is not claimed here.
The same correction applies to my IRC answer's sentence on N(O). The answer to Q1 (the (C2) wording: the first added
O-vertex after d has gcd 2, so k <= 1 <= 3) stands.

## Resources
No process was ever launched by this worker; nothing to settle.
