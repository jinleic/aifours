# Checkpoint 001: ROT-SING+ (terminal k = p+1, kappa^ = p-1)

Owner OlsonAssemblyLS. /bin/date 2026-10-19T11:15:11-0700. Active slice started 10:59:40 (scope freeze).

- Scope (frozen 10:59:40): TERMINAL-PPLUS1-SINGLETONS-scope-v1.md, sha256 8c4239c6fd6a9159ba17bf4db379bd5e1499a269cda2babad1ea2249b5d10f9d.
- Candidate (frozen 11:14:41, chmod a-w): proof-ROT-SINGPLUS-v1.md, sha256
  68865d55311128167ead7e3e966e92545520eb5224e4b44458ab469af67a8d9d, 153 lines, 14114 bytes. CANDIDATE_UNVERIFIED.
- Result claimed: for p >= 7 and an avoider of length 4p-2 with some admissible NF of terminal k = p+1, kappa^ = p-1, the rotation
  multiset is rho_c^(2p-2) rho_(-c)^(p-1), c != 0.
- Route: GRX all-plus -> (ZP_(p-1)); NEW Lemma CL via CT (n = p-3) giving types H1 (v_a = 2p-1), H2a (a^(2p-2) b^(p-1)),
  H2c (a^(2p-3) b^(p-1) (2a-b)), type (2p-2, p-2, 1) excluded; Lemma OM (pattern omission, K = p-3+2m) with RS(b) full coverage;
  Lemma ER (empty runs in H1, using a FOUR-change pattern); run count kills H1; OM' kills H2a with b != -a and all of H2c.
- Imports re-hashed 11:14:57 and equal to the hashes printed in Sec. 7 of the proof; no pending result used.
- Blocker: none. Next action: review package + excerpt manifest (<= 100 KB), then IRC Main and park.
