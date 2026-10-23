# BASE2 erratum 1 (consolidated): full hypotheses, source pins, explicit wrap checks and signed sums

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T08:37:16-0700. This disposes both reviews frozen in run
review/olson-BASE2-cells-review-freeze-v1.json (991e6317edc02f86f5c2716e65d2ecf107fb796872f90efb6a2a49a888bdc8b8):
- Codex: review/olson-BASE2-cells-codex-v1.prompt.stdout.txt, SHA256 c5881387dcbfc9a9800827c8d4fa64cb90ace805e358c1a6b4d1fafb531f5710;
  all four claims ACCEPT, 0 FATAL / 0 MAJOR / 0 MINOR requiring repair.
- Claude: review/olson-BASE2-cells-claude-v1.prompt.note.md, SHA256 c940e636258e406c04cc1b989b493fdbd20b2127eb541fb45bd6a35c4856cb05;
  no mathematical gap; editorial/nonblocking MINORs G1, G2, L1-1 (optional), B-1, B-2, B-3, S2-1, S2-2, S2-3 (optional).

Governing source (unchanged): proof-LS-BASE2-cells-v2.md, SHA256
fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306. Read the source through this erratum: replacements below govern where they
conflict. In Old quotations source line breaks are joined by spaces. No theorem statement is strengthened, no new external
result is imported and no proof strategy is changed. Sublemma (a) below isolates the elementary argument already written and
used in the source; it is not a newly imported inverse theorem. Both optional explicitness repairs are adopted. All results
remain CANDIDATE_UNVERIFIED until the parent verdict. No S3 result or the separate conditional S3 file is used here.

## E-G1: lower bound on delta0 (Claude G1, source line 23)
Old: 'By LS-II' Y is in case (I) of the dichotomy: 1 <= delta0 <= e - 2 = 2m - 3 and r := |U| = p - 2e + 1 + delta0 = 2m + 2 + delta0.'
New: 'By LS-II' Y is in case (I) of the dichotomy: delta0 <= e - 2 = 2m - 3 and r := |U| = p - 2e + 1 + delta0 = 2m + 2 + delta0;
moreover delta0 >= 1 by CF(a), since (ZP_kappa) forces M <= 2p - 1 and delta0 = 2p - M.'

## E-G2: full RED and general-r greedy authority pins (Claude G2, source Sec. 0)
Old: 'RED (review/olson-KPS-SLZ-parent-verdict-v1.md): LS(p, kappa) fails iff some odd Y of length exactly p + 2kappa + 1 has (ZP_kappa)
and a long zero-sum.'
New: 'RED, accepted in /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-KPS-SLZ-parent-verdict-v1.md,
SHA256 23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612, accepted statement 4 (line 11), source/overlay pins at line 16:
proof-SLZ-EXT-v2.md (2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751, statement lines 28-31) read through
proof-SLZ-EXT-v2-erratum-1.md (907b3d06dd2ac93686ea4f49cf812dfd41f80f9abdefa6fd2d4398821c234daa, lines 14-25, especially the shrink repair E-2).
At the present parameters 1 <= kappa <= p - 2, LS(p, kappa) fails iff some odd Y of length exactly p + 2kappa + 1 has (ZP_kappa)
and a long zero-sum. Failure of (S1) is not assumed hereditary.'

Old: 'the greedy step of proof-LSplus-e2-v1.md Sec. 3 (C) (part of item 4, as used in the LS+ chain verdict with r := |U'|).'
New: 'the greedy step of proof-LSplus-e2-v1.md Sec. 3 (C), source SHA256
2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1, lines 51-54 (part of delta verdict item 4), with its general-r application
accepted in /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LSplus-chain-parent-verdict-v1.md,
SHA256 4005007f4e073386236016b62949cba925cb5cde12ba13c24ce27b2a2c351b55, read through its governing
erratum-1-lsplus-chain-consolidated-v3.md (f1573d6c8b1ac00afe3ce438ff5ebca64cce1e4c2682aaf3ef01e18831a608c0), C4, especially lines 63-65:
apply with r := |U'| and S := S', checking S' <= p - 1 < p + 1 <= 2|U'|. Here the two applications check
S' <= 16 < 18 <= 2|U'| at p = 17 and S' <= 22 < 24 <= 2|U'| at p = 23, delta' >= 2. This imports the accepted greedy argument,
not the out-of-range LS+-RED theorem.'

