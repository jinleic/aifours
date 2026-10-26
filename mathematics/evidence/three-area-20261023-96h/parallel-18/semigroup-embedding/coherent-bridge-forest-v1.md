# A combined multi-gap/context bridge construction: the acyclic single-load criterion

MathSemigroup, math-4. Clock actually observed immediately before creation: **2026-10-23T14:46:26-0700**.

**CANDIDATE / PARTIAL / NOVELTY_UNCLEAR.** This directly attacks the combined MULTIGAP and CONTEXT-CROSSING cases of the SAME canonical idempotent-fibre construction. It allows arbitrary numbers of gaps and arbitrary rewrite contexts; its remaining hypothesis is instead a precisely defined finite dependency condition. It does not prove that all canonical derivations have that condition. No scientific executable, graph program, solver or enumeration was run. No acceptance is claimed before reconstruction.

## 1. Exact source, goal and new bounded claim

Work in the orthodox diagnostic branch already frozen: S is regular, E-unitary orthodox, every local idempotent band is regular, and sigma:S→G is the least group quotient with sigma^(-1)(1)=E(S). Letters X_(u,s) are actual arrows u→u sigma(s). The canonical band presentation uses actual composition M_G, band idempotency U^2=U, and

    P Z P X P Z P Y P Z P = P Z P X P Y P Z P.     (LR_P)

No fixed outer context or width-one assumption is made below.

**Claim.** Given any FINITE primitive canonical-congruence derivation D between two path words of the same endpoints, construct the finite occurrence-level bridge constraints in §2. If the resulting constraints are **single-load and acyclic** as defined in §4, then the two path words have the same value in S.

Therefore a canonical derivation that collapses distinct source paths must fail this criterion: at least one bridge class has multiple distinct inverse loads, or its dependency graph has a directed cycle (including a self-loop). This is a necessary obstruction in this sufficient construction, not a nonembedding theorem from a failed graph test. In particular, it is not asserted that every failed criterion is a genuine source collapse.

The claim handles R1 and R2 simultaneously whenever the finite dependency condition holds. It is not a further width-one refinement. Its mathematical imports are source regularity, purity of sigma, the actual typed local-corner identity proved in the pinned predecessor, and elementary finite topological ordering. The predecessor remains CANDIDATE pending parent composition; the present argument does not independently promote it.

## 2. Occurrence-level variables and the finite constraint construction

For each word at each stage of D, place one variable at EACH incompatible adjacency of consecutive absolute-object-labelled arrows. If that adjacency runs from an arrow ending at b to an arrow starting at a, give its variable the required grade b^(-1)a. No variable is inserted at a compatible adjacency. An assignment of source elements of the required grades completes every word to an actual path. Its value is the ordered product of original source labels and the inserted elements. Every completed word has its original first/last objects, regardless of how many internal gaps there are.

Initially treat different gap occurrences as different variables, even if they have the same ordered endpoints. This distinction is essential; there is NO global identification by endpoint pair.

Impose only the following identifications and equations as D is traversed. All variables being identified have the same grade, because the underlying absolute endpoints are the same.

### 2.1 Common contexts and actual M_G steps

At every elementary step, identify variables at corresponding untouched context adjacencies, including the two outer context/rewrite boundaries whenever they are gaps. The two rewritten expressions have the same first/last objects, so these correspondences are well defined.

For an M_G step, its two composable letters have no gap between them. Their product label is literally st. The common-context identifications are all that is needed: the completed values on the two sides are equal by source multiplication, even when the rewrite crosses a boundary of a previously chosen excursion core.

### 2.2 LR_P steps

For each substituted formal block P,Z,X,Y, identify variables at corresponding internal gap positions across all copies of that SAME formal block on both sides of the step. Different formal blocks are NOT identified merely because their substitution words happen to be equal.

Also identify variables at corresponding boundary occurrences of the same ordered formal-block pair on the two sides and across repeated occurrences. The only such pairs are

    PZ, ZP, PX, XP, PY, YP.

