# Global compactness of all seven-state spectral candidates above z=1/2

**WRITTEN THEOREM CANDIDATE, not independently reviewed; no 8/9 answer.** MathResearch96h-2. This is a new prospective all-topology bridge. It imports the explicitly reconstructed 3/5/6-state Metzler spectral lemmas and SCC argument of `frontier-20261028-ph7-global-irreducibility-v1.md`, SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`; parent has separately reported independent written support for that source's PH application. The new resolvent-limit/compactness argument below requires its own full review. No held output is a premise, and the previously known PH6 bound is not claimed as a new result.

## 1. The theorem and why it is a real global reduction

Fix ANY finite interval `[L,U]` with `1/2<L<=U`. Let S(L,U) be the set of pairs `(G,z)` such that

* G is a real seven-state row generator: `G_ij>=0` for i!=j and `G1=0`;
* `z in [L,U]`; and
* `D_z(y)=y[(y+1)^2+z]^2` divides the ACTUAL characteristic polynomial `det(yI-G)`.

**Claim.** S(L,U) is compact in its 42 off-diagonal rates and z, and every G in it is irreducible. Consequently, if the set is nonempty then there is a positive constant epsilon(L,U) such that EVERY nontrivial directed cut has total crossing rate at least epsilon. No explicit numerical bound or decision procedure is claimed.

In particular the spectral search on `[7/9,8/9]` cannot escape by sending any rate to infinity or by approaching a reducible zero-cut generator. It has a genuine attained global maximum: the earlier explicit `frontier-20261028-ph7-explicit-band-41over50-v2.md` SHA256 `8e9d10653ef1c930a07bf8a6ee06ae6e99f61194eccb2edaeeac4f51c4ffde91` supplies an actual nonempty point at z=4/5 (parent reports an independent exact check), after positive Perron normalization. The separate candidate strict-local maximum at z_* is one local maximum, not automatically the global maximum. Proving that the global maximum is <8/9, or constructing a valid point at8/9 with the SAME PH numerator, remains the central open step.

## 2. Spectral block fact needed for the proof

The named predecessor's SCC/trace argument proves the following **spectral-only** statement, independent of any initial or exit vector:

> If a real Metzler row generator of order at most seven has eigenvalues `-1 +/- i sqrt(z)` each with algebraic multiplicity at least2 and z>1/2, then its order is exactly seven and its graph is irreducible.

Indeed, every SCC has spectral bound<=0; a visible pair cannot lie in a 1-, 2- or 3-state SCC (the predecessor's exact 3-state trace-square bound). Two distinct such SCCs would need at least8 states. Their common SCC needs at least5 states by a real Perron eigenvalue, but order5 is excluded by the trace-square inequality and order6 by the fully written centered trace2/3 lemma after shifting/scaling by its Perron root. That argument uses no PH reachability or nonminimality premise. Repeated hidden roots, extra coincidences and defective Jordan structure do not change the counting.

We use both consequences: no row generator of order <=6 has this spectrum, and every seven-state G in S(L,U) is irreducible.

## 3. Suppose rates diverge: a compact family of nonnegative resolvents

Assume toward contradiction there is a sequence `(G_n,z_n)` in S(L,U) with an unbounded rate. By passing to a subsequence take `z_n -> z_bar in [L,U]`. Since G_n is a row generator, `-tr G_n` is the sum of all off-diagonal rates and goes to infinity. Every eigenvalue of G_n has nonpositive real part, so at least one eigenvalue has modulus tending to infinity.

Let

    R_n=(I-G_n)^(-1).

The nonnegative Markov semigroup, or the nonsingular M-matrix resolvent, gives `R_n>=0` and `R_n 1=1`. Thus the matrices R_n lie in the compact set of row-stochastic seven-by-seven matrices. Pass to a subsequence with `R_n -> R_0`. R_0 is nonnegative and row stochastic. It is SINGULAR: one eigenvalue of G_n diverges, so one eigenvalue of R_n tends to0; all others are bounded. Equivalently, all factors `|1-lambda(G_n)|>=1` while one tends to infinity, so `det R_n ->0`.

Each visible eigenvalue of G_n gives an eigenvalue of R_n of algebraic multiplicity at least2:

    mu_n^+ = 1/(2-i sqrt(z_n)),    mu_n^- = conjugate(mu_n^+).

Eigenvalues of matrices depend continuously as multisets on their entries. Thus R_0 has `mu_bar^+` and `mu_bar^-` each with multiplicity at least2 and has eigenvalue1. These three values are nonzero and distinct.

## 4. A positive stochastic projection from the resolvent limit

Every eigenvalue mu of R_n satisfies `Re(mu)>=|mu|^2`: write it as `mu=1/(1-lambda)` with `Re(lambda)<=0`. The same closed disk constraint holds for eigenvalues of R_0. Hence for real s>=1 the matrix `I+(s-1)R_0` is invertible. Define

    R(s)=R_0 [I+(s-1)R_0]^(-1).

The ordinary resolvent identity gives `R(s)=lim_n (sI-G_n)^(-1)`. Therefore for every s>=1,

    R(s)>=0,         R(s)1=1/s.                       (RES)

In particular `sR(s)` is row stochastic and bounded in max-row-sum norm. This forces eigenvalue0 of R_0 to be semisimple: a nontrivial nilpotent Jordan block at0 would make `s R_0[I+(s-1)R_0]^(-1)` unbounded as s grows. Consequently the limit

    E=lim_(s->infinity) s R(s)

exists and is the spectral projection of R_0 onto its nonzero generalized eigenspaces. By(RES), E is a nonnegative row-stochastic idempotent. Because R_0 is singular, its rank `m=rank E` is at most6; the nonzero eigenvalues above ensure m>=5.

### Positive factorization of E

Decompose the row-stochastic idempotent E into its recurrent irreducible classes and transient states. On each recurrent class, irreducibility plus `E^2=E` makes the block rank1 with identical rows equal to its stationary probability vector. The transient diagonal block is also idempotent but has spectral radius<1, so it is0; transient rows are convex combinations of the recurrent class rows. Consequently there are nonnegative row-stochastic matrices

    U in R^(7 x m),   V in R^(m x 7),
    E=U V,            V U=I_m,                         (FACT)

where each row of V is a recurrent stationary distribution padded by zeros, and each row of U lists the corresponding convex weights. The number of recurrent classes equals rank E=m. This supplies the positive factorization explicitly; an arbitrary real projection factorization would not be enough.

## 5. A smaller row generator retains the forbidden repeated pair

For s>=1 set `R_tilde(s)=V R(s) U`. From(RES) and(FACT), `R_tilde(s)>=0` and `R_tilde(s)1=1/s`. Since R(s) acts on the range E as a genuine resolvent, and U,V are inverse coordinate maps between that range and R^m, there is a real m-by-m matrix B with

    R_tilde(s)=(sI-B)^(-1),        s>=1.

For s sufficiently large, expand in 1/s:

    R_tilde(s)=I/s+B/s^2+O(s^-3).

Off-diagonal nonnegativity for all large s implies `B_ij>=0` for i!=j; the row-sum identity gives `B1=0`. Thus B is a real m-state row generator, with m<=6.

On the nonzero spectral subspace the map from an eigenvalue mu of R_0 to an eigenvalue of B is `lambda=1-1/mu`; it preserves algebraic multiplicity because mu!=0. Therefore B has the eigenvalues

    -1 +/- i sqrt(z_bar), each with algebraic multiplicity >=2.

But z_bar>=L>1/2, contradicting the spectral block fact of §2 for m<=6. This contradiction proves all off-diagonal rates in S(L,U) are bounded.

## 6. Closedness and uniform irreducibility margin

The row-generator inequalities are closed, `[L,U]` is compact, and divisibility by D_z is equivalent to the four polynomial coefficient equalities printed in the first-order source. Hence S(L,U) is closed. Bounded plus closed gives compactness.

Every G in the set is irreducible by §2. Define the continuous finite-cut quantity

    cut(G)=min_(nonempty proper A subset {1,...,7})
                 sum_(i in A, j outside A) G_ij.

It is strictly positive exactly for strongly connected directed graphs. A positive continuous function on the nonempty compact set S(L,U) attains a strictly positive minimum, proving the claimed uniform cut gap. This is existential and depends on L,U; the proof supplies no computable epsilon, no explicit rate bound, and no uniform assertion as L approaches1/2.

## 7. Review and nonclaims

Named ordinary imports: Perron and SCC spectral facts from the predecessor; finite-dimensional stochastic semigroup/resolvent positivity; continuity of characteristic roots as multisets; Jordan form at0; elementary classification of finite stochastic idempotents; inverse-function/large-s resolvent expansion; compactness. Every model-specific application is written above. No scientific program, numerical optimization, or formal/kernel proof was used for this theorem. A reviewer must independently check the singular resolvent limit, positive idempotent factorization, transfer of algebraic multiplicities, the six-state spectral-only premise, and cut-gap argument.

This is global compactness of the SPECTRAL necessary set, not a PH7 feasibility characterization or global bound at8/9. The existence of a compact set does not mean it is empty; the maximum might be above z_* and may belong to another graph. No computable bound, witness, novelty claim, independent review or historical process repair is asserted.

END — the entire seven-state repeated-pair spectral search in any closed interval above1/2 is compact and uniformly irreducible; 8/9 remains unresolved.
