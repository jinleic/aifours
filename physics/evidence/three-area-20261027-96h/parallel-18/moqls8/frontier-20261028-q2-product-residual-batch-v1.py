#!/usr/bin/env python3
"""Serial bounded residual-q2 formulas with additional true pair-product clauses."""
import argparse,datetime,hashlib,importlib.util,json,pathlib
H=pathlib.Path(__file__).parent
MODS=[('prod','frontier-20261028-q2-cross-product-cnf-v1.py','34b8e208af2c42ff48b0f974cf1493bf73ac52d05260bbfc923c361879583857'),
      ('audit','frontier-20261028-q2-cross-product-cnf-check-v1.py','d67566048cffeec09dded934ea250078d965e45a60baae357cb129b59bc065fb'),
      ('runner','frontier-20261028-q2-nonmax-proof-batch-v1.py','b6dcc9cea6d1b9ce5ce963545ba237433a18d44a45a9fba3304c2bb2355aea75')]
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(path,h):
 b=pathlib.Path(path).read_bytes()
 if sha(b)!=h:raise ValueError('pin '+str(path))
 return b
mods={}
for name,file,p in MODS:
 pin(H/file,p);s=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);mods[name]=m
EX='frontier-20261028-nonmax2-net-extract-receipt-v1.json';ES='cda00277e356426194cc2051d7e92b32ad6f639f017f621ef0b69e9d0fbcdf8d'

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();cases=[16,17,35]
 ex=json.loads(pin(H/EX,ES));pairs={z['index']:z for z in ex['pairs']};runner=mods['runner'];fifo=runner.mods['fifo']
 controls=runner.controls('product-residual-16-35');records=[];begin=datetime.datetime.now().astimezone().isoformat()
 for i in cases:
  item=pairs[i];pair=H/item['file'];pin(pair,item['sha256'])
  T=mods['prod'].base.pair(pair,item['sha256']);data,info=mods['prod'].build(T)
  n,expect,k,t,np=mods['audit'].expected(pair,item['sha256']);m,actual=mods['audit'].audit.parse(data)
  if n!=m or expect!=actual or k!=info['added_clauses'] or np!=info['nonadjacent_offrow_pairs']:raise ValueError('independent CNF mismatch')
  stem=H/f'frontier-20261028-q2-nonmax{i:02d}-product-v1';cnf=pathlib.Path(str(stem)+'.cnf');proof=pathlib.Path(str(stem)+'-proof.drup');receipt=pathlib.Path(str(stem)+'-receipt.json')
  if any(z.exists() for z in (cnf,proof,receipt)):raise ValueError('existing case output')
  with cnf.open('xb') as h:h.write(data)
  pin(cnf,info['formula_sha256']);observed=runner.solver(cnf,proof);P=proof.read_bytes() if proof.exists() else b''
  rec={'index':i,'pair':item,'formula':cnf.name,'formula_sha256':sha(data),'formula_bytes':len(data),'variables':info['variables'],
       'clauses':info['clauses'],'added_cross_product_clauses':info['added_clauses'],'independent_clause_multiset':'PASS',
       'solver':observed,'proof':proof.name if proof.exists() else None,'proof_sha256':sha(P) if proof.exists() else None,
       'proof_bytes':len(P),'replay':None,'outcome':'UNKNOWN'}
  if observed['returncode']==20 and observed['status_lines']==['s UNSATISFIABLE'] and not observed['stop'] and not observed['stderr']:
   steps=fifo.parse_ascii(P,info['variables']);binary=fifo.encode(steps)
   if fifo.decode(binary)!=steps:raise ValueError('proof conversion')
   replay=fifo.run(f'product-residual-p{i:02d}',data,binary,data,binary);rec['replay']=replay
   rec['binary_proof_sha256']=sha(binary);rec['ascii_steps']=len(steps)
   if replay['strict_pass']:rec['outcome']='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW'
  elif observed['returncode']==10 and observed['status_lines']==['s SATISFIABLE'] and not observed['stop']:
   rec['outcome']='SAT_SUPPORT_ONLY_NOT_A_PHYSICAL_WITNESS'
  with receipt.open('x',encoding='utf-8') as h:json.dump(rec,h,indent=2);h.write('\n')
  rec['case_receipt']=receipt.name;rec['case_receipt_sha256']=sha(receipt.read_bytes());records.append(rec)
 out={'result':'BOUNDED_RESIDUAL_PRODUCT_BATCH_COMPLETE','source_sha256':sha(pathlib.Path(__file__).read_bytes()),
      'source_extraction_receipt_sha256':ES,'modules':{file:p for name,file,p in MODS},'start':begin,
      'end':datetime.datetime.now().astimezone().isoformat(),'preflight_controls':controls,'records':records,
      'limits':'New sound product-singleton constraints only; owner-local proofs require parent replay and disjoint mathematical/encoder review. UNKNOWN remains open.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({'result':out['result'],'outcomes':[(r['index'],r['outcome']) for r in records]},indent=2))
if __name__=='__main__':main()
