#!/usr/bin/env python3
"""Independent literal-table and finite-control audit; no author checker imports."""
import ast
import hashlib
import itertools
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
manifest = json.loads((HERE / 'manifest-v1.json').read_text())
texts = []
for item in manifest['inputs_in_read_order']:
    blob = Path(item['path']).read_bytes()
    if hashlib.sha256(blob).hexdigest() != item['sha256']:
        raise ValueError('pinned SHA-256 mismatch: ' + item['path'])
    if len(blob) != item['bytes'] or blob.count(b'\n') != item['LF']:
        raise ValueError('pinned length/LF mismatch: ' + item['path'])
    texts.append(blob.decode('utf-8'))
print('PASS manifest input hashes and sizes: 6/6')

# Free abelian expressions in (1,U,V,W); specializing to Z_n preserves equality.
Z = (0, 0, 0, 0)
def plus(a, b): return tuple(x + y for x, y in zip(a, b))
def minus(a, b): return tuple(x - y for x, y in zip(a, b))
def times(k, a): return tuple(k * x for x in a)
def value(node, env):
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return (node.value, 0, 0, 0)
    if isinstance(node, ast.Name) and node.id in env: return env[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return times(-1, value(node.operand, env))
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return plus(value(node.left, env), value(node.right, env))
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
        return minus(value(node.left, env), value(node.right, env))
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
        if isinstance(node.left, ast.Constant) and type(node.left.value) is int:
            return times(node.left.value, value(node.right, env))
        if isinstance(node.right, ast.Constant) and type(node.right.value) is int:
            return times(node.right.value, value(node.left, env))
    raise ValueError('unsupported expression ' + ast.dump(node))
def expr(s, env): return value(ast.parse(s.strip(), mode='eval').body, env)
def check(cond, msg):
    if not cond: raise AssertionError(msg)
def same(actual, wanted, env):
    check(actual == expr(wanted, env), f'{actual} != {wanted}')
def read_rows(text):
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines):
        if not line.startswith('| target t |'): continue
        columns = [c.strip()[2:] for c in line.strip('|').split('|')[1:]]
        check(lines[i+1].startswith('|---'), f'bad separator at {i+2}')
        j = i + 2
        while j < len(lines) and lines[j].startswith('| '):
            cells = [c.strip() for c in lines[j].strip('|').split('|')]
            check(len(cells) == len(columns)+1, f'bad width at {j+1}')
            out.append((j+1, columns, cells[0], cells[1:]))
            j += 1
    return out

checks = 0
def audit(row, group, known, env, survivors):
    global checks
    line, columns, target, cells = row
    check(columns == group, f'line {line}: wrong source columns {columns}')
    check(len(set(columns)) == len(group), f'line {line}: duplicate source')
    got = []
    for source, cell in zip(columns, cells):
        candidate = minus(expr(target, env), expr(source, env))
        if cell == '*':
            got.append((source, candidate))
            continue
        m = re.fullmatch(r'([^/]+)/\(([^,]+),([^,]+)\)', cell)
        check(m is not None, f'line {line}: invalid cell {cell}')
        k, q, q2 = (v.strip() for v in m.groups())
        check(q in group and q2 in group and q != q2,
              f'line {line}: witness elements not distinct group sources: {cell}')
        check(expr(k, env) in known, f'line {line}: witness {k} not yet known')
        check(plus(candidate, expr(q, env)) == plus(expr(k, env), expr(q2, env)),
              f'line {line}: incorrect identity for source {source}: {cell}')
        checks += 1
    check([v[0] for v in got] == survivors,
          f'line {line}: unexpected survivors {got} vs {survivors}')
    return [v[1] for v in got]

def base(): return {'U':(0,1,0,0), 'V':(0,0,1,0), 'W':(0,0,0,1)}
def anchors(xs, env): return {expr(str(x), env) for x in xs}
def force(name, v, known, env, wanted):
    same(v, wanted, env)
    env[name] = v
    known.add(v)

