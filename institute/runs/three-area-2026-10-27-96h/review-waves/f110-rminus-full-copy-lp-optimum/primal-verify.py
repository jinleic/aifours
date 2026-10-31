#!/usr/bin/env python3
"""Independently check the pinned three-branch rational primal, exactly.

No author code is imported or executed. The separately compiled scanner uses
first differences to cover all positive n for the original-variable family.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from math import lcm, hypot
from pathlib import Path
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
MANIFEST_HASH = '36bfb4303c5f2c3c1851b8f2bd6141fa2b19e29a1e8d516d67e561b55f811978'
PAPER_HASH = '373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8'
SVG_HASH = '64142da3b73659d5085c072df2b01810d1b455b9f1149a3b30cb19e96402f9b7'
ORIG = tuple('abcdefghij')
AUX = (("b'0",), ("d'1", "e'1", "g'2"), ("f'3", "g'3", "h'4"))
ALL_NAMES = set(ORIG).union(*map(set, AUX))
# Independently transcribed from Fig. 2; the SVG check below binds its strokes.
EDGES = {(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),
         (2,3),(2,7),(2,9),(2,10),(3,4),(3,8),(3,9),
         (4,5),(4,8),(4,10),(5,6),(5,9),(5,10),
         (6,7),(6,8),(6,9),(7,8),(7,10),(8,9),(8,10)}

class Reject(Exception):
    def __init__(self, code, detail=None):
        super().__init__(code, detail)
        self.code, self.detail = code, detail

def require(ok, code, detail=None):
    if not ok:
        raise Reject(code, detail)

def digest(raw):
    return sha256(raw).hexdigest()

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def no_duplicates(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'DUPLICATE_JSON_KEY', key)
        out[key] = value
    return out

def json_exact(raw):
    return json.loads(raw, object_pairs_hook=no_duplicates)

def pin_inputs():
    raw = (ROOT/'manifest-v1.json').read_bytes()
    require(digest(raw) == MANIFEST_HASH, 'MANIFEST_HASH')
    manifest = json_exact(raw)
    sources, facts = [], []
    for item in manifest['inputs_in_read_order']:
        data = Path(item['path']).read_bytes()
        observed = (digest(data), len(data), data.count(b'\n'))
        require(observed == (item['sha256'], item['bytes'], item['LF']),
                'SOURCE_PIN', (item['path'], observed))
        sources.append(data)
        facts.append({'role':item['role'], 'path':item['path'], 'sha256':observed[0],
                      'bytes':observed[1], 'LF':observed[2]})
    require(len(sources) == 10, 'SOURCE_COUNT')
    return sources, facts

def rows_of(doc, field, allowed):
    rows = doc[field]
    require(isinstance(rows, list), 'ROWS_TYPE', field)
    out = {}
    for row in rows:
        require(isinstance(row, dict) and set(row) == {'entropy_variables','value'}, 'ROW_SCHEMA')
        names, text = row['entropy_variables'], row['value']
        require(isinstance(names, list) and names and all(isinstance(x,str) for x in names), 'ROW_NAMES')
        require(len(names) == len(set(names)) and set(names) <= allowed, 'ROW_NAMES', names)
        key = frozenset(names)
        require(key not in out, 'DUPLICATE_COORDINATE', sorted(key))
        require(isinstance(text,str) and re.fullmatch(r'-?\d+(?:/\d+)?',text), 'RATIONAL_FORMAT', text)
        try:
            out[key] = Fraction(text)
        except (ValueError, ZeroDivisionError) as exc:
            raise Reject('RATIONAL_FORMAT',text) from exc
    return out

def named_mask(names, labels):
    out = 0
    for v in names:
        require(v in labels, 'UNKNOWN_VARIABLE', v)
        out |= 1 << labels.index(v)
    return out

def build_profiles(sources):
    base_doc = json_exact(sources[3])
    old = rows_of(base_doc, 'primal_values', ALL_NAMES)
    require(len(old) == len(base_doc['primal_values']) == base_doc['coordinates'] == 4397, 'BASE_TOTAL')
    base = {k:v for k,v in old.items() if k <= set(ORIG)}
    expected_base = {frozenset(ORIG[i] for i in range(10) if mask >> i & 1)
                     for mask in range(1,1<<10)}
    require(set(base) == expected_base, 'ORIGINAL_UNIVERSE', len(base))
    require(Fraction(base_doc['exact_objective']) == Fraction(1847,276), 'DECLARED_OBJECTIVE')
    profiles, old_comparisons = [], []
    for i, aux in enumerate(AUX):
        doc = json_exact(sources[4+i]); labels = ORIG + aux
        require(doc['branch'] == i+1 and doc['variables'] == list(labels), 'BRANCH_LABELS', i+1)
        values = rows_of(doc, 'auxiliary_values', set(labels))
        aux_universe = {frozenset(labels[j] for j in range(len(labels)) if mask >> j & 1)
                        for mask in range(1,1<<len(labels)) if mask & ~1023}
        require(set(values) == aux_universe, 'AUX_UNIVERSE', (i+1,len(values),len(aux_universe)))
        require(doc['fixed_base_coordinates'] == 1023 and
                doc['unknown_auxiliary_coordinates'] == len(aux_universe), 'BRANCH_METADATA', i+1)
        overlaps = set(old) & set(values)
        old_comparisons.append({'branch':i+1,'shared_old_aux':len(overlaps),
                                'changed_old_aux':sum(old[k] != values[k] for k in overlaps)})
        merged = dict(base); merged.update(values)
        scale = lcm(*(x.denominator for x in merged.values()))
        H = [0]*(1<<len(labels))
        for key,value in merged.items():
            H[named_mask(key,labels)] = int(value*scale)
        profiles.append({'labels':labels,'H':H,'scale':scale})
    return base, profiles, old_comparisons

def check_projection(base, profiles):
    for mask in range(1,1024):
        key = frozenset(ORIG[i] for i in range(10) if mask >> i & 1)
        for n,p in enumerate(profiles,1):
            require(Fraction(p['H'][mask],p['scale']) == base[key],
                    'ORIGINAL_PROJECTION_MISMATCH', (n,mask))
    return 1023*len(profiles)

def cycles_to_perm(cycles):
    p = list(range(10))
    for cycle in cycles:
        for i,v in enumerate(cycle):
            p[v-1] = cycle[(i+1)%len(cycle)]-1
    return tuple(p)

def group_generated(generators):
    identity = tuple(range(10)); group = {identity}; todo = [identity]
    while todo:
        p = todo.pop()
        for q in generators:
            r = tuple(p[q[i]] for i in range(10))
            if r not in group:
                group.add(r); todo.append(r)
    return group

def verify_graph():
    paper = (ROOT/'primal-publisher-2024.pdf').read_bytes()
    svg = (ROOT/'primal-graph-page18.svg').read_bytes()
    require(digest(paper) == PAPER_HASH, 'PUBLISHER_PDF_HASH')
    require(digest(svg) == SVG_HASH, 'GRAPH_SVG_HASH')
    # Node centres (and their numeric labels) visually read from Fig. 2.
    centres = {1:(0,0),2:(0,42.919),3:(18.584,10.730),4:(37.167,-21.459),
               5:(0,-21.459),6:(-37.169,-21.459),7:(-18.586,10.730),
               8:(0,85.438),9:(73.994,-42.720),10:(-73.992,-42.720)}
    xml = ET.fromstring(svg)
    transform = 'matrix(0.999096, 0, 0, -0.999096, 245.936549, 180.240056)'
    paths = [x.get('d') for x in xml.iter('{http://www.w3.org/2000/svg}path')
             if x.get('transform') == transform and x.get('fill') == 'none'
             and x.get('stroke') == 'rgb(0%, 0%, 0%)']
    require(len(paths) == 21, 'GRAPH_PATH_COUNT', len(paths))
    def closest(x,y):
        d,v = min((hypot(x-a,y-b),n) for n,(a,b) in centres.items())
        require(d < 2.3, 'GRAPH_ENDPOINT', (x,y,d))
        return v
    edges, triangle_count = set(), 0
    for path in paths:
        toks = re.findall(r'[MLCZ]|[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?',path)
        commands = ''.join(x for x in toks if x in ('M','L','C','Z'))
        nums = [float(x) for x in toks if x not in ('M','L','C','Z')]
        if commands == 'MLLZM':
            triangle_count += 1
            require(len(nums)==8, 'GRAPH_TRIANGLE_TOKENS')
            points = [(nums[k],nums[k+1]) for k in (0,2,4)]
            require([closest(*p) for p in points] == [2,6,4], 'GRAPH_TRIANGLE')
            for j in range(3):
                (x,y),(u,v) = points[j],points[(j+1)%3]
                dx,dy = u-x,v-y; norm = dx*dx+dy*dy
                through = []
                for label,(a,b) in centres.items():
                    t = ((a-x)*dx+(b-y)*dy)/norm
                    distance = hypot(a-(x+t*dx),b-(y+t*dy))
                    if -.02 <= t <= 1.02 and distance < .6:
                        through.append((t,label))
                through.sort()
                require(len(through)==3, 'GRAPH_TRIANGLE_SUBDIVISION', through)
                edges.update(tuple(sorted((through[k][1],through[k+1][1]))) for k in range(2))
        else:
            require(commands in ('ML','MC') and len(nums)==(4 if commands=='ML' else 8),
                    'GRAPH_PATH_FORMAT', commands)
            edges.add(tuple(sorted((closest(*nums[:2]),closest(*nums[-2:])))))
    require(triangle_count == 1 and edges == EDGES, 'GRAPH_EDGE_SET', (len(edges),sorted(edges^EDGES)))
    sigma = cycles_to_perm(((1,8),(2,10,5,9),(3,7,4,6)))
    tau = cycles_to_perm(((2,5),(3,6),(4,7)))
    group = group_generated((sigma,tau))
    require(len(group)==8, 'GROUP_ORDER', len(group))
    def mapped_edges(p):
        return {tuple(sorted((p[a-1]+1,p[b-1]+1))) for a,b in EDGES}
    require(all(mapped_edges(p)==EDGES for p in group), 'GRAPH_AUTOMORPHISM')
    # Exhaust the degree-preserving permutations, not all 10! permutations.
    degree = Counter(v for e in EDGES for v in e)
    classes = {d:tuple(v for v in range(1,11) if degree[v]==d) for d in set(degree.values())}
    require(sorted(map(len,classes.values())) == [2,8], 'GRAPH_DEGREES', dict(degree))
    small = classes[6]; large = classes[5]; automorphisms = set()
    for sp in permutations(small):
        for lp in permutations(large):
            p = [0]*10
            for a,b in zip(small,sp): p[a-1]=b-1
            for a,b in zip(large,lp): p[a-1]=b-1
            if all(tuple(sorted((p[a-1]+1,p[b-1]+1))) in EDGES for a,b in EDGES):
                automorphisms.add(tuple(p))
    require(automorphisms == group, 'FULL_AUTOMORPHISM_GROUP', len(automorphisms))
    return group, {'paper_sha256':digest(paper),'svg_sha256':digest(svg),
                   'selected_black_strokes':len(paths),'edges':len(edges),
                   'edge_list':[list(e) for e in sorted(edges)],
                   'degrees':[degree[i] for i in range(1,11)],
                   'generated_order':len(group),'exhaustive_automorphism_order':len(automorphisms),
                   'degrees_preserving_candidates':80640}

def original_objective(H,scale):
    require(Fraction(H[1023],scale)==Fraction(1847,276), 'OBJECTIVE')

def caps(H,scale):
    for i in range(10):
        require(H[1<<i] <= scale, 'CAP', i+1)
    return 10

def fds(H):
    for v in range(1,11):
        neighbours = [b if a==v else a for a,b in EDGES if v in (a,b)]
        mask = sum(1<<(u-1) for u in neighbours)
        require(H[mask | (1<<(v-1))] == H[mask], 'FD', v)
    return 10

def symmetry(H,group):
    count = 0
    for p in group:
        if p == tuple(range(10)): continue
        for mask in range(1,1024):
            image = sum(1<<p[i] for i in range(10) if mask>>i&1)
            require(H[mask] == H[image], 'SYMMETRY', (mask,image))
            count += 1
    return count

def monotonic(H,n):
    full = (1<<n)-1; count = zeros = 0; least = None
    for i in range(n):
        slack = H[full]-H[full ^ (1<<i)]
        require(slack >= 0, 'ELEMENTAL_MONOTONIC', (i,slack))
        count += 1; zeros += slack==0; least = slack if least is None else min(least,slack)
    return count,zeros,least

def cmis(H,n):
    full = (1<<n)-1; count = zeros = 0; least = None
    for i in range(n):
        for j in range(i+1,n):
            x,y = 1<<i,1<<j; rest = full ^ x ^ y; z=rest
            while True:
                slack = H[z|x]+H[z|y]-H[z|x|y]-H[z]
                require(slack >= 0, 'ELEMENTAL_CMI', (i,j,z,slack))
                count += 1; zeros += slack==0; least = slack if least is None else min(least,slack)
                if not z: break
                z = (z-1)&rest
    return count,zeros,least

def subsets(mask):
    z = mask
    while True:
        yield z
        if not z: break
        z = (z-1)&mask

def copy_specs(number):
    o = ''.join(ORIG)
    if number==1:
        return [(('b',), ("b'0",), tuple('adefghij'), tuple(o))]
    if number==2:
        return [(('d','e'), ("d'1","e'1"), tuple('abcfghi'), tuple(o)),
                (('g',), ("g'2",), tuple('abcd')+("e'1",)+tuple('fhi'), tuple(o)+("d'1","e'1"))]
    return [(('f','g'), ("f'3","g'3"), tuple('abcdehij'), tuple(o)),
            (('h',), ("h'4",), tuple('abcdef')+("f'3",)+tuple('ij'), tuple(o)+("f'3","g'3"))]

def copies(H,labels,number):
    results=[]
    for step,(old,new,cond,past) in enumerate(copy_specs(number),1):
        b=named_mask(cond,labels); p=named_mask(past,labels); nm=named_mask(new,labels)
        require((b&p)==b and (p&nm)==0 and len(old)==len(new), 'COPY_SPEC', (number,step))
        count=0
        for sel in range(1,1<<len(old)):
            orig=named_mask([v for i,v in enumerate(old) if sel>>i&1],labels)
            fresh=named_mask([v for i,v in enumerate(new) if sel>>i&1],labels)
            for s in subsets(b):
                require(H[s|orig] == H[s|fresh], 'COPY_MARGINAL', (number,step,sel,s))
                count += 1
        independence = H[b|nm] + H[p] - H[b] - H[p|nm]
        require(independence==0, 'COPY_INDEPENDENCE', (number,step,independence))
        results.append({'step':step,'matching_subset_equalities':count,'independence_equalities':1})
    return results

def expected_rejection(tag, code, fn):
    try:
        fn()
    except Reject as exc:
        require(exc.code == code, 'CONTROL_WRONG_REASON', (tag,code,exc.code,exc.detail))
        return {'name':tag,'expected':code,'observed':exc.code,'detail':exc.detail}
    raise Reject('CONTROL_ACCEPTED',tag)

def mutation_controls(base, profiles, group, sources):
    out=[]
    for branch,p in enumerate(profiles,1):
        labels,H,scale = p['labels'],p['H'],p['scale']; n=len(labels)
        changed=H.copy(); changed[(1<<n)-1]=changed[((1<<n)-1)^(1<<(n-1))]-1
        out.append(expected_rejection(f'b{branch}_monotonic','ELEMENTAL_MONOTONIC',lambda:monotonic(changed,n)))
        changed=H.copy(); x=1; y=1<<10; changed[x|y]=changed[x]+changed[y]+1
        out.append(expected_rejection(f'b{branch}_cmi','ELEMENTAL_CMI',lambda:cmis(changed,n)))
        changed=H.copy(); changed[1<<10]+=1
        out.append(expected_rejection(f'b{branch}_copy_subset','COPY_MARGINAL',lambda:copies(changed,labels,branch)))
        changed=H.copy(); first=copy_specs(branch)[0]; index=named_mask(first[1]+first[3],labels); changed[index]+=1
        out.append(expected_rejection(f'b{branch}_copy_independence','COPY_INDEPENDENCE',lambda:copies(changed,labels,branch)))
        changed=H.copy(); changed[1]+=1
        altered=[dict(q) for q in profiles]; altered[branch-1]['H']=changed
        out.append(expected_rejection(f'b{branch}_projection','ORIGINAL_PROJECTION_MISMATCH',lambda:check_projection(base,altered)))
    H=profiles[0]['H']; scale=profiles[0]['scale']
    changed=H.copy(); changed[1]=2*scale
    out.append(expected_rejection('original_cap','CAP',lambda:caps(changed,scale)))
    changed=H.copy(); neigh=sum(1<<(u-1) for e in EDGES if 1 in e for u in e if u!=1); changed[neigh|1]+=1
    out.append(expected_rejection('original_fd','FD',lambda:fds(changed)))
    changed=H.copy(); changed[3]+=1
    out.append(expected_rejection('original_symmetry','SYMMETRY',lambda:symmetry(changed,group)))
    changed=H.copy(); changed[1023]+=1
    out.append(expected_rejection('original_objective','OBJECTIVE',lambda:original_objective(changed,scale)))
    doc=json_exact(sources[4]); bad=dict(doc); bad['auxiliary_values']=doc['auxiliary_values']+[doc['auxiliary_values'][0]]
    out.append(expected_rejection('duplicate_aux_coordinate','DUPLICATE_COORDINATE',
                                  lambda:rows_of(bad,'auxiliary_values',set(ORIG+AUX[0]))))
    return out

def main():
    started=clock(); sources,pins=pin_inputs()
    base,profiles,old_comparisons=build_profiles(sources)
    group,graph=verify_graph()
    projection=check_projection(base,profiles)
    branch_results=[]
    for number,p in enumerate(profiles,1):
        H,scale,labels=p['H'],p['scale'],p['labels']; n=len(labels)
        original_objective(H,scale)
        cap_count=caps(H,scale); fd_count=fds(H); sym_count=symmetry(H,group)
        mono_count,mono_zeros,mono_min=monotonic(H,n)
        cmi_count,cmi_zeros,cmi_min=cmis(H,n)
        cp=copies(H,labels,number)
        require((mono_count+cmi_count,sum(x['matching_subset_equalities']+x['independence_equalities'] for x in cp)) ==
                ((28171,257) if number==1 else (159757,642 if number==2 else 1282)), 'BRANCH_COUNTS', number)
        branch_results.append({'branch':number,'labels':list(labels),'coordinate_count':len(H)-1,
                               'common_scale':scale,'objective':str(Fraction(H[1023],scale)),
                               'singletons':[str(Fraction(H[1<<i],scale)) for i in range(10)],
                               'caps':cap_count,'graph_fd':fd_count,'nonidentity_group_symmetry_equalities':sym_count,
                               'elemental_monotonic':mono_count,'elemental_monotonic_zero':mono_zeros,
                               'elemental_monotonic_minimum':str(Fraction(mono_min,scale)),
                               'elemental_cmi':cmi_count,'elemental_cmi_zero':cmi_zeros,
                               'elemental_cmi_minimum':str(Fraction(cmi_min,scale)),'copy_steps':cp})
    controls=mutation_controls(base,profiles,group,sources)
    bscale=lcm(*(f.denominator for f in base.values()))
    baseints=[0]+[int(base[frozenset(ORIG[i] for i in range(10) if mask>>i&1)]*bscale) for mask in range(1,1024)]
    scan=subprocess.run([str(ROOT/'primal-family')], input=' '.join(map(str,baseints))+'\n',
                        text=True,capture_output=True,check=True,timeout=180)
    family=json_exact(scan.stdout); require(family['disjoint_substitutions_mod_ab']==13729980 and
                                             family['minimum_twice_scaled_slack']>=0, 'FAMILY_RESULT')
    result={'started_native_clock':started,'completed_native_clock':clock(),
            'manifest_sha256':MANIFEST_HASH,'input_pins_in_read_order':pins,
            'verifier_sha256':digest(Path(__file__).read_bytes()),
            'family_source_sha256':digest((ROOT/'primal-family.cpp').read_bytes()),
            'family_binary_sha256':digest((ROOT/'primal-family').read_bytes()),
            'family_stdout_sha256':digest(scan.stdout.encode()),'graph':graph,
            'common_original_coordinates':1023,'projection_coordinate_comparisons':projection,
            'distinct_union_coordinates':1023+sum((1<<len(p['labels']))-1024 for p in profiles),
            'branch_results':branch_results,'old_partial_comparisons':old_comparisons,
            'base_scale_for_family':bscale,'family_scan':family,'controls':controls,
            'limits':'Primal only. Branches share originals but contain no mixed cross-branch Shannon rows. Graph labels are visually transcribed from publisher figure; vector paths independently checked. No entropic realization, dual review, formal proof, human/cross-family review, or priority claim.'}
    target=ROOT/'primal-receipt-v1.json'
    with target.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False); f.write('\n')
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':
    try: main()
    except (Reject,subprocess.SubprocessError) as exc:
        print('FAILED:',repr(exc),file=sys.stderr); sys.exit(1)
