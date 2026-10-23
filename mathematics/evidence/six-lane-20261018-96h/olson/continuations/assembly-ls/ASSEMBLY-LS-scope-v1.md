# Frozen scope: Theorem ASSEMBLY-LS (word-level D_(2p) consequence of the accepted LS-ALL), v1

Owner OlsonAssemblyLS. Frozen after /bin/date 2026-10-19T09:53:20-0700, BEFORE any written derivation of the assembly.
Authority: Main's assignment to OlsonAssemblyLS (2026-10-19). Intended use recorded before LS was proved:
evidence/LS-scope-v1.md lines 16-17 (sha256 80ae8041118d68f4c1417a67a2891ceaceeba181a375b29dfd73820957cfddfa).
Status of every statement below: CANDIDATE_UNVERIFIED target, NOT a proof and NOT a verdict. Written research only: no
computation, enumeration, solver, test, build or model CLI. All writes stay in this directory; every old file is read-only.

## Definitions (exactly those of the accepted verdicts; no new notion)
- D_(2p), p odd prime, (v,e)(v',e') = (v+ev', ee'), rho_x = (x,+1), sigma_y = (y,-1) (GRX convention, lowodd verdict v2).
- Avoider: a word with no 2p letters in increasing original index order whose ordered product is the identity.
- F = number of reflection letters; o_F = number of ODD blocks of the maximal cyclic constant reflection-block decomposition
  (each maximal cyclic reflection run split wherever its value changes); kappa(w) = p - 1 - (F - o_F)/2.
- INV*: all rotation letters lie in one set {rho_c, rho_-c} with c != 0, and every maximal cyclic reflection run is constant.
- Admissible normal form: any terminal word of the accepted PM*/fusion process (proof-ROT-few-E-v4.md Sec. 0), read with
  ZX overlay 2 (existential reading). Terminal block count k, kappa^ = p - 1 - (F - k)/2, rotation sequence Y of the
  values Y(x) = (1,x) in C_2 x C_p = C_(2p) over the rotation letters.
- (ZP_kappa), (S1_kappa): as in the LS definition, LS-scope-v1.md lines 10-12.

## Exact candidate statements
**Theorem ASSEMBLY-LS.** Let p >= 7 be prime.
(A) Every avoider of length 4p-2 over D_(2p) with o_F <= p-1 satisfies INV*.
(B) Every word of length 4p-1 over D_(2p) with o_F <= p-1 has an identity 2p-subword in increasing original index order.

**Proposition ROT-LS (terminal form; intermediate statement, part of this candidate).** Let p >= 7 be prime and w an
avoider of length 4p-2 over D_(2p). If SOME admissible normal form of w has terminal 1 <= k <= p-1, then every rotation
letter of w lies in one set {rho_c, rho_-c}, c != 0. No hypothesis on o_F(w).

**p = 5.** Not claimed as an LS consequence. To be decided in the proof by citation only: if the accepted p=5 lift verdict
already gives (A)/(B) at p = 5, o_F <= 4, a union corollary for p >= 5 may be recorded with that verdict's separate
(computer-assisted finite) trust class. No new p = 5 argument is part of this candidate.

## Trust class to be carried
- G-LS is conditional on Lev 2022 Theorem 2 (statement level) for e = p - kappa >= 3. The assembly inherits that condition
  exactly in the cells floor(2p/3)+1 <= kappa^ <= p-3 (nonempty only for p >= 11); cells kappa^ <= floor(2p/3) use
  S1-sharp and kappa^ = p-2 uses the e = 2 block, both Lev-free. To be verified, not assumed.
- Classical and accepted transitive imports keep their own scopes; transitive computer-assisted imports are disclosed.

## Frozen route (each interface checked at the ORIGINAL scope of its accepting verdict, with mandatory overlays)
1. Normal form: existence; same length, F and rotation multiset; 1 <= k <= o_F, k = o_F (mod 2); even-block end impossible;
   kappa^ integral; GRX gives kappa^ >= 0 and (ZP_kappa^) for k >= 2; DAV gives kappa^ <= k-1 <= p-2 when k <= p-1.
2. Length: |Y| = R = 2p + 2kappa^ - k >= p + 2kappa^ + 1 iff k <= p-1; then LS-ALL at (p, kappa^) gives (S1_kappa^).
   Check LS-ALL's domain (prime p >= 5, integer 0 <= kappa <= p-2, odd elements of C_(2p)) and record which block is used.
3. k = 1: Proposition K1 (c != 0). 2 <= k <= p-1, kappa^ = 0: ROT-K01 (ROT-FB(a) needs kappa^ >= 1; isolate if K01 fails).
   2 <= k <= p-1, kappa^ >= 1: ROT-FB(a) with (S1) from step 2.
4. Decide whether the ZX terminal criterion (3k <= 2p+1) or any other accepted step still restricts k.
5. Restricted REFL-few-odd (o_F <= p) for (A).
6. Ordered deletion ledger (Cases 1-3) preserves o_F <= p-1 and feeds (A); RGR-LONG(p) gives (B).
7. Quantifier: show every admissible normal form is covered (so the existential criteria apply); state residual quantification.

## Residual description required (NOT a claim)
- o_F = p: terminal k = p, the ROT-FB(b)/ROT-KP+ hypotheses and the one-short LS length p + 2kappa^.
- o_F > p: reflection rigidity beyond o_F <= p, and terminal k >= p.

## If an interface blocks
Write an obstruction note with the exact blocking hypothesis and the smallest missing lemma, with a proof attempt where
reachable. No silent weakening, no replacement target.

## Not claimed
LS+, STAB, unrestricted INV*(p), ordered Olson for D_(2p) or for all groups, any statement at o_F >= p, novelty or priority,
Lean, human review.
