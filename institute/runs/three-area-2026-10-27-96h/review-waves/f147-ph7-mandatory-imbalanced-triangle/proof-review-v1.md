# f147 proof slice: geometric-mean symmetrization, mandatory triangle, imbalanced triangle

**Scoped verdicts (same-harness, independently written, not human / independent-family / formal-kernel / novelty verification).**

| Scope | Verdict | Load-bearing dependency |
|---|---|---|
| Spectral mandatory-triangle theorem (irreducible real 7×7 Metzler `G`, spectral bound 0, `D(y)=y[(y+1)²+8/9]²` divides `det(yI−G)` ⇒ `G` has a directed 3-cycle) | **0 FATAL / 0 MAJOR / 3 MINOR** — written argument independently reconstructed and found correct | D1 (nonnegative-domain `Qpol,Hpol>0`, certificate slice) |
| Imbalanced-triangle extension (same hypotheses ⇒ some triple has `G_ij G_jk G_ki ≠ G_ik G_kj G_ji`; stated for `T`) | **0 FATAL / 0 MAJOR / 2 MINOR** — extension at `y⁴` and `y³` independently reconstructed and found correct | D1 |
| PH caller of both (seven-state representation at `z=8/9`) | consistent with the manifest's normalization import, **1 MINOR** (presentational) | D2 (input 2) |
| §6 "consequences" of the mandatory-triangle candidate (combination with the one-triangle-exclusion candidate; eight-edge ⇒ nine-edge corollary), any PH7 existence/nonexistence, minimum order, novelty | **NOT REVIEWED, NOT ADOPTED** | — |

Native clock observed immediately before composing this file: `2026-10-28T21:44:51-0700 PDT` (`2026-10-29T04:44:52Z`). Not an asserted file-creation time.

## 1. Inputs actually read and verified

Manifest `manifest-v1.json` SHA-256 `6ddba0f76b0183136dae7cd3cc822f24e1c591342fcc0c88c12dd7accbc41476`, 4,473 B, verified at `2026-10-29T04:16:13Z`. All seven inputs re-hashed at `2026-10-29T04:16:31Z`; every SHA-256, byte count and LF count equals the manifest. Each text body was read completely in the listed order with exact `:raw` reads; the certificate JSON was parsed in full (13 top-level keys, 5,332 Q and 5,334 H leaf-path strings, two coefficient digests, scope/identity/compactification strings). The two author Python files were read and hashed only; neither was imported or executed, and no author or sibling code is imported by my control script.

| # | Input | SHA-256 (verified) | B / LF |
|---|---|---|---|
| 1 | `dispositions/math-1-ph7-girth-four-two-or-three-cycle-parent-v1.md` | `789b687a…86253f` | 6,488 / 37 |
| 2 | `dispositions/math-1-ph7-global-irreducibility-eight-edges-parent-v1.md` | `42ae3d99…4b281` | 6,427 / 31 |
| 3 | `frontier-20261028-ph7-critical-mandatory-triangle-v1.md` | `d2437a46…48612` | 8,157 / 95 |
| 4 | `frontier-20261028-ph7-critical-imbalanced-triangle-v1.md` | `37660f6c…37fa88` | 4,133 / 40 |
| 5 | `frontier-20261028-ph7-girth4-critical-bernstein-certificate.json` | `b2674b82…6987d8` | 254,486 / 10,697 |
| 6 | `frontier-20261028-ph7-girth4-critical-integer-replay.py` (read/hash only) | `ac5b069e…116177` | 3,631 / 90 |
| 7 | `frontier-20261028-ph7-girth4-nonnegative-boundary-check.py` (read/hash only) | `03d2853e…359ee204` | 1,655 / 33 |

## 2. Independent reconstruction of the mathematics

Notation: `G` irreducible Metzler, `s(G)=0`; `S_ii=G_ii`, `S_ij=√(G_ij G_ji)`; `χ_M(y)=det(yI−M)=Σ_k (−1)^k E_k(M) y^{7−k}` with `E_k` the sum of principal `k×k` minors.

