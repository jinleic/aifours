# f174 review: Shor universal 55-tail infinite branch

Reviewer **ReviewF174ShorQ55**. Kind: independent **same-harness** scientific review of one prospectively frozen bundle. Native clocks: session start `2026-10-29T07:27:36-0700 PDT`; control run `07:42:35`–`07:42:37 PDT`; observed immediately before writing this report `2026-10-29T07:46:04-0700 PDT`.

**Verdict at the exact manifest scope: PASS. 0 FATAL / 0 MAJOR / 2 MINOR / 3 INCONCLUSIVE, all three non-load-bearing.** Every load-bearing step of theorem (1) was reconstructed independently, conditional only on the standard imports listed in §3. This review covers only the anchored direct-tiling exclusion at `n=165·2^k`, `k≥2`, with `|P|=3·2^k`, `|Q|=55`. It does **not** adopt a numerical order floor, any other tail cardinality, exclusion of a full order, any order outside this family, or Shor finite completion or noncompletion. The original completion problem remains open. Same-harness review is not human, independent-model-family, formal/kernel or novelty acceptance.

## 1. Manifest, inputs and actual source order

| Step | Object | SHA-256 (verified) | Bytes | LF |
|---|---|---|---|---|
| 0 | `review-waves/f174-shor-55-tail-infinite-branch/manifest-v1.json` | `6694b67a997163c5999eed791c577679d06403d62990334be19a4ca53c93f5da` (matches the task) | 2701 | — |
| 1 | `dispositions/math-5-shor-order1320-border-exclusion-parent-v1.md`. Role: adopted same-code framework, **scope only** | `715755734f720c37027d178d17cd2df9b6c69ea48af732b75daebaba25ef9d90` | 9593 | 68 |
| 2 | `mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261028-universal-55-tail-obstruction-v1.md`. Role: universal Q55 candidate | `d6c9929c1a6a2a69f79f4951e76443b752764f035f1d80af9760876aba1c6673` | 5575 | 62 |

What I actually did, in order:

1. Read the manifest and verified its hash.
2. Verified the hash, byte count and LF count of both inputs.
3. Read input 1 completely as one raw read.
4. Read input 2 completely as one raw read.
5. Only then began interpreting the mathematics.

I did not open any other source. That includes the author's family-check script (§5 of input 2), the earlier f128 review, the authority file and any review or result linked from input 1. Main sent two status-only IRC notices during the work (holds on f162/Olson and f161). I have never accessed any material they cover.

## 2. Statement reviewed

Let `k≥2`, `m=2^k` and `n=165m`. There is no direct tiling `P⊕Q=Z_n` with `{0,3,8,11}⊆P`, `{0,1,7,13,14}⊆Q`, `|P|=3m` and `|Q|=55`. The condition `|P|=3m` is implied by `|Q|=55` and `|P||Q|=n`. The statement is uniform in `k`. It is not a statement about every order that admits a 55-element tail; see MINOR m1.

## 3. Standard imports identified

These are reconstructed in writing here. I did not search the literature or check attribution or priority.

* **I1 (mask/cyclotomic criterion).**
  * `P⊕Q=Z_n` iff `|P||Q|=n` and, for every `s|n` with `s>1`, `Φ_s` divides `P(X)` or `Q(X)`.
  * Forward direction: evaluate `P(X)Q(X)≡(X^n−1)/(X−1)` mod `X^n−1` at `ζ_s`.
  * Reverse direction: the DFT of `1_P*1_Q` is `n·δ_0`.
  * `Φ_s|S(X)` iff `S(ζ_s)=0`, because `Φ_s` is irreducible.
