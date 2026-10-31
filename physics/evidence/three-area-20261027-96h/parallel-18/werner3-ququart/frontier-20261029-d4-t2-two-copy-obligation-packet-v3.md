# T2 at d=4: proved subclasses, an exact reduction of the rank-one-B residual, and finite evidence (v3)

**PhysicsResearch96h-2 / physics-1. WRITTEN, plus exact-arithmetic computations; UNREVIEWED.** This is the single successor packet for this line. It replaces `frontier-20261029-d4-t2-two-copy-obligation-packet-v2.md` (SHA256 `022049e48a2c0e3c7fa96235fc049d633ffeee5478e9be5cedac910459a23423`) and its addendum `frontier-20261029-d4-t2-packet-v2-addendum-1-block-identity.md`. Both are kept unchanged. Their content is carried over here, so v3 can be reviewed on its own.

It relies on the v2 stratified packet (SHA256 `bf50bfbf3d0f4d24ec6a9e5fc55b19ced5cd2acdb223bbb1518fe6ebf4177329`), as dispositioned with qualifications in `dispositions/physics-1-werner-stratified-duals-and-support-ladder-parent-v1.md`. "Leg" always means a leg at a **site**. Only v2 Theorem 6 with s=1 is used here: a single ≤2-dimensional leg at **one** site.

The finite search and the second-order tests are evidence and local behaviour only. They are not a proof of T2 or of q3 positivity. This packet makes no claim of T2, T3, Z2, literature status, novelty, adoption, or f153/f62/f168 scope change. Held material and held guidance are not used. Explicit operators are evaluated only in §6, under Main's authorization of an exact counterexample search.

## 1. The obligation

At d=4 the following are equivalent (v2 Theorem 1):

- **(T2, primal)** `q2(C)=||C||²−½||Tr_1C||²−½||Tr_2C||²+¼|TrC|² >= 0` for every complex C on C⁴⊗C⁴ with rank C ≤ 2.
- **(T2, dual)** `σ1(X)²+σ2(X)² <= ||X||²/2 = 2(||A||²+||B||²)` for every `X=A⊗I+I⊗B` with A, B traceless.

The original target implies T2 (v2 Corollary 1). Tracelessness is essential: v2 gives an exact counterexample when it is dropped.

*[Unverified recollection, not a premise and not a source result.]* The dual resembles a matrix inequality discussed in the two-copy distillability literature. Its status was not checked.

## 2. The safe-subspace lemma and the normal case

**Lemma 2.1.** Let F⊂C⁴⊗C⁴ be two-dimensional, and suppose its leg at some site has dimension ≤2. Then `||XP_F||²<=||X||²/2` for every X in W_odd. The same holds for left subspaces, by passing to X†.

*Proof.* Suppose `||XP_F||²>||X||²/2`, and set `C=XP_F`. Then C has rank ≤2, `||C||²=<X,C>=||XP_F||²`, and `||P_odd C||²>=|<X,C>|²/||X||²>||C||²/2`. Hence `q2(C)<0`. But `ran C†⊂F`, so the input leg of C at that site has dimension ≤2. By v2 Theorem 6 (s=1) together with T1, `q2(C)>=0`, a contradiction. ∎

**Theorem 2.2.** T2 holds whenever A or B is normal.

*Proof.* By local-unitary invariance we may take `B=diag(b)`. Then `X=⊕_j(A+b_jI)` over the site-2 basis. Its top two right singular vectors can be chosen as `ψ⊗e_j` and `φ⊗e_l`, so their span has site-2 leg inside `span{e_j,e_l}`. Lemma 2.1 finishes the proof. ∎

**Premise-dependent case.** Assume the imported Böttcher–Wenzel inequality `||[A,Ψ]||²<=2||A||²||Ψ||²`. Then T2 holds when `B=−A^T`, because `XvecΨ=vec[A,Ψ]`. Without this premise, nothing is claimed for this case.

## 3. Exact block identity and the trace-sign criterion

For any C, fix an orthonormal site-2 basis and define the blocks `C^(kl)=<e_k|C|e_l>_2`. Expanding `K_2=I−½|Ω_2><Ω_2|` gives

`q2(C) = Σ_(k,l) q1(C^(kl)) − ½ q1(Tr_2 C)`, with `q1(Y)=||Y||²−½|TrY|²`.   (3.1)

The same identity holds with the sites exchanged.

**Lemma 3.2.** Suppose rank C ≤ 2 and either `q1(Tr_2C)<=0` or `q1(Tr_1C)<=0`. Then `q2(C)>=0`.

*Proof.* Each block is a contraction of C, so it has rank ≤2, and T1 gives `q1(C^(kl))>=0`. Apply (3.1). ∎

**Split identity.** Let P be a rank-2 projection at site 2, `J=2P−I`, and `C_P=(I⊗P)C`. Then

`q2(C)=q2(C_P)+q2(C_(I−P))−¼q1(Tr_2C)+¼q1(Tr_2[C(I⊗J)])`.   (3.3)

For rank C ≤ 2, the first two terms are ≥0 by v2 Theorem 6 (s=1). So T2 holds for C whenever some such J satisfies `q1(Tr_2[C(I⊗J)])>=q1(Tr_2C)`. No general J is proved to exist.

Averaging over Haar-random P uses `E[J⊗J]=−(1/15)I+(4/15)F`. The averaged form of (3.3) contains no information beyond (3.1).

## 4. Exact reduction of the rank-one-B case to a single-matrix inequality

Let B be traceless of rank one. Then `B=|x><y|` with `<y|x>=0`. After a local unitary and a phase, `B=b|e0><e1|` with b≥0. Since `Be_j=bδ_(j1)e_0`,

