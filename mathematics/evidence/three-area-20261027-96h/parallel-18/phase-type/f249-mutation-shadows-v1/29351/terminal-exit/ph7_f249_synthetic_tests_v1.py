#!/usr/bin/env python3
"""Synthetic f249 controls only: no GLOBAL scientific obligation is run."""
import ast
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import signal
import subprocess
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

OWNER=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type')
ROOT=Path(os.environ.get('PH7_F249_TEST_MODULE_ROOT',str(OWNER))).resolve()
if ROOT!=OWNER and OWNER not in ROOT.parents:raise RuntimeError('synthetic root outside owner')
sys.dont_write_bytecode=True
sys.path.insert(0,str(OWNER/'frontier-20261028-localdeps'))
import sympy as S

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
launch=load('f249_launcher','ph7_isolated_launcher_v1.py')
consume=load('f249_consumer','ph7_terminal_consumer_v1.py')
ob=load('f249_obligations','ph7_global_obligations_v2.py')
rt=load('f249_runtime','ph7_gate_runtime_v1.py')
_idx=0

def fixture(name):
    global _idx;_idx+=1
    p=OWNER/'f249-synthetic-fixtures-v1'/f'{os.getpid()}-{_idx}-{name}'
    p.mkdir(parents=True,exist_ok=False);return p

