# v41-E — PH8-to7 invariant compression obstruction, fully written reconstruction

**Reviewer:** PhysicsRQLS10-2, physics-5. **Author:** MathResearch96h. Actual pre-write `/bin/date`: **Sun Oct 25 05:54:18 PDT 2026**.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR at the exact real full-rank intertwining-QUOTIENT scope defined below.** The displayed quotient, boundaries, transfer, fixed hidden quadratic and uniform shifted trace-square obstruction are reconstructed. No load-bearing identity in that theorem remains NOT_RECONSTRUCTED. This does NOT establish infeasibility for all PH7 realizations, all five orbit representatives, arbitrary non-intertwining reductions or every PH8 realization of the target.

Strict written reconstruction only. No scientific interpreter, eval, symbolic/arithmetic program, enumeration, solver, sampled matrix check or certificate replay was used. Metadata clocks/hashes and literal source reading only. No scientific GO exists or is inferred.

## 1. Exposure, complete reading and current authority

Parent erratum v8 was read FIRST, all LF1–37, SHA256 `52408180ac48dec69d2144ea0dee07acf08f0739f65a8cdb2b007656243527e9`. In particular its LF19–21 identifies this compression claim as an unreviewed author successor, not an accepted parent theorem. Its withdrawal of premature coverage/acceptance is respected; no prior headline supplies proof here. V7's no-execution exception remains withdrawn.

The pre-body ACK is `peer-review-ph8-to7-compression-obstruction-ack-v1.json`, observed **Sun Oct 25 05:50:13 PDT 2026** and written before opening the proof body. No prior review was actually pending; the primary was safely settled in park-v6.

- Manifest: `peer-review-wave-eighteen-v41.json`, exact entry LF130–151, SHA256 `cd45439a2c5171a355e66dc75aca29a7d100f784837cb4affbc2b8c3ded732bf`.
- Packet receipt: `peer-review-wave-eighteen-v41-packet-receipt-v1.json`, ALL LF1–37, SHA256 `8d477259c3dd08f474ebcbe405a8b1847b843160fee766d97bd58169da2cd2e0`, recording literal equality.
- Full literal packet: `peer-review-wave-v41-ph8-to7-compression-obstruction-sources-v1.md`, ALL LF1–129 read, SHA256 `cc147920d2e3f2424e14a4de611f88add70d45faac54b5842cb4e35d42d1352d`.
- **S**, the entire declared source: `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-eight-ninths-one-state-compression-obstruction-v1.md`, ALL LF1–120, SHA256 `32bf6ec2fb9c0113415c2dab92e4a1bdaafaa35579cb2110f0085431843b0a59`. Fresh metadata hashes match all frozen pins.

Long/load-bearing packet lines explicitly reread with `:raw`: LF11,15,17,21,23,43,55,67,73,79–85,98–100,104–120,124–128. Citations below are source S line numbers; packet line number is S LF+8. No unseen earlier PH8 manuscript is described as completely read.

## 2. Literal companion, complete characteristic factorization and transfer

### 2.1 Deriving the coefficients, not copying a target polynomial — S:15–35

For an n-state companion with superdiagonal1 and last row `(a0,...,a_(n−1))`, its characteristic polynomial is `Y^n−a_(n−1)Y^(n−1)−...−a0`. Thus the displayed last row gives the source p8 directly.

Independently expand the visible factor. First

    (Y²−2Y+9)²=Y⁴−4Y³+22Y²−36Y+81,

and therefore

    F(Y)=(Y−4)(Y²−2Y+9)²
        =Y⁵−8Y⁴+38Y³−124Y²+225Y−324.

Multiplying F by `q3=Y³+8Y²+26Y+28` yields the following actual coefficient groups:

    Y⁸: 1,
    Y⁷: 8−8=0,
    Y⁶: 26−64+38=0,
    Y⁵: 28−208+304−124=0,
    Y⁴: −224+988−992+225=−3,
    Y³: 1064−3224+1800−324=−684,
    Y²: −3472+5850−2592=−214,
    Y¹: 6300−8424=−2124,
    Y⁰: −324*28=−9072.

