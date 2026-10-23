# FC19 process-wording erratum 1

Recorded after /bin/date 2026-10-20T10:35:00-0700. No mathematical claim, frozen target or rule changes.

1. FC19-scope-v1.md Sec. 4 (prior exposure): 'selected UB certificates fail at (7,19) and (8,19)' describes the
unexcluded cases of the UMR written method, not any proved UB failure in every frame or any residual existence. UMR
left Lemma FC unproved there. This packet uses no UB or RES inference at all. The scope's recorded untrusted hint
was not checked before the freeze; all new p=19 derivations were after it.
2. FC19-scope-v1.md Sec. 4 (pre-freeze machine steps): shasum covered every listed input. wc covered the authority,
UMR verdict and erratum v2 only; erratum v1, UMR proof, FC717 proof and FQW verdict were hash-only at that step.
3. checkpoints/cp-01.md: the UMR proof was opened in ranges covering LF1-406, but LF400 (a context-only table row)
was tool-truncated and was not used. Full text seen was LF1-399 and LF401-406. No omitted LF400 content was guessed.
4. checkpoints/cp-02.md's 'hand draft; recheck pending' is a preliminary derivation record. The final proof's
hybrid nonnegative-six branch, sparse lower-window lemma and empty-run counts are the complete versions. No cp-02
claim is a mathematical premise.

These are wording/disclosure corrections, not a missed freeze or cadence breach. All files remain immutable;
corrections are exclusively created as this separate file. Machine steps: text drafting and exclusive creation.
