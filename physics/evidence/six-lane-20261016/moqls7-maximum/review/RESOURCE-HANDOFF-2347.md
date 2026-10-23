# Resource handoff at the 23:47:55 checkpoint

This supplements `RESOURCE-HANDOFF-2318.md`; its proof/evidence hashes and unresolved scientific scope are unchanged.
M(7) is not determined. All scientific processes launched by this worker have ended.

## Authorized resumption and observed outcome
Parent released launches at23:26. The fresh23:26:41 outer check observed14,309,265,408 bytes free, above12.2e9 plus
projected10MiB retained logs/model/receipt growth. `evidence/RESUME-GATE-2326.json` records it. Only the existing
A/C311 residual-lex input was restarted, using a new output directory and unchanged native1800-second cap.

The resumed run ended at23:47:55 with **UNKNOWN safety stop**, after1229.385 seconds, cooperative SIGTERM rc-15,
sampled aggregate RSS492994560 bytes. Its continuous monitor detected the free-space floor; no confirming disk
poll was made. Receipt: `explore/k3lex/screenA_r2/A_C311.json`. The CNF remains
`059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f`.
Both lex runs were interrupted before their1800-second caps; neither is a completed negative search or UNSAT.
No CNF/proof copy or large retained-data growth occurred in the resumed run.

## Current boundary
Renewed deferral was reported once and saved as `evidence/DISK-DEFERRAL-2347.json`. No new solver/checker/enumerator/
compiler/reviewer launch follows. Await parent resource release, then a fresh>=12.2e9 gate with projected retained
growth fitting and original-deadline headroom. No polling, deletion/thinning, proof retention, duplicate CNFs or
>10MiB snapshots/copies is authorised.

The retained producer results remain:294 K2 verified instances; original A/C321 and A/C411 verified; requested
K1 corollary note frozen and delivered. C311, independent B K3 routes, parent integration and any exact-vector
witness remain separate obligations.

## Prepared alternative, not activated
`review/drafts/AMENDMENT-4.r2.md` preserves the earlier draft and removes an unnecessary prerequisite: transporting
the checked C321/C411 exclusions to every frame can justify w_a<=3 and never(w_a>=3 and w_b>=2), independently of
a full-cap C311 miss. This may share the hard-case knowledge globally instead of repeatedly losing solver state to
resource interruption. It remains **unfrozen/inactive**: no generator, finite-control execution, cut CNF or search
exists. Proof-composition review, exact local controls, code/freeze and resource gates must precede use.
