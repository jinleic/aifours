# Sun(7): K6.2* with e_d <= 3 excluded

Recorded at 2026-10-19T05:15:12-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** In the exact K6.2* class, every configuration has **e_d >= 4 and e* = 2**, over arbitrary groups with finite-index subgroups. All positions and unbounded exponents of the 3- and 5-markers are covered. Lemmas1–3 and Corollaries C1/C2 are accepted at their stated scopes. **K6.2* with e_d >=4 remains OPEN; K7 with the 2- and 3-markers on different vertices and full Sun(7) remain OPEN.**

## Frozen text and reviews

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-E3-v1.md), SHA256 `70a60d551583e8d6ad920acadb829d3ddf0d9c5c46ac988f8677645ee5457372`.
- Mandatory [erratum1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-E3-erratum-v1.md), SHA256 `095c31dcb9623cf3aa3887aef8d0a2d92708a0037b3bc3c7a8ad64b06ef3f797`, and consolidated [erratum2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-E3-erratum-v2.md), SHA256 `f9f52e1bc4896d94cd014ed3f8915af0318ddcd06d1efc1ad7f14478685add4c`. Erratum2 supersedes F1/F3; F2 stands. Parent read both completely and verified all twelve quoted Old blocks uniquely match the frozen candidate.
- [Codex review](sun7-K62E3-codex-v1.prompt.stdout.txt): observed gpt-6.1-sol, max effort, read-only; FATAL0/MAJOR0/MINOR1. [Receipt](sun7-K62E3-codex-v1.prompt.receipt.json). Output SHA256 `45adc810ef55c1388292a0d6b9508a63e0996998ef29baca6015fcaced751763`.
- [Claude review](sun7-K62E3-claude-v1.prompt.note.md): observed claude-opus-5-5, max effort, no tools; FATAL0/MAJOR0/MINOR9. [Receipt](sun7-K62E3-claude-v1.prompt.receipt.json). Output SHA256 `6329464530997e5204751d47596c220d831e5b3a8aabc2b86b4c4e7286fa392b`.

## Exact setting and parent derivation

C = {i*} disjoint-union O, |O|=5. n_d=2^e_d 5^h_d w_d has no 3-part; n_i*=2^e* 3^f* 5^h* w_*; n_c=2·3^f_c 5^h_c w_c for c in O. min(e_d,e*)=2; at most one vertex has f>=2 and at most one has h>=1; the w parts are pairwise coprime and prime to30. Pairwise gcds are6 inside C,4 on d–i*,2 on d–O.

The parent independently checked the following written argument before the reviews and checked the editorial repairs afterwards:
1. At d, the six local indices have pairwise gcd3 unless the d–i* entry is3 and the 3-marker is in O. Uniform weight1/3 gives 5/6+a/12<1; a=2 is impossible. INV and a+a*<=4 ensure at least one orientation has a=1. Invert first if necessary, then normalise g_d=1.
2. At each O-vertex, pairwise incompatibility and feasible local weights exclude O–O entry3 and three entries1. When h_d>=1, they also exclude entry5; inverse entries1 handle four fives. These facts hold in both orientations without circularity.
3. Intersect the conjugated O-subgroups, marked vertices first. Each subsequent unmarked index is6w_e; the multiplier k in T_(m+1)=lcm(n_e,T_m)k satisfies k<=alpha*_ej<=5. No prime greater than5 enters except the pairwise-coprime w factors. If h_d>=1, all O-indices and multipliers are5-free. Consequently gcd(n_d,T*_O)=2^min(e_d,v2(T*_O)).
4. The six other cosets meet the U_d-fibres with total incidence11n_d/4. Each fibre holds at most3 pieces by Sun(4). The M fibres in W*_O U_d meet none of the five O-cosets, and U_d meets no other coset, so 11n_d/4 <=3(n_d-M)+(M-1), yielding M<n_d/8.
5. Lagrange and the subgroup product formula give M>=n_d/gcd(n_d,T*_O). Thus gcd(n_d,T*_O)>8, forcing e_d>=4 and e*=2. R0 preserves the conjugated intersections in a finite quotient and extends the result to arbitrary groups.

C1 follows by the same index-chain proof on each four-subset Q of O: v2([G:W*_Q])>=3. C2 uses the no-5 argument at h_d=0, pair-fibre double counting and integrality: n4>=2n1+2. These corollaries are not premises of the main theorem.

## Findings, provenance and limits

All minor findings are disposed by Z1–Z12. Claude's suggested promotion of an extra Lemma2 item and a broader Lemma3 statement was implemented as proof subclaims in C2/C1 instead; no accepted statement was broadened. The e_d=4 numerical compatibility check is not an existence claim; using a=3 removes the three-piece cap, as the reviews explicitly check.

Direct Sun instances are Sun(2) and Zhu's classical Sun(4), through LFC(c) at subset sizes2 and4. **The imported general LFC package retains its recorded computer-assisted Sun(5)/Sun(6) provenance; the global Sun(7) class reduction also retains those imports.** No package-level computation-free claim is made. K63-RES, K62-FG, K62-A and the superseded R2 candidates are not theorem premises here. No Lean or human peer review; no novelty clearance or full-target gate.

Citation-only correction also noted for K63-RES-erratum-v2 X1 and K62-FG-erratum-v2 Y1: L0.1 is in the old README section0, not section1 (which is R0). The formula and argument are unchanged; original files remain frozen.