Also `(Y+2)(Y²+6Y+14)=Y³+8Y²+26Y+28`. These derivations bind the entire factorization to the LITERAL companion coefficients. In particular the only real eigenvalues are4 and−2; the other roots are1±i sqrt(8), each twice, and−3±i sqrt(5), each once. No sampled determinant or copied coefficient triangle is used.

Solving `(YI−C8)x=e8` successively along the first seven rows gives

    (YI−C8)^(-1)e8=(1,Y,...,Y⁷)^T/p8(Y).

Consequently the displayed beta8 and gamma8 give exactly

    H=K q3(Y)/p8(Y)=K/F(Y).

The factor Y−4 is a genuine visible simple pole: K>0, and the other visible quadratic is nonzero at4. The same is true of its repeated nonreal poles. The transfer has no remaining numerator cancellation and McMillan degree five, not eight.

### 2.2 Raw stability and positive normalization

With lambda=c+4 and c>0, every eigenvalue of M8=C8−lambda I has negative real part by the factorization above. Its off-diagonal coefficients are nonnegative, so it is Metzler/Hurwitz. Moreover

    F(lambda)=c[(c+3)²+8]²=K,
    p8(lambda)=K q3(lambda).

The raw normalizer can be derived explicitly rather than imported unseen:

    h8=(lambda I−C8)^(-1)gamma8
       =(1,lambda,...,lambda⁷)^T/q3(lambda)>0.

Then beta8 h8=1, and `−M8 h8=gamma8`. The positive diagonal normalization therefore has a probability initial row and the correct exit/row ties. This verifies the literal PH8 anchor at this point from the supplied data; it does not re-review the old proof's entire parameter family or upper-bound history.

**Boundary verdict:** 0F/0M/0m.

## 3. Reachability, observability and what is actually minimal

This distinction is important for S:7,35,110; the eight-state realization must NOT be assumed both reachable and observable.

For k=0,...,7, the vector `C8^k e8` has leading coefficient1 at e_(8−k) and only higher-index terms. This follows inductively from the companion columns `C8 e_j=e_(j−1)+a_(j−1)e8` for j>1. Thus gamma8, which is a nonzero scalar times e8, reaches the whole eight-dimensional space.

On the other hand, `e1^T C8^k=e_(k+1)^T` for k=0,...,7, and

    beta8=e1^T q3(C8).

Hence a vector x is unobservable from beta8 exactly when `q3(C8)x=0`: the forward direction tests all eight rows `e1^T C8^k q3(C8)`, while the reverse direction is immediate. The three distinct roots of q3 are disjoint from F and each is simple in p8, so this unobservable subspace has dimension three. In particular the eigenvector at−2 is unobservable. It is not an unreachable state that was silently deleted.

The reduced target transfer is degree five; neither this eight-state anchor nor its seven-state signed quotient is a minimal linear realization. The uniform quotient argument below does not require either to be observable. It uses the genuine visible pole4 and the full-rank invariant quotient condition, not an invalid minimal-eight-state premise.

**Boundary verdict:** 0F/0M/0m. The prior PH minimum set{7,8} remains an imported problem boundary, not a consequence of this linear-realization degree calculation.

## 4. Explicit rank-seven quotient and every boundary identity

### 4.1 Rank, invariant kernel and matrix entries — S:39–65

P is upper bidiagonal rectangular, with2 on its first seven diagonal entries and1 immediately to their right. Its first seven columns form an invertible triangular matrix, so rank P=7. The recurrence `2v_i+v_(i+1)=0` gives exactly

    ker P=span_R{(1,−2,4,−8,16,−32,64,−128)^T}.

