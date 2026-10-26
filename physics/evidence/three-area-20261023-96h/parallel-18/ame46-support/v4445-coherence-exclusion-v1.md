# Candidate v1 — local block dequantization excludes the whole v=(4,4,4,5) support48 stratum

Observed immediately before creation: **2026-10-24T03:38:50-0700**. PhysicsAME46, physics-6. This executes the EXACT whole-stratum obligation frozen before attack in `continuation-v4445-freeze-v1.json` and ACKed to Main. **CANDIDATE complete written coherence argument, not yet separately reconstructed or parent-accepted.** No scientific executable/import, arithmetic script, enumeration, solver, compilation, tests, CLI, native launch or nested agent.

## 1. Literal target, achieved candidate and scope

For every normalized arbitrary-complex pure AME(4,6), in every product orthonormal basis, use

    A=6psi,  T={x:|A_x|=1},  N=supp(A)\T,
    t=|T|, h=36−t, e=|supp(A)|−(72−t),
    d_(i,a)=6−#{x∈T:x_i=a},  V_i={a:d_(i,a)>0}, v_i=|V_i|.

**Candidate theorem.** No such tensor has h=12, e=0 and active alphabet sizes(4,4,4,5), allowing the five-value alphabet to occur at ANY party. Equivalently the whole support48/t24 stratum with that active-size profile is excluded, not one officer placement, graph, phase alphabet or symmetry class.

The new mechanism is an ACTUAL local-unitary rectification of one closed2×2 flattening block. It would turn a deficit3 slice into an impossible deficit1 slice. This forbids Hamming-distance-one support pairs, forces a parity tetrahedron in every thin slice, and makes the required officer incidences incompatible with all three active-pair matchings. The final count closes a coherent geometric argument; it is not merely another officer-moment/profile narrowing.

A stronger intermediate statement proved below is: at e=0, if coordinates1,2,3 each have four active values all of deficit3, the remaining coordinate cannot have even ONE value of deficit2. The targeted v4445 profile necessarily has those hypotheses, as verified in §7.

This does NOT exclude every support48 configuration, improve the unrestricted lower bound to49, or remove e=0 from this new argument. The documented48..60 range and source/novelty/formal qualifications remain unchanged.

## 2. Exact two-party facts, including the universal deficit1 obstruction

Every two-party marginal of the original AME state equals I36/36. For every cut P|Pc, its flattening M_P of A therefore satisfies

    rho_P=M_P M_P†/36=I36/36,
    rho_Pc=(M_P†M_P)^T/36=I36/36.

Thus every fixed pair-value line has squared A-norm1; an officer exhausts that line, and distinct officers cannot agree in two coordinates. Every line is occupied. An officer-free line has at least two nonzero entries: a singleton would have modulus1 and be an officer. Non-officer points use only active local values, since six officers at a deficit0 value already cover all partner lines.

At e=0, every officer-free line has EXACTLY two nonzero entries. In every flattening there are t officer rows and h other rows, each of the latter needing at least2 entries. Total support is t+2h, so equality holds in every row and, separately, every column of all three cuts. A pair of non-officer rows sharing one column must share another, because a one-term nonzero inner product cannot vanish. Their degree2 and the column degrees2 give a CLOSED2×2 unitary block with four nonzero entries.

For a local value with deficit d, its non-officer slice has exactly2d entries at e=0; every other coordinate takes exactly d values, each twice. This follows by counting the d officer-free partner lines, not from a constant-modulus assumption.

**Universal lemma: deficit1 is impossible, without any e restriction.** If a value c at party j had exactly five officers, those officers use five distinct values in every other coordinate. A further nonzero point at j=c must avoid every officer pair-line, so all its other coordinates are forced to the sole remaining value in each party. There is at most one possible position. But the corresponding missing partner line is nonempty and officer-free; it cannot have only one nonzero coefficient, as just proved. Equivalently that singleton would have modulus1 and be a sixth officer. Contradiction.

## 3. NEW coherence lemma: a deficit3 slice admits no one-coordinate N pair

**Lemma D3.** In an e=0 AME tensor, suppose two distinct N points differ only in coordinate i, taking values a,b there. If j!=i is another coordinate and c is their common j-value, then d_(j,c) cannot equal3.

