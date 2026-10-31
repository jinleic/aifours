#!/usr/bin/env python3
"""Synthetic-only checks of gate, lifecycle, Bernstein and safety predicates.

No test constructs the PH7 global polynomials or calls GlobalVerifier on the
seven scientific obligations. All files are created under the owner root.
"""
import ast
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

OWNER=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type')
ROOT=Path(os.environ.get('PH7_TEST_MODULE_ROOT',str(OWNER))).resolve()
if ROOT != OWNER and OWNER not in ROOT.parents: raise RuntimeError('synthetic root outside owner')
sys.dont_write_bytecode=True
sys.path.insert(0,str(OWNER/'frontier-20261028-localdeps'))
import sympy as S

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
rt=load('test_runtime','ph7_gate_runtime_v1.py')
env=load('test_environment','ph7_environment_guard_v1.py')
gate=load('test_gate','ph7_global_gate_v1.py')
src=load('test_source','ph7_source_binding_v1.py')
ob=load('test_obligations','ph7_global_obligations_v1.py')
loc=load('test_local','frontier-20261029-ph7-local-hardened-v2.py')

_fixture_index=0
def fixture(name):
    global _fixture_index
    _fixture_index+=1
    p=OWNER/'hardening-synthetic-fixtures-v1'/f'{os.getpid()}-{_fixture_index}-{name}'
    p.mkdir(parents=True,exist_ok=False);return p

def wb(path,data):
    with path.open('xb') as f:f.write(data)

def no_guard(): pass

class RuntimeSafetyTests(unittest.TestCase):
    def test_duplicate_json_rejected(self):
        with self.assertRaisesRegex(rt.GateError,'DUPLICATE_JSON_KEY'):rt.strict_json(b'{"x":1,"x":2}')
    def test_nonfinite_json_rejected(self):
        with self.assertRaisesRegex(rt.GateError,'NONFINITE_JSON'):rt.strict_json(b'{"x":NaN}')
    def test_bad_hash_and_missing_rejected(self):
        p=fixture('pin')/'data';wb(p,b'actual')
        with self.assertRaisesRegex(rt.GateError,'INPUT_SHA_MISMATCH'):rt.read_pinned(p,hashlib.sha256(b'old').hexdigest(),32)
        with self.assertRaisesRegex(rt.GateError,'INPUT_OPEN_FAILED'):rt.read_pinned(p.with_name('absent'),'0'*64,32)
    def test_oversized_rejected(self):
        p=fixture('size')/'data';wb(p,b'12345')
        with self.assertRaisesRegex(rt.GateError,'INPUT_TOO_LARGE'):rt.read_pinned(p,'0'*64,4)
    def test_existing_output_never_opened(self):
        p=fixture('exclusive')/'output';wb(p,b'preserve')
        with self.assertRaisesRegex(rt.GateError,'OUTPUT_CLAIM_FAILED'):rt.exclusive_create(p)
        self.assertEqual(p.read_bytes(),b'preserve')
    def test_signal_is_sticky_and_checked(self):
        g=rt.Guard(5,100,clock=lambda:0,rss=lambda:1);g.signal_handler(15,None)
        with self.assertRaisesRegex(rt.GateError,'COOPERATIVE_SIGNAL_STOP'):g.check()
    def test_deadline_fail_closed(self):
        ticks=iter((0,5));g=rt.Guard(5,100,clock=lambda:next(ticks),rss=lambda:1)
        with self.assertRaisesRegex(rt.GateError,'COOPERATIVE_DEADLINE'):g.check()
    def test_rss_fail_closed(self):
        g=rt.Guard(5,100,clock=lambda:0,rss=lambda:101)
        with self.assertRaisesRegex(rt.GateError,'COOPERATIVE_RSS_STOP'):g.check()
    def test_optimized_mode_assertions_are_active(self):
        tree=loc.transform(b'assert False, "synthetic"\n',top_level=False)
        def check(value,code,detail):rt.require(value,code,str(detail))
        with self.assertRaisesRegex(rt.GateError,'SCIENTIFIC_ASSERT_LINE_1'):
            exec(compile(tree,'synthetic','exec',optimize=2),{'active_check':check,'guard_check':no_guard})
    def test_local_engine_bytes_must_be_pinned(self):
        guard=rt.Guard(5,100,clock=lambda:0,rss=lambda:1)
        with self.assertRaisesRegex(rt.GateError,'ENGINE_BYTES_NOT_PINNED'):
            loc.invoke_transformed(b'',b'wrong engine',guard,{'require':rt.require},OWNER/'fake-local-source')
    def test_inside_root_guard(self):
        p=fixture('within')
        with self.assertRaisesRegex(rt.GateError,'PATH_OUTSIDE_ROOT'):rt.within(p,OWNER/'outside-synthetic')
    def test_local_pin_failure_writes_incomplete_receipt(self):
        p=fixture('local-incomplete')
        wb(p/'ph7_gate_runtime_v1.py',(ROOT/'ph7_gate_runtime_v1.py').read_bytes())
        wb(p/'local.py',(ROOT/'frontier-20261029-ph7-local-hardened-v2.py').read_bytes())
        wb(p/'frontier-20261029-ph7-local-global-dual-check.py',b'not the pinned source')
        child=subprocess.run([sys.executable,'-O',str(p/'local.py'),'--run-id','synthetic-failure',
                              '--seconds','10','--rss-bytes','1073741824'],
                             env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True,timeout=20)
        self.assertEqual(child.returncode,1,child.stdout+child.stderr)
        receipt=json.loads((p/'local-hardened-synthetic-failure-receipt.json').read_text())
        self.assertEqual(receipt['status'],'INCOMPLETE')
        self.assertIn('INPUT_SHA_MISMATCH',receipt['reason'])
        self.assertFalse((p/'local-hardened-synthetic-failure-result.json').exists())

