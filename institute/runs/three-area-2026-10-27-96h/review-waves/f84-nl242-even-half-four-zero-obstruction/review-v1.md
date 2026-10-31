# Independent same-harness review: four-zero spatial barrier, even-half obstruction, and coupled ranks

Native `/bin/date` observed immediately before writing: **2026-10-28T19:02:08-0700 PDT**.

## Verdicts and frozen scope

Binding assignment: `manifest-v2.json`, SHA-256 `b1f92ec81e657d78b503c64191a223518e3d89c4929700b65ba2c7565eee79c7`. The three inputs were hash-checked first, then completely read in the manifest order, in raw windows. Each matched its pinned SHA-256, byte count and LF count. No input-identity or other process mismatch was found.

| Input (abbreviation used below) | Full SHA-256; bytes; LF | Verdict within reviewed scope |
|---|---|---|
| S: `frontier-20261028-four-zero-spatial-barrier-v1.md` | `74086dad519c2ec0a0a0378ef4c6b2af151d8c5d05aa515a41a738557f3501c9`; 3,602; 29 | **FATAL 0 / MAJOR 0 / MINOR 0**. The stated selected-filter coexistence is confirmed for the pinned *formal* spectrum, which is not a Boolean witness. |
| E: `frontier-20261028-even-half-four-zero-obstruction-v1.md` | `7344078fb115eb47f9d5e3c731a63d16567cb09d23af4868810c5d45ef38f8c4`; 5,867; 59 | **FATAL 0 / MAJOR 0 / MINOR 0**. The universal inequality, its exclusions and the displayed failed cube are supported. |
| C: `frontier-20261028-even-odd-quadratic-coupling-v1.md` | `30a9d8ec35a9a6d25da2e84caa172d5d019733a49f36b3d5767c75834e5b9c6f`; 6,071; 63 | **FATAL 0 / MAJOR 0 / MINOR 0**. The common-polar classification, necessary table and stated formal survivor are supported. |

These verdicts do not adopt any result on the parent's behalf. **No general exclusion of four-zero balanced targets follows.** In particular, neither E's `Z+F≥64` nor C's table forbids all cases with `Z=4`; the surviving `Z=4, F=140` object is itself only a formal model, not a function. No actual NL242 witness or unrestricted impossibility has been established in this review.

## Reconstruction of the even-half proof

For a balanced Boolean function write `M={x:f(x)=1}`, `|M|=256`, `T=⊕M`, and `n_a=|{x∈M:a·x=1}|`. Directly from the Walsh definition, `k(0)=0=n_0` and for `a≠0`, `k(a)=n_a−128`. Thus `k≡n (mod 4)`, including at zero, and `k(a) mod 2=a·T`. These facts, not an author replay, give E:21–29. On `K=T^⊥`, each coordinate sum `m_i=Σ_{x∈M} b_i·x` is even. The integer XOR expansion modulo four yields

`q(Σ ε_i b_i) = Σ (m_i/2) ε_i + Σ_{i<j} (Σ_{x∈M}(b_i·x)(b_j·x)) ε_i ε_j  (mod 2)`,

so `q=k/2 mod 2` has degree at most two and `q(0)=0`. Hence `h=1+q` is nonzero. For a nonzero Boolean polynomial of degree at most `r≤d`, the support lower bound `2^(d−r)` follows by writing `p=p0+x_d p1`: if `p1=0`, support doubles; otherwise `wt(p0)+wt(p0+p1)≥wt(p1)`, and induction applies to `p1` of degree at most `r−1`, with the trivial `d=r` base. This verifies E:31–33 and does not require the rank classification.

Parseval gives `Σ k²=2^14`. If `T=0`, then `d=9` and at least 128 entries have `q=0`. With `|k|≤7`, even entries with `q=0` have square at most 16, and all other entries have square at most 36; consequently `Σ k²≤128·16+384·36=15,872<16,384`, impossible. Thus `T≠0`, `d=8`, and at least 64 entries on `K` have `q=0`. The cap makes these exactly `k=0,±4`; off `K` the coefficients are odd. Therefore `Z+F=|supp(1+q)|≥64`, and if `Z=4` then `F≥60` (E:7–11, 35–41). The equality example `q=x0+x1+x0x1` has exactly 64 zeros in dimension eight, but this only makes the *isolated polynomial bound* sharp.

