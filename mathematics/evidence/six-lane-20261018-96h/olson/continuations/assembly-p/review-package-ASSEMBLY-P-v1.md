# Review package: Theorem ASSEMBLY-P (o_F <= p; conditional on ONE-SHORT-LS and ROT-SING) and Corollary ASSEMBLY-P0, v1

Owner OlsonAssemblyP. Frozen after /bin/date 2026-10-19T11:45:39-0700. CANDIDATE_UNVERIFIED. CONDITIONAL on two PENDING
candidates used only as labelled premises, [ONE-SHORT-LS] and [ROT-SING]; Corollary ASSEMBLY-P0 uses neither. For p >= 11 Lev
2022 Theorem 2 (statement level) enters exactly as recorded in proof Sec. 8. No computation, model launch, novelty, priority,
Lean or human-review claim. The parent owns reviews and verdicts.

## 1. Review exactly this candidate
WHOLE proof: proof-ASSEMBLY-P-v2.md, sha256 059033b00b669e10f0fa49bdb2fdb55a135a85644f792ef2b3b3d6eb61dacfb5, lines 1-320
(37,385 bytes). v1 (2f6e8468c060448b05b51bffc8a435cc8e04f224f1484652cacd905b33293b4d) is a preserved, never-sent draft; v2
changes only the LED-row domain wording, one trust attribution, one added trust citation and one explanatory sentence (header
lines 3-9); do not review v1.
Frozen BEFORE derivation: ASSEMBLY-P-scope-v1.md, sha256 5a4d9064b05e7dfbc9ac478ba3df95e89de00b573be379c3ce968ec848c2f64f
(11:30:13); ASSEMBLY-P-scope-v1-addendum-1.md, sha256 d75211261e4108eff5ec9ada3f702d8408fbf235b8b0ff6570a2106f5727a2d9
(11:35:16, Corollary ASSEMBLY-P0).
Statements (proof Sec. 0), p >= 7 prime:
- Theorem ASSEMBLY-P [ONE-SHORT-LS, ROT-SING]: (A) every length-(4p-2) avoider over D_(2p) with o_F <= p satisfies INV*;
  (B) every length-(4p-1) word with o_F <= p has an identity 2p-subword in increasing original index order.
- Proposition ROT-P: SOME admissible normal form with terminal k = p => all rotations in one {rho_c, rho_-c}, c != 0; no o_F
  hypothesis; [ROT-SING] only at kappa^ = p-1, [ONE-SHORT-LS] only at kappa^ in U(p).
- Proposition DEP: U(p) := {kappa : floor(2p/3)+1 <= kappa <= p-3, p < 10(p-kappa)-13, not (p = 1 mod 3 and
  kappa = (2p+1)/3)}; for floor(2p/3)+1 <= kappa <= p-2 outside U(p), odd Y with |Y| = p+2kappa and (ZP_kappa) satisfies
  (S1_kappa) by accepted LS+2 / LS+ linear band / BASE1+. U(7) is empty.
- Corollary ASSEMBLY-P0 (no pending premise): (A0)/(B0) for words with o_F <= p-1, or o_F = p and kappa(w) not in
  U(p) u {p-1}. At p = 7 this excludes only o_F = F = 7; (A)/(B) at p = 7 need [ROT-SING] only and no Lev.
- Remark P5: p = 5 is not claimed.

## 2. Coverage and trust accounting (not an extra claim)
| Invoked normal form | Route | Pending | Lev | S(p) |
| --- | --- | --- | --- | --- |
| k <= p-1 | accepted ROT-LS (any o_F) | none | as the ROT-LS verdict (p >= 11, floor(2p/3)+1 <= kappa^ <= p-3) | no |
| k = p, kappa^ in {0,1} | accepted ROT-KP item 1 (p >= 5); ROT-K01 does not cover k = p | none | no | no |
| k = p, 2 <= kappa^ <= floor(2p/3) | S1-sharp (no length hypothesis) + ROT-KP+ | none | no | yes |
| k = p, floor(2p/3)+1 <= kappa^ <= p-2, not in U(p) | LS+2 / LS+ band / BASE1+ + ROT-KP+ | none | no | yes |
| k = p, kappa^ in U(p) (p >= 11 only) | [ONE-SHORT-LS] at |Y| = p+2kappa^ + ROT-KP+ | ONE-SHORT-LS | yes (inside it) | yes |
| k = p, kappa^ = p-1 | [ROT-SING] | ROT-SING | no | no |
Word level: restricted REFL on the original w (o_F <= p); ordered deletion ledger with B = p; RGR-LONG(p). Classical imports
carried by accepted interfaces: index-one (Savchev-Chen/Yuan), EGZ, Davenport constants incl. D(C_p + C_2p) = 3p-1,
Cauchy-Davenport. No computation is a recorded premise of any p >= 7 interface used (proof Sec. 8 cites each record).