class EnvironmentSafetyTests(unittest.TestCase):
    def make_fixture(self):
        p=fixture('env')
        for pkg in ['mpmath','sympy']:
            (p/pkg).mkdir();wb(p/pkg/'__init__.py',pkg.encode())
        files=[{'path':pkg+'/__init__.py','sha256':hashlib.sha256(pkg.encode()).hexdigest()} for pkg in ['mpmath','sympy']]
        return p,{'schema_version':1,'kind':'PH7_PYTHON_PACKAGE_INVENTORY_V1','packages':['mpmath','sympy'],'files':files}
    def test_good_inventory(self):
        p,m=self.make_fixture();self.assertTrue(env.verify_manifest(p,m,rt.read_pinned,no_guard)['files_verified'])
    def test_missing_inventoried_file(self):
        p,m=self.make_fixture();m['files'].append({'path':'sympy/absent.py','sha256':'0'*64})
        with self.assertRaisesRegex(env.EnvironmentErrorGate,'ENV_INVENTORY_MISSING'):env.verify_manifest(p,m,rt.read_pinned,no_guard)
    def test_unlisted_file_fails_for_correct_reason(self):
        p,m=self.make_fixture();wb(p/'sympy'/'unlisted.py',b'x')
        with self.assertRaisesRegex(env.EnvironmentErrorGate,'ENV_UNLISTED_FILE'):env.verify_manifest(p,m,rt.read_pinned,no_guard)
    def test_changed_file_rejected(self):
        p,m=self.make_fixture();m['files'][0]['sha256']='0'*64
        with self.assertRaisesRegex(rt.GateError,'INPUT_SHA_MISMATCH'):env.verify_manifest(p,m,rt.read_pinned,no_guard)
    def test_duplicate_manifest_rejected(self):
        p,m=self.make_fixture();m['files'].append(dict(m['files'][0]))
        with self.assertRaisesRegex(env.EnvironmentErrorGate,'ENV_DUPLICATE_PATH'):env.verify_manifest(p,m,rt.read_pinned,no_guard)
    def test_symlink_rejected(self):
        p,m=self.make_fixture();os.symlink(p/'mpmath'/'__init__.py',p/'sympy'/'link.py')
        with self.assertRaisesRegex(env.EnvironmentErrorGate,'ENV_NONREGULAR_OR_SYMLINK'):env.verify_manifest(p,m,rt.read_pinned,no_guard)

