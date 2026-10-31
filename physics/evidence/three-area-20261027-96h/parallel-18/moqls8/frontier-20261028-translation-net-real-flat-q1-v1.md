# Real-flat q1 exclusion for ALL binary translation five-nets of order 8

**PhysicsMOQLS8-2 / physics-4. COMPUTER-ASSISTED AUTHOR CANDIDATE**, using the independently recounted32-case exact rank certificate below;not yet peer/parent/formal/novelty accepted. This is a full result for an explicit net class,not a classification of all order-8 3-MOLS or unrestricted four-family classicality.

## 1. Theorem and exact class

Let Q,B1,B2,B3 be an ACTUAL ordinary four-MOQLS(8) family. Suppose Q is real-flat in one member-specific output frame,and the other three members are classical. In the F2^3 coordinate labels furnished by Q's ACTUAL first-row Walsh frame,suppose their classical Latin maps have the translation form

    L_a(i,j)=j+f_a(i),  a=1,2,3,  i,j∈V=F2^3,                 (1)

where the SAME row and column labels are used by every member. The f_a are arbitrary maps;do NOT assume them linear or scalar field maps. Normalize f_a(0)=0 by individual symbol relabellings. Actual row/column ONBs and all six ordinary pair-product ONBs are retained.

**Theorem candidate.** Under these exact hypotheses Q is classical. Therefore an all-real-flat four-family with translation-form classical mates at its sole possible nonclassical member is entirely classical. Any counterexample to unrestricted real-flat q1 must have a three-classical-mate net NOT equivalent to (1) in the selected Q's compatible Walsh labels.

This includes scalar-affine nets and noncommuting linear maps,but not general 3-MOLS nets. It does not claim all 5-nets are translation nets,all QLS are real-flat,or M(8) is determined.

## 2. Actual 3-MOLS makes the translation functions permutations

For a fixed a,each column of L_a is a permutation of V,so f_a is a permutation. For distinct a,b,an ordered pair of symbols satisfies

    L_a(i,j)+L_b(i,j)=f_a(i)+f_b(i).

The two actual classical squares are orthogonal iff every ordered symbol pair occurs once;for each difference this holds exactly when f_a+f_b is a permutation. Thus the conditions are both NECESSARY and SUFFICIENT for the three given translation squares to be actual 3-MOLS. No catalogue or quantum realization assumption is hidden.

Relabel rows by `i'=f_1(i)`;this is a common row permutation,fixes row0,and leaves Q's first-row Walsh labels unchanged. The three functions become

    I, A=f_2∘f_1^(−1), B=f_3∘f_1^(−1),

where A,B and I+A,I+B,A+B are ALL permutations fixing0.

## 3. Complete-mapping lemma: the apparently nonlinear maps are linear

The following ordinary finite lemma was proved in full independently in `frontier-20261028-binary-character-pair-classicality-v1.md`, SHA256 **6a8d3189460dfaa34738d1ee9eeaebd16d4e2d56e5170ce2858bc3206f78ab41**, §6;its proof is summarized here with every decisive case.

**Lemma.** If K:F2^3→F2^3 fixes0 and BOTH K and K+I are permutations,then K is additive linear.

For each nonzero x,the three distinct nonzero vectors `{x,Kx,x+Kx}` form a Fano line. Every nonzero point appears exactly once in each of these three positions. If m_l counts the seven lines,the 7×7 point-line incidence matrix B satisfies `BB^T=2I+J` and `Bm=3·1=B1`;hence every line appears exactly once.

K has no fixed nonzero point and no 2-cycle,otherwise K+I repeats a value. Its cycle type is 7 or3+4. A collinear 3-cycle repeats a line. For an independent 3-cycle a,b,c,the three K+I outputs are the nonzero points of the plane H={0,a+b,b+c,c+a};the remaining domain is H\{0} plus a+b+c. Its 4-cycle must contain an edge joining two H-points,whose sum repeats one of those already-used outputs. Thus a 3+4 cycle is impossible.

For the 7-cycle,write consecutive a,b,c. Repeated-line exclusion makes them a basis. The fourth point cannot be b+c (repeated line) or a+b+c (repeated K+I output),so is a+b or a+c. The same two-choice argument and no repeated points force the rest of the cycle:

    a,b,c,a+b,b+c,a+b+c,a+c;  or
    a,b,c,a+c,a+b+c,a+b,b+c.

Each is the orbit of the linear map sending a→b,b→c and c to its respective fourth point. Thus K is linear. This proves the lemma for ALL permutations,not merely for the 48 matrices in the computation.

Apply it to A and B. Both are invertible linear maps,and their pairwise differences with I and each other are invertible. This pays the nonlinear-to-linear reduction for the FULL translation class.

## 4. Nonzero D: a purely written universal exclusion

Define the linear map

    D=I+A+B.

At any heavy Q cell in a nonfirst row,the predecessor's exact support-plane XOR caller gives `j+L1+L2+L3=0`. Under (1),the four j terms cancel,so `D i=0`. This uses the SAME actual classical mates and Q frame,not an independently chosen net.

If D≠0,its kernel has dimension at most2,so at most THREE nonzero rows can contain heavy cells. Any actual Q column containing a heavy cell must contain at least FOUR heavy cells:all four support coordinates of that heavy ray require total ONB squared mass1,and each other real-flat heavy contribution is at most1/4 while light singletons cannot meet its support. This contradicts confinement to at most three nonfirst rows. Thus no heavy cell exists and Q is classical. This branch is entirely WRITTEN and applies to every nonzero D,including a hypothetical rank1;no code count is needed.

## 5. Rank1 D cannot occur — further exact structural strengthening

The actual 3-MOLS hypotheses in fact rule out rank(D)=1. This fact is not needed for §4,but identifies the full translation-net geometry.

