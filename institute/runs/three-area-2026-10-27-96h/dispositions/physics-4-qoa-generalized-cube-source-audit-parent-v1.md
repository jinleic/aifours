# Parent disposition - QOA generalized cube (Proposition 4.8 / Appendix H) source audit

Observed native clock before writing: **2026-10-28T17:17:12-0700 PDT**. Owner-authorized bounded source-proof audit under [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json). Same-harness written support plus exact finite checks; not formal/kernel, human, configured-family or novelty acceptance.

## Inputs actually read by Main

| Input | SHA-256 | LF |
|---|---|---|
| Faithful P3 view (Definition 4.6, Remark 4.7, Proposition 4.8) | `39edeaabcad0db5eab28ce9110ac1afd786829d908e60d834b7075a506855658` | 38 |
| Faithful Appendix H view (complete proof, all four cases) | `9ce883e63fe9cb5ac03ac714032ca1961987fabcf511c2ea6160bba1d9e9131a` | 34 |
| Faithful P2 view (Definition 4.1 QOA, Definition 4.2, Proposition 4.4) | `6157a3bea3a8776fc8ab33a74341f0cafbbb0b57238cb10d74d2189f31158665` | 65 |
| Faithful P1 view (Definitions 2.5-2.8, Lemma 2.7) | `fc61d41f3c94d0d55353fac097124cae833ab347f36d985dd441f1becc090367` | 53 |
| Reviewer audit review-v1.md (complete, 1-140) | `00b170cac97692ea4f263dae708370e36a6adfe6a8dbbea75ec3efb3e8fe5c5e` | 167 |
| Reviewer exact checker check-exact-v1.py | `9d12390ac9d9eacd8b1fbf7c5ffc16afd415336dd7702939fdcb8b9920a12c35` | 165 |
| Parent exact checker check_qoa_cube_rows.py | `afdc8614b43eee8b52831af1ee275ffa6ca907bace67860444b5d5e85ec733ae` | 101 |

The faithful views emit every MathML alttext once from the pinned public HTML (source SHA-256 `9b5efb907f2172be70c7d463a8bbbbc25e63e9a1a7654d7e9015b988a34d724e`); no expression was evaluated by the view builder.

## Findings adopted at exact scope

1. **Existence equivalence holds.** For fixed address bases on three parties and fixed physical output factors, `sum_{r,s} Tr_{S^c}|phi_r><phi_s| = I_{d^3}` for every three-party set S (Definition 4.1 with r=d^3) is equivalent to equations (15)-(22) of Definition 4.6 for the conditional vectors `psi_{ijk} = (<ijk| tensor I) Phi`, `Phi = sum_r phi_r`. Main checked the block identity (2) of the review (surviving address coordinates A, surviving outputs B) and the case count 1 + 3t + 3C(t,2) + C(t,3) = C(t+3,3). The converse is constructive: rows `|ijk> tensor psi_{ijk}`.
2. **MINOR (source rendering): three Appendix H trace subscripts are dimensionally wrong** (case 3 twice: `t-1` should be `t-2`; case 4: `t-2` should be `t-3`). Main confirmed the subscripts in the faithful view (case 3 writes `Tr_{l_1,...,l_{t-1}}` while retaining two output parties; case 4 writes `Tr_{l_1,...,l_{t-2}}` after tracing `t-3`). The corrected expansion proves the statement.
3. **MAJOR (source wording, not mathematics of Proposition 4.8): the literal one-to-one correspondence between QOA row arrangements and generalized cubes is false.** Two independent exact witnesses: (a) parent, d=5, six parties, 125 orthonormal computational rows of the extended quadratic-evaluation code; all 20 three-party marginals are exactly I_125; replacing two rows by the Gaussian-rational unitary mix with coefficients (1+i)/2, (1-i)/2 keeps all rows orthonormal, keeps the coherent sum and the address-conditioned cube exactly, and changes the two rows (checker state EXACT_FINITE_CHECK_PASSED, run 17:0x PDT, exit 0); (b) reviewer, d=8, seven parties, three rows mixed by the real orthogonal matrix [[2,-1,2],[-1,2,2],[2,2,-1]]/3 with all row and column sums 1 (Main verified orthogonality and the sums by hand). Hence a bijection exists only after quotienting arrangements by equality of coherent sums; the source does not state that quotient.
4. **MINOR (definition convention): Definition 4.1 depends on row vector phases, not rays**; the review's sign-flip example shows the three-address reduction becomes diag-like with values 1/9, 25/9, 1/9. Interpreting the printed kets as phase-fixed vectors resolves this.
5. **Target-relevant negative result (exact, d=8):** a 3-uniform seven-party state whose fixed-plane generalized four-square array has every cell of Schmidt rank 8 across each physical output versus the other three; so generalized QOA/GMOQLC existence does not by itself give an ordinary product-valued four-MOQLS(8). Main verified the Lagrange coefficient `(z_s+1)(z_s+alpha)/alpha != 0` (character 2 form of the basis polynomial at 0), the Vandermonde invertibility of any three evaluation points for degree <= 2, the unitarity of the additive-character Hadamard, and the permutation/Schmidt argument. The classical seed (a=0 plane) gives four classical ordinary Latin squares from one computational ONB: not a nonclassical witness.

## Parent replay of the reviewer checker

Command: `python3 -B check-exact-v1.py` in the audit directory, exit 0, finished 2026-10-28T17:14:41-0700 PDT. Observed: q7 source Example 4.9 35/35 exact triple reductions = I_343 (exact in Z[z]/(Phi_7)); q8 classical seed 35/35 strength-three projections bijective, a=0 plane gives four Latin squares and 6/6 orthogonal pairs; q8 transformed state 35/35 exact triple reductions = I_512; x=0 plane 64/64 cells mutually orthonormal and 256/256 one-output marginals equal I_8/8.

## What this does not establish

No ordinary nonclassical four-MOQLS(8) witness or no-go; no whole-paper status, priority or novelty judgment (NR); no claim about other address bases (the inverse address Hadamard returns the classical seed). The physics-4 registered target and its written-supported five-family classicality are unchanged. This disposition supersedes the earlier P1/P2 square-only parent scope ([source disposition](../source-screens/qoa-ordinary-square-source-correspondence-parent-v1.md)) by adding the cube scope; it does not alter that record.
