#!/usr/bin/env python3
"""Independent direct-coordinate, exact-integer review of three frozen duals.

Uses no author code.  All coefficient equations are checked on the original
1023 labelled subset coordinates, not only in the symmetry quotient.
"""
from collections import Counter, defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, permutations, product
from pathlib import Path
import json, math

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'manifest-v1.json'
MANIFEST_SHA = '2851477a354693144813bbfd3c0551e206744336636a44d4cf218ef6161acf4f'
N = {1:(2,3,4,5,6,7), 2:(1,3,7,9,10), 3:(1,2,4,8,9),
     4:(1,3,5,8,10), 5:(1,4,6,9,10), 6:(1,5,7,8,9),
     7:(1,2,6,8,10), 8:(3,4,6,7,9,10), 9:(2,3,5,6,8),
     10:(2,4,5,7,8)}
GEN = [(7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9)]
FULL = (1<<10)-1

class CheckError(Exception):
    pass

def require(condition, reason):
    if not condition: raise CheckError(reason)

def unique_object(pairs):
    d = {}
    for k,v in pairs:
        require(k not in d, 'duplicate_json_key')
        d[k]=v
    return d

def load(b):
    return json.loads(b, object_pairs_hook=unique_object)

def pin_inputs():
    b=MANIFEST.read_bytes()
    require(sha256(b).hexdigest()==MANIFEST_SHA, 'manifest_hash')
    m=load(b); raw=[]; pins=[]
    require(len(m['inputs_in_read_order'])==14, 'manifest_count')
    for item in m['inputs_in_read_order']:
        bb=Path(item['path']).read_bytes()
        digest=sha256(bb).hexdigest()
        require(digest==item['sha256'], 'input_hash')
        require(len(bb)==item['bytes'] and bb.count(b'\n')==item['LF'], 'input_size')
        raw.append(bb); pins.append({'name':Path(item['path']).name,'sha256':digest,
                                    'bytes':len(bb),'LF':bb.count(b'\n')})
    return raw,pins

def perm_mask(s,p):
    return sum(1<<p[i] for i in range(10) if s>>i&1)

def graph_group():
    require(all(u!=v and u in N[v] for v,ns in N.items() for u in ns), 'graph_symmetry')
    edges={tuple(sorted((v-1,u-1))) for v,ns in N.items() for u in ns}
    require(len(edges)==26, 'graph_edges')
    identity=tuple(range(10)); group={identity}; frontier=[identity]
    while frontier:
        x=frontier.pop()
        for y in GEN:
            z=tuple(y[x[k]] for k in range(10))
            if z not in group: group.add(z);frontier.append(z)
    require(len(group)==8, 'group_order')
    require(all(set(p)==set(range(10)) and
        {tuple(sorted((p[a],p[b]))) for a,b in edges}==edges for p in group),'group_edge')
    # Exhaust all degree-preserving vertex permutations independently of generators.
    degree_classes=defaultdict(list)
    for v,ns in N.items(): degree_classes[len(ns)].append(v-1)
    classes=list(degree_classes.values()); all_graph_autos=set()
    for choices in product(*(permutations(c) for c in classes)):
        p=[None]*10
        for cls,dest in zip(classes,choices):
            for a,b in zip(cls,dest): p[a]=b
        if all(tuple(sorted((p[a],p[b]))) in edges for a,b in edges):
            all_graph_autos.add(tuple(p))
    require(group==all_graph_autos, 'full_automorphism_group')
    return sorted(group),edges,classes

def bit(v):
    require(type(v) is int and 1<=v<=10, 'vertex_range')
    return 1<<(v-1)

def clean(d): return {k:v for k,v in d.items() if v}

def add_term(d,mask,c):
    if mask: d[mask]+=c

def cmi_terms(a,b,z):
    d=defaultdict(int)
    for s,c in [(a|z,1),(b|z,1),(a|b|z,-1),(z,-1)]: add_term(d,s,c)
    return clean(d)

def ingleton_terms(a,b,c,d,z):
    # Direct expanded entropy polynomial, NOT author checker CMI construction.
    out=defaultdict(int)
    for s in (a|c|z,b|c|z,a|d|z,b|d|z,a|b|z): add_term(out,s,1)
    for s in (a|b|c|z,a|b|d|z,c|d|z,a|z,b|z): add_term(out,s,-1)
    return clean(out)

