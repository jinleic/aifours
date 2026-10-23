# SW(25,16) post-result priority screen (scout report, verbatim)

Recorded 2026-10-17 14:13:16 PDT from read-only scout `SW25Priority`. The parent independently read the DataCite record of doi:10.5281/zenodo.23404962 (state findable; registered 2026-10-15T20:42:34Z; creator Long, Griffin; title "Symmetric weighing matrices SW(25,16), SW(27,16) and SW(29,16)"; resourceTypeGeneral Preprint).

**Outcome: PRIOR-ART.** Our SW(25,16) cannot claim priority. Someone else publicly claimed explicit symmetric weighing matrices SW(25,16), SW(27,16) and SW(29,16) about two days before the lane's witness was found: Griffin Long, Zenodo preprint doi:10.5281/zenodo.23404962 (concept DOI 23404961), issued 2026-10-15, registered 2026-10-15T20:42:34Z. That is about 48h06m before the witness solve ended at 2026-10-17 13:48:53 PDT (`producer-receipt-v1.json:30-31`). The pre-freeze screen missed it. The record has no references, so the screen's citer sweeps could not see it; I found it through a full-text search on OpenAlex and DataCite.

I could not open Long's certificate: every Zenodo endpoint returned HTTP 403. So I have not checked whether his matrix is valid or whether it is equivalent to ours. The construction method is also prior art. Ben-Av et al. (2024) built the non-symmetric W(25,16) from 5×5 circulant blocks over an integer weighing matrix IW(5,16), and Goldberger et al. (2026) describe that lift.

## Evidence table
Web reads were done around 2026-10-17 20:57–21:00Z, going by the arXiv feed timestamps. I had no shell, so there is no host-clock stamp.

