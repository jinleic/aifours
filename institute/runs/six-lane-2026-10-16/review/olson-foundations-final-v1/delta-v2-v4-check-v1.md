# Desk delta check: R/olson-runs-assembly-proof-v2.md -> v4 (OlsonFoundationDesk, 2026-10-18T01:48:14-07:00 host clock)

Inputs (snapshot copies, byte-identical): v2 0b78850fa232f61c6f45e01c5e8e9f3e2582e96572c3a4fa810fe357ac324abb (293 LF lines),
v3 c5f896912291d144f3fef8d00f846f80d6185ca8cbfab042151bee71705c0665 (355), v4 06579ba5d23f194cf4cf61241fbbc6eebdaa6fb991d004f1642f43277bb3b104
(362); R/olson-gc-parent-verdict.md 8e363920d01132ba7432647ef9a126526b836ec0fb7a60dafefe63b549156f70; the two v2 audit notes and
receipts.  Method: difflib line diff of text.split('\n') (26 hunks, listed below with v2 -> v4 LF ranges); every hunk read and
classified; v3 -> v4 also compared as whitespace token streams.  Desk derivation, not a parent acceptance.

Classes: W wording/naming/citation; S status or review record; H hypothesis clarification (states a hypothesis already in force or
narrows a gloss to what is actually used); J proof-justification change (statement unchanged, argument re-justified); N new stated
consequence (not in v2).

| # | v2 L -> v4 L | change | class | desk verification |
|---|---|---|---|---|
| 1 | 1 -> 1 | title "(v1)" -> "(v4)" (v2 carried a stale "v1" title) | W | - |
| 2 | 4 -> 4-5 | status line | S | - |
| 3 | + -> 9-14 | version notes v3, v4 | S | v3 sha matches the file |
| 4 | 15-18 -> 22-28 | (GC): "normalised NMH word", erratum 1 cited, acceptance status; (IMP) status; conclusion "with F, R >= 1" | H+S | GC verdict L5 "every normalized NMH word with R <= 2p-3", L36 erratum 1; Theorem C already had F, R >= 1 (v2 L155) |
| 5 | 23 -> 33 | "C2" -> "proof-C2.md" | W | - |
| 6 | 40-41 -> 50-51 | citation L14-16 -> L12-16; "defined for RGR words with F, R >= 1" | W+H | proof-INV-reduction.md L12-16 |
| 7 | 43-45 -> 53-56 | v2's "only the one-pattern direction is used" (false) -> direct certificates use it, OR/M0 transfers use the full HW/H equivalence (GR/WAS, U9) | H (dependency description corrected; no step changed) | Fact T unchanged since v2; OR proof proof-PAR-Kplus-partial-r2.md L32-35 ("its avoidance conditions are a subset"), M0 proof-RUNS.md L406-407 |
| 8 | 103 -> 114; 106 -> 117 | "C2 L.." -> "proof-C2.md L.." | W | - |
| 9 | 110-111 -> 121-122 | ZSI-B gloss restricted to R <= 2p - 3 | H | GC verdict L5, L36; N2's input was already R <= 2p - 3 in v2, application unchanged; see DC-1 for the unchanged GC sentence |
| 10 | 122 -> 133 | exit R^ >= 2p: "trivial cut" -> "cannot occur (R^ = A^ <= A <= 2p - 1)" | J (vacuous case) | else-branch of the trivial cut has A <= 2p - 1; M0 lowers A; B^ = 0 gives R^ = A^ |
| 11 | 146-147 -> 157-158 | same in Theorem B's proof | J | Fact Z(i) at v4 L151 (unchanged from v2 L140) |
| 12 | 149 -> 160 | title of Corollary B' | W | statements (a), (b) identical |
| 13 | 166-167 -> 177-181 | C2: v2 used K0's (P) "as e_R <= e_F" from inheritance; v4 shows (P) unnecessary and automatic for k >= p | J (valid) | K0 uses (P) only at proof-PAR-K0.md L103 (even ROTATION run -> e_F >= 1); in C2 e_F = k - o_F >= 2; Step 3 L127-131 needs only e_R = e_F (mod 2) (L102); floor(r/2) <= r - 1 gives F + sum floor(r_i/2) <= 4p - 2 - k <= 3p - 2 for k >= p; (V) <=> o_F >= 1 when kappa = 0 (Fact Z(iii)) |
| 14 | 170 -> 184 | C3: "((D0) here is the only inherited condition used anywhere in Theorem C)" | S | true only with Sec. 5's reading that (V) is used but automatic (KB lists (V), v4 L182); DC-2 |
| 15 | 173 -> 187-188 | C5 = B < kappa half of RL | W | - |
| 16 | 180-181 -> 195-198 | Remark (1) separates the gap Theorem P (proof-INV-reduction.md L23) from PAR's Theorem P; Remark (2) "(F, R >= 1)" | W/H | proof-dihedral-partial.md Sec. 2 vs proof-R4-closure-r1.md L84-94 |
| 17 | 196 -> 213 | table header | S | - |
| 18 | 198-204 -> 215-221 | coverage column; C2 inherited "none"; C3 "(V) (automatic)"; C6 drops "cut," and "/cut" | S (+ consequences of 10, 11, 13) | Theorem B uses Fact Z(i) instead of the cut since v2 |
| 19 | 206-208 -> 223-226 | inherited audit: (P) "only in C2" -> "never used in Theorem C" | J-consistent with 13 | - |
| 20 | 214-224 -> 232-244 | Sec. 6 U1-U6 status | S | U1: GC verdict L3-6, errata L36-42; U2: Codex note L339, Claude note L256; U3: olson-c2-codex-review-v1 "VERDICT: ACCEPT", Claude note L257, Codex v2 audit hypothesis-matched (Codex note L350); U4: Claude note L258; U5: Codex note L343, Claude note L259; U6: Claude note L255, Codex note L340-342 and L252-265 (K1-K6 and the greedy crossing, i.e. S1 Steps 3-4 as used); DC-3 |
| 21 | 226-227 -> 246 | U6 status sentence | S | - |
| 22 | 229-239 -> 248-271 | U7-U10 status; "not covered by a second family" list; non-inherited remark incl. new sentence L269-270 | S + N | new: "every RGR word of length 4p - 2 with F, R >= 1, B = 0 (after normalisation) and k >= p + 1 is solvable" -- correct: an avoider has B <= kappa without inheritance (Fact Z(ii)); C1 (kappa >= 1) and C2 (kappa = 0, k >= p + 1) use no inherited condition (row 13); same as the earlier upstream statement proof-RUNS.md L391-397 and Claude v2 note L285; not used by any theorem |
| 23 | + -> 304-307 | four pins added | S | SHAs equal the snapshot files |
| 24 | 291-292 -> 327-331 | Appendix: assembler's later C0-B hand check; Depth-Lemma reading note (proof-RUNS.md L288-293) | N (aid) | reading note not re-checked here (C0-B chain out of scope; both v2 audits list Depth as fully checked) |
| 25 | + -> 333-362 | Sec. 8 review record and change log | S | receipts: Codex gpt-6.1-sol/openai/max/read-only, 1070.5 s, note 4f231741...; Claude claude-opus-5-5 (init + modelUsage), tools [], 1957.5 s, note aadb6d55...; dispositions ACCEPT-WITH-FIXES, 0/0/2 and 0/0/7 |
| 26 | (v3 -> v4) | title, status, v4 version note, change-log item 11; otherwise only line breaks/blank lines | W/S | whitespace-token diff: exactly these four token changes |

