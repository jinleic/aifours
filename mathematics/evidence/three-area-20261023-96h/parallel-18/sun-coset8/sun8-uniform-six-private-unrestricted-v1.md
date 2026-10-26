# Sun8 — UNIFORM-SIX source closure with UNRESTRICTED private indices

Owner MathSun8-2. Actual pre-write `/bin/date`: **Sun Oct 25 16:03:55 PDT 2026**. **NEW COMPLETE WRITTEN CANDIDATE; NOT ACCEPTED.** This removes the prime-to-six hypothesis from the136LF direct theorem. It is one complete actual-group/source-lift proof plus its precise original-normalizer corollaries, not another local section enumeration. All original private prime powers, possible private2/3/5/7 owners, hidden/full U_j and the selected/e sources remain literal.

The136LF candidate `sun8-uniform-six-actual-source-lift-closure-v1.md`, SHA `e6c1714454413c5f032134e4b1a5f58604884a29096eb99e7ebc8f3d3e51e982`, remains separately under v99 review; no future verdict is used here as acceptance. The58LF direct-normalizer corollary SHA `40b074bcc5c7fc82f85bdd9f94be9249f0c7527d3796b0dc06101c185f097d86` correctly removes the unnecessary rank-two kernel prerequisite. This successor now ALSO removes its prime-to6 restriction. The217LF rank-two detour, SHA `8be5b4c65fe9aa6d14045805e1ee71c4e15263a0988b71f8cb238cab4127feef`, is retained as immutable unaccepted history, not needed or counted as independent new branch credit.

## 1. Exact direct theorem and named input boundary

Let G be an ACTUAL finite group with EIGHT pairwise-disjoint LEFT cosets g_l U_l of ORIGINAL subgroups, [G:U_l]=7r_l, all r_l arbitrary positive pairwise-coprime integers. Distinguish SIX sources j=1,...,6; the other two are i and e. Suppose an ACTUAL subgroup M≤G satisfies

[G:M]=7t,
gcd(t,r_j)=1 for all six j,
[U_j:U_j∩M]=6t for all six FULL original U_j.

**There is NO gcd(r_j,6)=1 assumption.** M need not normalize U_i, contain U_i, equal a core normalizer, or be normal G. No achieved minimum, simple-G, bounded t, elementary quotient, private-prime or source-preserving divisibility assumption belongs to this direct theorem.

> **UNIFORM-SIX-ALLPRIVATE:** no such eight-coset family and actual M exist.

The sole non-elementary-sized finite input is the complete catalogue-free faithful degree-seven classification already reconstructed in complete predecessor Part2,181LF SHA `2c8949dfa512ca3d89549b04d42bea9be8a515081cb3a3ba7762dd3b2e7b46e8`, at its named classical A7 simplicity/Eisenstein boundary: a two-transitive degree-seven group is affine42, GL3(2), A7 or S7; in A7/S7 every index-seven subgroup is a natural point stabilizer, and in GL3(2) every index-seven subgroup is point or line stabilizer. Classical A6 simplicity is explicitly used below to exclude relative index5. The SAME-ACTION completion needed here is proved in §5, so the full mixed NC7 theorem is not a hidden additional prerequisite.

Current predecessor adoption `RUN/sun-global-kernel-section-complete-parent-v1.md`,45LF SHA `4d23122673282636bd4c008bae7b1cc1c241090238e1c721b47592af46f88232`, was read completely after actual v93 RETURN/resumptionACK. Mandatory M1 permits abelian exponent4/PhiV4 under class AT MOST2; exact nonabelianness/class2 remains NOT_RECONSTRUCTED. None of Part3, class2, R4 or a rank theorem is a premise here; its finding history is not erased. This new complete proof/application requires its own fresh union disposition, not automatic v92/v99 inheritance.

## 2. Actual orbit construction and unique shared component — no private-prime restriction

Let Omega=G/M, the actual7t-point left G-SET. For any U_j orbit of length ell, the subgroup index [G:U_j∩gMg^−1]=7r_j ell is a multiple of7t. Thus t divides ell, using gcd(t,r_j)=1. The orbit through M has6t points. The remaining t points form ONE additional orbit T_j, necessarily unique. U_j acts with exactly TWO orbits on the SAME Omega.

