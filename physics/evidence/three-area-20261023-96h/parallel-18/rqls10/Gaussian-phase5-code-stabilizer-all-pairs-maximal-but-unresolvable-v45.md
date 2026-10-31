# RQLS10 v45 — ENTIRE Gaussian same-code meet4 family closed: duplicate rays OR50 untransversalizable cells

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 10:43:13 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact code/permutation/quadratic/Gauss/affine-polynomial proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

## 1. Entire meet4 theorem and new literal100-ray example

Use the literal Gaussian fifth-root Hadamard H and self-dual code D printed/proved in ENTIREv43. Its coordinates are L_j,R_j(j inF5), and its ten dephased row classes, in code coordinates(a,b,d,t), are

    A_i=(0,i,i,3i^2),
    B_k=(1,2k,-k,-k^2).

A code coordinate word represents

    f(L_j)=4a*j^2+b*j,
    f(R_j)=3a*j^2+d*j+t,

modulo a constant word. Let P be ANY coordinate permutation preserving D; equivalently its two row-code4-spaces have meet dimension4. Consider the actual Hadamard-pair QLS with phases P p_row-p_column.

**Theorem.** EVERY such pair fails to be a maximal1-RQLS10. Exactly one parameter class gives100 distinct rays; in that entire class fifty SAME-top/bottom-block cells belong to NO quantum transversal. Every other class has repeated rays. No resolution covariance is assumed.

The maximal class is NONEMPTY: the literal coordinate permutation action

    (P f)(L_j)=f(R_j),
    (P f)(R_j)=f(L_(3j))

is one example. Together with H's explicit formulas in v43, this defines a NEW100-distinct-ray phase5 QLS10 at AUTHOR-WRITTEN level. It has50 untransversalizable cells, so is NOT an original1-RQLS witness.

Combined as a CANDIDATE union with v43(transverse meet0) and v44(odd meets1/3), the literal Gaussian self-pair construction under ARBITRARY relative coordinate permutations is now reduced ONLY to meet dimension2. No Gaussian-WLOG or arbitraryphase5 classification is claimed.

## 2. ALL coordinate permutations preserving D, derived without a code classifier

Recall D consists of all words

    f(L_j)=4a*j^2+b*j+c,
    f(R_j)=3a*j^2+d*j+e.

If a!=0, each block quadratic has at mosttwo zeros, so its total Hamming weight is at least6. If a0, both blocks are linear; a weightFOUR word must be a nonconstant linear function on ONE whole5-block and ZERO on the other. Hence the weight4 supports are EXACTLY the ten four-subsets obtained by deleting one point from one of the two5-blocks.

The relation two coordinates lie in a common weight4 support recovers exactly the two blocks. Therefore any coordinate permutation preserving D must preserve or exchange L,R. This is not an assumed block ansatz.

Projection of D onto either block is the complete length5 quadratic evaluation code RS3=<1,j,j^2>. Its dot-product dual is RS2=<1,j>, since all power sums throughdegree3 vanish. A coordinate permutation preserving RS3 preserves RS2; in particular the permuted coordinate function j must be alpha*j+beta with alpha!=0. Thus every block permutation is AFFINE, not an arbitraryS5 matrix guessed from examples.

All code-preserving permutations therefore have precisely one of these forms, with a inF5^*, b,d inF5:

PRESERVE blocks:

    (P f)(L_j)=f(L_(a j+b)),
    (P f)(R_j)=f(R_(c j+d)),      c=+a or-a.

SWAP blocks:

    (P f)(L_j)=f(R_(a j+b)),
    (P f)(R_j)=f(L_(c j+d)),      c=+2a or-2a.

The slope constraints follow by equating the transformed quadratic coefficients: preserving requires a^2=c^2; swapping requires3a^2/4=4c^2/3, hence c^2=4a^2. Conversely each listed map preserves the entire defining code, so this is an exhaustive two-sided classification. There are no hidden monomial scalings; we classify the actual relative COORDINATEPERMUTATIONS, with row/coordinate phases removable as already stated.

## 3. Exact difference set of the ten row classes

Let R={A_i,B_k}. Its nonzero difference set is the DISJOINT union:

- a=0,b!=0,d=b,t arbitrary (20 words);
- a=0,b!=0,d=2b,t arbitrary (20 words);
- a=+1,t=3d^2-b^2,b,d arbitrary (25 words);
- a=-1,a*t=3d^2-b^2,b,d arbitrary (25 words).

