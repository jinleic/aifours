# Review f129 — PH7 at z=8/9: any 7-state irreducible Metzler realization has a directed 2- or 3-cycle

**Verdict: 0 FATAL / 0 MAJOR / 4 MINOR. General theorem ACCEPTED at the exact boundaries below (computer-assisted inequality independently re-established); PH caller ACCEPTED conditional on the one named import.** UTC clock read by `/bin/date` in the same shell command that wrote this file: **2026-10-29T03:43:35Z**.

This is a same-harness written-mathematics and exact standard-library arithmetic review. It is not a human, independent-model-family, formal/kernel or novelty certification. It neither constructs nor excludes any PH7 realization at 8/9; it only evaluates the stated theorem (girth ≥ 4 is impossible) and its PH caller.

## 0. Manifest and inputs

Manifest `manifest-v1.json` SHA-256 `bdfa01e52e02bfecbfd7e4f05e031411ce31445c2299f16be1b02087fcbec369` (3317 B) — matched. Every input was read completely, in declared order, after full SHA-256/bytes/LF verification (all matched the manifest):

| # | role | SHA-256 | bytes / LF |
|---|------|---------|-----------|
| 1 | adopted girth≥5 disposition (framework only) | `de045d1b…cc9892` | 6597 / 41 |
| 2 | theorem candidate `frontier-20261028-ph7-critical-two-or-three-cycle-theorem-v1.md` | `76ff3768…e50f33b` | 8013 / 101 |
| 3 | author primary checker `…girth4-critical-bernstein-check.py` (read only) | `8f5fc02b…9e116c4` | 3729 / 69 |
| 4 | author certificate `…girth4-critical-bernstein-certificate.json` (all 10,697 lines read) | `b2674b82…4269e87d8` | 254486 / 10697 |
| 5 | author integer replay `…girth4-critical-integer-replay.py` (read only) | `ac5b069e…e48116177` | 3631 / 90 |

No author code was executed or imported. The certificate JSON was parsed by my own engine only for its two pinned digests and its two leaf-path lists, which are the objects under test. No web search, external model, author contact, Git, deletion or build/test suite was used. The adopted disposition (input 1) was used for framework only; no held outcome is a premise.

## 1. Reconstructed mathematics

Load-bearing premises used: (P1) G is a real 7×7 Metzler matrix, irreducible, with spectral bound 0; (P2) `D(y)=y[(y+1)²+8/9]²` divides `χ_G(y)=det(yI−G)`; (P3) the off-diagonal digraph of G has no directed cycle of length 2 or 3; (P4) Perron–Frobenius for irreducible nonnegative matrices; (P5) the two polynomial inequalities `Qpol>0`, `Hpol>0` on the open positive six-orthant (Section 2).

**1.1 Positive rates.** By (P1),(P4): with `c=max_i(−G_ii)`, `G+cI≥0` is irreducible, its Perron root is `c` (spectral bound of G is 0), and the positive Perron vector `v` satisfies `Gv=0`, so `G_ii v_i = −Σ_{j≠i}G_ij v_j < 0` (every row of an irreducible 7×7 matrix has an off-diagonal positive entry). Hence `u_i:=−G_ii>0`. Let `e_k` be the elementary symmetric functions of `u_1..u_7`.