When a boundary is compatible no variable is present. When it is incompatible, repeated occurrences of the same formal pair have the same absolute endpoint pair and hence can consistently share a variable. Repeated PZ and ZP boundaries are included, not omitted.

These identifications ensure that repeated completed blocks and their boundary bridges agree exactly where the local identity needs them to agree. Section3 proves preservation for arbitrary simultaneous gaps, rather than assuming it.

### 2.3 Band idempotency steps

For a substitution U^2=U, identify variables at corresponding internal gap positions in every copy of U and on both sides. Context variables are transported as in §2.1. Let w be the resulting completed S-word for ONE U, retaining its bridge variables as formal inputs.

If U starts and ends at the same object, no new between-copy bridge is present. The completed w has grade1 and is idempotent by purity; no inverse equation is imposed.

If U has endpoints a→b with a!=b, let beta be the between-copy bridge variable. It has grade b^(-1)a. Record the constraint

    w beta w = w.                                (INV)

The same rule applies to contractions as well as expansions. This is an actual source inner-inverse equation, not a band axiom assumed to hold in S. Its solvability will be constructed under the finite condition in §4.

After processing all steps, quotient the finite variable set by the identifications. Substitute these variable classes into all completed words and INV constraints. A variable may now occur inside a completed word w whose INV constraint also targets that variable; that is a genuine self-dependency, not something to erase silently.

If two recorded constraints have literally the same target beta and the same ordered completed word w after this substitution, keep one copy. This is syntactic duplicate removal only; no unproved equality in S or computation of a normal form is used.

## 3. Why satisfying these constraints preserves every primitive step

Actual multiplication steps were handled in §2.1. For idempotency, the internal-copy identifications make the two U completions have the same value w. In the loop case w^2=w follows from purity; in the nonloop case the completed double has value w beta w, equal to w by its recorded INV equation. Multiplying the unchanged completed outer contexts preserves equality. This proof does not require natural-order compatibility.

For an LR step, first complete each formal block internally. Let the completed P be a path a→b. Let completed Z,X,Y have arbitrary endpoint pairs c→d, f→g, h→k. Absorb their shared boundary bridges into

    Z_tilde=(bridge b→c) Z (bridge d→a),
    X_tilde=(bridge b→f) X (bridge g→a),
    Y_tilde=(bridge b→h) Y (bridge k→a),

omitting any bridge at a compatible pair. Each tilde block is a nonempty actual path b→a. The forced identifications in §2.2 make all repeated P and Z_tilde values identical across their occurrences and across the two LR sides. X_tilde,Y_tilde each occur once, with their corresponding values on the two sides.

The completed LR relation is therefore precisely a path-typed instance

    p z_tilde p x_tilde p z_tilde p y_tilde p z_tilde p
       = p z_tilde p x_tilde p y_tilde p z_tilde p.

The actual corner proof at e=pp' from `path-separation-attack-v1.md` establishes this equality in S: purity makes p z_tilde,p x_tilde,p y_tilde idempotent, and the regular-band identity in E(eSe) supplies the result. Nothing requires the original raw blocks or the whole raw word to be paths, and nothing bounds the number of gaps. The completed outer contexts on both sides agree by §2.1.

Thus ANY assignment satisfying the grade, identification and INV constraints gives equal completed S-values throughout the full derivation, including multiple gaps and changing rewrite contexts. If both endpoints are path words, they contain no bridge variables, so their actual S-values are equal.

## 4. Constructive solvability under the acyclic single-load condition

For each remaining INV equation w beta w=w call beta its **target** and w its **load word**. A bridge variable is **single-load** if, after the syntactic deduplication above, it is targeted by at most ONE INV equation. The whole constraint system is single-load if every bridge variable has this property.

Make a finite directed dependency graph on the variable classes: for every variable alpha occurring in the load word w of a constraint targeting beta, draw an edge alpha→beta. Constants from S create no graph vertex or edge. A beta occurring in its own load creates a self-loop. The system is acyclic when this entire graph has no directed cycle.

