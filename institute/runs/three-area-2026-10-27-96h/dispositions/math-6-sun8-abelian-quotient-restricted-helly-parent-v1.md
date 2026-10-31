# Sun8: restricted Helly for actual bad-family images in an abelian quotient

**Disposition: same-harness written support for the corrected f260 composite.** For every group G, normal N, abelian Q=G/N and positive integers r,s, suppose Q has no subgroup of index three or four. Then

**B₇(N)≤r and B₇(Q)≤s imply B₇(G)≤R(r+1,s+1)−1.**

B₇(X)≤r means every r+1 pairwise-disjoint actual LEFT cosets of finite-index subgroups contain two subgroup indices with gcd≥8. No splitting, finite-G or normality-of-the-original-subgroups assumption is made. In particular, if both factor bounds are two and Q is abelian, Q cannot have an index-three or index-four subgroup, so B₇(G)≤5 and Sun8(G) follows. These factor bounds are stronger than the original factor Sun8 bounds B₇≤7.

Native clock before composing: **2026-10-29T16:02:28-0700 PDT**.

## Parent reconstruction

Let n_i=a_ib_i with a_i=[Q:π(U_i)] and b_i=[N:N∩U_i]. For any pair, gcd(a_i,a_j)gcd(b_i,b_j) divides gcd(n_i,n_j), but need not equal it. When projected cosets overlap, their intersections with one actual quotient fiber right-translate to disjoint LEFT cosets of conjugated N-subgroups; their indices b_i,b_j cannot be coprime. Thus in a bad original family, gcd(a_i,a_j)≤3 on every quotient-overlap edge.

For a finite overlap clique take H=∩π(U_i). Abelianity makes H normal, and F=Q/H is a finite abelian quotient preserving these cosets, indices and all intersections. The no-index-three/four hypothesis forces the 3-primary part to vanish and the 2-primary part to have order at most two. Split F and its subgroups/cosets into these coprime primary components. Pairwise intersection gives a common point for all of the at-most-two-point component constraints. The odd-component indices are pairwise coprime: their gcd divides a number at most three and cannot contain two or three. The finite intersection-index/product bijection gives a common odd-component point. Therefore every quotient clique arising from this actual bad family has a common fiber, even though Q need not be globally Helly.

A clique of r+1 contradicts B₇(N)≤r in that fiber; an independent set of s+1 contradicts B₇(Q)≤s. Finite Ramsey gives the stated bound. At r=s=2, R(3,3)=6; selecting six of any eight original labels gives **two indices whose gcd is at least eight**, not merely two indices each at least eight.

## Example and limits

For every prime p>7, N=C2, Q=C2×F_p², G=N×Q meet the theorem with both factor bounds two and have the source's stated 4≤B₇(G)≤5. Q is not globally 3-Helly (three index-p affine-line cosets), repetitions of its index-two subgroup defeat every finite J₇ bound, and μ(G)=2. These are comparisons only with the exact supplied f151/f242/f243 interfaces. The reviewer's stronger example equality B₇(G)=4 is a separate derived observation, not automatically adopted by this disposition.

Arbitrary quotients need not be abelian or lack index-three/four subgroups; original factor Sun8 gives only B₇≤7. **Unrestricted Sun8, the general normal-extension implication, priority and novelty remain unestablished.** The construction makes no eight-coset counterexample.

## Evidence and chronology

- Manifest: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f260-sun8-abelian-restricted-helly-corrected/manifest-v1.json, SHA-256 **4f224e0a23ce3acf5548af1e7d55028a55190151a0e8ea6deed0188e2df537e0**. All nine live SHA/byte/LF input bindings matched during this disposition.
- Mandatory gcd erratum: /Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261029-f253-review-b-gcd-additive-erratum-v1.json, SHA-256 **c0e21498f56ebe292ef8745a2d8457f6dcf508ecb567cd0de6f0b7a9bf5540f3**, 25 LF; read after the three alternating overlays and f243 CRT correction and before the full candidate integration.
- Candidate: same directory/frontier-20261029-abelian-quotient-restricted-helly-v1.txt, SHA-256 **e7314d8fdc0db90ecb2a9339aff42d4529194fb683dddb41ce63a9ece791ad97**, 190 LF. Parent read the entire base under the correction; earlier previewed source lines predated the new erratum and are not backdated.
- Review: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f260-sun8-abelian-restricted-helly-corrected/review-v1.md, SHA-256 **e3781f19ff0dfd5757c4c16631247cd0a7584e3ef9e9fc7a2727a7ac643bc1ef**, 89 LF, **0F/0M/0m remaining** in the corrected composite; the unchanged original's wording MINOR remains historically recorded. Parent displayed all review lines. The reviewer read all nine inputs in order, did not inherit f253 findings, and leaves provenance assertions INCONCLUSIVE.
- Reviewer-owned bounded synthetic controls exited zero; receipt SHA-256 **861cda709c7b6ec22fb8e8f68aa8111a9cf19d615c3f9ec8c49ba56c386c8c5d**. They exercise nonnormal fibers, gcd divisibility, actual restricted-Helly triples, missing-index hypotheses and examples. These are reviewer executions, not a new parent replay or a universal computational proof. Parent verification is the written reconstruction above.
- Imports are elementary finite-index coset arithmetic, finite abelian primary decomposition, Bézout, finite Ramsey and the explicitly scoped comparison statements. No held/f161/f162 or selected prime-2/3 payload is a premise. Same-harness, not human, independent-model-family, formal/kernel, source-equivalence or novelty verification.
