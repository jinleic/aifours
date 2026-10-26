# A source-valid rewrite diagram obstructs uncontextualized all-load solving

MathSemigroup, math-4. Clock observed immediately before creation: **2026-10-23T15:56:30-0700**.

**CANDIDATE / PARTIAL / NOVELTY_UNCLEAR.** This resumes the SAME unmatched later-load coherence obligation after reading the operative parent disposition `semigroup-coherent-birth-parent-v1.md` in full. The accepted conditional forest/birth statements are unchanged. The result below is a concrete obstruction to upgrading them by solving every uncontextualized inverse-load system INSIDE the original S. It is **not** a counterexample to embedding. The distinction is demonstrated by an actual already-embedded source, not merely stipulated.

No scientific executable, enumeration, solver, compilation or new environment was used.

## 1. Exact source and original hypotheses

Let E={0,a,b} be the semilattice with 0 absorbing, a and b incomparable, and ab=ba=0. Let G={1,g}, g^2=1, and set

    S=E cross G, (e,h)(f,k)=(ef,hk),
    sigma(e,h)=h.

This is an inverse semigroup with idempotent band E cross{1}. The grading is onto and idempotent pure, hence S is E-unitary orthodox; every local idempotent band is a semilattice, in particular regular. It satisfies the exact book hypotheses and the stronger pure-orthodox diagnostic hypotheses.

It is already the allowed semidirect product E⋊G for the trivial action. Thus it is not, and cannot be presented here as, a nonembedding witness.

Use absolute-object-labelled letters

    U_c=X_(1,(c,g)) : 1→g,       c=0,a,b,
    Z_1=X_(1,(0,1)) : 1→1,
    Z_g=X_(g,(0,1)) : g→g.

Actual multiplication in S gives the typed composition relations

    Z_1 U_c = U_0 = U_c Z_g,
    Z_1 U_c Z_g=U_0.                             (M0)

Every occurrence of these relations below is an actual M_G step or two such steps. No relation equating a with b is imposed in the source.

## 2. An explicit finite path-origin derivation

Start at the path word U_0. Perform the following steps, indicating each genuinely new bridge origin according to the already frozen occurrence construction.

1. Expand by band idempotency:

       U_0 → U_0 U_0.

   The sole new between-copy gap has origin beta_0, with birth load (0,g).

2. In the FIRST U_0, use(M0) in reverse, then duplicate U_a:

       U_0 U_0
         → Z_1 U_a Z_g U_0
         → Z_1 U_a U_a Z_g U_0.

   This introduces beta_a between the two U_a copies. Its recorded uncontextualized birth load is (a,g).

3. Contract the typed pairs Z_1 U_a and U_a Z_g using(M0):

       Z_1 U_a U_a Z_g U_0 → U_0 U_0 U_0.

   The left gap is beta_a and the right gap is the transported beta_0.

4. Do the same to the LAST U_0 using b instead of a:

       U_0 U_0 U_0
         → U_0 U_0 Z_1 U_b Z_g
         → U_0 U_0 Z_1 U_b U_b Z_g
         → U_0 U_0 U_0 U_0.

   This introduces beta_b with birth load (b,g). The three gaps in the last displayed word have origins, from left to right,

       beta_a, beta_0, beta_b.

5. Put V=U_0 U_0, a RAW nonpath word, and apply the actual band identity V^2=V:

       U_0 U_0 U_0 U_0 = V V → V = U_0 U_0.

   The occurrence construction's copy-identification rule now **FORCES beta_a=beta_b**: they are the corresponding internal gap positions in the two copies of the SAME substituted word V. This is not an artificial endpoint-only identification. The between-copy target is beta_0; its recorded later load is the completion U_0 beta_a U_0.

6. Finally contract U_0^2→U_0. The remaining gap class receives the additional load (0,g).

All raw primitive steps are allowed by the canonical band congruence. M_G is used only on composable adjacent letters; arbitrary contexts may be nonpath, exactly as the presentation permits. The derivation starts and ends at the SAME typed path U_0, and its width is3. It contains the actual multiple-gap and changing-core-context interactions the original isolated lemma did not cover.

This is a genuine source-valid finite rewrite diagram. No claim that it collapses two distinct source elements is made.

## 3. Its uncontextualized inverse-load equations have NO solution in S

After final copy identifications, beta_a and beta_b are one class beta. Its grade is g, so any source assignment has the form

    beta=(c,g), c in E.

The TWO actual birth equations retained from steps2 and4 demand

    (a,g) beta (a,g)=(a,g),
    (b,g) beta (b,g)=(b,g).

They are exactly

    ac=a,   bc=b.                                (INV-fork)

