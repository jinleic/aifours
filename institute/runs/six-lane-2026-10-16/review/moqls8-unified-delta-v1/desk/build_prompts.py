"""Build the two reviewer prompts for the unified one-P4 delta audit from the pinned snapshot.
Creates (exclusively): R/<CLAUDE>.prompt.txt, R/<CODEX>.prompt.txt, desk/gmap_extract.json, desk/PROMPTS_PIN.json.
Usage: python3 -B build_prompts.py
"""
import hashlib
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent.parent          # R/moqls8-unified-delta-v1
R = HERE.parent
SNAP = HERE / 'snapshot'
CLAUDE = 'moqls8-unified-delta-claude-v1'
CODEX = 'moqls8-unified-delta-codex-v1'
LANE_REL = 'LANE/'
ARGV_CAP = 900_000

ROLES = [
    ('OVL', 'target: versioned review-repair overlay r1 (N8_UNIFIED_REVIEW_REPAIRS.r1.md)'),
    ('BR2', 'frozen unified bridge r2 (unchanged by OVL)'),
    ('DEL', 'frozen deletion spec v1 (unchanged by OVL)'),
    ('CL1', 'prior Claude review: 7 bridge + 3 deletion MINORs'),
    ('CX1', 'prior Codex review: ACCEPT, zero findings'),
    ('TPL', 'template-cover proof r1 (proof used by T16)'),
    ('LINK', 'semantic repair/generation link JSON'),
    ('RCPT', 'byte-filter verification receipt (VER run 2026-10-18 00:04:37 PDT)'),
    ('RECIPE', 'base recipe written by PROD'),
    ('VER', 'byte-filter verifier code'),
    ('PROD', 'producer code (byte filter + 16-case manifest)'),
    ('WMAN', 'weakened 16-case manifest (F_one + 42 units per case)'),
    ('SMAN', 'old-F (strong) 16-case manifest from which PROD copies cases'),
    ('GA', 'encoder gram_a.py that emitted old F'),
    ('ENC', 'accepted encoding-soundness note r3'),
    ('IMP', 'residual normal form r3 imports'),
    ('SEM', 'earlier generic semantic review repairs r1'),
    ('PV', 'parent A8 verdict (correctness-accepted partial result)'),
    ('SRC', 'Ball-Simoens arXiv:2607.12933v2 raw text'),
    ('RM', 'lane README (hashed as found; strict predicate at 216-224; sections 11-12 at 350-427)'),
    ('GMAP', 'encoder variable map GA5L_K5_sb2.map.json'),
]
RM_EXCERPTS = [(179, 232), (350, 427)]