| Source (version/date) | Access | Quote (≤40 words) | Applicability to exact SW(25,16) |
|---|---|---|---|
| Long, Zenodo 10.5281/zenodo.23404962, issued 2026-10-15 | Only the abstract and metadata, via the DataCite API, OpenAIRE Graph and OpenAlex. The record page, API, OAI-PMH and files all returned 403 | "We exhibit symmetric weighing matrices SW(25,16), SW(27,16) and SW(29,16)… Each matrix was found by a SAT search in which a signed-permutation automorphism of a chosen cycle type was prescribed. Existence is established by the explicit certificates" | **Direct prior claim.** Same object, and the same method class: SAT with a prescribed automorphism. The cycle type is not disclosed. It also pre-empts the lane's alternates, n=27 and n=29. |
| Rosin arXiv:2505.23881, v1 (29 May 2025); the arXiv API still lists v1 as latest | Body | "This paper's results include construction of a w = 16 n = 22 Symmetric Weighing Matrix, resolving this open instance and leaving n ∈{25,27,29} as the remaining open instances for w = 16." | Shows the case was listed open as of May 2025. Not a construction. |
| Rosin arXiv:2501.17725 v1, Table 2 | Body (table layout garbled in extraction) | Row "(23,16)? (25,16)? (27,16)? (29,16)? (28,25)?" in the column of the Handbook's smallest open instances | Secondary attestation that the 2006 Handbook (Table 2.88) listed it open. |
| Rosin, NeurIPS-25 MATH-AI workshop paper (OpenReview WlXSZiqcbH); constructive.codes | Paper **blocked** by a bot check on the forum, PDF and API pages. Site read | Site: "This is an updated brief workshop paper that summarizes the results in the preprints below." | [INFERENCE] No new SW(25,16). The repo commits of 2025-12-03 changed only the README. |
| CPro1 repo, main branch, latest commit 827f02b (2026-06-03) | Repo read | `OPEN_INSTANCES = [[19,9], [21,9], [22,16], [23,16]]` | The symmetric-weighing designs folder holds only 19-9, 21-9 and 22-16. Commits after May 2025 touch code and README only. Not applicable. |
| Ben-Av, Dula, Goldberger, Kotsireas, Strassler, Discrete Math. 347:113908 (2024) | Abstract from the Bar-Ilan CRIS page; ScienceDirect body 403 | "We solve the smallest four open cases of weighing matrices, W(n,16) for n=23,25,27,29… The study of partitioned group matrices generalizes some well known constructions, namely … block circulant matrices" | Gives the **non-symmetric** W(25,16) only. Method prior art for our block-circulant model. |
| Goldberger, Ben-Av, Dula, Strassler arXiv:2603.17552v1 (18 Mar 2026) plus the assafg-dev repo (latest commit 2026-06-08) | Body (§1, Prop 5.2, Cor 5.3, refs) and repo | "The authors [4], have used this method to construct W(25,16) from a certain IW(5,16)." / "There exist symmetric weighing matrices SW(23,16), SW(30,17), SW(28,25)" / "…IW and W matrices are abundant" | Describes the IW-quotient lift and a criterion for finding a symmetric member of a class. **Does not claim SW(25,16).** The repo has no SW25 file and no IW(5,16) classification. |
| Dinitz, "New Results in Part V" (live, "Last edited 2/15/18"); Munemasa wo.htm (live, "Last modified February 2, 2017") | Pages read | "Weighing matrices W(n,w) for w = 16 have been found for the four values of n that were previously unknown." / "symmetric W(23,16) found by Giora Dula, Assaf Goldberger and Yossi Strassler" | Only W(23,16) is posted in symmetric form. The posted W(25,16) is not symmetric. The lane's B1 run says it is not equivalent to any symmetric matrix (DRAT-checked, `README.md:189-193`; producer claim, not reviewed by me). |
| Adin–Epstein–Strassler, math/9910164 (1999) | Abstract | "It turns out that the order must be an odd multiple of either 21 or 31." | No circulant W(25,16), so no back-circulant SW(25,16). |
| Arasu–Hollon, Australas. J. Combin. 55 (2013), Table 14 | Body, table rows | "'.' denotes previously known non-existence; 'N' denotes non-existence given in this paper"; Z25: k=16 '.', Z5×Z5: k=16 'N' | No W(25,16) developed over either group of order 25, so no group-developed or back-developed SW(25,16). |
| Egan–Ó Catháin–Švob arXiv:2607.16069v1 (Jul 2026) | Partial body | "We also found a symmetric W(21,9), listed as an open case in the Handbook of Combinatorial Designs" | Their order-25, weight-16 matrix is complex (cube roots of unity), not real. No real SW(25,16). |
| Valtonen arXiv:2608.06920v2 (Sep 2026); Tan arXiv:2608.18468v2; Goryainov et al. arXiv:2512.16653v1 | Text search | Valtonen: "The extension of the algorithm to weighing matrices is also described" | No (25,16) result in any of them. |
| Georgiou–Stylianou–Alrweili, Mathematics 11:2076 (2023) | Abstract via DOAJ; body blocked (MDPI and Academia 403, Figshare has no files) | "The first of the infinite families includes a symmetric weighing matrix of order 30 and weight 25." | Their families have even orders. Not applicable. |
| Topno–Saurabh, NNTDM 31(3) (2025) | Body | "The smallest open case for symmetric weighing matrix with weight 16 is SW(22,16) (see [3, Table 2.88]), which is settled in this note." | Their Theorem 3.1 gives SW(2v, v+t), always even order. Not applicable. |

## Other families I checked
None of these yields SW(25,16):
- **Kronecker products.** W(5,4) cannot exist: odd order requires (n−w)²−(n−w)+1 ≥ n, which gives 1 ≥ 5.
- **Direct sums.** Each block would need order at least 16, which cannot fit in 25.
- **Zero-diagonal forms** (Seidel or signed-graph matrices, conference matrices). These need trace 0. Here trace = 4(p−q) with p+q = 25 odd, so the trace is never 0 (lane fact F1).
- **Kharaghani–Pender–Suda 2022, Theorem 4.** For weight 16 it gives orders 5n−4 or 15n−14, which can never equal 25 (my arithmetic).
- **Dula–Goldberger cohomology-developed matrices.** Their symmetric example is SW(15,9); nothing at order 25.