def row_terms(meta):
    k=meta['kind']
    if k=='CMI':
        require(set(meta)=={'kind','i','j','condition_mask'}, 'row_schema')
        a,b=bit(meta['i']),bit(meta['j']); z=meta['condition_mask']
        require(a!=b and type(z) is int and 0<=z<=FULL and not (z&(a|b)), 'row_input')
        return cmi_terms(a,b,z)
    if k=='conditional-ingleton':
        require(set(meta)=={'kind','A','B','C','D','Z_mask'}, 'row_schema')
        a,b,c,d=(bit(meta[t]) for t in ('A','B','C','D'));z=meta['Z_mask']
        require(len({a,b,c,d})==4 and type(z) is int and 0<=z<=FULL and
                not z&(a|b|c|d), 'row_input')
        return ingleton_terms(a,b,c,d,z)
    if k=='FD':
        require(set(meta)=={'kind','vertex'}, 'row_schema')
        v=meta['vertex']; a=bit(v); z=sum(bit(w) for w in N[v])
        return {z|a:1,z:-1}
    raise CheckError('unknown_kind')

def orbits(group):
    reps={s:min(perm_mask(s,g) for g in group) for s in range(1,FULL+1)}
    ordered=sorted(set(reps.values())); index={s:i for i,s in enumerate(ordered)}
    require(len(ordered)==185,'orbit_count')
    return reps,ordered,index

def verify(doc,group,reps,ordered,index, expected):
    require(doc['orbits']==ordered, 'orbit_list')
    require(doc['bound']=='20/3' and doc['expected_row_count']==expected[0]
            and len(doc['rows'])==expected[0], 'row_count')
    caps={x['orbit_representative']:Q(x['weight']) for x in doc['caps']}
    require(len(caps)==len(doc['caps']) and caps=={1:Q(4,3),2:Q(8,3),4:Q(8,3)}, 'caps')
    acc=[Q(0) for _ in range(FULL+1)]
    kinds=Counter(); ingletons=[]; fd={}; min_cmi=None; min_ing=None
    for row in doc['rows']:
        require(set(row)=={'metadata','orbit_terms','weight'}, 'row_schema')
        md=row['metadata']; k=md['kind']; kinds[k]+=1
        coeff=row_terms(md); w=Q(row['weight'])
        if k in ('CMI','conditional-ingleton'):
            require(w>0,'inequality_sign')
        elif k=='FD':
            require(md['vertex'] not in fd,'fd_repetition'); fd[md['vertex']]=w
        if k=='CMI': min_cmi=w if min_cmi is None else min(min_cmi,w)
        if k=='conditional-ingleton':
            min_ing=w if min_ing is None else min(min_ing,w)
            ingletons.append((md['A'],md['B'],md['C'],md['D'],md['Z_mask'],w))
        # Check every supplied quotient row against independent expansion.
        oq=defaultdict(int)
        for mask,value in coeff.items(): oq[index[reps[mask]]]+=value
        oq=clean(oq)
        actual=row['orbit_terms']
        require(all(type(i) is int and type(v) is int and v and 0<=i<len(ordered)
                    for i,v in actual), 'row_terms_type')
        require(len({i for i,v in actual})==len(actual) and
                sorted(oq.items())==sorted((i,v) for i,v in actual), 'row_mismatch')
        # Expand each averaged row directly over all 8 automorphisms.
        for mask,value in coeff.items():
            for g in group:
                acc[perm_mask(mask,g)]+=w*value/Q(len(group))
    require(dict(kinds)==expected[1],'kind_counts')
    require(fd=={1:Q(-2,3),2:Q(-4,3),3:Q(-4,3)}, 'fd_weights')
    if expected[2] is not None: require(sorted(ingletons)==expected[2], 'named_ingletons')
    target=[Q(0) for _ in range(FULL+1)]
    for v in range(1,11): target[bit(v)]=Q(2,3)
    target[FULL]=-1
    mismatch={s:str(acc[s]-target[s]) for s in range(1,FULL+1) if acc[s]!=target[s]}
    require(not mismatch, 'coefficient_residual')
    return {'row_counts':dict(kinds),'all_labelled_subset_coordinates_compared':1023,
            'nonzero_coefficient_residual':mismatch,'minimum_CMI_weight':str(min_cmi),
            'minimum_ingleton_weight':str(min_ing),
            'total_ingleton_weight':str(sum((x[-1] for x in ingletons),Q(0))),
            'ingleton_rows':[[*x[:-1],str(x[-1])] for x in ingletons] if len(ingletons)<=2 else '83 separately verified',
            'fd_weights':{str(k):str(v) for k,v in fd.items()},'caps':{str(k):str(v) for k,v in caps.items()}}

