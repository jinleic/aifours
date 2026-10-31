# Independent same-harness review: PH7 global irreducibility and edge bound

Observed clock immediately before review creation: `2026-10-28T17:57:49-0700 PDT`. This is a prewrite observation, not an inferred exact completion time. Reviewer: `PH7IrreducibilityReview`. Scope: the frozen f61 lower-bound and structural claims only. This is a written mathematical reconstruction with independent exact arithmetic; it is not human, cross-model, kernel, publication, or priority verification.

## Disposition and findings

**FATAL: 0. MAJOR: 0. MINOR: 1.** Subject to the standard mathematical imports identified below, I independently reconstruct the claimed conditional result: for `z>1/2`, any actual PH representation of the stated transform with at most seven states has exactly seven states, all reachable, and is irreducible; it has at least eight positive off-diagonal entries. The claim is conditional on a representation existing. No author conclusion or held payload was assumed.

- **MINOR — ambiguous witness wording**, global irreducibility source LF11. The phrase “an 8/9 witness, if any” could be read as covering an arbitrary-order PH witness, although the theorem only constrains representations of at most seven states. Suggested wording: “a PH representation at `z=8/9` using at most seven states, if one exists, has exactly seven states and is irreducible.” The proof and its explicitly quantified theorem are unaffected; the proof says nothing about arbitrary higher-order representations.
- **Not a finding on the lower bound:** the edge source LF9 and LF35 also report sharpness somewhere using a separate v4 construction and mandatory erratum. Neither was an input to this frozen review, and neither was read. **Edge sharpness is NOT_RECONSTRUCTED and not adopted here.** No endpoint or eight-edge realization is certified.

The strict `z>1/2` hypothesis matters; no assertion is made at equality or below. In particular `z=8/9` is inside the structural region, but neither the existence nor impossibility of a seven-state PH realization at `8/9`, nor its exact minimum order, is established here. The lower-state barrier is a reconstruction, not a claim of novelty. The novelty of the SCC and edge observations remains unassessed.

## Input binding and read order

The complete manifest was read first and then each complete listed input was read in manifest order. For every input I computed the SHA-256, byte count, and LF count against the manifest; all matched. The manifest has no independent expected hash in the assignment; its observed SHA-256 is recorded, not falsely presented as a comparison against a second pin.

- Manifest `manifest-v1.json`: SHA-256 `46e6d3adb42b414b4e04e598abb61d6b50d241b1db136974a9ffda5ca590ffaa`, 2280 bytes.
- 1. `written-releases/math-1-ph-order-definitions-v1.md`: `a4db7478cf384fabdddccede032efe2cd1f33d12ad3e771788e58d5596682e85`, 1534 bytes, 17 LF.
- 2. `mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-ph7-global-irreducibility-v1.md`: `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`, 10148 bytes, 117 LF.
- 3. `mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-ph7-minimum-eight-edges-v1.md`: `1c81a83db9f65f6c87d62c01ac4a8ed39662a9a246af242877b7fc947be6e9cf`, 4190 bytes, 35 LF.

