# CONFERENCE-GLUING v1 — an arbitrary-complex-phase local compatibility obstruction

Clock actually observed before creation: **2026-10-23T14:30:49-07:00**. PhysicsRQLS10, physics-5. This continues the *actual independent-phase gluing* obligation from `complex-lift-scope-v1.md` and checkpoint002. It does not enlarge a checker or an encoding.

**CANDIDATE WRITTEN PARTIAL.** Unlike the earlier real exclusion or the two-valued global-gauge exclusion, the theorem below retains **arbitrary complex diagonal compatibility phases** and **arbitrary relative core permutations**. It rules out a definite class of local three-basis configurations, including the direct conference-seeded prolongation route. The assumptions about the two conference-equivalence classes and zero-matching cycles are explicit. They are not assumed without loss for all 1-RQLS(10).

No scientific program, enumeration, numerical arithmetic, solver, formal kernel or outside-model CLI was used. Arithmetic reductions below are written algebraic identities, not an executed finite-field assay.

## 1. Three actual nine-dimensional bases at a single cell

Assume an H0 equality-route array: every required row/column/B-class pair has squared overlap0 and every line-disjoint pair has squared overlap1/8. Fix any cell p and its three incident lines L_A,L_B,L_D. Their common unit vector is q_p. Remove p. Each line's remaining nine vectors forms an ONB of `q_p^perp≅C^9`.

Any two of these nine-vector bases have exactly one orthogonal partner per vector, and all eight remaining squared overlaps equal1/8. Indeed the two corresponding cells, already on different lines through p, can additionally share at most their third coordinate class; that class meets the other line at a unique cell different from p. Thus each normalized transition is a complex conference matrix of order9 up to row/column permutation.

Label the A basis as e_i, i=1,...,9. Relabel B so its vector b_i is the unique one orthogonal to e_i; independently relabel D so d_i is the unique one orthogonal to e_i. There is then a permutation rho of [9] such that

    <b_i,d_(rho(i))>=0,                                    (Z)

and these are exactly the nine zeros of the B/D transition. Its cycle type is the invariant composition of the three zero matchings, up to simultaneous relabeling. No numerical closeness to a zero is involved.

## 2. The precise complex conference baseline, without a classification claim

Let F=GF(9), chi its quadratic character, and

    w=(1+i sqrt7)/sqrt8,
    C_ii=0,
    C_ij=w^chi(i-j)   for i≠j in F.

