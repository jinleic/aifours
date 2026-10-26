# Bounded reconstruction of Sun8/P7 four-wise generation

Reviewer: **MathKacMoody**, actual slot math-3, at the parent's explicit one-review assignment. Observed immediately before creation: **2026-10-23T14:38:35-07:00**. Only this review file is written in the reviewer's own Kac–Moody root; no author file was edited. No scientific execution, enumeration, CLI, kernel or nested agent was used.

## 1. Corrected source binding and exact verdict

Complete reviewed main source: sun-coset8/four-wise-generation-v1.md, lines1–107, actual observed SHA-256:

    69f55c231f9d9458370a9c3464e5208e9043e37858c82c3b28820e809433883c

The parent's first assignment message instead supplied the string with segment `e37858f82c`; the actual file has `e37858c82c`. I stopped the binding gate and reported this mismatch. The parent explicitly confirmed the FULL ACTUAL hash above as the intended immutable snapshot and corrected its assignment. This review proceeds ONLY on that confirmed pin; it is not a silent substitution.

Complete reviewed dependency: sun-coset8/four-overgroup-residual-v1.md, lines1–145, actual observed SHA-256:

    d588fe306856763d5a48ae71d4504a10c3430124c3c258c823944fb448057eee

This matched both assignment and main-source dependency. Also read the complete reduction-and-generation-v1.md and structural-addendum-v1.md at their definitions/fibre/projection interfaces, plus the internal Sun5 statement and its two parent errata. Primary Zhu Theorem1.1 and Margolis–Schnabel TheoremB/Proposition4.5 statements were opened.

**Verdict: no FATAL or MAJOR mathematical defect found in the complete R4→G4 argument at its explicit imported interfaces. One MINOR standalone-LemmaF wording clarification follows.** The claimed result is four-wise generation for P7, in both orientations, NOT P7 exclusion or unrestricted Sun8. Parent composition, formal verification, import authentication beyond the reads stated here, novelty and priority remain separate.

## 2. Finding

### MINOR — order-three selection in a possibly nonfaithful standalone action

**four-wise-generation-v1.md lines23–25.** LemmaF is stated for an arbitrary acting group Q without faithfulness, but line25 says that raising a stabilizer element gives an element of order3. What is directly proved is that its INDUCED PERMUTATION has order3; a lift to a group with nontrivial/infinite kernel need not itself have order3. All subsequent incidence reasoning uses only that permutation, so the proof is fixed by saying “pass to the permutation image” or “an induced permutation sigma of order3.” The actual application has faithful finite Q≤S7, so this has NO consequence for G4's mathematical conclusion. It is a clarification of the lemma's standalone proof, not a counterexample to LemmaF or G4.

## 3. Imported statements and their actual application scopes

### Internal S5

Read institute/runs/six-lane-2026-10-18-96h/review/sun56-S56W-parent-verdict-v1.md, especially lines5–10, with errata1/2. Actual source hashes:

- parent verdict: `63baa72b107e0f809c26a5057f10b6fd31f8ae2f09cffb527873bec11a8107ee`;
- erratum1: `b2299b6ffd37fcc1a68370fd0c75abf4a3590fc8d6fad41b0ef7e5da39f40aae`;
- erratum2: `ef62c628e1ad37d0302d451d6862f3d4c859e9deac237d5bdc5925c8b960fded`.

The literal accepted interface says every five disjoint left cosets of finite-index subgroups in ANY group have an index pair with gcd>=5. It permits equal subgroups and has no covering, solvability, minimal-order or finite-original-group restriction. The verdict records that the C5W composition gate is discharged; the errata restrict statement substitution and preserve its trust boundary. R4 uses exactly that statement once, for the five actual fibre pieces in the baseline2-cell in the all-four-t=4 branch. Their pairwise gcds are at most4. This is a matched application. I have not independently re-proved the entire historical S5 DAG or authenticated its old model-review process.

