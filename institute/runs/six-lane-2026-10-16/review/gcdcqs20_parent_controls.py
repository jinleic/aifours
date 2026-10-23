"""Parent intended-reason mutation controls for the pinned gcDCQS(20^4:0) certificate (input A).
Every fixture is retained with its SHA-256; acceptance rests on check_gcdcqs_parent.py. Refuses overwrite.
Usage: python3 -B gcdcqs20_parent_controls.py
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PIN = HERE / 'gcdcqs20-parent-inputs-v1'
CERT = PIN / 'gcdcqs20-e1s1_p10.txt'
CERT_SHA = '58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca'
CHECKER = HERE / 'check_gcdcqs_parent.py'
OUT = HERE / 'gcdcqs20-parent-controls-v1'


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(timespec='seconds')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load():
    data = CERT.read_bytes()
    if sha(data) != CERT_SHA:
        raise SystemExit('pinned certificate hash changed')
    lines = data.decode('ascii').split('\n')
    if lines[-1] != '':
        raise SystemExit('expected final newline')
    lines = lines[:-1]
    groups_at = lines.index('GROUPS') + 1
    groups = [list(map(int, lines[groups_at + i].split())) for i in range(4)]
    blocks_at = lines.index('BLOCKS') + 1
    first_point = next(i for i, l in enumerate(lines) if l.startswith('POINT '))
    sections = {}
    x = j = None
    for i in range(first_point, len(lines)):
        l = lines[i]
        if l.startswith('POINT '):
            x = int(l.split()[1])
            sections[x] = {'line': i, 'classes': []}
        elif l.startswith('CLASS '):
            sections[x]['classes'].append({'line': i, 'triples': []})
        else:
            sections[x]['classes'][-1]['triples'].append((i, frozenset(map(int, l.split()))))
    return lines, groups, blocks_at, first_point, sections


def text(lines):
    return ('\n'.join(lines) + '\n').encode('ascii')


def main():
    lines, groups, blocks_at, first_point, sec = load()
    group_of = {p: gi for gi, g in enumerate(groups) for p in g}
    blocks = [(i, frozenset(map(int, lines[i].split()))) for i in range(blocks_at, first_point)]
    block_set = {b for _, b in blocks}
    fixtures = []

    def add(name, new_lines, expect, args=None, raw=None):
        fixtures.append((name, raw if raw is not None else text(new_lines), expect, args))

    # 1 swap two points between two blocks (both stay group-legal and distinct)
    (i1, b1), done = blocks[0], False
    for i2, b2 in blocks[1:]:
        for p1 in sorted(b1 - b2):
            for p2 in sorted(b2 - b1):
                n1, n2 = (b1 - {p1}) | {p2}, (b2 - {p2}) | {p1}
                ok = all(max(sum(group_of[p] == g for p in nb) for g in range(4)) <= 2 for nb in (n1, n2))
                if ok and n1 not in block_set and n2 not in block_set and n1 != n2:
                    L = list(lines)
                    L[i1], L[i2] = ' '.join(map(str, sorted(n1))), ' '.join(map(str, sorted(n2)))
                    add('swap-points-between-blocks', L, 'COVERAGE: triple')
                    done = True
                    break
            if done:
                break
        if done:
            break
    # 2 out-of-range point
    L = list(lines); t = lines[blocks_at].split(); t[3] = '80'; L[blocks_at] = ' '.join(t)
    add('block-point-out-of-range', L, 'BLOCK: ')
    # 3 repeated point in a block
    L = list(lines); t = lines[blocks_at].split(); t[3] = t[2]; L[blocks_at] = ' '.join(t)
    add('block-repeated-point', L, 'BLOCK: ')
    # 4 duplicate a block (line 2 replaced by line 1)
    L = list(lines); L[blocks_at + 1] = lines[blocks_at]
    add('duplicate-block', L, 'BLOCK: ')
    # 5 drop a block
    L = lines[:blocks_at + 5] + lines[blocks_at + 6:]
    add('drop-block', L, 'BLOCK: 19399 blocks')
    # 6 block with three points of one group
    L = list(lines); L[blocks_at + 2] = '0 1 2 20'
    add('block-three-in-group', L, 'BLOCK: ')
    # 7 swap points 19 and 20 between groups 0 and 1
    gl = lines.index('GROUPS') + 1
    L = list(lines)
    g0 = [20 if p == 19 else p for p in groups[0]]
    g1 = [19 if p == 20 else p for p in groups[1]]
    L[gl], L[gl + 1] = ' '.join(map(str, g0)), ' '.join(map(str, g1))
    add('swap-group-points', L, 'BLOCK: ')
    # 8 move a triple into another class of point 0 where it meets a triple
    c = sec[0]['classes']
    (ti, tr) = c[10]['triples'][0]
    clash_class = next(j for j in range(11, 40) if any(tr & t2 for _, t2 in c[j]['triples']))
    L = list(lines)
    moved = L.pop(ti)
    ins = c[clash_class]['line']  # after the CLASS header, index shifted by the pop
    L.insert(ins, moved)
    add('move-triple-breaks-ppc', L, f'COLOURING: point 0 class {clash_class} is not a partial parallel class')
    # 9 move a hole-meeting triple into a hole-free class of point 0, keeping both classes disjoint
    hole = set(groups[group_of[0]]) - {0}
    holefree = [j for j in range(40) if not any(t & hole for _, t in c[j]['triples'])]
    target = holefree[0]
    used = set().union(*[t for _, t in c[target]['triples']])
    src = next((j, ti, t) for j in range(40) if j not in holefree for ti, t in c[j]['triples'] if t & hole and not t & used)
    L = list(lines)
    moved = L.pop(src[1])
    ins = c[target]['line'] + 1 if c[target]['line'] < src[1] else c[target]['line']
    L.insert(ins, moved)
    add('holemeeting-into-holefree-class', L, f'COLOURING: point 0 has {len(holefree) - 1} hole-free classes')
    # 10 drop one derived triple at point 5
    L = list(lines); del L[sec[5]['classes'][3]['triples'][0][0]]
    add('drop-derived-triple', L, 'COLOURING: point 5 misses 1 derived triples')
    # 11 non-derived triple at point 6 (third point replaced by an unused point of that class)
    cls = sec[6]['classes'][12]
    ti, t = cls['triples'][-1]
    used = set().union(*[t2 for _, t2 in cls['triples']])
    a, b, cc = sorted(t)
    newp = next(p for p in range(80) if p not in used and p != 6 and frozenset({a, b, p}) not in {t2 for c2 in sec[6]['classes'] for _, t2 in c2['triples']})
    L = list(lines); L[ti] = ' '.join(map(str, sorted({a, b, newp})))
    add('non-derived-triple', L, 'COLOURING: point 6 triple')
    # 12 copy a triple as the FIRST triple of a later class -> listed twice (fires before any PPC clash)
    c7 = sec[7]['classes']
    src_t = c7[0]['triples'][0][1]
    L = list(lines); L.insert(c7[1]['line'] + 1, ' '.join(map(str, sorted(src_t))))
    add('triple-listed-twice', L, 'COLOURING: point 7 lists triple')
    # 13 class order swapped at point 3
    L = list(lines); c3 = sec[3]['classes']
    L[c3[0]['line']], L[c3[1]['line']] = 'CLASS 1', 'CLASS 0'
    add('class-order', L, 'FORMAT: point 3 lists CLASS 1 where CLASS 0 is required')
    # 14 drop the POINT 79 section
    L = lines[:sec[79]['line']]
    add('drop-point-section', L, 'COMPLETENESS: ')
    # 15 repeat a point section label
    L = list(lines); L[sec[79]['line']] = 'POINT 78'
    add('repeat-point-section', L, 'COMPLETENESS: POINT sections repeat')
    # 16 header values
    L = list(lines); L[lines.index('HOLEFREE 10')] = 'HOLEFREE 9'
    add('holefree-9', L, 'PARAMS: HOLEFREE 9')
    L = list(lines); L[lines.index('COLOURS 40')] = 'COLOURS 39'
    add('colours-39', L, 'FORMAT: point 0 has more than 39 classes')
    # 17 empty class
    L = [l for k, l in enumerate(lines) if k not in {ti2 for ti2, _ in sec[8]['classes'][0]['triples']}]
    add('empty-class', L, 'COLOURING: point 8 class 0 is empty')
    # 18 lexical strictness
    L = list(lines); L[blocks_at] = lines[blocks_at] + ' '
    add('trailing-space', L, 'FORMAT: line')
    L = list(lines); L[blocks_at] = '0' + lines[blocks_at]
    add('leading-zero', L, 'FORMAT: line')
    add('carriage-return', None, 'FORMAT: carriage return', raw=text(lines).replace(b'\n', b'\r\n', 1))
    # 19 wrong expected parameters and wrong digest on the unmodified bytes
    add('expected-order-16', None, 'PARAMS: header', args=('16', '4', '4'), raw=text(lines))
    add('wrong-sha', None, 'INPUT: SHA-256 mismatch', args=('80', '4', '20', '0' * 64), raw=text(lines))

    OUT.mkdir(exist_ok=False)
    results = []
    for name, data, expect, args in fixtures:
        fx = OUT / (name + '.txt')
        with fx.open('xb') as f:
            f.write(data)
        digest = sha(data)
        a = list(args) if args else ['80', '4', '20']
        if len(a) == 3:
            a.append(digest)
        rec = OUT / (name + '.json')
        proc = subprocess.run(['/usr/bin/python3', '-B', str(CHECKER), str(fx), *a, str(rec)], capture_output=True, text=True)
        got = json.loads(rec.read_text())
        ok = proc.returncode == 1 and got.get('status') == 'FAIL' and got.get('reason', '').startswith(expect)
        results.append({'name': name, 'fixture_sha256': digest, 'expected_reason_prefix': expect, 'exit': proc.returncode,
                        'reason': got.get('reason'), 'intended': ok})
    summary = {'recorded_at_pt': stamp(), 'certificate_sha256': CERT_SHA, 'checker_sha256': sha(CHECKER.read_bytes()),
               'controls_script_sha256': sha(Path(__file__).read_bytes()), 'fixtures': len(results),
               'all_intended': all(r['intended'] for r in results), 'results': results}
    with (OUT / 'parent-result.json').open('x') as f:
        json.dump(summary, f, indent=2)
        f.write('\n')
    print(json.dumps({'all_intended': summary['all_intended'], 'fixtures': len(results),
                      'failures': [r for r in results if not r['intended']]}, indent=1))


if __name__ == '__main__':
    main()
