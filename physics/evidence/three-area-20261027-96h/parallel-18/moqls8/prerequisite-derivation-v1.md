# physics-4 prerequisite — literal source check and the exact common-mate lifting obstruction

Actual native clock immediately before this first substantive packet: **Tue Oct 27 14:48:46 PDT 2026**.
Owner **PhysicsMOQLS8-2**, same physics-4 slot. **WRITTEN / UNREVIEWED** at explicitly named elementary complex-Hilbert-space facts. No scientific interpreter, numerical example, selected parameter/control, solver, replay, nested agent or model CLI.

## 1. Admissible input and source coverage

The19LF S1 controls were read FIRST, then the complete release,35LF packet and equality receipt. The pre-paper-body exposure ACK is `prerequisite-exposure-ack-v1.json`, SHA256 `15b048ae4a84c28b43b71b71561a004489106fcf96b6fc047f9dc7c0d352447c`,49LF/5183B, actual prewrite14:41:49/postpin14:42:33. Prior MOQLS authorship/review/public-source briefings and all held/ZERO exposures remain disclosed; this is not a blindness or clean-cognition certificate.

S2 expressly admits [Ball–Simoens, *Large sets of mutually orthogonal quantum Latin squares*, arXiv:2607.12933v2](https://arxiv.org/html/2607.12933v2). I actually read its complete returned reader body: initially displayed1–300 of486 reader lines, then the explicitly spilled `artifact://41291` at301–520 through the actual ending. No bibliography link or old proof was opened. The header says v2,27Jul2026. Main's retained raw-HTTP pin is `f2ef2a3f2493585ce22e022eca571f9c5e2268fd166f6599f3820afdf1b6d5ad`,274893B. Reader text is a rendered extraction, not a claimed byte-identical raw-HTML transcript or book-edition certification.

Only S0/current contract/own envelope/safe final status, this released paper/definition packet and elementary facts below are correctness inputs. No old F9, affine/q2/q3/gluing body, candidate graph, protected L_A/L_B/L_C, I_EW38/I_EWcompletion, old unwritten request, commutant shortcut or ZERO consumer is used. Old accepted statuses are not substituted for a missing operative proof.

## 2. Literal definitions and exact prior-claim check

The following quotations preserve the paper's wording, with its mathematical notation typeset normally rather than the reader's duplicated MathML/TeX text. Section labels refer to the admitted v2, not an unverified book definition.

### §2.2 — QLS and memberwise classicality

> “A *quantum Latin square of order* n is an n×n matrix over C^n such that each row and each column forms an orthonormal basis of C^n.”

It defines isotopy of an individual square by:

> “(i) multiplying each entry by a phase factor,
> (ii) permuting rows and columns, and
> (iii) applying a unitary transformation on all entries.”

> “A quantum Latin square is *classical* or *not genuinely quantum* if, up to isotopy, all entries are contained in {|1>,…,|n>}, a fixed orthonormal basis.”

The paper then says this is independent of the chosen basis by item(iii). It does not introduce a separate “apparently-quantum” predicate in these definitions; its actual distinction is classical/not genuinely quantum versus non-classical.

### §2.3 — orthogonality and family isotopy

> “Two quantum Latin squares (psi_ij) and (phi_ij) are *orthogonal* if {psi_ij tensor phi_ij : i,j in {1,…,n}} is an orthonormal basis of C^n tensor C^n.”

> “A set of t mutually orthogonal quantum Latin squares of order n, denoted t MOQLS(n), is a set of t quantum Latin squares of order n such that any two of them are orthogonal.”

Family isotopy allows entry phases, row/column permutations **simultaneously among all squares**, and:

> “(iii) applying, separately to each square, a unitary transformation to all of its entries.”

The family is classical/not genuinely quantum if, up to that isotopy, all entries are in the fixed ONB. In particular separate member frames are allowed. Individual classicality of every member implies family classicality under this definition: use each member's own unitary and entry phases, and leave the common row/column permutations as the identity. The reverse implication is immediate. No common output unitary is inferred.

### §1 — meaning of the cardinality question

Problem1 is verbatim:

> “Given n≥2, what is the largest value of t such that t MOQLS(n) exist?”

The following paragraph defines M(n) as the largest t for which a **non-classical set** exists, and M(n)=0 if none exists. That is a source definition, not a numerical value asserted by this packet.

Theorem5 is verbatim:

> “Suppose n≥3. A set of n−2 MOQLS(n) is classical. Thus, M(n)≤n−3.”

### §5 — Problem16 and order8/four-family status

Problem16 is verbatim:

> “Is a set of n−3 MOQLS(n), n≠4, necessarily classical?”

At the literal target n=8 this asks about FIVE members, not four. Theorem5 concerns SIX at that order. The printed Table2 has the order8 entry “2-5”. The paper's construction statements Theorem6/Corollary7 are sufficient restricted constructions, not an asserted unrestricted four-family exclusion or an explicit order8 nonclassical four-family witness.

**PRIOR-CLAIM decision, bounded to this complete v2:** the proposed unrestricted four-family alternative is **not stated as settled in this paper**. Neither the displayed general classicality theorem nor Problem16 is a four-family theorem at order8; the table does not resolve it either. This is not a current-world novelty/open-status certificate and not a claim that the broader literature has no solution. I do not reprove the paper's already stated six-family theorem or import the old five-family proof as new progress.

The Main-bound proposed successor therefore has an exact source-compatible predicate: for every actual ordinary complex four-tuple satisfying all row/column and pair-product ONB conditions, either all members are classical in the above sense, or an exact tuple with at least one nonclassical member is exhibited. Every mixed classical/nonclassical combination remains included. The old adopted five-family result is not re-adjudicated here.

## 3. A source-local obstruction to reversing classicalization

The paper's §3 Lemma10 states, verbatim:

> “If Psi is a quantum Latin square without entries of weight three or more, then there exists a classical quantum Latin square Psi' such that whenever Psi and Phi are orthogonal, Psi' and Phi are orthogonal as well.”

Its proof applies a unitary to **all entries with one particular two-coordinate support**, leaving other entries unchanged, then repeats. This is generally **not** a global isotopy of the original square. It proves a forward inclusion of common-mate sets, not the reverse lifting of arbitrary mates of the classicalized square.

Below I isolate the exact missing reverse implication and prove a localized, all-member lifting criterion for that operation. This is a conditional coupling/transfer candidate, not an assertion that every unrestricted four-family admits that classicalization. The transfer is stronger than merely listing an encoding: it identifies exactly which newly created orthogonal pairs require simultaneous compensating zeros from **every actual mate**, and classifies those pairs for the source's operation.

## 4. Notation, quantifiers and ordinary imports

Let n≥2 and X={1,…,n}² be the actual common cell set. For any array A of unit vectors write

    Z(A)={ {x,y}: x,y in X, x≠y, <A_x,A_y>=0 }.

Pairs here are unordered because zero inner product is symmetric; the underlying vectors and every nonzero overlap remain complex. No phase is set to a preferred value.
For two QLS A,B, their n² product vectors have norm1 in dimension n². Thus their being an ONB is equivalent to pairwise orthogonality:

    for every x≠y,  <A_x,A_y><B_x,B_y>=0.                 (O)

Equivalently every cell pair is in Z(A) or Z(B). This elementary identity will be used to prove the transfer, not advertised by itself as scientific progress.

Named ordinary imports: the complex Hilbert tensor-product inner-product identity; norm preservation by a unitary; coordinate orthogonal projection; and the finite-dimensional fact that n² mutually orthogonal unit vectors in dimension n² form an ONB. No classification, catalogue, finite field, computational witness, old local-span theorem or nonordinary mathematical import is used.

## 5. Single-operation theorem — exact created-pair classification and simultaneous lift

**Hypotheses.** A is an ACTUAL QLS(n), in an arbitrary fixed ONB for this member only, with every entry of weight at most2 in that frame. Choose two distinct coordinate indices p,q, let S=span{e_p,e_q}, and

    Omega={x in X: support(A_x)={p,q}}.

Let U be ANY unitary on S, extended by the identity on S-perp. Define the source's entrywise operation

    A'_x=U A_x if x in Omega;   A'_x=A_x otherwise.       (T)

U and all entries remain universally quantified; no numerical vector, angle or tested configuration is chosen. Collapse of some active entry to one coordinate is optional for this theorem; it is what the source chooses when reducing weight.

### 5.1 Forward actual-object implication

A' is an ACTUAL QLS and Z(A)⊆Z(A').

