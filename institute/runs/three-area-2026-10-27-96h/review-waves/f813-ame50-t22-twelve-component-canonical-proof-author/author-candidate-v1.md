# Every actual twelve-word component: canonical complex gadget

**Status.** NONBLIND GENERAL AUTHOR written reconstruction, not an automatic disposition. Conditional on one actual normalized complex AME(4,6) tensor with exactly 50 nonzero coefficients and exactly 22 coefficients of modulus one after multiplying by 6, every 12-word residual agreement component has the canonical support and the complete arbitrary-complex-amplitude form in Theorem 1 below. This is a universal necessity statement about every such component, not an assertion that any such tensor exists. The converse is a **local partial-unitary** construction only. It does not complete P, the other 16 residual words, or an AME tensor. No global support-50 exclusion, novelty, source-identity, human, independent-family, kernel, or parent-verification claim is made.

## 1. Exact physical interface and imports

The mathematical inputs are the six complete, nonblind source bodies in the one frozen literal packet, identified in Section 7. In particular, S1 states the claim being independently reconstructed, S2 and S3 describe the common-tensor interface, S4 gives the exact global phase-interface disposition, S5 records the incumbent component/alphabet scope and expressly leaves S1's stronger 12-word claim unadopted, and S6 records a local finite check. S6 is not a proof of the universal classification and is not used as such here. The proof of Theorem 1 below reconstructs its needed unitary and incidence facts; it does **not** assume the S1 classification. The global completion discussion invokes the S4 integer-kernel interface explicitly. None of the listed status/permission controls supplies a mathematical premise.

Fix a single local orthonormal product basis and write U=6ψ. In each balanced cut U is a 36-by-36 unitary. Let P be its 22 modulus-one words and E its other 28 nonzero words. In every cut a P entry is an isolated unitary singleton. Removing the P rows and columns leaves a 14-by-14 unitary with 28 entries. No residual row or column has degree zero; degree one would contain a modulus-one entry, contrary to membership in E. Thus every residual degree is two. A connected bipartite degree-two support is an even cycle; a cycle longer than four has two rows with exactly one common nonzero column, so their inner product cannot vanish. Consequently every cut consists of seven full 2-by-2 unitary blocks. These are three flattenings of the **same** physical words and amplitudes.

It follows that each physical pair value appearing in E has exactly two extensions in E, and no P word has that pair value. Define an agreement edge between distinct E words sharing at least two physical coordinates. For each physical pair the two extensions are agreement-adjacent, so every agreement component is closed under the corresponding pair mate. In each complementary cut its words partition into four-word squares. Distinct agreement components therefore have disjoint physical pair projections.

Let C be any agreement component with |C|=12. For a symbol x used by C in party i, let n_i(x) be its number of C words and d_ij(x) the number of its distinct neighbors at party j. Closure under pair mates gives

    n_i(x) = 2 d_ij(x)   for every j != i.

Thus d_ij(x) is independent of j; call it d_i(x). It is at least two: if d_i(x)=1, x has only one neighbor in each of the other three parties, so at most one distinct word contains x, contradicting n_i(x)=2. For each party, summing gives sum_x d_i(x)=6; hence it uses at most three symbols. Each pair projection has exactly six values, so each party uses at least two symbols and no two parties can both use only two. The only possibilities, up to party permutation, are 3333 and 2333. All ternary-party degrees are 2; the binary-party degrees, when present, are 3.

## 2. The pure-incidence exclusion of 3333

Suppose all four C alphabets have three symbols. Every pair projection is a bipartite graph on 3+3 symbols with all degrees 2. Its three missing cells form a perfect matching. Every chosen 2-by-2 rectangle contains a missing cell: the two missing columns associated to its two rows are distinct, and every two-column subset of a three-column set meets them.

Fix a symbol a of one party. Its four words use exactly two symbols, twice each, in every other party. Each of those three coordinates defines a balanced partition of the four distinct words into two pairs. If any two of these partitions were distinct, all four intersections would be singletons, and all four cells of the corresponding 2-by-2 pair rectangle would occur. This contradicts the missing-matching observation. Thus all three partitions coincide; the other three coordinates then take only two different triples, each twice. That would repeat a four-coordinate word, impossible for the support of a tensor. Hence **3333 cannot occur**, without any phase, equal-modulus, or finite-enumeration assumption.

