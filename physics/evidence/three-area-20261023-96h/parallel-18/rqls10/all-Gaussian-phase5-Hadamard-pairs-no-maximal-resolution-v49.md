# RQLS10 v49 — EXTEND to ALL independently chosen prime5 Gaussian Hadamards, not merely one matrix's self-pairs

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 11:22:02 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact Gauss/code/flat/moment/MUB/completed-square proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

## 1. The exact larger family, with BOTH matrices chosen independently

For any r0,r1 inF5^* with r1/r0 a NONSQUARE(2or3), put

    d=r1-r0,
    l=d/(4r0r1).

Define the literal fifth-root Hadamard H(r0,r1) by ten exponent rows

    A_i(L_j)=i*j,
    A_i(R_j)=l*i^2+i*j;

    B_k(L_j)=r0*j^2-2r0*k*j,
    B_k(R_j)=r1*j^2-2r1*k*j+d*k^2.

ALL i,j,k are inF5. There are eight parameter choices, but NO equivalence or classification between them is assumed. Let H(r0,r1) and H(s0,s1) be chosen INDEPENDENTLY, with arbitrary independent monomial transformations and arbitrary relative coordinate permutations. Form their actual entrywise row-product QLS10.

**Theorem.** NONE of these pairs produces a MAXIMAL1-RQLS10. Some pairs have100 distinct rays and no resolution; some fail maximality. The theorem covers all parameter pairs/relative pairings, not only the fixedH(4,3) self-family ofv48.

It is a CANDIDATE extension/union pending ENTIRE review. It does NOT classify allBH(10,5), all mutually unbiased product constructions or arbitraryphase5/original arrays. The original maximal1-RQLS10 remains UNKNOWN in general.

## 2. Every parameter matrix and its code really have the required form

The row/column Hadamard proof is exact. Same A-type and same B-type rows give nontrivial linear character sums. For a mixed row pair, restore B_k's removed row phase r0*k^2 and complete squares. The two constant phases are

    -k*i-i^2/(4r0),
    -k*i-l*i^2-i^2/(4r1),

which are EQUAL by l=1/(4r0)-1/(4r1). The Gauss sums with coefficients r0,r1 are OPPOSITES because their ratio is nonsquare. Hence mixed rows are orthogonal and all row norms squared10; columns follow since the matrix is square.

Its code D_r is all words

    f(L_j)=r0*a*j^2+b*j+c,
    f(R_j)=r1*a*j^2+e*j+f0.

It has dimension5, contains1 and the right-block indicator T, and is self-dual for the coordinate dot product. Indeed r0^2+r1^2=0 inF5 and all lower degree power sums vanish. The phase row set R_r spans U_r=D_r/<1>, a maximal totally isotropic4-space in S=1-perp/<1>, and is

    A_i=i*u+l*i^2*t,
    B_k=w+k*v+d*k^2*t,
    u=X+Y, v=-2r0X-2r1Y,
    t=T, w=r0L2+r1R2.

The four directions are independent; l,d are nonzero. The ten points have exactlyTWO five-point affine parabola planes, whose directions intersect in<t>, as proved directly by the no-three-collinear/pigeonhole argumentv43. Thus every affine bijection between TWO such Gaussian row sets sends the first set's t-direction to a nonzero scalar of the second's t-direction. It need NOT be an automorphism of the SAME finite point set; this is the explicit extension needed here.

After all monomial phase/row-label changes are removed, keep an ARBITRARY relative coordinate permutation P. Let

    U=D_r/<1>, V=P(D_s/<1>), k=dim(U intersect V).

All k=0,1,2,3,4 are exhausted below.

## 3. Meet0 and odd meets need no identical-matrix assumption

For k0, any actual quantum transversal's phase flat has dimension<=4 and its projection to the full row4-space has rank4. Hence it is an affine graph bijecting the two ten-point row sets. The unique parabola-plane intersection direction forces its linear part to send t_source to gamma*t_target. Its isotropy at that direction demands dot(P T,T)=0.

But this dot product is the physical5-block overlap m modulo5. If m0or5, P T is1-T orT and supplies a nonzero common phase direction, contradicting k0. Hence m1,2,3or4 and the dot product isNONZERO. This is the complete v43 argument with TWO different Gaussian row sets and their independently proved t-invariants. No relative parameter equivalence is assumed.

