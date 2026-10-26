# CURRENT P44 CONSOLIDATION v21 — PART19/19: off the z=0 slice the Bob-0 peel is separable EXACTLY on the v=0 slab |w|^2+|z|^2<=2; this gives a new SN2 slab with arbitrary u, its involution image, and a sharp barrier whenever vz!=0

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 00:44:07 PDT 2026**. Exact WRITTEN mathematics; every step is displayed. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## G0. Scope and union

The NEW claims C37, C37′ and C38 sit on the ORIGINAL chart. The complete current union is the eighteen parts plus Part15 ADDENDUM-1 bound in `checkpoint-101-complete-current-v20-eighteen-part-manifest-v1.json` (SHA256 db0d5fce84b22d0ff53eaf16eeeaf875a6fbf855387e26bc7ce40cfae385cf5e), THIS part, and all mandatory overlays. Parts 9–19 are LATER UNREVIEWED.

C38 SUPERSEDES the determinant condition of Part15 Q7(e) by a stronger, self-contained statement. Part15 itself is not edited.

Imports:
- Part15 Q2 Lemma L;
- Part15 Q6 (every R_x is entangled);
- Part10 H5 / Part6 Y4.1 involution: for z!=0, R_x is locally equivalent to R_x' with x'=(w/z,v/z,-u/z,1/z);
- (I1) Horodecki: PPT on C^2⊗C^2 or C^2⊗C^3 implies separable.

## G1. The Bob-0 compression for general x

Let B=1-|0><0| on Bob. Bob vectors are p=|1>, q=|2>, s=|3>, and x̃=vp+wq+zs. Deleting Bob-0 components of the Part10 chart vectors gives:
- t1=|1>p+|2>q (from a), t2=|0>p+|1>q (from b), t3=-|2>p (from c);
- t4=|0>q+|3>x̃ (from d_x), t5=|3>q (from g), t7=|3>s (from e), j'=|2>s (from j);
- t6=|0>x̃ (from h_x); f=|30> is deleted entirely.

```
S(x) = P(t1)+P(t2)+P(t3) + 3[P(t4)+P(t5)+P(t7)+P(j')+P(t6)].            (G1.1)
```

These eight vectors are linearly independent whenever z!=0: t6 is the only one with a |0>s component.

## G2. Forced structure of products carrying Alice |1> (z!=0)

**Lemma G2.** Let z!=0 and suppose S(x)=Σ_i w_i P(α_i⊗β_i) with w_i>0. Every term with <1|α_i>!=0 can be normalised to <1|α>=1, and then has the form

`α = r|0> + |1> + r^{-1}|2> + v r^2|3>,   β = p + r q,   r!=0,`

with Σ w = 1 and Σ w|r|^2 = 1 over these terms.

*Proof.* The Alice-1 block of S is |p><p|+|q><q|. Hence β is in span{p,q}, and Σ w ββ^† = |p><p|+|q><q| over the terms carrying Alice |1>.

Each product vector lies in range S, so α⊗β = Σ c_k t_k uniquely. Compare components:
- **Alice-1.** |1>p occurs only in t1 and |1>q only in t2. So c1=b_p and c2=b_q.
- **β=q is impossible.** If b_p=0, then c2=1 puts |0>p into the expansion. Its only other source is t6, whose |0>s part forces c6=0 (z!=0). So |0>p survives while α⊗q has no p-component, a contradiction. Hence b_p!=0; set b_p=1 and b_q=r.
- **Alice-0.** The s-part gives c6 z=0, so c6=0 (the "zero h-coefficient"). The p-part gives α0=c2=r, and the q-part gives α0 r=c4, so c4=r^2.
- **Alice-2.** The q-part gives α2 r=c1=1, so α2=1/r; in particular r!=0. The p-part gives α2=-c3 (t3=-|2>p), and the s-part gives c_j'=0.
- **Alice-3.** The p-part gives α3=c4 v=v r^2. The q- and s-parts only fix c5 and c7.

The two weight sums are the (1p,1p) and (1q,1q) entries. ∎

## G3. Theorem C38 (sharp Bob-0 barrier off the slice)

**C38.** If z!=0 and v!=0, then S(x) is ENTANGLED. So the Bob-0 peel can never certify SN<=2 there. This is a METHOD barrier, not a statement about SN(R_x).

