# Sun P7 — mixed6+1/5+2 sources force the private2/3/5 exceptional ownership pattern

Owner **MathSun8-2**. Actual preceding `/bin/date`: **Mon Oct 26 07:10:30 PDT 2026**. **NEW WRITTEN CANDIDATE, not reviewed/adopted.** This is an ACTUAL mixed-source/global-fibre theorem, not a subgroup table, abstract cell witness or unrestricted Sun8 solution. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/GO.

## 0. Exact theorem and the complete source-union boundary

Let G be finite, M ACTUAL of index7t, and H6,H5 ACTUAL subgroups of indices7r6,7r5 with

    gcd(r6,r5)=1, gcd(t,r6*r5)=1.

Suppose ACTUAL nonempty left cosets of H6,H5 are disjoint. On the SAME Omega=G/M, suppose H6 has EXACTLY TWO orbits6t+t, and H5 EXACTLY TWO orbits5t+2t. Let T6,T5 be their UNIQUE small orbits of sizes t,2t. No source is replaced, independently conjugated into a different family, or selected merely from an index divisor.

**Generic conclusions, requiring no F7/classification input:**

1. 3 MUST divide r5; otherwise such a mixed source pair is impossible.
2. If5 does NOT divide r6, Omega has an ACTUAL G-invariant partition into SEVEN blocks of size t; M fixes its base block, giving a faithful transitive seven-point quotient.
3. The SAME seven-block conclusion holds whenever the common nontrivial irreducible dimension is6. If5|r6,3|r5 and t is ODD, that dimension is forced to be6.
4. In the remaining private-owner case, let d be that common irreducible dimension. Necessarily d>=6. If v2(t)=1 then d<=20; if v2(t)>=2 then d<=160. These are representation-dimension bounds, not a bound on |G|, t or a witness.

**Original-family consequence:** in an eight-coset P7 family with all FULL indices7r_l/private r_l pairwise coprime, selected7-free U_i<=M, a mixed6+1/5+2 source pair can therefore occur ONLY if

    2|t (hence2|r_i), 5|r6, 3|r5,

and d>=7 with the indicated20/160 ceiling. The selected vertex, six-orbit source and five-orbit source are the THREE DISTINCT private owners of2,5,3. Thus only ONE selected vertex of the original family can admit such a mixed pair at a verified M. In the separately accepted least-GROUP-ORDER/simple direct-P7 reduction the same restriction applies at EVERY vertex, including the possible private7-owner.

The final contradiction for a constructed seven-point quotient uses only the named **F7-P7** finite faithful degree7 exclusion at the complete99LF `sun8-two-source-seven-free-normalizer-exclusion-v1.md`, SHA256109bcd2d7873a8bba0042581360cc73d2db05946812d7250cbf928550cada0ae, §2, and the supplied181LF degree-seven/NC7 proof2c8949dfa512ca3d89549b04d42bea9be8a515081cb3a3ba7762dd3b2e7b46e8 at A6/A7 simplicity/Eisenstein. Generic statements1–4 do NOT consume it.

This is a NEW mixed complement to the ENTIRE200LF two5+2-source theorem `sun8-two-five-plus-two-sources-seven-star-quotient-v1.md`, SHA256258442f4516d5ac10f78e85737b21e8d758e7aff1fa13855e2aa4c83b9f54667. Neither new paper is assumed accepted. A fresh gate should consume BOTH entire bodies as one current high-two-orbit source union, not replace their different hypotheses.

## 1. Every translated small-orbit intersection has the required actual divisibility

For A=H6 cap H5, private coprimality gives[G:A]=7r6*r5*delta with integer1<=delta<=7. Original coset disjointness forces delta<=6, since delta7 would mean H6 H5=G and all their left cosets meet.

The bound also holds for EVERY conjugate intersection, a fact needed for the full cross-matrix below. If H6*(gH5g^(-1))=G for even ONE g, H6 has an orbit of FULL size7r5 on G/H5, namely the orbit through gH5. That orbit is the entire set; H6 is transitive and its orbit through H5 is also full, contradicting H6H5!=G. Hence for EVERY g,

    [G:H6 cap gH5g^(-1)]=7r6*r5*delta_g,
    1<=delta_g<=6.                                  (1)

All orbits of this intersection on Omega have lengths divisible by t/gcd(t,delta_g): its orbit length ell gives7t|7r6*r5*delta_g*ell, and gcd(t,r6*r5)=1.

Consequently for ANY translated orbit sets aT6,bT5, their intersection is invariant under aH6a^(-1) cap bH5b^(-1), so

    z_(a,b)=|aT6 cap bT5|/t

is a nonnegative multiple of1/gcd(t,delta_(a^(-1)b)), lying in[0,1]. This is an ACTUAL all-column statement, not an unproved extension of one identity-position intersection factor.

## 2. ONE common nontrivial irreducible and the exact normalized Gram relation

Define G-equivariant0/1 matrices I6,I5 with rows Omega and columns G/H6,G/H5, putting1 when the row lies in the translated small orbit. I6 has column t/row r6; I5 has column2t/row2r5.