### Classical Z3/Z4 and MS45/MSB

Opened [Zhu2008 Theorem1.1](https://arxiv.org/html/0807.2207v1), which states Sun3/Sun4 for arbitrary groups and disjoint finite-index LEFT cosets. Opened [Margolis–Schnabel](https://arxiv.org/html/1803.03569): TheoremB is only for tuple length<=4; Proposition4.5 excludes(2q1,4q2,4q3,4q4) for pairwise-coprime q_i with q1 odd, in any group. These are the exact interfaces the dependency declares. Its use of TheoremB occurs only AFTER proving that each fibre cell has at most four pieces. No general G-to-Z transfer is used, and no statement about length>4 is imported.

## 4. Reconstruction of the complete R4 reduction

### 4.1 Fibre orientation and t=4 closure

For an intersection point g_i u0=x w0, the fibre in xW is

    g_iU_i ∩ xW = x w0(U_i∩W).

Thus translating by x^{-1} gives a LEFT coset of the ACTUAL U_i∩W, with no missing conjugation. It has index lambda_i=r_i t_i. The number of occupied W-cosets is t_i=[U_i:U_i∩W]. Four baseline subgroups inside W occupy different cells because their r_i indices in W are coprime. An outlier sharing a baseline requires gcd(r_b,t_i)>1, so t_i<=3+omega(t_i); t5,6,7 are excluded, leaving t<=4.

A t4 outlier meets the unique baseline owning2 and all three holes. Therefore every outlier cofactor is odd. A t1 outlier cannot meet its holes or any baseline. If a t3 outlier coexists, its fibre index is coprime to4r_A unless3 divides r_A; otherwise it has too few possible cells. Hence at most one t4 can coexist with t3. In that branch baseline cofactors have no3, all t3 outliers use all holes, and any t2 outlier is coprime to them and has too few cells. The other three outliers must be t3; their three fibres with the t4 fibre have all pairwise gcds3 in a hole, excluded by Z4.

Without t3, the dependency exhausts k=1,2,3,4 t4 outliers:

- k1: each of the four cells occupied by t4 can admit at most one of the three t2 outliers by Z3; six required incidences exceed four.
- k2: a t2 piece cannot enter the baseline2-cell. If v2(r_b)=1, Z3 applies to it, the baseline and one t4 piece. If v2(r_b)>=2, the tuple is(2r_C,4(r_b/4),4r_A,4r_B), satisfying MS45: r_C is odd, all four cofactors remain pairwise coprime. Two t2 pieces then need four hole incidences where only three are available.
- k3: any t2 piece shares a cell with all three t4 pieces, directly the MS45 pattern with odd r_C.
- k4: baseline plus all four t4 pieces gives five disjoint fibres with every index gcd<=4; the literal internal S5 interface applies.

No valuation or positive-cofactor case was silently dropped.

### 4.2 Six-residue capacity and vacancy exhaustion

Once t∈{1,2,3}, every pair gcd(lambda_i,lambda_j) divides6: a common prime can only be2 or3, and the cofactor coprimality bounds its COMMON exponent to1. A hole has at most four pieces. A baseline cell has at most three: if both t2 and t3 types entered, their indices would be coprime; otherwise Z3/Z4 bounds same-type outliers beside the baseline. Therefore MSB's length<=4 interface is valid in EVERY cell.

Disjoint integer congruence classes supplied by MSB remain disjoint when enlarged to modulus d_i=gcd(lambda_i,6), because the pairwise gcd is unchanged. Counting in Z6 yields C6 and summing gives sum t_i/d_i<=7. All ordinary cofactors contribute1. A single carrier of both2 and3 can save at most5/6 and cannot offset the required deficit1; one prime carrier alone also cannot. Thus the two distinct exceptional owners E2,E3 are forced, with x=t_E2∈{1,3}, y=t_E3∈{1,2} and contributions1/2,1/3.

After removing the q exclusive ordinary-t1 cells, ordinary-t2 and ordinary-t3 cells cannot mix, and h2>=b,h3>=c,h0<=1. I reconstructed all three vacancy cases:

- h0=1 forces all other cells full and exceptionals into a single cell, impossible by their t counts or coprime denominators2,3.
- h2=b+1,h3=c forces E3 to use two d6 pieces in two ordinary2 vacancies; those exhaust all vacancies. E2 cannot fit as x1 (capacity7/6) or x3 (only two available cells).
- Thus h2=b,h3=c+1; E2 has x3 and exactly exhausts three ordinary3 vacancies. E3 must have y2 and occupy two of those cells. Both exceptionals are outliers; the four baselines are ordinary-t1, so at most two ordinary outliers remain. Three E2 cells force c>=2, hence b0,c2,q4.

This proves exactly the R4 three-hole incidence, not a realization of it.

### 4.3 Finite-image projection and |Q| dividing1008

Put N=core_G(W), Q=G/N≤S7, H=W/N. The action is faithful and transitive even if original G is infinite. Its7-adic group-order valuation is exactly1. Each image V_i has the same base-point orbit t_i<=3. If7 did not divide D_i=[Q:V_i], V_i would contain a7-cycle by Cauchy and hence be transitive, contradiction. Thus D_i=7d_i and

    c_i=n_i/D_i=r_i/d_i

DIVIDES the private cofactor r_i. In particular the c_i are pairwise coprime, including any possible private7-power. LemmaQ, read in structural-addendum-v1.md at actual hash `7b8200a58d43c0b53459a2a16fe1ffdc1f32c8ddce820c7a51d2f6193fee0b13`, proves that an overlap of projected cosets would force two coprime-index fibre cosets to meet in one N-coset. The projected eight cosets therefore really remain disjoint; mere projection of disjoint sets is not being assumed safe.

For each of the six ordinary vertices, D_i/7 can only involve the prime5, since it divides r_i, is coprime to6 and D_i divides7!. At least one of the two ordinary outliers C,D has D_i=7 by cofactor coprimality. Its subgroup K has an orbit3 and invariant complementary4, so its faithful action embeds K into S3×S4. Hence |Q|=7|K| divides1008. This excludes5, forcing all six ordinary indices to7. Baseline images are exactly H. The exceptional image indices are7·2^a and7·3^b; neither exponent can be0, since seven disjoint index7 cosets would already cover Q and exclude the eighth. Their stated exponent upper bounds follow from1008. The same three-hole incidence survives in the actual quotient.

## 5. Reconstruction of LemmaF and the Fano image

The seven blocks have constant point degree3 by transitivity and incidence count21. After the harmless permutation-image clarification in the MINOR, an order3 permutation stabilizing B0 has precisely the two cycle types listed.

With one3-cycle and four fixed points, fixed-block count is1 or4 modulo3. With one fixed block, the two moving block-orbits must each have a fixed F-pair and one B0 point. B0 points have six co-degrees1, whereas an F-point has one co-degree3, three1 and two0. Point-transitivity forbids the distinct profiles. With four fixed blocks, the three fixed triples in F leave three points at degree2, and the remaining orbit adds0 or3, never the required1.

With two3-cycles B0,C and fixed point g, only B0 can be a fixed block because fixed-block count is1 modulo3. Exactly one moving orbit contains g. Its B0-incidence a and the other's b satisfy a+b=2. The case(a,b)=(2,0) would make the second orbit the fixed set C. In(0,2), g has profile(2,2,2,0,0,0), while a B0-point has(2,2,1,1,0,0); the two C-points paired with that B0-point are distinct because sigma cycles C. This again violates point-transitivity. In(1,1), g has co-degree1 with all six points, so transitivity makes every pair co-degree1. Thus LemmaF is proved.

For K of index7, its3-orbit B0 has a stabilizer containing K. The stabilizer's index divides7 and cannot be1, so it equals K and has seven conjugate blocks. Their stabilizers are point-transitive on the triples by construction. LemmaF yields an ACTUAL invariant Fano plane, so faithful Q embeds in its automorphism group without any transitive-group database/classification.

## 6. GL3(2), parity, Sylow and the SAME-plane line cosets

The forced lines123,145,167,246,257,347,356 use every pair once and give the stated binary-vector model. A line automorphism is determined by images of an ordered independent triple;7·6·4=168 choices each extend to a unique linear map. Thus Aut(F)=GL3(2). Each elementary coordinate addition fixes three nonzero vectors and transposes two pairs, hence is even. These additions generate GL3(2), including swaps as products of three additions, so Q≤A7.

The two exceptional positive prime-power factors force42 to divide |Q|, while |Q| divides168; only42,84,168 remain. In orders42 and84, the Sylow7 count is1 because it divides6 or12 and is1 modulo7. A subgroup normalizing a7-cycle lies in its affine normalizer of order42 in S7; its even part has order21, since x↦−x is odd. Therefore Q≤A7 cannot have either smaller order, and Q=GL3(2), |Q|168. This is an elementary argument, not an assumption of simplicity.

Any3-orbit of the other index7 subgroup L is stabilized by L of order24. In this SAME Fano plane, noncollinear triples have orbit28/stabilizer6 under GL3(2); hence the3-orbit must be a line and L its full stabilizer. For the actual base point a=H, the R4 incidence gives |K·a|=|L·a|=3. Thus those actual orbit-lines contain a. Their cosets have point-image triples equal to the common hole set T, so T is a line. Being full set stabilizers, their cosets are exactly the sets mapping respective lines L1,L2 through a onto T. The lines must be distinct, or the cosets coincide.

## 7. Last line-coset contradiction and both orientations

For q(a)∈T, q^{-1}(T) is uniquely one of the three lines through a. This partitions the72 elements outside the four H-cosets into three full line-map cosets of size24. The two ordinary K/L cosets occupy two such parts; the complement of the six ordinary cosets is exactly xJ for the remaining line stabilizer J.

If an exceptional full left coset gV lies in xJ, write g=xj with j∈J; then jV⊆J implies V≤J. After translating by x^{-1}, the two exceptional pieces are actual left cosets inside J, of subgroup indices2^a and3^b. Coprime-index left cosets must intersect in ANY group, contradicting their disjointness. The R4 subcase is therefore excluded.

For any four original subgroup vertices, their generated subgroup has finite index dividing all four7r_i; their gcd is7, so its index is1 or7. The index7 case was excluded, leaving G. Inversion sends g_iU_i to g_i^{-1}(g_iU_i g_i^{-1}), again disjoint LEFT cosets with identical indices and unrestricted pairwise-coprime cofactors. The entire argument applies, giving the conjugated/inverted orientation without assuming common conjugation or normality.

## 8. Remaining target and review level

The result does NOT force a proper four-vertex join and therefore does NOT exclude P7. The exact remaining hypothetical geometry can have every four vertices generate G in both orientations. It is not shown to exist either. Existing no-subnormal/O_7'-minimal statements remain their own earlier imported/reconstructed claims; they are not an unrestricted Sun8 proof here.

This is a separate supplied-proof in-harness written reconstruction at the corrected observed pins: **0FATAL,0MAJOR,1MINOR** (a standalone-action wording issue with no effect on faithful Q). No executable finite classification, test suite, proof-assistant kernel, human review, external-model independence, novelty or publication acceptance is claimed. Historical internal S5/S7 statements and classical Z3/Z4/MS interfaces retain their stated trust boundaries. Parent must compose its own verdict. Reviewer returns to its one Kac–Moody four-cell problem; that slot's proposed assay remains NOT ADMITTED.