def diamond_orbit(group,edges):
    a,b,c,d=map(bit,[2,4,1,3]); z=FULL^(a|b|c|d)
    result=set()
    def vertex(single): return single.bit_length()
    for g in group:
        aa,bb,cc,dd=(vertex(perm_mask(x,g)) for x in (a,b,c,d))
        zz=tuple(i for i in range(1,11) if perm_mask(z,g)&bit(i))
        row=(tuple(sorted((aa,bb))),tuple(sorted((cc,dd))),zz)
        result.add(row)
        verts=[aa,bb,cc,dd]
        missing=[tuple(sorted((x,y))) for x,y in combinations(verts,2)
                 if tuple(sorted((x-1,y-1))) not in edges]
        require(missing==[tuple(sorted((aa,bb)))], 'diamond_graph')
        # A,B see both C,D; C,D see each other and A,B.
        for x in (aa,bb): require(cc in N[x] and dd in N[x], 'diamond_fd')
        for x,y in ((cc,dd),(dd,cc)): require(aa in N[x] and bb in N[x] and y in N[x], 'diamond_fd')
    specified={((2,4),(1,3),(5,6,7,8,9,10)),
      ((2,6),(1,7),(3,4,5,8,9,10)), ((3,5),(1,4),(2,6,7,8,9,10)),
      ((3,10),(4,8),(1,2,5,6,7,9)), ((4,9),(3,8),(1,2,5,6,7,10)),
      ((5,7),(1,6),(2,3,4,8,9,10)), ((6,10),(7,8),(1,2,3,4,5,9)),
      ((7,9),(6,8),(1,2,3,4,5,10))}
    require(result==specified, 'diamond_orbit_table')
    return sorted(result)

def lower(edges):
    tri=[(1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),
         (3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8)]
    require(len(set(tri))==10 and all(sum(v in t for t in tri)==3 for v in range(1,11)), 'triangle_cover')
    require(all(tuple(sorted((a-1,b-1))) in edges for t in tri for a,b in combinations(t,2)), 'triangle_edges')
    # 30 coordinate positions, one per (triangle, vertex).  Row reduction
    # checks 10 independent XOR parity equations, not a solver claim.
    equations=[sum(1<<(3*i+j) for j in range(3)) for i in range(10)]
    pivots={}
    for row in equations:
        while row:
            k=row.bit_length()-1
            if k not in pivots: pivots[k]=row; break
            row ^= pivots[k]
    require(len(pivots)==10, 'triangle_rank')
    return {'triangles':tri,'occurrences_per_vertex':3,'q':8,
            'binary_coordinates':30,'independent_parity_checks':len(pivots),
            'fixed_words':2**(30-len(pivots)), 'log_q_fixed_words':'20/3'}

def factor(n):
    require(n>0,'factor_nonpositive'); out={};p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def entropy(mask,words,weights):
    total=sum(weights); bins=defaultdict(int)
    for w,n in zip(words,weights): bins[w&mask]+=n
    terms=defaultdict(Q)
    for p,e in factor(total).items(): terms[p]+=e
    for n in bins.values():
        for p,e in factor(n).items(): terms[p]-=Q(n*e,total)
    return clean(terms)

def linear_entropy(expr,words,weights):
    out=defaultdict(Q)
    for m,c in expr.items():
        for p,v in entropy(m,words,weights).items(): out[p]+=c*v
    return clean(out)

def avg_terms(expr,group):
    out=defaultdict(Q)
    for m,c in expr.items():
        for g in group: out[perm_mask(m,g)]+=Q(c,len(group))
    return clean(out)

