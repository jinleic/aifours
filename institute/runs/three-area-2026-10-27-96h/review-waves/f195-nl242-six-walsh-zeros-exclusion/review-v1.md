# f195 independent same-harness review: six Walsh zeros

Native clock observed before composition: **2026-10-29T09:57:59-0700 PDT**; this is not a file-creation timestamp.

## Disposition by claim

| Claim | Disposition |
|---|---|
| For every balanced Boolean `f:F₂⁹→F₂` with `max |W_f|≤28`, `|Z|≠6` | **F=0, M=0, m=0; written support conditional on the expressly adopted f131/f152 basic, degree and coset-parity facts and the standard finite-field/Boolean facts identified below.** The complete rank-8 and rank-6 implications are reconstructed below. |
| Fidelity and sufficiency of the basic imports, `(Deg)` and `(P)` | **F=0, M=0, m=0** at the manifest's scope. In particular `(P)` is a conclusion of f131's displayed residue formula for restricted rank at most 2; `⊕Z=0` follows from `(Deg)`. The f131 four-zero reduction and f152 four-zero phase conclusions are not used as six-zero premises. |
| No P1 profile roster, complete rank-two/rank-four closure, or `q|R=0` premise | **F=0, M=0, m=0.** Neither the written rank-6 proof nor the reviewer controls use one. Possible restrictions of `q` to the radical are not assumed. |
| Finite subspace/geometry counts and selected necessary-condition controls | **F=0, M=0, m=0** for the independently exercised finite counts and controls specified below. The positive and intended-reason negative controls do not themselves establish the universal Boolean theorem. |
| Author's claimed exhaustive execution and its reported zero survivors | **INCONCLUSIVE as an execution/reproduction claim:** the author programs and receipts were not run or accepted as evidence, and the 33,732,216-set search was not replayed. The written argument below separately implies the same zero-survivor conclusion for the specified necessary conditions; that implication is not a replay of an author run. |
| Optional union `|Z|≥8` | **INCONCLUSIVE/unadopted as a standalone conclusion in this wave.** It follows *conditionally* by adding a separately established `|Z|≠4` to the present theorem, evenness and `|Z|≥4`; no four-zero exclusion is an input here and none is inferred from f183 or a linked document. |
| Exclusion of eight zeros, an NL242 witness or global NL242 exclusion, and novelty | **INCONCLUSIVE/outside scope.** No such claim is supported here. |

The F/M/m counts are findings on the listed scientific claims, not a human, independent-model-family, formal/kernel or novelty clearance. The author source calls itself unreviewed, and its separate four-zero candidate is not silently adopted.

## Explicit imports and basic reductions

Write `M={x:f(x)=1}`, `|M|=256`, `T=⊕_{x∈M}x`, `k=W_f/4`, and `Z={a:k(a)=0}`. For `a≠0`, `k(a)=#{x∈M:a·x=1}−128`; `k(0)=0`, and `k(a)≡a·T (mod 2)`. Parseval gives `Σ_a k(a)²=2¹⁴`, while the peak hypothesis gives `|k|≤7`.

Only the following mathematical content is adopted from the two scope-only dispositions: `T≠0`; on `K=T^⊥`, the function `q=(k/2 mod 2)|K` is quadratic or lower, with alternating polar `B`; if `rank B≤4`, the peak-bounded zero set has at least eight points; `1_{Z₈}` has degree at most 6; and f131's five-space squared-residue/coset-parity statement. In particular the four-zero conclusions and the unequal radical phase statement in those dispositions are **not** needed. Independently, the displayed f152 bound for `T=0` is consistent: then `q` is quadratic on all nine variables with at least 128 zeros; the peak bound would give `Σk²≤128·16+384·36=15872<16384`.

Under the peak bound, `Z=Z₈={a∈K:k(a)≡0 (mod 8)}`. The degree assertion also has the following direct Lucas-bit reconstruction: for support bits `a·x`, the bit-1 and bit-2 functions of their integer sum are the elementary symmetric polynomials `e₂` and `e₄`; on the even half, `1_{Z₈}=(1+e₂)(1+e₄)`, of degree at most 6. Here `k(a)` and the support count are congruent modulo 8 also at `a=0`. The standard minimum-weight bound for a nonzero degree-≤6 Boolean function on eight variables gives `|Z|≥4`; its total sum, and the sums of `a_i 1_Z(a)`, vanish modulo 2 because their degrees are at most 7. Thus `|Z|` is even and **`⊕Z=0`**. This is the only global zero-sum consequence used in rank 8.

