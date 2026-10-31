# Addendum1 — unrestricted all-member boundary exposure exactly controls a two-coordinate move

Actual native clock before writing: **Tue Oct 27 14:56:40 PDT 2026**.
PhysicsMOQLS8-2 / physics-4. **WRITTEN, UNREVIEWED all-variable coupling candidate**, no novelty or stronger-verification claim. Original output `prerequisite-derivation-v1.md` stays frozen at SHA256 `7e6c40061b6079dc306296f21dc37d908424045ec4f10ba8bd2e94aefe662e24`.

## 1. New scope relative to v1

The first packet identifies the failed reverse lifting of classicalization and the paper's global weight≤2 ceiling. Here the **global weight bound is removed**: every other entry of the selected member and every entry of its three mates may have arbitrary weight and arbitrary complex phases. The result is an exact actual-family necessary-and-sufficient condition for the proposed operation, followed by a genuine rigidity obstruction and a complete support-collapse criterion.

This does not posit that a nonclassical four-family exists or that every family has the required exposure pattern. It is a universally quantified consequence for any ACTUAL four-family. It is not merely another support budget or a claim that an abstract pattern can be glued.

Correctness inputs are only the admitted QLS/MOQLS definitions, the operation explicitly described in the admitted paper's §3 Lemma10, and the elementary complex-inner-product facts proved/used below. The operation's source is PRIOR; its forward theorem is not used as a black box. No old proof, local-span source, held candidate, commutant shortcut or ZERO consumer is used. Prior authorship/exposure is not erased and no unaffected-private-cognition certificate is asserted.

## 2. Actual-family variables and the operation

Let (A,B2,B3,B4) be ANY actual ordinary complex four-MOQLS(n) family, in particular allowing n=8. Every member is an actual QLS and every same-cell pair-product list is an ONB. None of the four is assumed classical.

Choose an arbitrary ONB for **A only**, two distinct coordinate indices p,q and S=span{e_p,e_q}. Write P_S for its orthogonal projection. Let

    Omega={x in X: support(A_x)={p,q}},  X={1,…,n}².

The other members keep their own independent frames. For an arbitrary unitary U on S, define

    A^U_x=U A_x  if x in Omega;    A^U_x=A_x otherwise.

There is **no restriction on P_S A_y for y outside Omega**. In particular it may have two nonzero coordinates when A_y also has coordinates outside S. This is exactly where the prior global weight≤2 argument no longer applies.

For a mixed pair x∈Omega,y∉Omega call it *constrained* if at least one of these holds:

1. x and y share a row or a column; or
2. for at least one a∈{2,3,4}, <B_a(x),B_a(y)>≠0.

Define the **exposed-ray set**

    E_S={ [A_x] : x in Omega and there is a constrained y outside Omega
                         with P_S A_y≠0 }.

The brackets denote projective rays in S, not a selected coordinate representative. All x,y,members and U are quantified; no numerical state, angle, boundary sample or finite probe is chosen.

## 3. Theorem — exact all-member move criterion

> **(A^U,B2,B3,B4) is an ACTUAL four-family if and only if U stabilizes EVERY ray in E_S.**

Here stabilization means U A_x belongs to the same ray as A_x for each exposed ray. It permits a phase on that ray; it is not a requirement that vectors be pointwise fixed.

### 3.1 Why an exposed ray imposes an eigenray condition

Fix a pair that witnesses exposure, and put u=A_x∈S and w=P_S A_y≠0. The original actual family gives <u,w>=0:

- in a common row/column this is A's own QLS orthogonality;
- otherwise a nonzero mate overlap, together with original pair-product orthogonality, forces the A overlap to vanish.

Since S has complex dimension2 and w is nonzero, its orthogonal complement inside S is exactly span{u}. Therefore

    <Uu,w>=0  iff  Uu belongs to span{u}.                 (EIG)

This is an exact two-dimensional linear-algebra implication, not a reality or sign argument. It does not assume that w is a coordinate vector.

### 3.2 Necessity, including the row/column caller

