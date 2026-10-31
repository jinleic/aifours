#!/usr/bin/env python3
"""Fresh one-protection mutants plus copied tests, all retained in owner root.

A mutant counts as KILLED only if the complete11-test suite actually ran and
returned nonzero. Setup/import failures are INCONCLUSIVE, not counted killed.
No original helper, test, frozen evidence or prior fixture is edited/deleted.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE='frontier-20261029-frozen-input-guard.py'
TESTS='frontier-20261029-frozen-input-guard-tests.py'
MUTANTS={
'unsafe_path':"    if not isinstance(name,str) or Path(name).name!=name or not candidate.resolve().is_relative_to(root): refuse('unsafe inventoried path: '+str(name))",
'missing_input':"    if not path.is_file(): refuse('inventoried input is missing: '+name)",
'changed_input':"    if count!=pin['bytes'] or digest.hexdigest()!=pin['sha256']: refuse('inventoried input bytes differ: '+name)",
'missing_inventory':"    if not inventory_path.is_file(): refuse('input inventory is missing: '+inventory_name)",
'changed_inventory':"    if hashlib.sha256(raw).hexdigest()!=expected_sha256: refuse('input inventory bytes differ')",
'duplicate_source':"        if resolved in seen_paths or pin['sha256'] in seen_digests: refuse('duplicate inventoried source: '+name)",
'unlisted_extra':"    if extras: refuse('unlisted sealed inputs: '+','.join(sorted(extras)))",
'unlisted_request':"    if name not in context['pins']: refuse('requested input is unlisted: '+name)",
}


def new_file(path,content):
    with path.open('x') as stream:stream.write(content)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--only',choices=list(MUTANTS));args=ap.parse_args()
    source=(ROOT/SOURCE).read_text();tests=(ROOT/TESTS).read_text()
    controls=ROOT/'frozen-guard-controls-v1';controls.mkdir(exist_ok=True)
    results=[]
    chosen=[args.only] if args.only else list(MUTANTS)
    for label in chosen:
        anchor=MUTANTS[label];assert source.count(anchor)==1,label
        indent=anchor[:len(anchor)-len(anchor.lstrip())]
        changed=source.replace(anchor,indent+'pass  # exactly one refusal protection removed',1)
        assert changed!=source and changed.count('exactly one refusal protection removed')==1
        case=controls/('mutant-'+label);case.mkdir(exist_ok=False)
        module=case/SOURCE;testfile=case/TESTS
        new_file(module,changed);new_file(testfile,tests)
        env=dict(os.environ,KAC_EXCLUSIVE_ROOT=str(ROOT),KAC_GUARD_MODULE=str(module),KAC_GUARD_CONTROL_ROOT=str(case/'fixtures'))
        run=subprocess.run([sys.executable,str(testfile)],cwd=case,env=env,capture_output=True,text=True,timeout=120)
        new_file(case/'stdout.txt',run.stdout);new_file(case/'stderr.txt',run.stderr)
        exercised='Ran 11 tests' in run.stderr
        status='KILLED' if exercised and run.returncode!=0 else 'SURVIVED' if exercised else 'INCONCLUSIVE_SETUP_OR_IMPORT'
        results.append({'mutant':label,'removed_anchor':anchor,'exactly_one_protection_removed':True,
            'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'mutant_sha256':hashlib.sha256(changed.encode()).hexdigest(),
            'tests_sha256':hashlib.sha256(tests.encode()).hexdigest(),'suite11_tests_actually_ran':exercised,
            'returncode':run.returncode,'status':status,'directory':str(case)})
        print(status,label,'returncode',run.returncode,'suite_ran',exercised,flush=True)
    record={'owner':'MathKacMoody-2','source':{'file':SOURCE,'sha256':hashlib.sha256(source.encode()).hexdigest()},
        'tests':{'file':TESTS,'sha256':hashlib.sha256(tests.encode()).hexdigest()},'mutants':results,
        'all_killed':all(r['status']=='KILLED' for r in results),
        'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'limits':'Synthetic guard controls only; no actual rank/source/library/scientific adoption. No old filesystem-discovery code existed in this fixed-catalogue analyzer,so there is no invented old-discovery mutant. Unlisted-file and unlisted-copy controls test refusal/no fallback. All fixtures/copies retained;no evidence edited or files deleted.'}
    output=controls/('mutation-results-'+(args.only or 'all')+'-v1.json')
    with output.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    if not record['all_killed']:raise SystemExit('A mutant survived or did not run the suite;add the missing test,do not drop the mutant.')
    print('PASS all single-protection mutants killed',len(results),output,flush=True)


if __name__=='__main__':main()
