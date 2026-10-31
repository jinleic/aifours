# Real-flat q1 exclusion for an actual scalar-affine order-8 five-net

**PhysicsMOQLS8-2 / physics-4. COMPUTER-ASSISTED AUTHOR CANDIDATE: exact finite exhaustion independently recounted by two differently implemented checkers, with an explicit complex-rank certificate.** Awaiting disjoint mathematical/code review and parent replay; no formal/kernel or novelty claim. This is not an unrestricted four-family theorem.

## 1. Exact theorem candidate and limits

Let Q,B1,B2,B3 be an ACTUAL ordinary four-MOQLS(8) family. Assume Q is real-flat in one member-specific ONB,as defined in `frontier-20261028-flat-real-four-family-heavy-rigidity-v1.md` SHA256 **c19176626318f4ad2da6b597b5f32013d34d99cf3e4b871b744a69b20fad7568**. Assume the other three members are classical,and in the F2^3 labels furnished by Q's first-row Walsh frame their actual Latin symbols are

    L_a(i,j)=j+a i,  L_b(i,j)=j+b i,  L_c(i,j)=j+c i,          (1)

for three distinct nonzero scalars a,b,c of F8. The same affine grid is used by all members. Independently rephasing cells,member output unitaries,global row/column relabels and permutation of the three mates are allowed. The F8 addition must be the additive F2^3 structure in Q's Walsh labels;this is a compatibility HYPOTHESIS,not an arbitrary field relabelling inferred from the Latin squares.

**Candidate theorem.** Under these hypotheses Q is classical. If a+b+c≠0 this is a complete written support-plane proof;if a+b+c=0 it uses the exact finite rank certificate §§4–6. Hence an all-real-flat four-family is entirely classical whenever,after the allowed normalizations,the three classical mates of its possible sole nonclassical member have the specified scalar-affine net. This does NOT classify all 3-MOLS nets as affine,does not cover arbitrary GL(3,2)-linear mate maps,and does not settle q1 for nonaffine nets or unrestricted complex QLS.

## 2. Zero-sum versus nonzero-sum slopes

The predecessor `frontier-20261028-flat-real-q1-reduction-v1.md` SHA256 **d7f90ef8420ab431be46dc3753338cc92d425231aa1cc4a691532de2eb88c0d1** proves the following actual caller,independently reconstructible from the supplied definitions:

- In Q's first-row frame,every real-flat entry has support1 or support4. A support4 is an affine2-plane of the F2^3 Walsh labels.
- At any nonfirst cell (i,j),the column constraint and three classical mate product constraints forbid the four DISTINCT first-row labels `j,L_a(i,j),L_b(i,j),L_c(i,j)` from Q's support. If Q is heavy,its four-element support is the complement of those labels,so they form an affine2-plane and their XOR is0.
- Thus every heavy cell satisfies `j+L_a+L_b+L_c=0` in the Walsh-label F2^3 structure. A nonclassical Q has a heavy cell in every first-row frame.

For (1) the XOR equals `i(a+b+c)`. If a+b+c≠0,field multiplication is injective and no i≠0 heavy cell exists. First row is light;all Q entries lie in its first-row basis,so Q is classical. This branch uses NO finite enumeration and covers every choice of the three distinct nonzero slopes at these explicit label hypotheses.

## 3. Complete normalization for the zero-sum branch

Suppose a+b+c=0. Then `{0,a,b,c}` is a 2-dimensional F2-subspace A of F8. There are seven such planes. The multiplicative group F8* has order7;any nonidentity scalar has order7. If it preserved A,it would carry any nonzero a∈A through all seven nonzero field elements,contradicting |A\{0}|=3. Thus every plane has a seven-element scalar orbit,so all seven planes are scalar-equivalent.

A common row relabelling `i' = u i`,with j unchanged,changes slopes to a/u,b/u,c/u and preserves first row0. Choose u to make the slope set exactly `{1,2,3}` in the explicit bit encoding F2[x]/(x³+x+1);permuting the three companion members arranges that order. This reduction is complete for SCALAR F8 slopes,not an assertion about other 3-MOLS classes.

If a heavy cell exists,it lies in some nonfirst row i0 and column j0. Put `t=i0^(−1)` and `d=t j0`;apply common grid relabellings

    i'=t i,   j'=t j+d,

and,for every classical mate,relabel its output symbol z as `t z+d`. Then the three maps remain `L_s(i',j')=j'+s i'` for s=1,2,3,and the heavy cell becomes (1,0).

