#!/usr/bin/python3
"""Independently bind parent-built Lean list literals to both raw certificates, preserving every row/class order.
No worker parser/generator/checker imports. This is a literal binding audit, not a replacement design verifier.
Usage: python3 -B gcdcqs20-parent-literal-binding-v1.py NEW.json. Refuses overwrite.
"""
import ast
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SRC = HERE / 'gcdcqs20-lean-parent-audit-v2/src/Gc80'


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def raw_read(path, gc):
    data = path.read_bytes()
    require(data.endswith(b'\n') and b'\r' not in data, 'raw line endings')
    lines = [s for s in data.decode('ascii').split('\n') if s and not s.startswith('#')]
    require(lines.pop(0) == ('GCDCQS 80 4 20' if gc else 'MCDSQS 80'), 'raw header')
    require(lines.pop(0) == 'COLOURS 40', 'raw colours')
    groups = []
    if gc:
        require(lines.pop(0) == 'HOLEFREE 10', 'raw hole-free')
        require(lines.pop(0) == 'GROUPS', 'raw groups header')
        for _ in range(4):
            row = lines.pop(0)
            require(re.fullmatch(r'[0-9]+(?: [0-9]+){19}', row), 'raw group row')
            groups.append([int(x) for x in row.split()])
    require(lines.pop(0) == 'BLOCKS', 'raw blocks header')
    blocks, points, p, c = [], [], -1, -1
    for line in lines:
        if line.startswith('POINT '):
            require(line == 'POINT ' + str(p + 1), 'raw point order')
            if p >= 0:
                require(c == 39 and all(points[-1]), 'raw incomplete point')
            p += 1
            c = -1
            points.append([])
        elif line.startswith('CLASS '):
            require(p >= 0 and line == 'CLASS ' + str(c + 1) and c < 39, 'raw class order')
            c += 1
            points[-1].append([])
        elif p < 0:
            require(re.fullmatch(r'[0-9]+(?: [0-9]+){3}', line), 'raw block syntax')
            blocks.append(tuple(map(int, line.split())))
        else:
            require(c >= 0 and re.fullmatch(r'[0-9]+(?: [0-9]+){2}', line), 'raw triple syntax')
            points[-1][-1].append(tuple(map(int, line.split())))
    require(p == 79 and c == 39 and all(points[-1]), 'raw ending')
    require(len(blocks) == (19400 if gc else 20540), 'raw block count')
    require(all(len(P) == 40 and sum(map(len, P)) == (970 if gc else 1027) for P in points), 'raw point count')
    return {'groups': groups, 'blocks': blocks, 'points': points, 'sha256': hashlib.sha256(data).hexdigest()}


def list_body(text, name):
    match = re.search(r'^def\s+' + re.escape(name) + r'\s*:.*?:=\s*(?:List\.flatten\s*)?\[', text, re.M)
    require(match is not None, 'missing literal ' + name)
    start = match.end() - 1
    depth = 0
    for i in range(start, len(text)):
        if text[i] == '[':
            depth += 1
        elif text[i] == ']':
            depth -= 1
            if depth == 0:
                return re.sub(r'--[^\n]*', '', text[start:i+1])
    raise ValueError('unclosed literal ' + name)


def numeric(text, name):
    body = list_body(text, name)
    require(re.fullmatch(r'[0-9\[\](),\s]*', body) is not None, 'nonliteral arithmetic ' + name)
    return ast.literal_eval(body)


def names(text, name):
    body = list_body(text, name)
    require(re.fullmatch(r'\[[A-Za-z0-9_,\s]*\]', body) is not None, 'nonliteral aggregation ' + name)
    return [s.strip() for s in body[1:-1].split(',') if s.strip()]