## 3. The actual 2333 product and six-triple graph

Let D denote the binary party, and A,B,C the ternary parties. In each ternary pair, the six used cells are a 3-by-3 array minus a perfect matching. In every D-versus-ternary pair, all six cells occur.

Fix a symbol a of A. Its four words give balanced 2+2 partitions by B and by C. Distinct partitions would fill a prohibited 2-by-2 rectangle in the B,C graph; hence they coincide. The two resulting B,C pairs each occur in two distinct words. Since D has exactly two possible values, each such pair occurs once with each D value. Doing this for every a proves, with no choice of amplitudes,

    C = T x {0,1},                                           (1)

where T consists of exactly six distinct A,B,C triples. Each ternary symbol occurs in exactly two triples. No two triples share two coordinates: otherwise their common physical pair would have four C extensions, contradicting the actual two-extension condition. These conclusions are properties of the given physical component, not independent per-cut constructions.

Construct a graph G on T by joining two triples when they share a ternary coordinate. Each vertex has one neighbor for each of A,B,C; the three neighbors are distinct because no two triples share two coordinates. Therefore G is a simple cubic graph on six vertices. Its edge colors A,B,C are three perfect matchings.

For an edge t,t' sharing A=a, write t=(a,b,c), t'=(a,b',c'). The pairs (b,c) and (b',c') differ, and the actual AD|BC square is

             columns (b,c)  (b',c')
      D=0        U_t0          U_t'0
      D=1        U_t1          U_t'1 .                    (2)

Write U_td=sqrt(p_td) z_td, with 0<p_td<1 and |z_td|=1. The two column and two row norms in this square imply p_t0=p_t'1, p_t1=p_t'0, and p_t0+p_t1=1. Orthogonality then cancels the common **positive** factor sqrt(p_t0 p_t1) and yields

    z_t0 z_t'1 = - z_t1 z_t'0,
    r_t := z_t0/z_t1 = -r_t'.                              (3)

The same conclusion holds for a B- or C-colored edge in its corresponding actual cut. Every r_t is nonzero; a walk around an odd cycle would give r_t=-r_t. Thus G is bipartite, for **all** nonzero complex moduli and phases. This uses phase ratios, not the generally false unnormalized identity U_t0 U_t'1 = -U_t1 U_t'0 when the two opposite magnitudes differ.

A cubic bipartite graph has equally large color classes, and six vertices give three vertices in each class. Every vertex is adjacent to all three vertices of the other class. Therefore G=K_3,3. Within either class no two triples share an A, B, or C symbol; with three triples, each class contains each ternary symbol exactly once.

## 4. Canonical support and all complex amplitudes

Relabel A,B,C independently and index one bipartition class by its A coordinate so that

    L_i = (i,i,i),                 i in Z/3.

Index the other class by its A coordinate: R_i=(i, beta(i), gamma(i)). Each of beta and gamma is a permutation of Z/3. Neither fixes i, because R_i and L_i already share A and cannot share a second coordinate. The only fixed-point-free permutations of three symbols are the two opposite 3-cycles. They cannot be equal: otherwise R_i and L_beta(i) would share both B and C. Interchanging the names B and C if needed gives the canonical form

    R_i = (i,i-1,i+1),             i in Z/3.               (4)

This is a classification under physical party and symbol relabelings, not a restriction to a chosen example.

**Theorem 1 (complete amplitude form).** After those relabelings, every coefficient in the actual 12-word component, and every possible nonzero amplitude pattern making just this component a partial unitary in all three cuts, is exactly

    U_(L_i,0) = sqrt(p)     v_(L_i),
    U_(L_i,1) = sqrt(1-p) eta v_(L_i),
    U_(R_i,0) = sqrt(1-p)   v_(R_i),
    U_(R_i,1) = -sqrt(p) eta v_(R_i),                      (5)

where 0<p<1, |eta|=1, and the six v_t are arbitrary unit phases. Choosing the other bipartition as L merely changes this parametrization. These v_t are phases of individual triples; no unsupported claim that they all arise from local-party gauge transformations is needed.

