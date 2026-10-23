# Research task: exclude more balanced residue types (pure mathematics)

Read only files in this directory (see manifest.json). Do not modify files, delegate, use the network, or read elsewhere.

Setting. A balanced f: F_2^9 -> F_2 with max|W_f| <= 28 has nonzero support XOR s; an odd split gives odd 8-variable halves g,h with |G|+|H|<=28; canonical spectra K_g,K_h (transforms in {+/-256}); S=K_g+K_h, R=K_g-K_h, p=R/8 in {-3..3}, D = p mod 2 quadratic = Q = W_f/8 mod 2 on s-perp, Q(0)=0. Reviewed: wt(D)>=112 and D is one of 8 types (rank,weight): (2,192),(4,128),(4,160),(6,112),(6,128),(6,144),(8,120),(8,136). The zero-set/Pfaffian/next-bit lemmas (zero-set-lemmas-candidate.md, Opus-reviewed correct-with-fixes) and the exclusion of (4,128) (type-4-128-exclusion-PROOF.md, Codex-reviewed ACCEPT) are established inputs. The unreviewed remaining-types notes record new necessary conditions and where each lever stops (scalar count relaxations are satisfiable; single-character projection cannot reach (6,112),(6,128),(8,120),(8,136)). Treat the unreviewed notes as untrusted leads: re-prove anything you use.

Task: attempt NEW mathematics, in priority order:
(1) Rigorously exclude one or more of the seven remaining types. Highest-value targets: the four rank-6/8 types via a GLOBAL argument (not single-character projection), and (2,192) via Boolean realizability of the per-coset functions.
(2) Otherwise prove a strictly stronger necessary condition that a finite computation could audit and that materially shrinks a type (e.g. forces the zero set's geometry, forces c, or forces a sub-case).
(3) Otherwise explain precisely why natural global strategies fail, with explicit integer/residue fakes where possible.

Rules: complete proofs only; label every unproven step GAP and do not claim its consequence. Use the established lemmas with their stated hypotheses and errata. Cite outside literature only with precise statements you are sure of. Make no novelty claim. For each claimed result give a concrete finite audit that could falsify it.

Output markdown. First line exactly one of: RESULT: TYPE-EXCLUSION | RESULT: PARTIAL | RESULT: NO-PROGRESS. Then: Statements, Proofs, Gaps, Suggested audits, Why other routes fail.
