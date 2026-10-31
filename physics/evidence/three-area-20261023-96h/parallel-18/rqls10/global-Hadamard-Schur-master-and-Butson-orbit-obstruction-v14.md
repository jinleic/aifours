# RQLS10 v14 — a different Hadamard-Schur master and a complete monomial-orbit support obstruction

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 05:57:28 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact symbolic/fraction/integer-product and graph arguments only; no interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no decimal/private approximate scout or old-probe backconversion. No machine/kernel/formal/human/configured-family/novelty acceptance.

Original unrestricted maximal1-RQLS(10) remains UNKNOWN. Unlike v13's single-Weyl-fiducial representation, this route uses an ARBITRARY complex Hadamard basis. No cyclic covariance of its rows is imposed. It is still an ANSATZ, not a WLOG theorem for all1-RQLS10. No companion pair satisfying the final noncollision condition has been supplied.

## 1. New exact constructive master

Let omega=exp(2*pi*i/10), Z=diag(omega^k), and let H be a10x10 matrix with unit-modulus entries. Write F10 for the UNNORMALIZED Fourier matrix, (F10)_jk=omega^(j*k). Define

    q_(i,j)(k)=omega^(i*k)*H_jk/sqrt10,
    R=H entrywise-multiplied by F10.                  (HMASTER)

**Theorem A.** H and R are complex Hadamard matrices iff (HMASTER) has every row, column and cyclic designated class j-i=t an actual ONB. Its cardinality is100 iff

    row_j(H) is NOT proportional to Z^m row_j'(H)
           for every j!=j' and every m mod10.        (NONCOLLISION)

Proof. Fix j. Its ten vectors Z^i row_j(H)/sqrt10 form an ONB because the row is flat and the Fourier character sums vanish. Fix i. Its ten vectors are the same diagonal unitary Z^i applied to the H row basis, so form an ONB iff H is Hadamard. In class j-i=t, relabel by j to obtain Z^(-t)*(Z^j row_j(H))/sqrt10. These are one common unitary applied to the R row basis, so all TEN designated classes are ONBs iff the SINGLE matrix R is Hadamard. There are not ten independent extra tests.

Within a fixed j, the vectors are orthonormal and therefore distinct rays. Any cross-j collision is exactly the forbidden relation in NONCOLLISION. Conversely every such relation repeats rays in the array. Thus all original ONB, normalization and nonparallelness requirements are explicitly accounted for. No genericity assertion replaces NONCOLLISION.

This is not a single Weyl-orbit requirement on H: its ten row vectors may be unrelated except for the two matrix identities. A genuine solving H would directly produce an actual maximal1-RQLS10, not merely a spectral tuple.

## 2. A necessary SAME-H zero-pattern matching

Put J=diag((-1)^k) in the PHYSICAL Fourier column order, and

    S=(1/10)*H*J*H^dagger.

S is a Hermitian unitary involution with diagonal0 for every Hadamard H. If R is Hadamard, its physical row pairs j,j+5 require

    0=(1/10)*sum_k (-1)^k H_jk conj(H_(j+5),k)
      =S_(j,j+5).

Thus the SIMPLE zero graph of S (distinct row vertices, edge iff the entry is zero) must have a PERFECT MATCHING covering all10 vertices.

Under an arbitrary row permutation this graph is merely relabeled; row phases do not change its zeros. Under a column permutation, J becomes an arbitrary balanced sign diagonal with FIVE plus and FIVE minus entries. Column phases commute with J and do not change this zero graph. Consequently:

**Theorem B.** If for EVERY balanced5/5 column split the SAME-H zero graph has no perfect matching, then NO matrix monomial-equivalent to H can have a Fourier-Schur companion. This includes ALL row/column permutations and arbitrary unit row/column phases. The criterion is necessary, not sufficient if a perfect matching does exist: all other row differences of R still matter.

There is no search or computational matching algorithm here. The next sections prove failure symbolically for whole classes.

## 3. Entire full-support McNulty-Weigert blocks in the aligned split

Let F,L,K be p-dimensional unitary matrices, with p ODD, such that

    W=(1/sqrt2)*[[F,L],[K^dagger F,-K^dagger L]]

has flat entries. It is unitary directly by block multiplication. If EVERY entry of K is nonzero, then

    W*diag(I_p,-I_p)*W^dagger=[[0,K],[K^dagger,0]].    (BLOCK)

Its zero graph consists of two DISJOINT odd p-vertex cliques and no cross edge. It has no perfect matching. Therefore in any physical column ordering whose Fourier parity split agrees with those two p-column blocks, NO row permutation or arbitrary row/column phasing can give W a Fourier-Schur companion. Arbitrary column permutations within or exchanging the blocks are included.

This proof is independent of the phases, Gaussian status or numerical entries of K,F,L. It does NOT cover a balanced split mixing the two blocks differently. In particular, it is not a declaration that every McNulty-Weigert matrix has been excluded under every equivalence. The explicit model next permits that stronger all-split proof.

## 4. A completely specified BH(10,5) model

