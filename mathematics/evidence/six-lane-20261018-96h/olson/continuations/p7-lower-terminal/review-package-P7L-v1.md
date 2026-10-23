# Review package P7L v1 (p = 7, terminal k = 8, kappa_hat in {1,2})

Owner OlsonThirdCutWindow (reassigned math2 slot, Olson lane). Written after /bin/date 2026-10-20T06:21:03-0700.
Status: CANDIDATE_UNVERIFIED written mathematics; no model review has been run by this owner (the parent runs all reviews
and verdicts). No novelty, priority, "first", Lean, human-referee or runtime claim. TCW (unaccepted) is not a premise.

## 1. Claims under review (each cell separately)

- Cell (2,7): THEOREM P7L-2 (proof-P7L-v1.md Sec. 0 and Sec. 2). No word of length 26 over D_14 without an identity
  14-subword (increasing original index order) has an admissible normal form with terminal k = 8 and kappa_hat = 2.
  Status: PROVED (candidate); no failing lemma.
- Cell (1,7): THEOREM P7L-1 (proof-P7L-v1.md Sec. 0 and Sec. 3). The same with kappa_hat = 1.
  Status: PROVED (candidate); no failing lemma.
Antecedent in both: the full existential one (SOME admissible NF; extra reflection pairs anywhere in the odd blocks;
genuine empty-run rule; no o_F, nonempty-run, rotation-pair or rigidity hypothesis). Read with erratum-1 (process count
and two clarifications; no statement change).
Not claimed: kappa_hat = 0 (K0T) and kappa_hat = 3 (R7) are not re-proved; every other kappa_hat at p = 7; nonterminal k;
the whole of p = 7; any other prime (neither route is claimed beyond p = 7); reflection rigidity; INV*; o_F assembly;
full ordered Olson; multiset-only statements outside the antecedent.

## 2. Files (this directory)

| File | Bytes | SHA256 |
|---|---|---|
| P7L-scope-v1.md (frozen 2026-10-20T05:53:51-0700, before any derivation) | 8794 | a1f2f6835c71b2a96a2062f830032144a2d5e590adf65864c1307e87db1113f3 |
| proof-P7L-v1.md | 37053 | 7e8bee08dacb10a9b4dd373dc9e57e526a21bd4bc77e91a41091b8e88cacb7e8 |
| erratum-1-proof-P7L-v1.md | 1127 | f5a6782742b5b25b3daca039b29c5e5049da53b36404c77fb7d62cd50827d910 |
| review-excerpts-P7L-v1.json (manifest, 16 entries) | 3685 | ffcfada8a77ae032db314a853e0900faaf34386923c98030b4ec1c0a4875733b |
| checkpoints/cp-01.md | 1998 | f753bedf13d10a9153d0acf93e05d5cdf06950f16ffca3f49ed1866c1af43eb3 |
| checkpoints/cp-02.md | 2151 | 2f1fb7adaa0c0c76a676006c9d6da01f287df2590444e8eaf764413e3d3d423b |
| checkpoints/cp-03.md | 648 | 96dcce39f19f0beda18a720aa1a1cb1942098f8b8b1747f06c0cfc93890481f5 |
| checkpoints/cp-04.md | 512 | bc362ab85a50040337ccbd566d24d53108d6f214a84822c49871bb45a4ccee1f |
| checkpoints/cp-05.md | 811 | 7d378feb15ae8a6f7b6719ad2fc17345956054cb57fa1238cfd39c4e61d4f86a |
This package and the closing checkpoint cp-06 are hashed in cp-06 and in the owner's final report.

## 3. Manifest

