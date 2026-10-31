#!/usr/bin/env python3
"""Bounded one-worker replay of pinned public d=4 verifier plus separate PSD audit.

This runs the author's ep3core and verify_perd code from the pinned archive,
NOT independent proof of their global map. Pickle globals are forbidden. The
only AST instrumentation saves final exact rational multipliers and runs our
separate Fraction-Schur PSD routine before returning. All data stay in OWN.
"""
import ast
import hashlib
import importlib.util
import io
import json
import lzma
import sys
import tarfile
import time
import types
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / 'frontier-20261028-tomar-release-ep3-v3.tar.gz'
BASE = ROOT / 'frontier-20261028-independent-d4-base-check.py'
RESULT = ROOT / 'frontier-20261028-d4-author-replay-and-independent-psd-results.json'
CORRECTED = ROOT / 'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
EXPECTED = {
    'archive':'2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3',
    'certificate':'0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f',
    'ep3core':'0f0d84a9ce257edbf9b0b6cbbff2690041fbd6aad18d139c8845e8edf547d450',
    'verify_perd':'98311b321bad13d2c2ea7d4b5469cc7c3ca519b96da17f78d74118297e7e1d62',
}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    start=time.monotonic()
    archive=ARCHIVE.read_bytes()
    if sha(archive)!=EXPECTED['archive']:
        raise ValueError('archive hash mismatch')
    spec=importlib.util.spec_from_file_location('frontier_base',BASE)
    base=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    with tarfile.open(fileobj=io.BytesIO(archive),mode='r:gz') as tf:
        files={k:tf.extractfile(path).read() for k,path in {
            'certificate':'release_ep3/certs/ep3_perd_d4.pkl.xz',
            'ep3core':'release_ep3/ep3core.py',
            'verify_perd':'release_ep3/verify_perd.py'}.items()}
    for key,raw in files.items():
        if sha(raw)!=EXPECTED[key]:
            raise ValueError(f'{key} hash mismatch')
    pkg=base.DataOnlyUnpickler(io.BytesIO(lzma.decompress(files['certificate'],memlimit=256*1024*1024))).load()
    if (pkg['k'],pkg['d'],pkg['nrow'])!=(3,4,4675):
        raise ValueError('wrong target package')
    errors,_,_=base.structural_checks(pkg)
    if errors:
        raise ValueError('independent input structure check failed: '+str(errors[:3]))

    # The public modules were statically read: no top-level calls in ep3core;
    # verify_perd only inserts a local path and adjusts int string digit limit.
    core=types.ModuleType('ep3core')
    core.__file__='archive:release_ep3/ep3core.py'
    exec(compile(files['ep3core'],core.__file__,'exec'),core.__dict__)
    sys.modules['ep3core']=core

    def capture(pkg,Zs,lam,acc,nz,psd,D,correction):
        print('CAPTURE: independently checking exact corrected PSD',flush=True)
        t0=time.monotonic()
        failed=[]
        disagreements=[]
        matrices=[]
        for i,Z in enumerate(Zs):
            n=len(Z)
            flat=[Fraction(v) for row in Z for v in row]
            symmetric=all(flat[a*n+b]==flat[b*n+a] for a in range(n) for b in range(n))
            good=symmetric and base.exact_schur_psd(flat,n)
            if not good:
                failed.append(i)
            if bool(psd[i])!=good:
                disagreements.append(i)
            matrices.append({'r':n,'values':[[str(x.numerator),str(x.denominator)] for x in flat]})
        equalities=[]
        for name,items in sorted(lam.items()):
            for index,value in sorted(items.items()):
                v=Fraction(value)
                equalities.append({'group':name,'index':list(index),
                                   'numerator':str(v.numerator),'denominator':str(v.denominator)})
        exact={'kind':'exact_corrected_d4_multipliers_and_equality_coefficients',
               'source_archive_sha256':EXPECTED['archive'],'source_member_sha256':EXPECTED['certificate'],
               'dimension':D,'copies':3,'matrices':matrices,'equality_coefficients':equalities}
        with lzma.open(CORRECTED,'wt',encoding='utf-8',preset=3) as f:
            json.dump(exact,f,separators=(',',':'),sort_keys=True)
            f.write('\n')
        raw=CORRECTED.read_bytes()
        result={'kind':'author_d4_exact_verifier_replay_with_independent_final_psd',
                'archive_sha256':EXPECTED['archive'],'certificate_member_sha256':EXPECTED['certificate'],
                'author_ep3core_sha256':EXPECTED['ep3core'],'author_verify_perd_sha256':EXPECTED['verify_perd'],
                'dimension':D,'copies':3,'author_reported_orbit_rows':pkg['nrow'],
                'author_recomputed_nonzero_orbit_residuals':nz,
                'author_psd_fail_count':sum(not x for x in psd),
                'independent_fraction_schur_psd_fail_indices':failed,
                'independent_vs_author_psd_disagreements':disagreements,
                'final_multiplier_count':len(Zs),'equality_coefficient_count':len(equalities),
                'correction_coordinate_count':len(correction),
                'max_correction_denominator_bits':max(v.denominator.bit_length() for v in correction),
                'corrected_data_path':CORRECTED.name,'corrected_data_sha256':sha(raw),
                'corrected_data_bytes':len(raw),'independent_psd_seconds':round(time.monotonic()-t0,3),
                'elapsed_seconds':round(time.monotonic()-start,3),
                'scope':'Author code computes orbit map/identity and exact correction; independent Fraction-Schur PSD checks final corrected matrices. This is NOT an independently rebuilt whole orbit-identity map or Lean kernel acceptance.',
                'verdict':'PASS' if nz==0 and all(psd) and not failed and not disagreements else 'FAIL'}
        RESULT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        print('CAPTURE RESULT '+json.dumps(result,sort_keys=True),flush=True)

    # Instrument just the return of verify_file; author verifier mathematics unchanged.
    tree=ast.parse(files['verify_perd'],filename='archive:release_ep3/verify_perd.py')
    target=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='verify_file']
    if len(target)!=1:
        raise ValueError('unexpected author function structure')
    f=target[0]
    locations=[i for i,s in enumerate(f.body) if isinstance(s,ast.Return)
               and isinstance(s.value,ast.Name) and s.value.id=='ok']
    if len(locations)!=1:
        raise ValueError('unexpected verify_file return structure')
    call=ast.Expr(value=ast.Call(func=ast.Name(id='capture_final',ctx=ast.Load()),
                  args=[ast.Name(id=n,ctx=ast.Load()) for n in ('pkg','Zs','lam','acc','nz','psd','D','uu')],
                  keywords=[]))
    f.body.insert(locations[0],call)
    ast.fix_missing_locations(tree)
    mod=types.ModuleType('frontier_author_verify_perd')
    mod.__file__='archive:release_ep3/verify_perd.py'
    mod.capture_final=capture
    exec(compile(tree,mod.__file__,'exec'),mod.__dict__)
    # Fail closed on anything other than the expected in-memory certificate.
    def data_open(path,mode='r'):
        if path!='pinned-d4-certificate' or mode!='rb':
            raise ValueError('unexpected author verifier file access')
        return io.BytesIO(files['certificate'])
    class SafePickle:
        @staticmethod
        def loads(raw):
            return base.DataOnlyUnpickler(io.BytesIO(raw)).load()
    mod.open=data_open
    mod.pickle=SafePickle
    print('BEGIN pinned author d4 replay, 1 worker; exact independent final PSD follows',flush=True)
    ok=mod.verify_file('pinned-d4-certificate',1)
    print('AUTHOR_VERIFIER_RETURN',ok,flush=True)
    return 0 if ok and RESULT.is_file() else 1


if __name__=='__main__':
    raise SystemExit(main())
