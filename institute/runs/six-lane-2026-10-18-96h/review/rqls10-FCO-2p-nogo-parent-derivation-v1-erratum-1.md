# Erratum 1 to the Proposition FCO-2p derivation (parent-owned)

Recorded at 2026-10-19T06:24:56-0700. Amends [the derivation](rqls10-FCO-2p-nogo-parent-derivation-v1.md) `355718b429d69f6892bf1dda4342dcde35ab92cd18f90d0963d41e118ee23569`. The derivation file is unchanged. The changes are presentation only: no inference changes and no scope is broadened.

This erratum disposes of [Claude](rqls10-FCO-2p-claude-v1.prompt.note.md) `af89e816e0a9063248f00359ccba5e414cd00d5392b5f7863751639cb08b0211` (ACCEPT, MINOR m1–m6). [Codex](rqls10-FCO-2p-codex-v1.prompt.stdout.txt) `8f61f8c0322c765e0df6e7a0b954de64ac425111638db84dfed75df4ae3f8e50` returned ACCEPT 0/0/0.

- **m1 (definition).** Add to Setting: "A QLS q is *orthogonal* to the Latin square L if, for each symbol s, the vectors {q_ij : L_ij = s} are pairwise orthogonal. Equivalently, {q_ij ⊗ e_{L_ij}} is an orthonormal basis of C^{n²}. Here L_ij = j − i."
- **m2 (Step 1).** Add: "ω^{c'} = ω^c because c' ≡ c (mod p)." Also add the degree argument: "Re-index the coefficients by w = cv ∈ {0, …, p−1} and let g(x) = Σ_w N(w)x^w, which has degree ≤ p−1. Then g(ω) = 0 iff Φ_p | g, iff g = κΦ_p with κ ∈ Z, iff all N(w) = κ."
- **m3 (Step 3).** Replace with: "(F*) is (F) for the pair (ρ, π). So Steps 1–2 apply verbatim with (i, ρ) ↔ (t, π), and π supplies the pair with both differences odd." Note that this step is load-bearing: (F) together with the parity of π alone gives no contradiction.
- **m4 (optional).** Note that #even − #odd = 2·#even − 2p is always even, so κ ∈ {−2, 0, 2}. Only κ = 0 needs the mod-4 exclusion.
- **m5 (coverage).** Replace the coverage sentence with: "Covers exactly n = 2p, p an odd prime. Not covered: every n ≡ 0 (mod 4), where at n = 8 the zero count rests on the parent enumeration only; and n = 2m with m odd composite (18, 30, …). For odd n the family does contain mates, e.g. π = ρ = id."
- **m6 (external consistency).** Withdraw the clause "and with the Ball–Simoens order-6 result". That result (arXiv:2603.02334v1, as quoted by the scout) was not read by the parent, and the proof does not use it. The agreement with the parent FCO enumeration (0 at n = 6, 10) stays as a consistency remark only.
- The reviewer's further remarks are **not adopted into the accepted scope**, because only one family reviewed them. They cover the i + j square, global unitaries, and arbitrary maps forced to be bijections.