The first path is relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`; the last two are relative to `/Users/jinleic/repos/aifours/`. I did not import or run the author's cited checker. No source claimed to be held was used as a premise.

## Independent reconstruction

### 1. Transfer, trimming, exits, and spectral bound

Let `a=c+d`, `d>0`, `b>0`, `z=b²/d²`, and let `omega=-T1`. The numerator `c(a²+b²)²` is nonzero. Since `c<a` and `b>0`, the reduced denominator has exactly one pole at `-c` and order-two poles at each of `-a±ib`. For any finite representation,

`H(s) = alpha adj(sI-T) omega / det(sI-T)`.

Thus every pole appears as a characteristic root with algebraic multiplicity at least its pole order, regardless of hidden roots, cancellations at other eigenvalues, or Jordan structure. In particular its characteristic polynomial is divisible by `(s+c)((s+a)²+b²)²`.

Let R be the states reachable from `supp(alpha)` by positive off-diagonal transitions. R is forward closed; restricting `T`, `alpha`, and `omega` to R preserves the entire transfer and `omega_R=-T_R 1`, while `alpha_R1=1`. The retained `T_R` is Hurwitz. Also `(-T_R)^(-1)omega_R=1`: this follows algebraically from `omega_R=-T_R1`. Since `(-T_R)^(-1)=∫_0^∞ exp(tT_R)dt` is entrywise nonnegative, every retained state can reach a positive exit; otherwise the corresponding left-hand entry would vanish.

For each retained SCC with principal block B, choose any fixed `t0>0`. The vectors `p=(alpha exp(t0 T_R))|_B` and `q=(exp(t0 T_R)omega_R)|_B` are positive: reachability/exit paths and the nonnegative Metzler semigroup yield strictly positive path contributions. Nonnegative semigroup expansion gives `[exp(tT_R)]_BB >= exp(tB)` entrywise, so

`f(t+2t0) = alpha exp((t+2t0)T_R) omega_R >= p exp(tB) q`.

Irreducible Metzler Perron theory supplies positive left/right Perron vectors and a simple real spectral bound `rho(B)`, strictly larger in real part than all other block eigenvalues. Hence the right side is at least a positive constant times `exp(rho(B)t)` for all sufficiently large t. On the other hand the actual rational H has inverse transform `f(t)=A exp(-ct)+O((1+t)exp(-at))`, with

`A = c(a²+b²)²/(d²+b²)² > 0`.

Thus each `rho(B)<=-c`. The spectral bound of retained T is exactly `-c`: all block spectral bounds are at most `-c`, and `-c` is itself an eigenvalue by the genuine pole. For `G=(T_R+cI)/d`, every SCC has spectral bound at most zero, and `0` plus two algebraic copies of each `-1±i√z` are present. This is a positivity argument on the actual transfer; no inference is made about unreachable blocks before trimming.

### 2. Small SCCs and counting algebraic copies

For any real Metzler matrix C of order n,

`tr(C²) = Σ C_ii² + 2Σ_{i<j} C_ij C_ji >= (tr C)²/n`.

This holds without diagonalizability, since trace power sums count eigenvalues with algebraic multiplicity. Orders one and two have only real eigenvalues: in order two the discriminant is `(C11-C22)²+4 C12 C21 >=0`.

If a three-state SCC contains `-1±i√z`, its remaining eigenvalue is its simple Perron root `-r`, with `0<=r<1`; strict Perron dominance supplies the second inequality. Its trace-square necessity is

`3[r²+2(1-z)]-(r+2)² = 2[(1-r)²-3z] >=0`,

impossible for `z>1/2`. Thus every SCC containing a visible nonreal root has at least four states. Realness forces conjugate roots into the same SCC. If the two algebraic copies of a visible root were distributed over two SCCs, these would use at least eight states, contradicting the retained `m<=7`. Hence a single SCC contains both copies of both visible roots. Its real Perron eigenvalue is distinct from these four nonreal roots, so it has at least five states.

At size five its spectrum is exactly the two conjugate pairs and `-r` with `0<=r<1`. The trace-square necessity is

`5[r²+4(1-z)]-(r+4)² = 4[(1-r)²-5z] >=0`,

again impossible. Additional hidden eigenvalues coinciding with a visible root increase, never decrease, its algebraic multiplicity and are included in this counting; no generic-eigenvalue assumption was made.

### 3. Six-state spectral obstruction, including degeneracies

Consider any real six-state Metzler M, even reducible, whose spectrum is `0,-u,-1±i√Z` with each nonreal root twice and `u>=0`. Define `h=(u+4)/6` and `X=M+hI`, so `tr X=0`. Direct spectral power sums give

`q=tr(X²)=(5u²-8u+8-24Z)/6`,

`p=tr(X³)=-(u-2)(5u²-2u+18Z+2)/9`.

The diagonal and reciprocal-edge expression above implies `q>=0`. Set `S_ii=X_ii`, `S_ij=√(X_ij X_ji)` for `i!=j`; S is real symmetric, `tr S=0`, and `tr S²=q`. Expanding closed three-step walks shows precisely

`tr X³-tr S³ = 3 Σ_{i<j<k}(√(X_ij X_jk X_ki)-√(X_ik X_kj X_ji))² >=0`.

For symmetric traceless S let its real eigenvalues be `lambda_i`. If `q>0`, a compact constrained extremum of `Σ lambda_i³` subject to zero sum and square sum q has at most two distinct values by Lagrange multipliers. If k entries take the negative value, `1<=k<=5`, the extremal ratio is

`(Σ lambda_i³)/q^(3/2) = (2k-6)/√(6k(6-k))`.

Its minimum is `-4/√30` at k=1; `q=0` is trivial. Consequently `p >= -(4/√30)q^(3/2)`, and when `p<0` the necessary inequality is `(8/15)q³-p²>=0`.

If `Z>1/2`, the numerator of q is convex in u and is strictly negative at both endpoints `u=0` and `u=2`; it is therefore negative throughout `[0,2]`. Since `q>=0`, put `s=u-2>0`, `delta=Z-1/2>0`. Exact algebra yields

`q=q0-4delta`, `q0=s(5s+12)/6 >0`,

`p=p0-2s delta`, `p0=-s(5s²+18s+27)/9 <0`,

`(8/15)q0³-p0² = -s²(30s²+116s+135)/15 <0`.

Now `0<=q<=q0` and `p<=p0<0`, so `(8/15)q³-p²` is at most that strictly negative expression, a contradiction. This argument uses algebraic power sums and allows repeated eigenvalues and nontrivial Jordan blocks.

If the common SCC of G had size six, its simple real Perron root would be `-r`, `0<=r<1`; after the four prescribed nonreal roots only one eigenvalue remains, which must also be real, say `-u` with `u>=r`. For `A=(B+rI)/(1-r)`, the spectrum is `0, -(u-r)/(1-r), -1±i√z/(1-r)` with the nonreal roots repeated. The lemma applies because the remaining real parameter is nonnegative and `Z=z/(1-r)²>=z>1/2`. It contradicts size six. The proof remains valid if roots elsewhere in the full matrix coincide, or if the two remaining roots of the standalone lemma coincide; irreducible Perron simplicity is used only where actually applicable.

The common SCC therefore has at least seven vertices. Since trimming retained at most seven, it has exactly seven and is all of the retained graph. The original graph had at most seven vertices, so none was trimmed: every original state is reachable and T is irreducible.

### 4. Single-cycle consequence

A strongly connected graph on seven vertices has at least seven positive off-diagonal edges. If it has exactly seven, every vertex has outdegree one; strong connectivity makes it one directed seven-cycle. For an n-cycle (`n>=2`) with real diagonal `-u_j` and positive edge product `K`, the determinant permutation expansion has only the diagonal and full-cycle terms:

`P(y)=det(yI-M)=∏(y+u_j)-K`.

For a nonreal root `lambda`, no factor `lambda+u_j` is zero, and

`P'(lambda)=∏(lambda+u_j) Σ_j 1/(lambda+u_j)`.

