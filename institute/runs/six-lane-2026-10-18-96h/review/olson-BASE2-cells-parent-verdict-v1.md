# Olson sequence lane: BASE2 cells (17,12) and (23,16)

Recorded at 2026-10-19T08:42:09-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Two exact LS cells and two threshold-counterexample lemmas. Written proof relative to the accepted import statements, including the external index-one theorem; no scientific computation or Lean replay. Full LS, LS+, STAB, INV* and ordered Olson remain OPEN.

## Exact conclusions
- **LS(17,12):** every odd sequence Y over C_34 of length at least42 with no zero-sum subsequence of length in [26,34] has no zero-sum subsequence of length at least36.
- **LS(23,16):** every odd sequence Y over C_46 of length at least56 with no zero-sum subsequence of length in [34,46] has no zero-sum subsequence of length at least48.
- **L1 and B2-1**, only in the threshold-counterexample setting: p=6m-1 prime, m>=3, kappa=4m, Y odd of length14m satisfying (ZP_4m) and containing a zero-sum of length>=2p+2; CF data is with respect to the dominant generator g0. L1 forces a shortest long zero-sum to have length2p+2 and supplies W*<=U of residue-1 and |W*|>=delta0+2. B2-1 excludes delta0=1 there. It does not prove LS(p,4m) for all m.
- The isolated Sublemma(a) retains its explicit zero-sum-free, length2m+3 and forbidden-residue hypotheses. It is an elementary part of B2-1's proof, not an imported inverse theorem.

## Governing evidence
- [Proof v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LS-BASE2-cells-v2.md) `fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306` read through [consolidated erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-BASE2-consolidated-v1.md) `05749bc842c94cc628d05383d301551d62255adede75c5f1876295180afd780b`. Frozen earlier versions remain historical.
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BASE2-cells-codex-v1.prompt.stdout.txt) `c5881387dcbfc9a9800827c8d4fa64cb90ace805e358c1a6b4d1fafb531f5710`: observed gpt-6.1-sol/max, all4 ACCEPT, no findings requiring repair.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BASE2-cells-claude-v1.prompt.note.md) `c940e636258e406c04cc1b989b493fdbd20b2127eb541fb45bd6a35c4856cb05`: observed claude-opus-5-5/max, no mathematical gap, only editorial/shared/optional MINORs. Do not add per-claim counts: some findings are shared.
- Parent read the full118-line proof and the full consolidated erratum. Checks included threshold14m, CF lower bound delta0>=1, L1 parity, occurrence-disjoint complements, the B=4m pair/triple wrap windows, the p=23 signed-sum argument, both index-one length thresholds and the p=23 delta'=1 residue-interval contradiction. These are written derivation checks, not executed enumeration.

## Disposed findings and import boundaries
G1/G2 now pin delta0>=1 to CF(a), RED to `23d1a488…`, and general-r greedy to the accepted LS+ chain `4005007f…` / C4 `f1573d6c…`; both required inequalities S'<=p-1<p+1<=2|U'| are explicit. B-1/B-2 make wraps and the lifted-pair triple bound explicit. B-3 restricts B2-1 to threshold CF data. S2-1 isolates the exact elementary sublemma before applying it to U'; S2-2 marks the unused bound; S2-3 states the negative signed sum=-q>=-1. L1 specifies ord(g0)=2p and coefficients2mu+1. No result was strengthened.

Index-one is used at n=p only where the appended minimal zero-sum has length>=floor(p/2)+2: at p17 lengths10 or12; at p23 length11+delta'>=13. It is NOT used in the p23 delta'=1 branch. SLZ3 bounds only a shortest long zero-sum, not the ambient sequence. AP' uses the corrected D1 proof. CF(b)/R4 is internal to the accepted I-small import; L1 uses its direct coefficient identity. No inaccessible Zeng–Yuan or additional Savchev–Chen theorem is imported.

## Progress and open remainder
These cells lie outside the accepted LS-lin band:17<6*5-10 and23<6*7-10. That establishes new coverage relative to this lane, not novelty. Neither LS+ nor STAB at these cells is claimed. S3, the general BASE2 family, remains unproved; `proof-S3-lowdefect-core-v1.md` is a separate conditional candidate, not included in this verdict. Priority/applicability increment is pending; no matched-SOTA or major-contribution claim.