**1.2 (CHAR), including overlapping cycles.** `det(yI−G)=Σ_σ sgn(σ) Π_{i∉S}(y+u_i) Π_{i∈S}(−G_{iσ(i)})` with `S` the support of σ; a term is nonzero only if every cycle of σ is a directed cycle of the off-diagonal digraph, and it has y-degree `7−|S|`. The coefficient of `y^k` therefore collects permutations with `|S|≤7−k`. Nonidentity permutations with `|S|≤4` are: one 2-cycle, one 3-cycle, one 4-cycle, or two disjoint 2-cycles. Under (P3) only 4-cycles survive, so `[y⁶]=e1`, `[y⁵]=e2`, `[y⁴]=e3`. A 4-cycle is odd (`sgn=−1`) and `Π_{i∈S}(−G_{iσ(i)})=+Π G_{iσ(i)}>0`; its contribution to `[y³]` is `−Π_{i∈S}G_{iσ(i)}` (the `y³` coefficient of the three remaining linear factors is 1). Distinct directed 4-cycles are distinct permutations, so overlapping 4-cycles (sharing vertices or arcs) each contribute their own product; hence `[y³]=e4−C4`, `C4=Σ_{directed 4-cycles} Π(weights) ≥ 0` (zero if there are none). The candidate's extra remark that two disjoint 4-cycles do not fit in seven vertices is true but irrelevant to `[y³]` (see MINOR 3). Independent numeric check: Faddeev–LeVerrier characteristic polynomial of a seeded bipartite girth-≥4 Metzler matrix with 6 mutually overlapping directed 4-cycles reproduced `c6=e1, c5=e2, c4=e3, c3=e4−C4` exactly (receipt `CHAR_spot_check`).

