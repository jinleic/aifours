# Review package UH-CONSTRAINTS: upper-half k=p+1 partial result and exact remaining obstruction, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T13:48:10-0700. CANDIDATE_UNVERIFIED written mathematics; outcome O3, NOT a proof
of UH-EXCL. Parent owns two-family reviews and verdicts. No model CLI, scientific computation, enumeration, solver, test/build,
Lean or paid API was run. No novelty, priority or human-review claim.

## 1. Review exactly these frozen texts

- proof-UH-CONSTRAINTS-v1.md, SHA256 56327b678bf9f7fe62d6f518499ab692f00897a3ecff2c62ddecac4a42a5115c,
  whole file lines 1-266, 23,987 bytes. Interfaces/scopes in Sec. 9.
- obstruction-UH-EXCL-v1.md, SHA256 f2f1a232c98b3ef6eb45fa0486912bd54170521e5adc00e09c436b1fb8c7849d,
  whole file lines 1-138, 11,368 bytes. It explicitly does not claim the original target and retains failed-route arithmetic.
- Scope UH-EXCL-scope-v1.md, SHA256 6ff7fec519944d57c3162f45e1b19403b12a8bea19647634dc86ba20e03d15e9,
  lines 1-50, 4,490 bytes; frozen 13:08:38 before derivation, with generic-plan-only pre-freeze disclosure.

FULL antecedent for ALL results: prime p>=7, (p-1)/2<=kappa<=p-3, an avoider w of length4p-2 over D_(2p), SOME admissible NF
u with terminal k=p+1,kappa^=kappa; odd blocks with H=e-1 arbitrary across blocks, e=p-kappa, and every empty run separates
different reflection values. No o_F, reflection-rigidity or nonempty-run hypothesis. All multiset conclusions retain this
antecedent; there is NO multiset-only exclusion outside the word/NF class.

## 2. Exact claims, not the requested full exclusion

(A) THEOREM UH-A. Re-proved pairing gives a common nonzero dominant class {a,-a}. Orient A=v_a(X)>=A'=v_(-a)(X), b=R-A,
delta=R-A-A'. Under the full antecedent:
  A>=2kappa+3, A<=2p-1, A'<=kappa, p-2e<=b<=p-4, 0<=delta<=p-2.
Thus the subcase A<=2kappa+2 is excluded uniformly over the WHOLE kappa interval. No entire kappa cell is claimed excluded.
(B) Lemma MW: every non-constant pattern satisfies the exact multi-length omitted-letter count inequality when q>=1,s!=0.
(C) Proposition SH: if 3e<=p+2, a run has alpha_h-beta_h>=p+1+delta, every set avoiding it is ordinary-low, >=2 runs empty.
This is necessary structure, NOT an exclusion band.
(D) Proposition L, with EXPLICIT EXTRA PREMISE delta=0: low arcs have exact allowed intervals, and their integer lifts add
along a path all of whose consecutive subarcs are low. No rigidity result is imported to supply delta=0.
(E) Corollary PH: pure rotations PLUS a run with >=p letters are impossible. The pure case with all runs<p is NOT closed.
(F) Lemma E and obstruction Sec. 4: precise empty-negative-side subset-family exclusions, with both occurrence/filler bounds.

Remaining: A=2kappa+c with 3<=c<=2e-1 (b=p-1-c). No word witness is supplied. Obstruction Sec. 2 gives the exact remaining
word-level claim R-UH; Secs. 3-5 say where the attempted routes stop. The lower kappa range is untouched.

## 3. Manifest, trust and byte boundary

Use review-excerpts-UH-CONSTRAINTS-v1.json SHA256 26fc165c2f755b0a84d9eb28b055d8cdebdfcb39c7775f82ad5f94b5878bd226
(3,871 bytes), a JSON list {path,sha256,start,end}. Each SHA256 is of the WHOLE file, ranges inclusive LF line numbers.
16 ranges from 14 files; selected raw bytes 60,355; adding LF-number prefixes gives 63,083. With this package and manifest the
embedded material remains below 100,000 bytes. No whole-file bytes outside the specified ranges need be inlined.

Accepted interfaces ONLY: NF (ROT-few-E-v4 28-43, empty-run rule at38, lowodd item2/M1/M4, fewodd addendum1 line12 and ZX
overlays1-3); GRX (notes-GRX7-20, lowodd item1/M2, every representation and sign pattern, empty runs allowed); RS(b)
(proof-ROW16-27 plus R5 at erratum36-38, integer K>=0/nonzero terms); classical Cauchy-Davenport stated at proof-ROW4-5.
CT was allowed but is not needed. No outside theorem is hidden in a lemma or ancillary route.

