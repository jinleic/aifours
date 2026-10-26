"""Frozen proposed assay; execution requires its OWN named parent GO.

V2 supersedes unexecuted V1 solely to invoke the actual exact-dual gate on both
coefficient and negative-weight mutations. Three LP stages; no retries or installs.
"""
from __future__ import annotations

import datetime
import itertools
import json
import os
import signal
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_array

import check_entropy_imports_v1 as base

HERE = Path(__file__).resolve().parent
ZY_PATH = base.BASE / 'evidence' / 'zy-cond-cg-Rminus.json'
ZY_PIN = 'd7a293025dc28d6244f734fa8315238d86b6cc963e5ce8157fcb7c99e16d0af4'
DIAMONDS = ((2,4,1,3),(2,6,1,7),(3,5,1,4),(5,7,1,6),
            (3,10,4,8),(4,9,3,8),(6,10,7,8),(7,9,6,8))
TRIPLETS = ((1,0,0),(2,0,1),(2,1,0),(3,1,1),(3,0,3),(3,3,0),
            (4,1,3),(4,3,1),(6,3,5),(6,5,3),(7,5,5))
ZY_TERMS = (('A',-2),('B',-2),('C',-1),('AB',3),('AC',3),('AD',1),
            ('BC',3),('BD',1),('CD',-1),('ABC',-4),('ABD',-1))
OUTPUTS = ('assay-shannon-v2.json','assay-zy-v2.json','assay-mem5-v2.json')
START = time.monotonic()
DEADLINE = START + 480.0
STOP = False


def request_stop(signum, frame):
    global STOP
    STOP = True


signal.signal(signal.SIGTERM, request_stop)
signal.signal(signal.SIGINT, request_stop)


def guard():
    if STOP:
        raise InterruptedError('cooperative stop requested')
    if time.monotonic() >= DEADLINE:
        raise TimeoutError('cooperative 480-second deadline reached')


def need(condition, reason):
    guard()
    if not condition:
        raise ValueError(reason)


def combine(*weighted_rows):
    row = {}
    for factor, term in weighted_rows:
        base.add(row, term, factor)
    return {mask: value for mask, value in row.items() if value}


def info(a, b, conditioned=0):
    return base.information(a, b, conditioned)


def ing(a, b, c, d, conditioned=0):
    return combine((1,info(a,b,conditioned|c)),(1,info(a,b,conditioned|d)),
                   (1,info(c,d,conditioned)),(-1,info(a,b,conditioned)))


