# Independent written reconstruction: all-topology six-state layer constraints

Before-review clock observed: **2026-10-23T13:49:27-07:00**. Reviewer: PhysicsResearch96h. No author edit, scientific execution, finite graph enumeration, symbolic program, model CLI or proof-assistant verification was performed. New angular candidate generation remains paused as requested.

## Snapshot, dependencies and verdict

Reviewed the complete 127-line manuscript `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/proof-H12-six-state-layer-constraints-v1.md`, source SHA-256 **`25610ef0518f476257d329ca52708d71a4349e86b800d15ae2e7dbb671c50aab`**, observed by metadata hashing.

The exact-degree obstruction and explicit positive six-state anchor were also read in `proof-repeated-pole-PH-v1.md`, notably its trace argument and full Section 6 parameters. The review reconstructs those relevant implications below rather than importing an unspecified six-state exclusion.

**Verdict: 0 FATAL / 0 MAJOR / 1 MINOR.** No substantive defect found in L6's necessary structural conclusions at `beta>1/sqrt3`. The minor is an omitted `ell>=1` qualification in one intermediate block statement; it does not affect the actual five-/three-state block exclusions. No six-state impossibility or minimum-seven conclusion is supplied or endorsed.

## Finding M1 — MINOR: specify a block actually contains a conjugate pair

**Location:** lines 56–58. The sentence about “a block with one real eigenvalue -r and ell conjugate pairs” claims r<a and the displayed b inequality without explicitly excluding ell=0. Perron theory gives r<a only for a block that contains at least one of the nonreal eigenvalues. A singleton block has no such comparison: its rate could exceed a, and b is not in its spectrum.

**Repair:** begin the statement “For an irreducible block containing ell>=1 conjugate pairs and one real eigenvalue -r ...”. The proof uses it only for the five-state block (ell=2) or the two three-state blocks (ell=1), so the claimed L6 theorem is unchanged. In a 1+5 split it is the **five-state** block, not the singleton, that supplies the contradiction.

## 1. Denominator, trimming and the canceled dominant mode (lines 36–50)

A scalar resolvent transform has reduced denominator dividing det(sI-T). Here D5 is monic degree five and uncanceled because its numerator K is positive constant. For a real six-state T, the monic quotient is s+u with real u; Hurwitz stability gives u>0.

The universal five-state obstruction follows directly from the exact degree spectrum. For an order-five representation, shift by c. The eigenvalues become zero and -d±ib, each twice, so trace=-4d and trace of the square=4(d^2-b^2). Nonnegative off-diagonal products and diagonal Cauchy give `16d^2<=5·4(d^2-b^2)`, hence beta^2<=1/5. Degree excludes orders below five. Therefore the present beta>1/sqrt3 excludes every representation with at most five states.

If a state were unreachable from the initial support, deleting all unreachable states preserves the transform and yields at most five states. No transition from a reachable state into the deleted set can exist, so the restricted row sums/exit remain valid. This contradicts the obstruction. Co-reachability also follows: a transient state with no route to a positive exit would contain a reachable final communicating class with zero row sums, forcing a zero eigenvalue of the Hurwitz generator.

For a dominant irreducible diagonal block, reachability and co-reachability make the restrictions of alpha exp(Tt0) and exp(Tt0)w nonzero and nonnegative for any fixed t0>0. Trajectories remaining in that block yield a lower bound by its own Metzler exponential. Its positive left/right Perron vectors imply `f(t+2t0)>=C exp(rho t)` for large t. The exact target density has leading term `K exp(-ct)/(d^2+b^2)^2`, with all other terms polynomial times exp(-at). Consequently rho cannot exceed -c. Since -c is in the spectrum, rho=-c and u>=c. This correctly rules out a canceled, accessible slower mode; it does not assume every eigenvalue must itself be an observable pole.

## 2. Reducible block alternatives and strict diagonal rates (lines 52–66)

Each irreducible Metzler block has a real algebraically simple Perron eigenvalue. Only two real spectral entries are available, counted with multiplicity: -c and -u. A reducible T therefore has exactly two diagonal blocks, each consuming one real spectral entry. The remaining entries occur in conjugate pairs, so the sizes are 1+5, 3+3 or 5+1. This also covers u=c: the repeated real spectral value must occur in separate blocks because the Perron eigenvalue within an irreducible block is simple.

For a block with ell>=1 conjugate pairs and real Perron eigenvalue -r, Perron strictness gives a-r>0. Shifting by r, its trace is `-2ell(a-r)` and square trace `2ell((a-r)^2-b^2)`. Diagonal Cauchy and nonnegative reverse-edge products give

`[2ell(a-r)]^2 <= (2ell+1)2ell[(a-r)^2-b^2]`,

hence `b^2<=(a-r)^2/(2ell+1)`. Since r is c or u and u>=c, the five-state block would force beta^2<=1/5 and two three-state blocks would force beta^2<=1/3. Both contradict the scoped beta condition. Thus T is irreducible. Its real Perron eigenvalue is -c and simple, so u>c.

For its positive Perron vector h, every row has at least one positive off-diagonal rate. The relation `-c=T_ii+Σ_(j!=i)T_ij h_j/h_i` therefore gives `lambda_i=-T_ii>c` strictly. No constant-diagonal ansatz is imposed.

