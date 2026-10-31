# f188 — characteristic 7, corrected composite review

This is a fresh same-harness review of the f188 frozen scope, **not** a continuation of f185 and not a review of any f185 output. The observed clock immediately before preparing this review was `2026-10-29T09:22:56-0700 PDT`. F/M/m denote fatal/major/minor scientific findings; process findings are separately labelled. A zero means no finding within the stated review and imports, not an unconditional theorem or acceptance gate.

## 1. Disposition and process qualification

| Claim or interface | Disposition | Exact scope |
|---|---|---|
| **Source-order process** | **PROCESS MAJOR 1: sequence and early consideration** | All three alternating overlays and E1/E2 preceded both primary sources and the candidate. Cross-packet Lemmas 1–2 were read before the primary sources and candidate, but the rest of that declared file was completed only after the candidate and checker. Before those complete reads, I also noticed the missing q0 factor in Maslova p. 5 by comparison with already-read E2: this was mathematical consideration before the manifest allowed it. Strict complete-input-before-consideration/order compliance was not met and must not be certified. |
| Lemma U, exceptional three-index exclusion and direct-P7/Sun8 consequence | **F0 M0 m0 conditional** | For each of the seven displayed characteristic-7 exceptional families, conditional on BBGT Theorem 2(iii)/the actual Table C rows, Zsigmondy, standard group order and faithful-action facts. E1 is essential to this corrected disposition. |
| Lemma O, parabolic Lemma P | **F0 M0 m0 conditional** | Eight indices, pairwise gcd exactly 7; Lemma P uses only the named cross-packet Lemma 2 and elementary cyclotomic facts. Repeated unit cofactors are allowed. |
| Lemma Q, classical groups other than PSL2(7), PSL2(49) | **F0 M0 m0 conditional** | Conditional on the quoted Maslova theorem, group-order/centralizer and classical-form structure, and the indicated 7-part calculations. E2 is essential: item 11 for every even f≥4 cannot be dropped. |
| Statement 2, classical direct-P7 exclusion | **F0 M0 m0 conditional** | Above Lemmas O/P/Q plus cross-packet Lemma 1. It is not a standalone Sun8 theorem. |
| Statement 3, PSL2(49) | **F0 M0 m0**, using the standard PSL2 order and simplicity | Exact support argument below; it excludes eight pairwise-gcd-7 subgroup indices even without coset disjointness. |
| E1 and E2 against uncorrected body | **Two already-disclosed m defects, corrected only in the composite** | E1 fixes a genuinely false general inference about a minus sign; E2 adds the missing even-f item 11. The frozen candidate bytes remain unmodified. These are not newly discovered faults in the E1/E2-corrected arguments. |
| Maslova p. 5 displayed index for item 11 | **Source m1; not a candidate error** | The printed expression omits q0; §5 below derives the correct index, whose oddness is unaffected. We import the classification, not that erroneous numerical formula. |
| Identification with the older cited P7 source; optional Sun7/R8 consequence | **INCONCLUSIVE / outside authorized source reads** | Here P7 means exactly the candidate's explicit eight-disjoint-coset/all-28-gcds-7 condition. The older definition source and Sun7/R8 proof DAG were not read. The elementary proof actually excludes the stronger eight-index configuration in the listed groups. |

The cross-packet file is a declared input in full: Main clarified that the Lemmas 1–2 restriction limits **imports**, not which of its lines may be seen. My earlier message characterizing its heading-search exposure as outside the authorized source was mistaken. The heading search displayed lines 14, 83, 85, 106 and section headings, in addition to the Lemmas 1–2 range; the rest of the 106-LF file was subsequently read. Its Theorem A is for p≥11 and Theorem B is for **p≠7**, not p=7. Neither theorem, Lemma 3, its q=3 table, or its optional corollary is used as a premise in this review. No f185 reasoning, code, frontier or output was opened. A parent directory listing incidentally showed f185 **filenames/metadata only**, not their contents. The old reviewer's earlier exposure to the uncorrected body is not repaired by, or retroactively attributed to, this new review.

No actual derivation in this review used the later-read cross-packet theorems, Lemma 3, tables or corollary, either as premises or as mathematical steps. The elementary cyclotomic argument in §3 was worked out before that late complete-file read; the only cross-packet mathematical imports are Lemmas 1–2. The late completion is a sequencing deviation, not evidence that the candidate is mathematically false or a clean-exposure certificate.

## 2. Frozen inputs and actual read sequence