eight = read_rows(texts[1])
check([x[0] for x in eight] == [33,34,44,50,51,59], 'unexpected eight-tail tables')
A = [0,3,8,11]
env=base(); known=anchors(A,env); group=['0','1','7','13','14','V']
force('D', audit(eight[0],group,known,env,['1'])[0],known,env,'V+6')
audit(eight[1],group,known,env,[])
env=base(); known=anchors(A,env); group=['0','1','7','13','14','U','V']
root=audit(eight[2],group,known,env,['13','U'])
same(root[0],'V-12',env); same(root[1],'V-U+1',env)
env1=dict(env); p=set(known); force('B',root[0],p,env1,'V-12')
force('D',audit(eight[3],group,p,env1,['V'])[0],p,env1,'U-V+2')
force('E',audit(eight[4],group,p,env1,['V'])[0],p,env1,'U-V+1')
check(plus(env1['D'],expr('0',env1)) == plus(env1['E'],expr('1',env1)), 'eight-tail final collision')
env2=dict(env); p=set(known); force('B',root[1],p,env2,'V-U+1')
audit(eight[5],group,p,env2,[])
print(f'PASS eight-tail: 6 literal rows, {checks} collision cells, both branches')

before = checks
nine = read_rows(texts[3])
check([x[0] for x in nine] == [31,39,47,48,49,59,60,61,69,70,71,72], 'unexpected nine-tail tables')
env=base(); known=anchors(A,env); group=['0','1','7','13','14','U','V','W']
root=audit(nine[0],group,known,env,['13','U','V'])
same(root[0],'W-12',env); same(root[1],'W-U+1',env); same(root[2],'W-V+1',env)
def swap_uv(v): return (v[0],v[2],v[1],v[3])
check(swap_uv(root[1]) == root[2], 'root symmetry')
check({swap_uv(expr(x,env)) for x in group} == {expr(x,env) for x in group}, 'Q symmetry')
enva=dict(env); common=set(known); force('B',root[0],common,enva,'W-12')
second=audit(nine[1],group,common,enva,['U','W'])
same(second[0],'V-U+1',enva); same(second[1],'V-W+1',enva)
env1=dict(enva); p=set(common); force('T',second[0],p,env1,'V-U+1')
force('D',audit(nine[2],group,p,env1,['W'])[0],p,env1,'V-W+2')
force('E',audit(nine[3],group,p,env1,['V'])[0],p,env1,'U-V+2')
force('F',audit(nine[4],group,p,env1,['V'])[0],p,env1,'2-V')
check(plus(env1['E'],expr('0',env1)) == plus(env1['F'],expr('U',env1)), 'nine-tail A1 collision')
env2=dict(enva); p=set(common); force('T',second[1],p,env2,'V-W+1')
force('D',audit(nine[5],group,p,env2,['U'])[0],p,env2,'V-U+2')
force('E',audit(nine[6],group,p,env2,['V'])[0],p,env2,'U-V+1')
audit(nine[7],group,p,env2,[])
envb=dict(env); p=set(known); force('B',root[1],p,envb,'W-U+1')
force('D',audit(nine[8],group,p,envb,['V'])[0],p,envb,'W-V+2')
force('E',audit(nine[9],group,p,envb,['W'])[0],p,envb,'2-W')
force('F',audit(nine[10],group,p,envb,['13'])[0],p,envb,'V-12')
force('G',audit(nine[11],group,p,envb,['14'])[0],p,envb,'U-12')
check(plus(envb['F'],expr('U',envb)) == plus(envb['G'],expr('V',envb)), 'nine-tail B collision')
print(f'PASS nine-tail: 12 literal rows, {checks-before} collision cells, all branches and U/V symmetry')

