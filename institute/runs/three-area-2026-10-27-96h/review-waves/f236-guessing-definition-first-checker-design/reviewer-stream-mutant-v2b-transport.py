#!/usr/bin/env python3
"""Definition-first exact identities and streaming archive coverage.

No producer code is imported. Unknown grammars or incomplete coverage are
UNKNOWN; even complete finite replay is conditional, not theorem acceptance.
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
import zipfile
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
    need(set(advertised)==actual, 'ALLOWED_MASK_SET_MISMATCH')
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
        if kind == 'gate' and len(name)==2:
            need(type(name[1]) is int and name[1]==1,'GATE_BRANCH_NOT_FULL_STATE')
            return factor_gate_vector(True),'le'
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

TARGET_ARCHIVE = {
    'sha256': '3bde5418e776a88b6a8f9c3e7a147a016b2b09272908eac226e1f3b33ced3040',
    'bytes': 67393983, 'members': 71, 'uncompressed': 457373801,
    'packet_sha256': '999b2a8d7a460953702ed8d5e21dfecdb1f2dfc57ef84a675218427ffcf88086',
    'certificates': 748, 'rows': 1811001, 'planes': 174251,
    'four_cases': 247, 'classes': 515,
    'coefficient_members': (
        'coefficients/proper-subgraph.jsonl',
        'coefficients/scalar-visibility-and-fourfactor.jsonl',
        'coefficients/residual-part2.jsonl',
        'coefficients/residual-part3.jsonl',
        'coefficients/residual-recovered3.jsonl',
        'coefficients/residual-new20.jsonl'),
    'graph_member': 'data/graph-factor-actions-and-proper-color.json',
    'class_member': 'data/residual-class-proof-map.json',
    'four_member': 'data/four-factor-all-247-cases.jsonl',
    'plane_member': 'data/all-174251-direction-planes.jsonl',
}

def stream_digest(stream):
    h=hashlib.sha256(); count=0
    while True:
        tick()
        block=stream.read(1024*1024)
        if not block: return h.hexdigest(),count
        h.update(block); count+=len(block)

def member_bytes(z, entry, cap):
    if entry['bytes']>cap: raise Unknown('MEMBER_SIZE_CAP:'+entry['member'])
    with z.open(entry['member']) as stream:
        data=stream.read(cap+1)
    if len(data)>cap: raise Unknown('MEMBER_SIZE_CAP:'+entry['member'])
    need(len(data)==entry['bytes'] and sha256(data)==entry['sha256'],
         'MEMBER_PIN_MISMATCH:'+entry['member'])
    return data

def member_jsonl(z, entry):
    """Yield complete records; verify the uncompressed stream before exhaustion."""
    h=hashlib.sha256(); total=0; count=0
    with z.open(entry['member']) as stream:
        while True:
            tick()
            line=stream.readline(8*1024*1024+1)
            if not line: break
            if len(line)>8*1024*1024: raise Unknown('RECORD_SIZE_CAP:'+entry['member'])
            need(line.endswith(b'\n'),'JSONL_NO_FINAL_LF:'+entry['member'])
            h.update(line); total+=len(line); count+=1
            yield parse_json(line),sha256(line)
    need(total==entry['bytes'] and h.hexdigest()==entry['sha256'],
         'MEMBER_PIN_MISMATCH:'+entry['member'])
    if 'records' in entry:
        need(type(entry['records']) is int and count==entry['records'],
             'MEMBER_RECORD_COUNT:'+entry['member'])

def packet_table(packet, infos):
    need(isinstance(packet,dict) and isinstance(packet.get('members'),list), 'PACKET_SCHEMA')
    table={}
    for item in packet['members']:
        need(isinstance(item,dict) and {'member','sha256','bytes','role'}<=set(item),'MEMBER_ENTRY_SCHEMA')
        name=item['member']; digest=item['sha256']; size=item['bytes']
        need(isinstance(name,str) and name and not name.startswith('/') and
             all(x not in ('','.','..') for x in name.split('/')), 'MEMBER_PATH')
        need(name not in table and name!='packet-manifest.json','DUPLICATE_MEMBER_DECLARATION')
        need(isinstance(digest,str) and SHA.fullmatch(digest) is not None and
             type(size) is int and size>=0, 'MEMBER_PIN_SCHEMA')
        table[name]=item
    names=[i.filename for i in infos]
    need(len(names)==len(set(names)), 'DUPLICATE_ARCHIVE_MEMBER')
    need(set(names)==set(table)|{'packet-manifest.json'}, 'ARCHIVE_MEMBER_SET')
    for info in infos:
        if info.filename!='packet-manifest.json':
            need(info.file_size==table[info.filename]['bytes'],'MEMBER_SIZE_METADATA:'+info.filename)
    return table

def graph_metadata(meta):
    exact_keys(meta,('factor_preserving_vertex_actions','factor_actions_zero_based',
                     'proper_subgraph_graph_actions_order8','proper_delete_1_color',
                     'visibility_generators'),'GRAPH_METADATA')
    all_graph=graph_actions()
    proper=meta['proper_subgraph_graph_actions_order8']
    factor=meta['factor_preserving_vertex_actions']
    need(isinstance(proper,list) and all(isinstance(x,list) and all(type(v) is int for v in x) for x in proper), 'PROPER_ACTION_TABLE')
    need(len(proper)==len(set(tuple(x) for x in proper)) and
         set(tuple(x) for x in proper)==set(all_graph), 'PROPER_ACTION_TABLE_MISMATCH')
    legal={x for x in all_graph if factors_of_action(x) is not None}
    need(isinstance(factor,list) and all(isinstance(x,list) and all(type(v) is int for v in x) for x in factor) and
         len(factor)==len(set(tuple(x) for x in factor)) and
         set(tuple(x) for x in factor)==legal, 'FACTOR_ACTION_TABLE_MISMATCH')
    need(isinstance(meta['factor_actions_zero_based'],list) and
         all(isinstance(x,list) and all(type(v) is int for v in x) for x in meta['factor_actions_zero_based']),
         'FACTOR_IMAGE_TABLE_SCHEMA')
    need(meta['factor_actions_zero_based']==[list(factors_of_action(tuple(x))) for x in factor],
         'FACTOR_IMAGE_TABLE_MISMATCH')
    need(meta['visibility_generators']==[sorted(x) for x in VISIBILITY_GENERATORS],
         'VISIBILITY_GENERATOR_TABLE_MISMATCH')
    coloring=meta['proper_delete_1_color']
    need(isinstance(coloring,dict) and set(coloring)=={str(v) for v in range(2,11)} and
         all(type(c) is int and 0<=c<=2 for c in coloring.values()),'DELETE_ONE_COLOR_SCHEMA')
    need(all(coloring[str(v)]!=coloring[str(u)] for v in range(2,11)
             for u in NEIGHBORS[v] if u!=1),'DELETE_ONE_COLOR_INVALID')
    return tuple(tuple(x) for x in proper),tuple(tuple(x) for x in factor)

def index_metadata(packet, contract, table):
    idx=packet.get('coefficient_certificate_index')
    need(isinstance(idx,list) and len(idx)==contract['certificates'],'CERTIFICATE_INDEX_COUNT')
    result={}; sources=set(); rows=0; source_locations=set()
    for item in idx:
        exact_keys(item,('certificate_id','source_member','source_index','rows','coordinate_system','scope'),'INDEX_ENTRY')
        ident=item['certificate_id']; source=item['source_member']; count=item['rows']
        need(isinstance(ident,str) and ident and ident not in result, 'DUPLICATE_CERTIFICATE_ID')
        need(isinstance(source,str) and source.startswith('sources/') and source.endswith('.json') and source in table,
             'INDEX_SOURCE_NOT_LISTED')
        need(type(count) is int and count>0, 'INDEX_ROW_COUNT')
        location=(source,json.dumps(item['source_index'],sort_keys=True))
        need(location not in source_locations,'DUPLICATE_SOURCE_INDEX')
        source_locations.add(location); sources.add(source); rows+=count; result[ident]=item
    need(rows==contract['rows'],'INDEX_TOTAL_ROW_COUNT')
    return result,sources

def verify_archive_certificates(z, table, index, contract, max_rows):
    verified={}; rows=0; count=0
    for member in contract['coefficient_members']:
        need(member in table,'MISSING_COEFFICIENT_MEMBER:'+member)
        for record,record_sha in member_jsonl(z,table[member]):
            if count>=contract['certificates']: raise Reject('EXTRA_CERTIFICATE_RECORD')
            need(isinstance(record,dict) and isinstance(record.get('certificate_id'),str),'CERTIFICATE_SCHEMA')
            ident=record['certificate_id']
            need(ident in index and ident not in verified,'UNLISTED_OR_DUPLICATE_CERTIFICATE')
            entry=index[ident]
            need(isinstance(record.get('rows'),list) and len(record['rows'])==entry['rows'],
                 'INDEX_RECORD_ROW_COUNT:'+ident)
            if rows+len(record['rows'])>max_rows: raise Unknown('ARCHIVE_ROW_CAP')
            binding={k:entry[k] for k in ('certificate_id','source_member','source_index','coordinate_system','scope')}
            binding['record_sha256']=record_sha
            verify_identity(record,binding,max_rows)
            verified[ident]={k:record[k] for k in ('certificate_id','source_member','source_index','coordinate_system','scope')}
            rows+=len(record['rows']); count+=1
    need(set(verified)==set(index),'CERTIFICATE_INDEX_SET_MISMATCH')
    need(rows==contract['rows'] and count==contract['certificates'],'CERTIFICATE_TOTAL_MISMATCH')
    return verified

def required_visibility(scope):
    if 'visibility_required' in scope:
        values=scope['visibility_required']
        need(isinstance(values,list) and len(values)==len(set(values)) and
             all(type(v) is int and 1<=v<=10 for v in values),'VISIBILITY_REQUIREMENT_SCHEMA')
        return set(values)
    if 'syndrome_visibility_vertex' in scope:
        v=integer(scope['syndrome_visibility_vertex'],1,10,'VERTEX_RANGE')
        group=scope.get('group')
        need(isinstance(group,list) and group,'VISIBILITY_GROUP_SCHEMA')
        return {a[v-1] for a in group}
    return set()

def certificate_actions(cert, plane, factor_actions):
    """All source-to-client actions justified by the certificate scope."""
    selected,visible,_=plane_info(plane)
    scope=cert['scope']; typ=cert['coordinate_system']['type']
    if typ!='entropy_bitmask' or len(cert['coordinate_system']['variables'])!=11:
        return set()
    if 'syndrome_plane' in scope:
        source=plane_tuple(scope['syndrome_plane'])
        return {i for i,a in enumerate(factor_actions)
                if move_plane(source,factors_of_action(a))==plane}
    required=required_visibility(scope)
    if not required: return set()
    source_factors=check_selected(scope['factors']) if 'factors' in scope else None
    possible=set()
    for i,a in enumerate(factor_actions):
        f=factors_of_action(a)
        if source_factors is not None and {f[t-1]+1 for t in source_factors}!=set(selected):
            continue
        if {a[v-1] for v in required} <= visible:
            possible.add(i)
    return possible

def build_class_map(value,index,verified,factor_actions,expected_classes):
    need(isinstance(value,list) and len(value)==expected_classes,'CLASS_MAP_COUNT')
    by_plane={}; ids=set()
    for item in value:
        tick()
        exact_keys(item,('class_id_zero_based','coloring','base_plane','proof','action_images'),'CLASS')
        cls=integer(item['class_id_zero_based'],0,expected_classes-1,'CLASS_ID_RANGE')
        need(cls not in ids,'DUPLICATE_CLASS_ID'); ids.add(cls)
        proof=item['proof']
        exact_keys(proof,('certificate_id','historical_declared_id','source','source_certificate_index'),'CLASS_PROOF')
        ident=proof['certificate_id']
        need(ident in verified and ident in index,'CLASS_CERTIFICATE_NOT_VERIFIED')
        cert=verified[ident]; scope=cert['scope']
        need(cert['coordinate_system']['type']=='functional_branch' and
             scope.get('class_id_zero_based')==cls and scope.get('coloring')==item['coloring'],
             'CLASS_CERTIFICATE_COLOR_BINDING')
        need(proof['source']==Path(cert['source_member']).name and
             proof['source_certificate_index']==cert['source_index'],'CLASS_SOURCE_INDEX_BINDING')
        base=plane_tuple(item['base_plane'])
        need(same_color_orbit(plane_info(base)[2],check_colors(scope['colors'])),
             'CLASS_BASE_PLANE_COLOR_MISMATCH')
        images=item['action_images']
        need(isinstance(images,list) and len(images)==len(factor_actions),'CLASS_ACTION_COUNT')
        action_ids=set()
        for image in images:
            exact_keys(image,('plane','source_to_target_action'),'CLASS_ACTION')
            aid=integer(image['source_to_target_action'],0,len(factor_actions)-1,'CLASS_ACTION_INDEX')
            need(aid not in action_ids,'DUPLICATE_CLASS_ACTION'); action_ids.add(aid)
            target=plane_tuple(image['plane'])
            need(move_plane(base,factors_of_action(factor_actions[aid]))==target,'CLASS_ACTION_IMAGE_MISMATCH')
            if target in by_plane:
                need(by_plane[target][0]==cls,'CLASS_ORBITS_OVERLAP')
            else:
                by_plane[target]=(cls,ident)
        need(action_ids==set(range(len(factor_actions))),'CLASS_ACTION_SET')
    need(ids==set(range(expected_classes)),'CLASS_ID_SET')
    return by_plane

def verify_four_case(value,verified,factor_actions):
    exact_keys(value,('case_id_zero_based','global_plane','factors','syndrome_plane','allowed_masks','color'),'FOUR_CASE')
    case_id=integer(value['case_id_zero_based'],0,10**9,'FOUR_CASE_ID')
    plane=plane_tuple(value['global_plane']); selected,_,_=plane_info(plane)
    factors=check_selected(value['factors'])
    need(factors==selected and len(factors)==4 and
         set().union(*(set(TRIANGLES[t-1]) for t in factors))==set(range(1,11)),
         'FOUR_CASE_FACTORS')
    order=sorted(factors)
    local=sorted(sum(1<<i for i,t in enumerate(order) if direction & (1<<(t-1))) for direction in plane)
    need(value['syndrome_plane']==local,'FOUR_CASE_LOCAL_PLANE')
    listed=value['allowed_masks']
    need(isinstance(listed,list) and all(type(x) is int and 1<=x<1024 for x in listed) and
         len(set(listed))==len(listed),'FOUR_CASE_MASK_SCHEMA')
    need(set(listed)==allowed_masks(plane),'ALLOWED_MASK_SET_MISMATCH')
    if value['color'] is not None:
        check_color_applicability(plane,value['color'],listed)
        return case_id,plane,'color',set()
    candidates={ident for ident,cert in verified.items() if ident.startswith('F4-') and
                certificate_actions(cert,plane,factor_actions)}
    if not candidates: raise Unknown('FOUR_CASE_NO_VERIFIED_APPLICABLE_PROOF')
    return case_id,plane,'certificate',candidates

def action_constraint(row,allowed,factor_actions):
    key='certificate_to_client_action'
    if key in row:
        action=integer(row[key],0,len(factor_actions)-1,'CERTIFICATE_ACTION_INDEX')
        need(action in allowed,'CERTIFICATE_ACTION_NOT_APPLICABLE')
    else:
        need(bool(allowed),'CERTIFICATE_NOT_APPLICABLE')
    if 'client_to_certificate_action' in row:
        need(key in row,'MISSING_FORWARD_ACTION')
        inverse=integer(row['client_to_certificate_action'],0,len(factor_actions)-1,'CLIENT_ACTION_INDEX')
        forward=factor_actions[row[key]]; reverse=factor_actions[inverse]
        need(compose(forward,reverse)==tuple(range(1,11)) and
             compose(reverse,forward)==tuple(range(1,11)),'TRANSPORT_ACTIONS_NOT_INVERSES')

def verify_plane_roster(z,entry,universe,verified,factor_actions,proper_actions,class_map,four_cases,max_planes):
    actual=set(); categories={k:set() for k in ('noncover','four_factor','full_visibility',
                                               'mixed_visibility','residual_functional')}
    mixed=[(ident,cert) for ident,cert in verified.items() if ident.startswith('M')]
    mixed_cache={}
    for row,_ in member_jsonl(z,entry):
        tick()
        if len(actual)>=max_planes: raise Unknown('ARCHIVE_PLANE_CAP')
        need(isinstance(row,dict) and {'plane','J','W','category','proof_id'}<=set(row),'PLANE_ROW_SCHEMA')
        plane=plane_tuple(row['plane']); need(plane not in actual,'DUPLICATE_PLANE')
        selected,visible,_=plane_info(plane)
        need(type(row['J']) is int and row['J']==sum(1<<(t-1) for t in selected),'PLANE_FACTOR_MASK_MISMATCH')
        need(type(row['W']) is int and row['W']==mask_of(visible),'PLANE_VISIBILITY_MASK_MISMATCH')
        covered=set().union(*(set(TRIANGLES[t-1]) for t in selected)) if selected else set()
        if covered!=set(range(1,11)): category='noncover'
        elif len(selected)==4: category='four_factor'
        elif any(g <= visible for g in VISIBILITY_GENERATORS): category='full_visibility'
        else:
            key=(row['J'],row['W'])
            if key not in mixed_cache:
                if any('syndrome_plane' in cert['scope'] for _,cert in mixed):
                    raise Unknown('MIXED_PLANE_SCOPE_NOT_CACHEABLE')
                mixed_cache[key]=any(certificate_actions(cert,plane,factor_actions) for _,cert in mixed)
            category='mixed_visibility' if mixed_cache[key] else 'residual_functional'
        need(row['category']==category,'PLANE_CATEGORY_MISMATCH')
        ident=row['proof_id']
        if category=='noncover':
            exact_keys(row,('plane','J','W','category','proof_id','missing_vertex',
                            'representative_missing_vertex','proper_graph_action'),'NONCOVER_RECORD')
            missing=integer(row['missing_vertex'],1,10,'MISSING_VERTEX')
            rep=integer(row['representative_missing_vertex'],1,10,'SOURCE_MISSING_VERTEX')
            aid=integer(row['proper_graph_action'],0,len(proper_actions)-1,'PROPER_ACTION_INDEX')
            need(True,'NONCOVER_TRANSPORT')
            need(ident in verified and verified[ident]['scope'].get('missing_vertex')==rep and
                 len(verified[ident]['coordinate_system'].get('variables',[]))==9,'NONCOVER_PROOF_BINDING')
        elif category in ('full_visibility','mixed_visibility'):
            permitted={'plane','J','W','category','proof_id','certificate_to_client_action','client_to_certificate_action'}
            if set(row)-permitted: raise Unknown('UNSPECIFIED_PLANE_FIELDS:'+category+':'+','.join(sorted(set(row)-permitted)))
            need(ident in verified,'PLANE_PROOF_NOT_VERIFIED')
            need((category=='full_visibility' and ident in ('V6','V25','V12T')) or
                 (category=='mixed_visibility' and ident.startswith('M')),'PLANE_PROOF_FAMILY')
            action_constraint(row,certificate_actions(verified[ident],plane,factor_actions),factor_actions)
        elif category=='four_factor':
            permitted={'plane','J','W','category','proof_id','case_id_zero_based',
                       'certificate_to_client_action','client_to_certificate_action'}
            if set(row)-permitted: raise Unknown('UNSPECIFIED_PLANE_FIELDS:'+category+':'+','.join(sorted(set(row)-permitted)))
            need(plane in four_cases,'FOUR_CASE_NOT_FOUND')
            case_id,kind,candidates=four_cases[plane]
            if kind=='color':
                if 'case_id_zero_based' not in row: raise Unknown('COLOR_CASE_ID_GRAMMAR_UNSPECIFIED')
                need(row['case_id_zero_based']==case_id,'COLOR_CASE_BINDING')
            else:
                need(ident in candidates,'FOUR_CASE_CERTIFICATE_BINDING')
                action_constraint(row,certificate_actions(verified[ident],plane,factor_actions),factor_actions)
        else:
            permitted={'plane','J','W','category','proof_id','class_id_zero_based'}
            if set(row)-permitted: raise Unknown('UNSPECIFIED_PLANE_FIELDS:'+category+':'+','.join(sorted(set(row)-permitted)))
            need(plane in class_map and class_map[plane][1]==ident,'RESIDUAL_CLASS_PROOF_BINDING')
            if 'class_id_zero_based' in row:
                need(row['class_id_zero_based']==class_map[plane][0],'RESIDUAL_CLASS_ID_BINDING')
        actual.add(plane); categories[category].add(plane)
    need(actual==universe,'PLANE_UNIVERSE_SET_MISMATCH')
    need(categories['four_factor']==set(four_cases),'FOUR_FACTOR_ACTUAL_SET_MISMATCH')
    need(categories['residual_functional']==set(class_map),'RESIDUAL_ACTUAL_SET_MISMATCH')
    return {k:len(v) for k,v in categories.items()}

def verify_archive(archive_path,contract,max_certificates,max_rows,max_planes,source_bindings=()):
    if contract['certificates']>max_certificates: raise Unknown('ARCHIVE_CERTIFICATE_CAP')
    if contract['rows']>max_rows: raise Unknown('ARCHIVE_ROW_CAP')
    if contract['planes']>max_planes: raise Unknown('ARCHIVE_PLANE_CAP')
    with open(archive_path,'rb') as archive:
        actual_sha,actual_bytes=stream_digest(archive)
        need(actual_sha==contract['sha256'] and actual_bytes==contract['bytes'],'ARCHIVE_PIN_MISMATCH')
        archive.seek(0)
        with zipfile.ZipFile(archive) as z:
            infos=z.infolist()
            need(len(infos)==contract['members'] and sum(i.file_size for i in infos)==contract['uncompressed'],
                 'ARCHIVE_STRUCTURE_MISMATCH')
            info=z.getinfo('packet-manifest.json')
            if info.file_size>1000000: raise Unknown('PACKET_SIZE_CAP')
            with z.open(info) as stream: packet_raw=stream.read(1000001)
            need(len(packet_raw)<=1000000 and sha256(packet_raw)==contract['packet_sha256'],'PACKET_PIN_MISMATCH')
            packet=parse_json(packet_raw); table=packet_table(packet,infos)
            for source in source_bindings:
                member=source['archive_member']
                need(member in table and table[member]['sha256']==source['sha256'] and
                     table[member]['bytes']==source['bytes'],'WRITTEN_ARCHIVE_BINDING:'+member)
            index,sources=index_metadata(packet,contract,table)
            for name in sources:
                with z.open(name) as stream: got,size=stream_digest(stream)
                need(got==table[name]['sha256'] and size==table[name]['bytes'],'INDEXED_SOURCE_PIN_MISMATCH:'+name)
            graph=parse_json(member_bytes(z,table[contract['graph_member']],1000000))
            proper_actions,factor_actions=graph_metadata(graph)
            verified=verify_archive_certificates(z,table,index,contract,max_rows)
            classes=parse_json(member_bytes(z,table[contract['class_member']],1000000))
            class_map=build_class_map(classes,index,verified,factor_actions,contract['classes'])
            four_cases={}; case_ids=set()
            for row,_ in member_jsonl(z,table[contract['four_member']]):
                case_id,plane,kind,candidates=verify_four_case(row,verified,factor_actions)
                need(case_id not in case_ids and plane not in four_cases,'DUPLICATE_FOUR_CASE')
                case_ids.add(case_id); four_cases[plane]=(case_id,kind,candidates)
            need(case_ids==set(range(contract['four_cases'])),'FOUR_CASE_ID_SET')
            universe=(set(contract['fixture_universe']) if 'fixture_universe' in contract
                      else all_planes(10,max_planes))
            need(len(universe)==contract['planes'],'UNIVERSE_COUNT')
            categories=verify_plane_roster(z,table[contract['plane_member']],universe,verified,
                                           factor_actions,proper_actions,class_map,four_cases,max_planes)
            coverage=packet.get('literal_coverage_data')
            need(isinstance(coverage,dict) and coverage.get('category_records')==categories,
                 'CATEGORY_METADATA_COUNT_MISMATCH')
        archive.seek(0)
        need(stream_digest(archive)==(actual_sha,actual_bytes),'ARCHIVE_CHANGED_DURING_REPLAY')
    return {'certificates':len(verified),'rows':contract['rows'],'planes':len(universe),
            'category_counts':categories,'classes':len(classes),'four_cases':len(four_cases),
            'claim':'expanded identities and plane/case/class sets only; written premises, source-projection equality and theorem remain separate'}


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
    parser.add_argument('mode',choices=('identity','planes','color','applicability','archive'))
    parser.add_argument('--record'); parser.add_argument('--record-sha256')
    parser.add_argument('--binding'); parser.add_argument('--binding-sha256')
    parser.add_argument('--proof'); parser.add_argument('--proof-sha256')
    parser.add_argument('--archive')
    parser.add_argument('--output',required=True)
    parser.add_argument('--max-items',type=int,default=5000)
    parser.add_argument('--max-certificates',type=int,default=1)
    parser.add_argument('--max-rows',type=int,default=5000)
    parser.add_argument('--max-planes',type=int,default=5000)
    parser.add_argument('--time-limit-ms',type=int,default=120000)
    args=parser.parse_args()
    started=time.monotonic()
    max_time=14400000 if args.mode=='archive' else 120000
    if (args.time_limit_ms<1 or args.time_limit_ms>max_time or args.max_items<1 or
        args.max_certificates<1 or args.max_rows<1 or args.max_planes<1):
        print('INVALID_RESOURCE_CAP',file=sys.stderr); return 2
    DEADLINE=started+args.time_limit_ms/1000
    result={'status':'UNKNOWN','mode':args.mode,'manifest_sha256':MANIFEST_SHA,
            'checker_sha256':sha256(Path(__file__).read_bytes()),
            'record_sha256':args.record_sha256,
            'claim_boundary':'conditional finite checks only; not theorem acceptance or source-projection equality'}
    code=3
    try:
        result['source_sha256']=verify_sources()
        if args.mode=='archive':
            need(args.archive is not None,'ARCHIVE_REQUIRED')
            need(all(x is None for x in (args.record,args.record_sha256,args.binding,args.binding_sha256,
                                         args.proof,args.proof_sha256)), 'UNEXPECTED_ARCHIVE_ARGUMENT')
            manifest=parse_json(read_pinned(MANIFEST,MANIFEST_SHA,1000000))
            result['archive_sha256']=TARGET_ARCHIVE['sha256']
            result['details']=verify_archive(args.archive,TARGET_ARCHIVE,args.max_certificates,
                                             args.max_rows,args.max_planes,manifest['inputs_in_read_order'])
            result['status']='VALID_ARCHIVE_FINITE_REPLAY_CONDITIONAL'; code=0
        else:
            need(args.archive is None,'UNEXPECTED_ARCHIVE')
            need(args.record is not None and args.record_sha256 is not None,'RECORD_REQUIRED')
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
