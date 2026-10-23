#!/usr/bin/env python3
"""Assemble the no-tools Claude review prompt from the PINNED snapshot (never the live lane).
Every inlined text is LF-numbered by content.split('\n') (1-based); excerpts keep original numbers.
Writes ../pa19-final-bridge-claude-v1.prompt.txt with open mode 'x'.  Usage: python3 -B build_claude_prompt.py
"""
import difflib
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), 'pa19-final-bridge-claude-v1.prompt.txt')  # v2 assembler; draft1 superseded

HEADER = """You are a hostile, independent, STATIC auditor of a finite nonexistence argument for PA(19,8,6): a 19 x 8 array over 6 symbols in which every two rows agree in at most one column. You review the mathematical bridges and the actual production code. You do NOT certify the target; you look for every defect that could make the claimed "no such array exists" conclusion unsound, and you separate soundness defects from bounded operational deviations.

You have NO tools. Everything you may use is inlined below; do not use outside context or prior knowledge of this project, and do not assume facts that the inlined texts do not state. Each inlined file is shown as lines 'N|text', where N is the 1-based line number in content.split('\\n') of the pinned snapshot file; excerpts keep their original numbers. Cite every finding as PATH:N using the PATH shown in the file banner. Where a fact you need is not inlined (for example stream_check revisions 1-4 and 9, most runners, controls' raw outputs), say so explicitly instead of guessing.

The proof map (first file, PROOF-MAP-v4.md) is the desk's CLAIM, not evidence. Pinned M1-complete candidate: cycle2/m1-complete-candidate-20261018T012523.json sha256 cf3e87c5fd8201286aa7a2b1e09999733cab7e5018a7e49c738f91ff13d1d791 (M1 counts all 5577 A2 cases and all 486 E0 graphs UNSAT; M2 486 E0 + 5411/5577 A2, 166 open; producer candidate, not the final gate).

AUDIT (all items; if you must prioritise, do B3-B8 first):
B1 Profiles/multisets: the 6 profiles and 10 multisets cover EVERY valid array, including all non-balanced ones; counting lemma and L = 3 - excess.
B2 E0: quad-graph lemma (t <= 2, n2 = 13 + n0, simple graph, max degree 4, 13..16 edges), the 486-graph list, encode_q0.py and encode_q0b.py (necessary constraints only; symmetry breaking valid simultaneously).
B3 A2 skeletons: every pruning in gen_skel.py and gen_skel_b.py (tmax, hmax, single-special-column matching filter, linearity/-Z1, degree 4, rows <= 19, h <= 2*c0, hyperedge candidates) is a NECESSARY condition of validity, not a heuristic; both generators are complete; the isomorphism quotient (networkx dedup, nauty genbg canonical classes, compare_skel bijection) quotients only by genuine symmetries; state what is trusted from nauty/networkx and what the two generators share.
B4 Encoders (encode_e1 CNF class, encode_skel, encode_skel_b build_v2/build_partbatch, encode_full/full2, encode_partq, encode_partbatch): (a) every genuine valid array, after the WLOG normalisation of the proof map section 8, satisfies ALL symmetry-breaking clauses AT ONCE (one reading order and one group; for M2 v1 the non-lex P0 label fixing composed with special-column lex-leader constraints); (b) exact cardinality / at-most / weighted / totalizer / pair encodings admit every assignment that satisfies the intended constraint (the completeness direction is what UNSAT soundness needs); (c) every degenerate branch (empty clause, all-literals-negated, assert) is unreachable or mathematically correct on the production domain; prove or refute the proof map section 4 claims.
B5 Splits: extend_p1q.py (and the extend_p1.py diff), extend_b.py, the full / one-column / batched selector semantics (batch UNSAT => every listed subcase UNSAT), the subcase symmetry breaking for the stabilizer of the placement; changing method/solver per subcase is acceptable only with exact CNF binding (check rerun_batch12.py and the route switches described in README); no dropped placement and no heuristic denominator.
B6 ms06_s00468 six-unit cover: base binding, literal map x[8][6][s] = 421 + s, the six positive units cover every cell value, summarize15 reconstruction.
B7 Acceptance (aggregate15.py, summarize15.py and the post-pin aggregate16/summarize16 diffs, stream_check15.py, stream_check5.py, stream_check9/4/1 excerpts, run_proofpass.py, check_proofs.py, drat-trim.c excerpts incl. the early-EOF claim of the proof map section 7): proof reader EOF, self exit of solver and checker, rc, exact '\\r'-normalised s-lines == ['s VERIFIED'], no abort/admission refusal, caps, replay hash/length binding, CNF-byte binding through FIFOs, route selection a/b/c5/d/e/cell, split coverage (_r2 exclusion, the `multiset` + 2-entry range heuristic, vacuous n = 0), E0 counting, SAT listing; list what the aggregator does NOT check. Do not promote historical lrat-check-only, proof-free, capped or retired revision-10 records.
B8 The M2 ms09 b-index-3 empty placement list: check the parent structural argument and the worker JSON against the skeleton entry and extend_b.py; it must be a separate STRUCTURAL row, never DRAT, never a generic 0/0 pass; check whether aggregate16/summarize16 fail closed on empty lists for BOTH M1 and M2.
B9 Controls/provenance: from the inlined README/proof map, say which controls are post hoc (they stay post hoc) and that none is load-bearing as proof.
B10 Old scout gaps: confirm or contest each disposition in proof map section 11 against the inlined gap sections of the two old scout audits, gap by gap.
B11 Trust base and binding: the exact trust base; every representation bound only by its producer or by a parent SAMPLE rather than an all-case parent binding.
B12 Residuals required before any final "optimum 18" claim, ordered by importance.

Separate (S) mathematical soundness issues from (O) bounded operational/process deviations. FATAL only if a counted UNSAT could be unsound or a valid array could be left uncovered; MAJOR if acceptance is blocked until checked/repaired; MINOR otherwise.

OUTPUT FORMAT (plain markdown, at most about 3000 words):
Line 1 exactly: DISPOSITION: ACCEPT-BRIDGES | ACCEPT-BRIDGES-WITH-RESIDUALS | REJECT-BRIDGE  (pick one)
Then sections FATAL, MAJOR, MINOR (each finding: id, S or O, one-paragraph argument, citations PATH:N; "none" if empty);
then "Bridge verdicts" (B1..B12, one line each: PASS / PASS-WITH-RESIDUAL / FAIL + citation);
then "Old scout gap dispositions" (one line per gap: CONFIRM or CONTEST + reason);
then "Producer/sample-only representations"; then "Trust base"; then "Residuals before final claim".
State plainly what you could not check. Never claim to have run anything.

INLINED PINNED TEXTS FOLLOW.
"""

