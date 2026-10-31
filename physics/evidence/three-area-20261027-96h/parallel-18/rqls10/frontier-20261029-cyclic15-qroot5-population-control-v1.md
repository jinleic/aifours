# A simpler Q(sqrt(5)) population control for the cyclic-15 problem

**WRITTEN + EXACT-Q(sqrt(5))-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:18:20 PDT 2026. This strengthens the scope control in `frontier-20261029-cyclic15-irrational-population-control-v1.md` SHA-256 `2be67ea564df7c38820d0dee789221ed62325d1b3ce62d7ac5a341cc5c195baf`: the linear necessary conditions are feasible already over the real quadratic field Q(sqrt(5)). It does **not** construct the cross-Gram phases or any rays.

## Exact population solution

Take the six distinct U-eigenvalue exponents `(0,1,2,4,5,12)` modulo 15. Define

`X=(sqrt(5)-1)/3`, `Y=1-sqrt(5)/3`, `q=(X,X,Y,Y,X,Y)`,

`p2=p7=q/2`, and `p5_j=1/2-q_j`.

All 18 populations are strictly positive and lie in Q(sqrt(5)). Since `X+Y=2/3`, each of the three rows sums to 1, each coordinate satisfies `p2_j+p5_j+p7_j=1/2`, and the total p5 population in every exponent residue class mod 3 is 1/3. Indeed each residue class contains one X and one Y.

Let `zeta=zeta_15`, `omega=zeta^5`, `eta=zeta^3`, and `c=(sqrt(5)-1)/2=eta+eta^(-1)`. Since `Y=cX`, the p2 moment vanishes by the exact identity

`sum_j q_j zeta^(-2 a_j)`

`= X [(1+zeta^13+zeta^5) + c(zeta^11+zeta^7+zeta^6)]`

`= X omega² [(eta-1) + c(eta^4-eta²)] = 0`.

For the last equality, `c(eta^4-eta²)=(eta+eta^(-1))(eta^(-1)-eta²)=1-eta`. The automorphism `zeta -> zeta^11` fixes Q(sqrt(5)) and sends exponent −2 to −7 modulo 15, so the p7 moment vanishes as well. Strict positivity follows from `2<sqrt(5)<5/2`: `1/3<X<1/2` and `1/6<Y<1/3`.

## Scope and checks

The coordinate support is not a union of two complete 3-cycles and contains no complete 3- or 5-cycle, so the rational-support step in `frontier-20261029-cyclic15-rational-spectral-no-go-v1.md` SHA-256 `bb0d0cf314b2c7c94afddb99a3bfdfe44d7f16a28251f197e464215cf9b49ada` cannot be extended to Q(sqrt(5)) by population positivity and paired moments alone. The example is consistent with the disjoint-field obstruction: Q(sqrt(5)) is a nontrivial subfield of Q(zeta_15).

`frontier-20261029-cyclic15-qroot5-population-control-v1.py`, SHA-256 `332c00258b49c069fce7d106317a2a2132f02684b3cb44e7bcfbb54a567d91a1`, checks the moment in the exact basis `1,omega,eta,omega eta` over Q(sqrt(5)), each residue sum, and the stated positivity bounds. Its result `frontier-20261029-cyclic15-qroot5-population-control-v1.json`, SHA-256 `a30eaf0557b97cb51c9db1c4ec0e3313f2e7c6688c5021349bf0e6b7693b9531`, is **PASS** at 02:18:19 PDT. This establishes only a necessary marginal relaxation; remaining Gram orthogonality, phases, distinctness, cyclic implementation and the full QLS are not addressed. Independent review is required; no novelty or formal-kernel claim is made.