**Proof.** If both cells lie in Omega their inner product is unchanged by applying the same unitary. If neither lies there it is unchanged as well. If x∈Omega,y∉Omega, then P_S A_y is either0 or supported on exactly ONE of e_p,e_q: two nonzero coordinates there would, under the global weight≤2 hypothesis, put y in Omega.
Since A_x has both coordinates nonzero, <A_x,A_y>=0 in this mixed case forces P_S A_y=0. That also makes <U A_x,A_y>=0. Thus every original orthogonal pair stays orthogonal. All vector norms are preserved; in particular each original row and column is still an orthonormal set of n unit vectors in dimension n and is an ONB. This proves A' is QLS, not just a unitary pattern. ∎

Consequently if (A,B2,B3,B4) is an actual four-family, then (A',B2,B3,B4) is an actual four-family: an already zero first factor stays zero, and an already zero mate factor is untouched. Pair-product completeness follows from (O), while all other three pairs and row/column ONBs are unchanged. The same proof works for any number of actual mates.

### 5.2 Exact created-pair set

Define

    E=Z(A') minus Z(A).

Every pair in E has exactly one active endpoint. More precisely, up to exchanging its endpoints,

    x in Omega, y notin Omega,
    P_S A_y=alpha e_k with alpha≠0 and k in {p,q},
    <e_k,U A_x>=0.                                      (E)

These conditions are also sufficient for the pair to lie in E.

**Proof.** Both-active and both-inactive inner products are unchanged. In a mixed pair a zero projection gives no newly created zero. A nonzero projection is alpha e_k as above, so the original inner product is nonzero because the kth coordinate of A_x is nonzero. The new inner product vanishes exactly when the kth coordinate of U A_x vanishes. These are all possibilities, with no reality, sign or common-frame assumption. ∎

Thus the new constraints are localized at the active cells that have become the coordinate ray opposite to a nonzero coordinate projection of an inactive cell. This classification includes arbitrarily many active cells, repeated projective rays and arbitrary complex entry phases; no finite example is being sampled.

### 5.3 Full converse caller — ALL actual mates, not a single favorable one

Suppose B2,B3,B4 are actual QLS, pairwise mutually orthogonal, and each is orthogonal to A'. Then

    (A,B2,B3,B4) is an actual four-family
       iff for EVERY {x,y} in E and EVERY a in {2,3,4},
              <B_a(x),B_a(y)>=0.                        (LIFT)

**Proof of necessity.** At an E-pair the original A overlap is nonzero. Applying (O) to each actual mate forces its overlap to vanish.

**Proof of sufficiency.** For any x≠y and any mate a: if the original A overlap is zero, (O) holds. If the A' overlap is nonzero, A'-B_a orthogonality already forces the mate overlap zero. The only remaining case is an E-pair, handled by (LIFT). All product vectors have unit norm and their number is the tensor-space dimension, so they are an ONB, not merely a list of vanishing tests. All individual QLS and unchanged mate-pair conditions were hypotheses and have been preserved. ∎

**Exact failure identified:** the supplied source gives

    every common mate of A is a common mate of A',

whereas a proposed inverse/gluing argument would need the reverse implication. That reverse follows **only with the complete additional (LIFT) constraints**; it is not supplied by classicality or pair-product orthogonality of the new family alone. This packet does not assert that the reverse is always false or furnish a selected counterexample. It proves the exact necessary-and-sufficient residual at all variable values.

### 5.4 Degenerate and phase/frame cases

- Omega empty gives A'=A and E empty: the criterion is vacuous and makes no nonclassicality claim.
- A unitary that creates no new zero gives E empty even if phases/values changed. No strict enlargement of the mate set is assumed.
- A mixed pair with zero projection was already orthogonal; it never enters E. Both-active and both-inactive pairs never enter E.
- A created pair cannot be a same-row or same-column pair, since those were already orthogonal in A. This follows from the actual QLS hypothesis, not an assumed graph pattern.
- Independent rephasing of entries changes nonzero inner products by nonzero phases, not Z/E or (LIFT). Separate global unitaries on each mate preserve its zero inner products. The chosen frame for A specifies operation(T), but imposes no common frame on the other members.
- The theorem does not claim that independently specified supports, partial rows or local inequalities can supply the actual A,B_a used in its converse.

## 6. Joint all-member lift — common classicalization does not remove coupled defects

The following consequence does not assume weight≤2 for arbitrary original members. Its explicit premise is that the required zero-preserving comparison is actually supplied; §5 proves one legitimate mechanism for that premise, not a universal one.

Let A1,…,A4 be actual individual QLS on the SAME cells. Suppose C1,…,C4 form an ACTUAL four-family, and for every a,

    Z(A_a) subset Z(C_a).

For a finite sequence of legitimate §5 operations this follows by transitivity, including when the selected member/active supports vary from step to step. Define the defect set

    D_a=Z(C_a) minus Z(A_a).

For every cell pair e let N_C(e) be the members with a nonzero C overlap and let D(e)={a:e in D_a}. Since the C tuple is actual, |N_C(e)|≤1. The exact identity is

    N_A(e)=N_C(e) disjoint-union D(e).

Therefore the original tuple is an actual four-family **iff** at every cell pair

    |N_C(e)|+|D(e)|<=1.                                 (JOINT)

Equivalently:

1. the four defect sets D_a are pairwise disjoint; and
2. every defect pair lies where **ALL FOUR** C members have zero overlap.

**Proof.** If a C overlap is nonzero, zero preservation makes the original one nonzero. If it is zero, the original is nonzero exactly when that pair belongs to D_a. These alternatives are disjoint and exhaustive. Formula(O) for every member pair says precisely that no cell pair has nonzero overlap in two original members. This is(JOINT). Individual QLS and n²-vector completeness supply the physical forward/converse caller as in §5.3. ∎

When C is classical, its nonzero-overlap pairs are exactly cells with the same classical ray/value in that member. Thus every defect must avoid **all** those coincidence pairs, and no two members may consume the same remaining pair. This is a simultaneous compatibility obstruction, not four independent one-square inverse choices. Pairwise orthogonality of the classical C tuple alone says nothing that automatically pays those defect-ownership conditions.

No arbitrary classical net assignment or abstract defect graph is asserted realizable: (JOINT) is sufficient only when the original individual QLS and the actual zero-preserving comparison already exist. Complex amplitudes/row-column ONBs and the comparison itself remain load-bearing inputs.

## 7. Exact unrestricted gap; no six-to-four substitution

The source's Theorem5 obtains weight≤2 using **n−2 actual members** in standard form. At order8 that is six, not four. With only four, its same support-disjointness argument does not exclude weights3 or4. This is a hypothesis ceiling of the printed proof, not a new necessary-budget result and not a constructed heavy entry.

Accordingly Lemma10/§5 cannot simply be applied to every member of an unrestricted four-family. The first unproved premise for that proposed route is an admissible orthogonality-preserving classicalization for the original higher-weight members, or another input-clean replacement connecting the actual same-family data. The current paper does not supply that premise for four members.
Even when a legitimate comparison exists, inverse gluing also requires the **full joint defect criterion** §6; local or classicalized compatibility is not its converse.

There is a second distinct source ceiling: Theorem9 extends **n−3 classical MOLS(n)** to n−1 when n≠4. At order8 its hypothesis is five classical MOLS, not four (and a four-family with a genuinely nonclassical member has even fewer classical members). It does not license extending an arbitrary classicalized four-tuple. No prior C4 classification/completion theorem is imported, and no unextendability of four MOLS is claimed here.

The inherited separately adopted GAP3/C2/C3/local-span exports are safe-status statements, not supplied operative proof definitions for a new equivalence. They do not provide a classicalization/lift theorem or a physical higher-component gluing witness in this release. F9 and all excluded later/held candidate bodies remain NONINPUT rather than an answer to this missing premise.

## 8. What has and has not changed; continuation

**Delivered within the first source/written cycle:**

- Complete literal-definition/Problem16/order8/prior-claim check for the specifically admitted v2. Its printed definitions match the proposed per-member-frame four-family predicate; its statements do not settle that four-family alternative.
- A full all-variable actual-QLS/common-mate transfer candidate: zero preservation, exact classification of newly created zeros, all-three-mate necessary-and-sufficient inverse criterion, every degenerate/complex-phase/frame case.
- The simultaneous four-member defect-ownership criterion and the exact failed implication from a classicalized family to an unrestricted actual inverse family.
- Named missing higher-weight classicalization and missing classical-four completion premises. Neither is filled by a budget, an unreviewed local packet or an old metadata/reference graph.

This is **WRITTEN / UNREVIEWED conditional transfer and scope-obstruction work**, not full four-family classicality, a physical nonclassical witness, a numerical M(8)/maximum-three statement, book equivalence, novelty/priority clearance or stronger verification. The paper's forward Lemma10 is PRIOR; the reverse-compatibility formulation is supplied here at its exact hypotheses, with no claim of historical novelty or an independent-provenance certificate.

The next genuinely admitted question is whether the residual conditions in §5–§6 impose an additional actual-family obstruction without assuming a global higher-weight classicalization. No excluded guide or missing local theorem may select that next method. If such a source-separated implication cannot be established from these admitted inputs, the exact blocked premise above must be sent to Main for a new narrowly frozen input/duty—not silently replaced by an affine, all-four-nonclassical or tested low-weight task.

All original STOP/HOLD/ZERO boundaries outside S1 remain; N4 UNKNOWN with historical exit UNESTABLISHED; aux214 STOP. No old proof/review/park/checkpoint/bibliography expansion, numeric state/control/boundary/decimal probe or scientific execution occurred. Source reading and written identities are not executable/formal/human/configured-family or novelty acceptance. Only the new exclusive root was written. The new research deadline remains2026-10-31T21:23:27.000Z; one submission is not completion of the96-hour request.
