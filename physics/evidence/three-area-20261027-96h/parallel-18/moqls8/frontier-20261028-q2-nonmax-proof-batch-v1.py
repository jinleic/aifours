#!/usr/bin/env python3
"""Serial bounded q2 net proofs with independently checked CNFs and measured replay."""
import argparse,datetime,hashlib,importlib.util,json,os,pathlib,shutil,signal,subprocess,time
H=pathlib.Path(__file__).parent
MODULES=[('enc','frontier-20261028-q2-net-triangle-cnf-v1.py','f2db8cd92f24ed93ace21d9971dede1832df30bc4c893220c2dcc8d268d51d0a'),
         ('audit','frontier-20261028-q2-support-cnf-check-v3.py','c95730409fec6bb10488fcfc22f96dbe19ce42fd73ca0e6c1ab4e2a12204249c'),
         ('fifo','frontier-20261028-q2-measured-fifo-replay-v3.py','0e2b5e95f5cf25a8c4a4e9b175b60d8165bfa29257467c399647d1ce11508945')]
EXTRACT='frontier-20261028-nonmax2-net-extract-receipt-v1.json';ESHA='cda00277e356426194cc2051d7e92b32ad6f639f017f621ef0b69e9d0fbcdf8d'
SOLVER='/opt/homebrew/bin/kissat';SPIN='05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848';FLOOR=2*1024**3

def sha(x):return hashlib.sha256(x).hexdigest()
def pin(path,expected):
 b=pathlib.Path(path).read_bytes()
 if sha(b)!=expected:raise ValueError('pin '+str(path))
 return b
mods={}
for name,file,h in MODULES:
 pin(H/file,h);s=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);mods[name]=m

def solver(cnf,proof):
 if shutil.disk_usage(H).free<FLOOR:raise ValueError('disk floor')
 pin(SOLVER,SPIN);begin=time.monotonic();p=None;stop=None
 args=[SOLVER,'--quiet','--plain','--no-binary','--no-preprocess','--no-eliminate','--no-substitute','--no-factor','--no-probe','--no-sweep','--no-vivify','--no-transitive','--time=3','--conflicts=50000',str(cnf),str(proof)]
 try:
  p=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True);pid=p.pid
  while p.poll() is None:
   if time.monotonic()-begin>4:stop='wall';break
   if shutil.disk_usage(H).free<FLOOR:stop='disk';break
   if proof.exists() and proof.stat().st_size>20*1024**2:stop='proof_size';break
   time.sleep(.01)
  if stop is not None and p.poll() is None:
   try:os.killpg(p.pid,signal.SIGTERM)
   except ProcessLookupError:pass
  stdout,stderr=p.communicate();rc=p.returncode;p=None
 finally:
  if p is not None:
   if p.poll() is None:
    try:os.killpg(p.pid,signal.SIGTERM)
    except ProcessLookupError:pass
   p.communicate()
 pin(SOLVER,SPIN)
 txt=stdout.decode('utf-8','strict');err=stderr.decode('utf-8','strict')
 return {'pid':pid,'returncode':rc,'status_lines':[z.replace('\r','') for z in txt.split('\n') if z.replace('\r','').startswith('s ')],
         'stdout':txt,'stderr':err,'stop':stop,'wall_seconds':time.monotonic()-begin,'solver_sha256':SPIN}

def controls(label):
 f=mods['fifo'];pc=b'p cnf 2 4\n1 2 0\n-1 2 0\n1 -2 0\n-1 -2 0\n';pp=f.encode([(False,(2,)),(False,())]);nc=b'p cnf 1 1\n1 0\n';np=f.encode([(False,())]);wc=b'p cnf 2 1\n1 0\n'
 tests={'positive':f.run(label+'-pos',pc,pp,pc,pp), 'sat_empty':f.run(label+'-sat',nc,np,nc,np),
        'wrong_formula':f.run(label+'-wrong',wc,pp,wc,pp),'truncated_cnf':f.run(label+'-tcnf',pc[:-7],pp,pc,pp),
        'truncated_proof':f.run(label+'-tproof',pc,pp[:-2],pc,pp)}
 if not tests['positive']['strict_pass']:raise ValueError('positive control')
 if tests['sat_empty']['returncode']!=1 or tests['sat_empty']['status_lines']!=['s NOT VERIFIED'] or not tests['sat_empty']['transport_exact']:raise ValueError('sat control')
 if tests['wrong_formula']['status_lines']!=['s NOT VERIFIED'] or tests['wrong_formula']['strict_pass']:raise ValueError('wrong formula control')
 for k in ('truncated_cnf','truncated_proof'):
  if tests[k]['strict_pass'] or tests[k]['transport_exact']:raise ValueError(k+' control')
 return {k:{'returncode':v['returncode'],'status_lines':v['status_lines'],'transport_exact':v['transport_exact'],'strict_pass':v['strict_pass']} for k,v in tests.items()}

