# A physical-coordinate Hermitian dual for the RT equal-norm obstruction

**PhysicsRQLS10 / physics-5.** Actual pre-write `/bin/date`: **Sun Oct 25 04:30:49 PDT 2026**. **Level: WRITTEN, symbolic mathematical derivation only; not independently reconstructed or formally verified.** This is the return to the primary problem after completing the single assigned v30-F review. No scientific arithmetic program, eval, enumeration, certificate replay or solver is used. HOLD v2 and parent erratum v7 remain binding.

## 1. Materially different representation

The current RT+ candidate describes a two-dimensional right kernel and coefficient forms for its nine coordinate norms. This note instead gives a **physical-coordinate Hermitian row-space identity**:

    diagonal(lambda) = M* Z + Z* M,   sum(lambda) != 0.       (D)

It acts directly on all nine physical coordinates and supplies a closed-form lift from any kernel norm identity. It does not require a chosen free-coordinate parameterization to state or inspect the final certificate. The star/matching imports and earlier candidate outputs are not rechecked or promoted.

Identity(D), if established for the literal M, immediately excludes a coordinate-unit vector delta in its right kernel:

    delta* diagonal(lambda) delta
      = (M delta)* Z delta + delta* Z* (M delta) = 0,

whereas unit coordinate moduli make the left side sum(lambda), nonzero. This is an identity over the complex numbers, with no reality, phase-alphabet or projective-K restriction on delta.

The representation change is substantive but does not itself supply literal separators for every source core. The complete closed-form equivalence below is the delivered written result; its family application boundary is explicit in Section5.

## 2. Exact setting and theorem

Let K=Q(s) with s=i sqrt(7), under its usual embedding in C and conjugation s->−s. Let M in K^(m by n) have rank r, with 0<r<n, and let V in K^(n by k), k=n−r, be any basis of its full right kernel. A star denotes conjugate transpose.

The following are equivalent:

**(A) Affine norm inconsistency.** There is no Hermitian complex k-by-k matrix X satisfying

    diagonal(V X V*) = 1_n.

**(B) Rational diagonal annihilator.** There exists lambda in Q^n such that, with Lambda=diagonal(lambda),

    V* Lambda V=0,   trace(Lambda)=sum(lambda)!=0.

Lambda may be multiplied by a positive integer to make all its entries integers.

**(C) Physical row-space dual.** There exist such a rational diagonal Lambda and Z in K^(m by n) with

    Lambda=M* Z+Z* M,   trace(Lambda)!=0.

Every one of these equivalent conditions excludes the full coordinate-unit torus from ker_C M. They are stronger than merely excluding rank-one physical lifts: they exclude the entire affine Hermitian equal-norm system. This is not asserted to be a complete criterion for torus emptiness when that affine system IS consistent.

## 3. Full written proof of the equivalence

### 3.1 (A) if and only if (B): rational linear separation, without inequalities

Write the real coordinates of a Hermitian X using rational diagonal coordinates and, for each upper off-diagonal entry, `a+b*s` with a,b real. Because V has entries in K, the real-linear map `X -> diagonal(VXV*)` has a coefficient matrix F over Q. The target vector 1_n is rational.

A rational linear system `F x=1_n` is inconsistent over R exactly when some rational linear combination of its equations has zero coefficient row and nonzero target. This follows by ordinary symbolic row reduction over Q: an inconsistent reduced equation has form `0=c` for nonzero rational c, and its row operations supply the rational combination. Conversely such a combination forbids a solution. No numerical or positivity separation theorem is needed.

Thus inconsistency is equivalent to a rational lambda satisfying

    lambda^T F=0,   lambda^T 1_n!=0.

The first identity says `trace(V*Lambda V X)=0` for EVERY Hermitian X. The Hermitian trace pairing is nondegenerate: testing diagonal matrix units, symmetric off-diagonal units and imaginary skew off-diagonal units forces every entry of the Hermitian matrix V*Lambda V to vanish. Hence this is exactly(B). Clearing the finitely many rational denominators preserves both identities and gives integral lambda.

### 3.2 Full row-rank compression and orthogonal projectors

Choose any r independent rows of M, with row-selector S, and set

    A=S M in K^(r by n),
    G=A A* in K^(r by r),
    P=A* G^(-1) A,   Q=I_n-P.