Let zeta=exp(2*pi*i/5). Index rows by T_i or B_k (i,k in F5), and columns by(0,j) or(1,j). Define the unit-entry matrix H0 by

    H0_(T_i),(0,j)=zeta^(i*j),
    H0_(T_i),(1,j)=zeta^(3i^2+i*j),
    H0_(B_k),(0,j)=zeta^(4(j-k)^2),
    H0_(B_k),(1,j)=zeta^(2(j-k)^2).                  (MODEL)

H0 is Hadamard by a written block identity. Take the normalized F5, K=diag(zeta^(j^2))*F5 and L=diag(zeta^(3j^2))*F5. Then H0/sqrt10 is the matrix W in Section3. The exact quadratic Gauss sum gives K^dagger F5 entries zeta^((j-k)^2/4)/sqrt5; since1/4=4 in F5 this is the third block in MODEL. The coefficient2=3-1 is a nonsquare, so -K^dagger L entries are zeta^(2(j-k)^2)/sqrt5, the fourth block. Unit-modulus entries and W's block unitarity prove H0*H0^dagger=10I. No literal-table checker is run.

The following theorem concerns the ENTIRE monomial equivalence orbit of THIS explicit model. No unprovided classification that all BH(10,5) matrices lie in it is assumed.

## 5. Complete all-column-split obstruction for H0

**Theorem C.** For EVERY balanced sign diagonal J, the zero graph of H0*J*H0^dagger has NO perfect matching. Hence NO monomial-equivalent H can have H entrywise-multiplied by F10 Hadamard, even before asking for maximal cardinality.

### 5.1 Exhaustive balanced-split form

Changing J to -J leaves its zero graph unchanged. Therefore the plus columns can be written

    (0,j) with j in A,
    (1,j) with j NOT in B,
    |A|=|B|=a<=2.

This covers ALL balanced splits: if its first block contains more than2 plus columns, take the complement. Here B is a missing-column set in the second block, not a set of rows. No subset instance is evaluated or sampled.

For a distinct row pair, write L0(j),L1(j) for its two exponent differences. Since the full row inner product is zero, its J-twisted inner product vanishes iff the plus-column sum vanishes. This sum is

    sum_(j in A) zeta^L0(j)
      -sum_(j in B) zeta^L1(j)
      +sum_(j in F5) zeta^L1(j).                    (PART)

A polynomial in zeta with integer coefficients and coefficient sum0 can vanish only if all coefficients are0: its degree<=4 representative must be a multiple of1+x+x^2+x^3+x^4, and the coefficient-sum condition makes that multiple zero. This exact fact will compare phase multisets.

### 5.2 Cross-row zeros for a=0 or1 are impossible

For the top row T_i and bottom row B_k, direct expansion of MODEL gives

    L0(j)=j^2+(i+3k)j+k^2,
    L1(j)=3j^2+(i-k)j+3i^2+3k^2
         =3(j+i-k)^2+i*k.

The full second-block character sum is -sqrt5*zeta^(i*k), by the nonsquare coefficient3. Thus a cross zero would require

    sum_A zeta^L0(j)-sum_B zeta^L1(j)
        =sqrt5*zeta^(i*k).                          (CROSS)

For a=0 this is impossible. For a=1 the left side has modulus at most2 whereas sqrt5>2. Hence for either a=0 or1 the zero graph has NO cross T/B edge. Each half has ODD size5, so no perfect matching exists, regardless of its internal zero edges.

### 5.3 At a=2, cross zeros can involve ONLY T_0

The exact identity

    sqrt5=zeta+zeta^-1-zeta^2-zeta^-2

has coefficient sum0. CROSS and the phase-multiset fact from Section5.1 therefore force

    { L0(j)-i*k : j in A }={1,-1},
    { L1(j)-i*k : j in B }={2,-2},                  (PHASE-SETS)

with no repeated or cancelling phase allowed. There are precisely two positive and two negative terms on either side; coefficient equality leaves no hidden extra multiple of the cyclotomic polynomial.

But

    L0(j)-i*k=(j-k)*(j+i-k).

With t=j+i-k, this is t*(t-i). To attain BOTH values+1 and-1, both quadratic equations must have roots, so BOTH discriminants i^2+4 and i^2-4 must be quadratic residues (zero included) in F5.

For nonzero i, i^2 is either1 or4. At i^2=1 the second discriminant is2, a nonsquare. At i^2=4 the first discriminant is3, a nonsquare. Therefore PHASE-SETS is impossible for EVERY i!=0. All possible cross zero edges are incident to the SINGLE top vertex T_0. This is a symbolic all-i obstruction, not a table of tested pairs. No assertion that every possible T_0 edge actually exists is needed.

### 5.4 At a=2, at least one half has NO internal edges

For two distinct top rows T_i,T_l, set d=i-l!=0 and sigma=i+l. Their differences are

    L0(j)=d*j, L1(j)=d*j+3d*sigma.

The full second-block sum is0. PART and phase-multiset equality imply

    A=B+3sigma as SETS.

Thus a top internal zero edge can occur only if the two-element sets A,B have the SAME gap, up to sign.

For two distinct bottom rows B_k,B_l, with d=k-l and sigma=k+l, the differences are

    L0(j)=2d*j+4d*sigma,
    L1(j)=d*j+2d*sigma.

