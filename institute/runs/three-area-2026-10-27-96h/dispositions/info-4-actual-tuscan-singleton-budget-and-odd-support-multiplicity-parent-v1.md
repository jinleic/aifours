# Actual Tuscan rows: singleton budget and odd-support multiplicity exclusions

**Disposition: scoped same-harness written support with independent exact finite actual-row corroboration.** Native observation before composition: 2026-10-30T11:16:10-0700 PDT. f416 reports **0 FATAL / 0 MAJOR / 0 MINOR**. This excludes stated actual T2(11) branches, not unrestricted T2(11).

## Exact universal actual-row identity

An actual T2(n), n>=3, is n permutation rows on the SAME n symbols, with all directed linear distance1 pairs distinct and all directed linear distance2 pairs distinct. Distance2 counts ONLY original positions i→i+2, not wrap events after adjoining infinity. For every B of size b, let q be the number of black runs in one row, s its singleton black runs INCLUDING boundaries, t its INTERNAL singleton white runs, and d its distance2 black-to-black slots. Then d=b−2q+s+t. Actual adjacency exhaustion gives sum_rows q=b(n+1−b). If M is the missing ORDERED distinct distance2 pairs, mu_B=card(M∩B²), then

W_B=sum_rows(s+t)=b(n+1−b)−mu_B.

The empty/full B boundaries are included. Adjoining one WHITE infinity to each actual row gives an actual directed Hamilton decomposition; W counts finite singleton vertices, EXCLUDES infinity, and does not impose uniqueness on its extra distance2 events. Abstract Latin incidences or disconnected cycle covers are not substituted for rows.

## Whole odd-order branch theorem

For n=2m−1, m>=2, fix an m-symbol B and let k_B count rows whose odd-position support is B. Each such row contributes2m−1 singletons, hence

(2m−1) k_B <= m²−mu_B, so k_B<=floor(m/2).

Thus every ACTUAL T2(11) has at most3 rows with any fixed6-symbol odd-position support and at least4 distinct such supports. Equivalently, at most3 actual augmented Hamilton cycles can alternate across any fixed6+6 cut. Every branch with4 shared-support rows, at most3 distinct supports, or4 actual cycles alternating across one fixed cut is impossible. This does not exclude the remaining multiplicities1/2/3 or construct eleven rows.

## Conditional three-row boundary, not a universal endpoint identity

If ADDITIONALLY M=C={ (last(row),first(row)) } and exactly3 rows share B, then mu_B=3 and the other8 augmented Hamilton cycles have no singleton vertices, including infinity. Their monochromatic cyclic runs have lengths>=2. If u_j counts those8cycles with j black runs, then u3=u1+2, u2=6−2u1, u1∈{0,1,2,3}. Without M=C only0<=mu_B<=3 and their total finite singleton count3−mu_B follow. Universal M=C and exclusion of this remaining three-row branch are not proved.

## Verification and limits

[Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f398-tuscan11-actual-hamiltonian-row-closure-frontier/review-v1.md) · [Written reconstruction](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f416-tuscan-actual-row-singleton-run-identity-proof-review/review-v1.md) · [Independent finite report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f417-tuscan-singleton-run-independent-finite-check/review-v1.md) · [Exact checker](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f417-tuscan-singleton-run-independent-finite-check/independent-actual-row-singleton-finite-v1.py) · [Actual parent run](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f417-tuscan-singleton-run-independent-finite-check/parent-independent-finite-run-v1-receipt.json). Parent displayed the full548-line author,315-line written review and767-line finite-report/source, reconstructed run counts, directed/missing-pair universe, odd-floor bound, actual Hamilton interpretation and conditional equality case, and checked every frozen input pin. Separately authored stdlib code was parent-run once, exit0: ALL4088 binary words of lengths3..11, every boundary and subset size, an ACTUAL T2(4) with all16 subsets, an ACTUAL T1(6)-not-T2 control found after20 bounded normalized bases, finite m2..20 and6 intended-invariant rejections. Child execution was NOTRUN; these cases do not prove the universal theorem.

The reviewer directly checked the cited1989 publication record and Rosin2025 exact actual-row definition, not the full1989paper or exhaustive current literature. Novelty/priority and full current status remain inconclusive. No eleven-row witness, unrestricted no-go, OLS implication, human/independent-family or formal/kernel verification follows. All held episodes/consumers remain NONINPUT.