For within-parabola pairs, difference h!=0 fixes b,d, while the sum of the two parameters runs overF5, giving every t. For a cross difference B_k-A_i, solve b=2k-i,d=-k-i, then k=2(b-d),i=3b+d, and compute

    -k^2-3i^2=3d^2-b^2.

Thus each of the90 ordered nonzero row differences is distinct; the ten-point row set is a Sidon set at this exact code scope. No finite set enumeration was run.

For a general code word(a,b,d,t), the corresponding flat phase ray is orthogonal to the all-ones phase ray IFF

    a=0:      b!=0 AND d!=0;
    a!=0:     a*t=3d^2-b^2.                       (ORTH)

The a0 statement follows from two linear character sums. For a!=0, the two quadratic Gauss sums have opposite square characters; completing squares leaves equal phases exactly when a*t=3d^2-b^2. The common Gauss sum is nonzero (its primitive fifth-root polynomial is not a multiple ofPhi5). Therefore ORTH is an EXACT complex orthogonality criterion, not a finite-field necessary relaxation.

## 4. Exactly WHICH same-code pairs have100 distinct rays

A projective collision in a pair occurs exactly when a nonzero difference of R also lies in P(R-R). All differences are code classes modulo1; this is the correct maximality test, not a trace or orbit census.

For a block-preserving P, the quadratic coefficient a_code is multiplied by a^2=+1or-1. Coordinate permutation preserves the exact balanced counts. The entire25-word ORTH surface at a_code=+1 is therefore mapped to the corresponding surface at a_code=+1or-1, BOTH already in R-R. Thus repeated rays necessarily occur in ALL preserving-block cases.

For a block-swap P, the quadratic coefficient is multiplied by lambda=2a^2, equal to2or3. Its cross differences go to a_code=+lambda or-lambda and cannot meet the old a_code=+-1 surfaces. On the a_code0 differences, the slope ratio d/b transforms to(c/a)/(d/b). The old ratios are1,2.

- If c=+2a, they map to2,1, giving collisions.
- If c=-2a=3a, they map to3,4, disjoint from1,2.

In the latter case BOTH parts of the old difference set avoid the new one, so ALL100 rays are distinct. These exhaust all parameter cases, including shifts b,d, which change t but not the asserted ratio sets/surface levels.

Hence maximality occurs EXACTLY in the block-swap class c=-2a. The example in section1 is a1,b0,d0,c3.

## 5. A structural lemma: any ten-ray basis inside D uses exactlyTWO quadratic-coefficient levels

Write

    Q2(a,b,d,t)=a*t+b^2-3d^2.

When two phase points have DIFFERENT a_code, ORTH says their difference is Q2-isotropic. The binary quadratic b^2-3d^2 is anisotropic overF5 because3 is nonsquare.

If v is Q2-isotropic with v_a!=0 and w is another isotropic vector orthogonal to v, subtract(v_a^-1*w_a)v from w. Its a-coordinate is0 and it remains isotropic/orthogonal to v. Anisotropy forces its b,d coordinateszero; orthogonality to v then forces its t coordinatezero. Thus w is proportional to v. No two independent totally singular directions can include such a v.

Consequently three mutually orthogonal phase points at THREE different a_code levels lie on one isotropic affine line. Any additional clique point is orthogonal to two of those at different a_code levels from its own, so it lies on that SAME line. A line overF5 has only5points, hence a ten-ray ONB cannot use three or more levels.

Within ONE a_code level, ORTH requires all b coordinates pairwise different, so at mostFIVE points fit. Therefore EVERY ten-ray ONB inside this code uses EXACTLYTWO a_code levels, with five rays in each.

This is an actual complex-orthogonality lemma using ORTH, not a generic quadratic clique condition or imported spectral classification.

## 6. Maximal same-code pairs force a block-preserving OR block-swapping transversal

In the maximal class c=-2a let A=a^2, lambda=2A in{2,3}. The four cell blocks(top/bottom row versus top/bottom column) have four DISTINCT a_code levels:

    top/top:0,       top/bottom:-1,
    bottom/top:lambda, bottom/bottom:lambda-1.

A full transversal has x top/top and x bottom/bottom cells, and5-x cells in each cross block. If1<=x<=4, it has allFOUR levels, contradicting section5. Hence x=0or5: a quantum transversal must be wholly block-SWAPPING or wholly block-PRESERVING. This consequence holds for arbitrary chosen resolution, not one declared symmetric.

