# Exact all-inverse-section obstruction to the star-bandification route — POSITIVE original sources

Owner MathSemigroup-2. Actual preceding `/bin/date`: **Sun Oct 25 21:06:22 PDT 2026**. NEW AUTHOR-WRITTEN / UNREVIEWED successor to the complete204LF packet `semigroup-post-CG-star-bandification-and-inverse-reflection-v1.md`, SHA256 `97b04cbe9db35c26f68dcfc70fcb50296ca8b556c829a66428c2b98cfb7d6141`.

All calculations below are exact WRITTEN structural group/semigroup algebra. No scientific interpreter, calculator, program, CAS, generated table, enumeration, solver, replay, CLI, nested agent or GO. No frozen file is edited.

## 1. Exact target and what is closed by this note

The predecessor's Theorem D is an exact auxiliary criterion, not a full original embedding theorem. For the true one-sided map p:A->T and the faithful cocycle retaining star, it says:

`B_full is a BAND IFF K_tau=<t tau_t:t in T> is a band`,

where every tau_t is an ACTUAL inverse of t and all unshifted/transformed coefficients are retained.

The predecessor left open whether EVERY actual weakly E-unitary locally inverse T admits a section tau satisfying that condition. This NEW note answers that question **NEGATIVELY**, even for an explicit finite locally inverse T at its ACTUAL least pure-CS quotient. It then propagates the obstruction to an actual one-sided source with NONTRIVIAL least-LI L-kernel.

These are POSITIVE original-class sources with explicit allowed Pastijn embeddings. Thus the conclusion is ONLY: changing the inverse-section choices cannot repair THIS entire star-retaining source-valued coefficient representation. It is NOT a book-class nonembedding certificate, not a solution of the original problem, not a scope reduction, and not a repair of CG/RU-LU. It replaces the failed section-choice approach with an exact closed route barrier; the original faithful W_L/W_R completion remains.

## 2. A locally inverse source with a pure completely-simple grading

Let G={1,g}, g^2=1, g!=1. Define the completely simple semigroup

`C=M[G;{0,1},{0,1};P]`,

`p00=p01=p10=1`, `p11=g`.

Its idempotent at row i,column lambda is `(i,p_(lambda,i)^(-1),lambda)`.

Let Y={y,z,0} be the meet semilattice with y,z incomparable and y meet z=0. The WHOLE product P(Y,C), with TRIVIAL G action, is just Y cross C. Its normal semilattice base is allowed and its actual local monoids are inverse (semilattice corners times a group).

Inside it define

`T0 = ({0} cross C)`

`   union { (y,(0,h,0)) : h in G }`

`   union { (z,(0,h,1)) : h in G }`.                       (T0)

The two upper pieces are actual groups H00 and H01, since their sandwich entries p00 and p10 are1. Their cross products, and every product with a lower element, lie in {0} cross C. Thus T0 is closed and associative by the displayed ambient product. Each upper element has its group inverse in the same upper piece; every lower element has a Rees inverse in the lower C. Hence T0 is REGULAR.

All its idempotent corners can also be checked directly:

- at `e_y=(y,(0,1,0))`, the corner is `{y,0} cross H00`, a two-level semilattice times the group;
- at `e_z=(z,(0,1,1))`, the corner is `{z,0} cross H01`;
- at a lower idempotent `(0,e_(i,lambda))`, the corner is `{0} cross H_(i,lambda)`.

These are all inverse monoids. Therefore T0 is LOCALLY INVERSE and in the exact original locally r-orthodox class.

The ACTUAL second-coordinate map

`q0:T0->C`, `(d,c)->c`,

is onto through the lower piece and is idempotent-pure: (d,c) is idempotent exactly when c is idempotent. This also proves weak E-unitarity in the regular natural-order reading: a homomorphism preserves that order, C has the equality natural order, and an element above an idempotent has an idempotent C-image, hence is idempotent by purity. The source has the literal positive original embedding T0 included in P(Y,C).

## 3. q0 is the ACTUAL least-CS quotient, not a coarser convenience grading

Write `e_y^0=(0,(0,1,0))`, `e_z^0=(0,(0,1,1))` for the lower group identities corresponding to the two upper ones. In T0,