For the specified spatial assignment, independent direct evaluation gives the eight cube values `(0,−6,−6,−6,−6,−6,−6,−6)` at `(0,8,16,24,32,40,48,56)` and `Δ8Δ16Δ32 k(0)=−6≡2 (mod 4)` (E:13–17). More generally each parity character in `n_a` has every third XOR difference divisible by four, giving the Boolean necessary condition. The old histogram has `Z=4, F=4`, so the new inequality excludes **every** Boolean sign/frequency assignment of that histogram, not only this one.

For E:43–45, with `U(x)=Σ_a k(a)(−1)^(a·x)` and `R(b)=Σ_a k(a)k(a+b)`, expanding `U(x)^2` gives `Σ_b R(b)(−1)^(b·x)`. The Walsh transform is invertible, so `R=2^14 δ_0` iff every `U(x)=±128`. If also `k(0)=0`, `U/128` is a balanced sign table and its Walsh transform is `4k`. This equivalence says nothing about the realizability of the surviving formal model.

## Reconstruction of the coupled-rank table

For an actual spectrum, the above triple-difference condition gives, for every `u,v∈K`, `Δa0ΔuΔv k(0)≡0 (mod 4)`. The two polar numerators of `q` and `Q=(k(a0+·)−1)/2 mod 2` are even; dividing their difference by two proves equality of polar forms. Consequently `Q+q` is affine, and `Q` is quadratic as well (C:7–12, 27–31).

For an alternating polar form of rank `2r`, select hyperbolic pairs recursively and a radical basis. In these coordinates the quadratic is `Σ x_i y_i` plus a linear function and a constant. Summing its sign over the radical gives zero when a radical linear coefficient is nonzero; otherwise each hyperbolic pair contributes `±2`, so the absolute sum is `2^(8−r)`. Thus the unbalanced weights are `128±2^(7−r)`, and a balanced weight 128 occurs only with nontrivial radical. Rank zero permits weights 0, 128 or 256. Because `q(0)=0`, its zero count `z` is not zero. Taking the union over the *same* rank for q and Q yields exactly C:14–21; the full-rank `z=120 or 136` row cannot include 128. Conversely, canonical quadratics and affine shifts attain every listed marginal pair as polynomials, without implying realization by an actual Walsh spectrum.

Consequently, conditional on `Z=4`, the only values of `F` left by these count constraints are `{60,92,108,116,124,132,140,156,188,252}` (C:23). This is a necessary set, not a claim that any member is realizable.

## Independent exact computations

All checks below are fresh standard-library integer computations in this review directory, with no author script imported or replayed. The first program enumerates all zero-constant quadratics by their ANF truth masks, calculates polar rank using GF(2) elimination, and compares every affine shift with the character-sum rank formula. The reported distribution is `z=wt(1+q)=#zeros(q)`:

| dimension | quadratics | exact distribution `z:count` | quadratic/affine pairs checked |
|---:|---:|---|---:|
| 4 | 1,024 | `4:35, 6:168, 8:435, 10:280, 12:105, 16:1` | 32,768 |
| 5 | 32,768 | `8:155, 12:5208, 16:18259, 20:8680, 24:465, 32:1` | 2,097,152 |

The dimension-eight canonical rank-0/2/4/6/8 quadratics, all linear terms, and all affine shifts give 655,360 pairs; their exact `(z,w)` union agrees with every row of C:14–21. This finite canonical check supplements, not replaces, the symplectic argument above.

A separately coded **actual balanced truth table** is specified completely by its one-support `M={256,…,511}\{256,259,320} ∪ {1,2,64}` in the nine-bit integer convention. Its 512 truth bytes have SHA-256 `60c337f6be420b6b86005e904f06705fec4ef6ce35d5e5b6ba93b6fd869faf42`. Direct double-sum Walsh evaluation gives `T=256`, `q=x0x1`, `Q=x0x1+x0+x1+x6`, common polar rank 2, `z=192`, `w=128`, and matching polars for all 65,536 pairs `(u,v)`. Its maximum `|W|` is **500**, not ≤28: it tests the quadratic identities but is explicitly **not** a target witness, and `z` need not equal `Z+F` without the cap.

Independently reading the two pinned 512-entry formal spectra and evaluating from their entries:

