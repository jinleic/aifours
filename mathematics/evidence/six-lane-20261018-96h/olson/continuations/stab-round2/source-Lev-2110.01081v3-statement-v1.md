# Lev 2022, Theorem 2: primary statement read, not yet a parent-accepted import

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T08:53:31-0700. Source read directly via the static reader:
https://arxiv.org/html/2110.01081v3#Thmtheorem2
Vsevolod F. Lev, Zero-sum-free sequences with few subsequence sums, arXiv:2110.01081v3 [math.CO], displayed version date
01 Jun 2022. Author affiliation as displayed: University of Haifa at Oranim. Read scope: Section 1 definitions, Theorem 2,
its immediately following discussion and the contrast with Theorem 1. No proof-body replay, formal verification, journal-status
or novelty claim. No external source was executed.

## Definitions actually read
Section 1 defines a sequence as zero-sum-free if it has no finite nonempty zero-sum subsequence.
Section 1, paragraph beginning 'Given a sequence alpha', defines Sigma(alpha) as ALL subsequence sums INCLUDING the empty sum:
  Sigma(alpha) = {sum_(i in I) a_i : I subset [1,n]}.
The size used in Theorem 2 is therefore inclusive; it is NOT the nonempty-only Sigma convention used in some lane files.

## Theorem 2: mathematical transcription (typography normalized from primary HTML)
Suppose that alpha = (a_1,...,a_n) is a zero-sum-free sequence of elements of an abelian group. If |Sigma(alpha)| < 2n, then,
having the elements of alpha suitably renumbered, there are a group element a and integers
  1 = x_1 <= ... <= x_n
satisfying
  x_(k+1) <= x_1 + ... + x_k,  k in [1,n-1],
such that a_k = x_k a for all k in [1,n]. Moreover,
  Sigma(alpha) = {0,a,2a,...,(x_1+...+x_n)a},
and if a is of finite order, then x_1+...+x_n < ord(a).

The inequality in THEOREM 2 has NO extra '+1'. Theorem 1 (the earlier Savchev-Chen/Yuan result printed immediately above) DOES
have '+1' and a length>group-order/2 hypothesis. Those are distinct statements; Theorem 2 has no half-order length hypothesis,
requires the strict few-sums inequality, and works over any abelian group.

## Exact boundary of this record
This is a statement-level primary-source record and a local normalized transcription, NOT a byte snapshot of the remote HTML.
Its local SHA256 binds these notes only. Source identity is the version-pinned arXiv URL and anchor above. Parent must review the
transcription/application before accepting this as a correctness import. All new consequences below are CONDITIONAL on the
stated published theorem; the proof of Lev's external theorem is not reproduced or replayed by this worker.
