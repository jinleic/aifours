#!/usr/bin/env python3
"""One bounded joint released-system16 attempt; no retry or infeasibility claim."""
import argparse
import faulthandler
faulthandler.enable()
from collections import Counter, defaultdict
import hashlib
import itertools
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
from types import SimpleNamespace

sys.dont_write_bytecode = True
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
TARGET = Path('/Users/jinleic/jinleic-workspace/ai4s/kirkman-large-sets-57-87')
sys.path.insert(0, str(TARGET / 'work'))
import c19_search as c19
import c19_verify as independent
import c19_staged_completion as staged
import ortools
from ortools.sat.python import cp_model

ROOT = Path(__file__).resolve().parent
EXPECTED = '6515e4041991d0c857df9c5d5752613f8d958d4ee76296cbbc24c024b807d714'

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--seconds', type=float, default=600)
    ap.add_argument('--pair-seconds', type=float, default=480)
    ap.add_argument('--threads', type=int, default=2)
    ap.add_argument('--seed', type=int, default=19161014)
    args = ap.parse_args()
    assert 0 < args.pair_seconds <= args.seconds <= 600 and 1 <= args.threads <= 2
    out = ROOT / 'evidence' / 'joint57'
    out.mkdir(exist_ok=False)
    started = time.monotonic()
    deadline = started + args.seconds
    source_names = ['c19_search.py','c19_verify.py','c19_staged_completion.py',
                    'search_staged.py','search_cyclic.py','check_lkts.py','check_partial_packing.py']
    source_hashes = {}
    for name in source_names:
        src = TARGET / 'work' / name
        source_hashes[str(src)] = sha(src)
        shutil.copyfile(src, out / name)
    shutil.copyfile(__file__, out / 'joint_search.source.py')
    source_hashes[str(Path(__file__).resolve())] = sha(__file__)
    packing_path = TARGET / 'evidence' / 'c19-17-staged.frozen-packing.json'
    assert sha(packing_path) == EXPECTED
    shutil.copyfile(packing_path, out / 'input-packing17.json')
    packing = json.loads(packing_path.read_text())
    data, orbit_ids = c19.inventory()
    independent.verify_inventory(data)
    used = set()
    for candidate in packing:
        actual = {orbit_ids[key] for key in independent.check_fixed(candidate)}
        assert len(actual) == 28 and actual == set(candidate['orbit_ids'])
        assert not used.intersection(actual)
        used.update(actual)
    assert len(packing) == 17 and len(used) == 476
    retained = packing[:16]
    forbidden = set().union(*(set(c['orbit_ids']) for c in retained))
    remaining = sorted(set(range(1540)) - forbidden)
    assert len(forbidden) == 448 and len(remaining) == 1092
    residual = Counter(p for oid in remaining for p in data['triple_orbits'][oid]['pair_orbits'])
    assert residual == Counter({p: 39 for p in range(84)})
    save(out / 'retained16.json', retained)
    save(out / 'released-system16.json', packing[16])
    save(out / 'inventory.json', data)
    # Reuse the inspected fixed_model's row conventions. Count 5 enables all
    # ABC starter rows. Its last equality is broadened to the mathematically
    # complete feasible interval 4..9; no original source is modified.
    model, fixed_rows = c19.fixed_model(data, forbidden, 5, cp_model)
    last = model.proto.constraints[len(model.proto.constraints) - 1]
    assert list(last.linear.domain) == [5,5]
    last.linear.domain[0] = 4
    last.linear.domain[1] = 9
    fixed_count = len(fixed_rows)
    assert len(model.proto.variables) == fixed_count
    orbit_columns = {oid: [] for oid in remaining}
    for index, (oid, shift) in enumerate(fixed_rows):
        orbit_columns[oid].append(model.get_bool_var_from_proto_index(index))
    pairs = list(itertools.combinations(range(57), 2))
    pair_ids = {pair: index for index, pair in enumerate(pairs)}
    pair_columns = [[[] for _ in pairs] for _ in range(2)]
    free_rows = []
    anchor_oid = min(data['inadmissible_fixed_AAA_orbit_ids'])
    anchor_variable = None
    for oid in remaining:
        representative = data['triple_orbits'][oid]['representative']
        for shift in range(19):
            block = c19.translate(representative, shift)
            indices = [pair_ids[p] for p in itertools.combinations(block,2)]
            for base in range(2):
                var = model.new_bool_var('')
                free_rows.append([base, oid, shift, list(block)])
                orbit_columns[oid].append(var)
                for p in indices:
                    pair_columns[base][p].append(var)
                if (oid,shift,base) == (anchor_oid,0,0):
                    anchor_variable = var
    assert len(free_rows) == 41496
    for column in orbit_columns.values():
        model.add_exactly_one(column)
    for base in pair_columns:
        for column in base:
            model.add_exactly_one(column)
    # AP orbits cannot enter the replacement, so this anchor loses only base
    # interchange and independent translation of base0. No third-point order.
    assert anchor_variable is not None
    model.add(anchor_variable == 1)
    assert not model.validate(), model.validate()
    model_path = out / 'model.pbtxt'
    model_path.write_text(str(model.proto))
    rows_path = out / 'rows.json'
    save(rows_path, {'fixed_rows': fixed_rows, 'free_rows':free_rows})
    manifest = {
        'scope':'one incomplete feasibility attempt, with free-base resolution deferred',
        'command':sys.argv,'python':platform.python_version(),'ortools':ortools.__version__,
        'packing_sha256':EXPECTED,'source_hashes':source_hashes,
        'released_zero_based_index':16,'retained_zero_based_indices':list(range(16)),
        'remaining_orbit_ids':remaining,'remaining_orbits':len(remaining),
        'pair_orbit_incidence_counts':dict(residual),'fixed_rows':fixed_count,
        'free_rows':len(free_rows),'variables':len(model.proto.variables),
        'constraints':len(model.proto.constraints),'model_sha256':sha(model_path),
        'rows_sha256':sha(rows_path),'inventory_sha256':sha(out/'inventory.json'),
        'replacement_aaa_range':[4,9],
        'replacement_model':'one 19-class orbit from a starter and nine fixed ABC classes; every feasible AAA count',
        'anchor':{'orbit_id':anchor_oid,'shift':0,'base':0,'reason':'mandatory-free AP orbit'},
        'forbidden_orbit_ids':sorted(forbidden),
        'pair_cover_columns':3192,'joint_orbit_columns':1092,
        'replacement_point_columns':57,'replacement_pair_orbit_columns':84,
        'no_candidate_blocking':True,'total_wall_limit':args.seconds,
        'construction_wall_seconds':time.monotonic()-started}
    save(out/'manifest.json',manifest)
    print(json.dumps({k:manifest[k] for k in ('fixed_rows','free_rows','variables','constraints','model_sha256','construction_wall_seconds')}),flush=True)
    solver, info = staged.cp_solve(model, min(args.pair_seconds,max(0.001,deadline-time.monotonic())),args.threads,args.seed,str(out/'pair.log'))
    result = {'manifest_sha256':sha(out/'manifest.json'),'pair_cover':info,
              'full_goal_solved':False,'target57_solved':False,'target87_solved':False,
              'candidate_found':solver is not None,'resolution_verdicts':[]}
    if solver is not None:
        # extract_fixed expects only its own prefix of decision variables.
        prefix_solver = SimpleNamespace(response_proto=SimpleNamespace(
            solution=list(solver.response_proto.solution)[:fixed_count]))
        replacement = c19.extract_fixed(prefix_solver,fixed_rows,data)
        replacement_orbits = {orbit_ids[k] for k in independent.check_fixed(replacement)}
        assert replacement_orbits == set(replacement['orbit_ids'])
        selected = [free_rows[i] for i in range(len(free_rows))
                    if solver.value(model.get_bool_var_from_proto_index(fixed_count+i))]
        bases = [sorted(tuple(row[3]) for row in selected if row[0]==base) for base in range(2)]
        actual_orbits = set(replacement_orbits)
        for blocks in bases:
            assert len(blocks)==len(set(blocks))==532
            assert Counter(p for b in blocks for p in itertools.combinations(b,2))==Counter(pairs)
            keys = {orbit_ids[independent.key(b)] for b in blocks}
            assert len(keys)==532 and not actual_orbits.intersection(keys)
            actual_orbits.update(keys)
        assert actual_orbits==set(remaining)
        save(out/'replacement.json',replacement)
        save(out/'pair-cover.json',{'selected_rows':selected,'bases':bases,'replacement':replacement})
        result['pair_cover_independent_check']='PASS'
        resolutions=[]
        for base, blocks in enumerate(bases):
            cap = max(0,deadline-time.monotonic())/(2-base)
            if cap < 0.01:
                classes=None
                verdict={'status':'NOT_RUN','reason':'overall deadline','unrestricted':True}
            else:
                classes,verdict=staged.resolve(blocks,cap,args.threads,args.seed+base+1,out/f'resolution{base}')
            resolutions.append(classes)
            result['resolution_verdicts'].append(verdict)
        if all(r is not None for r in resolutions):
            cert=out/'candidate-lkts57.txt'
            c19.write_certificate(cert,retained+[replacement],resolutions)
            checked=subprocess.run([sys.executable,str(TARGET/'work'/'check_lkts.py'),str(cert)],capture_output=True,text=True)
            (out/'certificate-check.log').write_text(checked.stdout+checked.stderr)
            assert checked.returncode==0
            result['target57_solved']=True
            result['certificate_sha256']=sha(cert)
    assert all(sha(p)==h for p,h in source_hashes.items())
    assert sha(packing_path)==EXPECTED
    result['total_wall_seconds']=time.monotonic()-started
    result['remaining_owned_solver_children']=0
    result['interpretation']='UNKNOWN never proves infeasibility; no proof trace and no exhaustion of the joint model'
    save(out/'result.json',result)
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':
    main()