Et-Taoui [arXiv:1409.4282v1](https://arxiv.org/html/1409.4282v1), §2 Theorem2 and Corollary3, proves `CC*=8I`. The actual order9 example was read. The nine coordinates may be labeled by F in any bijection. C is symmetric. This is a baseline construction; **not every complex conference matrix of order9 is asserted equivalent to C**.

In this note monomial equivalence permits arbitrary row phases, column phases, row permutations and column permutations independently. They are not limited to finite phase alphabets or to the symmetric-equivalence operations used in the source.

### Hypothesis CC

Both A/B and A/D transitions, multiplied by sqrt8, are monomially equivalent to this C.

This is a concrete and natural conference-seeded route, but an explicit restriction. It makes no assumption that the B/D transition is equivalent to C; only its required zero matching (Z) is used.

## 3. Normal form keeps every independent diagonal phase

Under CC, allowed phases and relabelings of A and B put

    b_i = column_i(C)/sqrt8.

A still has the standard rays. The A/D transition retains its monomial class. After its zero diagonal is aligned as in §1, it has exactly the form

    [d_1 ... d_9] = D P C P^T E /sqrt8,                    (NF)

where P is an **arbitrary** permutation matrix, and D,E are **arbitrary** diagonal unitary matrices. To see why the two permutations are inverse: the zero pattern of `P C Q` is `J-PQ`, and a zero diagonal means PQ=I. All diagonal scalings can be absorbed into D,E without restricting their values.

Let delta_t=D_tt. Right-column phase E_(rho(i),rho(i)) is nonzero and cancels from each required zero (Z). Write `C'=PCP^T`. The nine zero conditions are exactly

    M delta=0,
    M_(i,t)=conjugate(C_(t,i)) C'_(t,rho(i)).                (M)

In particular delta can have arbitrary unit complex coordinates. We will prove that for certain rho this **linear** system has no nonzero complex solution at all. Reducing the fixed coefficient matrix does not reduce or discretize delta.

## 4. A fixed-prime reduction of M, uniform over all P

Put `s=i sqrt7`, so s²=-7 and

    w²=(-3+s)/4,       w^-2=(-3-s)/4.

Whenever M_(i,t) is nonzero it is one of `1,w²,w^-2`, independently of P: the two factors use exponents±1. It is zero precisely when `t=i` or `t=rho(i)`, with just one zero when rho(i)=i.

All coefficients lie in the ring

    R=Z[1/2,s] ⊂ C,       s²=-7.

There is a ring homomorphism

    phi:R→F7,       phi(s)=0,       phi(1/2)=4.

It is well-defined by the quadratic relation. Both w² and w^-2 map to `-3/4=1 mod7`. Therefore

    phi(M)=N_rho=J-I-P_rho+F_rho,                         (N)

where `(P_rho)_(i,t)=[t=rho(i)]` and `F_rho=diag([rho(i)=i])`.

This reduction is uniform over **every** relative permutation P and all phases D,E in (NF). P only changes which of 1,w²,w^-2 occurs; all three have the same reduction. If N_rho is invertible over F7, then det M has nonzero image under phi and is therefore nonzero in C. It follows that M delta=0 forces delta=0 for **all complex delta**, including phases transcendental over R. Thus the argument does not silently constrain compatibility phases to a number field.

## 5. Exact cycle criterion, and the resulting complex no-go

### Lemma N

If every cycle of rho has odd length and rho has at least one fixed point, then N_rho is invertible over F7.

**Proof.** Set

    A=I+P_rho-F_rho,       N_rho=J-A.

On a fixed point, A is the1×1 matrix1. On an odd cycle of length greater than1, A=I+P_cycle has determinant2 and is invertible over F7: -1 is not an eigenvalue of an odd-order permutation, or directly `det(I+P_cycle)=2` for odd cycle length. Thus A is invertible.

If f is the number of fixed points, `A^-1 1` equals1 on fixed points and1/2 on every other coordinate. Hence

    1^T A^-1 1 = f+(9-f)/2=(9+f)/2.

The rank-one determinant formula, valid over F7, now gives

    det(J-A)=det(-A)*(1-1^T A^-1 1)
            =det(A)*(7+f)/2
            =det(A)*f/2     in F7.

The only positive f≤9 divisible by7 is f=7; this is impossible when all cycles are odd, because the remaining two nonfixed points would have to form a2-cycle. Thus f is nonzero in F7. Since det A is nonzero, so is det N_rho. QED.

### Theorem CGLUE

Under CC, **no** local triple of actual conference-related nine-dimensional bases exists if its zero-matching permutation rho has only odd cycles and at least one fixed point.

**Proof.** Lemma N makes the fixed coefficient matrix M invertible by §4. But (NF) requires a nonzero unimodular delta satisfying M delta=0. Contradiction. QED.

The simplest and strongest-to-use case is

    rho=id_9.

Then `N_rho=J-I` and `det N_rho=8=1 mod7`. This rules out **all** relative core permutations P and all independent coordinate/entry phases—not only the direct two-value gauge excluded by W2.

For clarity about the boundary: if rho has an even cycle, an alternating vector on that cycle is in ker N_rho (its coordinate sum is zero). If rho is a derangement with only odd cycles, the determinant expression above is zero. These singular reductions are **inconclusive**, not compatible phase constructions and not evidence of feasibility.

## 6. A genuine complex construction route eliminated: diagonal prolongation

Let B have index set `{infinity} union F` and satisfy

    B(infinity,x)=B(x,infinity)=x,
    B(x,x)=infinity              for every finite x,
    B(infinity,infinity)=infinity.

Off-diagonal entries are any Latin completion; no affine symmetry, translation covariance or reality is assumed for the q vectors.

At p=(infinity,infinity), choose

- A: the finite cells `(infinity,x)` of its row;
- B: the finite cells `(x,infinity)` of its column;
- D: the finite diagonal cells `(x,x)` of its symbol-infinity class.

The A/B zeros are aligned by the common B-symbol x; A/D zeros by the common column x; B/D zeros by the common row x. Thus all three matchings align and `rho=id_9`.

### Corollary DP

No H0 equality-route lift for this B can have **both** of those local conference cores in the Et-Taoui monomial class CC, even with arbitrary complex compatibility phases, arbitrary relative core permutations, and completely unrestricted remaining cell vectors.

This includes the natural F9+infinity diagonal-prolongation seed, not merely the old AGL(1,9)-covariant ansatz. The old symmetry exclusions were about global representations; this conclusion assumes only the displayed Latin incidences, H0 and the two specific local conference classes. It is therefore a genuinely different route obstruction, but still not an H0-wide no-go.

The cyclic order10 resolution illustrates an important survivor. At p=(0,0), with the row/column/symbol zero matchings labeled as in §1, rho is inversion on the nine nonzero labels of Z10: one fixed point (5) and four2-cycles. It has even cycles, so the present criterion does **not** exclude it. No claim that every Latin square has an odd-cycle/fixed-point cell is made.

## 7. What changed, and the remaining actual obligation

The earlier W2 result only showed that independent compatibility phases could not all be removed into one nonreal two-value gauge. CGLUE now handles those **independent phases themselves**, not a gauge-fixed substitute, at a precisely identified local class and cycle condition. For the diagonal-prolongation conference seed, the local zero equations already contradict linear algebra before any full-grid completion or ray-distinctness issue arises.

Still open:

1. Local zero-matching types with an even cycle or an odd-cycle derangement, including the cyclic10 inversion type.
2. Conference cores not in the specified Et-Taoui monomial class; the source does not classify all order9 cores.
3. Nonuniform overlaps, hence the full maximal 1-RQLS(10) target.

The next bounded complex obligation is one of the genuine surviving local configurations, not a repeat of the excluded identity-matching seed. No scientific execution, enumeration of P, numerical search or old runtime is authorized by this manuscript. No new problem slot or solved-target count is created.

## 8. Review and import boundary

The only external construction premise is the explicit C9 from the actually read Et-Taoui §2 theorem; row/column ONBs and transversal incidence come from the unchanged Zhang–Cao definition. Linear algebra, the ring homomorphism and determinant identity are written out. No source classification, old float result, real-only integrality argument or unexecuted checker is a premise.

This complete candidate is pending actual separate reconstruction and parent review on pinned bytes. Correctness, source trust, scope, novelty and full-target significance remain separate. General finite-field and conference-matrix methods are prior art; novelty of this particular gluing restriction is **UNCERTIFIED**. No kernel/human/cross-vendor acceptance or target-level solution is asserted.