We now rule out the ENTIRE preserving possibility. Thus any cell in either same-block25-cell region will be untransversalizable, enough to forbid any full resolution.

## 7. ALL preserving permutations fail by a nonsquare discriminant, including ALL affine coordinate shifts

For the maximal class, dephase the transformed Hadamard row words at L0. Its top and bottom rows are respectively

    C_i=(0,a*i,3a*i,2i^2+(d-b)i),
    D_k=(lambda,a*(b-k),a*(k-d),
                   k^2+(2d+b)k+4d^2-3b^2).

These are complete formulas for ALL a!=0 and ALL b,d; no shift normalization is assumed WLOG. A preserving transversal would pair C_i with original A_(f(i)), and D_k with original B_(g(k)), where f,g are permutations ofF5.

The two phase differences lie at levels0 andlambda-1. Apply ORTH to every cross pair. Direct expansion gives the required equation E(i,k)=0 for ALL i,k, where

    E(i,k)=2i^2+a*i*f(i)+A*f(i)^2
            +4k^2+3a*k*g(k)+2A*g(k)^2
            +2a*[k*f(i)+g(k)*i]
            +(d-b)i+a*(2b+d)f(i)
            -(2d+b)k+a*(b+d)g(k)+d^2+3b^2.      (E)

All coefficients are exact inF5. This expansion retains the arbitrary coordinate shifts; its mixed terms and quadratic coefficients were not replaced by a special zero-shift example.

Take a mixed finite difference between ANY distinct i1,i2 and k1,k2. The only surviving terms force

    [f(i1)-f(i2)]/(i1-i2)
       =-[g(k1)-g(k2)]/(k1-k2).

Thus f(i)=s*i+v0 and g(k)=-s*k+w0, with s!=0. Substitute into E. Its coefficient of i^2 must vanish (a degree<=2 polynomial vanishing at allfive i has all coefficientszero):

    A*s^2+a*s+2=0.

Its discriminant is a^2-8A=3A. Since A=a^2 is a NONZERO SQUARE and3 is a NONSQUARE inF5, this equation has NO solution. Contradiction. No preserving quantum transversal exists for ANY parameters a,b,d in the maximal class.

Therefore ALL50 same-block cells belong to NO quantum transversal. Swapping transversals were not needed and are not asserted absent. A full resolution cannot cover the same-block cells, so no maximal1-RQLS10 results from ANY code-stabilizing Gaussian pairing.

## 8. Entire union scope, literal positive example and remaining meet2 problem

This covers ALL relative permutations with P(D)=D (meet4): nonmaximal classes by actual difference collisions, maximal c=-2a classes by the complete orthogonality/two-level/discriminant argument. It supplies a genuine literal100-distinct-row/column example but PROVES its original resolution impossible. It is not a near-witness promoted to100-ray1-RQLS.

The literal Gaussian self-pair family under arbitrary relative permutations now has candidate closures at meet0(v43),meet1/3(v44) andmeet4(here). ONLY meet2 remains. This is a JOINT CANDIDATE union until full review reads/reconstructs all three scopes and v44's exact-rank dependencies. No code/Gaussian classification is assumed for arbitrary BH(10,5), generalphase5QLS or original noncovariant arrays.

Review ALL EIGHT sections/endings plus ENTIREv43 literal Hadamard/code input: intrinsic weight4support block recovery; projectionRS3/dualRS2 affine proof; both slope cases; all difference-set surfaces; exact complex ORTH; exhaustive maximality classes; all two-level and contingency cases; FULLshift-dependent E and slope/discriminant proof; positive example and no-fullresolution application. A code automorphism count or one parameter value is not the theorem.

No Magma/code classifier or native enumeration was run. Public quinary-code data was read statically while investigating, but is NOT an operative premise; every classification used here is proved from the literal D. All claims are AUTHOR-WRITTEN pending entire math/dependency/application gates. No independent finite-witness checker/control/vendor/priority gate performed or passed; no formal/kernel/family/human/current-openness/novelty/original-witness promotion. Original maximal1-RQLS10 and its generalintrinsic10/4+6/5+5 branches remain OPEN. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues genuinely remaining Gaussianmeet2 or another original geometry, no early pending-review park.
