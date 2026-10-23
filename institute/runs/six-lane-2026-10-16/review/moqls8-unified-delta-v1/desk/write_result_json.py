"""Write RESULT.json (exclusive create) for the moqls8 unified one-P4 delta audit. Values were read from the
pinned snapshot, the two reviewer notes/receipts and the desk outputs; hashes are recomputed here where files exist.
Usage: python3 -B write_result_json.py
"""
import hashlib
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent.parent
R = HERE.parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def first_line(p):
    return Path(p).read_text().split('\n', 1)[0]


def last_tally(p):
    lines = [x for x in Path(p).read_text().split('\n') if x.startswith('DELTA FATAL=')]
    return lines[-1] if lines else None


def reviewer(name, runner):
    rec = json.loads((R / f'{name}.receipt.json').read_text())
    files = {k: R / f'{name}.{k}' for k in ('prompt.txt', 'note.md', 'receipt.json')}
    for k in ('stdout.txt', 'stderr.txt', 'stdout.json'):
        if (R / f'{name}.{k}').exists():
            files[k] = R / f'{name}.{k}'
    gate = json.loads((HERE / 'desk' / f'gate_{name}.json').read_text())
    return {'name': name, 'runner': runner, 'runner_sha256': rec['runner_sha256'],
            'requested_model': rec['requested_model'], 'requested_effort': rec['requested_effort'],
            'status': rec['status'], 'duration_seconds': round(rec['duration_seconds'], 2),
            'started_at_pt': rec['started_at_pt'], 'finished_at_pt': rec['finished_at_pt'],
            'reported_identity': rec.get('reported_identity') or rec.get('reported_init_models'),
            'output_tokens': (rec.get('reported_model_usage', {}).get('claude-opus-5-5', {}) or {}).get('outputTokens'),
            'files_sha256': {k: sha(v) for k, v in files.items()},
            'receipt_note_sha256': rec.get('note_sha256'),
            'disposition_line': first_line(files['note.md']), 'tally': last_tally(files['note.md']),
            'disk_gate': {'checked_at_pt': gate['checked_at_pt'], 'free_bytes': gate['free_bytes'],
                          'required': gate['floor'] + gate['projected_growth'], 'pass': gate['pass']}}


TASK_PINS = {
    'LANE/review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md': 'c391a67ab7cb468c2500dd4fc0d565fa4e104b97777a5bab668ed5fdc82ebbb3',
    'LANE/evidence/UNIFIED_ONE_P4_DELETIONS_v1.json': '4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6',
    'LANE/review/N8_UNIFIED_REVIEW_REPAIRS.r1.md': 'e0f3c860aaa81dd7b8214aabb84f5094fcaf425a6a17a01159d3aa779a9d1704',
    'LANE/evidence/N8_UNIFIED_SEMANTIC_REPAIR_LINK_v1.json': '483dcdb6e0f80a80da07e51d32bf50514fb63d888d102a8004359c2c17298608',
    'LANE/evidence/n8_one_p4_templates_v1/BYTE_FILTER_VERIFICATION_v1.json': '65aafe0ad577645036c6cc15e4f4705f0bb19a4f5e8eed2867954da8d761cc88',
    'LANE/evidence/n8_one_p4_templates_v1/BASE_RECIPE.json': '264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18',
    'LANE/code/verify_one_p4_deletion.py': '825c3cd7fabfd2efe25ff9e21f1044bed09c32a58e6be92aa63a3961e2893016',
    'LANE/code/n8_one_p4_formula.py': '61eda23ce7174e7cee77ee873ff06e5f22a2beaf0c197b8282f41dc8ddded400',
    'LANE/review/K5_COLUMN0_TEMPLATE_COVER.r1.md': '1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a',
    'LANE/review/K5_SEMANTIC_REVIEW_REPAIRS.r1.md': '413951379f248a87e02b52dfb942fb131f25524557c35adf9c54f68981b31022',
    'LANE/review/K4K5_ENCODING_SOUNDNESS.r3.md': 'a83d305013fa920d1ffe361d6d0aeb589f958da477420b2b053a503221858e59',
    'LANE/review/K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md': '34e11e52c28a798eb378c397097dbccaa753aca74d54e8ccbf6465b2088177d4',
    'LANE/evidence/n8_one_p4_templates_v1/MANIFEST.json (weakened 16-case, located)': '355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74',
    'LANE/sources/2607.12933v2.raw.txt (located)': '265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9',
    'R/moqls8-k5nf-unified-claude-v1.note.md': '6200c8d7b72a0335d1bd2bc11b98226ea4439d64ce7ab425fd3d7468477d98f5',
    'R/moqls8-k5nf-unified-codex-v1.note.md': 'e439c8c0f2c14b5dbf5a3ddc881966495372d7610c784ef54370f8439a47bdb3',
    'R/moqls8-k1k2-parent-verdict.md': '919daeac811bd551c4165ba415f9c6835b564adcb9bb6fcde1969307f2caa8f9',
}