# Independently audit the explicit literal tables in the unpinned eight-head prerequisite.
# Its SHA is reported, not promoted as a manifest pin.
headpath = Path(manifest['inputs_in_read_order'][0]['path']).with_name('frontier-20261028-eight-head-border-obstruction-v1.md')
headbytes=headpath.read_bytes()
print('eight-head prerequisite SHA256:',hashlib.sha256(headbytes).hexdigest())
head=read_rows(headbytes.decode())
check([x[0] for x in head] == [31,32,33,43,44,45,46,54,55,56], 'unexpected eight-head tables')
before=checks
env=base(); group=['0','3','8','11','U','V','W']; known=anchors([0,1,7,13,14],env)
root=audit(head[0],group,known,env,['V','W'])
same(root[0],'U-V+4',env); same(root[1],'U-W+4',env)
force('E',root[0],known,env,'U-V+4')
force('F',audit(head[1],group,known,env,['U'])[0],known,env,'W-U+4')
branch=audit(head[2],group,known,env,['0','V'])
same(branch[0],'W+9',env); same(branch[1],'W-V+9',env)
env1=dict(env); p=set(known); force('B',branch[0],p,env1,'W+9')
force('C',audit(head[3],group,p,env1,['W'])[0],p,env1,'U-W+9')
force('D',audit(head[4],group,p,env1,['0'])[0],p,env1,'U+12')
force('H',audit(head[5],group,p,env1,['V'])[0],p,env1,'W-2*V+12')
audit(head[6],group,p,env1,[])
env2=dict(env); p=set(known); force('B',branch[1],p,env2,'W-V+9')
force('D',audit(head[7],group,p,env2,['0'])[0],p,env2,'W+12')
force('H',audit(head[8],group,p,env2,['V'])[0],p,env2,'U-2*V+W+12')
force('I',audit(head[9],group,p,env2,['V'])[0],p,env2,'W-2*V+15')
check(plus(env2['H'],expr('3',env2)) == plus(env2['I'],expr('U',env2)), 'eight-head collision')
print(f'PASS eight-head prerequisite: 10 literal rows, {checks-before} collision cells')

# Reconstruct the small-head prerequisite independently from the displayed equations.
before=checks; env=base(); oldQ=anchors([0,1,7,13,14],env)
audit((0,['0','3','8','11'],'6',['1/(3,8)','0/(0,3)','1/(3,0)','0/(8,3)']),
      ['0','3','8','11'],oldQ,env,[])
audit((0,['0','3','8','11','U'],'U+4',
       ['7/(3,U)','1/(0,U)','7/(11,U)','1/(8,U)','1/(0,3)']),
      ['0','3','8','11','U'],oldQ,env,[])
group=['0','3','8','11','U','V']
e=audit((0,group,'U+4',['7/(3,U)','1/(0,U)','7/(11,U)','1/(8,U)','1/(0,3)','*']),
        group,oldQ,env,['V'])[0]
same(e,'U-V+4',env); env['E']=e; oldQ.add(e)
f=audit((0,group,'U+9',['*','14/(8,U)','1/(0,U)','1/(3,U)','1/(0,8)','E/(3,8)']),
        group,oldQ,env,['0'])[0]
same(f,'U+9',env)
check(plus(f,expr('V',env)) == plus(expr('V+9',env),expr('U',env)), 'six-head collision')
print(f'PASS size-4/5/6 P prerequisite: {checks-before} reconstructed collision identities and symmetry')

# Check both literal derangement tables, including which old P-pair each equation uses.
lines=texts[5].splitlines(); tabs=[]
for i,line in enumerate(lines):
    if line.startswith('| source in P |'):
        j=i+2
        while j<len(lines) and lines[j].startswith('| '):
            tabs.append((j+1,[v.strip() for v in lines[j].strip('|').split('|')]))
            j+=1
check(len(tabs)==10,'derangement table dimensions')
env=base(); env['x']=env['U']; oldp=anchors(A,env); oldp.add(env['x']); oldq=anchors([0,1,7,13,14],env)
for index,(line,cells) in enumerate(tabs):
    source,candidate,equation=cells
    offset=4 if index<5 else 10
    check(expr(candidate,env)==minus(expr('x+'+str(offset),env),expr(source,env)), f'derangement candidate line {line}')
    lhs,rhs=equation.split('=')
    l=ast.parse(lhs,mode='eval').body; r=ast.parse(rhs,mode='eval').body
    check(isinstance(l,ast.BinOp) and isinstance(l.op,ast.Add) and isinstance(r,ast.BinOp) and isinstance(r.op,ast.Add), f'bad equation {line}')
    cand=value(l.left,env); p1=value(l.right,env); q=value(r.left,env); p2=value(r.right,env)
    check(cand==expr(candidate,env) and p1 in oldp and p2 in oldp and p1!=p2 and q in oldq, f'bad collision witnesses {line}')
    check(value(l,env)==value(r,env),f'bad collision equality {line}')
derangements=[p for p in itertools.permutations(range(4)) if all(p[i]!=i for i in range(4))]
def cycles(p):
    seen=set(); lens=[]
    for i in range(4):
        if i in seen: continue
        x=i; length=0
        while x not in seen:
            seen.add(x); length+=1; x=p[x]
        lens.append(length)
    return tuple(sorted(lens))