Each source has EXACTLY TWO orbits on Omega. As in the complete200LF paper§2, finite unitary decomposition/Schur gives precisely one nontrivial common irreducible W6 or W5, multiplicity ONE in both C[Omega] and the corresponding permutation module. The actual incidence image is constants plus that irreducible.

If W6 and W5 were different, their nonconstant incidence images would be orthogonal and I6^*I5=(2t/7)J. In particular the ACTUAL T6 cap T5 would have size2t/7. By§1 its size must be a multiple of t/gcd(t,delta), forcing7|2gcd(t,delta), impossible with delta<=6. Thus W6=W5=W. Let d=dim W and E its orthogonal projector.

Constants and trace now give

    I6 I6^*= (r6/7)J+(6t*r6/d)E,
    I5 I5^*= (4r5/7)J+(10t*r5/d)E.

The first total trace is7t*r6 with constant eigenvalue t*r6; the second total14t*r5 has constant4t*r5. Normalize by r6,r5 respectively and call the resulting matrices A,B. Then

    A=(1/7)J+(6t/d)E,
    B=(4/7)J+(10t/d)E=(5A+J)/3.                     (2)

For any two rows let c6,c5 be their INTEGER common-column counts. Their bounds are0<=c6<=r6,0<=c5<=2r5, and(2) says

    3r6*c5=r5*(5c6+r6).                             (3)

Since r6,r5 are coprime, r6 divides5c6. Thus k=5c6/r6 is an integer0..5, and c5/r5=(k+1)/3. Diagonal k5 means identical I6 rows and identical I5 rows, because their equal-weight0/1 row inner products attain their full row weight simultaneously. No selected row/fiber was discarded.

## 3. The private5-free source gives actual seven blocks

If5 does not divide r6, (3) gives c6=0 orr6 for EVERY row pair. Thus distinct I6 rows are either disjoint or identical. Identical-row equivalence is G-invariant. ANY two rows in one actual incidence column cooccur, so must be identical; that column is contained in one equivalence class. Conversely all rows identical to a row in that column also belong to it. Therefore EVERY column is EXACTLY one equivalence class, of size t.

There are SEVEN actual t-classes, permuted transitively by G. The class of the basepoint M is fixed by M, so the image of M is inside a point stabilizer in the faithful seven-point image F. No overgroup was manufactured from a divisor, and no independent source-coset deformation is asserted. This proves generic conclusion2.

## 4. A private3-free five-orbit source is impossible already generically

Suppose3 does not divide r5. From c5/r5=(k+1)/3 and integrality of c5, only k2 or5 is possible. Value5 identifies identical rows; between DISTINCT actual identical-row classes, the normalized A entry is2/5.

Transitivity gives all such row classes one size b. Each I6 column is a union of them, so b|t; write h=t/b. The number of classes is7h. Compress A to one representative per class. Its row sum is t/b=h, because uncompressed A has constant eigenvalue t. But its diagonal is1 and EVERY off-diagonal entry2/5, so that row sum would be

    1+(7h-1)*2/5=(14h+3)/5>h,

contradiction. This proves generic conclusion1 without F7 or a group classification.

## 5. Full cross-matrix first/second moments and the ODD outer-index case

Any remaining pair has5|r6 and3|r5, so gcd(t,15)=1. By§1, if t is ODD then gcd(t,delta_g)=1 for EVERY delta_g<=6. Hence EVERY translated cross intersection z_(a,b) is0 or1.

Let Z=I6^*I5/t, with7r6 by7r5 entries. Counting row products gives the EXACT full-matrix average

    mean Z = 2/7.

Also

    ||I6^*I5||_F^2
      =tr[(I6 I6^*)(I5 I5^*)]
      =t²*r6*r5*(4+60/d),

using the constant eigenvalues and the d common nonconstant eigenvalues in(2). Thus

    mean Z²=(4+60/d)/49.                             (4)

For0/1 entries these two means are equal, so4+60/d=14 and d6.

For d6, A=(1/7)J+tE has every nonzero eigenvalue t, hence P=A/t is a symmetric NONNEGATIVE stochastic idempotent. Every vector in its range satisfies the averaging equation f=Pf. On a connected component of its positive-entry graph, the maximum principle makes f constant: at a maximum every positive-weight neighbour has the same value, then propagate. Conversely constants on a component are fixed. Therefore each component has rank1, P is the averaging projector there, and A has all entries t/(component size). Its diagonal is1, so EVERY component has size t and A is all-ones on it.

These are the same ACTUAL SEVEN t-blocks as§3, and M fixes its base block. This proves generic conclusion3 and the odd-t seven-point quotient. The proof also shows d6 gives that quotient even when t is even.

## 6. Exact dimension bounds in the remaining even-t case

For ALL entries0<=Z<=1, Z²<=Z. Equation(4) gives d>=6. In a P7 application where the seven-block quotient is forbidden, d6 is excluded by§5, so d>=7.

