# A modular separator survives the full factor-coprime Shor multiplier route

Observed before freezing this candidate: **2026-10-23T14:06:51-0700 PDT**. Status: **CANDIDATE written route-limit theorem**, not a completion, noncompletion, stronger order restriction, kernel proof, or novelty claim. No scientific execution was used.

## 1. Exact scope and why it is different from the order baseline

The earlier dossier already says that unit transforms of the sixteen forced words do not contradict their code property when 1320 divides n. Its section 8 explicitly did not analyze arbitrary-length known-border products beyond an actor composition argument. Here the multiplier class is enlarged to the **factor-coprime** class from Cordero 2023 Theorem 7.2, including non-units modulo n, and the known-border product is handled for every length t by one explicit modular separator.

The conclusion is a **failure of this enlarged forced-data attack**, not progress toward a new numerical lower bound. It prevents misreporting a search over additional multipliers as promising unrestricted headroom. Unknown added words, actual border completions, cardinality n, and raw-word finite realization remain outside the theorem.

The exact Shor pair set is

    C = {(0,j):j∈{0,1,7,13,14}}
        ∪ {(3,j),(8,j):j∈{0,2,4,6}}
        ∪ {(11,j):j∈{0,1,2}}.

Put R0={0,1,7,13,14} and L0={0,3,8,11}.

## 2. Separator theorem (purely combinatorial)

Let n>0 be divisible by 1320. A residue's membership in pZ_n is well-defined for p=2,3,5,8,11 because each p divides n. Define

    T = {x∈Z_n : x∉5Z_n, x∉11Z_n, x∉8Z_n,
                   and not (x∈3Z_n and x∉2Z_n)}.

In words, T consists of residues not divisible by 5, 11 or 8, with every 3-divisible member even. In particular 0∉T, and T=-T.

For each position k choose positive integers u_k,v_k satisfying

    u_k odd,       8u_k ≠ 0 (mod n),       gcd(v_k,330)=1,

and let

    Z_k = {(u_k i,v_k j) mod n : (i,j)∈C}.

Then:

**(S1)** Each Z_k has exactly sixteen elements.

**(S2)** In the superposition of the difference graphs of all such Z_k, every nonzero target of an edge out of 0 belongs to T, and no vertex of T is the source of an edge. Consequently the superposition has no nonempty directed path from 0 to 0.

**(S3)** For every t≥0 and every fixed choice Z_1,…,Z_t as above, the map

    R0 × Z_1 × … × Z_t × L0 → Z_n^(t+1),
    (r,(i1,j1),…,(it,jt),l) ↦ (r+i1,j1+i2,…,jt+l)

is **injective**. No surjectivity is asserted. The two tuples being compared use the same Z_k at position k; this is not a claim that the union of all transformed word sets is a UD code.

### Proof

The positive differences between distinct left exponents of C are exactly

    D={3,5,8,11}.

The positive differences between distinct right exponents *in one fixed row* are exactly

    S={1,2,4,6,7,12,13,14}.

The positive differences in R0 are {1,6,7,12,13,14}⊆S, and those in L0 are D. These lists follow directly from the four displayed rows: row 0 gives {1,6,7,12,13,14}, rows 3/8 give {2,4,6}, and row 11 gives {1,2}.

**Separator facts.** For every s∈S and every v coprime to 330, ±vs lies in T. Indeed v is odd and prime to 3,5,11. No s is divisible by 5 or 11. Its 2-adic divisibility is at most 4, so 8∤vs. The only 3-divisible s are 6 and 12, which are even. Multiplication by v preserves all these statements. Such residues are nonzero modulo n, since none is divisible by 5 while 5|n.

For every d∈D and every odd u with 8u≠0 mod n, ±ud is nonzero and outside T. For d=3, the residue is odd and 3-divisible. For d=5 or 11 it is divisible by that prime. For d=8 it is divisible by 8. Nonzeroness for odd d follows by reduction modulo 8 (an odd number cannot be 0 modulo 8), and for d=8 it is the explicit assumption. These are residue arguments and hold for every multiple n of 1320, not finite evaluations.

**S1.** Distinct original rows remain distinct after multiplication by u: their differences are ±uD, just shown nonzero. Within one row, distinct right exponents remain distinct after multiplication by v, since their differences ±vS are nonzero. Thus the image map on C is injective.

