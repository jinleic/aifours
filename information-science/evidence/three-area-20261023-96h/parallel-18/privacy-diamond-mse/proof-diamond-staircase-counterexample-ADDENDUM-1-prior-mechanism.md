# Mandatory source addendum: prior mechanism, comparison-only candidate

Observed source-authentication clock: **2026-10-23T14:58:10-0700** (`/bin/date`). This is an operative source/claim-boundary addendum to [proof-diamond-staircase-counterexample-v1.md](proof-diamond-staircase-counterexample-v1.md), SHA-256 `d2f7771852c05edb32905b2d99c42a0403faecb42c08a16a90e8df1662d8c148`. The immutable original is not edited. Its mathematical inequalities remain CANDIDATE pending actual independent and parent reconstruction. No program or formal verification was performed.

## 1. Authenticated primary antecedent

Jordi Soria-Comas and Josep Domingo-Ferrer, **Optimal data-independent noise for differential privacy**, *Information Sciences* 250 (2013), 200–214, DOI [10.1016/j.ins.2013.07.004](https://doi.org/10.1016/j.ins.2013.07.004).

The publisher-facing page was inaccessible, the old author PDF route failed, and the publisher XML route returned metadata only. A lawful accepted manuscript was then found through the actual OpenAlex location and the [UOC institutional record](https://openaccess.uoc.edu/handle/10609/152758). The record identifies an accepted version and supplies the [actual repository PDF](https://openaccess.uoc.edu/server/api/core/bitstreams/9bd7f6d0-d854-4ff6-8559-8d891001863b/content).

Preserved sources:

- [source-soria-comas-2013-UOC.pdf](source-soria-comas-2013-UOC.pdf), SHA-256 `46d83f7de654e1047cf6eb1959b56f214c7de929408592d201f06ae0490b2c5c`;
- [source-soria-comas-2013-UOC.txt](source-soria-comas-2013-UOC.txt), SHA-256 `3e625b3c6d2d47fc73accbe3f66be916658be6949e005fd8f4d6ea47da07c6a1`;
- [actual opened Theorem 13 page image](source-soria-comas-theorem-19.png): manuscript printed p.18, PDF p.19 (the institutional cover adds one page).

Actual read scope: abstract/model, Definitions 3–5, Section 5 theorem interfaces, **the whole Section 6 construction and worked multivariate comparison**, conclusions, the Appendix proof of Theorem 13, and the full reference list. The theorem image was opened to authenticate the set formulas, not inferred from text extraction alone.

## 2. Exact prior containment of the mechanism class

Section 6, printed pp.17–18, chooses a maximum-density core `S0` inside the sensitivity difference set `Sf`, with the coordinate-downward property that the rectangle between 0 and x lies in S0 whenever x does. The immediately preceding displayed construction defines successive reachability shells by adding Sf and removing earlier shells, and assigns density `M exp(-i epsilon)` on the ith shell. Theorem 13 then states the associated result.

For our parameter regime:

- choose `Sf=D={|x1|+|x2|<=1}`;
- choose `S0=rP`, `P={|xi|<=1, |x1|+|x2|<=3/2}`;
- `r=(3/4)b^(1/4)<=3/40000`, so `S0` is strictly inside D because its maximum l1 norm is `3r/2<1`;
- P, hence rP, is coordinate-downward: coordinatewise shrinking absolute values preserves all three defining inequalities;
- the cumulative reachable sets are `S0+kD`; their disjoint new shells carry exactly density `Z^-1 b^k`.

Thus **the non-homothetic core plus Minkowski-shell mechanism is a prior published construction, and our density is an instance of that construction**. No novelty claim may attach to the general mechanism, its geometric density levels, or the general reachability-shell privacy argument.

A source-notation caution is preserved rather than silently repaired: the paragraph directly above Theorem 13 defines `S_i` using subtraction through `S_(i-1)`, whereas the theorem's final bullet is printed with `S_(i+1)` on the left but a union only through `S_(i-1)` on the right. We cite the clear preceding shell construction as the mechanism antecedent, not import an unqualified corrected theorem or treat this indexing discrepancy as our research contribution. Our candidate's probability/translation proof is complete on its own and imports no theorem-level optimality claim from this source.

## 3. Why this source does not yet supply the strict comparison

The source's Definition 5 means **minimality under a probability-concentration partial order**, defined in Definitions 3/4. It does not say that every permissible core minimizes every particular expected loss, nor does it identify the global minimum of our mixed-geometry MSE functional. We do not rely on its asserted optimality proof.

The actual Section 6 example uses the rectangular sensitivity set `[-1,1] x [-10,10]` and a rectangular core, and compares its component variances/confidence regions with independent Laplace noise. It explicitly puts the form of all optimal multivariate noises outside its scope. Its full Section 6, conclusions and references contain **no comparison against the optimized full-diamond f_gamma family** for squared-Euclidean loss; the Geng–Viswanath December 2013 conjecture is not among its references. This is a bounded statement about the read paper, not a claim that all later citations are exhausted.

The January 2026 Melbourne–Diaz–Asoodeh paper itself cites Soria-Comas–Domingo-Ferrer as reference 13, and treats geometric level-set expansion in Theorem 3. Its explicit Assumption 1 is still same-norm radial cost, so the mixed comparison is outside the read optimality interface. General level-set geometry therefore has additional explicit prior treatment and is not new here either.

## 4. Operative honest delta and remaining status

The candidate is now framed only as:

> A **strict, all-gamma cost comparison**: an explicit octagonal-core instance of a known 2013 mechanism class has lower squared-Euclidean cost than every member of the conjectured-optimal homothetic-diamond staircase family, for every epsilon at least 16 log10.

If the written inequalities survive reconstruction and no earlier matched comparison is found, this refutes the literal Geng–Viswanath Section-III conjecture. It is **not a new mechanism**, not the exact unrestricted optimum, and not an accepted novelty result.

The broader citation screen remains in progress: an OpenAlex public metadata query returned 75 indexed citing works; titles/DOIs are being screened and relevant theorem interfaces opened. That metadata inventory is neither a complete worldwide citation set nor evidence that every citing manuscript has been read. Source misses, incomplete indexing and papers using different privacy/utility models cannot certify novelty.

**Status unchanged: mathematical CANDIDATE; NOVELTY_UNCLEAR.** All downstream summaries must carry the prior-mechanism qualification and the separate mathematical-review status. No external contact, execution, account change or publication occurred.
