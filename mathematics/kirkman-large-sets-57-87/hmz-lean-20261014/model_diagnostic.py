import sys,faulthandler,json
from pathlib import Path
faulthandler.enable()
sys.dont_write_bytecode=True
ROOT = Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent / 'work'))
import c19_search as c19
from ortools.sat.python import cp_model
print('imports',flush=True)
data,_=c19.inventory()
print('inventory',flush=True)
p=json.loads((ROOT / 'evidence/joint57/retained16.json').read_text())
forbidden=set().union(*(set(c['orbit_ids']) for c in p))
m,rows=c19.fixed_model(data,forbidden,5,cp_model)
print('fixed built',len(rows),len(m.proto.variables),len(m.proto.constraints),flush=True)
print('domain',list(m.proto.constraints[-1].linear.domain),flush=True)
m.proto.constraints[-1].linear.domain[0]=4
m.proto.constraints[-1].linear.domain[1]=9
print('modified domain',list(m.proto.constraints[-1].linear.domain),flush=True)
v=m.get_bool_var_from_proto_index(0)
print('getvar',v.index,flush=True)
cols={oid:[] for oid in sorted(set(range(1540))-forbidden)}
for i,(oid,shift) in enumerate(rows):
    cols[oid].append(m.get_bool_var_from_proto_index(i))
print('all fixed vars',sum(map(len,cols.values())),flush=True)
for _ in range(41496):
    m.new_bool_var('')
print('all vars',len(m.proto.variables),flush=True)
print('valid',m.validate(),flush=True)