Because gcd(t,15)=1, all gcd(t,delta_g), delta_g<=6, lie in{1,2} when v2(t)=1 and in{1,2,4} when v2(t)>=2.

- In the first case Z lies on the half-grid{0,1/2,1}, so Z²>=Z/2. Taking means in(4) gives4+60/d>=7, hence d<=20.
- In the second case Z lies on the quarter-grid. At EVERY quarter-grid point in[0,1], (Z-1/4)(Z-1/2)>=0. Thus mean Z²>=(3/4)mean Z-1/8=5/56. Equation(4) yields4+60/d>=35/8 and d<=160.

These are universal exact grid/moment inequalities proved from ALL conjugate intersection factors. They are not numerical parameter scouts, a finite group enumeration, or proof that the exceptional case is feasible/empty. No group-order/t bound follows.

## 7. Restore ALL original P7 cosets and keep the exceptional owner pattern literal

Now suppose the eight original indices are7r_l with pairwise-coprime r_l, selected U_i<=M and7 not dividing r_i. Any seven-block quotient constructed in§3 or§5 has selected image inside an ACTUAL point stabilizer in a faithful transitive F<=S7. That stabilizer is seven-free, while v7(|F|)=1. Thus the selected quotient index d_i retains7, with kernel-fiber index k_i dividing its OWN r_i and prime to7.

Exactly as in the ENTIRE200LF paper§7, this recovers ALL eight projected disjointness constraints: selected/source overlaps would lift inside one normal-kernel fiber with coprime k_i,k_l; any source quotient index lacking7 would be coprime to d_i and force such an overlap; therefore all quotient indices retain7, every kernel index divides its OWN private cofactor, and all pairwise projected overlaps lift. The actual F would carry eight P7 cosets, contrary to the named F7-P7 input.

Therefore the original mixed pair can occur only if5|r6,3|r5 and EVEN t. Since t divides r_i (M>=U_i), the selected vertex owns2, while the distinct source vertices own5 and3. Pairwise private coprimality makes these three owners unique; in particular there is at most ONE selected vertex in the full original family that can exhibit ANY such mixed pair at a verified M. Any remaining irreducible dimension lies in7..20 or7..160 according to v2(t).

At the separate least-GROUP-ORDER/simple direct-P7 reduction, any nontrivial seven-block quotient is faithful, and F7-P7 again contradicts the actual original family without selected7-freeness. Thus the same owner-pattern restriction holds at EVERY vertex there. This is not an assertion about minimum private SUM in a fixed G.

For infinite G use the common finite core of all eight original U_l and M first; every coset is a full preimage and every relevant index/orbit partition/disjointness is preserved. No general Sun8-to-P7 ancestry is certified by that direct transfer.

## 8. Complete current high-two-orbit union and exact residual

The old six+one/two-source theorem, the NEW200LF two-five+two theorem, and THIS mixed theorem have DIFFERENT hypotheses. At their exact selected7-free/least-simple boundaries they give at most one6+1 source, at most one5+2 source, and prohibit their coexistence except at the unique private2-owner with the six-source owning5, five-source owning3, actual even outer index and the stated finite dimension ceiling. They do not assert those exceptional sources exist, merge capacities blindly, or rule out every mixed configuration.

ALL5+1+1 sources have Hom dimension THREE and remain outside these two-orbit arguments. Other alpha1–4/7, configurations forcing neither pair, the remaining exceptional even-t mixed case, odd/nonabelian/maximal/self-normalizing/private-composite actual-enlargement collisions and arbitrary full-fibre coherence remain OPEN. A beta5 graph is not automatically a5+2-source graph; the complete orbit partition is required. Original kernel-section/M1 class-AT-MOST2/abelian-exponent4 alternative, high-source136, uniform125/99/least-order63 and EA8 C/O/E/all hidden-neighbour/private/s/outert leads retain their exact scopes. Other group families/extensions/infinite reductions and the global Sun7/general-Sun8 ancestry remain separate unresolved burdens.

A complete fresh gate should consume THIS whole manuscript plus the ENTIRE200LF source and its FULL99/181/F7 boundary, with separate mathematics and dependency/application verdicts. No old positive return, source hash, formal mask or integer divisor is an actual global group/coset lift or acceptance of the union. Original arbitrary-group Sun8 remains NOT_PROVED, no t/group-size/numerical/novelty/SOTA/priority or eight-coset witness claim.

The proof is exact WRITTEN symbolic/index/representation/matrix/finite-grid algebra after actual v121 review RETURN and the new WHOLE primary ACK WRITTEN+SENT before any primary reasoning. No withdrawn historical trial/guidance is consumed, repeated or back-converted. OWN057/047/078/COUNT/M1/v26/v31 TWO late/v33 and all received parent/owner/reviewer findings remain permanent. No scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/GO, dead-kernel restart, author/shared/frozen edit, git, deletion or publication. No formal/human/family/kernel/executable/triple/novelty gate, global cognition/runtime census, new owner/deadline or early final park. Same18, science cutoff2026-10-27T11:05:38-07:00 and delivery12:35:38; original research continues.
