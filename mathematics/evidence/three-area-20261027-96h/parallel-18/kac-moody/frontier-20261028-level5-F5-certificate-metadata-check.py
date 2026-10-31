#!/usr/bin/env python3
"""Check exact F5 certificate class sets, polynomial degrees and signs.

Addresses f55-style metadata limitations for the actual F5 input bytes.  This
is NOT a replay of the matrices, a B4 audit, or an independent proof/review.
"""
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SEVEN=('22','32','23','33','43','34','44')


def load(name):return json.loads((ROOT/name).read_text())
def expected_degree(ab):return [int(ab[0]),int(ab[1]),5]


def check_uni(P,polynomial,sign,nonzero,k):
    assert P['joint_horizontal_kernel_dim']==k and len(polynomial)==k+1
    coefficients=[Q(v) for v in polynomial]
    assert sign in (-1,1) and sign*coefficients[0]>0
    assert all(sign*q>=0 for q in coefficients) and sum(bool(q) for q in coefficients)==nonzero
    assert len(P['matrix'])==k and all(len(row)==k for row in P['matrix'])


def check_terms(terms,k,sign):
    seen=set();constant=None
    for a in terms:
        x,y=a['x_power'],a['y_power'];q=Q(a['coefficient'])
        assert type(x)==type(y)==int and x>=0 and y>=0 and x+y<=k
        assert (x,y) not in seen and sign*q>0;seen.add((x,y))
        if (x,y)==(0,0):constant=q
    assert constant is not None and sign*constant>0


def fixed(ab,r,s):
    P=load(f'frontier-20261028-level5-fixed-{ab}-r{r}-s{s}-v1.json')
    R=load(f'frontier-20261028-level5-fixed-{ab}-r{r}-s{s}-independent-replay-v1.json')
    c=P['case'];assert P['degree']==expected_degree(ab) and c['r_class']==r and c['s_class']==s
    assert c['status']=='CERTIFIED_ONE_SIGN' and R['status']=='PASS_FULL_SPAN_TREE_JACOBI_GRID_SIGN'
    assert c['source_dim']==R['source_dim'] and c['horizontal_kernel_dim']==R['horizontal_kernel_dim']
    check_terms(c['determinant_coefficients'],c['horizontal_kernel_dim'],1 if Q(c['determinant_coefficients'][0]['coefficient'])>0 else -1)
    assert len(c['determinant_coefficients'])==1 and c['determinant_coefficients'][0]['x_power']==c['determinant_coefficients'][0]['y_power']==0


def smallrow(ab,r):
    P=load(f'frontier-20261028-level5-r{r}-{ab}-smallrow-pencil-v1.json')
    D=load(f'frontier-20261028-level5-r{r}-{ab}-smallrow-determinant-v1.json')
    assert P['degree']==expected_degree(ab) and P['r']==r and P['s_class']=='>=4';k=P['joint_horizontal_kernel_dim']
    if r==2 and ab=='23':
        A=load(f'frontier-20261028-level5-r{r}-{ab}-smallrow-alternate-v1.json');R=load(f'frontier-20261028-level5-r{r}-{ab}-smallrow-alternate-independent-replay-v1.json')
        assert D['status']=='MIXED_OR_ZERO_CONSTANT' and A['status']=='ONE_SIGN_ALTERNATE' and R['status']=='PASS_ENTIRE_SMALLROW_ALTERNATE_QUOTIENT_POLYNOMIAL'
        alt=A['result'];check_uni({'joint_horizontal_kernel_dim':k,'matrix':alt['matrix']},alt['determinant_coefficients'],alt['sign'],alt['nonzero_coefficient_count'],k)
    else:
        R=load(f'frontier-20261028-level5-r{r}-{ab}-smallrow-independent-replay-v1.json')
        assert D['status']=='ONE_SIGN_ALL_S_GE_4' and R['status']=='PASS_ENTIRE_SMALLROW_QUOTIENT_POLYNOMIAL'
        check_uni(P,D['determinant_coefficients'],D['signs'][0],D['nonzero_coefficient_count'],k)
    assert R['degree']==expected_degree(ab) and R['r']==r and R['joint_horizontal_kernel_dimension']==k


