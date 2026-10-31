# Sun8 for simple groups with at most two prime divisors above seven

**Status: WRITTEN, source-conditional, UNREVIEWED.** Let S be a finite nonabelian simple group with at most two distinct prime divisors greater than 7. At the named source and written-lemma scope below, S satisfies Sun8: any eight pairwise disjoint left cosets of its subgroups have two indices with gcd at least 8. This is an actual-group family, not an integer relaxation. The proof does not use Sun7 or R8 and does not claim all-simple/all-group Sun8, an infinite family, novelty, independent review, formal verification or adoption.

## 1. Exact imports and nonblind provenance

Read the complete mandatory overlays in order before earlier affected bodies: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. A7 and GL3(2) have seven distinct index-7 subgroups; the former all-alternating no-seven-index assertion remains withdrawn.

- The written subgroup-index support lemma `frontier-20261028-small-prime-support-sun8-v1.md` SHA `619c36eb5a029e97095b94f3d845772e8f4852fae05b60e33dbee55355e59ec8` proves Sun8 when the minimum proper subgroup index is at least 8 and there are at most two prime divisors above 7. It is unreviewed and its proof is an explicit input here.
- The written small alternating result `frontier-20261028-alternating-small-written-sun8-v1.md` SHA `cb2c2ae804915798e5545cb4be9432677cac012df567f82b114967ba732b6647` treats A5,A6,A7 and depends on that same support lemma. The written Fano-plane result `frontier-20261028-gl32-sun8-geometric-v1.md` SHA `d7c18486c27d7f50d792d57c6ed493f4ceb19c4a8df0c2ff041a59e3ff1c4da0` treats GL3(2). Both are separately unreviewed, not adopted sources.
- For the classification of simple groups with subgroup index ≤7, import Gareth A. Jones, [arXiv:1209.5169v1, Theorem 1.2 at k=0 and k=1](https://arxiv.org/html/1209.5169v1). The exact cases and pinned HTML bytes are recorded in `frontier-20261028-jones-k0-source-v1.json` SHA `ce6d3b4a032bf9fe04446c87a538d09e012142ef4fbc1e29853a31c29769130a` and `frontier-20261028-jones-k1-source-v1.json` SHA `6a0056fb90eb33a5a9f7327f0db013577980ecc07a383d21a4e99bfa8f915f4a`. The source says its proof uses CFSG; that proof has not been replayed or independently verified. Elementary group, Sylow and finite-field matrix facts are also used.

The author's earlier finite checks and incidental cross-topic display are disclosed separately; no old hold is reopened and no clean-cognition, priority or historical-rehabilitation claim is made.

## 2. Reduction to indices 5, 6 and 7

If S has no proper subgroup of index below 8, the named support lemma immediately gives Sun8. Otherwise let H have index m≤7. Its core is trivial by simplicity, so the coset action embeds S into S_m; the sign map is trivial for a nonabelian simple group, hence S embeds into A_m. For m≤4 the group A_m is solvable, which is impossible. Thus m is 5, 6 or 7. The action is transitive; for prime m it is primitive. For m=6 a nontrivial block system has two or three blocks. The induced block action is nontrivial by transitivity and injective by simplicity, but S_2 and S_3 are solvable. Hence this action is primitive too.

For m=5 or 6, 5 divides |S|. Otherwise |S| divides 72=2³·3², because |S| divides |A6|=360. If 3 does not divide |S|, S is a 2-group and cannot be nonabelian simple. If 3 divides |S|, a Sylow-3 count divides 2³ and is 1 mod 3, so it is 1 or 4. A count of 1 gives a nontrivial normal Sylow subgroup; a count of 4 gives an injective conjugation action into S4, and the sign map makes its image a subgroup of the solvable A4. Both contradict nonabelian simplicity. By Cauchy's theorem, in degrees 5 and 6 the faithful action therefore contains a 5-cycle, fixing respectively zero or one point. In degree 7 the index itself shows 7 divides |S|, so Cauchy's theorem supplies a 7-cycle.

## 3. Exhausting the small-index cases

At m=5, if S contains A5 then S=A5. Otherwise Jones k=0 applies. Its affine case contains a normal C5, so is not nonabelian simple; its sporadic cases have degrees 11 or 23. The projective case requires 5=1+q+⋯+q^(d−1). The only possibility is d=2,q=4, in which PGL2(4) has order q(q²−1)=60; since S is inside A5 of order 60, S=A5 after all.

At m=6, if S contains A6 then S=A6. Otherwise Jones k=1 applies to the 5-cycle. Its affine degree q^d cannot be 6, and its sporadic degrees are 12 or 24. Its projective case has p+1=6 and hence S is PSL2(5) or PGL2(5). The latter has the proper normal subgroup PSL2(5) of index 2 and is not simple. The former is isomorphic to A5, as can be seen explicitly: in SL2(5) let

\[A=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad B=\begin{pmatrix}2&0\\0&3\end{pmatrix},\quad T=\begin{pmatrix}1&2\\1&3\end{pmatrix}.\]

Modulo the central {±I}, the images of A,B generate V4, T has order 3, and conjugation by T cycles its three nonidentity elements. They generate a subgroup of order 12 in PSL2(5), whose order is 5(25−1)/2=60. A simple group of order 60 with a subgroup of index 5 embeds in A5 via its coset action, and hence equals A5. Direct matrix multiplication gives A²=B²=−I, BA=−AB, T³=I, TA=−BT and TB=−(AB)T; no external exceptional isomorphism is needed.

At m=7, if S contains A7 then S=A7. Otherwise Jones k=0 applies to the 7-cycle. The affine and sporadic cases are excluded as above. The projective degree equation 7=1+q+⋯+q^(d−1) has only d=3,q=2: d=2 would give q=6, not a prime power, and d≥4 gives at least 15. The field has no nontrivial automorphism and its scalar center is trivial, so S=GL3(2).

Therefore every nonabelian simple group with a proper subgroup index ≤7 is one of A5, A6, A7 or GL3(2), at the exact Jones-source scope named above.

## 4. Sun8 and the remaining boundary

The three alternating exceptions satisfy the named small-degree written Sun8 candidate; GL3(2) satisfies the separately named Fano-plane written candidate. All other groups in the theorem have minimum proper subgroup index at least 8, so the support lemma applies. This establishes the stated **conditional candidate** for all nonabelian simple S having at most two primes above 7 in its order. Groups with three or more such primes remain outside this result even if |S|/7 has few distinct prime factors; the separate direct-P7 prime-support theorem has a different scope and optional Sun7 assumption.

A disjoint reviewer should attack the support lemma and both exception proofs independently, the Sylow-3 exclusion for order dividing 72, primitivity at degree 6, every named Jones case and the explicit PSL2(5) matrices. The source proof, public priority and all-simple/global Sun8 remain unreplayed/open. No historical process finding or source is changed.