FINDINGS = [
    {'id': 'F1', 'severity': 'MINOR', 'questions': ['Q4', 'Q1:DEL-m2'],
     'sources': ['Claude D-m1', 'desk', 'Codex Q4 states the same boundary without classifying it as a finding'],
     'lines': ['OVL:81-86', 'LINK:19', 'RCPT:16,18', 'VER:1', 'VER:37-42', 'VER:90', 'VER:99-100', 'PROD:31-40',
               'PROD:80-81', 'RECIPE:13-19,46-47'],
     'defect': ('The F_one SHA 374d6fb4..., the header bytes "p cnf 509915 5740226\\n" and "p cnf 509915 5740268\\n" and '
                'all 16 leaf SHAs are computed only by the producer Formula class (PROD:33,38) and re-observed '
                'in the same process by VER (VER:40 compares f.sha with a constant; VER:90 calls f.leaf_sha). RCPT:16,18 '
                'are string literals written by VER:99-100. VER re-reads DEL without re-hashing it (VER:42; PROD:45 '
                'hashed it once in-process), never compares the rebuilt recipe r with BASE_RECIPE, RECIPE:46-47 are '
                'hard-coded True (PROD:80-81), and VER:1 calls itself an "Independent traversal check". The genuinely '
                'second-path checks are the body traversal, source header/CR/comment checks, the 4 deleted and Q1 '
                'hashes, the name-table domains and the unit reconstruction (VER:43-89). CL1:89 asked for an '
                'independently streamed F_one SHA pinned beforehand; that was not done.'),
     'correction': ('Reword OVL:86 and LINK:19: "second-path body traversal and unit reconstruction; header bytes, '
                    'F_one SHA and leaf SHAs recomputed only by the producer Formula (same code path)". Gate 5 '
                    'regeneration must recompute sha256(header + retained body + "%d 0\\n" units) with an independent '
                    'implementation and compare with every WMAN cnf_sha256 (or a VER v2 doing so with its own hashlib, '
                    'also asserting sha256(DEL) and RECIPE == r).'),
     'blocks_spending_runs': False},
    {'id': 'F2', 'severity': 'MINOR', 'questions': ['Q2', 'Q4', 'Q5'],
     'sources': ['Claude D-m2', 'desk', 'Codex Q4 lists the same items as "not checked by VER/PROD" and checked them'],
     'lines': ['OVL:23-24', 'OVL:29-30', 'OVL:105-108', 'PROD:97-101', 'VER:65-66', 'VER:80-89'],
     'defect': ('Two load-bearing identities are checked by no lane code and named in no gate: (a) WMAN '
                'supports_row2to7 equal the T16 lists TPL:88-95/101-104 (PROD copies SMAN; VER derives units from '
                "WMAN's own lists and never reads TPL); (b) F = GA(argv) and the variable map / name table bound to F "
                '(map 7b4dd597... and name table b8423861... are pinned by SHA only; the map meta cnf_sha256 and the '
                'parent binding receipt are not cited in OVL:105-111).'),
     'verification_now': ('No mismatch exists: Codex compared all 16 lists and matched all 7,840 g ids to the GA '
                          'allocation order (snapshot check); Claude verified the 16 lists and all 672 unit literals '
                          'via g_1((0,c),(i,0)) = 49c + 7i - 6 by reading; desk t16_enum.result.json '
                          '(tpl_lists_equal_weakened_manifest_supports=true), SMAN=WMAN supports/units, GMAP meta '
                          '(argv, 509915/5740230, cnf 6ecb77a7..., encoder bf1aada1...) and alo_reconstruct.result.json.'),
     'correction': ('Append to gate 3 (OVL:108): "WMAN supports_row2to7 = TPL:88-95/101-104 verbatim; unit ids per '
                    'GMAP 7b4dd597... whose meta binds cnf 6ecb77a7... and encoder bf1aada1...". Append to gate 1 '
                    '(OVL:106): "F = GA(argv) and name table b8423861... per parent binding-result.v2.json '
                    'dce638a9... (SEM:96-97)". Optionally assert both in VER v2 / the parent replay.'),
     'blocks_spending_runs': False},
    {'id': 'F3', 'severity': 'MINOR', 'questions': ['Q2'], 'sources': ['Claude D-m3', 'desk concurs'],
     'lines': ['OVL:26-28', 'TPL:1', 'TPL:4-5', 'TPL:20', 'TPL:59', 'TPL:62-63'],
     'defect': ('OVL excludes only TPL:111-113,117-120, but TPL:20 ("by the accepted K5 SB2 normalisation"), TPL:59 '
                '(moves justified via the reduced-K5 bridge, IMP:11-14,72-74) and TPL:62-63 ("All reduced-K5/P4 '
                'properties are preserved") still route through reduced-K5/old F. Not mathematically needed: the T16 '
                'hypothesis and OVL section 2 replace them.'),
     'correction': ('State the exact excision: T16 uses TPL:9-19 (line 20 justification replaced by the hypothesis '
                    'supp Q1(1,0)=A), 22-55, 60-64 as made explicit by OVL:34-38 minus the "All reduced-K5/P4..." '
                    'sentence, and 66-109; TPL:1, 4-5, 59 and 111-131 are not used.'),
     'blocks_spending_runs': False},
    {'id': 'F4', 'severity': 'MINOR', 'questions': ['Q5', 'Q1:BR2-m6'],
     'sources': ['Claude D-m4', 'desk', 'Codex reads the concrete meaning from RM:216-228; runner/checker binaries not audited'],
     'lines': ['OVL:109', 'RM:216-224', 'RM:413'],
     'defect': ('Gate 4 names predicate categories ("self-exit/feed/proof-stream/hash/guard") but pins neither the '
                'strict predicate nor the solver, checker or runner.'),
     'correction': ('Replace with: 16/16 receipts meeting RM:222-224 exactly (README as snapshotted 45b80b2f...): both '
                    'processes self-exited, no guard trip or relay error; CaDiCaL exit 20 with "s UNSATISFIABLE"; '
                    'drat-trim d834b649... exit 0 with a line equal to "s VERIFIED" after stripping CR and no '
                    '"s NOT VERIFIED"; solver-feed and checker-feed SHA-256 equal to that case\'s WMAN cnf_sha256; '
                    'proof-stream SHA and bytes recorded; runner run_n8_one_p4_templates.py 268e743b... (RM:413). '
                    'LRAT-only checker results do not count.'),
     'blocks_spending_runs': False},
    {'id': 'F5', 'severity': 'MINOR', 'questions': ['Q1', 'Q2', 'Q3', 'Q4'],
     'sources': ['Claude D-m5 (a-c)', 'desk (a, d, e)'],
     'lines': ['OVL:17-19', 'OVL:48', 'OVL:11', 'OVL:93', 'OVL:102', 'OVL:3-4', 'OVL:77', 'OVL:84', 'RECIPE:13-44'],
     'defect': ('Editorial: (a) OVL:17-19 says "aligned" supports in both frames; in the column-0 frame disjointness '
                'is Prop 1/G2 on the cell pair ((0,k),(i,0)), frame-free, and "Prop1" is unpinned (primary: SRC:300-302; '
                'ENC:95,134). (b) OVL:48 "prefix equality" must be the inclusive prefix v_i[0..k]=v_(i+1)[0..k] '
                '(GA:262-269; lexeq(i,0) forced true by a unit); value unique, Q3 unaffected. (c) OVL:11,93,102 use '
                'truncated pins for SEM and PV. (d) Missing-space typography fuses hashes and numbers with words '
                '(e.g. "SHA2566200c8d7...", "SHA256264288f8...", "SHA6ecb77a7..."); every value is correct on inspection '
                'but not machine-parseable. (e) RECIPE lists the Q1 KEEP record under "removed".'),
     'correction': ('Fix in any r2 overlay: frame-free disjointness wording with SRC/ENC citations; "inclusive prefix"; '
                    'full SEM 413951379f...1022 and PV 919daeac...a8f9 pins; separated hash tokens; read RECIPE '
                    '"removed" as "verified ALO records".'),
     'blocks_spending_runs': False},
]