## 3. Origin zeros, a simple four-edge path and all six placements (lines 68–84)

The large-s expansion of the finite resolvent is `Σ_j alpha T^j w/s^(j+1)`. Comparing with `K/s^5+O(s^-6)` gives exactly the first four zero derivatives and f^(4)(0)=K.

For B=T+Lambda I>=0, binomial expansion preserves those zero lower moments and gives alpha B^4 w=K. Every walk term is nonnegative, so no positive initial-to-exit walk has fewer than four steps, and at least one has exactly four. A diagonal step or repeated vertex in that walk could be removed to produce a shorter positive walk; therefore the four steps are off-diagonal edges on a simple path through five distinct states.

Distance from the initial support along that chosen shortest path is exactly 0,1,2,3,4: a smaller intermediate distance followed by the remaining suffix would shorten an exit route. Reachability in a six-vertex graph bounds every distance by five. The single remaining vertex can thus lie in any of layers0,1,2,3,4,5. This retains all six alternatives: a doubled layer among0–4 or six singleton layers0–5.

For any edge i→j, the definition of distance gives delta(j)<=delta(i)+1. This only limits forward jumps; it does **not** forbid within-layer edges or arbitrary backward edges. Layer zero is exactly the positive initial support, and every positive exit has distance at least four, hence lies in layer4 or5. In particular a doubled layer zero means both its vertices initially have positive mass. The reduction does not smuggle in acyclicity, one-way chains, or a single start/exit state.

## 4. Cofactor/simple-path numerator and both coefficients (lines 86–105)

The standard cofactor permutation expansion for alpha(sI-T)^(-1)w consists of one open simple path from an initial index to an exit index, plus disjoint cycles on unused vertices. The signs of that open path cancel the negative off-diagonal entries of sI-T; its rate product is positive. The remaining permutation sum is exactly the complementary **principal** determinant. This is valid with feedback and with multiple initial/exit supports.

All path weights of lengths below four vanish by the preceding argument. A simple four-edge path uses five vertices, leaving one vertex m and complementary determinant s+lambda_m. A simple five-edge path leaves the empty determinant one. There is no longer simple path in six states. Hence the full transfer numerator is exactly

`Σ_m W_m(s+lambda_m)+R5`.

The characteristic polynomial and exact target transfer give the same numerator as `K(s+u)`. Comparing its s coefficient and constant coefficient yields

`Σ_m W_m=K`, `Ku=Σ_m W_m lambda_m+R5`.

All weights are nonnegative and at least one four-edge weight is positive. Cycles have not been omitted; they are accounted for by the denominator and complementary determinants in the exact cofactor identity. Shorter-path cycle terms cannot reappear because their initial-to-exit path weights are zero.

## 5. Trace equations and the remaining lower-bound gap (lines 107–121)

For M=T+cI, its eigenvalues are `0,-v,-d±ib` each twice. Thus

`tr M=-(4d+v)`, `tr M^2=v^2+4(d^2-b^2)`.

Its diagonal is -x_i, while its off-diagonal entries remain nonnegative. Therefore

`Σ_i x_i=4d+v`,

`Σ_i x_i^2<=v^2+4(d^2-b^2)`.

Dividing the path constant identity by K and using ΣW_m=K gives `v=Σ_m(W_m/K)x_m+R5/K`, with x_i,v strictly positive. Diagonal Cauchy gives the displayed weaker six-times-square-trace inequality. It is only necessary: its v^2 term does not bound a large hidden rate on its own, and the manuscript does not claim otherwise.

## 6. Independent positive anchor: T6 with doubled layer zero

The earlier exact T6 has alpha support{1,2}, weights `d/u,a/u`, with `u=c+2d=a+d`; diagonal rates are all a, superdiagonal rates a, and only state6 exits, at rate `K u/a^5`. Its feedbacks from state6 go to1,3,5, with the last possibly zero at beta^2=1/2.

The only simple four-edge initial-to-exit path is `2→3→4→5→6`, omitting vertex1. Its weight is

`(a/u)a^4(Ku/a^5)=K`,

so W1=K and every other W_m=0. The simple five-edge path `1→2→3→4→5→6` has weight

`(d/u)a^5(Ku/a^5)=dK`,

so R5=dK. Feedback cannot create another simple path ending at6 without visiting the exit earlier and repeating it. Thus `Ku=K a+dK` exactly, with lambda1=a.

Distances are delta1=delta2=0, delta3=1, delta4=2, delta5=3, delta6=4. The edge1→2 is within the doubled initial layer; the feedbacks are permitted backward edges. This checks that the layer statement does not accidentally exclude a valid construction.

Here x_i=d and v=2d. The trace constraints reduce to `6d^2<=8d^2-4b^2`, precisely beta^2<=1/2, and the path identity is v=d+d. In the overlap `1/3<beta^2<=1/2`, the positive anchor satisfies every scoped L6 condition. This is written symbolic reconstruction, not a point evaluation or new scientific run.

## Boundaries

The corrected block qualification is the only finding. The lemma supplies all-topology **necessary** structure; it neither classifies rates on the six placements nor rules out all six-state realizations in the G7 residual band. Existing PH existence, six-state upper constructions and the minimum-six-or-seven gap remain compatible. Ordinary written checking is separate from novelty, human review and formal/kernel verification.