A has full row rank over C, so for nonzero u,

    u* G u = (A* u)* (A* u) > 0.

Therefore G is invertible. Its inverse has entries in K by the adjugate formula. Direct multiplication gives P*=P and P²=P. Its image is the row space of A, and Q is the Hermitian projection onto ker A. Since the selected rows span the row space of M, ker A=ker M; no complex kernel directions are lost by this compression.

In particular, Q can also be written

    Q=V (V*V)^(-1) V*.

The same positive-definiteness argument makes V*V invertible. Consequently

    V*Lambda V=0  if and only if  Q Lambda Q=0.              (K)

The forward direction follows by substituting the displayed formula for Q. The reverse direction follows because QV=V and V*Q=V*.

### 3.3 Closed-form lift from(B) to(C)

Define the r-by-n matrix

    Y=G^(-1) A Lambda (I_n-P/2).

Its entries lie in K. Since Lambda and P are Hermitian,

    A*Y + Y*A
      = P Lambda (I_n-P/2) + (I_n-P/2) Lambda P
      = P Lambda + Lambda P - P Lambda P
      = Lambda - Q Lambda Q.

Under(B), identity(K) makes the final term Q Lambda Q zero. Therefore `A*Y+Y*A=Lambda`. Set

    Z=S*Y in K^(m by n).

Using A=S M gives

    M*Z+Z*M = A*Y+Y*A = Lambda,

which is(C), with the same nonzero trace. This is a closed expression, not an instruction to run an inverse calculation or a hidden numerical feasibility step.

### 3.4 (C) implies(B), and the torus consequence

Since MV=0, multiplying(C) by V* on the left and V on the right gives V*Lambda V=0. The trace condition is unchanged. This proves(C)->(B).

Finally, for any complex delta in ker M, identity(D) gives `sum_i lambda_i |delta_i|²=0`. If every coordinate modulus is one, this contradicts the nonzero trace. Thus(A), (B) and(C) all imply the claimed torus obstruction. The complete proof is symbolic and applies to every M satisfying the stated finite-dimensional hypotheses.

## 4. Why this representation helps the actual convention boundary

For the frozen RQLS necessary equation, the physical row is i, the phase-coordinate column is t, and `(M delta)_i=sum_t M_it delta_t`. In(D), Lambda acts on the **phase-coordinate column space**. Z has the same rectangular shape as M, and both products M*Z and Z*M act on that same physical phase space. The dimensions therefore expose an accidental transpose before any numerical or finite-field computation is contemplated.

The certificate is independent of a chosen kernel basis: replacing V by V T with T invertible transforms V*Lambda V by congruence and preserves its zero value. Changing which independent rows form A changes the lift Z but not the diagonal annihilator or the right-kernel assertion.

For the candidate's nine-by-four norm coefficient matrix F, the target remains the COLUMN 1_9. The separating condition is `F^T lambda=0`, `lambda^T1_9!=0`. Appending a row of four ones is not this separation problem. This is a written interface clarification, not a replay of any withdrawn parent checker.

## 5. Application boundary and current park

The earlier RT+ candidate asserts integral diagonal annihilators for its entire rank-seven residual family. **IF** those literal annihilator identities are reconstructed correctly, the theorem above converts EACH one into a physical operator identity(D), with no additional existential assumption. Conversely, a directly established(D) would reconstruct that core's affine norm obstruction without needing its previously chosen kernel basis.

This supplies a new proof representation for a future written reconstruction: direct literal M and a rational Hermitian row-space dual, rather than another phase/case enumeration. It does NOT manufacture a uniform lambda from the core geometry, verify any of the frozen finite tables, or replace the outstanding all-input completeness gate. No literal Z for an unreviewed source core is claimed to have been constructed here.

A useful remaining mathematical gap is now sharply separated: obtain diagonal annihilators or direct identities(D) from literal source structure uniformly, without treating the unadmitted finite outputs as established premises. The algebraic lift itself has no remaining gap in this written derivation. Independent reconstruction of this generic theorem, of the earlier RT+ data, and of the conditional all-P composition remains outstanding.

All older source/certificate files remain immutable. Parent erratum v7 continues to qualify the actual earlier computations; this written note grants no executable-verification or retroactive-admission credit. No all-P orientation acceptance, unrestricted maximal1-RQLS10 solution, novelty, formal or cross-vendor claim follows.
