# Row imbalance plus the cross determinant excludes 16 cyclic spectra

**WRITTEN + EXACT-CYCLOTOMIC-CERTIFICATE-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 03:19:56 PDT 2026. This is an all-field, all-phase exclusion for the cyclic-equivariant 6D graph, conditional on the earlier simple-spectrum and two-plane reductions. It is not a general G6 or QLS10 no-go.

## Claim

Of the 29 cyclic spectral classes left by `frontier-20261029-cyclic15-selfplane-3-no-go-v1.md` SHA-256 `f4f22317a1d497473b7767ef84924da11fcd018e47fad8be084618cb21f37479`, **16 cannot occur**. This leaves **13** classes: seven with U^5 multiplicities `(3,2,1)` and six with `(2,2,2)`. The remaining representatives are recorded in `frontier-20261029-cyclic15-13-residual-spectra-v1.json` SHA-256 `eea1390fac4544cab4500e8e3980fdf19285fe9ef30ac2b93900557383c52c7b`; no feasibility claim is made for them.

## Combining two field-free necessary conditions

Each of the 16 excluded spectra has exactly one 2D U^5 eigenspace whose two U exponents differ by ±3. The row-imbalance theorem `frontier-20261029-cyclic15-row-imbalance-v1.md` SHA-256 `5fd6191eb69c5720eaf5a272b98693249578a41cab90571ec7b73260e09aef04` gives, for its two v5 populations,

`|p_j-1/6| >= delta`, where `delta=(1/3)sqrt((3sqrt(5)-5)/10) > 11/80`.

The strict rational lower bound follows from `sqrt(5)>4289/1920`, since `5*1920²-4289²=36479>0`. The two populations sum to 1/3. Thus one is strictly below `7/240` and the other strictly above `73/240`.

For either choice of the low index l and high index h, introduce positive variables `x_l,x_h` with `x_l+x_h=1` and write

`p_l=(7/240)x_l`, `p_h=(73/240)x_l+(1/3)x_h`.

For each other U^5 residue class introduce positive variables summing to 1 and set `p_j=x_j/3`. These substitutions cover **every** population satisfying the strict imbalance, including the exact irrational boundary implied by delta.

The four cross-plane matrices must have zero determinant, as in `frontier-20261029-cyclic15-crossplane-38-no-go-v1.md` SHA-256 `0a4bd44d9dca934397153be9547e029b6e171677f0690c9862e6262293d06bd8`. For every one of the 16 spectra and **both** choices of low index, the exact certificate substitutes the above expressions into the Cauchy–Binet determinant numerator P. It multiplies individual terms by powers of the three group identities `sum x=1`, so the resulting polynomial is multihomogeneous of degree 2 in each group and equals P up to a fixed sign on the branch. Every nonzero coefficient is strictly positive. Since all x variables are strictly positive, P cannot vanish. Both branches are impossible.

## Exact certificate and boundary

`frontier-20261029-cyclic15-imbalance-determinant-proof-v1.py` SHA-256 `f678d1f5d3c335b018bfaa81e2087352ef737769c6336d8c2455e23d4e8d3f8e` produces all 32 branch polynomials and cofactor data in `frontier-20261029-cyclic15-imbalance-determinant-proof-v1.json` SHA-256 `6e3accab7481596ca29a504d12e7792f735ae5e1c457bdc75fa0adf9887f392f`.

The separate same-owner replay `frontier-20261029-cyclic15-imbalance-determinant-replay-v1.py` SHA-256 `5b21f2f79c7887748e740aac9ed8e2a958da155f059160e190deb83a2e7e3305` rebuilds the determinants in `1,omega,eta,omega eta` over Q(sqrt(5)), verifies both branches for every spectrum, compares every coefficient in independent field coordinates, and checks **576** strict signs with rational trigonometric intervals. Result `frontier-20261029-cyclic15-imbalance-determinant-replay-v1.json` SHA-256 `cc3afe4a96840d92a3c1cd00c5fe15dcd37e540990bec7fdd12577295c4ff019` records **PASS** at 03:19:56 PDT.

The proof uses no constraint on the population field or vector phases. Its row-inequality caller, branch substitutions, cofactor determinant and sign intervals require independent mathematical review. The 13 residual cyclic cases and all symmetry-breaking 6D complements remain open; no formal-kernel or novelty claim is made.