def r3(ab):
    P=load(f'frontier-20261028-level5-r3-{ab}-quotient-pencil-v1.json')
    D=load(f'frontier-20261028-level5-r3-{ab}-quotient-determinant-v1.json')
    assert P['degree']==expected_degree(ab) and P['r']==3 and P['s_class']=='>=4';k=P['joint_horizontal_kernel_dim']
    if ab in ('32','33','44'):
        A=load(f'frontier-20261028-level5-r3-{ab}-alternate-minor-search-v1.json');R=load(f'frontier-20261028-level5-r3-{ab}-quotient-independent-replay-v1.json')
        assert D['status']=='MIXED_OR_ZERO_CONSTANT' and A['status']=='ONE_SIGN_ALTERNATE' and R['status']=='PASS_ENTIRE_R3_QUOTIENT_ALTERNATE_POLYNOMIAL'
        a=A['result'];check_uni({'joint_horizontal_kernel_dim':k,'matrix':a['matrix']},a['determinant_coefficients'],a['sign'],a['nonzero_coefficient_count'],k)
    else:
        R=load(f'frontier-20261028-level5-r3-{ab}-baseline-independent-replay-v1.json')
        assert D['status']=='ONE_SIGN_ALL_S_GE_4' and R['status']=='PASS_ENTIRE_R3_QUOTIENT_BASELINE_POLYNOMIAL'
        check_uni(P,D['determinant_coefficients'],D['signs'][0],D['nonzero_coefficient_count'],k)
    assert R['degree']==expected_degree(ab) and R['r']==3 and R['joint_horizontal_kernel_dimension']==k


def quadrant(ab,label):
    P=load(f'frontier-20261028-level5-free-{ab}-pencil-v1.json');D=load(f'frontier-20261028-level5-free-{ab}-determinant-v1.json')
    assert P['degree']==expected_degree(ab) and P['variables']=='x=r-4,y=s-4';k=P['joint_horizontal_kernel_dim']
    if label:
        A=load(f'frontier-20261028-level5-{label}-alternate-minor-search-v1.json');R=load(f'frontier-20261028-level5-{label}-alternate-independent-replay-v1.json')
        assert D['status']=='MIXED_OR_ZERO_CONSTANT' and A['status']=='ONE_SIGN_ALTERNATE' and R['status']=='PASS_FULL_FREE_TYPE_ALTERNATE_POLYNOMIAL'
        a=A['result'];terms=a['determinant_coefficients'];sign=a['sign'];matrix=a['matrix'];assert a['grid_evaluations']==(k+1)*(k+2)//2
    else:
        R=load('frontier-20261028-level5-free-22-independent-replay-v1.json');assert D['status']=='ONE_SIGN_ALL_ORTHANT' and R['status']=='PASS_FULL_FREE_TYPE_POLYNOMIAL'
        terms=D['determinant_coefficients'];sign=D['signs'][0];matrix=P['matrix'];assert D['evaluations']==(k+1)*(k+2)//2
    assert len(matrix)==k and all(len(row)==k for row in matrix)
    assert R['degree']==expected_degree(ab) and R['joint_horizontal_kernel_dimension']==k
    check_terms(terms,k,sign)


def main():
    out=ROOT/'frontier-20261028-level5-F5-certificate-metadata-check-v1.json'
    if out.exists():raise FileExistsError(out)
    assert len(set(SEVEN))==7
    for ab in SEVEN+('55',):
        smallrow(ab,1)
        for s in (2,3):fixed(ab,1,s)
    for ab in SEVEN:
        smallrow(ab,2);r3(ab);fixed(ab,3,2)
    for ab,label in [('22',None),('32','35'),('33','27'),('43','10'),('44','8')]:quadrant(ab,label)
    I=load('frontier-20261028-invariant5-independent-replay-v1.json')
    assert I['degree']==[5,5,5] and I['horizontal_kernel_dimension']==6 and I['all_coefficients_equal_shifted_producer']
    check_terms(I['determinant_x_r_minus_2_y_s_minus_2'],6,1)
    result={'expected_fixed_degree_set':list(SEVEN),'r1_uniform_cases':8,'r1_fixed_cases':16,
            'r2_uniform_cases':7,'r3_uniform_cases':7,'r3_s2_fixed_cases':7,
            'large_row_representative_cases':5,'large_row_invariant_cases':1,'total_case_count':51,
            'check':'exact named class sets; univariate coefficient list length <=k+1; bivariate unique nonnegative exponents with total degree<=k; strict one-sign/nonzero constant; full matrix shapes; recorded replay statuses',
            'scope':'metadata checking of actual F5 input bytes, not determinant or quotient reconstruction and not an independent review',
            'no_f55_major_resolution_or_B4_adoption':True,'not_formal_or_external_model_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS F5 metadata: 51 named cases, exact class sets, polynomial degree/sign/constants and full matrix shapes;',out.name,flush=True)

if __name__=='__main__':main()
