# Parent resolution of focused sign-digit proof review

The configured Claude Opus 5.5 delegate at maximum effort returned **ACCEPT-WITH-FIXES** for the
self-contained Claims 1–4 and Corollary 5 embedded in the parent prompt. Because the parent is also
Claude-family, this is same-vendor independent-instance review; a Codex cross-vendor review of the
identical prompt runs separately. It found no mathematical error. It did not read or review the
entire dossier, run computations, assess novelty, or audit Sections 5–8. The prompt SHA-256 is
`3076fdb8f0644d9673a1cd6e116e34e559af786c8e7839cce26c4b84ad9231c6`.

| Finding | Disposition |
|---|---|
| Normalization and coset statements require `s != 0` | Applied in notation, Lemma 2, Theorem 4's specialization and Corollary 5. General hyperplane digit parity and target sign parity for arbitrary nonzero h do not require s nonzero. These normalized statements do not themselves handle the s=0 branch. |
| False wording `abs(W_Dq)>=16` at zero coefficients | Replaced by `16 divides W_Dq(z)` for every z. Added the rank-2h quadratic spectrum formula `{0, ±2^(8−h)}`, h≤4. |
| Least-nonnegative-residue digit convention | Explicit in notation; carry and sign interpretation remain distinct. |
| Original versus translated polar rank | Clarified translated matrix and invariance of restriction to `s^perp`. |
| Affine hyperplane coefficient/basis argument | Expanded: weight parity equals top coefficient; only eight linear parts contribute; affine offset has no effect; determinant is invariant under invertible change of basis. |
| Undefined kappa and missing frequency quantifier | Set `kappa=[rank D=8]`; congruence holds for every eight-variable frequency. |
| Mod-8 congruence actually holds without target cap | Recorded explicitly, with the carry-term argument. It is not promoted as a target-specific obstruction. Only exact no-carry identity and negative-sign interpretation need the cap. |

The pre-errata PROOF/README/result/review/manifest bytes are preserved in `pre-parent-errata/`.
The original manifest's README pin already differed from the live pre-errata README after the
worker's clock correction. The parent did not rewrite that historical manifest; the new post-review
manifest owns current documentation pins. Scientific code and original result/solver evidence were
not changed by these proof-exposition fixes.

Parent checks: original 40-control script replay passed with both mutations rejected. A separate,
stdlib-only direct-character-sum/bitset-rank implementation checked 4,088 affine hyperplanes on four
controls, including complemented linear `1+x0`, which rejects removal of the cap from the sign
statement. These checks supplement, not replace, the written proof.

No residue type was excluded and no balanced NL242 function was found. The main problem remains open.