Context-only excerpts of proof-ROT-PP1-v2 and its notation erratum show which arguments were re-derived (M/P/U and ordinary
window/route counts). They are NOT premises. Neither the old ROT-PP1/TOP, PP1-EXCL or KP2-EXCL argument nor any source code is
imported. Status note: Main subsequently accepted PP1-EXCL under its exact NF antecedent; the proof header's grouped label
"pending PP1-EXCL" is stale administrative context only. PP1-EXCL is not used at all. RPdelta, ASSEMBLY-P, REFL, RGR-LONG/RUNS,
S(p), Lev, (S1), LS-family statements are not premises, whatever their separate current statuses.

## 4. Argument map and hostile-review focus

1. SR (proof Sec.1): delta_GRX=p+1-Phi, C_max=Phi+2H; independent block-pair capacities realise every even C in that interval.
   n even in [max(0,2kappa+2-2m),min(2p-2m,R)]. Arbitrary H distribution preserved.
2. M/P/U (Sec.2, RE-DERIVED): q=p-1 unequal pairs; n=max(p-1,2kappa+2-2m); 0<=n-p+1<=2kappa-p+1 actual fillers. Uniqueness
   since 2(2kappa+1)>R. Repeated reflection value arc with n=2kappa rules out a=0. A'<=kappa, A<=2p-1 via all-plus.
   W thresholds lambda=p-2-b, Lambda=2kappa+1-A'; g=p-2e+3+delta. Heavy-run and two-high-set bounds are conditional.
3. UH-A (Sec.3, NEW): b>=p-3 gives a high h. b>=p-1 fails from light sets/lambda<0. b=p-2 has A<2Lambda, hence two empty
   runs. At b=p-3 either light sets give two empties, or equality A=2Lambda forces A'=kappa, delta=e-3, a-letters in at most
   two runs and -a letters in ONE outside run, leaving >=kappa+1 empties. Then:
   - b=p-2: M singleton, n=2kappa free and n=2kappa+2=A+1 permits every NONEMPTY minority subset, forcing
     tau=-(2e-2)a,M={2a}; the pair at n=2kappa forces 2(e-1)=0 modp, impossible.
   - b=p-3: M has <=2 elements; all-plus and two single-empty free lengths force tau=-2a; a pair at free n=2kappa+2
     forces 4a=0 or2a=0. Verify m=2 upper bound 2kappa+2<=2p-4 from e>=3.
4. MW (Sec.4, NEW): even omission K in [max(w0,K_min),min(phi,K_max)], K_min=max(0,p-1-2e+2m), K_max=p-3+2m.
   Every subset of the minority can be omitted with K-|J| distinct dominant fillers because w0<=K<=phi. Attained set
   D-s calK-G_s; RS(b)+CD gives min(p,w0+q). q=0 and s=0 are explicitly excluded from the inference.
5. SH (Sec.5, NEW): at m=e, either q=e or q=kappa+1-ceil(w0/2). Under 3e<=p+2 the latter branch conflicts with w0<=2e-3;
   hence phi>=p+kappa. Audit the explicit single-toggle path from P0={0,2,...,2e-2} to its complement, all m=e. A low->high
   jump has gap p+1+delta, deletion impossible as beta_i<=kappa; addition gives h. A disjoint ordinary-high set then exceeds A.
6. L and PH (Sec.6, NEW): exact union of signed +-a selection intervals gives [kappa-epsilon,U]. Complement lifts lie in
   [U+1-p,kappa-epsilon-1], possibly NEGATIVE. For appended arcs the lift difference D is in pZ and -p<D<p. PH uses only the
   case all rotations a, kappa=(p-1)/2, alpha_h>=p: D(P)=X(P)+alpha(P)/2>=-1/2 and empty lifts>=1, contradicting run count.
7. Empty-run residual (proof Sec.7, obstruction Sec.4): keep |J|<=n AND n-|J|<=A. Check the qualified j=-1 length for two
   nonadjacent empties at the bottom endpoint. No assertion that two empty runs alone exclude every c>=3 is made.

Endpoints: p=7; bottom kappa=(p-1)/2 (R=2p-2, alternating m=(p+1)/2 permits n=0); e=3; all H in one block versus distributed;
a=0 only in the ruled-out Lemma U branch; rho_0 among deviants; empty runs, adjacent versus separated empties; s!=0 and q>=1
in MW; delta=0 as an explicit premise in L. Check new/re-derived labels separately from mathematical correctness.

## 5. Review boundary and retained failed routes

Judge A-F at precisely their stated scopes. Do NOT return a verdict accepting UH-EXCL as proved: it remains the missing target.
Check obstruction Sec.6's corrections to exploratory checkpoint sketches (wrong U, overstrong "iff" for delta bound, and
unproved forced-cardinality shorthand); these are not premises of the candidate. No old file was changed. No claim is made
about reflection rigidity, INV*, o_F assembly, full ordered Olson, p=5, novelty/priority, human review or Lean.
