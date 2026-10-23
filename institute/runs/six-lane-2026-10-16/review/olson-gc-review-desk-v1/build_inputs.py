"""Build the pinned review snapshot, manifest and both reviewer prompts for proof-GC.md (desk OlsonGCReviewDesk).

Exclusive creation only: every directory with mkdir(exist_ok=False), every file with mode 'x'/'xb'.  Lane O is only read.
Usage (cwd = review dir): /usr/bin/python3 -B olson-gc-review-desk-v1/build_inputs.py
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo

O = Path('/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson')
R = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review')
S = R / 'olson-gc-review-inputs-v1'
DESK = R / 'olson-gc-review-desk-v1'
P = 'inverse-run-count/mixdef-high'
TARGET = P + '/c6/proof-GC.md'
TARGET_PIN = 'f968a396facf396854662cbcb566c614e7e1e1dac415ca23ae70309878998425'
WITHHELD = 'olson-gc-parent-math-spot-v1.md'

# (relative path under olson/, role, review status, pin or None)
LANE = [
    (TARGET, 'TARGET: Lemma GEN (closed genericity criterion), Lemma GC (generic configuration at every run), Theorem NMH-iii',
     '[W] written, unreviewed; reviewed here', TARGET_PIN),
    (P + '/c6/proof-SEEDG-r2.md',
     "IMPORT: Sec. 0 setting (0.1'), (0.2'), Lemma H lam/lamc/U, (ARC), (CLAIM), Lemma P0, canonical lifts; Sec. 1 Lemma TS, seed "
     'Definition, (QS), actual-empty alternative, Lemma NW, Lemma GS (a)/(b); Secs. 2-3 Lemma SL, Lemma SCW-G (pin step), Lemma C0+, '
     'Theorem SEED-G (reached through the A0-r1 Corollary, case (b))',
     'parent CORRECTNESS-ACCEPTED at stated scope (review-notes/olson-c6-uniform-parent-verdict.md row "SEED-G r2"); r1 Codex and Claude '
     'ACCEPT-WITH-FIXES; r2 delta rated DELTA-ACCEPT-WITH-NOTES (review-notes/olson-c6g-r2-delta-v1/delta-check-v2.md)',
     '353b0e95c4e58d874038a11b5864514f4049753853d355015e27ebf7330130b7'),
    (P + '/c3/proof-C-r1.md',
     'IMPORT: Sec. 0 NMH setting and (0.1); Sec. 1 coordinates and Kill lemma; Sec. 2 Case A/B identities (2.1)-(2.3) (used by A0/C0-all)',
     'Codex ACCEPT for this file (review-notes/olson-c3-codex-review-v1.note.md per-file table; that note\'s overall REJECT concerns '
     'proof-NOBCplus.md only)', 'b5eb9fa7d511447d06b9d7b8abb406fff187f186bf5ae81a72e3f1ea9077b65b'),
    (P + '/c6/proof-A0-r1.md',
     'IMPORT: Lemma A0, Theorem C0-all, Corollary (count-free seed certificate) cases (a) and (b)',
     'parent CORRECTNESS-ACCEPTED (row "A0 and C0-all"; C0W accepted, so C0-all is no longer conditional in the NMH/lift setting); '
     'r0 Codex and Claude ACCEPT-WITH-FIXES; r1 changes read by the parent final delta (review-notes/olson-c6-final-parent-delta-v1/result.json)',
     'fba51b126e05e865c0af50de1d2572f569e46e0a941d6b3f88d796332eb781a0'),
    (P + '/c6/proof-C0WB-r2.md', 'IMPORT (through C0-all case (ii)): Lemma DF, Lemma C0W',
     'parent CORRECTNESS-ACCEPTED (row "DF / C0W / C0B"); r0 Codex and Claude ACCEPT-WITH-FIXES with no change to DF/C0W',
     '7900f468c3f0cb10a1c586972b784e4184bc737ce6ad9caa6710f7a6b0d036f1'),
    (P + '/c6/c5-fixes/proof-Cplus-r2.md', 'IMPORT (through C0-all cases (i), (iii)): steps (B1+), (B2+), refinement C4',
     'r1 Codex ACCEPT and Claude ACCEPT-WITH-FIXES; r2 C4 delta parent-verified (as recorded in proof-A0-r1.md dependency list)',
     '00e850cf10ed6a7dbea6f17928eef82321af7e8d63cb011940532b4e07848bd3'),
    ('inverse-parity/proof-PAR-K0.md',
     'IMPORT: Sec. 1 Lemma H (half windows) with its 07:39 correction; Sec. 2 Claim in the proof of Lemma BC (source of (CLAIM))',
     'Lemma H, Lemma BC, Theorem K0: Codex ACCEPT per review-notes/olson-par-mixlow-parent-verdict.md imports list; correction origin '
     'review-notes/olson-kbh-codex-review-v1.note.md', '4b107fffb766855d82a1c421707d426dc7fdc0a0ece77864a73d8db1ad5f9a38'),
    (P + '/README.md', 'DEFINITIONS: Sec. 1 MIX_DEF_HIGH(p) target, reductions, NMH(p); Sec. 2 frozen representation', 'definitions/context',
     '91ca37169af72cc273a6d524e95e8e0e93b00780d6f01d89b65b51df369069c1'),
    (P + '/c3/README.md', 'DEFINITIONS: Sec. 1 item (iii) := NMH words with R <= 2p-3 outside the ZSI-B case', 'definitions/context',
     'e8da2973ff55b0d0104b172884017f8ead0179fd3a315311d1e56babd566be03'),
    (P + '/proof-MH.md', 'SCOPE CONTEXT: Sec. 6 open items (i)-(iii), Lemma ZSI-B', 'context',
     'd742605f286d4b3e6e90c4a1d79e053a46c844bc393ee3dfc2daec728fe77012'),
    (P + '/c6/gc_controls.py', '[F] control script of the target (aid, never a premise; do not run)', 'producer aid, unreviewed',
     'a6c752163fee4e9a838983fe9647722d50296a3ffffb38746ad02c3d853604fc'),
    (P + '/c6/out/gc_controls.txt', '[F] receipt of gc_controls.py (aid, never a premise)', 'producer aid, unreviewed',
     '84c01c26871d86ee54452eeff81be80a65737acba6de0c46881d0745699cb572'),
    (P + '/c6/out/freeze.txt', 'freeze record (LF 330-333 pin proof-GC.md, gc_controls.py and its receipts)', 'producer record', None),
    (P + '/c6/README.md', 'producer log; Secs. 40-42 narrate the GC derivation and freeze (context, not premise)', 'producer log', None),
]
REVIEW = [
    ('olson-c6-uniform-parent-verdict.md', 'parent acceptance verdict for SEED-G r2, A0/C0-all, C0W (cycle 6)',
     'e5ac31d9f83ab71cda8af6c024f25d22f03f30b820089863b2a13dcde61c61ce'),
    ('olson-par-mixlow-parent-verdict.md', 'parent acceptance verdict for MIX_low/PAR; lists import review statuses (Lemma H etc.)',
     'c0ee2c467726abafaf50208b0c4c7b2881760fec714410bbfe59d97d6f7e42a1'),
    ('olson-c6-final-parent-delta-v1/result.json', 'parent final delta receipt for the six r1/r2 files', None),
    ('olson-c6g-codex-review-v1.note.md', 'Codex review of SEEDG r1', None),
    ('olson-c6g-claude-review-v1.note.md', 'Claude review of SEEDG r1', None),
    ('olson-c6g-r2-delta-v1/delta-check-v2.md', 'delegated delta check of SEEDG r1 -> r2', None),
    ('olson-uniform-codex-review-v1.note.md', 'Codex review of A0 r0 (T3) etc.', None),
    ('olson-uniform-claude-review-v1.note.md', 'Claude review of A0 r0 (T3) etc.', None),
    ('olson-c0wb-codex-review-v1.note.md', 'Codex review of C0WB r0', None),
    ('olson-c0wb-claude-review-v1.note.md', 'Claude review of C0WB r0', None),
    ('olson-c3-codex-review-v1.note.md', 'Codex review of c3 files (proof-C-r1.md ACCEPT)', None),
    ('olson-c5-codex-review-v1.note.md', 'Codex review of Cplus r1', None),
    ('olson-c5-claude-review-v1.note.md', 'Claude review of Cplus r1', None),
    ('olson-parity-k0-kplus-codex-review-v1.note.md', 'Codex review of PAR-K0/K+', None),
    ('olson-kbh-codex-review-v1.note.md', 'Codex review that triggered the Lemma H 07:39 correction', None),
]
# Claude packet: (path key, LF ranges inclusive, label).  Paths starting with 'review-notes/' are snapshot review copies.
CLAUDE_EXCERPTS = [
    (TARGET, [(1, None)], 'TARGET (whole file)'),
    (P + '/c6/proof-SEEDG-r2.md', [(1, 181)], 'IMPORT: header, Secs. 0-3 (setting, seeds, TS, NW, GS, SL, SCW-G, C0+, SEED-G)'),
    (P + '/c3/proof-C-r1.md', [(1, None)], 'IMPORT: whole file (Sec. 0 setting, Sec. 1 Kill lemma, Sec. 2)'),
    (P + '/c6/proof-A0-r1.md', [(1, None)], 'IMPORT: A0, C0-all, Corollary (whole file)'),
    (P + '/c6/proof-C0WB-r2.md', [(1, 72)], 'IMPORT: header, Sec. 0, Lemma DF, Lemma C0W'),
    (P + '/c6/c5-fixes/proof-Cplus-r2.md', [(1, 89)], 'IMPORT: header, Secs. 1-2 (B1+), (B2+), C4'),
    ('inverse-parity/proof-PAR-K0.md', [(1, 91)], 'IMPORT: Secs. 1-2 (Lemma H with correction, Lemma BC Claim)'),
    (P + '/README.md', [(1, 41)], 'DEFINITIONS: Secs. 1-2'),
    (P + '/c3/README.md', [(14, 28)], 'DEFINITIONS: Sec. 1 (item (iii))'),
    (P + '/proof-MH.md', [(171, None)], 'SCOPE CONTEXT: Sec. 6'),
    (P + '/c6/README.md', [(609, None)], 'PRODUCER LOG Secs. 40-42 (context only)'),
    (P + '/c6/out/gc_controls.txt', [(1, None)], '[F] receipt (aid only)'),
    ('review-notes/olson-c6-uniform-parent-verdict.md', [(1, None)], 'PARENT VERDICT (import statuses)'),
    ('review-notes/olson-par-mixlow-parent-verdict.md', [(1, None)], 'PARENT VERDICT (import statuses)'),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def mkdirs(root, rel_dir, made):
    cur = root
    for part in Path(rel_dir).parts:
        cur = cur / part
        if cur not in made:
            cur.mkdir(exist_ok=False)
            made.add(cur)


def section_c0w(text):
    """Return the Lemma DF and Lemma C0W paragraphs (from their bold labels to the closing '[]')."""
    out = []
    for label in ('**Lemma DF', '**Lemma C0W.**'):
        i = text.index(label)
        j = text.index('[]', i) + 2
        out.append(text[i:j])
    return out


def src_of(key):
    """Source path of a snapshot key (snapshot copies are byte-identical to these)."""
    return R / key[len('review-notes/'):] if key.startswith('review-notes/') else O / key


def plan():
    """Read and pin every source; build manifest and both prompts in memory; write nothing."""
    files, notes, blobs = {}, {}, {}
    for rel, role, status, pin in LANE:
        data = (O / rel).read_bytes()
        h = sha(data)
        if pin is not None and h != pin:
            raise SystemExit(f'PIN MISMATCH {rel}: {h}')
        blobs[rel] = data
        files[rel] = {'sha256': h, 'bytes': len(data), 'lf_lines': len(data.decode().split('\n')), 'source': str(O / rel),
                      'role': role, 'review_status': status, 'matches_pin': (pin == h) if pin else None}
    for rel, role, pin in REVIEW:
        if rel == WITHHELD:
            raise SystemExit('withheld file listed')
        data = (R / rel).read_bytes()
        h = sha(data)
        if pin is not None and h != pin:
            raise SystemExit(f'PIN MISMATCH {rel}: {h}')
        blobs['review-notes/' + rel] = data
        notes['review-notes/' + rel] = {'sha256': h, 'bytes': len(data), 'source': str(R / rel), 'role': role}
    freeze = (O / P / 'c6/out/freeze.txt').read_text().split('\n')
    freeze_hits = [(i + 1, l) for i, l in enumerate(freeze) if 'proof-GC.md' in l or 'gc_controls' in l]
    c0w = {v: section_c0w((O / P / f'c6/{v}').read_text()) for v in ('proof-C0WB.md', 'proof-C0WB-r1.md', 'proof-C0WB-r2.md')}
    c0w_identical = all(c0w[v] == c0w['proof-C0WB.md'] for v in c0w)
    manifest = {
        'label': 'olson-gc-review pinned inputs (desk OlsonGCReviewDesk): target proof-GC.md + direct imports + statuses',
        'recorded_at_pt': stamp(), 'source_root': str(O), 'snapshot_root': str(S),
        'line_convention': 'LF lines, 1-based index in text.split("\\n")',
        'write_policy': 'snapshot root and every subdirectory mkdir(exist_ok=False); every file opened xb; lane O read-only',
        'target': {'path': TARGET, 'sha256_pin': TARGET_PIN},
        'files': files, 'review_notes': notes,
        'excluded': {
            P + '/c6/proof-SEEDGstar-r2.md': 'not used by the target (proof-GC.md LF 18); Corollary case (c) is not invoked',
            P + '/c2/proof-C2.md': 'mentioned only as [I] (R >= 2p-2) in the target scope paragraph; not a premise',
            'other c6 region/E2 files': 'listed as NOT used by the target (proof-GC.md LF 18-20, 119-121)',
        },
        'desk_provenance_checks': {
            'freeze_txt_lines': freeze_hits,
            'lemma_DF_and_C0W_text_identical_r0_r1_r2': c0w_identical,
            'lemma_DF_and_C0W_text_sha256': {v: [sha(x.encode()) for x in c0w[v]] for v in c0w},
        },
    }
    manifest_text = json.dumps(manifest, indent=1) + '\n'
    prompts = {'olson-gc-review-codex-v1': codex_prompt(manifest), 'olson-gc-review-claude-v1': claude_prompt(manifest)}
    for label, text in [('manifest', manifest_text)] + list(prompts.items()):
        if WITHHELD in text or 'parent-math-spot' in text:
            raise SystemExit('withheld reference leaked into ' + label)
    sizes = {k: len(v.encode()) for k, v in prompts.items()}
    if sizes['olson-gc-review-claude-v1'] > 180_000:
        raise SystemExit(f'claude packet too large: {sizes}')
    for name in prompts:
        if (R / (name + '.prompt.txt')).exists():
            raise SystemExit('prompt exists: ' + name)
    return blobs, manifest_text, prompts, {'files': len(files), 'notes': len(notes), 'c0w_identical': c0w_identical,
                                          'freeze_hits': freeze_hits, 'prompt_bytes': sizes}


def main():
    dry = sys.argv[1:] == ['--dry-run']
    if sys.argv[1:] not in ([], ['--dry-run']):
        raise SystemExit('usage: build_inputs.py [--dry-run]')
    if S.exists():
        raise SystemExit('snapshot exists; refusing')
    blobs, manifest_text, prompts, info = plan()
    if dry:
        print(json.dumps({'dry_run': True, **info}, indent=1))
        return
    S.mkdir(exist_ok=False)
    made = {S}
    for key, data in blobs.items():
        mkdirs(S, str(Path(key).parent), made)
        with open(S / key, 'xb') as f:
            f.write(data)
        if (S / key).read_bytes() != data:
            raise SystemExit('copy mismatch ' + key)
    with open(S / 'manifest.json', 'x') as f:
        f.write(manifest_text)
    with open(DESK / 'desk-record.json', 'x') as f:
        json.dump({'recorded_at_pt': stamp(), 'manifest_sha256': sha(manifest_text.encode()),
                   'withheld_from_reviewers': {'review/' + WITHHELD: 'parent hand derivation; not in snapshot, manifest or '
                                                                      'prompts until both reviewer findings are final'}},
                  f, indent=1)
        f.write('\n')
    out = {}
    for name, text in prompts.items():
        with open(R / (name + '.prompt.txt'), 'x') as f:
            f.write(text)
        out[name] = {'bytes': len(text.encode()), 'sha256': sha(text.encode())}
    with open(DESK / 'prompts.json', 'x') as f:
        json.dump({'recorded_at_pt': stamp(), 'prompts': out}, f, indent=1)
        f.write('\n')
    print(json.dumps({'snapshot': str(S), **info, 'prompts': out}, indent=1))


COMMON_CONTEXT = """Context: dihedral ordered-Olson (EGZ-type) lane for D_(2p), p >= 5 prime; inverse statement RUNS(p), sub-target
MIX_DEF_HIGH(p) reduced to NMH(p) (P/README.md Sec. 1).  An NMH word is an all-odd RGR word of length 4p-2 (k rotation runs over
{r, r^-1} alternating cyclically with k constant reflection runs, every reflection run of odd length) with p+1 <= k <= 2p-2, every
rotation run pure aligned (a_t >= 1 letters r, d_t = a_t), pure anti (b_t >= 1 letters r^-1, d_t = -b_t) or a (1,1)-pair (d_t = 0),
1 <= B <= kappa-1, B <= A <= 2p-1 (normalized A >= B).  Avoidance = no 2p letters in increasing index order with product 1.
TARGET: P/c6/proof-GC.md (sha256 f968a396facf396854662cbcb566c614e7e1e1dac415ca23ae70309878998425), a NEW unreviewed written proof:
Lemma GEN (closed form |4m-(k+2)| + |2y-D| <= E + 2 Delta0 of "generic" from Lemma H with beta = 0), Lemma GC (for EVERY run t an
actual proper Q, t notin Q, Q+t proper, Q and Q+t both generic, via a walk inside a class of 2-colourings of the path of the other
k-1 runs), and Theorem NMH-iii (every NMH word with R <= 2p-3, every prime p >= 5, has an identity 2p-subword) obtained from GC plus
the parent-ACCEPTED imports Lemma GS (b)/NW/GS (a) and its actual-empty alternative (P/c6/proof-SEEDG-r2.md) and the count-free
Corollary of P/c6/proof-A0-r1.md (through Theorem C0-all, whose case (ii) uses Lemma C0W of P/c6/proof-C0WB-r2.md, accepted).
No finite census or table is claimed as a premise.  Import statuses: see the two parent verdicts and the manifest.  You may rely on
parent-accepted imports AT THEIR EXACT STATED SCOPE, but you must check that the target uses each one inside its hypotheses.

