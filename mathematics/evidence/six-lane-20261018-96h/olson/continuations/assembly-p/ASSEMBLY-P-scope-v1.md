# Frozen scope: Theorem ASSEMBLY-P (word-level D_(2p) assembly on o_F <= p, conditional on ONE-SHORT-LS and ROT-SING), v1

Owner OlsonAssemblyP. Frozen after /bin/date 2026-10-19T11:30:13-0700, BEFORE any written derivation of the assembly.
Authority: Main's assignment to OlsonAssemblyP (2026-10-19), Target 1. Status of every statement below: CANDIDATE_UNVERIFIED
target, NOT a proof and NOT a verdict. Written research only: no computation, enumeration, solver, test, build or model CLI.
All writes stay in assembly-p/; every old file is read-only.

## Definitions (exactly those of the accepted verdicts; no new notion)
- D_(2p), p odd prime, (v,e)(v',e') = (v+ev', ee'), rho_x = (x,+1), sigma_y = (y,-1) (GRX convention, lowodd verdict v2).
- Avoider: a word with no 2p letters in increasing original index order whose ordered product is the identity.
- F = number of reflection letters, R = number of rotation letters; o_F = number of ODD blocks of the maximal cyclic constant
  reflection-block decomposition; kappa(w) = p - 1 - (F - o_F)/2.
- INV*: all rotation letters lie in one set {rho_c, rho_-c} with c != 0, and every maximal cyclic reflection run is constant.
- Admissible normal form, terminal k, kappa^ = p - 1 - (F - k)/2, rotation sequence Y over C_(2p): exactly as in the accepted
  ASSEMBLY-LS proof (proof-ASSEMBLY-LS-v2.md Sec. 1, sha256 ac854c31ae1446c4710f3c19bb1beb80d8c25333aeb6b350c7f7d4dc7fafcfb3)
  read with ZX overlay 2 (existential reading). (ZP_kappa), (S1_kappa): as in EV/LS-scope-v1.md lines 10-12.

## Conditional premises (PENDING candidates; used ONLY as explicitly labelled premises, never as accepted results)
- [ONE-SHORT-LS] continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md, sha256
  c544aad2ab0cadc4c76870dc97382b6a749bbdda85f96596bdb128efe9b19ffc, statement lines 16-17: p >= 7 prime,
  floor(2p/3)+1 <= kappa <= p-2, odd Y in C_(2p), |Y| = p+2kappa EXACTLY, (ZP_kappa) => (S1_kappa). Itself conditional on the
  statement-level Lev 2022 Theorem 2 (its Sec. 11: used for every e >= 2 in its case (I)).
- [ROT-SING] continuations/terminal-p-singletons/proof-ROT-SING-v2.md, sha256
  ae5feaa1cd99aad9d2c0c35d1521ec27c3a1e5516225b102b4cb4bb793a4b1f1, statement lines 14-16, read with parent erratum
  R18/olson-ROT-SING-parent-erratum-v1.md (sha256 aad62a162f1fb25cc786ea0b96f1ceaeacf8cad8532bd16a36c15058d612d25b; commentary only):
  p >= 7 prime, avoider of length 4p-2, SOME admissible normal form with k = p and kappa^ = p-1 => rotation multiset
  rho_c^(2p-1) rho_(-c)^(p-1), c != 0.
ROT-SING+ (k = p+1) is NOT a premise of Target 1.

## Exact candidate statements
**Theorem ASSEMBLY-P (conditional on [ONE-SHORT-LS] and [ROT-SING]).** Let p >= 7 be prime.
(A) Every avoider of length 4p-2 over D_(2p) with o_F <= p satisfies INV*.
(B) Every word of length 4p-1 over D_(2p) with o_F <= p has an identity 2p-subword in increasing original index order.

**Proposition ROT-P (terminal k = p; intermediate statement, part of this candidate).** Let p >= 7 be prime and w an avoider
of length 4p-2 over D_(2p). If SOME admissible normal form of w has terminal k = p, then every rotation letter of w lies in
one set {rho_c, rho_-c}, c != 0. No hypothesis on o_F(w). It uses [ONE-SHORT-LS] only when the invoked normal form has
floor(2p/3)+1 <= kappa^ <= p-2 (narrowed further by Proposition DEP) and [ROT-SING] only when kappa^ = p-1.

