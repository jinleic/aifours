#!/usr/bin/env python3
"""Bind the full 14-variable cross-branch primal to source branch 3 and dual.

Per-branch elemental/copy checks are supplied by pinned independent verifier
receipts; this checker independently merges coordinates, verifies all source
rows and the seven cross-independence equalities, and revalidates the dual.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
CROSS=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
CROSS_R=('frontier-20261028-crossbranch12-independent-check-result.json','371ed6d0da680cdbacf36704f61f7d1888b800a5489470c9c36512811df9a86e')
B3=('frontier-20261028-affine-exact-branch-3.json','fd53af75dfa47e9eb03af60fb9704d89719ba8720ddf6aeb192533bcb44c4cd0')
B23_R=('frontier-20261028-branch23-exact-independent-check-result.json','24632017c2defe3aea5debb8f4a1b8541bbe38a87804ce3e1d708bed31373ea2')
FN=('frontier-20261028-separator-primal-independent-result.json','dac76b954fbd166eac73ce461d2bca641420991ebceb721093f49db6df54284d')
AUDITOR=ROOT/'frontier-20261028-gurpinar-certificate-independent.py'
OUT=ROOT/'frontier-20261028-crossbranch12-combined-check-result.json'
ORIGINAL=set('abcdefghij');FIRST={"b'0"};SECOND={"d'1","e'1","g'2"};THIRD={"f'3","g'3","h'4"}


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def source_holds(values,source):
    for row in source:
        try:value=sum(Fraction(c)*values[tuple(sorted(names))] for names,c in row['terms'].items())
        except KeyError as exc:raise ValueError(('MISSING_SOURCE_COORDINATE',row['name'])) from exc
        if value!=row['rhs']:raise ValueError(('SOURCE_NOT_TIGHT',row['name']))


def cross_holds(values):
    def H(labels):return values[tuple(sorted(labels))]
    v=ORIGINAL;u=FIRST;items=sorted(SECOND)
    for bits in range(1,8):
        t={items[i] for i in range(3) if bits&(1<<i)}
        if H(v|u)+H(v|t)-H(v|u|t)-H(v)!=0:raise ValueError(('CROSS_INDEPENDENCE',bits))


def main():
    base=pin(BASE);cross=pin(CROSS);r=pin(CROSS_R);b3=pin(B3);r23=pin(B23_R);fn=pin(FN)
    if r['base_sha256']!=BASE[1] or r['candidate_sha256']!=CROSS[1] or not r['all_checked']:
        raise ValueError('CROSS_RECEIPT')
    cc=r['exact_checks']
    if (cc['elemental_shannon_checks'],cc['copy_equalities'],cc['cross_branch_independence_equalities'],cc['source_tight_rows'])!=(372750,899,7,1052):
        raise ValueError('CROSS_COUNTS')
    b3r=next(x for x in r23['branches'] if x['branch']==3)
    if r23['base_sha256']!=BASE[1] or not r23['all_checked'] or b3r['candidate_sha256']!=B3[1]:raise ValueError('B3_RECEIPT')
    bc=b3r['exact_checks']
    if (bc['elemental_shannon_checks'],bc['copy_equalities'],bc['source_tight_rows'])!=(159757,1282,1372):raise ValueError('B3_COUNTS')
    if any(x!='rejected' for x in r['mutation_controls'].values()) or any(x!='rejected' for x in b3r['mutation_controls'].values()):raise ValueError('BRANCH_CONTROLS')
    family=fn['all_disjoint_blocks_all_positive_n']
    if fn['primal_sha256']!=BASE[1] or fn['exact_objective']!='1847/276' or family['disjoint_substitutions_mod_AB_swap']!=13729980 or family['positive_integers_n']!='all, via exact quadratic-minimum check' or family['min_twice_slack_scaled']<0:
        raise ValueError('FN_COVERAGE')
    old={tuple(sorted(e['entropy_variables'])):Fraction(e['value']) for e in base['primal_values']}
    values={k:v for k,v in old.items() if set(k)<=ORIGINAL}
    if len(values)!=1023 or values[tuple(sorted(ORIGINAL))]!=Fraction(1847,276) or any(values[(v,)]!=1 for v in ORIGINAL):raise ValueError('BASE')
    info=[]
    for name,doc,aux,expected in (('cross12',cross,FIRST|SECOND,15360),('branch3',b3,THIRD,7168)):
        allowed=ORIGINAL|aux;local={}
        if set(doc['variables'])!=allowed:raise ValueError('BRANCH_LABELS')
        for e in doc['auxiliary_values']:
            k=tuple(sorted(e['entropy_variables']))
            if not set(k)<=allowed or not set(k)&aux or k in local:raise ValueError('AUX_COORDINATE')
            local[k]=Fraction(e['value'])
        if len(local)!=expected or any(k in values for k in local):raise ValueError('AUX_COUNT')
        shared=set(local)&set(old)
        info.append({'branch':name,'shared_old_aux_coordinates':len(shared),
                     'different_from_old_partial_values':sum(local[k]!=old[k] for k in shared)})
        values.update(local)
    if len(values)!=23551:raise ValueError('UNION_COORDINATES')
    spec=spec_from_file_location('publisher_audit',AUDITOR);audit=module_from_spec(spec);spec.loader.exec_module(audit)
    data={k:(ROOT/info2[0]).read_bytes() for k,info2 in audit.FILES.items()}
    for k,(_,digest) in audit.FILES.items():audit.pin(k,data[k],digest)
    source=audit.parse_input(data['layout'],data['text']);dual=audit.validate(source)
    allowed=[ORIGINAL|FIRST|SECOND,ORIGINAL|THIRD]
    if any(not any({v for names in row['terms'] for v in names}<=A for A in allowed) for row in source):raise ValueError('SOURCE_ROW_OUTSIDE_SETS')
    source_holds(values,source);cross_holds(values)
    controls={}
    def bad_source(name,key):
        changed=dict(values);changed[key]+=Fraction(1,7)
        try:source_holds(changed,source)
        except ValueError:controls[name]='rejected'
        else:raise ValueError(('SOURCE_CONTROL_ACCEPTED',name))
    bad_source('changed_original_joint',tuple(sorted(ORIGINAL)))
    k=next(tuple(sorted(names)) for row in source for names in row['terms'] if set(names)&THIRD)
    bad_source('changed_branch3_coordinate',k)
    key=tuple(sorted(ORIGINAL|FIRST|{sorted(SECOND)[0]}));changed=dict(values);changed[key]+=Fraction(1,7)
    try:cross_holds(changed)
    except ValueError:controls['changed_cross_only_coordinate']='rejected'
    else:raise ValueError('CROSS_CONTROL_ACCEPTED')
    out={'base_sha256':BASE[1],'cross12_candidate_sha256':CROSS[1],'cross12_independent_receipt':CROSS_R[1],
         'branch3_candidate_sha256':B3[1],'branch3_independent_receipt':B23_R[1],
         'all_order_base_family_receipt':FN[1],'nonempty_LP_coordinates':len(values),
         'elemental_shannon_checks':[372750,159757],'copy_equalities':[899,1282],
         'cross_independence_equalities':7,'source_rows_all_tight':len(source),
         'source_dual_exact':dual,'primal_objective':'1847/276','base_entropy_balance_gap':'7/276',
         'all_order_disjoint_substitutions':13729980,'all_order_positive_integers_n':'all',
         'old_partial_auxiliary_scope':info,'mutation_controls':controls,
         'limits':'Exact optimum after all Shannon inequalities between branches 1 and 2 plus their conditional independence given originals, with branch 3 separate and the stated F_n family. Cross constraints involving branch3 or entropic realization remain unproved.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
