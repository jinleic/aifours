#!/usr/bin/env python3
"""Independent f151 supplemental exact mathematical controls; stdlib only.

This file does not import/execute any author code or the v1 reviewer checker.
Its resource-free divisor enumerations, support-family enumerations, witness
checks, and deliberate mutations are independently implemented here.

Correction to reviewer-control-v1.py's introductory scope sentence: its
DISTINCT-vertex graph computes a SET relaxation. It models index families
only for lower bound >=8 and gcd cap 7. For mu<=7 repeated indices <=7 are
possible; for gcd cap 8 repeated 8 is possible. The v1 negative-control set
witnesses remain genuine counterexamples, but their finite maxima must not be
called maxima of MULTISET families. V1's mu7 and min_size1 probes are not
sensitive negative controls. This file preserves v1 and records the correction.
"""
from pathlib import Path
import datetime
import hashlib
import itertools
import json
import math
import subprocess
import sys

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'manifest-v1.json'
SMALL = (2, 3, 5, 7)
CAP = {2: 4, 3: 3, 5: 2, 7: 2}
LARGE = (11, 13, 17, 19, 23)
EXPECTED_MANIFEST = 'c92cf3011beb60b23c51fb00eded8383564c9654ef7c05df8d682573e10da1fe'

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def metadata(p):
    b = p.read_bytes()
    return {'path': str(p), 'sha256': hashlib.sha256(b).hexdigest(),
            'bytes': len(b), 'LF': b.count(b'\n')}

started = clock()
manifest_meta = metadata(MANIFEST)
assert manifest_meta['sha256'] == EXPECTED_MANIFEST
manifest = json.loads(MANIFEST.read_bytes())
input_metadata = []
for spec in manifest['inputs_in_read_order']:
    got = metadata(Path(spec['path']))
    assert all(got[key] == spec[key] for key in ('sha256', 'bytes', 'LF')), (spec, got)
    input_metadata.append(got)

# All small-prime divisor possibilities, with exponents high enough to include
# every resource boundary. Larger exponents cannot create new resource-free
# cases, because the listed least forbidden prime powers already divide them.
def divisors(Y):
    vals = [1]
    for p in sorted(Y):
        vals = [a * p**e for a in vals for e in range(CAP[p] + 1)]
    return sorted(vals)

def least_power_over7(p):
    a = p
    while a <= 7:
        a *= p
    return a

resources = []
def resource_case(label, Y, common, rs, threshold, expected_free, expected_eligible):
    assert common in Y
    assert all(math.lcm(common, r) > 7 for r in rs)
    free = [n for n in divisors(Y)
            if n % common == 0 and not any(n % r == 0 for r in rs)]
    eligible = [n for n in free if n >= threshold]
    assert free == expected_free, (label, free, expected_free)
    assert eligible == expected_eligible, (label, eligible, expected_eligible)
    assert len(eligible) <= 1
    if eligible:
        assert eligible[0] > 7  # the leftover is itself globally one-use
    rec = {'label': label, 'Y': sorted(Y), 'common_prime': common,
           'resources': rs, 'least_forced_common_divisors': [math.lcm(common, r) for r in rs],
           'mu_threshold': threshold, 'resource_free_divisors': free,
           'eligible_leftovers': eligible,
           'small_resource_plus_leftover_count': len(rs) + len(eligible)}
    resources.append(rec)
    return rec

for p, rs, base in [(2, [8,9,5,7], [2,4,6,12]),
                    (3, [4,9,5,7], [3,6]),
                    (5, [2,3,7,25], [5]),
                    (7, [2,3,5,49], [7])]:
    rec = resource_case('item1-common'+str(p), SMALL, p, rs, 8, base, [12] if p==2 else [])
    assert rec['small_resource_plus_leftover_count'] <= 5

allY = [tuple(c) for r in range(1,5) for c in itertools.combinations(SMALL,r)]
for Y in allY:
    if 2 not in Y or 3 not in Y:
        for p in Y:
            rs = sorted(set(Y)-{p}) + [least_power_over7(p)]
            base = [n for n in divisors((p,)) if 1 < n <= 7]
            rec = resource_case('item2-'+str(Y)+'-common'+str(p), Y, p, rs, 8, base, [])
            assert len(rs) == len(Y)
    if len(Y) <= 2:
        for p in Y:
            if Y == (2,3):
                rs, base = ([8,9], [2,4,6,12]) if p==2 else ([4,9], [3,6])
            else:
                rs = sorted(set(Y)-{p}) + [least_power_over7(p)]
                base = [n for n in divisors((p,)) if 1 < n <= 7]
            resource_case('item3-'+str(Y)+'-common'+str(p), Y, p, rs, 13, base, [])
            assert len(rs) <= 2
