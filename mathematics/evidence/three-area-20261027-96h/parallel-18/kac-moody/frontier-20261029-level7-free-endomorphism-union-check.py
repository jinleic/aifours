#!/usr/bin/env python3
"""Complete19-representative/31-oriented free level7 certificate union check.

Checks every polynomial coefficient (not a metadata count), degree bound,
positive constant, whole pencil shape, source/operand fingerprints, completed
source/matrix replay bindings and exhaustive free character cover. Does NOT
rerun any determinant or establish the actual Kac-Moody source interface.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

SCRIPT_ROOT=Path(__file__).resolve().parent
ROOT=SCRIPT_ROOT
sys.path.insert(0,str(SCRIPT_ROOT/'frontier-20261028-fastalgebra'))
import flint
GUARD='frontier-20261029-frozen-input-guard.py'
GUARD_SHA='0cceb1807a030687a2a1da0fe1daba28d56674b70e8e399ff5badf0e4a9ff6b1'
_guard_raw=(SCRIPT_ROOT/GUARD).read_bytes()
if hashlib.sha256(_guard_raw).hexdigest()!=GUARD_SHA:raise SystemExit('frozen input guard bytes differ')
_spec=importlib.util.spec_from_file_location('strict_frozen_input_guard',SCRIPT_ROOT/GUARD)
guard=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(guard)
CONTEXT=None
CENSUS='frontier-20261029-level7-exhaustive-lowest-character-census-v1.json'
CENSUS_SHA='18dc3d0812ae004f6babf424a200b4b5a1bcd03e9f8e44c881266b65a33a0336'
F173='frontier-20261029-f173-conditional-scope-and-conventions-addendum-v1.json'
F173_SHA='87ba070ce17ffb2c381e2734be8513b3997e8c2965d555d31fc9c484c945aafa'
LABELS=('10','20','30','11','21','31','41','22','32','24','33','43','53','44','54','55','65','66','77')
GENERAL={'44','54','55','65','66'}


def blob(name):
    return guard.input_bytes(CONTEXT,name)


def document(name):
    raw=blob(name)
    return json.loads(raw),{'file':name,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}


def main():
    global ROOT,CONTEXT
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--evidence-root',default=str(SCRIPT_ROOT/'frontier-20261029-level7-free19-sealed-inputs-v1'))
    ap.add_argument('--inventory',default='frontier-20261029-level7-free19-input-inventory-v1.json')
    ap.add_argument('--inventory-sha256',default='88971535369069479adfbfd1cb1e6a3996f06f598b779777bb73624a87459ab0')
    ap.add_argument('--output',default=str(SCRIPT_ROOT/'frontier-20261029-level7-nineteen-free-endomorphism-union-check-v1.json'))
    args=ap.parse_args();ROOT=Path(args.evidence_root).resolve()
    CONTEXT=guard.verify_inventory(ROOT,args.inventory,args.inventory_sha256)
    assert flint.__version__=='0.9.0'
    census,cp=document(CENSUS);assert cp['sha256']==CENSUS_SHA
    correction,fp=document(F173);assert fp['sha256']==F173_SHA
    assert correction['kind']=='MANDATORY_ADDITIVE_F173_SCOPE_AND_NOTATION_QUALIFICATION'
    roster={tuple(row['lowest_degree']):row for row in census['rows']}
    assert len(roster)==31 and sum(r['isotypic_dimension'] for r in roster.values())==299592
    assert len(LABELS)==len(set(LABELS))==19
    components=[];covered=set();all_inputs={CENSUS:cp,F173:fp};positive=0
    for label in LABELS:
        degree=(int(label[0]),int(label[1]),7)
        dname=f'frontier-20261029-level7-{label}-canonical-determinant-v1.json' if label!='77' else 'frontier-20261029-level7-trace-dynkin-canonical-determinant-v1.json'
        D,dp=document(dname);P,pp=document(D['pencil'])
        assert D['pencil_sha256']==pp['sha256'] and D['degree']==P['degree']==list(degree)
        assert D['variables'].replace(' ','')=='x=r-7,y=s-7'
        assert P['variable_meaning'].replace(' ','')=='x=r-7,y=s-7'
        k=D['size'];assert k==P['entire_primitive_dimension']==roster[degree]['entire_free_lowest_multiplicity']
        assert D['entire_source_endomorphism'] is True
        assert len(P['matrix'])==k and all(len(row)==k and all(len(e)==3 for e in row) for row in P['matrix'])
        S,sp=document(P['source_pencil']);assert sp['sha256']==P['source_pencil_sha256']
        seen=set();constant=Q(0)
        for term in D['coefficients']:
            a,b=term['x_power'],term['y_power']
            assert type(a) is int and type(b) is int and min(a,b)>=0 and a+b<=k
            assert (a,b) not in seen;seen.add((a,b))
            value=Q(term['coefficient']);assert value>0
            if a==b==0:constant=value
        assert constant>0
        if 'positive_coefficients' in D:assert D['positive_coefficients']==len(seen)
        if 'negative_coefficients' in D:assert D['negative_coefficients']==0
        assert Q(D['constant_coefficient'])==constant
        if label=='77':
            rname='frontier-20261029-level7-trace-invariant-left-replay-v1.json'
            R,rp=document(rname)
            assert R['status']=='PASS_ALTERNATE_ENTIRE_INVARIANT_MATRIX_AND_HALF_LEVEL_POLYNOMIAL'
            assert R['canonical_pencil_sha256']==pp['sha256'] and R['source_input_sha256']==sp['sha256']
            assert R['entire_invariant_dimension']==k and R['all3_entire_word_reconstructions'] is True
            assert R['all_affine_coefficients_match_right_transport_pencil'] is True
            SR,srp=document(R['source_replay']['file']);assert srp['sha256']==R['source_replay']['sha256']
            assert SR['status']=='PASS_LITERAL_ENTIRE_INVARIANT_SOURCE_AND_BYTE_SEED_REPLAY'
            assert SR['input_sha256']==sp['sha256'];all_inputs[srp['file']]=srp
            hname='frontier-20261029-level7-trace-invariant-half-level-polynomial-v1.json'
            H,hp=document(hname)
            assert hp['sha256']==R['half_level_polynomial_sha256']
            assert H['original_polynomial']=={'file':dp['file'],'sha256':dp['sha256']}
            all_inputs[hp['file']]=hp
            replay_scope='literal source/NPY seed replay plus LEFT matrices and5151 shifted matrix determinants'
        elif label in GENERAL:
            version='v2' if label=='55' else 'v1'
            rname=f'frontier-20261029-level7-{label}-general-left-replay-{version}.json'
            R,rp=document(rname)
            assert R['status']=='PASS_ALTERNATE_WHOLE_SOURCE_AND_LEFT_CANONICAL_PENCIL'
            assert R['pencil']=={'file':pp['file'],'sha256':pp['sha256']}
            assert R['source']=={'file':sp['file'],'sha256':sp['sha256']}
            assert R['entire_lowest_dimension']==k and R['all_vectors_Dynkin_Lie_membership'] is True
            assert R['all_vectors_literal_lowest'] is True and R['detector_minor_nonzero'] is True
            assert R['independent_Witt_Weyl_completeness']==k
            assert R['every_canonical_matrix_entry_reproduced']==3*k*k
            assert len(R['all3_entire_word_reconstructions'])==3 and all(n>0 for n in R['all3_entire_word_reconstructions'])
            assert len(D['multimodular_sources'])==2
            exact,ep=document(D['multimodular_sources'][0]['file']);residue,vp=document(D['multimodular_sources'][1]['file'])
            assert ep['sha256']==D['multimodular_sources'][0]['sha256'] and vp['sha256']==D['multimodular_sources'][1]['sha256']
            assert exact['status']=='EXACT_MULTIMODULAR_PENCIL_DETERMINANT'
            assert residue['status']=='PASS_DISJOINT_PRIME_OPPOSITE_ORIENTATION_RESIDUE_REPLAY'
            assert residue['verified_table']=={'file':ep['file'],'sha256':ep['sha256']}
            assert exact['pencil']==residue['pencil']=={'file':pp['file'],'sha256':pp['sha256']}
            assert exact['orientation']!=residue['orientation'] and not set(exact['primes'])&set(residue['disjoint_primes'])
            assert exact['nonzero_coefficients']==exact['positive']==len(seen) and exact['negative']==0
            scales=list(map(int,exact['row_scales']))
            assert len(scales)==k and all(s>0 for s in scales)
            column_energy=[[0,0,0] for _ in range(k)];row_bound=1
            for i,row in enumerate(P['matrix']):
                qrow=[[Q(v) for v in e] for e in row]
                assert scales[i]==math.lcm(*(v.denominator for e in qrow for v in e))
                energy=[0,0,0]
                for j,e in enumerate(qrow):
                    values=[int(v*scales[i]) for v in e]
                    if exact.get('shear'):values[1]+=values[2]
                    for t,v in enumerate(values):
                        energy[t]+=v*v;column_energy[j][t]+=v*v
                row_bound*=sum(math.isqrt(v)+1 for v in energy)
            column_bound=math.prod(sum(math.isqrt(v)+1 for v in energy) for energy in column_energy)
            bound=min(row_bound,column_bound)
            assert bound.bit_length()==exact['hadamard_bound_bits']
            primes=list(map(int,exact['primes']));replay_primes=list(map(int,residue['disjoint_primes']))
            assert len(primes)==len(set(primes))==exact['prime_count']
            assert len(replay_primes)==len(set(replay_primes))==12
            assert not set(primes)&set(replay_primes)
            assert all(p>4*k+40 and flint.fmpz(p).is_prime() for p in primes+replay_primes)
            assert math.prod(primes)>2*bound+1
            table_pin=exact['coefficient_file'];compressed=blob(table_pin['file'])
            assert hashlib.sha256(compressed).hexdigest()==table_pin['sha256']
            serial=gzip.decompress(compressed)
            assert hashlib.sha256(serial).hexdigest()==table_pin['uncompressed_serialization_sha256']
            canonical={(e['x_power'],e['y_power']):e['coefficient'] for e in D['coefficients']}
            scale=math.prod(scales);matched=set()
            for a,b,c in json.loads(serial):
                assert type(a) is int and type(b) is int and min(a,b)>=0 and a+b<=k
                assert (a,b) not in matched;matched.add((a,b))
                assert Q(int(c),scale)==Q(canonical[a,b])
            assert matched==seen
            all_inputs[table_pin['file']]={'file':table_pin['file'],'sha256':table_pin['sha256'],'bytes':len(compressed)}
            all_inputs[ep['file']]=ep;all_inputs[vp['file']]=vp
            del canonical,compressed,serial,matched
            replay_scope='literal whole source/LEFT matrices plus exact bounded-CRT determinant and12 disjoint opposite-orientation residue tables'
        else:
            rname=f'frontier-20261029-level7-{label}-canonical-independent-replay-v1.json'
            R,rp=document(rname)
            assert R['status']=='PASS_ENTIRE_CANONICAL_SOURCE_MATRIX_AND_WHOLE_QUADRANT_POLYNOMIAL'
            assert R['source_pencil_sha256']==sp['sha256'] and R['canonical_pencil_sha256']==pp['sha256']
            assert R['canonical_polynomial_sha256']==dp['sha256']
            assert R['entire_source_dimension']==k and R['all_free_source_membership_and_Witt_completeness_checked'] is True
            assert R['all_three_entire_canonical_coordinate_matrix_products_checked'] is True
            assert R['all_affine_matrix_entries_match'] is True and R['all_coefficients_one_sign_and_constant_nonzero'] is True
            assert R['polynomial_terms']==len(seen)
            assert R['shifted_unisolvent_determinants']==(k+1)*(k+2)//2
            replay_scope='entire literal source/three matrices plus complete shifted exact determinant triangle'
        transpose=(degree[1],degree[0],7)
        assert transpose in roster and roster[transpose]['entire_free_lowest_multiplicity']==k
        covered.update((degree,transpose));positive+=len(seen)
        for pin in (dp,pp,sp,rp):all_inputs[pin['file']]=pin
        components.append({'label':label,'degree':list(degree),'transpose':list(transpose),'entire_lowest_dimension':k,
            'positive_polynomial_terms_physically_parsed':len(seen),'positive_constant':str(constant),
            'degree_bound':k,'source':sp,'pencil':pp,'polynomial':dp,'completed_replay':rp,'replay_scope':replay_scope})
        print('PASS entire free component',degree,'lowest',k,'positive terms',len(seen),flush=True)
        del D,P,S,R
    assert covered==set(roster)
    result={'owner':'MathKacMoody-2','kind':'COMPLETE_FREE_19_COMPONENT_31_TYPE_UNION_CHECK_NOT_ACTUAL_SOURCE_ADOPTION',
        'census':cp,'f173_scope_qualification':fp,'representatives':19,'oriented_types':31,'full_free_level_dimension':299592,
        'source_lowest_multiplicity_sum':5901,'all_positive_polynomial_terms':positive,'matrix_variable_origin':'x=r-7,y=s-7',
        'actual_parameter_scope_if_source_and_canonical_interfaces_hold':'integer r,s>=7 only;no low-parameter result is inferred by this record',
        'components':components,'bound_json_inputs':list(all_inputs.values()),'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_inventory':{'file':args.inventory,'sha256':args.inventory_sha256},
        'sealed_evidence_root':str(ROOT),'all_inventoried_inputs_verified':len(CONTEXT['pins']),
        'frozen_input_guard':{'file':GUARD,'sha256':GUARD_SHA},'flint_version':flint.__version__,
        'large_polynomial_canonical_conversion_and_exact_CRT_bounds_and_prime_lists_rechecked':True,
        'status':'PASS_EXHAUSTIVE_19_FREE_ENDOMORPHISMS_31_ORIENTED_TYPES',
        'limits':'Every coefficient/sign/degree/metadata operand/replay/roster binding was checked,not rerun determinants or actual source proofs. Actual-source/seed/PBW/canonical and numerical scientific adoption remain UNREVIEWED. f173 conditional finite-Levi support is not transferred. Same-owner/shared FLINT;no parent/formal/kernel/configured-family/human/native-library/global-status/novelty acceptance.'}
    name=Path(args.output)
    with name.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS COMPLETE FREE UNION',19,31,'positive coefficients',positive,str(name),flush=True)


if __name__=='__main__':main()
