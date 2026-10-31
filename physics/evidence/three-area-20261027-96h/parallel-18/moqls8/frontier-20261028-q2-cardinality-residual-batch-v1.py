#!/usr/bin/env python3
"""Bounded separate q2 support-size cases for the one unresolved pair."""
import argparse,datetime,hashlib,importlib.util,json,pathlib
H=pathlib.Path(__file__).parent
MODS=[('enc','frontier-20261028-q2-cell-cardinality-cnf-v1.py','fbd15d78f11a878bca1696bbb395715d0902686fd1a5aaaf0377f40565fc5fb8'),
      ('audit','frontier-20261028-q2-cell-cardinality-cnf-check-v1.py','c57acc43bf2366fa66e7088b302b643b21d1e2e0ba3d0201c94b4a6390e4fa85'),
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
 cases=[(1,2),(1,3),(1,4),(2,2),(2,3)];run=mods['runner'];fifo=run.mods['fifo'];ctl=run.controls('card17-other');records=[]
 T=mods['enc'].match.prod.base.pair(H/PAIR,PS);begin=datetime.datetime.now().astimezone().isoformat()
 for x,y in cases:
  data,info=mods['enc'].build(T,x,y);n,expect,k,cases_checked,truth=mods['audit'].expected(H/PAIR,PS,x,y);n2,actual=mods['audit'].sym.prod.audit.parse(data)
  if n!=n2 or expect!=actual or k!=info['cardinality_clauses']:raise ValueError('independent formula mismatch')
  stem=H/f'frontier-20261028-q2-nonmax17-card{x}{y}-v1';cnf=pathlib.Path(str(stem)+'.cnf');proof=pathlib.Path(str(stem)+'-proof.drup');receipt=pathlib.Path(str(stem)+'-receipt.json')
  if any(z.exists() for z in (cnf,proof,receipt)):raise ValueError('existing output')
  with cnf.open('xb') as h:h.write(data)
  pin(cnf,info['formula_sha256']);obs=run.solver(cnf,proof);P=proof.read_bytes() if proof.exists() else b''
  rec={'support_sizes':[x,y],'formula':cnf.name,'formula_sha256':sha(data),'formula_bytes':len(data),
       'independent_clause_multiset':'PASS','all_six_unordered_size_pairs':cases_checked,'solver':obs,
       'proof':proof.name if proof.exists() else None,'proof_sha256':sha(P) if proof.exists() else None,'proof_bytes':len(P),
       'replay':None,'outcome':'UNKNOWN'}
  if obs['returncode']==20 and obs['status_lines']==['s UNSATISFIABLE'] and not obs['stop'] and not obs['stderr']:
   steps=fifo.parse_ascii(P,info['variables']);binary=fifo.encode(steps)
   if fifo.decode(binary)!=steps:raise ValueError('conversion')
   replay=fifo.run(f'card17-{x}{y}',data,binary,data,binary);rec['replay']=replay
   rec['ascii_steps']=len(steps);rec['binary_proof_sha256']=sha(binary)
   if replay['strict_pass']:rec['outcome']='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW'
  elif obs['returncode']==10 and obs['status_lines']==['s SATISFIABLE'] and not obs['stop']:
   rec['outcome']='SAT_SUPPORT_ONLY_NOT_PHYSICAL_WITNESS'
  with receipt.open('x',encoding='utf-8') as h:json.dump(rec,h,indent=2);h.write('\n')
  rec['case_receipt']=receipt.name;rec['case_receipt_sha256']=sha(receipt.read_bytes());records.append(rec)
 out={'result':'BOUNDED_CARDINALITY_SPLIT_COMPLETE','source_sha256':sha(pathlib.Path(__file__).read_bytes()),
      'modules':{file:h for name,file,h in MODS},'pair_sha256':PS,'start':begin,'end':datetime.datetime.now().astimezone().isoformat(),
      'controls':ctl,'records':records,'limits':'Cases only; index17 remains unresolved unless all six cases are independently accepted. SAT support is not a physical witness; UNKNOWN remains open.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({'result':out['result'],'outcomes':[(r['support_sizes'],r['outcome']) for r in records]},indent=2))
if __name__=='__main__':main()