class SourceOrderTests(unittest.TestCase):
    def test_mandatory_overlay_order(self):
        p=fixture('source');a=p/'erratum';b=p/'body';wb(a,b'overlay');wb(b,b'body')
        pairs=[('overlay',a,hashlib.sha256(b'overlay').hexdigest()),('body',b,hashlib.sha256(b'body').hexdigest())]
        records=[{'role':role,'path':str(path),'sha256':sha} for role,path,sha in pairs]
        m={'schema_version':1,'kind':'PH7_ORDERED_SOURCE_MANIFEST_V1','sources':records}
        self.assertEqual(src.verify_manifest(m,pairs,rt.read_pinned,no_guard)['body'],b'body')
        m['sources'].reverse()
        with self.assertRaisesRegex(src.SourceBindingError,'SOURCE_ORDER_OR_PIN_MISMATCH'):src.verify_manifest(m,pairs,rt.read_pinned,no_guard)

class AdmissionTests(unittest.TestCase):
    def base(self):
        h=lambda c:c*64
        exp={'candidate_sha256':h('a'),'repair_sha256':h('b'),'author_verifier_sha256':h('c'),
             'runtime_sha256':h('d'),'obligation_engine_sha256':h('e'),'environment_guard_sha256':h('f'),
             'source_binding_sha256':h('1'),'gate_validator_sha256':h('2'),'local_hardened_sha256':h('3')}
        invocation={'program':'verifier.py','go_path':'/tmp/parent-go.json','arguments':'--go PATH --go-sha256 SHA256'}
        g={'schema_version':1,'kind':'PH7_GLOBAL_EXECUTABLE_GO_V1','status':'AUTHORIZED','run_id':'synthetic',
           **{k:v for k,v in exp.items() if k!='repair_sha256'},
           'bundle_path':'/synthetic/bundle','bundle_sha256':h('4'),
           'environment_manifest_path':'/synthetic/env','environment_manifest_sha256':h('5'),
           'source_manifest_path':'/synthetic/source','source_manifest_sha256':h('6'),'python_executable_sha256':h('7'),
           'seconds':10,'rss_bytes':10000,'output_bytes':10000,'invocation':invocation,
           'reviews':{'f202':{'verdict':'NO_MAJOR','review_sha256':h('8'),'scope_sha256':h('a')},
                      'f203':{'verdict':'THREE_MAJORS_RETAINED','review_sha256':h('9'),'scope_sha256':h('a')},
                      'f223':{'verdict':'M2_M3_REPAIR_SUPPORTED','review_sha256':h('0'),'scope_sha256':h('b')}},
           'independent_checker':{'status':'READY','code_sha256':h('4'),'definition_first':True},
           'hardening_review':{'verdict':'NO_MAJOR','report_sha256':h('5'),'verifier_sha256':h('c')},
           'prior_art_scope':{'status':'PARENT_AUTHORIZED','scope_sha256':h('6')},
           'settlement':{'timeout':'INTERNAL_COOPERATIVE','tool_timeout_seconds':0,'auto_retry':False,'on_failure':'INCOMPLETE'},
           'obligations':['QO','HO','NB','MC','R3','SB','MP']}
        return g,exp,invocation
    def test_synthetic_go_shape(self):
        g,e,i=self.base();self.assertIs(gate.validate(g,e,i),g)
    def test_no_go_cannot_admit(self):
        g,e,i=self.base();g['status']='NO_GO'
        with self.assertRaisesRegex(gate.AdmissionError,'GO_NOT_AUTHORIZED'):gate.validate(g,e,i)
    def test_historical_majors_not_erased(self):
        g,e,i=self.base();g['reviews']['f203']['verdict']='NO_MAJOR'
        with self.assertRaisesRegex(gate.AdmissionError,'GO_REVIEW_NOT_CLEARED'):gate.validate(g,e,i)
    def test_repair_review_required(self):
        g,e,i=self.base();g['reviews']['f223']['scope_sha256']='0'*64
        with self.assertRaisesRegex(gate.AdmissionError,'GO_REVIEW_NOT_CLEARED'):gate.validate(g,e,i)
    def test_independent_must_be_distinct(self):
        g,e,i=self.base();g['independent_checker']['code_sha256']=e['author_verifier_sha256']
        with self.assertRaisesRegex(gate.AdmissionError,'GO_CHECKER_NOT_DISTINCT'):gate.validate(g,e,i)
    def test_hardening_review_required(self):
        g,e,i=self.base();g['hardening_review']['verdict']='PENDING'
        with self.assertRaisesRegex(gate.AdmissionError,'GO_HARDENING_NOT_CLEARED'):gate.validate(g,e,i)
    def test_missing_obligation_rejected(self):
        g,e,i=self.base();g['obligations'].pop()
        with self.assertRaisesRegex(gate.AdmissionError,'GO_OBLIGATION_SET'):gate.validate(g,e,i)
    def test_wrong_candidate_pin_rejected(self):
        g,e,i=self.base();g['candidate_sha256']='0'*64
        with self.assertRaisesRegex(gate.AdmissionError,'GO_CODE_OR_SCOPE_PIN'):gate.validate(g,e,i)
    def test_invalid_resource_bounds_rejected(self):
        g,e,i=self.base();g['rss_bytes']=0
        with self.assertRaisesRegex(gate.AdmissionError,'GO_RSS_BOUND'):gate.validate(g,e,i)
    def test_boolean_schema_is_not_version_one(self):
        g,e,i=self.base();g['schema_version']=True
        with self.assertRaisesRegex(gate.AdmissionError,'GO_NOT_AUTHORIZED'):gate.validate(g,e,i)
    def test_settlement_cannot_autoretry(self):
        g,e,i=self.base();g['settlement']['auto_retry']=True
        with self.assertRaisesRegex(gate.AdmissionError,'GO_SETTLEMENT'):gate.validate(g,e,i)

