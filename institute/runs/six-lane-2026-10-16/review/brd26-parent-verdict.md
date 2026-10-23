# Bhaskar Rao design BRD(26,130,25,5,4): parent verdict — verified witness of an already-claimed design

## Result

An explicit **BRD(26,130,25,5,4)** is verified: a 26 × 130 matrix over {−1,0,1} with 25 nonzero entries per row, 5 per column, and exactly two +1 and two −1 products for each of the 325 row pairs. Witness [brd26-130-witness-v1.brd](brd26-parent-inputs-v1/brd26-130-witness-v1.brd), 7103 bytes, SHA-256 `eb15cba18110e8c2e4ba7798838fc0a8fd508310d8a73a04132abb49977d71fe`; all 130 columns are distinct. It is the development of six signed base blocks over Z₂₅ ∪ {∞} (five full orbits and one orbit of length 5).

**This does not meet the info-2 gate.** The [frozen contract](../screening/info-2-brd26-contract.json) relied on the CPro1 `OPEN_INSTANCES` list (derived from the 2006 Handbook). A post-launch primary-source check found that Abel, Chan, Combe and Palmer, *Existence of GBRDs with block size 4 and BRDs with block size 5*, Des. Codes Cryptogr. 61 (2011) 285–300, state in their abstract that the necessary conditions for BRD(v,5,λ), λ ∈ {4,10,20}, "are sufficient, except for v = 5, λ ∈ {4,10}" (read by the parent on the [zbMATH review](https://zbmath.org/1229.05045) and the [Springer landing page](https://link.springer.com/article/10.1007/s10623-010-9477-6)). (v,λ) = (26,4) satisfies all four conditions, so existence was already claimed in 2011. The open-list entry is stale; the paper body (and whether it gives an explicit v = 26 construction) was not accessible.

## Verification of the witness (all PASS)

| Evidence | Result |
|---|---|
| Parent definition-first checker | VALID; 26 row and 130 column weights; all 325 pairs (+2, −2, 0×126) ([receipt](brd26-parent-inputs-v1/parent-check-v1.json)) |
| Parent controls and seed | 19/19 intended-reason controls, including a sign flip that preserves all supports but breaks pair balance; independent expansion of the six base blocks is byte-identical ([receipt](brd26-parent-inputs-v1/controls-seed-result.json)) |
| Parent structure checks | order-25 group action on all 84,500 entries; signed-difference certificate (each nonzero difference mod 25 and the ∞ pairs give exactly two + and two −) ([action](brd26-parent-inputs-v1/action-audit-v1.json), [differences](brd26-parent-inputs-v1/signed-difference-certificate-v1.json)) |
| Codex CLI `gpt-6.1-sol`, own verifier | RESULT: VALID; ten corruption controls and four invariances ([note](brd26-codex-verifier-v1.note.md)) |
| Claude CLI `claude-opus-5-5`, prompt-only checker run by the parent | 40/40 runs as expected under `-B` and `-O -B` ([checker](brd26-claude-checker-v1/checker.py), [receipt](brd26-claude-checker-v1/result.json)) |

Priority screen: [report](brd26-priority-screen-v1.md). A Lean formalization task was stopped once the prior claim was found.

## Status

**FRONTIER: VERIFIED-WITNESS; PRIOR-ART (existence claimed 2011); not a gate.** The value is at most an explicit, compact cyclic construction of a known design. The info-2 slot rotates to a target re-screened against post-2006 literature before freezing.
