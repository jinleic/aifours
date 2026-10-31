#!/usr/bin/env python3
"""NEW isolation variants; preserve the correct helper and both frozen suites.

First exercise the two predicate mutants with the old11-test suite, so any
coverage gap is recorded honestly. Then baseline the new12-test suite and
exercise both predicate mutants AND all eight prior clause mutants with it.
No original source/evidence/test/fixture is overwritten, moved or deleted.
"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'frontier-20261029-frozen-input-guard.py'
OLD=ROOT/'frontier-20261029-frozen-input-guard-tests.py'
NEW=ROOT/'frontier-20261029-frozen-input-guard-tests-v2.py'
CONTROLS=ROOT/'frozen-guard-predicate-controls-v1'
OUTPUT=ROOT/'frontier-20261029-duplicate-predicate-verification-v1.json'
PIN='0cceb1807a030687a2a1da0fe1daba28d56674b70e8e399ff5badf0e4a9ff6b1'
ANCHOR="        if resolved in seen_paths or pin['sha256'] in seen_digests: refuse('duplicate inventoried source: '+name)"


def new_file(path,content):
    with path.open('x') as stream:stream.write(content)


def run_suite(label,module,test,count):
    case=CONTROLS/label;case.mkdir()
    testfile=case/'tests.py';text=test.read_text();new_file(testfile,text)
    env=dict(os.environ,KAC_EXCLUSIVE_ROOT=str(ROOT),KAC_GUARD_MODULE=str(module),KAC_GUARD_CONTROL_ROOT=str(case/'fixtures'))
    run=subprocess.run([sys.executable,str(testfile)],cwd=case,env=env,capture_output=True,text=True,timeout=120)
    new_file(case/'stdout.txt',run.stdout);new_file(case/'stderr.txt',run.stderr)
    exercised=f'Ran {count} tests' in run.stderr
    status=('PASS' if run.returncode==0 else 'KILLED') if exercised else 'INCONCLUSIVE_SETUP_OR_IMPORT'
    answer={'label':label,'module':str(module),'module_sha256':hashlib.sha256(module.read_bytes()).hexdigest(),
        'tests':test.name,'tests_sha256':hashlib.sha256(text.encode()).hexdigest(),'tests_expected':count,
        'whole_suite_actually_ran':exercised,'returncode':run.returncode,'status':status,'directory':str(case)}
    print(status,label,'whole_suite_ran',exercised,flush=True)
    return answer


def main():
    source=SOURCE.read_text();assert hashlib.sha256(source.encode()).hexdigest()==PIN
    assert source.count(ANCHOR)==1
    CONTROLS.mkdir(exist_ok=False)
    predicates={
        'path_predicate':ANCHOR.replace('resolved in seen_paths','False',1),
        'digest_predicate':ANCHOR.replace("pin['sha256'] in seen_digests",'False',1),
    }
    modules={}
    for label,changed_anchor in predicates.items():
        text=source.replace(ANCHOR,changed_anchor,1);assert text!=source
        path=CONTROLS/(label+'.py');new_file(path,text);modules[label]=path
    old=[]
    for label,module in modules.items():
        row=run_suite('old11-'+label,module,OLD,11)
        if row['status']=='PASS':row['status']='SURVIVED'
        old.append(row)
    baseline=run_suite('new12-baseline',SOURCE,NEW,12)
    results=[run_suite('new12-'+label,module,NEW,12) for label,module in modules.items()]
    original=json.loads((ROOT/'frozen-guard-controls-v1/mutation-results-all-v1.json').read_text())
    assert original['all_killed'] and len(original['mutants'])==8
    for prior in original['mutants']:
        module=Path(prior['directory'])/SOURCE.name
        assert module.resolve().is_relative_to(ROOT)
        assert hashlib.sha256(module.read_bytes()).hexdigest()==prior['mutant_sha256']
        results.append(run_suite('new12-clause-'+prior['mutant'],module,NEW,12))
    record={'owner':'MathKacMoody-2','kind':'EXPLICIT_PREDICATE_ISOLATION_AND_COMPLETE12_TEST_REGRESSION',
        'source':{'file':SOURCE.name,'sha256':PIN},'old11_predicate_isolation':old,'new12_baseline':baseline,
        'new12_all10_mutants':results,'all10_killed_with_real12_test_execution':all(r['status']=='KILLED' and r['whole_suite_actually_ran'] for r in results),
        'preservation':'All variants and test fixtures NEW and retained. Original production helper,old11 suite,prior eight mutants and scientific evidence unchanged.',
        'limits':'Synthetic integrity/refusal diagnostics only. A surviving old11 path-predicate mutant does not imply acceptance of unsafe data:the duplicate-digest and byte-pin guards still reject it. The new distinct-pin fixture isolates the duplicate-path refusal reason. No scientific source/rank/native-library adoption.',
        'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    record['original_source_still_pinned']=hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN
    with OUTPUT.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    if baseline['status']!='PASS' or not record['all10_killed_with_real12_test_execution'] or not record['original_source_still_pinned']:
        raise SystemExit('A full-suite baseline failed,mutant survived,or source changed;do not drop the failed case.')
    print('PASS new12 baseline and all10 isolated/clause mutants',OUTPUT.name,flush=True)


if __name__=='__main__':main()