QUESTIONS = {
    'Q1': {'consolidated': 'CLOSED IN SUBSTANCE; 2 residues (BR2 m6 -> F4, DEL m2 -> F1); nothing reopened',
           'codex': 'CLOSED (10/10, as documentation/specification repairs)',
           'claude': 'PARTIAL (8 closed; BR2 m6 and DEL m2 partial)',
           'desk': 'agrees: all 10 addressed; residues are pin/labelling only; no conflict with SEM/IMP/ENC or CX1',
           'per_minor': {'BR2-m1': 'closed (OVL:52-57)', 'BR2-m2': 'closed (OVL:61-65,81-88); labelling residue F1',
                         'BR2-m3': 'closed (OVL:13-30); excision residue F3', 'BR2-m4': 'closed (OVL:34-38)',
                         'BR2-m5': 'closed (OVL:92)',
                         'BR2-m6': 'Codex closed / Claude partial: strict predicate unpinned (F4)',
                         'BR2-m7': 'closed (OVL:24,38,42-43,48-50,99-101)', 'DEL-m1': 'closed (OVL:61-63,81-88)',
                         'DEL-m2': 'Codex closed / Claude partial: F_one and leaf SHAs producer-path only (F1)',
                         'DEL-m3': 'closed (OVL:67-73)'}},
    'Q2': {'consolidated': 'PASS-WITH-FIXES (mathematics passes; fixes F2a, F3, F5a are binding/documentation)',
           'codex': 'PASS', 'claude': 'PASS-WITH-FIXES',
           'desk': ('PASS: degree bounds, component theorem and all 16 canonical choices re-derived by reading; '
                    'pinned stdlib enumeration finds 140 sorted / 43,290 labelled patterns, 16 orbits, bijection with '
                    'the 16 TPL lists, no other component type; no reliance on reduced-K5, P4 of squares 2-5, '
                    'non-classicality or the 13-case/c112 interface')},
    'Q3': {'consolidated': 'PASS (wording F5b only)', 'codex': 'PASS', 'claude': 'PASS',
           'desk': ('PASS: G2-G5, constants, b3/c4 AND, u5, lexeq, SB2, 42 units and P4 one-way clauses hold for the '
                    'stated values; w3 occurs positively only in the five ALOs (GA:247); deleting exactly the four '
                    'ALOs of squares 2-5 is sound for arbitrary squares 2-5 and nothing else is needed')},
    'Q4': {'consolidated': ('PASS-WITH-FIXES: deletions, Q1 keep, ordered retained body, source header and unit '
                            'reconstruction are bound on a second path; F_one/leaf SHAs and header bytes only via the '
                            'producer Formula (F1); WMAN=TPL and map/name-table=F unchecked by code (F2); claim scope '
                            '(generation/identity evidence, no refutation, no parent replay) correct'),
           'codex': 'PASS (states the same independence boundary)', 'claude': 'PASS-WITH-FIXES',
           'desk': 'PASS-WITH-FIXES (F1, F2)'},
    'Q5': {'consolidated': ('PASS-WITH-FIXES: the six gates are sufficient in substance (classical sets need nothing; '
                            'A8 all-five-squares/all-entries premise plus W8; squares 2-5 unrestricted; consequent is '
                            'SRC:642 at n-3=5); gates 1/3/4 should name F2 and F4 explicitly'),
           'codex': 'PASS', 'claude': 'PASS-WITH-FIXES', 'desk': 'PASS-WITH-FIXES (F2, F4)'},
}

