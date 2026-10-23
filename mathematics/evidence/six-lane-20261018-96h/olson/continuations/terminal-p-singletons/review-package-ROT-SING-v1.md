# Review package: Theorem ROT-SING (terminal k = p, kappa^ = p-1, all-singleton blocks), v1

Owner OlsonAssemblyLS. Frozen after /bin/date 2026-10-19T10:54:21-0700. CANDIDATE_UNVERIFIED written word-level proof. No Lev, no
(S1), no ONE-SHORT-LS (still CANDIDATE; not imported), no ROT-KP+/ROT-FB(b), no computation or model launch. The parent owns
reviews and verdicts.

## 1. Review exactly this candidate
WHOLE proof: proof-ROT-SING-v2.md, sha256 ae5feaa1cd99aad9d2c0c35d1521ec27c3a1e5516225b102b4cb4bb793a4b1f1, lines 1-111
(10,591 bytes). v1 (72b6f222417e5b9b5ee46f886950691d3edad536c70c7e0b8acc0bed33eea702) is a preserved, never-sent draft that differs
only in the second bullet of Sec. 4 (rigid-case remark made exact). Do not review v1.
Frozen scope, written BEFORE derivation: TERMINAL-P-SINGLETONS-scope-v1.md, sha256
38d1b15deba4be3a924cc6416363ce8fad8dbe92ccfc5b4d3df19bd29774c543 (10:50:41).
Statement (copied): Let p >= 7 be prime and w an avoider of length 4p-2 over D_(2p). Suppose SOME admissible normal form w^ of w
has terminal k = p and kappa^ = p-1. Then every rotation letter of w lies in one set {rho_c, rho_-c} with c != 0; more precisely
the rotation multiset of w is rho_c^(2p-1) rho_(-c)^(p-1). No hypothesis on o_F(w); nothing about reflection runs.

## 2. Governing source manifest and trust
Use ONLY review-excerpts-ROT-SING-v1.json, sha256 b1540b10760d24f31f4d1c360adf11dc9f1b2ad142f09e53805f4d05c78999bb (3,744 bytes):
JSON list of {path, sha256 of the WHOLE file, start, end}, inclusive ranges, absolute paths; 16 ranges from 14 files, 25,418
selected bytes (whole proof and scope included). Package + manifest + selected text are far below 100 KB.
Inputs: the accepted normal form (proof-ROT-few-E-v4.md 28-43; fewodd addendum line 12; ZX overlays 1-3; lowodd item 2, M1, M4),
GRX for every cyclic constant-block representation and every sign pattern (lowodd verdict item 1), its accepted ARC form
(proof-ROT-KP-v1.md 34-38; ROT-KP verdict line 25), Lemma CT (STAB-delta item 6), and the classical Cauchy-Davenport theorem.
Context only (not premises): ROT-KP+ (KPS-SLZ item 3) and ROT-FB(b) (FB verdict lines 11-13) need (S1) resp. zero-sums
<= 2kappa^-2, unavailable here; the ZS v2 overlay V6 sequence g^(2p-1)(3g)^(p-1) is a sequence obstruction, not a word.

## 3. Argument map with endpoints for hostile review
A. Shape (proof Sec. 2): k = p, kappa^ = p-1 give H^ = 0, so the p terminal blocks are single reflections, F = p, R = 3p-2.
B. Step 1: GRX with the all-plus pattern: delta = p, C_max = 0, so C = 0 and 2p rotations; T = 0. Check that this is exactly
   (ZP_(p-1)) for the rotation sequence (positions irrelevant).
C. Step 2: CT at kappa = p-1, n = p-2 (|Y| - n = 2p). Check the heavy count, the one-heavy contradiction (2p equal values), and
   the two-heavy multiplicity pair {2p-1, p-1} (j(b-a) = 0 iff p | j). Result X = a^(2p-1) b^(p-1), a != b.
D. Step 3: ANY arc A = runs j+1..j' (j != j'): z = -1 on A, +1 off A; check f_j = f_(j') = 1, Phi = 2, delta = p-2, C_max = 2,
   C = 2, 2p-2 rotations, T = y_(j') - y_j. On the side with >= p letters a, omit om = p - y - z' of them (1 <= om <= p), omit y
   and z' letters b on the two sides; check the count 2p-2 and the signed sum D -/+ ((a+b)y + (a-b)z') in cases (i)/(ii).
   Cauchy-Davenport with range lengths beta_+ + 1 and beta_- + 1 (total p+1) gives all of Z_p when a+b != 0 (and a != b).
   Conclude b = -a and then a != 0.
E. Endpoints: beta_+ = 0 or beta_- = 0 (one sumset factor is {0}); alpha split (2p-1, 0) (all a in A or none); j' = j+1
   (single-run arc); empty runs in w^ (GRX allows them); a or b equal to 0 (the involution-free rotation rho_0 is just value 0 in
   Z_p: if a = 0 or b = 0 the coefficients a+b, a-b are still nonzero unless b = -a).
F. Rigid case b = -a: no contradiction in general (proof Sec. 4); no existence claim either way.

## 4. Requested verdict boundary
Judge validity of Theorem ROT-SING for prime p >= 7 relative to the accepted inputs at their original scopes. Report any use of an
input outside its scope separately from any gap. Not requested and not claimed: reflection rigidity, INV*, any o_F = p assembly
(that remains separate until ONE-SHORT-LS is accepted), ordered Olson for D_(2p) or all groups, p = 5, novelty or priority, Lean or
human review.
