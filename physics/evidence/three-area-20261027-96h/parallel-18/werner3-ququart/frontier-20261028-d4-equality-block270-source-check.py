#!/usr/bin/env python3
"""Bind source block270 to the stated scalar antisymmetric Gram tensor.

All source/corrected bytes are checked and parsed from byte snapshots; only
built-in pickle data are accepted. In-memory faults do not modify any file or
choose an original q3 target state.
"""
import copy
import hashlib
import io
import json
import lzma
import pickle
import tarfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ARCH=ROOT/'frontier-20261028-tomar-release-ep3-v3.tar.gz'
DATA=ROOT/'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
PIN_ARCH='2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3'
PIN_DATA='c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'
MEMBER='release_ep3/certs/ep3_perd_d4.pkl.xz'
PIN_MEMBER='0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'
OUT=ROOT/'frontier-20261028-d4-equality-block270-source-check-results.json'
SITE='S|0,1|f0_11_2';AUX='A|0,1|f0_2_2';LABEL=(0,(1,1),(2,))
KEYS=(((),((2,0),(3,1)),((0,-1),(1,-1))),
      ((),((2,1),(3,0)),((0,-1),(1,-1))))

class SafeData(pickle.Unpickler):
    def find_class(self,module,name):raise pickle.UnpicklingError('global loading forbidden')

def digest(x):return hashlib.sha256(x).hexdigest()
def freeze(x):return tuple(freeze(v) for v in x) if isinstance(x,(list,tuple)) else x

def valid(pkg,corr):
    try:
        t=pkg['types'][270];z=corr['matrices'][270]
        if (t['kind'],t['family'],tuple(t['rows']),t['r'])!=('src','31',('a* a* a b',),1):return False
        if tuple(t['modules'])!=(SITE,SITE,SITE,AUX) or t['W']!=[[1]]:return False
        keys,C=pkg['diagrams'][(4,(0,1))][LABEL]
        if freeze(keys)!=KEYS or C!=[[-1],[1]]:return False
        J=pkg['aux'][AUX]
        if len(J)!=16 or any(len(row)!=1 for row in J) or [row[0] for row in J]!=[int(i==12) for i in range(16)]:return False
        if z['r']!=1 or len(z['values'])!=1:return False
        num,den=map(int,z['values'][0])
        return num>0 and den>0
    except (IndexError,KeyError,TypeError,ValueError):return False

araw=ARCH.read_bytes();draw=DATA.read_bytes()
if digest(araw)!=PIN_ARCH or digest(draw)!=PIN_DATA:raise ValueError('source snapshot mismatch')
with tarfile.open(fileobj=io.BytesIO(araw),mode='r:gz') as tf:member=tf.extractfile(MEMBER).read()
if digest(member)!=PIN_MEMBER:raise ValueError('member mismatch')
pkg=SafeData(io.BytesIO(lzma.decompress(member,memlimit=256*1024*1024))).load()
corr=json.loads(lzma.decompress(draw,memlimit=256*1024*1024))
actual=valid(pkg,corr)
p=copy.deepcopy(pkg);keys,C=p['diagrams'][(4,(0,1))][LABEL];p['diagrams'][(4,(0,1))][LABEL]=(keys,[[1],[1]])
f1=not valid(p,corr)
p=copy.deepcopy(pkg);p['aux'][AUX][12][0]=0;p['aux'][AUX][0][0]=1
f2=not valid(p,corr)
c=copy.deepcopy(corr);c['matrices'][270]['values'][0][0]='-1'
f3=not valid(pkg,c)
p=copy.deepcopy(pkg);p['types'][270]['rows']=['a* a a b']
f4=not valid(p,corr)
controls={'wrong_site_wedge_sign_rejected':f1,'wrong_aux_basis_rejected':f2,
          'nonpositive_corrected_scalar_rejected':f3,'wrong_physical_row_rejected':f4}
r={'kind':'actual_d4_scalar_gram_270_physical_tensor_binding',
   'archive_sha256':PIN_ARCH,'member_sha256':PIN_MEMBER,'corrected_data_sha256':PIN_DATA,
   'source_block_index':270,'actual_binding_passed':actual,
   'source_row':'a* a* a b','family':'31','source_rank':1,'joint_W':[[1]],
   'site_tensor':'e3⊗e3⊗(e1⊗e0−e0⊗e1) at each of three C4 sites',
   'aux_tensor':'e1⊗e1⊗e0⊗e0 in C2 replicas','corrected_scalar_strictly_positive':actual,
   'intentional_faults_detected':controls,
   'scope':'Exact source-block/positive-scalar binding only; no physical C/state tested, no entire certificate identity, equality classification, formal kernel, independent family or novelty claim.',
   'verdict':'PASS' if actual and all(controls.values()) else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