## 3. Governing source manifest
Use ONLY review-excerpts-ASSEMBLY-P-v1.json, sha256 6efb151b6d0e08b27892be10e9f8b5b09c108ded5f3edfe676726051c0f6d8ff
(13,383 bytes): a JSON list of {path, sha256 of the WHOLE file, start, end}, inclusive line ranges, absolute paths; 58 ranges
from 34 files, 77,681 selected bytes (the whole proof, the statement/route parts of the scope, the whole addendum). Every entry
was re-verified (whole-file SHA256, in-bounds inclusive range) at creation. Package + manifest + selected text < 100,000 bytes.
Abbreviations R16/R18/ROT/REF/EV/SR2/CON are defined in proof Sec. 2. Accepting authority = the cited parent verdict lines plus
mandatory overlays; the two PENDING texts are included only so that their exact statements and trust lines can be checked
against the use made of them (they are conditions, not imports). Model reviews are not acceptance authorities.

## 4. Argument map with endpoints for hostile review
A. Normal form at k = p (proof 1.5, row NF): all terminal blocks odd, F = p (mod 2), H^ = (F-p)/2, R = p+2kappa^ (one below
   the LS threshold, so LS-ALL/G-LS are NOT used); o_F(w) >= p; o_F(w) = p implies kappa^ = kappa(w).
B. Step 1 (rows GRX, DAV): all-plus pattern at k = p gives delta = p, C_max = 2H^, T = 0; kappa^ >= 0 and (ZP_kappa^); DAV:
   R + H^ = 2p-1+kappa^ <= 3p-2, so kappa^ <= p-1. The four kappa^ ranges partition [0, p-1] for p >= 7.
C. Step 2 (row KP): ROT-KP item 1 is the accepted interface for kappa^ = 0 (and 1) at k = p; check its verdict lines 15, 17
   and overlay m5 (SHgen-E base words keep k = p, o_F(u°) <= p).
D. Steps 3-4 (rows S1S, KP+, OSL, DEP rows): S1-sharp has no length hypothesis; ROT-KP+ has no o_F, F or upper kappa^
   hypothesis (KPS-SLZ verdict line 10, source 38-40, erratum M-1/M-6); [ONE-SHORT-LS] is applied only at its exact length
   p+2kappa and range floor(2p/3)+1 <= kappa <= p-2 (never at kappa = p-1, where it is false).
E. Proposition DEP (proof Sec. 4): LS+2 bound 3p-5 < 3p-4; LS+ band bound 3kappa+1 < 3kappa+e; BASE1+ bound 2p+2 < (7p+2)/3.
   Check that (i)-(iii) exhaust the complement of U(p) in [floor(2p/3)+1, p-2], that U(7) is empty, and the remark that U(p) is
   nonempty for p >= 11 (agrees with LS+ chain verdict line 24).
F. Step 5 (row SING): kappa^ = p-1 means H^ = 0, F = p, R = 3p-2; [ROT-SING] has no o_F hypothesis.
G. (A) (row REFL): REFL-few-odd on the ORIGINAL w with o_F <= p; caller obligations (REFL verdict line 16) concern SHgen-E
   rebasing only and are discharged inside ROT-LS / ROT-KP / ROT-KP+.
H. (B) (rows LED, RGR): B = p <= 2p-3; Case 1: F - o_F >= 3p-3 >= 2p; Case 2: o_F - 1; Case 3: <= o_F (fusion never raises
   the odd count); third-rotation pair identification; adjacency persistence; RGR-LONG(p).
I. (A0)/(B0): Case 3 deletion with unchanged o_F keeps F hence kappa; a deletion lowering o_F lands in o_F <= p-2 (accepted
   ASSEMBLY-LS). The ledger is used with a class not of the form o_F <= B: the written case analysis is re-run with explicit
   membership checks (precedents for multi-condition classes: K01 verdict line 38, ROT-KP verdict line 43, FB verdict line 29).
J. Endpoints to test: p = 7 (Step-4 cell only kappa^ = 5 = p-2, cells (i) and (iii); ROT-SING-only class o_F = F = 7);
   p = 11 (U = {8}); p = 13 (U = {10}; BASE1+ at 9); kappa^ = 0, 1, 2, floor(2p/3), floor(2p/3)+1, p-3, p-2, p-1; o_F = p with
   some normal form k <= p-2; R = 0 and R <= 2 in Case 1; o_F(w_i) = o_F(w) - 2 in Case 3.

## 5. Requested verdict boundary
Judge, for prime p >= 7: Theorem ASSEMBLY-P (A), (B) and Proposition ROT-P CONDITIONALLY on [ONE-SHORT-LS] and [ROT-SING];
Proposition DEP and Corollary ASSEMBLY-P0 relative to accepted interfaces only. Report separately any interface used outside
its original domain, any logical gap, any missing case or endpoint, and any place where a pending candidate is treated as
accepted. Not requested and not claimed: acceptance of ONE-SHORT-LS or ROT-SING; novelty or priority; Lean or human review;
any statement at o_F >= p+1 (proof Sec. 9 is a residual description only); p = 5; unrestricted INV*(p); ordered Olson for all
D_(2p) or for all finite groups.
