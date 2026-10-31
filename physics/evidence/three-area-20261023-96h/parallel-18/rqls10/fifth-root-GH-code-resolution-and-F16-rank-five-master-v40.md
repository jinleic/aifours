# RQLS10 v40 — REPLACEMENT outside the closed alphabets: exact fifth-root GH-code resolution master and sharpF16 context rank5

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 09:54:16 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact cyclotomic/orthogonal-array/code/finite-Hermitian/rank-valuation reasoning only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

This is a genuinely DIFFERENT phase model after C/G Hadamard pairs were closed. Fifth-root phases have neither that unique exceptional-coordinate pattern nor its quadratic-polynomial obstruction. No former no-go is reused without its hypotheses, and no finite-field relaxation is claimed an original witness.

## 1. Exact original-model phase5 scope

Fix zeta=exp(2pi*i/5) and ONE common orthonormal basis of C10. Consider an ACTUAL prospective array

    q_c(s)=zeta^f_s(c)/sqrt10,
    c=(a,b) in the100cells, s=1..10,
    f(c) in F5^10.

Rows and columns are the original ten-cell contexts. A designated full resolution is ANY ten-symbol Latin square L on the SAME cell grid; its ten symbol classes give the third contexts. No cyclicity, covariance, linearity or selected resolution is assumed WLOG.

**Fifth-root equivalence.** Two such rays are orthogonal IFF the ten differences f_s(c)-f_s(d) contain EACH element of F5 EXACTLYTWICE. Their rays coincide IFF their phase words differ by a CONSTANT vector a*1.

Indeed the unscaled inner product is sum_(j=0)^4 n_j zeta^j, where the integer counts sum10. The minimal polynomial Phi5=1+x+x^2+x^3+x^4 forces n_0=...=n_4, hence all2. Equality of normalized rays forces the coordinate ratios all equal fifth roots, equivalently one constant exponent difference. These are exact iff statements, not finite-field approximate tests.

Thus the full phase5 maximal1-RQLS10 problem is EXACTLY100 phase-word classes in F5^10/<1>, distinct, for which every pair in any original ROW,COLUMN or L-SYMBOL context has the balanced difference profile(2,2,2,2,2). No actual satisfying table is supplied here.

## 2. Equivalent500-word code with THREE orthogonal GH-code partitions

Expand EACH phase class into its five representatives:

    C={f(c)+a*1 : c a cell, a in F5}.

Maximal distinctness is EXACTLY |C|=500 (no repeated phase orbit), not merely five hundred entries counted with multiplicity. For every original ten-cell context K define its50-word block C_K by the same expansion.

The phase5 conditions are equivalent to:

1. The100 five-word phase orbits are placed in the100 actual cells, with one full Latin resolution L.
2. EACH of the thirty context blocks C_K is a phase-translation-invariant GH(5,2) code: words from DIFFERENT phase orbits have every difference symbol twice (Hamming distance8), while words within one orbit differ by a nonzero constant (Hamming distance10).
3. The ten row blocks, ten column blocks and ten L-symbol blocks are THREE partitions of the SAME500-word code into ten50-word GH blocks each. Any block from two different partition types intersects in exactlyONE five-word phase orbit, because the underlying row/column/transversal contexts intersect in one actual cell.

This retains ALL actual cell incidences, not just a collection of unrelated OA50 blocks or a pair-count census. Conversely such a placed500-word code/three-partition structure reconstructs the literal normalized complex rays above and proves every required ONB and100-ray distinctness by section1.

No third partition may be dropped: a two-partition GH-code object would only be a QLS, as the100-ray unresolvable counterexamples earlier illustrated.

## 3. Equivalent orthogonal-array description, including why it is TWO-SIDED

Each50-word context code, as a50x10 array overF5, is an OA(50,10,5,2), of strength2 and index2, together with its prescribed five-word translation-orbit structure. Here the parameters mean50runs,10coordinates,5symbols, and each ordered pair in two distinct coordinate columns occurs2times.

To prove necessity, arrange one representative from each of its ten phase orbits as a10x10 exponent matrix M and let H=(zeta^M). The context ONB says HH^dagger=10I, so ALSO H^dagger H=10I. Its two coordinate columns therefore have balanced difference counts2 each across the ten representatives. Adding all five constant shifts produces each of the25 ordered coordinate pairs twice, exactly the stated OA.

For sufficiency, an OA50 with the specified constant-shift orbits gives those column-difference balances, so H^dagger H=10I; since H is square, HH^dagger=10I, yielding the actual context ONB. Merely an arbitrary OA with no phase-orbit/cell-placement structure is NOT sufficient for the full original array.

Globally the500runs also give a mixed-level OA

    OA(500;10^3*5^10;strength2),