* S:7–15: the counts have `Σk=128`, `Σk²=16,384`, four zeros, four `|k|=4`, 129 peaks, the asserted `{0,1,2,3}` and `{4,5,6,7}` planes, and the claimed odd-half signs. `(wt(P),wt(Q),wt(P∩Q))=(150,120,80)`, and the ANF degree of P is exactly 4. The direct inverse has **493** entries not `±128`; all **511** nonzero-shift autocorrelations are nonzero.
* C:37–45: the explicit second spectrum has `Z=4`, `F=140`, 200 peaks, `z=w=144`, the asserted rank-six q and Q, and the global mod-4 identity at all 512 positions. Its zero set is `{0,64,128,192}`; both the zero and `|k|=4` sets have XOR zero. Its odd-half P has degree 3, and its complement is a 32-point affine 5-flat. The direct inverse has **507** entries not `±128`, and **508** nonzero-shift autocorrelations are nonzero.
* For both spectra, an independent RREF construction enumerated all **97,155** linear 5-directions and their eight cosets, and directly checked all **777,240** affine 5-flat parities for each P. Flipping one indicator bit makes a specified 5-flat parity fail. These checks support S:11–13 and C:43 but do not establish other unstated spatial/energy/exchange conditions.
* From the two histograms, independent direct-binomial Krawtchouk evaluation verified all **257** dual coefficients are nonnegative integers. A separately formulated recurrence computed the inverse and recovered all 257 primal coefficients. `(D254,D255,D256)=(69,0,0)` for the first and `(47,1,0)` for the second. The second dual vector also matches every entry of its pinned count-model receipt. These are exact count identities, **not** a code construction.

## Evidence, imports and limits

All named evidence below lies under `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/`. The additional predecessor `frontier-20261028-four-zero-enumerator-barrier-v1.md` was read and its SHA-256 `6adfa5ecdc131f8ce45ac370e87d36722def54176a35e22b8743a8f150ec2229` verified. The actual spectrum inputs used by the fresh computations were `frontier-20261028-four-zero-spatial-placement-result.json` at `9e7c777f5478a124c122323c875de94f6d7a3ee5fbdc9fb4077840c031bf3f39`, and `frontier-20261028-four-zero-coupled-placement-result.json` at `ba99cc035f8cc8bbbcb9edfc99d9068263e93bdb93dfa9e368b2219f1e223c0f`; the coupled count receipt `frontier-20261028-four-zero-coupled-rank-result.json` was verified at `0a4ebd458300628a6962b6038b91172ddf5aa27dbc2c2075a9702b165bc07406`. The independent program verifies those three hashes again before consuming the JSON.

Fresh, exclusive-created artifacts in the review directory:

| File | SHA-256 |
|---|---|
| `independent-check-v1.py` | `dd1185903e322de4dc739495e8592859fdf60788f497cd24fd0d261e9d030c7f` |
| `independent-check-result-v1.json` | `7e1a17b969255dc47b4adf99953b8699b89ee9544e7b0913def73612b635184a` |
| `independent-balanced-nontrivial-v1.py` | `7c76d92e247e62fe5b917670b7a0bddfcdee696b8747740de89135000cd5930b` |
| `independent-balanced-nontrivial-result-v1.json` | `699c3d08825ef383754714e5feb7bf201677820974f11463a64037958e3c4af0` |

Named imports **not** independently audited as historical or execution claims: the parent disposition `info-6-walsh-caller-and-mod4-coupling-parent-v1.md`; the prior adopted peak-count floor ≥92; the correction record `frontier-20261028-quadratic-scope-correction-v1.json`; and the author-owned solver, finder, checker scripts and their execution/seed histories named in S:23–27, E:47–57 and C:49–61. The results needed here were instead derived from the pinned spectrum bytes or proved above; the count-model JSON listed above is the only author checker/count receipt compared. No assertion is made that the earlier correction history, author finder behavior, or any other imported claim was verified.

This is a same-harness review, not a cross-family or human review, Lean/kernel proof, independent priority/novelty audit, or parent acceptance. No held, withdrawn or quarantined body is used as a premise. No full search over balanced nine-variable functions, nor verification of every previously adopted affine-energy, multiscale, sign or exchange condition, was performed. The four-zero existence/exclusion question remains open **within this review**.
