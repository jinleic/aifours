# Ordered Olson D_2p: universal longest-zero-sum balance and the F≥2o_F−1 band

Recorded at 2026-10-19T01:34:06-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIALS (written).** Two candidates are accepted relative to the declared accepted imports:

1. **ROT-ZB v2 with mandatory erratum 1** (BAL1, ROOM, Theorem ROT-ZB and its uniform corollary 2F≥2p+3o_F−5). Its condition (B) forces kappa^≤(p−1)/2, so 2kappa^+k≤2p−2 automatically; the withdrawn cell counts are not results.
2. **BAL-full v2 with pre-review erratum 1** (Lemma BAL-forall, Lemma ROOM, Theorem ROT-ZB+, Corollary INV*/OLSON-ZB+). This supersedes ROT-ZB's band.

## Exact accepted statements

- **BAL-forall.** In setting (S′) (p≥5 prime, 1≤k≤p−1, integer 1≤kappa<p, Y odd elements of C_(2p) of length 2p+2kappa−k with (S1) at kappa), if L=|Y−Z|≥2t+1 then every longest zero-sum Z (|Z|=2t) is balanced relative to every index-<1 generator g of Y−Z. In particular this holds for every longest Z whenever 2kappa+k≤2p−1.
- **ROT-ZB+.** For prime p≥7, an avoider w of length 4p−2 over D_(2p) with an admissible normal form of terminal 2≤k≤p−1, kappa^≥1 and 2kappa^+k≤2p−1 has all rotation letters in one pair {rho_c,rho_−c}, c≠0.
- **Corollary ZB+.** For every prime p≥7: (a) every length-(4p−2) avoider with o_F≤p−1 and F≥2o_F−1 satisfies INV*; (b) every word of length 4p−1 over D_(2p) with o_F≤p−1 and F≥2o_F−1 has an identity 2p-subword in increasing index order.

Combined with the accepted S1-sharp corollary (3o_F≤2p+1, any F), the remaining o_F≤p−1 dihedral cases satisfy 3o_F≥2p+2 and F≤2o_F−2. This is NOT unrestricted INV*, ordered Olson for D_(2p), or the all-groups conjecture.

## Evidence

- [ROT-ZB v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-ROT-ZB-v2.md) `65dbedbf8f679b583a0186c84d64ede9c0564fc15ca8b13404c4766019f4f5f1` + [erratum 1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-ROT-ZB-v2-erratum-1.md) `a181edbba0c6763e7e55a8d97ad47f3f2be58af11badf0bd999c86b3a88fc0de`. Reviews: [Codex](olson-rotzb-codex-v1.prompt.stdout.txt) ACCEPT all four items, 0 findings; [Claude](olson-rotzb-claude-v1.prompt.note.md) BAL1/ROOM/ROT-ZB ACCEPT, corollary AWF, 0 FATAL/0 MAJOR/6 MINOR, all disposed by erratum 1.
- [BAL-full v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-BALfull-v2.md) `dffbfea8d97730e6c7a7a5f384cb471c64dda17091829fcd289a5c5a9775a3e1` + [pre-review erratum 1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-BALfull-v2-erratum-1.md) `e0f826a29b3209857144e563db7516717a3e447e8a2ee8ab48c1584140311fcf`. Reviews: [Codex](olson-balfull-codex-v1.prompt.stdout.txt) `edfa15be1677897951754776af43091d3a6f7fba5ef975a4e13f6efb9ac8b624` ACCEPT all four items, 0 FATAL/0 MAJOR/0 required MINOR; [Claude](olson-balfull-claude-v1.prompt.note.md) `38fad73b947e3d141bf0747652ce278659eb690af2b224fc129d35932f074dea` ACCEPT all four, 0 FATAL/0 MAJOR/4 MINOR. Observed CLI models gpt-6.1-sol and claude-opus-5-5.

## Parent derivation

Assume an unbalanced longest Z, so S(N)=n_++2pj with j≥1 because 0≤n_+≤2t<2p. Every integer weight in [0,W+n_+] is realized by a submultiset of P=(units of Z)∪Y′ (REALIZE's proof interval plus units). Prefixes N_0 of N with S(N_0)≤m+n_+ give actual zero-sums with available units, so f(N_0)=S(N_0)+|N_0|≤2t. Prefixes with 2p−W≤S(N_0)≤2p+n_+ give the occurrence-disjoint zero-sum (N−N_0)∪X with X⊆P of weight n_++2p−S(N_0); since |X|≥weight−e′, f(N_0)≥2p−e′. The first prefix crossing m+n_+ increases by s≤slack and lands in the second window because W+m≥2L≥2p+2. Combining the two bounds gives L≤2t, contradicting L≥2t+1. ROOM's W-bound uses only longestness; balance gives E=e′+n_+−n_−≤k−1. In ROT-ZB+, DAV and 2kappa^+k≤2p−1 give kappa^≤(2p−2)/3, so S1-sharp supplies (S1); SHgen(H) is 2p−2−2kappa^≥k−1≥E and SHgen(K) uses KETA's k-free inequality with k≤p−1. The corollary's F≥2o_F−1 is equivalent to 2kappa(w)+o_F≤2p−1 and transfers to every admissible normal form; deletion cases preserve both conditions.

## Parent overlays for Claude BAL-full MINORs (no statement change)

1. The terminal residual statement in erratum item 4 is restricted to terminal k≤p; terminal k≥p+1 (forcing o_F≥p+1) also remains open. A word is residual only if every admissible normal form lies in a residual cell (ZX overlay 2).
2. Remark (ii)'s example lies outside (S′); it only shows that “longest” is needed.
3. Probe consistency wording reads “consistent with”, not “as predicted”; probes are not premises.
4. With F≡o_F (mod 2), the illustrative p=31,o_F=30 bound is F≥60.
5. The REALIZE/ZSTRUCT extension to (S′) and to every index-<1 generator is accepted through their embedded proofs (both referees checked this), not by their original statements.

## Limits

Index-one/Savchev–Chen and EGZ remain classical imports at their recorded author-statement scope. Written proofs only: no Lean, human review, or novelty/priority clearance. Remaining rotation obstruction: longest zero-sums of maximal length t=kappa^ (high cells 2kappa^+k≥2p with k≤p−1, and k=p via S(p)); reflection half o_F>p untouched.