Q's first-row ray labels change by the same affine map `j→t j+d`. In its real-flat sign frame the unitary taking Walsh character χ_j to χ_(t j+d) is a signed coordinate permutation:for the F2-linear multiplication matrix T, `(U v)(x)=(-1)^(d·x) v(T^T x)`. Hence it preserves the real-flat ± sign alphabet and maps the new first row back to the standard labelled Walsh rays. This establishes the anchored search **without loss within the stated scalar-affine/compatible-frame class**,not within all ordinary QLS.

## 4. Exact coverage of the first two nonfirst rows

Use the explicit sign-ray encoding in the certificates:the first of eight sign coordinates is fixed plus;the other seven bits have even parity,so six bits determine the seventh. First-row Walsh rays in field-label order are

    [0,21,38,51,56,45,30,11].

An integer 0..63 denotes its six-bit sign ray. For any two such rays their raw real inner product numerator is `8−2·HD_7`,and physical normalized overlap is that integer divided by8. Orthogonality is therefore checked exactly by the sign bits,not by numerical tolerance.

Let A0={0,1,2,3}. For nonzero row i and column j,the column and the three classical-symbol lines force the selected Q vector orthogonal to the first-row axes labelled `j+i A0`. This is an affine 2-plane;its complementary support plane has FOUR axes. Among the64 sign rays,exactly FOUR light rays and FOUR heavy rays are supported there. The latter form an ONB of that four-space,as do the former:for a fixed support plane the four allowable Fourier sign patterns have product−1,modulo common sign,and distinct patterns differ at exactly two of the four coordinates.

For fixed i,the columns j split into two cosets of iA0,FOUR columns each. All Q entries in one column coset lie in the SAME corresponding four-space. Their four unit vectors are mutually orthogonal because they lie in the SAME actual Q row. A singleton and a heavy vector cannot be orthogonal inside this four-space because every heavy coordinate is nonzero. Therefore each four-cell group uses EITHER all four distinct light rays OR all four distinct heavy rays. Every ordering is allowed in the enumeration.

Consequently every row has exactly `(2·4!)²=2304` possible real-flat ONBs compatible with the first row and the four initial net lines. In row1 the anchor (1,0) is heavy,so its four-cell group must be the heavy type: exactly **1152** row1 options. No assumption about rows3–7 is made here.

For rows i≠k,actual column orthogonality and the three actual classical mate fibres require

    Q(i,j) ⟂ Q(k, j+s(i+k))   for EVERY j∈F8, s∈{0,1,2,3}.      (2)

The s=0 case is the original column;the others follow from equality of mate symbols `j+s i`. These are precisely32 distinct original line constraints for each row pair.

## 5. Exhaustive row-pair and arbitrary-complex continuation obstruction

`frontier-20261028-affine-q1-span-exhaust-v1.py`, SHA256 **f296f1188492bf4cbedd4942d9311d5e4ecd48113794104109efe7c4f9d46aef**, enumerates ALL1152×2304=**2,654,208** row1/row2 combinations and applies ALL32 conditions (2). It finds exactly **512** compatible pairs involving **32 distinct row1 patterns**. The complete machine-readable certificate is `frontier-20261028-affine-q1-span-exhaust-receipt-v1.json`, SHA256 **0f498ce65d5b711acbac89390b3312066a5bc0751604b7dde497d4b6fdf38749**. Every pattern,its number of compatible row2 choices,its witness row and its exact 4×4 projection matrix/determinant are in that receipt.

For EACH of those32 row1 patterns,the certificate supplies k∈{3,4,5} such that the hypothetical actual Q entry in cell (k,0) must be orthogonal to:

- the FOUR first-row axes at columns `s k`,s=0,1,2,3;and
- the FOUR actual row1 rays at columns `s(k+1)`,s=0,1,2,3.

These are the column and three mate-symbol lines through the SAME cell (k,0). The first four axes are distinct and span a four-space. Project the four specified row1 rays to its four-dimensional orthogonal complement. The certificate's corresponding 4×4 matrix contains their raw sign inner products with the remaining first-row basis rays;EVERY determinant is exactly **+1024 or −1024**. Dividing entries by8 does not change nonzero rank. The projected rays span the entire complement.

Thus the eight required constraints span C8,and NO nonzero complex vector can occupy that actual cell. This obstruction is stronger than failure to choose another flat sign ray:after the first two nonfirst rows,that one later cell is allowed to be an ARBITRARY complex vector. It also preserves exactly the same three classical mates and row incidence,not four independently chosen orthogonality systems.