*Necessity.* Along every G edge, the square norms give p_t'0=1-p_t0, while the two D entries of each triple obey p_t0+p_t1=1. Connectedness of K_3,3 therefore gives the displayed alternating p and 1-p. Equation (3) gives one common phase ratio on L and its negative on R. Set v_t=z_t0 and eta=z_L1/z_L0; the displayed phase signs follow for every vertex. There is no assumption that p=1/2.

*Local converse.* For each ternary symbol there is one L triple and one R triple having that symbol. In the cut pairing that ternary party with D, the corresponding active square, after possible transposition, is

      [ sqrt(p) v_L          sqrt(1-p) eta v_L  ]
      [ sqrt(1-p) v_R       -sqrt(p) eta v_R    ].       (6)

Its row norms are one and its row inner product is zero, so it is unitary for every parameter in (5). There are exactly three disjoint such squares per cut. The canonical six triples have distinct values in each ternary pair, so there are no additional active rows or columns. Taking all other tensor entries to be zero makes a partial tensor with a 6-by-6 active block and 30 zero rows and 30 zero columns in every 36-by-36 cut. Thus (5) is both necessary for an actual component and sufficient for this **local** partial-unitary gadget. It is not a full unitary flattening, P completion, 50-word witness, or AME state.

The agreement graph on the 12 actual words is exactly K_3,3 square K_2: for distinct triples a horizontal edge occurs precisely when they share one ternary coordinate and the same D value, and the two D values over one triple form a vertical edge. Distinct triples cannot share two ternary coordinates, so there are no additional agreement edges. The graph is connected. The three ternary-pair mate involutions all flip the vertical D coordinate; the three D-versus-ternary mate involutions are the three horizontal colored matchings.

## 5. Why the complex phase argument is essential

The preceding bipartiteness is not a consequence of the two-extension and square-support incidences alone. As a fully explicit local negative control, take six triples in A,B,C:

    t0=(0,2,0)   t1=(0,0,2)   t2=(2,0,0)
    s0=(1,2,1)   s1=(1,1,2)   s2=(2,1,1).

Each symbol appears twice in each ternary coordinate; distinct triples share at most one coordinate. Their shared-coordinate graph consists of the triangle t0-t1-t2-t0, the triangle s0-s1-s2-s0, and the three edges ti-si. Taking their product with the two D values gives six pair values, each with two extensions, in every physical pair, and three complete 2-by-2 support squares in each cut. But (3) around the first triangle gives r_t0=-r_t0, so **no** choice of nonzero complex amplitudes, flat or nonflat, makes all those squares unitary. This is an incidence-only counterexample to skipping the phase step, not an actual 12-word component or a global witness. It was derived in writing; no executable or solver was run.

## 6. Completion boundary and remaining actual cases

The classification is conditional on an actual component. It neither constructs nor excludes the accompanying 16-word component or the 22 P words. In the split case a complete common physical realization still requires:

1. Another **connected** set E16 of 16 actual four-coordinate words, whose six pair projections each have eight values occurring twice, disjoint from the six corresponding projections of C; its three cut supports must consist of four actual squares each.
2. One set P of 22 actual words, with pair projections injective, disjoint from the 14 values used by C union E16, and hence exactly the 22 complementary values in **each** physical pair. These are the same P words in all pairs, not independently chosen matchings.
3. A simultaneous nonzero phase assignment on E16 satisfying its 12 cut-indexed square equations. The canonical component's nine equations are paid by (5), but its phases do not pay E16's equations. Equivalently, using the S4 interface, every integer left-kernel vector of the 12-by-16 signed square matrix for E16 must have even coordinate sum. In this equivalence the square rows and word columns are physical, and the integral, not merely mod-two, kernel is required. A valid phase assignment permits flat E16 moduli; any allowed arbitrary moduli may instead alternate on its bipartite components or be forced to one-half by an odd cycle. The singleton P phases are arbitrary.