DESK_EVIDENCE = [
    {'id': 'E1', 'what': 'all task-pinned SHA-256 values matched before snapshot; weakened manifest and primary text located',
     'files': 'TASK_PINS'},
    {'id': 'E2', 'what': ('T16 enumeration (desk evidence, not proof): script pinned before run; 30 candidate column '
                          'supports; 140 passing sorted multisets; 43,290 labelled patterns (equals WMAN/SMAN '
                          'finite_orbit_control and README:362); 16 orbits under Sym(A)xSym(B) (144); all map into the 16 '
                          'TPL lists, orbit-list bijection, each list needed; components only K11/K22/K33-e/K33/K44-PM; '
                          'TPL lists ROWLEX-sorted, satisfy H1-H4 and equal WMAN supports; 0.13 s, 21 MB. Limit: uses the '
                          'same necessary conditions as TPL section 2, which were checked by reading, not mechanically.'),
     'script': 'desk/t16_enum.py', 'pin': 'desk/t16_enum.PIN.json', 'result': 'desk/t16_enum.result.json'},
    {'id': 'E3', 'what': ('ALO reconstruction from the GA allocation order (no CNF read): w3 base 509600; all five '
                          'reconstructed ALO line hashes equal the DEL pins; derived indices 5733728/5735297/5736866/'
                          '5738435/5740004 equal DEL; deleted bytes 1576 = RECIPE:45'),
     'script': 'desk/alo_reconstruct.py', 'pin': 'desk/alo_reconstruct.PIN.json', 'result': 'desk/alo_reconstruct.result.json'},
    {'id': 'E4', 'what': ('GMAP meta binds argv (as ENC:44-45), 509915 vars, 5740230 clauses, cnf 6ecb77a7..., encoder '
                          'bf1aada1...; row-2 ids 57..351 = IMP:55; extract given to the tool-less reviewer as [F]'),
     'result': 'desk/gmap_extract.json'},
    {'id': 'E5', 'what': ('SMAN vs WMAN: ids, supports and units identical for all 16 cases; WMAN old_strong_leaf_cnf_sha256 '
                          '= SMAN cnf_sha256; WMAN base_cnf_sha256 = 374d6fb4...; every case run_required=true and '
                          'excluded_by_imported_c112=false')},
    {'id': 'E6', 'what': 'byte arithmetic: 137664569 - 21 (header) - 1576 (4 x 394) = 137662972 = RECIPE:12'},
    {'id': 'E7', 'what': ('artifact mtimes: DEL 23:32:44, BR2 23:33:57, PROD 23:41:38, RECIPE/WMAN 23:42:13, VER 00:03:53, '
                          'RCPT 00:04:37, OVL 00:06:59, LINK 00:07:47 (PDT) - consistent with the OVL section 4 timeline')},
]

