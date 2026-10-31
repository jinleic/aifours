#!/usr/bin/env python3
"""Sequential bounded q1 CNF/proof production with two local RUP replayers.

Stored proof and formula artifacts are intentional. No parent drat-trim/FIFO
replay or independent mathematical review is claimed here.
"""
import argparse,datetime,hashlib,importlib.util,json,os,pathlib,shutil,signal,subprocess,time
H=pathlib.Path(__file__).parent
MODULES=[('enc','frontier-20261028-q1-support-cnf-v1.py','4c95605057d0dd540041b905f889b68e35fb6a8682011faed021a403c0cd4d53'),
         ('audit','frontier-20261028-q1-support-cnf-check-v1.py','e824a35b1f304ce8472770d1d281a36d88ce983a95b480ce7de2697d0f19021b'),
         ('rup','frontier-20261028-rup-proof-check-v1.py','82e0b595da1798a67e83fc2b80885856dab3c004b07abddadb04fb59f31c08cc'),
         ('scan','frontier-20261028-rup-scan-check-v1.py','77fdc7f3918c6945adce1e7124c6e21552da1d57fbcedad3c52549e73c39321c')]
SOLVER='/opt/homebrew/bin/kissat';SOLVER_SHA='05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848';FLOOR=2*1024**3

def digest(b):return hashlib.sha256(b).hexdigest()
def filehash(p):return digest(pathlib.Path(p).read_bytes())
def now():return datetime.datetime.now().astimezone().isoformat()
mods={}
for name,file,pin in MODULES:
 if filehash(H/file)!=pin:raise ValueError('module pin '+file)
 spec=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);mods[name]=m
if filehash(SOLVER)!=SOLVER_SHA:raise ValueError('solver pin')

