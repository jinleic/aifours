# rules-k6 erratum v1 (cumulative over rules-k6-v1, and README §2 and §3)

**Freeze record.** Host-clock time and sha256 are in `evidence/proofs-v1.sha256`. `README.md` (10fc493e…e2bf) and `rules-k6-v1.md` (3b135fea…b187) stay frozen and unchanged.

**What changes.** Only wording, hypotheses and specifications change. No rule predicate used by any engine changes.

**Sources.**
- Codex review `R/sun-coset6-rules-v1-codex-v1.note.md` (4908018d…df70b).
- Claude review `R/sun-coset6-rules-v1-claude-v1.note.md`.

## Corrections

**E1. README R1(6), step 3, and the dependence paragraph** (Codex MINOR).
- **Wording.** "All six gcds equal 3" should read "all fifteen pairwise gcds equal 3".
- **Status of Core(5).** The Core(5) input is now the **accepted** correctness record `R/sun-coset5-parent-verdict-v1.md` (2cf02436…5301). That record binds sun-coset5 proof-v4 and its cumulative errata, not proof-v3.
- **Scope.** The acceptance is a correctness verdict, not a gate for a new open target. A prior unpublished k = 5 claim (Z. Gong, as reported by Sun) exists.
- **Remark.** Given Sun(5), the whole p = 2 branch of R1(6) could also be closed by taking any five of the cosets.

**E2. rules-k6-v1 L6 (H5)** (Codex MINOR).
- **Units.** Sizes are normalised measures: |X| = c|G|/5, |W| = |G|/5 and |U_vW| = t_v|G|/5. Equivalently, μ = size/|G| throughout.
- **Index of W.** In step 5, add the justification: [G:W] divides gcd(5r_a, 5r_b) = 5 **because both U_a ≤ W and U_b ≤ W**.

**E3. rules-k6-v1 L7 (RLP)** (Codex MINOR; Claude MINOR).
- **μ.** μ(S) is the normalised mass of the right U_v-cosets whose type is exactly S.
- **Six cosets.** The proofs of (R1)–(R5′) use only pairwise disjointness, so they hold verbatim for six cosets.
- **Translation and inversion for s pieces.** This step is written out in `proof-k6-lemmas-v1.md` §1(b).
- **What a witness is.** For every admissible q, it is an exact rational y ≥ 0 with Σ_{j∈S} y_j ≤ 1 on **all** allowed S and Σ q_jy_j/5 ≥ 1. The verifier recomputes which supports are allowed, over all 31 non-empty subsets.
- **What does not count.** Simplex output and Bland's rule are not evidence. The format is fixed in `CERT-FORMAT-k6-v1.md`.

**E4. rules-k6-v1 L5 (F2)** (Codex hypothesis repair; Claude).
- When F2 uses s = 6, assume explicitly that H < G, inside the minimal-counterexample frame. H5 supplies properness.
- F2 does not assert anything unconditional about a coset meeting six fibres in a group that is not minimal.

**E5. rules-k6-v1 L8 (M2)** (Codex MINOR; Claude MINOR).
- **Old text.** "Class-2 E2, E3 and E5 contribute exponents larger than any t-part" is replaced by a saturation argument.
- **Saturation.** For t ≤ 5, the largest t-part exponents are e₂ = 2, e₃ = 1 and e₅ = 1. A marked cofactor has v_p(r) ≥ 1, and for class-2 E2, v₂(r) ≥ 2. Hence min(v_p(t_l) + v_p(r_l), v_p(t_l′)) = v_p(t_l′), which does not depend on the instance.
- **Representatives.** So every instance has the same gcd vector as the representatives 2⁴, 3⁴ and 5⁴. These representatives have large exponents, but actual cofactors may have v₃ = 1 or v₅ = 1.
- **Class 1.** For class-1 E2 the exponent v₂ = 1 is exact.
- **The same holds for the RLP maxgcd,** where the partner exponents are v₂(q) ≤ 2 and v₃(q) ≤ 1.

**E6. rules-k6-v1 FH5 enumeration clause** (Claude MINOR).
- Every vertex except a ranges over all t_l-subsets:
  - b, and each inside vertex of V, over all five singleton labels;
  - each forced vertex of V over all C(5,c) subsets;
  - each free vertex over every t and every t-subset.
- Only a's coset is fixed, to label 0.

**E7. rules-k6-v1 §0** (Claude MINOR). "Any two of these may coincide" should read "any of these may coincide, including all three".

**E8. rules-k6-v1 controls** (Codex MAJOR reporting correction; Claude MINOR).
- **Replace.** "Any other orbit would mean a rule is unsound" becomes: "a Core(5) survivor beyond the engine-v1 N2/FH2/S-D set is a **reproduction mismatch requiring investigation**: compare universes, marker conventions, omitted rules and witnesses."
- **Overstrength.** If T, K or P kills an orbit that sun-coset5 killed only by N2, FH2 or S-D, that is an overstrength warning. Only RLP may legitimately kill such an orbit.
- **What these controls can and cannot show.** Because Core(5) and Core_3(4) are accepted theorems, these reruns cannot detect a false elimination. The evidence for soundness is the written proofs, the survival of realisable configurations, and the selected mutation demonstrations.
- **Universe.** The 21,150 count refers to the full orbit universe, not only to T-consistent leaves.

**E9. "Admissible τ"** (Codex). Wherever this phrase appears, it means "satisfying the necessary T constraints (T1), (T2)". It does not mean that some group realises that τ.

**E10. Downward closure of the allowed family.**
- Under the rules-k6-v1 definition (all pairs ≥ 2, and some pair ≥ |S|), the allowed family need not be closed under taking subsets.
- Under the hereditary definition of rules-k6-v2 L9 (used by engines v2 and v3), it is closed under taking subsets.
- In both cases constraints on the maximal allowed sets suffice: y ≥ 0, and every allowed set lies in a maximal one.