## E-L1: generator order and coefficients (Claude L1-1, optional, adopted; source lines 31-32)
Old: 'Write T = g^i W*, W* <= U, i <= M. Its g-coefficient sum i + |W*| + 2sigma_int(W*) = 2p + 2 + 2sigma_int(W*) (sigma_int: the
integer sum of the mu) is = 0 (mod 2p)'.
New: 'Write T = g^i W*, W* <= U, i <= M, identifying W* with the corresponding occurrence subsequence of the non-g terms of Y.
DGM-p gives ord(g) = 2p, and CF gives the coefficient c = 2mu + 1 for every such occurrence. Thus its g-coefficient sum
i + |W*| + 2sigma_int(W*) = 2p + 2 + 2sigma_int(W*) (sigma_int: the nonnegative integer sum of the mu) is = 0 (mod 2p)'.
The direct coefficient argument is retained; no extra application of CF(b) is inserted. CF(b)/R4 is used only internally to
the accepted I-small import, as both reviewers noted.

## E-B3: restrict B2-1 explicitly to threshold-counterexample CF data (Claude B-3)
Source line 34, Old: '## 2. Lemma B2-1: at every BASE2 cell, delta0 = 1 is impossible'
New: '## 2. Lemma B2-1: for a threshold LS counterexample at a BASE2 cell, with CF data w.r.t. g0 (Sec. 1 setting), delta0 = 1 is impossible'
Source line 112, Old: 'and Lemma B2-1 at every BASE2 cell.'
New: 'and Lemma B2-1 for threshold LS counterexamples at every BASE2 cell, with CF data w.r.t. g0 as in Sec. 1.'
In full: p = 6m - 1 prime, m >= 3, kappa = 4m, Y odd of length 14m with (ZP_4m) and a zero-sum of length >= 2p + 2; the lemma
excludes delta0 = 1 w.r.t. the dominant generator g0. This is a restriction made explicit, not LS(p,4m) for every m.

## E-S2-1: isolate Sublemma (a) at its exact elementary hypotheses (Claude S2-1; source lines 36-40 and 101-102)
Old (B2-1(a)): '(a) A := Sigma(U) u {0} (Sigma: nonempty subset sums), sigma := sigma(U). Prefix sums of the zero-sum-free U
(any order) are distinct and nonzero, so |A| >= 2m + 4. Complementation W -> U - W gives A = sigma - A. A avoids [1, 2m - 2],
hence also [sigma - 2m + 2, sigma - 1]. As sigma is in Sigma(U), sigma is not in [0, 2m - 2]. If sigma >= 4m - 3, the two arcs
are disjoint (sigma - 2m + 2 >= 2m - 1) and lie in [1, p - 1], so |A| <= p - (4m - 4) = 2m + 3: contradiction. So
2m - 1 <= sigma <= 4m - 4, the arcs merge into [1, sigma - 1], and A <= {0} u [sigma, p - 1].'
New: '(a) Sublemma (a) (the elementary argument here isolated with all its hypotheses). Let p = 6m - 1 be prime, m >= 3.
Let V be zero-sum-free over Z_p, |V| = 2m + 3, with no nonempty subset-sum residue in [1, 2m - 2]. Put
A_V := {0} u Sigma(V), sigma_V := sigma(V), taking sigma_V in [0, p - 1]. Then
  sigma_V in [2m - 1, 4m - 4], and A_V subset {0} u [sigma_V, p - 1].
Proof of sublemma. Zero-sum-freeness gives sigma_V != 0 and distinct nonzero prefix sums (any order); hence
|A_V| >= |V| + 1 = 2m + 4. By hypothesis sigma_V is not in [1, 2m - 2], so sigma_V >= 2m - 1. Complementation, including empty
and full occurrence subsets, gives A_V = sigma_V - A_V, so A_V avoids both [1, 2m - 2] and
[sigma_V - 2m + 2, sigma_V - 1]. If sigma_V >= 4m - 3 these are disjoint nonwrapping intervals in [1, p - 1], excluding
4m - 4 residues and forcing |A_V| <= p - (4m - 4) = 2m + 3, a contradiction. Otherwise their union is [1, sigma_V - 1], proving
the claimed containment and the upper bound sigma_V <= 4m - 4. End of sublemma.
Apply it here to V = U: delta0 = 1 gives |U| = 2m + 3, U is zero-sum-free by (F*), and (F*) excludes every nonempty subset-sum
residue in [0, 2m - 2]. Write A := A_U and sigma := sigma_U. This gives exactly the original conclusion of (a).'