**Solvability lemma.** Every single-load acyclic system just constructed has an assignment in S satisfying all its constraints.

**Proof.** Process the finite graph in topological order. If a variable beta has no target equation, choose any element of S of its required grade; surjectivity of sigma supplies one. If beta is targeted, its unique load w involves only earlier variables, so it already has an actual value s in S. Its grade is a^(-1)b for the endpoints a→b of the duplicated block. Choose any mutual inverse s' in V_S(s), which exists by regularity. Then

    sigma(s')=sigma(s)^(-1)=b^(-1)a,

so assigning beta=s' has the required grade and satisfies s beta s=s. It does not violate a previously imposed target constraint: beta could occur in such an earlier load only if an edge beta→earlier-target forced beta earlier in topological order. It cannot carry a second different target equation by single-load. Therefore this induction assigns every variable and satisfies every INV equation. QED.

Combine this lemma with §3 to prove the claim in §1. This is an actual finite construction of the source bridge assignment under the stated dependency hypotheses, not an assertion that a desired assignment exists.

Purity is used exactly for loop idempotency and the typed LR corner argument; regularity supplies the selected mutual inverses. The topological-assignment proof alone does not remove the purity requirement from the full bridge construction.

## 5. Concrete control: this differs from the failed endpoint-only ansatz

Let E={0,a,b} be the semilattice with a,b incomparable and a b=0. Let S=E cross C2, C2={1,g}. This is an explicitly embedded inverse/E-unitary source with pure group projection. Take the two nonloop letters

    U_a=X_(1,(a,g)), U_b=X_(1,(b,g)),

and their reverse-object letters V_a=X_(g,(a,g)), V_b=X_(g,(b,g)). The word

    U_a V_a U_b V_b

is a loop. Expand both U_a and U_b by band idempotency before contracting them again; this produces two simultaneous gaps, a genuine width-two derivation, although the endpoints are of course identical.

A SINGLE fixed endpoint bridge g→1 would be(c,g) for some c in E and would have to satisfy

    a c=a,   b c=b.

No such c exists: c=0 fails both, c=a fails the second, and c=b fails the first. Thus even a finite given derivation can defeat the endpoint-only bridge prescription on an already embedded source; this is not merely the earlier infinite absence-of-a-common-upper-bound control.

The occurrence-level construction does not make that mistake. The two new bridge variables beta_a,beta_b are independent unless a later step actually identifies them. Here their separate load words are the constants(a,g),(b,g). Repeated expansion/contraction constraints deduplicate syntactically. There are no dependency edges and each target has one load. Choose

    beta_a=(a,g), beta_b=(b,g),

their actual self-inverses. The width-two derivation is correctly validated. This illustrates why the criterion really reaches some MULTIGAP cases rather than being another width-one statement.

Failure of the criterion in other examples still does not imply source nonembeddability; bridge identifications or multiple loads can be too demanding for a particular proof diagram even when another faithful construction exists. The control is not a new book-case result or an enumeration.

## 6. Exact remaining combined gap

The criterion has no gap-count bound and no untouched-context requirement. Its unresolved configurations are now finite and explicit:

- **reused inverse load:** one bridge class is forced to be an inner inverse of two syntactically different completed words;
- **cyclic bridge dependency:** mutual-inverse choices would depend cyclically on one another, including a load containing its own target variable.

The earlier isolated-excursion lemma can handle one special reused-load situation by retaining the identity for ALL bridge values and substituting different actual inverses separately. No general treatment of such reused loads or cycles has been proved.

A complete embedding proof would need to show that canonical collapse derivations can always be transformed to admissible constraint diagrams, or directly discharge the repeated-load/cyclic cases without assuming a common inverse. No such transformation is asserted. The broad nonorthodox Rees analogue remains an independent extension obligation.

This is a single combined construction attempt within the original problem. All claims remain author-written candidates at the declared boundary, with novelty unclear and no theorem/discovery count. The original R1/R2 regimes are not announced closed; some configurations from both are now handled under the explicit bridge-dependency condition.