Use Hermitian permutation modules X=C[Omega], Y_j=C[G/U_j]. An equivariant matrix Y_j→X is constant on diagonal G-orbits, equivalently on U_j-orbits in Omega, so Hom dimension is2. Finite unitary modules decompose orthogonally by invariant complements. A map between irreducibles is0 or an isomorphism; over C an endomorphism commuting with the group is scalar by subtracting an eigenvalue. Hence the Hom dimension is the sum of products of multiplicities. Each transitive permutation module contains constants once. The remaining dimension1 proves EXACTLY ONE nontrivial shared irreducible, multiplicityONE in BOTH modules. Denote its unique actual subspace of X by W_j.

Define the ACTUAL integer incidence matrix I_j(omega,gU_j)=1 if omega∈gT_j and0 otherwise. It is well-defined because U_j preserves T_j. Each column has t ones; transitivity/counting gives row degree r_j. Its nonempty proper columns show its image is constants plus W_j, not constants alone. No matrices/characters are evaluated by a program.

If W_j and W_k are different, they are orthogonal. Their incidence operators therefore give

I_j^* I_k=(t/7)J,  |T_j∩T_k|=t/7>0.

The scale follows from column size t and row degrees: the constant eigenvalue calculation gives r_k t on a space whose constant vector has7r_k entries. The intersection is invariant under A=U_j∩U_k. ORIGINAL disjointness makes U_jU_k proper, so

[G:A]=7r_jr_k d, 1≤d≤6.

Every A-orbit on Omega has length a positive multiple of t/gcd(t,d)>t/7. Such an orbit cannot fit in that nonempty invariant intersection of size t/7. Thus all W_j are one SAME W. Only private coprimality, not prime-to6, was used.

## 3. One ACTUAL seven-block action for ALL six full original groups

Let E project orthogonally to W and dW=dim W. Constants, Schur's scalar argument and the trace give

I_j I_j^*=(r_j/7)J+(6t r_j/dW)E.

Indeed the constant eigenvalue is t r_j and trace is7t r_j, leaving6t r_j for W. Thus all normalized Gram matrices I_j I_j^*/r_j are identical. Every entry is c_j(x,y)/r_j, where c_j is an integer number of common incidence columns between0 and r_j. Equality for two privately-coprime r_j,r_k forces c_j either0 or r_j. Two incidence rows are therefore disjoint or identical.

Every column gT_j is EXACTLY one identical-row class: points in a column share an incidence and hence have identical rows; identical rows share that column. Each class has t points. There are SEVEN classes, identical for all six j because their normalized Gram matrices agree. Equivariance makes them an ACTUAL G-invariant block system on Omega.

Let L be the stabilizer of the block containing basepoint M, K=core_G(L), F=G/K, pi:G→F. L contains M and has index7. Each H_j=pi(U_j) fixes its small block and is transitive on the OTHER SIX blocks, because U_j is transitive on its6t-point large orbit. Thus F is two-transitive on seven blocks. Each regular projected subgroup index is

[F:H_j]=7a_j, a_j|r_j,
[K:K∩U_j]=r_j/a_j.

The fixed-block condition alone gives factor7; full point-stabilizer equality is NOT assumed for a private2/3 source. This is the essential correction to the older proof route.

## 4. Full point-stabilizers: retain the actual thin sources

By the named faithful-degree7 classification F is affine42, GL3(2), A7 or S7. Call a regular source FULL when a_j1, so H_j is the natural block point stabilizer; otherwise call it THIN. All remain actual original sources.

- **Affine42:** a point stabilizer has order6. Since H_j is transitive on six points, its order is divisible6, so a_j1. ALL six regulars are FULL, irrespective of private indices.
- **GL3(2):** a natural point stabilizer has order24. Since6 divides |H_j|=24/a_j, necessarily a_j divides4. Thus every thin regular consumes private2, and private coprimality permits AT MOST ONE. There are at least FIVE full regulars. No transitive-subgroup catalogue or unnecessary index4 elimination is needed.
- **A7/S7:** natural point stabilizers have orders360/720 and are A6/S6. If gcd(r_j,6)=1 then a_j is1 or5. An index5 subgroup of A6 is impossible: its five-point action would inject simple A6 into S5 of smaller order. For S6, restricting a five-point coset action to A6 is either injective (again impossible) or trivial, which would put order360 A6 into a subgroup of order144. Hence a_j5 is impossible and such a regular is FULL. At most TWO private factors among the six own2 or3, so there are at least FOUR full regulars; any two thin regulars consume BOTH private2/3 owners.