## Corrected GC scope (all NMH hypotheses, not merely Delta0 >= 3 and k >= 7)

Accepted scope (R/olson-gc-parent-verdict.md L5, L36; mixdef-high/c3/proof-C-r1.md L19-21; c6/proof-GC.md L24-30): every
normalised NMH word with R <= 2p - 3, i.e. an RGR word of length 4p - 2 (x = 1, F, R >= 1) with all reflection runs odd, k >= p + 1,
every rotation run pure or a (1,1)-pair, 1 <= B <= kappa - 1, B <= A <= 2p - 1 and R <= 2p - 3 (whence Delta0 = 2p - R >= 3 and
k = 2 kappa + Delta0 >= 2(B + 1) + 3 >= 7).  Erratum 5 (verdict L40): GC's Remark (1) (proof-GC.md L103-104) also uses Lemma H with
beta = 0, (1.1), |d_s| <= e_s + 1, e_s >= 0 and E = sum e_s, all of which are NMH-setting facts.
Applications in v4: Theorem A (L146-148) applies NMH-iii to an NMH word (v4 L58-59; p + 1 <= k <= 2p - 2 is inside k >= p + 1) with
R <= 2p - 3: every hypothesis holds.  Theorem B (L153-156) feeds w^ with p + 1 <= k^ <= 2p - 2, all reflection runs odd (OR makes
them odd, M0 keeps parities), pure/(1,1) runs (M0 end state), kappa^ - B^ = kappa - B >= 1, B^ >= 1, A^ - B^ = A - B >= 0,
A^ <= A <= 2p - 1, length 4p - 2 and R^ >= 2: every hypothesis holds.  So the corrected scope is respected.
DC-1 (MINOR, documentation): v4 L122 (unchanged from v2 L110-111) still says "Lemma GC uses only Delta0 >= 3 and k >= 7 (GC
L103-104)", i.e. the uncorrected Remark (1).  Read it with erratum 5; it is not load-bearing because N2 applies Theorem NMH-iii with
the full setting, not Lemma GC with two parameters.

## Other desk findings on the delta (documentation only)

DC-2 (NIT) v4 L184: "(D0) ... the only inherited condition used" should read "the only inherited condition not automatic for
  avoiders" ((V) is a hypothesis of KB, automatic by Fact Z(iii)).
DC-3 (NIT) v4 L244-246 (U6 "full by Codex"): Codex's list line (note L341) says "S1 Steps 0-2"; its Steps 3-4 check is in the C0-B'
  paragraph (note L252-265).  Cite that paragraph.
DC-4 (NIT) The change log omits two cosmetic consequences: C6's table entry losing "cut," (row 18) and 1.3's L14-16 -> L12-16.
DC-5 (MINOR, documentation) The change log heading "wording and status only" (v4 L345) understates row 13 (a valid C2
  re-justification without (P)) and row 22 (a new, correct non-inherited B = 0 remark).  Neither changes a theorem statement.

## Verdict of the delta check

No theorem statement, branch split, hypothesis of an applied import or validity of a proof step changed from v2 to v4.  All review
repairs are wording, citation, status or hypothesis clarification, except rows 10-11 (a vacuous exit removed), row 13 (C2
re-justified without (P)) and row 22 (new B = 0 remark); the desk re-derived those by hand and they are correct.  The GC import is
applied only inside its corrected full scope; v4 L122's gloss should be read with erratum 5 (DC-1).  v3 -> v4 is layout only.
