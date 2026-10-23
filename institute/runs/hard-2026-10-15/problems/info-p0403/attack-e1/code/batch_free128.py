"""Bounded production/audit of the four parallel 128-point classes per seed."""
import json
from pathlib import Path
import subprocess
import time
from free_flat_sat import produce


def command(args,log=None,expected=(0,)):
    if log:
        with open(log,'w') as out: result=subprocess.run(args,stdout=out,stderr=subprocess.STDOUT)
    else: result=subprocess.run(args)
    assert result.returncode in expected,(args,result.returncode)


flat=json.loads(Path('results/flat-class.json').read_text())
cases=[]
planned=[]
for seed,info in flat['seeds'].items():
    basis=info['basis'].copy()
    V={0}
    for b in basis: V|={v^b for v in list(V)}
    for bit in (1<<j for j in range(9)):
        if len(basis)==7: break
        if bit not in V:
            basis.append(bit); V|={v^bit for v in list(V)}
    assert len(V)==128
    reps=sorted({min(x^v for v in V) for x in range(512)})
    assert len(reps)==4
    for rep in reps: planned.append((seed,basis.copy(),rep))

for number,(seed,basis,rep) in enumerate(planned,1):
    if sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file())>780*1024**2:
        print('Stopping batch before disk budget; unfinished cases remain.',flush=True)
        break
    prefix='results/%s-free128-origin%d'%(seed,rep)
    origin=rep
    if seed=='dsbf40' and rep==0:
        prefix='results/dsbf40-free128'; origin=5
    print('case',number,'of',len(planned),prefix,'basis',basis,'origin',origin,flush=True)
    if not Path(prefix+'.cnf').exists(): produce(seed,basis,origin,prefix)
    runpath=Path(prefix+'-run.json')
    if not runpath.exists(): command(['python3','code/run_cadical.py',prefix,'--seconds','60','--proof-mb','60'])
    status=json.loads(runpath.read_text())['status']
    if status!='UNSAT':
        cases.append({'seed':seed,'basis':basis,'coset_representative':rep,'origin':origin,'prefix':prefix,'status':status})
        continue
    command(['python3','code/audit_free_flat.py',prefix,'--output',prefix+'-encoding-audit.json'],log='logs/'+Path(prefix).name+'-audit.log')
    command(['python3','code/check_lrat.py',prefix+'.cnf',prefix+'.lrat.gz','--output',prefix+'-proof-check.json'],log='logs/'+Path(prefix).name+'-proof-check.log')
    control=prefix+'-control'; inp=control+'-input.json'
    command(['python3','code/free_flat_control.py',prefix,'--output',inp])
    produce(seed,basis,origin,control,bound=32,force_json=inp)
    controllog='logs/'+Path(control).name+'-solver.log'
    command(['cadical','-t','30',control+'.cnf'],log=controllog,expected=(10,))
    command(['python3','code/audit_free_flat.py',control,'--model-log',controllog,'--output',control+'-audit.json'],log='logs/'+Path(control).name+'-audit.log')
    cases.append({'seed':seed,'basis':basis,'coset_representative':rep,'origin':origin,'prefix':prefix,'control_prefix':control,'control_model_log':controllog,'status':'UNSAT, encoding audited, LRAT checked, planted SAT control checked'})
    result={'planned_cases':len(planned),'complete':len(cases)==len(planned) and all(c['status'].startswith('UNSAT, encoding') for c in cases),'cases':cases,'scope':'arbitrary changes on any one coset of the explicitly specified 128-point linear space for each seed, followed by any linear output shift; restricted union only'}
    Path('results/free128-batch.json').write_text(json.dumps(result,indent=2)+'\n')
print('finished checked cases',len(cases),'of',len(planned),flush=True)