def subprocess_solver(cnf,proof):
 args=[SOLVER,'--quiet','--plain','--no-binary','--no-preprocess','--no-eliminate','--no-substitute','--no-factor','--no-probe','--no-sweep','--no-vivify','--no-transitive','--time=3','--conflicts=20000',str(cnf),str(proof)]
 if shutil.disk_usage(H).free<FLOOR:raise ValueError('pre-spawn disk floor')
 if filehash(SOLVER)!=SOLVER_SHA:raise ValueError('pre-spawn solver pin')
 started=now();timer=time.monotonic();p=None;stop=None;sent=None
 try:
  p=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
  pid=p.pid
  while p.poll() is None:
   if time.monotonic()-timer>4:stop='wall_limit';break
   if shutil.disk_usage(H).free<FLOOR:stop='disk_floor';break
   if proof.exists() and proof.stat().st_size>50*1024**2:stop='proof_size_limit';break
   time.sleep(.01)
  if stop is not None and p.poll() is None:
   try:os.killpg(p.pid,signal.SIGTERM);sent='SIGTERM'
   except ProcessLookupError:sent='already_exited'
  # No KILL or wait(timeout): retain ownership and reap the one known child.
  stdout,stderr=p.communicate();rc=p.returncode;p=None
 finally:
  if p is not None:
   if p.poll() is None:
    try:os.killpg(p.pid,signal.SIGTERM)
    except ProcessLookupError:pass
   p.communicate()
 if filehash(SOLVER)!=SOLVER_SHA:raise ValueError('post-solver binary changed')
 return {'pid':pid,'started':started,'finished':now(),'returncode':rc,'stop':stop,'signal':sent,
         'stdout':stdout.decode('utf-8','strict'),'stderr':stderr.decode('utf-8','strict'),
         's_lines':[x.rstrip('\r') for x in stdout.decode('utf-8','strict').split('\n') if x.startswith('s ')],
         'wall_seconds':time.monotonic()-timer,'solver_sha256_before_after':SOLVER_SHA}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,required=True);ap.add_argument('--end',type=int,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
 if a.start<1 or a.end>38 or a.start>a.end:raise ValueError('batch range; species0 already pinned separately')
 output=pathlib.Path(a.output)
 if output.exists():raise ValueError('batch receipt exists')
 nets=mods['audit'].parse_nets()
 if len(nets)!=39:raise ValueError('catalogue')
 # Preflight soundness controls for both local replayers.
 controls={}
 for name in ('rup','scan'):
  try:mods[name].verify(b'p cnf 2 1\n1 2 0\n',b'0\n')
  except ValueError:controls[name+'_sat_empty']='rejected'
  else:raise ValueError(name+' accepts bogus SAT proof')
 cases=[];start=now();status='COMPLETE'
 for sp in range(a.start,a.end+1):
  r,c=(1,0) if sp==38 else (0,1);anchor=0
  prefix=H/f'frontier-20261028-q1-support-batch-s{sp:02d}-v1'
  cnf=pathlib.Path(str(prefix)+'.cnf');proof=pathlib.Path(str(prefix)+'.drup');receipt=pathlib.Path(str(prefix)+'-receipt.json')
  if any(p.exists() for p in (cnf,proof,receipt)):raise ValueError('case output already exists')
  data,info=mods['enc'].build(sp,r,c,anchor,True)
  with cnf.open('xb') as h:h.write(data)
  facts=mods['audit'].reconstruct(nets[sp],r,c,anchor);nv,expect,tri=mods['audit'].expected(facts);nv2,actual=mods['audit'].parse_cnf(data)
  if nv!=nv2 or expect!=actual or tri!=info['sound_two_axis_triangles']:raise ValueError('independent encoding mismatch')
  obs=subprocess_solver(cnf,proof);proof_bytes=proof.read_bytes() if proof.exists() else b''
  rec={'case':[sp,r,c,anchor],'formula':cnf.name,'formula_sha256':digest(data),'formula_bytes':len(data),
       'variables':info['variables'],'clauses':info['clauses'],'triangles':tri,'independent_clause_multiset':'PASS',
       'solver':obs,'proof':proof.name if proof.exists() else None,'proof_sha256':digest(proof_bytes) if proof.exists() else None,
       'proof_bytes':len(proof_bytes),'rup':None,'scan_rup':None,'outcome':'UNKNOWN',
       'limits':'Local proof only; no parent FIFO/drat-trim replay, independent mathematical review, Hcat or novelty clearance.'}
  if obs['returncode']==20 and obs['s_lines']==['s UNSATISFIABLE'] and obs['stop'] is None and not obs['stderr']:
   rec['rup']=mods['rup'].verify(data,proof_bytes);rec['scan_rup']=mods['scan'].verify(data,proof_bytes)
   if rec['rup']['rup_additions']!=rec['scan_rup']['additions']:raise ValueError('RUP checkers disagree')
   rec['outcome']='LOCAL_DUAL_RUP_PASS_PENDING_PARENT_REPLAY'
  elif obs['returncode']==10 and obs['s_lines']==['s SATISFIABLE'] and obs['stop'] is None:
   rec['outcome']='SAT_SUPPORT_RELAXATION_NOT_A_PHYSICAL_WITNESS'
  with receipt.open('x',encoding='utf-8') as h:json.dump(rec,h,indent=2);h.write('\n')
  rec['case_receipt']=receipt.name;rec['case_receipt_sha256']=filehash(receipt);cases.append(rec)
  if rec['outcome']=='UNKNOWN':status='PARTIAL_STOP_AFTER_UNKNOWN';break
 summary={'result':status,'batch_range':[a.start,a.end],'start':start,'end':now(),
          'source_sha256':filehash(__file__),'modules':{f:p for n,f,p in MODULES},'solver_sha256':SOLVER_SHA,
          'preflight_controls':controls,'cases_completed':len(cases),'cases':cases,
          'limits':'Necessary-support CNFs and local RUP replays only; no physical witness from SAT, no strict parent replay or classification review.'}
 with output.open('x',encoding='utf-8') as h:json.dump(summary,h,indent=2);h.write('\n')
 print(json.dumps({'result':status,'range':[a.start,a.end],'cases_completed':len(cases),
                   'outcomes':[(x['case'][0],x['outcome']) for x in cases], 'output':str(output)},indent=2))
if __name__=='__main__':main()
