# Olson TCW — parent erratum v2 (Codex MINOR-1; all governing parent corrections)

Recorded 2026-10-20T05:48:20-0700 (`/bin/date`). Governs proof-TCW-v1.md (62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713) after worker erratum1 (00ba0139bc3f13025f7ba9474d3c48813c746839a35e33f95fb5ac3fa4edea01) and parent erratumv1 (eb673b3200d4d0f8f7e36f61fbf3225e5c3542e0b14de05a604ca50c640ee8c9). Codex review /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-codex-v1.prompt.stdout.txt (f8c56c41377758953ac02a28f2eba5c3dddd5988878d50bacbf9cd5f3b379f54):0F/0M/3m. Parent erratumv1 already repairs Codex MINOR2 (parity typo) and MINOR3 (K1 provenance).

**MINOR1 — Lemma9(a), unused generality.** Require **x+y≤B*** in its general formulation (LF185–189). This ensures the excluded interval [a,b]=[−nu0+x,Pi0−y] is nonempty and the representative interval has length 2p−2−B*+x+y≤2p−2<2p, so uniqueness follows along with the existing parity/residue argument. Without that restriction an empty excluded interval would make the hypothesis vacuous and would not force uniqueness. EVERY tabulated application already has x+y=lambda+mu+2≤6<B* (B*≥R≥18), so no used case, lemma application or TCW conclusion changes. The general unused formulation is expressly narrowed, not silently claimed proved as before.

## Parent erratum v1, literal governing text
00001|# Olson TCW — parent erratum v1 (parity and provenance wording)
00002|
00003|Recorded 2026-10-20T05:47:25-0700 (`/bin/date`). Governs proof-TCW-v1.md (62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713) after worker erratum1 (00ba0139bc3f13025f7ba9474d3c48813c746839a35e33f95fb5ac3fa4edea01). No lemma, case or conclusion changes; both-family review remains required.
00004|
00005|1. **Parent-found parity typo, LF219.** Replace "Pi0−nu0 = B* is even" by **"Pi0−nu0 is congruent to B*=Pi0+nu0 modulo2, hence is even."** This is the parity fact needed for reflection of the realised interval in (Pi0−nu0)/2. Equality Pi0−nu0=B* would require nu0=0 and is not asserted.
00006|2. **K1 provenance, LF32/LF497.** The K1 verdict is context, not blanket acceptance of PL Secs2–7. (SR) is derived directly from NF and GRX if-direction at LF47–50, with m(P) per the LOWER erratum; IF(a), normalisation, the SS bijection (through Lemma4(a)) and the light-side argument are all written out in TCW.
00007|3. **Scope of exception lists.** Lemma7's "except possibly" is the logical claim used by Lemma9. No additional necessity/classification assertion is required by LF455's prose "exactly listed"; read it as the displayed exhaustive candidate-exception lists.
00008|
00009|Process history unchanged: the cp01→cp02 gap4138s exceeds1800s and the discarded long derivation turn was redone; six pre-creation text replacements and metadata-only byte-count/JSON-parse steps are disclosed. No strict cadence-compliance claim.