REQUIRED OUTPUT.  The first line must be exactly one of
DISPOSITION: ACCEPT
DISPOSITION: ACCEPT-WITH-FIXES
DISPOSITION: REJECT
(overall, for the target).  Then sections FATAL, MAJOR, MINOR (write "none" if empty).  Each finding: path:LF-line (LF-line =
1-based index in text.split('\\n') of that file), what is wrong, the exact corrected statement/bound/wording, and an explicit
counterexample or hand computation whenever you assert a failure (explicit p, k, kappa, B, run weights d_t in cyclic order, target
run t, pattern Q).  Then short answers to Q1-Q5 below, each with the key hand computation.  End with counts (FATAL/MAJOR/MINOR) and a
short separate paragraph distinguishing correctness, novelty and significance (no novelty or priority search is requested; make no
firstness claim).  [F] controls are aids only, never premises; solutions of relaxed window/arc systems are not group
counterexamples.  The target claims no NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered-Olson theorem; flag any text
that overreaches.

REVIEW QUESTIONS (answer every item; cite path:LF-line; do the arithmetic by hand).
Q1 Lemma GEN (P/c6/proof-GC.md Sec. 2).  Re-derive the four floor-term conditions (i)-(iv) from lam/lamc (P/c6/proof-SEEDG-r2.md
   Sec. 0, Lemma H with beta = 0), their doubled forms, the parity elimination with th = [y+B odd], th' = [A-y odd] for BOTH parities
   (is the replacement by 2kB+B+1 <= 2m+y <= 2p-B+1 and 2kappa+1-A <= 2m-y <= 2p-A+1 an exact equivalence, not just an implication?),
   the centres/lengths, a1+a2 = 4m-(k+2) and a1-a2 = 2y-D via (1.1)/(0.1'), and the max/abs identity.  Check the complement symmetry
   (1.2) (m(Q^c) = m, D_(Q^c) = D-y) and the domain: proper Q only, every integer y, every 1 <= m <= k/2, all signs.  Is Lemma GEN
   EXACT (iff) in every integer and boundary case?  If not, give a tuple (p, k, kappa, B, E, m, y) where it fails.
Q2 Lemma GC construction (Sec. 3).  For EVERY k >= 7: m = floor((k+4)/4), c = |4m-(k+2)| by the residue of k+2 mod 4, 2 <= m,
   2m <= k-2 = L-1; non-adjacency of r_1, r_L; cyclic blocks of X(chi) and Y(chi) equal the path blocks (both exactly m); properness
   of Q = X(chi) and Q+t = [k]-Y(chi); the use of (1.2); D_X + D_Y = D - d.  chi0 = block lengths (1,...,1, L-2m+1); chi* = colour
   exchange then recolour position 1 by X and position L by Y: verify chi* is in C (compute its block lengths and its boundary vector
   b* explicitly), and (3.2) v(chi0)+v(chi*) = D - d + d_(t+1) - d_(t-1).  The walk: strict monotonicity in BOTH passes, exactly one
   recoloured position per unit move, first/last colours preserved, every intermediate colouring in C with exactly m X-blocks and m
   Y-blocks.  Confirm or refute that Lemmas TS and GS need no isolation of t from Q (Q may contain t+1).
Q3 Window and crossing.  Derive (3.1) (lo, hi with ceil/floor and max(0, +-d)) exactly; inequality (S) for a pure target and for a
   pair target (d = 0, e_t = 1), and hi - lo + 1 >= W' - |d|; inequality (M) and (3.3) for every sign of d; the crossing argument
   (no step jumps the window; endpoints force a crossing).  Check edge cases explicitly: pure aligned, pure anti and pair targets;
   E = 0 and E >= 4; the smallest case k = 7 (p = 5) and p = 7; each residue of k mod 4 (c = 0, 1, 2); parity of D +- W'.  Remark (3):
   compute the EXACT number of unit moves of the specified walk from chi0 to chi* (derive b* and count; is the second pass ever
   used?) and judge whether "linear in the word" and the stated bound (2m-1)(L-2) are correct and mutually consistent.
Q4 Invocation (Sec. 4).  Does GS (b)'s definition of generic (lambda(P) and lambda(P^c) both equal their floor terms) match the
   target's?  Does GS (b) need anything beyond Q, Q+t proper, t notin Q, both generic?  Does NW supply exactly the no-wrap hypothesis
   of GS (a)?  The "empty GS (a) interval => w does not avoid" step: compare with the seed Definition (which requires a_t <= b_t),
   the actual-empty alternative of SEEDG-r2 (Definition parenthetical, Theorem SEED-G, Remark (1)) and case (a) of the A0-r1
   Corollary; do NOT conflate an empty (QS) window with an empty interval computed from an actual configuration.  Is case (b)
   (quality seeds from actual configurations at EVERY run) met, and are ALL other hypotheses of the Corollary and of Theorem C0-all
   (canonical lifts, SCW-G with its pin step, SL, C0W at its accepted scope; no count condition, no defect bound) satisfied?  List
   every NMH hypothesis the imports need (k >= p+1, all reflection runs odd/beta = 0, pure or (1,1) runs, 1 <= B <= kappa-1,
   B <= A <= 2p-1, R <= 2p-3 i.e. Delta0 >= 3, (0.1) k >= 2kappa+3) and say where each holds.  The imports are about NMH words,
   not arbitrary dihedral words.
Q5 Scope and overclaim.  The theorem should be exactly: all normalized NMH words with R <= 2p-3 (item (iii) plus ZSI-B), every prime
   p >= 5 -- not NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR, INV, INV* or ordered Olson.  Check every scope/status sentence (LF 1-20,
   103-124) and the Remarks (e.g. Remark (1)'s list of what is used) for overreach or omission; confirm that no finite control, the
   E2 315-row table, or any census is a premise; check that every cited path resolves under the stated convention ("Paths are
   relative to mixdef-high/").  If you find any gap, give an explicit counterexample or a concrete repair.
"""


def codex_prompt(manifest):
    return ("""Hostile independent STATIC proof audit of one new written result in the dihedral ordered-Olson RUNS lane.

SNAPSHOT (read ONLY inside it): S = """ + str(S) + """
Do not open, list or search any path outside S.  S/manifest.json lists every file with sha256, role and review status.
P := inverse-run-count/mixdef-high (paths below are relative to S).  STATIC ONLY: you may read files and verify sha256
(shasum -a 256); do NOT run python or any other program, solver or compiler; no network, no writes, no delegation.  All
mathematical checks are by hand reasoning.  First verify the target hash; on mismatch output "DISPOSITION: SNAPSHOT-MISMATCH" and
stop.
 TARGET P/c6/proof-GC.md  f968a396facf396854662cbcb566c614e7e1e1dac415ca23ae70309878998425
IMPORTS (status in S/manifest.json and the parent verdicts S/review-notes/olson-c6-uniform-parent-verdict.md,
S/review-notes/olson-par-mixlow-parent-verdict.md; earlier review notes are in S/review-notes/):
 - P/c6/proof-SEEDG-r2.md (353b0e95...30b7): Sec. 0 (0.1'), (0.2'), lam/lamc/U, (ARC), (CLAIM), P0, canonical lifts; Sec. 1 TS,
   seed Definition, (QS), actual-empty alternative, NW, GS (a)/(b); Secs. 2-3 SL, SCW-G (pin), C0+, SEED-G.  Parent-accepted.
 - P/c6/proof-A0-r1.md (fba51b12...): A0, C0-all, Corollary cases (a), (b).  Parent-accepted (C0W accepted).
 - P/c6/proof-C0WB-r2.md (7900f468...): Lemma DF, Lemma C0W.  Parent-accepted.
 - P/c3/proof-C-r1.md (b5eb9fa7...): Sec. 0 setting, Kill lemma (Sec. 1), Sec. 2 identities.  Codex ACCEPT.
 - P/c6/c5-fixes/proof-Cplus-r2.md (00e850cf...): (B1+), (B2+), C4.  Reviewed (see manifest).
 - inverse-parity/proof-PAR-K0.md (4b107fff...): Lemma H with its 07:39 correction, Claim of Lemma BC.  Codex ACCEPT.
 - Definitions: P/README.md Secs. 1-2; P/c3/README.md Sec. 1; P/proof-MH.md Sec. 6.
 - [F] aids only (never premises; read only if useful, never run): P/c6/gc_controls.py, P/c6/out/gc_controls.txt.
   P/c6/README.md Secs. 40-42 are the producer's log (context only).
""" + COMMON_CONTEXT)


def claude_prompt(manifest):
    head = ("""You are a hostile, independent mathematical referee.  You have NO tools: everything you need is inlined below.  Hashes were
computed by the review desk; you cannot verify them.  Every file excerpt is LF-numbered: "L<n>: " precedes original LF line n
(1-based index in text.split('\\n')); cite findings as path:L<n>.  Paths are relative to olson/ (P := inverse-run-count/mixdef-high).
Be thorough but economical: prioritise the review questions, do the arithmetic by hand, and keep the final note focused.
""" + COMMON_CONTEXT + "\nINLINED SOURCES FOLLOW.\n\n")
    parts = [head]
    for key, ranges, label in CLAUDE_EXCERPTS:
        if key.startswith('review-notes/'):
            meta = manifest['review_notes'][key]
        else:
            meta = manifest['files'][key]
        lines = src_of(key).read_text().split('\n')
        n = len(lines)
        spans = [(a, n if b is None else b) for a, b in ranges]
        span_txt = ', '.join(f'{a}-{b}' for a, b in spans)
        parts.append(f"=== FILE {key}  (sha256 {meta['sha256']}; {n} LF lines; included LF lines {span_txt}) -- {label}\n")
        for a, b in spans:
            for i in range(a, b + 1):
                parts.append(f'L{i}: {lines[i - 1]}\n')
        parts.append(f'=== END FILE {key}\n\n')
    parts.append('END OF PACKET.  Now write the review in the REQUIRED OUTPUT format.\n')
    return ''.join(parts)



if __name__ == '__main__':
    main()
