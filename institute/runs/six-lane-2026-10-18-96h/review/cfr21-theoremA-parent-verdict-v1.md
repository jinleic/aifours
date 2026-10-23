# CFR(6,21): mod-3 constant-character theorem accepted as a necessary condition

Recorded at 2026-10-19T00:22:21-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL (necessary condition only).** Theorem A, Corollary A1 and Corollary A2 hold as stated, read through errata 1 and 2. **CFR(6,21) remains OPEN.** Theorem A does not construct or exclude a seven-row cyclic Z_21 difference matrix. Priority and significance are unresolved; a focused primary screen is pending.

## Accepted statements

Let 3 | n and 9 ∤ n, and let D be any (Z_n,k;1) difference matrix with k ≥ 4. Reduce entries modulo 3. Call a coefficient vector χ on the rows translation-invariant if Σχ_i = 0.

- **Theorem A.** If such a χ makes Σχ_i a_i(c) constant over all columns, then χ = 0 or |supp χ| ≥ 6.
- **Corollary A1 (k=7).** The space K of such constant characters has dimension at most one, so the mod-3 affine rank is 5 or 6. Rank 5 occurs only if K is spanned by one of three support-6/7 shapes up to sign and row relabelling. This applies to the seven-row matrix {0, τ_1,…,τ_6} associated with a CFR(6,n), τ_r = σ_r^−1, not to the six positional rows alone.
- **Corollary A2.** k=4,5 force full rank; k=6 forces rank at least 4. The same counting bound gives dim K ≤ 1 for every 4 ≤ k ≤ 7.
- **Consequence for constructions.** No seven-row cyclic Z_n difference matrix, with 3 | n and 9 ∤ n, satisfies any constant mod-3 relation Σχ_i a_i ≡ const with Σχ_i = 0 and 1 ≤ |supp χ| ≤ 5. Relations with nonzero coefficient sum are not excluded in general, because a column offset can create them.

## Parent derivation

Pair differences of a cyclic difference matrix are bijections onto Z_n; reducing modulo 3 makes every row difference balanced. For functions f,g on the columns, if f, g, f+g and f−g are balanced, each point (u,v) of F_3^2 receives exactly n/9 columns. The parent proved this by incidence rather than Fourier: the four lines through a point cover it four times and every other point once, so 4n/3 = n+3N(u,v). The [incidence control](cfr21-rank-parent-control-v1/incidence-control-v1.json) checks all nine points. A support-m sum-zero vector over F_3 with μ entries equal to −1 satisfies m+μ ≡ 0 (mod 3), giving the exhaustive support-3/4/5 shapes. The explicit pairs (f,g) in the proof make all four functions balanced, contradicting 9 ∤ n. A two-dimensional K would have total weight at most 6k but eight nonzero vectors of weight at least six, total at least 48, impossible for k ≤ 7. Row offsets, column offsets, units and permutations preserve K and the rank.

## Texts, reviews and dispositions

- [Theorem text v1](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/cfr21/evidence/theoremA-mod3-rank-v1.md), SHA256 `10e9b724b40b2a6d1f81827cf82f4cabf7d1e14d8b113cbe9fa15291ac969094`; [erratum 1](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/cfr21/evidence/theoremA-mod3-rank-v1-erratum1.md), `7f92e7c303d928297ab6255c43ee5d7e7b9fe4a38f31f9b18fa65dec73b83e66`; [erratum 2](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/cfr21/evidence/theoremA-mod3-rank-v1-erratum2.md), `83679b8e3c387f96610cc350ff5e354050d61a1f25d56535203fd0d1f6c82aca`. Read together; no statement changed.
- [Codex review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/cfr21-mod3-rank-codex-v1.prompt.stdout.txt): ACCEPT-WITH-FIXES, observed gpt-6.1-sol, max, read-only. Its MAJOR concerns only the auxiliary unnormalized point form, fixed by E1/E4 with an arbitrary column function h(c). Its minors are fixed by E2/E5/E6/E8.
- [Claude review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/cfr21-mod3-rank-claude-v1.prompt.note.md): ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR, observed claude-opus-5-5. m1–m6 are fixed by E4–E11. Claude also independently proved the seven-cap census mentioned below.

The lane's machine checks (support witnesses, 96 known six-row matrices of full rank5, seven-cap census) are exploratory supporting evidence, not premises. The proof uses none of them.

## Limits

This is a written proof with two model reviews and a parent derivation; no Lean, human review or novelty clearance. Erratum E10's paraphrase of Evans (2013, Theorem 4) has not been checked against the primary paper by the parent; read it only as a lead for the pending screen. The worker's suggested overlap with 3-level orthogonal-array J-characteristics is likewise unscreened. Significance: a modest specialist necessary condition; the generic rank-6 stratum is untouched.