# (banner path, snapshot file relative to HERE, list of (start, end) 1-based inclusive ranges or None for all)
FILES = [
    ('PROOF-MAP-v4.md', 'PROOF-MAP-v4.md', None),
    ('run/screening/info-1-packing-array19-contract.json', 'snapshot/run/screening/info-1-packing-array19-contract.json', None),
    ('lane/README.md (855-line copy; first 848 lines byte-identical to the 01:41 snapshot)', 'snapshot-supp3/lane/README.md',
     [(1, 46), (74, 143), (177, 207), (259, 330), (344, 367), (517, 523), (775, 789), (800, 805), (849, 855)]),
    ('lane/cycle2/m1-complete-candidate-20261018T012523.json', 'snapshot/lane/cycle2/m1-complete-candidate-20261018T012523.json',
     [(1, 148), (586, 656)]),
    ('lane/src/profiles.py', 'snapshot/lane/src/profiles.py', None),
    ('lane/src/gen_skel.py', 'snapshot/lane/src/gen_skel.py', None),
    ('lane/src/gen_skel_b.py', 'snapshot/lane/src/gen_skel_b.py', None),
    ('lane/src/compare_skel.py', 'snapshot/lane/src/compare_skel.py', None),
    ('lane/src/gen_skel_cases.py', 'snapshot/lane/src/gen_skel_cases.py', None),
    ('lane/cycle2/genbg-help-flags.txt', 'snapshot/lane/cycle2/genbg-help-flags.txt', None),
    ('lane/src/encode_e1.py', 'snapshot/lane/src/encode_e1.py', [(1, 101)]),
    ('lane/src/encode_q0.py', 'snapshot/lane/src/encode_q0.py', None),
    ('lane/src/encode_q0b.py', 'snapshot/lane/src/encode_q0b.py', None),
    ('lane/src/encode_skel.py', 'snapshot/lane/src/encode_skel.py', None),
    ('lane/src/encode_skel_b.py', 'snapshot/lane/src/encode_skel_b.py', [(1, 76), (181, 186), (382, 621)]),
    ('lane/src/extend_p1q.py', 'snapshot/lane/src/extend_p1q.py', None),
    ('lane/src/extend_b.py', 'snapshot/lane/src/extend_b.py', None),
    ('lane/src/encode_full2.py', 'snapshot/lane/src/encode_full2.py', None),
    ('lane/src/encode_partq.py', 'snapshot/lane/src/encode_partq.py', None),
    ('lane/src/encode_partbatch.py', 'snapshot/lane/src/encode_partbatch.py', None),
    ('lane/cycle2/s00468-six-unit-contract.json', 'snapshot/lane/cycle2/s00468-six-unit-contract.json', None),
    ('lane/src/run_s00468_cell14.py', 'snapshot/lane/src/run_s00468_cell14.py', [(1, 82)]),
    ('lane/src/summarize15.py', 'snapshot/lane/src/summarize15.py', None),
    ('lane/src/aggregate15.py', 'snapshot/lane/src/aggregate15.py', None),
    ('lane/src/stream_check15.py', 'snapshot/lane/src/stream_check15.py', [(16, 88), (138, 230), (365, 591)]),
    ('lane/src/stream_check5.py', 'snapshot/lane/src/stream_check5.py', [(1, 13), (42, 168)]),
    ('lane/src/stream_check9.py', 'snapshot/lane/src/stream_check9.py', [(109, 171)]),
    ('lane/src/stream_check4.py', 'snapshot/lane/src/stream_check4.py', [(121, 183)]),
    ('lane/src/stream_check.py', 'snapshot/lane/src/stream_check.py', [(89, 142)]),
    ('lane/src/run_proofpass.py', 'snapshot/lane/src/run_proofpass.py', [(32, 62)]),
    ('lane/src/check_proofs.py', 'snapshot/lane/src/check_proofs.py', [(29, 58)]),
    ('lane/src/run_hard12.py', 'snapshot/lane/src/run_hard12.py', [(118, 196)]),
    ('lane/src/run_m2_12.py', 'snapshot/lane/src/run_m2_12.py', [(90, 165)]),
    ('lane/src/rerun_batch12.py', 'snapshot/lane/src/rerun_batch12.py', None),
    ('lane/src/run_m2q0c.py', 'snapshot/lane/src/run_m2q0c.py', None),
    ('lane/tools/drat-trim/drat-trim.c', 'snapshot/lane/tools/drat-trim/drat-trim.c',
     [(720, 730), (1052, 1149), (1213, 1222), (1366, 1374), (1385, 1502)]),
    ('snapshot-supp2/pa19-ms09-b3-structural-parent-v1.md', 'snapshot-supp2/pa19-ms09-b3-structural-parent-v1.md', None),
    ('lane/cycle2/structural-ms09-b00003-proof.json (worker)', 'snapshot-supp3/lane/cycle2/structural-ms09-b00003-proof.json', None),
    ('lane/cycle2/m2part_drat/ms09_b00003/ext.json', 'snapshot-supp1/lane/cycle2/m2part_drat/ms09_b00003/ext.json', None),
    ('review/pa19-parent-cover-replay-v1/cover-binding-result.json',
     'snapshot/review/pa19-parent-cover-replay-v1/cover-binding-result.json', None),
    ('review/pa19-ms06-placement-binding-v2/result.json', 'snapshot/review/pa19-ms06-placement-binding-v2/result.json', None),
    ('review/pa19-subcase-binding-v1/README.md', 'snapshot/review/pa19-subcase-binding-v1/README.md', None),
    ('review/pa19-cover-scout-audit-v1.md', 'snapshot/review/pa19-cover-scout-audit-v1.md', [(1, 14), (74, 100)]),
    ('review/pa19-encoder-scout-audit-v1.md', 'snapshot/review/pa19-encoder-scout-audit-v1.md', [(1, 9), (42, 99)]),
]
DIFFS = [
    ('DIFF lane/src/extend_p1.py -> lane/src/extend_p1q.py', 'snapshot/lane/src/extend_p1.py', 'snapshot/lane/src/extend_p1q.py'),
    ('DIFF lane/src/encode_full.py -> lane/src/encode_full2.py', 'snapshot/lane/src/encode_full.py', 'snapshot/lane/src/encode_full2.py'),
    ('DIFF lane/src/aggregate15.py -> post-pin lane/src/aggregate16.py', 'snapshot/lane/src/aggregate15.py', 'snapshot-supp3/lane/src/aggregate16.py'),
    ('DIFF lane/src/summarize15.py -> post-pin lane/src/summarize16.py', 'snapshot/lane/src/summarize15.py', 'snapshot-supp3/lane/src/summarize16.py'),
]