review-excerpts-P7L-v1.json (sha256 ffcfada8a77ae032db314a853e0900faaf34386923c98030b4ec1c0a4875733b): 16 entries
{path, sha256, start, end}, absolute paths, inclusive LF ranges: proof (1-381), erratum-1 (1-13), scope (1-96), authority
transition (1-42), NF (proof-ROT-few-E-v4.md 28-43), GRX (7-20), SC0 (1-11), FB verdict (1-16), proof-FB (9-24), FB
erratum 1 (1-7), balfull (S') extension (26-34), (S1) definition (zx-s1c line 19), LOWER parent erratum (1-10), FCW parent
erratum (1-14; derivation patterns only), R7 verdict (1-23) and K0T verdict (1-20) (context: NF/GRX used at p = 7).
Raw excerpt size about 70.6 KB in 689 lines (whole-file entries from wc byte counts; partial ranges from the byte counts
measured for the identical files, hashes and ranges during the TCW packet). Every hash was re-checked with
shasum -a 256 at 2026-10-20T06:20 and equals the scope/proof records.
Not in the manifest (context or untrusted; hashes in proof Sec. 6): FCW, SCW, USK and LOWER-K1 verdicts; the FCW, SCW and
TCW proof texts; PL (not imported at p = 7).

## 4. Premises actually used (each at its accepted scope)

NF (Sec. 0 at p = 7, as in the accepted R7 and K0T verdicts); GRX if-direction (Lemma 1); SC0 through Y'z (Lemma 3(c));
ZSTRUCT and Lemma FB in (S') at (k',kappa') = (6,1), only for kappa = 2, t = 1 (Lemma 3(d)); the (S1) definition; the
LOWER parent erratum conventions. Everything else (windows, frame counts, light side, density, margin, zero-signed sets,
representatives, additivity, complements, theta, connectivity, sorting) is proved in the text at p = 7.
NOT used: PL (p >= 11) in its entirety; Theorem P; B0S-CJ'''; S1(a); the Setting fact; FB-E; every FCW, SCW, USK, K1, K2,
K3, R7 and TCW lemma.

## 5. Where a reviewer should look first

- Lemma 9: the common lift principles at p = 7 (all windows satisfy lo >= 0 >= hi and x+y <= 2; pair-independence of
  theta from 2(14-R) < 14; complements via the enlarged interval [2Pi0, 28-2nu0]).
- Cell (1,7), Sec. 3: Lemma 3.1(ii) (the m = 1 window [2,8] realises every even value of a two-signed singleton, v = 0
  by Z0) and (G2)-(G3) (f constant on all proper nonempty sets except S_ev, S_od; f0 = 0 via {0},{2},{0,2}); the final
  sum over all eight singletons.
- Cell (2,7), Sec. 2: (F3) (the FCW-form pair {0,3,6}, {1,4,7} has union of m = 2, joined to Fp by deleting run 7) and the
  CLAIM (one exceptional alternating set at most; empty-run evenness when nu0 = 0).

## 6. Process disclosure

- Freeze: P7L-scope-v1.md created at 2026-10-20T05:53:51-0700 (date taken immediately before mkdir and creation), before
  any derivation. Pre-freeze exposure (scope Sec. 4): my whole previous TCW assignment (FCW/SCW/inputs read; TCW derived),
  the Main IRC assignment and the transition including the parent's untrusted route notes, ONE brief unwritten arithmetic
  observation (7 = 4*2-1, so (2,7) is the kappa = 2 member of the FCW family below FCW's range; PL's range p >= 11
  excludes p = 7), shasum/wc/ls metadata, and the harness memory summary. The SCW and R7 verdict texts were read only after
  the freeze (cp-01).
- Machine steps: /bin/date before every timestamp; shasum -a 256; wc -c -l; ls; mkdir of this directory and
  checkpoints/; reading files; exclusive creation of drafted text with Python open(path,'x'). The proof was drafted by hand
  in six in-memory parts with two rewording replacements before its single creation (erratum-1 item 1 corrects the count
  printed in the proof). No assert statement of any kind, no parsing or checking of mathematical objects, no script,
  enumeration, solver, test, Lean, model CLI, nested agent, network, /tmp, deletion, commit or push. No file was edited,
  overwritten, moved or deleted.
- Checkpoint cadence: freeze 05:53:51; cp-01 06:04:03 (612 s); cp-02 06:09:40 (337 s, both sub-cases recorded before
  drafting); cp-03 06:12:17; cp-04 06:13:32 (after the (2,7) draft); cp-05 06:17:52 (after creation of the proof); all gaps
  below 1200 s. No output was lost in this assignment.
- Exposure use: the parent's untrusted notes were not premises; proof Sec. 4 (M1)-(M2) records how they compare with the
  chosen routes (kappa = 2: a different additive pair; kappa = 1: the singleton route avoids the tight top-two sorting).
