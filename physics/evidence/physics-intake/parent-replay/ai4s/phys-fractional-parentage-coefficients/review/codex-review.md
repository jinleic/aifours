1. **Critical — [code/brauer_residues.py:62](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/code/brauer_residues.py:62), `tame`; RESULTS §D “Certification”; README “All arithmetic is exact.”**

   The residue calculation uses floating point. Python evaluates `(-1) ** negative_integer` as a float, which contaminates the subsequent SymPy arithmetic.

   Concrete failure: for \(k=6\), the generator \(v+\tfrac12\), at \(v=-\tfrac12\), has valuations \(1,-1\). The correct tame symbol is
   \[
   \frac{32768}{800415},
   \]
   whose square class is **30**. The implementation returns **11799795063484930**, the square class of a rounded binary approximation. I found incorrect generator residues in every listed family.

   **Fix:** use `sp.Integer(-1) ** (a*b)` or an integer parity calculation; assert that no `Float` enters residue arithmetic; check reciprocity for every generator, not only the base algebra; regenerate the certificates.

   An independent exact recomputation still gives an inconsistent residue system for all five families. Thus the bounded obstruction survives correction, but the supplied computation does not certify it.

2. **Major — [RESULTS.md:113](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:113), §B, paragraph following the table; also the newly added §B′ “all N” conclusion.**

   The five reduced CFPs do **not** provide every CFP of these parents at arbitrary \(N\). They determine the \(v\to v-1\) branch. The \(v\to v+1\) branch requires reverse reduced CFPs whose higher-seniority parent can have deficit as large as \(k+2f\).

   There is a concrete counterexample to the claimed all-\(N\) Bao–Li form. For spin 2, take the \(k=2\) parent, \(N=v+2\), and the trio-first daughter with seniority \(v+1\), deficit 6. Combining A with C gives
   \[
   c^2=
   \frac{294(4v-1)}
   {(v+2)(2v+3)(2v+5)(18v^2+127v-81)},\qquad v\ge5.
   \]
   The quadratic is irreducible. At \(v=6\), direct polynomial computation gives \(1127/451860\), agreeing exactly.

   **Fix:** restrict B’s conclusion to the five reduced CFPs and their \(v\to v-1\) extensions. Claim complete all-\(N\) formulas only after supplying every required reverse coefficient. The same logical limitation applies to B′.

