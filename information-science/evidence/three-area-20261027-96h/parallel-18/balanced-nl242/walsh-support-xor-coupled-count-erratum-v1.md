# info-6: coupled frequency-count correction for the support-XOR and peak bounds

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observation returned before this write: **2026-10-27T15:13:12-0700 PDT**. This is an **additive wording/inequality erratum**, not an edit of either pinned author body and not a new independent review. Main reports the original T≠0 / at least 86 peak-frequency result at **same-harness written-support** level with this mandatory MINOR overlay; the parent disposition and actual review were not opened in this S1 input scope. The later ≥92 claim remains **unreviewed**.

## Incorrect independent-count wording

In `walsh-support-xor-obstruction-v1.md` the phrases saying the `Q=0` nonzero counts are “at most 127” in the full-space case and “at most 63” in the T^⊥ case do not follow from the lower bounds on the number of Q-zeros. The counts are coupled to the number q of Q-ones: they are exactly **511−q** and **255−q**, respectively. The same imprecise “at most 63 other nonzero points” wording appears in `walsh-peak-multiplicity-v1.md`. Preserve both originals; do not import those independent upper bounds.

## Correct coupled maximization

- In the T=0 branch, q≤384 and Q(0)=0. The exact nonzero complement count is 511−q, so

      Σ_a k(a)² ≤ 36q+16(511−q)=8176+20q ≤ 15856 < 2¹⁴.

  This is the originally intended contradiction; it does **not** assume a separate upper bound of 127 on the complement count.
- In the T≠0 branch on K=T^⊥, q≤192, Q(0)=0, and the exact nonzero complement count is 255−q. Thus

      E_K≤36q+16(255−q)=4080+20q≤7920.

  Combining this with the odd-half energy gives the earlier at-least-86 claim. With the separately unreviewed all-hyperplane energy congruence, the later ≥92 derivation also uses precisely this corrected E_K bound; its conclusion is **not** promoted by Main's earlier adoption.

The inequalities increase with q, which is why the numerical upper bounds remain valid after replacing the flawed wording. No selected spectrum, state, frequency or computational check was introduced. This derivation does not independently re-review either candidate.

## Exact scope and controls

- `walsh-support-xor-obstruction-v1.md`, SHA-256 `380655caaa06ea27e4236070ff66e070be63963960efebfabef2e730d2091fc4`, 49 LF: parent-notified support is T≠0 and at least 86 |W|=28 frequencies, at same-harness written-support level only and with this MINOR overlay.
- `walsh-peak-multiplicity-v1.md`, SHA-256 `8a64a73bc552f9e71cc04f07159c1f09feab17894d31966c16ebfe80d9fd37b8`, 28 LF: the at-least-92 refinement remains an unreviewed author candidate and requires its own full-scope review, including the corrected inequality and its hyperplane-energy input.
- Parent notified `dispositions/info-6-support-xor-peak-multiplicity-parent-v1.md`; its exact bytes/hash and the 117-LF review body are **not independently read or pinned here**. No configured-independent-model, human, formal/kernel, executable, book-source equivalence or novelty claim follows.

The unrestricted balanced NL242 witness-or-exclusion problem and `(24,24,2)` gap remain OPEN. The metadata-clock-status-poll incident remains an administrative MINOR per Main; S1 HOLD/STOP/ZERO/NONINPUT, N4 UNKNOWN, aux214 STOP, prior exposure and all earlier findings remain binding.
