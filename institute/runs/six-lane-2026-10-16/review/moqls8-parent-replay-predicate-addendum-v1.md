# MOQLS(8) parent-replay predicate — clarification addendum v1

Parent at 2026-10-18T06:30:26-07:00. This corrects ambiguous wording in the [normal-form verdict](moqls8-p1-normalform-parent-verdict-v1.md) (`4748f023…7826`). That verdict said the six strengthened inputs must meet "the unchanged F4 strict predicate" and then listed its elements. In the [unified disposition](moqls8-unified-parent-disposition-v1.md) L40, F4 is stated "for EACH counted **worker** refutation" and includes "proof-stream SHA and byte count recorded".

**Exact predicate actually used for every MOQLS(8) parent native replay** ([first ten](moqls8-fone-first10-parent-verdict-v1.md), [last two](moqls8-fone-direct12-parent-verdict-v1.md), and the six strengthened inputs now running in `moqls8-strengthened-parent-replay-v1/`):
- measured complete solver and checker CNF feeds, with byte length and SHA256 equal to the parent-bound input;
- solver rc 20 with exact `s UNSATISFIABLE`;
- parent drat-trim (`a46c0c71…8e37`) rc 0 with exact `s VERIFIED` after removing only CR;
- no `s NOT VERIFIED` or `s TIMEOUT`, and no guard, feed or relay failure;
- the proof byte count taken from the checker's own log line (`c finished parsing, read N bytes from proof file`).

**No parent replay recorded a proof-stream SHA256.** In these replays the parent's own solver streams its proof directly into the parent checker, and the proof is not retained. This holds for all twelve accepted direct leaves and for P1-B1.M2 (receipt `ada3f86e…03d2`; checker log reads 274,062,094 proof bytes). A digest of a discarded stream adds no soundness: the checker verified exactly the bytes it read. It also offers no later re-verification. The F4 proof-stream SHA element therefore applies to worker-produced refutations offered as evidence, not to parent solve-and-check replays.

This is the predicate already applied in the accepted first-ten and direct-twelve verdicts, made explicit, not a weakening introduced now. An advisory flagged the missing digest; the parent decided not to pause the running desk. The B1.M2 receipt's absence of a proof digest is recorded here explicitly.
