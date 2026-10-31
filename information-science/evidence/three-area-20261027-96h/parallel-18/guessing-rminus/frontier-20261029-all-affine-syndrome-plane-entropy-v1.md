# Every binary affine syndrome plane has nonpositive entropy balance gap

## 0. Required source-first entry

Read the following corrections before their source consumers:

1. `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md`, SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`: the publisher's cross-branch omission is Remark 5.4, not 3.8. No publisher copy-LP upper bound is used in the present proof.
2. `frontier-20261028-mixed-plane-symmetry-erratum-v1.md`: the invalid exploratory mixed-plane permutation/script is NONINPUT. Only the checked four-factor certificates named below are imported.
3. `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md`, SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f`: a smaller local decoder does NOT follow from graph FDs alone. Here every local decoder is proved from ACTUAL component parities. Neither the withdrawn nor the repaired two-syndrome entropy theorem is an input.
4. `frontier-20261029-primal-checker-subset-coverage-erratum-v1.json`: old new-v1 primal coverage claims are withdrawn. This theorem uses exact dual identities and the independent RREF coverage bridge, not those primal receipts.

**Status: WRITTEN candidate theorem with exact independently checked coefficient identities and exact finite coverage, importing the stated earlier written proper-subgraph/four-factor/visibility arguments. The complete mathematical caller and all named imports await scientific review.** No proof-assistant formalization, novelty clearance, publication or scientific adoption is claimed.

**Frozen evidence entry.** `frontier-20261029-all-affine-syndrome-plane-entropy-evidence-v1.json`, SHA-256 `3064c76b7ae540e990f9dec22158a6bf609ed115209e39b265cda697cd49a62d`, pins all named certificate/checker/receipt and written-import bytes by scope. No held f161 review or parent assessment is included or consumed.

## 1. Exact setting and theorem

The original graph has vertices 1,...,10 and neighborhoods:

| v | N(v) |
|---|---|
| 1 | 2,3,4,5,6,7 |
| 2 | 1,3,7,9,10 |
| 3 | 1,2,4,8,9 |
| 4 | 1,3,5,8,10 |
| 5 | 1,4,6,9,10 |
| 6 | 1,5,7,8,9 |
| 7 | 1,2,6,8,10 |
| 8 | 3,4,6,7,9,10 |
| 9 | 2,3,5,6,8 |
| 10 | 2,4,5,7,8 |

This is the literal 26-edge R-minus graph transcribed from Fig. 2, printed p570, of the pinned Gurpinar 2024 publisher PDF (SHA-256 `373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8`). Edge 3-4 is present; 9-10 is absent.

Use these ten ordered triangle factors:

```
123, 145, 167, 239, 2-7-10, 389, 4-5-10, 4-8-10, 569, 678.
```

Each vertex occurs in exactly three factors. A word has one binary component at every triangle occurrence, so its space is F_2^30 and every vertex variable X_v is a three-bit tuple (alphabet q=8). Let sigma_t be the XOR of the three bits of factor t, and let sigma=(sigma_1,...,sigma_10).

**Theorem.** Let X be any finite joint law on this word space satisfying the original-neighbor FDs

H(X_v | X_(N(v))) = 0 for v=1,...,10.

If its syndrome support is contained in an affine subspace of F_2^10 of dimension at most two, then

H(X_V) <= (2/3) sum_v H(X_v).

Probabilities and correlations are arbitrary. The support can be any subset of the affine plane; it need not be uniform, linear, maximal or a full union of cosets.

Consequently, within this support class:

- H(X_V) <= (20/3) max_v H(X_v);
- a uniform FD support has at most 2^20 words;
- no nonuniform reweighting supplies an entropy-ratio gain over 20/3.

The uniform word-count conclusion was already obtained in the predecessor plane-transversal result. The new conclusion is the arbitrary-law entropy inequality. It does not establish the unrestricted R-minus guessing number.

## 2. Reduction to selected-factor fibers

It suffices to treat a two-dimensional affine plane: an affine point or line extends to one. Write its syndromes as sigma=s0+A*a+B*b, with a,b independent binary direction vectors and S=(A,B). Each factor is either fixed or has parity equal, up to a fixed offset, to one of A,B,A+B. Call these three colors 0,1,2 and let J be the nonfixed factors.