cycle_counts={k:sum(cycles(p)==k for p in derangements) for k in {(4,),(2,2)}}
check(cycle_counts=={(4,):6,(2,2):3},'S4 derangement types')
print('PASS derangement tables: 10 literal identities; S4 cycle counts',cycle_counts)

# A bare five-element tail set cannot cover 2.
env=base(); p=anchors(A,env); group=['0','1','7','13','14']
audit((0,group,'2',['3/(1,0)','0/(0,1)','8/(13,0)','3/(14,0)','0/(13,1)']),
      group,p,env,[])
print('PASS five-tail prerequisite: all 5 target-2 candidates forbidden')

# Intended-reason mutations of one literal table cell.
env=base(); p=anchors(A,env); group=['0','1','7','13','14','V']
for changed,reason in [('8/(0,V)','incorrect identity'),
                       ('9/(1,V)','not yet known'),
                       ('8/(1,1)','not distinct group sources')]:
    line,columns,target,cells=eight[0]
    mutated=list(cells); mutated[0]=changed
    try:
        audit((line,columns,target,mutated),group,p,env,['1'])
    except AssertionError as err:
        check(reason in str(err), f'unintended mutation rejection: {err}')
    else:
        raise AssertionError('bad collision certificate accepted: '+changed)
print('PASS three intended-reason collision-table mutation controls')

# Direct anchor and conditional n=1320 arithmetic.
Y=[0,1,7,13,14]
for n in range(1,26):
    check(len({(a+y)%n for a in A for y in Y})<20, f'unexpected viable n={n}')
ps=[d for d in range(1,1321) if 1320%d==0 and d>=8 and 1320//d>=9 and d not in (8,11)]
expected=[10,12,15,20,22,24,30,33,40,44,55,60,66,88,110,120,132]
check(ps==expected,'1320 divisor list')
heads=[1320-4*(1320//(10-m)) for m in range(6)]
tails=[1320-5*(1320//(10-m)) for m in range(5)]
check(heads==[792,736,660,568,440,264] and tails==[660,590,495,380,220],'1320 thresholds')
print('PASS n<26 anchors, 1320 divisor list and both numeric threshold tables')

# Independently reconstruct the graded packet's tiny Sardinas-Patterson controls.
def is_ud(code):
    code=tuple(code)
    residual={v[len(u):] for u in code for v in code if u!=v and v.startswith(u)}
    seen=set()
    while residual:
        if '' in residual: return False
        key=frozenset(residual)
        if key in seen: return True
        seen.add(key); nxt=set()
        for u in residual:
            for v in code:
                if u.startswith(v): nxt.add(u[len(v):])
                if v.startswith(u): nxt.add(v[len(u):])
        residual=nxt
    return True

check(is_ud(('aa','b','ab')), 'positive prefix-free control rejected')
check(not is_ud(('aa','b','aab')), 'direct aab=aa+b ambiguity accepted')
print('PASS Sardinas-Patterson positive and direct-ambiguity controls')
inclusive=['a'*i+'b'*k for i in range(4) for k in range(1,4)]
check(len(list(itertools.combinations(inclusive,2)))==66, 'inclusive n=2 pair count')
check('b' in inclusive and 'ab' in inclusive and is_ud({'aa','b','b','ab'}),
      'inclusive n=2 UD witness missing')
print('PASS minor control-domain witness: inclusive n=2 gives 66 pairs and {aa,b,ab} is UD')
observed=[]
for n in range(2,7):
    words=[('a'*i+'b'*k,i%n) for i in range(2*n) for k in range(1,4) if not (i==0 and k==1)]
    total=ud=dup=0
    for (u,ru),(v,rv) in itertools.combinations(words,2):
        total+=1; ok=is_ud(('a'*n,'b',u,v)); ud+=int(ok)
        if ru==0 or rv==0 or ru==rv:
            dup+=1
            check(not ok, f'repeated border head accepted n={n}')
    observed.append((n,total,ud,dup))
expected=[(2,55,0,55),(3,136,36,100),(4,253,108,145),(5,406,216,190),(6,595,360,235)]
check(observed==expected, f'SP controls differ: {observed}')
print('PASS independently implemented SP synthetic controls:',observed)
print('LIMIT: necessary border/packing statements only; no completion or n=1320 exclusion')
