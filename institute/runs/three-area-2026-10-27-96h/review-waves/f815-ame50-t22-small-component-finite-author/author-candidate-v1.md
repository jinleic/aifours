# Twelve-word component: exact local interface and bounded finite source

**Status.** Fresh nonblind GENERAL AUTHOR analysis and one newly prepared, immutable, **UNRUN** local finite source. All mathematical arguments and predicted counts in this note are author claims awaiting scrutiny; no output from the new source is reported. This is not a disposition. The only tensor under discussion is one common complex AME(4,6) tensor in one product basis, conditional on support `N=50`, `t=22`; P denotes its 22 unit-modulus words and E its 28 remaining words. The source does not enumerate any physical P set or complete a 28-word E support. The connected 28-word case, all actual support/phase completion questions, and the other ten surviving profiles remain open.

## 1. Exact input boundary

The complete literal packet part `literal-packet-part-01-v1.md`, declared SHA-256 `36e9a77bfe0386c2f8d1c0c4782e82c70acb5ed3bf274a7c8cf76039f67bcd37`, 536 LF, contains these complete bodies. The following hashes and lengths are the supplied administrative pins, not independently recomputed here:

1. S1 `review-waves/f805-ame50-t22-binary-box-and-incidence-author/author-candidate-v1.md`, 141 LF, `edbe988b6c814550d84bce78f3fef8b132c07b47af75307b990303dc953696fe`. Its stronger gadget and three-profile connectivity arguments are explicitly unadopted in S5; this note reconstructs them rather than treating their conclusions as an independent disposition.
2. S2 `review-waves/f786-ame50-t22-same-complex-tensor-author/author-candidate-v1.md`, 143 LF, `14c09bbaf27bbf57d77cfd4bba0225c693834a531371ec1c9eb0bc241e01549c`.
3. S3 `review-waves/f804-ame50-t22-phase-integer-kernel-author/author-candidate-v1.md`, 119 LF, `12d2e4c748b290b60b9cbd332473d59dc6e6fd14aca6bb1dc682bdfc07641bec`.
4. S4 `dispositions/physics-6-actual-AME50-t22-common-support-phase-integer-kernel-criterion-parent-v1.md`, 21 LF, `85878560f5fb5cb5b60893aa774b1f961322f8ea10c79aef792c93264e8cd8f9`.
5. S5 `dispositions/physics-6-actual-AME50-t22-binary-box-component-and-alphabet-frontier-parent-v1.md`, 16 LF, `4ae01f3ce54accaff22bc43bffbad6008b8fbd46e210252ddfd6552417c016bb`.
6. S6 `review-waves/f806-ame50-t22-exact-local-gadget-finite-author/parent-t22-local-v1-run-v1-receipt.json`, 70 LF, `5e7dcce95218534c9548760142b480b874b374627c974c2db7d9b7a16bcbad30`.