Condition on the complete tuples of all fixed factors. In any positive-probability fiber, let Y_v be the tuple of selected J-components at v. The original graph FDs persist: conditioned components are constants supplied to the original decoder. The selected parities determine S, because the direction map is injective. Thus H(S|Y_V)=0.

All the following premises hold for these actual variables:

- A functional l_c is determined by each selected triangle carrying color c.
- The graph FD reconstructs Y_v from its neighbors; those neighbors also contain the other two components of each triangle at v. Therefore each incident functional is known from Y_(N(v)). Two distinct functionals determine S.
- Given S and Y_(L_J(v)), with L_J(v) the other vertices of the selected triangles through v, every component at v is recovered by its XOR equation. Hence H(Y_v|Y_(L_J(v)),S)=0. This is an actual component decoder, not a deduction from a smaller graph neighborhood.
- Each functional is a function of S. Two distinct nonzero functionals jointly determine S. The data-processing and pair-determination rows of the functional certificates follow from these deterministic relations and ordinary CMIs.

### The new finer local decoder

If the nonempty set of selected incident colors at v is the singleton {c}, S contains unnecessary information for this local decoder: all incident parities are known from l_c alone. Therefore

H(Y_v | Y_(L_J(v)),l_c) = 0.

The proof solves each incident component as the XOR of its other two components and its known affine parity, then concatenates the recovered bits. This holds with arbitrary probabilities. The predicate MUST be recomputed from the coloring and must be exactly a singleton; it cannot be asserted at a vertex with two or three incident colors.

This load-bearing observation is `frontier-20261029-single-functional-local-decoder-lemma-v1.md`, SHA-256 `77679e92b2927373e288cd5c91c647d43f606136273079bda649a89435984c61`. The earlier coarse relaxation imposed the local decoder only given the whole S. Its twenty positive abstract profiles violate this finer actual decoder; they were never actual coding laws.

### The full-state factor gate

Given S, all selected factor parities are fixed. For any ordering of the selected factors, any two bits of each factor determine its third even after conditioning on the earlier factor tuples. Pairwise entropy subadditivity gives 3H(Z_t|S,past) <= 2 sum_(v in t) H(X_v^t|S,past). Replacing all-past conditioning on the right by each vertex's own past components can only increase it. Summation and the chain rule give

3H(Y_V|S) <= 2 sum_v H(Y_v|S).

Since S is determined by Y_V, this is exactly

G_S = 3H(Y_V)+17H(S)-2 sum_v H(Y_v,S) <= 0.

This is the ONLY imported entropy gate in the new residual identities. There is no gate obtained by conditioning a Delta theorem on A, B or A+B, and no two-syndrome entropy theorem, DFZ inequality or numerical entropy cap on S is used.

## 3. Exact coverage of every direction plane

There are (1023*1022)/6 = 174251 binary two-dimensional direction subspaces. The independently replayed, disjoint case split is:

| Category in the proof | Direction planes |
|---|---:|
| J misses a graph vertex | 20,993 |
| J covers and has exactly four factors | 247 |
| Full-model visibility criterion applies | 145,248 |
| One of the 219 checked mixed-visibility identities applies | 5,858 |
| Residual functional colorings | 1,905 |
| Total | 174,251 |

**Noncover import.** A selected vertex outside the factor union is constant. The nine-active proper-subgraph inequality gives nonpositive gap for the conditional selected law. Its k=1 case has a three-color reconstruction proof; k=2,3 have exact integer Shannon/FD identities, and the checked eight-element graph group transports them to all vertices. The written import and all exact certificate/checker/receipt bytes are in the evidence manifest's `proper_subgraph` group.

**Four-factor import.** The existing complete four-factor theorem covers every four-varying-factor plane with arbitrary probabilities: 206 color-reconstruction cases, 13 visibility cases, and the last 28 planes in seven checked orbits. Only the final exact checked certificates are used; the known invalid exploratory symmetry script is excluded. Dependencies are in `four_factor`.

