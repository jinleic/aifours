# n8 assembly qualification correction r1 — mandatory addendum

Read with the unchanged frozen assembly `N8_ASSEMBLY.r1.md` SHA
`8c9cf1c2cc079e2bfdbab8bd6e0a2c9a79268a534fb4043f9ad1028820fea986` and link registry
`2b727fde73816970724ff560c8384ed1ce3293caec36c3ce5e5d449686e21798`.
This addendum SUPERSEDES any interpretation there that the existing GA parent receipts are fully protocol-qualified.

## 1. Authoritative correction and exact status change

Parent `R/moqls8-parent-replay-provenance-correction-v2.md`, SHA256
`a4b511195f64e0f8cfe2f8d0fe7ccc0bac278bec0859a9d3897c8de612b47b70`, withdraws the interpretation that
omitting proof-stream SHA256 was only a clarification. The retained F4 contract requires a proof SHA256 and byte count.

The twelve GA direct inputs and the observed P1-B1.M2 native verification remain **observations of successful
native verification against measured, bound CNFs**. They are not declared false, SAT or physical counterexamples.
But the discarded proof streams had no recorded SHA256, and no historical digest can now be recovered or backfilled.
Their protocol status must be **PROOF_DIGEST_MISSING / QUALIFICATION_INCOMPLETE**, not fully accepted F4 evidence.

Consequences for assembly links D12 and S6:
- Keep their native status/log/feed observations, receipt hashes and all historical parent verdicts immutable.
- Do NOT count those receipts as protocol-complete final-gate refutations solely from the old acceptance wording.
- Require fresh conforming evidence, or a later separately explicit authorised protocol exception as the parent
  correction states; none is granted by this note. The new hashing/counting relay requires its own source review
  and controls. Do not assume that its later source supplies missing hashes for older discarded streams.
- No final n8 conclusion is currently protocol-complete. Mathematical reduction/normal-form statements and
  input-byte identities are separate links, not invalidated or certified by this provenance correction.

## 2. Independent second-encoding gate is also load-bearing

Frozen contract `R/../screening/phys-1-moqls8-problem16-contract.json`, acceptance.positive_answer, requires
“two independently written encodings for every exhaustive step”, together with the stated exact/proof-certified
computation and written exhaustive reduction. GA alone cannot close that requirement. The older K3 route used
A with DRAT and independent B with kissat status; that history is not a new protocol-completeness judgment here.

The NEW GB source-preparation package uses untouched gram_b_r2.py4b593e55…eae0 and its own literal names,
P4 only for Q1, SB2/G5 and no ROWLEX. Its planned16+6 formulas must be independently mapped/bound and receive
qualifying evidence under the parent's final contract interpretation. Construction, hashes, a relaxed classical
control or an unqualified future solver status do not alone settle the gate. No GB result is claimed in this note.

## 3. Current conditional conclusion

The implication toward “every5MOQLS(8) is classical” still needs ALL accepted mathematical/byte bindings,
normal-form coverage and its remaining review dispositions, conforming evidence closing all16 original leaf
obligations (directly or through the accepted six-formula transfer), the independent-encoding obligation and a
final parent reconciliation. At present the missing proof-digest provenance and the incomplete GB counterpart
are explicit blockers, in addition to any still-pending solves/reviews. No theorem, novelty claim, weakened
formula/checker, skipped case or reduced resource limit is authorised by this addendum.
