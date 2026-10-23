"""Only the frozen data-plane refinement delta: append3ordered unit clauses
at L1 and3more at L2; the F_one body and variables never change.
Expected hashes are PLANNED, not measured-feed fields. Legacy executor stays
90b6f592...8484; only parent measured replay counts final refutations.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
DESIGN=ROOT/'review/N8-FONE-REFINE.r2.json'
DESIGN_SHA='bf9f71937d7fcc98fceb26b3aaf05505d8df68bdc5005fe90b61c9fb74422d1a'
WMAN=ROOT/'evidence/n8_one_p4_templates_v1/MANIFEST.json'
WMAN_SHA='355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74'
BASE_SHA='374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9'
Z1=(1625,1674,1723)
Z2=(1632,1681,1730)


def load_inputs():
    db=DESIGN.read_bytes(); wb=WMAN.read_bytes()
    if hashlib.sha256(db).hexdigest()!=DESIGN_SHA or hashlib.sha256(wb).hexdigest()!=WMAN_SHA:
        raise RuntimeError('frozen refinement design/WMAN changed')
    d=json.loads(db); w=json.loads(wb)
    if d['L1']['variables']!=list(Z1) or d['L2']['variables']!=list(Z2) or w['base_cnf_sha256']!=BASE_SHA:
        raise RuntimeError('split/base identity mismatch')
    cases={x['id']:x for x in w['cases']}
    if len(cases)!=16: raise RuntimeError('missing/duplicate template')
    for x in cases.values():
        if len(x['units'])!=42 or ({abs(u) for u in x['units']} & (set(Z1)|set(Z2))):
            raise RuntimeError('split variable fixed by template')
    if set(Z1)&set(Z2): raise RuntimeError('levels overlap')
    return d,cases


def signs(z,b):
    if type(b) is not int or not 0<=b<8: raise ValueError('sign index must be0..7')
    return [v if(b>>j)&1 else -v for j,v in enumerate(z)]


def path_units(template_units,b,c=None):
    if len(template_units)!=42: raise ValueError('source must be exactly42units')
    out=list(template_units)+signs(Z1,b)
    if c is not None: out+=signs(Z2,c)
    if len(out) not in(45,48) or len({abs(v) for v in out})!=len(out):
        raise ValueError('path variables overlap')
    return out


def header(units):
    return ('p cnf 509915 %d\n'%(5740226+len(units))).encode()


def tail(units):
    return ''.join('%d 0\n'%u for u in units).encode()
