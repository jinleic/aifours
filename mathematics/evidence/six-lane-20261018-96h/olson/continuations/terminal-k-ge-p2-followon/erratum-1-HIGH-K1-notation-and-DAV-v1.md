# HIGH-K1 erratum 1 — coefficient-count and residual notation precision

Clock:2026-10-21T15:00:42-0700 (`/bin/date` before exclusive creation).
Co-governs proof-HIGH-K1-and-core-v1.md, whole SHA256
f5b9357294f0e2cacd02e8f5494277df75b172414820821c9bf3ef8a1ecefe2a,231LF/18521bytes, unchanged.

1. In Sec.4 LF109-120 ONLY, rename the scalar coefficient-one count `u` to `u_one`. Thus
`u_one+s=p`, `b<=p-s=u_one`, `b>u_one=p-1`, and the cancellation uses `b` of those `u_one` occurrences.
Every `u` denoting the NF WORD, including LF122's reflection runs, remains the word. No inequality changes.
2. Read LF183-184's general-NF/DAV sentence EXPLICITLY as: 'Also require kappa<=k-1, the accepted DAV
bound; it is redundant here since kappa<=p-1 and k>=p+2. No additional unspecified DAV predicate is part
of the numerical definition. R>=p follows from the displayed upper k bound, not an extra assumption.'
The actual admissible-NF antecedent and ALL explicit(R0)-(R3) fields/tests remain. This disambiguates the
one already-displayed bound; it neither deletes a test nor imports an unlisted condition.

All hypotheses, proofs, parameter ranges, diagnostic outcomes and the ENTIRE remaining core are unchanged.
Full high-terminal cover remains UNPROVED. This is not a new scope/freeze/acknowledgement or deadline reset;
all permanent process departures remain. Both proof and this erratum must be supplied to every reviewer.
