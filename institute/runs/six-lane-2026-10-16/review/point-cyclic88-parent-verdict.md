# Point-cyclic resolutions of 2-(88,4,1) designs: parent verdict

## Result

**Theorem.** For every 2-(88,4,1) design D = (V, B) and every resolution R of D, no single 88-cycle σ on V satisfies both σ(B) = B and σ(P) ∈ R for every class P of R. Equivalently, under the convention of Topalova–Zhelezova (Axioms 15(10):762, 13 Oct 2026, p.2 and Definition 5), **no 2-(88,4,1) design is cyclically resolvable**.

**Corollary (same proof).** The same holds for v = 8p for every prime p ≡ 11 (mod 12); 88 is the smallest case.

The source's §7 (PDF p.11) states that "v = 88 is the smallest v for which the existence of cyclically resolvable 2-(v, 4, 1) designs has not yet been determined" ([parent excerpts](point-cyclic88-primary-excerpts.txt), [definitions addendum](point-cyclic88-primary-definitions-addendum.txt)). The frozen info-2 target ([contract](../screening/info-2-point-cyclic88-contract.json), 2026-10-17 00:38:45 PDT) asked for exactly this statement.

Not covered: general resolvable 2-(88,4,1) designs; cyclic designs whose resolutions are not preserved by the cycle; the class-transitive convention; automorphisms that are not one 88-cycle; v = 8p with p ≡ 5 (mod 12) or composite cofactors.

## Proof (reviewed r1 [PROOF.md](point-cyclic88-parent-inputs-v1/PROOF.md), SHA-256 `227c200c…6bfa`; write-up revision [r2](point-cyclic88-parent-inputs-r2/PROOF.md), `d6faaf11…8358`)

Relabel σ as x ↦ x+1 on Z_88. (1) Any translate meeting a block in two points equals it (λ = 1). (2) Block stabilizers are trivial or H_4 = {0,22,44,66}; the diameter pairs {a, a+44} force all 22 cosets of H_4 to be blocks. (3) For a class with stabilizer of order h and m short blocks: 88/h ≤ 29, h | 22−m and (88/h)m ≤ 22, which excludes every mixed class, so the short blocks form one class (type T1 is derived, not assumed). (4) Every other class has h | 22 and h ≥ 4, so its stabilizer is ⟨8⟩ or ⟨4⟩ and contains 8. (5) A block of such a class cannot contain x and x+8. The pair {0,8} lies in no short block (8 ∉ H_4) and no full block, contradicting the design property.

Revision r2 (01:13:07 PDT) applies the four review minors: verbatim Definitions 1–5, an explicit T1 definition, crediting backed by verbatim source quotes in Appendix A, and the full corollary substitution list. The parent diff of r1 and r2 from the Theorem through §5 shows only the inserted T1 definition and the retitled Corollary 4 ([pin receipt](point-cyclic88-parent-inputs-r2/pin-receipt.json)). The r2 write-up was not separately re-reviewed.

## Verification

| Gate | Result | Artifact |
|---|---|---|
| Parent mathematical reading | Re-derived the full chain from Definitions 1–5 before the worker's write-up; independent integer check of the orbit arithmetic for v = 52, 64, 88: mixed classes impossible only at 88 among these, stabilizers {11, 22}, uncovered differences = nonzero multiples of 8; known-positive 52 and 64 not excluded | [`cyclic88-orbit-arithmetic-parent-check-v1.json`](cyclic88-orbit-arithmetic-parent-check-v1.json) |
| Worker finite controls | All C(88,4) = 2,331,890 four-subsets: stabilizer orders {1: 2,330,944; 2: 924; 4: 22}; admissible nontrivial-stabilizer blocks are exactly the 22 cosets of H_4; exhaustive (h, m) table gives only (11,0), (22,0), (88,22) | `information-science/evidence/six-lane-20261016/point-cyclic88/evidence/check88-receipt.json` |
| Semantic positive control | The published point-cyclic 2-(64,4,1) resolution (source pp.6–7) transcribed and verified: 336 blocks, every pair once, 21 classes, +1-invariant, class orbits 1/4/16; lemmas hold and the 88 contradiction has no analogue; three corruptions rejected | `…/point-cyclic88/controls/control64-receipt.json` |
| Hostile review (Claude) | Claude Opus 5.5 max on r1: **VERDICT: ACCEPT** — "complete, self-contained and correct"; T1 derived; corollary for all primes p ≡ 11 (mod 12) verified; no fatal or major findings; four write-up minors (definition quote, unbacked §6 remarks, substitution list, T1 label), addressed in r2. Same vendor as the Claude task worker | [review](point-cyclic88-hostile-review.note.md) |
| Codex cross-vendor review | Codex `gpt-6.1-sol` (effort max, read-only) on r2: **VERDICT: ACCEPT**, no fatal or major findings. One optional exposition minor: state why p ≡ 5 (mod 12) escapes, since (h,m) = (8,2) satisfies Lemma 3. Its own independent checks agreed: all 2,331,890 four-subsets with stabilizer counts {1: 2,330,944, 2: 924, 4: 22}; the (h,m) table [(11,0),(22,0),(88,22)]; 440 forbidden pairs; 142 excluded values among 833 admissible v ≤ 10000; and a fresh transcription of the v=64 example (336 blocks, 21 classes, orbit lengths 1/4/16) | [final message](point-cyclic88-codex-review-v1/final.md) (`fb249f14…`), [prompt](point-cyclic88-codex-review-v1/prompt.txt) |
| Formal proof: full v=88 theorem | **Parent rebuild and fresh kernel replay PASS**. Five worker modules rebuilt from pinned sources, followed by a parent-authored theorem spelling out all design, resolution, image and cycle hypotheses without worker predicates. `leanchecker --fresh -v ParentAudit` exited 0 (86.576 s). Root axioms: only propext, Classical.choice, Quot.sound. Changing 88 to the known-positive 64, or dropping class preservation, makes the same proof term fail with the intended type error | [parent receipt](point-cyclic88-kernel-parent-replay-v1/parent-result.json), [unfolded statement](point-cyclic88-kernel-parent-replay-v1/ParentAudit.lean), [driver](point_cyclic88_parent_replay.py) |

