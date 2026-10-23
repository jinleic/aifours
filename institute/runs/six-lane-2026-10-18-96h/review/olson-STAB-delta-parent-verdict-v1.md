# Olson sequence delta: LS-II', LS-small, BASE1, LS+2, LS-lin, CT and CTgen

Recorded at 2026-10-19T06:52:35-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, relative to the exact accepted imports below. These are sequence-level written results, not a proof of unrestricted LS, LS+, STAB, INV* or ordered Olson. No finite computation or Lean verification was performed for this verdict.

## Definitions and governing texts

Y is a sequence of odd elements of C_(2p). (ZP_kappa) forbids zero-sum subsequences of even lengths from 2kappa+2 through 2p. Under this condition a long zero-sum has length at least 2p+2. Put kappa0=floor(2p/3), e=p-kappa. For the new-range LS/LS+/STAB claims below, p is prime >=7 and kappa0+1 <= kappa <= p-2 unless a narrower range is stated.

Read the [delta package](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/delta-review-package-v1.md) through mandatory [AP-prime erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-delta-APprime.md) and [consolidated delta erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-2-delta-consolidated.md) `16cc18235f4353605ebd55753de4304bcf80e5b2c18b42f6fa0c68117795cc27`. CF/AP also require the [prerequisite consolidated erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-2-prereq-consolidated.md), especially R4/R6.

## Accepted results

1. **LS-II'.** No threshold LS counterexample (odd Y of length p+2kappa+1, with (ZP_kappa) and a long zero-sum) lies in case (II) with respect to g=g0 of DGM-p. The former induction premise H'(kappa) and Lemma SH are not used; declared accepted imports still are.
2. **LS-small and Proposition I-small.** LS(p,p-2) for p>=7; LS(p,p-3) for p>=11; LS(p,p-4) for p>=13. Proposition I-small is accepted only with its own literal hypotheses and corrected AP-prime proof.
3. **BASE1 / BASE1+.** For p congruent to 1 mod3, p>=7, kappa=(2p+1)/3, an odd (ZP_kappa) sequence of length 3kappa+1=2p+2 containing a long zero-sum is exactly
   - g^(p+3)(3g)^(p-1), or
   - g^(2p-1)(cg)^3, where c=(2p+1)/3=3^(-1) mod2p,
   for an odd generator g. Any odd (ZP_kappa) sequence containing a long zero-sum has length <=2p+2. This is STAB and LS+ at these cells only; the first p congruent to 2 mod3 cell is not covered.
4. **LS+2.** At kappa=p-2, p>=7, every odd (ZP_kappa) sequence containing a long zero-sum has length <=3p-5=3kappa+1. The stated E2/E3 families attain this bound. This does not classify every endpoint extremizer (general STAB(p,p-2) is not proved).
5. **LS-lin.** For e>=3 and p>=6e-10, LS(p,kappa) holds. Together with the accepted e=2 cell, the linear band is e<=(p+10)/6, always restricted to the new kappa range above.
6. **CT.** For prime p>=5, 0<=kappa<=p-1, odd (ZP_kappa) Y, and 1<=n<=|Y| with |Y|-n even in [2kappa+2,2p], sum_x min(n,v_x(Y)) <= p+n-2.
7. **CTgen.** For prime p>=5, (p-3)/2<=kappa<=p-1, N=|Y|>=2kappa+3, odd (ZP_kappa) Y containing a long zero-sum: the involution p has multiplicity <=N-2kappa-2 and some odd generator g has multiplicity >=N-2kappa-1. At N=3kappa+2 this supplies v_g>=kappa+1 to the restricted ROW dichotomy; it is not itself a proof of LS+.

## Exact combined cells and remainder

Within the stated new range, accepted LS cells are the union of:
- e<=(p+10)/6;
- e<=4 (including the standalone LS-small cell (13,9), also BASE1);
- kappa=(2p+1)/3 when p congruent to1 mod3.

Cells not decided by this package have e>=5, p<6e-10, excluding those BASE1 cells. Examples: (p,kappa)=(17,12),(19,14),(23,16),(23,17). This describes the package's coverage, not a literature-wide open-status theorem. LS+ is accepted here only at e=2 and BASE1 cells; STAB only at BASE1 cells.

## Reviews, parent checks and import boundary

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-STAB-delta-codex-v1.prompt.stdout.txt) `ade272c4b13b0ff797bd346c7633db72ebe0278820e81ef582a6b9fb1b03e705`: observed gpt-6.1-sol, max, read-only; six main claims pass, 0 FATAL/0 MAJOR/2 MINOR.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-STAB-delta-claude-v1.prompt.note.md) `92752d227cba11b1058b7517f0971633b07fd21f483b19aea08e23f81f03fc0a`: observed claude-opus-5-5, max, no tools; all six main claims pass at stated scopes, 0 FATAL/0 MAJOR/18 MINOR (including CTgen editorial note).
- Parent read the consolidated erratum in full; all findings are disposed without strengthening a theorem. Parent separately checked CT's complement argument, CTgen's heavy-generator/even-involution deletion, LS-lin's maximal zero-sum-free core, no-wrap bound and signed first-crossing inequalities, and inspected BASE1's endpoint classification. These checks supplement, rather than replace, the two reviews.
- Accepted imports: the prerequisite CF/RS/DGM-p/ROW/dichotomy/AP verdict `ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0`, S1-sharp at its lower-range kappa0 scope, SLZ3 as a bound on the **shortest long zero-sum T**, RED, and the external index-one theorem at n=p or n=2p as explicitly pinned in the previous-round primary-statement record. The external theorem's proof was not replayed here.
- Classical-route/priority suggestions in the credit addendum remain **[INFERENCE]** context, not premises or a novelty finding. Some cells may be corollaries of known inverse zero-sum theorems; no consequential novelty delta is certified.
- LS+-RED, its later addenda and LS+-lin remain **CANDIDATE_UNVERIFIED**. This verdict discharges only their CT/CTgen/LS+2 dependencies.

## Candidate source pins

- [proof-LS-caseII-v2-addendum-1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LS-caseII-v2-addendum-1.md) `c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718`
- [proof-LS-caseI-smalldelta-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LS-caseI-smalldelta-v1.md) `2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1`
- [erratum-1-delta-APprime.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-delta-APprime.md) `e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461`
- [proof-STAB-base-p1mod3-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-STAB-base-p1mod3-v1.md) `8a41189cb8d2c254394c4ac44963d7a64f7f6ace00a9ad829f7e0af96def0985`
- [proof-LSplus-e2-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LSplus-e2-v1.md) `2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1`
- [proof-LS-lin-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LS-lin-v1.md) `434a5dfd38e3f82ef596b7c23cdf528069207e35581c573e83e1613626c19aec`
- [lemma-CTgen-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/lemma-CTgen-v1.md) `462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad`
