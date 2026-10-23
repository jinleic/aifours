# Olson P7L — parent erratum v2 (second-family wording and dependency precision)

Recorded 2026-10-20T07:17:47-0700 (`/bin/date`). Governs proof-P7L-v1.md after worker erratum1 and parent erratumv1 (d020cb6bc747be9f7f1abbdd88e7c2078573158758d63b6cee5dc3c387d270a5). Claude reviewed the corrected packet at0F/0M/0 new MINOR; confirmed the one Codex MINOR already corrected.

1. At nu0=0 there may be several singleton runs with letters({i})=A=empty: parent erratumv1's "the exceptional run" means **each exceptional run**. Each is empty and has nonzero even theta≤0, hence≤−2. "At most one" applies only at nu0≥1. The actual proof has these cases correctly.
2. P7L-1 needs NF, GRX if-direction and SC0 only. P7L-2 additionally uses ZSTRUCT in(S′) at(6,1) only when t=1. Lemma FB is a valid but unnecessary input: ZSTRUCT's n−≥1, s_j≤2t−1=1 and S(N)≡n+ mod14 force n+=n−=s1=1; W≤12 follows from parity. The verdict retains only the necessary ZSTRUCT import.
3. Parent check provenance: olson-P7L-parent-written-check-v1.md (ab386a48bc5e6e600d6e46b3e4cb4fdbac02f9fcf720864a2a4ea30a000aab85) originally said LF1–343 and worker erratum1 had been read; the actual first surface reads reached LF333, and LF334–381 plus worker erratum1 were completed at the later parent reading before this verdict. All mathematical proof steps LF1–316 had been read before the check was authored. Record this reading-range qualification rather than retroactively asserting the full range was seen earlier.

Pre-freeze unwritten observations and inherited worker byte estimates remain disclosed; strict pre-derivation preregistration is not certified. No theorem changes.