for d in (5,7):
    Y = (2,3,d)
    for p in Y:
        rs, base = (([8,9,d],[2,4,6,12]) if p==2 else
                    ([4,9,d],[3,6]) if p==3 else ([2,3,least_power_over7(d)],[d]))
        resource_case('item4-'+str(Y)+'-common'+str(p), Y, p, rs, 13, base, [])

# Resource-free exact {2,3} support (the only repeatable nonsingleton type).
free23 = [n for n in divisors((2,3)) if n%6==0 and n%4 and n%9]
assert free23 == [6]
assert math.lcm(6,4)==12 and math.lcm(6,9)==18
assert all(q>7 for q in LARGE)

# Enumerate every support family (not just a selected maximal pattern).
def support_families(Y, cap):
    types = [frozenset(c) for r in range(2,len(Y)+1) for c in itertools.combinations(Y,r)]
    valid = []
    for mask in range(1,1<<len(types)):
        fam = [types[j] for j in range(len(types)) if mask>>j & 1]
        if set.intersection(*(set(a) for a in fam)):
            continue
        if all(bool(a&b) and math.prod(a&b)<=cap for a,b in itertools.combinations(fam,2)):
            valid.append([sorted(a) for a in fam])
    mx = max(map(len,valid),default=0)
    return {'maximum': mx, 'valid_family_count': len(valid),
            'maximal_cardinality_families': [f for f in valid if len(f)==mx]}

types7 = support_families(SMALL,7)
assert types7['maximum']==4
assert len(types7['maximal_cardinality_families'])==6
three_types = {str(d):support_families((2,3,d),7) for d in (5,7)}
for d in (5,7):
    assert three_types[str(d)]['valid_family_count']==1
    assert three_types[str(d)]['maximal_cardinality_families']==[[[2,3],[2,d],[3,d]]]
missing23_types = {}
for Y in allY:
    if 2 not in Y or 3 not in Y:
        res = support_families(Y,7)
        assert res['maximum'] <= len(Y)
        missing23_types[str(Y)] = res
mutated_types15 = support_families(SMALL,15)
assert mutated_types15['maximum']==6 > 4

# Direct witness checks: these use all pairwise gcds and preserve MULTIPLICITY.
def witness(values, threshold, Y, k, cap=7):
    pairs = [[a,b,math.gcd(a,b)] for a,b in itertools.combinations(values,2)]
    nprime = set()
    for n in values:
        t = n
        p = 2
        while p*p<=t:
            if t%p==0:
                nprime.add(p)
                while t%p==0:
                    t//=p
            p += 1
        if t>1:
            nprime.add(t)
    valid = all(n>=threshold for n in values) and all(2<=g<=cap for _,_,g in pairs)
    assert nprime & set(SMALL) == set(Y)
    assert len(nprime-set(SMALL)) == k
    assert valid
    return {'values':values, 'count':len(values), 'threshold':threshold,
            'Y':sorted(Y), 'k':k, 'gcd_cap':cap, 'gcd_values':sorted(set(g for _,_,g in pairs)),
            'all_conditions_hold':True}

positive_witnesses = []
for k in range(6):
    q = LARGE[:k]
    rows = [([8,12,18,20,28]+[6*p for p in q],8,SMALL,5),
            ([8,10,14]+[2*p for p in q],8,(2,5,7),3),
            ([16,18]+[6*p for p in q],13,(2,3),2),
            ([24,18,20,15]+[6*p for p in q],13,(2,3,5),4)]
    for vals,threshold,Y,offset in rows:
        rec=witness(vals,threshold,Y,k)
        assert rec['count']==k+offset
        rec['bound_offset']=offset
        positive_witnesses.append(rec)

negative = []
def exceeds(label,vals,threshold,Y,k,bound,cap=7,reason=''):
    rec=witness(vals,threshold,Y,k,cap)
    assert len(vals)>bound
    rec.update(label=label,mutated_bound=bound,intended_reason=reason)
    negative.append(rec)

exceeds('lower-mu8-to7-repetition',[7]*7,7,(7,),0,5,
        reason='Index 7 can repeat; >=8 was what excluded all index repetition.')
exceeds('lower-mu13-to12-item3',[12,16,18],12,(2,3),0,2,
        reason='The resource-free even index 12 is now admissible.')
exceeds('remove-missing2or3-item2',[8,12,18],8,(2,3),0,2,
        reason='Products of two shared small primes may now equal 6, not exceed 7.')
exceeds('allow-four-small-primes-item4',[24,18,20,15,42],13,SMALL,0,4,
        reason='Fourth small prime allows a fourth support type beside repeated {2,3}.')