by adjoining the original row,column,L-symbol labels (each alphabet10) to the ten phase coordinates. A pair of10-level labels occurs5times (one cell's orbit); a10-level/5-level pair occurs10times; two5-level coordinates occur20times. These counts follow from the already proved context OA and constant shifts. This global mixed OA is a NECESSARY summary; without the THREE50-run block refinements it is not declared sufficient.

Neither the500-word code nor a50-word block can be a linear F5-code, since500 and50 are not powers of5. No global linear-code ansatz is silently treated WLOG. This observation is only a boundary on representations, not the claimed scientific obstruction.

## 4. A second exact structure: each ACTUAL context reduces to a maximal isotropic5-space overF16

Let O=Z[zeta], and reduce modulo the prime2. Phi5 is irreducible overF2 because an element of order5 first occurs in degree4 (5 divides2^4-1 but not2^d-1 for1<=d<4). Hence

    O/(2)=F16,

with the image t of zeta having order5. Complex conjugation zeta->zeta^-1 reduces to t->t^4, the order2 field involution of F16 overF4.

For an ACTUAL context phase matrix H with HH^dagger=10I, reduction gives

    Hbar * (Hbar)^(4T)=0 overF16,

where the bar here means reduction, not complex conjugation. Thus its ten reduced ray rows span a TOTALLY ISOTROPIC subspace for the nondegenerate Hermitian form

    h(x,y)=sum_s x_s*y_s^4.

Its dimension is at most5 since W is contained in W-perp in a10-space.

The dimension is EXACTLY5, not only bounded. At the unique prime above2 in Q(zeta),2 is unramified/inert (the same irreducibility and2!=5 give the ordinary cyclotomic local ring with uniformizer2). Write its integral valuation as v_2. Taking determinants in the exact identity gives

    detH*conj(detH)=10^10.

The prime is unique and conjugation preserves it, so2*v_2(detH)=10, i.e. v_2(detH)=5. If the reduced matrix had rankr<5, lifted row elimination would give at least10-r>5 factors of2 in detH, contradiction. Hence rank exactly5. Each original context therefore determines a MAXIMAL totally isotropic5-space overF16, with ten distinct projective points from its prescribed phase-torus alphabet.

Named classical arithmetic input here is the standard cyclotomic ring/local-prime fact: O is the integer ring, the prime2 is unramified and inert because Phi5 is irreducible mod2. The operative conjugation/valuation/rank calculation is printed. No Smith-form program, field package or scientific interpreter was used.

## 5. Distinctness survives reduction; orthogonality does NOT become an iff

The order5 roots inject into F16. If two reduced phase vectors are projectively proportional overF16, their first-coordinate ratio lies in the order5 subgroup, so ALL exponent differences are the same constant inF5. They were therefore already the SAME complex ray. Thus100-ray distinctness is EXACTLY100 distinct reduced projective phase-torus points, not just a heuristic hash.

But finite Hermitian orthogonality is STRICTLYWEAKER than complex orthogonality. If the ten difference counts are n_0..n_4, finite orthogonality says sum(n_j mod2)t^j=0. Irreducibility of Phi5 forces all five parities equal; since their sum has even parity10, they must ALL beEVEN. Hence

    finite Hermitian orthogonality IFF every n_j is even;
    ACTUAL complex orthogonality IFF every n_j is2.

For example counts(4,2,2,2,0) satisfy the finite condition but NOT the complex one. This is a written negative-control profile, not an executed check. Distinct reduced points inside common isotropic5-spaces alone therefore do NOT produce an original quantum ONB or witness. The balanced-difference/GH-code conditions must remain literal acceptance conditions.

Nor is it assumed that two original contexts intersecting in one actual ray have distinct reduced5-spaces or intersect only in that line. Those stronger finite-geometric assertions have not been proved.

## 6. Exact replacement task and assurance

This supplies TWO compatible representations of the new phase5 branch: an EXACT500-word/three-GH-partition/Latin-placement master, and a sharp necessary F16 Hermitian5-space geometry with exact distinctness but explicitly weaker orthogonality. It is not a numerical search recipe declared successful, nor a finite-field substitute for the original complex target.

A genuine solution needs the literal100 phase classes, ANY valid full Latin resolution L and ALL thirty GH balance tables, together with100-ray distinctness. Alternatively one must rule out the entire exact code/partition model, not merely a linear-code or generic finite-point subcase. No such table or contradiction is supplied here; phase5 and the general original problem remain OPEN.

An entire gate must reconstruct ALLsix sections/endings: both directions of the OA equivalence, the three actual placement/partition constraints, all mixed-OA multiplicities, the cyclotomic local-rank argument, reduction injectivity and the finite-versus-complex counterprofile. A finite Hermitian clique or one OA50 is not an accepted100-ray result. No external classifier or unprovided field-code output is operative.

No100-ray1-RQLS witness/unrestrictedno-go/formal/kernel/family/human/current-openness/novelty/finite-witness gate promotion. All statements are AUTHOR-WRITTEN candidates pending complete mathematical/dependency/application review. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues this genuinely different exact GH-code geometry or a full-master construction, no early pending-review park.
