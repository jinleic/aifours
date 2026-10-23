# K62-HD: parent corollary-reading erratum v1

Recorded at 2026-10-19T10:32:49-0700. Applies after K62-HD-v2.md6c1858c04d7da52bde8533ba71d4dcea814fb69b30a357462e36024226b9f476 and its scope/package. Original files stay unchanged. Disposes Codex5c885c6a's one MINOR by making its explicit monotonicity consequence visible; no hypothesis or main proof changes. Still CANDIDATE_UNVERIFIED pending second-family review and parentverdict.

Old (proof168-169):
````text
Theorem DG (a), (b) apply to both families in G with no remaining hypothesis: N(O) <= n_d / 16, the triple sum is
  <= 19/16 - 2/n_d, and each family has at least two O-triples of capped depth >= 4, or exactly one, of capped depth 5
  (values (4,4,4), tau = 16, e_d >= 5);
````

New:
````text
Theorem DG (a), (b) apply to both families in G with no remaining hypothesis: N(O) <= n_d / 16 and the triple sum is
  <= 19/16 - 2/n_d. Each family has at least two O-triples of capped depth exactly 4. Indeed each O-triple R lies in
  an O-four-subset Q, so W_Q is contained in W_R and T_x(R) divides T_x(Q). Theorem HD forces every triple raw depth
  <=4, excluding the old exactly-one-depth5 alternative (even at e_d=4, where capping would hide rawdepth5). By P2 the
  deep triples have tau=8 and values (2,4,4) or (4,4,4);
````

The same corollary wording governs the frozen scope's informational DG consequence; its main raw-depth<=4 statement does not change. This is a proved immediate consequence of the candidate HD and accepted DG, not a new exclusion of G or Sun7. N(O) is read separately in each corresponding orientation. Computer-assisted Sun5/6 remain transitive imports.
