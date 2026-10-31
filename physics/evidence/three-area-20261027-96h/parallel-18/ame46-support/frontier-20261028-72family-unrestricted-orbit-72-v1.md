# No product saturators and a full 72-support GL-orbit barrier for the interior phase families

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:31:19 PDT 2026`; not an exact completion clock. **WRITTEN author candidate** with exact source-data and finite controls described below. Independent scientific review is required before any adoption. This is neither a formal proof nor a global AME(4,6) minimum or novelty claim.

## 1. Claim

Let T be any normalized AME(4,6) tensor in the explicit E∪P∪P′ support and fixed-E gauge of [Pandya Eq. (3)](https://arxiv.org/html/2610.16673#S4.E3), with `|δ|<1` and phases satisfying the paper's AME mixed-block conditions. Thus all 72 source coefficients are nonzero: the 48 E coefficients are the signed Pauli coefficients of Table 1 divided by `√72`, while the 12 P and 12 P′ coefficients are nonzero. Equivalently for the proof, assume the E source facts and color-block support in §2, 2|2 unitarity, and nonzero P/P′ entries; no parametric phase classification is imported.

**Candidate A.** No normalized product vector φ has `|<φ,T>|=1/6`. Equivalently, no contraction of T with any pair of nonzero complex covectors has matrix rank one.

**Candidate B.** For arbitrary `V_0,…,V_3∈GL(6,C)`,

`support((V_0⊗V_1⊗V_2⊗V_3)T) ≥ 72`.                                (1)

Identity attains72, so the full local invertible and local-unitary orbit of every such source tensor has exact support minimum72. Generic nonunitary outputs need not be AME; only their support is considered. In particular the separately checked source with E/P/P′=`±1/1/i`, normalized by `√72`, is an explicit 72-support AME example in this class.

These are statements about the two published **interior phase families**, not all AME(4,6) states. The same paper's 60-support endpoints are different source tensors; (1) is not asserted at `δ=±1`. The global AME(4,6) support minimum remains unresolved.

## 2. Exact source and block facts

Let `H=span{|1>,|2>}` and `K=span{|0>,|3>,|4>,|5>}` on each party. Relabel the four K levels as in the dependency `frontier-20261028-unrestricted-orbit-60-barrier-v1.md`, SHA-256 `d21c734fa2830bf20e7330e118f03d3e1367f1794815c82162075c7df6dac251`. In this gauge:

- E consists of six sectors with H exactly at the active pair; the spectator K colors agree. For each active pair, the four 2×2 H matrices are, up to sign, exactly `I,X,Z,J=ZX`, one per color.
- P comprises all 12 even color permutations; P′ comprises all 12 odd permutations. Thus the 24 all-K positions are all four-color permutations.
- In each 2|2 cut, for any unordered pair `{a,b}` of input K colors and its complementary pair `{c,d}`, the ordered inputs `(a,b),(b,a)` and ordered outputs `(c,d),(d,c)` form one full 2×2 block; all four entries are nonzero. Since T is AME, the normalized block is unitary. There are six such blocks.
- No source term has one, three, or four H indices. All three 2|2 source flattenings are U/6 with U unitary.

The phase-independent support-block certificate `frontier-20261028-72state-block-isometry-v1.py`, SHA-256 `00a9c65d8be91f8f0ee8013eb97f12a9276995eb7af31a160101ec6dad15bf07`, checks all 18 all-K blocks and, for the special E/P/P′=`±1/1/i` state, all 3888 exact complex-integer entries of the three source Gram identities `F F†=2 I`; receipt SHA-256 `af5a829b5bf2711f7c0198383f910a3d7f7a35a41198c6d34f6e25a79cb4bce2`. Source table SHA-256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`; P′ coordinates are transcribed from the linked paper Eq. (6), and should be independently reconstructed. The separate signed-Pauli/color certificate and its source identities are listed in the dependency. The exact special-state Gram check is not a numerical validation of every family phase: general phases are covered here by the stated AME and nonzero-entry hypotheses.

## 3. Product saturation forces equal H masses