All summands of the latter sum have strictly negative imaginary part when `Im lambda>0` and strictly positive imaginary part when `Im lambda<0`. Thus the sum and derivative are nonzero: every nonreal root is algebraically simple. This contradicts either genuine order-two complex pole, which forces characteristic multiplicity at least two. Therefore at least eight positive off-diagonal entries are necessary. This is only a lower structural bound, not an existence or sharpness result.

## Independent exact computation and controls

Self-authored checker: `review-v1-exact-check.py`, SHA-256 `2f1dd7cbf2fc47796152a6eeeaab2a7167df90725e8f126596b64589f3658a22`, 7764 bytes, 218 LF. Actual execution in this review directory: `python3 -B review-v1-exact-check.py`, exit 0; every printed check passed. It uses sparse rational polynomial arithmetic implemented with the Python standard library and does not import the candidate's checker.

It independently computes the displayed 3-, 5-, and 6-state identities and substituted strict-negative polynomial. The substantive controls were:

1. At exact `u=3, Z=3/4`, `q=11/6>0`, `p=-109/18`, and `(8/15)q³-p²=-2003/60<0`: the cubic obstruction is genuinely stronger there than merely requiring nonnegative square trace.
2. A real non-diagonalizable conjugate-pair Jordan-block matrix, explicitly **not** claimed Metzler, has the required algebraic spectrum at `u=3,Z=1`; direct exact matrix multiplication gives centered moments `5/6` and `-59/9`, agreeing with the formulas. Its coupling polynomial is nonzero but squares to zero.
3. An asymmetric directed triangle embedded in six dimensions gives equal square traces `142` for X and S and a strictly positive cubic gap `1587=3(24-1)²`. The symmetric diagonal control `(-5,1,1,1,1,1)` saturates the extremal square form. These controls do not replace the general inequalities proved above.
4. Exhaustive seven-cycle determinant permutation computation found exactly two nonzero terms and `K=24`; independently altered spectral coefficients and cycle weight were rejected as negative controls.

The checker does not prove Perron theory, reachability, the general extremal inequality, or the theorem formally. Trust assumptions include exact Python integer/Fraction arithmetic and the checker implementation, in addition to the standard finite-dimensional results used in the written proof. It performs no search for a PH realization or prior art.

END — lower structural claims reconstructed with one wording MINOR; optional sharpness, existence/exclusion at 8/9, and novelty remain outside this review.
