# Classification of Fermat-spiral limit types

Date: 2026-10-14 PT. **Verdict: SOLVED for the exact type/covolume questions in Theorems 1–2. Evidence label: Certification by a written proof.** The local-lattice mechanism is classical (Bacher 2014); no new approximation method or worldwide first-priority claim is made. An independent referee found no mathematical gap; attribution/source clarifications and finite controls are recorded below. This is not a Lean/kernel certificate.

## 1. Exact statements

Identify the plane with C. For a fixed real alpha put

`P_n=sqrt(n)*exp(2*pi*i*n*alpha)`, `X_alpha={P_n:n>=1}`.

A translation limit means `X_alpha+t_j -> Y` in the Chabauty–Fell topology with `|t_j| -> infinity`. There are **no rescalings or rotations in this definition**. We use local closed-set convergence: for every fixed R and epsilon, eventually each point of either set in the radius-R ball lies within epsilon of the other **full** set. This formulation avoids artificial boundary errors from intersecting both sets with the same ball.

This is equivalent to Tevet's metric formulation: for a requested metric error epsilon use the fixed radius `1/epsilon` (or a slightly larger radius) and a smaller local error; conversely a metric error smaller than both epsilon and `1/R` supplies the fixed-radius inclusions. We also use continuity of translations by convergent vectors and of invertible linear maps converging to an invertible map. On a fixed ball, the preimages remain in a larger bounded ball and the displacement errors are bounded by the vector error plus the matrix-norm error times that larger radius.

**Theorem 1 (types and covolume).** For every real alpha, every nonempty translation limit of X_alpha is either an affine line or an affine rank-two lattice with covolume **pi**. Thus no translate of a point, an infinite cyclic discrete group, `R x Z`, or `R^2` occurs.