For a five-space `L⊂K` with `rank(B|L)≤2`, f131 gives, for each coset `A`,

`Σ_{a∈A} k(a)² ≡ 16[ wt(q|A)/4 + |A∩Z₈| ] (mod 32)`,

with left side independent of `A`. A quadratic on a five-space with polar rank at most 2 has every affine-coset weight divisible by 8, including possible affine/radical terms. Consequently `|A∩Z| mod 2` is constant over the eight cosets. If `|Z|=6`, that constant cannot be odd, so **every such coset has even zero count**. Since the imported rank-≤4 bound excludes six, only ranks 6 and 8 remain.

## Universal rank-8 reconstruction

Assume `B` is nondegenerate. For a five-space `L`, put `D=L^{⊥_B}`. Since `dim D=3`, the restriction to `L` has rank 2 exactly when `D⊆L`, equivalently when `D` is totally isotropic. Cosets of `L=D^⊥` are labeled by `z↦B(z,·)|D`; their even zero counts therefore imply, for all `x,y∈D`,

`G(x,y):=Σ_{z∈Z}B(z,x)B(z,y)=0` in `F₂`.

Every orthogonal pair lies in an isotropic three-space: extend its span inside its orthogonal complement, using nondegeneracy. Hence `G(x,y)=0` whenever `B(x,y)=0`. For nonzero `x`, the functional `G(x,·)` vanishes on the hyperplane `x^⊥`, so `G(x,·)=c(x)B(x,·)`. If `x,y` are distinct nonzero vectors, `B(x,·),B(y,·)` are independent; linearity at `x+y` forces `c(x)=c(y)=c(x+y)`. Thus **`G=cB`**.

The six covectors `w_z=B(z,·)` are distinct, include zero, and sum to zero. Their span has dimension `d≤4`, so `rank G≤4`; the nonzero possibility `G=B` would have rank 8. Thus `G=0`. Express the six covectors in a basis of their span, as a full-row-rank `d×6` matrix `W'`. If `P` is the injective change-of-coordinates matrix, `0=G=P W'W'ᵀPᵀ`, and a left inverse of `P` gives `W'W'ᵀ=0`. Its row space is therefore a self-orthogonal length-6 binary code, so `d≤3`.

But six distinct points in `F₂^d`, including zero, cannot have zero XOR for `d≤3`: there are too few when `d≤2`; when `d=3`, the XOR of all eight points is zero, so the XOR of the chosen six equals the nonzero XOR of the two distinct omitted points. Contradiction. This uses no `q` or profile classification.

## Universal rank-6 reconstruction

Let `R=rad B` (dimension 2), `V=K/R` (six-dimensional symplectic), and choose any vector-space complement `K=R⊕V`. Let `m(v)` be the number of zero points in the fiber over `v`, reduced modulo 2.

**Fiber evenness.** For every three-space `S≤V`, its full inverse image `L=R⊕S` has dimension 5 and restricted alternating rank at most 2. Evenness on all its cosets says `Σ_{v∈a+S}m(v)=0`. In particular, each third coordinate derivative of `m` is zero at every point; its algebraic normal form has degree at most 2, equivalently `m∈RM(2,6)`. A nonzero degree-≤2 Boolean function on six variables has weight at least 16, but `wt(m)≤6`. Thus `m=0` and **every R-fiber has an even number of zeros**. The RM duality phrasing in the author packet is also consistent; the derivative argument does not require importing a complete weight roster.

The fiber containing zero must have 2 or 4 points, so the only multiplicity patterns are `2+2+2`, `2+4`, and `4+2`. For a nonzero `r∈R` and a totally isotropic two-plane `U≤V`, take `L=⟨r⟩⊕U^⊥`. Here `dim U^⊥=4`, `rad(B|U^⊥)=U`, and `rank(B|L)=2`; cosets have labels `(ρ mod ⟨r⟩, s mod U^⊥)`. A pair in one R-fiber with nonzero difference `d` contributes one point to each first-coordinate label exactly when `d≠r`; if `d=r` its contribution is even in one label. A complete four-point fiber contributes two points to each first-coordinate label.