**(a) `S ≤ 0` via Perron left/right Cauchy weights.** Pick `k ≥ max_i(−G_ii)`, so `A=G+kI ≥ 0` is irreducible with Perron root `k` (because `s(G)=0`) and strictly positive right/left Perron vectors `v,w`. With `h_i=√(v_i w_i)>0`, Cauchy–Schwarz on `Σ_j √(A_ij v_j)·√(A_ji w_j)` gives `((S+kI)h)_i ≤ √((Av)_i (Aᵀw)_i) = k h_i`; the `j=i` term is `A_ii h_i` and matches `S_ii+k`. For the nonnegative symmetric matrix `M=S+kI` and positive `h`, `D_h^{-1} M D_h` has row sums `≤ k`, so `ρ(M) ≤ k`; symmetric ⇒ largest eigenvalue `≤ k` ⇒ every eigenvalue of `S` is `≤ 0`. Irreducibility of `S` is never needed; one-way edges only drop terms on the left. Hence `−S` has real eigenvalues `λ_1..λ_7 ≥ 0`, zero allowed. **Confirmed.**

**(b) Cycle-cover comparison through `y³`.** In the permutation expansion a permutation with fixed set `F` contributes `sgn(σ)·Π_{i∉F}(−G_{iσ(i)})·Π_{i∈F}(y−G_ii)`. Per cycle type: fixed points and 2-cycles (and disjoint 2+2) are identical in `G` and `S` since `S_ij S_ji = G_ij G_ji`. A 3-cycle on `{i,j,k}` with forward/backward products `P,P'` contributes to `[y⁴]`: `−(P+P')` in `G` versus `−2√(PP')` in `S`; to `[y³]`: `(P+P')·Σ_{l∉{i,j,k}}G_ll` versus `2√(PP')·Σ_l G_ll` with the same (negative) outside-diagonal factor. A 4-cycle with products `P,P'` contributes to `[y³]`: `−(P+P')` versus `−2√(PP')`. By AM–GM `P+P' ≥ 2√(PP')` (one-way cycles: `P'=0`, `S` term 0). Therefore, for every `G` in the class, `[y⁶],[y⁵]` agree, `[y⁴]χ_G ≤ [y⁴]χ_S` and `[y³]χ_G ≤ [y³]χ_S`; `[y⁴]` is an **equality exactly when every triple is balanced** (`P=P'`, including `P=P'=0`). No other support sizes reach `y³`. This is the candidates' (SAME)/(ORDER) and (CMP), with the correct direction `c3(G) ≤ c3(S)`. **Confirmed**, including the extension from "no triangle" to "all triangles balanced": the triangle terms coincide at both `y⁴` and `y³`, the 2+2 terms coincide, only 4-cycle terms remain and they obey AM–GM.

**(c) Target coefficients and `q>0`.** `D(y)=y⁵+4y⁴+(70/9)y³+(68/9)y²+(289/81)y`. With `χ_G=D·(y²+py+q)`: `[y⁶]=p+4`, `[y⁵]=q+4p+70/9`, `[y⁴]=4q+(70/9)p+68/9`, `[y³]=(70/9)q+(68/9)p+289/81`. Irreducibility makes `0` a simple Perron root with all other eigenvalues in `Re<0`, so the quotient is Hurwitz and `q>0` (also `p>0`). Writing `e_j` for the elementary symmetric functions of the `λ_i` (so `χ_S=Π(y+λ_i)`): `p=e₁−4`, `q=e₂−4e₁+74/9`, `E4:=e₃−4e₂+(74/9)e₁−28/3=0` from the `y⁴` equality, and `E3:=e₄−(70/9)e₂+(212/9)e₁−1007/27 ≥ 0` from the `y³` inequality. **Confirmed symbolically** (receipt S1).

