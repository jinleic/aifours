# The exact registered septic SPR7 question is a real-closed-field sentence

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 17:48:40 PDT 2026**. **WRITTEN candidate; no quantifier-elimination computation performed.** The following identifies an exact finite decision problem for the literal fixed-degree-seven target. It does NOT determine its truth value or produce an original counterexample.

## 1. Inputs, named classical imports, and conclusion

The registered original definitions are `institute/runs/three-area-2026-10-27-96h/written-releases/info-2-septic-box-definitions-v1.md`, SHA256 `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad`. Import the full written reductions in `frontier-20261028-rational-box-rational-numerator-reduction-v1.md`, SHA256 `6d29bc63925a100394b1b3efc8fe9fecf49660f7c6ff19798ba246e42442f328`, in particular its monic-numerator normalization, four actual corners for a fixed numerator, and rational-positive-width superbox reduction. That paper is author-unreviewed; its conclusions are not promoted by being imported here.

The **ordinary Routh–Hurwitz criterion** says that a real monic degree-seven polynomial is strictly Hurwitz exactly when all seven leading Hurwitz determinants defined below are strictly positive. The **Tarski quantifier-elimination theorem for real closed fields** provides an effective procedure that takes any first-order formula with integer-coefficient polynomial equalities/inequalities and outputs an equivalent quantifier-free formula over the reals. For a closed sentence this decides true or false. These are named classical mathematical imports, not claims that a particular solver ran or that its output is available.

**Theorem, conditional on these named imports and the full predecessor:** the ORIGINAL fixed-n=7 robust-synthesis question is equivalent to the explicit closed first-order real-field sentence Phi_7 in §3. Therefore its yes/no truth is decidable in principle by real-closed-field quantifier elimination. This says nothing about whether a feasible implementation or affordable run is available, and supplies neither branch of the answer.

## 2. Polynomial predicates, including the exact denominator and numerator degree

Write the denominator as `a(s)=s^7+sum_(j=0..6)a_j s^j`. Define `c_0=1`, `c_i=a_(7-i)` for i=1,...,7, and `c_i=0` outside 0,...,7. Define the 7x7 Hurwitz matrix by

`H(a)_(i,j)=c_(2j-i)`, for i,j=1,...,7,

and `D_k(a)=det H(a)[1..k,1..k]`. These are explicit integer-coefficient polynomials in the seven a_j. Set

`Box(l,u,a) := AND_(j=0..6) (l_j<=a_j<=u_j)`,
`Hurwitz(a) := AND_(k=1..7) D_k(a)>0`,
`StableBox(l,u) := forall a in R^7: Box(l,u,a) => Hurwitz(a)`.

The first row of H is `(c_1,c_3,c_5,c_7,0,0,0)` and the second is `(c_0,c_2,c_4,c_6,0,0,0)`, fixing the determinant convention. By the named Routh–Hurwitz criterion, `StableBox` has exactly the registered all-member strictly-Hurwitz meaning; it is not merely positivity of a few corners.

For a normalized numerator `b(s)=s^7+sum_(k=0..6)b_k s^k`, put `a_7=b_7=1` and define the REAL polynomial

`P(a,b,t) = sum_(0<=j,k<=7; j+k even) (-1)^((k-j)/2) a_j b_k t^((j+k)/2)`.

The exponent `(k-j)/2` is an integer, so its sign is +1 or -1 even when it is negative. This is exactly `Re[b(i sqrt(t)) a(-i sqrt(t))]`; the latter notation is explanatory only. Every coefficient in P is an integer polynomial in a,b, and its degree in t is seven with leading coefficient1. For a Hurwitz a its denominator `|a(iw)|^2` is positive, hence the original strict real-part condition at every finite real w is exactly `P(a,b,t)>0` for every real t>=0. No square-root, division by a possibly zero polynomial, denominator reversal, or infinity-as-an-original-frequency is present in the formal predicate.