def partition(mask,words):
    bins=defaultdict(list)
    for i,w in enumerate(words): bins[w&mask].append(i)
    return tuple(sorted(tuple(x) for x in bins.values()))

def no_fd_collision(words):
    count=0
    for a,b in combinations(words,2):
        for v in range(1,11):
            nbr=sum(bit(w) for w in N[v]); count+=1
            require((a&nbr)!=(b&nbr) or (a&bit(v))==(b&bit(v)), 'fd_collision')
    return count

def witness(group):
    words=[0,6,3,15]; w1=[2,1,1,2]; w2=[21,4,16,9]
    count=no_fd_collision(words)
    require(count==60,'fd_count')
    j1=ingleton_terms(bit(2),bit(4),bit(1),bit(3),sum(bit(x) for x in (5,6,7,8,9,10)))
    j2=ingleton_terms(bit(2),bit(5),bit(3),bit(6),sum(bit(x) for x in (1,4,7,8,10)))
    e1=linear_entropy(j1,words,w1)
    require(e1=={2:Q(3),3:Q(-2)}, 'local_J1')
    require(linear_entropy(cmi_terms(bit(2),bit(4),bit(1)),words,w1)=={} and
            linear_entropy(cmi_terms(bit(2),bit(4),bit(3)),words,w1)=={}, 'local_conditionals')
    require(entropy(bit(1),words,w1)=={2:Q(1)} and entropy(bit(3),words,w1)=={2:Q(1)},'first_M')
    require(9**8>2**25 and Q(1,8)>Q(7,69), 'local_integer_compare')
    require(sum(n for w,n in zip(words,w2) if w&bit(1))==25 and sum(w2)==50,'second_M')
    eavg1=linear_entropy(avg_terms(j1,group),words,w2)
    eavg2=linear_entropy(avg_terms(j2,group),words,w2)
    require(eavg2=={}, 'average_J2')
    # Check J2=0 for EVERY probability vector on this support, by partition
    # coefficients, not by evaluation at the one reported weighted law.
    pcoef=defaultdict(Q)
    for mask,c in avg_terms(j2,group).items(): pcoef[partition(mask,words)]+=c
    trivial=(tuple(range(len(words))),)
    remaining={str(k):str(v) for k,v in pcoef.items() if v and k!=trivial}
    require(not remaining, 'J2_partition_remainder')
    exponents={p:q*400 for p,q in eavg1.items()}
    require(all(x.denominator==1 for x in exponents.values()),'average_denominator')
    num=math.prod(p**int(e) for p,e in exponents.items() if e>0)
    den=math.prod(p**int(-e) for p,e in exponents.items() if e<0)
    require(8*num<den, 'average_exact_strict')
    approx=sum(float(q)*math.log2(p) for p,q in eavg1.items())
    return {'words':words,'FD_word_pair_vertex_checks':count,
            'local_weights':w1,'local_J1_log2_prime_coefficients':{str(k):str(v) for k,v in e1.items()},
            'local_strict_compare':{'9^8':9**8,'2^25':2**25,'result':True},
            'average_weights':w2,'average_J1_log2_prime_coefficients':{str(k):str(v) for k,v in sorted(eavg1.items())},
            'average_J1_approx_bits_nonproof':approx,
            'average_J1_times_400_prime_exponents':{str(k):str(v) for k,v in sorted(exponents.items())},
            'numerator_bits':num.bit_length(),'denominator_bits':den.bit_length(),
            'eight_times_numerator_less_than_denominator':True,
            'average_J2_exact':str(eavg2), 'J2_all_distributions_partition_remainder':remaining}

