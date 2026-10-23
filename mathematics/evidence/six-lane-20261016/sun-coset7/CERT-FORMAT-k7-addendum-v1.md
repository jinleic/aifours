# CERT-FORMAT-k7-addendum-v1: Stage C universe rows and the engine-v3 output deltas (pre-launch; overlay)

- **Freeze record:** host-clock time and sha256 in `evidence/certformat-addendum-v1.sha256`.
- **What it overlays:** `CERT-FORMAT-k7-v1.md` (2c0e483011a0ea3aace670da4b9a200ae333e676682e0e10fb47d2e584401545). That file stays frozen and byte-identical, and still binds every run.
- **Why:** this file supplies the two Stage C universe rows that §1 of v1 does not list, and records how `core7_engine_v3.py` (a26e6c68…23a7) differs in its outputs.
- **Status:** written under the parent HOLD; no Stage C run exists. Any Stage C output is EXPLORATORY until it is independently replayed and reviewed.

## 1. Universe rows added to CERT-FORMAT-k7-v1 §1

These rows are defined identically in engines v1, v2 and v3. The engine diffs never touched the `UNIVERSES` table. Vertex 0 is the D-vertex.

| name | roles (vertex order 0..6) | allowed gcds | class covered |
|---|---|---|---|
| K62 | D2, C, C, C, C, C, C | C–D2 {2, 4}; C–C {6} | README class K6.2\*, plus the case already eliminated in writing by Lemma D2 (all six gcds equal to 2). Covering that case again is harmless and sound. |
| K63 | D3, C, C, C, C, C, C | C–D3 {3}; C–C {6} | README class K6.3 in full. Lemma D3 (partial) is not used as a premise. |

- **Role domains:** D2 has e ∈ {1,2,3,4}, f = 0, g ∈ {0,1,2}. D3 has e = 0, f ∈ {1,2}, g ∈ {0,1,2}. C is as in v1 §1.
- **Profile coverage:** the rule of v1 §1 applies unchanged. There is one representative per orbit under role-preserving permutations, non-decreasing within the run of C roles, and every pairwise gp must lie in the allowed set.
- **CAP hypotheses:** H1–H3 hold by README P0–P1 (rules-k7-addendum-v1 §A3, table row for the 7-vertex classes).
- **No independent count:** I have not counted these profiles independently. A checker must enumerate them itself.

## 2. Engine-v3 output deltas relative to CERT-FORMAT-k7-v1 §4

- **`run.json`:**
  - `engine` = "core7_engine_v3".
  - New fields: `sigterm_received`, `rss_cap_bytes`, `peak_rss_bytes_last_check`, `peak_rss_bytes_at_write` and `stats.profile_in_progress`.
  - `stats.profile_in_progress` is null when the run is COMPLETE. Otherwise it holds the profile being processed when the stop occurred, and `profiles_done` counts the profiles completed before it, in the deterministic enumeration order.
  - On an UNKNOWN stop, the counts for the profile in progress (nodes, leaves, closures) are partial and certify nothing.
- **`lp_duals.json.gz`:**
  - **The selection mechanism changed.** v1/v2 re-enumerated every q-vector of every killed signature at write time, called `lp_solve` on each resulting key, and then added every memoised key of value ≥ 1. v3 removes that re-enumeration and writes only the memoised keys of value ≥ 1.
  - The key set is the same. The kill test evaluates and memoises every q of each signature it kills, and all of those values are ≥ 1. Every RPLP "R" certificate cites a memoised key of value ≥ 1. This argument is unexecuted, and the independent replay checks every cited key directly.
  - Keys appear in key-tuple order rather than string order, and the separators differ. JSON object order is not part of the format.
  - Each value is unchanged: {"value", "y"} with exact rational strings.
- **Output buffering changed.** Each certificate file is compressed incrementally in memory by a bounded compressor, so there is no joined copy of the leaf text. A no-op loop that re-parsed every leaf line was removed. Engine v3 is therefore **not** only a guard patch; its full delta is in `evidence/engine-v2-to-v3.diff` (f6315f1f…a697).
- **Gzip container:** produced by zlib with wbits 31 instead of `gzip.compress(…, mtime=0)`. The content is the same; header bytes may differ. A checker decompresses the files and must not compare their compressed bytes.
- **Empty leaf file.** When there are no leaf orbits, the decompressed `leaves.jsonl.gz` from v1/v2 is a single newline; from v3 it is empty. When there are leaf orbits, the lines are identical, each terminated by a newline. A checker must split on newlines and ignore empty lines.
- **Unchanged:** `leaves.jsonl.gz`, `vfc_killed.json.gz` and `survivors.json` keep their content format, and the 15 MiB rule is the same: if exceeded, only `survivors.json` and `run.json` are written, with the note.

## 3. Unchanged checker obligations

CERT-FORMAT-k7-v1 §5 still applies, as clarified by rules-k7-addendum-v1 §A5 E5 and by rules-k7-erratum-v1 W2:
- **Independent recomputation:** the checker enumerates profiles itself, computes canonical codes and LP keys itself, checks every q and every allowed subset, and walks the full tree.
- **Exact verification:** every certificate is checked in exact rationals. (★) ≤ 1 must hold on all columns of 𝒞(q), with Obj ≥ 1.
- **UNKNOWN runs:** a run with status UNKNOWN proves nothing about its unvisited part.
