# A natural exterior-square lift cannot complete any Pauli60 parity core

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:54:11 PDT 2026**. This rejects one proposed 6D representation, not the general 6D complement problem.

## Proposed lift and no-go

For a 4D ONB `(u1,u2,u3,u4)`, the six normalized exterior products `u_i wedge u_j` form an ONB of `Lambda² C4`, which has dimension6. A natural attempt to complete a 4+6 parity core is to assign those six bivector rays to the six complementary 6D edges at EACH context, using the SAME exterior-square space at all 15 contexts.

This cannot work for ANY 30-ray/15-basis parity core drawn from the published [Waegell–Aravind 60 two-qubit rays](https://arxiv.org/html/1109.1299v2#S2.T1), including the explicit tripartite core in `frontier-20261029-pauli60-positive-tripartite-4d-core-v1.md` SHA **734e0ff4397534dd8e486f9375984ddb6b3bcbdc51530e57505621726571af96**.

Indeed, for a 6D complementary edge joining two contexts, the two 4D bases are ray-disjoint, and the chosen wedge ray must occur in BOTH of their six-bivector frames. Define a compatibility graph on the source's 105 exact 4D bases: connect two bases iff they are ray-disjoint and their bivector frames share at least one ray. The exact census below finds that **90 bases have compatibility degree4**, while only **15 bases have degree12**. A context in a 6-regular complementary graph needs six DISTINCT compatible neighbors, so all 15 chosen contexts would have to come from the degree12 set. But those 15 bases are pairwise ray-disjoint and together contain all60 source rays once, whereas a parity core requires each of its 30 chosen rays to appear twice. Contradiction.

Thus this is a failure of the natural 'wedge the local 4D basis' representation, not a proof that no arbitrary 6D representation of the complementary graph exists. Context-specific arbitrary 6D ONBs, or other functions of 4D bases, remain entirely open.

## Exact evidence

`frontier-20261029-pauli60-exterior-square-census-v1.py` SHA **00337e44bed4b95f0126f5bcb0c9aee5da93927b016c61d9e7acc9097ba01ddf**, result SHA **de8094add537d98073432920ac6a6ba6a55ed6b275ad20082cc797daf959e3da**, reconstructs all105 source ONBs and the six projective bivectors of each using exact Gaussian-integer wedges with rational projective normalization. Among 5460 unordered base pairs, the histogram `(shared original rays, shared wedge rays)` is `(0,0):4200`, `(0,2):270`, `(1,0):720`, `(2,2):270`. It records every compatible pair and all105 degrees.

`frontier-20261029-pauli60-exterior-square-replay-v1.py` SHA **f824764b36c215316534d8f7da23a1c2943460e1e7de747ebf3a854664e77b33**, result SHA **d80d82e1ac25f5ad9aa2cc8bd78486da9396a92ef1b82229f6d6e859f1777c57**, independently regenerates the 105 bases by neighbor intersections and detects equality of planes using the exact 2×2 Gram-determinant saturation identity rather than wedge coordinates. It matches every one of the270 compatible pairs and all105 degrees, and confirms that the 15 degree12 bases are mutually ray-disjoint.

Both calculations share the public source-ray transcription `frontier-20261029-pauli60-source-vectors-v1.json` SHA **8edccd50a66289a669b30fa5ec40b6b215147af3e9731545cc4ffe3bf8b33294**. Source transcription, Gaussian arithmetic, plane equality and global-to-local caller need independent full review. No 100-ray 1RQLS10 or universal obstruction is claimed.