**Proposition DEP (dependency refinement; part of this candidate).** In ROT-P, for the invoked normal form with k = p and
floor(2p/3)+1 <= kappa^ <= p-2, the needed (S1_kappa^) at |Y| = p+2kappa^ also follows from accepted interfaces whenever
(i) kappa^ = p-2 (accepted LS+2), or (ii) e := p-kappa^ >= 3 and p >= 10e-13 (accepted LS+ linear band), or
(iii) p = 1 (mod 3) and kappa^ = (2p+1)/3 (accepted BASE1+). Hence [ONE-SHORT-LS] is invoked only on
U(p) := {kappa : floor(2p/3)+1 <= kappa <= p-3, p < 10(p-kappa)-13, and not (p = 1 mod 3 and kappa = (2p+1)/3)}.
U(7) is empty, so at p = 7 the statements (A), (B) and ROT-P are conditional on [ROT-SING] only, with no Lev input.
(To be verified against the exact accepted statements; if any of (i)-(iii) fails at its original scope, it is withdrawn,
not repaired.)

## Trust classes to be carried (to be verified, not assumed)
- Lev 2022 Theorem 2 (statement level): through accepted ROT-LS for k <= p-1 at floor(2p/3)+1 <= kappa^ <= p-3 (p >= 11);
  through [ONE-SHORT-LS] at k = p for kappa^ in U(p) (its case (I), every e >= 2).
- S(p) (classical import at the secondary-statement trust level of the KPS-SLZ verdict item 1 with erratum M-1): through
  ROT-KP+ at k = p, kappa^ >= 2.
- Classical: index-one theorem (Savchev-Chen/Yuan), EGZ, Davenport constants incl. D(C_p + C_2p) = 3p-1, Cauchy-Davenport
  (via CT/RS/ROW inside G-LS, ONE-SHORT-LS, LS+; directly inside ROT-SING).
- Computer-assisted: record whether any is a premise of the p >= 7 chain; p = 5 is NOT claimed unless separately justified
  by citation (expected not: ROT-LS, ROT-KP+, ONE-SHORT-LS and ROT-SING are stated for p >= 7).

## Frozen route (each interface at the ORIGINAL scope of its accepting verdict, with mandatory overlays)
1. Normal form: every avoider of length 4p-2 has an admissible normal form; every one has 1 <= k <= o_F <= p.
2. k <= p-1: accepted Proposition ROT-LS (ASSEMBLY-LS verdict item 1; no o_F hypothesis; Lev cells as recorded there).
3. k = p: kappa^ integral; GRX all-plus gives kappa^ >= 0 and (ZP_kappa^); DAV gives kappa^ <= k-1 = p-1; |Y| = R = p+2kappa^.
   - kappa^ = 0 (and 1): identify the accepted interface (expected: ROT-KP item 1, k = p, kappa^ in {0,1}, p >= 5; ROT-K01 is
     stated for 2 <= k <= p-1 only). If none covers it, isolate it.
   - 2 <= kappa^ <= floor(2p/3): S1-sharp gives (S1_kappa^) with no length hypothesis; ROT-KP+ (KPS-SLZ item 3).
   - floor(2p/3)+1 <= kappa^ <= p-2: (ZP_kappa^) at |Y| = p+2kappa^ exactly; [ONE-SHORT-LS] (or the accepted cells of DEP)
     gives (S1_kappa^); ROT-KP+.
   - kappa^ = p-1: [ROT-SING].
4. (A): restricted REFL-few-odd on the original w (o_F <= p); record its caller-side obligations and where they are discharged.
5. (B): accepted ordered deletion ledger with B = p (B <= 2p-3); Case 1 (R <= 2): F - o_F >= 2p; Case 2: o_F - 1; Case 3:
   <= o_F; class o_F <= p preserved with no F condition; RGR-LONG(p) finishes.
6. Quantifier: every admissible normal form of every avoider with o_F <= p is covered, so existential criteria suffice.

## Residual description required (NOT a claim)
o_F >= p+1: rotation half at terminal k >= p+1 (and k = p when ROT-P's premises are unavailable) and the reflection half
beyond o_F <= p. Word level of length 4p-1 with o_F >= p+1.

## If an interface blocks
Write an obstruction note with the exact blocking hypothesis and the smallest missing lemma. No silent weakening, no
replacement target.

## Not claimed
Acceptance of ONE-SHORT-LS or ROT-SING; any statement at o_F >= p+1; reflection rigidity beyond o_F <= p; unrestricted INV*(p);
ordered Olson for D_(2p) or for all groups; p = 5 (unless separately justified by citation); novelty or priority; Lean;
human review.