3. **Major — [RESULTS.md:207](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:207), §D “Setting.”**

   The displayed normalization does not match the code. The text calls \(y_d\) normalized and defines \(b_d\) as the full Fock overlap. The code uses an **unnormalized rational covariant** and factorial-scaled overlaps and norms. As written, the displayed identity has incorrect factorial factors, and \(b_d(x)\) need not belong to \(\mathbb Q(v)\).

   **Fix:** explicitly define
   \[
   b_d(x)=\frac{\langle x,z_\mu y_d\rangle_F}{(v-k)!},
   \qquad
   n_d=\frac{\langle y_d,y_d\rangle_F}{(v-1-k')!},
   \]
   with \(y_d\) unnormalized and rational, and set
   \[
   C_d=\frac{(v-k)!/(v-1-k')!}{w_\mu n_d\,v\,CG^2}.
   \]
   Then \(c^2=b_d(x)^2C_d/q(x)\) is correct. For \(b_d(x)\ne0\) and \(C_d\in L_T\), the square-class reduction is valid. The subsequent representation statement should be phrased existentially: **some such \(x\) exists iff \(q\) represents an element of \(L_T\)**.

   The quaternion criterion itself is correct:
   \[
   q\simeq\langle a,\Delta/a\rangle\simeq\langle a,a\Delta\rangle,
   \qquad
   q\text{ represents }c\iff(ca,-\Delta)\text{ splits}.
   \]

4. **Major — [RESULTS.md:222](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:222), §D optimality statement and proof; README “Key formulas.”**

   The bounded theorem does not establish unrestricted quadratic-factor optimality. Excluding square classes supported on \(T\) leaves open a norm consisting entirely of linear factors with a root **outside \(T\)**. Such a vector could have zero nonlinear factors.

   The supplied formulas do establish the attainable upper bound: each nonzero \(k=6\) coefficient into a multiplicity-free daughter has one quadratic factor. The discriminant \(21961\) correctly proves its irreducibility. The unrestricted lower bound remains unproved.

   **Fix:** say “the trio-first basis attains one quadratic factor.” State minimality only within an explicitly restricted comparison class whose odd linear support lies in \(T\), or make unrestricted minimality conditional on completing the rational-point analysis.

5. **Major — [RESULTS.md:340](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:340), §G(1); [STATUS.md:81](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/STATUS.md:81), §5; README multiplicity verdict.**

   “Bao–Li-type forms cannot exist … once multiplicity appears” exceeds D’s scope. D concerns five particular two-dimensional families, rational directions, and a bounded \(T\). It says nothing general about higher multiplicities.

   Nor does the original CFP problem require a **canonical non-rational basis**. A specified rational basis with algebraic CFPs containing nonlinear factors remains a legitimate closed-form solution. The obstruction excludes one restricted product ansatz, not closed forms generally.

   STATUS’s unrestricted “decidable problem” wording also outruns the demonstrated finite search.

   **Fix:** repeat all three restrictions in the summary claims. Describe the unresolved objective as obtaining uniform formulas in a specified basis; qualify decidability by the finite permitted support.

6. **Minor — [RESULTS.md:218](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:218), §D theorem and “Scope and limits.”**

   “Rational orthonormal basis” and “normalized rational vectors” are not interchangeable. The intended class consists of rational **directions**, followed by normalization, which generally introduces square roots. Literally requiring unit vectors over \(\mathbb Q(v)\) makes the statement vacuous once representation of 1 has been excluded.

   The scope sentence excluding coefficients involving square roots also appears to exclude the unavoidable normalization of the bases being studied.

   **Fix:** define the class as orthogonal rational covariant directions \(x_i\), with physical states \(x_i/\|x_i\|\). Distinguish this normalization from an algebraic change of direction between covariants.

7. **Minor — [RESULTS.md:49](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:49), §A hypotheses and proof (iv); §E1 “any normalized” scalar state.**

   The signed reverse relation assumes a real harmonic basis. Condon–Shortley conventions fix ladder phases but do not prohibit independent complex phases or complex multiplicity rotations. Hermitian adjointness generally relates the forward coefficient to the **complex conjugate** of the reverse coefficient.

   Likewise E1’s weight should be \(\sum_\alpha |c_\alpha|^2\) for an arbitrary normalized scalar state; plain squares are phase dependent.

   **Fix:** impose real harmonic bases explicitly throughout the signed formulas, or insert the required conjugations and modulus squares. The existing real-basis signs, including the spin-1 pair-phase conversion, are consistent.

8. **Minor — [RESULTS.md:91](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:91), §§A–C domain statements; claims-at-a-glance C.**

   Several qualifications reside only in code or output files. A’s dimension formula requires \(f\ge1\); one-body CFPs require \(N\ge1\); absent seniority branches must be discarded.

   B’s five rows start respectively at \(v=2,3,3,3,4\). C’s certified domain is
   \[
   v\ge\max(k,k'+1,1),
   \]
   rather than every small seniority at which an individual state happens to exist. Below this range multiplicities can drop—for example, the \(k=6\) family contains a scalar at \(v=3\), rather than a two-dimensional block.

   C also supplies rational functions for **\(r^2\)**, with signs; \(r\) itself is generally algebraic. Its two bases are specified conventions, rather than intrinsically canonical bases.

   **Fix:** state these domains and change C’s summary to “squared reduced CFPs in two specified Gram–Schmidt bases.” Within the stated stable domains, I found no hidden degeneration: both symbolic reruns reported no exclusions or sign exceptions, and the harmonic projector is correct.

9. **Minor — [RESULTS.md:215](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:215), §D definition of \(T\).**

   The assertion that every formula in B–C uses only linear roots in this fixed \(T\) is false for unrestricted spin \(f\). For example, \(2fv-2f-1\) at \(f=17\) has root \(35/34\), outside both parts of \(T\).

   **Fix:** restrict this sentence to the relevant **spin-2** formulas and the transcribed Pan entries. D’s spin-2 proof does not require the general-\(f\) assertion.

10. **Minor — [RESULTS.md:306](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:306), §E2 evidence; README low-spin verdict.**

    The count is accurate but its description is inaccurate. The rerun’s 800 agreements comprise **742 individual CFP checks across 26 product formulas**, plus **58 checks of two block-weight formulas**. The product formulas have 27–30 checked seniorities, not 19–28.

    Two of the 26 formulas are already established: E1 and the scalar-to-spin-2 unit weight. Thus “26 formulas conjectured” overcounts the conjectural content. One block formula follows from completeness, so its checks are not independent of the other checks and completeness.

    The daughter block is only one-dimensional at \(v=4\), becoming two-dimensional at \(v=7\).

    **Fix:** report these counts and boundary qualifications explicitly. Retain the conjecture label for the unproved infinite extensions.

11. **Minor — [code/verify_bottom_conjectures.py:85](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/code/verify_bottom_conjectures.py:85), verifier termination; [code/compare_pan2014.py:86](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/code/compare_pan2014.py:86), Table IV comparison; RESULTS claim F.**

    Both comparison scripts can print disagreements and exit successfully. The conjecture checker also lacks an assertion that every intended formula received its expected coverage. Consequently the README’s `&&` command is not a reliable acceptance check.

    “Certification of the implementation” also overstates what finite tests, some using sampled input polynomials, establish.

    **Fix:** assert zero disagreements, full expected coverage, and all eight Table IV agreements. Label F “exact validation on the stated cases,” reserving certification for proved identities and symbolic certificates.

12. **Minor — [STATUS.md:51](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/STATUS.md:51), §§3–4 citation and novelty wording.**

    “Explicitly open (primary text)” includes a secondary report and a failed-search conclusion. “Every published closed form” exceeds the evidence actually identified, which is principally Pan’s chosen \(k=6\) basis.

    **Fix:** distinguish historical primary-source statements, secondary reports, and search results; narrow the universal publication claim to the surveyed sources. Add precise version/page locations where practical.

    I detected no definite bibliographic error from the supplied local material. The known/reproduction labels for A’s mechanism and Pan’s coefficients are appropriate. The primary papers are absent from the permitted directory, so the `[read]` history and current literature completeness cannot be independently audited here; I found no basis for accusing those labels of dishonesty.

13. **Minor — [RESULTS.md:336](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:336), newly added §F′.**

    “At most five intermediate spins” is the spin-2 bound. General integer \(f\) permits up to \(2f+1\) intermediate spins, with an additional sum over multiplicity labels.

    **Fix:** state the general bound and identify five as the spin-2 specialization. Availability of the recoupling formula alone does not supply missing one-body closed forms.

The mathematical residue framework is otherwise sound for the listed inputs: constants contribute at odd valuations, even-valuation places must retain unit residues, infinity is treated with uniformizer \(1/v\), and the listed nonlinear residues are squares. Vanishing residues would still leave a possible constant Brauer class; the no-go argument correctly needs only necessity when no candidate survives.

Read-only reruns reproduced the 462 self-tests, 74 first-quantized checks, B’s 200 checks, E1’s 19 checks, C’s 769/585 comparisons, Pan’s 14/14 and 8/8 comparisons, and E2’s 800 agreements. The bounded rational-point search reproduced no extra places for \(k\le10\), and only \(s=2\) for \(k=11\). Corrected exact residue calculations retained the obstruction in all five families.

| Claim | Verdict |
|---|---|
| A | **Accept with fixes** — explicit domains and real-phase hypothesis. |
| B | **Accept with fixes** — five reduced formulas accepted; all-\(N\) Bao–Li conclusion rejected. |
| C | **Accept with fixes** — squared formulas, stable domains, and specified bases. |
| D | **Reject as written** — bounded core survives correction; supplied certificate and unrestricted optimality need repair. |
| E1 | **Accept with fixes** — formula and proof sound; use modulus squares for arbitrary states. |
| E2 | **Accept with fixes as a conjecture** — exact evidence confirmed; counts and boundaries need correction. |
| STATUS | **Accept with fixes** — narrow the obstruction, decidability, and literature-scope statements. |