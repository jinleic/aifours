# S1 addendum 2 — a total rectangular boundary invariant of every canonical derivation

**Owner:** MathSemigroup-2, math-4. **AUTHOR-WRITTEN / UNREVIEWED.** This additive packet uses the same S1 narrow release and the exact seven-source packet `5a671de2533ed5c1dd241695bde1cb03f2833f0467a67f0c7440b0f7f5eddf4e`, read completely as recorded in prerequisite-derivation-v1.md.

Last actual clock before writing: **Tue Oct 27 14:41:36 PDT 2026** (`/bin/date`). No scientific interpreter, calculator, program, enumeration or selected probe is used; every statement below is symbolic and universally quantified.

## 1. Exact claim and origin

Let S be any original nonempty finite/infinite source, with its **actual** pure onto syntactic completely-simple quotient q(s)=(i_s,g_s,lambda_s), C=M[G;I,Lambda;P]. Keep the full canonical B_q and all mixed relations from packet S3:138–159, and local V from S3:15–19.

The preceding packet refuted naive source-product evaluation on all placed words. Here is a different invariant that is **total**, even on incoherent words. It records the first placed origin/actor row and the last placed endpoint/actor column. It comes directly from the literal M multiplication: its first coordinate survives from the first factor, while its final group coordinate is the shifted second factor's endpoint.

This is not an interpretation from any old held representation/corner/homogeneity outline, a globalization, or a proof that arbitrary source idempotents are separated. It is a quotient of the already supplied presentation; no new actor or host equivalence is assumed. Same-author exposure and all exclusions remain disclosed. All three mandatory corrections are retained and none of their false clauses is used. Main's fresh six-body complete reads are not claimed.

**Theorem BOUNDARY.** There is an onto equivariant band homomorphism

F : B_q -> R,   R=(G x I) x (G x Lambda),

where R is rectangular, with

F([X_(u,s)])=((u,i_s),(u g_s,lambda_s)).                 (BND)

In particular, beta(s)=beta(t) implies q(s)=q(t), for **all** source s,t, not just idempotents. This is a total all-derivation actor-boundary invariant. It does not separate any pair already in one q-fibre.

## 2. The target is an actual V-band with actual G-action

Define multiplication on R by

((a,i),(b,lambda)) · ((c,j),(d,mu)) = ((a,i),(d,mu)).

It is associative, every element is idempotent, and each local corner rRr consists of r alone. Hence R lies in the original local-regular band variety V, without replacing V by global right regularity.

For k in G define

alpha_k((a,i),(b,lambda))=((k a,i),(k b,lambda)).

This preserves the displayed product and is invertible with inverse alpha_(k^-1). Also alpha_k alpha_l=alpha_(kl), with no commutativity of G assumed. Thus it is a genuine automorphism action on the whole band R.

All sets are nonempty because C is nonempty. No cardinality, FULL, complete regularity, selected quotient or common source identity is required.

## 3. Every relation, arbitrary substitution and every context

Assign each generator its BND value and extend multiplicatively to the free semigroup of nonempty words. The resulting value of an arbitrary word W=X_(u1,s1)...X_(un,sn), coherent or incoherent, is

F0(W)=((u1,i_(s1)),(u_n g_(sn),lambda_(sn))).             (WORD)

Check the entire generating list:

### 3.1 Mixed relations M

Let v=u w(s,t)=u g_s p_(lambda_s,i_t). Then

F0(X_(u,s)X_(v,t))
 =((u,i_s),(v g_t,lambda_t))
 =((u,i_s),(u g_s p_(lambda_s,i_t) g_t,lambda_t))
 =((u,i_(st)),(u g_(st),lambda_(st)))
 =F0(X_(u,st)).

This is every s,t,u, not an instance at an assumed idempotent or selected coordinate.

### 3.2 Associativity

WORD depends only on the first and last letters, not parentheses. Equivalently, R's product is associative. Every associativity application preserves F0.

### 3.3 Band idempotency, every nonempty substituted word

For any U, the first and last coordinates of UU are those of U, so F0(UU)=F0(U). This includes nonidempotent **source** products, the case that defeated the partial invariant. No source equality t²=t is inferred.

### 3.4 Local regular identity LOC, every nonempty word substitution

Both sides of the literal LOC equation begin and end with the same substituted E-word. Their F0 values therefore both equal F0(E). No source idempotency assumption on the E-block is needed here. Arbitrary repeated/coinciding substitutions are included.

