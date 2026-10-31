# Derivatives and first-order stability preservers keep SPR ratios

**Status: WRITTEN theorem with WRITTEN-checked-in-kernel finite examples; author candidate, not parent adoption.** The theorem supplies additional necessary inequalities for any common septic numerator and a sound mixed-operator certificate format. The bounded search reported below found no negative certificate. No unrestricted synthesis verdict or novelty claim is made.

## Preservation theorem

Let \(a,b\) be real polynomials of the same positive degree \(n\), with \(a\) Hurwitz and
\[
\operatorname{Re}[b(i\omega)/a(i\omega)]>0\quad(\omega\in\mathbb R).
\]
Then \(b\) is Hurwitz with positive leading coefficient. Both operations
\[
D:f\mapsto f',\qquad T_h:f\mapsto f+h f'\quad(h\ge0)
\]
preserve the SPR ratio when applied to numerator and denominator together. In particular, for every \(0\le k<n\) and \(h\ge0\),
\[
\frac{b^{(k)}+h b^{(k+1)}}{a^{(k)}+h a^{(k+1)}}
\]
is SPR of equal degree \(n-k\). The operation may be iterated or composed with other \(D,T_h\) operations while the degree remains positive.

**Proof.** The leading coefficient ratio of \(b/a\) is positive, since the real part is strictly positive at all sufficiently large imaginary frequencies. The real part of \(b/a\) is harmonic on the right half-plane, positive on its imaginary boundary, and tends to that positive leading ratio uniformly at infinity. The minimum principle on increasing half-disks gives \(\operatorname{Re}(b/a)>0\) throughout the closed right half-plane. Hence \(b\) has no zero there and is Hurwitz.

For every real \(\lambda\), the complex polynomial \(f_\lambda=a+i\lambda b\) has no zero in the closed right half-plane: otherwise \(b/a=i/\lambda\) there. Its leading coefficient is nonzero for every real \(\lambda\), so it has exact degree \(n\) and all roots in the open left half-plane.

If a complex polynomial \(f\) has all roots \(r_j\) in the open left half-plane, then for every \(\operatorname{Re}s\ge0\),
\[
\operatorname{Re}\frac{f'(s)}{f(s)}=
\sum_j\operatorname{Re}\frac1{s-r_j}>0.
\]
Thus \(f'\) and \(f+h f'\) are zero-free on the closed right half-plane for every \(h\ge0\) (the latter is \(f\) at \(h=0\)). Both are therefore Hurwitz. By linearity, for either operation \(T\), the complex pencil \(Ta+i\lambda Tb=T f_\lambda\) is Hurwitz for every real \(\lambda\). Also \(Ta\) and \(Tb\) are Hurwitz.

Consequently \(Tb/Ta\) is nonzero and cannot be purely imaginary anywhere on the closed right half-plane: such a value would make \(Ta+i\lambda Tb\) vanish for a suitable real \(\lambda\). The domain is connected, and the leading coefficient ratio is positive, so its real part is strictly positive there. This proves the two operations and their compositions. The argument is the complex-pencil form of Gauss–Lucas/stability preservation; no unverified converse is asserted.

## Mixed-operator certificate implication

For a monic septic interval box \(K\), every common numerator \(b\) must satisfy, for every actual \(a\in K\), \(0\le k<7\), \(h\ge0\) and \(t\ge0\), the transformed pairing inequalities for
\[
A_{k,h}=\frac{a^{(k)}+h a^{(k+1)}}{(7)_k},\qquad
B_{k,h}=\frac{b^{(k)}+h b^{(k+1)}}{(7)_k}.
\]
Here \((7)_k=7\cdot6\cdots(7-k+1)\), with \((7)_0=1\). Each transformed pairing is **linear in the original eight coefficients of \(b\)**. Therefore, conditional only on the written theorem above, an exact finite nonzero nonnegative weighted sum of original and/or transformed actual-member pairing rows whose eight coefficient sums are all nonpositive would be a genuine obstruction to the original septic synthesis problem. A common numerator would be Hurwitz, hence have positive coefficients, making its dot product with those sums nonpositive while every weighted pairing is positive. Transformed interval endpoints must not be treated as independently attainable: each row must come from an actual original member.

The converse fails: a numerator for a derivative family need not integrate to an SPR numerator for the original family, as shown by the separately replayed `frontier-20261028-derivative-integration-obstruction-v1.md`. The preservation theorem is a necessary condition, not an automatic lift.

## Exact finite evidence and bounded search

For \(a=(s+1)^7\), \(b=(s+1)^7+s\), 28 transformed pairings with \(k=0,\ldots,6\) and \(h\in\{0,1/10,1,10\}\) have complete exact Bernstein certificates. The minimum compactified bound across the 28 is \(7/30\); all transformed denominators factor as \((s+1)^{n-1}(s+1+nh)\) at their corresponding degree \(n\). Frozen example `frontier-20261028-spr-operator-hierarchy-example-frozen-v1.json` has SHA-256 `0c4c3977ab80ff30918342a16a48c5eb640bc7ec8eb35b5c3cd2e249b8a2789c`. Standalone checker `frontier-20261028-spr-operator-hierarchy-independent-kernel-v1.py` (SHA-256 `9766a4eb1e994e8ea2323f2f449150e975f9c267457931b0e35fc7e96c30fd4e`) reconstructs the transforms by a separate recursive-derivative route, all denominator factorizations and Bernstein leaves, and rejects a corrupted leaf. Receipt `frontier-20261028-spr-operator-hierarchy-independent-result-v1.json` has SHA-256 `387e4ee7c6bb435e06317c01d5ff2c3316339d5575749dca0129c47ba5b7e2b8`.

A bounded exact hybrid search on one different all-member-stable asymmetric septic box used \(k=0,\ldots,6\), \(h\in\{0,1\}\), its four actual corners and a finite rational grid. It checked 448 rows initially and 616 after adding original-pairing violations; both finite minimax margins were positive, and no full-halfline numerator or negative certificate was obtained. Separately, 3,584 first-grid unit-coefficient values were recomputed by direct polynomial convolution and matched the producer's row vectors. Search data `frontier-20261028-spr-operator-hybrid-search-results-v1.json` has SHA-256 `603a257ba3bd15ea50cc711a6bd6ff0bd1d7c7ef798c9872d282ec09898fdd68`. Finite-grid positivity does not exclude certificates at other frequencies or in other boxes.

Imports are harmonic minimum principle, elementary root/continuity facts and the stated complex stability argument; all finite calculations used exact integers and `fractions.Fraction` on one Python Eval host. This is not formal verification, cross-vendor review, novelty clearance, or a general septic verdict.
