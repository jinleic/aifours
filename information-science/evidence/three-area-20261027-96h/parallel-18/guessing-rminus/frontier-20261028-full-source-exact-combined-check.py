#!/usr/bin/env python3
"""Bind three independently verified branches to the exact publisher dual.

Checks every one of 1,920 publisher rows on the common exact original profile,
revalidates the pinned dual, and binds the all-order base-family receipt. The
branch elemental/copy audits are separate pinned verifier receipts.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
CANDS={1:('frontier-20261028-affine-exact-branch-1.json','1898339bb4ba63c53dbda6dff9603f82414f29645543631bc21d82d752941e37'),
       2:('frontier-20261028-affine-exact-branch-2.json','09981982317f1659a9a291dbbc416f77d2ac8a91eac818191048cb0ac9cd7a87'),
       3:('frontier-20261028-affine-exact-branch-3.json','fd53af75dfa47e9eb03af60fb9704d89719ba8720ddf6aeb192533bcb44c4cd0')}
R1=('frontier-20261028-branch1-exact-independent-check-result.json','a6c8e46fb679a8638d31cb6d76b6ef091aca89c5147bf84ee77fe5893261204e')
R23=('frontier-20261028-branch23-exact-independent-check-result.json','24632017c2defe3aea5debb8f4a1b8541bbe38a87804ce3e1d708bed31373ea2')
FN=('frontier-20261028-separator-primal-independent-result.json','dac76b954fbd166eac73ce461d2bca641420991ebceb721093f49db6df54284d')
AUDITOR=ROOT/'frontier-20261028-gurpinar-certificate-independent.py'
OUT=ROOT/'frontier-20261028-full-source-exact-combined-check-result.json'
ORIGINAL=set('abcdefghij')
AUX={1:{"b'0"},2:{"d'1","e'1","g'2"},3:{"f'3","g'3","h'4"}}


def pin(item):
    path=ROOT/item[0];raw=path.read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def source_rows_hold(values,source):
    for row in source:
        try:value=sum(Fraction(c)*values[tuple(sorted(names))] for names,c in row['terms'].items())
        except KeyError as exc:raise ValueError(('MISSING_SOURCE_COORDINATE',row['name'])) from exc
        if value!=row['rhs']:raise ValueError(('SOURCE_NOT_TIGHT',row['name']))


def main():
    base=pin(BASE);r1=pin(R1);r23=pin(R23);fn=pin(FN)
    if r1['base_sha256']!=BASE[1] or not r1['all_checked'] or r1['candidate_sha256']!=CANDS[1][1]:raise ValueError('BRANCH1_RECEIPT')
    if r23['base_sha256']!=BASE[1] or not r23['all_checked'] or {r['branch']:r['candidate_sha256'] for r in r23['branches']}!={2:CANDS[2][1],3:CANDS[3][1]}:
        raise ValueError('BRANCH23_RECEIPT')
    expected={1:(28171,257,623),2:(159757,642,933),3:(159757,1282,1372)}
    for n,r in [(1,r1)]+[(r['branch'],r) for r in r23['branches']]:
        checks=r['exact_checks'];observed=(checks['elemental_shannon_checks'],checks['copy_equalities'],checks['source_tight_rows'])
        if observed!=expected[n] or not r['mutation_controls'] or any(x!='rejected' for x in r['mutation_controls'].values()):
            raise ValueError(('BRANCH_AUDIT_COUNTS_OR_CONTROLS',n,observed))
    if fn['primal_sha256']!=BASE[1] or fn['exact_objective']!='1847/276':raise ValueError('FN_BASE')
    allorder=fn['all_disjoint_blocks_all_positive_n']
    if allorder['disjoint_substitutions_mod_AB_swap']!=13729980 or allorder['positive_integers_n']!='all, via exact quadratic-minimum check' or allorder['min_twice_slack_scaled']<0:
        raise ValueError('FN_COVERAGE')
    old={tuple(sorted(e['entropy_variables'])):Fraction(e['value']) for e in base['primal_values']}
    values={k:v for k,v in old.items() if set(k)<=ORIGINAL}
    if len(values)!=1023 or values[tuple(sorted(ORIGINAL))]!=Fraction(1847,276):raise ValueError('BASE_PROFILE')
    if any(values[(v,)]!=1 for v in ORIGINAL):raise ValueError('BASE_CAPS')
    old_differences={};branches={}
    for number,item in CANDS.items():
        doc=pin(item);allowed=ORIGINAL|AUX[number]
        if doc['branch']!=number or set(doc['variables'])!=allowed:raise ValueError('BRANCH_LABELS')
        local={}
        for e in doc['auxiliary_values']:
            k=tuple(sorted(e['entropy_variables']))
            if not set(k)<=allowed or not set(k)&AUX[number] or k in local:raise ValueError('AUX_COORDINATE')
            local[k]=Fraction(e['value'])
        if len(local)!={1:1024,2:7168,3:7168}[number] or any(k in values for k in local):raise ValueError('AUX_COUNT')
        shared=set(local)&set(old);old_differences[str(number)]={'shared_old_aux_coordinates':len(shared),
              'different_from_old_partial_values':sum(local[k]!=old[k] for k in shared)}
        values.update(local);branches[number]=allowed
    if len(values)!=16383:raise ValueError('UNION_COORDINATES')
    spec=spec_from_file_location('publisher_audit',AUDITOR);audit=module_from_spec(spec);spec.loader.exec_module(audit)
    data={k:(ROOT/info[0]).read_bytes() for k,info in audit.FILES.items()}
    for k,(_,digest) in audit.FILES.items():audit.pin(k,data[k],digest)
    source=audit.parse_input(data['layout'],data['text']);dual=audit.validate(source)
    cross=[r['name'] for r in source if not any({v for names in r['terms'] for v in names}<=vs for vs in branches.values())]
    if cross:raise ValueError(('SOURCE_ROW_OUTSIDE_BRANCHES',cross))
    source_rows_hold(values,source)
    controls={}
    def expect(name,key):
        changed=dict(values);changed[key]+=Fraction(1,7)
        try:source_rows_hold(changed,source)
        except ValueError:controls[name]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',name,key))
    expect('changed_original_joint',tuple(sorted(ORIGINAL)))
    for number in (1,2,3):
        k=next(tuple(sorted(names)) for row in source for names in row['terms']
               if set(names)&AUX[number] and {v for z in row['terms'] for v in z}<=branches[number])
        expect('changed_branch_'+str(number),k)
    out={'base_sha256':BASE[1],'branch_candidate_sha256':{str(n):x[1] for n,x in CANDS.items()},
         'branch1_verifier_receipt':R1[1],'branch23_verifier_receipt':R23[1],
         'all_order_base_family_receipt':FN[1],'original_entropy_coordinates':1023,
         'distinct_nonempty_source_LP_coordinates':len(values),
         'branch_elemental_shannon_checks':[28171,159757,159757],
         'branch_copy_equalities':[257,642,1282],'original_FDs':10,'original_singletons':10,
         'source_rows_all_tight':len(source),'source_rows_outside_branch_sets':len(cross),
         'source_dual_exact':dual,'primal_objective':'1847/276','all_singletons':'1',
         'base_entropy_balance_gap':'7/276',
         'all_order_disjoint_substitutions':13729980,'all_order_positive_integers_n':'all',
         'old_partial_auxiliary_scope':old_differences,'mutation_controls':controls,
         'limits':'Exact optimum for the published three-branch LP and its augmentation by the stated disjoint original-variable F_n family. Cross-branch Shannon/copy constraints, other families and entropic realization are NOT established.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
