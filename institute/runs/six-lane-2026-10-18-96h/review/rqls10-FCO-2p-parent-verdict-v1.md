# RQLS10 lane: Proposition FCO-2p

Recorded at 2026-10-19T06:24:56-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL — restricted negative.** Let n = 2p with p an odd prime. No permutations π, ρ of Z_n make q_ij(t) = ζ^{tj+π(t)ρ(i)}/√n a QLS orthogonal to Cay(Z_n), where the symbol classes are {(i, i+s)}. Equivalently, H = [ζ^{it+ρ(i)π(t)}] is never complex Hadamard.

- **Texts:** [derivation](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-FCO-2p-nogo-parent-derivation-v1.md) `355718b429d69f6892bf1dda4342dcde35ab92cd18f90d0963d41e118ee23569` together with [erratum 1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-FCO-2p-nogo-parent-derivation-v1-erratum-1.md) `013893adb51a4c5cd1aaff3faed4c961e8dac6a9b0948227995253a225bb4978`.
- **Proof sketch source:** the read-only scout QuantumGroupTableNoGo3 ([record](rqls10-quantum-grouptable-nogo-scout-v3.json) `0d7a5d1810c1c0b8bcf7db52d91176cf8b16cff19d4e7f8a1e5a0fb4cab9c629`). The parent checked every step and wrote the derivation.
- **Reviews:**
  - [Codex](rqls10-FCO-2p-codex-v1.prompt.stdout.txt) `8f61f8c0322c765e0df6e7a0b954de64ac425111638db84dfed75df4ae3f8e50` (observed gpt-6.1-sol, max, read-only): ACCEPT, 0/0/0.
  - [Claude](rqls10-FCO-2p-claude-v1.prompt.note.md) `af89e816e0a9063248f00359ccba5e414cd00d5392b5f7863751639cb08b0211` (observed claude-opus-5-5, max, no tools): ACCEPT, 0/0/6 MINOR. Erratum 1 disposes of all six.
- **Consistency:** this is an analytic confirmation of the parent's exhaustive FCO(10) enumeration ([audit](rqls10-FCO-parent-run-v1/), one producer), which found 0 solutions over all 362,880 normalised π. An independent verifier source is frozen and unrun (`9c33ab6a…`).
- **Not covered:**
  - n ≡ 0 (mod 4); the FCO(8) zero count is enumeration-only.
  - n = 2m with m odd composite.
  - Unrestricted QLS mates of Cay(Z_10) or Cay(D_5).
  - 1-RQLS(10), which remains **UNKNOWN**.
- **Calibration:** a short argument within one restricted family. The scout judges it may be folklore among Fuglede specialists. No novelty or priority claim.