def main():
 p=argparse.ArgumentParser();p.add_argument('--start',type=int,required=True);p.add_argument('--end',type=int,required=True);p.add_argument('--output',required=True);a=p.parse_args()
 if a.start<1 or a.end>37 or a.start>a.end:raise ValueError('index range; 0 handled separately')
 ex=json.loads(pin(H/EXTRACT,ESHA));items={x['index']:x for x in ex['pairs']}
 if set(items)!=set(range(1,38)):raise ValueError('source coverage')
 label=f'nb{a.start:02d}-{a.end:02d}';ctl=controls(label);records=[];start=datetime.datetime.now().astimezone().isoformat()
 for i in range(a.start,a.end+1):
  item=items[i];pair=H/item['file'];pin(pair,item['sha256'])
  T=mods['enc'].pair(pair,item['sha256']);data,info=mods['enc'].build(T)
  expect_n,expect,tri=mods['audit'].expected(mods['audit'].facts(pair,item['sha256']));got_n,got=mods['audit'].parse(data)
  if expect_n!=got_n or expect!=got or tri!=info['axis_triangles']:raise ValueError('independent CNF mismatch')
  prefix=H/f'frontier-20261028-q2-nonmax-batch-p{i:02d}-v1';cnf=pathlib.Path(str(prefix)+'.cnf');proof=pathlib.Path(str(prefix)+'.drup');receipt=pathlib.Path(str(prefix)+'-receipt.json')
  if any(x.exists() for x in (cnf,proof,receipt)):raise ValueError('existing case output')
  with cnf.open('xb') as h:h.write(data)
  if pin(cnf,info['formula_sha256'])!=data:raise ValueError('formula write')
  observed=solver(cnf,proof);P=proof.read_bytes() if proof.exists() else b''
  rec={'index':i,'pair':item,'formula':cnf.name,'formula_sha256':sha(data),'formula_bytes':len(data),
       'independent_clause_multiset':'PASS','solver':observed,'proof':proof.name if proof.exists() else None,
       'proof_sha256':sha(P) if proof.exists() else None,'proof_bytes':len(P),'replay':None,'outcome':'UNKNOWN'}
  if observed['returncode']==20 and observed['status_lines']==['s UNSATISFIABLE'] and observed['stop'] is None and not observed['stderr']:
   steps=mods['fifo'].parse_ascii(P,info['variables']);B=mods['fifo'].encode(steps)
   if mods['fifo'].decode(B)!=steps:raise ValueError('proof conversion mismatch')
   replay=mods['fifo'].run(label+f'-p{i:02d}',data,B,data,B)
   rec['replay']=replay;rec['binary_proof_sha256']=sha(B);rec['ascii_steps']=len(steps)
   if replay['strict_pass']:rec['outcome']='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW'
  elif observed['returncode']==10 and observed['status_lines']==['s SATISFIABLE'] and observed['stop'] is None:
   rec['outcome']='SAT_SUPPORT_ONLY_NOT_PHYSICAL_WITNESS'
  with receipt.open('x',encoding='utf-8') as h:json.dump(rec,h,indent=2);h.write('\n')
  rec['case_receipt']=receipt.name;rec['case_receipt_sha256']=sha(receipt.read_bytes());records.append(rec)
 out={'result':'BOUNDED_BATCH_COMPLETE','source_sha256':sha(pathlib.Path(__file__).read_bytes()),
      'source_extraction_receipt_sha256':ESHA,'modules':{file:h for name,file,h in MODULES},
      'start':start,'end':datetime.datetime.now().astimezone().isoformat(),'range':[a.start,a.end],
      'preflight_controls':ctl,'records':records,
      'limits':'Each UNSAT owner replay needs independent parent verification and disjoint physics/CNF review; SAT support is not a physical witness; UNKNOWN remains unresolved.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({'result':out['result'],'range':out['range'],'outcomes':[(z['index'],z['outcome']) for z in records]},indent=2))
if __name__=='__main__':main()