**S2.** A difference-graph edge produced by two points (ui,vj),(ui',vj') of one Z has source u(i-i') and target v(j'-j). If its source is zero, S1's row argument gives i=i', and then its nonzero target belongs to ±vS⊆T. If its source is nonzero, it lies in ±uD, hence outside T. Thus T has no outgoing edges at all. An edge from 0 enters T and cannot continue, proving the no-path statement. This argument remains valid when each edge uses a different admissible (u,v).

**S3, t=0.** A nontrivial equality r+l=r'+l' would give a nonzero element r-r' of T equal to l'-l outside T; if one difference were zero so would the other. Hence both pairs agree.

**S3, t≥1.** Compare two input tuples with equal output. At coordinate 0,

    r-r' = -(i1-i1').

The left side, if nonzero, lies in T; the right side, if nonzero, is a transformed row difference outside T. Hence both are zero: r=r' and the first original rows agree. The first right difference j1-j1', if nonzero, therefore lies in T. At coordinate 1 it must be the negative of the next transformed row difference, which is either zero or outside T. Both must again vanish. Continue through each coordinate. At the final coordinate, the last right difference (zero or in T) equals a difference from L0 (zero or outside T), so both vanish. Every endpoint and every transformed pair agrees. This proves injectivity for all t without a finite-length cutoff. QED.

## 3. Application to the full factor-coprime permission

The following imported interfaces are stated explicitly; they are not new results here.

- The dossier's completion-to-tiling proof gives actual |R|=r, |L|=ell, n=r·ell, 330|r, 2|ell and 1320|n.
- The October 22 Rédei consequence supplies at least three distinct prime divisors of ell; in particular ell has an odd prime divisor. Its exact theorem import remains Cordero 2023 Lemma 5.2, citing the unread Szabó–Sands monograph proof.
- Cordero 2023 Theorem 7.2 says that, for a compatible n-cbc family with stable border (P,Q), adjoining a left multiplier u prime to |Q| and a right multiplier v prime to |P| preserves compatibility and that border. In our orientation P=R and Q=L. Primary statement and proof were read at https://arxiv.org/html/2301.13566v1 (retained text lines 1156–1194). This is a precisely declared external theorem input, not a formal import or a claim to have reconstructed its proof.

For any multipliers allowed by this theorem, gcd(u,ell)=1 makes u odd. If 8u=0 mod n, any odd prime p|ell also divides n and hence divides 8u, forcing p|u, a contradiction. Thus 8u≠0 mod n. Likewise gcd(v,r)=1 and 330|r imply gcd(v,330)=1. Therefore **every factor-coprime transform of the known sixteen words is covered by S1–S3**. Any finite sequence of such transforms, with arbitrary allowed non-unit multipliers, still has no forced-data path obstruction and no known-border collision, for every admissible n.

This is not merely the special case n=19800, and it does not repackage that baseline restriction. It is also not an existence theorem for any border, n-cbc or finite maximal code. The theorem only says that the displayed forced pieces remain mutually injective under these operations. An actual completion would have vastly more one-b data and border elements, and those unknown elements may create an obstruction.

## 4. Consequence for the next attack

The proposed expanded multiplier scan has **HEADROOM-ABSENT for known-word/known-border collision certificates** once the existing baseline predicates hold. Executing such a scan would add examples, not the missing all-order contradiction. No GO is requested for it.

A consequential continuation must incorporate unknown additional words or a new finite-realization condition; it cannot consist solely of applying more permitted multipliers to C, R0 and L0. A positive result must still provide actual finite raw words and independent UD plus completeness certification. A negative result must still exclude all hypothetical extensions, not just this forced substructure.

## 5. Verification and novelty boundary

This candidate has a complete written proof but has not yet had a separate in-harness reconstruction, parent acceptance, finite replay, Lean check or human review. The separator lists, multiplier orientation, non-unit row-collapse guard, and the absence of a surjectivity/union-UD claim are its load-bearing review points. The proof imports no Szabó 2006 transcription. No new numerical order restriction or solved-book claim is made. The exact extension of the old route-limit statement has not been novelty-cleared against the original 2006 proof or inaccessible Sands construction.
