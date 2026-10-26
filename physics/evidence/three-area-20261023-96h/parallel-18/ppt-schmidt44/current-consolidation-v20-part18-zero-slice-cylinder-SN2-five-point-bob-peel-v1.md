# CURRENT P44 CONSOLIDATION v20 — PART18/18: a whole cylinder of the z=0 slice, {|v|^2+2|w|^2<=5/3} with arbitrary u, has Schmidt number two, via a five-point Bob-0 peel

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 00:33:23 PDT 2026**. Exact WRITTEN mathematics; every entry and minor is computed by hand below. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## E0. Scope and union

NEW claim C36 extends Part15 (Theorem E0/E) on the ORIGINAL chart. The complete current union is the seventeen parts plus ADDENDUM-1 bound in `checkpoint-100-complete-current-v19-seventeen-part-manifest-v1.json` (SHA256 70093aebeeb1823cce0356c9fad1da20d5df6eb21b46661c20c69c07a1a3526a), THIS part, and all mandatory overlays. Parts 9–18 are LATER UNREVIEWED.

Imports:
- Part15 Q2 Lemma L, the peel lift proved there;
- Part15 Q3, the u-independent Bob-0 compression S(x)=T(v,w)+3P(|33>)+3P(|23>) at z=0, and its phase lemma reducing (v,w) to real v,w>=0;
- Part15 Q6, so that every R_x is entangled;
- (I1) Horodecki: a PSD operator on C^2⊗C^2 with PSD partial transpose is separable.

## E1. Statement

**Theorem C36 (cylinder).** Let x=(u,v,w,0) with u in C arbitrary and |v|^2+2|w|^2 <= 5/3. Then SN(R_x)=2.

The region is unbounded in u, and the certificate is uniform in u. Examples outside every earlier region:
- (2,1,1/2,0): normx^2=5.25>2, and m_L=|u|/√2-√2|v|-2|w|=√2-√2-1=-1<1, so it is outside Theorem C.
- (1,1.2,0,0): 1.44<=5/3, normx^2=2.44>2, and m_L=1/√2-1.2√2<0.

For very large |u| the cylinder overlaps Theorem C (Part10 H4.3, m_L>=1); the new content is the uniform-in-u coverage at moderate u. With Part15 Theorem E (|v|=|w|=t, t^2 in [1/2,9/8]), the whole diagonal |v|=|w|=t, 0<=t^2<=9/8, is covered, since 3t^2<=5/3 iff t^2<=5/9.

## E2. Proof

By Part15 Q3 and Lemma L it suffices to show that T(v,w) is separable for real v,w>=0 with v^2+2w^2<=5/3. Use p=|1>_B, q=|2>_B:
- t1=|1>p+|2>q, t2=|0>p+|1>q, t3=|2>p;
- t4=|0>q+|3>(vp+wq), t5=|3>q, t6=|0>(vp+wq);
- T = P(t1)+P(t2)+P(t3)+3P(t4)+3P(t5)+3P(t6).

**Five-point product family.** For r^5=1 put

`π_r = [ r|0> + |1> + r^{-1}|2> + v r^2|3> ] ⊗ (p + r q).`

Its components are:
- |0>p: r; |0>q: r^2;
- |1>p: 1; |1>q: r;
- |2>p: r^{-1}; |2>q: 1;
- |3>p: v r^2; |3>q: v r^3.

Grouping by the power of r gives π_r = Σ_{k=-1}^{3} r^k V_k with:
- V_{-1}=|2>p=t3;
- V_0=|1>p+|2>q=t1;
- V_1=|0>p+|1>q=t2;
- V_2=|0>q+v|3>p =: y;
- V_3=v|3>q=v·t5.

Since (1/5)Σ_{r^5=1} r^m=0 for 1<=|m|<=4,

`(1/5)Σ_r P(π_r) = P(t1)+P(t2)+P(t3)+P(y)+v^2 P(t5).`

Using y = t4 - w t5,

```
T(v,w) = (1/5)Σ_{r^5=1} P(π_r) + Res,
Res = 3P(t6) + 3P(t4) + 3P(t5) - P(t4 - w t5) - v^2 P(t5).                    (E2.1)
```

**Res>=0.** In the independent basis (t6,t4,t5) the coefficient matrix of Res is

`K = [[3,0,0],[0,2,w],[0,w,3-w^2-v^2]]`,

