#!/usr/bin/env python3
"""Bind the exercised certificates, sources, code, and reviews to one receipt."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
RUN = '20261014T084950Z_c585326d_3cdc4c499527'


def main():
    verified = json.loads((ROOT/'evidence/verification-n5.json').read_text())
    summary = json.loads((ROOT/'evidence/summary.json').read_text())
    controls = json.loads((ROOT/'evidence/referee-controls.json').read_text())
    assert verified['certified'] and controls['all_passed']
    assert sum(x['classes'] for x in summary['summary'].values()) == 248
    assert sum(x['collection_complete'] for x in summary['summary'].values()) == 243
    excluded = {'evidence/acceptance.json'}
    inputs = {}
    for path in sorted(ROOT.rglob('*')):
        relative = path.relative_to(ROOT).as_posix()
        if not path.is_file() or relative in excluded or relative.startswith('campaigns/'):
            continue
        content = path.read_bytes()
        inputs[relative] = {'sha256':hashlib.sha256(content).hexdigest(), 'bytes':len(content)}
    receipt = {'schema':'vcs-acceptance-1', 'date_pt':'2026-10-14',
               'command':' '.join(sys.argv), 'campaign':RUN,
               'original_problem_solved':False, 'status':'PARTIALLY-SOLVED',
               'basis_scope':'all nonconstant strong structures n=1..5',
               'basis_classes_certified':248, 'collection_classes_all_four_certified':243,
               'collection_scope':'all n<=4 plus 203/208 at n5; maximum alpha for all248',
               'remaining_collection_cases':5, 'novelty_claimed':False,
               'primary_source_numeric_comparisons':len(summary['published_comparisons']),
               'referee':'main correct-with-fixes; collection lemma sound; resolutions recorded',
               'kernel_formalized':False, 'integer_infeasibility_trust':'Z3 exact integer arithmetic',
               'inputs':inputs}
    payload = json.dumps(receipt, indent=2)+'\n'
    (ROOT/'evidence/acceptance.json').write_text(payload)
    (ROOT/'campaigns'/RUN/'acceptance.json').write_text(payload)
    print(json.dumps({k:v for k,v in receipt.items() if k != 'inputs'}, indent=2))
    print(f'Hashed {len(inputs)} files, {sum(x["bytes"] for x in inputs.values())} bytes')


if __name__ == '__main__':
    main()