*Proof.* Suppose S(x) is separable. Let Π be the sum of the Alice-1 terms (Lemma G2) and Rm=S-Π. Rm is a sum of the remaining product terms, so Rm>=0 and Rm^Γ>=0.

Write E for the weighted average over the Alice-1 terms. Then Π_00=E[|r|^2ββ^†]=[[1,m],[m̄,E|r|^4]] on (p,q), with m=E[|r|^2 r̄]. Also S_00=|p><p|+3|q><q|+3|x̃><x̃|. So

`Rm_00 = 3|x̃><x̃| + D,   D = [[0,-m],[-m̄, 3-E|r|^4]] (on p,q, zero on s).`

Take k=(z̄,0,-v̄), so that <x̃|k>=v̄z̄-z̄v̄=0. Let b ⊥ x̃ be any vector with b_q!=0. For small t, <k+tb|Rm_00|k+tb> = -2Re(m z t b_q)+O(t^2). Since Rm_00>=0 and z!=0, this forces m=0. Then <q|k>=0 and <x̃|k>=0 give k in ker Rm_00, and k'=conj(k)=(z,0,-v) is in ker (Rm_00)^T.

The Alice-(0,3) block of S is S_03=3|q><x̃|, coming only from 3P(t4). For the products, α0ᾱ3=v̄|r|^2 r̄, so Π_03=v̄ E[|r|^2 r̄ ββ^†]. Its (q,p) entry is v̄E[|r|^4].

In Rm^Γ, PSD requires the row k'^†(Rm_03)^T to vanish:
- (S_03)^T=3|x̄><q|, and k'^†|x̄>=z̄v̄-v̄z̄=0;
- k'^†(Π_03)^T = z̄·(p-row of (Π_03)^T), whose q-entry is z̄ v̄ E|r|^4.

So the q-entry of k'^†(Rm_03)^T is -z̄v̄E|r|^4. This is nonzero, because E|r|^4 >= (E|r|^2)^2 = 1. That is a contradiction. ∎

**Cross-check against Part15.** At V=W=1, Part15's determinant was -13, consistent with C38. At z=0 the vector k=(0,0,-v̄) is |s>, which has no partner, so there is no contradiction; this is consistent with C36/Theorem E.

## G4. Theorem C37 (v=0 slab, exact for z!=0)

**C37.** Let x=(u,0,w,z) with u arbitrary.
- (i) If |w|^2+|z|^2<=2, then S(x) is separable and SN(R_x)=2. This includes z=0.
- (ii) If z!=0 and |w|^2+|z|^2>2, then S(x) is entangled. This is a method barrier only.

*Proof of (i).* By a local phase choice on Alice{0,3}⊗Bob{q,s}, take w,z>=0: the phase of |3> absorbs arg w, and the relative Bob phase of s absorbs arg w-arg z, while every term P(·) is unchanged. For r^4=1 put

`π_r = (r|0> + |1> + r^{-1}|2>) ⊗ (p + r q).`

By powers of r:
- r^{-1}: |2>p;
- r^0: |1>p+|2>q;
- r^1: |0>p+|1>q;
- r^2: |0>q.

Since (1/4)Σ r^m=0 for m=1,2,3,

`(1/4)Σ_r P(π_r) = P(t3)+P(t1)+P(t2)+P(|0>q).`

