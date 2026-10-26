# ADDENDUM-1 to Part15: degree-plus-interpolation proof of the Theorem E determinant, and a typo in the source's displayed range-criterion identity

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 23:51:41 PDT 2026**. This note is additive to `current-consolidation-v17-part15-decisive-point-SN2-zero-slice-bob-peel-and-coordinate-peel-boundaries-v1.md` (SHA256 83597721fb22a6c8109e7155739609647e2f8d45a452ededd940aeaeff60c303), whose bytes are unchanged.

Exact WRITTEN polynomial algebra and hand arithmetic only. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## A1. The Part15 determinant m4(T) is fixed by degree bounds and three evaluations

Part15 Q5 obtained m4(T)=det(4Res_t^Γ)=-2592T^3+4248T^2-1404T, T=t^2, by symbolic cofactor expansion. Here is an independent argument that does not depend on that expansion.

**Degree.** The matrix has two 2x2 diagonal Alice blocks, Alice{0} and Alice{3}, whose entries are affine in T. Its off-diagonal Alice block has entries that are constant multiples of t. A permutation term of the determinant uses k entries from the off-diagonal blocks, with k even, so it has t-degree at most 2(4-k)+k=8-k. The determinant is therefore a polynomial in T=t^2 of degree at most 4.

**Leading coefficient.** Degree-8 terms need k=0. Their total is det of the T-coefficients of the Alice{0} block times det of the T-coefficients of the Alice{3} block, which is det[[12,12],[12,12]]·det[[10,11],[11,10]] = 0·(-21) = 0. So the T^4 coefficient is 0.

**Constant term.** At T=t=0 the |3>p row is (−t, 0, 10T, 11T) = 0, so det=0 and the constant term is 0.

Hence m4(T)=c1T+c2T^2+c3T^3, with three unknowns. Three independent direct numeric determinants, each displayed in Part15 Q5, give:
- T=1: 252;
- T=1/4: -126 (from -32256/256);
- T=4: -103536.

The linear system c1+c2+c3=252, c1/4+c2/16+c3/64=-126, 4c1+16c2+64c3=-103536 has the unique solution c1=-1404, c2=4248, c3=-2592. Check at T=1/4: -351+265.5-40.5 = -126. Check at T=4: -5616+67968-165888 = -103536.

So m4(T)=-36T(72T^2-118T+39) is proved without relying on the symbolic expansion. The same degree argument for m3, a 3x3 minor of degree <=3 with zero T^3 coefficient and zero constant term, reduces it to two unknowns. The symbolic m3=1188T^2-117T agrees with the direct value 1071 at T=1.

## A2. A typo in the source's displayed certificate identity (2509.07086v1, Theorem 5 proof)

The captured source text (`2509.07086v1.txt`, lines 954–955 in this root) prints

`psi00(g5-g3-g4) - psi02 g1 + psi20 g2 = psi00^4`

with
- g1 = psi20(psi00^2 - psi01 psi10);
- g2 = psi02(psi00^2 + psi01 psi10);
- g3 = psi20(psi01^2 - psi00 psi02);
- g4 = -psi02(psi10^2 + psi00 psi20);
- g5 = psi00^3 + psi01^2 psi20 - psi10^2 psi02 - psi00 psi02 psi20.

Each g_i was re-derived here as the stated 3x3 minor of the source matrix (11): rows (0,1,3)x cols (0,1,3), rows (1,2,3)x cols (1,2,4), rows (0,1,3)x cols (1,2,3), rows (1,2,3)x cols (0,1,4), and rows (0,1,2)x cols (0,1,2).

**Written check.**
- g5-g3-g4 = psi00^3 + psi00 psi02 psi20, so psi00(g5-g3-g4) = psi00^4 + psi00^2 psi02 psi20.
- psi02 g1 = psi00^2 psi02 psi20 - psi01 psi10 psi02 psi20.
- psi20 g2 = psi00^2 psi02 psi20 + psi01 psi10 psi02 psi20.

The printed left side therefore equals psi00^4 + psi00^2 psi02 psi20 + 2 psi01 psi10 psi02 psi20, not psi00^4. **Counterexample:** psi00=0, psi01=psi10=psi02=psi20=1 gives g=(-1,1,1,-1,0) and printed left side 1+1=2, while the right side is 0.

**Corrected identity.**

`psi00(g5-g3-g4) - (1/2)(psi02 g1 + psi20 g2) = psi00^4`,

because psi02 g1 + psi20 g2 = 2 psi00^2 psi02 psi20.

**Consequence.** Only the displayed coefficients are wrong. The ideal membership of psi00^4, and hence the source's conclusion that every Schmidt-rank-2 range vector of rho^{4x5} has psi00=0, still holds. An independent case check confirms it:
- if psi20,psi02!=0, then g1=g2=0 force psi00^2 = psi01psi10 = -psi01psi10, so psi00=0;
- if psi20=0, then g4=0 gives psi02psi10^2=0, and g5=psi00^3=0;
- if psi02=0, then g3=0 gives psi20psi01^2=0, and g5=psi00^3=0.

No owner result imported the printed identity. This is a source-text MINOR about the captured arXiv v1 text only, not a claim about any later or journal version.

## A3. Scope

No new P44 claim is made. Part15's Theorem E statement and interval are unchanged; A1 only replaces reliance on the symbolic expansion by an independent proof. Original P44 remains UNMET.

**END OF ADDENDUM-1.**
