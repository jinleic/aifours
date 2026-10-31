# Fourier-product no-transversal for every root order not divisible by 3

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 20:51:57 PDT 2026**. This additive successor removes the 7∤q restriction from `frontier-20261028-even-no3-no7-product-no-transversal-v1.md` SHA **8a901af9c6aeb993a663b7d3d597ccce80542b06e391456100795fb89b9d03e7**. The only additional named import is the equality case of the same Lam–Leung source, **Uniqueness Theorem 6.5**. No prior bytes are changed.

## 1. Claim

For EVERY positive q with 3∤q and EVERY `K∈BH(10,q)`, the Fourier-product QLS10 has **NO orthogonal transversal**, even with repeated rays, arbitrary root gauges and permutations. As in the predecessor, the even-q part is conditional on [Lam–Leung Cor.3.4, Thms.4.8 and 6.5](https://arxiv.org/pdf/math/9511209v1), the standard `roots(Q(zeta10))=mu10` fact, and the universal q10 no-T candidate SHA **a2814fa152a3e0c2e41993a172a1f4320378667be08a202b0dd8a39ed5dd721f** (itself importing the published 51-class classification). Odd q was already covered by `frontier-20261028-all-odd-fourier-product-no-transversal-v1.md` SHA **d9422ffac608ddd9b128e979dc105b20c6ca94ad06f4a63af4e086a42e6e9490**.

Combining the two all-q filters: a still-unexcluded Butson root order MUST be divisible by **6**. Orders6 and12 are separately excluded by their catalog-conditional no-T certificates; 18 is the smallest remaining root order. In particular q=70, previously open in the even no3/no7 packet, is now excluded. Nothing here proves an unrestricted original QLS10 no-go.

## 2. The only new ten-term exceptional sum

For 3∤q, the five-root rule remains unchanged: a zero sum of five q-roots is a regular5-gon and 5|q. Assume q even and 5|q; write `G=mu_q/mu5`. If 7∤q the predecessor applies directly. If 7|q, the three smallest prime factors are2,5,7 and the Lam–Leung asymmetric minimal weight bound is exactly10. A ten-term zero sum is therefore either a sum of symmetric prime polygons, hence `5+5` or five 2-gons, OR is an asymmetric MINIMAL sum of weight10. The latter is unique up to rotation by Theorem6.5, and its explicit form is

`gamma * ( -zeta5 - zeta5^2 - zeta5^3 - zeta5^4 + zeta7 + zeta7^2 + ... + zeta7^6 )`.

This is a positive sum of q-th roots: minus signs are the q-th root −1. In G its first four terms share the coset −gamma, and its last six terms are six DISTINCT cosets gamma*zeta7^j, none equal to −gamma. Its multiplicity pattern is therefore

```text
4,1,1,1,1,1,1  (seven distinct quotient values).
```

The order7 subgroup injects into G and has odd order, so the asserted distinctness and noncollision with −1 are exact. Additional prime factors or powers in q do not alter the equality-classification conclusion: Theorem6.5 uses the three smallest prime divisors of q and allows arbitrary rotation by a q-root.

## 3. Carrying the predecessor proof through

A putative transversal still yields a five-pair perfect matching with both coordinate half sums zero. Each five-term half sum is a 5-gon, so the quotient multiplicity of any two coordinate rows in the same half is EVEN for every G value. The additional asymmetric 4+six-singletons pattern is impossible under that even-multiplicity condition. The predecessor already rules out a nonconstant 5+5 pattern by odd multiplicities and five antipodal pairs because even multiplicities would make their total divisible by4. Therefore row quotients within each half are constant in G, exactly as in its §3.

In its §4, quotient terms of two columns from DIFFERENT delta-modulo-± groups occupy exactly two distinct, non-antipodal G cosets. The asymmetric sum has seven distinct quotient values and is again impossible; five antipodal pairs are impossible too. The sum is therefore two 5-gons, one per coordinate half. The construction of a genuine B∈BH(10,10) and the SAME-transversal specialization argument are literally the predecessor's §§4–5. The q10 no-T certificate yields the contradiction.

## 4. Limitations

The equality classification is a NEW and necessary explicit source import; the predecessor's minimum-weight bound alone did not establish this extension. The result still requires independent full review of the source use, physical half matching, parity, q10 construction and specialization. It leaves even orders divisible3 and every arbitrary-phase or non-Fourier construction open.