**(d) Elimination.** With `f_j` the elementary functions of any six of the `λ_i` and `x` the seventh: `E4=Ax+B`, `E3=h₁x+h₀`, and the exact polynomial identities `A·q = Qpol/81 + (f₁−4)·E4` and `A·E3 = −Hpol/243 + h₁·E4` hold, so on `E4=0`: `q=Qpol/(81A)`, `E3=−Hpol/(243A)`; also `Qpol−81A² = −81(f₁−4)B`, so `A=0 ⇒ B=0 ⇒ Qpol=0`. Given D1, `A>0` from `q>0`, then `E3<0`, contradicting `E3≥0`. The argument never uses `x≥0`; it uses only that six eigenvalues of `−S` lie in `[0,∞)`. **Confirmed symbolically** (receipt S2) and the reconstructed `Qpol`/`Hpol` (168/435 integer monomials, degree ≤2 per variable, `x`-free) reproduce the certificate's coefficient digests exactly — this links my algebra to the object the certificate slice certifies; it is not itself a positivity verification.

**(e) Conclusions.** Mandatory triangle: if `G` had no directed 3-cycle then all triples are trivially balanced, so (c)–(d) apply and contradict — hence a directed 3-cycle exists. Imbalanced triangle: if every triple were balanced, (b) still gives equality at `y⁴` and `≤` at `y³`, so the same contradiction follows; hence some triple has `P≠P'`, in particular one orientation is positive. Invariance of `P=P'` under positive diagonal similarity and positive scaling (`G=(T+cI)/d` scales each triangle product by `d^{-3}`) lets the statement be made for `T`. **Confirmed.** The direction of every inequality in both candidates is correct.

**(f) PH caller.** The spectral theorems need: exactly seven states, irreducible `G`, `s(G)=0`, `D | χ_G`, and the off-diagonal graph of `G` equal to that of `T`. Input 2's exact statement supplies seven states and strong connectivity for `z=8/9>1/2`; its proof body supplies Perron bound `≤0` after `G=(T+cI)/d` and the roots with at least the pole multiplicities (`−c` at least once, `−a±ib` at least twice ⇒ `0` once and `−1±i√(8/9)` twice in `χ_G`). `s(G)=0` exactly follows because `−c` is a genuine pole (`d²+b²>0`) hence an eigenvalue of `T`. Shift/scale preserves the off-diagonal support. So the caller imports exactly what the normalization result provides, up to the one-line gluing in MINOR-3.

## 3. Actual exact controls (own code, actually run)

Script `proof-controls-v1.py` (final SHA-256 `a5d6b755db84b2f482e4b730317b07749830780a23763d3212d6af63f5472c2e`, 30,288 B, 697 LF), stdlib only, exact `Fraction`/`int`. Receipt `proof-controls-result-v1.json`, SHA-256 `ee1df25aca8d87d1e1bea07eb48dc5220f3e7e1c1992c99f0e9b38f57d7f279e`, 66,140 B. Final run: start `2026-10-29T04:42:18Z`, end `2026-10-29T04:42:20Z`, 1.40 s, Python 3.14.3, **199 checks / 0 failures / `ALL_CONTROLS_PASS`**, exit 0.

Run history (honest): attempt 1 (`04:40:59Z`, script `abc9cd49…`) and attempt 2 (`04:41:20Z`, `2a60abec…`) computed every mathematical check but crashed while serializing the JSON receipt (`Fraction`, then tuple keys); the partial receipt files were overwritten by my later runs. Attempt 3 (`04:41:32Z`, `183ef36d…`) reported 198/199: the only failure was my strict-margin Cauchy row check on the P1 similarity control, where Cauchy–Schwarz holds with **exact equality** (`v_j w_j=(4,16,4,4,16,4,4)`, margins `−O(10⁻⁴⁰)` from rounding only); the check was refined to evaluate the row inequality exactly when all `v_j w_j` are perfect squares (equality allowed) and to keep rigorous rational `isqrt` bounds otherwise. No mathematical claim changed between attempts.

