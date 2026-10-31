# Addendum4 — static normalized-decomposition rigidity and the exact same-family tensor caller

Actual native clock before writing: **Tue Oct 27 15:17:48 PDT 2026**.
PhysicsMOQLS8-2 / physics-4. **WRITTEN, UNREVIEWED conditional coupling/obstruction candidate** at the admitted original definitions and explicitly named elementary matrix facts. No numeric example, selected parameter, interpreter, calculator, CAS, enumeration, solver or replay.

## 1. Representation change and exact purpose

The motion route in the earlier packets does not prove that every possible nonclassical four-family is connected to a classical tuple. I do not count more motion filters as a substitute for that missing premise. This packet instead examines STATIC gluing of the SAME four factor arrays.

The family-to-tensor framework is not claimed as an invention: the admitted paper itself mentions AME/perfect-tensor and quantum-design applications. A new coordinate encoding alone is NOT the claimed progress. The substantive proved obstruction is an exact **positive phase-defect identity**: at the minimal normalized decomposition length/mass, nonorthogonal factors cannot be repaired by cancellation of cell phases. Its equality case pays a genuine converse from a global operator condition to the actual pair-product ONBs.

No outside quantum-design paper has been opened, so historical novelty/source-equivalence is unresolved. Correctness here uses only the original QLS/MOQLS definitions and finite-dimensional tensor/trace/Cauchy–Schwarz facts proved or applied below. No old local/channel/commutant, held or unreviewed candidate is an input; resemblance of notation does not supply one. Prior exposure is not erased and no private-cognition certificate is claimed.

## 2. General positive defect identity

Let V:C^m→C^N be a coisometry, VV*=I_N. Suppose it has an EXACT finite rank-one decomposition

    V=sum_(z=1)^L lambda_z |q_z><r_z|,
    ||q_z||=||r_z||=1.

Here q_z∈C^N,r_z∈C^m, and lambda_z may have arbitrary phases and amplitudes. For nonzero lambda_z write w_z=|lambda_z| and eta_z=lambda_z/w_z. A zero term has weight0 and can be omitted; its phase is irrelevant. Let W=sum_z w_z.

Then

    W−N = (1/2) sum_z w_z ||V* q_z−conj(eta_z) r_z||².   (PD)

In particular W≥N. This is an identity for the ACTUAL same operator V/decomposition, not an inequality for independently chosen left/right factors.

**Proof.** Since V* is isometric on C^N, ||V*q_z||=1. Also

    N=tr(V*V)=sum_z lambda_z <r_z,V*q_z>.

The trace is real. Expanding each squared norm gives

    ||V*q_z−conj(eta_z)r_z||²
       =2−2Re(eta_z <r_z,V*q_z>).

Multiply by w_z/2 and sum. The right side becomes W−Re tr(V*V)=W−N. Every term is nonnegative, with no phase-cancellation assumption. ∎

## 3. Saturated minimal-length rigidity

Assume L=N and W=N. Then every nonzero term in(PD) vanishes:

    V* q_z=conj(eta_z)r_z.

Rank(V)=N and there are only N rank-one terms, so none has zero coefficient. Substituting these equalities into the exact decomposition gives

    V*V=sum_z w_z P_(r_z).

Each r_z lies in the N-dimensional image of V*. In that image, the N columns sqrt(w_z)r_z form a square Parseval matrix. A square matrix RR*=I is unitary, hence its columns have norm1 and are orthogonal. Consequently

    w_z=1 for EVERY z,
    {r_z} is an ONB of image(V*),
    {q_z} is an ONB of C^N.

The last assertion follows from q_z=conj(eta_z) V r_z. This proves the full equality structure, not just a trace bound.

Conversely, such orthonormal systems and unit-modulus coefficients give a coisometry by direct multiplication. Thus at N normalized rank-one terms and total amplitude massN, coisometry is equivalent to actual orthonormal factor frames.

### Essential ceilings