The first companion rows give C8 v=−2v there; the last follows from the derived factor Y+2 in p8. Therefore ker P is invariant and there is a unique quotient matrix A7 satisfying P C8=A7 P.

For the first six rows, `P_i C8=P_(i+1)`, giving the six superdiagonal1 entries. For the final row, multiplying `(4536,−1206,710,−13,8,−4,2)` by P gives the coordinate expressions

    2*4536=9072,
    4536−2*1206=2124,
    −1206+2*710=214,
    710−2*13=684,
    −13+2*8=3,
    8−2*4=0,
    −4+2*2=0,
    2.

This is exactly `2e8^T+lastrow(C8)=P_7 C8`. Thus every displayed quotient entry is derived by the actual intertwining identity, not inferred from desired eigenvalues.

Its companion characteristic is the stated p7. Multiplying by Y+2 gives coefficient groups

    1; −2+2; 4−4; −8+8; 13−16;
    −710+26; 1206−1420; −4536+2412; −2*4536,

which are exactly the p8 coefficients derived in Section2. This proves the complete division and characteristic binding.

### 4.2 Boundaries and the entire transfer — S:67–77,92

Directly

    (14,6,1,0,0,0,0)P
      =(28,14+12,6+2,1,0,0,0,0)=beta8,
    P(K e8)=K e7.

The resolvent intertwining

    (YI−A7)^(-1)P=P(YI−C8)^(-1)

therefore proves equality of the two scalar transfer functions. Cancelling Y+2 yields `K(Y²+6Y+14)/p7(Y)`, equivalently K/F(Y). Neither the initial nor exit boundary is missing or chosen independently of the matrix.

Furthermore h7=P h8 is strictly positive, `−(A7−lambda I)h7=gamma7`, and beta7 h7=beta8 h8=1. This is a valid positive normalization of a SIGNED realization. It does not make negative off-diagonal entries positive.

### 4.3 Common 3+3 block location — S:81–92

With R={1,2,3}, o=4, S={5,6,7}, the first three states form the upper-shift J_lambda; b=e3 links state3 to4 and t=e1 links4 to5. The last row supplies D=(4536,−1206,710) only on its third S row, f3=−13, and F last row `(8,−4,2−lambda)`, with its two superdiagonal1 entries. The initial row is (14,6,1) on R and the exit is K at state7. Thus the displayed common blocks really are from one matrix, with D32, f3 and F32 negative. Positive diagonal similarity preserves those off-diagonal signs.

**Boundary verdict for the complete literal quotient, blocks, transfer and normalization:** 0F/0M/0m.

## 5. The shifted trace-square obstruction, including arbitrary real bases

### 5.1 Direct identity — S:96–108

For any real Metzler B,

    tr(B²)=sum_i B_ii²+2sum_(i<j) B_ij B_ji>=0.

This uses only the nonnegative OFF-diagonal entries; no sign of the diagonal is assumed. Adding ANY real scalar multiple of the identity preserves the Metzler property, so the same necessary inequality applies after any real scalar shift.

For the explicit A7, the last diagonal contributes2²=4. The only nonzero two-cycle is6↔7, with product1*(−4); all other reverse superdiagonal entries are zero. Therefore `tr(A7²)=4−8=−4`. This is also Newton's identity from its first two characteristic coefficients: tr A7=2 and tr(A7²)=2²−2*4.

If a real similarity of M7=A7−lambda I were Metzler, adding lambda I would give a Metzler real similarity of A7, contradicting this invariant. The source does NOT need, and does not claim, `tr(M7²)=−4`; the negative invariant is for the correctly SHIFTED matrix A7. This distinction prevents an incorrect application to the unshifted generator.

### 5.2 Uniformity over ALL full-rank real intertwining quotients — S:110–112

Precisely, let L be ANY real7-by8 matrix of rank seven, and let A be any real7-by7 matrix with

    L C8=A L.

