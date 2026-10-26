# Supplied-proof reconstruction — AME thin axes, twisted officers and active profiles

Observed clock before creation: **2026-10-23T15:37:47-0700**. Reviewer **InfoSPR7**, info-2, temporarily performing the exact assignment in `peer-review-wave-eighteen-v5.json`. The common contract and full reviewer entry were read. Only this named output in the reviewer's own root is written. No scientific executable, arithmetic interpreter, solver, enumeration, compilation, tests, CLI delegation or nested agent was used.

## 1. Actual snapshots, read coverage and verdict

All four assigned hashes were independently observed and matched before reconstruction:

| Source in physics/.../parallel-18/ame46-support/ | SHA256 | Actual complete read |
|---|---|---|
| `two-thin-axes-exclusion-v1.md` | `7cfef4e5b07b4d24bab86e0fa0f6615c817a1b4569245731c357dae64c57b4b9` | all101 lines |
| `officer-holonomy-v1.md` | `8be8781d6d0f4a4b32e0ca6a108b028282431c5c42432368c25f8812a291d498` | all79 lines |
| `profile3333-exclusion-v1.md` | `5e1907bd1b0f60f19e32ac4d19287f7dc4b466de5dfff72cc81890c71a3cec27` | all128 lines |
| `active-slice-corollaries-v1.md` | `04b3ee1c19b7a6051cc91953ab3ce2933d846f9972e9417478363e9c16d1b68d` | all76 lines |

Required predecessor `thin-slice-obstruction-v1.md` was read completely, all153 lines; its observed hash is **`ba269009d0f352e9b9fed1967cead86b5594b9ddee6d822cd8190fc67c2bce4f`**, matching the author's explicit import. The complete40-line `selection-v1.md` was read, observed hash **`7de67a35b7402f47e88d6de0e86f650dbca141b31cecdd7a8a4f8948d0c0fea9`**. Line counts were observed by metadata-only `wc -l`.