* In `2+4` or `4+2`, choose `r≠d` for the sole pair. Its split contributions are odd and cannot be canceled modulo 2 by the full fiber, regardless of its quotient label.
* In `2+2+2`, let the three differences be `d₀,d₁,d₂`. If they occupy at most two of the three nonzero elements of `R`, choose `r` outside that set. All three pairs split; among the four quotient labels, three total occurrences cannot all have even multiplicity.
* If the differences are all distinct, set `r=d₀`. The first pair contributes no parity, and the other two split. Evenness would require their distinct quotient-fiber representatives `s₁,s₂` to have the same image modulo `U^⊥`. Their difference `v=s₁+s₂` is nonzero. Nondegeneracy gives `u₁` with `B(u₁,v)=1`; choose `u₂∈u₁^⊥\⟨u₁⟩`. Then `U=⟨u₁,u₂⟩` is isotropic and `v∉U^⊥`, a contradiction.

Thus all rank-6 cases are excluded. This argument deliberately allows zero sets that would violate `q=0` or global XOR, so it does not need an assumption about `q|R`.

## Independent exact controls and limits

Reviewer-authored standard-library code and runner were executed once, not the author code. The runner observed **2026-10-29T09:55:05-0700 PDT** to **09:55:07-0700 PDT**, monotonic **2.317030 s**, exit **0**, child cap **115 s** (below the 120 s limit), no timeout, empty stderr, source hash unchanged across the run. Any cap would have been `UNKNOWN`, not a proof. `PASS` applies only to the enumerated controls.

* Independently generated all **97,155** five-spaces as kernels of canonical three-dimensional dot-annihilators and evaluated the restricted polar ranks. Rank 8 gives **11,475** admissible and **85,680** rank-4 restrictions. Rank 6 gives `(dim(L∩R),rank(B|L))` counts `(0,4):64512`, `(1,2):15120`, `(1,4):16128`, `(2,0):135`, `(2,2):1260`; the admissible total is **16,515**. The four-point radical is even on every rank-6 admissible space; replacing 192 by 193 is rejected for an **odd coset**.
* The same finite geometry finds **5,355** isotropic 2-planes in symplectic dimension 8, each with **15** isotropic 3-space extensions. In dimension 6 it finds **315** isotropic 2-planes; every one of the 63 nonzero vectors is separated by exactly **240** of them. The zero vector is intentionally rejected as having **no separating plane**. A nonisotropic generating pair gives restricted rank 4 and is rejected as **not admissible**.
* All **4,194,304** six-variable degree-≤2 truth tables were traversed by their 22 ANF coefficients as bitsets. The exact weight histogram is `0:1, 16:2604, 24:291648, 28:888832, 32:1828134, 36:888832, 40:291648, 48:2604, 64:1`. Thus the smallest nonzero weight is 16. A degree-3 monomial has weight 8 and is an intended **outside RM(2,6)** negative, not a counterexample.
* A GF(2) linear constraint calculation on all 32,896 ordered `B`-orthogonal pairs gives rank 63 on 64 arbitrary bilinear-form coefficients; the one-dimensional solution space is spanned by nonzero `B`. For six distinct zero-sum columns containing zero in ambient dimensions at most 4, all 168 possibilities have span 4 and none has self-orthogonal Gram. All 168 corresponding four-coordinate embeddings also violate an actual rank-8 admissible-coset constraint. An explicitly non-self-orthogonal Gram is the intended negative.
* Rank-6 split-label checks cover **378** full-fiber/pair examples and **1,701** three-pair representatives, including all 63 nonzero differences of quotient fibers and all 27 radical-difference triples; 378 of those have all three differences distinct. These are controls of the construction, not a six-set census.
* Two seeded genuine balanced functions supplied **64** admissible five-space checks of the residue and parity laws. They are out of target scope: their even-half maxima were `|k|=16,14`, and `Z₈` contained respectively 35 and 29 nonzero coefficients. This deliberately demonstrates why the peak hypothesis is needed to identify `Z₈` with `Z`. Flipping one non-basis/non-pair value of `q` is rejected as **not quadratic**.

