# Review package: Theorem PP1-EXCL (no avoider has an admissible normal form with terminal k = p+1, kappa^ = p-1), v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T12:48:32-0700. CANDIDATE_UNVERIFIED written word-level proof. Not used as premises:
the pending ROT-SING+ (context only), ROT-SING (k = p), ONE-SHORT-LS, ASSEMBLY-P, ROT-PP1 / ROT-PP1-TOP, (S1), Lev, S(p), the
index-one theorem, REFL at any o_F. No computation and no model launch. The parent owns reviews and verdicts.

## 1. Review exactly this candidate
WHOLE proof: proof-PP1-EXCL-v1.md, sha256 6fea2fd20ba4d13fb1cf972927da379556b1f33ea18a8ea661740705c80944d0, lines 1-248
(23,669 bytes). Frozen scope, written BEFORE derivation and disclosing a mental pre-freeze sketch: PP1-EXCL-scope-v1.md, sha256
d386f94414f0bdcbd44694d9676b836da511daa5c923200ff9375db977e32fba (2026-10-19T12:37:11-0700).
Statements (copied from proof Sec. 0):
- THEOREM PP1-EXCL. Let p >= 7 be prime. No avoider w of length 4p-2 over D_(2p) (no 2p letters in increasing original index
  order with identity product) has an admissible normal form w^ (SOME normal form produced by the accepted process; ZX overlay 2)
  with terminal k = p+1 and kappa^ = p-1. No hypothesis on o_F(w), on the reflection runs of w, or on nonempty runs is made.
- THEOREM PP1-EXCL' (word form, implies PP1-EXCL by Sec. 2.1). No avoider u of length 4p-2 has a cyclic constant-block
  representation R_1 S_1 ... R_(p+1) S_(p+1) with every S_i ONE reflection sigma_(y_i), runs possibly empty, and every empty run
  separating blocks of different values.
- THEOREM EXCL-PM (Sec. 3). PP1-EXCL' under the extra hypothesis that all rotation letters lie in one {rho_c, rho_-c}, c != 0
  (the conclusion of the pending ROT-SING+, used only as a stated hypothesis). Input: GRX only.
Reading notes: "blocks of ODD length" in NF means each block has odd length; here every block has length 1 and k = p+1 is even.
Labels: [NEW] = written for this target; [RE-DERIVED] = same statement/argument as the pending proof-ROT-SINGPLUS-v1.md,
re-proved in full here (not new progress). Please check that the labels are accurate.

## 2. Governing source manifest and trust
Use ONLY review-excerpts-PP1-EXCL-v1.json, sha256 234e16855526e944fc6b354f514c97d28b382582250ee4f6594da176c931d190 (4,052
bytes): JSON list of {path, sha256 of the WHOLE file, start, end}, inclusive LF line ranges, absolute paths; 17 ranges from 15
files, 60,987 selected bytes (whole proof, scope and slot transition included). Package + manifest + selected text < 100 KB.
Inputs, each at its accepted scope: the normal form with its empty-run rule (proof-ROT-few-E-v4.md 28-43, rule at 38; fewodd
addendum 1 line 12; ZX overlays 1-3 at zx-s1c verdict lines 51-53; lowodd v2 item 2 (PM*), M1, M4); GRX for every cyclic
constant-block representation and every sign pattern, here with Phi = 0, 2, 4 (lowodd v2 item 1 and M2; notes-GRX-v1.md 7-20);
Lemma CT (STAB-delta item 6, line 23; (ZP_kappa) at line 9; proof-LSplus-e2-v1.md 13-19); Lemma RS(b) for an integer K >= 0 and
nonzero terms (CFXT item 4; proof-ROW-v1.md 16-27 with erratum-2 R5 at lines 36-38), which rests on the classical
Cauchy-Davenport theorem (proof-ROW-v1.md lines 4-5). No input rests on a computer-assisted step.
Context only (NOT premises; included so that the re-derived parts can be compared): proof-ROT-SINGPLUS-v1.md (pending) and
olson-ROT-SINGPLUS-parent-erratum-v1.md.