DEVIATIONS = [
    'desk/t16_enum.time.txt was created by shell stderr redirection (fresh file), not by an exclusive-open call.',
    'desk/snapshot_pin.py, desk/build_prompts.py and desk/disk_gate.py were not hash-pinned before execution (only the '
    'two optional independent checks were); their SHA-256 values are recorded below.',
    'The owned TMPDIR received CLI caches (tmp/node-compile-cache, 561 files, about 2.7 MB, and an empty '
    'tmp/.tmpSfXxuS); left in place, nothing deleted.',
    'Codex also read workspace context files outside the snapshot (a skill file, aifours and institute READMEs, AGENTS.md '
    'probes); its 22 commands were read-only and never opened the CNF or name table; its sandbox refused one xcrun cache '
    'write to /tmp, so no write occurred.',
    'The lane README was snapshotted as found (45b80b2f...), not task-pinned.',
    'The Claude run used 126,187 of 128,000 maximum output tokens (120,161 thinking); its note is complete (ends with the '
    'tally line), but a larger packet could truncate.',
    'No reviewer timed out; no retry was needed.',
]


def main():
    out = HERE / 'RESULT.json'
    result = {
        'kind': 'moqls8-unified-delta-v1: static delta audit of the unified one-P4 bridge repair overlay (no theorem verdict)',
        'desk': 'N8UnifiedDeltaDesk',
        'written_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
        'target': {'overlay': 'LANE/review/N8_UNIFIED_REVIEW_REPAIRS.r1.md',
                   'overlay_sha256': 'e0f3c860aaa81dd7b8214aabb84f5094fcaf425a6a17a01159d3aa779a9d1704'},
        'delegated_disposition': 'DELTA-ACCEPT-WITH-FIXES',
        'disposition_basis': ('0 FATAL and 0 MAJOR from Codex, Claude and the desk; five consolidated MINORs (F1-F5) are '
                              'labelling, pinning and binding-documentation fixes. None changes a clause, unit, leaf SHA, '
                              'case or mathematical step, so none blocks spending the 16 WMAN-pinned refutations; F1, F2 '
                              'and F4 should be in an r2 overlay or parent note before any result is counted.'),
        'not_claimed': ['no Problem 16 / n=8 theorem verdict', 'no refutation or SAT result', 'no novelty assessment',
                        'no parent disposition', 'no replay of PROD/VER and no read of the 137 MB CNF or name table'],
        'task_pins_verified': {k: {'sha256': v, 'match': True} for k, v in TASK_PINS.items()},
        'snapshot': {'manifest': 'SNAPSHOT_MANIFEST.json', 'manifest_sha256': sha(HERE / 'SNAPSHOT_MANIFEST.json'),
                     'files': 21, 'bytes': json.loads((HERE / 'SNAPSHOT_MANIFEST.json').read_text())['total_bytes'],
                     'pinned_before_reviews': True},
        'reviewers': [reviewer('moqls8-unified-delta-codex-v1', 'run_codex_note_coop.py'),
                      reviewer('moqls8-unified-delta-claude-v1', 'run_claude_note_coop.py')],
        'questions': QUESTIONS,
        'findings': FINDINGS,
        'notes': [
            'N1: T16 (OVL:21-24) could state that the moved set is again a genuine aligned five-set (isotopy), which OVL section 3 uses; trivial.',
            "N2: given SB2, Q1's kept ALO and every P4 clause are always satisfiable via w3_1(0,(1,0)), so F_one plus units carries no effective P4 strength (CL1:135); not a defect.",
        ],
        'desk_evidence': DESK_EVIDENCE,
        'desk_files_sha256': {str(p.relative_to(HERE)): sha(p) for p in sorted((HERE / 'desk').iterdir()) if p.is_file()},
        'deviations': DEVIATIONS,
    }
    with out.open('x') as fh:
        json.dump(result, fh, indent=1, ensure_ascii=False)
        fh.write('\n')
    print(sha(out))


if __name__ == '__main__':
    main()
