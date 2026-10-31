#!/usr/bin/env python3
"""Independent reviewer exact controls, designed from the frozen prose only.
No author program is imported, executed, or used as a library.
"""
import collections
import datetime
import hashlib
import itertools
import json
import math
import pathlib
import sys
import time

N = 2640
A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
GA = frozenset((3, 5, 8, 11))
GY = frozenset((1, 2, 6, 12))
DG = tuple(math.gcd(i, N) for i in range(N))
START = time.monotonic()
DEADLINE = START + 300
ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / 'reviewer-independent-exact-v1-receipt.json'
if OUT.exists():
    raise SystemExit('Refusing receipt overwrite')
R = {'kind': 'INDEPENDENT_EXACT_INTEGER_CONTROL',
     'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'source_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
     'python': sys.version, 'n': N, 'author_code_imported_or_executed': False,
     'sections': {}, 'mutations': [], 'unknown': []}

def gcdiff(x, y):
    return DG[(x-y) % N]

def delta(xs):
    return frozenset(gcdiff(x,y) for x,y in itertools.combinations(xs,2))

def screen(anchors, forbidden):
    return tuple(x for x in range(N) if all(x == b or gcdiff(x,b) not in forbidden for b in anchors))

def compatible(xs, forbidden):
    return not (delta(xs) & forbidden)

def counts(xs, m):
    return [sum(x % m == r for x in xs) for r in range(m)]

def gs(m,k):
    return [(m,r,k) for r in range(m)]

def capacity(xs, quotas):
    return all(sum(x % m == r for x in xs) >= k for m,r,k in quotas)

def valid_selection(xs, candidates, forbidden, quotas, anchors):
    assert len(xs) == len(set(xs))
    assert set(xs) <= set(candidates)
    assert set(anchors) <= set(xs)
    assert compatible(xs, forbidden)
    assert all(sum(x % m == r for x in xs) == k for m,r,k in quotas)

# Independently implemented exact independent-set-with-overlapping-counts solver.
# It propagates fully forced groups simultaneously, then does binary branching.
# State = available-vertex bitset plus residual counts; only exhausted states memoize.
def solve(candidates, forbidden, quotas, anchors=()):
    vals = tuple(x for x in sorted(set(candidates)) if any(x % m == r for m,r,k in quotas))
    ix = {x:i for i,x in enumerate(vals)}
    masks = [sum(1<<i for i,x in enumerate(vals) if x % m == r) for m,r,k in quotas]
    member = [tuple(j for j,g in enumerate(masks) if (g>>i)&1) for i in range(len(vals))]
    bad = [sum(1<<j for j,y in enumerate(vals) if i != j and gcdiff(x,y) in forbidden) for i,x in enumerate(vals)]
    active = (1<<len(vals))-1
    need = tuple(k for m,r,k in quotas)
    chosen = 0
    nodes = 0
    prunes = 0
    exhausted = set()
    def put(v, avail, wants):
        b = 1<<v
        return avail & ~(b | bad[v]), tuple(k-(j in member[v]) for j,k in enumerate(wants))
    for x in anchors:
        if x not in ix or not ((active>>ix[x])&1):
            return {'sat':False,'nodes':0,'prunes':1,'witness':None}
        i = ix[x]
        active, need = put(i,active,need)
        chosen |= 1<<i
    def dfs(avail, wants, selected):
        nonlocal nodes,prunes
        nodes += 1
        if nodes > 2000000 or (nodes % 1024 == 0 and time.monotonic() > DEADLINE):
            raise TimeoutError('bounded exact control reached limit; UNKNOWN, not UNSAT')
        while True:
            if min(wants, default=0) < 0:
                prunes += 1
                return None
            for j,k in enumerate(wants):
                if not k:
                    avail &= ~masks[j]
            forced = 0
            for j,k in enumerate(wants):
                g = avail & masks[j]
                c = g.bit_count()
                if c < k:
                    prunes += 1
                    return None
                if k and c == k:
                    forced |= g
            if not any(wants):
                return selected
            if not forced:
                break
            while forced:
                b = forced & -forced
                i = b.bit_length()-1
                forced ^= b
                if not (avail & b):
                    prunes += 1
                    return None
                avail,wants = put(i,avail,wants)
                selected |= b
        key = (avail,wants)
        if key in exhausted:
            return None
        j = min((j for j,k in enumerate(wants) if k), key=lambda j:((avail&masks[j]).bit_count()-wants[j],(avail&masks[j]).bit_count(),j))
        options = avail&masks[j]
        vi = []
        while options:
            b = options & -options
            options ^= b
            i = b.bit_length()-1
            vi.append(i)
        i = max(vi,key=lambda v:((bad[v]&avail).bit_count(),len(member[v]),-v))
        newavail,newwants = put(i,avail,wants)
        answer = dfs(newavail,newwants,selected | (1<<i))
        if answer is None:
            answer = dfs(avail & ~(1<<i),wants,selected)
        if answer is None:
            exhausted.add(key)
        return answer
    try:
        answer = dfs(active,need,chosen)
    except TimeoutError as e:
        return {'sat':None,'nodes':nodes,'prunes':prunes,'witness':None,'reason':str(e)}
    witness = None if answer is None else [x for i,x in enumerate(vals) if (answer>>i)&1]
    if witness is not None:
        valid_selection(witness, candidates, forbidden, quotas, anchors)
    return {'sat': answer is not None,'nodes':nodes,'prunes':prunes,'witness':witness}

