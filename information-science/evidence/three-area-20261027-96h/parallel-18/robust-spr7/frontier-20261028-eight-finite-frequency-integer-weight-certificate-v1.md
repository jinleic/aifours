# SPR7 counterexamples admit eight distinct finite rational-frequency, integer-weight certificates

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:13:13 PDT 2026**. **WRITTEN author-unreviewed candidate.** This is a normal form for a hypothetical negative witness, not an exhibited counterexample or an executed search.

## 1. Exact original-target equivalence

Import the COMPLETE `frontier-20261028-strict-rational-certificate-completeness-v1.md`, SHA256 `d9b42aa4609dca9b1e33bbd8bd60bd3b23f0f73f1866e1fc871b97dffb740001`, with its entire named predecessor chain, actual all-member Hurwitz prerequisite and proof that every common exact-degree-seven numerator has strictly positive coefficients. That source is an unreviewed candidate; its acceptance is not assumed.

**Theorem.** An original eligible septic box with NO common unrestricted exact-degree-seven SPR numerator exists **if and only if** there are:

- an actual monic septic independent coefficient box K with rational endpoints, all seven widths strictly positive, and every member strictly Hurwitz;
- **exactly eight distinct positive rational frequencies** `w_1,...,w_8`;
- eight indices `i_l in {1,2,3,4}` selecting the four ACTUAL parity corners of that ONE K, with repeats allowed;
- eight strictly positive integer weights `N_1,...,N_8`;

such that, for EVERY numerator monomial index k=0,...,7,

`C_k := sum_(l=1..8) N_l [b_k] Re[b(i w_l) a_(i_l)(-i w_l)] < 0`.

All C_k are rational and their signs can be checked with integers after clearing a known positive common denominator. The proof does not restrict the original numerator to any profile, coefficient box, or lower degree. The weighted coefficients are a STRICT nonpositive-cone obstruction, not an exact zero-annihilator; consequently the older endpoint requirements for five-node zero-annihilators do not apply to this certificate.

For rational K and w_l, with monic a_7=1, the actual coefficient in this formula is explicitly

`[b_k] Re[b(iw_l) a(-iw_l)]`
`= sum_(0<=j<=7; j+k even) (-1)^((k-j)/2) a_j w_l^(j+k)`.

The sign exponent is an integer; these are polynomial/rational operations only. The registered all-member stability of K is separately checkable by the named rational-box Routh/Sturm procedure. No finite-frequency point is substituted for a whole-half-line positivity proof in the original target: these frequencies are atoms in a logically sufficient obstruction.

## 2. A displayed certificate really forbids every original numerator

Suppose such K,w,i,N exist, and suppose b is an original common numerator. After positive monic normalization, the predecessor's elementary no-imaginary-crossing homotopy shows b itself is Hurwitz and **every b_k>0**. Then

`sum_l N_l Re[b(iw_l) a_(i_l)(-iw_l)] = sum_(k=0..7) C_k b_k < 0`.

Each a_(i_l) is an actual Hurwitz denominator, so its squared modulus on the imaginary axis is positive. Original strict SPR requires each of the eight left summands to be positive, contradiction. This proves the certificate implies a genuine original negative box, without appeal to any optimizer or approximate computation.

## 3. Rational finite nodes and distinctness are without loss for a strict certificate

Assume ANY original negative box exists. The imported d9 completeness theorem supplies an eligible rational, strictly positive-width box K and a positive normalized at-most-eight actual-corner certificate with rational compactified nodes `x_l in [0,1]`, rational positive weights lambda_l, and every coefficient of

`sum_l lambda_l V_(i_l)(x_l)`

strictly negative. Retain all eight strict margins; call their minimum gamma>0. The vectors V_i(x) are rational-coefficient polynomials and are continuous on `[0,1]`.

The set `{w^2/(1+w^2): w in Q, w>0}` is dense in `[0,1]`: positive rationals are dense in the positive reals; w near0 approximates x=0 and sufficiently large rational w approximates x=1. Replace each node, including any zero/infinity node, by a sufficiently close positive rational frequency via this map, keeping its same ACTUAL corner. Finiteness and continuity preserve all eight strict-negative coefficients. If two frequencies coincide, choose nearby rational frequencies independently so all are distinct; again choose them close enough to preserve strictness.

If the certificate currently has r<8 atoms, split one positive rational weight into `8-r+1` positive rational pieces summing to the original weight, initially duplicating its corner and frequency. Perturb these duplicate frequencies to distinct positive rationals in an arbitrarily small neighborhood, also distinct from the other atoms. This leaves exactly eight positive rational weights with total1 and changes the coefficient vector arbitrarily little; its eight strict signs remain negative. The same argument handles an original endpoint by first moving it to a sufficiently close finite positive rational frequency.

No claim that an **exact zero** annihilator can be perturbed this way is made: strict negativity is essential. No bound on the denominators, frequency magnitudes or perturbation radius is inferred.

## 4. Clearing positive denominators to get integer weights

For each resulting rational frequency w_l, put `t_l=w_l^2` and

`r_l = lambda_l/(1+t_l)^7`.

Each r_l is strictly positive rational. The compactified weighted vector is exactly the raw pairing coefficient vector weighted by r_l. Multiply all r_l by one common positive integer denominator M and set `N_l=M r_l`. Each N_l is a positive integer, and multiplication by M preserves all eight strict-negative signs. Every raw pairing coefficient is rational because K and w_l are rational. This is the certificate stated in §1.

Conversely, such integer weights give a normalized rational compactified certificate on dividing by a positive sum if desired. An exact verifier need only check the full-box rational Hurwitz predicate, distinct positive rational w_l, membership of each selected corner, positivity of integer weights, and the eight strict rational coefficient sums. It need not trust or reproduce a floating optimizer.

## 5. Verification boundary and remaining task

The equivalence is a written consequence of the full d9 source chain plus elementary rational density and continuity; it requires independent review of that chain, particularly d9's actual-member Vandermonde perturbation and support reduction. No selected box, numeric coefficient instance, interpreter, solver, enumeration, or strict certificate was produced in this derivation. The one-sided rational search described here is in principle complete for finding a negative box but is **not run**, and has no claimed practical complexity or termination in the positive case. The original septic synthesis question remains OPEN; no novelty, formal proof, human/configured-family acceptance or altered historical quarantine follows.

**END.**