The actual primary [Ball–Simoens, arXiv:2603.02334v1](https://arxiv.org/html/2603.02334v1) was opened at Definitions1–3 and Theorem6; its §4.3 import/computational boundary and final theorem assembly were also inspected. The author's saved raw HTML hash was observed as `a7dfc338bffac67f00b5360a9533882f7b1458ea6457a95ff8f79a8c4add8c9c`; no byte-identity between live rendered HTML and that saved file is claimed.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR mathematical defects found at the stated scopes and named external-theorem boundary.** The two-entirely-thin-axis exclusion reconstructs conditional on the explicitly imported Ball–Simoens Theorem6. The holonomy restriction, complete e=0 all-three-profile exclusion and active-slice consequences reconstruct directly from the displayed AME/unitarity conditions and written predecessor arguments.

This is ordinary in-harness supplied-proof reconstruction, not blind, different-model-family, formal/kernel, human or novelty acceptance. The external QLS6 theorem's full classification/computation was **not** independently replayed or re-proved. Parent reconstruction is separate. No unrestricted support lower bound is improved by this verdict.

## 2. Definitions and the complete predecessor interface

The selection's object is a normalized pure state in `(C^6)^tensor4`, with **all six** two-party marginals equal to `I36/36`, in an arbitrary product orthonormal basis and with arbitrary complex amplitudes. For `A=6psi`, the three flattenings `M_(12|34),M_(13|24),M_(14|23)` are36×36 unitaries. Their complementary density matrices are respectively `M M†/36` and `(M† M)^T/36`; the transpose is the correct column-index convention. Thus the exact two-party and off-diagonal coherence conditions, not one-body mixing or diagonal norms alone, are being used.

An officer coefficient has modulus1 in A. Every fixed pair-value line has squared norm1; an officer is therefore alone on every such line through it, and two officers cannot agree in two coordinates. Any officer-free line has at least two support entries: a single entry of norm1 would itself be an officer. If `t=|T|`, every flattening has t singleton officer rows and `h=36-t` officer-free rows. At `e=s-(72-t)=0`, `s=t+2h`, forcing every officer-free row and column to have exactly two entries. This holds for all six choices of fixed coordinate pair.

Two non-officer rows sharing a column must share a second: otherwise their inner product has exactly one nonzero complex term and cannot vanish. Since columns also have degree2, the resulting four entries form a **closed**2×2 block; no third row or outside column can attach.

For a local value a in coordinate i, its `6-d_(i,a)` officers cover that many distinct partner-coordinate values. The remaining `d_(i,a)` pair-lines have two entries each, so the non-officer slice contains exactly `2d_(i,a)` points, with each of its partner coordinates taking exactly d values twice. Deficit0 values support no non-officers. Deficit1 is impossible at e=0: those two slice points would agree in every other coordinate and hence be the same tensor position. Thus every positive deficit is at least2, as required in the profile consequences.

### Doubled-fiber theorem used by the thin-axis proof

For two levels a,b of coordinate i, a doubled fiber over a triple z has both coefficients nonzero and lies in N. In the flattening `ij|kl`, its column consists of precisely those two entries. Closed2×2 closure gives a unique partner z' with the same j-value and different k,l-values. A repeated j-value cannot occur on a third vertex because its row is already full. Distinct such triples cannot share two coordinates, since then four nonzero entries would lie on an exact-two pair-line. Hence each vertex has three **distinct** color neighbors, producing the claimed simple cubic3-edge-colored graph.

The fiber vector `v_z=(A_(a;z),A_(b;z))` has norm1, and adjacent vectors are orthogonal columns of a2×2 unitary block. In C² the orthogonal-complement ray is unique. Rays therefore alternate along every path; an odd cycle would make a nonzero ray orthogonal to itself. Each component is bipartite. Cubic degree gives equal part sizes and simplicity makes each part have at least3 vertices, so each component has at least6 vertices. It contributes that many distinct entries to each relevant local slice; since the slice has `2d` entries, both varying-coordinate deficits are at least3. This verifies the exact pointwise statement excluding a Hamming-distance-one support pair at a thin value, without support minimization or an old numerical lower bound.

The predecessor's module rotation uses one unitary on the actual two-dimensional local span, not separate row rotations. Its support-cost inequality also reconstructs: a component loses one nonzero per doubled fiber, other doubles do not increase, and each singleton can gain at most one. The subsequent orbit-minimal/support48 classification invokes the old lower48 theorem only for its own final corollary. That old executable certificate chain is **not a dependency of the four newly assigned proofs** and is not re-authenticated by this review.

### Self-contained no-AME(4,2) boundary

The predecessor supplies the needed elementary proof. For a purported normalized four-qubit AME state, let A_k be the sum of squares of weight-k Pauli expectations. Pair marginals give `A0=1,A1=A2=0`. Each triple has purity1/2 by its complementary maximally mixed qubit, so each exact triple contributes3 and `A3=12`. Global purity gives `A4=3`. Spin flip changes each weight-k coefficient by `(-1)^k`; the overlap with the original density matrix would be `(1-12+3)/16=-1/2`. It must instead be nonnegative, being the trace of a product of positive semidefinite matrices. This is a valid arbitrary-complex-state contradiction. No external no-AME4,2 proof or numerical tensor is needed.

## 3. Two entirely thin axes and the product-officer bridge

### Slice classification and cycle propagation

If coordinates3,4 are entirely thin and N is nonempty, their active value sets have size `k=h/2`, because every positive deficit is2 and the deficits sum to h. In a thin coordinate3 slice, the four N positions give four distinct binary triples in coordinates1,2,4, balanced2+2 in each coordinate.

There are exactly three unordered2+2 partitions of four points. If two bit-coordinate partitions coincide, those two bits have a fixed XOR and the third bit is free; the third partition cannot also coincide because the triples are distinct. Otherwise the three partitions are the three different ones and the third bit is XOR/complement of the first two. This proves the stated plane classification without a missing support pattern.

The plane free in coordinate4 contains a pair differing only in that thin coordinate, contradicting the doubled-fiber deficit consequence just reconstructed. The remaining three types have two entries on every fixed(3,4) pair-line: E differs in both coordinates1,2; P1 differs only in1; P2 only in2. The same classification applies at the coordinate4 endpoint. Thus the difference pattern determines the type at both ends of each edge.

The bipartite active(3,4) hole graph has degree2 at every vertex; it is a disjoint union of simple cycles of length2r, r>=2. Each connected component has one type. In an E component, the selected pairs of coordinate1 and2 values propagate unchanged across every edge, while the diagonal/opposite-diagonal choice alternates. Each of the two rows of a diagonal in `M_(12|34)` receives r nonzero entries. Its exact degree is2, so r<=2; hence r=2 and the component is K2,2.

The resulting eight entries lie in a2×2×2×2 subcube. In `12|34`, each selected row is full internally. In `13|24`, each selected(a,c) row is filled by the two entries given by the coordinate3 parity-plane slice, and the columns are filled by the coordinate4 slices; `14|23` follows similarly. Hence in all three cuts the4×4 restricted matrix has four internally full orthonormal rows and is unitary.

The normalization in the manuscript is correct: the restricted A block has squared norm4, so the restricted psi has norm squared4/36; multiplying by3 gives a normalized four-qubit vector omega, whose `2omega` flattenings are exactly the restricted A blocks. Both density matrices in each of the three cuts are `I4/4`, giving **all six** qubit marginals. The no-AME4,2 proof therefore excludes every E cycle, not merely an unnormalized or one-marginal proxy.

### Ordinary product QLS, not entangled officers

Every normalized column `w_cd=sum_ab A_abcd |a,b>` is now a product vector: a singleton column is computational product, and each two-entry column is P1/P2 and varies in only one of a,b. Factor it into **unit** vectors `p_cd tensor q_cd`, placing its arbitrary overall phase in either factor.

Column orthonormality gives

`<p_cd,p_c'd'><q_cd,q_c'd'>=delta_cc' delta_dd'`.

This alone would not prove that p,q are separate QLS. The manuscript supplies the missing bridge correctly. The diagonal blocks of four actual cross-pair marginals give

`sum_d |p_cd><p_cd|=I6`, `sum_c |p_cd><p_cd|=I6`,

`sum_d |q_cd><q_cd|=I6`, `sum_c |q_cd><q_cd|=I6`.

Each sum is exactly six unit rank-one projectors in a six-dimensional space. Its square synthesis matrix V satisfies `VV†=I6`, hence is unitary and has orthonormal columns. Thus every row and every column of each array is an ONB. The remaining original marginals12,34 are supplied by the row and column unitarity of `M_(12|34)`. All six original conditions have been accounted for, and no arbitrary phases or unequal two-term amplitudes were discarded.

The actual primary Definition1 is exactly this row/column ONB notion in C^6. Definition2 is exactly tensor-product entry orthogonality, whereas Definition3 separately permits entangled entries and corresponds to general AME states. The actual primary Theorem6 states: **“There does not exist a pair of orthogonal quantum Latin squares of order six.”** Its surrounding text explicitly distinguishes non-entangled ordinary pairs from the known entangled-officer solutions. Therefore the inferred p,q match the forbidden ordinary product pair, not the allowed entangled-officer object.

**Import trust:** I read that exact version's definitions, theorem interface, §4.3's real-or-complex orthonormal-representation algorithm boundary and final theorem assembly. The source uses a classification/computation for ten of twelve cases and a written treatment of the other two. I did **not** replay the algorithm, authenticate all of its input graphs, reconstruct its entire external proof DAG or perform formal verification. The two-thin theorem is supported at its stated **named external Theorem6 import boundary**, not as a new local proof of that theorem. The other three assigned claims do not need this import.

## 4. Officer counts and the holonomy result

The line norms imply for arbitrary e that N uses only active local values, every pair-line is occupied, and a hole cannot share a line with an officer. There are exactly h hole lines in every pair grid. If `v_i` counts active local values, counting officers in active singleton/pair grids gives

`sum_T c=6 sum_i v_i-4h`,

`sum_T binom(c,2)=sum_(i<j) v_i v_j-6h`.

For the all-three profile, `h=12,t=24,v_i=4`, so these are48 and24. The nonnegative integer polynomial `(c-1)(c-2)/2` has total0; hence c is1 or2 for every officer, and average2 forces every officer to have exactly two active coordinates. Every active value has three active hole neighbors in a partner alphabet of size4, leaving exactly one active officer neighbor. This defines the bijections F_ij and inverse maps. Each four-officer set T_ij projects injectively onto the other two binary inactive coordinates, hence uses all four pairs.

For three distinct active coordinate pairs ij,jk,ki, successive officers agree in one active coordinate and cannot also agree in the fourth inactive coordinate. Their binary inactive bits therefore flip three times. This proves `chi(H_ijk(a))=chi(a)+1`, with chi balanced2+2. A triangle holonomy has no fixed point, so its permutation type on four points is a4-cycle or2+2 transpositions. Coherent equal-color identifications would make all such triangle maps identity and are impossible. This uses no e=0 assumption, as the holonomy manuscript correctly states; it is a necessary officer-code restriction, not an exclusion of the full twisted profile by itself.

## 5. Complete all-three matching normal form and one-term contradiction

### Exhaustiveness of the allowed relabelings

Use the actual bijections F_12,F_13,F_14 to identify the active alphabets so they become identities. Label the common active alphabet by the two inactive bits of T_12, denoted(x,y). Every inactive bit flip and every active-symbol permutation is a local permutation of the six basis values and therefore preserves support and all AME marginals.

Officers sharing active value1 force

`T12: inactive3=x, inactive4=y`,

`T13: inactive2=z, inactive4=y+1`,

`T14: inactive2=z+1, inactive3=x+1`.

Both(z,y) and(z,x) must be bijections on the four labels. Equivalently z changes under either single-bit change, so `z=x+y+constant`; an inactive2 flip removes that constant.

At coordinate2, the same pair-bijection argument makes the inactive1 bit of T23 equal to `x+y+c2`, while that of T24 is its complement. Flip inactive1 to remove c2. At coordinate3 the independent coordinate pair is `(y,x+y)`, forcing the inactive1 bit of T23 to be `x+c3`. At coordinate4 the corresponding pair is `(x,x+y)`, forcing the inactive1 bit of T24 to be `y+c4`. These are the explicit balanced-bijection meanings of the binary independence language; no probabilistic, phase or enumeration hypothesis is needed.

Matching the two descriptions of each same officer gives exactly

`F23(x,y)=(x+y+p,y+1)`,

`F24(x,y)=(x+1,x+y+q)`,

`F34(x,y)=(y+r,x+r+1)`, `p=c3`, `q=1+c4`, `r=p+q`.

I independently checked the endpoints: F23 equates inactive4 and1; F24 equates inactive3 and1; F34 equates inactive2 and1. Conjugating all four active alphabets by `(x,y)->(x+q,y+p)` changes the constant parts of these three affine maps respectively to `(0,1),(1,0),(0,1)`, while the three identity F_1j maps remain identities. Thus no genuinely twisted matching case is discarded. Later use is only of the transformed maps, so there is no need to assume the earlier inactive-bit formulas stay identical after that translation.

With labels0=(0,0),1=(1,0),2=(0,1),3=(1,1), the resulting tables are indeed

`F23: 2,3,1,0`, `F24: 1,2,3,0`, `F34: 2,0,3,1`.

### Forced lines and arbitrary-complex orthogonality

N lies in the active four-value alphabets and avoids every officer pair. In this normal form that is precisely the six **necessary** inequalities(*) in the manuscript; no sufficiency for AME is inferred.

The hole line12=(3,0) allows only `c in{0,1}`, `d in{0,2}`. The F34 restriction removes d=2 when c=0 and d=0 when c=1, leaving only

`X=(3,0,0,0)`, `Y=(3,0,1,2)`.

At e=0 the line needs two nonzeros, so both are present and that flattening row has precisely the columns(0,0),(1,2).

Line34=(1,2) is a hole because F34(1)=0. The remaining necessary restrictions allow only `a,b in{0,3}`, `a!=b`, so its two possible rows are(3,0),(0,3). The second coefficient `Z=(0,3,1,2)` is therefore also nonzero. The entry(0,3,0,0) is forbidden by `c=a` under F13=id. Row(3,0) has no other column, so its inner product with row(0,3) is exactly the single nonzero complex product `A_Y conjugate(A_Z)`, contradiction.

This derives a complete exclusion of the stated all-three/e0 profile, rather than merely excluding the coherent matching ansatz. It relies on neither the external QLS6 theorem nor a hidden support enumeration. The theorem retains its literal e=0 restriction here; I do not promote its scope beyond what was assigned.

## 6. Local moment consequences and exact residual profiles

For an active value a in coordinate i, with deficit d and `S_i=sum_(j!=i)v_j`, counting its active officer neighbors gives

`#officers at(i,a)=6-d`,

`sum_(x in T, x_i=a)(c(x)-1)=S_i-3d`.

The second identity is a direct sum of the three partner counts `v_j-d`; it does not require an old computational C3 certificate. If every officer has c=2, this gives `d=(S_i-6)/2`. If c is2 or3, it gives exactly

`S_i-12<=d<=floor((S_i-6)/2)`.

For `h=12,t=24,v=(4,4,4,4)`, the global moments are48,24. The same nonnegative polynomial forces all officer weights to be2, and each S_i=12 then forces **every** positive deficit to equal3. Thus the complete four-active-values-per-coordinate support48/e0 stratum reduces to the profile just excluded. This is not an assumption about its initial deficits.

The two residual calculations also reconstruct:

- For `(4,4,4,5)`, the moments are54,36 and the total of `(c-2)(c-3)/2` is0, so weights are2 or3. The four-value coordinates have deficits3,3,3,3; the five-value coordinate has3,3,2,2,2. The weight counts are18 of weight2 and6 of weight3.
- For `(3,5,5,5)`, moments60,48 give the same2/3 weight restriction. The three-value coordinate has4,4,4; the other coordinates each3,3,2,2,2. There are12 officers of each weight.

Here positive deficits are at least2 by the exact-two slice argument in §2. The displayed local upper bounds and sums to h=12 force the listed profiles without omitting another integer possibility. These last two strata remain **residual obligations**, not exclusions, exactly as the author says.

## 7. Final scope and trust ceiling

The four proofs preserve arbitrary complex coefficients, all original two-party marginal conditions, literal e restrictions and actual local basis relabelings. The two-thin proof excludes ordinary product-officer QLS through its exact external theorem interface and never rules out known entangled-officer AME4,6 states. The all-three normal form genuinely retains the twisted maps rather than replacing them with coherent diagonals.

No claim `48->49` follows. Other active-size/deficit profiles and the necessary e>0 support48 strata remain outside the proved exclusions. The documented48..60 baseline was read as a historical interface in the selection, not independently re-certified here; no old finite lower-bound program or60-term witness was replayed. Parent acceptance, complete external-theorem authentication, formal/kernel verification and novelty remain separate gates.

The assigned bounded reconstruction is complete. The reviewer returns to the owned robust-SPR7 problem/review gate; this temporary assignment does not create another counted primary problem or a reviewer-only slot.