Paths above are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h`. Imports used are exactly the common physical pair/mate and cut-square conditions, the binary-box/component alternatives, alphabet and degree/moment conditions, and common complex phase interface in these bodies. The preceding S6 result is imported only at the local scope stated in that receipt. No prior finite source code or transitive source link was read.

## 2. Twelve words: from physical incidence to six triples

Assume the packet's actual-component interface: each pair value has exactly two E extensions in one component, every complementary pair produces four-word square orbits, and a used symbol occurs twice its common pair degree. Thus the 12-word component has six distinct values in each physical pair and local degrees summing to six in each party, with each used degree at least two. Its local profile is `3333` or `2333`.

**The `3333` fiber obstruction.** In each pair the 3-by-3 E graph has every vertex of degree two, hence is the full graph minus a perfect matching. Any selected 2-by-2 subrectangle meets that missing matching: the images of two chosen rows and two chosen columns cannot be disjoint inside a three-set. Fix one symbol at A. Its four words use exactly two values twice in each of B,C,D. Their balanced `2+2` partitions for B and C must coincide, since two distinct balanced partitions would realize all four selected B/C cells; likewise for B/D and C/D. If all three partitions coincide, the four words contain only two different BCD triples, contradicting word distinctness. This argument uses the actual common fiber and all the pair omissions, not a single-cut relaxation.

**The `2333` form.** Take A,B,C ternary and D binary. In the four-word fiber at any A symbol, B/C again have coinciding balanced partitions. Since the four physical words are distinct and D has only two values, each resulting ABC triple occurs with both D values. There are therefore exactly six distinct ABC triples T and E12 is exactly `T x {0,1}`. Every symbol in each ternary party appears in two triples; each AB, AC and BC pair projection is injective, because each resulting physical pair already has its two D extensions. Conversely, these six-triple conditions imply each of the six physical pair projections on `T x {0,1}` has six values, each with multiplicity two. For each physical cut the active 6-by-6 support is three `K_2,2` blocks: two triples sharing a ternary symbol and their two D values form one block.

The finite source separately enumerates four-triple fibers and all `C(27,6)=296010` subsets T. Its one-pair-only fiber mutation is a control, not a physical `3333` witness.

## 3. Signed graph and canonical phase gadget

Join two elements of T when they share a ternary coordinate. Each vertex has one neighbor per coordinate, and pair-projection injectivity prevents two vertices sharing two coordinates. The graph is simple cubic on six vertices. It is connected: a simple cubic component contains at least four vertices, so two components would require at least eight.

Each graph edge supplies a physical square with both D values. For the unit phases set `r_t=z_(t,0)/z_(t,1)`. That square equation is precisely `r_t=-r_u` on an edge `{t,u}`. Since the ratios are nonzero, any odd cycle is impossible. Conversely a bipartition allows `r_t` to be one arbitrary unit value on one side and its negative on the other; this satisfies all nine physical square equations. A simple cubic bipartite graph on six vertices has classes of size three and is `K_3,3`. Each class contains each symbol once in A, B and C: the edge of a given coordinate is a perfect matching between the classes.

After independent ternary-symbol relabelings, write one class as `L_i=(i,i,i)`, `i in Z/3`. The other class can be indexed by its A coordinate. Its B and C maps are fixed-point-free permutations of three symbols and must differ, since agreement in both B and C with one L would duplicate a pair projection. They are therefore the two opposite three-cycles. Up to exchanging B and C,

```
L_i = (i,i,i),        R_i = (i,i-1,i+1)     (mod 3).
```

Thus the bipartite six-triple supports are precisely the relabeling orbit of this gadget. Writing arbitrary unit phases `v_t, eta` and `0<p<1`, a local realization is

```
U_(L_i,0) = sqrt(p) v_(L_i)       U_(L_i,1) = sqrt(1-p) eta v_(L_i)
U_(R_i,0) = sqrt(1-p) v_(R_i)   U_(R_i,1) = -sqrt(p) eta v_(R_i).
```

The displayed form follows from the common edge ratios and alternating squared moduli; it supplies a partial tensor only. It does not supply the other 16 E words, the 22 P words, or a full state.

**Counts, derived expectations, not run results.** Among 6-labelled simple cubic graphs, complementation identifies the two 2-regular types `C6` and `C3+C3`; these give 60 triangular-prism graphs and 10 `K_3,3` graphs, respectively. The prism admits six labeled proper 3-edge-colorings and `K_3,3` admits twelve. A coloring assigns the physical coordinates A,B,C to the three perfect matchings; labeling the three matching edges in each coordinate gives `6^3` symbol assignments. Each physical triple set occurs six-factorial times under vertex labeling. This predicts `(60*6+10*12)*6^3/6! = 144` pair-compatible six-triple sets and `10*12*6^3/6! = 36` bipartite sets. There are 20 signed **labelled graph/sign pairs**, and 72 triple-set/sign pairs, because each connected bipartite graph has two signs. These counts have different underlying labeled objects and neither counts physical P completions. Complex phases form continuous families, so a sign count is also not a count of all complex phase assignments.

## 4. Exact P-cell accounting for the three profiles

All following inequalities are necessary conditions on the **same physical words**. For a party X and component C, denote its alphabet `X^C`. Pair values belonging to different components are disjoint. If X and Y have disjoint component alphabets, each cell of `X^12 x Y^16` is a P pair and requires a different P word. If Z also has disjoint component alphabets, then classifying those P words by their Z coordinate gives the bound

```
|X^12| |Y^16| <= (|Z^12||X^12|-6) + (|Z^16||Y^16|-8)
                  + |Z_unused| |Y^16|.                         (*)