HEADER = """Hostile independent STATIC delta audit, before any of 16 weakened-template refutations is spent, of a versioned review-repair overlay in a computer-assisted proof attempt (Ball-Simoens arXiv:2607.12933v2, Problem 16 at n = 8: is every set of five MOQLS(8) classical?). You give NO theorem verdict (the parent decides) and no novelty or significance judgement.

First line exactly:
DISPOSITION: DELTA=<ACCEPT|ACCEPT-WITH-FIXES|REJECT>; Q1=<CLOSED|PARTIAL|OPEN>; Q2=<PASS|PASS-WITH-FIXES|FAIL>; Q3=<PASS|PASS-WITH-FIXES|FAIL>; Q4=<PASS|PASS-WITH-FIXES|FAIL>; Q5=<PASS|PASS-WITH-FIXES|FAIL>
Then sections FATAL, MAJOR, MINOR (write "none" if empty). Each finding: an id, exact KEY:LF-line(s) using the keys below, the defect, why it matters, and an exact correction (or an explicit counterexample). Severity: FATAL = the conditional implication or a cited fact is false; MAJOR = a load-bearing step, hypothesis or gate is missing or unproved; MINOR = wording, pins or evidence labelling that does not change the mathematics. Then answer Q1-Q5 briefly with KEY:line citations, separating what you verified by reading from reported provenance. End with `DELTA FATAL=<n> MAJOR=<n> MINOR=<n>`. Be decisive and concise (at most about 2,500 words).

Context. Old F = base CNF evidence/gram_dev_v1/GA5L_K5_sb2.cnf (SHA-256 6ecb77a7...469b; 509,915 variables; 5,740,230 clauses), emitted by GA = code/gram_a.py with `--order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --g5 --rowlex`. F_one = F minus exactly the four row-0-frame P4 at-least-one (ALO) clauses of squares 2-5 (zero-based clause indices 5735297, 5736866, 5738435, 5740004), keeping Q1's ALO (index 5733728) and every other clause byte and order. Bridge BR2 and deletion spec DEL were frozen about 2026-10-17 23:34 PDT. Earlier static reviews: CL1 (Claude) = ACCEPT-WITH-FIXES with 7 bridge MINORs (CL1:31-75) and 3 deletion MINORs (CL1:83-99); CX1 (Codex) = ACCEPT with zero findings. The overlay OVL (2026-10-18 00:06 PDT) claims to close all 10 CL1 MINORs without editing BR2/DEL, restates the template theorem in property form (T16), fixes the canonical auxiliary values, and records byte-filter generation evidence (VER run at 00:04:37 PDT, receipt RCPT). The 16 refutations (F_one + 42 units each, WMAN) have NOT been run.

Questions.
Q1. Does OVL close each of the 10 CL1 MINORs (BR2 m1-m7, DEL m1-m3) without reopening any earlier finding (CL1, CX1, or the generic repairs SEM/IMP/ENC)? Give a per-MINOR verdict (closed / partial / not) with OVL:line.
Q2. PROPERTY-FORM T16 (OVL:13-30, with the moves at OVL:32-43 and the proof in TPL sections 1-4). From ONLY the stated hypotheses (five genuine pairwise-orthogonal row0-aligned QLS(8); (1,0) supports A={1,2,3},{4},{5},{6},{7} in square order; unitary Q1 column-0 transition U with row and column degree <= 3), do the common column/coordinate permutations in Sym(A)xSym(B), the relabelling of squares 2-5 and the common sort of rows 2-7 really force one of the SIXTEEN column-0 support lists (TPL:84-104; WMAN supports_row2to7)? Look for hidden reliance on reduced-K5 membership, P4 on squares 2-5, non-classicality, or the old 13-case/c112 interface; for normalisation moves that break alignment or the support assumptions; and for any missed or wrongly canonicalised list. Check the component theorem (TPL:22-55) and every canonical choice (TPL:57-109) against the exact ROWLEX key (GA:248-270; coordinate 0 most significant, False<True, ascending non-strict).
Q3. OVL section 3 (OVL:45-57) canonical auxiliary extension: is every retained clause of F_one plus the template units (G2; G3 with its b3 ANDs; G4 with c4; G5 with u5; P4 one-way w3 implications and Q1's kept ALO; ROWLEX with lexeq; SB2 units; the 42 units) satisfied by the stated canonical values whenever the vectors meet the hypotheses (a genuine aligned five-set after the OVL section 2 moves and T16)? Use GA (CNF.add/AND 39-80, g() 127-138, G2 150-153, G3 179-190, G4 191-206, G5 207-232, P4 233-247, ROWLEX 248-270, SB2 271-281). Is deleting exactly the four ALOs of squares 2-5 safe, i.e. sound for arbitrary (classical or not) squares 2-5, and is nothing else needed?
Q4. Byte filter. Do RCPT and the code (VER, PROD), with RECIPE, WMAN and LINK, actually bind: the 4 deleted clauses (index, line SHA and 56-flag meaning); Q1's kept ALO; the 5,740,226 retained clauses byte-for-byte in order; the headers `p cnf 509915 5740230\\n`, `p cnf 509915 5740226\\n` and `p cnf 509915 5740268\\n`; and the 16 x 42-unit cases with their leaf SHAs? State exactly which facts are checked on a second path, which only by the producer's own code path, and which are not checked at all (for example identity of WMAN's support lists with TPL's lists, the g-variable map, header bytes). Is the claim limited correctly (generation/identity evidence, not a refutation, not a parent replay)?
Q5. The six-gate conditional conclusion (OVL:90-115, with BR2:91-101). Are these gates exactly sufficient for the implication "every set of 5 MOQLS(8) is classical" (SRC:642, n-3 = 5), and is anything missing: classical-case handling, any requirement on all five squares, the A8 premise scope (PV:13; BR2:38-39) and W8, the encoder/CNF/variable-map binding, the exact strict-refutation predicate and checker, or the identity of the 16 pinned lists with T16's lists?
"""

CLAUDE_INTRO = """
No tools: audit only the exact LF-numbered packet below. Each FILE header gives KEY, the path (LANE/ = physics/evidence/six-lane-20261016/moqls8-problem16/, RUN-R/ = institute/runs/six-lane-2026-10-16/review/), the SHA-256 of the COMPLETE file, and whether the block is complete or an excerpt. Line numbers are LF-split positions (split on newline, 1-based) of the complete file; excerpts keep the original numbers. A block marked [F] is a desk extract: an aid, never a premise. Static audit only: no execution, no SAT, no claim about Problem 16.

"""

CODEX_INTRO = """
Read-only STATIC audit. The pinned snapshot below holds byte-identical copies of the lane/run files (their source paths are listed in {snap_manifest}), so line numbers coincide with the originals. First verify every SHA-256 below with `shasum -a 256`; stop and report on any mismatch. Read the files yourself. You may run sha256 checks and tiny stdlib Python one-liners (under 60 s and 1 GiB) over the snapshot. Do not execute lane code, do not open or hash the 137 MB CNF or the compressed name table, no SAT solving, no network, no file writes. Cite as KEY:line.

"""


def sha(b):
    return hashlib.sha256(b).hexdigest()


def numbered(text, ranges=None):
    lines = text.split('\n')
    out = []
    if ranges is None:
        ranges = [(1, len(lines))]
    for a, b in ranges:
        for n in range(a, b + 1):
            out.append(f'{n}: {lines[n - 1]}')
        out.append('')
    return '\n'.join(out), len(lines)