`e_y^0 e_y=e_y e_y^0=e_y^0`,

and dually for z. Thus e_y^0<=e_y and e_z^0<=e_z in the natural order. Every homomorphism into a completely simple semigroup identifies these respective pairs, because the CS natural order is equality.

For upper t=(y,c), with c in H00, multiplication e_y^0 t gives (0,c), while e_y t=t. Therefore ANY CS homomorphism identifies t and (0,c). The same argument works at the z group. Every upper element is consequently identified with its lower element of the SAME actual C-value.

The restriction to the lower piece is a homomorphism on its copy of C. Hence every CS homomorphism factors through q0. Since q0 itself is an onto CS homomorphism distinguishing all lower C-values, its kernel is the least completely-simple congruence. It is pure as already proved. The least-LI reflection of T0 is T0 itself because T0 is locally inverse.

No claim of actual least-quotient status is inferred from a chosen nonpure coarsening or from a finite producer; the entire written proof is above.

## 4. EVERY inverse section fails the band criterion

Choose ARBITRARILY tau_t in V_(T0)(t) for ALL t. No assumption about source inverses, a classwise transversal or coherence is imposed. Put h_t=t tau_t.

First, an inverse of e_y MUST have semilattice coordinate y: otherwise the y-coordinate of e_y tau e_y would be0 instead of y. Within the upper y group, the inverse of its identity e_y is e_y itself. Therefore

`h_(e_y)=e_y`.

Exactly the same argument gives h_(e_z)=e_z. These TWO range idempotents are forced in EVERY section.

Now take the fixed lower element

`t_*=(0,(1,1,0))`.

Its range h_*=t_* tau_(t_*) lies in the lower piece, has row1, and is idempotent. There are exactly TWO possibilities, according to its actual column:

`f0=(0,(1,1,0))`, OR `f1=(0,(1,g,1))`.                     (R)

This is simply the Rees idempotent formula for the two columns, not an enumeration of source tables/sections.

- If h_*=f0, then K_tau contains

  `f0 e_z=(0,(1,1,1))`.

  Its square is `(0,(1,g,1))`, different because p11=g and g!=1. Thus K_tau contains a nonidempotent.

- If h_*=f1, then K_tau contains

  `f1 e_y=(0,(1,g,0))`.

  Its square is `(0,(1,1,0))`, again different. Thus K_tau contains a nonidempotent.

Both alternatives in(R) fail. **For EVERY possible inverse section, K_tau is NOT a band.** The predecessor's exact Theorem D therefore proves: for p=identity on T0, the entire star-retaining B_full is nonband for EVERY source-section/inverse choice. This is stronger than the earlier single-CS bad-choice control; it rules out all coherent-section choices for an actual weakly E-unitary locally inverse source with its actual least pure-CS quotient.

## 5. The same failure persists with an ACTUAL nontrivial one-sided least-LI kernel

The p=identity example is not an inadmissible source, but it does not need star for source separation. To show that the barrier is not an artefact of choosing only an already-injective quotient, use the supported positive E5 from old Part3 Section27:

- upper U={u0,u1} is RIGHT zero;
- lower {a,b,c} is LEFT zero and lower-first products retain that lower element;
- u0 a=c, u1 a=b, and both upper maps fix b,c.

Its upper corners are {u_i,b,c}, identity over a left-zero pair; lower corners singleton. It belongs to W_L. Its ACTUAL least-LI quotient identifies b with c and nothing else. Call this quotient Q, with upper u0,u1 and lower {a,k}; both upper maps send a to k and fix k. Its upper corners are two-element semilattices, lower corners singleton, so Q is locally inverse. The kernel is contained in L.

Set

`A=E5 cross T0`, `p=p_E5 cross identity:A->Q cross T0`.

A is regular and locally LEFT regular: its idempotent local corners are a left-regular E5 corner times a semilattice idempotent corner of T0. It is the ACTUAL R-side source, not a later R-quotient: every local idempotent band already has trivial Green R, so the local-R generating congruence rho_R is equality.