### 3.5 Context, direction, transitivity and congruence closure

F0 is a homomorphism into an actual semigroup. Replacing equal-valued terms inside an arbitrary one-hole left/right word context preserves their values. Empty outer contexts mean omit those factors; no source identity is adjoined. All preceding equations are symmetric, so both replacement directions are covered. A chain of arbitrary substitutions/context replacements preserves F0 at every step, including chains that pass through incoherent words.

Thus every defining relation of B_q lies in ker(F0). The map factors to the asserted band homomorphism F. This pays every all-derivation case, not just coherent reductions.

## 4. Equivariance and surjectivity

For each generator,

F(alpha_k[X_(u,s)])=F([X_(ku,s)])
 =((k u,i_s),(k u g_s,lambda_s))
 =alpha_k F([X_(u,s)]).

The equality extends multiplicatively and through the congruence, giving equivariance.

For arbitrary ((u,i),(z,lambda)) in R, onto q supplies an s with q(s)=(i,u^-1 z,lambda). Then its letter X_(u,s) has exactly that BND value. Hence F is onto. No finite choice, enumeration or algorithmic source selection is involved; this is the direct onto-map existence implication for each arbitrary target element.

## 5. Consequences and distinctions

### 5.1 Every canonical generator equality already preserves q

At beta(s), BND gives

F(beta(s))=((1_G,i_s),(g_s,lambda_s)).

Equality beta(s)=beta(t) therefore gives equality of all three q-coordinates, hence q(s)=q(t). This holds for arbitrary s,t. Any alleged canonical collapse with different actors is impossible by this invariant.

### 5.2 Beta set-injectivity is equivalent to SEP, not a band embedding of S

At the existing U205/SEP cut:

- if beta is injective as a **set map**, SEP holds;
- if SEP holds and beta(s)=beta(t), §5.1 gives q(s)=q(t), so CAN(s)=CAN(t); the exact SEP-to-CAN injectivity proof (S3:175–183) gives s=t.

Thus SEP iff beta is set-injective; combined with U5, this is another equivalent formulation of the full original target. It is **not** proof of that injectivity.

Beta is not asserted to be an ordinary semigroup homomorphism S -> B_q. Its product formula is twisted by the actor weight. Therefore no claim that S embeds as a semigroup into a band follows.

### 5.3 Boundary retrieval is not a homomorphism into C

On R one can read a triple (i,a^-1 b,lambda) from ((a,i),(b,lambda)). This recovers q(s) on F(beta(s)), but this reading is **not** a general semigroup homomorphism R -> C. Products of rectangular elements omit the sandwich interaction except when their positions are compatible. In particular no nonidempotent actor is being asserted to be the homomorphic image of a band idempotent.

### 5.4 It preserves actor type even through the failed expansion

For v1's legal derivation from X_(u,sr) to X_(u,s)^2X_(u w(s,r),r), WORD keeps exactly the same first origin and last endpoint. Thus BOUNDARY retains q(sr) while the naive unplaced source product s²r has a different actor. The invariant is genuinely total on that failed relation, not a redefinition of the naive source product as if it had stayed valid.

### 5.5 Exact limit: the whole fibre is collapsed

For fixed c=(i,g,lambda), every s with q(s)=c has the same value

F(beta(s))=((1_G,i),(g,lambda)).

Thus F cannot separate **any** two elements of the same q-fibre, in particular the remaining R/L pairs. The theorem restores correct global boundary type; it does not restore the missing noncommutative source-idempotent label within that type. Neither its surjectivity nor its actual group action is a hidden universal-embedding conclusion.

## 6. Exact next prerequisite and assurance

A full invariant must refine one fixed boundary fibre while respecting all M/V substitutions, including the incoherent terms shown in v1. The total boundary theorem supplies the actor/position typing for such a refinement, not the source-separating refinement itself. A successful refinement must distinguish the same-q R-pairs and dual L-pairs; the original faithful-embedding/all-host alternative remains OPEN.

Only the explicitly supplied seven-source packet, S1 controls and ordinary equational reasoning were used. The six older source bodies are not edited; this is an additive candidate requiring full mathematics and dependency/application review. All STOP/HOLD/ZERO and process findings, N4 UNKNOWN/historical exit unestablished, auxiliary214 STOP, and no-execution/no-selected-probe/no-CLI/no-nested-agent limits remain. No independent-model/formal/kernel/executable/novelty acceptance is claimed. Deadline: 2026-10-31T21:23:27.000Z.
