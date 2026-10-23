# PhysEpQutrit bounded handoff — resource-blocked at the 23:18:55 checkpoint

The frozen target remains determining M(7), not merely its K1/K2 cases. **M(7) is unresolved.** No exact triple
witness or unrestricted K3 exclusion has been obtained. The parent has the final theorem/integration verdict.
All scientific jobs launched by this worker have ended; parent/other-lane jobs are outside this statement.

## Retained results

1. **K1 candidate and requested corollaries.** Corrected proof `K1-THEOREM.r3.md`:
   `2d77c63719fafd1e7f7cfe2a3161931f2e90dff0976e3ee9c5083a88d076a096`.
   Parent technical routes PASS and static ACCEPT-WITH-FIXES reviews are separately recorded in the parent review
   directory; their final integration is not claimed here.
   Requested new `K1-COROLLARY.r1.md`:
   `7ded3c698163c18757a21964d3552e053f1081f9fd854895054a606e56ef6b6d`.
   It proves every 2-RQLS(7) and every PQLS(7) is classical/cardinality seven, so neither maximal-cardinality
   2-RQLS(7) nor MCPQLS(7) exists, conditional on K1. It includes the harmonic-net shear and the requested
   Ball–Simoens/Zhang–Cao prior-art acknowledgement; no priority claim.

2. **K2 producer proof package.** Both frozen encoders have all 147 class instances DRAT-verified (294 total), with
   exact `s VERIFIED`, solver/checker rc20/0 and no safety stops.
   - A inventory `evidence/gram/k2A_cert_summary_r4.json`:
     `31aa7eb25bfb760c3b71af21698612ffc6ee8c877f0507d2dd7d3cfa462ddc29`.
   - B inventory `evidence/gram/k2B_cert_summary_r4.json`:
     `ed29e3a199a650f11a10f98d0c262c5ebe4c905e68ce6de18adeee030fa20f4b`.
   - Updated candidate proof `K2-THEOREM.r2.md`:
     `a73a90078a3b9923935755d2663ecba645ba7f231d8f07384b8f34656ab532cd`.
   Parent LS147 checks supply separate technical coverage/group evidence. Parent K2 replay is assigned to
   M7K2ParentReplay; this worker does not claim that replay completed.

3. **K3 original cube partials.** The three covering types are C311, C321, C411, frozen in AMENDMENT-2. G6 singleton
   identities are already implied by G1/G2 plus cube units (`G6-G2-DERIVATION.r1.md`).
   - A/C321 certified: receipt `evidence/k3cubes/cert_r2/A_C321.json`
     `c3a30df311eff2ed9b9b5a3706c2ca03a8d4337d8663ea529a9978126fde9314`;
     CNF `d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388`.
   - A/C411 certified: receipt `evidence/k3cubes/cert_r2/A_C411.json`
     `5f117b60c6b7833978ea012b3c07921d2d19fa6d0a161c4b93d1d13cd6aa23cf`;
     CNF `2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2`.
   Both have exact verification, rc20/0, no safety stop. Independent B K3 routes are pending.
   - Original A/C311 was UNKNOWN at 1800 seconds.
   - Its residual-lex screen, on the distinct existing CNF
     `059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f`, ended **UNKNOWN safety stop** at
     23:18:55, after769.881 seconds, cooperative SIGTERM rc-15, sampled aggregate RSS527564800 bytes.
     Reason: free-space floor. Receipt: `explore/k3lex/screenA_r1/A_C311.json`. This was not a completed full-cap
     mathematical miss, and it is not UNSAT.

## Review/provenance work completed

- Corrected proof source `GRAM-ENCODING.r2.md` is also the new canonical `GRAM-ENCODING.md`:
  `c6c506a7d1ecba15b2e31393b0da4caa248db5c9227f512c0df9ea5bd07ad6c7`.
  Substantive late `LEMMAS.md`: `4bddc9d422cf989bb9bfdf4f09de72742ea2d423b9a082f8fd76263ba1c850c9`.
- `REVIEW-CORRECTIONS.r2.json` and `K2-REVIEW-DELTA.r2.json` explicitly map corrections and intentionally unchanged
  historical encoder bytes. No frozen inputs were silently rewritten.
- New matched component controls:26/26 expected outcomes, inputs/CNFs/logs/hashes under
  `evidence/gram/review_controls_r1/`; summary
  `6ce1ddc241a88da9f0d2fdc0be3551b8a73f5659a979c5034ebcee5caaecd685`.
  Their AFTER-K2/BEFORE-new-K3 chronology is explicit.
- End-to-end transport controls under `evidence/gram/transport_controls_r2/`; summary
  `34a69ae60c1f09bc4029ae9bb589b581d45204e68146af6dc4f5d54be6fd95e6`.
  Both native UNSAT streams verified; both SAT models retained/directly checked and not accepted as UNSAT;
  invalid binary proof and intentional early writer rejected. Each control's scope/count is stated separately.
- New storage-only certificate driver `code/k3_cube_certify_r3.py`
  `da9c210ebf8ab56c59a687155b8ccd106ff90fe748ff6f867ee01fc65997ac78` regenerates/hashes in memory against the
  single existing search input, without CNF duplication. A/B C321 in-memory byte-identity controls PASS in
  `evidence/k3cubes/no_duplicate_regen_controls_r1.json`. Its native transport remains the already controlled
  FIFO/RSS/checkpoint module.

## Blocker and exact continuation boundary

Parent23:17 reported12.16e9 free bytes, below the new12.2e9 launch gate. Recorded once in
`evidence/DISK-DEFERRAL-2317.json`; no disk poll followed the notice. The already-in-flight lex solver then hit its
continuous12e9 floor and stopped. No new solver/checker/enumerator/compiler/reviewer stage has been launched.
No deletion, snapshot thinning, unlink compression, proof retention or duplicate-CNF creation is authorised.
Historical K1 DRAT artifacts and pre-notice copies remain unchanged; new K2/K3 proofs were streamed only.

Await explicit parent resource release, a fresh>=12.2e9 free-space observation with projected retained growth
fitting, and headroom before the original deadline2026-10-18T18:31:43-07:00. The immediate reachable continuation is
the interrupted existing C311 lex input, using a new output directory, for example:

    ../../depolarizing/env/bin/python -B k3_screen_r2.py A ../explore/k3lex/screenA_r2 --input-dir ../explore/k3lex --cubes C311 --seconds 1800

Run from the lane's `code/`, only after those gates and without a certificate-pipeline overlap. The output name is
new; the interrupted receipt must not be overwritten. Independent B routes and any exact vector reconstruction
remain additional obligations.

If a completed C311 lex chunk is still UNKNOWN, `review/drafts/AMENDMENT-4.md` prepares proof-assisted all-frame
cardinality cuts derived from the two checked cube exclusions. That draft is **unfrozen and inactive**; no cut
CNF/search exists. Its finite local coverage controls, code, proof-composition review and freeze must precede use.
No scope is silently dropped. No claim here resolves the remaining original M(7) problem.
