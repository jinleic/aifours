# Review package: Theorem ASSEMBLY-LS (word-level D_(2p) consequence of LS-ALL on o_F <= p-1), v1

Owner OlsonAssemblyLS. Frozen after /bin/date 2026-10-19T10:11:06-0700. CANDIDATE_UNVERIFIED; for p >= 11 CONDITIONAL on the
statement-level external Lev 2022 Theorem 2, exactly as inherited from G-LS (e = p-kappa >= 3 cells). No computation, model
launch, novelty, priority, Lean or human-review claim. The parent owns reviews and verdicts.

## 1. Review exactly this candidate
WHOLE proof: proof-ASSEMBLY-LS-v2.md, sha256 ac854c31ae1446c4710f3c19bb1beb80d8c25333aeb6b350c7f7d4dc7fafcfb3, lines 1-263
(30,115 bytes). v1 (b308e20d5c9ddc42dbfd94636461acb67e171e6aee74e2ea663eaf2f5aa8ff2d) is a preserved, never-sent draft that
differs only by one citation line number (BAL-full overlay 5 is line 33); do not review v1.
Frozen scope, written BEFORE derivation: ASSEMBLY-LS-scope-v1.md, sha256
53be77405c8b1369dfbde986a090350829a00cf2a83c3749fb7e87ff09c172a1 (09:53:20).
Statements (copied from the proof, Sec. 0):
- Theorem ASSEMBLY-LS. Let p >= 7 be prime. (A) Every avoider of length 4p-2 over D_(2p) with o_F <= p-1 satisfies INV*.
  (B) Every word of length 4p-1 over D_(2p) with o_F <= p-1 has an identity 2p-subword in increasing original index order.
- Proposition ROT-LS. p >= 7 prime, w an avoider of length 4p-2: if SOME admissible normal form of w has terminal
  1 <= k <= p-1, all rotation letters of w lie in one {rho_c, rho_-c}, c != 0 (no o_F hypothesis).
- Remark P5. p = 5 is NOT an LS consequence: (A)/(B) at o_F <= 4 are items 1-2 of the accepted p5-lift verdict
  (computer-assisted C5). Only the UNION with that verdict gives p >= 5, trust classes kept apart.
o_F counts ODD blocks of the maximal cyclic constant reflection-block decomposition, exactly as in the accepted verdicts.

## 2. Coverage and trust accounting (not an extra claim)
| Block | Status |
| --- | --- |
| p >= 7, o_F <= p-1 | Candidate (A), (B). Every admissible normal form has 1 <= k <= p-1. |
| kappa^ <= floor(2p/3) | (S1) from S1-sharp (no length hypothesis); no Lev input. |
| kappa^ = p-2 | G-LS with e = 2; no Lev input. All new cells at p = 7 are of this kind. |
| floor(2p/3)+1 <= kappa^ <= p-3 | G-LS with e >= 3: conditional on Lev 2022 Theorem 2 (statement read by parent, proof not replayed). Nonempty only for p >= 11. |
| kappa^ = 0 / k = 1 | ROT-K01 / Proposition K1 (no LS needed). |
| p = 5 | Citation union only (Remark P5). ROT-FB is accepted only for p >= 7. |
| o_F = p, o_F > p | NOT claimed. Residual description only (proof Sec. 7). |
Classical imports carried by the accepted interfaces: index-one (Savchev-Chen/Yuan), EGZ, Davenport constants incl.
D(C_p + C_2p) = 3p-1, Cauchy-Davenport inside G-LS. The cited verdicts record no computation as a premise for p >= 7.

## 3. Governing source manifest
Use ONLY review-excerpts-ASSEMBLY-LS-v1.json, sha256 b5158d37abc8c59dedd452c3bc93a63d631b7d18ef213959d58946242198c09d
(12,536 bytes): a JSON list of {path, sha256 of the WHOLE file, start, end}, inclusive line ranges, absolute paths;
55 ranges from 34 files, 77,462 selected bytes (whole proof and scope included). Package + manifest + selected text stay
below 100 KB. Abbreviations R16/R18/ROT/REF/EV/SR2 are defined in proof Sec. 2. Old CANDIDATE headers in imported files are
superseded ONLY by the cited parent verdict lines plus mandatory overlays; model reviews alone are not acceptance authorities.
The interface table (proof Sec. 2) gives for every row: source lines + sha256, accepting verdict lines + sha256 + item,
original domain, and how each hypothesis is met. Residual-only rows are not premises of Secs. 3-5.