def put(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as f:f.write(data)

def sha(b):return hashlib.sha256(b).hexdigest()
def enc(obj):return json.dumps(obj,sort_keys=True,separators=(',',':')).encode()

class ParentAuthorityTests(unittest.TestCase):
    def policy(self):
        go={'kind':'PH7_GLOBAL_EXECUTABLE_GO_V1','status':'AUTHORIZED','author_verifier_sha256':'b'*64}
        gb=enc(go)
        p={'schema_version':1,'kind':'PH7_PARENT_LAUNCH_POLICY_V1','status':'AUTHORIZED',
           'launcher_sha256':'a'*64,'prelude_sha256':'c'*64,'snapshot_root':'/synthetic/snapshot',
           'snapshot_manifest_path':'/synthetic/manifest','snapshot_manifest_sha256':'d'*64,
           'entry_rel':'entry.py','entry_sha256':'b'*64,'go_rel':'go.json','go_sha256':sha(gb),
           'interpreter_rel':'bin/python','interpreter_sha256':'e'*64,'expected_sys_path':['/synthetic/snapshot/lib'],
           'native_supervisor_attestation_path':'/synthetic/admission','native_supervisor_attestation_sha256':'f'*64}
        return p,gb
    def test_current_production_policy_is_deny_by_default(self):
        self.assertEqual(launch.APPROVED_PARENT_POLICY_SHA256,frozenset())
        p,_=self.policy()
        with self.assertRaisesRegex(launch.LaunchRejected,'PARENT_POLICY_NOT_ADMITTED'):
            launch.authenticate_policy(enc(p),launch.APPROVED_PARENT_POLICY_SHA256)
    def test_nonisolated_launcher_refused(self):
        if sys.flags.isolated==0:
            with self.assertRaisesRegex(launch.LaunchRejected,'ISOLATION_FLAGS'):launch.main([])
    def test_fabricated_self_hashed_go_rejected(self):
        p,gb=self.policy();pb=enc(p);trusted={sha(pb)}
        authorized,_=launch.authenticate_policy(pb,trusted)
        self.assertEqual(launch.verify_go(gb,authorized)['status'],'AUTHORIZED')
        bad=enc({'kind':'PH7_GLOBAL_EXECUTABLE_GO_V1','status':'AUTHORIZED','author_verifier_sha256':'b'*64,'forged':True})
        self.assertNotEqual(sha(bad),sha(gb))
        with self.assertRaisesRegex(launch.LaunchRejected,'GO_NOT_PARENT_APPROVED'):launch.verify_go(bad,authorized)
        forged=dict(p);forged['go_sha256']=sha(bad)
        with self.assertRaisesRegex(launch.LaunchRejected,'PARENT_POLICY_NOT_ADMITTED'):
            launch.authenticate_policy(enc(forged),trusted)
    def test_writable_snapshot_rejected(self):
        p=fixture('snapshot');files={'entry.py':b'entry','go.json':b'go','bin/python':b'python'}
        for name,data in files.items():put(p/name,data)
        m={'schema_version':1,'kind':'PH7_IMMUTABLE_SNAPSHOT_V1','files':[{'path':k,'sha256':sha(v)} for k,v in files.items()]}
        policy={'entry_rel':'entry.py','entry_sha256':sha(files['entry.py']),'go_rel':'go.json','go_sha256':sha(files['go.json']),
                'interpreter_rel':'bin/python','interpreter_sha256':sha(files['bin/python'])}
        with self.assertRaisesRegex(launch.LaunchRejected,'SNAPSHOT_NOT_READONLY'):
            launch.verify_snapshot(p,m,policy,mount_check=lambda _:False)
        self.assertEqual(len(launch.verify_snapshot(p,m,policy,mount_check=lambda _:True)),3)
    def test_unlisted_snapshot_file_rejected(self):
        p=fixture('unlisted');files={'entry.py':b'entry','go.json':b'go','bin/python':b'python'}
        for name,data in files.items():put(p/name,data)
        m={'schema_version':1,'kind':'PH7_IMMUTABLE_SNAPSHOT_V1','files':[{'path':k,'sha256':sha(v)} for k,v in files.items()]}
        policy={'entry_rel':'entry.py','entry_sha256':sha(files['entry.py']),'go_rel':'go.json','go_sha256':sha(files['go.json']),
                'interpreter_rel':'bin/python','interpreter_sha256':sha(files['bin/python'])}
        put(p/'unlisted.py',b'bad')
        with self.assertRaisesRegex(launch.LaunchRejected,'SNAPSHOT_UNLISTED_FILE'):
            launch.verify_snapshot(p,m,policy,mount_check=lambda _:True)
    def test_verified_entry_uses_loaded_bytes_not_later_path(self):
        p=fixture('entry-swap')/'entry.py';good=b"print('APPROVED_BYTES')\n";bad=b"print('REPLACED_BYTES')\n"
        put(p,bad);out=io.StringIO()
        with contextlib.redirect_stdout(out):launch.exec_verified_entry(good,sha(good),p,{})
        self.assertEqual(out.getvalue(),'APPROVED_BYTES\n')
        with self.assertRaisesRegex(launch.LaunchRejected,'ENTRY_BYTES_MISMATCH'):
            launch.exec_verified_entry(bad,sha(good),p,{})
    def test_direct_v2_entry_requires_isolated_launch(self):
        p=ROOT/'frontier-20261029-ph7-global-verifier-v2.py'
        r=subprocess.run([sys.executable,'-I','-S',str(p),'--go','/not-a-go','--go-sha256','0'*64],capture_output=True,text=True,timeout=15)
        self.assertEqual(r.returncode,2,r.stdout+r.stderr);self.assertIn('ISOLATED_LAUNCH_REQUIRED',r.stderr)
    def test_isolated_python_ignores_ambient_module_and_sitecustomize(self):
        p=fixture('ambient');mark=p/'contaminated'
        put(p/'sitecustomize.py',f"open({str(mark)!r},'w').write('site')\n".encode())
        put(p/'hashlib.py',f"open({str(mark)!r},'w').write('hashlib')\n".encode())
        code="import sys,hashlib; print(sys.flags.isolated,sys.flags.no_site); print(hashlib.__file__); print('sitecustomize' in sys.modules)"
        r=subprocess.run([sys.executable,'-I','-S','-c',code],env={**os.environ,'PYTHONPATH':str(p),'PYTHONUSERBASE':str(p)},capture_output=True,text=True,timeout=15)
        self.assertEqual(r.returncode,0,r.stderr);self.assertIn('1 1',r.stdout);self.assertTrue(r.stdout.strip().endswith('False'))
        self.assertNotIn(str(p),r.stdout);self.assertFalse(mark.exists())
    def test_prelude_executes_pinned_launcher_and_denies_unapproved_policy(self):
        pre=(ROOT/'ph7_isolated_prelude_v1.py').read_bytes();lb=(ROOT/'ph7_isolated_launcher_v1.py').read_bytes()
        r=subprocess.run([sys.executable,'-I','-S','-c',pre.decode(),str(ROOT/'ph7_isolated_launcher_v1.py'),sha(lb),sha(pre),'--policy','/not-a-policy'],capture_output=True,text=True,timeout=15)
        self.assertEqual(r.returncode,2,r.stdout+r.stderr);self.assertIn('NO_PARENT_POLICY_ANCHOR',r.stderr)
    def test_prelude_rejects_wrong_launcher_pin(self):
        pre=(ROOT/'ph7_isolated_prelude_v1.py').read_bytes()
        r=subprocess.run([sys.executable,'-I','-S','-c',pre.decode(),str(ROOT/'ph7_isolated_launcher_v1.py'),'0'*64,sha(pre),'--policy','/not-a-policy'],capture_output=True,text=True,timeout=15)
        self.assertNotEqual(r.returncode,0)
        self.assertIn('PRELUDE_LAUNCHER_BYTES_MISMATCH',r.stderr)

class PathAndExactnessTests(unittest.TestCase):
    def test_duplicate_leaf_separately_rejected(self):
        leaves=[{'path':'','label':'pos'},{'path':'','label':'pos'}]
        with self.assertRaisesRegex(ob.ProofError,'DUPLICATE_OR_PREFIX_PATH'):ob.parse_cover(leaves,1,{'pos'})
    def test_prefix_conflict_separately_rejected(self):
        leaves=[{'path':'0','label':'pos'},{'path':'00','label':'pos'},{'path':'1','label':'pos'}]
        with self.assertRaisesRegex(ob.ProofError,'PATH_PREFIX_CONFLICT'):ob.parse_cover(leaves,1,{'pos'})
    def test_malformed_leaf_path_type_and_alphabet(self):
        for path in (None,True,17,[], '012','0x'):
            with self.subTest(path=path):
                with self.assertRaisesRegex(ob.ProofError,'PATH_SYNTAX'):ob.parse_cover([{'path':path,'label':'pos'}],1,{'pos'})
    def test_malformed_leaf_label_is_named_error(self):
        with self.assertRaisesRegex(ob.ProofError,'UNKNOWN_LEAF_LABEL'):ob.parse_cover([{'path':'','label':[]}],1,{'pos'})
    def test_float_tensor_never_becomes_verdict(self):
        with self.assertRaisesRegex(ob.ProofError,'NONINTEGER_TENSOR_COEFFICIENT'):ob.Tensor([0.1],(1,),1)
        with self.assertRaisesRegex(ob.ProofError,'NONINTEGER_TENSOR_COEFFICIENT'):ob.Tensor([True],(1,),1)
    def test_float_polynomial_never_becomes_verdict(self):
        x=S.symbols('toy_x')
        with self.assertRaisesRegex(ob.ProofError,'FLOAT_POLYNOMIAL_FORBIDDEN'):
            ob.tensor_from_expr(S,x+S.Float('0.1'),[x],[(Q(0),Q(1))],[False],[1],lambda:None)
    def test_float_bound_never_becomes_exact_rational(self):
        for value in (0.1,S.Float('0.1'),True):
            with self.assertRaisesRegex(ob.ProofError,'NONEXACT_RATIONAL'):ob._r(value)

class TerminalConsumerTests(unittest.TestCase):
    def payload(self):
        h=lambda c:c*64
        counts={k:{'pos':1} for k in consume.COVERS}
        result={'status':'AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED','scope_sha256':h('a'),'repair_sha256':h('b'),
                'face_sha256':h('c'),'bundle_sha256':h('d'),'go_sha256':h('e'),'counts':counts}
        rb=enc(result)
        receipt={'pid':1234,'status':'AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED','go_sha256':h('e'),
                 'candidate_sha256':h('a'),'repair_sha256':h('b'),'face_sha256':h('c'),'bundle_sha256':h('d'),
                 'author_verifier_sha256':h('f'),'result_name':'candidate-result.json','result_sha256':sha(rb),'counts':counts}
        cb=enc(receipt)
        sup={'kind':'PH7_PARENT_TERMINAL_OBSERVATION_V1','terminal_observed':True,'exit_code':0,'pid':1234,
             'go_sha256':h('e'),'entry_sha256':h('f'),'receipt_sha256':sha(cb),'result_sha256':sha(rb)}
        sb=enc(sup)
        trusted={'go_sha256':h('e'),'candidate_sha256':h('a'),'repair_sha256':h('b'),'face_sha256':h('c'),
                 'bundle_sha256':h('d'),'entry_sha256':h('f'),'result_name':'candidate-result.json','supervisor_sha256':sha(sb)}
        return receipt,result,sup,trusted
    def test_complete_pair_is_bound_not_adopted(self):
        r,x,s,t=self.payload();out=consume.consume(enc(r),enc(x),enc(s),t)
        self.assertEqual(out['status'],'AUTHOR_COMPLETE_BOUND_NOT_ADOPTED')
    def test_orphan_result_is_unknown(self):
        r,x,s,t=self.payload();out=consume.consume(None,enc(x),enc(s),t);self.assertEqual(out['status'],'UNKNOWN')
    def test_absent_parent_observation_is_unknown(self):
        r,x,s,t=self.payload();out=consume.consume(enc(r),enc(x),None,t);self.assertEqual(out['status'],'UNKNOWN')
    def test_incomplete_receipt_is_unknown_even_when_pinned(self):
        r,x,s,t=self.payload();r['status']='INCOMPLETE';rb=enc(r);s['receipt_sha256']=sha(rb);sb=enc(s);t['supervisor_sha256']=sha(sb)
        out=consume.consume(rb,enc(x),sb,t);self.assertEqual(out['status'],'UNKNOWN');self.assertIn('RECEIPT_NOT_COMPLETE',out['reason'])
    def test_mismatched_result_or_go_is_unknown(self):
        r,x,s,t=self.payload();x['scope_sha256']='0'*64
        self.assertEqual(consume.consume(enc(r),enc(x),enc(s),t)['status'],'UNKNOWN')
        r,x,s,t=self.payload();t['go_sha256']='0'*64
        self.assertEqual(consume.consume(enc(r),enc(x),enc(s),t)['status'],'UNKNOWN')
    def test_nonzero_process_exit_is_unknown(self):
        r,x,s,t=self.payload();s['exit_code']=1;sb=enc(s);t['supervisor_sha256']=sha(sb)
        out=consume.consume(enc(r),enc(x),sb,t);self.assertEqual(out['status'],'UNKNOWN');self.assertIn('PROCESS_EXIT_NOT_ZERO',out['reason'])
    def test_fabricated_supervisor_self_hash_is_not_parent_pin(self):
        r,x,s,t=self.payload();s['pid']=999;fake=enc(s)
        self.assertNotEqual(sha(fake),t['supervisor_sha256'])
        out=consume.consume(enc(r),enc(x),fake,t);self.assertEqual(out['status'],'UNKNOWN');self.assertIn('SUPERVISOR_PIN',out['reason'])

class RealSignalTests(unittest.TestCase):
    def test_os_sigterm_yields_incomplete_receipt(self):
        p=fixture('os-signal');receipt=p/'receipt.json'
        code='''import importlib.util,json,os,sys,time\ns=importlib.util.spec_from_file_location("synthetic_rt",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)\ng=m.Guard(2,1073741824);old=m.install_latch(g);fd=m.exclusive_create(sys.argv[2]);print("READY",flush=True)\ntry:\n while True:\n  time.sleep(0.02)\n  try:g.check()\n  except m.GateError:break\n rec={"status":"LOCAL_COMPLETE_IMPORT_ROOT","reason":"synthetic","signal":None};m.settle_receipt(fd,rec,g)\nfinally:\n os.close(fd);m.restore_latch(old)\nsys.exit(1)\n'''
        child=subprocess.Popen([sys.executable,'-I','-S','-c',code,str(ROOT/'ph7_gate_runtime_v1.py'),str(receipt)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=True)
        line=child.stdout.readline().strip();self.assertEqual(line,'READY')
        os.kill(child.pid,signal.SIGTERM)
        out,err=child.communicate(timeout=5)
        self.assertEqual(child.returncode,1,err);rec=json.loads(receipt.read_text())
        self.assertEqual(rec['status'],'INCOMPLETE');self.assertEqual(rec['signal'],signal.SIGTERM)

if __name__=='__main__':unittest.main(verbosity=2)