def main():
    parts = [HEADER]
    for banner, rel, ranges in FILES:
        data = open(os.path.join(HERE, rel), 'rb').read()
        text = data.decode()
        lines = text.split('\n')
        sha = hashlib.sha256(data).hexdigest()
        rs = ranges or [(1, len(lines))]
        desc = ', '.join('%d-%d' % r for r in rs)
        parts.append('\n===== FILE %s (sha256 %s, %d lines; shown %s) =====\n' % (banner, sha, len(lines), desc))
        for a, b in rs:
            if ranges:
                parts.append('[... lines %d-%d ...]\n' % (a, b))
            for i in range(a, min(b, len(lines)) + 1):
                parts.append('%d|%s\n' % (i, lines[i - 1]))
    for banner, a, b in DIFFS:
        A = open(os.path.join(HERE, a)).read().split('\n')
        Bt = open(os.path.join(HERE, b)).read().split('\n')
        d = '\n'.join(difflib.unified_diff(A, Bt, a.split('/')[-1], b.split('/')[-1], lineterm='', n=1))
        parts.append('\n===== %s (unified diff, context 1; diff line numbers are the files\' own) =====\n%s\n' % (banner, d))
    parts.append('\n===== END OF INLINED TEXTS. Write your note now in the required format. =====\n')
    prompt = ''.join(parts)
    with open(OUT, 'x') as f:
        f.write(prompt)
    print(len(prompt.encode()), hashlib.sha256(prompt.encode()).hexdigest())


if __name__ == '__main__':
    main()