## 4. Argument map with endpoints for hostile review
A. Normal form (proof 1.3-1.4, row NF): existence and termination of the PM*/fusion process; same length, F, rotation
   multiset; avoidance original-to-reduced; 1 <= k <= o_F, k = o_F (mod 2); even ending impossible (K1/M4); kappa^ integral;
   R = 2p+2kappa^-k; non-uniqueness handled existentially (ZX overlay 2).
B. Step 2 (rows GRX, DAV): all-plus pattern has delta = k, C_max = 2H^, T = 0; H^ >= p gives the empty-rotation identity, so
   kappa^ >= 0; even m in [2kappa^+2, 2p] gives (ZP_kappa^). DAV at N = 4p-2, F >= k >= 2, frame at a run gap (empty runs
   allowed): R + H^ = 3p-1+kappa^-k <= 3p-2, i.e. kappa^ <= k-1 <= p-2. Check DAV's authority path (RUNS m4 + ZX/ROT-KP import
   lists; the o3o4 verdict does not pin o3-v4).
C. Step 3 (row LS): |Y| >= p+2kappa^+1 iff k <= p-1. LS-ALL used ONLY on its original definition (EV/LS-scope-v1.md 10-12:
   integer 0 <= kappa <= p-2, odd Y in C_(2p)); no use at kappa = p-1 or below the threshold length. Identify the block
   (S1-sharp / G-LS e = 2 / G-LS e >= 3) for each kappa^.
D. Steps 4-5 (rows K01, FB): kappa^ = 0 -> ROT-K01 (2 <= k <= p-1, any prime p >= 5); kappa^ >= 1 -> ROT-FB(a) (p >= 7). Confirm
   ROT-FB(a) has no hidden 3k <= 2p+1, 2kappa+k <= 2p, F, or o_F(w) hypothesis: FB verdict lines 11-12, setting (S') at
   proof-FB-v1.md 11-17, (S') objects via BAL-full overlay 5, SHgen-E discharge o_F(u°) <= k <= p-1 inside ROT-FB.
E. (A) (row REFL): REFL-few-odd applied to the ORIGINAL w with o_F <= p-1 <= p and the pair from ROT-LS.
F. (B) (rows LED, RGR): ledger with B = p-1 <= 2p-3; Case 1 (R <= 2): F - o_F >= 3p-2 >= 2p; Case 2 gives o_F-1; Case 3 gives
   <= o_F; third-rotation pair identification; adjacency persistence; RGR-LONG(p). Only deletions with o_F <= p-1 reach (A).
G. Quantifier and residual (proof Sec. 7): nothing at o_F >= p is asserted as a theorem. The 7.1 bullet "SOME normal form with
   k <= p-2" is flagged as an immediate consequence of ROT-LS; the length-(4p-1), o_F = p ledger remark is flagged as not frozen.
   Check the kappa = p-1 sequence remark: Y = g^(2p-1)(3g)^(p-1) (ZS v2 V6) satisfies (ZP_(p-1)) and contains
   g^(p+3)(3g)^(p-1) of length 2p+2; no word realization is claimed.
H. Endpoints to test: k = 1, 2, p-1; kappa^ = 0, 1, floor(2p/3), floor(2p/3)+1, p-2; p = 7 (only e = 2 new cells, e.g.
   (o_F, F) = (6, 8)); o_F = 0 (no avoider: even ending); R = 0 and R <= 2 in ledger Case 1; F = 0 (impossible for avoiders).

## 5. Requested verdict boundary
Judge validity of Theorem ASSEMBLY-LS (A), (B) and Proposition ROT-LS for prime p >= 7, relative to the accepted interfaces
at their ORIGINAL scopes with mandatory overlays and to the declared Lev statement (p >= 11 cells only). Report any interface
used outside its original domain separately from any logical gap, and any missing case or endpoint. Remark P5 is a citation
union, not an LS consequence. Not requested and not claimed: novelty or priority, Lean or human review, unrestricted INV*(p),
any statement at o_F >= p, ordered Olson for all D_(2p) or for all finite groups.