class BernsteinAndCoverageTests(unittest.TestCase):
    def test_affine_uniform_parameter_basis(self):
        x,z=S.symbols('tx tz')
        t=ob.tensor_from_expr(S,x+z,[x,z],[(0,1),(1,2)],[False,False],[1,1],no_guard)
        self.assertEqual([Q(n,t.scale) for n in t.values],[Q(1),Q(2),Q(2),Q(3)])
        l,r=t.split(0,no_guard)
        self.assertEqual([Q(n,l.scale) for n in l.values],[Q(1),Q(2),Q(3,2),Q(5,2)])
        self.assertEqual([Q(n,r.scale) for n in r.values],[Q(3,2),Q(5,2),Q(2),Q(3)])
    def test_compactification_exact(self):
        x=S.symbols('tx');t=ob.tensor_from_expr(S,x,[x],[(0,1)],[True],[1],no_guard)
        self.assertEqual([Q(n,t.scale) for n in t.values],[Q(0),Q(1)])
    def test_coverage_requires_both_children(self):
        with self.assertRaisesRegex(ob.ProofError,'INCOMPLETE_PATH_COVER'):
            ob.parse_cover([{'path':'0','label':'pos'}],1,{'pos'})
    def test_duplicate_and_prefix_paths_rejected(self):
        for leaves in ([{'path':'0','label':'pos'},{'path':'0','label':'pos'}],
                       [{'path':'','label':'pos'},{'path':'0','label':'pos'}]):
            with self.assertRaises(ob.ProofError):ob.parse_cover(leaves,1,{'pos'})
    def test_synthetic_tree_checks_both_branches(self):
        x,z=S.symbols('toy_x toy_z')
        v=ob.GlobalVerifier.__new__(ob.GlobalVerifier);v.S=S;v.guard=no_guard
        v.defs={'polynomials':{'resA':x-2,'resF':S.Integer(-1)}}
        v._spec=lambda kind:([x,z],[(Q(0),Q(1)),(Q(0),Q(1))],[False,False],1)
        leaves=[{'path':'0','label':'f1-4<0'},{'path':'1','label':'Abar<=0'}]
        self.assertEqual(v.verify_cover('R3',leaves),{'f1-4<0':1,'Abar<=0':1})
        v.defs={'polynomials':{'resA':x,'resF':S.Integer(-1)}}
        with self.assertRaisesRegex(ob.ProofError,'RESIDUAL_SIGN'):v.verify_cover('R3',leaves)
    def test_internal_admissible_face_must_be_positive(self):
        shape=(2,2,2,2,2,2,1)
        vals=[0 if ix[0]==0 else 1 for ix in __import__('itertools').product(*(range(k) for k in shape))]
        t=ob.Tensor(vals,shape,1);bounds=((Q(1,2),Q(1)),)*6
        self.assertFalse(ob._corner_positive(t,bounds,6))
    def test_irrelevant_outer_face_can_vanish(self):
        shape=(2,2,2,2,2,2,1)
        vals=[0 if ix[0]==0 else 1 for ix in __import__('itertools').product(*(range(k) for k in shape))]
        t=ob.Tensor(vals,shape,1);bounds=((Q(0),Q(1,2)),)*6
        self.assertTrue(t.nonnegative())
        self.assertTrue(ob._corner_positive(t,bounds,6))
    def test_nonstrict_residual_accepts_zero_face(self):
        t=ob.Tensor([0,-1],(2,),1)
        self.assertTrue(t.nonpositive())
        self.assertFalse(t.negative())
    def test_sorted_interval_equality_not_discarded(self):
        self.assertFalse(ob.unsorted(((Q(1),Q(4)),(Q(0),Q(3)))))
        self.assertFalse(ob.unsorted(((Q(3),Q(5)),(Q(0),Q(3)))))
        self.assertTrue(ob.unsorted(((Q(4),Q(5)),(Q(0),Q(3)))))
    def test_adaptive_anchor_uses_exact_floor(self):
        tensor=lambda x:ob.Tensor([x],(1,),1)
        v=ob.GlobalVerifier.__new__(ob.GlobalVerifier)
        # Lq=1-2^-55, so exact floor(1024 Lq)=1023. The rounded-up
        # binary64 value 1 is prohibited by the anchor interval check.
        den=2**55;ma=tensor(den-1);fm=tensor(den)
        tensors={'mA':ma,'Fm':fm,'g0':tensor(1),'c0':tensor(0),'c1':tensor(-1),'c2':tensor(0),'c3':tensor(-1)}
        v._adaptive(tensors,((Q(0),Q(1)),)*6)
    def test_parameter_corner_zero_is_rejected(self):
        shape=(2,2,2,2,2,2,2)
        vals=[0 if ix[-1]==1 else 1 for ix in __import__('itertools').product(*(range(k) for k in shape))]
        t=ob.Tensor(vals,shape,1);self.assertFalse(ob._corner_positive(t,((Q(1,2),Q(1)),)*6,6))
    def test_missing_bundle_cover_rejected_without_science(self):
        v=ob.GlobalVerifier.__new__(ob.GlobalVerifier)
        v.verify_cover=lambda name,leaves:{'synthetic':len(leaves)}
        base={'schema_version':1,'kind':'PH7_GLOBAL_COVERS_V1',
              'candidate_sha256':'b2b7770d8b024782c5d0c1cfbd8f6e01368892801d1f3882e7b3279b59059ca5',
              'covers':{name:[] for name in ob.OBLIGATIONS}}
        self.assertEqual(len(v.verify_bundle(base)),7)
        del base['covers']['MP']
        with self.assertRaisesRegex(ob.ProofError,'OBLIGATION_SET_MISMATCH'):v.verify_bundle(base)
    def test_common_basis_mismatch_rejected(self):
        a=ob.Tensor([1],(1,),1);b=ob.Tensor([1,1],(2,),1)
        with self.assertRaisesRegex(ob.ProofError,'COMMON_BASIS_MISMATCH'):ob._combination([a,b],[Q(1),Q(1)],'positive')
    def test_scientific_modules_have_no_assert_statements(self):
        for name in ['ph7_global_obligations_v1.py','ph7_gate_runtime_v1.py','ph7_global_gate_v1.py']:
            tree=ast.parse((ROOT/name).read_text())
            self.assertFalse(any(isinstance(n,ast.Assert) for n in ast.walk(tree)),name)

if __name__=='__main__':unittest.main(verbosity=2)