Suppose the updated tuple is actual. At a witnessing same-row/column pair, A^U must still be orthogonal. At any other witnessing pair, the unchanged nonzero mate overlap makes the updated A overlap zero. Thus <Uu,w>=0 in either case, and (EIG) says U stabilizes the exposed ray. This holds for EVERY witness and hence every ray of E_S.

### 3.3 Sufficiency, with all physical conditions checked

Suppose U stabilizes E_S. All vector norms are preserved. If both cells are in Omega, the same unitary acts on both and their A inner product is unchanged. If neither is in Omega, nothing changes.

For a mixed pair:

- If P_S A_y=0, the new A overlap is zero automatically.
- If the pair is constrained and the projection is nonzero, its active ray is exposed, so (EIG) makes the new overlap zero.
- If it is not constrained, the cells share no row/column and **all three** mate overlaps are zero; no A overlap is needed to make any of their pair products orthogonal.

Every row and column of A^U is therefore an orthonormal list of n unit vectors in dimension n, hence an ONB. Every A^U–B_a same-cell product list is pairwise orthogonal by the above cases. It contains n² unit vectors in dimension n², hence is an ONB. All other QLS and B_a–B_b conditions are unchanged. The tuple is actual. This proves the full converse rather than just a necessary graph constraint. ∎

## 4. Rigidity obstruction — nonorthogonal exposed rays freeze the move

> If E_S contains TWO distinct, nonorthogonal rays, every admissible U is scalar on S. Consequently it cannot turn any active full-two-coordinate entry into a one-coordinate entry.

**Proof.** Let unit representatives u,v of those distinct rays satisfy <u,v>≠0. The theorem gives Uu=alpha u,Uv=beta v with |alpha|=|beta|=1. Unitarity gives

    <u,v>=<Uu,Uv>=conj(alpha) beta <u,v>.

The nonzero overlap implies alpha=beta. Distinct rays in dimension2 span S, so U=alpha I_S. Scalar multiplication preserves both nonzero coordinates of every active entry. This rules out a support-shrinking move, without selecting any physical input numerically. ∎

This is a coupling obstruction caused jointly by A's row/column boundary and **ALL three actual mate Gram relations**. An isolated-square operation, an abstract net or only the mate with the most convenient zero pattern does not determine E_S and cannot justify the update.

### Complete stabilization alternatives

A nonscalar unitary can stabilize only its two orthogonal eigendirections. Conversely, if E_S is contained in some pair of orthogonal rays L,L-perp, every

    U=alpha P_L+beta P_(L-perp),   |alpha|=|beta|=1,

stabilizes it; nonscalar choices have alpha≠beta. If E_S is empty, all unitaries are admissible. If it has exactly one ray, that ray and its orthogonal complement give the same diagonal description.

Thus a nonscalar **linear operator** is available precisely when the exposed rays fit inside at most two orthogonal rays. This is not automatically a projectively nontrivial change of A: all active entries might themselves lie in those eigendirections. No new nonclassical family is asserted from operator nonscalarity alone.

## 5. Complete criterion for collapsing an active entry

Let z∈Omega be arbitrary and k∈{p,q}. The question is whether an admissible U can send A_z to the coordinate ray[e_k]. This is a source-prescribed all-variable operation question, not a selected test state.

1. **E_S empty.** Any unitary is allowed, and a unitary basis extension maps any unit A_z to e_k up to phase.
2. **E_S has distinct nonorthogonal rays.** Only scalar U is allowed; A_z has both coordinates nonzero, so collapse is impossible.
3. **E_S is nonempty and lies in orthogonal rays L,L-perp.** Fix ANY unit v∈L. Collapse is possible exactly when

       |<v,A_z>|=|<v,e_k>|.                              (C)

   This condition is phase-independent. Norm1 then gives the same equality of moduli on L-perp.

