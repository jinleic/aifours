# Independent review: R-minus linear Ingleton and defect gates

**Clock observed immediately before this report's exclusive creation:** 2026-10-28T19:11:58-0700 PDT  
**Review type:** same-harness independent mathematical reconstruction; not a cross-family, human, formal, or novelty review.  
**Binding manifest:** `manifest-v1.json`, SHA-256 `2851477a354693144813bbfd3c0551e206744336636a44d4cf218ef6161acf4f`.

## Verdicts and findings

The following verdicts are for the graph explicitly listed at `frontier-20261028-linear-ingleton-bound-v1.md:42-49`, with all ten listed graph FDs. The separate question whether this labelling is the original published R-minus graph has not been independently resolved from a primary source; see Scope.

1. **Linear Ingleton bound and q=8 lower code:** **FATAL 0 / MAJOR 0 / MINOR 0** within the stated graph, representable-rank/finite-field scope. The exact identity, the general-field subspace argument, and the full-neighbour lower construction check out. The all-entropy defect statement is a necessary condition, not a general numerical upper bound. Claim anchors: `frontier-20261028-linear-ingleton-bound-v1.md:7-14,23-38,49-62,71-90`; exact rows: `frontier-20261028-linear-ingleton-exact-dual-v1.json:193-206,207-1864,1865-5811,5812-5867`.
2. **Two-Ingleton gate and its local four-atom witness:** **FATAL 0 / MAJOR 0 / MINOR 0** in that scope. The claimed `2 avg J1 + avg J2 <= -12 Delta` and the `-4 epsilon` consequence follow; the local witness really violates the proposed pointwise sign shortcut. Claim anchors: `frontier-20261028-two-ingleton-defect-gate-v1.md:12-54`; exact rows, including J1/J2 and FDs: `frontier-20261028-two-ingleton-exact-dual-v1.json:193-206,207-2789,2790-2927`.
3. **Single-diamond gate and averaged four-atom witness:** **FATAL 0 / MAJOR 0 / MINOR 0** in that scope. The 62-CMI identity, the eight listed diamonds, the `-3 epsilon` gate, and the negative averaged example check out. Claim anchors: `frontier-20261028-single-diamond-defect-gate-v1.md:14-57`; exact rows: `frontier-20261028-diamond-ingleton-exact-dual-v1.json:193-206,207-1810,1811-1915`.

**No unrestricted `20/3` upper bound follows.** The examples disprove the particular proposed Ingleton-sign shortcuts, not the unrestricted bound itself; neither is a strict-gain strategy. None of these verdicts accepts an unrestricted upper bound or establishes novelty.

## Pins and reading

Every one of the 14 inputs was SHA-256, byte-count, and LF-count checked against the binding manifest and read in manifest order in raw, exact windows. All 14 full hashes and sizes matched; no process mismatch was found. The role/order is as in the manifest; complete computed values also appear in `review-exact-check-result.json`.

| # | Frozen input | Computed SHA-256 | bytes / LF |
|---|---|---|---|
| 1 | `frontier-20261028-linear-ingleton-bound-v1.md` | `e056dd9695a4b3e308431441b4f15ec3a2d81f3c733c604cff8246796abf3da4` | 7485 / 99 |
| 2 | `frontier-20261028-linear-ingleton-exact-dual-v1.json` | `ce3fe7a8a77576dca4fd21315055cffdf767484a7a60883a2dc532b15708086a` | 80534 / 5867 |
| 3 | `frontier-20261028-linear-dual-independent-check.py` | `13d9e7abc5941600184479e4cbb7abeee773627caab0a3341981e7a112570940` | 7116 / 148 |
| 4 | `frontier-20261028-linear-dual-independent-check-result.json` | `203d474692e5506da5f0e4cd22286e466aad2910197ca351adf4487f4853c113` | 996 / 25 |
| 5 | `frontier-20261028-two-ingleton-exact-dual-v1.json` | `b8d049baf687e6b38024c085369970c0b05fa46e4c1ba7517b9c2c7a652b5d9c` | 39927 / 2931 |
| 6 | `frontier-20261028-two-ingleton-independent-check.py` | `bf0f7122772b7fc8cd978cf56a02474e64806f8cc2143956ff9ec2f52b9447b8` | 7429 / 150 |
| 7 | `frontier-20261028-two-ingleton-independent-check-result.json` | `3d1505ee4afeb3b992a2e03b6ba4a9787923eef2322390dd58617896c07722fd` | 995 / 25 |
| 8 | `frontier-20261028-two-ingleton-defect-gate-v1.md` | `3f9f543bb5893e26a5abecb21a5c81b6408214446dc495ea8c66747ea84f5f2b` | 5298 / 63 |
| 9 | `frontier-20261028-diamond-ingleton-witness-result.json` | `cb8fcc169d2d0889e5787eced4df44616547e809256ab02e493292cb8cd6fca5` | 681 / 34 |
| 10 | `frontier-20261028-diamond-ingleton-exact-dual-v1.json` | `3704cb337dba009deffece5ab4e66932bf4a315e01d2e8e6d5e35567dbc6f90f` | 25812 / 1915 |
| 11 | `frontier-20261028-diamond-ingleton-independent-check.py` | `eede3dab5cfe1135fee27d526d3e890ac031be8ce1de5725481e1bf3ef1b74b7` | 7403 / 150 |
| 12 | `frontier-20261028-diamond-ingleton-independent-check-result.json` | `0ae781de13843b5b64145b7e466ce5324ed022ed2d24111f472f51a4d0c075a1` | 995 / 25 |
| 13 | `frontier-20261028-single-diamond-defect-gate-v1.md` | `2ea2c5c414dc0a88dcecfe9da1423d4117bb06cc8420b01965d8f2e4604c4011` | 5682 / 66 |
| 14 | `frontier-20261028-negative-averaged-diamond-result.json` | `8c6d55a95e81e4068b520075ae421537aabf4aecfdeab5952e6ecfad8a35e743` | 669 / 26 |