No c in E satisfies both: c=0 fails both; c=a fails the b equation; c=b fails the a equation. This written three-element argument is not an enumeration run.

The other targets do not fix this contradiction. Beta_0's birth load is (0,g); its later load U_0 beta U_0 also evaluates to(0,g) for every grade-correct beta. Its inverse equations are automatic. The final load(0,g) for beta is automatic as well. The obstruction is precisely the genuinely forced reuse of beta at the two incompatible birth loads, not a directed-cycle counting artifact.

Consequently the following proposed universal upgrade is FALSE even for an explicitly embedded finite inverse source:

> For every finite path-origin canonical derivation, its frozen uncontextualized occurrence inverse-load equations admit a simultaneous assignment inside S.

The supported forest/birth criteria did not assert this, so no earlier accepted conditional result is withdrawn. Rather, this supplies an exact falsifier for that possible next step. **Failure of these equations is not nonembeddability**: the actual embedding of this S was displayed in §1, and the diagram's endpoint is unchanged.

A full proof must therefore either transform diagrams, weaken the unnecessary inverse equations in a source-valid way, or introduce an appropriately justified auxiliary construction. Merely requiring all old loads to share a source inner inverse cannot work in general.

## 4. Source-valid contextual load equations repair this diagram

There is a precise weakening that remains sufficient for the entire rewrite argument.

At a primitive nonloop idempotency step A U B ↔ A U U B, keep exactly the same occurrence-variable identifications for internal U copies and the same transported outer-boundary gaps. Write w for the completed U value, and beta for the between-copy bridge. Let ell include the completed left context and its boundary bridge, and let r include the right boundary bridge and completed right context. If a context is absent, its multiplication is simply omitted; formal units here are notation in S^1, not a new identity assumed to lie in S or an allowed unitization of the target band.

The two completed WHOLE-word values are

    ell w r,        ell w beta w r.

Thus the equation actually needed for this step is only

    ell w beta w r = ell w r.                    (CINV)

The earlier w beta w=w is a sufficient strengthening of(CINV), not a necessary requirement on a given contextual step. This distinction matters when later LR/idempotency identifications merge bridge classes.

Replacing each recorded raw inverse-load equation by its exact(CINV), while retaining all grade/copy constraints, gives the following source-valid conditional construction for arbitrary gap counts and contexts:

> Every simultaneous assignment satisfying the contextual equations validates all primitive steps and therefore preserves the original source values at path endpoints.

The proof is direct for idempotency by the displayed whole-word values. M_G and LR_P are unchanged from the already reconstructed completion argument; loop U gives w^2=w by purity. No natural-order compatibility or faithful functor is assumed. No universal solvability of(CINV) is claimed here.

### Exact repair of the control

In the diagram of §2, **every completed entire word evaluates to(0,g) for every grade-correct assignment**, even after the forced beta_a/b merge. Every raw stage contains an original zero-labelled letter, either U_0 or Z_1/Z_g. Multiplication in E has an absorbing zero, while the grade of the completed whole word telescopes from1 to g. Consequently all complete values are(0,g), independently of inserted bridge labels.

Hence all contextual equations(CINV) are simultaneously satisfied, for example by assigning every bridge the value(0,g). At the two births U_a→U_a^2 and U_b→U_b^2, the zero-bearing outer context absorbs exactly the defects that made(INV-fork) impossible. This is an actual source-valid repair of the concrete forced-reuse diagram, not an inference from a failed recipe to the original theorem.

## 5. Consequence for the SAME remaining construction

The single primary obligation is still canonical idempotent-fibre separation. This packet does not answer it. It establishes two concrete facts:

1. Universal solving of all uncontextualized later loads inside the original source is a dead route, already on the above valid finite diagram.
2. Exact contextual load equations are the appropriate weaker word-level requirements; they repair this first explicit forced-reuse obstruction without changing source hypotheses or claiming a nonembedding counterexample.

The consequential missing step is now a genuine **all-contextual-load solution or source-valid normalization**, not another common-inner-inverse recipe. One must either prove that every hypothetical distinct-idempotent collapse diagram admits an assignment/normalization that preserves its endpoints, or supply an actual valid semigroup with all required properties and a true separation obstruction. The failed(INV-fork) system supplies neither a distinct-endpoint collapse nor a negative embedding conclusion.

This remains the orthodox pure group-graded route. The nonorthodox Rees-typed extension and arbitrary infinite purity are not inferred. No theorem/discovery count or novelty promotion is made; this complete bounded construction/falsifier needs its own pinned reconstruction and parent composition. Original snapshots remain immutable and all writes stay in the owned root.
