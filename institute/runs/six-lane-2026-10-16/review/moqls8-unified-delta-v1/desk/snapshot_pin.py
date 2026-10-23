"""Pin a read-only snapshot of the unified one-P4 delta-audit inputs (copies + SHA manifest).
Every output file is created exclusively; aborts on any SHA mismatch against the task pins.
Usage: python3 -B snapshot_pin.py   (run once, from anywhere)
"""
import hashlib
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent.parent          # R/moqls8-unified-delta-v1
R = HERE.parent                                          # R
LANE = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16')
SNAP = HERE / 'snapshot'
CAP = 10_000_000

# (key, source path, required sha256 or None for supporting files that are hashed but not task-pinned)
FILES = [
    ('BR2', LANE / 'review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md', 'c391a67ab7cb468c2500dd4fc0d565fa4e104b97777a5bab668ed5fdc82ebbb3'),
    ('DEL', LANE / 'evidence/UNIFIED_ONE_P4_DELETIONS_v1.json', '4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6'),
    ('OVL', LANE / 'review/N8_UNIFIED_REVIEW_REPAIRS.r1.md', 'e0f3c860aaa81dd7b8214aabb84f5094fcaf425a6a17a01159d3aa779a9d1704'),
    ('LINK', LANE / 'evidence/N8_UNIFIED_SEMANTIC_REPAIR_LINK_v1.json', '483dcdb6e0f80a80da07e51d32bf50514fb63d888d102a8004359c2c17298608'),
    ('RCPT', LANE / 'evidence/n8_one_p4_templates_v1/BYTE_FILTER_VERIFICATION_v1.json', '65aafe0ad577645036c6cc15e4f4705f0bb19a4f5e8eed2867954da8d761cc88'),
    ('RECIPE', LANE / 'evidence/n8_one_p4_templates_v1/BASE_RECIPE.json', '264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18'),
    ('WMAN', LANE / 'evidence/n8_one_p4_templates_v1/MANIFEST.json', '355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74'),
    ('VER', LANE / 'code/verify_one_p4_deletion.py', '825c3cd7fabfd2efe25ff9e21f1044bed09c32a58e6be92aa63a3961e2893016'),
    ('PROD', LANE / 'code/n8_one_p4_formula.py', '61eda23ce7174e7cee77ee873ff06e5f22a2beaf0c197b8282f41dc8ddded400'),
    ('TPL', LANE / 'review/K5_COLUMN0_TEMPLATE_COVER.r1.md', '1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a'),
    ('SEM', LANE / 'review/K5_SEMANTIC_REVIEW_REPAIRS.r1.md', '413951379f248a87e02b52dfb942fb131f25524557c35adf9c54f68981b31022'),
    ('ENC', LANE / 'review/K4K5_ENCODING_SOUNDNESS.r3.md', 'a83d305013fa920d1ffe361d6d0aeb589f958da477420b2b053a503221858e59'),
    ('IMP', LANE / 'review/K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md', '34e11e52c28a798eb378c397097dbccaa753aca74d54e8ccbf6465b2088177d4'),
    ('SRC', LANE / 'sources/2607.12933v2.raw.txt', '265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9'),
    ('CL1', R / 'moqls8-k5nf-unified-claude-v1.note.md', '6200c8d7b72a0335d1bd2bc11b98226ea4439d64ce7ab425fd3d7468477d98f5'),
    ('CX1', R / 'moqls8-k5nf-unified-codex-v1.note.md', 'e439c8c0f2c14b5dbf5a3ddc881966495372d7610c784ef54370f8439a47bdb3'),
    ('PV', R / 'moqls8-k1k2-parent-verdict.md', '919daeac811bd551c4165ba415f9c6835b564adcb9bb6fcde1969307f2caa8f9'),
    # supporting (pinned by SHA inside the pinned inputs above)
    ('GA', LANE / 'code/gram_a.py', 'bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a'),
    ('SMAN', LANE / 'evidence/k5_column_templates_v1/MANIFEST.json', 'f77c061947aa64d1107736d27723373ccc9e02633dd099c1a58cf9d77a2c0b71'),
    ('GMAP', LANE / 'evidence/gram_dev_v1/GA5L_K5_sb2.map.json', '7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197'),
    # supporting, not pinned elsewhere by the task: hashed as found
    ('RM', LANE / 'README.md', None),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    rows, total = [], 0
    for key, src, want in FILES:
        data = src.read_bytes()
        got = sha(data)
        if want is not None and got != want:
            raise SystemExit(f'PIN MISMATCH {key} {src}: {got} != {want}')
        total += len(data)
        if total > CAP:
            raise SystemExit('snapshot cap exceeded')
        dst = SNAP / f'{key}__{src.name}'
        with dst.open('xb') as fh:
            fh.write(data)
        if sha(dst.read_bytes()) != got:
            raise SystemExit(f'copy mismatch {key}')
        rows.append({'key': key, 'source': str(src), 'snapshot': str(dst.relative_to(HERE)), 'bytes': len(data),
                     'lines_lf': data.count(b'\n'), 'sha256': got,
                     'pin': 'task-pinned' if want is not None else 'hashed-as-found'})
    manifest = {'kind': 'moqls8-unified-delta-v1 input snapshot (read-only copies)',
                'created_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
                'script_sha256': sha(Path(__file__).read_bytes()), 'total_bytes': total, 'files': rows}
    with (HERE / 'SNAPSHOT_MANIFEST.json').open('x') as fh:
        json.dump(manifest, fh, indent=1)
        fh.write('\n')
    print(json.dumps({'files': len(rows), 'total_bytes': total}))


if __name__ == '__main__':
    main()