The named `frontier-20261028-triangle-baseline-result.json` was additionally read and hashed to `1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82`; its triangle list was **not** trusted as proof. The named linear LP proposer and its base module hashed to their references `1eb7bf0fe48166c5076c6baaaf4d02c8e3cd78329ed60f5946f1821b45202254` and `f23e91be2a2440ab29b759983f4b0306e146c4a2dabc90038c6a461582c275e0`. Only the base's displayed graph was inspected, not used as independent provenance of the graph's historical name. The author checker scripts and receipts are evidence to review, not proof premises.

## Independent exact reconstruction

`review-exact-check.py` (SHA-256 `3200e8e06d09a7616db410e474a2835e32e623ed3da12396c8b18ab16763d12a`) imports no author code and uses Python `Fraction`/integers. Its exclusive-created receipt `review-exact-check-result.json` has SHA-256 `fa7b1b9104462bcb5b452169a645486aea2da5f8b266504eb23b9f1426fdd233`. It regenerates each CMI, FD, and Ingleton entropy polynomial from the named row arguments, verifies each stored orbit-term list, requires strict positivity of every CMI and Ingleton multiplier, checks conditioning-disjointness and the three signed FD multipliers, and expands all rows by all eight group elements. It compares the resulting rational coefficients against the target on **all 1023 labelled nonempty subset coordinates**, not merely on the 185 quotient coordinates.

The stated graph is symmetric with 26 edges. From the two stated generators the script constructs eight automorphisms; independently, it exhausts all `2! * 8! = 80,640` degree-preserving permutations and finds no other graph automorphism. The nonempty subsets have 185 orbits, with singleton orbits `{1,8}`, `{2,5,9,10}`, `{3,4,6,7}`. Thus the three certificate caps `4/3,8/3,8/3` are exactly `(2/3) sum_v h(v)`, not three individual-vertex entropies.

| Certificate | Rows CMI / J / FD | Minimum CMI weight | Minimum J weight | Sum J weights | Labelled-coordinate residual |
|---|---:|---:|---:|---:|---|
| linear | 64 / 83 / 3 | `96434/53358365` | `8506/32015019` | `1856350733/320150190` | empty |
| two-Ingleton | 99 / 2 / 3 | `1/36` | `1/12` | `1/4` | empty |
| single diamond | 62 / 1 / 3 | `1/6` | `1/3` | `1/3` | empty |

For each certificate the three FD rows have weights `-2/3,-4/3,-4/3` for vertices `1,2,3`; these rows vanish when all graph FDs hold. The check retains these rows while comparing the universal linear identity; it does not assume an FD while forming the residual. The two special rows are exactly `J1=J(2,4;1,3 | 5,6,7,8,9,10)` with weight `1/6`, and `J2=J(2,5;3,6 | 1,4,7,8,10)` with weight `1/12`; the single-diamond row is the same J1 at weight `1/3`. The script independently regenerates the eight diamond rows in `single-diamond-defect-gate-v1.md:30-39`, checks their conditioning sets are the complementary six vertices, checks their induced `K4` minus the `A,B` edge, and checks the stated graph dependencies.

Five in-memory mutations of the single-diamond certificate are each rejected for the intended reason: changed positive weight by nonzero **coefficient residual**; negative weight by **inequality sign**; overlapping condition by **row input**; wrong cap by **caps**; altered stored coefficient by **row mismatch**. These controls exercise the reviewer checker; they do not replace the exact identity.

Writing `Delta=H(V)-(2/3)sum_v H(v)` and `epsilon=H(V)-(20/3)M`, `M=max H(v)`, gives `Delta >= epsilon`. The checked identities and `I(X;Y|Z)>=0` give

* linear certificate: if `epsilon>0`, one of its 83 shapes under one group element is at most `-epsilon/T`, `T=1856350733/320150190`;
* two-Ingleton certificate: `2 avg J1 + avg J2 <= -12 Delta`, hence some J1/J2 automorphic instance is `<= -4 epsilon`;
* diamond certificate: `avg J1 <= -3 Delta`, hence one of its eight diamond instances is `<= -3 epsilon`.