def mem_rows():
    for diamond in DIAMONDS:
        outside = [v for v in range(1,11) if v not in diamond]
        for vertices in itertools.permutations(diamond):
            a,b,c,d = (1 << (v-1) for v in vertices)
            for z_vertex in outside:
                guard()
                z = 1 << (z_vertex-1)
                w = 1023 ^ a ^ b ^ c ^ d ^ z
                zz = combine((1,info(a,z,w|b)),(1,info(b,z,w|a)))
                cc = combine((1,info(a,c,w|b)),(1,info(b,c,w|a)))
                dd = combine((1,info(a,d,w|b)),(1,info(b,d,w|a)))
                for alpha,beta,gamma in TRIPLETS:
                    row = combine((1,info(a,b,w|z)),(alpha,ing(a,b,c,d,w)),
                                  (alpha,zz),(beta,cc),(gamma,dd))
                    yield row, {'kind':'MEM-I','abcd':vertices,'z':z_vertex,
                                'W_mask':w,'triplet':[alpha,beta,gamma]}
                for k in range(1,7):
                    row = combine((1,info(a,b,w|z)),(k,ing(a,c,b,d,w)),
                                  (k,zz),(k*(k-1)//2,cc))
                    yield row, {'kind':'MEM-II','abcd':vertices,'z':z_vertex,
                                'W_mask':w,'k':k}


def sparse(rows):
    data, indices, indptr = [], [], [0]
    for row in rows:
        guard()
        for mask, value in row.items():
            indices.append(mask-1)
            data.append(float(value))
        indptr.append(len(data))
    return csr_array((np.asarray(data),np.asarray(indices,dtype=np.int32),
                      np.asarray(indptr,dtype=np.int32)),shape=(len(rows),1023))


def dual_identity(rows, fds, y, u, z, lower):
    need(len(y)==len(rows) and len(u)==10 and len(z)==10 and len(lower)==1023,
         'missing dual weight')
    need(all(v>=0 for v in y+u+lower),'negative dual weight')
    residual = {1023:F(1)}
    for v, weight in enumerate(u):
        base.add(residual,{1<<v:1},-weight)
    for row, weight in zip(rows,y):
        base.add(residual,row,weight)
    for row, weight in zip(fds,z):
        base.add(residual,row,weight)
    for mask, weight in enumerate(lower,1):
        base.add(residual,{mask:1},weight)
    need(not any(residual.values()),'rational dual coefficient identity failed')


def reject_dual_mutation(reason, rows, fds, y, u, z, lower):
    try:
        dual_identity(rows,fds,y,u,z,lower)
    except ValueError as error:
        need(str(error)==reason,'mutation failed for wrong reason: '+str(error))
        return
    raise ValueError('dual mutation was accepted')


def exact_dual(result, rows, fds):
    # min(-hV), rows -g<=0, caps h(v)<=1, fds=0, and all h>=0.
    y = [F(float(v)).limit_denominator(10**6) for v in -result.ineqlin.marginals[:len(rows)]]
    u = [F(float(v)).limit_denominator(10**6) for v in -result.ineqlin.marginals[len(rows):]]
    z = [F(float(v)).limit_denominator(10**6) for v in result.eqlin.marginals]
    lower = [F(float(v)).limit_denominator(10**6) for v in result.lower.marginals]
    dual_identity(rows,fds,y,u,z,lower)
    positive = next((index for index,weight in enumerate(y) if weight>0),None)
    need(positive is not None,'missing positive inequality weight for control')
    altered = list(y)
    altered[positive] += F(1,7)
    reject_dual_mutation('rational dual coefficient identity failed',rows,fds,altered,u,z,lower)
    altered = list(y)
    altered[positive] = F(-1)
    reject_dual_mutation('negative dual weight',rows,fds,altered,u,z,lower)
    return y,u,z,lower,sum(u)


def solve_stage(index, rows, labels, fds, expected=None):
    guard()
    caps = [{1<<v:1} for v in range(10)]
    constraints = [{mask:-value for mask,value in row.items()} for row in rows] + caps
    objective = np.zeros(1023)
    objective[-1] = -1
    matrix_ub = sparse(constraints)
    matrix_eq = sparse(fds)
    guard()
    remaining = DEADLINE-time.monotonic()
    need(remaining>1.0,'insufficient cooperative window for next LP stage')
    stage_start = time.monotonic()
    result = linprog(objective,A_ub=matrix_ub,
                     b_ub=np.asarray([0.0]*len(rows)+[1.0]*10),
                     A_eq=matrix_eq,b_eq=np.zeros(10),bounds=(0,None),
                     method='highs-ds',options={'time_limit':min(120.0,remaining-1.0),
                       'threads':1,'presolve':True,'dual_feasibility_tolerance':1e-9,
                       'primal_feasibility_tolerance':1e-9})
    guard()
    record = {'stage':index,'lp_status':int(result.status),'lp_message':result.message,
              'float_objective':None if result.fun is None else float(-result.fun),
              'elapsed_seconds':time.monotonic()-stage_start,'rows':len(rows),
              'certificate_status':'NO_EXACT_BOUND','pid':os.getpid(),'pgid':os.getpgrp()}
    certificate_error = None
    if result.success:
        try:
            y,u,z,lower,bound = exact_dual(result,rows,fds)
            if expected is not None:
                need(bound==expected,'exact calibration value mismatch')
            record.update(certificate_status='EXACT_RATIONAL_DUAL_IDENTITY',exact_bound=str(bound),
                improves_published_bound=bound<F(1847,276),
                inequality_terms=[{'row':{str(m):str(c) for m,c in row.items()},'weight':str(weight),
                  'source':label} for row,label,weight in zip(rows,labels,y) if weight],
                singleton_weights=[str(v) for v in u],
                fd_terms=[{'row':{str(m):str(c) for m,c in row.items()},'weight':str(weight)}
                          for row,weight in zip(fds,z) if weight],
                nonnegative_entropy_terms={str(mask):str(weight) for mask,weight in enumerate(lower,1) if weight},
                controls=['coefficient mutation rejected by actual identity gate',
                          'negative multiplier rejected by actual identity gate'])
        except ValueError as error:
            certificate_error = str(error)
            record['certificate_error'] = certificate_error
    with (HERE / OUTPUTS[index]).open('x') as destination:
        json.dump(record,destination,indent=2)
    print(json.dumps({key:record[key] for key in ('stage','lp_status','float_objective','certificate_status')},default=str),flush=True)
    need(result.success,'LP did not return an optimal solution; no retry')
    need(certificate_error is None,'exact certificate/calibration failed; no retry')


def main():
    need(not any((HERE / name).exists() for name in OUTPUTS),'refusing to overwrite assay output')
    graph = base.load_pinned(HERE/'inputs-v1.json',base.GRAPH_PIN)['graph']
    zy = base.load_pinned(ZY_PATH,ZY_PIN)['zy_instances']
    need(len(zy)==36,'wrong calibration input count')
    fds = base.fd_rows(list(range(1,11)),graph['undirected_edges'])
    rows = base.elemental_rows(10)
    labels = [{'kind':'elemental-Shannon','index':i} for i in range(len(rows))]
    seen = {base.signature(row) for row in rows}
    def append(row,label):
        key = base.signature(row)
        if key and key not in seen:
            rows.append(row)
            labels.append(label)
            seen.add(key)
    solve_stage(0,rows,labels,fds,F(114,17))
    for masks in zy:
        values = dict(zip('ABCD',masks))
        row = {}
        for names,coefficient in ZY_TERMS:
            mask = 0
            for name in names:
                mask |= values[name]
            base.add(row,{mask:1},coefficient)
        append({mask:value for mask,value in row.items() if value}, {'kind':'Zhang-Yeung','ABCD':masks})
    solve_stage(1,rows,labels,fds,F(1212,181))
    for row,label in mem_rows():
        append(row,label)
    solve_stage(2,rows,labels,fds)


if __name__ == '__main__':
    state = 'ERROR'
    print(json.dumps({'launch':{'pid':os.getpid(),'pgid':os.getpgrp(),
          'observed_clock':datetime.datetime.now().astimezone().isoformat(),
          'cooperative_total_seconds':480,'native_LP_limit_seconds_per_stage':120,
          'scientific_processes':1,'threads':1}}),flush=True)
    try:
        main()
        state = 'COMPLETED'
    finally:
        print(json.dumps({'settlement':{'status':state,'pid':os.getpid(),'pgid':os.getpgrp(),
              'observed_clock':datetime.datetime.now().astimezone().isoformat(),
              'elapsed_seconds':time.monotonic()-START}}),flush=True)
