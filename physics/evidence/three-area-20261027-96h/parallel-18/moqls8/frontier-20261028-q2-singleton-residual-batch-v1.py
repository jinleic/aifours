#!/usr/bin/env python3
"""Bounded owner-local proof batch for nine remaining unordered singleton pairs."""
import argparse,datetime,hashlib,importlib.util,itertools,json,pathlib
H=pathlib.Path(__file__).parent
MODS=[('enc','frontier-20261028-q2-singleton-pair-cnf-v1.py','3ea39b618f86880058b0afc0471641f2cf225962f2ce4849e451bd6d7a3fce49'),
      ('audit','frontier-20261028-q2-singleton-pair-cnf-check-v1.py','ab6be653af9cd19d93a86f116f421fe65d72b41af1bc7ad74dbce9d7bd6fe1c3'),
      ('runner','frontier-20261028-q2-nonmax-proof-batch-v1.py','b6dcc9cea6d1b9ce5ce963545ba237433a18d44a45a9fba3304c2bb2355aea75')]
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(path,h):
 b=pathlib.Path(path).read_bytes()
 if sha(b)!=h:raise ValueError('pin '+str(path))
 return b
mods={}
for name,file,h in MODS:
 pin(H/file,h);s=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);mods[name]=m
PAIR='frontier-20261028-source-wanless-nonmax2-pair17-v1.txt';PS='14471ce215e3c97e1fcaa4109bbd58dca4438adc5039e1d8df11d5f46d029415'

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();pin(H/PAIR,PS)
 T=mods['enc'].card.match.prod.base.pair(H/PAIR,PS);axes=[3,4,5,6,7];cases=[z for z in itertools.combinations(axes,2) if z!=(3,4)]
 run=mods['runner'];fifo=run.mods['fifo'];ctl=run.controls('single17-rest');records=[];start=datetime.datetime.now().astimezone().isoformat()
 for t,u in cases:
  data,info=mods['enc'].build(T,t,u);n,C,allpairs=mods['audit'].expected(H/PAIR,PS,t,u);m,D=mods['audit'].card.sym.prod.audit.parse(data)
  if n!=m or C!=D or [list(z) for z in allpairs]!=info['all_unordered_axes']:raise ValueError('independent CNF mismatch')
  stem=H/f'frontier-20261028-q2-nonmax17-singleton{t}{u}-v1';cnf=pathlib.Path(str(stem)+'.cnf');proof=pathlib.Path(str(stem)+'-proof.drup');receipt=pathlib.Path(str(stem)+'-receipt.json')
  if any(z.exists() for z in (cnf,proof,receipt)):raise ValueError('existing case output')
  with cnf.open('xb') as f:f.write(data)
  pin(cnf,info['formula_sha256']);obs=run.solver(cnf,proof);P=proof.read_bytes() if proof.exists() else b''
  rec={'axes':[t,u],'formula':cnf.name,'formula_sha256':sha(data),'formula_bytes':len(data),
       'independent_clause_multiset':'PASS','all_unordered_axes':info['all_unordered_axes'],'solver':obs,
       'proof':proof.name if proof.exists() else None,'proof_sha256':sha(P) if proof.exists() else None,'proof_bytes':len(P),
       'replay':None,'outcome':'UNKNOWN'}
  if obs['returncode']==20 and obs['status_lines']==['s UNSATISFIABLE'] and not obs['stop'] and not obs['stderr']:
   steps=fifo.parse_ascii(P,info['variables']);binary=fifo.encode(steps)
   if fifo.decode(binary)!=steps:raise ValueError('conversion')
   rep=fifo.run(f'single17-{t}{u}',data,binary,data,binary);rec['replay']=rep;rec['ascii_steps']=len(steps);rec['binary_proof_sha256']=sha(binary)
   if rep['strict_pass']:rec['outcome']='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW'
  elif obs['returncode']==10 and obs['status_lines']==['s SATISFIABLE'] and not obs['stop']:
   rec['outcome']='SAT_SUPPORT_ONLY_NOT_PHYSICAL_WITNESS'
  with receipt.open('x',encoding='utf-8') as h:json.dump(rec,h,indent=2);h.write('\n')
  rec['case_receipt']=receipt.name;rec['case_receipt_sha256']=sha(receipt.read_bytes());records.append(rec)
 out={'result':'BOUNDED_SINGLETON_BRANCH_BATCH_COMPLETE','source_sha256':sha(pathlib.Path(__file__).read_bytes()),
      'modules':{file:h for name,file,h in MODS},'pair_sha256':PS,'start':start,'end':datetime.datetime.now().astimezone().isoformat(),
      'controls':ctl,'records':records,'limits':'All ten unordered pairs must be independently accepted before closing singleton/singleton. Any UNKNOWN is open; SAT support not physical.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({'result':out['result'],'outcomes':[(r['axes'],r['outcome']) for r in records]},indent=2))
if __name__=='__main__':main()
