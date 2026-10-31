#!/usr/bin/env python3
"""Serial owner-local measured DRAT replay of all pinned q1 RUP cases."""
import argparse,datetime,hashlib,importlib.util,json,pathlib
H=pathlib.Path(__file__).parent
FM='frontier-20261028-q2-measured-fifo-replay-v3.py';FS='0e2b5e95f5cf25a8c4a4e9b175b60d8165bfa29257467c399647d1ce11508945'
MAN='frontier-20261028-q1-39-species-local-proof-manifest-v1.json';MS='23113cb67e2653c196d9b1c3a2b9cf6f8bb881031c192862a4963e3436c7887f'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(path,h):
 b=pathlib.Path(path).read_bytes()
 if sha(b)!=h:raise ValueError('pin '+str(path))
 return b
pin(H/FM,FS);spec=importlib.util.spec_from_file_location('fifo',H/FM);fifo=importlib.util.module_from_spec(spec);spec.loader.exec_module(fifo)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 manifest=json.loads(pin(H/MAN,MS));cases=manifest['records']
 if [x['species'] for x in cases]!=list(range(39)):raise ValueError('manifest coverage')
 # Exact measured controls, once per serial replay batch.
 pc=b'p cnf 2 4\n1 2 0\n-1 2 0\n1 -2 0\n-1 -2 0\n';pp=fifo.encode([(False,(2,)),(False,())]);nc=b'p cnf 1 1\n1 0\n';np=fifo.encode([(False,())]);wc=b'p cnf 2 1\n1 0\n'
 ctl={'positive':fifo.run('q1batch-pos',pc,pp,pc,pp),
      'sat_empty':fifo.run('q1batch-sat',nc,np,nc,np),
      'wrong_formula':fifo.run('q1batch-wrong',wc,pp,wc,pp),
      'truncated_cnf':fifo.run('q1batch-tcnf',pc[:-7],pp,pc,pp),
      'truncated_proof':fifo.run('q1batch-tproof',pc,pp[:-2],pc,pp)}
 if not ctl['positive']['strict_pass']:raise ValueError('positive control')
 if ctl['sat_empty']['returncode']!=1 or ctl['sat_empty']['status_lines']!=['s NOT VERIFIED'] or not ctl['sat_empty']['transport_exact']:raise ValueError('negative SAT control')
 if ctl['wrong_formula']['status_lines']!=['s NOT VERIFIED'] or ctl['wrong_formula']['strict_pass']:raise ValueError('wrong formula control')
 if any(ctl[k]['strict_pass'] or ctl[k]['transport_exact'] for k in ('truncated_cnf','truncated_proof')):raise ValueError('truncation control')
 rows=[];start=datetime.datetime.now().astimezone().isoformat()
 for rec in cases:
  i=rec['species'];cnf=pin(H/rec['formula'],rec['formula_sha256']);proof=pin(H/rec['proof'],rec['proof_sha256'])
  hdr=cnf.splitlines()[0].split()
  if len(hdr)!=4 or hdr[:2]!=[b'p',b'cnf']:raise ValueError('formula header')
  steps=fifo.parse_ascii(proof,int(hdr[2]));binary=fifo.encode(steps)
  if fifo.decode(binary)!=steps:raise ValueError('proof conversion mismatch')
  result=fifo.run(f'q1batch-p{i:02d}',cnf,binary,cnf,binary)
  path=H/('frontier-20261028-q2-measured-'+f'q1batch-p{i:02d}'+'-v3-receipt.json')
  rows.append({'species':i,'formula_sha256':sha(cnf),'ascii_proof_sha256':sha(proof),
               'binary_proof_sha256':sha(binary),'binary_bytes':len(binary),'ascii_steps':len(steps),
               'strict_pass':result['strict_pass'],'transport_exact':result['transport_exact'],
               'checker_status':result['status_lines'],'checker_returncode':result['returncode'],
               'checker_reported_proof_bytes':result['checker_reported_proof_bytes'],
               'case_receipt':path.name,'case_receipt_sha256':sha(path.read_bytes())})
  if not result['strict_pass']:break
 out={'result':'ALL_39_OWNER_MEASURED_FIFO_PASS' if len(rows)==39 and all(x['strict_pass'] for x in rows) else 'PARTIAL_OR_FAILED',
      'source_sha256':sha(pathlib.Path(__file__).read_bytes()),'fifo_module_sha256':FS,'input_manifest_sha256':MS,
      'start':start,'end':datetime.datetime.now().astimezone().isoformat(),
      'controls':{k:{'returncode':v['returncode'],'status_lines':v['status_lines'],'transport_exact':v['transport_exact'],'strict_pass':v['strict_pass']} for k,v in ctl.items()},
      'completed':len(rows),'cases':rows,'limits':'Owner-local measured native checking only; parent replay, mathematical/encoding/driver review and Hcat remain separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))
if __name__=='__main__':main()