- **S1** (symbolic, 7 variables): `D(y)` expansion; `[y⁶..y³]` target formulas on 4 affinely independent `(p,q)`; `e₃−c₄=E4`, `e₄−c₃=E3`, `q=e₂−4e₁+74/9` as exact polynomial identities; a wrong constant (`1007/28`) is detected.
- **S2** (symbolic): `E4=Ax+B`, `E3=h₁x+h₀`, the two elimination identities, `A=0⇒Qpol=−81(f₁−4)B`; mutations (`73/9`, `Qpol+1`) detected; `Qpol`/`Hpol` 168/435 integer monomials, degree 2 per variable, `x`-free, digests `2e26d636…` / `9453ccad…` equal the certificate's; certificate SHA, leaf counts 5,332/5,334 and identity string match.
- **S3** (SAMPLE ONLY): eight exact evaluations on zero faces and interior points, e.g. origin `Qpol=2452, Hpol=21094`; `(0,1,0,2,0,3)`: `1525, 13141`; all positive. Not a positivity proof.
- **S4** (exact rational 7×7 graphs, `Gv=0` with `v>0`, squares arranged so `S` is rational; `χ` by Faddeev–LeVerrier **and** by full 5,040-permutation cycle-type expansion, equal in every case; `−S` tested by all 127 principal minors; left Perron vector by exact nullspace of `Gᵀ`, 1-dimensional and positive; Cauchy rows `(S+kI)h ≤ kh` with rigorous bounds):

| Case | Content | `[y⁴]` G−S | `[y³]` G−S | min minor of `−S` |
|---|---|---|---|---|
| N1 | no triangle; 2-cycles; unbalanced bidirectional 4-cycle (108 vs 1728); two one-way 4-cycles | 0 | −2988 (strict) | 7/3 |
| N2 | one-way 7-cycle + one bidirectional chord; `S` **reducible**; one-way 4-cycle (48 vs 0) | 0 | −48 (strict) | 1 |
| B1 | one **balanced** triangle (18=18), two unbalanced 4-cycles | 0 | −103051/2 (strict) | 7/3 |
| B2 | three balanced triangles (18, 27, 10) sharing edges, one balanced (216=216) and one unbalanced 4-cycle | 0 | −61347/16 (strict) | 3 |
| B3 | balanced triangle, **no 4-cycles** | 0 | **0** | 7/3 |
| U1 | **unbalanced** triangle (8 vs 72) — negative control | **−32** | −72053/3 | 7/3 |
| U2 | one-way triangle (6 vs 0) — negative control | **−6** | −192 | 2 |
| P1 | `G=D·S0·D⁻¹`, every cycle balanced — positive control | 0 (all coefficients equal) | 0 | **0** (singular `S`) |
| R0 | B1 off-diagonals with zero diagonal (`s(G)>0`) — wrong-sign control | — | — | `−S` **not** PSD |

