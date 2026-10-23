#!/usr/bin/env python3
"""Freeze the completed FDGDD18 worker evidence bundle; no solver/checker is launched by this script.
Usage from lane root: write_fdgdd18_receipt.py NEW_RECEIPT.json
"""
import lane_guard  # noqa: F401
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime
from lane_guard import xopen

EV='evidence/fdgdd18-d15-inflated'
PIN=f'{EV}/fdgdd_5_18_inflated_D15.txt'
EXPECTED='3e22f5021631ac82ea5b5fa6f884984bb874f1f9a384fd35bfeff523e731a998'
RUN='runs/b3-fd-d15-inflation-s1'
REPLAY='runs/b3-fd-d15-inflation-replay-v1'
CHAIN='runs/b3-full-chain-replay-v1'


def info(p):
    data=open(p,'rb').read()
    return {'path':p,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}


def main():
    out=sys.argv[1]
    assert info(PIN)['sha256']==EXPECTED
    source=json.load(open(f'{RUN}/summary.json'))
    mutations=json.load(open(f'{EV}/mutations/mutation-results.json'))
    chain=json.load(open(f'{CHAIN}/chain-replay.json'))
    seed=json.load(open(f'{EV}/seed-v1.json'))
    assert source['route1']['result']=='PASS' and source['route1']['sha256']==EXPECTED
    assert source['route2'].startswith('PASS kind=FDGDD k=5 m=18 ')
    assert mutations['mutations']==mutations['as_intended']==8
    assert mutations['unmutated_route1']=='PASS' and mutations['unmutated_route2'].startswith('PASS ')
    replay=f'{REPLAY}/fdgdd_5_18_inflated_D15.txt'
    chainraw=f'{CHAIN}/assembly/fdgdd_5_18_inflated_D15.txt'
    expansion='runs/b3-seed-replay-v1/fdgdd18.txt'
    for p in (replay,chainraw,expansion):assert open(p,'rb').read()==open(PIN,'rb').read()
    assert chain['byte_identical'] and seed['audit']['byte_identical']
    files=[os.path.join(d,f) for d,_,fs in os.walk('.') for f in fs]
    codes=['inflate_h6_frames.py','gdd_seed_search4.py','lanelib.py','lane_guard.py','check_gdd34.py','check_gdd34.c',
           'mutations_fmt.py','replay_fdgdd18_chain.py','seed_fdgdd18.py','diagnose_h6_frame.py']
    rec={
        'recorded_at_host':datetime.now().astimezone().isoformat(),
        'object':'FDGDD(3,4,5{18}) = FDH(5,18,4,3)',
        'status':'CANDIDATE: worker finite checks/reproducibility complete; parent verification, bridge and priority separate',
        'certificate':info(PIN),
        'definition':{'source':info('sources/tz/tan-zhou-2503.11934.txt'),'lines':'LF237-247',
                      'points':90,'groups':5,'group_size':18,'blocks':14580,'transverse_triples':58320,
                      'derived_triples_each_point':648,'frame_classes_each_point':36,
                      'triples_each_frame_class':18,'classes_missing_each_other_group':9},
        'ingredients':{
            'master_bare_H_5_6':info(f'{EV}/master_H_5_6.json'),
            'master_model_inputs':[info(f'{EV}/master-inputs/{p}') for p in ('model.cnf','model.cnf.log','summary.json')],
            'master_level':'Bare H-design only, NOT an FDGDD or RDGDD assumption',
            'specific_master_nonframe_diagnosis':info(f'{EV}/master-nonframe-diagnosis-v1.json'),
            'local_RDTD_3_4_3':info(f'{EV}/local_RDTD_3_4_3.txt'),
            'local_RDTD_check_receipt':info('runs/b2/local-rdtd3/receipt-v1.json')},
        'construction':{
            'code':info('code/inflate_h6_frames.py'),'master_group':'D15 of order30, regular master action',
            'blocks':'540 master blocks, each weighted by all27 zero-sum copy assignments on Z3:14580 blocks',
            'frames':'New size18 fixed-design frame searches at copies0 and1; master action transports and copy negation maps1 to2',
            'not_assumed':'No master KF(6^4); no natural lift of a master frame; chosen copy0 frame negation-invariance not claimed',
            'frame_models':source['colourings'],'source_summary':info(f'{RUN}/summary.json'),
            'models':[info(f'{RUN}/{p}') for p in ('colour-copy0.cnf','colour-copy0.cnf.log','colour-copy1.cnf','colour-copy1.cnf.log')],
            'note':info(f'{EV}/construction-note.md')},
        'worker_checkers':{
            'route1':{'code':info('code/check_gdd34.py'),'raw_result':source['route1'],
                      'raw_pin_binding':'same exact SHA and observed rerun on the pin; positive-on-pin also retained in mutation receipt'},
            'route2':{'author':'Tz43CCheckers, definition/format only; no route1 code read',
                      'source':info('code/check_gdd34.c'),'binary':info('code/bin/check_gdd34_c'),
                      'result':source['route2']},
            'assumed_symmetry':'none in either raw checker',
            'calibration':'published RDGDD(3,4,10{2}), earlier FDGDD(3,4,5{8}) and explicit RDTD(3,4,3); controls per saved receipts'},
        'mutations':{'receipt':info(f'{EV}/mutations/mutation-results.json'),'total':8,'both_routes_as_intended':8,
                     'all_files_retained':True,'fixtures':[info(f'{EV}/mutations/{p}') for p in sorted(os.listdir(f'{EV}/mutations')) if p.endswith('.txt')]},
        'replay':{
            'pinned_master_model_plus_resolved_frames':{'output':info(replay),'byte_identical':True,
                                                       'summary':info(f'{REPLAY}/summary.json')},
            'full_three_SAT_solves':{'receipt':info(f'{CHAIN}/chain-replay.json'),'output':info(chainraw),
                                     'master_seed':0,'frame_seed':1,'byte_identical':True},
            'solver_free_seed':{'seed':info(f'{EV}/seed-v1.json'),'expander':info('code/seed_fdgdd18.py'),
                                'output':info(expansion),'byte_identical':True,'action_audit':seed['audit']}},
        'resources_observed_native_time_l':{
            'source_frame_solve_seconds':[r['seconds'] for r in source['colourings']],
            'producer_replay':{'wall_seconds':6.71,'user_seconds':6.64,'sys_seconds':0.06,'max_rss_bytes':65028096},
            'full_solver_chain_replay':{'wall_seconds':6.92,'user_seconds':6.82,'sys_seconds':0.09,'max_rss_bytes':65126400},
            'mutations':{'wall_seconds':2.14,'user_seconds':1.96,'sys_seconds':0.15,'max_rss_bytes':67076096},
            'seed_make':{'wall_seconds':0.22,'user_seconds':0.20,'sys_seconds':0.01,'max_rss_bytes':48267264},
            'seed_expand':{'wall_seconds':0.13,'user_seconds':0.11,'sys_seconds':0.01,'max_rss_bytes':26755072},
            'scope':'These are per-command native observations, not a claimed aggregate peak.'},
        'lane_resources':{'new_lane_bytes_before_receipt':sum(os.path.getsize(p) for p in files),
                          'lane_files_before_receipt':len(files),'host_free_disk_bytes':shutil.disk_usage('.').free,
                          'cooperative_stops':info('runs/stops-after-fdgdd18-candidate.json'),
                          'operational_checkpoints':info('runs/resource-monitor-v1/resource-checkpoints.jsonl')},
        'code_hashes':{p:info('code/'+p) for p in codes},
        'other_required_finite_input':{'path':'evidence/gcdcqs18-z8z3z3/gcdcqs18_4_2_z8z3z3.txt',
                                       'sha256':'1382d572f8024c9b93ff6f5cf8aff942a9538119e8462ba54b02b6f160da282e',
                                       'receipt':info('evidence/gcdcqs18-z8z3z3/receipt-v1.json')},
        'written_family_bridge':info('sources/tz43-family-consequence-v1.md'),
        'limits':'Both finite objects now have worker-checked candidates. No novelty, priority, formal proof or met-gate claim; parent verification and hostile/source bridge review remain authoritative.'}
    rec['receipt_generator']=info(__file__)
    with xopen(out) as fh:json.dump(rec,fh,indent=1,ensure_ascii=False);fh.write('\n')
    print(json.dumps(info(out)))


if __name__=='__main__':main()