def subspace_check():
    # Exhaust all subspaces of F_2^3, all A,B,C,D,Z; conditioning is via sums.
    subs=set()
    for choices in range(1<<7):
        s={0}
        for i in range(7):
            if choices>>i&1:
                v=i+1;s|={x^v for x in list(s)}
        subs.add(tuple(sorted(s)))
    S=sorted(subs); require(len(S)==16,'subspace_count')
    idx={x:i for i,x in enumerate(S)}
    plus=[[idx[tuple(sorted({x^y for x in a for y in b}))] for b in S] for a in S]
    r=[int(math.log2(len(s))) for s in S]
    require(all(2**rr==len(s) for s,rr in zip(S,r)), 'subspace_size')
    def sr(*aa):
        t=aa[0]
        for k in aa[1:]:t=plus[t][k]
        return r[t]
    minimum=999; count=0
    for a,b,c,d,z in product(range(16),repeat=5):
        # Expanded same identity evaluated as dimension sums; independent from FD rows.
        val=(sr(a,c,z)+sr(b,c,z)+sr(a,d,z)+sr(b,d,z)+sr(a,b,z)
             -sr(a,b,c,z)-sr(a,b,d,z)-sr(c,d,z)-sr(a,z)-sr(b,z))
        minimum=min(minimum,val); count+=1
        require(val>=0,'finite_subspace_ingleton')
    return {'ambient':'F_2^3','subspaces':len(S),'conditional_quintuples':count,'minimum_J':minimum}

def controls(doc,group,reps,ordered,index,expected):
    first_cmi=next(i for i,r in enumerate(doc['rows']) if r['metadata']['kind']=='CMI')
    first_j=next(i for i,r in enumerate(doc['rows']) if r['metadata']['kind']=='conditional-ingleton')
    def set_weight(d): d['rows'][first_cmi]['weight']=str(Q(d['rows'][first_cmi]['weight'])+1)
    def negative(d): d['rows'][first_cmi]['weight']='-1'
    def overlap(d): d['rows'][first_j]['metadata']['Z_mask']|=bit(d['rows'][first_j]['metadata']['A'])
    def wrongcap(d): d['caps'][0]['weight']='1'
    def wrongrow(d): d['rows'][first_cmi]['orbit_terms'][0][1]+=1
    tests=[('weight',set_weight,'coefficient_residual'),('negative',negative,'inequality_sign'),
           ('overlap',overlap,'row_input'),('caps',wrongcap,'caps'),('row',wrongrow,'row_mismatch')]
    result={}
    for name,mutation,reason in tests:
        d=deepcopy(doc);mutation(d)
        try: verify(d,group,reps,ordered,index,expected)
        except CheckError as e:
            require(str(e)==reason,'control_wrong_reason');result[name]=reason
        else: raise CheckError('control_not_rejected')
    return result

def main():
    raw,pins=pin_inputs();group,edges,classes=graph_group();reps,ordered,index=orbits(group)
    expect=[(150,{'CMI':64,'conditional-ingleton':83,'FD':3},None),
            (104,{'CMI':99,'conditional-ingleton':2,'FD':3},
             [(2,4,1,3,1008,Q(1,6)),(2,5,3,6,713,Q(1,12))]),
            (66,{'CMI':62,'conditional-ingleton':1,'FD':3},[(2,4,1,3,1008,Q(1,3))])]
    docs=[load(raw[i]) for i in (1,4,9)]
    cert=[verify(d,group,reps,ordered,index,e) for d,e in zip(docs,expect)]
    require(cert[0]['total_ingleton_weight']=='1856350733/320150190','linear_ingleton_sum')
    diamond=diamond_orbit(group,edges);low=lower(edges);wit=witness(group)
    mutation=controls(docs[2],group,reps,ordered,index,expect[2])
    rankcontrol=subspace_check()
    result={'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'manifest_sha256':MANIFEST_SHA,'pins':pins,'graph_edges':len(edges),
      'graph_degree_classes':[len(x) for x in classes],'automorphisms':len(group),
      'all_degree_preserving_permutations_exhausted':math.prod(math.factorial(len(c)) for c in classes),
      'subset_orbits':len(ordered),'singleton_orbits':[sorted({g[v-1]+1 for g in group}) for v in (1,2,3)],
      'certificates':cert,'single_diamond_orbit':diamond,'lower_code':low,'witness':wit,
      'mutation_controls_with_expected_reason':mutation,'subspace_check':rankcontrol,
      'scope':'Exact identities for graph as given; no arbitrary-entropy 20/3 upper bound, no novelty or external-family/formal review.'}
    path=HERE/'review-exact-check-result.json'
    with path.open('x',encoding='utf8') as f: json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps({'certificates':cert,'diamond':diamond,'lower':low,'witness':wit,
                      'controls':mutation,'subspace':rankcontrol,'receipt':str(path)},indent=2))

if __name__=='__main__': main()
