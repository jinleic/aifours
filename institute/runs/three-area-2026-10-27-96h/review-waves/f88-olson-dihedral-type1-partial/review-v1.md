# f88: independent review of the type-I separated-pair theorem

Observed native `/bin/date` immediately before this write: **2026-10-28T19:02:26-0700 PDT**.
Reviewer: same-harness scientific reviewer; no author contact or external-model review.

## Verdict and finding

**FATAL 0 / MAJOR 0 / MINOR 1.** The stated sufficient-condition theorem for **odd primes** is supported by my reconstruction below. I found no defect in its signed-count or original-position selector argument. This verdict is for the pinned partial theorem only; it does not constitute an acceptance of full type I, `L_RES`, the original Olson target, priority, or novelty.

- **MINOR — reflection-exponent convention omitted.** Candidate LF7 introduces `D_(2p)` and `r` without a presentation, and LF25 first uses reflection exponents `y_i,y_j` without defining them; LF31 and LF39 rely on their signs. Specify a fixed reflection `s`, `r^p=s^2=1`, `srs=r^-1`, and write each reflection at position `t` as `r^{y_t}s`. Under that convention the displayed missing target `y_j-y_i` and four-reflection contribution `y_i-y_j+y_k-y_l` are correct. With the alternative notation `sr^{y_t}`, the corresponding signs reverse. This is a repairable definition/clarity omission, not a counterexample to the theorem.

The manifest informally says “any odd p”; candidate LF7 says **any odd prime** and uses `F_p`. I have reviewed the latter, explicit domain, and make no composite-`p` claim.

## Frozen inputs and process

Manifest `manifest-v1.json`: SHA-256 `0902a8b5755aa55ca52707bd827011f3b99810754dde8e4985e0dd63b9159f94`.
All manifest inputs were hash-checked first and then read completely in the declared order in exact raw windows. Both expected hashes and lengths matched; **no input-hash process finding**.

| Order | Input | SHA-256 | Bytes / LF |
|---|---|---|---|
| 1 | `written-releases/math-2-ordered-word-definitions-v1.md` | `010ef028f750f718df327102ec92e1803289169b512d361bf66ed2e28145c9fc` | 1,275 / 16 |
| 2 | `mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-dihedral-type1-separated-proof-v1.md` | `244dfd9d900ad39e2c26c6aa4497675cb4fc1106c8471a0b34791a9e4e2aa4ec` | 5,448 / 57 |

The first path is under `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`; the second is under `/Users/jinleic/repos/aifours/`. Below, “candidate LF” refers to input 2.

## Reconstruction of the load-bearing argument

Fix the convention in the MINOR finding and choose actual reflection positions `i<j`. The rotation exponent changes sign exactly between them. If `u=Q_j-Q_i`, the actual signed counts are `2p-1-u` of `+a` and `p-3+u` of `-a`. For `1<=u<=p+1`, both are at least `p-2`. Their total is `T_ij=2(1-u)a` in `F_p`: the raw difference is `(p+2)a=2a`, and sign reversal changes it by `-2ua`. This checks candidate LF19–23.

Omit `p-2` rotations, with `q` signed negative and `p-2-q` signed positive. Every `q=0,...,p-2` is feasible and the omitted sum is `-2(q+1)a`. Since `p` is odd prime and `a` is nonzero, these are exactly all nonzero residues. Consequently the `2p-2` selected rotation sums are precisely `F_p\{T_ij}`. The ordered product with `r^{y_i}s,r^{y_j}s` is identity exactly when the selected signed rotation sum is `y_j-y_i`; therefore this pair fails exactly when `y_j-y_i=T_ij`, as required at candidate LF25 and LF29–31.

For selected `i<j<k<l`, the two reversal intervals are disjoint and original. The actual signed rotation counts are `P=2p-1-(u+v)` and `N=p-3+(u+v)`. The hypothesis gives `P,N>=p-1`. If both pairs fail, their reflection contribution is `-2(1-u)a-2(1-v)a`, while the signed rotation total is `[2-2(u+v)]a`, so the total exponent is `-2a`. Omitting any `p-1` actual signed positive rotations and one actual signed negative rotation omits `(p-2)a=-2a`. The remaining product has even reflection parity and exponent zero. Exactly `(3p-4)-p+4=2p` distinct original positions remain, in their original order. This checks candidate LF33–41, including the endpoint `p=3`.

## Independently written finite checks

The independent standard-library program `independent-type1-check-v1.py` has SHA-256 `db7d740f60bf20b20abf49fc7ec2431d63ab8229c9025511eb343da362117c27`. Executed once as:

```text
python3 -B independent-type1-check-v1.py independent-type1-receipt-v1.json
```