If a nonzero two-party contraction has rank one, normalize the two input covectors. Since the corresponding 2|2 source flattening is U/6, its output is a normalized product up to phase. After complex-conjugating the input vectors this gives a normalized four-party product φ with `|<φ,T>|=1/6`. Equality in the unitary Cauchy–Schwarz bound then makes the analogous product-to-product relation hold in **every** 2|2 cut. Conversely any such φ yields rank-one contractions. Complex conjugation does not change H/K masses or K probabilities.

Let

`h_i=||φ_{i,H}||²`, `p_i(g)=|φ_{i,K,g}|²`, `k_i=Σ_g p_i(g)=1−h_i`.

The elementary pure-H and pure-K rank arguments of `frontier-20261028-72state-one-restricted-party-orbit-barrier-v1.md`, SHA-256 `cd3eccbfd5e6efd67b7be594d5932a90392d14e1ea5fae0696906f24272bf536`, exclude pure H or pure K at any party of a product saturator. Thus `0<h_i<1`.

For distinct i,j,k,l, Pauli Hilbert–Schmidt orthogonality gives

`h_i h_j = Σ_g p_k(g)p_l(g)`.                                      (2)

The matched-color output `(g,g)` is fed only by an HH-input Pauli block. Cauchy–Schwarz and (2) give

`p_k(g)p_l(g) ≤ (1/2) h_i h_j = (1/2) Σ_t p_k(t)p_l(t)`.       (3)

The support is invariant under simultaneous local parity `D` equal to −1 on H and +1 on K: E has two H entries and P/P′ have none. A product saturator and source unitarity equate the two-party parity expectations on either side of every cut. For `z_i=1−2h_i`,

`z_i z_j = z_k z_l` for all complementary pairs.                 (4)

If all z_i are nonzero, their magnitudes are equal and their sign product is positive. Four negative signs would give all h_i>1/2, impossible by (2) and `p_k·p_l≤k_k k_l`. Two negative signs would give two H masses a and two 1−a, with a<1/2; equation (2) would saturate `p_high1·p_high2≤k_high1 k_high2=a²`, forcing both K distributions onto the same singleton, contrary to (3). Thus all h_i are equal below 1/2 in the nonzero case.

If one z_i is zero, (4) forces at least three zeros. Four zeros likewise saturate `p_k·p_l≤k_k k_l` and contradict (3). Suppose exactly three vanish: `h_0=h_1=h_2=1/2`, `h_3=b∈(0,1)`. Then `p_i·p_3=1/4` for i=0,1,2, `p_i·p_j=b/2` for i,j among 0,1,2, and (3) gives `p_i(g)p_j(g)≤b/4`. Each such entry is at most 1/2. For `Q_g=p_0(g)+p_1(g)+p_2(g)`, sorting the entries and using the pair-product bound yields

`Q_g≤max(3√b/2, 1/2+b)`.                                        (5)

Indeed, if the maximum x is at most `√b/2` this is immediate; otherwise the other entries are at most `b/(4x)`, and the convex function `x+b/(2x)` has its maximum on `[√b/2,1/2]` at an endpoint. But

`3/4=Σ_g p_3(g)Q_g ≤ (1−b)max(3√b/2,1/2+b) ≤ max(1/√3,9/16)<3/4`,

a contradiction. The two scalar maxima occur at b=1/3 and b=1/4. Therefore

`h_i=h∈(0,1/2)`, `k_i=k=1−h`, `p_i·p_j=q=h²` for i≠j.          (6)

This equal-H result is also written in `frontier-20261028-72state-product-saturator-constraints-v1.md`, SHA-256 `4c7df8bd862d29580fa5a5671253a108c3c475a4972734493c7410a8cbf0a86a`; the argument above is repeated so that no prior review is presumed.

## 4. Color-pair conservation and column rigidity

For complementary party pairs ij|kl and complementary unordered color pairs `{a,b}|{c,d}`, unitary conservation in the corresponding all-K 2×2 block gives

`p_i(a)p_j(b)+p_i(b)p_j(a) = p_k(c)p_l(d)+p_k(d)p_l(c)`.       (7)

Fix a color g and sum (7) over its three partner colors. Using the common row sum k and pair inner product q from (6),