The ACTUAL least-LI congruence of A is exactly ker p. To prove it, Q cross T0 is locally inverse, so theta_A is contained in ker p. Conversely, for ANY t in T0 choose a source inverse t' and e=tt'. The two idempotents (b,e),(c,e) lie in the actual corner (u0,e)A(u0,e) and are its forced local commutator pair. Right multiplication by (u0,t) gives

`(b,e)(u0,t)=(b,t)`, `(c,e)(u0,t)=(c,t)`.

Thus theta_A identifies every pair in ker p; no other E5 pair is in that kernel. Hence theta_A=ker p. It is nontrivial and contained in L_A; for the latter, (b,t) and (c,t) have the explicit left multipliers (b,tt') and (c,tt').

The ACTUAL supplied grading may be

`q_A:E5 cross T0 -> C`, `q_A(x,t)=q0(t)`.

It is onto and pure (the E5 coordinate is always idempotent), and factors through p with an onto pure map Q cross T0->C. This is the same admitted positive-source setup as the faithful auxiliary cocycle. No claim that this product grading is its least-CS quotient is needed for the route obstruction, and none is made.

The source has an explicit original POSITIVE host:

`(x,(d,c)) -> ((x,d),c) in P(E5 cross Y,C)`,

with trivial G action. E5 cross Y is in W_L and V, and the map is injective and multiplicative by the displayed products. Thus this source also cannot be an original nonembedding witness.

Nevertheless EVERY inverse section on the ACTUAL T=Q cross T0 fails the band criterion. Fix any idempotent q in Q. The range idempotents chosen for (q,e_y),(q,e_z),(q,t_*) project to e_y,e_z and one of f0,f1 in T0, because projection preserves mutual inverses. If their generated semigroup in Q cross T0 were a band, its T0-image would be a band containing those forced elements. Section4 gives the same nonidempotent product in either case, contradiction.

Therefore the predecessor's Theorem D shows **B_full is nonband for EVERY inverse/representative choice even for an ACTUAL one-sided source with NONTRIVIAL least-LI L-kernel and a positive allowed host.** This closes the attempted 'choose a better section' route at the original hypotheses rather than imposing a narrowed source class.

## 6. Relation to other claims and the full remaining construction

This is a later new negative route theorem, NOT a correction to Theorem D: the iff criterion remains exactly true. It closes the existential section question left open in its Section7 by a positive actual countercontrol. Completely simple target T alone still admits the good section displayed in its Section4, and inverse T still gives the semilattice of range idempotents. Those proper controls do not cover all locally inverse T.

The predecessor's Theorem I (the ORIGINAL inverse-reflection case via supported LG) is separate and unreviewed; the T in Section5 is locally inverse but not inverse, so no conflict or verdict transfer occurs. Full CG/RU-LU and the Part7 proof remain withdrawn. The general gauge lemma remains separately pending. No old packet is amended or this later theorem retroactively inserted into a live review.

A faithful original W_L/W_R host must therefore use a different coefficient/globalization construction, not merely replace the r_t' in the whole source-valued star cocycle. The actual normal-indexed row atoms, all(M), nonloop squares, loaded/multiple-gap returns, shared lower rows and source-idempotent separation remain the literal full gap. A different representation is required; this note supplies neither its band completion nor an original obstruction to every allowed base. The separate arbitrary-infinite pure-CS existence prerequisite is unchanged.

## 7. Assurance

All new products, inverse quantifiers, natural-order/least-quotient reasoning, local corners and full source/host maps are WRITTEN. Ordinary inputs are Rees multiplication, finite group/semilattice identities and the supported local-R/least-LI setup; no unsupported right compatibility of R appears. There is no generated checker, arithmetic kernel, table search or replay. This is not executable/triple-finite, formal/kernel, configured-family/human, novelty/priority or parent acceptance.

The complete structural definition, not just a table identifier, is supplied. Source fibres/units remain precise (M1); no common source identity or nonpure grading is invented. All parent/reviewer/owner process findings and LI2003 original-proof NOT_RECONSTRUCTED boundary remain, as do HOLD, the original eighteen owners, cutoff and deadline. The original unrestricted embedding/obstruction acceptance remains UNMET.