Then ker L is a real invariant line of C8 and carries a real eigenvalue r. Choosing a real basis beginning with that line block-triangularizes C8, and its seven-dimensional quotient block is similar to A. Therefore, WITHOUT any diagonalizability assumption,

    p8(Y)=(Y−r)det(YI−A),
    tr(A²)=tr(C8²)−r².

The only possible real r are4 and−2 by the full factorization. If the quotient preserves the target transfer, r=4 is impossible: it would remove the sole algebraic copy of4 from det(YI−A), so no transfer generated by A could have the target's genuine simple pole at4, regardless of its boundaries. This is not an unsupported claim that removing every visible or hidden mode is interchangeable.

Consequently r=−2, every such quotient has characteristic p7, and the same negative trace-square follows. Directly C8 has zero diagonal and no nonzero two-cycle, so `tr(C8²)=0`; thus `tr(A²)=−(−2)²=−4`. The conclusion is independent of which invariant kernel/basis L was chosen and even allows L to have negative entries. Full rank and exact intertwining are essential hypotheses.

In particular it applies to every putative positive state-coordinate quotient of the specific anchor and to its real similar PH normalization. This is genuinely a uniform quotient obstruction, not an inference from the signs of the single displayed P/A7.

**Boundary verdict:** 0F/0M/0m.

## 6. Exact quotient/subspace scope and the fixed hidden-pair consequence

A codimension-one REAL INVARIANT SUBSPACE restriction of C8, if separately specified and preserving the same target, has the same characteristic-factor argument: a real one-dimensional complementary quotient carries r, so the restriction's characteristic is p8/(Y−r), and the visible pole again forces r=−2. This is the same elementary invariant-block reasoning, not a statement that an arbitrary oblique compression is an invariant restriction.

By contrast, an arbitrary L C8 R with L R=I, a non-invariant state elimination, a nonlinear transformation, or an unrelated PH7 realization need not have a degree-one characteristic factor removed from p8. Those broader mechanisms are NOT proved impossible here. Nor does the argument classify all positive8-state realizations of H.

For any other seven-state realization whose shifted characteristic is EXACTLY p7, the negative trace-square remains basis/topology independent. Thus the particular remaining hidden quadratic `Y²+6Y+14` is genuinely excluded even if a realization with that same characteristic was not obtained by the displayed quotient.

The normalized d=1 form is derived, not merely copied. Time-scaling the d=3 units gives `Y=3y+4`; substituting into that hidden quadratic yields

    (3y+4)²+6(3y+4)+14=9y²+42y+54
      =9[y²+(14/3)y+6].

Positive time scaling preserves the sign of the corresponding shifted trace-square. It does NOT constrain other hidden quadratics, their coefficients, or their root locations.

## 7. Unreconstructed non-premises and final disposition

**NOT_RECONSTRUCTED here:** the complete earlier PH8 parameter-family manuscript, its full historical reviews and upper-bound region; the earlier PH7 lower-bound/exact-band proofs; all-five-orbit feasibility; or a theorem excluding every possible degree-two cancellation. These are not concealed load-bearing premises for this quotient obstruction. The supplied literal anchor and all its needed identities were derived above. The previously stated minimum set{7,8} is preserved at its prior import boundary, not newly proved by this review.

At the reviewed scope, the source correctly closes the mechanism “delete one real hidden mode by an exact real full-rank intertwining quotient of THIS anchor”: it cannot yield a Metzler seven-state realization in any real basis. It also excludes the same fixed remaining hidden pair. It does not settle unrestricted PH7 existence at8/9, the entire3+3 orbit, other time-reversal representatives or any other canceled quadratic. No new PH7 witness or exact interval is supplied.

Parent v8's prior premature acceptance is not backdated by this review. This is a new complete same-harness cross-domain written reconstruction for the exact stated theorem; parent integration remains separate. No formal/kernel, human, cross-vendor, executable-certificate or novelty acceptance, and no new scientific permission. All frozen source/author files remain unchanged.