`k Σ_r p_r(g) − (k²−q) = 2[p_i(g)p_j(g)+p_k(g)p_l(g)]`.       (8)

The left side is independent of the party partition. Writing `x_i=p_i(g)`, the three pair sums on the right must agree. Their differences are

`(x_0−x_3)(x_1−x_2)=0`,  `(x_0−x_2)(x_1−x_3)=0`.

For four real numbers these equations force at least three to be equal. Write the four-entry column as `c_g` at three rows and `c_g+d_g` at at most one exceptional row `r(g)`; a constant column has `d_g=0`. Define

`D_i=Σ_{g:r(g)=i} d_g`,  `E_i=Σ_{g:r(g)=i} c_g d_g`.

Since all row sums are k, all D_i have one common value D. Also, for i≠j,

`p_i·p_j=Σ_g c_g²+E_i+E_j=q`,

so all E_i have one common value.

## 5. Rigidity of the probability matrix

We show that the complete 4×4 probability matrix must have the form

`p_i(g)=a+(b−a)Π_{ig}`, with a>0, b≥0 and Π a permutation matrix. (9)

### 5.1 Nonzero common deviation

If D≠0, every row must own at least one nonzero column deviation. There are only four columns, so there is exactly one per row and all four deviations equal D. Their weighted sums E_i are equal, hence all four baseline values c_g equal some a. The exceptional value is b=a+D. Nonnegativity gives b≥0. If a=0, distinct rows have disjoint singleton support and q=0, contrary to q=h²>0. Thus a>0, proving (9).

### 5.2 Zero common deviation: at most two affected rows

Now suppose D=0. An affected row must own at least two nonzero deviations, so at most two rows are affected. At least one row is unaffected and has E_i=0; therefore every E_i=0.

If two rows are affected, each owns exactly two deviations. For one row they are s and −s with s≠0 on columns a,b, and `E_i=0` makes their baselines equal, say c. Apply (8) to these two columns and subtract. Their column sums differ by 2s, while the right sides differ by 4cs; hence k=2c. Substituting in (8) for either column gives q=0, a contradiction. Thus two affected rows are impossible.

Suppose at most one row is affected. Three rows are the same nonnegative vector `c=(c_0,…,c_3)`; the fourth is `c+Δ`, with

`Σ_g Δ_g=0`, `Σ_g c_g Δ_g=0`.                                    (10)

For complementary color pairs `{a,b}|{c,d}`, (7) gives

`c_a Δ_b+c_b Δ_a = 2(c_c c_d−c_a c_b)`.                          (11)

At least two c_g are positive: otherwise the inner product of two identical rows is concentrated on one color, contrary to (3). If exactly two c_g are positive, choose a,b to be the two zero colors in (11), giving 0 equal to a positive number. If exactly three are positive, write a for the zero color and vary the positive b in (11): the resulting common value of Δ_a forces the three positive c values to be equal. Equation (10) then forces Δ_a=0, but (11) makes Δ_a>0. Therefore all four c_g are positive.

Set `u_g=1/c_g²`, `s_g=1+Δ_g/c_g`, and `C=∏_g c_g>0`. Dividing (11) by `c_a c_b` yields

`s_a+s_b = 2 C u_a u_b`.

The sum over the two complementary pairs is independent of the partition, so `u_a u_b+u_c u_d` is the same for all three pairings. The same difference-product argument as in §4 shows that at least three u_g, and hence three c_g, are equal. If all four c_g are equal, (11) makes all pairwise Δ sums zero, so Δ=0. If exactly three equal a and the fourth is b≠a, (10) forces the exceptional Δ to vanish; (11) for any two of the three equal entries forces each of their Δ values to be b−a, contradicting `ΣΔ=0`. Hence Δ=0 and the common row c is uniform. This is the b=a case of (9).

The classification (9) follows in every case. Equation (6) now gives

`h²=2a(a+b)`.                                                       (12)

## 6. Eliminate all b≥0

### 6.1 The case b>0

For any pair of parties i,j, the products `p_k(g)p_l(g)` at the four complementary colors equal `a²` twice and `ab` twice. Using the matched HH-to-KK Pauli entries and normalizing the H spinors `η_i`,