**Proof.** Use the flattening whose row coordinates are(i,j), in that order; permuting row/column index conventions does not change unitarity. The two N points are in rows(a,c),(b,c) and the SAME column (the remaining two coordinates). The exact-two/orthogonality facts in §2 put them in a closed2×2 unitary block B. The entire entries of these two rows lie in its two columns.

Take a6×6 unitary U_i acting as B† on span{|a>,|b>} and as the identity on its orthogonal complement. Applying U_i to party i left-multiplies precisely these two block rows by B†, so at j=c the block becomes I2. Its four old non-officer coefficients become exactly two coefficients of modulus1 and two zeros. All other entries in these two rows were zero, so no overlooked coefficient can mix into that slice.

The original officers at j=c lie OUTSIDE levels a,b of party i, since both corresponding pair-lines already contained N. They are therefore unchanged. Every other i-level is unchanged by U_i; its old non-officers remain non-officers. Thus at j=c the officer count increases by exactly2.

If d_(j,c)=3, the original slice had3 officers. The transformed slice has5 officers, hence deficit1, impossible by the universal lemma. This is a contradiction within the original AME class: for EACH of all six two-party sets P, if i∈P then

    rho'_P=(U_i tensor I) rho_P (U_i tensor I)†=I36/36,

and if i∉P, invariance of the partial trace over i gives rho'_P=rho_P=I36/36. All six reductions and normalization are preserved. No assumption that a blockwise row operation on an arbitrary flattening is automatically local has been made: the two rows share the actual j-value c, so this particular row mixing is exactly the physical unitary on party i.

The entries/phases of B may be arbitrary complex numbers. B† exists and is unitary because it is an actual closed square unitary component. This is written existence of a feasible local basis transformation, not an executable tensor calculation or phase choice. ∎

**Consequence.** If at least two coordinates have ONLY deficit3 active values, N has no two points differing in exactly one coordinate. For a proposed varying coordinate i, choose one of those two coordinates j!=i; the common j-value is active and has deficit3, contradicting Lemma D3. In the stratum below coordinates1,2,3 all have that property, so the consequence applies to every possible one-coordinate difference.

## 4. Any remaining thin slice must be a parity tetrahedron

Assume now that coordinates1,2,3 have profile{3,3,3,3}, and coordinate4 has some active value y with deficit2. Its N-slice has exactly4 points. In each of coordinates1,2,3 it uses exactly two values, each twice. Write these two-value sets as B_1,B_2,B_3; here B_i is a subset of the four-element ACTIVE alphabet V_i, not an inactive alphabet.

The4 distinct points can be identified with4 binary triples balanced2+2 in each coordinate. There are exactly three unordered2+2 partitions of a4-element set. If two coordinate partitions coincide, those two bits have a fixed XOR and the third bit is free; distinctness forces all four words of that plane. It contains pairs differing only in the free coordinate, forbidden by §3. If no two partitions coincide, they are the three different partitions; the third bit is XOR or complement of the first two.

Therefore the slice is a parity tetrahedron. In particular its projection onto EACH pair(i,j) among1,2,3 is the FULL rectangle

    B_i × B_j,      |B_i|=|B_j|=2,

with one actual nonzero N point at each pair-value. No real-phase or equality-of-moduli assertion is needed for this support conclusion.

## 5. Parity rectangles are incompatible with two active officer coordinates at y

For i,j in{1,2,3}, each active value a∈V_i has deficit3, so exactly3 partner lines at party j are officer-free, all lying in the four-element V_j. Precisely ONE active partner value carries an officer. These neighbors form a bijection

    F_ij:V_i -> V_j.

The reverse statement from j proves bijectivity/inverse, so this is true for EVERY actual officer placement, not an assumed coherent matching or a selected catalogue representative.

The parity rectangle from §4 consists of N points. It cannot meet any officer pair-line. Hence

    F_ij(B_i) intersect B_j=empty.

Both sets have size2 in V_j of size4. Thus

    F_ij(B_i)=V_j\B_j,
    F_ij(V_i\B_i)=B_j.                                (M)