Per-type and per-unoriented-cycle terms were compared exactly in every case: identity/2/2+2 types identical through `y³`; each triangle's `y⁴`/`y³` terms equal exactly `−(P+P')`, `(P+P')·Σ_outside G_ll` versus the `2√(PP')` versions with the same outside factor (e.g. B1: outside sum `−184/3`, both `−2208`; U1: `−14720/3` vs `−2944`); each 4-cycle's `y³` term equals `−(P+P')` vs `−2√(PP')`; the reversed `y³` inequality fails wherever a 4-cycle is strict. U1/U2 show the balance hypothesis is load-bearing precisely at `y⁴`; B3 shows only 4-cycles move `y³`; P1 shows `λ=0` eigenvalues of `−S` do occur in the hypothesis class, so the nonnegative-domain certificate (D1) is genuinely required rather than a formality.

## 4. Findings

- **MINOR-1 (mandatory §3, presentational).** "The bidirectional graph of `S` has no triangle" is true but not the load-bearing fact; what is used is that every triple's forward and reverse `G`-products vanish, so both the `G` and `S` triangle terms are zero at `y⁴` and `y³`. The displayed argument is correct.
- **MINOR-2 (certificate metadata, documentary).** The pinned certificate's embedded `scope` string still reads "all irreducible 7-state Metzler graphs without directed 2- or 3-cycles, not unrestricted PH7". The polynomials are application-independent (my digest linkage confirms they are exactly the elimination polynomials), but the string under-describes the two new applications in which the six variables are eigenvalues of `−S`. No mathematical effect.
- **MINOR-3 (PH caller, both candidates, presentational).** The caller cites the manuscript (`729926c5…`) while the manifest's import is the parent disposition (input 2, `42ae3d99…`), and states the source "provides … spectral bound 0". The disposition literally gives Perron bound `≤ 0` after shift/scale plus the pole roots with their multiplicities; the one-line gluing "`−c` is a simple pole of `H` (`d²+b²>0`), hence an eigenvalue of `T`, hence `0` is an eigenvalue of `G` and `s(G)=0` exactly" should be written out. Consistent otherwise.
- **MINOR-4 (imbalanced extension, presentational).** The proof states `(CMP)` only under the balance hypothesis. In fact `[y⁴]χ_G ≤ [y⁴]χ_S` and `[y³]χ_G ≤ [y³]χ_S` hold for every `G` in the class (verified in U1/U2), and balance is used exactly to upgrade `y⁴` to equality so that `E4=0` is exact; saying so would make the load-bearing use of the hypothesis explicit. Not an error.
- **Remark (both).** Nonnegativity of the seventh eigenvalue `x` is never used; only six nonnegative eigenvalues enter the certificate. Harmless.

No FATAL or MAJOR finding. Every inequality direction, every permutation-cycle cover (2-cycles, disjoint 2+2, triangle with its four outside-diagonal factors, opposite 4-cycle pairs including one-way cycles), `λ_i(−S) ≥ 0` for reducible/singular `S`, `q>0`, the elimination and both conclusions were reconstructed and found correct.

## 5. Load-bearing dependencies

- **D1.** `Qpol>0` and `Hpol>0` on all of `[0,∞)^6` including every zero face. Owned by the certificate slice; the sibling `certificate-review-v1.md` reports a scoped `0 FATAL / 0 MAJOR / 0 MINOR` exact PASS on the nonnegative domain. That is **sibling status, not my verification**; my S3 samples are not a proof, and I did not infer the boundary extension from input 1's positive-rate result. Both theorem verdicts above are conditional on D1.
- **D2.** Input 2's normalization/irreducibility result, used only by the PH-caller form of the statements (seven states, irreducibility, Perron bound after `G=(T+cI)/d`, pole multiplicities). The spectral theorems themselves do not need it.
- **D3.** Ordinary imports: Perron–Frobenius for irreducible nonnegative matrices (simple Perron root, positive left/right vectors), the Collatz–Wielandt / diagonal-scaling row-sum bound, real spectrum of symmetric matrices, Cauchy–Schwarz, AM–GM, the permutation expansion of determinants, and that a real Hurwitz quadratic has positive constant term.
- **D4.** Python 3.14.3 standard-library `int`/`Fraction`/`json`/`sha256` semantics for my controls; same-harness execution.

## 6. Not adopted / out of scope

The mandatory-triangle candidate's §6 (combination with `frontier-20261028-ph7-one-triangle-full-critical-exclusion-v1.md` `2e30b352…`, and the eight-edge ⇒ nine-edge graph corollary) was not reviewed and is not adopted. Nothing here is a PH7 existence or nonexistence result at `z=8/9`, a minimum-order determination, a novelty, priority, formal/kernel, human or independent-family verification, or an admission of any held historical output. Outputs written by this slice: `proof-controls-v1.py`, `proof-controls-result-v1.json`, this file. No author contact, web search, external model, Git, deletion or shared-file edit occurred.
