# An odd-run full-support REF exclusion in the original lower band

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 19:10:16 PDT 2026**. An all-prime **WRITTEN sufficient-condition candidate**, with actual bounded checks below; no independent mathematical review, formal proof, novelty or global-adoption verdict.

## 1. Actual odd-run setup and theorem

Let p be ANY odd prime and let W be an actual `D_(2p)` word having exactly F=3p−2 reflections, in arbitrary positions among arbitrary rotations. In their CYCLIC reflection-only order, decompose the reflection exponents into maximal constant runs of lengths `ell_1,...,ell_r`. If all reflections have the same exponent, select any2p of them and stop. Otherwise cut the cyclic reflection order at a run boundary. Let o be the number of ODD-length runs, let `z_1,...,z_o` be their exponents in the resulting order, and let

`H=sum_j floor(ell_j/2) = (3p−2−o)/2`.

The following actual reflection-only selectors exist:

1. If `o<=p−2`, W is REF-covered.
2. If `o=p` and two odd-run exponents are equal, W is REF-covered.
3. If `o=p+2`, the odd-run exponents contain all p field values, and consecutive exponents in this odd-run list are unequal, W is REF-covered.

In particular, at the historical lower residual's odd-run boundary `o=p+2`, when **every** actual constant-reflection run has odd length (`e_F=0`), a REF-failing word must omit at least one field value from its odd-run exponents. This is a necessary residual restriction, NOT a proof that an L_RES residual exists or that the whole boundary is solved.

## 2. Lifting odd-run identities using actual even pairs

Within a constant reflection run of length ell, select any `2 floor(ell/2)` occurrences in reflection order; their product is identity as a sequence of identical reflection pairs. For an odd run, retain its one remaining occurrence as well if that odd-run representative is selected. No rotations are selected anywhere in these constructions.

If `o<=p−2`, H>=p, so select p such identity pairs: exactly2p actual reflections.

If `o=p`, then H=p−1. If two odd-run exponents agree, retain those two representatives and all H identity pairs. The selected count is `2(p−1)+2=2p`; after deleting the identity pairs in the actual selected word, the only remaining product is two equal reflections, hence identity.

If `o=p+2`, then H=p−2. If FOUR odd-run representatives in chronological run order have alternating exponent0, retain those four representatives and all H identity pairs. The selected count is `2(p−2)+4=2p`; after deleting the adjacent equal-reflection pairs from each selected run, the ordered product is exactly the chosen four-reflection product. This reduces the case to §3 without commuting or relocating nonidentity occurrences.

## 3. Four-reflection full-support lemma

**Lemma.** For p odd, any linear sequence `z_1,...,z_n` of n>=p+2 field elements, whose support is all F_p and whose neighboring values are unequal, has indices `i<j<k<l` with

`z_i−z_j+z_k−z_l=0`.  (1)

*Proof.* Suppose not. For every consecutive triple define `t_i=z_i−z_(i+1)+z_(i+2)`. Since the whole sequence contains every field value, some occurrence of t_i exists. If one occurs BEFORE the triple, those four positions give `t_i−z_i+z_(i+1)−z_(i+2)=0`. If one occurs AFTER it, the triple followed by that occurrence gives `z_i−z_(i+1)+z_(i+2)−t_i=0`. Both are forbidden. Hence t_i must occur within the triple.

It cannot equal z_i, since that would give `z_(i+2)=z_(i+1)`, nor z_(i+2), since that would give `z_i=z_(i+1)`. Thus `t_i=z_(i+1)` and

`z_(i+1)−z_i = z_(i+2)−z_(i+1)`

for every consecutive triple. All consecutive differences are therefore one common nonzero d, so `z_t=z_1+(t−1)d`. The four original positions `1,2,3,p+2` then have alternating sum

`z_1−(z_1+d)+(z_1+2d)−(z_1+(p+1)d) = −p d =0`,

contradiction. QED.

Apply the lemma to the odd-run exponent list in §1(3). If `e_F=0`, EVERY cyclic run is odd and adjacent cyclic run labels are automatically unequal by maximality, so the adjacent-unequal condition is guaranteed. If even runs intervene, adjacent odd-run exponents may coincide; this proof does NOT silently assume otherwise.

## 4. Cyclic restoration and historical trust

The cut in §1 is at an ACTUAL cyclic run boundary, not a deletion or reordering of the word. The identity selector found in the cyclic order consists of actual reflection occurrences. To express it in the original increasing full-word indices, cyclically rotate the selected list back. If a cyclic selected product UV=1, its rotation VU is also1. Thus all conclusions hold in the original order, including when a constant cyclic run straddles the original word start.

The old consolidated lower-band source records the separately retained residual floor `o_F>=p+2` with its S(p)/Lev statement-level ancestry. This paper uses no such external theorem for its own direct REF proofs. If that historical floor is indeed part of the frozen L_RES caller-failure interface, §1(3) excludes the full-support, e_F=0 portion of its first `o_F=p+2` boundary; the named historical trust is not upgraded here. Other odd-run profiles, other callers and the full L_RES bridge remain open.

## 5. Bounded work and nonclaims

Before the full-support lemma was written, `frontier-20261028-olson-odd-run-four-dfs.py`, SHA256 `7771f51759685cdf94f783e48dab756ff8cab685d74617862a8d64e7f41857ab`, reported no adjacent-distinct length-p+2 four-reflection avoider at p=11 and13. The saved p11 result SHA256 is `28639425c0c94e72facdd183415ab2bf2415ccf556590008b2ddcff383801796`, and the p13 result SHA256 is `9c227c33dcc5f967df4f15792b0c6c54885c9d00d21e0c8b01d2a9e41c5d797b`. This is an unreviewed bounded search for a STRONGER statement with no full-support hypothesis; it is NOT a proof of that stronger statement or a premise of §3.

`frontier-20261028-olson-odd-run-support-experiment.py`, SHA256 `5457f9c1a1f174bc2e5014372d2e6595f0dc97aaedb6abdf0ecb6837341de2ce`, generated `frontier-20261028-olson-odd-run-support-results.json`, SHA256 `5fe564e526a41095cab2029e6e547983065c526a66571661ab38e3ff3fd06b2b`. Separately written `frontier-20261028-olson-odd-run-support-checker.py`, SHA256 `d1a91e742751273b743aeb21c514a37bbc629aec77b81dab529c24f10f226e52`, imported no producer and returned `PASS_INDEPENDENT_ODD_RUN_SUPPORT_CHECK` in result `frontier-20261028-olson-odd-run-support-check-results.json`, SHA256 `da063654977a34018e69b3071c198bc852ed35f3d5665ca829c0cad16e379c5c`. It independently reconstructed all cyclic runs, odd-run support and actual run selection and directly multiplied 250 original-index reflection-only selectors at p=3,5,7,11,13; 231 constructions used a nonzero cyclic cut. Duplicate-index and changed-type/count mutations were rejected for their intended reasons. These are bounded fixtures, not the universal proof.

The full L_RES residual remains unproved. No SEL/IPGEN/GS/DS3 failures, arbitrary-group closure, formal/kernel, external-family or novelty conclusion is claimed. A disjoint complete written review is requested.

**END — odd-run full-support direct REF exclusion.**