These deductions do not assume Ingleton for arbitrary entropy. For finite laws, the CMI nonnegativity used here follows by averaging the nonnegative relative entropy `D(P_XY|Z || P_X|Z P_Y|Z)` over Z.

## Ingleton proof and lower code

For subspaces `A,B,C,D` over an arbitrary field, put `S=A intersect B`. The image of S in the quotient by C is contained in the intersection of the images of A and B, so `I(A;B|C) >= dim S - dim(S intersect C)`; the same holds with D. Also `I(C;D)=dim(C intersect D) >= dim(S intersect C intersect D)`. Since

`dim(S intersect C)+dim(S intersect D) <= dim S + dim(S intersect C intersect D)`,

adding the three bounds gives `I(A;B|C)+I(A;B|D)+I(C;D) >= dim S = I(A;B)`. Quotienting all four subspaces by the span of Z proves the conditional expression. This is a general proof, not an inference from a finite sample. As an additional exact control, the reviewer enumerated all 16 subspaces of `F_2^3` and all **1,048,576** ordered `(A,B,C,D,Z)` tuples; the minimum conditional J was 0.

For the claimed lower bound the reviewer independently checks the ten listed triples, that all 30 triangle pairs are graph edges, and that each vertex occurs three times. There is one bit per vertex-triangle occurrence. The ten XOR-zero equations have disjoint occurrence supports and exact binary rank 10, so there are `2^(30-10)=2^20` fixed words over `q=2^3=8`. At each vertex the three output bits are the XORs of the other two bits in the corresponding triangles; these are all-domain, full-neighbour local decoders, and their fixed point equations are exactly the ten parity equations. The certificate upper bound for the rank of any nonempty affine fixed-point space therefore matches this code, giving the supremum `20/3` for the stated finite-field vector-linear/affine strategies. The same upper bound holds for a uniform affine-subspace support with the graph FDs, irrespective of decoder linearity.

## Exact four-atom verification

Both laws use the 10-bit words `0,6,3,15`, with vertex 1 as the least significant bit and vertices 5--10 zero. The reviewer exhausts all `C(4,2)*10=60` pair/vertex FD checks. These words have `X2=X1 OR X3` and `X4=X1 AND X3`.

* For weights `(2,1,1,2)/6`, vertices 1 and 3 are fair and all variables are binary, so `M=1` bit. The two positive `I(2;4|1)` and `I(2;4|3)` terms are exactly zero and direct integer-prime entropy arithmetic gives `J1=3-2 log2(3)=log2(8/9)`. The comparison `9^8=43046721 > 2^25=33554432` proves `J1<-1/8<-7/69`. This is the **unaveraged** witness only.
* For weights `(21,4,16,9)/50`, vertex 1 is fair and `M=1`. After exact averaging over the eight graph automorphisms, independent prime factorization gives

  `2^(400 avg J1) = (2^56 * 3^39 * 7^21 * 29^58 * 41^41) / (5^190 * 13^13 * 37^37)`.

  Exact integer comparison shows eight times the numerator is less than the denominator. Consequently `avg J1<-3/400`; approximate `-0.00957827023657` bits is only explanatory. The J2 entropy coefficients cancel after grouping subsets by their partitions of the four support atoms, so `avg J2=0` for **every** distribution on this support; hence `2 avg J1 + avg J2<-3/200`. As an additional check of the author's unreduced product convention, the reviewer independently obtains `L.bit_length()=7946`, `R.bit_length()=7943`, and `L>8R`. Details are in `review-witness-unreduced-result.json` (SHA-256 `2f9c575b36ef8a1b1de2ce2cc40071de22f6c15299b7b69e94f1514bd94f3d04`). Since joint support has only four atoms, `H(V)<=2<20/3` while `M=1`; this is not a strict-gain example and does not violate the balance certificates.

## Scope, imports, and limits

* Mathematical verdicts above are conditional on the ten-vertex graph specified by the frozen candidate. Matching the label “original R-minus” to an independently identified primary graph is an **unverified import**; the named same-lane base module repeats the same adjacency but is not independent historical provenance. This does not change the verified identities for the listed graph.
* The inherited unrestricted `1847/276` upper bound and its original source are **unverified imports**. Only the arithmetic `1847/276=20/3+7/276` and the threshold implication `c<7/69` were checked; this bound is not a premise for the certificates.
* The float LP search/proposal, dual optimality, prior history, claimed publication priority, and novelty are not independently verified or needed. No author replay, author solver result, quarantined or withdrawn body, external model, paid API, Git operation, publication, or infrastructure mutation was used as a proof premise.
* No proof assistant, external-family reviewer, or human review was used. Exhaustive finite checks are controls, not substitutes for the displayed general-field subspace proof. All entropy-law statements assume finite joint laws and the graph FDs, and the exact `20/3` upper bound assumes representable ranks/affine finite-field supports as stated.