Old (source lines 101-102): '(F') says no nonempty W' <= U' has rho(W') in [0, 6]; Lemma B2-1 (a) applied to U'
(same argument: |A'| >= 12 for A' := Sigma(U') u {0}) gives sigma' := sigma(U') in [7, 12] and
A' <= {0} u [sigma', 22] <= {0} u [7, 22].'
New: '(F') at delta' = 1 says no nonempty W' <= U' has rho(W') in [0, 6]. Apply the isolated Sublemma (a) with
m = 4, p = 23 and V = U': U' is zero-sum-free by maximality of Z0, |U'| = 11 = 2m + 3, and its nonempty subset sums avoid
[1, 6] by (F'). Therefore, for A' := {0} u Sigma(U'), |A'| >= 12, sigma' := sigma(U') in [7, 12], and
A' subset {0} u [sigma', 22] subset {0} u [7, 22].'
This separates the already-used elementary sublemma from B2-1's delta0 = 1 threshold hypotheses; it does not assume that U'
is itself threshold-counterexample CF data.

## E-B2: triple lower bound obtained from a lifted pair (Claude B-2; source lines 47-48)
Old: 'If t >= 4, a proper triple has integer sum in [18m - 1 - 2B, 3B]'.
New: 'If t >= 4, a proper triple contains a pair whose integer sum is p + y with y in J, hence at least
p + (6m - B) = 12m - 1 - B; adding the third term, which is at least 6m - B, gives the triple lower bound
18m - 1 - 2B. Its upper bound is 3B. Thus a proper triple has integer sum in [18m - 1 - 2B, 3B]'.

## E-B1: explicit pair/triple wrap windows at B = 4m (Claude B-1; source lines 51-52)
Old: '(e) B = 4m, J = [2m, 4m]. Two terms: z + z' in [4m, 8m] with residue in J: z + z' = 4m (z = z' = 2m)
or z + z' in [8m - 1, 8m]. A proper triple (t >= 4) has sum in [8m - 1, 10m - 1];'
New: '(e) B = 4m, J = [2m, 4m]. For an integer pair/triple sum S of terms in J (so 4m <= S <= 12m = 2p + 2), its residue is
S if S < p; 0 if S = p or S = 2p; S - p if p < S < 2p; and 1 or 2 if S = 2p + 1 or 2p + 2. Since 0, 1, 2 are outside J
(m >= 3), a residue in J forces S in J before wrapping or S - p in J after one wrap. A pair sum is in [4m, 8m], so before
wrapping it must be S = 4m (both terms 2m), and after one wrap it lies in
[p + 2m, p + 4m] intersect [4m, 8m] = [8m - 1, 8m]. A proper triple (t >= 4) is in [6m, 12m], so it cannot land in J without
wrapping, cannot hit 0 or residues 1, 2 at the second wrap, and must lie in p + J = [8m - 1, 10m - 1];'
The subsequent high-pair and surviving-triple argument is unchanged.

## E-S2-2: unused size bound (Claude S2-2; source line 86)
Old: 'every s in [0, S'] is the x-sum of some W'_s, with |W'_s| >= s - E' (E' := S' - |U'|).'
New: 'every s in [0, S'] is the x-sum of some W'_s. The accompanying bound |W'_s| >= s - E' (E' := S' - |U'|) is valid but unused
in Sec. 4.'

## E-S2-3: negative signed sum (Claude S2-3, optional, adopted; source lines 98-99)
Old: 'If -24: s* <= 16 forces sigma~(Z*) <= -8, but the negative part of Z0 has total |sum| <= 1
(signed sum 0, at most one +1): contradiction.'
New: 'If -24: s* <= 16 forces sigma~(Z*) <= -8. But the signed sum of Z0 is 0, and q <= 1 of its terms have signed representative
+1; therefore the negative signed representatives of Z0 sum to -q >= -1. Every signed subset sum sigma~(Z*) is consequently
>= -q >= -1, contradicting sigma~(Z*) <= -8.'

## Disposition and scope
All Claude findings are disposed above; Codex required no repair. Old source/proof/package/excerpt files are preserved unchanged.
L1 and B2-1 retain their threshold-counterexample setting (p = 6m - 1 prime, m >= 3, kappa = 4m, g = g0). The two full LS
claims retain the exact scope copied in the package:
- every odd Y over C_34 with |Y| >= 42 and no zero-sum length in [26, 34] has no zero-sum length >= 36;
- every odd Y over C_46 with |Y| >= 56 and no zero-sum length in [34, 46] has no zero-sum length >= 48.
No proof of the full BASE2 family S3, LS+, STAB, INV* or ordered Olson follows from this package. The candidate's Sec. 5 remains
planning context, not a classification of all unresolved cases. No novelty/priority claim. No further S3 derivation was begun
while this erratum was prepared.
