# Independent checker I/O-boundary revision v2 (2026-10-19T08:26:58-0700)

New source: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v2.py, SHA256 9056dccb429239686356cd44721c07255cbc7d0bf8501fd9fd2a057af4479c7d. Base scientific checker remains preserved at
/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker.py, SHA256 e7e849627865db5c592507563b482a62873bd21413e0f46d4fec8bb5429e99a0.
Independent scientific algorithm authored by ContinueCFR21.CertChecker from the certificate specification alone.
Integration owner ContinueCFR21 changed ONLY the I/O boundary, added imports os/stat, and budget checks around final
publication. No producer code or mathematical helper is imported.

The EXACT source slice from FORMAT_TAG assignment through compute_facts, excluding the interface section, is
17,671 bytes in both files and SHA256 b2b8719207d7375189b982feacf0b8409220db14dab39d2da575f036009d9e56 in both.
This is a byte-comparison/hash statement only; neither source was run, compiled or syntax-parsed here.
Thus certificate schema/check0, G1 parsing/check1, equations, basis/check2, free-column identity/check3, rank/check4,
point reconstruction, rainbow/check5, failure/coverage/check6 and alpha_hat facts are byte-identical.

New read_capped_input:
- Open once with O_RDONLY|O_NONBLOCK|O_NOFOLLOW. A FIFO cannot block at open, and is rejected by descriptor fstat
  before read. Non-regular objects are ERROR, never an intended INVALID/check1 control outcome.
- Descriptor-bound cap+1 read in <=64KiB blocks, with actual accumulated-byte cap. Anchor1MiB, certificate8MiB.
  Pre-stat is not relied on for safety; file growth remains bounded by the bytes consumed. Hash and mathematical
  parse both use those exact returned bytes. No extra snapshot files or retained outputs are introduced.
- Budget ticks before/after every read and before returning the bytes. Overflow/read/deadline errors return ERROR2.
- finish checks before result publication and after its write/close. A late error preserves the exclusively created
  artifact but returns ERROR2 with a stdout ERROR report; the parent audit must reject any artifact/stdout mismatch.
  No output is silently overwritten or promoted from an artifact alone.

Original CLI/output keys and scientific INVALID reason strings remain unchanged for admitted regular small inputs.
No execution, control replay, configuration generation or supervisor assumption is authorized by this revision.
