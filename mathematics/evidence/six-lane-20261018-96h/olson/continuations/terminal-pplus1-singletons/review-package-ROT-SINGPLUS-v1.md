# Review package: Theorem ROT-SING+ (terminal k = p+1, kappa^ = p-1, all-singleton blocks), v1

Owner OlsonAssemblyLS. Frozen after /bin/date 2026-10-19T11:16:26-0700. CANDIDATE_UNVERIFIED written word-level proof. Not used:
Lev, (S1), the index-one theorem, ONE-SHORT-LS, ROT-SING (k = p; pending), ROT-LS, ROT-KP/KP+, ROT-FB, REFL. No computation and no
model launch. The parent owns reviews and verdicts.

## 1. Review exactly this candidate
WHOLE proof: proof-ROT-SINGPLUS-v1.md, sha256 68865d55311128167ead7e3e966e92545520eb5224e4b44458ab469af67a8d9d, lines 1-153
(14,114 bytes). Frozen scope, written BEFORE derivation: TERMINAL-PPLUS1-SINGLETONS-scope-v1.md, sha256
8c4239c6fd6a9159ba17bf4db379bd5e1499a269cda2babad1ea2249b5d10f9d (10:59:40).
Statement (copied): Let p >= 7 be prime and w an avoider of length 4p-2 over D_(2p). Suppose SOME admissible normal form w^ of w
has terminal k = p+1 and kappa^ = p-1. Then every rotation letter of w lies in one set {rho_c, rho_-c} with c != 0; more precisely
the rotation multiset of w is rho_c^(2p-2) rho_(-c)^(p-1). No hypothesis on o_F(w); nothing about reflection runs.
Reading note: "k odd blocks" in proof Sec. 1 means k blocks each of ODD LENGTH (as in the NF); here k = p+1 is even.

## 2. Governing source manifest and trust
Use ONLY review-excerpts-ROT-SINGPLUS-v1.json, sha256 e259d2200912795ef93fd1d54576b1f901ae3e62f8741f2a03721134949b3c9d (3,349
bytes): JSON list of {path, sha256 of the WHOLE file, start, end}, inclusive ranges, absolute paths; 14 ranges from 12 files,
29,583 selected bytes (whole proof and scope included). Package + manifest + selected text are far below 100 KB.
Inputs, each at its accepted scope: the normal form with its empty-run rule (proof-ROT-few-E-v4.md 28-43, rule at 38; fewodd
addendum line 12; ZX overlays 1-3; lowodd item 2, M1, M4); GRX for every cyclic constant-block representation and every sign
pattern, here with Phi = 0, 2 and 4 (lowodd item 1; notes-GRX-v1.md 7-20); Lemma CT (STAB-delta item 6; proof-LSplus-e2-v1.md
13-19); Lemma RS(b) for an integer K >= 0 and nonzero terms (CFXT item 4; proof-ROW-v1.md 16-27 with erratum 2, R5), which rests
on the classical Cauchy-Davenport theorem. No input rests on a computer-assisted step.

## 3. Argument map with endpoints for hostile review
A. Shape (Sec. 2): H^ = 0, so the p+1 blocks are single reflections, F = p+1, R = 3p-3; for Phi = 2m, delta = p+1-2m, so
   C_max = Phi and GRX selects exactly the 2m change blocks and 2p-2m rotations (only the "if" direction of GRX is used).
B. Lemma CL (Sec. 3, NEW at length 3p-3): all-plus gives (ZP_(p-1)); CT with kappa = p-1, n = p-3 (|Y|-n = 2p). Check: excess
   >= p+2; at most two heavy values (v >= p-2); one heavy => v_a = 2p-1; two heavy => at most one other letter c; the multiplicity
   list (2p-1,p-2,0), (2p-2,p-1,0), (2p-2,p-2,1), (2p-3,p-1,1); for eps = 1 the zero-sum a^(2p-1-j*) b^(j*) c, with j* = 0 iff
   c = a and j* = p-1 iff c = b; hence (2p-2,p-2,1) is impossible and (2p-3,p-1,1) forces c = 2a-b.
C. Lemma OM (Sec. 4): filler a-letters must lie in Pi_+ (z = +1) and be disjoint from C; count 3p-3-K = 2p-2m; the identity
   D - sum_C z u - a(K-|C|) = D - aK - sum_C omega. Corollary OM': K = p-3+2m >= p-1 and RS(b) applied to the NONZERO weights only.
D. Lemma ER (Sec. 5, type H1): the target algebra (2p-1)a - (p-1)a = pa and (2p-1)a - (p+1)a = (p-2)a = -2a; the complement
   symmetry s -> sigma(B~) - s with sigma(B~) = sigma(B) + 2a; T(z) for one empty run (= T_i), for two adjacent empty runs (= T_i +
   T_(i+1), changes at S_(i-1), S_(i+1)) and for two non-adjacent empty runs (Phi = 4, T = T_i + T_k, four distinct blocks); the NF
   rule that an empty run separates blocks of different values; r0 != 0 because 0 is the empty subsum.
E. Sec. 6: H1 with a = 0 (pigeonhole on p+1 block values, 2p-2 letters 0); H1 with a != 0 (single-run arcs force
   v_(-a)(R_i) >= alpha_i whenever 1 <= alpha_i <= p; one run with alpha >= p+1; every other nonempty run holds a B-letter; >= 2
   empty runs; Lemma ER); H2a with b != -a (any arc oriented with >= p-1 letters a on the plus side; the p-1 b-weights are nonzero);
   H2c in three sub-cases (-a not in {b, c}, including a = 0; b = -a with a b-free run R holding <= p-2 letters a; c = -a).
F. Endpoints to check: a = 0 or b = 0 (the letter rho_0); letters -a inside B; empty runs; arcs that are single runs; p = 7 bounds
   (K = p+1 <= 2p-1; two b-free runs among p+1); every use of RS(b) has nonzero terms and an integer K.

## 4. Requested verdict boundary
Judge validity of Theorem ROT-SING+ for prime p >= 7 relative to the accepted inputs at their original scopes. Report any use of an
input outside its scope separately from any gap. Not requested and not claimed: existence of avoiders in this cell, reflection
rigidity, INV*, any o_F statement or assembly, other (k, kappa^), ordered Olson for D_(2p) or all groups, p = 5, novelty or
priority, Lean or human review.