Manifest `manifest-v1.json`: SHA-256 `6c6db7ff3b1e8da7b6eb50ba07dc54329a6bf8e92829886e7b8cf0810e9d9700`, independently matched before opening declared inputs. Each following complete input's actual bytes, full SHA-256, and count of byte `0x0a` matched its frozen fields. The verification clocks are the actual `/bin/date` observations, PDT on 2026-10-29. The first five JSON documents were also parsed completely as JSON. Basenames below are under `mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/` unless otherwise stated.

| Order | Input basename / role | Bytes | LF | Full SHA-256 | Verification clock |
|---:|---|---:|---:|---|---|
| 1 | `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | 6883 | 56 | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 09:15:48 |
| 2 | `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | 3056 | 11 | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 09:15:50 |
| 3 | `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | 3164 | 10 | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 09:15:51 |
| 4 | `frontier-20261029-char7-f185-pre-source-erratum-v1.json` E1/E2 | 3711 | 34 | `7ad4942fb43ebf1f92268a54e760bad37bfd9761075e3cd4e3d650db93f49ba1` | 09:15:56 |
| 5 | `frontier-20261028-sun-wide-search-preview-frontier-v1.json`, status only | 2402 | 27 | `4ca6a3bb90795334dcd5783463863efe3b194facf1ed92f58f14f44e8689a2e6` | 09:15:59 |
| 6 | `frontier-20261029-lie-type-away-from-seven-v1.md`, cross-packet | 16887 | 106 | `d2af4a0dfa7cbf3a55274aeb30b5657a593737eef6ffd97d2d38a461ea579736` | 09:16:02 |
| 7 | `frontier-20261029-bbgt-2307.13976v2-source.html` | 2262535 | 3658 | `6cf5530f8386133e7208e6e0b77b1b44de78d8546549f2c3faf5144d403f9bfc` | 09:16:10 |
| 8 | `frontier-20261029-maslova-1710.01563v3-source.pdf` | 204412 | 3982 | `108397a5e0db8f4361d629f16c33e08b3810b8bd94a37d38e1fc5aafc9193cac` | 09:16:38 |
| 9 | `frontier-20261029-lie-type-characteristic-seven-v1.md`, all 85 LF | 12204 | 85 | `be02957248ee576d2a2d77a6c99114e0be8e7d1bea1ad42932f031b24ac2491b` | 09:16:59 |
| 10 | `frontier-20261029-char7-arithmetic-check-v1.py`, all 144 LF, **text only** | 4536 | 144 | `2a3e85b8286b43dda8bc62a1b407c25081a9d3bab29308a325b524a89c464b27` | 09:17:08 |

Actual content-read chronology: overlays 1, 2, 3, E1/E2, status-only frontier; cross-packet lines 16–70 (conventions, entire named Lemmas 1–2 and their prose), plus the incidental same-file heading/line exposure above; BBGT Theorem 2, §6 equation (3), §9 notation and Table C; Maslova PDF pp. 1–5, with theorem pp. 3–4 and p. 5 also visually rendered. At that point, before candidate/checker, I noticed the p. 5 missing q0 factor by comparison with the already-read E2; that was premature mathematical consideration. Then came the complete candidate and complete checker as text, followed by mathematical reconstruction and the exact controls. BBGT §2.1's Zsigmondy wording and Remark 9.2 were read subsequently, and finally the complete cross-packet 106-LF body. An actual clock observation after completing that last body was `2026-10-29T09:22:32-0700 PDT`. The primary source HTML/PDF were fully hash/byte/LF checked, but the **consulted mathematical prose was limited to those identified source locations**; this review does not claim to have read every paragraph of either paper. The status frontier's preview snippets are NONINPUT. The author checker was never imported or executed. `reviewer-control-receipt-v1.json` independently records all input byte/hash/LF pins at control execution; those source files were context pins, not inputs to the control program.

Maslova source image artifacts (own rendering, not separate mathematical sources): `reviewer-maslova-page3-v1.png` SHA `639561a34a9e67d51727d2f2cba68946b39025f6b1c906110994eed3686a61f3`; page 4 SHA `6d360ae0f82cee15b80950d945da7f5cc2659998f0cab373b168e9d599fdf568`; page 5 SHA `8e7e89b7bd326360f98b49ac5dcaf607be1e93303ec3136ec255097d06e8a6b4`.

## 3. Exact imports and interfaces

* **BBGT** means Baumeister–Burness–Guralnick–Tong-Viet, pinned HTML Theorem 2(iii), Table C, source HTML LF 3043–3125, §6 equation (3), and Remark 9.2. For G=T simple, odd r and a Sylow r-subgroup R, a qualifying Table C triple asserts the **unique maximal overgroup** property. This classification and its CFSG-dependent proof are imported, not replayed. `r_i` is a primitive prime divisor of q^i−1; α(m,ε) checks `(q^(1/k))^m != ε mod r` for every prime k|f except k=r, β checks the same excluding k=2 and k=r. □ and ⊠ in the literal table mean square and nonsquare respectively. The selected rows meet an f- or r-size alternative; no square/nonsquare alternative is needed.
* **Zsigmondy** is the theorem quoted in BBGT §2.1: a primitive prime divisor of a^n−1 exists except the specified n=2 and (a,n)=(2,6) cases. We use a=7, n=ef≥6 only, so no exception applies. It is an imported theorem, not deduced from the finite controls.
* **Maslova** is the pinned PDF's Theorem in §3, pp. 3–4, classifying maximal **odd-index** subgroups of the listed simple classical groups over odd q, including conditions (1)–(23) below. The theorem and classification infrastructure/CFSG, not its complete proof, are imported.
* **Cross-packet L1/L2** are the specific unreviewed statements: (L1) every proper overgroup of a Sylow 7-subgroup is in a proper parabolic, and (L2) every proper parabolic index is divisible by a specified Φ_e(q), e≥2. They depend on the packet's named BN-pair, root-group, parabolic/Levi and order-polynomial imports. Their fully general classification/structure-theory proof is not certified here; the statements remain conditional imports. For this characteristic-7 application all relevant D are ordinary cyclotomic values; Suzuki–Ree rows are not characteristic 7. I do **not** use its Lemma 3 as an import: directly, Φ_e(0)=1 for e>1, so D≡1 mod q; and D=∏ζ primitive |q−ζ|≥(q−1)^φ(e)>1 for q≥7. Consequently D cannot divide 7.
* Standard structure facts used separately: formulas for p-parts and central quotients of classical/exceptional Lie groups, subfield centralizers and orthogonal/symplectic decomposition stabilizers; projectivization and the indicated similitude/diagonal factors are prime to 7; ordinary factorial bounds; PSL2(q) order and simplicity; and faithful transitive coset action of a nonabelian simple group embeds in A_d. Low-dimensional isomorphisms place any simple low-rank orthogonal/symplectic description into the listed classical groups, e.g. Ω3≅PSL2, Ω5≅PSp4, PΩ6^+≅PSL4, PΩ6^-≅PSU4, and PΩ4^-≅PSL2(q²); nonsimple low-rank products are not simple inputs. These structure facts are conditional imports, not an independent CFSG proof.

## 4. BBGT source-row transcription and the sign/order check

The following is the literal `alttext` TeX of the used rows and all their condition continuations from the pinned Table C. The first G2 and ³D4 rows are included only as context for the blank first columns in their used second rows. Source formatting in the E6 condition has no printed `or` at the end of its f=2 line; no ambiguity affects the r>19 branch used here.

```tex
T&r&\mbox{Type of $H$}&\mbox{Conditions}\\
G_{2}(q)&r_{(3-\epsilon)/2}&A_{2}^{\epsilon}(q)&\mbox{$r=3$ and $f=3^{a}\geqslant 1$, with $q\equiv\epsilon\allowbreak\mkern 4.0mu({\operator@font mod}\,\,9)$ if $p\geqslant 5$ and $f=1$}\\
&r_{3(3-\epsilon)/2}&A_{2}^{\epsilon}(q)&\mbox{$\alpha(3,\epsilon)$ and either $p=2$ and $(\epsilon,q)\neq(-1,4)$, or}\\
&&&\mbox{$p\geqslant 5$ and either $f>3$, or $|R|>r$, or $r>13$, or}\\
&&&\mbox{$f=3$ and either $r=13$ or $p\equiv\pm 1,\pm 3\allowbreak\mkern 4.0mu({\operator@font mod}\,\,9)$, or}\\
&&&\mbox{$f=2$ and $p=\square\allowbreak\mkern 4.0mu({\operator@font mod}\,\,13)$, or}\\
&&&\mbox{$f=1$, $r=13$ and $p=\boxtimes\allowbreak\mkern 4.0mu({\operator@font mod}\,\,13)$}\\
{}^{3}D_{4}(q)&r_{(3-\epsilon)/2}&A_{2}^{\epsilon}(q)\times(q^{2}+\epsilon q+1)&\mbox{$r=3$, $f=3^{a}\geqslant 1$}\\
&r_{12}&q^{4}-q^{2}+1&\mbox{$(q^{1/k})^{6}\not\equiv-1\allowbreak\mkern 4.0mu({\operator@font mod}\,\,r)$ for all $k\in\pi(f)\setminus\{3,r\}$}\\
F_{4}(q)&r_{8}&\Omega_{9}(q)&\mbox{$p\geqslant 3$, $\alpha(4,-1)$ and either $f>2$, or $r>17$, or $|R|>r$, or}\\
&&&\mbox{$f=2$ and either $p=3$ or $p=\square\allowbreak\mkern 4.0mu({\operator@font mod}\,\,17)$, or}\\
&&&\mbox{$f=1$ and $p=\boxtimes\allowbreak\mkern 4.0mu({\operator@font mod}\,\,17)$}\\
E_{6}(q)&r_{9}&A_{2}(q^{3})&\mbox{$\alpha(9,1)$ and either $f>2$, or $r>19$, or $|R|>r$, or}\\
&&&\mbox{$f=2$ and $p=\square\allowbreak\mkern 4.0mu({\operator@font mod}\,\,5)$}\\
&&&\mbox{$f=1$ and either $p=\boxtimes\allowbreak\mkern 4.0mu({\operator@font mod}\,\,5)$ or $p=\boxtimes\allowbreak\mkern 4.0mu({\operator@font mod}\,\,19)$}\\
{}^{2}E_{6}(q)&r_{18}&A_{2}^{-}(q^{3})&\mbox{$\beta(9,1)$ and either $f>1$, or $r>19$, or $|R|>r$, or}\\
&&&\mbox{$f=1$ and either $p=\boxtimes\allowbreak\mkern 4.0mu({\operator@font mod}\,\,5)$ or $p=\square\allowbreak\mkern 4.0mu({\operator@font mod}\,\,19)$}\\
E_{7}(q)&r_{18}&{}^{2}\!E_{6}(q)\times(q+1)&\mbox{$\alpha(18,1)$ and either $f>2$, or $r>37$, or $|R|>r$, or}\\
&&&\mbox{$f=2$ and $p=\square\allowbreak\mkern 4.0mu({\operator@font mod}\,\,37)$, or}\\
&&&\mbox{$f=1$ and either $(q,r)=(2,19)$, or $r=37$ and $p=\boxtimes\allowbreak\mkern 4.0mu({\operator@font mod}\,\,37)$}\\
E_{8}(q)&r_{15(3-\epsilon)/2}&q^{8}-\epsilon q^{7}+\epsilon q^{5}-q^{4}+\epsilon q^{3}-\epsilon q+1&\mbox{$\alpha(30,1)$ and either $r>61$, or $|R|>r$, or $|R|=r=61$ and}\\
&&&\mbox{either $f>2$, or $f=2$, $i=15$ and $d_{p}(r)\in\{15,30\}$}\\
```

To avoid a false general ± inference, let n=ef and pick `ord_r(7)=n`. Since r is odd, `ord_r(7^f)=n/gcd(n,f)=e` and for every prime k|f, `ord_r(7^(f/k))=n/gcd(n,f/k)=ek`. For +1, ek∤m whenever m≤e, k≥2. For −1, ek|2m and ek∤m; `2m≤2e≤ek` forces k=2 and m=e, and then the congruence really is −1. Thus the sign **must** be checked row by row, as E1 requires. β omits k=2 altogether, and the ³D4 source omits k=3 and k=r.

| Table C source specialization | e | actual condition (m,ε) | k=2,m=e risk | Remaining row alternative for q=7^f; verified f=1 / f=2 witness |
|---|---:|---|---|---|
| G2, ε=−1, r6, A2^− | 6 | α(3,−1) | m<e, impossible | p=7≥5; r>13 for f=1,2,3 and f>3 thereafter. r=43 / 181. For f=3, r≡1 mod18 and r>13. |
| ³D4, r12, q⁴−q²+1 | 12 | (6,−1), k∉{3,r} | m<e, impossible | No extra size condition. Exact independent sample r=181 / 409. |
| F4, r8, Ω9 | 8 | α(4,−1) | m<e, impossible | p≥3; r>17 at f=1,2; f>2 thereafter. r=1201 / 169553. |
| E6, r9, A2(q³) | 9 | α(9,+1) | m=e but forbidden sign is +, not − | r>19 at f=1,2; f>2 thereafter. r=1063 (also 37) / 117307. |
| ²E6, r18, A2^−(q³) | 18 | β(9,+1) | m<e; k=2 excluded anyway | r>19 at f=1; f>1 thereafter. r=117307 / 13841169553. |
| E7, r18, ²E6(q)×(q+1) | 18 | α(18,+1) | m=e but forbidden sign is +, not − | r>37 at f=1,2; f>2 thereafter. r=117307 / 13841169553. |
| E8, ε=−1, r30, q⁸+q⁷−q⁵−q⁴−q³+q+1 | 30 | α(30,+1) | m=e but forbidden sign is +, not − | r>61 at f=1,2; f≥3 gives r≡1 mod 30f and r≥91>61. r=6568801 / 555915824341. |

For G2 at f≥3, r≡1 mod6f≥18 and r is prime, so r≥19; hence the size alternative also covers f=3. Zsigmondy gives r for all f, not merely the displayed controls. Since r≠7 and n≥6, r≠2; order divisibility r−1≥n gives r>7, with the e=6,f=1 borderline r=7 excluded because 7 never divides 7^n−1.

Independent exact `Φ_n(7)` factorization and exact order checks, using trial division rather than the author's checker, gave:

| n | Φ_n(7) | factorization | factors whose order of 7 is exactly n |
|---:|---:|---|---|
| 6 | 43 | 43 | 43 |
| 8 | 2402 | 2·1201 | 1201 |
| 9 | 117993 | 3·37·1063 | 37, 1063 |
| 12 | 2353 | 13·181 | 13, 181 |
| 16 | 5764802 | 2·17·169553 | 17, 169553 |
| 18 | 117307 | 117307 | 117307 |
| 24 | 5762401 | 73·193·409 | 73, 193, 409 |
| 30 | 6568801 | 6568801 | 6568801 |
| 36 | 13841169553 | 13841169553 | 13841169553 |
| 60 | 33910865284801 | 61·555915824341 | 61, 555915824341 |

A factor of Φ_n need not have order n: 3 divides Φ9(7) but 7≡1 mod3. At the critical real example E6, f=2, r=117307, `7^9 ≡ −1 (mod r)`, so α(9,+1) holds but a hypothetical α(9,−1) fails. E7/E8 at f=2 have the same sign pattern. This is why E1 is an actual necessary repair, not merely cosmetic.

For the universal exceptional exclusion, if K has r′-index it contains a conjugate of R, hence K is contained in a conjugate of the unique maximal M and [S:M] divides [S:K]. All seven simple exceptional families have 7² dividing their order, whereas 7²∤7!/2=2520. A proper index d≤7 would give a faithful embedding into A_d and hence |S| divides 2520, impossible. Therefore [S:M]≥8. Of three indices, either two are r-divisible, with gcd≥r>7, or two are r′, with gcd divisible by [S:M]≥8. This proves the claimed three-index statement under BBGT and Zsigmondy, and hence both the direct-P7 exclusion and the eight-coset gcd≥8 conclusion. No Sun7 import is needed for this exceptional slice.

## 5. Maslova pp. 3–4: literal item transcription and case verification

In this transcription mathematical notation is normalized to LaTeX, but the source's item conditions and prose are retained. The source notation `n ⪰ m` means each binary digit of m is at most the corresponding digit of n. G is a simple classical group from the theorem, q is odd, V is its natural projective module, and H is maximal of odd index.

1. `H = C_G(σ)` for a field automorphism σ of odd prime order r of the group G, where `q = q0^r`.
2. `G = PSL_n(q)`, H is the stabilizer of a subspace of dimension m of the space V, and `n ⪰ m`.
3. `G = PSU_n(q)` or `G = PSp_n(q)`, H is the stabilizer of a non-degenerate subspace of dimension m of the space V, and `n ⪰ m`.
4. `G = PΩ_n(q)`, H is the stabilizer of a non-degenerate subspace U of even dimension m of the space V, `D(U) = 1`, and `n ⪰ m`.
5. `G = PΩ_n^ε(q)`, H is the stabilizer of a non-degenerate subspace U of dimension m of the space V, and one of the possibilities is realized: (i) m is odd, `D(V) = −1`, and `n−2 ⪰ m−1`; (ii) m is even, `D(U) = D(V) = −1`, `n−2 ⪰ m−2`, `(q,m,sgn(U)) ≠ (3,2,+)`, and if m=n/2, then ε=−; (iii) m is even, `D(U) = D(V) = 1`, and `n ⪰ m`.
6. `G = PSL_n(q)`, H is the stabilizer of a decomposition `V = ⊕ V_i` into a direct sum of subspaces of equal dimension m, and one of the possibilities is realized: (i) `m=2^w≥2` and `(n,m,q)≠(4,2,3)`; (ii) m=1, `q≡1 (mod 4)`, `(n,q)≠(4,5)`, and q≥13 in the case n=2.
7. `G = PSU_n(q)`, H is the stabilizer of an orthogonal decomposition `V = ⊕ V_i` into a direct sum of isometric subspaces V_i of dimension m, and one of the possibilities is realized: (i) `m=2^w≥2`; (ii) m=1, `q≡3 (mod 4)`, and `(n,q)≠(4,3)`.
8. `G = PSp_n(q)`, H is the stabilizer of an orthogonal decomposition `V = ⊕ V_i` into a direct sum of isometric subspaces V_i of dimension m, and `m=2^w≥2`.
9. `G = PΩ_n(q)`, H is the stabilizer of an orthogonal decomposition `V = ⊕ V_i` into a direct sum of isometric subspaces V_i of dimension 1, q is prime, and `q≡±3 (mod 8)`.
10. `G = PΩ_n^ε(q)`, H is the stabilizer of an orthogonal decomposition `V = ⊕ V_i` into a direct sum of isometric subspaces V_i of dimension m, `D(V)=1`, and one of the possibilities is realized: (i) `m=2^w≥2`, `D(V_i)=1`, and `(m,q,sgn(V_i))≠(2,3,−),(2,5,+)`; (ii) `(n,ε)≠(8,+)`, m=1, q is prime, and `q≡±3 (mod 8)`.
11. `G = PSL_2(q)` and `H ≅ PGL_2(q0)`, where `q=q0²`.
12. `G = PSL_2(q)` and `H ≅ A4`, where q is prime and either q=5 or `q≡±3,±13 (mod 40)`.
13. `G = PSL_2(q)` and `H ≅ S4`, where q is prime and `q≡±7 (mod 16)`.
14. `G = PSL_2(q)` and `H ≅ A5`, where q is prime and `q≡±11,±19 (mod 40)`.
15. `G = PSL_2(q)` and `H ≅ D_(q+1)`, where `7<q≡3 (mod 4)`.
16. `G = PSU_3(5)` and `H ≅ M10`.
17. `G = PSL_4(q)` and `H ≅ 2^4.A6`, where q is prime and `q≡5 (mod 8)`.
18. `G = PSL_4(q)` and `H ≅ PSp_4(q).2`, where `q≡3 (mod 4)`.
19. `G = PSU_4(q)` and `H ≅ 2^4.A6`, where q is prime and `q≡3 (mod 8)`.
20. `G = PSU_4(q)` and `H ≅ PSp_4(q).2`, where `q≡1 (mod 4)`.
21. `G = PSp_4(q)` and `H ≅ 2^4.A5`, where q is prime and `q≡±3 (mod 8)`.
22. `G = PΩ_7(q)` and `H ≅ Ω_7(2)`, where q is prime and `q≡±3 (mod 8)`.
23. `G = PΩ_8^+(q)` and `H ≅ Ω_8^+(2)`, where q is prime and `q≡±3 (mod 8)`.

All 23 items were individually checked for q=7^f; the following table records the exhaustive branch disposition, not merely selected examples:

| Items | q=7^f analysis | Result for Lemma Q |
|---|---|---|
| 1 | Odd prime r divides f; q0=7^(f/r), and the 7-exponent gap is `N(f−f/r) ≥ 2N ≥ 2`. | ≥2, conditional on subfield centralizer 7-part. |
| 2 | Every listed linear subspace stabilizer is parabolic. | Excluded by non-parabolic hypothesis. |
| 3 | Unitary gap `f m(n−m)≥2`; symplectic m even gives `f m(n−m)/2≥2`. | ≥2. |
| 4 | n=2a+1, m=2b: gap `f b(n−2b)≥2`. | ≥2. |
| 5(i) | n=2a, m=2b+1, b+c=a−1≥3: gap `f(2bc+b+c)≥3`. | ≥2. |
| 5(ii),(iii) | m=2b, gap `2fb(a−b)≥6`. | ≥2. |
| 6(i), 7(i), 8, 10(i) | k=n/m≥2 and m≥2: linear/unitary gap `fm²k(k−1)/2−v7(k!)`; symplectic/even-orthogonal gap `fm²k(k−1)/4−v7(k!)`. | Both ≥2. |
| 6(ii), 7(ii) | m=1, n≥3: gap `fn(n−1)/2−v7(n!)≥3`. In linear n=2, q≡1 mod4 forces f even, giving gap f≥2. PSU has n≥3. | ≥2. |
| 9, 10(ii) | q prime forces q=7; 7≡−1, not ±3 mod8. | Impossible. |
| 11 | f=2h even; gap is h=f/2, by the separate exact calculation below. | f=2 is PSL2(49), explicitly excluded from Q; all even f≥4 have gap≥2. |
| 12 | q prime means 7, which is neither 5 nor ±3,±13 mod40. | Impossible. |
| 13 | q prime means 7, and 7≡+7 mod16. | Exactly the excluded S=PSL2(7); S4 has index 7. |
| 14 | q prime means 7, not ±11,±19 mod40. | Impossible. |
| 15 | q>7 and q≡3 mod4 force odd f>1, hence f≥3; the 7-gap is f. | ≥3. |
| 16 | q=5, not characteristic 7. | Impossible. |
| 17 | q prime means 7, not 5 mod8. | Impossible. |
| 18 | The projective linear 7-exponent is 6f and the PSp4 factor has 4f; .2 is 7′. | Gap 2f≥2. |
| 19 | q prime means 7, not 3 mod8. | Impossible. |
| 20 | The projective unitary 7-exponent is 6f and the PSp4 factor has 4f; .2 is 7′. | Gap 2f≥2; its congruence in fact forces f even. |
| 21, 22, 23 | q prime means 7, not ±3 mod8. | Impossible. |

**All even exponents in item 11 (E2).** Write f=2h and q0=7^h. For odd q0, `|PSL2(q0²)|=q0²(q0⁴−1)/2` and `|PGL2(q0)|=q0(q0²−1)`. Their quotient is exactly `q0(q0²+1)/2`; since 7∤(q0²+1)/2, its valuation is h. At h=1 it is 175; at h=2 it is 58849=49·1201, and it increases in valuation as h. **Source discrepancy:** Maslova p. 5, in the paragraph proving item 11, visibly prints `|G:H|=(q0²+1)/2`, missing the q0 factor. At q0=7 that printed formula gives 25 rather than 175. The theorem's subgroup type on p. 4 is the imported classification; the correct quotient above and oddness are derived independently. The p. 5 typo cannot be used as valuation evidence.

**Why the displayed valuation formulae hold uniformly.** The 7-parts of the indicated groups are q^N with `N_A=N_U=n(n−1)/2`, `N_C=a²` for n=2a, `N_B=a²` for n=2a+1, and `N_D=a(a−1)` for n=2a. For a nondegenerate orthogonal decomposition, subtract the exponents of both component groups: in type B, `a²−b(b−1)−(a−b)²=b(2a+1−2b)`; in D with odd components, `(b+c+1)(b+c)−b²−c²=2bc+b+c`; in D with even components, `a(a−1)−b(b−1)−(a−b)(a−b−1)=2b(a−b)`. For k equal even-dimensional blocks, subtract k block exponents and the possible wreath permutation factor v7(k!); projective and form-extension factors are 7′. Legendre gives `v7(k!)=(k−s_7(k))/6≤(k−1)/6`, so for k≥2 and m≥2 the smaller block expression is at least `k(k−1)−(k−1)/6>1`, hence integer ≥2. For m=1 and n≥3 the same bound gives `n(n−1)/2−(n−1)/6>2`, hence ≥3. The root exponent gap in item 1 is `(f−f/r)N`, at least 2N because r is an odd prime and r|f. These are universal inequalities; the finite controls below are diagnostics, not a substitute.

## 6. Reconstructing O, P, and the classical/PSL2(49) conclusions

For eight indices with all pairwise gcds 7, write them `7a_i` with pairwise coprime a_i. At most one a_i is even and at most one is divisible by 7; the exceptions can be different, so **at least six**, not seven, indices are odd and have 7-valuation exactly 1. There may be arbitrarily many a_i=1; the old alternating support-counting argument is not used. Two H_i contained in proper parabolics would both have indices divisible by D=Φ_e(7^f); the elementary bound and congruence in §3 show D>1 and D∤7, contradicting their gcd 7. Thus at most one H_i is parabolic-contained.

At least five of the six good H_i are not parabolic-contained. Extend any such H_i to a maximal subgroup M. Its index divides [S:H_i], so it is odd and has 7-valuation 0 or 1. If the valuation is 0, M contains a Sylow 7-subgroup; cross-packet L1 places M in a proper parabolic, contradiction. Hence M is a non-parabolic maximal odd-index subgroup of valuation 1, contrary to the complete item-by-item Lemma Q table, unless S is one of the two explicitly carved-out PSL2 groups. This proves Statement 2 with exactly those imports. The coset-disjointness hypothesis is not needed once all eight pairwise gcds equal 7.

For S=PSL2(49), `|S|=49(49²−1)/2=58800`. It is nonabelian simple, and 58800∤2520; therefore a proper index at most 7 is impossible. In a hypothetical eight-index configuration each a_i>1 and divides `58800/7=8400=2⁴·3·5²·7`. Pairwise coprimality requires eight disjoint nonempty prime supports, whereas only {2,3,5,7} are available. This proves Statement 3 independently of the classification, up to the standard PSL2 order/simplicity facts. PSL2(7) remains explicitly outside the candidate; seven index-7 cosets do not by themselves yield an eight-coset configuration.

## 7. Reviewer-authored exact controls, caps and receipts

The own control program `reviewer-exact-controls-v1.py` has SHA `897ae6a4c5e3e5b276b9f3ad811ed82d5cfa84d6ed523052cb6465c393a1868b`; the bounded runner `reviewer-control-runner-v1.py` has SHA `0eef48c61841cf99927f7bf70927c3c1da02ce42fde09d52e0af4f31e8ae4fb5`. Immutable receipt `reviewer-control-receipt-v1.json` has SHA `92793831de8b94c2b412198f593393073bc205c8540437f6302acf07872c7d02`. It records the actual interpreter, complete command and mode inputs, all context pins, `/bin/date` before/after each subprocess, monotonic time, exit, and stdout/stderr SHA/bytes/LF. Each one-shot subprocess has a 90-second timeout (<120 s); a timeout is `UNKNOWN`, not an exclusion. All seven runs completed, without a cap. Their recorded wall clocks were `2026-10-29T09:20:08-0700 PDT` before and after; the positive run took 0.2305 s and exited 0. Each intended negative exited 1 **with its explicit expected rejection**, not a crash; all stderrs were empty.

| Mode | Actual outcome and intended detection | stdout SHA-256 |
|---|---|---|
| `positive` | PASS: all ten Φ factorizations, exact primality/order, 14 f=1,2 row instances; group-order valuation samples; item 11 even f=2,…,24; PSL2 support. | `47f16106841cb56231456e4df446f1d9e771ad627c5fd36f99cad172c6102c7c` |
| `wrong-minus-sign` | Reject α(e,−1) at the real k=2,m=e E6 arithmetic example. | `348dbf88a850aff63b5e1ee214ab7095e5d0f1dfaa3fd9b39eb69ea68009a93b` |
| `cyclotomic-nonprimitive` | Reject treating the factor 3 of Φ9(7) as primitive of order 9. | `d26e25ffe70301c35c5a12de1fc2d3a7c2d3591dc6391bb660aeb4139fbd1bd4` |
| `item11-missing-factor` | Reject 25 instead of the true index 175. | `045dd383922e98c9a9718e3fc146e148737a63a4e65d862573a126095383b73c` |
| `item11-f4-valuation-one` | Reject valuation 1 at f=4, whose actual valuation is 2. | `6649549f747e35c7bbe09d7b5531c82d19b1c6b335424d9d5547852a4801a9de` |
| `repeated-unit` | Reject the false inference that pairwise-coprime cofactors have at most one unit. | `93d58c6eb3dc040ea9caa05469b1fd479dee52f928fd1c0fb9718cf0da890f1d` |
| `symplectic-factor-two` | Reject omitting the half in the PSp4 nondegenerate gap. | `0c593f1d20b734d7b549d1e5510a23a379848a5792b04455e522fd8375a24da5` |

The positive classical diagnostics used 90 linear, 90 unitary, 56 symplectic, 66 odd-orthogonal, 60 odd-subspace even-orthogonal, 50 even-subspace even-orthogonal, 128 m≥2 block, 48 m=1 block, 20 subfield and four item-(18)/(20) group-order 7-part comparisons. The linear and unitary diagnostic loops deliberately include n=2 and yield minimum 1; the lemma uses n≥3 for the unitary case and treats the linear n=2/parabolic or even-f special case separately. Item 11's universally quantified conclusion follows from the exact formula, not from the f≤24 control range. These diagnostics do not execute or validate the author checker.

**Limit:** This is a source-conditional, same-harness reconstruction with a disclosed sequence major. It is not an independent model-family review, human review, formal/kernel proof, validation of the cited classification proofs, novelty determination, a CFSG-based conclusion for arbitrary finite groups, or a finding about any HELD/ZERO or f161/f162 material.