## What our matrix still adds
- **Same object, same method class.** By the lane's own lemmas F5 and F7 (`facts-v1.md:36-71`, not reviewed by me), any order-5 symmetric automorphism of an SW(25,16) is conjugate to the 5^5 type we used. So if Long used order 5, the two models coincide up to conjugacy. His abstract does not say which type he used.
- **Structure of our witness**, read off by hand from `certs/sw25-16-witness-v1.circulant-first-rows.txt` (recompute this mechanically before citing it):
  - The block-sum quotient is B = [[3,1,−2,1,−1],[1,−1,2,−1,−3],[−2,2,0,2,−2],[1,−1,2,3,1],[−1,−3,−2,1,−1]].
  - B is symmetric, B² = 16I and trace B = 4, so it is a symmetric IW(5,16).
  - The diagonal blocks are symmetric circulants and A_ji = A_ij^T.
- **Equivalence to Long's matrix is unknown.** Even if the two turn out inequivalent, "a second inequivalent example" is a minor addition.
- **Significance.** This was an exact open table entry, not a corollary of any family above. It is narrow, though: the solve took 6.06 s under a natural symmetry. After 2026-10-15 it amounts to independent confirmation, not a resolution.

## Limits
- Blocked: Zenodo (record, API, OAI-PMH and file URLs all 403; Wayback returned 503), OpenReview, the Ben-Av et al. 2024 body on ScienceDirect, the Georgiou 2023 body, the Lampio–Ganzhinov classification slides (TLS error), and Munemasa's matrices index page (403; wo.htm itself read fine).
- Not read: the Handbook's Table 2.88.
- Not seen: whether the closed body of Ben-Av et al. 2024 contains other W(25,16) classes.
- None of the lane's own claims (B1, F7) were independently replayed here.

## Defensible wording
> "We obtained an explicit SW(25,16) (sha256 bfadf445…d4ab0) by SAT search over matrices invariant under a fixed-point-free order-5 permutation (cycle type 5^5): a symmetric 5×5 array of 5×5 circulants whose block-sum quotient is a symmetric IW(5,16). Existence of SW(25,16) was publicly claimed earlier by G. Long (Zenodo, doi:10.5281/zenodo.23404962, issued 2026-10-15), also via SAT with a prescribed signed-permutation automorphism; we have not compared the two matrices. The block-circulant method follows Ben-Av et al., Discrete Math. 347 (2024) 113908. Rosin (arXiv:2505.23881v1) listed n=25 as open in May 2025."

Do not use "first", "new", "resolves", "previously unknown", "inequivalent" or "novel".

## What you should do next
1. Get Long's files through a browser and pin their SHA-256.
2. Check his SW(25,16) with a checker written from the definition.
3. Run the lane's signed-permutation equivalence test (`code/equiv_cnf.py`) between his matrix and ours. Only a DRAT-certified UNSAT allows the word "inequivalent".
4. Mark SW(27,16) and SW(29,16) as pre-empted as well.