Independently of a search, the total number of six-sets containing zero and having XOR zero is `255·254·252·248/120 = 33,732,216`: the first three chosen nonzero points are independent, the fourth lies outside their 3-space, and each set is counted by the 120 ordered choices of four of its five nonzero members. This is a closed-form count, **not** an exhaustive survivor run. A separate in-kernel arithmetic evaluation checked the displayed integer expressions but has no standalone clock/hash/exit receipt; it is not included in the receipted control result.

Remaining mathematical assumptions are the expressly adopted f131/f152 basic/degree/coset-parity statements and the conventional finite-character/Parseval, Lucas-bit, Boolean minimum-weight, alternating-form, and finite-dimensional linear-algebra facts used in the reconstruction. The small finite controls are not substitutes for those universal steps. The separately reviewed four-zero exclusion, if available, remains a separate union premise.

## Frozen read order, coverage, and artifact pins

`RUN=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h`; `EVID=/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242`.

The manifest was the first frozen mathematical input: its SHA was checked **before** its complete read. Then all five input SHA-256/byte/LF counts were computed in manifest order before any mathematical analysis, and all five were read completely in that same order in short raw windows through their final LF. All were UTF-8 and LF-terminated. The two adopted contexts were read only for their manifest-scoped statements; no linked bodies were expanded.

| Read order | Frozen input | SHA-256 | Bytes | LF |
|---:|---|---|---:|---:|
| manifest | `RUN/review-waves/f195-nl242-six-walsh-zeros-exclusion/manifest-v1.json` | `be62e4fc6f55778b0bc1e323e79e9dfa6e62a3dfa4d883e29f16c1a4847a9070` | 4223 | 51 |
| 1 | `RUN/dispositions/info-6-four-zero-rank6-radical-parent-v1.md` | `12efd10b4a9de2ac70cd49541e36e6a0c5df6bd4deecbb74e085c2eb48795dc3` | 5831 | 31 |
| 2 | `RUN/dispositions/info-6-four-zero-unequal-radical-phases-parent-v1.md` | `a31e8f9c5c913d67ab980367e0347d64b1f6ad5e55c8d7bf0aab9efc85fbc6ec` | 6220 | 27 |
| 3 | `EVID/frontier-20261029-sixzero-exclusion-v1.md` | `ded2b06dee27914c401406a86adf45b78d1cc03a7157e29d541cfe8daab8ae9c` | 6351 | 71 |
| 4 | `EVID/frontier-20261029-sixzero-parity-exhaust.cpp` | `acef315f1a6f3c260f73f17aad9c5bb13fe1680150da020aa78bfde38534cd8a` | 5263 | 80 |
| 5 | `EVID/frontier-20261029-sixzero-controls.py` | `9475dbeda3068ed5d74471e7f24c63a532fb3d5370d185bed412692d991ed722` | 4350 | 119 |

Navigation disclosure: before opening the manifest, an initial listing of the run root exposed filenames/metadata including some f161/f162 and neighboring wave names. No corresponding held or sibling file body, mathematical payload, or result was opened or used. Required memory/skill instructions were also read before the manifest; they were not research inputs. There was no source-body read-order deviation, author contact, web/API expansion, author-code execution/import/compilation, Git, deletion, or heavy six-set/Boolean search.

All reviewer artifacts are in this wave directory:

| File | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `reviewer-f195-controls-v1.py` | `dad8c679333840a4aeb8ea1cea12a4d9028b35c702fb837e09224bdeefdeb606` | 15734 | 412 |
| `reviewer-f195-run-v1.py` | `289d8e186670039720959da64c43588ee07aa6bd2ba93bafb048df2714b2d68e` | 2596 | 63 |
| `reviewer-f195-controls-v1.stdout.json` | `81a2af9af9998223eabae236b994dff5f695672ea6b312bf009ea93494afdfd3` | 2570 | 99 |
| `reviewer-f195-controls-v1.stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 | 0 |
| `reviewer-f195-controls-v1-receipt.json` | `c599a968a17c539daade0e5487d89874322c1f300b69c2f70d155bdade5b116a` | 1179 | 28 |

The hash of this review itself is provided at handoff rather than self-embedded.