**Theorem 2 (realization of types for the question's class).** For every fixed irrational alpha that is not badly approximable:

1. a lattice limit of covolume pi exists;
2. **every affine line** is a translation limit;
3. the empty set is a translation limit.

Consequently, the exact possible **types** are empty, affine line, and affine rank-two lattice of covolume pi, and all three types occur for each such alpha. This does **not** assert that every covolume-pi lattice shape occurs for a fixed alpha. That is a different realization question.

The theorem proves Tevet's p. 4 containment **in sharpened form** and gives a complete proof of the affirmative p. 12 covolume answer. Read together with his one-to-one local description, Bacher's Remark 1.2(2) already asserts that answer in Voronoi-area form: under the nonmerging convergence at a lattice limit, the local Voronoi cells converge to its fundamental cell. That is an implication of his statements, not a separately named Chabauty theorem; the remark's area assertion is unproved. Our proof instead uses the explicit fixed-area lattices. It **excludes `Z x R`**, contrary to the p. 12 computational suggestion that all proposed types are achieved. We distinguish the containment reading from the suggestion of an exact attainable list.

**Boundary statements.** Every irrational alpha, including BA alpha, has at least one lattice limit. BA alpha has only lattices as nonempty limits. Rational alpha has only affine-line nonempty limits, parallel to one of its finitely many radial directions; it also has empty limits. Adding the point P_0=0 to the source changes none of these limits.

## 2. Uniform, two-sided local lattice approximation

For `r=sqrt(n)` define the frame-rotated centered set and a genuine lattice

```text
Y_n = exp(-2*pi*i*n*alpha)*(X_alpha-P_n),
L_n = { v_n(q,p) : (q,p) in Z^2 },
v_n(q,p) = (q/(2*r), 2*pi*r*(q*alpha-p)).
```

The basis matrix is

```text
[[ 1/(2*r),       0    ],
 [ 2*pi*r*alpha, -2*pi*r ]],
```

whose determinant is `-pi`. Therefore every L_n has covolume **exactly pi**, with no Diophantine hypothesis.

**Lemma 2.1 (forward inclusion).** If R>0, `r>=4R` and `|v_n(q,p)|<=R`, then `n+q>=1`, p is the unique nearest integer to q*alpha, and

`| sqrt(n+q)*exp(2*pi*i*(q*alpha-p))-r-v_n(q,p) | <= 5R^2/r`.

Thus `L_n intersect B_R` lies in the `5R^2/r` neighborhood of Y_n.

**Proof.** Write `a=q/(2r)`, `b=2*pi*r*(q*alpha-p)`, `theta=b/r`, `s=sqrt(r^2+q)`, `u=s-r`. Since `|q|<=2rR<=r^2/2`, the integer `n+q` is strictly positive and hence at least one. Also `|q*alpha-p|<=1/(8*pi)<1/2`, which proves the nearest-integer assertion.

The exact radial identity is `a=u+u^2/(2r)`, and `|u|=|q|/(s+r)<=2|a|`. Using the elementary integral-remainder inequalities

`|exp(i theta)-1|<=|theta|`,

`|exp(i theta)-1-i theta|<=theta^2/2`,

we obtain

```text
s*exp(i theta)-r-(a+i*b)
 = (u-a)+u*(exp(i theta)-1)+r*(exp(i theta)-1-i theta),

absolute value <= (2*a^2+2*|a*b|+b^2/2)/r
               <= (3*a^2+3*b^2/2)/r
               <= 3*R^2/r <= 5*R^2/r.
```

The advertised constant five is deliberately conservative. All estimates are uniform in alpha. QED.

**Lemma 2.2 (reverse inclusion).** Suppose `m=n+q>=1`, `|P_m-P_n|<=R`, and `r>=12R`. Let p be the nearest integer to q*alpha. Then

`|v_n(q,p)|<3R`

and the same physical/frame displacement differs from v_n(q,p) by at most `45R^2/r`. Thus `Y_n intersect B_R` lies in the `45R^2/r` neighborhood of L_n.

**Proof.** Set `z=exp(-2*pi*i*n*alpha)*(P_m-P_n)` and `s=sqrt(m)`. The reverse triangle inequality gives `|s-r|<=R`, hence

`|q/(2r)|=|s-r|*(s+r)/(2r)<=R*(1+R/(2r))<=25R/24`.

Since `Re(r+z)>=r-R>0`, the principal argument theta of r+z lies strictly between `-pi/2` and `pi/2`. Moreover

`|theta|<=|Im z|/(r-R)<=R/(r-R)`.

It is the unique representative of `2*pi*q*alpha` in this interval, so it selects the unique nearest integer p, and

`|2*pi*r*(q*alpha-p)|=r*|theta|<=12R/11`.

Therefore `|v|<=|a|+|b|<3R`. Apply Lemma 2.1 at radius 3R: its requirement is exactly `r>=12R`, and its error is `5*(3R)^2/r=45R^2/r`. QED.

**Corollary 2.3.** For any sequence `n_j -> infinity`, the centered physical sets `X_alpha-P_(n_j)` and the rotated lattices

`Lambda_j=exp(2*pi*i*n_j*alpha)*L_(n_j)`

have the same Chabauty limits. The statement remains true when alpha varies with j, provided each comparison uses the same alpha on its two sides.

**Proof.** For every fixed radius R, the two inclusion errors tend to zero. For instance, a sequence of bounded points of either set is within an error tending to zero of points of the other. Both limit inclusion criteria therefore agree. Rotations are used only as an isometric change of frame in this comparison; Lambda_j is already in physical coordinates. QED.

These lemmas reprove quantitatively the local affine-lattice framework of Bacher, Theorem 1.1 and §3. The convergent-pair basis in his Proposition 3.1 is obtained from our (q,p) lattice by a unimodular integer basis change; his Remark 3.3 already states area pi.

## 3. Fixed-covolume lattice compactification, proved directly

**Lemma 3.1.** Let Lambda_j be rank-two lattices in R^2, all of covolume A>0. If they converge as closed sets, their limit is either a rank-two lattice of covolume A or a line through zero. In particular, a fixed positive covolume prevents both plane and `R x Z` limits.

**Reduced-basis fact.** For any such lattice choose a shortest nonzero vector u and write `ell=|u|`. A shortest vector is primitive: in lattice coordinates its two integer entries have gcd one, since otherwise division by that gcd gives a shorter lattice vector. Bezout therefore extends u to a lattice basis `(u,v)`. Choose its orientation so `det(u,v)=A` and subtract an integer multiple of u from v so that its parallel component h satisfies `|h|<=ell/2`. Its perpendicular component is exactly `A/ell`. Since u is shortest,

```text
ell^2 <= |v|^2 = h^2+(A/ell)^2 <= ell^2/4+A^2/ell^2,
```

so `ell^2<=2A/sqrt(3)`. This classical bound, also stated at A=pi in Bacher's Remark 3.3, supplies a universal upper bound on the shortest length without importing a compactness theorem with hidden normalizations.

**Case 1: shortest lengths are bounded below along a subsequence.** Suppose `ell_j>=epsilon>0`. The reduced bases satisfy bounded lengths for both u_j and v_j. Extract a subsequence of basis matrices `B_j -> B`. Its determinant is A, so B is invertible. Then `B_j Z^2 -> B Z^2`: fixed integer-coordinate vectors converge, while a bounded sequence `B_j z_j` has bounded integer coordinates because `B_j^-1` is uniformly bounded. After a further subsequence its integer coordinates are constant. Thus the limit is a lattice and its covolume is A, not merely a multiple or divisor of A.

**Case 2: shortest lengths tend to zero along a subsequence.** Let `e_j=u_j/ell_j`; pass to a subsequence with `e_j -> e`. Every lattice point outside `Z u_j` has perpendicular component of absolute value at least `A/ell_j`. Thus, for any fixed R, eventually all points of `Lambda_j intersect B_R` belong to `Z u_j`. Conversely, every `t e` is approximated by `round(t/ell_j)*u_j`. The mesh tends to zero and directions converge, so the limit is exactly `R e`.

Every sequence of shortest lengths has a subsequence of one of these two kinds. If the original lattices already have a closed-set limit, every subsequence has the same limit, so the alternatives above classify it. In particular a mixture of thick and thin subsequences cannot create a third limit type. QED.

**Why the cylinder is excluded.** When `ell_j -> 0`, the perpendicular layer separation is `A/ell_j -> infinity`, not a finite nonzero number. A cylinder-type group `R x Z` would require a vanishing mesh in one direction but bounded nonzero separation in the other, forcing the covolume to vanish. Likewise a plane limit would require two independent vanishing spacings. No continuity of global point density under Chabauty convergence is assumed.

## 4. Arbitrary escaping translations and affine offsets

**Proof of Theorem 1.** Suppose `X_alpha+t_j -> Y != empty` with `|t_j| -> infinity`. Pick y in Y. Closed-set convergence supplies spiral points with

`P_(n_j)+t_j -> y`.

Necessarily `n_j -> infinity`, because `|P_(n_j)|>=|t_j|-|y|-o(1)`. Translating by the convergent offsets gives

`X_alpha-P_(n_j) -> Y-y`.

Corollary 2.3 then gives the same limit for the physical lattices `exp(2*pi*i*n_j*alpha)L_(n_j)`, each of covolume pi. Lemma 3.1 proves that Y-y is a line or a lattice of covolume pi. Thus Y itself is an **affine** line or affine lattice. This also excludes the remaining closed-subgroup types without relying on Tevet's Theorem 1 or its nearest-neighbor Proposition 8. QED.

The recentering is essential: a translation limit is not automatically a subgroup containing zero. Once a centered limit exists, adding any fixed vector to the translations realizes its affine translate, and the translation vectors still escape.

## 5. Lattice limits exist for every irrational alpha

Let `p_j/q_j` be consecutive continued-fraction convergents of an irrational alpha, and `delta_j=q_j*alpha-p_j`. The elementary convergent identities are

`p_j*q_(j-1)-p_(j-1)*q_j = +/-1`,

`|delta_j|<1/q_(j+1)`.

For completeness, the determinant identity follows inductively from the convergent recurrence. If beta is the next complete quotient, then

`alpha=(p_j*beta+p_(j-1))/(q_j*beta+q_(j-1))`,

so `delta_j=+/-1/(q_j*beta+q_(j-1))`. Since `beta>a_(j+1)`, its denominator exceeds `q_(j+1)`, proving the bound.

Take the **integer centers** `n_j=q_j^2`; then r_j=q_j. In L_(n_j), the two vectors from `(q_(j-1),p_(j-1))` and `(q_j,p_j)` form a basis and both have length at most

`M=sqrt(1/4+4*pi^2)`.

Indeed, their horizontal coordinates have absolute value at most 1/2, and the two vertical coordinates have absolute value less than 2*pi. The determinant has absolute value pi by the convergent identity. Adjust one basis sign to have determinant +pi and rotate into the physical frame. The resulting basis matrices remain bounded and retain determinant pi; a subsequence converges to an invertible matrix. Its lattice is a translation limit by Corollary 2.3. This proves the lattice-type existence assertion, with no BA assumption.

The numerical bound M already appears in the paragraph immediately after Bacher's Corollary 3.2. The present use at the exact integer centers `q_j^2` and the compactness argument are given explicitly so no nearest-neighbor assertion is required.

This is only existence of at least one shape for a fixed alpha. It does not claim universality of shapes.

## 6. Non-BA angles produce lines and empty limits

For an irrational non-BA alpha, select convergents with

`q_j*|delta_j| -> 0`.

This is the negation of Tevet's badly-approximable condition. Set

`N_j=q_j/(4*pi*|delta_j|)`, `n_j=nearest integer to N_j`.

The numbers N_j tend to infinity, and `n_j/N_j -> 1`. The vector in L_(n_j) corresponding to `(q_j,p_j)` has squared length

```text
q_j^2/(4*n_j)+4*pi^2*n_j*delta_j^2
 = pi*q_j*|delta_j|*(N_j/n_j+n_j/N_j) -> 0.
```

Thus its shortest length tends to zero. Lemma 3.1's thin-case argument, after choosing a subsequence of shortest directions in physical coordinates, gives a line through zero as a translation limit of the spiral. The use of a rounded real scale causes no integrality problem and does not change the limit.

To obtain the empty limit, first observe that a fixed relative-density constant passes to every closed-set translation limit: if every ball of radius rho meets a set, choose a point in that ball for each translated set and use compactness of the ball to pass to the limit. A line has no such constant. Therefore the spiral admitting a line limit is not relatively dense. For every integer j choose c_j with `dist(c_j,X_alpha)>j`. Because P_1 belongs to X_alpha, `|c_j|>j-|P_1| -> infinity`. The sets `X_alpha-c_j` miss the entire radius-j ball and hence converge to the empty set.

The relative-density inheritance argument is also used in Tevet's Proposition 4. Non-BA failure of relative density was already proved by Akiyama's Theorem 2; the argument here derives the needed conclusion directly from the line limit.

It remains to justify every orientation of an affine line using translations only; that is the next lemma.

## 7. Sublinear index windows give physical phase freedom

For positive integers m,n one has the **exact** identity

`L_m=diag(sqrt(n/m),sqrt(m/n))*L_n`.

Consequently, if `|m_j-n_j|=o(n_j)`, these diagonal maps and their inverses tend to the identity, and L_(m_j) and L_(n_j) have the same closed-set limits. On each bounded ball this follows just by multiplying the radius by the operator-norm error; it does not require a shortest-vector lower bound.

For fixed irrational alpha, let integer window lengths `h_j -> infinity`, `h_j=o(n_j)`. For every target phase zeta on the unit circle there are `0<=b_j<=h_j` such that

`exp(2*pi*i*(n_j+b_j)*alpha) -> zeta`.

Here is the uniformity needed in this assertion. Irrational rotation has a finite epsilon-dense initial orbit segment for each epsilon>0. One elementary proof uses pigeonhole to obtain a nonzero multiple of alpha whose distance to an integer is positive and less than epsilon; successive multiples of this small positive or negative rotation form a finite epsilon-net. A sufficiently long initial orbit contains those multiples. Rotating that finite net by any starting phase keeps it epsilon-dense. Thus sufficiently long windows work uniformly in n_j, and taking successively smaller epsilon proves the assertion.

For an explicit choice, take `h_j=floor(sqrt(n_j))` and choose b_j minimizing the circular phase error over `0<=b<=h_j` (use the first minimizer if necessary). For each fixed epsilon the uniform finite-net bound eventually applies, so these errors tend to zero without assuming a rate of equidistribution. The idea of varying the center index to change the physical angle appears already in Tevet's proof of Theorem 2, part 2, p. 11; this window formulation also covers the thin regime.

Now start with a subsequence for which L_(n_j) has a line or lattice limit H in the frame coordinates. Set `m_j=n_j+b_j`. The physical centered spiral then converges, along these **actual point centers**, to `zeta H`, by the exact diagonal relation and Corollary 2.3. This is not application of rotations to the translated point sets; it is selection of indices whose physical angular phases converge as desired. Add a fixed offset to realize every affine translate. Applied to the non-BA line above, it proves every affine line is attained and finishes Theorem 2. QED.

## 8. Rational and BA boundaries

For rational `alpha=a/b` in lowest terms, `(q,p)=(b,a)` gives the horizontal lattice vector `(b/(2r),0)`. It is the primitive shortest vector for all sufficiently large n: every q not divisible by b has `|q*alpha-p|>=1/b`, hence vertical component at least `2*pi*r/b`. Thus the centered frame sets tend to the real line. The physical phases take only the finitely many values `exp(2*pi*i*a*j/b)`; all their corresponding line directions occur by taking n in fixed residue classes. Theorem 1 and recentering show these exhaust the nonempty rational-angle limits. Translations away from the finite union of rays give empty limits. Arbitrary line orientations are not claimed in this rational case.

The rational-angle classification is already recalled by Tevet on p. 2; the paragraph above records its direction restrictions explicitly.

For BA irrational alpha, the equivalent Diophantine bound is `|q|*|q*alpha-p|>=c>0` for all q!=0 and all p. Akiyama, pp. 2–3, recalls the equivalence of this all-q bound with bounded partial quotients. To connect it to the convergent condition used in §6, we give the standard bridge separately: for `q_j<=q<q_(j+1)`, the best-approximation property gives `|q*alpha-p|>=|delta_j|`, so a uniform positive lower bound on convergent products gives one for all q; the converse is immediate. Therefore every such lattice vector has

`|v|^2>=2*|v_x*v_y|>=2*pi*c`.

Vectors with q=0 have length at least `2*pi*sqrt(n)`. Shortest lengths are uniformly bounded below, so only lattice nonempty limits occur, as already known from Tevet's Corollary 5. **Akiyama, Theorem 2 (arXiv:1904.10815v2, pp. 3 and 5–7; journal 2020)** proves BA equivalence to relative density; together with the transfer argument of §6, this excludes empty BA limits. Akiyama does not state a Chabauty-limit theorem. Bacher's Proposition 6.1 states the density equivalence but leaves its proof to the reader; it is not our proof source. This final density fact is classical background, not needed for the non-BA classification proof.

A finite change to the source, including adding P_0, disappears under all escaping translations: its translated points eventually leave every bounded ball. All indexing conventions therefore agree for this purpose.

## 9. Claim/evidence/novelty ledger

| Claim | Evidence | Novelty and scope |
|---|---|---|
| Two-sided local inclusions with constants 5 and 45; covolume pi | **Certification**, explicit inequalities in §2 | Quantitative reproof/normalization of Bacher's classical local-lattice description; no new mechanism claimed. |
| Fixed-covolume limits are same-area lattices or lines | **Certification**, elementary reduced-basis proof in §3 | Classical planar lattice compactification; no priority claim. |
| Nonempty spiral limit types and exact lattice covolume | **Certification**, §§2–4 | Answers Tevet's explicit 2025 question as a consequence of classical ingredients. Bacher overlap is material; worldwide first-priority unestablished. |
| Every non-BA irrational angle realizes both nonempty types and the empty type | **Certification**, §§5–7 | Universal existence argument, not an inference from samples. Does not classify all lattice shapes for a fixed angle. |
| Rational/BA boundary behavior | **Certification/Reproduction**, §8 | Standard boundary results, with the specified imported relative-density theorem. |
| Numerical/interval cases | **Certification of the individual finite inequalities only** | Controls of implementation, indexing and constants; not evidence establishing the universal quantifiers. |

The exact published question has an explicit primary conjecture, unlike an unproved-in-project target. Nevertheless, the theorem is a transparent classical consequence of the older local-lattice framework, so it must not be described as a new technique or a blanket first solution of a worldwide open problem. This is not a proof of energy minimization or optimal cone packing from the book.

## 10. Replay and independent review

From this folder, the one-command local replay is

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venvs/phys-fractional-parentage-coefficients/bin/python code/verify.py
```

The completed research run printed:

```text
PASS: 42 interval window cases; 29368 forward and 29067 reverse points certified, no tolerance fallback.
PASS: 66 independent absolute-Cartesian comparisons.
PASS: 36 exact determinant cases, fixed-area line degenerations, and diagonal scale identity.
PASS: 2 rigorous Liouville finite witnesses; 6 negative/boundary controls detected.
PASS: 5 pinned source hashes. Universal claims rest on RESULTS.md, not these finite checks.
```

That run used Python 3.13 and python-flint 0.9.0, Arb precision 256 bits for full finite windows and 1024 bits for the two thin witnesses. Source pins added while addressing review are included in the final replay separately; they do not change the geometric calculation. The finite windows exhaust all candidate q in their stated integer bounds, including exact boundary points. Source angles are three rationals, `sqrt(2)-1`, the golden conjugate, and the Liouville constant `sum_{j>=1}10^(-j!)`. Its five-term interval truncation uses the rigorous tail bound `2*10^(-720)`. The two isolated thin witnesses use indices `10^24` and `10^120`; they are not whole-window enumerations or a proof of the limiting theorem.

Independent Cartesian controls construct absolute P_n and P_(n+q), subtract and rotate them, instead of directly using the local chord formula. Exact Fraction calculations check unimodular determinants and normalized fixed-area degenerations. Negative/boundary controls detect a missing angular factor, missing frame rotation, wrong integer lift, invalid zero source index, and strip/plane examples whose covolumes vary rather than remain fixed.

**Initial checker issue and disposition:** the first run rejected the tight radial bound at `r=12,R=1,q=25` because an upper Arb enclosure of the exact rational `25/24` exceeds a separately rounded lower enclosure of the same number. A targeted exact comparison confirmed this enclosure effect. The check now compares the rational radial coordinate with Fraction arithmetic; no tolerance was introduced and no theorem constant was weakened. The corrected complete run passed.

### Independent referee and issue-by-issue dispositions

The configured other-vendor reviewer **claude-opus-5-5 / max** ran via Claude Code 2.1.300 with safe mode, read-only tools (`Read,Glob,Grep`), no web, no delegation and no write tools. It exited 0 with `subtype=success`, `is_error=false`, no permission denials. Its untouched report is `review/claude-review.md`; raw output and frozen input hashes are retained.

Verdict: **CORRECT-WITH-FIXES**. The reviewer found **no mathematical gap in Theorems 1–2** and independently checked both local inclusions, the lattice compactification, recentering, continued-fraction realization and translation-only phase freedom. Its required fixes concern sources/attribution and exposition:

1. **Bacher Remark 1.2 omitted — fixed.** STATUS.md now records the rational degeneration and the all-irrational Voronoi-area assertion, marking that assertion as unproved in the remark. We do not infer Voronoi-cell convergence from Fell convergence alone or rely on that assertion for Theorems 1–2.
2. **YSS21 not inspected — resolved by primary reading.** The arXiv Theorem 1/Corollary 2 and the published abstract explicitly assume a **badly approximable** angle. They support the BA area result, not an already-proved non-BA classification. The source is now pinned and its hypotheses are reported in STATUS.md.
3. **Bacher relative-density proof absent — fixed.** The optional BA no-empty statement now cites the inspected Akiyama Theorem 2/proof instead.
4. **Classical precedents under-attributed — fixed.** Relative-density transfer, rational/BA boundaries, index-phase freedom and both length bounds are explicitly credited above. The reviewed manuscript already called the main argument a classical corollary; that restriction is retained.
5. **Antecedent of the p. 12 quote missing — fixed.** STATUS.md includes the preceding list in a separate extract under 40 words.
6. **Containment versus attainability wording — fixed.** The result is described as the full p. 4 containment in sharpened form, excluding the p. 12 cylinder suggestion.
7. **Standard topological/Diophantine facts implicit — clarified.** The metric equivalence, continuity under convergent affine maps, best-approximation bridge and explicit index windows/minimizers are now stated.
8. **Book excerpt and finite controls outside referee scope — boundary preserved.** The calling agent read the book excerpt, copied it byte-for-byte, and exercised the interval controls. The report is not represented as an audit of those excluded artifacts.

The review's informal “new here” wording is **not** adopted as a first-priority assertion. Its computational-picture explanation is likewise only an interpretation, not verified evidence about the author's original simulations. The proof above—not a convergence plot—is the universal argument.

### Follow-up decision and final scientific replay

The focused other-vendor follow-up **ACCEPTED** all eight dispositions, with no mathematical error in the new clarifications. It read YSS21 pp. 1–3, Akiyama pp. 1–8, Tevet pp. 1–4 and 9–13, all of Bacher, and the publisher metadata. Model **claude-opus-5-5 / max**, exit 0, success, no permission denials; untouched report: `review/claude-followup-review.md`.

Its three nonblocking wording points were applied: (R1) the no-empty consequence is attributed to the density-transfer argument, not claimed to be stated by Akiyama; (R2) our best-approximation bridge is separated from Akiyama's bounded-partial-quotient equivalence; (R3) the implication of Bacher's one-to-one description plus his asserted Voronoi-area limit is now explicit, without calling that assertion proved. The M-bound citation now points to the paragraph after Corollary 3.2. No theorem, hypothesis, code or numerical parameter changed.

The final changed-path scientific replay completed successfully in **1.29 seconds** with the same one-command invocation and the unchanged four geometric PASS lines above, followed by:

```text
PASS: 8 pinned source hashes. Universal claims rest on RESULTS.md, not these finite checks.
```

The exact command, stdout, exit 0, Python 3.13.9 / python-flint 0.9.0 versions and code/manifest/output hashes are in `results/final-replay-receipt.json`. Detailed finite outputs are `results/verification.json`. The first and follow-up review receipts preserve their distinct scopes; neither review covered the code or book excerpt. No builds, lint suites or formatters were run.