For k1or3, the GROUP-FREE theoremv44 applies to ANY fifth-root Hadamard pair, using the actual context-rank4 chainv40–v42. It forbids every quantum transversal via the odd-dimensional nondegenerate alternating quotient form. No Gaussian-specific identification is required.

## 4. Meet2: cubic factor, physical blocks and ALL nonaffine cases still exhaust the residual

For the general Gaussian R_r, exact power sums give the cubic moment

    C_R(A,B,C,D)=-3*C*[l*A^2+d*B^2+d^2*C*D].

The binary part l*A^2+d*B^2 is anisotropic: -d/l=-4r0r1 is nonsquare because r1/r0 is nonsquare. Thus its nondegenerate quadratic4-factor has no totally singular2-plane. As inv47, the projected cubic is zero IFF the projected dual plane annihilates t, i.e. t belongs to the common phase2-space.

If either row shadow cubic is nonzero, ENTIREv47's group-free third/fourth-moment uniqueness theorem forbids a full resolution. If both arezero, T belongs to D_r intersect P D_s. Then P^-1T is a0/1 weight5 word in D_s. A nonconstant quadratic overF5 has THREE values and a nonconstant linear has FIVE; hence such a word must be T or1-T. Thus P preserves or exchanges the physical5-blocks.

For block-setwise P:

- BOTH component permutations affine give either the same quadratic gluing(k4) or only the four-dimensional block-linear vector code(k3), NEVERk2.
- EXACTLYONE affine and the other nonaffine is excluded by the complete v48 MUB/permutation argument, whose coefficients were ALREADY the general nonzero c_in,c_out. On the affine block, four chirp coefficients0,-c_out,c_in*a^2,c_in*a^2-c_out and integer tight-frame multiplicities force any transversal to preserve/swap A/B types. A preserving one has five A/A cells; its matching and both frequency maps force the nonaffine coordinate permutation to be affine. Thus fifty same-type cells cannot be covered.
- BOTH nonaffine leave a common code3-space containing1,T and an extra word with NONZERO quadratic coefficient: otherwise a nonconstant linear preimage would be a quadratic permutation and hence affine, contradiction. In each quotient2-space the two parabola directions remain independent, so each ten-point shadow is two NONPARALLEL full5-lines with one unique DOUBLEpoint and9 support points. Four alternating linear parts and the forced doublepoint translation give at mostFOUR projected transversal maps. They cannot cover9 target values in each row.

Every step uses only the universal polynomial/projection form of D_r,D_s and nonzero l,d, NOT the fixed coefficients4,3. All affine shifts/orientations/exchanges and multiplicities remain as inv48. This completely closes k2 for independently chosen parameters, while the entire nonzero-moment/doublepoint/permutation proofs remain operative dependencies—not assumed accepted branches.

## 5. Meet4 forces block-affine alignment, but maximality excludes two degenerate leading cases

Suppose P D_s=D_r. The intrinsic weight4 supports of EACH code are exactly the four-subsets of its two physical5-blocks: a nonzero quadratic has total weight>=6, and a block-linear word has weight4 only on one block. Therefore P maps blocks setwise.

Projection onto either block is RS3=<1,j,j^2>, with dual RS2=<1,j>. A coordinate permutation preserving those spaces must be affine because it sends j to a linear function. If P exchanges blocks, absorb that exchange into H(s0,s1): it replaces its parameters by(s1,s0), with d,l both negated, still in the same explicit family. Thus we may write the aligned coordinate maps

    L_j -> L_(a*j+b), R_j -> R_(c*j+e),
    a,c nonzero,
    s0*a^2=lambda*r0,
    s1*c^2=lambda*r1,

for some lambda!=0. ALL shifts b,e remain arbitrary.

A Gaussian row set's cross-type differences run through ALL25 balanced code words at quadratic level+1, and their negatives through level-1. The linear map from the two row parameters to its two block-linear coefficients is invertible because r0!=r1; Gauss balance fixes the remaining constant uniquely. Thus if lambda=+1or-1, the transformed cross differences coincide with one of those old surfaces, producing repeated projective rays. A MAXIMAL candidate must therefore have

    lambda=2or3.

Also a=c would align the two TOP parabola direction planes. Each five-point nondegenerate parabola has as its difference set ALL20 vectors with nonzero linear direction coefficient and arbitrary t coefficient in that plane. The two top difference sets would intersect, again producing repeated rays. Hence maximality additionally requires

    a!=c.

These are only NECESSARY maximality conditions; no full maximal-class classification is silently asserted.

