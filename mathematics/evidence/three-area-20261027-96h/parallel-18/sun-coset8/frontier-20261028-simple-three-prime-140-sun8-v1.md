# Sun8 for the three-large-prime simple family above index 140

**Status: WRITTEN, UNREVIEWED.** Let S be a finite nonabelian simple group with exactly three distinct prime divisors greater than 7. At the named written support/saturation scope below, if its minimum proper subgroup index exceeds 140 then S satisfies Sun8. In particular this holds if its largest prime divisor exceeds 140. More precisely, any putative Sun8 counterexample in this three-large-prime class must have a proper subgroup of index at most 140 and hence embeds in A_140; in particular its order divides 140!/2. This gives a finite-order-bound reduction, not an enumeration, an all-simple/global theorem, a source-proof acceptance or a novelty claim.

## 1. Inputs and saturation interface

Read in order the complete pre-source overlays `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. No earlier source or historical hold is modified.

The named **unreviewed written** inputs are the source-free support proof `frontier-20261028-small-prime-support-sun8-v1.md` SHA `619c36eb5a029e97095b94f3d845772e8f4852fae05b60e33dbee55355e59ec8`, equivalently its self-contained consolidation `frontier-20261028-source-free-support-consolidated-v1.md` SHA `eefaac6481bd7d5d40945f44863ce474fcfb2aaf5c8c6031a3494aa84ecd7f37`, and the equality analysis in `frontier-20261028-simple-three-large-primes-frontier-v1.md` SHA `1d78631af7f11cb0393af6850c760a7b6a7b43a8fc26770595066951561e4c55`. No Sun7/R8, Jones, Jordan, CFSG, maximal-subgroup theorem or published Sun3 statement is used in the proof. The author’s earlier type checks and incidental cross-topic display are disclosed separately; no novelty or clean-cognition claim is made.

Suppose eight actual disjoint cosets violate Sun8, and let p<q<r be the three prime divisors of |S| above 7. Since r≥17 and every proper coset action of S is faithful, every proper subgroup index is at least r. In particular index 12 is impossible. The named equality analysis then gives five core indices

\[3\,2^a,\quad 2\,3^b,\quad 6p^{e_p},\quad6q^{e_q},\quad6r^{e_r},\qquad a\ge3,\ b\ge2,\ e_p,e_q,e_r\ge1,\]

and three further indices whose prime supports among {2,3,5,7} are exactly one of

\[(25,27,357),\quad(25,35,237),\quad(27,37,235),\quad(35,37,257).\]

Here `25` abbreviates support {2,5}, etc.; it does **not** denote the numerical index 25. None of the three noncore indices has a prime divisor greater than 7. All eight pairwise index gcds lie in 2,…,7.

## 2. Uniform bounds on the four patterns

Every noncore index containing 2 but not 3 has 2-adic exponent at most 2: otherwise its gcd with 3·2^a is at least 8. Every noncore index containing 3 but not 2 has 3-adic exponent exactly 1: otherwise its gcd with 2·3^b is at least 9. We now bound one actual proper subgroup index in every pattern.

1. **Supports 25,27,357.** Write the three indices as 2^c5^d, 2^e7^f and 3·5^h7^i, with c,e≤2 and all exponents positive. Their respective gcds with the third index force min(d,h)=1 and min(f,i)=1. If d=1 the first index is at most 20; if f=1 the second is at most 28; otherwise h=i=1 and the third is exactly 105. Hence μ(S)≤105.
2. **Supports 25,35,237.** The first two indices have forms 2^c5^d and 3·5^f with c≤2 and min(d,f)=1. Since μ(S)≥r≥17, f=1 would give the impossible index 15. Therefore d=1 and the first index is at most 20, so μ(S)≤20.
3. **Supports 27,37,235.** The first two indices have forms 2^c7^d and 3·7^f with c≤2 and min(d,f)=1. If d=1 the first index is at most 28; if f=1 the second is 21. Thus μ(S)≤28.
4. **Supports 35,37,257.** Write them 3·5^f, 3·7^h and 2^c5^d7^i with c≤2. The gcd bound gives min(f,d)=1 and min(h,i)=1. Since index 15 is smaller than r≥17, f≥2 and d=1. If h=1 the second index is 21; otherwise i=1 and the third is at most 4·5·7=140. Thus μ(S)≤140.

Every case yields μ(S)≤140, contradicting the displayed minimum-index hypothesis. Since the faithful coset action of a nonabelian simple group has trivial sign, an index m≤140 gives S≤A_m≤A_140 and |S| divides 140!/2. The largest prime divisor r also satisfies r≤m≤140. Neither a list of the remaining simple groups nor an upper bound on their count is computed here.

## 3. Illustration and exact limitations

As an illustration, the classical PSL2 simplicity/order statements imply that PSL2(419) is simple of order 36,779,820=2²·3·5·7·11·19·419. Thus it has exactly three primes above 7 and largest prime 419>140; the theorem applies even though all of 2,3,5,7 divide its order. Those classical facts are additional named unreplayed imports **for this example only**; the displayed factorization and primality of 419 were checked in the author's eval kernel. Other existing PSL2 or simple-family routes may already cover it; no novelty claim is made.

A disjoint reviewer should independently reconstruct the unreviewed saturation lemma, verify each valuation and gcd implication in all four cases, the index-12 exclusion and the sign/embedding conclusion. The theorem is a written candidate only; it does not review the support lemma, solve the remaining index≤140 branch, infer an infinite family or change any historical process status.