Hence S = that average + 3P(j') + Rm, with

`Rm = 3P(t6)+3P(t4)+3P(t5)+3P(t7) - P(|0>q),   |0>q = t4 - w t5 - z t7.`

**Positivity.** In the basis (t6,t4,t5,t7), Rm has coefficient matrix 3I-uu^†, u=(0,1,-w,-z). Its eigenvalues are 3,3,3 and 3-(1+w^2+z^2), so Rm>=0 iff w^2+z^2<=2.

**PPT.** Rm lives on Alice{0,3}⊗Bob{q,s}. In the order (0q,0s,3q,3s) its entries are:
- (0q,0q)=3w^2+3-1=3w^2+2, (0q,0s)=3wz, (0s,0s)=3z^2;
- (0q,3q)=3w, (0q,3s)=3z, (0s,3q)=0, (0s,3s)=0;
- (3q,3q)=3w^2+3, (3q,3s)=3wz, (3s,3s)=3z^2+3.

The partial transpose moves (0q,3s)=3z to (0s,3q):

```
          [ 3w^2+2  3wz   3w      0      ]
Rm^Γ =    [ 3wz     3z^2  3z      0      ]
          [ 3w      3z    3w^2+3  3wz    ]
          [ 0       0     3wz     3z^2+3 ]
```

For w,z>0 the leading minors are:
- m1=3w^2+2;
- m2=(3w^2+2)3z^2-9w^2z^2=6z^2;
- m3=6z^2·(3w^2+3-3)=18w^2z^2. This uses the Schur value b^T M^{-1} b = [27w^2z^2-54w^2z^2+27w^2z^2+18z^2]/(6z^2) = 3, with b=(3w,3z);
- m4=m3·3=54w^2z^2. Here the last Schur complement is 3z^2+3-(3wz)^2·(M3^{-1})_{33}, and (M3^{-1})_{33}=6z^2/(18w^2z^2)=1/(3w^2), which gives exactly 3.

All four are positive, so Rm^Γ>0.

Boundary cases:
- w=0, z>0: the (0s,3q) block [[3z^2,3z],[3z,3]] has determinant 0, and the rest is diag(2,3z^2+3). PSD.
- z=0: the |0>s row and column of Rm^Γ vanish, the entry (3s,3s)=3 is decoupled, and the rest [[3w^2+2,3w],[3w,3w^2+3]] has determinant (3w^2+2)(3w^2+3)-9w^2=9w^4+6w^2+6>0. PSD.

By (I1) Rm is separable. Lemma L and Q6 then give SN=2.

*Proof of (ii).* By Lemma G2 with v=0, the Alice-1 terms are (r|0>+|1>+r^{-1}|2>)⊗(p+rq) with E|r|^2=1. The proof of C38 again forces m=0; that step uses only z!=0.

Compress Rm to Alice{0,3} by the local projector onto Alice span{|0>,|3>}; this preserves PSD. The compression of S is P(|0>p)+3P(t4)+3P(t5)+3P(t7)+3P(t6). The Alice-1 terms contribute only Π_00=|p><p|+E|r|^4|q><q| there, because m=0 and α3=0. So the compressed Rm equals 3P(t6)+3P(t4)+3P(t5)+3P(t7)-E[|r|^4]P(|0>q) exactly.

With A=3(P(t6)+P(t4)+P(t5)+P(t7)), we have <0q|A^{-1}|0q>=(1+w^2+z^2)/3 in the coefficient basis. So the compression is >=0 iff E|r|^4(1+w^2+z^2)<=3. Since E|r|^4>=(E|r|^2)^2=1, this needs w^2+z^2<=2. ∎

**Note on C36.** At v=0, Part18's E2 note already showed that the residual is PPT for every w. C37(i) with z=0 confirms the larger range |w|^2<=2 on the v=0 line, while C36 as stated claims only |w|^2<=5/6 there. C36 is not edited.

## G5. Corollary C37′ (involution image)

Let x'=(u',0,w',z') with z'!=0 and 2|z'|^2 >= 1+|u'|^2, with w' arbitrary. Then SN(R_x')=2.

*Proof.* The source x=(-w'/z', 0, u'/z', 1/z') has v=0 and z=1/z'!=0. It satisfies |w|^2+|z|^2 = (|u'|^2+1)/|z'|^2 <= 2, so C37 applies, and the involution preserves SN. ∎

## G6. Examples and remaining gaps

**New examples.**
- (2,0,1,1) satisfies C37: w^2+z^2=2. It lies outside the Part6 ball (6>2) and outside Theorem C (m_L=√2-2<1).
- (0,0,5,1) and (1,0,3,1) satisfy C37′: 2>=1 and 2>=2.

**Uncovered by the current union**, for example (2,0,2,1):
- C37: 5>2;
- C37′: 2<5;
- Theorem C: m_L<1;
- H5.1: 2/√2-4<1.

**Barrier map of coordinate peels at vz!=0.** Bob-0 is now dead everywhere (C38). Alice-2/Bob-2 and Alice-0 die there by Part15 Q7(b,c), and Alice-3/Bob-3 die always. Alice-1/Bob-1 are possible only when |z|>=1/(6√(1+|w|^2)) (Q7(a)). Non-coordinate peels (general φ) remain unexplored apart from Q7(f).

**Original physics-3/P44 remains UNMET.** These are author-WRITTEN candidates pending fresh reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v21 PART19/19.**