## 6. The remaining meet4 maximal case cannot contain a preserving transversal

For lambda2or3 the four restricted chirp coefficients on either affine physical block are distinct (or, equivalently, use the general tight-frame argumentv48). Therefore a quantum transversal must preserve or swap A/B row/column types. To cover any of the fifty same-type cells it must preserve types and include all five top/top cells.

Let the top matching be f(i). Their affine-block frequencies a*i-f(i) are all different, since proportional five-component restrictions would create five identical root terms in a ten-term orthogonal sum. The complete F5 permutation lemmav48 forces

    f(i)=v*i+w0,

with v!=0. Pick ANY one bottom/bottom cell of the same transversal. Its left/right quadratic coefficients RELATIVE to a top/top cell are

    qL=r0*(lambda-1), qR=r1*(lambda-1),

both nonzero and of opposite square character. Completing the two Gauss sums for its inner product with EACH of the five top/top cells therefore requires equality of their completed phase polynomials in i.

All arbitrary coordinate shifts and w0 affect only linear/constant terms. The coefficient of i^2 MUST satisfy

    l_s-l_r*v^2
      +(c-v)^2/[4r1*(lambda-1)]
      -(a-v)^2/[4r0*(lambda-1)]=0.                (LEAD)

This formula keeps both independent Gaussian curvatures l_s,l_r and the actual affine slopes; it is not v45's fixed-matrix discriminant copied unchanged.

Use

    4l_r=1/r0-1/r1,
    4l_s=1/s0-1/s1
          =a^2/(lambda*r0)-c^2/(lambda*r1).

Multiplying LEAD by4lambda(lambda-1) and collecting squares gives EXACTLY

    (c-lambda*v)^2/r1=(a-lambda*v)^2/r0,
    (c-lambda*v)^2=(r1/r0)*(a-lambda*v)^2.

The ratio r1/r0 is NONSQUARE. Therefore BOTH squared factors must beZERO. This forces a=c, contradicting the necessary maximality condition in section5. No preserving transversal exists; the fifty same-type cells cannot be covered by any full resolution.

This settles ALL remaining meet4 parameter pairs. Nonmaximal lambda+-1 or a=c branches were excluded by duplicates, NOT falsely declared unresolvable.

## 7. Entire all-parameter/all-permutation conclusion and exact original gap

Sections3–6 exhaust every code meet k and every independent choice(r0,r1),(s0,s1), together with every relative coordinate permutation and independent monomial changes. Hence no pair from this explicit eight-matrix prime5 Gaussian family produces a MAXIMAL1-RQLS10.

The extension is genuinely larger than v48's fixed self-pair theorem: transverse maps now relate TWO parabola sets; cubic factors have general l,d; same-code leading equations retain BOTH curvatures and reduce to a nonsquare-ratio equality. No assertion that all eight matrices are monomial-equivalent or that allBH(10,5) matrices have this form is used. Published names/possible equivalences ofS10,B10 are not operative inputs.

The original maximal100-ray1-RQLS10 remains UNKNOWN. Arbitrary otherBH5, non-Hadamard-pair phase5 configurations, other phase alphabets, the fullTypeIV biunitary master and unrestrictedintrinsic10/4+6/5+5 arrays remain OPEN. A further construction must leave this now-closed explicit Gaussian-pair family, not change another quadratic parameter or relative permutation inside it.

## 8. Full union review/import/assurance contract

Read/reconstruct ALL EIGHT sections/endings AND ENTIRE operativev40–v44/v47/v48 context-rank, graph, moment and MUB/permutation inputs. Required new claims include EVERYparameter Hadamard/code normalization; TWO-set t-invariant; general elliptic cubic; all t-common indicator/block cases; intrinsic weight4/RS alignment for TWO codes; lambda+-1 cross-surface collision; aligned top-parabola collision; FULLshift-independent LEAD justification; exact nonsquare square-equality closure; and distinction between maximality failure and no-resolution. A fixed q,l sample, one matrix's self-pairs or a branch review is not this full union.

No finite classifier, external model, scientific execution or private approximate scout was used. All operative arithmetic is exact WRITTEN and NOT machine-checked. Independent finite-witness/checker/control/vendor/priority gates NOT PERFORMED underHOLD. No100-ray1-RQLS witness/unrestrictedno-go/formal/kernel/family/human/current-openness/novelty promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues genuinely OTHER original geometry, no early pending-review park.