- Fewer than N nonzero terms cannot have rankN.
- More than N terms do not give the square-Parseval conclusion; an overcomplete frame is not silently declared an ONB.
- If W>N, the defect may be positive; no orthogonality conclusion is asserted from rank/trace alone.
- Unit norms and the amplitude-mass condition are genuine inputs. Arbitrary unnormalized factors cannot be rescaled and then silently assigned unit coefficients.
- Square unitary matrices are the special case m=N. All statements retain arbitrary complex phases, including zero/dependent candidate data rejected by the rank/equality argument.

## 4. A static obstruction to phase-repair gluing

Take a proposed square unitary of sizeN written as N rank-one terms with normalized left/right vectors and coefficients of modulus1. Its mass isN. By §3 both sets of vectors MUST already be ONBs.

Therefore, if a proposed normalized pair frame is not orthogonal, **no choice of unit cell phases and no choice of the other normalized factor frame can repair it into a unitary through that N-term decomposition**. The right-hand positive defects cannot cancel. This is an all-variable obstruction, not a selected failed numerical candidate.

The statement does not say that arbitrary nonorthogonal decompositions of a unitary are impossible: their total amplitude mass would have to be larger or the term/normalization assumptions different. Those altered decompositions do not meet the original unit-entry family caller below.

## 5. SAME four factors, all three unitary flattenings

Let X={1,…,n}² and N=n². For each cell z let a_z,b_z,c_z,d_z be unit vectors in C^n. Keep the SAME factors and arbitrary unit phases eta_z in the tensor

    T=sum_(z∈X) eta_z a_z tensor b_z tensor conj(c_z) tensor conj(d_z).

For a list of product vectors write Q_ab for the matrix with columns a_z⊗b_z, and use bars to denote conjugating that factor's vectors. The three square flattenings are

    T_12|34 = Q_ab diag(eta) Q_cd*,
    T_13|24 = Q_(a,bar c) diag(eta) Q_(bar b,d)*,
    T_14|23 = Q_(a,bar d) diag(eta) Q_(bar b,c)*.           (THREE)

These identities follow by inspecting each tensor coefficient; the conjugations on the two sides are essential.

### Forward actual-family consequence

If the four arrays form an actual four-MOQLS(n) family, each required unbarred pair-product list is an ONB. Conjugating one factor does not change whether the product of its two Gram overlaps is zero. The barred pair-product lists in(THREE) are therefore ONBs as well. Every matrix in(THREE) is unitary, for EVERY choice of the cell phases.

Thus an actual family gives one tensor with all three two-versus-two unitary flattenings. There is no common member frame or phase convention.

### Converse with every physical caller retained

Suppose the four arrays are actual INDIVIDUAL QLS on the SAME cell grid, and all three flattenings of this SAME tensor/decomposition are unitary. Each is an N-term decomposition with normalized factor vectors and amplitude massN. Apply §3:

- the first flattening makes Q_ab,Q_cd unitary;
- the second makes Q_(a,bar c),Q_(bar b,d) unitary;
- the third makes Q_(a,bar d),Q_(bar b,c) unitary.

The zero-product condition for a barred pair is equivalent to that of its unbarred pair: for complex alpha,beta, alpha·conj(beta)=0 iff alpha·beta=0. Unit norms and the N-vector count then give all SIX ordinary pair-product ONBs. Together with the supplied row/column QLS conditions, the four-tuple is actual.

This is the full forward/converse original-object caller. It does NOT infer individual QLS rows/columns from an unlabelled four-party tensor, and it does not combine three unrelated flattening decompositions. SAME factors, SAME cells, SAME tensor and SAME coefficients are essential.

A unitary flattening already forces tensor rank at leastN; this N-term decomposition attains that lower bound. No classification of all minimal-rank perfect tensors or of their decompositions is imported or claimed.

## 6. Anchored six-factor caller — all original rows and columns can be recovered too

There is an exact way to retain the row/column structure rather than forgetting it in an abstract four-party tensor.
For every z=(i,j) define SIX unit factors

    v0_z=e_i, v1_z=e_j, v2_z=a_z, v3_z=b_z, v4_z=c_z, v5_z=d_z,
    Q=sum_z eta_z v0_z tensor v1_z tensor v2_z tensor v3_z tensor v4_z tensor v5_z.