In every case there are at least FOUR full regulars, at least THREE of them7-free (at most one private factor owns7). Choose ONE full regular j with7∤r_j. Its K-kernel index is r_j, coprime to both selected/e kernel indices, which divide7r_i,7r_e. Hence its index7 projected coset is disjoint from both selected/e projected cosets. If either selected/e projected subgroup index lacked7, coprime indices would force intersection with that index7 coset. Therefore

[F:pi(U_i)]=7a_i, [F:pi(U_e)]=7a_e,
a_i|r_i, a_e|r_e,
[K:K∩U_i]=r_i/a_i, [K:K∩U_e]=r_e/a_e.

Now ALL EIGHT K-kernel indices divide their OWN pairwise-coprime private factors. Any overlap of projected cosets would lift in the SAME actual K-fibre to two cosets of coprime-index subgroups of K and force an original intersection. Thus ALL EIGHT projected cosets in F are pairwise disjoint, INCLUDING selected/e. This restores the complete actual projection before any enlargement of a thin point stabilizer.

## 5. Written same-action completion and a two-output rigidity fact

In ANY two-transitive action, natural point-stabilizer cosets are constraints g(x)=y. Two are disjoint exactly when they share an input with distinct outputs, or share an output with distinct inputs. If both inputs and outputs differ, two-transitivity supplies an intersection. A pairwise-disjoint family of at least three therefore lies in ONE rook row or column. Six such cosets have as their EXACT complement the one missing seventh natural point-stabilizer coset. Five have complement the UNION of the TWO missing natural point-stabilizer cosets.

If the clique is a column, invert the ENTIRE group variable once. Inverses of left subgroup cosets are left cosets of conjugate subgroups with the same indices; disjointness and all private divisors remain. Every constraint is reversed simultaneously. We may therefore orient a five-coset clique as g(p) taking five fixed distinct outputs; its complement is {g:g(p)∈{y1,y2}}. No per-source inversion is used.

For A7/S7 let a coset xH of index7a, with gcd(a,6)=1, lie in that complement. Since a divides |F|/7, a is1 or5. H's orbit on p has size at most2. If size2, H lies in the setwise stabilizer of a two-set, whose index is binomial(7,2)=21. Then21 divides7a, forcing3|a, contradiction. Thus H fixes p, and its relative index in that natural point stabilizer is a. The index5 impossibility from §4 gives a1. Consequently **any such privately-prime-to6 coset disjoint from five full natural point cosets is ITSELF full natural**. This is actual orbit/index reasoning, not a title/norm-style dismissal or an assumed lossless enlargement.

For GL3(2), an arbitrary index7 subgroup is point or line type at the named classification. A line coset disjoint from FIVE point cosets is impossible. After the one global orientation, the point constraints have one input P and five distinct outputs. Point/line constraints intersect iff input/output incidences agree, by transitivity on flags/nonflags. Disjointness would require five outputs all incident with one line (only3 available) or all nonincident (only4 available). Thus any additional index7 coset disjoint from those five is natural POINT type.

## 6. Complete elimination of ALL thin-source cases

Every index mentioned now is in the ACTUAL quotient F, with ALL eight projected cosets already disjoint. The a_l are divisors of the ORIGINAL pairwise-coprime r_l. A left coset contained in another subgroup coset becomes, after one translation, a subgroup coset inside it with the ratio of those indices; this is used literally below.

### No thin regular

The six full regular point cosets have one index7 complement by §5. It contains the ENTIRE selected/e projected cosets. Their relative subgroup indices in it are a_i and a_e, privately coprime. They intersect, contradiction. No statement that selected/e separately fix a point was needed.

### GL3(2), the one possible thin regular

It consumes private2, so among selected/e at least ONE private factor is prime-to6 (at most one can own3). For that source a divides |F|/7=24 and is prime-to6, so a1. There are already FIVE full regular point cosets; §5 rules out line type for this additional index7 coset. Thus six ACTUAL original projected cosets are full natural point cosets. Their complement is one index7 coset containing the remaining thin regular and the other selected/e coset, with relative indices privately coprime. They intersect. The thin subgroup was never presumed full or silently enlarged.

### A7/S7, exactly one thin regular

