#!/usr/bin/env python3
"""Bind both 14-variable exact primals on their shared 11-variable profile.

Pinned independent receipts verify all elemental/copy rows. This checker also
rebuilds the shared profile, all publisher rows, the two cross-independence
families, and the exact published dual.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
R12=('frontier-20261028-crossbranch12-independent-check-result.json','371ed6d0da680cdbacf36704f61f7d1888b800a5489470c9c36512811df9a86e')
C13=('frontier-20261028-crossbranch13-all-cuts-exact-candidate.json','1d7263364c8c543bdd07a4b140c7a7ab2d65753c38506f26c02072fc9bd29703')
R13=('frontier-20261028-crossbranch13-all-cuts-independent-check-result.json','2575991ec2e5fc62fa3b606d5884dddb9d98f1ba270eae6d882cb641ecb4c76c')
FN=('frontier-20261028-separator-primal-independent-result.json','dac76b954fbd166eac73ce461d2bca641420991ebceb721093f49db6df54284d')
AUDITOR=ROOT/'frontier-20261028-gurpinar-certificate-independent.py'
OUT=ROOT/'frontier-20261028-crossbranch-all-cuts-combined-check-result.json'
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


def cross_holds(values,branch):
    def H(labels):return values[tuple(sorted(labels))]
    v=ORIGINAL;u=FIRST;items=sorted(branch)
    for bits in range(1,8):
        t={items[i] for i in range(3) if bits&(1<<i)}
        if H(v|u)+H(v|t)-H(v|u|t)-H(v)!=0:raise ValueError(('CROSS_INDEPENDENCE',bits))


def main():
    base=pin(BASE);c12=pin(C12);r12=pin(R12);c13=pin(C13);r13=pin(R13);fn=pin(FN)
    if not r12['all_checked'] or r12['base_sha256']!=BASE[1] or r12['candidate_sha256']!=C12[1]:raise ValueError('R12')
    if not r13['all_checked'] or r13['base_sha256']!=BASE[1] or r13['candidate_sha256']!=C13[1] or r13['shared_branch1_sha256']!=C12[1]:raise ValueError('R13')
    for name,r,expected in (('12',r12,(372750,899,7,1052)),('13',r13,(372750,1539,7,1491))):
        c=r['exact_checks'];got=(c['elemental_shannon_checks'],c['copy_equalities'],c['cross_branch_independence_equalities'],c['source_tight_rows'])
        if got!=expected or not r['mutation_controls'] or any(x!='rejected' for x in r['mutation_controls'].values()):raise ValueError(('AUDIT',name,got))
    if r13['all_permuted_cross_copy_cuts_checked']!=45360 or Fraction(r13['min_cross_copy_cut'])<0 or r13['cut_receipt_sha256']!='199a7471622c6c3085a669e2b43e7235676e680ee7e8cb3fa8f636449a1aff45':raise ValueError('UNIVERSAL_CUT_AUDIT')
    family=fn['all_disjoint_blocks_all_positive_n']
    if fn['primal_sha256']!=BASE[1] or fn['exact_objective']!='1847/276' or family['disjoint_substitutions_mod_AB_swap']!=13729980 or family['positive_integers_n']!='all, via exact quadratic-minimum check' or family['min_twice_slack_scaled']<0:
        raise ValueError('FN_COVERAGE')
    old={tuple(sorted(e['entropy_variables'])):Fraction(e['value']) for e in base['primal_values']}
    values={k:v for k,v in old.items() if set(k)<=ORIGINAL}
    if len(values)!=1023 or values[tuple(sorted(ORIGINAL))]!=Fraction(1847,276) or any(values[(v,)]!=1 for v in ORIGINAL):raise ValueError('BASE')
    info=[]
    for name,doc,required,allowed,expected in (
        ('cross12',c12,FIRST|SECOND,ORIGINAL|FIRST|SECOND,15360),
        ('cross13_new',c13,THIRD,ORIGINAL|FIRST|THIRD,14336)):
        local={}
        if set(doc['variables'])!=allowed:raise ValueError(('BRANCH_LABELS',name))
        for e in doc['auxiliary_values']:
            k=tuple(sorted(e['entropy_variables']))
            if not set(k)<=allowed or not set(k)&required or k in local:raise ValueError(('AUX_COORDINATE',name))
            local[k]=Fraction(e['value'])
        if len(local)!=expected or any(k in values for k in local):raise ValueError(('AUX_COUNT',name))
        shared=set(local)&set(old)
        info.append({'branch':name,'shared_old_aux_coordinates':len(shared),
                     'different_from_old_partial_values':sum(local[k]!=old[k] for k in shared)})
        values.update(local)
    if len(values)!=30719:raise ValueError('UNION_COORDINATES')
    spec=spec_from_file_location('publisher_audit',AUDITOR);audit=module_from_spec(spec);spec.loader.exec_module(audit)
    data={k:(ROOT/info2[0]).read_bytes() for k,info2 in audit.FILES.items()}
    for k,(_,digest) in audit.FILES.items():audit.pin(k,data[k],digest)
    source=audit.parse_input(data['layout'],data['text']);dual=audit.validate(source)
    allowed=[ORIGINAL|FIRST|SECOND,ORIGINAL|FIRST|THIRD]
    if any(not any({v for names in row['terms'] for v in names}<=A for A in allowed) for row in source):raise ValueError('SOURCE_ROW_OUTSIDE_SETS')
    source_holds(values,source);cross_holds(values,SECOND);cross_holds(values,THIRD)
    controls={}
    def bad_source(name,key):
        changed=dict(values);changed[key]+=Fraction(1,7)
        try:source_holds(changed,source)
        except ValueError:controls[name]='rejected'
        else:raise ValueError(('SOURCE_CONTROL_ACCEPTED',name))
    bad_source('changed_original_joint',tuple(sorted(ORIGINAL)))
    for name,branch in (('cross12',SECOND),('cross13',THIRD)):
        key=tuple(sorted(ORIGINAL|FIRST|{sorted(branch)[0]}));changed=dict(values);changed[key]+=Fraction(1,7)
        try:cross_holds(changed,branch)
        except ValueError:controls['changed_'+name+'_only_coordinate']='rejected'
        else:raise ValueError(('CROSS_CONTROL_ACCEPTED',name))
    out={'base_sha256':BASE[1],'cross12_candidate_sha256':C12[1],'cross12_independent_receipt':R12[1],
         'cross13_candidate_sha256':C13[1],'cross13_independent_receipt':R13[1],
         'shared_first_copy_profile_coordinates':2047,'all_order_base_family_receipt':FN[1],
         'nonempty_LP_coordinates':len(values),'elemental_shannon_checks':[372750,372750],
         'copy_equalities_per_system':[899,1539],'overlap_first_copy_equalities':257,
         'cross_independence_equalities':[7,7],'universal_gluing_inequalities_checked':45360,'min_universal_gluing_slack':r13['min_cross_copy_cut'],'source_rows_all_tight':len(source),
         'source_dual_exact':dual,'primal_objective':'1847/276','base_entropy_balance_gap':'7/276',
         'all_order_disjoint_substitutions':13729980,'all_order_positive_integers_n':'all',
         'old_partial_auxiliary_scope':info,'mutation_controls':controls,
         'limits':'Exact optimum after all Shannon rows on branch1+2 and branch1+3, their conditional independence from branch1 given originals, and all 45,360 permutations of one unconditional gluing inequality across singleton auxiliary pairs. Cross rows mixing branches 2 and 3, all-17-variable Shannon, and entropic realization remain unproved.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
