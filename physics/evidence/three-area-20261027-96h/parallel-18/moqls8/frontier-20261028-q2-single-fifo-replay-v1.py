#!/usr/bin/env python3
"""One pinned q2 proof, source-bound conversion and measured owner-local replay."""
import argparse,hashlib,importlib.util,json,pathlib,re,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-nonmax-proof-batch-v1.py';PIN='b6dcc9cea6d1b9ce5ce963545ba237433a18d44a45a9fba3304c2bb2355aea75'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('runner pin')
spec=importlib.util.spec_from_file_location('runner',H/FILE);run=importlib.util.module_from_spec(spec);spec.loader.exec_module(run)
def main():
 p=argparse.ArgumentParser();p.add_argument('--cnf',required=True);p.add_argument('--cnf-sha',required=True);p.add_argument('--proof',required=True);p.add_argument('--proof-sha',required=True);p.add_argument('--label',required=True);p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 if not re.fullmatch(r'[a-z0-9-]{1,32}',a.label):raise ValueError('unsafe label')
 for name in (a.cnf,a.proof,a.output):
  if pathlib.Path(name).name!=name or not name.startswith('frontier-20261028-'):raise ValueError('output/input root')
 C=run.pin(H/a.cnf,a.cnf_sha);P=run.pin(H/a.proof,a.proof_sha);h=C.splitlines()[0].split()
 if len(h)!=4 or h[:2]!=[b'p',b'cnf']:raise ValueError('formula header')
 fifo=run.mods['fifo'];steps=fifo.parse_ascii(P,int(h[2]));binary=fifo.encode(steps)
 if fifo.decode(binary)!=steps:raise ValueError('proof conversion')
 controls=run.controls(a.label);actual=fifo.run(a.label+'-actual',C,binary,C,binary)
 after={'cnf_sha256':hashlib.sha256((H/a.cnf).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((H/a.proof).read_bytes()).hexdigest()}
 if after!={'cnf_sha256':a.cnf_sha,'proof_sha256':a.proof_sha}:raise ValueError('post input hash')
 out={'result':'OWNER_LOCAL_MEASURED_FIFO_PASS' if actual['strict_pass'] else 'OWNER_LOCAL_MEASURED_FIFO_NOT_PASS',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'runner_sha256':PIN,
      'cnf_file':a.cnf,'cnf_sha256':a.cnf_sha,'proof_file':a.proof,'ascii_proof_sha256':a.proof_sha,
      'ascii_steps':len(steps),'binary_sha256':hashlib.sha256(binary).hexdigest(),'binary_bytes':len(binary),
      'ascii_binary_roundtrip':'PASS','controls':controls,'actual':actual,'after_hashes':after,
      'elapsed_seconds':time.monotonic()-start,'limits':'Owner-local replay only; no independently owned parent replay, physical reduction/encoder audit, or source classification.'}
 with (H/a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('controls','actual')},indent=2));print('actual',actual['returncode'],actual['status_lines'],actual['transport_exact'],actual['checker_reported_proof_bytes'])
if __name__=='__main__':main()
