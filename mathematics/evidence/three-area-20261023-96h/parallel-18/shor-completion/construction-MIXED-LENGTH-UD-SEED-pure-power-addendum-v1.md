# The mixed-length UD seed admits every prescribed pure-a order n≥26

Observed before creation: **2026-10-23T16:01:39-0700 PDT**. MathShor, math-5. **CANDIDATE extension of the same constructive seed packet**, not a finite complete code, a new order bound, a novelty claim or an execution result.

Source: `construction-MIXED-LENGTH-UD-SEED-v1.md`, SHA256 `c45ef598f9b7cbf234d6dfc5adad448285b80ff58bf5650bc994948a8ff081df`, defines the actual20-word UD code M_seed and its finite residual invariant. Its source review is not inherited by this new extension; the complete two-file constructive packet needs its own reconstruction.

## Exact family

For EVERY integer n≥26, set

    M_n=M_seed∪{a^n}.

Then M_n is an actual21-word finite UD code containing literal Shor C, with unique pure-a codeword a^n, the same mixed extra lengths4,5,6,6,n, and the same realized two-/three-/four-a gap structure. In particular this supplies a raw UD seed for every order satisfying the much stronger inherited necessary completion predicate; it does not prove that any such seed has a finite completion.

## All-word residual certificate

Use the source's sets

    S={1,2,4,6,7,12,13,14},
    B={1,2,4,5,6,7,9,10},
    I={0,3,8,11}.

Let T be its finite set of b-containing residuals of length≤14 whose first-b delay is in B. Replace the pure residual set by

    P_n={a^s:s∈S}∪{a^(n-s):s∈S}.

Then R_n=P_n∪T is finite and excludes epsilon. All pure residual lengths are strictly between0 and n. Also n-s≥n-14≥12, which exceeds every positive first-b delay in I.

The new word a^n is not prefix-comparable with any old codeword: every old word has b within its first12positions, whereas n≥26. Thus initial proper-prefix residuals are unchanged and already lie in R_n.

For closure:

- Every t∈T is incomparable with all old codewords by the source's B∩I separation. It is also incomparable with a^n because it contains b and has length≤14<n.
- The old pure residuals a^s have exactly the old terminal transitions into T when compared with old codewords. Comparison with a^n adds a^(n-s), included in P_n.
- Each new a^(n-s) has length≥12, so is incomparable with every old codeword whose first b appears after at most11 a's. Comparison with a^n returns a^s, also in P_n.
- No pure residual equals a^n and no codeword can equal a b-containing T-residual, again by the first-b separation.

Therefore the actual initial-residual coverage, full prefix-comparison closure and empty exclusion hold for every n in the range. Prefix cancellation proves UD over ALL finite lists. There is no executed Sardinas–Patterson check or finite-n enumeration behind this proof.

## Still incomplete, by exact evidence

The binary Kraft sum is

    15811/16384+2^(-n)<1,

because n≥26>14 and the old deficit is573/16384. Finite UD completeness would force Kraft1 by the already proved counting argument. Thus no M_n is complete.

There is also an actual missing-factor certificate, so no mass criterion is being confused with the book definition. The word

    b^30 a^5 b^30

is a factor of no M_n-product. Any non-power codeword meeting one of its central a's lies inside that displayed factor because its length is≤15, much less than the b-margins. The pure-a word a^n cannot meet this isolated run of only5a's when n≥26. A codeword meeting central a's must therefore have a pure internal a-core of size≤5. The only such possibilities in M_n are ba (size1), ba^2b (size2) and a^3b (size3). At a zero internal b-gap, the ONLY legal boundary between these three types is ba followed by a^3b: the former's trailing delay is0 and the latter's leading delay0. That gives size4 and cannot be followed or preceded internally by another of these types. No size5 partition is possible. Hence the padded five-a factor cannot occur.

The source seed's missing a^26 is no longer a valid missing factor for M_n, since a^n contains it. The new fixed padded-factor proof replaces that claim explicitly rather than carrying it forward incorrectly.

## Remaining scope

This realizes a mixed-length UD starting point, including any prescribed admissible pure-a order, but not the many missing codewords required for a completion. Completing one M_n would suffice for C; no assertion is made that all hypothetical completions of C contain this fixed seed or r=t=1. Failure of this branch would remain restricted.

The full all-order mixed-length RAW-SELECTOR obligation stays open. No solver, scientific executable, finite table, formal kernel or source-access assumption was used. The numeric26 is a sufficient separation threshold for THIS raw UD family, not a lower bound on a finite Shor completion.
