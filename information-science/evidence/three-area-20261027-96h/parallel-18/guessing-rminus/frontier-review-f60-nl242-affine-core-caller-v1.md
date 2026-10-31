# f60 — review of the affine-four-flat Walsh caller

Reviewer **InfoGuessingRminus-2**. **Verdict: FATAL 0 / MAJOR 0 / MINOR 0 — NO SUBSTANTIVE DEFECT AT THE EXACT CONDITIONAL SCOPE BELOW.** This is same-harness written reasoning plus independently authored exact local computations, not a global existence/no-go proof, formal/kernel proof, external-family/human review, novelty finding or parent adoption.

## 1. Inputs, exact quantifiers and prior familiarity

- The assignment `f60-nl242-affine-core-caller/assignment-v1.json` was read before the candidate; the interrupted original-slot script was pinned first, SHA256 `a4b2979f872db8ef6f3ee9852879a8235178880f19d1d137174398e1e8b96b86`.
- Complete candidate `frontier-20261028-affine-core-caller-v1.md`: SHA256 `e12099f6140b5cf487eb60dd05adbefd9d47d00b3b07f57a815a1e826bcf53ab`, **85 LF / 9876 bytes**.
- Registered Boolean/Walsh definitions: `info-6-full-walsh-definitions-v1.md`, SHA256 `af51f147a8d56e915cbd17687b9a62c859e19cba1937346a8eedd40e108497b1`. My preceding f46 review reconstructed the same full-frequency Walsh/nonlinearity interface; this is disclosed prior familiarity, not blind cognition or transferred review confidence.
- Three source seed strings: `frontier-20261028-published-seeds.txt`, SHA256 `116ab5a7709dd35d951ddc878af227e5e05ce269d8293e5c0c269e158bd051f2`. The three strings were also visually matched to §3.1 of [Kavut and Yücel, arXiv:0808.0684v1](https://arxiv.org/html/0808.0684v1), whose displayed text supplies those strings; the calculations below use the explicitly stated high-bit-first input order.
- Expanded seed-1 move input `frontier-20261028-seed1-second-layer-results.json`, SHA256 `bc2d389fbba21515ba8e52c78b327eb5859080a007816f97cc59d87afb8c537d`, and the required local-rank notation erratum SHA256 `feeba2b56b404e5de5a1107aaa3271f3a5b532a1d35c61b09849a804e88d77fe` were read for exact claim/input identification. The author’s computation was not imported into either independently written checker.

**Exact universal statement reviewed (candidate LF7–18).** Fix ANY affine four-flat `A=x_0+U` in `F_2^9` and ANY Boolean values outside A. For EVERY `alpha in U*`, assume all 32 oriented outside sums R(a) in the corresponding restriction fibre lie in `[-22,26]`, with **both** endpoints attained in that same fibre. Then precisely 448 of all `2^16` local Boolean assignments have full Walsh peak at most 28. A local assignment followed by an affine Boolean addition reaches the balanced peak-28 target iff SOME outside sum is 6 or -2. The initial function need not be balanced or peak-28. Neither existence of such an outside assignment nor absence of other global constructions follows.

## 2. Full outside/local caller and exact interval

For any local sign vector `s(u)=(-1)^g(x_0+u)`, define `L(alpha)=sum_(u in U) s(u)(-1)^(alpha(u))`. Directly separating the 496 outside and 16 inside summands yields, for every a,

```
(-1)^(a·x_0) W_g(a) = R(a) + L(alpha_a).
```

The restriction map `a -> alpha_a` is onto `U*`: extend any character from a basis of U to a basis of V. Its kernel has dimension 5, so each of the 16 fibres has exactly 32 actual frequencies. No choice of a common outside R on a fibre is made.

If peak<=28, the two actual endpoint frequencies in a fibre impose both `|-22+L|<=28` and `|26+L|<=28`, equivalent to `-6<=L<=2`. Conversely, for any R in the stated interval and any L in `[-6,2]`, monotonicity of R+L gives `-28<=R+L<=28`; this covers ALL frequencies. Endpoint attainment is needed for the forward implication and is not inferred from extrema of a different fibre.

Every L is even. Write `u_alpha=(2-L(alpha))/2` in `{0,1,2,3,4}`. Orthogonality on the 16-element space gives

```
sum_alpha L(alpha)^2 = 16 sum_u s(u)^2 = 256,
sum_alpha L(alpha) = 16 s(0).
```

Thus `sum u_alpha` is 8 when `s(0)=1` and 24 when `s(0)=-1`, while `sum u_alpha^2=48+2 sum u_alpha`. The first case would demand 64 with `sum u^2<=4 sum u=32`, impossible. In the second, equality `sum u^2=4 sum u=96` forces each `u` to be 0 or 4. Exactly six are 4. Therefore `L=-6` on a six-set M and `L=2` off it, and `s(0)=-1`. This includes all local sign choices, not a selected sign or a numerical search assumption.

## 3. Fourier/Sidon equivalence and the count 448

For a putative six-set M, Fourier inversion at `u=0` gives s(0)=-1. For every `u!=0`, the sum of all 16 characters is zero, hence

```
s(u)=-(1/2) sum_(alpha in M) (-1)^(alpha(u)).
```

This is a Boolean sign precisely when the six-character sum is ±2 for every nonzero u. Let `r(d)` count **ordered** pairs `(alpha,beta)` in M² with `alpha+beta=d`. Orthogonality applied to the square of that character sum gives

```
16 r(d) = 36 + 4 sum_(u!=0) (-1)^(d·u).
```

For d!=0 the right side is 32, so `r(d)=2`. Conversely, if every nonzero d has r(d)=2, the squared character sum is `6+2 sum_(d!=0)(-1)^(d·u)=4` for each nonzero u. Thus the inverse signs are all ±1 and the required local spectrum is recovered. There are exactly 15 unordered pairs and 15 nonzero differences, so this is equivalent to all pair XORs being distinct. The local signs and M determine one another, hence no multiplicity is lost.

Any five points of a six-set with pairwise-distinct differences are affinely independent: a nontrivial affine dependence among at most five distinct points has even size; size 2 is impossible and size 4 would repeat a pair difference. The XOR of the 15 distinct nonzero differences is zero; each of the six points occurs in five pairs, so the XOR of all six points is zero. Conversely, an ordered affine basis of five points has a distinct sixth point equal to their XOR; no four of the resulting six can sum to zero, so all 15 pair differences are distinct.

The number of ordered affine bases is `16*15*14*12*8`; each six-set appears for six omissions and five orders of the remaining points. Thus the exact number is `16*15*14*12*8/(6*5!)=448`. Translating the six-sets in U* acts transitively on frequencies, so each alpha belongs to `448*6/16=168` of them and is omitted by 280. This proves both choices exist for every alpha, without assuming an additional group orbit classification.

## 4. Exact balance/twist iff, including constants

For any of the 448 choices, `R(a)+L(alpha_a)=0` iff either `R(a)=6` and `alpha_a in M` or `R(a)=-2` and `alpha_a notin M`. The membership/omission counts above guarantee an M exists in either case. Conversely, under the endpoint hypothesis every peak-28 local assignment has only L=-6 or 2, so no other R can yield zero.

If a zero occurs at frequency a, `g(x) xor a·x` has `W(0)=W_g(a)=0`; adding an affine constant merely changes all signs. The affine term permutes the entire Walsh spectrum, preserving its peak. From `d_H(g,a·x+c)=(512-(-1)^c W_g(a))/2`, peak<=28 is exactly NL>=242. If no outside sum is 6 or -2, no peak-28 local assignment has a zero and **no affine Boolean addition** can make it balanced. This is a complete iff only for the fixed outside assignment and flat.

## 5. Three actual source tables and all local spectra

I wrote `frontier-review-f60-affine-core-independent.py` without importing the author’s implementation or check receipts. It reads the three pinned source tables, and separately computes each of the 512 oriented outside sums by direct character summation over the 496 outside points, using x0=365 and the three bases printed in the candidate. All four basis generators are verified linearly independent by their 16-point span; a duplicated-basis mutation was rejected specifically as `BASIS_NOT_INDEPENDENT`.

For each of the three seeds, every fibre has 32 elements and exactly the cited multiset X or Y: six X, ten Y, both endpoints in every fibre, no R=6 or R=-2. The same checker independently computes each input’s full Walsh transform by direct character sums: seed weights `(250,250,242)`, W(0) `(12,12,28)`, peak 28 and zero-free spectra. It generates all 8008 six-subsets of `F_2^4`, checks Sidon differences and Fourier-inverts them, obtaining **448 distinct** Boolean assignments; separately enumerates all **65536** local sign vectors via a local transform and obtains exactly the same set. Every alpha has 168/280 membership/omission incidences.

For EACH of those 448 assignments and EACH of the three seeds, all 512 resulting Walsh values were checked. Every table has the absolute spectrum

```
{|W|=4:30, |W|=12:46, |W|=20:226, |W|=28:210},
```

and no zero, hence no balanced affine twist in that fixed core. The histogram also follows algebraically: with r of the six X-fibres in M, the four X-in/X-out/Y-in/Y-out contributions cancel r in each total. This is an exact finite result about these three seeds and their particular flats, not a theorem about other 16-flats, other starting functions or the global target.

## 6. Seed-1 local flip graph and rank qualification

Independently checking all **100128** unordered pairs among the 448 local assignments gives precisely **10080** Hamming-four edges, degree 45 at every vertex and one component of size 448. Each four-coordinate difference has XOR zero, hence is an affine two-plane inside A; no non-plane Hamming-four edge occurs **inside A**. There are 105 distinct local moves. Their GF(2) closure has 1024 elements, hence dimension/rank 10, and direct evaluation of all 1024 local states gives peak histogram `{28:448, 32:560, 40:16}` and zero balanced peak-28 targets.

The separate `frontier-review-f60-move-input-check.py` checks that the **actual union** of moves in the cited second-layer input equals the independently generated 105 affine two-planes avoiding the local origin. It does not certify the older search history outside this exact move-set equality. The 15 non-origin positions are correct because every valid local vector has `s(0)=-1`; no edge changes that bit.

The local degree-four statement is also direct: `L(0)` is either 2 or -6, so local Hamming weight is 7 or 11, both odd. The coefficient of the four-variable full monomial in the Boolean ANF is the XOR of all 16 local values and is therefore 1. The mandatory notation erratum correctly limits the receipt's `local_polar_rank` to a chosen-origin second-difference matrix; no global quadratic polar-rank claim is accepted.

## 7. Commands, pins and remaining limits

Executed locally after writing the independent programs:

```
python3 -B frontier-review-f60-affine-core-independent.py
python3 -B frontier-review-f60-move-input-check.py
```

- Main independent checker SHA256 `061c6bbf2fe9f5aaf370ceaa7e8b79d80c5fed32dbac7f1c111dcfd8acc263d2`; receipt SHA256 `3c63a43bf163a0842017b9087e75617b0ab8976e97a59492edc6935e4d7faf9d`, observed **Wed Oct 28 17:50:56 PDT 2026**.
- Move-input crosscheck SHA256 `5c1e67c1aa35a9df7d30e2719886749c932e31487b834c5ee1d8e042d220c8d4`; receipt SHA256 `fc30105821e14b4a7429ef90667d18c852f1ba63530ec5666ad57bab02b6a8df`, observed **17:51:35 PDT**.

The proof applies to arbitrary outside assignments **only under both per-fibre endpoints and the stated interval**. The checks use a fixed exact bit-order convention and the three named source tables. No external-model, human, formal or novelty review was performed; no author was contacted. The unbalanced local-family exclusions do not exclude other affine flats, other seeds, outside modifications or a balanced nine-variable NL242 function.

**END OF f60 REVIEW.**
