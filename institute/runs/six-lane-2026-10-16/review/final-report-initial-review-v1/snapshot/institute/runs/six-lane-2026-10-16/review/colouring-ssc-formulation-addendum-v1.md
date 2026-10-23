# Colouring proofs: precise small-subgraph-conditioning implication

## Scope

This addendum clarifies the SSC import in the frozen written proofs of χ(G_{n,7}) = 4, χ(G_{n,8}) = 4 and the candidate χ(G_{n,12}) = 5. It changes no entropy estimate, parameter, constant, residue construction or claimed graph model. The old proof files remain unchanged. The issue was identified by Codex CLI `gpt-6.1-sol` in the [χ12 hostile review](chi12-codex-hostile-review-v1.note.md); that review finds no fatal or major error in the colouring application.

The general conclusion P(Y > 0) = exp(−Σ_{δ_i=−1}λ_i) + o(1), quoted in the proof files, is stronger than the listed moment hypotheses alone warrant. For these exponentially growing colouring counts, replacing Y by Y + 1 preserves the limiting normalized moments but makes positivity certain. The correct colouring application follows directly from the accompanying **conditional contiguity conclusion**, without using that general equality.

## Source and implication actually used

Pinned primary source: Wormald (1999), [layout](chi12-parent-inputs-v1/wormald1999-models.layout.txt), LF1519–1548 and LF1561–1596 (LF only, not form feeds):

- G^(Y) weights the original model G by density Y/EY (LF1522–1527).
- G^(Y) ≈ Ĝ, where Ĝ is G conditioned on X_i = 0 for all δ_i = −1, provided Σ_{δ_i=−1}λ_i < ∞ (Theorem4.1, LF1589–1596).
- ≈ means mutual contiguity: an event sequence has probability tending to zero in one model if and only if it does so in the other (LF1533–1548).

In each application, on the balanced admissible subsequence (k divides n and dn is even),

λ_i = (d−1)^i/(2i),   δ_i = (−1)^i/(k−1)^{i−1}.

Thus δ_1 = −1, every other δ_i > −1, and Σ_{δ_i=−1}λ_i = λ_1 < ∞. Each proof verifies the four moment hypotheses at its own (k,d). Let A_n := {Y = 0}. Its probability under G^(Y) is **exactly zero**, since its size-biased mass is E[Y·1_{Y=0}]/EY = 0. Contiguity therefore gives

P(Y = 0 | X_1 = 0) → 0.

For a proper-colouring count, a loop prevents every colouring, so {Y > 0} ⊆ {X_1 = 0}. Consequently the equality used in these particular applications is now derived, not taken as a generic SSC conclusion:

P(Y > 0) = P(X_1 = 0)·P(Y > 0 | X_1 = 0) → e^{−λ_1}.

Finally,

P(Y = 0 | X_1 = X_2 = 0) ≤ P(Y = 0 | X_1 = 0) / P(X_2 = 0 | X_1 = 0) → 0,

because the denominator tends to e^{−λ_2} > 0. Conditioning on X_1 = X_2 = 0 gives the uniform simple regular model. The marked-colouring application uses the same implication once its marked-space moment hypotheses are established; its existing KPW Theorem10 reliance remains disclosed.

## Effect on the three proofs

| Application | k | λ₁ | Change |
|---|---:|---:|---|
| χ(G_{n,7}) = 4 | 4 | 3 | Use conditional contiguity, then loop support; the n ≡ 2 (mod4) transfer is unchanged |
| χ(G_{n,8}) = 4 | 4 | 7/2 | Same; every residue transfer is unchanged |
| Candidate χ(G_{n,12}) = 5 | 5 | 11/2 | Same; author applies the clarification in the next frozen revision |

The accepted χ7/χ8 conclusions do not depend on the overstrong generic formulation: the displayed support argument and the valid conditional-contiguity conclusion give exactly what their applications need. This is a source-formulation clarification, not a new colouring result, priority claim or independent formal verification.