For the four row1 patterns with k=4 arising in the separate row1–row3 exhaustion,the relevant raw matrices,for example,have determinant1024;the complete32-pattern certificate is the source of the ALL-cases assertion. It is not enough to verify one such matrix.

## 6. Independent exact recount and controls

A separately written verifier `frontier-20261028-affine-q1-rank-certificate-check-v1.py`, SHA256 **2d48aa55d78ca682b16cf3632ba55f734f2ea9f075a09d51a104e0968218dab9**,imports NO producer code. It hash-binds the full32-pattern certificate. It constructs each row's allowed sign rays from the ACTUAL five line labels and generates row ONBs by **per-cell orthogonality DFS**,rather than the producer's two 4D-block/permutation construction. It then:

1. recounts 1152 and2304 row options and all2,654,208 pairs;
2. reconstructs all32 surviving row1 patterns and all512 compatible pairs;
3. independently identifies the first-row/row1 lines through each certified cell;
4. recomputes all actual sign inner products and verifies each determinant by the **Leibniz permutation formula**,not the producer's rational Gaussian elimination;
5. checks a valid all-classical affine row-pair positive control;
6. rejects an omitted-pattern coverage mutation and a duplicated-matrix-row singularity control.

Execution: `python3 -B frontier-20261028-affine-q1-rank-certificate-check-v1.py --certificate frontier-20261028-affine-q1-span-exhaust-receipt-v1.json --output frontier-20261028-affine-q1-rank-certificate-check-receipt-v1.json`. Receipt SHA256 **c9e25983037994ce73caa38af87631a0d350c75fec416189081a3ac3d68aaec5**;actual output `PASS_INDEPENDENT_AFFINE_ROW_AND_COMPLEX_RANK_CERTIFICATES`,32/32 nonzero determinants,512 pairs,positive and two intended-reason negative controls. It ran in0.626s.

A third,in-house independently formulated **cell-domain AC-3** search `frontier-20261028-affine-five-net-flat-csp-v1.py` SHA **168ef1d9f261b2ca9e101f62e851b574240791ac3d44b0556a1dd9283f06a664**,receipt SHA **e18b2195f24b9ceba18e01da01c043b6a318845420252ad160512d109e9ad807**,also exhausts the SAME fixed net/anchor:no solution,17 DFS nodes,36,002 arc revisions,24 contradictions,0.046s. Its direct actual classical four-family control checked all rows/columns and all six pair-product ONBs;duplicate-cell control was rejected. It does not use the rank certificate or enlarge the class.

A separate exact row-exhaust source `frontier-20261028-affine-q1-row-exhaust-v1.py` SHA **fcd837578ec14116725cbf2eac23c8911158ceaffd8664b07f77c50b8ce07c4e**,receipt SHA **d47cebb5538893d97558ed8fb6dcba1d7a10c8365a065ac4ed33829de8212b74**,found512 compatible row1/row2 pairs,8 compatible three-row extensions,and0 compatible fourth nonfirst rows. This is consistency evidence,not a substitute for the32-rank certificate. Two in-kernel exploratory enumerations preceded these files;they are not counted as independent verifiers.

The three exact programs are different algorithms in the SAME harness,not independent-model/human/formal verification. They use no numeric tolerances. A peer must check row-option completeness,field/anchor automorphisms,all physical line callers,certificate hash and all32 determinants before adoption. Neither a solver timeout nor the earlier flat-sign Z3 memory failure is treated as an exclusion.

## 7. Original target and trust boundary

The sum-zero normalized representative plus all-field-slope/anchor reduction would prove q1 classicality ONLY for the explicitly defined scalar-affine 5-net and compatible real-flat selected frame. Together with the separately review-pending all-real-flat q≤1 theorem,it would settle all-real-flat four-families whose three classical companions fall in that special net class. It does not assert that other classical 5-nets are equivalent to it,that their labels are compatible with Q's flat frame,or that every ordinary QLS is real-flat.

No actual nonclassical four-family,wider numerical M(8) value,unrestricted no-go,novelty/priority,book-source,formal/kernel/human/configured-family acceptance is claimed. Further work must address other 5-net types or leave the real-flat hypothesis. The finite positive controls establish the actual ordinary row/column/pair-product interpretation,while finite UNSAT-like conclusions remain conditional on independent code/certificate review.
