# Ordered Olson: sharp odd-sequence lemma and uniform restricted dihedral consequence

Recorded at 2026-10-19T00:33:24-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL, relative to declared classical imports.** Lemma S1-sharp holds for every prime p≥5 and integer 0≤κ≤floor(2p/3). Consequently the accepted dihedral INV*/ordered-Olson route now covers **every prime p≥5** under **3o_F≤2p+1**, with no extra side condition on F. The previous terminal gap (p,k,κhat)=(31,21,20) is closed. This does not prove unrestricted INV*, ordered Olson for all D_2p, or ordered Olson for all finite groups.

## Exact statements

1. For any sequence Y of odd elements of Z_(2p), if Y has no zero-sum subsequence of length in [2κ+2,2p], then every zero-sum subsequence has length≤2κ, provided0≤κ≤floor(2p/3). No bound on the length of Y is assumed. The threshold is sharp: the implication fails at every κ in [floor(2p/3)+1,p] by the explicit F1 family; κ≥p+1 is not a failure claim.
2. Every length-(4p−2) avoider over D_2p with3o_F≤2p+1 satisfies INV* (rotations in one nonzero pair and constant maximal reflection runs). Here o_F counts odd maximal cyclic constant reflection blocks, not arbitrary reflection runs.
3. Every length-(4p−1) word over D_2p with3o_F≤2p+1 has an identity2p-subword in increasing index order.

## Evidence and mandatory overlays

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-S1-sharp-v1.md), SHA256 `992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c`.
- [Mandatory erratum1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-S1-sharp-v1-erratum-1.md), SHA256 `bf504cdf8b8cfd3e96a26609d00162d365415b3481ca3a7dcbd7112af82f9507`. Parent read completely; no statement change.
- [Codex](olson-s1sharp-codex-v1.prompt.stdout.txt): both(A)lemma and(B)corollary ACCEPT-WITH-FIXES,0FATAL/0MAJOR,3MINOR. Observed CLI gpt-6.1-sol, max, read-only.
- [Claude](olson-s1sharp-claude-v1.prompt.note.md): both ACCEPT-WITH-FIXES,0FATAL/0MAJOR,9lemma+5corollary MINOR. Observed CLI claude-opus-5-5, max, prompt-only.
- **Additional parent wording overlay on erratum1:66–69:** “foundF1/F2” means F1 at the listed sharp-boundary controls and F2 where p≡1(mod3); do not claim those are the only boundary families. The worker's probe-v3 reports additional perturbations for p≡2(mod3). All probes are non-premise aids, not classifications.

## Independent parent derivation

Induct onκ, using the accepted length-free S1+ forκ≤(p+1)/2. Setu=2κ=p+δ. A shortest long zero-sumT has evenN≥2p+2; every proper nonempty zero-sum lies in[l,u], l=N−u, and is minimal because a nested split would forceN≤3κ≤2p. Applying the induction toT itself forces a properQ of lengthu; Q′ has lengthl andD=u−l≥0.

The imported index-one theorem applies toQ over the composite cyclic groupC_(2p), since|Q|≥p+3. Its basis element has order2p: orders1/p give even elements, order2 would force length2. ThusQ has positive odd coefficients summing2p. WritingQ=g^m S gives mass(S)=p−δ, m≥(p+3δ)/2 andb_min≤p−δ+1.

For occurrence-submultisetsQ1⊆Q,W⊆Q′ with equal coefficient sum modulo2p, excluding exactly the empty/full exchange cases, (Q−Q1)W is a proper zero-sum; its length gives |W|≤|Q1|≤|W|+D. The Step6 inclusion-minimalZ0 construction produces aQ1 with too many terms for anyQ′coefficient≥D+2: the |Z0|=1 and |Z0|≥2 inequalities separately contradict the mass bounds. IfQ′coefficient sum≥4p, a first crossing of2p and its predecessor give mass(W)≥2p and≤2p−l+D, forcingp≤3δ−4, impossible. HenceQ′also has coefficient sum2p.

The same exchange forbids representingb_min as two or moreQ′terms. Thus t′<b_min and its low nonunit terms have total≤b_min−t′−1. The exact identity Σ_Y(c−3)/2=t′−base, with integralbase=(3l−2p)/2≥3, excludes t′≤2 and permits at most oneYterm above t′. Therefore l≤b_min, contradicting l≥p−δ+2>b_min. This closes the induction without the previous S1(g) Steps3–8 or the exploratory search.

For the dihedral consequence, GRX givesκhat≥0 andDAV givesκhat≤k−1≤o_F−1, hence3κhat≤2p−2. GRX supplies(ZP), the newlemma supplies(S1), and3k≤2p+1 supplies the accepted ZX terminal criterion. Restricted REFL applies sinceo_F≤p. The accepted ordered deletion ledger preserves the odd-block bound, andRGR-LONG finishes length4p−1. The former F-dependent alternative existed only to forceκhat into the olderS1range, so it is no longer needed.

## Scope, priority and preserved failures

New dihedral coverage begins atp≥31; p≤29 coverage was already accepted. The exact old terminal-pair list is discharged; the worker's Q1a/Q1b residual terminology is planning context, not a newly audited completeness claim. Cases outside3o_F≤2p+1 and reflection rigidity ato_F>p remain open.

The classical index-one theorem is imported at its generalC_n scope from the [author-statement record](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-index-one-primary-statement-parent-v1.md); its2007proofs were not read or formalized here. Other imports are the accepted S1+/ZX/GRX/DAV/restricted-REFL/deletion/RGR-LONG chain. Written proof only; no Lean, Comparator, human review or novelty clearance. Probe-v1's circular restricted representation and missing PID capture are preserved deviations and not premises; later support≤3 probes have proper launch/reap records but remain finite aids.
