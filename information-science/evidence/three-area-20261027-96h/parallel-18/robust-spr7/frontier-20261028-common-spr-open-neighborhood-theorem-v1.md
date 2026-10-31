# A common SPR numerator persists on an explicit coefficient neighborhood

**Status: WRITTEN theorem with WRITTEN-checked-in-kernel full-width septic examples; author candidate, not a parent adoption.** The theorem extends the fixed-parity result to open neighborhoods whose coefficient widths need not vanish. It does not say every stable interval box lies in one of those neighborhoods.

## Perturbation theorem, any degree

Let \(\mathcal A\) be a compact set of real monic Hurwitz polynomials of degree \(n\), and let \(b(s)=\sum_{k=0}^n b_ks^k\) be one real exact-degree-\(n\) numerator with \(\operatorname{Re}[b(i\omega)/p(i\omega)]>0\) for every \(p\in\mathcal A\) and every real \(\omega\). Set
\[
B=\sum_{k=0}^n|b_k|,\qquad
\delta=\min_{p\in\mathcal A,\;0\le x\le1}
\frac{P_{p,b}(x/(1-x))}{(1+x/(1-x))^n},
\]
with the value at \(x=1\) defined by its limit \(b_n\). Here \(P_{p,b}(t)=\operatorname{Re}[b(i\sqrt t)p(-i\sqrt t)]\). Then \(\delta>0\).

For any real lower-coefficient perturbation \(\Delta p(s)=\sum_{j=0}^{n-1}d_js^j\) with \(B\sum_j|d_j|<\delta\), the perturbed monic polynomial \(p+\Delta p\) is Hurwitz and the **same** \(b\) is SPR relative to it. The statement is uniform for all \(p\in\mathcal A\).

To see this, for \(t\ge0\),
\[
|P_{p+\Delta p,b}(t)-P_{p,b}(t)|
\le \sum_{j,k}|d_jb_k|\,t^{(j+k)/2}
\le B\Bigl(\sum_j|d_j|\Bigr)(1+t)^n.
\]
The last inequality uses \((j+k)/2\le n\). Hence the normalized pairing stays strictly positive, and the same bound holds throughout the straight-line homotopy \(p+\theta\Delta p\), \(0\le\theta\le1\). No member of that homotopy can have an imaginary-axis root, since such a root would make its pairing zero. Monicity prevents a root escaping through infinity on the bounded homotopy. Starting at the Hurwitz polynomial \(p\), the right-half-plane root count remains zero. The numerator remains of exact degree \(n\).

The positive minimum exists because the compactified pairing is continuous on a compact set, is positive at every finite frequency, and has positive limit \(b_n\) at infinity; exact degree and strict real-part positivity force \(b_n>0\). In particular, every compact stable fixed-parity odd-degree family from the preceding theorem has a nonzero full-coefficient neighborhood with a common numerator. This is an existence statement with an explicit admissible bound in terms of its actual \(\delta\) and \(B\), not a universal radius.

## Two fully nondegenerate septic boxes

For each fixed-parity septic example in `frontier-20261028-fixed-parity-arbitrary-odd-degree-theorem-v1.md`, expand every formerly fixed coefficient interval symmetrically by \(r=1/100000000\), leaving its other intervals unchanged. Thus **all seven independent coefficient widths are strictly positive**. The displayed numerator from the source example works on the entire expanded box. Its all-member Hurwitz stability follows from the theorem above, without assuming a four-corner converse.

| Original fixed parity | \(B\) | Original normalized margin \(\delta\) | Bound \(d r B\), with \(d\) expanded coefficients | Positive expanded margin \(\delta-d r B\) |
|---|---|---|---|---|
| odd, \(d=3\) | \(5973/40\) | \(162214533/481036337152\) | \(17919/4000000000\) | \(312616426696569/939524096000000000\) |
| even, \(d=4\) | \(964695671/17100000\) | \(1/100000\) | \(964695671/427500000000000\) | \(3310304329/427500000000000\) |

For the expanded boxes the corresponding strictly positive ratio lower bounds are, respectively,
\[
\frac{714157572893310478828125}{75646796954842075508865428881408},\qquad
\frac{15723945562750}{74305308131075260003249}.
\]
The estimates use \(|p(i\sqrt t)|\le S(1+t)^{7/2}\), with \(S=1+\sum_{j=0}^6u_j\) for the expanded box. Their exact endpoints and the source numerators are frozen below.

## Independent replay and scope

- Frozen source parity examples: `frontier-20261028-fixed-parity-septic-examples-frozen-v1.json`, SHA-256 `bd032a29ef541d3e628209814ba8a8bdd79ec2a786d7b15c076d64e57319736b`.
- Frozen full-width endpoints, perturbation margins, direct four-corner pairing leaves and ratio bounds: `frontier-20261028-fixed-parity-full-width-frozen-v1.json`, SHA-256 `2a9cb307380db02fb28a343acaa5574592fd414ddf381049b44924acd534e7d5`.
- Standalone independently written replay `frontier-20261028-fixed-parity-full-width-independent-kernel-v1.py`, SHA-256 `783668ab9539d20b4f50ebf32cbd8815ce2442dbd72ea92773a5a93d12187cd3`, checks exact box expansion, all seven strict widths, both perturbation inequalities and ratios, 56 rational corner Hurwitz minors, and all direct corner Bernstein leaves. It rejects a zero-margin perturbation control. Receipt `frontier-20261028-fixed-parity-full-width-independent-result-v1.json`, SHA-256 `e67a964b317429b8205de298db9bbeea48129f7fe060978ece80e18c07750172`.

The perturbation and all-member stability conclusions are written arguments; the indicated finite rational identities and Bernstein coefficients were replayed on one Python Eval host. This is not formal verification, cross-vendor review, novelty clearance, or the original unrestricted septic verdict.
