# Focused second-pass review: prior-art correction

Read only files under `/Users/jinleic/jinleic-workspace/ai4s/phys-quantum-code-construction/`. No delegation, no file writes, no installs, no web calls, and no user-file reads outside this folder. The caller saves your answer. Do not run script entry points because they write reports. You may extract PDFs to stdout without creating files.

An earlier hostile Codex review, `review/codex-review.md`, found no mathematical error in the rational LP, stabilizer-parent lemma, known seven-qubit CWS exclusion, the exact 32-frame circulant search at n=11,d=4, or the two positive-control distances. That report is retained verbatim and its input hashes are in review/invocation.json.

WHILE that frozen review ran, the author found stronger prior art that the initial screening missed: Alex Rigby, JC Olivier, Peter Jarvis, Heuristic construction of codeword stabilized codes (2019), source/cws-exhaustive-1907.04537.pdf, sha256 0f8b1561f13cc79b26dda5aed4749e468e76caa90620df93a2a80277f39e596e. Section III.C says an exhaustive search of the LC graph classes at n=11,d=4 found 3060 graph classes with K=4 and none larger. The later n=12,d=4 search explicitly uses a heuristic PLS clique finder and must not be conflated with n=11. Table I uses all LC-isomorphism classes (n=11 count 45144, not just connected classes). Sections III.A and III.B also give CWS exclusions for (7,25 or 26,2) and (9,13,3).

README.md, STATUS.md and RESULTS.md have now been corrected:
- the 32-frame local certificate is labeled Certification/Reproduction, a strict subset of a stronger already-known CWS result;
- the initially recommended further non-vertex-transitive CWS search is withdrawn;
- general ((11,5,4)) still has a 4–7 gap in the 2026 rational-SDP table, so a constructive resolution must leave CWS, not merely break graph symmetry;
- no genuinely tractable unrestricted open instance was established, and that user criterion is explicitly unmet;
- no novel theorem/parameter record/global solution is claimed;
- the primary classification was not fully computationally replayed here, only the restricted 32-frame result.

Please verify the NEW primary-source interpretation and changed recommendation against the pinned 2019 PDF, then check these three docs for stale contradictory wording, unqualified novelty, or laundering the previous READY report into review of the later changes. Do not repeat the earlier mathematical/computational review. Check that the actual baseline/selection failure is stated honestly. Return READY / READY-WITH-FIXES / NEEDS-REWORK, any numbered real findings with file locations, and one concise accepted final formulation. The folder is frozen for this review. Maximal concision is welcome if no issues are found.