Formal scope: the complete nonexistence theorem at **v=88**, for arbitrary finite point types and arbitrary designs, resolutions and full-support cycles. T1, short-block structure and stabilizer/cardinality facts are derived, not hypotheses. The all-primes 8p corollary remains a reviewed written proof. Lean and leanchecker share one toolchain; this is not a second independent kernel or Comparator. The mutation controls check statement/proof-term binding, not unprovability of arbitrary mutated propositions.

## Priority and significance

A bounded read-only audit ([report](point-cyclic88-priority-audit.md)) read Genma–Mishima–Jimbo 1997, Mishima–Jimbo 2000 and Lam–Miao–Mishima 2001 as Gifu author-version preprints. It read Lam–Miao 1999 and Mishima–Jimbo 1997 only through zbMATH reviews and quotations. It also checked forward citations of the 2026 source: OpenAlex shows 0 citing works, Crossref shows 0 references and no correction notice, and both authors' ORCID records list nothing later.

- **Known parts.** The orbit and short-block facts are classical. Excluding types T2 and T3, which forces T1, is known (Mishima–Jimbo 1997, restated as Lemmas 4.1–4.2 of Mishima–Jimbo 2000). The source itself says the possible point-cyclic resolutions for 88 are of type T1.
- **Not covered by any theorem read.** Known T1 exclusions need v/k to be prime (Genma–Mishima–Jimbo 1997, Thm 2.1) or a prime power coprime to k (Mishima–Jimbo 1997, as quoted in Lam–Miao–Mishima 2001, Lemma 2.1). Here v/k = 22 = 2·11, and for the corollary v/k = 2p. The proof extends the Genma–Mishima–Jimbo difference argument with one new observation: the divisor 2 is too small to be a class-stabilizer order, so every non-short class stabilizer contains ⟨8⟩.
- **Access holes.** Mishima–Jimbo 1997 and Lam–Miao 1999 full texts, the published versions of the three preprints, MathSciNet, the Handbook, Meszka–Rosa 2007 and Chang–Miao 2002 were not read. An earlier equivalent cannot be excluded.
- **Crediting.** Any write-up must credit Mishima–Jimbo 1997 for the T2/T3 exclusion and both earlier T1 lemmas, and must describe the new step as an extension of the Genma–Mishima–Jimbo mechanism.

Significance: a short, modest specialist result. It settles the smallest case the 13 Oct 2026 source calls undetermined and gives an infinite family, v = 8p with p ≡ 11 (mod 12). It is not a general theory of type-T1 resolutions.

**FRONTIER:** CORRECTNESS-ACCEPTED. The v=88 theorem is Lean-kernel checked, with a parent-authored unfolded statement and fresh replay. The written proof and 8p corollary have an independent parent derivation, finite and semantic controls, a Claude ACCEPT and a Codex ACCEPT. The bounded audit found no earlier equivalent, but that does not establish novelty: NOVELTY-UNCLEAR. **The frozen info-2 point-cyclic target gate is met** (decided 2026-10-17 PT after the priority audit; formal verification completed subsequently).