**Proof of case3.** Necessity follows because every allowed diagonal U preserves component moduli in L⊕L-perp. For sufficiency write A_z=a v+b w and e_k=c v+d w for a unit w∈L-perp. Under(C), |a|=|c| and |b|=|d|. Choose unit phases alpha,beta satisfying alpha a=c,beta b=d when these coefficients are nonzero; if a paired coefficient vanishes, its target counterpart also vanishes and that phase is free. The resulting diagonal U is unitary, stabilizes E_S, and maps A_z to e_k. These cases include zero components and need no division by zero. ∎

If E_S has just one ray, L is that ray; if it has two, they are orthogonal and either choice of L gives the same condition. No fixed numerical phase or parameter was evaluated.

## 6. Recovery of the prior low-weight lemma, and its exact missing extension

If A has all weights≤2, an inactive projection onto S is zero or one-coordinate. Every active A_x has both coordinates nonzero. Therefore a constrained mixed pair, whose original A overlap must be zero, cannot have a nonzero inactive projection. E_S is empty. The theorem allows every U, recovering the source's Lemma10 operation and the forward part of the first packet.

For arbitrary higher-weight entries, an inactive projection may instead lie on the nonzero ray orthogonal to A_x. The exact additional information needed is not “the row is unitary” or “the supports fit a budget”: it is the **actual exposed-ray geometry** from these mixed pairs, with every mate included. Two nonorthogonal exposures already prohibit the source's support-shrinking step.

This identifies a genuine failed implication in a proposed unrestricted classicalization argument:

    an allowed support pattern / low-weight-style move proposal
       does NOT by itself establish that the updated actual four-family exists;
    the correct iff condition is stabilization of E_S,
       with the scalar-rigidity obstruction above.

I do not claim that E_S must always contain two such rays in every nonclassical four-family, that it is always empty, or that every unrestricted member has a useful two-coordinate active set. Any such universal assertion would need another admitted proof.

## 7. Quantifier, degeneracy and assurance audit

- Original four members are arbitrary actual ordinary complex QLS, with any classical/nonclassical combination, n=8 included. Only the proposed local operation names a two-coordinate plane in one member; no global weight bound remains in this theorem.
- Omega empty makes E_S empty and A^U=A. The theorem then asserts no new family or nonclassicality.
- Repeated active rays give repeated witnesses, not extra independent eigenray conditions. Zero inactive projections impose no condition. Zero/nonzero mate overlaps are exact complex inner products, not approximations or support-only tests.
- Nonorthogonal exposed rays force the same eigenvalue, not contradictory entry phases. Two orthogonal exposed rays permit two eigenphases. These are distinct cases, all retained.
- Independent entry rephasings preserve exposure and every zero/nonzero test. Separate global output unitaries on the other members preserve their Gram relations; no common output frame is imposed. Changing A's frame changes which operation is being proposed, not the theorem's universally quantified validity for that frame.
- Sufficiency assumes an original ACTUAL family and a common U, not independently specified local rays or a family of different per-cell operators. It checks row, column, norm and all pair-product ONBs, including completeness.
- A successful update may be merely an isotopy and need not change classicality. No exact nonclassical four-family is constructed, no all-family classicality conclusion follows, and no numerical M(8)/maximum-three/A10/A11/native gate is changed.

This is an explicitly named elementary written proof: complex tensor inner products; orthogonal-complement dimension in a two-dimensional Hilbert space; norm preservation and the elementary spectral/eigenray facts for a unitary; ONB completeness by dimension. No machine identity or finite trial was performed. Historical novelty, stronger independence, formal/kernel, executable or publication assurance is not claimed.

The input cut remains S1/S2 and the admitted paper, not any old protected/held/candidate guide. The next admissible all-variable question is whether the exposure conditions can be forced from an unrestricted family's actual couplings, or whether a different admitted move is required. The missing universal exposure/continuation premise is OPEN, not paid by this local exact iff theorem. Main must review the entire proof and source boundary before adoption. Original STOP outside S1, scientific HOLDv2, N4 UNKNOWN/exit UNESTABLISHED, aux214 STOP and all findings/ZERO consumers persist.