```json
{
  "outcome": "PRIOR-ART",
  "basis": "Public dated existence claim with explicit certificates: Long, Zenodo doi:10.5281/zenodo.23404962 (concept 10.5281/zenodo.23404961), issued 2026-10-15, DataCite registered 2026-10-15T20:42:34Z; certificate bytes unread (Zenodo HTTP 403)",
  "our_witness": {
    "path": "institute/runs/six-lane-2026-10-16/review/sw25-parent-inputs-v1/sw25-16-witness-v1.sw",
    "sha256": "bfadf44596bc5138106432690bf507a8ff9c36cd3c40eb8eeb08195a9b2d4ab0",
    "found": "2026-10-17 13:48:47-13:48:53 PDT (producer-receipt-v1.json:30-31)",
    "model": "unsigned automorphism of cycle type 5^5; symmetric 5x5 array of 5x5 circulants, A_ji = A_ij^T",
    "quotient_B_hand_derived": [[3,1,-2,1,-1],[1,-1,2,-1,-3],[-2,2,0,2,-2],[1,-1,2,3,1],[-1,-3,-2,1,-1]],
    "trace_W": 20,
    "trace_B": 4
  },
  "timing_gap": {
    "long_registered_utc": "2026-10-15T20:42:34Z",
    "lane_freeze_utc": "2026-10-17T20:24:13Z",
    "witness_end_utc": "2026-10-17T20:48:53Z",
    "gap_to_witness": "48h06m19s"
  },
  "prior_claim": {
    "author": "Griffin Long (Independent researcher)",
    "type": "Zenodo preprint, CC-BY, not peer reviewed, produced by an AI agent (agent-afk) under the author's supervision",
    "claims": ["SW(25,16)", "SW(27,16) x2", "SW(29,16)"],
    "method": "SAT search with a prescribed signed-permutation automorphism of a chosen cycle type (cycle type undisclosed in the abstract)",
    "access": "abstract and metadata only (DataCite, OpenAIRE, OpenAlex)",
    "validity_checked": false,
    "equivalence_to_ours": "unknown"
  },
  "method_prior_art": [
    "Ben-Av, Dula, Goldberger, Kotsireas, Strassler, Discrete Math 347:113908 (2024): partitioned group matrices including block circulants; non-symmetric W(25,16)",
    "Goldberger et al. arXiv:2603.17552v1: W(25,16) built from an IW(5,16) by circulant-block lift; Prop 5.2 symmetric-member criterion; Cor 5.3 does not include n=25"
  ],
  "no_claim_found_in": [
    "Rosin arXiv:2505.23881v1 (lists n=25 open)",
    "Rosin arXiv:2501.17725v1",
    "CPro1 repo through commit 827f02b (2026-06-03)",
    "Goldberger repo through 2026-06-08",
    "Dinitz page (last edited 2/15/18)",
    "Munemasa wo.htm (last modified 2017-02-02)",
    "Egan-O Cathain-Svob arXiv:2607.16069v1",
    "Valtonen arXiv:2608.06920v2",
    "Tan arXiv:2608.18468v2",
    "Goryainov et al. arXiv:2512.16653v1",
    "Topno-Saurabh NNTDM 31(3) 2025",
    "Georgiou et al. 2023 (abstract only)",
    "arXiv API abstract search, OpenAlex and DataCite queries"
  ],
  "families_excluded": {
    "circulant_or_back_circulant": "Adin-Epstein-Strassler 1999: no CW(25,16)",
    "group_developed_order_25": "Arasu-Hollon 2013 Table 14: Z25 '.', Z5xZ5 'N'",
    "kronecker_or_direct_sum": "W(5,4) impossible; direct-sum blocks need order >= 16",
    "zero_diagonal_seidel_signed_graph": "trace must be nonzero at odd n (lane fact F1)",
    "known_infinite_families": "Georgiou 2023, Topno-Saurabh 2025, KPS Theorem 4 never give order 25 with weight 16"
  },
  "blocked": [
    "Zenodo record, API, OAI-PMH and files (403)",
    "OpenReview WlXSZiqcbH (bot check)",
    "ScienceDirect body of Ben-Av et al. 2024 (403)",
    "MDPI, Academia and Figshare copies of Georgiou 2023",
    "Lampio-Ganzhinov slides (TLS error)",
    "Munemasa matrices index (403)",
    "Handbook Table 2.88 (not read)"
  ],
  "significance": "Exact open table entry before 2026-10-15, not a corollary of any family checked; narrow and computationally light. Now only an independent confirmation.",
  "defensible_wording": "independent construction of an SW(25,16) invariant under a 5^5 automorphism; existence previously claimed by Long (Zenodo, 2026-10-15); no priority or inequivalence claim",
  "forbidden_wording": ["first", "new", "resolves open case", "previously unknown", "inequivalent", "novel"],
  "parent_actions": [
    "Fetch Long's certificates via a browser and pin their SHA-256",
    "Check them with a definition-first checker",
    "Run the signed-permutation equivalence test (equiv_cnf) between his SW(25,16) and ours; claim inequivalence only on DRAT-certified UNSAT",
    "Mark SW(27,16) and SW(29,16) as pre-empted"
  ],
  "writes": "none; no solver or model CLI used; no external contact"
}
```