**Full visibility import.** Put W={v: the incident selected parity projection is injective on the direction plane}. The archived full-model certificates suffice when W contains one of {6}, {7}, {2,5}, {9,10}, {1,2,10}, {1,5,9}, {5,8,9}, {2,8,10}. Their FD premises hold for the selected law: its stronger local set L_J(v) is contained in the full local set, and the visibility argument above recovers S. The three representative certificates and their four-factor-preserving transports are pinned in `full_visibility`.

**Mixed visibility import.** The 219 literal identities for selected J and required visible vertices use graph FDs, the actual selected local decoder given S, H(S|Y_V)=0 and G_S. The checked visibility condition and factor-preserving relabeling make each applicable to its listed planes. This is the part-3 certificate collection (not merely the earlier 73-certificate subset). Its 5,858-plane coverage is replayed independently in the new census.

### The last 1,905 directions

They form 515 canonical coloring classes: five one-element orbits, seventy two-element orbits and 440 four-element orbits. The older 197+295+3 exact functional certificates cover 495 classes. New identities cover the last twenty classes:

`65,72,150,157,225,247,335,336,353,354,355,359,363,493,494,495,496,497,498,499`.

Each new identity expresses 3H(Y_V)-2 sum_v H(Y_v) as nonpositive Shannon terms, nonnegative multiples of G_S when used, and vanishing original/functional/local FD rows, including the finer single-functional decoder. The Shannon terms include the translated data-processing and pair-determination consequences between the auxiliary branches. Thus each conditional selected law has nonpositive gap.

- New certificate bundle: `frontier-20261029-single-functional-local-certs-all20-v1.json`, SHA-256 `c129b79abcf916afb8a91d4145e6bb9316d0a3968d919f92beb516bdadf5450d`.
- Independent semantic checker: `frontier-20261029-plane-functional-local-decoder-check-v1.py`, SHA-256 `3570addd9c5fd1d26490e43173268259866814fcd28fe06f4748984cec182fb3`.
- Receipt: `frontier-20261029-single-functional-local-certs-all20-check-v1.json`, SHA-256 `5dfeb0f85cb1c4fbc40d424e0e59b35f483baae24f29c990e53be981af6c7e60`; all twenty checked. Changed lemma binding, wrong local functional and changed target controls are rejected.

### Set equality, not count matching

`frontier-20261029-all-plane-entropy-census-check-v1.py` independently enumerates the whole universe by RREF bases, replays the predecessor category predicates, validates the graph/factor actions and coloring canonicalization, and compares the exact unresolved set to the union of these 515 coloring orbits. The sets are identical, not merely equal-sized. It also binds every prior identity receipt to its exact certificate bytes.

Receipt `frontier-20261029-all-plane-entropy-census-result-v1.json`, SHA-256 `ef8b7154de6c5eecd836b64545f038687bc7d545e36acd4788d3f528c69d0140`, records zero uncovered directions and rejects a same-count wrong-plane-set control, a dropped proof class and a rank-one fake plane. It does not replace scientific review of the named written imports.

## 4. Lift from the fibers to the original law

Process the fixed-parity factors first. Each satisfies its conditional 2/3 factor inequality under any conditional law. In every final fixed-factor fiber the selected law has nonpositive gap by the complete case split above. Sum these inequalities. Replacing conditioning on all earlier factor components by conditioning on only each vertex's own earlier components increases the right side; the chain rule then gives

3H(X_V) <= 2 sum_v H(X_v).

This uses neither independent factors nor uniform probabilities and proves the stated claim with the named imports.

## 5. Exact scope and the next frontier

The proof rules out arbitrary-law entropy-ratio gains within any affine binary syndrome space of dimension at most two in this fixed q=8 encoding. In particular a positive balance-gap law would need at least four syndrome values with affine span at least three. Dimensions three and higher, other representations and the unrestricted guessing number remain open.

This does not improve the separately submitted, unreviewed unrestricted upper-bound candidate 2603/389 or construct a nonlinear strategy. It strengthens the predecessor uniform plane-transversal word-count result to an arbitrary-law entropy obstruction within this author-owned research branch; priority in the literature has not been audited.

The exact coefficient identities and finite coverage are same-harness machine checks, not Lean/formal proof or an independent scientific referee verdict. The written component inversion, conditional tensorization, import applicability and literal graph identification remain load-bearing review obligations. No frozen earlier packet was rewritten and no held review was rehabilitated.