```

The first two subtractions are exact counts of E pair cells within the component rectangles; pair injectivity bounds the numbers of P words using them. The last term bounds P cells with an E-unused Z symbol. The classes are disjoint because they have different Z alphabets. This is an upper bound, not an enumeration of P completions.

### `3666`

Every six-symbol-party degree is at most three, since it has the three-symbol partner; component alphabets there are disjoint because a common symbol would have component degrees at least two plus two. Each full alphabet is their union. If the 12-component is binary at the three-symbol party, take the other three parties as X,Y,Z in (*): the demand is `9` and the three capacities are `(3,1,0)`, giving `9<=4`, impossible. If the 12-component is binary at a six-symbol party Z, take the other two full parties as X,Y; the capacities are `(0,4,0)`, again `9<=4`. The global degree options at the three-symbol party are `(2,6,6),(3,5,6),(4,4,6),(4,5,5)`; at each full party they are `(2,2,2,2,3,3)`. Moment counts are `(n0,n1,n2,n3,n4)=(0,0,0,18,4)`.

### `3566`

Let A,B,X,Y have global alphabets 3,5,6,6. Their degree multisets are respectively `(4,5,5)`, `(2,3,3,3,3)`, and twice `(2,2,2,2,3,3)`. The only P cell inside `X_A x X_B` is the missing cell in the 3-by-5 E graph. The four outside-A/outside-B mask counts are `(both outside, A only, B only, neither)=(3,15,3,1)`: there are three unused A symbols, one unused B symbol, and each outside pair is P. The P moment vector is `(0,0,3,18,1)`.

At X,Y the component alphabets are disjoint. If the 12-component is binary at A, X and Y each split `3+3`. The 16-component cannot use two A symbols, because its two degrees would be four but its Y alphabet has size three. It uses all three with degrees `(2,3,3)`; the two binary-12 A symbols each contribute three, and the global maximum five would require both corresponding 16 degrees to be at most two, although only one is.

If the 12-component is binary at a full party X, then A is ternary in it and Y splits `3+3`. Again the 16-component must use all three A symbols. Relabel its 12-component A/B pair graph as `K_3,3` minus a matching. Any B symbol shared by the components then has only one A cell left for component 16, contrary to its degree at least two. Only the two B symbols outside the 12 alphabet remain, supplying at most six A/B cells, fewer than the eight needed. The source enumerates the eight-cell choices and includes a degree-one mutation to expose that exact obstruction.

If the 12-component is binary at B, its two B symbols cannot be shared, since their degree is already three and the global B maximum is three. Component 16 uses three other B symbols; one of the six physical B symbols is unused by E. In (*) choose Z=B and the two full parties as X,Y. The demand is nine and capacities are `(0,1,3)`, so `9<=4` is impossible.

### `4456`

Let A,B,C,D have alphabets 4,4,5,6. Moment counts are `(0,0,8,14,0)`. D is full, so every P word has one or two outside-alphabet coordinates among A,B,C. At each D value the unused A,B,C symbols give `2+2+1=5` P pair incidences, with at most two incidences per P word; there are at least three P words, hence `d_D<=3` and the degree multiset is `(2,2,2,2,3,3)`. For a D symbol of degree three, the three P words have two double-outside and one single-outside masks; for degree two, the four have one double-outside and three single-outside masks.

By P pair coverage, the double-outside masks `(AB,AC,BC)` have counts `(4,2,2)`. The outside marginal counts are `(12,12,6)` for A,B,C, so the single-outside counts are `(6,6,2)`. These are common-P-word incidence counts, not separately selectable matchings.

Each four-symbol party has global degree multiset `2444` or `3344`; C has `22244`, `22334`, or `23333`. The A/B graph has 14 E cells and two P holes. Two holes sharing a row yield ordered degree profiles `(2444,3344)`, sharing a column yield `(3344,2444)`, and sharing neither yield `(3344,3344)`. There are respectively 24,24,72 labelled two-hole placements; both parties cannot be `2444`.

If the 12-component is ternary at a four-symbol party, its three degrees there are two. Enumerating the 16-component alphabet sizes 2,3,4 and positive component degrees summing to eight, with the actual four-symbol union and global degree at most four, forces global profile `2444`: size two is impossible, size three has two shared degree-two symbols and one degree-four symbol, and size four has all component degrees two. Thus both A and B cannot be ternary in the 12-component, by the two-hole rule. The 12-component is binary at A or B. Its binary symbols have component degree three and therefore cannot overlap the 16-component under global degree at most four. The 16-component uses the two other symbols there, each of degree four, so it needs four symbols at D. But the ternary 12 alphabet and four-symbol 16 alphabet in the six-symbol D party overlap, giving degree at least four, contradicting `d_D<=3`.

The above is a conditional written exclusion of a `12+16` split in each of these profiles. It does not settle their connected 28-word cases. The other ten profiles remain unresolved here in both component alternatives unless separately decided.

## 5. UNRUN source, full finite coverage, and controls

`finite-small-component-v1.py` in this directory is the single new immutable source. It uses Python's standard library only, receives no data arguments, uses no input or output files and makes no network/subprocess calls. Intended invocation after full source review and a **separate** source-bound GO: `python3 -I -B -S finite-small-component-v1.py`, with an external parent tool deadline no greater than 55 seconds. It checks a cooperative internal monotonic deadline of 40 seconds; SIGINT/SIGTERM set a sticky stop flag. On a handled stop it returns `INCOMPLETE` rather than a mathematical pass; a failed reason control returns `FAILED`. An unhandled termination or broken output channel need not produce JSON. It prints one JSON result, explicitly recording completed sections and `physical_P_completion=NOT_ENUMERATED` with zero P candidates. Runtime, exit status, actual coverage, and JSON are not observed yet.

The intended complete-local finite scopes are:

* All `C(15,9)=5005` labeled edge subsets on six vertices, selecting simple cubic graphs; enumerate each graph's 64 possible sign vectors. Positive `K_3,3` and negative triangular-prism controls check the phase/bipartite reason. The signed graph count is not a P-completion count.
* All `C(27,4)=17550` distinct fibers in `[3]^3`, testing balanced `2+2` coordinate occurrences and the three deficient pair rectangles. A balanced fiber satisfying only one deficient-pair condition is an intended-reason mutation.
* All 296010 six-subsets T of `[3]^3`, checking balanced ternary symbols, all three injective ABC pair projections, actual `T x {0,1}` pair multiplicities, three cut decompositions, nine edge/square correspondences, and the phase-sign graph. Compare exactly with all independent ternary relabelings and ternary-party permutations of the canonical gadget. Controls include a duplicated AB pair, missing physical word and one flipped phase sign. The finite sign check is an exact consequence of the general complex-ratio argument above; it is not a claim that all phases must be signs.
* Exact moment vectors and degree multisets for `3566`, `3666`, `4456`; the three explicit cross-cell bounds in (*); the 4456 two-hole classifications and ternary-component degree vectors; the 4456 six-versus-seven-symbol disjointness control; and the 3566 binary-A relaxed-degree and binary-full-party degree-one mutations. This is a finite check of the stated necessary arithmetic and local cases, not an enumeration of physical P or 16-component realizations. The complete outside-mask accounting in Section 4 is a written derivation; the source specifically checks the underlying moments, fixed-D bound, and two-hole classes rather than independently enumerating all P-mask configurations.

A `COMPLETE_LOCAL` status would mean only that the source finished its bounded loops and its built-in controls passed under that particular run; it would still require a separately scoped review of source, inputs, output and mathematical import boundaries. No run has occurred and no such status is claimed here.

## 6. Actual process coverage

Before any packet body, I read the complete manifest, freeze receipt, final pre-dispatch binding, parent-live metadata supply and actual dispatch receipt, and every one of the 22 controls listed in `manifest-v1.json` through its ending. Controls were used for status and permissions only. All genuinely held episodes and every method/selection/planning/proof/verification/reporting/confidence/downstream consumer remain NONINPUT. I sent Main the direct PREBODY ACK naming those controls and the sole part's 536 LF, with no body, mathematics or comparison before the ACK. I then read part 01 serially as raw windows `1-20,21-40,41-60,61-80,81-100,101-120,121-140,141-160,161-180,181-200,201-220,221-240,241-260,261-280,281-300,301-320,321-340,341-360,361-380,381-400,401-420,421-440,441-460,461-480,481-500,501-520,521-536`, through the ending and complete displayed long lines, before research. No presentation or sequencing fault is known.

No scientific program, interpreter, solver, test, compiler, build, lint, formatter, external-model CLI or old code was run or opened; no linked/unlisted science, network, Git, installation or deletion was used. The source and this candidate are new file creations only. No P completion, physical support-50 witness, global exclusion or completion decision is asserted.
