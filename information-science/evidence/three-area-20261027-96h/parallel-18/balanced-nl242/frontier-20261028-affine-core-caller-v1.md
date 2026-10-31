# info-6 frontier: an exact 16-cell construction/obstruction caller

Owner **InfoBalancedNL242-2-2**, original balanced nine-variable target. Native `/bin/date` observed before writing: **2026-10-28T17:42:39-0700 PDT**. **NEW WRITTEN CANDIDATE, NOT YET DISJOINTLY REVIEWED OR ADOPTED.** The theorem below is universal over all outside truth assignments satisfying its explicitly stated spectral premise. Its application to three named published inputs is independently checked. Neither establishes an unrestricted witness or no-go, or novelty.

## 1. Universal exact caller

Let V=F₂⁹, let A=x₀+U be any affine 4-flat, and fix arbitrary Boolean values outside A. For each frequency a define the **oriented outside sum** and the restricted character

    R(a)=χ_a(x₀) Σ_{x∉A}(−1)^{f(x)}χ_a(x),
    α_a(u)=a·u  for u∈U.                                        (1)

For each of the 16 characters α∈U*, suppose the values R(a) among all a with α_a=α lie in [−22,26], and **both endpoints −22 and 26 occur**. The 16 Boolean signs on A may otherwise be changed arbitrarily. Then:

1. Exactly **448** choices of those 16 signs yield global Walsh peak ≤28.
2. Each such choice has local Walsh spectrum `−6` on a six-element set M⊂U* and `+2` on its complement. The set M is exactly a six-point set with all 15 distinct pairwise XORs (a Sidon six-set).
3. A choice with peak≤28 and **some global Walsh zero** exists iff some outside sum R(a) equals **6 or −2**. If so, an explicit local choice and the affine twist indexed by that zero produce an actual balanced nine-variable function with nonlinearity ≥242. If neither outside value occurs, **no** change on the 16 cells followed by any affine Boolean addition can meet the original target.

This is a conditional construction/obstruction criterion, not a proof that any outside assignment satisfying the premises and trigger exists. It covers all 2¹⁶ local restrictions at once and does not assume an actual initial balanced or NL242 function.

## 2. Proof and exact 448 count

For arbitrary local signs s(u)=(-1)^{g(x₀+u)}, let `L(α)=Σ_{u∈U}s(u)χ_α(u)`. The complete Walsh spectrum obeys

    χ_a(x₀)W_g(a)=R(a)+L(α_a).                                (2)

For a fixed α, the two assumed endpoint outside sums force −6≤L(α)≤2 whenever max|W_g|≤28. Conversely every such L-value works for **all** R∈[−22,26]. Since L is an even integer, define u_α=(2−L(α))/2∈{0,1,2,3,4}. Character orthogonality gives

    Σ_α L(α)²=256,       Σ_α L(α)=16s(0).

The second equality says Σu_α is 8 or 24; the first says Σu_α²=48+2Σu_α. Since u_α²≤4u_α, the first alternative is impossible and the second forces equality termwise. Thus every u_α is 0 or 4, exactly six equal 4, L is −6 on M and +2 elsewhere, and s(0)=−1.

Fourier inversion makes this a Boolean sign vector iff `Σ_{α∈M}χ_α(x)=±2` for every x≠0. Writing `r(d)=#{(α,β)∈M²:α+β=d}`, orthogonality gives `16r(d)=36−4=32` for d≠0. Hence every nonzero d is the sum of exactly one unordered pair from M. Conversely that distinct-pair property gives the same ±2 character sums and, by inversion, an actual local Boolean sign vector with L=2−8·1_M. This is a bijection, not a relaxation.

Any five points of a Sidon six-set are affinely independent: an affine dependence among at most five distinct binary points would contain four with zero sum, giving repeated pair differences. The XOR of all six points is zero because the XOR of the 15 distinct nonzero pair differences is zero and each point occurs five times. Conversely an ordered affine basis of five points determines the sixth as their XOR, yielding a Sidon six-set. Each six-set is counted by six choices of the omitted point and 5! orders. Thus the exact number is

    (16·15·14·12·8)/(6·5!) = 448.                               (3)

Every character α belongs to the same number of the 448 sets by translation of U*. Counting incidences gives 448·6/16=168 containing α and 280 not containing α. With L∈{−6,2}, a global coefficient in (2) is zero exactly when R=6 and α∈M, or R=−2 and α∉M. Both membership choices are available for every α. This proves the iff and constructs the local signs. If W_g(a)=0, set `h(x)=g(x)⊕a·x`; its full spectrum is a permutation of g's, W_h(0)=0, and all values remain ≤28. ∎

## 3. Application to the three pinned published inputs

For each seed in `frontier-20261028-published-seeds.txt` SHA-256 `116ab5a7709dd35d951ddc878af227e5e05ce269d8293e5c0c269e158bd051f2`, the independently found core has missing/origin point x₀=365 and these four direction generators in the published-input bit order:

| Seed | Basis of U | Outside classes, among the 16 α |
|---|---|---|
| 1 | 27,45,195,325 | six X and ten Y |
| 2 | 63,90,139,278 | six X and ten Y |
| 3 | 27,45,195,325 | six X and ten Y |