The thin regular consumes at least one private2/3 owner. At least ONE of selected/e is prime-to6. Its entire coset is disjoint from the FIVE full regular point cosets; the two-output orbit argument in §5 forces it to be full natural. We again have six actual full natural cosets, and their one-coset complement contains the thin regular and the other selected/e source with coprime relative indices. Contradiction.

### A7/S7, exactly two thin regulars

They consume the TWO distinct private2/3 owners, so selected/e are BOTH prime-to6. Their a_i,a_e are1 or5. At most one owns private5; therefore at least ONE a is1, giving a fifth actual full natural point coset alongside the FOUR full regulars. The other selected/e coset is now disjoint from five full point cosets and is prime-to6; §5 forces it full natural too, EVEN if its proposed index had been35. Six full natural cosets leave one index7 coset containing the TWO thin regular projected cosets. Their relative indices a_j,a_k divide DISTINCT private factors and are coprime, so they intersect. Contradiction.

Affine42 had no thin case. These cases exhaust every degree7 group and every possible thin regular, including private2/3/5/7/composite ownership. We did not need to classify the thin subgroups, align their independent fibres, or assume any full original U_j normalizes a common B. Thus **UNIFORM-SIX-ALLPRIVATE is proved as a WRITTEN CANDIDATE at the exact named finite/classical input boundary**.

## 7. Immediate original-normalizer consequences, ALL ranks and ALL private factors

Return to any actual finite P7 family and selected original U. At the separately written direct normalizer identity [G:N_G(U)]=7s, r_i=s|N/U|, every original neighbour has

[N:N∩U_j]=r_j alpha_j, alpha_j=beta_j c_j≤7,
[U_j:U_j∩N]=s alpha_j.

For ANY SIX alpha_j6 take M=N, t=s. Its coprimality with all six r_j follows from s|r_i. The theorem excludes the family. **At most FIVE original neighbours can have alpha_j6, with NO private-prime qualification, at EVERY selected vertex.** No achieved minimum is needed for this application once the actual direct normalizer identity is supplied.

This excludes SIX actual C sources beta3,c2 at ANY global character rank, INCLUDING rankONE3+3 and a C itself owning private3. It excludes SIX beta2,c3 sources INCLUDING an even-private source, any rank-one/aligned/hidden configuration, and cases with no character interpretation. It also excludes ANY mixture of (beta,c)=(1,6),(2,3),(3,2),(6,1) across six original neighbours. All integer indices remain full; no private2/3 was cancelled to make the theorem apply.

Taking M=U, t=r_i instead excludes SIX beta_j6 original neighbours, with unrestricted private factors. More generally ANY actual overgroup M≥U of index7t may be tested by its FULL original six source indices6t. An integer divisor alone does not manufacture such an M, and M is not claimed collision-free.

These corollaries properly supersede the prime-to6 caveat of the58LF corollary and its residual, ADDITIVELY. They do not retroactively enlarge the frozen136LF v99 source quantifiers, erase the217LF detour or Part3 M1, or obtain automatic acceptance from another gate. A fresh complete union reconstruction must check this new thin-source argument and all applications.

## 8. Exact residual, process and nonclaims

The actual remaining finiteP7/source-lift gap is now configurations with at most FIVE alpha6 neighbours at EVERY available actual test overgroup, alongside alpha1–5/7 mixed-source obstructions and the remaining nonabelian/odd/maximal/self-normalizing/private-composite legal-enlargement barriers. Six-C rankONE, a private3 C among six, and even-private ternary source among six alpha6 do NOT survive at this NEW CANDIDATE theorem. Fewer C/B sources and genuinely lower counts still remain; no claim forces every original vertex to have six alpha6 neighbours.

The unrestricted arbitrary-group Sun8 problem, inherited global Sun7/finite-core authentication, an actual eight-coset counterexample, all outer t/group-size/index bounds, worldwide priority/novelty and publication clearance remain OPEN/UNESTABLISHED here. Written mathematics is not formal/kernel, human, configured-family or executable verification. No scientific interpreter/Eval/calculator/arithmetic or symbolic program/enumeration/solver/replay/CLI/nestedagent/newGO was used; only written group/representation/orbit/index reasoning and source/clock/hash metadata. All frozen bytes/history, v9/v10/v11/HOLD, original eighteen slots/cutoff/deadline and exclusive write root remain. Primary research continues rather than parking at a gate.
