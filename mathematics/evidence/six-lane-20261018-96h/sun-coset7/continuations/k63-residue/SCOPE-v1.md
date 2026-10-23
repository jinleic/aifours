# k63-residue continuation: scope (written first)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T02:33:25-0700.
- **Owner:** worker Sun63Successor (successor to ContinueSun7 for the K6.3 residue only). New files only in this
  directory, exclusive creates, versioned names. Everything else read-only.
- **Contract read:** `RUN/control/sun7-successor-brief-v1.md` sha256
  6317171692bdaf905aa020b051db894c6874b1b207fd95cf565b5976ba5a82d5 (RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`).
  Its line 33 (K7 lead) contains an unrelated pasted JSON fragment; it is outside this scope and is not used.

## Target (exact)
Class K6.3 residue: d with f_d >= 2 (3-marker on d), a C-vertex i* with e_(i*) >= 2 (2-marker), the 5-marker
anywhere allowed, all exponents arbitrary. Accepted imports exclude every other K6.3 configuration (K63-U0, K63-D,
K63-E). Full Sun(7) and the K6.3 residue are OPEN at the start of this work.

## Work items
1. Independent rederivation of Lemma TG and the corrected full-C-clique theorem (`K63-TG-v1.md` + errata v1-v3, a
   CANDIDATE pending parent review; not used as an accepted premise here). Question: can a weaker star-type condition,
   or additional local invariants, force the triple granularity used there?
2. A written reduction of the residue from LFC row classification + INV + T + TG, with exact measure identities.
3. If no written closure: one finite certificate architecture (not implemented, not run), naming the lemma that
   would make it complete.

## Rules followed
Written proofs first; no computational output is a premise; no computation is run without a new parent item GO
(none requested at this time). Pending parent reviews (K62-A, TG/CLIQUE) are cited as CANDIDATE only.
Checkpoints at most 30 minutes apart while active; timestamps from /bin/date.