Conditions 1–3 are the split-branch completion problem, not a claim that a solution exists. The full 28-word connected case is also open in this return. The S5 necessary global profiles are 3566, 3666, 4456, 4466, 4555, 4556, 4566, 4666, 5555, 5556, 5566, 5666, and 6666. S1 makes separate connectedness claims for the first three; those claims are outside this assignment and are **not** adjudicated here. Consequently this return does not eliminate the split branch for any global profile by itself, and does not decide any connected case.

Two further necessary completion constraints follow directly from the actual canonical gadget and may help keep local and global statements distinct. Let A0,B0,C0 be its three ternary alphabets, and D0 its two binary symbols. All pairs in A0 x D0, B0 x D0, C0 x D0 are already exhausted by C. Thus any P word, or any E word outside C, whose D symbol lies in D0 must have all three ternary coordinates outside A0,B0,C0. If a P word or an E word outside C has all three ternary coordinates inside A0,B0,C0, its three ternary pair values must instead avoid the six gadget values. In the labels (4), the only such triples are

    H_i=(i,i+1,i-1),  i in Z/3,

and its D value must be outside D0. At most one P word can use each H_i, by P-pair injectivity. These are necessary conditions only: they do not assert that any H_i is used or that any P/E16 completion exists.

## 7. Actual coverage, sequencing, and limits

Before packet body access I read the complete f813 manifest, freeze receipt, final pre-dispatch binding, parent live metadata, actual dispatch receipt, and all 22 manifest-listed controls through their endings. The controls were status/permission only; all genuinely held episodes and **every** consumer remain NONINPUT. I sent Main the direct PREBODY ACK naming the 22 controls and the single ordered 536-LF part and affirming no body, mathematics, or mathematical comparison. Only afterwards I read the sole part serially RAW in windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, 321–340, 341–360, 361–380, 381–400, 401–420, 421–440, 441–460, 461–480, 481–500, 501–520, and 521–536, through the ending and with complete long lines, before research. No sequence or presentation fault is known. The global memory summary and applicable research/acceptance skills were read first, as process guidance, not mathematical evidence.

The manifest-declared packet-part SHA-256 is `36e9a77bfe0386c2f8d1c0c4782e82c70acb5ed3bf274a7c8cf76039f67bcd37`. Its complete source bodies, declared hashes and actual covered source LF ranges are:

- S1, `review-waves/f805-ame50-t22-binary-box-and-incidence-author/author-candidate-v1.md`, 1–141, `edbe988b6c814550d84bce78f3fef8b132c07b47af75307b990303dc953696fe`.
- S2, `review-waves/f786-ame50-t22-same-complex-tensor-author/author-candidate-v1.md`, 1–143, `14c09bbaf27bbf57d77cfd4bba0225c693834a531371ec1c9eb0bc241e01549c`.
- S3, `review-waves/f804-ame50-t22-phase-integer-kernel-author/author-candidate-v1.md`, 1–119, `12d2e4c748b290b60b9cbd332473d59dc6e6fd14aca6bb1dc682bdfc07641bec`.
- S4, `dispositions/physics-6-actual-AME50-t22-common-support-phase-integer-kernel-criterion-parent-v1.md`, 1–21, `85878560f5fb5cb5b60893aa774b1f961322f8ea10c79aef792c93264e8cd8f9`.
- S5, `dispositions/physics-6-actual-AME50-t22-binary-box-component-and-alphabet-frontier-parent-v1.md`, 1–16, `4ae01f3ce54accaff22bc43bffbad6008b8fbd46e210252ddfd6552417c016bb`.
- S6, `review-waves/f806-ame50-t22-exact-local-gadget-finite-author/parent-t22-local-v1-run-v1-receipt.json`, 1–70, `5e7dcce95218534c9548760142b480b874b374627c974c2db7d9b7a16bcbad30`.

Paths above are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h`. The hashes are declarations in the supplied records, not independently recomputed source identities or cognition certificates. Original source paths, linked files, sibling returns, old code and any held content were not opened. There was no scientific child execution, test, solver, CAS, compiler, build, lint, formatter, external-model CLI, network, Git, installation, or deletion. No finite source was assigned or created. This file is exclusively created with an administrative text-write operation; no scientific result is attributed to that operation. All new claims are written author claims pending independent scrutiny and a separate parent decision.
