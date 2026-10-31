# Shor completion: conditional order-2640 even-tail obstruction

**Disposition: same-harness computer-assisted written support, conditional on the stated classical tiling inputs and finite-search trust boundary.** For the literal code

`S=b{1,a,a⁷,a¹³,a¹⁴} ∪ {a³,a⁸}b{1,a²,a⁴,a⁶} ∪ a¹¹b{1,a,a²}`,

there is no finite uniquely decipherable, factor-complete D containing S whose actual pure-a atom is `a²⁶⁴⁰` and whose actual tail-border set

`Q={j mod 2640 : b^ℓa^j is an atom of D for some ℓ≥1}`

has even cardinality. The corresponding head border uses actual `a^i b^k` atoms with `k≥1`; P and Q are extracted from the **same D**, not an auxiliary code or single-b slice.

This excludes the even-`|Q|` branch **only at order 2640**. Odd tail at 2640, all other orders, and the unrestricted finite-completion question remain open. The conclusion is not an unconditional order-2640 exclusion, a novelty claim, human or independent-model-family review, or a formal/kernel-certified proof.

Native clock observed before composing: **2026-10-29T07:11:36-0700 PDT**; not a file-creation time.

## Parent reconstruction and computational boundary

Finiteness and factor-completeness force a pure-a atom by embedding a sufficiently long a-run; unique decipherability forbids two distinct pure-a atoms because their two orders commute. Since `b∈S`, it also forbids another pure-b atom. For two putative border representations with the same sum modulo n, choose actual border atoms, a common sufficiently long a-run, and b guards. Their atom lists factor the same `b^H a^G b^K`; positive central a-length and the opposite orientations of the actual border atoms distinguish different residue pairs, contradicting unique decipherability. Conversely an embedded `b^L a^g b^L`, with g longer than any atom, identifies actual left and right b-run border atoms separated by pure-a atoms; varying g proves coverage. Thus `P⊕Q=Z_2640`, with `A={0,3,8,11}⊆P` and `Y={0,1,7,13,14}⊆Q`.

The [Sands divisor-exclusion theorem](https://arxiv.org/html/2106.14042v1#S2.Thmtheorem5) states that a cyclic tiling of sets has disjoint proper gcd-difference classes; it does not require the period to have only two prime divisors. The [Coven–Meyerowitz T2 theorem](https://arxiv.org/html/2106.14042v1#S1.Thmtheorem1) applies to an **integer tile whose own cardinality** has at most two distinct prime factors, combining cyclotomic factors for distinct underlying primes. Parent read those public statements directly; their proofs are not replayed. They apply in the indicated P=12,22,24 branches because the actual P tiles the integers with complement `Q+2640Z`. The finite-maximal-code [actual-border theorem](https://arxiv.org/html/2301.13566v1#S1.Thmtheorem1) was also read directly but is not needed as a substitute for the same-D factor-completeness argument above.

The seven-head argument eliminates `|P|=4,5,6` by direct collisions with the old anchors. The reviewer independently checked the `224`-point head screen and `658`-point tail screen, the complete divisor sieve and a 266-clique cover of the latter. The only remaining even-tail head sizes are `10,12,15,20,22,24,30,33,40,44,55,88`. Each subsequent search is a **necessary relaxation**: it retains stated anchors, forbidden gcds and exact overlapping quotas; a complete UNSAT for a relaxation excludes the actual border, while a SAT result is not a tiling or code witness.

The P=12 two-quota relaxation is genuinely SAT for 16 head choices and six gcd-class patterns when the second owned two-power factor is Φ₁₆. Those survivors are not relabeled UNSAT. The remaining Φ₄Φ₈ ownership imposes eight additional mod-8 fiber quotas; the independent review reports all 146 surviving `(H,a)` cases UNSAT with those quotas and all old anchors. Parent inspected the independent search's include/exclude, forced-group, quota and timeout-to-UNKNOWN logic and the P=12 residual routing, and read its completed receipt; parent did not rerun the search or independently read all 28 pinned author implementations. This is a computer-assisted result conditional on the actual search implementation and its bounded oracle checks, not a proof certificate checked by a kernel.

## Evidence and limits

Parent read the complete 262-LF [self-contained candidate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261028-2640-even-tail-self-contained-review-v1.md), SHA-256 `53296d698836288dc2354e1fb24e4c25f35b2c67454590b4d5a173134bd4706a`, and the complete 197-LF [f157 review](../review-waves/f157-shor-2640-even-tail-self-contained/review-v1.md), SHA-256 `7057378fd5966826702890ffa6ac611f80408199d7f5ad23de4b532516871f65`. The [manifest](../review-waves/f157-shor-2640-even-tail-self-contained/manifest-v1.json) is `e877bec84b923e71a870b720b4eb414ac9d59395e4e1f8db176fd569a895d77c`. The review reports 0 FATAL / 0 MAJOR / 0 MINOR and says it read and statically audited all 28 pinned dependencies; those author programs were not executed.

The independently authored exact run's [receipt](../review-waves/f157-shor-2640-even-tail-self-contained/reviewer-independent-exact-v1-receipt.json), SHA-256 `40c3ea559cbd1c950f5360354fdc2263614ada76e5026ad2382bc17b50217027`, reports `all_assertions_passed=true`, no UNKNOWN, no author-code execution and the twelve branches, including the 146 P12 residuals. A separate [oracle and cover receipt](../review-waves/f157-shor-2640-even-tail-self-contained/reviewer-oracle-and-certificate-v1-receipt.json), SHA-256 `15cbc9dd82c0abb1da331cf8b1e9b7b284daf60b46db38d578fdb667a98737c1`, records 606 bounded powerset-oracle comparisons with zero disagreements and verification of the 266-clique partition; it does not prove general search correctness. The reviewer explicitly retained the earlier author P40 failure and P20 timeout as failure/UNKNOWN, not exclusions. Exact control claims are those of the receipted independent reviewer run; no parent replay is claimed.

The Q55-dependent f128 consequence remains outside this disposition. No prior held outcome, odd-tail theorem, unreviewed order floor, or all-order conclusion is imported.
