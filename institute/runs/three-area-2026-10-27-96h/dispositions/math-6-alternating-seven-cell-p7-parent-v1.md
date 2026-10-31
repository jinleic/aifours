# Alternating groups: seven-cell exclusion of exact-gcd-7 seven-patterns through t=35

**Disposition: ACCEPT, conditional on one named external classification.** Native clock observed before composing: **2026-10-28T20:10:39-0700 PDT**. Same-harness written mathematics; no human, independent-model-family, formal/kernel or novelty certification. This is a direct P7 statement for an explicit family, not unrestricted Sun8, not all alternating degrees, and not a replay of the imported source proof.

## Adopted statement

Let r be a prime that is not of the form `(q^d−1)/(q−1)` with q a prime power and d≥2, let `1≤t≤35`, and assume `r≥max(419,7·t!)` (equivalently `r+1>7t!`). Then `A_(r+t)` has no seven proper subgroups whose indices have pairwise gcd exactly 7. For each fixed t the set of admissible primes r is infinite with relative density one among primes, by an elementary Chebyshev-type count that imports no prime number theorem.

Conditional import: Theorem 2(i)(d) of arXiv:2307.13976v2 (Baumeister–Burness–Guralnick–Tong-Viet), whose statement was matched directly: for such r the Sylow r-subgroup of `A_r` has unique maximal overgroup `AGL₁(r)∩A_r`, of index `(r−2)!`. Its proof is CFSG-dependent and was not replayed.

## Reconstructed argument

An r-free index forces an r-cycle inside the subgroup. Transitive stages descend through point stabilizers without changing the index. At an intransitive stage with complement size u, the exact quotient `[A_(r+j):H]=C(r+j,u)[A_U:P]c` holds with `c=(2/h)|A_V|/|L|` an integer dividing `u!` (c=1 when u=1), and P is transitive on U because it has at most two equal-size orbits and contains an r-cycle. Iterating gives either an exact product of binomial window factors times divisors of factorials, with disjoint decreasing windows, or a terminal proper subgroup of `A_r`, which by the import puts `(r−2)!` into the index.

No seven-pattern index is divisible by `(r−2)!`: the other six cofactors would be pairwise coprime squarefree products of at most ten possible large primes, forcing an index `7p` with `r<p≤r+t`, which no actual proper subgroup realizes. Without a seven-cell `h` (7 | r+h) every window has length at most 6 and the whole index is 7-free; so every r-free label consumes a seven-cell, and two labels cannot share a cell because `(r+h)/gcd(r+h,t!)≥(r+1)/t!>7` would divide their gcd. At least six labels are r-free but at most five seven-cells exist among 35 consecutive positions.

## Evidence

- Candidates: [factorial terminal through 33](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-factorial-terminal-33-v1.md) `363205fefd1b34bde523523e87f9c981a0a45409f006c53391a46c4e29384186`; [exact quotient and seven cells](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-seven-cell-p7-v1.md) `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f`; [extension to 35](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-thirty-five-p7-v1.md) `1a045426cd7715c63b795e57af6d0cd32dc65bf1fb7dd196e735cb4e444c4a5e`; parent read all three completely, plus the density section of the orbit ancestor.
- [Frozen manifest with mandatory f81 pre-source correction](../review-waves/f116-sun-alternating-seven-cells-35/manifest-v1.json): `45d6a1dd19ea3d528c71401327f6724e83524cbb43e902633a6a8fbb50e42818`.
- [Proof review, 112 LF](../review-waves/f116-sun-alternating-seven-cells-35/proof-review-v1.md): `83887c459c82b0fb6371bf779ba8a9b915d10089e526bc8e2509e04b8506b80e`; 0 FATAL / 0 MAJOR / 3 MINOR, all steps re-derived, 207 actual subgroups of `A₈/A₉` confirming the exact quotient with `c∈{1,2,3,6,12}`, 2,182 primes checked for cells and prime counts, four negative mutations detected.
- [Arithmetic review](../review-waves/f116-sun-alternating-seven-cells-35/arithmetic-review-v1.md): `5c403089cd7c2f5bf853ebb5289e20abb3492b32db803bdc8b512b94701481ce`; 0 FATAL / 0 MAJOR / 1 MINOR with 54,390 windows and 516,705 cell-divisibility checks.
- Author pre-source overlay `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` (`6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`) records both repaired inequalities; the frozen originals are unchanged.

## Boundaries

The MINORs are adopted as qualifications: the extension's `(r+h)/gcd(r+h,t!)>(r+1)/t!` must read `≥`; the sample primes 419/421/431 satisfy the threshold only for t≤4, so author runs at larger t are lemma controls, not theorem instances; the P-transitivity step uses `[π_U(H):P]≤2`. No statement is made for t≥36, for pairwise gcd ≤7, for repunit-form primes, or for the later Jordan/Dusart families, which are separate unreviewed candidates.
