# Bounded mathematical reconstruction — unrestricted four-qubit central indices

Reviewer: MathSemigroup, actual math-4 owner. Clock observed immediately before creation: **2026-10-23T14:59:50-0700**.

## Verdict, pin and read scope

**FATAL0 / MAJOR0 / MINOR0 at the theorem's exact stated mathematical scope.** I found no substantive defect in the universal central-index proof, including its embedded H4 lemma. This is a separate in-harness supplied-proof reconstruction for parent consideration, not automatic parent acceptance, formal/kernel proof, human review or priority clearance.

Complete source read, lines1–163:

`physics/evidence/three-area-20261023-96h/parallel-18/depolarizing-majorization4/proof-unrestricted-central-indices-v1.md`

Observed SHA-256:

`10e4689c7ac8586fc920651eade6db37fa60be3b693f73b5f4ec7b6644fe6d23`.

This matches the requested pin. H4 is fully stated/proved in that same source, lines65–105; its entire pair-variable argument is reconstructed below. Also read the exact current selection, the inherited frozen PROOF and operative ADDENDUM, and the actual stored review. No author files changed and no scientific executable, arithmetic script, eigensolver, enumeration, optimizer, compilation or certificate replay was used. Only source reads, actual clocks and SHA metadata operations occurred.

## 1. Conventions and strongest scope being checked

The maps use **unnormalized** identity factors:

    X_s(rho)=sum_(|I|=s) rho_I tensor I_(I^c),
    D_p(Y)=(1-p)Y+(p/2)Tr(Y)I.

The new claim is K_k(X2)<=k+13 for every four-qubit density matrix, k=6,...,10. Its channel consequence is those five partial sums for every physical replacement p in[0,4/3]. The full high-noise interval additionally composes the explicitly inherited package; the low-noise k=2,3,4 obligations remain. Neither the broad quantum-capacity problem nor general n is claimed.

I checked the all-state quantifier directly. No moment, rank, pure-state, constant marginal spectrum, compatible-marginal ansatz or Pauli-Gram tightness hypothesis is used in the new proof.

## 2. Operator inequality and its direction — source lines27–63

For any qubit-versus-rest pure state, write

    psi=sqrt(mu)|0,alpha>+sqrt(nu)|1,beta>.

For an arbitrary test vector z, let A=<0,alpha|z> and B=<1,beta|z>. The elementary inequality

    |sqrt(mu)A+sqrt(nu)B|^2
       <=2mu|A|^2+2nu|B|^2
       <=2<z|I_i tensor rho_rest|z>

proves rho<=2(I_i tensor rho_rest). This includes a zero Schmidt coefficient. Every mixed state is a convex combination of pure states, and both sides depend linearly on rho; hence the same operator inequality holds for arbitrary mixed rho. Summing over four choices of i yields

    X3>=2rho.

Tensoring the exact qubit reduction identity R(Y)=sigma_y Y^T sigma_y=Tr(Y)I-Y gives

    rho_tilde=I-X1+X2-X3+rho.

The transpose here is **global**, so rho_tilde is positive trace one for arbitrary rho. Therefore

    X2=X1-I+(X3-rho)+rho_tilde
       >=X1-I+rho+rho_tilde
       >=X1-I.

The inequality direction is correct: the positive surplus is discarded on the LOWER-bound side. X2 is separately positive, and each of its six marginal summands has trace4, so Tr(X2)=24.

After independently diagonalizing the four one-qubit marginals, their commuting Kronecker-sum terms give

    X1-I=I+(1/2)sum_i t_i sigma_z^(i),  0<=t_i<=1.

Thus its ordered eigenvalues are1+eta_j/2. Weyl monotonicity in descending order gives lambda_j(X2)>=1+eta_j/2, and positivity separately gives lambda_j(X2)>=0. Combining these SCALAR inequalities yields max(0,1+eta_j/2). No false operator claim about taking positive parts is used. The half coefficient improves the useful negative-tail scalar bound relative to the cited earlier Weyl route; no global dominance over that other operator bound is needed or asserted.

## 3. Full independent pair-variable reconstruction of H4 — lines67–105

Order t1>=t2>=t3>=t4>=0. Set

    A=t1+t2, B=t1-t2, C=t3+t4, D=t3-t4.

The constraints needed in the proof follow directly:

- A>=C>=D>=0;
- A+B=2t1<=2;
- B+C=t1-t2+t3+t4<=t1+t2=A because t3+t4<=2t2;
- B+D<=B+C<=2.

The first pair of signed variables has sums ±A,±B; the second has ±C,±D. Their combinations give exactly four sets ±A±C,±A±D,±B±C,±B±D. Each set pairs with its negatives. Hence the eight nonnegative magnitudes, counted WITH multiplicity, are exactly

    |A+C|,|A-C|,|A+D|,|A-D|,
    |B+C|,|B-C|,|B+D|,|B-D|.

This remains valid when entries vanish or several magnitudes agree; no generic-position assumption is present.

Write L(x,y)=min(x+y,2)+min(|x-y|,2). Since B+C,B+D<=2,

    L(B,C)=2max(B,C), L(B,D)=2max(B,D).

For y=C or D, A>=y and A-y<=2, so

    L(A,y)=min(A+y,2)+A-y.

This is nondecreasing as A increases: its slope is2 before clipping and1 after clipping. Increase A to A'=2-B. It is at least A and still at least C,D; A'-y remains in[0,2]. The two exact cases are:

- y<=B: A'+y<=2, so L(A',y)=2A'=4-2B;
- y>=B: A'+y>=2, so L(A',y)=2+A'-y=4-B-y.

Together these say

    L(2-B,y)=4-B-max(B,y).

Adding all four pairs, the clipped sum is bounded by

    [4-B-max(B,C)]+[4-B-max(B,D)]
        +2max(B,C)+2max(B,D)
      =8-2B+max(B,C)+max(B,D)
      <=8-2B+(B+C)+(B+D)
      =8+C+D=8+2t3<=10.

This is the whole H4 engine, valid on the full cube. It neither samples signs numerically nor assumes purity constraints on the four Bloch lengths. The equality family t1=t2=t3=1, t4 arbitrary is consistent: A=2,B=0,C+D=2, giving exactly10.

## 4. Bottom tails and all central indices — lines109–131

The sixteen eta values pair as eta_(17-j)=-eta_j. Choose their nonnegative half a1,...,a8, with zero ties assigned consistently. The scalar lower bounds at the eight nonpositive eta positions have total

    F=sum_i max(0,1-a_i/2)
      =8-(1/2)sum_i min(a_i,2)>=3.

Each of these eight scalar numbers is at most1. For a bottom tail of m=6 or7, it omits8-m of those scalar positions. Their omitted lower-bound contribution is at most8-m, so the tail is at least F-(8-m)>=m-5. For m=8 the same statement gives3.

For m=9 or10, the bottom tail includes all eight nonpositive-eta positions plus m-8 positions with eta>=0. Each additional scalar lower bound is at least1. Therefore that tail is at least F+(m-8)>=m-5 as well. At zero eta the scalar value is exactly1, so choosing either half at a tie changes nothing.

These are bounds on a known SCALAR lower-bound sequence. The reasoning never subtracts unknown actual eigenvalues using an unjustified upper bound.

For k=6,...,10 set m=16-k. The trace identity then gives

    K_k(X2)<=24-(m-5)=k+13.

Independently, T2 has diagonal value binom(z,2) on a string with z zeros, hence spectrum

    6 (once), 3 (four times), 1 (six times), 0 (five times).

Its central sums are6+4*3+(k-5)*1=k+13, exactly the claimed reference. This verifies every k=6,7,8,9,10, not just the median index.

## 5. All-state channel bridge, including p>1 — lines135–147

For q in[0,1], expanding the tensor channel gives the exact nonnegative coefficients

    a_s=(1-q)^s q^(4-s)2^(s-4).

The other subset-size comparisons at central k are valid for arbitrary states:

- X0=I is exact;
- X4=rho has K_k<=1;
- X1 is a convex mixture of local bit-flip conjugates of T1 after diagonalizing each marginal, so is majorized by T1 independently of correlations in rho;
- X3 is positive with trace4*2=8, while K_k(T3)=8 for k>=5;
- X2 is the new theorem just reconstructed.

The diagonal T_s entries are binom(z,s), all monotone in the same Hamming order. Thus Ky-Fan subadditivity and common maximizing basis subsets give the central channel inequalities. Nonnegative coefficients are used only for q in[0,1]; p=0 and q=1 also follow directly or by continuity, without ambiguity from endpoint power notation.

For the upper physical range compute on an arbitrary qubit operator Y:

    sigma_y[D_p(Y)]^T sigma_y
       =(p-1)Y+(1-p/2)Tr(Y)I
       =D_(2-p)(Y).

Tensoring gives the source's GLOBAL transpose/unitary identity, so outputs at p and2-p have identical spectra, including the product reference. For1<p<=4/3, q=2-p lies in[2/3,1). No negative expansion coefficient is passed through a Ky-Fan inequality, and no partial-transpose positivity assumption is substituted for this spectral identity.

All new central comparisons consequently hold for every mixed or pure input and every physical replacement p in[0,4/3].

## 6. Inherited composition boundary and limitations

Observed SHA matches:

- inherited `frozen-partial-v1/PROOF.md`: `6789e392dbc70dbed479ba8f307e0eb6c786d735de691d425583ec0d8b2fce8a`;
- operative `ADDENDUM_v1_1.md`: `73b6abb4e0a10b4fb9fe54ae5be853130c45a466b65a258c17385bc9911267d4`.

Read the full stored `review/codex-frozen-partial-output.md`, including its actual ACCEPT-WITH-FIXES and the three low-severity fixes covered by the addendum. Its rational-certificate checks are historical receipts, NOT this review's executed verification. I did not replay LP certificates, and no new external-model review was launched.

That exact inherited package supplies indices1,5,11..15 for all physical p and2,3,4 for p in[2/3,4/3]. Combining it with the newly checked central indices indeed covers every k=1..15 on that high-noise interval, with equal trace. For0<p<2/3 the three low indices2,3,4 remain. This composition is valid at the named imported-package boundary and does not retroactively change old records.

**Strongest scope check:** the new central theorem is genuinely all-state. The sole pure-state derivation, the qubit marginal lower bound, is explicitly extended by linearity before it is used. The rest uses positivity, trace, Bloch-length ranges and universal scalar inequalities only. No purity, rank or moment condition reappears silently.

**Findings:** none at this exact mathematical scope. The Zhang prior-claim/novelty audit was deliberately not assessed; a correct mathematical reconstruction supplies no novelty verdict. The full all-noise four-qubit conjecture and the book's broader question remain outside acceptance. Parent full-body composition remains separate.

Assigned bounded reconstruction complete; returning to the ONE semigroup primary and its pinned consolidation review gate.