The exclusive-created receipt has SHA-256 `5d71a69d07f683531bb866192c279e56cd9262ab421421f647764f4d9253d820`. No author implementation or author result was imported by my checker. It constructs candidate selectors using subset enumeration and the dihedral semidirect-product law, then **separately** validates every produced selector by composing the selected polygon permutations right-to-left on every vertex of `F_p`. The validator enforces exactly `2p` distinct, in-range, increasing original indices. It passed a valid positive control and rejected wrong-length, duplicate-index, out-of-range, out-of-order and nonidentity controls for their respective intended reasons.

### Exhaustive p=3

I enumerated **all 673,596 type-I original words**: both nonzero `a`, all `C(11,6)=462` reflection-position layouts, and all `3^6=729` reflection exponent assignments per layout and `a`. There are five `r^a` rotations and no `r^-a` rotations. Of the 924 `(a,layout)` cases, 452 satisfy the four-position condition; thus 329,508 actual words qualify. Across those words I checked **every** qualifying quartet: 1,764,180 word/quartet instances. Their branches were 1,176,120 first-pair selectors, 392,040 second-pair selectors and 196,020 genuine both-pairs-missing/four-reflection selectors. All selectors passed the separate vertex-action check. Across all layouts I also checked the exact low-pair omission residue set and missing target for 9,240 `(a,layout,pair)` instances, including widths 1, 2, 3 and 4.

Separately, for **every** one of the 673,596 words, including the 344,088 outside the theorem condition, I enumerated all rotation subsets for every 2- and 4-reflection choice, and, where needed, tested the only 6-reflection choice. Zero-reflection selectors are impossible because there are only five rotations. Every word had an actual identity selector: the first found used 2 reflections in 672,540 words, 4 in 990, and 6 in 66. In particular, those 66 need six reflections in this finite type-I case; this is a bounded observation, not an all-prime family proof.

### Deterministic p=5 sample

Seed `88052026`: 5,000 shuffled raw words, with `a=1,2,3,4` cycling equally and independently sampled reflection exponents. For each qualifying word the program chose one qualifying quartet by the case number modulo the number of such quartets. **4,335** words qualified; **665** outside the condition were skipped rather than declared solved. For each chosen pair it independently enumerated all 165 selections of eight out of eleven rotations and all omissions of three; all **8,670** pair checks gave the exact claimed missing target and omission residues. Ordinary selector branches were 3,453 first pair, 686 second pair and 196 four reflections. Additionally, 4,335 copies forced both selected pair targets to their missing residues; every copy took the four-reflection branch and passed the separate vertex-action check. This sample is not exhaustive for `p=5`.

## Exact residual and scope

For an actual type-I word, call `(i,j)` a low pair when its reflection positions satisfy `i<j` and `1<=Q_j-Q_i<=p+1`. The reviewed theorem applies exactly when **some** two chronologically separated low pairs `(i,j),(k,l)` with `i<j<k<l` have `(Q_j-Q_i)+(Q_l-Q_k)<=p`. Its precise unhandled complement consists of type-I words for which **every** chronologically separated pair of low pairs has total increment at least `p+1` (vacuously so if there are none). Equivalently, for every `i<j<k<l`, at least one increment is outside `1..p+1` or their sum is at least `p+1`.

This includes zero or one low pair, low pairs with no chronologically separated pair (including overlaps or a shared endpoint), and separated low pairs all having sum at least `p+1`. Widths `p` or `p+1` cannot participate in the sufficient condition with another positive width. Being outside the condition does **not** imply absence of a selector; indeed all such `p=3` words were solved by the separate finite enumeration. The theorem does not establish this condition for every type-I word or resolve the complement for arbitrary odd primes. It also does not cover other rotation multiplicity patterns, arbitrary dihedral words, arbitrary groups, or the original ordered target stated in definitions LF12.

## Named imports and remaining verification limits

Candidate LF51–53 names an author experiment, raw result, separate checker, and check receipt. Their four SHA-256 identities match the hashes printed in the candidate. I read the two scripts and check receipt and parsed the raw result's counts: 532 random cases, 532 forced copies, and the stated branch and skip counts agree with those files. I did **not** regenerate that author's seed, rerun its scripts, or independently replay every one of its 1,064 stored selectors; those author-receipt execution claims remain unverified imports and are not premises of my deduction or independent checks.

Candidate LF47 also refers to an all-high candidate and an all-prime six-reflection-minimum family without importing either proof here; neither is verified or adopted. The first pinned input quotes a transcription of a book source; I did not check the underlying page image or original publication. No priority/openness search, formal proof, human review, external-family review, or general computer enumeration beyond the stated `p=3` and sampled `p=5` work was performed. Hash identity and same-harness review are not substitutes for those gates.