**1.3 Coefficient match.** `(y+1)²+8/9 = y²+2y+17/9`; `(y²+2y+17/9)² = y⁴+4y³+(70/9)y²+(68/9)y+289/81`; so `D(y)=y⁵+4y⁴+(70/9)y³+(68/9)y²+(289/81)y` (engine: `D_coefficients_at_8_9 = 4, 70/9, 68/9, 289/81`). By (P2) and degrees, `χ_G=D·(y²+py+q)` with real `p,q`. Matching:
`[y⁶]: e1=p+4 ⇒ p=e1−4`; `[y⁵]: e2=q+4p+70/9 ⇒ q=e2−4p−70/9`;
`[y⁴]: e3=4q+(70/9)p+68/9 ⇒ E4:=e3−4e2+(74/9)e1−28/3=0`;
`[y³]: e4−C4=(70/9)q+(68/9)p+289/81 ⇒ E3:=e4−(70/9)e2+(212/9)e1−1007/27=C4≥0`
(`4611/81+…`: `(70/9)(−70/9)−… ` all re-derived by hand and by the engine's affine-in-x bookkeeping; `3021/81=1007/27`). These are exactly the candidate's (REQ).

**1.4 q>0.** The eigenvalues of `G+cI` other than the simple Perron root `c` satisfy `|λ'|≤c` and `λ'≠c`; if `Re λ'=c` then `|λ'|≥c` forces `λ'=c`. So every eigenvalue of G other than the simple eigenvalue 0 has strictly negative real part. The roots of `Q=y²+py+q` are eigenvalues of G; `Q(0)≠0` because 0 is a simple root of `χ_G` already carried by D. Real roots `r1,r2<0` give `q=r1r2>0`; complex roots `α±iβ`, `α<0`, give `q=α²+β²>0`. Coincidence with the double roots of D changes nothing.

**1.5 Elimination.** For any six rates with elementary functions `f1..f4` and seventh rate `x`: `e1=f1+x, e2=f2+f1x, e3=f3+f2x, e4=f4+f3x`. Then `E4=Ax+B`, `E3=h1x+h0`, `q=(f1−4)x+A` with
`A=f2−4f1+74/9`, `B=f3−4f2+(74/9)f1−28/3`, `h0=f4−(70/9)f2+(212/9)f1−1007/27`, `h1=f3−(70/9)f1+212/9`
(engine: `closed_forms_match_candidate` all true, including `q`'s constant term `=A` and x-coefficient `=f1−4`). With `Qpol:=81[A²−(f1−4)B]` and `Hpol:=−243[h0A−h1B]`: if `A=0` then `E4=0` forces `B=0` and `Qpol=0`, contradicting (P5); so `A≠0`, `x=−B/A`, and the exact identities `q=Qpol/(81A)`, `E3=−Hpol/(243A)` hold (checked symbolically and at five seeded rational six-tuples, `elimination_spot_checks`). `q>0` and `Qpol>0` give `A>0`; then `Hpol>0` gives `E3<0`, contradicting `E3=C4≥0`. ∎ (The argument never uses `x>0`; incidentally, at all five sampled six-tuples the forced `x` was negative, which is a second contradiction there but is not claimed universally.)

**1.6 Literal coefficient reference.** My abstract-`f` derivation reproduces the candidate's Section 3 lists exactly:
`Qpol = 630f1² − 324f1f2 − 81f1f3 − 1908f1 + 81f2² + 36f2 + 324f3 + 2452`;
`Hpol = 7356f1² − 5724f1f2 + 108f1f3 + 972f1f4 − 18612f1 + 1890f2² − 972f2f3 − 243f2f4 + 1707f2 + 243f3² + 3456f3 − 1998f4 + 21094` (`literal_f_form` both true).

## 2. Independent certificate verification (own engine, actually run)

Engine `reviewer-f129-engine-v1.py` (SHA-256 `431122f8890f6591e1c0c562dfa885363d44edb6c489ff65f2b71ce6706e10bb`, 21303 B) was written for this review and shares no code with the author's checker or replay: elementary symmetric polynomials by the product recursion `Π(1+u_i t)`, affine-in-x elimination at general z, sparse Fraction dictionaries, degree-2 closed-form de Casteljau (`[4b0, 2(b0+b1), b0+2b1+b2]` / `[b0+2b1+b2, 2(b1+b2), 4b2]`), little-endian base-3 indexing, boolean per-coordinate "lo>0 / hi<1" tracking for open-cube vertex detection, explicit prefix-tree partition test. Run on Python 3.14.3, `utc_start 2026-10-29T03:39:06Z` → `utc_end …03:39:12Z`, 5.93 s wall; stdout `reviewer-f129-engine-stdout-v1.txt` (SHA `2f4db5e1dd8f1c9a83404608759fa52fe8d8e4f6dc995409392bfab3b54cf187`), receipt `reviewer-f129-engine-result-v1.json` (SHA `1c67f113d0af7760477a4c524fa7327305511d3aae90c6f5e11d7eaa217c4c89`).

**2.1 Coefficient arrays.** After substituting the elementary sums of `u0..u5`, `Qpol` and `Hpol` are integral with 168 and 435 nonzero monomials, individual degree exactly 2 in each variable. Canonical digests (sorted exponent rows `[[e0..e5],"coeff"]`, compact JSON, SHA-256) equal the certificate's pins `2e26d636…c29658b` and `9453ccad…eb3f6cc2`; term counts and degree vectors match the certificate header.

**2.2 Compactification and Bernstein form.** With `u_i=x_i/(1−x_i)`, `Π_i(1−x_i)²·P(u)=Σ_k [c_k/Π_i C(2,k_i)] Π_i B_{k_i,2}(x_i)` (valid because every exponent is ≤2); so the tensor Bernstein coefficients on `[0,1]⁶` are `b_k=c_k/ΠC(2,k_i)` (scaled by 64 to stay in ℤ; each midpoint split multiplies the common scale by 4). Signs are unaffected. The prefactor is positive on the open cube, so strict positivity of the compactified polynomial on `(0,1)⁶` is strict positivity of `P` on `(0,∞)⁶`.

**2.3 Partition.** Both leaf lists are prefix-free and every proper prefix has both children present (5331 and 5333 internal nodes), so the 5332 (Q) and 5334 (H) closed dyadic boxes are an exact partition of `[0,1]⁶`; conventions: split axis `depth mod 6`, bit `0` = lower half, bit `1` = upper half.

**2.4 Per-leaf receipt (all leaves).** Every one of the 10,666 leaves was reached by my own subdivision from the root array and satisfied: depth ≥6 (min 6; max 29 for Q, 24 for H) and every coordinate split at least once; all 729 scaled coefficients ≥0 (3,887,028 + 3,888,486 = 7,775,514 coefficient checks); every leaf vertex lying in the global open cube has strictly positive coefficient (230,864 + 190,246 = 421,110 vertex checks). Minimal open-cube vertex values of the compactified polynomials: `8760223779601/4503599627370496 ≈ 1.9·10⁻³` (Q) and `94660503049/17592186044416 ≈ 5.4·10⁻³` (H). The minimal coefficient over all leaves is 0, occurring only at infinite-rate boundary vertices (e.g. the vertex `x=(1,…,1)` of leaf `111111`, whose coefficient is the absent total-degree-12 monomial), which is allowed.

**2.5 Strict positivity on the open cube (spelled out).** Let `x∈(0,1)⁶` and let `L` be a leaf box containing it, local coordinates `t_i=(x_i−lo_i)/(hi_i−lo_i)∈[0,1]`. All Bernstein terms are ≥0 by 2.4. Choose the vertex `v` of `L` with `v_i=lo_i` if `t_i=0`, `v_i=hi_i` if `t_i=1`, and otherwise any endpoint of `[lo_i,hi_i]` lying in `(0,1)` — one exists because coordinate `i` was split at least once. Then `v∈(0,1)⁶` (endpoint coordinates equal `x_i∈(0,1)`), so `b_v>0` by 2.4, and the basis weight of `v` at `x` is `Π_i B_{k_i,2}(t_i)` with factor 1 where `t_i∈{0,1}` and positive elsewhere. Hence `P̃(x) ≥ b_v·weight > 0`. This is exactly the leaf predicate my engine checked, so (P5) holds.

**2.6 Negative controls (all actually run, all rejected loudly).**

| control | result |
|---|---|
| Q constant `2452→−2452` | digest mismatch; leaf `111111` negative coefficient `−310720` |
| Q constant `2452→2451` | digest mismatch; leaf `1110000001110001111` negative coefficient |
| H coefficient of `u0²` sign-flipped | digest mismatch; leaf `11111111` negative coefficient |
| Q first leaf `0000000` removed | partition failure: node `000000` lacks a child |
| H leaf #2501 removed | partition failure: node `10010101101011111` lacks a child |
| Q leaf duplicated | rejected: duplicate leaf path |
| Q leaf `00000000` appended (prefix collision) | rejected: `0000000` is a proper prefix of another leaf |
| bit convention flipped (`1`=lower), Q and H | leaf `00001111110011111` / leaf `000000` negative coefficient |
| wrong `z=1/2` | digests mismatch; `Q_{1/2}(1,…,1)=H_{1/2}(1,…,1)=0`; Q cover fails (zero open-cube vertex on leaf `111111`), H cover fails (negative coefficient) |
| wrong `z=7/9` | digests mismatch; both covers fail with negative coefficients |

Incidental observation, outside the reviewed claim and **not adopted**: with the same 8/9 leaf set my engine also certified `Qnum>0` and `−Hnum>0` at `z=1` and `z=10/9` (digests of course differ). This does not transfer any theorem; the candidate claims 8/9 only, and this review adopts nothing beyond 8/9.

**2.7 Author code (read, not executed).** The checker's acceptance predicate (depth ≥6, all coefficients ≥0, every open-cube corner >0, ≥1 interior corner), its scale 64 and integer de Casteljau, and the replay's prefix-walk completeness test agree with the predicate verified here. The PASS lines quoted in the candidate's Section 5 remain author claims; the evidence for this review is my own run above.

## 3. PH caller and exact dependencies

For `H(s)=c(a²+b²)²/[(s+c)((s+a)²+b²)²]`, `a=c+d`, `c,d,b>0`, `z=b²/d²=8/9`: a PH representation `(α,T)` has LST `α·adj(sI−T)·t/χ_T(s)`, so the reduced denominator `(s+c)((s+a)²+b²)²` divides `χ_T`; `G=(T+cI)/d` maps `−c↦0` and `−a±ib↦−1±i·b/d`, so `D|χ_G`, and the positive rescaling preserves the off-diagonal support (hence the girth). The caller's conclusion — every actual PH representation of H with at most seven states contains a directed 2- or 3-cycle — then follows from the theorem **provided** the named import `frontier-20261028-ph7-global-irreducibility-v1.md` (SHA-256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`, 10148 B; existence and hash verified, **content not read in this review**) supplies, as the candidate states: exactly seven reachable states (so 5- or 6-state representations are not left to the present argument, which does not cover them), irreducibility of G, and spectral bound 0. Exact dependencies of the accepted result: (P1)–(P4) as written mathematics, (P5) via my receipt, and for the PH caller additionally the named import and `d=a−c>0`, `b>0`, `z=8/9`.

## 4. Side claim: nine of fourteen eight-arc shapes

A strongly connected simple digraph on 7 vertices with 8 arcs is a directed cycle plus one ear (cyclomatic number 2): a theta with same-direction paths `{p1,p3}` and return path `p2`, `p1+p2+p3=8`, `(p1,p3)≠(1,1)`, or a figure-eight of cycle lengths `{L,8−L}`, `L≥2`. My enumeration (engine `eight_arc_shapes`): 11 thetas + 3 figure-eights = **14**; cycle lengths `{p1+p2, p3+p2}` resp. `{L,8−L}`. Girth ≥4: **9** (theta `{3,4}|1`, `{2,4}|2`, `{3,3}|2`, `{1,4}|3`, `{2,3}|3`, `{1,3}|4`, `{2,2}|4`, `{1,2}|5`, figure-eight `{4,4}`), of which 5 have girth ≥5 (already excluded by the adopted girth≥5 theorem) and 4 contain a 4-cycle and are newly excluded here. The remaining 5 (`{1,6}|1`, `{2,5}|1`, `{1,5}|2`, figure-eights `{2,6}`, `{3,5}`) all have a 2- or 3-cycle and stay open, as the candidate says. The author's "separate graph classification" was not an input; the counts agree with my own enumeration.

## 5. Findings

- **MINOR 1 (expository).** Section 4's one-sentence strict-positivity argument omits why a suitable open-cube vertex always exists (every coordinate split at least once) and how it is chosen on an internal face; Section 2.5 above supplies the argument, and the certified leaf predicate is sufficient. Same qualification as adopted for the girth≥5 result.
- **MINOR 2 (certificate self-description).** The certificate JSON records `split_axis` and the compactification but not the bit convention (`0`=lower half) nor the leaf acceptance predicate; both live only in the checker code. A replay with the opposite convention fails loudly (controls above), so soundness is unaffected, but the certificate should state them.
- **MINOR 3 (expository).** In Section 2 the justification "No two disjoint 4-cycles fit into seven vertices" is irrelevant to `[y³]` (support 8 cannot occur); the support-4 pattern actually excluded by hypothesis is a pair of disjoint 2-cycles. The conclusion "it must be one 4-cycle" is correct.
- **MINOR 4 (caller scope statement).** The theorem itself treats exactly seven states; "at most seven" in the caller relies entirely on the named import for the exactly-seven/irreducibility/spectral-bound facts and for excluding 5–6-state representations. The candidate names the import but should say explicitly that representations with fewer than seven states are not covered by the present argument.

No FATAL or MAJOR finding. No counterexample exists to the stated theorem within its hypotheses; every negative control failed as it should.

## 6. Non-claims

No PH7 existence or exclusion at 8/9; nothing about the five short-cycle eight-arc shapes or higher-arc graphs; no extension to other `z` (the incidental z=1, 10/9 observation is recorded, not adopted); no minimum-order, PH6/PH8, priority or novelty statement; no cure of any earlier process hold. Trusted computation: Python 3.14.3 integers/Fraction/JSON/SHA-256 and my inspected engine; Perron–Frobenius, the permutation expansion and Bernstein facts remain written mathematics.

## 7. Artifacts written (this directory only)

- `reviewer-f129-engine-v1.py` — SHA-256 `431122f8890f6591e1c0c562dfa885363d44edb6c489ff65f2b71ce6706e10bb`, 21303 B (written 2026-10-29T03:38:53Z).
- `reviewer-f129-engine-result-v1.json` — SHA-256 `1c67f113d0af7760477a4c524fa7327305511d3aae90c6f5e11d7eaa217c4c89`, 16479 B (run 2026-10-29T03:39:06Z–03:39:12Z).
- `reviewer-f129-engine-stdout-v1.txt` — SHA-256 `2f4db5e1dd8f1c9a83404608759fa52fe8d8e4f6dc995409392bfab3b54cf187`, 3106 B.
- `review-v1.md` — this file.