which is PSD iff 2(3-w^2-v^2)>=w^2, i.e. 2v^2+3w^2<=6. This follows from 2v^2+3w^2 <= 2(v^2+2w^2) <= 10/3.

**Explicit entries.** Order the basis as (|0>p,|0>q,|3>p,|3>q), with t4=(0,1,v,w), t5=(0,0,0,1) and t6=(v,w,0,0):
- (0p,0p) = 3v^2;
- (0p,0q) = 3vw;
- (0p,3p) = 0;
- (0p,3q) = 0;
- (0q,0q) = 3+3w^2-1 = 2+3w^2;
- (0q,3p) = 3v-v = 2v;
- (0q,3q) = 3w;
- (3p,3p) = 3v^2-v^2 = 2v^2;
- (3p,3q) = 3vw;
- (3q,3q) = 3w^2+3-v^2.

**PPT.** Res lives on the 2x2 system Alice{0,3}⊗Bob{p,q}. The partial transpose exchanges the (0p,3q) and (0q,3p) entries:

```
          [ 3v^2   3vw     0      2v        ]
Res^Γ =   [ 3vw    2+3w^2  0      3w        ]
          [ 0      0       2v^2   3vw       ]
          [ 2v     3w      3vw    3+3w^2-v^2 ]
```

Take v>0. The leading 3x3 block A3 is block-diagonal, consisting of M2=[[3v^2,3vw],[3vw,2+3w^2]] and the entry 2v^2. Since det M2 = 6v^2+9v^2w^2-9v^2w^2 = 6v^2 > 0, A3 is positive definite.

With b=(2v,3w,3vw), the Schur complement is s = 3+3w^2-v^2 - b^T A3^{-1} b. Here:
- M2^{-1} = (1/(6v^2))[[2+3w^2,-3vw],[-3vw,3v^2]];
- the M2 part of b^T A3^{-1} b is (1/(6v^2))[4v^2(2+3w^2) - 36v^2w^2 + 27v^2w^2] = (8+3w^2)/6;
- the last coordinate contributes (3vw)^2/(2v^2) = 9w^2/2.

Hence

`s = 3 + 3w^2 - v^2 - 4/3 - w^2/2 - 9w^2/2 = 5/3 - v^2 - 2w^2.`

So Res^Γ>=0 iff v^2+2w^2<=5/3. For v=0, Res^Γ has zero |0>p row and column, and its remaining block [[2+3w^2,0,3w],[0,0,0],[3w,0,3+3w^2]] is PSD because (2+3w^2)(3+3w^2)>=9w^2.

By (I1), Res is separable. So T(v,w) is a finite sum of product projectors, S(x) is separable, Lemma L gives SN(R_x)<=2, and Part15 Q6 gives SN>=2. ∎

**Spot check.** v=1, w=0 gives s=2/3 and Res^Γ=[[3,0,0,2],[0,2,0,0],[0,0,2,0],[2,0,0,2]], whose (0p,3q) block has determinant 6-4=2>0. At x0, (v,w)=(1,-1), we get v^2+2w^2=3>5/3. This agrees with Part15: at x0 the F=0 residual is non-PPT and the f=-1/2 family is needed.

## E3. Sharpness inside this family, and relation to other parts

1. **Sharp on w=0 for the real-f families F=f r^2 of Part15.** At w=0, write F2=f^2 and V=v^2. The residual partial transpose has entries (0p,0p)=(3-F2)V, (3q,3q)=3-V-F2V^2 and (0p,3q)=v(2-F2V). Its (0p,3q) principal 2x2 minor equals v^2(5 - 3V - 3F2 V^2 - 3F2 + 5F2 V). The F2-derivative of the bracket is -(3V^2-5V+3), which is negative because the discriminant is 25-36<0. So for V>5/3 this minor is negative for every real f, and V<=5/3 is the exact limit of these families at w=0. No claim is made about complex f or other families.
2. **Union with Part15.** On the diagonal, C36 covers t^2<=5/9 and Theorem E covers 1/2<=t^2<=9/8. An open neighbourhood of both pieces also follows by strict positivity, without an explicit radius.
3. **Not covered.** The rest of the z=0 slice (for example v^2+2w^2>5/3 off the Theorem E band, such as (u,√2,0,0)) and all z!=0 points remain governed by Parts 10–17. Part16's far ray and the z!=0 comparable core remain OPEN.

**Original physics-3/P44 remains UNMET.** These are author-WRITTEN candidates pending fresh reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v20 PART18/18.**
