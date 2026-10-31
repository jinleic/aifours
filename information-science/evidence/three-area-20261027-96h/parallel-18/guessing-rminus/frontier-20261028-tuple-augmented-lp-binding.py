#!/usr/bin/env python3
"""Bind nine cross-pair systems and one tuple/single system to the verified star.

Two pair systems are projections of the independently checked tuple system;
all other pair systems and the star remain fixed. No 17-variable claim.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
E110=('frontier-20261028-full-source-lp-optimum-v1-erratum-1.md','c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9')
L3E=('frontier-20261028-third-cross-cut-independent-label-erratum-v1.json','e6b01fe0362c99ad0a35dff4aea4a16bda7f0586a38144d1110c152913f7ed7a')
CORE=('frontier-20261028-threefamily-extended-binding-result.json','0e7fc001ab106169e0ef60cd080abafc50ed840a9eb0dc531a8e5179e321a9c6')
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
PAIRS=('frontier-20261028-crossbranch23-pairs-round4-independent-result.json','143db08d3ce5caf8e2f764473d0eb2fe5ce4f14a760e95df33b47903a4fc4540')
TUPLE=('frontier-20261028-cross-tuple-freepairs-candidate.json','fc0e45092f735a8d17a7b7b0363b04b716e0a48c70c6a3a9f32d09855d2e76ec')
TREC=('frontier-20261028-cross-tuple-freepairs-independent-result.json','ced2fff5c556165aeb2cb42b1e13291e4c08025f47dfc72002edcfb93a781c87')
AUDITOR=ROOT/'frontier-20261028-gurpinar-certificate-independent.py'
OUT=ROOT/'frontier-20261028-tuple-augmented-lp-binding-result.json'
ORIGINAL=set('abcdefghij');FIRST={"b'0"};SECOND={"d'1","e'1","g'2"};THIRD={"f'3","g'3","h'4"}


def pin(item,as_json=True):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw) if as_json else raw.decode('utf-8')


def source_holds(values,source):
    for row in source:
        try:value=sum(Fraction(c)*values[tuple(sorted(names))] for names,c in row['terms'].items())
        except KeyError as exc:raise ValueError(('MISSING_SOURCE',row['name'])) from exc
        if value!=row['rhs']:raise ValueError(('SOURCE_NOT_TIGHT',row['name']))


def pair_holds(values,a,b):
    def H(s):return values[tuple(sorted(s))]
    if H(ORIGINAL|{a})+H(ORIGINAL|{b})-H(ORIGINAL|{a,b})-H(ORIGINAL)!=0:raise ValueError(('PAIR_INDEPENDENCE',a,b))


def main():
    # Read binding errata before affected source receipts.
    err=pin(E110,False);label=pin(L3E)
    if 'REQUIRED BEFORE SOURCE' not in err or label['status']!='ADDITIVE REQUIRED BEFORE SOURCE':raise ValueError('ERRATA')
    core=pin(CORE);base=pin(BASE);c12=pin(C12);c13=pin(C13);pairs=pin(PAIRS);tup=pin(TUPLE);tr=pin(TREC)
    if not tr['all_checked'] or tr['candidate_sha256']!=TUPLE[1] or tr['base_sha256']!=BASE[1] or tr['cross12_sha256']!=C12[1] or tr['cross13_sha256']!=C13[1] or tr['exact_checks']['elemental_shannon_checks']!=159757 or tr['exact_checks']['tuple_independence']!=1 or tr['exact_checks']['implied_pair_independences']!=2 or any(v!='rejected' for v in tr['mutation_controls'].values()):raise ValueError('TUPLE_RECEIPT')
    if not core['all_bound'] or core['base_sha256']!=BASE[1] or core['cross12_sha256']!=C12[1] or core['cross13_sha256']!=C13[1] or core['optimum']!='1847/276':raise ValueError('CORE')
    if not pairs['all_nine_checked'] or pairs['base_sha256']!=BASE[1] or pairs['cross12_sha256']!=C12[1] or pairs['cross13_sha256']!=C13[1] or pairs['total_elemental_shannon_checks']!=608364 or pairs['total_conditional_independence_equalities']!=9:raise ValueError('PAIR_RECEIPT')
    old={tuple(sorted(e['entropy_variables'])):Fraction(e['value']) for e in base['primal_values']}
    values={k:v for k,v in old.items() if set(k)<=ORIGINAL}
    if len(values)!=1023 or values[tuple(sorted(ORIGINAL))]!=Fraction(1847,276):raise ValueError('BASE')
    for doc,required,allowed,expected in ((c12,FIRST|SECOND,ORIGINAL|FIRST|SECOND,15360),
                                           (c13,THIRD,ORIGINAL|FIRST|THIRD,14336)):
        local={}
        for e in doc['auxiliary_values']:
            k=tuple(sorted(e['entropy_variables']))
            if not set(k)<=allowed or not set(k)&required or k in local:raise ValueError('STAR_COORDINATE')
            local[k]=Fraction(e['value'])
        if len(local)!=expected or any(k in values for k in local):raise ValueError('STAR_COUNT')
        values.update(local)
    if len(values)!=30719:raise ValueError('STAR_UNION')
    expectedpairs={(a,b) for a in SECOND for b in THIRD};seen=set();pairfiles=[]
    for record in pairs['pairs']:
        a,b=record['pair'];pair=(a,b)
        if pair not in expectedpairs or pair in seen or record['exact_checks']['elemental_shannon_checks']!=67596 or record['exact_checks']['independence_equalities']!=1 or any(x!='rejected' for x in record['mutation_controls'].values()):raise ValueError('PAIR_AUDIT')
        seen.add(pair)
        if pair in {("d'1","f'3"),("g'2","f'3")}:continue
        item=(record['candidate_file'],record['candidate_sha256']);doc=pin(item)
        if tuple(doc['pair'])!=pair:raise ValueError('PAIR_LABEL')
        local={}
        for e in doc['cross_values']:
            k=tuple(sorted(e['entropy_variables']))
            if not {a,b}<=set(k) or not set(k)<=ORIGINAL|{a,b} or k in local:raise ValueError('PAIR_COORDINATE')
            local[k]=Fraction(e['value'])
        if len(local)!=1024 or any(k in values for k in local):raise ValueError('PAIR_COUNT')
        values.update(local);pairfiles.append({'pair':[a,b],'candidate_sha256':item[1]})
    if seen!=expectedpairs or len(values)!=37887:raise ValueError('PAIR_UNION')
    if tuple(tup['variables'])!=tuple('abcdefghij')+("d'1","g'2","f'3"):raise ValueError('TUPLE_LABEL')
    local={}
    for e in tup['cross_values']:
        k=tuple(sorted(e['entropy_variables']));s=set(k)
        if not s<=ORIGINAL|{"d'1","g'2","f'3"} or "f'3" not in s or not s&{"d'1","g'2"} or k in local:raise ValueError('TUPLE_COORDINATE')
        local[k]=Fraction(e['value'])
    if len(local)!=3072 or any(k in values for k in local):raise ValueError('TUPLE_UNION')
    values.update(local)
    if len(values)!=40959:raise ValueError('UNION_COORDINATES')
    for a,b in expectedpairs:pair_holds(values,a,b)
    def tuple_holds(vals):
        def H(s):return vals[tuple(sorted(s))]
        if H(ORIGINAL|{"d'1","g'2"})+H(ORIGINAL|{"f'3"})-H(ORIGINAL|{"d'1","g'2","f'3"})-H(ORIGINAL)!=0:raise ValueError('TUPLE_INDEPENDENCE')
    tuple_holds(values)
    spec=spec_from_file_location('publisher_audit',AUDITOR);audit=module_from_spec(spec);spec.loader.exec_module(audit)
    data={k:(ROOT/info[0]).read_bytes() for k,info in audit.FILES.items()}
    for k,(_,digest) in audit.FILES.items():audit.pin(k,data[k],digest)
    source=audit.parse_input(data['layout'],data['text']);dual=audit.validate(source);source_holds(values,source)
    controls={};changed=dict(values);changed[tuple(sorted(ORIGINAL|{"d'1","g'2","f'3"}))]+=Fraction(1,7)
    try:tuple_holds(changed)
    except ValueError:controls['changed_tuple_joint']='rejected'
    else:raise ValueError('CONTROL_ACCEPTED')
    changed=dict(values);changed[tuple(sorted(ORIGINAL|{"d'1","f'3"}))]+=Fraction(1,7)
    try:pair_holds(changed,"d'1","f'3")
    except ValueError:controls['changed_pair_joint']='rejected'
    else:raise ValueError('CONTROL_ACCEPTED')
    changed=dict(values);changed[tuple(sorted(ORIGINAL))]+=Fraction(1,7)
    try:source_holds(changed,source)
    except ValueError:controls['changed_original_joint']='rejected'
    else:raise ValueError('CONTROL_ACCEPTED')
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],
         'extended_star_receipt':CORE[1],'pair_independent_receipt':PAIRS[1],'unchanged_pair_candidates':pairfiles,'tuple_candidate_sha256':TUPLE[1],'tuple_independent_receipt':TREC[1],
         'f110_pre_source_erratum':E110[1],'third_scan_label_erratum':L3E[1],
         'nonempty_LP_coordinates':len(values),'star_elemental_checks':745500,'old_pair_checks_bound':7*67596,'two_pair_systems_are_tuple_projections':2,'tuple_elemental_checks':159757,
         'source_copy_equalities':2181,'star_cross_independence_equalities':14,'pair_independence_equalities':9,'tuple_independence_equalities':1,
         'source_rows_tight':len(source),'source_dual_exact':dual,'primal_objective':'1847/276',
         'extended_named_cut_families_bound_by':CORE[1],'mutation_controls':controls,
         'limits':'Exact optimum only for the named star+9 pair+one 13-variable tuple systems and previously enumerated cuts. Full 17-variable extension, all other inequalities and actual entropy realizability remain unproved.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='unchanged_pair_candidates'},indent=2))


if __name__=='__main__':main()
