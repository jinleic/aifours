# Olson D_2p: ROT-ZR and its uniform ZR2/ZR3 corollaries

Recorded at 2026-10-18T15:09:25-07:00.

**CORRECTNESS-ACCEPTED with the overlay below.** The written lemmas REALIZE, ZSTRUCT, LAMBDA, EBOUND, Theorem ROT-ZR and the stated ZR2/ZR3 corollaries are accepted relative to their recorded imports. The unrestricted ordered Olson conjecture and both unrestricted INV*(p) halves remain OPEN. No new contract gate or novelty claim.

## Frozen evidence

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-ZR-v1.md), SHA256 `e8903ff49f22c74ad8253599701a11f7d0af7efb63c7e9dc02cbcde4a77669a7`.
- [Packet manifest](olson-rotzr-v1-review-v1/manifest.json): candidate plus eleven dependencies.
- [Codex](olson-rotzr-v1-codex-v1.note.md), SHA256 `41861f3b34b9e8926b7a804de4564d68a869fb404241d216e535cbccf8f4f400`: all eight items ACCEPT, 0 FATAL/MAJOR/required MINOR; all twelve source hashes matched.
- [Claude](olson-rotzr-v1-claude-v1.note.md), SHA256 `ee7a520f7645f0dbb0cdaf080c9eb79e4c00498b92196d9d66ed8f6199bba8f1`: underlying four lemmas and ZR2 ACCEPT; ROT-ZR, ZR3 and uniform corollaries AWF, 0 FATAL/MAJOR, seven MINOR/optional clarifications. No computation or formal verification by either reviewer.

## Exact accepted statements

Let p≥7 be prime, w an identity-2p-subword avoider of length4p−2 over D_2p, and let an admissible normal form have terminal integers k,κ̂. Put

G(κ)=max_{s odd,1≤s≤2κ−1}(2κ(s−1)/(s+1)−s).

If **2≤k≤p−1**, **1≤κ̂≤(p−1)/2**, and all three requirements hold:

1. Λ: 8κ̂≤4p−3k+5 **or** 2κ̂(2κ̂−1)<2p;
2. H′: k−1+G(κ̂)≤2p−2−2κ̂;
3. K′: k−1+G(κ̂)≤2p−k−3,

then every rotation of w belongs to one nonzero pair {ρ_c,ρ_−c}. G(1..5)=−1,−1,0,1,2.

- **ZR2:** every terminal(k,2), 3≤k≤p−1, for p≥7 is covered.
- **ZR3:** every terminal(k,3), 4≤k≤p−1, for p≥17 is covered. At p=11 and13 the accepted partial terminal ranges are respectively4≤k≤8 and4≤k≤11.
- **Uniform INV*/OLSON-ZR2:** for p≥7, o_F≤p−1 and F−o_F≥2p−6 imply INV* for every length-(4p−2) avoider and an identity2p-subword in increasing index order for every length-(4p−1) word.
- **Uniform INV*/OLSON-ZR3:** for p≥17, replace that last bound by F−o_F≥2p−8, retaining o_F≤p−1.

These are sufficient conditions; no existence of avoiders is asserted. ROT-KP's separate boundary k=p,κ̂≤1 remains accepted but is not used by ROT-ZR.

## Parent derivation and integration check

Choose a longest zero-sum Z of size2t in the odd rotation sequence Y⊂C_2×C_p. Accepted S1(a) gives t≤κ; the complement Y′ is zero-sum-free of length L=2p+2κ−k−2t≥p+1. SC0 supplies ONE generator g, positive odd coefficients a_i and total W≤2p−1.

REALIZE's jump argument is exhaustive: if a heavy coefficient exceeds the sum X of earlier coefficients, the remaining n coefficients force W≥2p+1 when n=1, W≥2p+n for2≤n≤p−1, or W≥3p for n≥p. Hence each prefix fills its integer interval of subset sums, and any singleton realization of weight≥2 can be replaced by at least two strictly smaller occurrences.

For z=rg∈Z, 3≤r≤W would permit replacing z by a longer selection from Y′, contradicting maximal length. Otherwise r=1 or z=−sg with odd1≤s≤min(2t−1,slack); the s units exist since m−slack≥3. This also rules out Y(0) everywhere. Under Λ2 the two congruent integers Σs_i and n_+ lie in[0,2p); under Λ1 the partial-sum induction maintains P_j≤2t−j using m≥4t−2. Thus Σs_i=n_+.

With s=max s_i, E=e′+n_+−n_−, e′≤k−1−2κ+2t−s and n_−≥2t/(s+1). Substitution, monotonicity in t≤κ and maximization over odd s give E≤k−1+G(κ). The t=0 branch is separate and also valid. Every coefficient is the same generator's canonical signed odd representative with |b|≤p−2, excluding zero rotations.

H′ supplies SHgen(H). For E>0, KETA's **k-free inequality** η+a_max≤E+2 supplies SHgen(K) from K′; its narrower E≤k−1 corollary is not used. Empty runs use SHgen-E: expansions preserve k and odd blocks; base words have length4p−2, one nonzero pair, and o_F(u°)≤k≤p−1, so restricted REFL and the accepted V3 caller apply. The normal form preserves rotation letters.

For uniform corollaries, κ̂=κ(w)−(o_F−k)/2≤κ(w). K1 covers k=1; DAV forces κ̂≤1 at k=2; K01 covers κ̂≤1; ZR2/ZR3 cover the remaining cases. Restricted REFL applies to the original word. Deletion Case1 uses o_F≤p−1≤2p−3; Cases2/3 never increase o_F or reduce F−o_F. The accepted ledger and RGR-LONG therefore apply.

## Disposition of Claude findings

- **m1:** Setting(S) explicitly requires integer κ; theorem κ̂ already is integral.
- **m2:** Y(0)∉Y follows explicitly from the REALIZE swap and a_i≤p−2; no zero rotation remains.
- **m3:** use o_F(u°)≤k≤p−1, not an unsupported equality. Keep k fixed along expansions; apply the same REFL condition(d)/V3 discharge as K01.
- **m4:** cite the accepted normal form with F,R≥1, odd terminal blocks and κ̂≥0.
- **m5:** ZR3 is the actual statement written above, with explicit terminal ranges, not just an arithmetic observation.
- **m6:** retain the exclusion of the even terminal block, K1's c≠0, and the displayed κ̂ relation.
- **m7:** compare to K01, not just ZX. Additional uniform bands relative to K01 are F−o_F=2p−6 and, for p≥17,2p−8; within the low-odd range other accepted theorems may already cover them. At p=11 the example extends K01 only at F=o_F+16. This is internal coverage, not literature novelty.

Claude's optional Λ sharpening, improved integer G(3), and its extra uniform small-prime corollaries are NOT promoted. The parked ZR+ addendum and hand coverage-union note are not premises of this verdict.

## Imports and open boundary

GRX, normal form/PM*, DAV/K1, S1(a), SC0 with Savchev–Chen/Yuan index-one import, KETA/K01, SHgen/SHgen-E, restricted REFL, RGR-LONG and the deletion ledger remain imported at accepted scopes. No independent reproof of their internals, Lean, human review or priority audit here.

Uncovered by this route: k=p; κ̂>(p−1)/2; pairs failing Λ/H′/K′; o_F>p. In particular the low-odd p=31 terminal gap(21,20) is not closed. No new finite computation is a premise.