* **I2 (fibres).**
  * Since `Φ_{p^j}(1)=p`, `Φ_{p^j}|S(X)` in `Z[X]` forces `p | |S|`.
  * If `Φ_{p^j}|S` for all `1≤j≤e`, then `S` is uniform mod `p^e`. Reason: every nontrivial character of `Z_{p^e}` is a Galois conjugate of some `ζ_{p^j}`, so all nonzero Fourier coefficients of the fibre-count function vanish. Equivalently, reduce `(1+…+X^{p^e−1})R(X)` mod `X^{p^e}−1`.
  * Prime balance is the case `e=1`.
* **I3 (Sands' divisor-class theorem, necessary direction).** In a tiling, no nonzero P-difference and Q-difference share a gcd with `n`.
  * Suppose `δ_P=p−p'≠0` and `δ_Q=q−q'≠0` satisfy `gcd(δ_P,n)=gcd(δ_Q,n)=d`. Write `δ_P=dα` and `δ_Q=dβ` with `α, β ∈ Z_{n/d}^*`.
  * Lift `βα⁻¹ ∈ Z_{n/d}^*` to a unit `u ∈ Z_n^*`. This uses I5. Then `uδ_P≡δ_Q (mod n)`.
  * Galois invariance gives `(uP)(ζ_s)=σ_u(P(ζ_s))`. By I1, `uP⊕Q` is again a tiling.
  * But `up+q'=up'+q`, which contradicts directness.
  * Input 1 gives the same reconstruction. Control N8 sanity-checks it on all tilings of `Z_12, Z_16, Z_18, Z_20`; that is not a proof.
* **I4.** The Chinese remainder theorem: `Z_n≅Z_m×Z_3×Z_5×Z_11`.
* **I5.** `Z_n^*→Z_{n/d}^*` is surjective.
* **I6 (same-code border factorization, Restivo–Salemi–Sportelli type).**
  * Needed **only** for the code-level corollary sentence of input 2 §1, not for theorem (1).
  * Input 1 reconstructs it. Input 1 was adopted only at order-1320 scope.
  * This review did not re-verify it; it is the manifest's stated condition.

## 4. Independent reconstruction and per-lemma verdicts

Write `t(x)=x mod 4`. Since `4|n`, `x mod 4` and the 2-adic valuation `v₂` of a difference that is `≢0 (mod 4)` are well defined on `Z_n`.

**L1 – 2-power ownership and equal fibres: PASS.**
* `|Q|=55` is odd, so by I2 no `Φ_{2^j}` (`1≤j≤k`) divides `Q`.
* By I1 every one of them divides `P`, and by I2 `P` is uniform mod `m`.
* The fibre size is `|P|/m=3`.

**L2 – anchor classes for every `k≥2`: PASS.**
* Tail differences are `±{1,6,7,12,13,14}`. Their gcds with `n` are `{1,2,6,12}` because `12|n`.
* Head differences are `±{3,5,8,11}`. Their gcds are `{3,5,11,gcd(8,n)}`, where `gcd(8,n)` is 4 for `k=2` and 8 for `k≥3`.
* By I3, every `x∈P`, `a∈A` with `x≠a` has `gcd(x−a,n)∉{1,2,6,12}`.
* Control T checks this for `k=2..12`.

**L3 – forced rectangle, `r≡1 (mod 4)`: PASS.**
* Here `x∉A`, because every anchor is `≡0` or `3 (mod 4)`.
* `x−3` and `x−11` are `≡2 (mod 4)`, so the gcd is 2 times an odd part. Forbidding 2 and 6 forces the odd part to contain 5 or 11.
* Their difference is 8, so `(x mod 5, x mod 11)` is `(3,0)` or `(1,3)`.
* For `(1,3)`: `x` and `x−8` are odd and prime to 55. Forbidding gcd 1 forces `x≡0` and `x≡2 (mod 3)`, which is impossible.
* For `(3,0)`, with `x mod 3` free, the gcds are:
  * `gcd(x,n)∈{11,33}`;
  * `gcd(x−3,n)∈{10,30}`;
  * `gcd(x−8,n)∈{5,15}`;
  * `gcd(x−11,n)∈{22,66}`.

  All four are allowed.

**L4 – forced rectangle, `r≡2 (mod 4)`: PASS.**
* `x−0` and `x−8` are `≡2 (mod 4)`, which gives `(0,8)` or `(3,0)`.
* For `(0,8)`: `x−3` and `x−11` are odd and prime to 55, forcing `x≡0` and `x≡2 (mod 3)`, which is impossible.
* For `(3,0)` the gcds are `{22,66}`, `{5,15}`, `{10,30}` and `{11,33}` for anchors 0, 3, 8, 11 respectively. All are allowed.

**L5 – forcing for every `k`: PASS.**
* For `r≡1,2 (mod 4)`, the class `r+mZ_n` contains exactly three admissible elements: `CRT(r, s)` with `s∈{33,88,143}`, i.e. `x≡3 (mod 5)`, `x≡0 (mod 11)`.
* `P` has exactly 3 elements in that class (L1), so all three are forced.
* Machine check, independent of my case split:
  * **R0:** for `t(x)∈{1,2}`, every `x−a` has `v₂≤1`, so `gcd(x−a,n)=gcd(x−a,660)`.
  * **R1:** therefore the exhaustive check over `Z_660` is an all-k verification.
  * **R2:** confirms the two-branch mechanism.
  * **R3:** brute force directly in `Z_n` for `k=2..8` over every class `r`.
* The unforced classes `r≡0,3 (mod 4)` have 18–32 admissible residues.

**L6 – classes 15/30/55 for every `k≥2`: PASS.**
* Take `x=(1 mod m, 143)`. Then `x−8≡−7` (odd) and `≡135 (mod 165)`, so the gcd is 15.
* Take `x=(1,33)`. Then `x−3≡−2 (mod m)` with `v₂=1` because `m≥4`, and `≡30 (mod 165)`, so the gcd is 30.
* Take `x=(1,33)` and `y=(2,88)`. Then `x−y≡−1` and `≡110 (mod 165)`, so the gcd is 55.
* All witnesses lie in the rectangle. Control G checks `k=2..16`.

**L7 – transfer to 660: PASS.**
* Every `h∈H={3,5,11,15,30,55}` has `v₂(h)≤1`.
* If `gcd(d,660)=h`, then `v₂(d)=v₂(h)<2≤k`, so `gcd(d,n)=h`; the converse holds as well.
* Control M checks this exhaustively over all `d∈Z_n` for `k=2..8`.

**L8 – injectivity modulo 660, including `k=2`: PASS.**
* For `2≤a≤k−1`, the elements `(1,33)` and `(1+2^a,33)` are both forced, because `1+2^a≡1 (mod 4)`. Their difference has gcd `165·2^a`.
* If `q≠q'` and `q≡q' (mod 660)`, then `gcd(q−q',n)=165·2^b` with `2≤b≤k−1`. By I3 this is forbidden.
* For `k=2` the projection is the identity.
* Consequence used later: for `q∈Q` and `y∈Y`, `q≠y` implies `q mod 660 ≠ y`.
* Controls G and J check `k=2..16`.

**L9 – mod-11 quota: PASS.**
* `11∤3m`, so by I2 `Φ_11∤P`; by I1 `Φ_11|Q`. Hence `Q` has 5 elements in each class mod 11.
* Projection is injective (L8) and preserves residues mod 11, so the image has 5 elements `≡7 (mod 11)`.

**L10 – four-candidate screen: PASS, by hand and by machine.**

Let `z∈Z_660`, `z≡7 (mod 11)`, `u=z mod 3`, `w=z mod 5`.
* For `y∈{0,1,13,14}`, `11∤z−y`. The gcd lies in `H` iff either `z−y` is odd and `3|z−y` or `5|z−y`, or `z−y≡2 (mod 4)` and `15|z−y`.
* For `y=7`, the gcd lies in `{11,55}⊆H` iff `z−7` is odd and `3∤z−7`.

Case analysis on `t=z mod 4`:
* `t∈{0,2}`: `z−7` and `z−1` are odd. The `y=7` condition forces `u=1`, and then `gcd(z−1,660)∈{3,15}`. No candidates.
* `t=1`: `z` and `z−14` are odd, so `u=1` and `w∈{1,2,3}`. This gives `601, 337, 73`; the other comparisons are harmless.
* `t=3`: again `u=1` and `w∈{1,2,3}`. Now `z−1` and `z−13≡2 (mod 4)`, and `w=1` or `w=3` would make the gcd 30. So `w=2`, giving `z=7`.

Result: exactly `{7,73,337,601}`. Control S1 confirms this list and its split by `t`. Control S2 confirms in `Z_n` (`k=2..8`):
* the class-7 H-admissible set is exactly the `2^k` lifts of these four residues;
* any two of those lifts that agree mod 660 differ by a forbidden `165·2^a`.

**L11 – contradiction: PASS.** Five distinct residues are required (L9), but at most four are available (L10).

## 5. Corollary, background and remarks outside the proof

* **L12 – code-level corollary (input 2 §1, second paragraph): CONDITIONAL.** It follows from theorem (1) by I6. I6 is not re-verified in this wave.
* **L13 – specializations.** The pairs `(12,55)`, `(24,55)`, `(48,55)`, `(96,55)` at orders `660`, `1320`, `2640`, `5280` are correct instances (`k=2..5`). The remark that "the first three had previously received order-specific candidates" is INCONCLUSIVE (i1).
* **Background consistency (non-premise).** At `n=1320` my control (B1) independently reproduces input 1's:
  * 16 forced heads;
  * 15 classes `{3,5,8,10,11,15,22,30,33,55,66,165,220,440,660}`;
  * mod-11 counts `(4,5,5,4,14,14,14,3,14,14,14)`.

  The new proof does not depend on input 1's finite searches.
* **Robustness observation (machine only, unused by the candidate).** The `Z_660` screen with `H` has class counts `[15,4,4,15,9,9,9,4,9,9,9]`. So classes 1 and 2 mod 11 are also deficient.

## 6. Exact control and receipt

The control script was written independently by this reviewer. It uses only the standard library and exact integers, with no author code and no heavy computation.

| Item | Value |
|---|---|
| Script | `ReviewF174ShorQ55-exact-control-v1.py`, SHA-256 `d5b55192bb2f19bf755357820455182aeb34e8bd3cd8d51d8561becc2eddd97d`, 13312 B, 351 LF |
| Result | `ReviewF174ShorQ55-exact-control-v1-result.json`, SHA-256 `e3d362bfca1357608f747bd709d32ef45e940e5c07580cb6fcadd2a7b3b1fecc`, 15124 B, 1118 LF. Exclusive-create write, single run |
| Runtime | `/opt/homebrew/bin/python3`, Python 3.14.3, macOS-27.0.1-arm64 |
| Clock / exit | `2026-10-29T07:42:35-0700 PDT` → `07:42:37 PDT`; `exit=0`; harness wall time 1.85 s |
| Outcome | 131 checks, 0 failed, verdict PASS |

Positive families:
* T (anchor classes, `k=2..12`);
* R0–R3 (rectangle; all-k reduction plus direct check for `k=2..8`);
* G and J (witnesses and collision classes, `k=2..16`);
* M (transfer);
* S1–S2 (screen);
* N7+ (genuine tilings `{0..3m−1}⊕3m{0..54}` with `|Q|=55` satisfy fibre and quota uniformity and Sands disjointness);
* N8 (3956 tilings of `Z_12, Z_16, Z_18, Z_20`; zero violations of Sands or prime-power ownership).

The negative / intended-reason countercontrols below had their numeric predictions hand-derived and hard-coded before the only run. All matched.

| Control | Removed ingredient | Predicted = observed | Intended reason |
|---|---|---|---|
| N1 | head anchor 0, 3, 8 or 11 | admissible counts for `(r≡1, r≡2)`: `(4,14)`, `(8,4)`, `(4,8)`, `(14,4)` vs. full `(3,3)` | each anchor is one of the valuation-1 pair or one of the mod-3 killers |
| N2 | tail class 1 / 2 / 6 / 12 | `(6,6)` / `(18,18)` / `(5,5)` / `(3,3)`. For classes 2 and 6 only "breaks, count >3" was pre-registered; the numbers are observed | 1, 2, 6 essential; 12 is inert (`v₂≤1`), the discrimination case |
| N3 | one class of `H`: 3, 5, 11, 15, 30, 55 | class-7 counts 22, 8, 10, 8, 6, 8 (each ≥5) | every class of `H` is essential to the screen |
| N4 | tail anchor 0, 1, 7, 13, 14 (`H` fixed) | 14, 5, 14, 5, 14 (each ≥5) | every tail anchor is essential; 1 and 13 leave exactly the quota |
| N5 | injectivity (count in `Z_n`) | `2^k` for `k=3..8` | L8 is essential for `k≥3` |
| N6 | rectangle classes 15/30/55 | 14 | L6 is essential |
| N7− | one perturbed tail | not a tiling, and classes intersect | the checker detects failure |

## 7. Findings

* **FATAL:** none.
* **MAJOR:** none.
* **MINOR m1 (scope wording).** The title, the status line and §4 ("This proves the all-order theorem (1)") say "all-order". The theorem is all-`k` within `n=165·2^k`, `k≥2`. It says nothing about other orders admitting `|Q|=55` (e.g. `k∈{0,1}`, or `55t` with `t≠3·2^k`). Input 2 §§1 and 5 scope it correctly ("infinite branch", "just the named infinite family"), so the mathematics is unaffected. Recommended reading: "uniform in `k≥2`".
* **MINOR m2 (self-containment).** §4's decisive finite fact is asserted by "direct exact integer enumeration", supported only by the unexamined author script. The fact is `k`-independent by L7, so there is no all-k gap. The written congruence derivation in L10 and the independent enumeration close it.
* **INCONCLUSIVE i1 (non-load-bearing).** Earlier order-specific candidates at 660 and 2640 are not visible in the frozen inputs. Only `(24,55)` at 1320 appears, inside input 1.
* **INCONCLUSIVE i2 (non-load-bearing).** The author script (§5 of input 2, SHA `9d129c91…`) and its stated native clock were neither read nor executed, as the contract requires.
* **INCONCLUSIVE i3 (non-load-bearing).** Classical attributions, priority and novelty were not checked.

## 8. Deviations and limitations

* I found no deviation from the manifest's read order or write scope.
* The write tool set the executable bit on the script; this is benign.
* The initial `python3 --version` probe ran as a background job; this is benign.
* My only writes are `review-v1.md` and the two reviewer-prefixed files.
* Limitations:
  * Each count in N3, N4 and N6 isolates one step; none is a full tiling search.
  * N8 sanity-checks standard imports in small groups and is not a proof.
  * Verification rests on a written same-harness reconstruction plus stdlib integer arithmetic. There is no proof assistant, independent model family, human or literature check.

## 9. Bottom line

Conditional on the standard imports I1–I5, theorem (1) is correct as written for every `k≥2`. The code-level reading additionally needs I6. The proof steps are:
* odd `|Q|` puts every 2-power cyclotomic factor in `P`, giving three elements per class mod `2^k`;
* the forced CRT rectangle `{x: x mod 4∈{1,2}, x mod 165∈{33,88,143}}`;
* the classes 15, 30 and 55;
* injectivity modulo 660;
* the mod-11 quota of 5 against the 4-element class-7 screen.

Nothing beyond this exact branch is adopted.