exceeds('raise-gcd-cap-to8',[8,10,12,14,16,18],8,SMALL,0,5,8,
        reason='The resource 8 is no longer one-use when gcd 8 is allowed.')
# Actual tiny finite-group negative instance for the minimum-index hypothesis:
# C7 has only trivial and whole subgroups (prime-order Lagrange); the seven
# distinct singleton cosets of its trivial subgroup are pairwise disjoint.
cyclic7 = [{a} for a in range(7)]
assert all(not (a&b) for a,b in itertools.combinations(cyclic7,2))
assert sorted(set.union(*cyclic7)) == list(range(7))
cyclic7_control = {'group':'integers mod 7 under addition','subgroup':[0],
                   'cosets':[sorted(s) for s in cyclic7], 'indices':[7]*7,
                   'mu':7, 'k':0, 'Y':[7], 'pairwise_gcd':7,
                   'purpose':'Shows why item1 cannot be extended to mu>=7.'}
# Deliberately re-use the indicated resource; each fails for the intended gcd.
collisions=[]
for name,a,b,g in [('common2-resource8',8,16,8),('common2-resource9',18,36,18),
                   ('common2-resource5',10,20,10),('common2-resource7',14,28,14),
                   ('common3-resource4',12,24,12),('common5-resource25',25,50,25),
                   ('common7-resource49',49,98,49),('large-prime11',22,44,22)]:
    assert math.gcd(a,b)==g and g>7
    collisions.append({'label':name,'indices':[a,b],'gcd':g,'rejects_for_intended_reason':True})

# Factoring n!/2 is arithmetic only. Simplicity of A_n (n>=5) is an explicit
# separate elementary group-theory dependency for its coset action to be faithful.
def factors(n):
    ps=[]
    p=2
    while p*p<=n:
        if n%p==0:
            ps.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:ps.append(n)
    return ps
alternating=[]
for n in range(8,14):
    order=math.factorial(n)//2
    ps=factors(order)
    assert order>math.factorial(n-1)
    k=sum(p>7 for p in ps)
    assert k<=2
    alternating.append({'n':n,'order':order,'order_greater_than_previous_factorial':True,
                        'primes':ps,'k':k,'mu_ge_n_given_simplicity':True})

observed_end=clock()
result={'kind':'INDEPENDENT_BOUNDED_EXACT_MATHEMATICAL_CONTROL',
        'started_native_clock':started,'ended_native_clock':observed_end,
        'manifest_metadata':manifest_meta,'inputs_metadata':input_metadata,
        'reviewer_v1_scope_correction':__doc__.split('Correction to ')[1].strip(),
        'resource_cases':resources,'resource_case_count':len(resources),
        'resource_free_exact23':free23,
        'support_family_cap7':types7,'three_small_prime_supports':three_types,
        'missing2or3_supports':missing23_types,'support_cap15_negative_control':mutated_types15,
        'positive_integer_witnesses':positive_witnesses,
        'intended_reason_negative_controls':negative,'cyclic7_negative_control':cyclic7_control,
        'resource_reuse_rejections':collisions,'alternating_arithmetic':alternating,
        'all_assertions_passed':True,
        'limitations':'Not coset realization of positive integer witnesses; not formal/kernel, independent-family, classification, or novelty verification.'}
output=HERE/'reviewer-resource-control-v2-output.json'
receipt_path=HERE/'reviewer-resource-control-v2-receipt.json'
assert not output.exists() and not receipt_path.exists()
with output.open('x') as f:
    json.dump(result,f,indent=2,sort_keys=True)
    f.write('\n')
receipt={'kind':'ACTUAL_EXACT_CONTROL_EXECUTION_RECEIPT',
         'started_native_clock':started,'ended_native_clock':observed_end,
         'python':sys.version,'argv':sys.argv,
         'script':metadata(Path(__file__).resolve()),'output':metadata(output),
         'earlier_v1_script':metadata(HERE/'reviewer-control-v1.py'),
         'earlier_v1_output':metadata(HERE/'reviewer-control-v1-output.json'),
         'assertions':'All reached and passed; uncaught failure would prevent receipt creation.',
         'resource_cases':len(resources),'positive_integer_witness_cases':len(positive_witnesses),
         'negative_bound_cases':len(negative),'resource_reuse_rejections':len(collisions)}
with receipt_path.open('x') as f:
    json.dump(receipt,f,indent=2,sort_keys=True)
    f.write('\n')
print(json.dumps(receipt,sort_keys=True))
print(json.dumps({'receipt':metadata(receipt_path),'status':'ALL_ASSERTIONS_PASSED'},sort_keys=True))