Each α has 32 global frequencies. Its oriented outside-sum multiset is one of

    X={−22:15, −6:1, 10:5, 26:11},
    Y={−22:16,         10:4, 26:12}.                            (4)

Thus both endpoints occur in **every** α-class and neither trigger 6 nor −2 occurs. The caller gives, without a global search, exactly 448 peak≤28 restrictions on each full 16-point core and **no balanced twist among them**. In fact every one of the 448 has full absolute Walsh histogram `{4:30,12:46,20:226,28:210}`: if r of the six X-classes belong to M, summing their L=−6/L=2 contributions and the analogous Y contributions cancels r in all four counts. Hence each is an unbalanced NL242 function; this is not a claim about functions outside the fixed core.

## 4. Exact checks, local graph and interpretation caveat

One implementation computed the original full/local Walsh transforms by FWHT and exhausted **all 65,536** local truth tables per seed: it found the stated 448 peak≤28 tables and zero balanceable ones. A separately written checker directly summed all 496 outside truth values for **every one of the 512 global frequencies** per seed, independently confirming all 16 α-class multisets in (4); a duplicate-basis mutation was rejected for the intended reason. A third checker independently examined all 8,008 six-subsets of F₂⁴ by pair differences and direct character inversion: 448 satisfied the Sidon condition, with 448 distinct Boolean tables. These checks substantiate the finite premises/counts; the universal implication is the written proof above.

For seed 1, independently enumerating the expanded local flip span found 1,024 masks of rank 10, with global peak histogram `{28:448,32:560,40:16}` and no target among them. The 448 valid local states form a connected 45-regular graph with 10,080 edges under four-cell flips inside A; independent six-set inversion and all unordered Hamming-four state-pairs reproduced the graph and found no additional non-plane four-flip edges. This is a statement **inside A only**; no claim is made that four-flip moves involving cells outside A cannot leave the graph.

The earlier `core-structure-results.json` calls a diagnostic `local_polar_rank`; the mandatory additive `frontier-20261028-core-structure-notation-erratum-v1.md` clarifies that it is a second-difference matrix rank at a chosen origin, not a global quadratic polar rank. The local restrictions have degree 4; no global-polar claim is used here.

## 5. Pinned evidence

All paths below are in the exclusive `balanced-nl242` root; SHA-256 values were measured from actual bytes. The common filename prefix `frontier-20261028-` is omitted.

| File | SHA-256 | LF | Use |
|---|---|---:|---|
| `core-census.py` | `1db28b1e69d36720fe5cf91188955f760939eff26dc24c990c9a2d217163a4ad` | 153 | FWHT/all local restrictions |
| `core-census-results.json` | `7f5b59649bd21e72926e1c7d20d9fd56f9f0d8004d83ed9d0d19068a92d5f04c` | 352 | 3×65,536 census and outside fibres |
| `check-core-outside.py` | `fccda5004d893bc030da5c04603034f7e8a084ef17770a6cc3156883bf99ef96` | 103 | Independent direct outside sums |
| `independent-core-outside-audit.json` | `a3ca2d9a66488892ea1b33990aac68324faa3df4fe4f3243fc206a18b009be7d` | 53 | Exact X/Y and mutation checks |
| `core-sixsets-check.py` | `735765570d64505010c20c499ed63c19831c80bfb4e66c8be062901d8931ce11` | 67 | Difference-set and inverse check |
| `core-sixsets-check-result.json` | `53a01320c4ee888023b2e3e251ed3b264a5cb4bc92e54ea0f0ba5a6cb63ff565` | 8 | 8,008 checked, 448 exact |
| `core-graph.py` | `97fe5f3a5e818a7bcbbd2dc94e4bdc54fecfbcf229dac8886707b152855d3993` | 105 | Seed-1 induced graph |
| `core-graph-results.json` | `37bd626bfa4bba22f11f972080acffdec7ebf82263bb205d8838003c00cbf47e` | 20 | 448 vertices, 10,080 edges |
| `core-sidon-graph.py` | `ff1fbb353549c939376f36d95b5889760a9ddb2ea2f3ba3425c55f185734fff0` | 103 | Independent six-set graph |
| `independent-core-sidon-graph-audit.json` | `15a285dab94772af99274e4f5479eb98f958436996bd67a9727af18e749489fb` | 19 | Graph and mutation check |
| `core-hamming-graph.py` | `5854805449da82d9734aafe2adf8753ff321db460ac75a5d7bf9dfba9d08a601` | 78 | All unordered state pairs |
| `core-hamming-graph-results.json` | `3ff8884452ce50de6cc60189d24eecb02088b83158bf4d1d43d56c3e62f7e2cd` | 15 | No extra Hamming-four edges |
| `core-structure-notation-erratum-v1.md` | `feeba2b56b404e5de5a1107aaa3271f3a5b532a1d35c61b09849a804e88d77fe` | 3 | Mandatory rank-field qualification |

All checks above were executed locally using `/opt/homebrew/bin/python3 -B`; the 3×65,536 local census took 1.01 s. Source inspection and the precise published seed/bit-order provenance are in the prior two-flip report. These are actual finite verifications and written deductions, not human, Lean/kernel, independent-model, global search or priority/novelty acceptance. Historical quarantined outcomes are not used as accepted premises. **END.**