Suppose an officer at coordinate4=y had TWO active first-three coordinates i,j, with values a,b. The officer pair implies b=F_ij(a). Since it shares y with the N slice, its i-value cannot lie in B_i and its j-value cannot lie in B_j: otherwise it would share a norm-exhausted(y,i) or(y,j) pair-line with a nonzero N point. Therefore a∈V_i\B_i and b∈V_j\B_j. But(M) forces b∈B_j. Contradiction.

Consequently EVERY officer at y has at most ONE active coordinate among parties1,2,3. This conclusion holds simultaneously for all three active-pair matchings; no matching normal form or particular graph has been chosen.

## 6. The actual y-slice now gives a contradiction

There are6−d_(4,y)=4 officers at y. For each i in{1,2,3}, exactly the two active values B_i give hole lines with y, while the other two values of V_i carry officers on those pair-lines. Thus the total number of incidences of these four officers with an active coordinate among1,2,3 is

    (4−2)+(4−2)+(4−2)=6.

Section5 says each of the four officers contributes at most1, so that SAME incidence count is at most4. Contradiction6>4.

This proves the general coherence statement: three{3,3,3,3} axes at e=0 are incompatible with ANY deficit2 value in the remaining coordinate. The novel obstruction was the physical block rectification/deficit1 argument leading to the parity rectangles. The final incidence inequality alone would not follow from the old count predicates.

## 7. Why this excludes the ENTIRE frozen v4445 stratum

For completeness, here is the checked baseline reduction without omitting other proposed deficits. The target h=12 implies t=24. For v=(4,4,4,5), let c(x) count an officer's active coordinates. Counting active singleton/pair lines gives

    kappa1=sum_T c=6·17−4·12=54,
    kappa2=sum_T binom(c,2)=108−6·12=36.

Therefore

    sum_T (c−2)(c−3)/2=36−2·54+3·24=0.

Every integer summand is nonnegative, so all officers have c∈{2,3}. For an active value a at coordinate i, with deficit d and S_i=sum_(j!=i)v_j,

    #officers at(i,a)=6−d,
    sum_(T:x_i=a)(c−1)=S_i−3d.

Since c−1≥1, S_i−3d≥6−d and hence d≤(S_i−6)/2. At each four-value coordinate S_i=13, giving d≤3; four positive deficits sum to12, so all four are3. At the five-value coordinate S_i=12 also gives d≤3. Positive deficits cannot equal1 by §2, so its five parts are exactly3,3,2,2,2.

Thus every target tensor—not merely an ansatz—has the hypotheses of §§4–6, with three possible thin values y. Even one leads to contradiction. Permuting parties carries the same argument to any location of the five-value alphabet, preserving all six AME conditions and the definitions h,e,v. The whole v4445/e0 stratum is excluded. ∎

## 8. Verification, imports and exact remaining target

The proof is self-contained from the actual six AME pair conditions, finite-dimensional complex unitarity and elementary officer/slice counts. It does NOT consume Ball–Simoens QLS6 classification, a no-AME4,2 theorem, a historical42/46/48 certificate, an officer catalogue, an unchecked finite table, a support-minimal basis, or a real/equal-modulus assumption. The old counts in §7 are baseline identification; the new consequence is whole-stratum coherent impossibility.

The exact high-risk reconstruction target is Lemma D3: the row mixing must be a PHYSICAL local unitary at a shared second coordinate; all old slice officers must remain untouched; the local block must be genuinely closed/unitary; all six marginal conditions must survive; and the new deficit1 contradiction must not assume e=0 for the transformed state. Sections2–3 explicitly check these points. The parity-projection and matching-complement argument must then cover every officer placement, as written.

No separate reconstruction, formal/kernel/human proof or novelty clearance is claimed at this snapshot. Corrections must use a numbered successor. The source/open-status and original deadline/control qualifications remain. Scientific execution is neither needed nor authorized.

Other active-size/deficit profiles and required e>0 support48 cases still remain. In particular this does not settle the separately narrowed(3,5,5,5) profile or assert feasibility/nonemptiness of any residual. The unrestricted documented bound is STILL48≤s_min≤60; no lower49 follows from this one whole-stratum exclusion.