Its internal zero condition similarly implies

    2A+2sigma=B as SETS.

Thus a bottom internal zero edge can occur only if the gap of B is TWICE the gap of A, up to sign. A nonzero F5 gap cannot simultaneously have both types: up to sign the two possibilities are exactly1 and2. In particular at least ONE row half has NO internal zero edge.

If the top half has none, its four vertices T_i with i!=0 have no incident zero edge at all, by Section5.3. If the bottom half has none, ALL FIVE bottom vertices would have to match across, but cross edges can use only T_0. Either way a perfect matching is impossible.

This completes ALL a=0,1,2 and hence ALL balanced5/5 splits. Theorem B now proves Theorem C for every row/column permutation and arbitrary row/column phases of H0. Neither a favorable column ordering nor a different dephasing can evade the obstruction.

## 6. A second whole-family obstruction: phased tensor-Fourier matrices

For completeness, another common construction route is ruled out in its full phase/row-permutation scope, rather than assuming it lies in H0's class. In standard CRT column order(t,l), take

    H_(s,r),(t,l)=(-1)^(s*t)*zeta^(r*l)*d_r^t,
    s,t in Z2, r,l in F5, arbitrary |d_r|=1.

This is a Hadamard matrix. Allow ANY permutation assigning its ten rows(s,r) to physical Fourier row labels j. The companion row becomes a qubit vector with relative phase(-1)^(s+j_parity)*d_r, tensored with the pentit Fourier character of frequency r+3*j_mod5.

An ONB of ten such rows requires EXACTLY2 orthogonal rows in each of the five2-dimensional frequency sectors. A pair with the same r would also have the same j_mod5; distinct physical labels then have opposite parity and the original s labels are opposite, so their qubit phases agree. They are parallel and cannot form the pair.

Thus sector pairings give a loop-free degree2 graph on the five r-labels. Orient its cycle components (a two-edge component is allowed). The qubit orthogonality condition on each edge is

    d_r/d_r'=-(-1)^(s+s'+j_parity+j'_parity).

Multiplying around all five directed edges cancels every d_r. The right side is(-1)^5 times(-1)^(sum_all_rows s+sum_all_labels j_parity). Both sums are5, so it is-1, whereas the left side is1. Contradiction. This covers arbitrary d_r, row permutations and row/column phases in this standard column ordering; arbitrary non-affine column permutations mixing the two parity sectors are NOT covered by this separate tensor argument. The all-column theorem for H0 was proved independently above.

## 7. Public source context and exact unresolved mathematics

Static source reads found known order10 Hadamard material, but none is a witness claim here:

- Egan–Flannery–Ó Catháin, *Classifying cocyclic Butson Hadamard matrices* (2015), opening/Example3.5 read from the [primary PDF](https://doras.dcu.ie/29112/1/EganFlanneryOCathainArxiv.pdf), discusses a computer-established equivalence between an S10 matrix and Butson's construction.
- Their [current author catalogue](https://www.daneflannery.com/classifying-cocyclic-butson-hadamard-matrices) links literal BH10_10 data, which was read as text only. Its algorithmic equivalences/class counts were NOT executed, independently certified or adopted as a complete classification of all complex Hadamard matrices. The obsolete BHIndex link redirects to the author's homepage.

MODEL is independently specified/proved above; no catalogue equivalence is needed for its orbit obstruction. In particular this manuscript does NOT claim that every BH(10,5), every BH(10,10), every McNulty-Weigert matrix or every complex Hadamard is monomial-equivalent to MODEL. A separate equivalence proof would be required before transferring Theorem C to any differently named catalogue representative.

The genuinely new remaining constructive question is an arbitrary H satisfying BOTH Hadamard identities and NONCOLLISION, outside the uniformly excluded classes. The same-H zero graph must have a perfect matching for at least one balanced column split, but that necessary condition alone does not suffice for the full companion. No actual companion or100-ray array is supplied. The asymmetric coupled rank3/4 master of v13, the dihedral/free-MASTER/trine routes and the unrestricted original problem remain open separately.

## 8. Evidence-format qualification and assurance

The `observed_bin_date_verbatim` field in `checkpoint-v14-Hadamard-Schur-master-v1.json` normalized spaces as `Mon Oct26 05:51:11 PDT2026` while labeling itself verbatim. That lexical claim is withdrawn: the ACTUAL returned string was `Mon Oct 26 05:51:11 PDT 2026`. The clock value was observed, not invented, but the old field is not a verbatim copy. This additive qualification does not change that file or backdate any proof/checkpoint; it is a metadata transcription correction, not a mathematical or scientific-execution claim.

All previous process/source/clock/cadence/freeze/admission findings, the v9 proof-gap correction and ZERO-credit quarantines remain permanent. No clean-thought/runtime/census claim, novelty/priority/SOTA promotion, external publication, actual finite-witness certification, new owner/deadline or scientific GO follows. Same original18/exclusive root/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and at-most30min substantive actual-clock cadence. This is a fresh written representation and full orbit obstruction, not a final park because earlier gates are pending.