def main():
    man = json.loads((HERE / 'SNAPSHOT_MANIFEST.json').read_text())
    files = {}
    for row in man['files']:
        p = HERE / row['snapshot']
        data = p.read_bytes()
        if sha(data) != row['sha256']:
            raise SystemExit('snapshot changed: ' + row['key'])
        files[row['key']] = (row, data)
    assert [k for k, _ in ROLES] == [r['key'] for r in man['files']] or set(k for k, _ in ROLES) == set(files)

    # desk extract of the variable map for the tool-less reviewer
    grow, graw = files['GMAP']
    gm = json.loads(graw)
    g = {}
    for k, v in gm['vars'].items():
        n = json.loads(k)
        if n[0] == 'g':
            g[(n[1], tuple(n[2]), tuple(n[3]))] = v
    extract = {'kind': '[F] desk extract of LANE/evidence/gram_dev_v1/GA5L_K5_sb2.map.json (aid, not premise)',
               'map_sha256': grow['sha256'], 'meta': gm['meta'],
               'g_variable_count': len(g),
               'g_1((0,c),(i,0)) for i=2..7 (rows), c=1..7 (columns)':
                   {str(i): [g[(1, (0, c), (i, 0))] for c in range(1, 8)] for i in range(2, 8)},
               'g_s((0,c),(1,0)) for s=1..5, c=1..7 (SB2 variables)':
                   {str(s): [g[(s, (0, c), (1, 0))] for c in range(1, 8)] for s in range(1, 6)}}
    ext_path = HERE / 'desk/gmap_extract.json'
    with ext_path.open('x') as fh:
        json.dump(extract, fh, indent=1)
        fh.write('\n')
    ext_bytes = ext_path.read_bytes()

    roles = dict(ROLES)
    # ---------- Claude packet ----------
    parts = [HEADER, CLAUDE_INTRO, 'KEYS: ' + '; '.join(f'{k} = {roles[k]}' for k, _ in ROLES if k != 'GMAP')
             + '; GMAPX = [F] desk extract of the encoder variable map.\n\n']
    order = ['OVL', 'CL1', 'CX1', 'BR2', 'DEL', 'TPL', 'LINK', 'RCPT', 'RECIPE', 'VER', 'PROD', 'WMAN', 'SMAN',
             'GA', 'ENC', 'IMP', 'SEM', 'PV', 'SRC', 'RM']
    for key in order:
        row, data = files[key]
        src = row['source']
        label = src.replace('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/', LANE_REL)
        label = label.replace('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/', 'RUN-R/')
        text = data.decode('utf-8')
        if key == 'RM':
            body, n = numbered(text, RM_EXCERPTS)
            kind = 'EXCERPT lines ' + ', '.join(f'{a}-{b}' for a, b in RM_EXCERPTS) + f' of {n} LF-split lines'
        else:
            body, n = numbered(text)
            kind = f'complete; {n} LF-split lines'
        parts.append(f'FILE {key} {label} sha256 {row["sha256"]} ({kind})\n{body}\n')
    body, n = numbered(ext_bytes.decode('utf-8'))
    parts.append(f'FILE GMAPX [F] RUN-R/moqls8-unified-delta-v1/desk/gmap_extract.json sha256 {sha(ext_bytes)} '
                 f'(complete; {n} LF-split lines)\n{body}\n')
    parts.append('END OF PACKET. Remember: the first line of your answer must be the DISPOSITION line.\n')
    claude_prompt = ''.join(parts)

    # ---------- Codex prompt ----------
    rows = []
    for key, role in ROLES:
        row, _ = files[key]
        rows.append(f'- {key}: {HERE / row["snapshot"]} | sha256 {row["sha256"]} | {role} | original {row["source"]}')
    codex_prompt = (HEADER + CODEX_INTRO.format(snap_manifest=HERE / 'SNAPSHOT_MANIFEST.json') + 'Pinned files:\n'
                    + '\n'.join(rows) + '\n\nRemember: the first line of your answer must be the DISPOSITION line.\n')

    out = {}
    for name, text in ((CLAUDE, claude_prompt), (CODEX, codex_prompt)):
        b = text.encode('utf-8')
        if len(b) > ARGV_CAP:
            raise SystemExit(f'{name} prompt too large for argv: {len(b)}')
        p = R / f'{name}.prompt.txt'
        with p.open('xb') as fh:
            fh.write(b)
        out[name] = {'path': str(p), 'bytes': len(b), 'sha256': sha(b)}
    pin = {'built_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
           'builder_sha256': sha(Path(__file__).read_bytes()), 'snapshot_manifest_sha256':
               sha((HERE / 'SNAPSHOT_MANIFEST.json').read_bytes()),
           'gmap_extract_sha256': sha(ext_bytes), 'prompts': out}
    with (HERE / 'desk/PROMPTS_PIN.json').open('x') as fh:
        json.dump(pin, fh, indent=1)
        fh.write('\n')
    print(json.dumps(pin, indent=1))


if __name__ == '__main__':
    main()