`X = X01 ⊕ (A on C⁴⊗e2) ⊕ (A on C⁴⊗e3)`,
`X01=[[A, bI],[0, A]]` on `C⁴⊗span{e0,e1}`.

X is block diagonal, so its singular values are the union of those of the blocks. The top pair of X falls into one of three cases:

- **Both vectors from X01.** The span lies in `C⁴⊗span{e0,e1}`, so it is safe by Lemma 2.1.
- **Both vectors from the A blocks.** The span lies in `C⁴⊗span{e2,e3}`, so it is safe.
- **Cross case.** The value is `σ1(X01)²+σ1(A)²`, attained on `F=span{v1, φ⊗e2}`, where v1 is the top right singular vector of X01.

Write `v1=(ψ0,ψ1)` with `p²=||ψ0||²` and `q²=1−p²`. Expanding `||X01v1||²` and maximizing over b∈C gives the following exact equivalence.

**Proposition 4.1.** Fix a traceless A. T2 holds for every `X=A⊗I+I⊗B` with B traceless of rank one **if and only if**

`||Aψ0||²+||Aψ1||²+|<Aψ0,ψ1>|²/(1+p²)+σ1(A)² <= 2||A||²`   (†)

for all ψ0, ψ1 with `||ψ0||²+||ψ1||²=1`.

For the "only if" direction: if (†) fails, choose the optimal b. Then F above gives `||XP_F||²>||X||²/2`.

**Proved parts of (†), all WRITTEN:**

- **(a)** (†) holds whenever `||A||²>=((5−2sqrt2)/2)σ1(A)²`, approximately `1.0858σ1²`. The proof uses `|<Aψ0,ψ1>|<=σ1pq` and `max p²q²/(1+p²)=3−2sqrt2`.
- **(b)** For a fixed b, the cross case is safe whenever `|b|>=σ1(A)|<u,φ>|` for a top singular pair `Aφ=σ1u`. The reason is that `σ2(X01)²>=min(σ1², |b|²+σ1²(1−|<u,φ>|²))`, which follows from the orthogonal pair `(φ,0)`, `(0,χ)` with χ the normalized u-perpendicular part of φ. In particular, (†) holds for every A that has a top singular pair with `<u,φ>=0`. This includes every rank-one traceless A, where (†) is attained with equality when ψ0 and ψ1 are parallel to φ.

**Residual, exactly.** For rank-one B, the only part of T2 not yet proved is (†) in the regime where:

- `||A||²<1.0858σ1(A)²`, i.e. A is nearly rank one, with
- `|b|<σ1|<u,φ>|` for the optimal b.

In this regime tracelessness forces `σ1|<u,φ>|=|Tr(A−σ1uφ†)|<=sqrt(3(||A||²−σ1²))<0.51σ1`. Since (†) is attained with equality at rank-one A, any proof in this regime must be sharp to second order.

## 5. Status by class

**Proved (WRITTEN, source-independent; v2 and here):**

- Primal:
  - rank ≤1;
  - rank ≤2 with a ≤2-dimensional leg at some site;
  - rank ≤2 with a spread range (`μ1+μ2<=2`, v2 Theorem 3);
  - the trace-sign class of Lemma 3.2.
- Dual:
  - Lemma 2.1 subspaces;
  - A or B normal;
  - rank-one B, outside the explicit residual of §4;
  - `B=−A^T`, only under the explicit Böttcher–Wenzel premise.

**Open.** The non-normal residual: both A and B non-normal, with every top-2 singular subspace having legs ≥3 at both sites and `μ1+μ2>2`. Its sharpest isolated core is (†) in the residual regime of §4. Z2, the original stratum equivalent to T2, and the full target all remain open.

## 6. Finite exact evidence (authorized search; no further Hessian variants)

- **Descent search.** Integer-only descent on `q2(UV†)/||UV†||²`, 24 starts × 600 iterations. No negative value appeared. The limit points lie numerically in the class with a ≤2-dimensional leg at some site.
  - Script SHA256 `485885e8017c751dd73cb3c39e368ef963c8d5526da2f47a8ae992ea384652d5`.
  - Results SHA256 `4eda6670d3f05c47d6382e97428a958ba60b35cb7ff7c61fd94f7b4e9f904bda`.
- **Exact second-order forms** on all 60 real directions of `sl4⊕sl4`:
  - At `X0=|0><1|⊗I+I⊗|0><1|`: inertia (0,34,26). Script SHA256 `4ce2add20a4ba87b48bad53d597e408d972fc928c97a80aff15c5d51158a3e03`; results SHA256 `70b90bc41a34d96bb1806883986e00288216d57dfd8c465abbf82479eb1ea0ba`.
  - At `X1=diag(3,−1,−1,−1)⊗I+I⊗diag(1,1,−1,−1)`: inertia (0,38,22). Script SHA256 `dc572db4ba0e953a5219120df30606511ad6db63f2b6570276654fff41b51a44`; results SHA256 `79d9332c67b3a85e13b51b1e4d7aff928422e4d1f09488d2a0f19abb4edecc3f`.
  - Overestimating faults turn both forms indefinite.
- **Equality family (written).** The whole family `X=aE01⊗I+bI⊗E01` consists of dual equality points. Its squared singular values are `a²+b²` (×2), `a²` (×2), `b²` (×2) and 0 (×10), so `σ1²+σ2²=2(a²+b²)`.

All of these are finite or local observations and do not establish T2.

**Provenance.** This packet uses the original functional, v2 Theorems 1, 3 and 6 (s=1), local-unitary invariance, elementary singular-value inequalities, the Haar moments of rank-2 projections in C⁴, exact integer and Fraction arithmetic, and, in §2 only, the explicit Böttcher–Wenzel premise. No source premise or held input is used. The f153/f62/f168 boundaries are unchanged.