def record(name, data):
    R['sections'][name] = data
    print(name, json.dumps(data,sort_keys=True), flush=True)

def require_unsat(result, label):
    if result['sat'] is None:
        R['unknown'].append(label)
    else:
        assert result['sat'] is False, (label,result)

P = screen(A,GY)
Q = screen(Y,GA)
assert delta(A) == GA and delta(Y) == GY
assert len(P) == 224 and len(Q) == 658
vectors = {'P':{str(m):counts(P,m) for m in (3,5,11)},'Q':{str(m):counts(Q,m) for m in (3,5,11)}}
# This constructs and checks a different, simpler cover: ascending degree, first fit.
qedges = [sum(1<<j for j,y in enumerate(Q) if x != y and gcdiff(x,y) in GA) for x in Q]
cliques = []
for i in sorted(range(len(Q)),key=lambda i:(qedges[i].bit_count(),Q[i])):
    dest = next((j for j,c in enumerate(cliques) if not (c & ~qedges[i])),None)
    if dest is None:
        cliques.append(1<<i)
    else:
        cliques[dest] |= 1<<i
assert sum(c.bit_count() for c in cliques) == len(Q)
assert len(cliques) < 330
pairs = [(256,418),(415,253),(916,1078),(1075,913),(1576,1738),(1735,1573),(2236,2398),(2395,2233)]
assert len(set(itertools.chain.from_iterable(pairs))) == 16
assert all(x in P and y in P and x%3 == y%3 == 1 and gcdiff(x,y) in GY for x,y in pairs)
raw = [p for p in range(7,len(P)+1) if N%p == 0 and (N//p)%2 == 0]
left = [p for p in raw if p != 8 and p != 11 and p not in (60,66,120,132,165,110,220)]
assert left == [10,12,15,20,22,24,30,33,40,44,55,88]
record('size_sieve',{'vectors':vectors,'raw':raw,'twelve':left,'independent_clique_cover_count':len(cliques),'cliques':[[Q[i] for i in range(len(Q)) if (c>>i)&1] for c in cliques]})

# Small head-only branches, with literal matching and every T-subset.
T = tuple(x for x in P if x%3 == 1 and x%5 != 3)
Z = tuple(x for x in P if x%3 == 1 and x%5 == 3)
assert len(T)==8 and len(Z)==16 and all(z%11 == 0 for z in Z)
blockers = {z:[t for t in T if gcdiff(z,t) in GY] for z in Z}
p30max = 0
for mask in range(1<<len(T)):
    ts = [t for i,t in enumerate(T) if (mask>>i)&1]
    allowedz = [z for z in Z if all(gcdiff(z,t) not in GY for t in ts)]
    p30max = max(p30max,len(ts)+min(4,len(allowedz)))
assert p30max == 8
record('P30_P33',{'T':T,'Z':Z,'blockers':blockers,'all_T_subsets':256,'P30_upper_bound':p30max,'P33_upper_bound':len(T)+1})
four = [(872,459),(2192,1779),(987,344),(2307,1664)]
assert all(x in P and y in P and {x%5,y%5} == {2,4} and gcdiff(x,y)==1 for x,y in four)
assert len(set(itertools.chain.from_iterable(four))) == 8
# Independently enumerate every omission choice, not just rely on pigeonhole wording.
p55choices = 0
for u in (x for x in P if x%5==2):
    for v in (x for x in P if x%5==4):
        chosen = [x for x in P if x%5 in (2,4) and x not in (u,v)]
        p55choices += 1
        assert not compatible(chosen,GY)
# Intended-reason mutation: drop gcd 1; at least one of these exact choices survives.
p55control = next([x for x in P if x%5 in (2,4) and x not in (u,v)] for u in P if u%5==2 for v in P if v%5==4 if compatible([x for x in P if x%5 in (2,4) and x not in (u,v)], GY-{1}))
assert compatible(p55control,GY-{1}) and not compatible(p55control,GY)
record('P55',{'omission_choices':p55choices,'all_conflict':True,'drop_gcd1_witness':p55control})
R['mutations'].append({'name':'P55_drop_gcd1','changed_only':'GY loses 1','relaxation_sat':True,'original_rejects_for_gcd':1})

# Check all explicit forced-gcd proofs in the prose.
force = {}
for g, forced in ((4,(872,459)),(16,(872,1779))):
    s = screen(A,GY|{g})
    assert [sum(x%5==r for x in s) for r in (2,4)] == [8,8]
    assert all(x in s for x in forced) and gcdiff(*forced)==1
    force['P40_'+str(g)] = list(forced)
s = screen(A,GY|{1320})
cycles = [(264,1584),(344,1664),(459,1779),(539,1859),(924,2244),(1199,2519)]
assert {x for x in s if x%5==4} == set(itertools.chain.from_iterable(cycles))
assert all(gcdiff(x,y)==1320 for x,y in cycles)
force['P40_1320'] = cycles
s = screen(A,GY|{660})
class4 = tuple(x for x in s if x%5==4)
possible = [c for c in itertools.combinations(class4,8) if compatible(c,GY|{660})]
assert len(possible)==4
for c in possible:
    available = [x for x in s if x%5==1 and all(gcdiff(x,h) not in GY|{660} for h in c)]
    assert available == [11,396,1056,1331,1716,2376]
force['P40_660'] = {'class4':class4,'four_cases':possible,'class1_capacity':6}
s = screen(A,GY|{4})
assert [sum(x%11==r for x in s) for r in (1,4)] == [8,8]
assert 155 in s and 576 in s and gcdiff(155,576)==1
force['P88_4'] = [155,576]
s = screen(A,GY|{55})
for r,forced,pairs55 in ((5,456,[(368,423),(1028,1083),(1688,1743),(2348,2403)]),(2,35,[(68,123),(728,783),(1388,1443),(2048,2103)])):
    vals = [x for x in s if x%11==r]
    assert len(vals)==12 and forced in vals
    assert len(set(itertools.chain.from_iterable(pairs55)))==8
    assert all(x in vals and y in vals and forced not in (x,y) and gcdiff(x,y)==55 for x,y in pairs55)
assert gcdiff(456,35)==1
force['P88_55'] = [456,35]
s = screen(A,GY|{240})
pairs240 = [(35,1176),(68,1748),(123,1803),(783,2463),(816,395)]
assert [sum(x%11==r for x in s) for r in (2,10)] == [10,10]
assert len(set(itertools.chain.from_iterable(pairs240)))==10
assert all(x in s and y in s and {x%11,y%11} == {2,10} and gcdiff(x,y) in GY|{240} for x,y in pairs240)
force['P88_240'] = pairs240
record('explicit_forced_gcds',force)

# Small five-class forced-240 head selection, exactly as a necessary relaxation.
headquotas = [(11,r,2) for r in (2,10,9,7,3)]
fcandidates = tuple(x for x in screen(A,GY|{240}) if x%11 in (2,10,9,7,3))
assert len(fcandidates)==63
f240 = solve(fcandidates,GY|{240},headquotas,(3,))
require_unsat(f240,'forced240')
fc = [3,35,68,128,183,395,428,515,548,608]
valid_selection(fc,screen(A,GY),GY,headquotas,(3,))
assert 240 in delta(fc)
record('forced240',{'candidates':len(fcandidates),'original':f240,'drop240_literal_witness':fc})
R['mutations'].append({'name':'forced240_drop240','changed_only':'forbidden gcd set loses 240','relaxation_sat':True,'original_rejects_for_gcd':240})

# P88 slot-capacity proof, enumerating all seeds with no author program.
F88 = GA|{4,55,240}
C88 = screen(Y,F88)
assert not any(x%3==1 and x%5 in (0,4) for x in C88)
assert all(x%2==1 for x in C88 if x%3==1)
seeds = tuple(x for x in C88 if x%5 in (1,2,3) and x%3 != 1)
assert len(seeds)==16
ones = tuple(x for x in C88 if x%3==1)
for x,y in itertools.combinations(ones,2):
    if (x%5,x%16)==(y%5,y%16):
        assert gcdiff(x,y)==240
stages = collections.Counter()
for seed in itertools.combinations(seeds,8):
    if not compatible(seed,F88):
        stages['internal_conflict'] += 1
    elif any(sum(x%5==r for x in seed)>6 for r in (1,2,3)):
        stages['quota_overflow'] += 1
    else:
        potential = [x for x in ones if all(gcdiff(x,y) not in F88 for y in seed)]
        if any(len({x%16 for x in potential if x%5==r}) < 6-sum(x%5==r for x in seed) for r in (1,2,3)):
            stages['slot_shortfall'] += 1
        else:
            stages['survive'] += 1
assert dict(stages)=={'internal_conflict':12657,'quota_overflow':33,'slot_shortfall':180}
record('P88_slots',{'seeds':seeds,'all_seed_choices':math.comb(16,8),'stages':dict(stages)})

# Exhaustively group head subsets by their entire Delta(A union subset).
def head_partition(kind):
    frequency = collections.Counter()
    rejected = 0
    total = 0
    if kind in ('P10','P20'):
        k = 2 if kind=='P10' else 4
        chunks = [tuple(x for x in P if x%5==r) for r in (2,4)]
        generator = (c+d for c in itertools.combinations(chunks[0],k) for d in itertools.combinations(chunks[1],k))
    elif kind=='P44':
        chunks = [tuple(x for x in P if x%11==r) for r in (1,2)]
        generator = (c+d for c in itertools.combinations(chunks[0],4) for d in itertools.combinations(chunks[1],4))
    elif kind=='P24':
        chunks = [tuple(x for x in P if x%3==1 and x%2==par) for par in (0,1)]
        generator = (c+d for c in itertools.combinations(chunks[0],4) for d in itertools.combinations(chunks[1],4))
    elif kind=='P15':
        generator = (tuple(c) for z in (0,1) for c1 in itertools.combinations(T,5-z) for c2 in itertools.combinations(Z,z) for c in (c1+c2,))
    elif kind=='P22':
        chunks = [tuple(x for x in P if x%11==r and x%2==par) for r in (1,2) for par in (0,1)]
        generator = itertools.product(*chunks)
    else:
        raise ValueError(kind)
    for c in generator:
        total += 1
        h = delta(A+c)
        if h&GY:
            rejected += 1
        else:
            if kind in ('P22','P44'):
                h = h|{240}
            frequency[h] += 1
    return frequency, {'total':total,'conflict':rejected,'valid':sum(frequency.values()),'distinct_H':len(frequency)}

summaries = {}
for kind,cap1,cap2,quota,anchors in (
    ('P10',gs(3,88),gs(11,24),[(3,0,88),(11,2,24)],(0,13)),
    ('P15',gs(16,11),[],gs(16,11)+gs(11,16),Y),
    ('P20',gs(3,44),gs(11,12),[(3,0,44),(11,2,12)],(0,13)),
    ('P44',gs(3,20),gs(5,12),[(3,0,20),(5,1,12)],(0,1)),
    ('P24',gs(5,22),gs(11,10),[(5,0,22),(11,2,10)],(0,13)),
):
    freq,summary = head_partition(kind)
    summary.update({'capacity1_fail':0,'capacity2_fail':0,'search_choices':0,'search_H':0,'search_results':[]})
    for h,weight in sorted(freq.items(),key=lambda p:tuple(sorted(p[0]))):
        cand = screen(Y,h)
        if not capacity(cand,cap1):
            summary['capacity1_fail'] += weight
        elif not capacity(cand,cap2):
            summary['capacity2_fail'] += weight
        else:
            summary['search_choices'] += weight
            summary['search_H'] += 1
            ans = solve(cand,h,quota,anchors)
            require_unsat(ans,kind+':'+str(sorted(h)))
            summary['search_results'].append({'H':sorted(h),'frequency':weight,**ans})
    summaries[kind] = summary
    record(kind,summary)
# Intended-reason P10 mutation: only partial-head gcd additions are dropped.
p10base = solve(Q,GA,[(3,0,88),(11,2,24)],(0,13))
assert p10base['sat'] is True
h0 = frozenset(summaries['P10']['search_results'][0]['H'])
assert delta(p10base['witness']) & (h0-GA)
record('P10_drop_partial_head_gcds_control',p10base)
R['mutations'].append({'name':'P10_drop_partial_head_gcds','changed_only':'forbidden set becomes GA','relaxation_sat':True,'additional_H_reject_witness_by':sorted(delta(p10base['witness'])&(h0-GA))})

# P40 full prime-fibre relaxation after the written forced gcds.
f40 = GA|{4,16,660,1320}
c40 = screen(Y,f40)
assert len(c40)==457
p40 = solve(c40,f40,gs(3,22)+gs(11,6),Y)
require_unsat(p40,'P40')
record('P40',{'candidates':len(c40),**p40})

# P22: all parity allocations and every individually allowed high-fibre pair (H,a).
freq,summary = head_partition('P22')
summary.update({'prime_capacity_fail':0,'no_a_fail':0,'remaining_choices':0,'remaining_H':0,'cases':[]})
for h,weight in sorted(freq.items(),key=lambda p:tuple(sorted(p[0]))):
    cand = screen(Y,h)
    if not capacity(cand,gs(3,40)+gs(5,24)):
        summary['prime_capacity_fail'] += weight
        continue
    aa = [a for a in range(1,11) if capacity(cand,[(16,r,a if r%2==0 else 15-a) for r in range(16)])]
    if not aa:
        summary['no_a_fail'] += weight
        continue
    summary['remaining_choices'] += weight
    summary['remaining_H'] += 1
    for a in aa:
        quotas = [(16,r,a if r%2==0 else 15-a) for r in range(16)]+[(3,1,40),(5,1,24)]
        ans = solve(cand,h,quotas,Y)
        require_unsat(ans,'P22:'+str((sorted(h),a)))
        summary['cases'].append({'H':sorted(h),'a':a,**ans})
record('P22',summary)

# P12: do not silently treat the genuine two-quota SAT leaves as exclusions.
c0 = tuple(x for x in P if x%3==1 and x%2==0)
c1 = tuple(x for x in P if x%3==1 and x%2==1)
assert len(c0)==len(c1)==12
p12 = {}
residual = {}
for s in (2,3,4):
    freq = collections.Counter()
    stage = collections.Counter()
    for aa in itertools.combinations(c0,2):
        for bb in itertools.combinations(c1,2):
            part = aa+bb
            h = delta(A+part)
            if h&GY:
                stage['conflict'] += 1
                continue
            folded = collections.Counter(((x-1)//3)%(1<<s) for x in part)
            if any(folded[r]!=folded[r+(1<<(s-1))] for r in range(1<<(s-1))):
                stage['high_bit_fail'] += 1
                continue
            stage['valid'] += 1
            freq[h] += 1
    row = {'stages':dict(stage),'distinct_H':len(freq),'two_quota_sat_choices':0,'two_quota_unsat_choices':0,'two_quota_results':[]}
    for h,weight in sorted(freq.items(),key=lambda p:tuple(sorted(p[0]))):
        cand = screen(Y,h)
        ans = solve(cand,h,[(5,0,44),(11,2,20)],(0,13))
        row['two_quota_results'].append({'H':sorted(h),'frequency':weight,**ans})
        if ans['sat'] is True:
            row['two_quota_sat_choices'] += weight
            assert s==4
            residual[h] = weight
        elif ans['sat'] is False:
            row['two_quota_unsat_choices'] += weight
        else:
            R['unknown'].append('P12-two-quota:'+str((s,sorted(h))))
    p12[str(s)] = row
    record('P12_s'+str(s),row)
assert len(residual)==6 and sum(residual.values())==16
# The literal example is checked, not assumed to be SAT by its name.
hliteral = frozenset((3,4,5,8,11,16,20,24,44,80,88,165))
w = [0,13,50,60,110,120,170,180,211,240,277,290,300,343,350,360,410,541,600,607,660,673,720,770,780,830,840,871,890,900,960,1003,1010,1020,1070,1130,1201,1260,1267,1320,1333,1370,1380,1440,1490,1500,1531,1550,1560,1597,1610,1620,1680,1730,1790,1861,1920,1927,1980,2030,2257,2323,2521,2587]
assert hliteral in residual
valid_selection(w,screen(Y,hliteral),hliteral,[(5,0,44),(11,2,20)],(0,13))
assert len(w)==64
# Preserve quotas, old-anchor screen and mandatory 0,13, but insert a pair conflict.
mutation = None
for old in w:
    if old in (0,13):
        continue
    for new in screen(Y,hliteral):
        if new in w or (old%5==0,old%11==2)!=(new%5==0,new%11==2):
            continue
        altered = [new if x==old else x for x in w]
        if not compatible(altered,hliteral):
            assert all(sum(x%m==r for x in altered)==k for m,r,k in [(5,0,44),(11,2,20)])
            pair = next((x,y,gcdiff(x,y)) for x,y in itertools.combinations(altered,2) if gcdiff(x,y) in hliteral)
            mutation = {'name':'P12_quota_preserving_pair_conflict','removed':old,'inserted':new,'failing_pair':pair,'screen_preserved':True,'quotas_preserved':True,'mandatory_anchors_preserved':True}
            break
    if mutation is not None:
        break
assert mutation is not None
R['mutations'].append(mutation)
record('P12_literal_two_quota_positive',{'witness':w,'H':sorted(hliteral),'verified':True,'mod8_counts':counts(w,8)})
# Now enforce all eight folded counts; each is a necessary constraint for actual Q.
fibre = []
for h,weight in sorted(residual.items(),key=lambda p:tuple(sorted(p[0]))):
    cand = screen(Y,h)
    allowed = [a for a in range(1,55) if capacity(cand,[(8,r,a if r%2==0 else 55-a) for r in range(8)])]
    for a in allowed:
        quotas = [(8,r,a if r%2==0 else 55-a) for r in range(8)]+[(5,0,44),(11,2,20)]
        ans = solve(cand,h,quotas,Y)
        require_unsat(ans,'P12-fibre:'+str((sorted(h),a)))
        fibre.append({'H':sorted(h),'a':a,**ans})
assert len(fibre)==146
record('P12_residual_fibres',{'H_count':len(residual),'partial_head_choices':sum(residual.values()),'H_a_cases':len(fibre),'results':fibre})
R['mutations'].append({'name':'P12_omit_mod8_fibres','changed_only':'remove eight fibre quotas and old anchors outside quota union','relaxation_sat_H':6,'relaxation_sat_head_choices':16,'with_all_necessary_fibres_unsat_cases':146})

R['completed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
R['elapsed_seconds'] = time.monotonic()-START
R['all_assertions_passed'] = True
with OUT.open('x') as f:
    json.dump(R,f,indent=2,sort_keys=True)
    f.write('\n')
print('RECEIPT',OUT,hashlib.sha256(OUT.read_bytes()).hexdigest(),flush=True)
