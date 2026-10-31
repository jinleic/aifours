# One exact seed rules out Fourier transversals generically in an analytic family

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:38:12 PDT 2026**. This is a generic statement, not an all-phase theorem and not an unrestricted even-order no-go.

## Theorem

Let D be a connected open subset of R^d, and let `K(theta)` be a real-analytic family of n×n complex Hadamards on D. Suppose there is a point theta0 in D such that for EVERY source-row permutation, the ordinary cyclic Fourier-product QLS formed from `K(theta0)` has no orthogonal transversal. Then outside a closed nowhere-dense measure-zero subset of D, the same no-transversal statement holds for EVERY source-row order simultaneously. The corresponding fixed-source-order statement needs only a no-transversal seed at that order.

## Proof

There are finitely many source-row permutations pi and candidate column permutations sigma. For each pair define

`G_(pi,sigma)(theta) = sum_(r<s) |<psi_(r,sigma(r)),psi_(s,sigma(s))>|^2`,

using the Fourier-product QLS based on `pi K(theta)`. Each G is nonnegative and real analytic. It vanishes exactly when that candidate is an orthogonal transversal. The seed assumption makes every G strictly positive at theta0, hence no G is identically zero on the connected D. By the standard real-analytic zero-set theorem, each zero set has Lebesgue measure zero and empty interior; it is closed in D. The finite union of all of them is again closed, nowhere dense and measure zero. Its complement is the desired open dense, full-measure no-transversal set. No independence or algebraicity of parameters is assumed.

## Seed criterion and boundary

At `n=m p` for a prime p>m, a seed K whose entries lie in a conjugation-stable field with Phi_p irreducible satisfies the seed hypothesis by `frontier-20261028-large-prime-field-fourier-obstruction-v1.md` SHA **3348a6acd5876859722d980c20ec42433c4b7a6e91fa274fa8a4e40fe286**. In particular, a BH(2p,q) seed with p not dividing q suffices. This can be applied to affine or genuinely nonaffine analytic families; one must actually establish the Hadamard and analyticity hypotheses on the stated connected domain and locate the seed inside it. Disconnected components need their own seed.

The theorem does not characterize the exceptional set, prove it empty, or rule out an even Fourier transversal at exceptional parameters. The standard real-analytic zero-set theorem and the exact seed premise are named imports; the written caller requires independent review.