def lean_read(gc):
    tag = 'Gc' if gc else 'Mc'
    bt = (SRC / ('Data' + tag + 'B.lean')).read_text()
    prefix = 'blocks' + tag + '80'
    chunks = sorted(set(re.findall(r'^def (' + prefix + r'_\d+)\b', bt, re.M)), key=lambda s: int(s.rsplit('_',1)[1]))
    refs = names(bt, prefix)
    require(refs == chunks and refs == [prefix + '_' + str(i) for i in range(len(refs))], 'block aggregate order')
    blocks = [t for n in refs for t in numeric(bt, n)]
    aggregate = (SRC / ('Data' + tag + '.lean')).read_text()
    refs = names(aggregate, 'colour' + tag + '80')
    require(refs == ['col' + tag + '80_' + str(i) for i in range(80)], 'point aggregate order')
    texts = [(SRC / ('Data' + tag + 'P' + str(i) + '.lean')).read_text() for i in range(8)]
    points = [numeric(texts[i//10], refs[i]) for i in range(80)]
    return {'groups': numeric(bt, 'groupsGc80') if gc else [], 'blocks': blocks, 'points': points}


def compare(raw, lean):
    require(raw['groups'] == lean['groups'], 'GROUPS mismatch')
    require(raw['blocks'] == lean['blocks'], 'BLOCKS mismatch')
    require(len(raw['points']) == len(lean['points']), 'POINT count mismatch')
    for p, (a, b) in enumerate(zip(raw['points'], lean['points'])):
        require(len(a) == len(b), 'CLASS count mismatch at POINT ' + str(p))
        for c, (x, y) in enumerate(zip(a,b)):
            require(x == y, 'POINT %d CLASS %d mismatch' % (p,c))


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    records = []
    for gc, rel, expected in [
        (True, 'gcdcqs20-parent-inputs-v1/gcdcqs20-e1s1_p10.txt', '58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca'),
        (False, 'mcdsqs80-parent-inputs-v1/mcdsqs80_c21_A.txt', '49f500c5eedd9a79553e1228d0232e203a749bbda04e3a891c52778dbe9d44a3')]:
        raw, lean = raw_read(HERE / rel, gc), lean_read(gc)
        require(raw['sha256'] == expected, 'raw SHA mismatch')
        compare(raw, lean)
        controls = []
        for kind in ['block', 'class'] + (['group'] if gc else []):
            changed = copy.deepcopy(lean)
            if kind == 'block':
                changed['blocks'][0] = (79,) + changed['blocks'][0][1:]
                wanted = 'BLOCKS mismatch'
            elif kind == 'class':
                changed['points'][0][0], changed['points'][0][1] = changed['points'][0][1], changed['points'][0][0]
                wanted = 'POINT 0 CLASS 0 mismatch'
            else:
                changed['groups'][0][0] = 79
                wanted = 'GROUPS mismatch'
            try:
                compare(raw, changed)
            except ValueError as e:
                require(str(e) == wanted, 'wrong mutation rejection')
                controls.append({'kind':kind,'rejection':str(e)})
            else:
                raise ValueError('mutation accepted: ' + kind)
        records.append({'raw_file':rel,'sha256':expected,'blocks_equal_in_order':len(raw['blocks']),
                        'points_equal_in_order':80,'classes_equal_in_order':3200,
                        'triples_equal_in_order':sum(len(C) for P in raw['points'] for C in P),
                        'groups_equal_in_order':len(raw['groups']),'controls':controls})
    rec = {'recorded_at_pt':subprocess.check_output(['date','+%Y-%m-%d %H:%M:%S %Z'],text=True).strip(),
           'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'status':'PARENT_RAW_TO_LEAN_LITERAL_BINDING_PASS','records':records,
           'scope':'Independent literal parse/equality and aggregation-order check; design validity is covered by the definition-first checkers and kernel roots.'}
    with open(sys.argv[1], 'x') as f:
        json.dump(rec,f,indent=2)
        f.write('\n')
    print(json.dumps(rec,indent=1))


if __name__ == '__main__':
    main()