`|η_i^T Q_g η_j|²` equals `a/(a+b)` twice and `b/(a+b)` twice.   (13)

For each pair, the four Q_g are the same fixed Pauli set I,X,Z,J up to signs and transpose. Let `r_i∈R³` be the unit Bloch vector of η_i. Complex conjugation reflects its y coordinate but does not change the support of a Bloch vector. The four numbers `2|η_i^T Qη_j|²−1` are the four Hadamard sign sums of the three coordinate products, so:

- If a=b, all four overlaps are 1/2. All three products `r_{i,t}r_{j,t}` vanish for every pair. Four nonzero Bloch vectors cannot have pairwise disjoint nonempty supports in three axes.
- If a≠b, the four signed sums are `+γ,+γ,−γ,−γ`, where `γ=|a−b|/(a+b)∈(0,1)`. Hadamard inversion makes **exactly one** coordinate product nonzero for each pair, with magnitude γ. Thus the four nonempty Bloch-axis supports have pairwise intersection size exactly one.

Four subsets of a three-element set with pairwise intersection size one must share a common axis: otherwise, three of them would be `{x,y}`, `{x,z}`, `{y,z}`, and no fourth subset meets each in exactly one element. On the common axis, the four absolute Bloch components have pairwise product γ and therefore each equals `√γ<1`. Every Bloch vector has a nonempty remaining support, and these four remaining supports must be pairwise disjoint subsets of only two axes. That is impossible. Hence b>0 cannot occur.

### 6.2 The case b=0

Equation (9) says every party is missing exactly one K color, and those four missing colors `g_0,g_1,g_2,g_3` are all distinct. Choose any cut ij|kl and the unordered **input** pair `{g_i,g_j}`. Of its two ordered input products, `(g_i,g_j)` is zero and `(g_j,g_i)` is nonzero. The complementary **output** colors are `{g_k,g_l}`; output `(g_k,g_l)` is zero and `(g_l,g_k)` is nonzero. But the source 2×2 block connecting these pairs has all four entries nonzero, so it maps an input with exactly one nonzero component to an output with two nonzero components. Contradiction.

No case in (9) remains. Thus the hypothesized product saturator does not exist, proving Candidate A, subject to independent review.

## 7. Full orbit support

The source 2|2 unitary sends every nonzero product of two covectors to a nonzero matrix. Candidate A excludes rank one, so every such contraction has rank at least 2. For arbitrary invertible local maps, choose any C,B and their six output covectors each. The resulting 36 A,D slices have rank at least 2 even after the arbitrary invertible A,D maps. Their disjoint output coefficients therefore have support at least `36·2=72`. Identity gives 72, proving Candidate B.

## 8. Bounded controls and limits

`frontier-20261028-probability-rigidity-controls-v1.py`, SHA-256 `dbf8a3ee6a87d71d2896987d2d7584620c0bcbccfc3f7d2aec807420912f8f76`, checks integer probability matrices with row sums 2 through 8 against equal inner products, the per-color Pauli bound and all pair-sum equations: every accepted case has the normal form (9). It also exhausts 75 four-axis-support configurations with pairwise singleton intersections and finds all share an axis, and checks no four nonempty disjoint private supports fit in the remaining two axes. Its positive normal-form control passes and a pair-sum mutation is rejected. Receipt `frontier-20261028-probability-rigidity-controls-v1.json`, SHA-256 `cceb633bac84387a4bff9296abc53cd289568a4431705986606ef790612ca422`. These are finite exact checks, **not** the real/complex proof.

For the special δ=0 state, a separate exact F_5 diagnostic exhausted `183,082,032` projective covector pairs across all 12 ordered cuts and found no rank≤1 contraction; aggregate SHA-256 `cff522cb4cc795f7d92be0730d9a65a53e8679bed67f74df391d554332017e45`. Its field, scope and independent rank-predicate controls are detailed in the 72-support dependency. Finite-field absence does not imply absence over C; the claimed complex result is the written argument §§3–7 and needs independent review.

The global support minimum across **all** AME(4,6) states, and the existence or absence of an orbit outside these phase families with fewer than 60 terms, are not decided.