A and I+A are invertible. Its characteristic polynomial is a cubic over F2 with no root0 or1,so irreducible. Hence F2[A] is F8 acting on V as a one-dimensional vector space. Write A as multiplication by α∈F8\{0,1};its multiplicative order is7.

Suppose D has rank1,so D=uℓ with u≠0 and nonzero linear functional ℓ. Since B=I+A+D and I+B=A+D and A+B=I+D are all invertible,the elementary rank-one update identity says

    ℓ((I+A)^(−1)u)=ℓ(A^(−1)u)=ℓ(u)=0.                           (2)

Indeed for invertible T,`T+uℓ=T(I+vℓ)` with v=T^(−1)u;over F2,the latter is singular iff ℓ(v)=1,and if ℓ(v)=0 its inverse is itself.

But the three vectors `u,A^(−1)u,(I+A)^(−1)u` are linearly independent. In the field,divide by u;the corresponding scalars are `1,α^(−1),(1+α)^(−1)`,distinct and nonzero. A dependence over F2 would make their sum0,which after multiplying α(1+α) says α²+α+1=0. Then α³=1,contradicting its order7. No nonzero ℓ can annihilate all three. Hence D has rank0,2 or3.

Therefore if D≠0,the actual stronger consequence is that at most ONE nonfirst row could satisfy the heavy XOR condition. The proof of Q classical still only needs the ≤3-row argument in §4.

## 6. D=0: exact scalar-affine reduction and finite rank certificate

If D=0,then B=I+A. By the same irreducible-cubic argument,an invertible change of F2^3 basis conjugates A to multiplication by a nonzero F8 element α≠1. Apply that SAME linear change to the common row and column labels and to each classical mate's output labels. Its action on Q's first-row Walsh basis is implemented by a signed permutation of its real-flat coordinates,so the real-flat property and actual grid are preserved.

The three maps are now scalar-affine with slopes `{1,α,1+α}`,a three-element nonzero part of a 2-dimensional F2-subspace. The multiplicative group F8* acts transitively on the seven 2-planes,so a common row scaling/mate permutation normalizes the slopes to `{1,2,3}`. Any hypothesized heavy cell can then be moved to (1,0) by the explicit common affine grid/flat-frame symmetry of the preceding certificate packet.

The full candidate `frontier-20261028-affine-net-real-flat-q1-exclusion-v1.md`, SHA256 **8bc663817b639e4eef9fbfda864d165cba13462253e13367dd4caff68c62b79c**, proves the normalization/physical callers and binds the exact finite check. It enumerates ALL1152 possible anchored first nonfirst rows and ALL2304 possible second nonfirst rows,applying every actual column and three mate line constraints. Exactly512 pairs survive,with32 distinct first-row patterns. For each pattern a later ACTUAL cell must be orthogonal to four first-row axes and four selected first-row-after-anchor rays;the resulting 4×4 projected determinant is ±1024,so no complex unit vector can occupy that cell.

The full32-pattern certificate is SHA256 **0f498ce65d5b711acbac89390b3312066a5bc0751604b7dde497d4b6fdf38749**. A separately written per-cell-DFS/Leibniz checker,receipt SHA256 **c9e25983037994ce73caa38af87631a0d350c75fec416189081a3ac3d68aaec5**,recounts ALL2,654,208 pairs and checks ALL32 determinants,with genuine classical positive and omitted-coverage/singular-matrix negative controls. Another independent in-harness AC-3 formulation also exhausts the fixed anchored net. This is **computer-assisted at the D=0 branch** and requires independent review of the source,normalization,coverage and proof receipt;the common determinant or a caption alone is not a proof.

Combining §4 with §6 proves the stated translation-net result conditional on that exact finite certificate and its mathematical caller.

## 7. Exact finite translation-net census and a genuine enlargement

Executed once: `python3 -B frontier-20261028-translation-net-classifier-v1.py --output frontier-20261028-translation-net-classifier-receipt-v1.json`. Source SHA256 **0ae3414b880609c923a2c8e5bb3003aebd5c03751c11ace5ee54c4a68dbeb6ff**;receipt SHA256 **99d16af91f0705a3b5418141e6d8a57fc954ae98c13f4edeed7133233710dbc2**.

Actual exact output: all5040 normalized permutations examined;48 complete mappings,all additive. All168 invertible linear maps generated;all **576** ordered normalized 3-MOLS translation nets directly checked for every Latin row/column and every ordered symbol pair. D-rank histogram **0:48, 2:336, 3:192**;all48 D=0 operators have order7. Among the576 nets,240 have AB=BA and **336 do not**,showing that the all-translation theorem covers genuinely noncommuting linear examples beyond the original scalar-affine net. Duplicate-square and nonpermutation negative controls were rejected. Observed elapsed0.037s. This census corroborates §§3–5 but is not used to replace their proofs or establish all-net coverage.

## 8. Original residual and assurance

This is an exact all-variable q1 theorem for real-flat Q and three translation-form classical mates in its Walsh label group,with a finite D=0 certificate. The input may be nonlinear in its original row parameter;row normalization and the complete-mapping lemma cover it. It does not apply automatically to arbitrary classical 3-MOLS,whose symbols may depend non-translation-wise on both row and column,or to non-real-flat Q.

With the separate real-flat q≤1 candidate,an actual all-real-flat four-family satisfying the translation-net condition at its possible quantum member would be classical. The general real-flat/nontranslation q1 problem and original unrestricted four-family problem remain OPEN. No physical nonclassical witness,global no-go,M(8),novelty/priority,independent-model/human or formal/kernel acceptance is claimed. Parent review must read the complete predecessor and32-case certificate/checker source;the two in-harness finite verifiers are not independent vendors.
