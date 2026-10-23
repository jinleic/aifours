"""Deletion-based MUS over constraint groups for the resolution of D0 of a cyclic SQS(22)."""
import sys, json, collections
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, derived, CNF
v=22; ncl=10
M=SQSKM(v,[tuple((x+1)%v for x in range(v))])
cnf,rv=M.cnf(); p='runs/mus22/km.cnf'; cnf.write(p)
st,model,_=kissat(p,60,seed=int(sys.argv[1]) if len(sys.argv)>1 else 0)
sel=[j for j,x in enumerate(rv) if x in model]
blocks=M.blocks_of(sel); der=derived(blocks,0); pts=list(range(1,v))
# variables
def build(groups):
    c=CNF(); tv=[[c.var() for _ in range(ncl)] for _ in der]
    inc=collections.defaultdict(list)
    for i,t in enumerate(der):
        for q in t: inc[q].append(i)
    for g in groups:
        if g[0]=='T': c.exactly_one(tv[g[1]])
        elif g[0]=='P': c.exactly_one([tv[i][g[1]] for i in inc[g[2]]])
        elif g[0]=='A': c.add([tv[g[1]][g[2]]])
    return c
through=sorted([i for i,t in enumerate(der) if 1 in t], key=lambda i: der[i])
groups=[('T',i) for i in range(len(der))]+[('P',c,q) for c in range(ncl) for q in pts]+[('A',i,c) for c,i in enumerate(through)]
def unsat(gs):
    c=build(gs); c.write('runs/mus22/t.cnf'); st,_,_=kissat('runs/mus22/t.cnf',30,seed=1); return st=='UNSAT'
assert unsat(groups)
core=list(groups); i=0
while i < len(core):
    trial=core[:i]+core[i+1:]
    if unsat(trial): core=trial
    else: i+=1
print('MUS size',len(core))
print('T groups',sum(1 for g in core if g[0]=='T'),'P groups',sum(1 for g in core if g[0]=='P'),'A',sum(1 for g in core if g[0]=='A'))
print('points in P groups', sorted(collections.Counter(g[2] for g in core if g[0]=='P').items()))
print('classes in P groups', sorted(collections.Counter(g[1] for g in core if g[0]=='P').items()))
print('triples', [der[g[1]] for g in core if g[0]=='T'])
print('D0 triples through 11:', [t for t in der if 11 in t])
print('rows', sel)
