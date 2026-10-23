"""DESK EVIDENCE, NOT PROOF. Reconstruct the five row-0-frame P4 ALO clause lines of old F from the encoder's
variable-allocation order alone (no CNF read) and compare their SHA-256 with the pinned DEL hashes.
Derivation (GA = gram_a.py bf1aada1...): total vars 509915; ROWLEX lexeq vars are allocated last, 5 pairs x 7 = 35;
the 5 x 56 = 280 w3 flags are allocated just before them, square-major, cells row-major skipping row 0
(GA:235-247), so square s uses 509600 + 56(s-1) + 1 .. 509600 + 56 s and its ALO line is those ids, ' 0\\n'.
Inputs: snapshot DEL and GA (SHA-checked). Output: desk/alo_reconstruct.result.json (exclusive).
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DEL = HERE / 'snapshot/DEL__UNIFIED_ONE_P4_DELETIONS_v1.json'
DEL_SHA = '4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6'
GA = HERE / 'snapshot/GA__gram_a.py'
GA_SHA = 'bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a'
OUT = HERE / 'desk/alo_reconstruct.result.json'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    draw, graw = DEL.read_bytes(), GA.read_bytes()
    assert sha(draw) == DEL_SHA and sha(graw) == GA_SHA, 'snapshot pin'
    d = json.loads(draw)
    nv, n_lexeq, n_w3 = 509915, 5 * 7, 5 * 56
    base = nv - n_lexeq - n_w3
    pinned = {d['keep_q1']['square']: d['keep_q1']} | {x['square']: x for x in d['delete']}
    rows = []
    for s in range(1, 6):
        ids = [base + 56 * (s - 1) + k for k in range(1, 57)]
        line = (' '.join(map(str, ids)) + ' 0\n').encode()
        rec = pinned[s]
        rows.append({'square': s, 'first_id': ids[0], 'last_id': ids[-1], 'line_bytes': len(line),
                     'reconstructed_sha256': sha(line), 'pinned_sha256': rec['clause_bytes_sha256'],
                     'match': sha(line) == rec['clause_bytes_sha256'],
                     'operation': 'keep' if s == 1 else 'delete', 'index': rec['clause_index_zero_based']})
    # index arithmetic: ROWLEX 5 x (1 + 36 + 1) = 190 clauses after P4, SB2 5 x 7 = 35 units, total 5740230
    tail = 190 + 35
    alo5 = 5740230 - 1 - tail
    idx = {s: alo5 - 1569 * (5 - s) for s in range(1, 6)}
    result = {'kind': 'desk evidence, not proof: ALO line reconstruction from GA allocation order',
              'script_sha256': sha(Path(__file__).read_bytes()), 'w3_id_base': base, 'rows': rows,
              'all_five_hashes_match': all(r['match'] for r in rows),
              'derived_indices': idx, 'indices_match_DEL': all(idx[r['square']] == r['index'] for r in rows),
              'deleted_bytes_if_squares_2_5': sum(r['line_bytes'] for r in rows if r['square'] != 1)}
    with OUT.open('x') as fh:
        json.dump(result, fh, indent=1)
        fh.write('\n')
    print(json.dumps({k: result[k] for k in ('w3_id_base', 'all_five_hashes_match', 'derived_indices',
                                            'indices_match_DEL', 'deleted_bytes_if_squares_2_5')}))


if __name__ == '__main__':
    main()