The first two factors are fixed common grid anchors. Do not replace them by independent labels for different members. For each choice of two factors, flatten Q as a map from the other four factors to those two. It has N rows and n^4 columns and is a sum of N normalized rank-one terms of massN.

> The original four arrays are an ACTUAL four-family iff EVERY such two-versus-four flattening is a coisometry.                     (ANCHOR)

**Forward.** Every pair of the six factor lists is an ONB:

- the two anchors give the standard cell basis;
- anchor0 with a member gives that member's rows, block by block;
- anchor1 with a member gives its columns;
- two member factors give the original pair-product ONB.

For a two-versus-four split, the left pair is an ONB. The right four-factor list is orthonormal, since it contains a pair whose product list is an ONB; all factors have unit norm. The flattening is therefore a coisometry by direct multiplication.

**Converse.** Apply the rectangular saturated-rigidity theorem §3 to each coisometric flattening. Its left pair list is an ONB. Therefore every anchor–member pair is an ONB, which forces that member's actual rows/columns to be ONBs in their corresponding fixed anchor blocks. Every member–member pair is an ONB as well. All four arrays are actual QLS and mutually orthogonal. No separate row/column ansatz is hidden. ∎

After normalization by n, this anchored tensor is a pure six-party state with every two-party marginal maximally mixed. This is **2-uniform**, not a claim of an AME six-party state (which would require three-party conditions). The quantum-design/framework correspondence itself is not claimed as new; the in-body positive-defect/equality argument supplies the exact normalized same-decomposition converse and no-phase-repair obstruction used here.

## 7. What this does NOT allow one to drop

1. A generic four-party multiunitary/perfect tensor is not a physical four-family witness: the SAME normalized N-term factor decomposition and the actual common grid/QLS conditions, or the anchored caller, are still required.
2. Different product decompositions for different flattenings cannot be glued by their existence alone. The rigidity argument concerns one actual common factorization.
3. An arbitrary2-uniform six-party state without the fixed row/column anchors and normalized N-term product decomposition is not automatically a MOQLS family.
4. A locally classical or otherwise convenient tensor representation does not classify all possible CP decompositions or prove each factor array classical. Decomposition uniqueness is not supplied.
5. A projective change or an operator with large available freedom is not automatically a genuinely nonclassical family. Entry phases and separate member unitaries remain isotopy freedoms.
6. None of the old five-family proof, old native/GB output, finite classification or held candidate data is used to fill the static factorization/compatibility premise.

The exact remaining original-model task is a universal obstruction or actual realization for this fully coupled normalized/grid-anchored object, including at least one nonclassical factor array. Nothing here proves that every such object must be classical or constructs a nonclassical one. Numerical M(8),maximum-three,A10/A11 and stronger assurance remain open.

## 8. Input, source-equivalence and assurance

Only S1/S2, the admitted source definitions and elementary finite-dimensional matrix facts enter: trace cyclicity/linearity, coisometry/isometry identities, expansion of a norm square, positive finite sums, rank subadditivity, square Parseval matrices and tensor inner products. Every special equality/phase/actual-family application is proved above; no opaque external tensor-classification theorem is assumed.

The admitted paper's reference[14] (*Quantum combinatorial designs and k-uniform states*) may already contain the framework correspondence or related rigidity. It has NOT been opened: bibliography expansion is outside the present S1 source packet. Historical novelty and exact source overlap are therefore **NOT_RECONSTRUCTED**, not inferred from a failed search or from this derivation. A narrowly admitted source comparison would be needed before any priority/contribution claim.

This packet is not an algebraic/programmatic certificate. No matrix, phase, state, sampled boundary or decimal was evaluated. No scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control probe, nested agent/model CLI/paid API, Git/delete/contact/infrastructure action occurred. Only the new owner root was written; earlier packets stay immutable. Original STOP outside S1, global HOLDv2, N4 UNKNOWN/exit UNESTABLISHED, aux214STOP and all findings/ZERO consumers persist. Main must read the full source/proof and full-scope peer returns before adoption. Same-harness writing is not formal/kernel/human/configured-family/executable or novelty acceptance.