## 3. Argument map with endpoints for hostile review
A. Reduction (Sec. 2.1): kappa^ = p-1 gives H^ = 0, so every block is one reflection, F = p+1, R = 3p-3; w^ is an avoider (NF).
B. Selection rule (Sec. 2.2): delta = p+1-Phi, so C_max = Phi and C = Phi; omitted rotations K = p-3+2m. (P0) T = 0; (P1) arc
   J = {i..j}, |J| <= p, T = y_j - y_(i-1); (P2) two non-adjacent runs, four distinct change blocks, T = tau_i + tau_l. Direct
   group-law check of (P1) for one run: product (A + y_(i-1) - B - y_i, +1). Only the "if" direction of GRX is used.
C. Sec. 3 [NEW]: Lemma W (Phi = 2, n = 2p-2; both signed counts >= p-1 give p consecutive q, hence all residues since 2c is a
   unit); Step 1 all-plus gives (A,B) = (2p-2,p-1) or (2p-1,p-2) after c <-> -c; Step 2 single runs give E_- <= p-2 or >= 2p-1;
   case (2p-2,p-1): >= p runs need a rho_(-c); case (2p-1,p-2): Step 3 (empty run: q = 0..p-2 gives every NONZERO residue and
   tau_i != 0 by the empty-run rule), then >= p nonempty runs with b_i >= 1.
D. Sec. 4.1 [RE-DERIVED] Lemma CL: CT with kappa = p-1, n = p-3 (|Y|-n = 2p); one or two heavy values (v >= p-2); eps in {0,1};
   j* in [1, p-2]; (2p-2,p-2,1) impossible; (2p-3,p-1,1) forces c = 2a-b.
E. Sec. 4.2 [RE-DERIVED] Lemma OM/OM': fillers are a-letters of Pi_+ (disjoint from C); K = p-3+2m >= p-1; RS(b) on the nonzero
   weights only.
F. Sec. 4.3 [NEW] Lemma SR: z = -1 on one run; nonzero-weight count N + alpha_i - beta_i (a = 0 included: beta_i = alpha_i).
G. Sec. 4.4 [RE-DERIVED] Lemma ER: |Sigma(B~)| >= p-1, complement symmetry with sigma(B~) = sigma(B) + 2a; (i) tau_i = r0 - 2a,
   r0 != 0; (ii) adjacent empty runs force y_(i+1) = y_i against the empty-run rule; (iii) Phi = 4, K = p+1, T + 4a = r0 forces
   r0 = 0.
H. Sec. 4.5: H2a [NEW] (>= p runs with alpha_i <= p-1 need beta_i >= alpha_i + 1; N = p-1); H2c [NEW] (>= p runs with
   alpha_i <= p-2 need beta_i >= alpha_i + 2; N = p); H1, a = 0 [RE-DERIVED] (pigeonhole on p+1 block values, T = 0, 2p-2 zero
   letters); H1, a != 0 [RE-DERIVED via SR] (unique run with alpha >= p+1; every other nonempty run holds a letter != a; >= 2
   empty runs; ER).
Endpoints to check: a = 0 (the letter rho_0) in every type; letters of value -a; empty runs (Sec. 3 Step 3, Lemma ER); the
uniqueness thresholds 2p > 2p-2, 2p-2 > 2p-3, 2p+2 > 2p-1; p = 7 bounds; arcs with |J| <= p; every RS(b) use has an integer K and
nonzero terms; CT hypotheses at kappa = p-1.

## 4. Requested verdict boundary
Judge validity of Theorem PP1-EXCL (and separately Theorem EXCL-PM as a conditional statement) for prime p >= 7 relative to the
accepted inputs at their original scopes. Report any use of an input outside its scope separately from any gap, and say whether
the [NEW]/[RE-DERIVED] labels are accurate. Not requested and not claimed: reflection rigidity, INV*, any o_F statement or
assembly, other (k, kappa^), ordered Olson for D_(2p) or all groups, existence or non-existence of avoiders outside this cell,
p = 5, Lev, S(p), REFL, novelty or priority, Lean or human review. Suggested split: Secs. 2-3 need only NF and GRX; Sec. 4 also
needs CT and RS(b).
