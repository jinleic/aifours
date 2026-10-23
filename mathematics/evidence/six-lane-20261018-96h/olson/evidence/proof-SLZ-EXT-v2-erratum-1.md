# Erratum 1 to evidence/proof-SLZ-EXT-v2.md (sha256 2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:46:30-0700.
Reviews answered: run review/olson-kps-slz-codex-v1.prompt.stdout.txt (sha256 6ce69cb0eb1a2e23b9edff9d85868e17278adfbb1dd4943e9388380cef102408; 0 FATAL / 0 MAJOR / 3 MINOR, all
on SLZ-EXT) and run review/olson-kps-slz-claude-v1.prompt.note.md (sha256 c98dc2f491e739d374329d2489218a81837512e03b979714cdb57287f1bda3bd; 0 FATAL / 0 MAJOR / 8 required MINOR
M-1..M-8 + 2 editorial E-1, E-2 + optional O-1..O-5).  One coordinated round: this file and its two siblings
(import note, KPS v4, SLZ-EXT v2).  The frozen texts are not edited; no proof strategy or theorem statement changes.

## M-7 (Claude) = M1 (Codex): the generic FB instantiation needs t0 <= p - 1
Sec. 1 reads: 'if a sequence Y1 of odd elements has a longest zero-sum Z0 with |Z0| = 2t0, 1 <= t0 <= p - 1, and
L := |Y1| - 2t0 >= p + 1, then (S') holds with kappa' := t0 and k' := 2p - L'.  (Without t0 <= p - 1 the statement is false:
Y1 = g^(3p+1), Z0 = g^(2p), complement g^(p+1), N empty, S(N) = 0 != n+ = 2p.)  Both call sites satisfy it: in SLZ,
t_d <= kappa <= p - 2 (T - d satisfies (S1_kappa)); in EXT, t0 <= kappa <= p - 2 (Y1 satisfies (S1_kappa)).
## M-8 (Claude) = M3 (Codex): the endpoint kappa = 0
PROP's case 2 and RED's length-thr clause are restricted to kappa >= 1.  For kappa = 0 every statement of the text holds
trivially: (ZP_0) implies (S1_0), since a nonempty zero-sum of odd elements contains a minimal zero-sum of even length in
[2, D(C_(2p))] = [2, 2p], which (ZP_0) excludes; so a (ZP_0) sequence has no nonempty zero-sum, and RED's clause is vacuous.
## E-1 (Claude) = M2 (Codex): notation
In Sec. 2 (proof of SLZ) the length |T| is renamed N_T (so 'N_T - s - 1', 'N_T <= p + kappa + t_d'); the negative part of Z0
keeps the name N in Sec. 1 and is written calN in Sec. 3.  In Sec. 3 Step 3 the constructed sequence S(N1) := y H* N1 U(N1)
is renamed Q(N1); S(N1) denotes only the integer sum of the s_i over N1.
## E-2 (Claude): the shrink step of RED
The last sentence of Corollary RED is justified by PROP's contrapositive: if Y is a counterexample of length >= thr + 1,
no one-term deletion Y - x (length >= thr) satisfies (S1_kappa) (else PROP, case 1, would give (S1_kappa) for Y), so every
Y - x is again a counterexample; iterate down to length thr.  Failure of (S1) is not assumed hereditary.
## O-5 (noted)
PROP alone already yields the reduction in RED; the SLZ paragraph of RED's proof is not needed (kept; harmless).