Let `a^(sigma,tau)(l,u)`, sigma,tau in `{-,+}`, be the four actual corner coefficient vectors from §4 of the predecessor: for even j=0,2,4,6 the minus vector uses `(l_0,u_2,l_4,u_6)` and plus uses `(u_0,l_2,u_4,l_6)`; for odd j=1,3,5 minus uses `(l_1,u_3,l_5)` and plus uses `(u_1,l_3,u_5)`. The leading coefficient is always1. All four are actual members, with duplicates permitted for degenerate intervals. The predecessor proves that for a FIXED b their four pairing polynomials are strictly positive on t>=0 if and only if that SAME b works for every a in the box.

## 3. The closed exact sentence

Using the explicit terms above, define

`Phi_7 := forall l,u in R^7:`

`  [ (AND_j l_j<=u_j) AND StableBox(l,u) ] =>`

`  [ exists b_0,...,b_6 in R: forall t in R,`
`       t>=0 => AND_(sigma,tau in {-,+}) P(a^(sigma,tau)(l,u),b,t)>0 ].`

Every quantifier is over real variables and every atom is a polynomial equality or weak/strict inequality with integer coefficients. The formula has fourteen outer endpoint variables, seven denominator variables local to StableBox, seven shared numerator variables, and one nonnegative-frequency variable; no quantifier over functions, infinitely many algebraic expressions, random variables, or unbounded polynomial degree is hidden.

If Phi_7 is true, the Routh predicate makes its antecedent exactly every eligible original K, and its consequent gives an actual exact-degree-seven common numerator by the four-corner proof. Conversely, an original numerator necessarily has positive leading coefficient, so dividing by that coefficient makes it monic; the original strict inequalities then imply the Phi_7 consequent. Thus Phi_7 and the registered target have the SAME truth value. Degenerate intervals are covered by `<=`; zero frequency by `t>=0`; strictness and shared-b quantifiers are explicit.

Invoking the named quantifier-elimination theorem on this ONE closed formula would terminate in a Boolean answer in the ordinary abstract computability model. This is a logical consequence of the known theorem, NOT a claim that we have executed CAD, produced a QE proof certificate, estimated practical resource costs, or established either Boolean value. For the book's unbounded all-orders assertion, there is a different formula for each fixed order; this single Phi_7 does **not** decide their infinite conjunction.

## 4. Exact one-sided rational-box consequence

The predecessor proves that any real-endpoint/degenerate counterexample is contained in an actual eligible rational-endpoint superbox with all seven widths positive, which is itself a counterexample. Enumerate such rational boxes in any effective exhaustive order. For each, decide `StableBox` by either the predecessor's finite Routh/Sturm sign procedure or real-field QE. If stable, substitute its rational endpoints into the consequent of Phi_7 and apply real-field QE to its seven numerator and one t variable. If that consequent is false, the rational box is an actual negative original witness, not a finite numerical scan or profile failure.

This yields, **in principle**, a one-sided exact search that halts if an original counterexample exists; it is not claimed to halt under universal synthesis and has not been executed. The full Phi_7 QE would, in principle, decide both outcomes independently of such an enumeration. If the consequent is true for a rational box, the predecessor's compact-margin/rational-density argument also guarantees a monic rational witness, which can be found in principle by enumerating rational coefficients and applying its four Sturm tests. There is no asserted effective practical bound on when either enumeration finds a witness.

## 5. Assurance and remaining scientific issue

The original sign question is still OPEN in this record: no QE, numerical experiment, global proof, actual negative box, witness certificate, novelty or stronger verification follows from the existence of a decision algorithm. The work is a precise bridge to a fully specified original-object algebraic decision problem, not a substitution by the already solved local box or a claim that an unexecuted program establishes science. A complete source/whole-proof review is needed before adoption. No mathematical interpreter, external model, nested agent, scientific subprocess, network publication, Git action or deletion was used for this written derivation. Earlier STOP/HOLD/ZERO histories are not altered or supplied as premises.

**END.**
