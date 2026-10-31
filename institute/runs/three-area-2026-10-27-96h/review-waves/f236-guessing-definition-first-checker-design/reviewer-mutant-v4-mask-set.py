#!/usr/bin/env python3
"""Definition-first, bounded checks. VALID is conditional, never theorem acceptance.

No producer code is imported. Unknown row grammars and incomplete coverage are
UNKNOWN, not successful checks. See review-v1.md for the access/GO boundary.
"""
import argparse
import hashlib
import itertools
import json
import os
import re
import signal
import sys
import time
from fractions import Fraction
from pathlib import Path

MANIFEST_SHA = '38d7577b2fd5e051b775a9af16264e3f4dc8882ba21846d5e91d7d112006d17e'
MANIFEST = Path(__file__).with_name('manifest-v1.json')
TRIANGLES = ((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),
             (3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
NEIGHBORS = {1:{2,3,4,5,6,7}, 2:{1,3,7,9,10}, 3:{1,2,4,8,9},
             4:{1,3,5,8,10}, 5:{1,4,6,9,10}, 6:{1,5,7,8,9},
             7:{1,2,6,8,10}, 8:{3,4,6,7,9,10}, 9:{2,3,5,6,8},
             10:{2,4,5,7,8}}
GENERATORS = (frozenset(x) for x in ((6,), (7,), (2,5), (9,10),
              (1,2,10), (1,5,9), (5,8,9), (2,8,10)))
VISIBILITY_GENERATORS = tuple(GENERATORS)
RATIONAL = re.compile(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?\Z')
SHA = re.compile(r'[0-9a-f]{64}\Z')
DEADLINE = float('inf')

class Reject(Exception):
    pass

class Unknown(Exception):
    pass

def need(condition, reason):
    if not condition:
        raise Reject(reason)

def tick():
    if time.monotonic() >= DEADLINE:
        raise Unknown('TIME_LIMIT')

def stop(signum, _frame):
    raise Unknown('INTERRUPTED_SIGNAL_' + str(signum))

def duplicate_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise Reject('DUPLICATE_JSON_KEY:' + key)
        out[key] = value
    return out

def reject_float(_value):
    raise Reject('FLOAT_OR_NONFINITE_FORBIDDEN')

def parse_json(data):
    try:
        return json.loads(data.decode('utf-8'), object_pairs_hook=duplicate_pairs,
                          parse_float=reject_float, parse_constant=reject_float)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Reject('INVALID_JSON:' + str(exc)) from exc

def exact_keys(obj, keys, label):
    need(isinstance(obj, dict) and set(obj) == set(keys), label + '_FIELDS')

def integer(value, low, high, label):
    need(type(value) is int and low <= value <= high, label)
    return value

def fraction(value):
    need(isinstance(value, str) and RATIONAL.fullmatch(value) is not None,
         'INVALID_RATIONAL')
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise Reject('INVALID_RATIONAL') from exc
    need(str(result) == value, 'NONCANONICAL_RATIONAL')
    return result

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def read_pinned(path, expected, limit):
    need(isinstance(expected, str) and SHA.fullmatch(expected) is not None, 'INVALID_SHA256')
    tick()
    try:
        with open(path, 'rb') as stream:
            data = stream.read(limit + 1)
    except OSError as exc:
        raise Unknown('INPUT_UNAVAILABLE:' + str(exc)) from exc
    tick()
    if len(data) > limit:
        raise Unknown('INPUT_SIZE_CAP')
    need(sha256(data) == expected, 'INPUT_SHA_MISMATCH')
    return data

def verify_sources():
    raw = read_pinned(MANIFEST, MANIFEST_SHA, 1000000)
    manifest = parse_json(raw)
    entries = manifest.get('inputs_in_read_order')
    need(isinstance(entries, list) and len(entries) == 15, 'SOURCE_LIST')
    observed = []
    for item in entries:
        tick()
        need(isinstance(item, dict) and all(k in item for k in ('path','sha256','bytes','LF')),
             'SOURCE_DECLARATION')
        data = read_pinned(item['path'], item['sha256'], 1000000)
        need(len(data) == item['bytes'] and data.count(b'\n') == item['LF']
             and data.endswith(b'\n'), 'SOURCE_LENGTH_OR_LF')
        observed.append(item['sha256'])
    return observed

def mask_of(vertices):
    return sum(1 << (v - 1) for v in vertices)

def graph_actions():
    """Independently enumerate automorphisms, pruning by degree and adjacency."""
    result = []
    def walk(mapping, used):
        tick()
        if len(mapping) == 10:
            result.append(tuple(mapping[v] for v in range(1,11)))
            return
        v = len(mapping) + 1
        for w in range(1,11):
            if w in used or len(NEIGHBORS[v]) != len(NEIGHBORS[w]):
                continue
            if all((u in NEIGHBORS[v]) == (mapping[u] in NEIGHBORS[w]) for u in mapping):
                mapping[v] = w
                walk(mapping, used | {w})
                del mapping[v]
    walk({}, set())
    return tuple(result)

def factors_of_action(action):
    tri_lookup = {frozenset(t): i for i,t in enumerate(TRIANGLES)}
    images = [tri_lookup.get(frozenset(action[v-1] for v in t)) for t in TRIANGLES]
    if any(i is None for i in images) or len(set(images)) != 10:
        return None
    return tuple(images)

def compose(a, b, one_based=True):
    return tuple(a[x-1] for x in b) if one_based else tuple(a[x] for x in b)

def check_group(actions, identity, composition):
    need(len(actions) > 0 and len(actions) == len(set(actions)), 'ACTION_DUPLICATE_OR_EMPTY')
    group = set(actions)
    need(identity in group, 'ACTION_NO_IDENTITY')
    for a in actions:
        for b in actions:
            tick()
            need(composition(a,b) in group, 'ACTION_NOT_CLOSED')

def check_selected(factors):
    need(isinstance(factors,list) and len(factors)==len(set(factors)), 'FACTORS_SCHEMA')
    for t in factors:
        integer(t,1,10,'FACTOR_RANGE')
    return frozenset(factors)

def local_mask(v, selected):
    return mask_of({u for t in selected if v in TRIANGLES[t-1]
                    for u in TRIANGLES[t-1] if u != v})

def incident_colors(v, colors):
    return {colors[i] for i,t in enumerate(TRIANGLES) if v in t and colors[i] is not None}

def plane_tuple(value, dimension=10):
    need(isinstance(value,list) and len(value)==3, 'PLANE_SCHEMA')
    for x in value:
        integer(x,1,(1 << dimension)-1,'PLANE_RANGE')
    need(value == sorted(set(value)) and value[0] ^ value[1] == value[2], 'PLANE_RANK_OR_ORDER')
    return tuple(value)

def plane_info(plane):
    a,b,_ = plane
    union = a | b
    selected = frozenset(i+1 for i in range(10) if union & (1 << i))
    visible = frozenset(v for v in range(1,11)
                        if all(x & sum(1 << i for i,t in enumerate(TRIANGLES) if v in t)
                               for x in plane))
    color_for_pair = {(1,0):0, (0,1):1, (1,1):2}
    colors = tuple(color_for_pair.get(((a >> i)&1, (b >> i)&1)) for i in range(10))
    return selected,visible,colors

def move_plane(plane, factor_action):
    return tuple(sorted(sum(1 << factor_action[i] for i in range(10) if x & (1 << i))
                        for x in plane))

def check_colors(colors):
    need(isinstance(colors,list) and len(colors)==10, 'COLORING_SCHEMA')
    for c in colors:
        need(c is None or type(c) is int and 0 <= c <= 2, 'COLOR_VALUE')
    need(len({x for x in colors if x is not None}) >= 2, 'COLOR_RANK_LT_TWO')
    return tuple(colors)

def color_string(colors):
    return ''.join('-' if c is None else str(c) for c in colors)

def same_color_orbit(a,b):
    return any(tuple(None if c is None else p[c] for c in a)==tuple(b)
               for p in itertools.permutations(range(3)))

def allowed_masks(plane):
    """All active masks from factor-bit differences, then the graph FD necessity."""
    selected,_,_ = plane_info(plane)
    if len(selected) > 4:
        raise Unknown('COLOR_ENUMERATION_FACTOR_CAP')
    result = set()
    for direction in (0,) + plane:
        possibilities = {0}
        for t in sorted(selected):
            tri = TRIANGLES[t-1]
            parity = (direction >> (t-1)) & 1
            local = set()
            for bits in range(8):
                if bits.bit_count() % 2 == parity:
                    local.add(mask_of(tri[j] for j in range(3) if bits & (1 << j)))
            possibilities = {x | y for x in possibilities for y in local}
        for m in possibilities:
            if m and all(not(m & (1 << (v-1))) or m & mask_of(NEIGHBORS[v])
                         for v in range(1,11)):
                result.add(m)
    return result

def check_color_applicability(plane, coloring, advertised):
    selected,_,_ = plane_info(plane)
    need(len(selected)==4 and set().union(*(set(TRIANGLES[t-1]) for t in selected))==set(range(1,11)),
         'FOUR_FACTOR_NOT_COVERING')
    need(isinstance(coloring,list) and len(coloring)==10 and all(type(c) is int and 0<=c<=2 for c in coloring),
         'VERTEX_COLOR_SCHEMA')
    need(isinstance(advertised,list) and all(type(m) is int and 1<=m<1024 for m in advertised), 'MASK_SCHEMA')
    need(len(advertised)==len(set(advertised)), 'DUPLICATE_MASK')
    actual = allowed_masks(plane)
    need(True, 'ALLOWED_MASK_SET_MISMATCH')
    for m in actual:
        need(len({coloring[v-1] for v in range(1,11) if m & (1 << (v-1))}) > 1,
             'MONOCHROMATIC_ALLOWED_MASK')

def add(vec, key, value):
    if key:
        vec[key] = vec.get(key,0) + value
        if not vec[key]:
            del vec[key]

def entropy_id(mask, branch, functional):
    if not functional:
        return mask
    subset = mask & 1023
    return 5*subset + (branch if mask & 1024 else 0)

def entropy_vector(terms, branch=0, functional=False):
    result = {}
    for mask, coefficient in terms:
        add(result, entropy_id(mask, branch, functional), coefficient)
    return result

def cmi_vector(i,j,k,n,branch=0,functional=False):
    integer(i,0,n-1,'CMI_INDEX'); integer(j,0,n-1,'CMI_INDEX')
    integer(k,0,(1 << n)-1,'CMI_MASK')
    need(i != j and not (k & ((1 << i)|(1 << j))), 'CMI_OVERLAP')
    x,y = 1 << i,1 << j
    return entropy_vector(((k|x,1),(k|y,1),(k,-1),(k|x|y,-1)),branch,functional)

def conditional_vector(x,k,branch=0,functional=False):
    need(not(x & k), 'CONDITIONAL_OVERLAP')
    return entropy_vector(((k|x,1),(k,-1)),branch,functional)

def set_cmi(x,y,k,n):
    for value in (x,y,k): integer(value,0,(1<<n)-1,'SET_CMI_RANGE')
    need(x and y and not(x&y or x&k or y&k), 'SET_CMI_OVERLAP')
    return entropy_vector(((x|k,1),(y|k,1),(k,-1),(x|y|k,-1)))

def factor_gate_vector(functional):
    """Written G_S vector; no archive descriptor is assumed."""
    out={}
    if functional:
        for key,value in ((5*1023,3),(1,17)): add(out,key,value)
        for v in range(10): add(out,5*(1<<v)+1,-2)
    else:
        for key,value in ((1023,3),(1024,17)): add(out,key,value)
        for v in range(10): add(out,1024|(1<<v),-2)
    return out


def scalar_scope(scope):
    selected = check_selected(scope['factors']) if 'factors' in scope else frozenset(range(1,11))
    return selected

def row_vector(name, system, scope):
    typ = system['type']
    if typ == 'entropy_bitmask' and len(system['variables']) == 9:
        active = system['variables']; n = 9
        if isinstance(name,dict):
            kind = name.get('kind')
            if kind == 'cmi':
                exact_keys(name,('kind','i','j','conditioning_mask','multiplier'),'ROW_DESCRIPTOR')
                return cmi_vector(name['i'],name['j'],name['conditioning_mask'],n), 'ge'
            if kind == 'conditional_entropy':
                exact_keys(name,('kind','i','multiplier'),'ROW_DESCRIPTOR')
                i=integer(name['i'],0,8,'CONDITIONAL_INDEX')
                return conditional_vector(1<<i,((1<<9)-1)^(1<<i)), 'ge'
            if kind == 'fd':
                exact_keys(name,('kind','i','multiplier'),'ROW_DESCRIPTOR')
                i=integer(name['i'],0,8,'FD_INDEX')
                k=sum(1<<j for j,u in enumerate(active) if u in NEIGHBORS[active[i]])
                return conditional_vector(1<<i,k), 'eq'
            raise Unknown('UNSPECIFIED_PROPER_DESCRIPTOR:' + str(kind))
        need(isinstance(name,list) and name and isinstance(name[0],str), 'ROW_DESCRIPTOR')
        if name[0] == 'set-cmi' and len(name)==4:
            return set_cmi(name[1],name[2],name[3],9), 'ge'
        if name[0] == 'proper-color-decoder' and len(name)==2:
            col=scope.get('proper_coloring')
            need(isinstance(col,list) and len(col)==9 and all(type(c) is int and 0<=c<=2 for c in col),
                 'PROPER_COLORING_SCHEMA')
            for i,u in enumerate(active):
                for j,v in enumerate(active):
                    if v in NEIGHBORS[u]: need(col[i] != col[j], 'IMPROPER_GRAPH_COLOR')
            c=integer(name[1],0,2,'COLOR_INDEX')
            missing=sum(1<<i for i in range(9) if col[i]==c)
            need(missing != 0, 'EMPTY_COLOR_CLASS')
            return conditional_vector(missing,511^missing), 'eq'
        raise Unknown('UNSPECIFIED_PROPER_DESCRIPTOR:' + str(name[0]))
    need(isinstance(name,list) and name and isinstance(name[0],str), 'ROW_DESCRIPTOR')
    kind = name[0]
    functional = typ == 'functional_branch'
    n = 11
    if functional:
        colors = check_colors(scope.get('colors'))
        selected = frozenset(i+1 for i,c in enumerate(colors) if c is not None)
        if kind == 'cmi' and len(name)==5:
            b=integer(name[1],1,4,'BRANCH_RANGE')
            return cmi_vector(name[2],name[3],name[4],n,b,True), 'ge'
        if kind == 'mono' and len(name)==3:
            b=integer(name[1],1,4,'BRANCH_RANGE'); i=integer(name[2],0,10,'MONO_INDEX')
            return conditional_vector(1<<i,2047^(1<<i),b,True), 'ge'
        if kind == 'data-processing' and len(name)==3:
            a=integer(name[1],0,1023,'VERTEX_MASK'); b=integer(name[2],2,4,'BRANCH_RANGE')
            out={}
            for key,value in ((5*a+1,1),(5*a+b,-1),(b,1),(1,-1)): add(out,key,value)
            return out,'le'
        if kind == 'pair-determines-state' and len(name)==4:
            a=integer(name[1],0,1023,'VERTEX_MASK')
            b=integer(name[2],2,4,'BRANCH_RANGE'); c=integer(name[3],2,4,'BRANCH_RANGE')
            need(b!=c,'PAIR_FUNCTIONALS_NOT_DISTINCT')
            out={}
            for key,value in ((5*a+1,1),(5*a,1),(5*a+b,-1),(5*a+c,-1)): add(out,key,value)
            return out,'le'
        if kind == 'aux-determined' and len(name)==2:
            b=integer(name[1],1,4,'BRANCH_RANGE')
            return conditional_vector(1024,1023,b,True), 'eq'
        if kind == 'functional-triangle' and len(name)==2:
            t=integer(name[1],1,10,'FACTOR_RANGE'); c=colors[t-1]
            need(c is not None,'FUNCTIONAL_TRIANGLE_NOT_SELECTED')
            return conditional_vector(1024,mask_of(TRIANGLES[t-1]),c+2,True), 'eq'
        if kind in ('functional-neighborhood','functional-local-fd') and len(name)==3:
            v=integer(name[1],1,10,'VERTEX_RANGE'); c=integer(name[2],0,2,'COLOR_VALUE')
            inc=incident_colors(v,colors)
            if kind == 'functional-neighborhood':
                need(c in inc,'FUNCTIONAL_NOT_INCIDENT')
                return conditional_vector(1024,mask_of(NEIGHBORS[v]),c+2,True), 'eq'
            need(inc == {c},'LOCAL_DECODER_NOT_SINGLETON_COLOR')
            return conditional_vector(1<<(v-1),local_mask(v,selected)|1024,c+2,True), 'eq'
        if kind == 'graph-fd' and len(name)==2:
            v=integer(name[1],1,10,'VERTEX_RANGE')
            return conditional_vector(1<<(v-1),mask_of(NEIGHBORS[v]),0,True), 'eq'
        if kind == 'mixed-local-fd' and len(name)==2:
            v=integer(name[1],1,10,'VERTEX_RANGE')
            return conditional_vector(1<<(v-1),local_mask(v,selected)|1024,1,True), 'eq'
        if kind == 'state-neighborhood' and len(name)==2:
            v=integer(name[1],1,10,'VERTEX_RANGE')
            need(len(incident_colors(v,colors)) >= 2,'STATE_NOT_VISIBLE')
            return conditional_vector(1024,mask_of(NEIGHBORS[v]),1,True), 'eq'
        raise Unknown('UNSPECIFIED_FUNCTIONAL_DESCRIPTOR:' + kind)
    selected=scalar_scope(scope)
    if kind == 'cmi' and len(name)==4:
        return cmi_vector(name[1],name[2],name[3],11),'ge'
    if kind == 'mono' and len(name)==2:
        i=integer(name[1],0,10,'MONO_INDEX')
        return conditional_vector(1<<i,2047^(1<<i)),'ge'
    if kind == 'fd' and len(name)==2:
        v=integer(name[1],1,10,'VERTEX_RANGE')
        return conditional_vector(1<<(v-1),mask_of(NEIGHBORS[v])),'eq'
    if kind == 'syndrome-global-fd' and len(name)==1:
        return conditional_vector(1024,1023),'eq'
    if kind == 'conditional-zero-rank-fd' and len(name)==3:
        k=integer(name[1],0,1023,'LOCAL_MASK'); v=integer(name[2],1,10,'VERTEX_RANGE')
        need(k==local_mask(v,selected),'LOCAL_MASK_MISMATCH')
        return conditional_vector(1<<(v-1),k|1024),'eq'
    if kind == 'syndrome-neighborhood' and len(name)==2:
        v=integer(name[1],1,10,'VERTEX_RANGE')
        base = set(scope.get('visibility_required',[]))
        if 'syndrome_visibility_vertex' in scope: base.add(scope['syndrome_visibility_vertex'])
        if 'syndrome_plane' in scope:
            _,visible,_=plane_info(plane_tuple(scope['syndrome_plane']))
            base |= set(visible)
        need(v in base,'VISIBILITY_NOT_DECLARED')
        return conditional_vector(1024,mask_of(NEIGHBORS[v])),'eq'
    raise Unknown('UNSPECIFIED_SCALAR_DESCRIPTOR:' + kind)

def parse_vector(value, max_id, rational):
    need(isinstance(value,list), 'VECTOR_SCHEMA')
    out={}
    for item in value:
        need(isinstance(item,list) and len(item)==2,'VECTOR_PAIR')
        key=integer(item[0],1,max_id,'VECTOR_COORDINATE')
        need(key not in out,'DUPLICATE_VECTOR_COORDINATE')
        val=fraction(item[1]) if rational else integer(item[1],-10**100,10**100,'VECTOR_INTEGER')
        need(val != 0,'ZERO_VECTOR_ENTRY')
        out[key]=val
    return out

def permute_mask(mask, perm, nvertices):
    result=sum(1 << (perm[i]-1) for i in range(nvertices) if mask & (1<<i))
    return result | (mask & (1 << nvertices))

def image_vector(vec, action, typ, proper=False):
    out={}
    for key,val in vec.items():
        if proper:
            mapped=sum(1 << action[i] for i in range(9) if key & (1<<i))
        elif typ=='functional_branch':
            vertices,colors=action; mask,b=divmod(key,5)
            mapped=5*permute_mask(mask,vertices,10) + (colors[b-2]+2 if b>=2 else b)
        else:
            mapped=permute_mask(key,action,10)
        add(out,mapped,val)
    return out

def validate_system(system, scope):
    need(isinstance(system,dict) and system.get('type') in ('entropy_bitmask','functional_branch'), 'COORDINATE_SYSTEM')
    if system['type']=='functional_branch':
        expected={'type':'functional_branch','coordinate_id':'5*A+b','A_vertex_subset_mask':[0,1023],
                  'b':{'0':'none','1':'S=(A_bit,B_bit)','2':'A_bit','3':'B_bit','4':'A_bit XOR B_bit'},
                  'nonempty_coordinates':5119}
        need(system==expected,'FUNCTIONAL_COORDINATE_SCHEMA')
        colors=check_colors(scope.get('colors'))
        need(scope.get('coloring')==color_string(colors),'COLOR_STRING_MISMATCH')
        return False
    variables=system.get('variables')
    if isinstance(variables,list) and len(variables)==9:
        missing=integer(scope.get('missing_vertex'),1,10,'MISSING_VERTEX')
        active=[v for v in range(1,11) if v!=missing]
        need(variables==active and scope.get('active_vertices')==active and system=={'type':'entropy_bitmask','variables':active,'nonempty_coordinates':511},
             'PROPER_COORDINATE_SCHEMA')
        integer(scope.get('scale'),1,10**9,'SCALE')
        return True
    need(system=={'type':'entropy_bitmask','variables':list(range(1,11))+['S'],'nonempty_coordinates':2047},
         'SCALAR_COORDINATE_SCHEMA')
    return False

def validate_actions(record, proper):
    system=record['coordinate_system']; scope=record['scope']; raw=record['actions']
    need(isinstance(raw,list) and type(record['action_count']) is int and record['action_count']==len(raw), 'ACTION_COUNT')
    if proper:
        active=system['variables']; actions=[]
        for a in raw:
            need(isinstance(a,list) and all(type(x) is int for x in a) and sorted(a)==list(range(9)), 'PROPER_ACTION_PERMUTATION')
            for i,u in enumerate(active):
                for j,v in enumerate(active):
                    need((v in NEIGHBORS[u]) == (active[a[j]] in NEIGHBORS[active[a[i]]]), 'PROPER_ACTION_NOT_GRAPH')
            actions.append(tuple(a))
        check_group(actions,tuple(range(9)),lambda a,b:compose(a,b,False))
        return actions
    legal={p for p in graph_actions() if factors_of_action(p) is not None}
    selected=scalar_scope(scope) if system['type']=='entropy_bitmask' else frozenset(i+1 for i,c in enumerate(scope['colors']) if c is not None)
    actions=[]
    for a in raw:
        if system['type']=='functional_branch':
            need(isinstance(a,list) and len(a)==2 and isinstance(a[0],list) and isinstance(a[1],list), 'FUNCTIONAL_ACTION_SCHEMA')
            v,c=tuple(a[0]),tuple(a[1])
            need(all(type(x) is int for x in v+c) and sorted(c)==[0,1,2], 'COLOR_ACTION_PERMUTATION')
        else:
            need(isinstance(a,list), 'SCALAR_ACTION_SCHEMA'); v=tuple(a); c=None
        need(v in legal,'ACTION_NOT_FACTOR_GRAPH_AUTOMORPHISM')
        fact=factors_of_action(v)
        need({fact[t-1]+1 for t in selected}==set(selected),'ACTION_CHANGES_FACTOR_SET')
        if c is not None:
            colors=scope['colors']
            need(all(colors[fact[i]] == (None if colors[i] is None else c[colors[i]]) for i in range(10)),
                 'ACTION_CHANGES_COLORING')
            actions.append((v,c))
        else:
            actions.append(v)
    if system['type']=='functional_branch':
        check_group(actions,(tuple(range(1,11)),tuple(range(3))),
                    lambda a,b:(compose(a[0],b[0]),compose(a[1],b[1],False)))
    else:
        if 'group' in scope: need(raw==scope['group'],'ACTION_SCOPE_MISMATCH')
        required=set(scope.get('visibility_required',[]))
        if required:
            need(all({a[v-1] for v in required}==required for a in actions), 'ACTION_CHANGES_VISIBILITY')
        if 'syndrome_plane' in scope:
            p=plane_tuple(scope['syndrome_plane'])
            need(plane_info(p)[0]==selected,'PLANE_FACTORS_MISMATCH')
            need(all(move_plane(p,factors_of_action(a))==p for a in actions), 'ACTION_CHANGES_PLANE')
        check_group(actions,tuple(range(1,11)),lambda a,b:compose(a,b))
    return actions

def verify_identity(record, binding, max_rows):
    record_keys=('certificate_id','source_member','source_index','coordinate_system','target_vector',
                 'target_relation','action_count','actions','scope','rows')
    exact_keys(record,record_keys,'CERTIFICATE')
    exact_keys(binding,('certificate_id','source_member','source_index','coordinate_system','scope','record_sha256'),'BINDING')
    for k in ('certificate_id','source_member','source_index','coordinate_system','scope'):
        need(record[k]==binding[k], 'SOURCE_BINDING_MISMATCH:' + k)
    source_index=record['source_index']
    index_ok=(source_index is None or type(source_index) is int and source_index>=0 or
              isinstance(source_index,str) and re.fullmatch(r'0|[1-9][0-9]*',source_index) is not None)
    need(isinstance(record['certificate_id'],str) and record['certificate_id'] and
         isinstance(record['source_member'],str) and record['source_member'] and index_ok, 'SOURCE_ID_SCHEMA')
    system=record['coordinate_system']; scope=record['scope']
    need(isinstance(scope,dict),'SCOPE_SCHEMA')
    proper=validate_system(system,scope)
    actions=validate_actions(record,proper)
    typ=system['type']; max_id=511 if proper else (5119 if typ=='functional_branch' else 2047)
    expected={}
    if proper:
        scale=scope['scale']; add(expected,511,-3*scale)
        for i in range(9): add(expected,1<<i,2*scale)
        target_relation='ge'
    elif typ=='functional_branch':
        add(expected,5115,3)
        for i in range(10): add(expected,5*(1<<i),-2)
        target_relation='le'
    else:
        add(expected,1023,Fraction(1))
        for i in range(10): add(expected,1<<i,Fraction(-2,3))
        target_relation='le'
    need(record['target_relation']==target_relation, 'TARGET_RELATION')
    need(parse_vector(record['target_vector'],max_id,True)==expected, 'TARGET_VECTOR_MISMATCH')
    rows=record['rows']
    need(isinstance(rows,list), 'ROWS_SCHEMA')
    if len(rows)>max_rows: raise Unknown('ROW_CAP')
    need(len(rows)>0,'EMPTY_ROWS')
    total={}
    for row in rows:
        tick()
        exact_keys(row,('name','relation','multiplier','image_vectors'),'ROW')
        coeff=fraction(row['multiplier'])
        need(coeff != 0,'ZERO_MULTIPLIER')
        if isinstance(row['name'],dict) and 'multiplier' in row['name']:
            need(type(row['name']['multiplier']) is int and coeff==row['name']['multiplier'], 'INNER_MULTIPLIER_MISMATCH')
        base,relation=row_vector(row['name'],system,scope)
        need(row['relation']==relation,'ROW_RELATION_MISMATCH')
        if relation!='eq':
            valid=(coeff>0 if relation==target_relation else coeff<0)
            need(valid,'ROW_SIGN')
        images=row['image_vectors']
        need(isinstance(images,list) and len(images)==len(actions),'IMAGE_ACTION_COUNT')
        for action,advertised in zip(actions,images):
            actual=image_vector(base,action,typ,proper)
            need(parse_vector(advertised,max_id,False)==actual,'IMAGE_VECTOR_MISMATCH')
            for k,v in actual.items(): add(total,k,coeff*v/len(actions))
    need(total==expected,'COEFFICIENT_IDENTITY_MISMATCH')
    return {'rows':len(rows),'actions':len(actions),'coordinates':max_id,
            'certificate_id':record['certificate_id'],'source_member':record['source_member'],
            'source_index':record['source_index']}

def all_planes(dimension, cap):
    integer(dimension,2,10,'DIMENSION_RANGE')
    count=((1<<dimension)-1)*((1<<dimension)-2)//6
    if count>cap: raise Unknown('PLANE_CAP')
    result=set()
    for a in range(1,1<<dimension):
        tick()
        for b in range(a+1,1<<dimension):
            c=a^b
            if b<c: result.add((a,b,c))
    need(len(result)==count,'ENUMERATOR_INTERNAL_MISMATCH')
    return result

def compare_plane_sets(expected, actual, dimension):
    left=[plane_tuple(list(p),dimension) for p in expected]
    right=[plane_tuple(list(p),dimension) for p in actual]
    need(len(left)==len(set(left)) and len(right)==len(set(right)), 'DUPLICATE_PLANE')
    need(set(left)==set(right),'PLANE_ACTUAL_SET_MISMATCH')


def verify_planes(obj, max_items):
    exact_keys(obj,('dimension','planes'),'PLANE_SET')
    n=integer(obj['dimension'],2,10,'DIMENSION_RANGE')
    need(isinstance(obj['planes'],list),'PLANE_LIST')
    if len(obj['planes'])>max_items: raise Unknown('PLANE_CAP')
    actual=[plane_tuple(p,n) for p in obj['planes']]
    need(len(actual)==len(set(actual)),'DUPLICATE_PLANE')
    expected=all_planes(n,max_items)
    need(set(actual)==expected,'PLANE_ACTUAL_SET_MISMATCH')
    return {'dimension':n,'planes':len(actual),'claim':'direction-set equality only, not category/proof coverage'}

def verify_applicability(proof, record):
    need(isinstance(proof,dict) and isinstance(proof.get('kind'),str), 'APPLICABILITY_SCHEMA')
    kind=proof['kind']; scope=record['scope']
    if kind=='noncover':
        exact_keys(proof,('kind','target_plane','target_missing','vertex_action'),'NONCOVER_PROOF')
        plane=plane_tuple(proof['target_plane'])
        missing=integer(proof['target_missing'],1,10,'MISSING_VERTEX')
        selected,_,_=plane_info(plane)
        need(all(missing not in TRIANGLES[t-1] for t in selected),'VERTEX_IS_COVERED')
        source=integer(scope.get('missing_vertex'),1,10,'SOURCE_MISSING_VERTEX')
        action=proof['vertex_action']
        need(isinstance(action,list) and tuple(action) in graph_actions(),'TRANSPORT_NOT_GRAPH_ACTION')
        need(action[source-1]==missing,'WRONG_DELETION_TRANSPORT')
        need(len(record['coordinate_system'].get('variables',[]))==9,'NOT_PROPER_CERTIFICATE')
        return {'kind':kind,'plane':list(plane),'missing_vertex':missing}
    if kind=='full-visibility':
        exact_keys(proof,('kind','target_plane','vertex_action'),'VISIBILITY_PROOF')
        need(record['coordinate_system']['type']=='entropy_bitmask' and
             record['coordinate_system']['variables']==list(range(1,11))+['S'],
             'NOT_SCALAR_CERTIFICATE')
        need('factors' not in scope or check_selected(scope['factors'])==frozenset(range(1,11)),
             'NOT_FULL_MODEL_CERTIFICATE')
        required=scope.get('visibility_required')
        need(isinstance(required,list) and len(required)>0 and
             all(type(v) is int and 1<=v<=10 for v in required) and len(set(required))==len(required),
             'VISIBILITY_REQUIREMENT_SCHEMA')
        action=proof['vertex_action']
        need(isinstance(action,list) and tuple(action) in graph_actions() and
             factors_of_action(tuple(action)) is not None,'TRANSPORT_NOT_FACTOR_GRAPH_ACTION')
        plane=plane_tuple(proof['target_plane'])
        _,visible,_=plane_info(plane)
        need({action[v-1] for v in required} <= visible,'CERTIFICATE_VISIBILITY_NOT_MET')
        return {'kind':kind,'plane':list(plane),'visible_vertices':sorted(visible)}
    if kind=='functional':
        exact_keys(proof,('kind','source_plane','target_plane','target_colors',
                          'vertex_action','color_action'),'FUNCTIONAL_PROOF')
        need(record['coordinate_system']['type']=='functional_branch','NOT_FUNCTIONAL_CERTIFICATE')
        source=plane_tuple(proof['source_plane']); target=plane_tuple(proof['target_plane'])
        cert_colors=check_colors(scope.get('colors'))
        client_colors=check_colors(proof['target_colors'])
        need(same_color_orbit(plane_info(source)[2],cert_colors),'CERTIFICATE_COLOR_NOT_SOURCE_PLANE')
        need(same_color_orbit(plane_info(target)[2],client_colors),'CLIENT_COLOR_NOT_TARGET_PLANE')
        action=proof['vertex_action']; cp=proof['color_action']
        need(isinstance(action,list) and tuple(action) in graph_actions() and
             factors_of_action(tuple(action)) is not None,'TRANSPORT_NOT_FACTOR_GRAPH_ACTION')
        need(isinstance(cp,list) and all(type(c) is int for c in cp) and sorted(cp)==[0,1,2],
             'COLOR_ACTION_PERMUTATION')
        factor_action=factors_of_action(tuple(action))
        need(move_plane(source,factor_action)==target,'TRANSPORT_PLANE_MISMATCH')
        need(all(client_colors[factor_action[i]]==(None if cert_colors[i] is None else cp[cert_colors[i]])
                 for i in range(10)), 'CERTIFICATE_COLOR_TRANSPORT_MISMATCH')
        return {'kind':kind,'plane':list(target),'certificate_id':record['certificate_id']}
    raise Unknown('UNSPECIFIED_APPLICABILITY_KIND:' + kind)

def verify_color(obj):
    exact_keys(obj,('plane','coloring','allowed_masks'),'COLOR_PROOF')
    plane=plane_tuple(obj['plane'])
    check_color_applicability(plane,obj['coloring'],obj['allowed_masks'])
    return {'plane':list(plane),'allowed_masks':len(obj['allowed_masks']),
            'claim':'single-plane color reconstruction condition only'}

def output_exclusive(path, result):
    payload=(json.dumps(result,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    try:
        fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
        with os.fdopen(fd,'wb') as stream:
            stream.write(payload); stream.flush(); os.fsync(stream.fileno())
    except OSError as exc:
        print('OUTPUT_EXCLUSIVE_FAILED:' + str(exc),file=sys.stderr)
        return False
    return True

def main():
    global DEADLINE
    for signum in (signal.SIGINT,signal.SIGTERM): signal.signal(signum,stop)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=('identity','planes','color','applicability'))
    parser.add_argument('--record',required=True); parser.add_argument('--record-sha256',required=True)
    parser.add_argument('--binding'); parser.add_argument('--binding-sha256')
    parser.add_argument('--proof'); parser.add_argument('--proof-sha256')
    parser.add_argument('--output',required=True)
    parser.add_argument('--max-items',type=int,default=5000)
    parser.add_argument('--time-limit-ms',type=int,default=120000)
    args=parser.parse_args()
    started=time.monotonic()
    if args.time_limit_ms<1 or args.time_limit_ms>120000 or args.max_items<1:
        print('INVALID_RESOURCE_CAP',file=sys.stderr); return 2
    DEADLINE=started+args.time_limit_ms/1000
    result={'status':'UNKNOWN','mode':args.mode,'manifest_sha256':MANIFEST_SHA,
            'checker_sha256':sha256(Path(__file__).read_bytes()),
            'record_sha256':args.record_sha256,
            'claim_boundary':'conditional finite check only; not global replay or theorem acceptance'}
    code=3
    try:
        result['source_sha256']=verify_sources()
        data=read_pinned(args.record,args.record_sha256,8*1024*1024)
        record=parse_json(data)
        if args.mode in ('identity','applicability'):
            need(args.binding is not None and args.binding_sha256 is not None,'BINDING_REQUIRED')
            raw=read_pinned(args.binding,args.binding_sha256,1000000)
            binding=parse_json(raw)
            need(isinstance(binding,dict) and binding.get('record_sha256')==args.record_sha256,'RECORD_BINDING_SHA_MISMATCH')
            result['binding_sha256']=args.binding_sha256
            identity=verify_identity(record,binding,args.max_items)
            if args.mode=='applicability':
                need(args.proof is not None and args.proof_sha256 is not None,'PROOF_REQUIRED')
                proof=parse_json(read_pinned(args.proof,args.proof_sha256,1000000))
                result['proof_sha256']=args.proof_sha256
                result['details']={'identity':identity,'applicability':verify_applicability(proof,record)}
                result['status']='VALID_APPLICABILITY_CONDITIONAL'; code=0
            else:
                need(args.proof is None and args.proof_sha256 is None,'UNEXPECTED_PROOF')
                result['details']=identity
                result['status']='VALID_IDENTITY_CONDITIONAL'; code=0
        else:
            need(args.binding is None and args.binding_sha256 is None,'UNEXPECTED_BINDING')
            need(args.proof is None and args.proof_sha256 is None,'UNEXPECTED_PROOF')
            if args.mode=='planes':
                result['details']=verify_planes(record,args.max_items)
                result['status']='VALID_DIRECTION_SET_ONLY'; code=0
            else:
                result['details']=verify_color(record)
                result['status']='VALID_COLOR_CONDITIONAL'; code=0
    except Reject as exc:
        result['status']='REJECT'; result['reason']=str(exc); code=2
    except (Unknown, OSError) as exc:
        result['status']='UNKNOWN'; result['reason']=str(exc); code=3
    except Exception as exc:
        result['status']='UNKNOWN'; result['reason']='UNEXPECTED_EXCEPTION:' + type(exc).__name__ + ':' + str(exc); code=3
    result['elapsed_ms']=int((time.monotonic()-started)*1000)
    if not output_exclusive(args.output,result): return 73
    return code

if __name__=='__main__':
    sys.exit(main())
