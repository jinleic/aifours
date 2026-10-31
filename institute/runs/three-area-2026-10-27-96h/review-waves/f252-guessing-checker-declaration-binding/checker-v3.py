#!/usr/bin/env python3
"""Prospective declaration-bound row checks; never an archive/theorem replay.

Adapted from the independently authored f236 reviewer-checker-v2.py; this is
not a new independent checker. Only built-in synthetic controls and the one
pinned R382 diagnostic are exposed. All scientific applicability remains
conditional on the actual component law and separately reviewed premises.
"""
import argparse
import collections
import copy
import hashlib
import itertools
import json
import math
import re
import signal
import sys
import time
import zipfile
from fractions import Fraction
from pathlib import Path

MANIFEST_SHA = '2cb4880ea4b6e73fa79c6db06825cb303ea06bce36e12586dea756701d9a9b3f'
DECLARATION_SHA = 'c67ecd5bce3ef5cab01a0e9949f56a5f801d80e17209864b7b85ea51b16eea4d'
PREDECESSOR_SHA = 'ce407f9780f95559f801940594d2d71e1f969a1e6bceb9c13c41535f9bf0b840'
ARCHIVE_SHA = '3bde5418e776a88b6a8f9c3e7a147a016b2b09272908eac226e1f3b33ced3040'
R382_SHA = '48118dc6a138998cb509675f7ffd497aa131d5c00b106950427f164c45f50d29'
R382_SIZE = 137939
R382_MEMBER = 'coefficients/residual-recovered3.jsonl'
MANIFEST = Path(__file__).with_name('manifest-v2.json')
TRIANGLES = ((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),
             (3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
NEIGHBORS = {1:{2,3,4,5,6,7}, 2:{1,3,7,9,10}, 3:{1,2,4,8,9},
             4:{1,3,5,8,10}, 5:{1,4,6,9,10}, 6:{1,5,7,8,9},
             7:{1,2,6,8,10}, 8:{3,4,6,7,9,10}, 9:{2,3,5,6,8},
             10:{2,4,5,7,8}}
RATIONAL = re.compile(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?\Z')
DEADLINE = float('inf')

# Coordinate family, descriptor, arity, relation, exact unweighted formula.
# This schema is fixed before seeing any record/image vector; it is not selected
# by fitting an image. It reflects the frozen author's prospective declaration.
SCHEMA_ROWS = (
 ('entropy_bitmask_11','cmi',4,'ge','H(K OR (1<<i))+H(K OR (1<<j))-H(K OR (1<<i) OR (1<<j))-H(K)'),
 ('entropy_bitmask_11','conditional-zero-rank-fd',3,'eq','H(a union {v,S})-H(a union {S})'),
 ('entropy_bitmask_11','fd',2,'eq','H(N(v) union {v})-H(N(v))'),
 ('entropy_bitmask_11','local-fd',2,'eq','H(L_ALL(v) union {v,S})-H(L_ALL(v) union {S})'),
 ('entropy_bitmask_11','mixed-local-fd',2,'eq','H(L_J(v) union {v,S})-H(L_J(v) union {S})'),
 ('entropy_bitmask_11','syndrome-global-fd',1,'eq','H(V union {S})-H(V)'),
 ('entropy_bitmask_11','syndrome-neighborhood',2,'eq','H(N(v) union {S})-H(N(v))'),
 ('entropy_bitmask_9','cmi','dict','ge','H(K OR (1<<i))+H(K OR (1<<j))-H(K OR (1<<i) OR (1<<j))-H(K)'),
 ('entropy_bitmask_9','conditional_entropy','dict','ge','H(511)-H(511 XOR (1<<i))'),
 ('entropy_bitmask_9','fd','dict','eq','H(nb union {i})-H(nb), where nb={j: s_j belongs to N(s_i)}'),
 ('functional_branch','aux-determined',2,'eq','h_b(V)-h_0(V)'),
 ('functional_branch','cmi',5,'ge','H_b(K OR (1<<i))+H_b(K OR (1<<j))-H_b(K OR (1<<i) OR (1<<j))-H_b(K)'),
 ('functional_branch','data-processing',3,'le','h_j(a)-h_1(a)'),
 ('functional_branch','functional-local-fd',3,'eq','h_{2+c}(L_J(v) union {v})-h_{2+c}(L_J(v))'),
 ('functional_branch','functional-neighborhood',3,'eq','h_{2+c}(N(v))-h_0(N(v))'),
 ('functional_branch','functional-triangle',2,'eq','h_{2+c}(T_t)-h_0(T_t)'),
 ('functional_branch','gate',2,'le','3*h_0(V)+17*h_1(0)-2*sum_{v=1}^{10} h_1({v})'),
 ('functional_branch','graph-fd',2,'eq','h_0(N(v) union {v})-h_0(N(v))'),
 ('functional_branch','mixed-local-fd',2,'eq','h_1(L_J(v) union {v})-h_1(L_J(v))'),
 ('functional_branch','mono',3,'ge','H_b(2047)-H_b(2047 XOR (1<<i))'),
 ('functional_branch','pair-determines-state',4,'le','h_1(a)-h_j(a)-h_l(a)+h_0(a)'),
 ('functional_branch','state-neighborhood',2,'eq','h_1(N(v))-h_0(N(v))'),
)
SCHEMA = {(family,kind):(arity,relation,formula)
          for family,kind,arity,relation,formula in SCHEMA_ROWS}

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
    raise Unknown('TIME_LIMIT' if signum == signal.SIGALRM else 'INTERRUPTED')

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def duplicate_pairs(pairs):
    result = {}
    for key,value in pairs:
        need(key not in result, 'DUPLICATE_JSON_KEY:' + key)
        result[key] = value
    return result

def reject_float(_):
    raise Reject('FLOAT_OR_NONFINITE_FORBIDDEN')

def parse_json(data):
    try:
        return json.loads(data.decode('utf-8'), object_pairs_hook=duplicate_pairs,
                          parse_float=reject_float, parse_constant=reject_float)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Reject('INVALID_JSON:' + str(exc)) from exc

def read_pinned(path, digest, size, lf=None):
    tick()
    try:
        with open(path,'rb') as stream:
            data = stream.read(size+1)
    except OSError as exc:
        raise Unknown('INPUT_UNAVAILABLE:' + str(exc)) from exc
    tick()
    need(len(data)==size, 'INPUT_SIZE_MISMATCH:' + str(path))
    need(sha256(data)==digest, 'INPUT_SHA_MISMATCH:' + str(path))
    if lf is not None:
        need(data.count(b'\n')==lf and data.endswith(b'\n'), 'INPUT_LF_MISMATCH:' + str(path))
    return data

def guard_declaration_digest(raw):
    need(sha256(raw)==DECLARATION_SHA, 'DECLARATION_SHA_MISMATCH')

def verify_sources():
    try:
        raw=MANIFEST.read_bytes()
    except OSError as exc:
        raise Unknown('MANIFEST_UNAVAILABLE:' + str(exc)) from exc
    need(sha256(raw)==MANIFEST_SHA, 'MANIFEST_SHA_MISMATCH')
    manifest=parse_json(raw)
    entries=manifest.get('inputs_in_read_order')
    need(isinstance(entries,list) and len(entries)==17, 'SOURCE_LIST')
    observed=[]; declaration_raw=None
    for index,item in enumerate(entries):
        tick()
        need(isinstance(item,dict) and set(item)=={'path','role','sha256','bytes','LF'}, 'SOURCE_DECLARATION')
        data=read_pinned(item['path'],item['sha256'],item['bytes'],item['LF'])
        if index==15:
            need(item['sha256']==DECLARATION_SHA, 'DECLARATION_MANIFEST_BINDING')
            declaration_raw=data
        if index==16:
            need(item['sha256']==PREDECESSOR_SHA, 'PREDECESSOR_MANIFEST_BINDING')
        observed.append({'sha256':item['sha256'],'bytes':len(data),'LF':data.count(b'\n')})
    need(manifest['archive']['sha256']==ARCHIVE_SHA and manifest['archive']['bytes']==67393983,
         'ARCHIVE_MANIFEST_BINDING')
    guard_declaration_digest(declaration_raw)
    declaration=parse_json(declaration_raw)
    validate_declaration(declaration)
    return manifest,declaration_raw,observed

def validate_declaration(decl):
    need(isinstance(decl,dict) and decl.get('kind')=='ADDITIVE_AUTHOR_ROW_SEMANTICS_DECLARATION_NOT_A_PROOF_OR_REPLAY', 'DECLARATION_KIND')
    need(decl.get('archive_sha256')==ARCHIVE_SHA, 'DECLARATION_ARCHIVE_BINDING')
    rows=decl.get('all_exported_descriptor_formulas')
    need(isinstance(rows,list), 'DECLARATION_FORMULAS_SCHEMA')
    mapping={}
    fields={'coordinate_system','literal_descriptor_kind','arity','relation','parameters',
            'EXACT_unweighted_base_formula','disambiguation'}
    for row in rows:
        need(isinstance(row,dict) and set(row)==fields, 'DECLARATION_FORMULA_FIELDS')
        key=(row['coordinate_system'],row['literal_descriptor_kind'])
        need(key not in mapping, 'DECLARATION_DUPLICATE_DESCRIPTOR')
        need(key in SCHEMA, 'DECLARATION_UNSUPPORTED_DESCRIPTOR')
        arity,relation,formula=SCHEMA[key]
        need(row['arity']==arity and type(row['arity'])==type(arity), 'DECLARATION_ARITY_MISMATCH')
        need(row['relation']==relation, 'DECLARATION_RELATION_MISMATCH')
        need(row['EXACT_unweighted_base_formula']==formula, 'DECLARATION_FORMULA_MISMATCH')
        mapping[key]=row
    need(set(mapping)==set(SCHEMA), 'DECLARATION_DESCRIPTOR_SET_MISMATCH')
    for title,kind in (('EXPLICIT_DATA_PROCESSING_RESOLUTION','data-processing'),
                       ('EXPLICIT_PAIR_RESOLUTION','pair-determines-state')):
        need(decl.get(title)==mapping[('functional_branch',kind)], 'DECLARATION_RESOLUTION_MISMATCH')
    inventory=decl.get('descriptor_only_inventory')
    need(isinstance(inventory,dict) and isinstance(inventory.get('forms'),list), 'DECLARATION_INVENTORY_SCHEMA')
    inv={}
    for item in inventory['forms']:
        need(isinstance(item,dict), 'DECLARATION_INVENTORY_FORM')
        key=(item.get('coordinate_system'),item.get('descriptor_kind'))
        need(key not in inv and key in SCHEMA, 'DECLARATION_INVENTORY_DUPLICATE_OR_UNKNOWN')
        arity,relation,_=SCHEMA[key]
        need(item.get('descriptor_arity')==arity and type(item.get('descriptor_arity'))==type(arity)
             and item.get('relation')==relation, 'DECLARATION_INVENTORY_CONFLICT')
        inv[key]=item
    need(set(inv)==set(SCHEMA), 'DECLARATION_INVENTORY_SET')
    gate=decl.get('literal_nonzero_GS_inventory')
    need(gate==[{'member':R382_MEMBER,'record_index_zero_based':1,'certificate_id':'R382',
                 'row_index_zero_based':849,'literal_name':['gate',1],
                 'relation':'le','literal_multiplier':'832/8731'}], 'DECLARATION_GATE_INVENTORY')

def integer(value, low, high, label):
    need(type(value) is int and low<=value<=high, label)
    return value

def fraction(value):
    need(isinstance(value,str) and RATIONAL.fullmatch(value) is not None, 'INVALID_RATIONAL')
    try:
        result=Fraction(value)
    except (ValueError,ZeroDivisionError) as exc:
        raise Reject('INVALID_RATIONAL') from exc
    need(str(result)==value, 'NONCANONICAL_RATIONAL')
    return result

def mask_of(vertices):
    return sum(1<<(v-1) for v in vertices)

def add(vec,key,value):
    if key:
        vec[key]=vec.get(key,0)+value
        if not vec[key]:
            del vec[key]

def entropy_id(mask,branch,functional):
    return (5*(mask&1023)+(branch if mask&1024 else 0)) if functional else mask

def entropy_vector(terms,branch=0,functional=False):
    out={}
    for mask,value in terms:
        add(out,entropy_id(mask,branch,functional),value)
    return out

def cmi_vector(i,j,k,n,branch=0,functional=False):
    integer(i,0,n-1,'CMI_INDEX'); integer(j,0,n-1,'CMI_INDEX')
    integer(k,0,(1<<n)-1,'CMI_MASK')
    need(i<j and not (k&((1<<i)|(1<<j))), 'CMI_ORDER_OR_OVERLAP')
    x,y=1<<i,1<<j
    return entropy_vector(((k|x,1),(k|y,1),(k,-1),(k|x|y,-1)),branch,functional)

def conditional_vector(x,k,branch=0,functional=False):
    need(not(x&k), 'CONDITIONAL_OVERLAP')
    return entropy_vector(((k|x,1),(k,-1)),branch,functional)

def factor_gate_vector(functional):
    out={}
    if functional:
        for key,value in ((5*1023,3),(1,17)): add(out,key,value)
        for v in range(10): add(out,5*(1<<v)+1,-2)
    else:
        for key,value in ((1023,3),(1024,17)): add(out,key,value)
        for v in range(10): add(out,1024|(1<<v),-2)
    return out

def data_processing_vector(a,b):
    out={}
    for key,value in ((5*a+b,1),(5*a+1,-1)): add(out,key,value)
    return out

def pair_vector(a,b,c):
    out={}
    for key,value in ((5*a+1,1),(5*a,1),(5*a+b,-1),(5*a+c,-1)): add(out,key,value)
    return out

def check_colors(colors):
    need(isinstance(colors,list) and len(colors)==10, 'COLORING_SCHEMA')
    for c in colors:
        need(c is None or type(c) is int and 0<=c<=2, 'COLOR_VALUE')
    need(len({c for c in colors if c is not None})>=2, 'COLOR_RANK_LT_TWO')
    return tuple(colors)

def local_mask(v,selected):
    return mask_of({u for t in selected if v in TRIANGLES[t-1]
                    for u in TRIANGLES[t-1] if u!=v})

def incident_colors(v,colors):
    return {colors[i] for i,t in enumerate(TRIANGLES) if v in t and colors[i] is not None}

def selected_factors(scope):
    factors=scope.get('factors',list(range(1,11)))
    need(isinstance(factors,list) and all(type(t) is int and 1<=t<=10 for t in factors)
         and len(factors)==len(set(factors)), 'FACTORS_SCHEMA')
    return frozenset(factors)

def family_of(system):
    if system.get('type')=='functional_branch': return 'functional_branch'
    if system.get('type')=='entropy_bitmask' and len(system.get('variables',[]))==9: return 'entropy_bitmask_9'
    if system.get('type')=='entropy_bitmask' and len(system.get('variables',[]))==11: return 'entropy_bitmask_11'
    raise Unknown('UNSUPPORTED_COORDINATE_SYSTEM')

def descriptor(name,family):
    if family=='entropy_bitmask_9':
        need(isinstance(name,dict) and isinstance(name.get('kind'),str), 'ROW_DESCRIPTOR')
        kind=name['kind']
    else:
        need(isinstance(name,list) and name and isinstance(name[0],str), 'ROW_DESCRIPTOR')
        kind=name[0]
    key=(family,kind)
    if key not in SCHEMA: raise Unknown('UNSUPPORTED_DESCRIPTOR:' + str(key))
    arity,relation,_=SCHEMA[key]
    if family!='entropy_bitmask_9':
        need(len(name)==arity, 'DESCRIPTOR_ARITY')
    return kind,relation

def row_vector(name,system,scope):
    family=family_of(system)
    kind,relation=descriptor(name,family)
    if family=='entropy_bitmask_9':
        active=system['variables']
        keys={'cmi':{'kind','i','j','conditioning_mask','multiplier'},
              'conditional_entropy':{'kind','i','multiplier'},'fd':{'kind','i','multiplier'}}
        need(set(name)==keys[kind], 'PROPER_DESCRIPTOR_FIELDS')
        if kind=='cmi': return cmi_vector(name['i'],name['j'],name['conditioning_mask'],9),relation
        i=integer(name['i'],0,8,'PROPER_INDEX')
        if kind=='conditional_entropy': return conditional_vector(1<<i,511^(1<<i)),relation
        k=sum(1<<j for j,u in enumerate(active) if u in NEIGHBORS[active[i]])
        return conditional_vector(1<<i,k),relation
    if family=='functional_branch':
        colors=check_colors(scope.get('colors'))
        selected=frozenset(i+1 for i,c in enumerate(colors) if c is not None)
        if kind=='gate':
            need(type(name[1]) is int and name[1]==1, 'GATE_BRANCH_NOT_FULL_STATE')
            return factor_gate_vector(True),relation
        if kind=='cmi':
            b=integer(name[1],1,4,'BRANCH_RANGE')
            return cmi_vector(name[2],name[3],name[4],11,b,True),relation
        if kind=='mono':
            b=integer(name[1],1,4,'BRANCH_RANGE'); i=integer(name[2],0,10,'MONO_INDEX')
            return conditional_vector(1<<i,2047^(1<<i),b,True),relation
        if kind=='data-processing':
            a=integer(name[1],0,1023,'VERTEX_MASK'); b=integer(name[2],2,4,'BRANCH_RANGE')
            return data_processing_vector(a,b),relation
        if kind=='pair-determines-state':
            a=integer(name[1],0,1023,'VERTEX_MASK')
            b=integer(name[2],2,4,'BRANCH_RANGE'); c=integer(name[3],2,4,'BRANCH_RANGE')
            need(b<c, 'PAIR_ORDER')
            return pair_vector(a,b,c),relation
        if kind=='aux-determined':
            b=integer(name[1],1,4,'BRANCH_RANGE')
            return conditional_vector(1024,1023,b,True),relation
        if kind=='functional-triangle':
            t=integer(name[1],1,10,'FACTOR_RANGE'); c=colors[t-1]
            need(c is not None, 'FUNCTIONAL_TRIANGLE_NOT_SELECTED')
            return conditional_vector(1024,mask_of(TRIANGLES[t-1]),c+2,True),relation
        if kind in ('functional-neighborhood','functional-local-fd'):
            v=integer(name[1],1,10,'VERTEX_RANGE'); c=integer(name[2],0,2,'COLOR_VALUE')
            inc=incident_colors(v,colors)
            if kind=='functional-neighborhood':
                need(c in inc, 'FUNCTIONAL_NOT_INCIDENT')
                return conditional_vector(1024,mask_of(NEIGHBORS[v]),c+2,True),relation
            need(inc=={c}, 'LOCAL_DECODER_NOT_SINGLETON_COLOR')
            return conditional_vector(1<<(v-1),local_mask(v,selected)|1024,c+2,True),relation
        if kind=='graph-fd':
            v=integer(name[1],1,10,'VERTEX_RANGE')
            return conditional_vector(1<<(v-1),mask_of(NEIGHBORS[v]),0,True),relation
        if kind=='mixed-local-fd':
            v=integer(name[1],1,10,'VERTEX_RANGE')
            return conditional_vector(1<<(v-1),local_mask(v,selected)|1024,1,True),relation
        if kind=='state-neighborhood':
            v=integer(name[1],1,10,'VERTEX_RANGE')
            need(len(incident_colors(v,colors))>=2, 'STATE_NOT_VISIBLE')
            return conditional_vector(1024,mask_of(NEIGHBORS[v]),1,True),relation
    selected=selected_factors(scope)
    if kind=='cmi': return cmi_vector(name[1],name[2],name[3],11),relation
    if kind=='fd':
        v=integer(name[1],1,10,'VERTEX_RANGE')
        return conditional_vector(1<<(v-1),mask_of(NEIGHBORS[v])),relation
    if kind=='syndrome-global-fd': return conditional_vector(1024,1023),relation
    if kind=='conditional-zero-rank-fd':
        k=integer(name[1],0,1023,'LOCAL_MASK'); v=integer(name[2],1,10,'VERTEX_RANGE')
        need((k&local_mask(v,selected))==local_mask(v,selected), 'LOCAL_MASK_MISSING_COMPONENTS')
        return conditional_vector(1<<(v-1),k|1024),relation
    if kind in ('local-fd','mixed-local-fd'):
        v=integer(name[1],1,10,'VERTEX_RANGE')
        factors=frozenset(range(1,11)) if kind=='local-fd' else selected
        return conditional_vector(1<<(v-1),local_mask(v,factors)|1024),relation
    if kind=='syndrome-neighborhood':
        v=integer(name[1],1,10,'VERTEX_RANGE')
        declared=scope.get('visibility_required',[])
        need(isinstance(declared,list) and all(type(x) is int and 1<=x<=10 for x in declared)
             and len(declared)==len(set(declared)), 'VISIBILITY_REQUIREMENT_SCHEMA')
        # A declared set is a condition on the eventual law, not a proof of it.
        need(v in declared, 'VISIBILITY_NOT_DECLARED')
        return conditional_vector(1024,mask_of(NEIGHBORS[v])),relation
    raise Unknown('UNIMPLEMENTED_DECLARED_DESCRIPTOR:' + kind)

def graph_actions():
    result=[]
    def walk(mapping,used):
        tick()
        if len(mapping)==10:
            result.append(tuple(mapping[v] for v in range(1,11))); return
        v=len(mapping)+1
        for w in range(1,11):
            if w in used or len(NEIGHBORS[v])!=len(NEIGHBORS[w]): continue
            if all((u in NEIGHBORS[v])==(mapping[u] in NEIGHBORS[w]) for u in mapping):
                mapping[v]=w; walk(mapping,used|{w}); del mapping[v]
    walk({},set())
    return tuple(result)

def factors_of_action(action):
    lookup={frozenset(t):i for i,t in enumerate(TRIANGLES)}
    images=[lookup.get(frozenset(action[v-1] for v in t)) for t in TRIANGLES]
    return None if any(i is None for i in images) or len(set(images))!=10 else tuple(images)

def compose(a,b,one_based=True):
    return tuple(a[x-1] for x in b) if one_based else tuple(a[x] for x in b)

def check_group(actions,identity,composition):
    need(actions and len(actions)==len(set(actions)), 'ACTION_DUPLICATE_OR_EMPTY')
    group=set(actions)
    need(identity in group, 'ACTION_NO_IDENTITY')
    for a in actions:
        for b in actions:
            tick(); need(composition(a,b) in group, 'ACTION_NOT_CLOSED')

def validate_system(system,scope):
    need(isinstance(system,dict) and isinstance(scope,dict), 'SYSTEM_OR_SCOPE_SCHEMA')
    family=family_of(system)
    if family=='functional_branch':
        expected={'type':'functional_branch','coordinate_id':'5*A+b','A_vertex_subset_mask':[0,1023],
                  'b':{'0':'none','1':'S=(A_bit,B_bit)','2':'A_bit','3':'B_bit','4':'A_bit XOR B_bit'},
                  'nonempty_coordinates':5119}
        need(system==expected, 'FUNCTIONAL_COORDINATE_SCHEMA')
        colors=check_colors(scope.get('colors'))
        need(scope.get('coloring')==''.join('-' if c is None else str(c) for c in colors), 'COLOR_STRING_MISMATCH')
        allowed={'colors','coloring','class_id_zero_based'}
    elif family=='entropy_bitmask_9':
        missing=integer(scope.get('missing_vertex'),1,10,'MISSING_VERTEX')
        active=[v for v in range(1,11) if v!=missing]
        need(system=={'type':'entropy_bitmask','variables':active,'nonempty_coordinates':511}
             and scope.get('active_vertices')==active, 'PROPER_COORDINATE_SCHEMA')
        integer(scope.get('scale'),1,10**9,'SCALE')
        allowed={'missing_vertex','active_vertices','scale'}
    else:
        need(system=={'type':'entropy_bitmask','variables':list(range(1,11))+['S'],
                     'nonempty_coordinates':2047}, 'SCALAR_COORDINATE_SCHEMA')
        selected_factors(scope)
        allowed={'factors','visibility_required','group'}
    if set(scope)-allowed:
        raise Unknown('UNSUPPORTED_SCOPE_FIELDS:' + ','.join(sorted(set(scope)-allowed)))
    return family

def validate_actions(record,family):
    system=record['coordinate_system']; scope=record['scope']; raw=record['actions']
    need(isinstance(raw,list) and type(record['action_count']) is int and record['action_count']==len(raw), 'ACTION_COUNT')
    if family=='entropy_bitmask_9':
        need(raw==[list(range(9))], 'PROPER_ACTION_NOT_SINGLE_IDENTITY')
        return [tuple(range(9))]
    legal={p for p in graph_actions() if factors_of_action(p) is not None}
    selected=selected_factors(scope) if family=='entropy_bitmask_11' else frozenset(i+1 for i,c in enumerate(scope['colors']) if c is not None)
    actions=[]
    for action in raw:
        if family=='functional_branch':
            need(isinstance(action,list) and len(action)==2 and isinstance(action[0],list) and isinstance(action[1],list), 'FUNCTIONAL_ACTION_SCHEMA')
            v,c=tuple(action[0]),tuple(action[1])
            need(all(type(x) is int for x in v+c) and sorted(c)==[0,1,2], 'COLOR_ACTION_PERMUTATION')
        else:
            need(isinstance(action,list) and all(type(x) is int for x in action), 'SCALAR_ACTION_SCHEMA')
            v=tuple(action); c=None
        need(v in legal, 'ACTION_NOT_FACTOR_GRAPH_AUTOMORPHISM')
        fact=factors_of_action(v)
        need({fact[t-1]+1 for t in selected}==set(selected), 'ACTION_CHANGES_FACTOR_SET')
        if c is not None:
            colors=scope['colors']
            need(all(colors[fact[i]]==(None if colors[i] is None else c[colors[i]]) for i in range(10)), 'ACTION_CHANGES_COLORING')
            actions.append((v,c))
        else:
            actions.append(v)
    if family=='functional_branch':
        check_group(actions,(tuple(range(1,11)),tuple(range(3))),
                    lambda a,b:(compose(a[0],b[0]),compose(a[1],b[1],False)))
    else:
        if 'group' in scope: need(raw==scope['group'], 'ACTION_SCOPE_MISMATCH')
        required=scope.get('visibility_required',[])
        need(isinstance(required,list) and all(type(v) is int and 1<=v<=10 for v in required), 'VISIBILITY_REQUIREMENT_SCHEMA')
        need(all({a[v-1] for v in required}==set(required) for a in actions), 'ACTION_CHANGES_VISIBILITY')
        check_group(actions,tuple(range(1,11)),lambda a,b:compose(a,b))
    return actions

def permute_mask(mask,perm):
    return sum(1<<(perm[i]-1) for i in range(10) if mask&(1<<i))

def image_vector(vec,action,family):
    out={}
    for key,val in vec.items():
        if family=='entropy_bitmask_9':
            mapped=sum(1<<action[i] for i in range(9) if key&(1<<i))
        elif family=='functional_branch':
            vertices,colors=action; mask,b=divmod(key,5)
            mapped=5*permute_mask(mask,vertices)+(colors[b-2]+2 if b>=2 else b)
        else:
            mapped=permute_mask(key,action)|(key&1024)
        add(out,mapped,val)
    return out

def parse_vector(value,max_id,rational):
    need(isinstance(value,list), 'VECTOR_SCHEMA')
    out={}
    for item in value:
        need(isinstance(item,list) and len(item)==2, 'VECTOR_PAIR')
        key=integer(item[0],1,max_id,'VECTOR_COORDINATE')
        need(key not in out, 'DUPLICATE_VECTOR_COORDINATE')
        val=fraction(item[1]) if rational else integer(item[1],-10**100,10**100,'VECTOR_INTEGER')
        need(val!=0, 'ZERO_VECTOR_ENTRY')
        out[key]=val
    return out

def verify_rows(rows,system,scope,family,actions,expected,target_relation,max_rows):
    need(isinstance(rows,list) and rows, 'ROWS_SCHEMA')
    if len(rows)>max_rows: raise Unknown('ROW_CAP')
    max_id={'entropy_bitmask_9':511,'entropy_bitmask_11':2047,'functional_branch':5119}[family]
    total={}
    for row_index,row in enumerate(rows):
        tick()
        need(isinstance(row,dict) and set(row)=={'name','relation','multiplier','image_vectors'}, 'ROW_FIELDS')
        coeff=fraction(row['multiplier'])
        need(coeff!=0, 'ZERO_MULTIPLIER')
        if isinstance(row['name'],dict) and 'multiplier' in row['name']:
            need(type(row['name']['multiplier']) is int and coeff==row['name']['multiplier'], 'INNER_MULTIPLIER_MISMATCH')
        base,relation=row_vector(row['name'],system,scope)
        need(row['relation']==relation, 'ROW_RELATION_MISMATCH')
        if relation!='eq':
            need(coeff>0 if relation==target_relation else coeff<0, 'ROW_SIGN')
        images=row['image_vectors']
        need(isinstance(images,list) and len(images)==len(actions), 'IMAGE_ACTION_COUNT')
        scale=coeff/len(actions)
        for action,advertised in zip(actions,images):
            actual=image_vector(base,action,family)
            need(parse_vector(advertised,max_id,False)==actual, 'IMAGE_VECTOR_MISMATCH')
            for key,value in actual.items(): add(total,key,scale*value)
    need(total==expected, 'COEFFICIENT_IDENTITY_MISMATCH')
    return {'rows':len(rows),'actions':len(actions),'coordinates':max_id}

def verify_record(record,max_rows):
    keys={'certificate_id','source_member','source_index','coordinate_system','target_vector',
          'target_relation','action_count','actions','scope','rows'}
    need(isinstance(record,dict) and set(record)==keys, 'CERTIFICATE_FIELDS')
    need(record['certificate_id']=='R382', 'CERTIFICATE_ID_MISMATCH')
    need(isinstance(record['source_member'],str) and record['source_member'].startswith('sources/')
         and record['source_member'].endswith('.json'), 'SOURCE_MEMBER_SCHEMA')
    source_index=record['source_index']
    need(source_index is None or type(source_index) is int and source_index>=0 or
         isinstance(source_index,str) and re.fullmatch(r'0|[1-9][0-9]*',source_index) is not None,
         'SOURCE_INDEX_SCHEMA')
    system=record['coordinate_system']; scope=record['scope']
    family=validate_system(system,scope)
    need(family=='functional_branch', 'R382_COORDINATE_FAMILY')
    actions=validate_actions(record,family)
    expected={}; add(expected,5115,3)
    for i in range(10): add(expected,5*(1<<i),-2)
    need(record['target_relation']=='le', 'TARGET_RELATION')
    need(parse_vector(record['target_vector'],5119,True)==expected, 'TARGET_VECTOR_MISMATCH')
    details=verify_rows(record['rows'],system,scope,family,actions,expected,'le',max_rows)
    need(len(record['rows'])>849 and record['rows'][849]['name']==['gate',1]
         and record['rows'][849]['relation']=='le' and record['rows'][849]['multiplier']=='832/8731',
         'R382_GATE_LOCATOR_MISMATCH')
    details.update({'certificate_id':'R382','source_member':record['source_member'],
                    'source_index':source_index,'scope':scope})
    return details

def stream_digest(stream):
    h=hashlib.sha256(); size=0
    while True:
        tick(); block=stream.read(1024*1024)
        if not block: return h.hexdigest(),size
        h.update(block); size+=len(block)

def diagnostic_r382(manifest,max_rows):
    archive=manifest['archive']
    try:
        with open(archive['path'],'rb') as stream:
            need(stream_digest(stream)==(ARCHIVE_SHA,archive['bytes']), 'ARCHIVE_PIN_MISMATCH')
            stream.seek(0)
            with zipfile.ZipFile(stream) as z:
                entries=[x for x in z.infolist() if x.filename==R382_MEMBER]
                need(len(entries)==1, 'R382_MEMBER_AMBIGUOUS_OR_ABSENT')
                with z.open(entries[0]) as member:
                    skipped=member.readline(8*1024*1024+1)
                    need(skipped.endswith(b'\n') and len(skipped)<=8*1024*1024, 'PRECEDING_RECORD_FRAMING')
                    raw=member.readline(R382_SIZE+1)
                need(len(raw)==R382_SIZE and raw.endswith(b'\n'), 'R382_RECORD_SIZE_OR_LF')
                need(sha256(raw)==R382_SHA, 'R382_RECORD_SHA_MISMATCH')
                record=parse_json(raw)
                details=verify_record(record,max_rows)
            stream.seek(0)
            need(stream_digest(stream)==(ARCHIVE_SHA,archive['bytes']), 'ARCHIVE_CHANGED_DURING_DIAGNOSTIC')
    except (OSError,zipfile.BadZipFile) as exc:
        raise Unknown('ARCHIVE_UNAVAILABLE_OR_INVALID:' + str(exc)) from exc
    return details

def literal(vec):
    return [[k,v] for k,v in sorted(vec.items())]

def expect_reject(callback,reason):
    try:
        callback()
    except Reject as exc:
        if str(exc)==reason: return
        raise AssertionError('WRONG_REJECTION:' + str(exc) + ':expected:' + reason) from exc
    raise AssertionError('GUARD_DID_NOT_REJECT:' + reason)

def fixture_scope():
    colors=[0,1]+[None]*8
    return {'colors':colors,'coloring':'01--------','class_id_zero_based':0}

def fixture_system():
    return {'type':'functional_branch','coordinate_id':'5*A+b','A_vertex_subset_mask':[0,1023],
            'b':{'0':'none','1':'S=(A_bit,B_bit)','2':'A_bit','3':'B_bit','4':'A_bit XOR B_bit'},
            'nonempty_coordinates':5119}

def one_row(name,relation,multiplier,vec):
    return {'name':name,'relation':relation,'multiplier':multiplier,'image_vectors':[literal(vec)]}

def identity_action():
    return (tuple(range(1,11)),tuple(range(3)))

def functional_entropy(vec,states):
    # Each fixture coordinate has equiprobable values; all entropies are integers.
    total=0
    for coord,weight in vec.items():
        mask,branch=divmod(coord,5)
        samples=[]
        for state,vertices in states:
            b0,b1=state
            aux=(None,(b0,b1),b0,b1,b0^b1)[branch]
            samples.append(tuple(vertices[i] for i in range(10) if mask&(1<<i)) + (() if branch==0 else (aux,)))
        counts=collections.Counter(samples)
        need(len(set(counts.values()))==1 and len(counts)&(len(counts)-1)==0, 'FIXTURE_NONUNIFORM')
        total+=weight*int(math.log2(len(counts)))
    return total

def control(which,raw):
    decl=parse_json(raw)
    system=fixture_system(); scope=fixture_scope(); action=identity_action()
    if which=='digest':
        expect_reject(lambda:guard_declaration_digest(raw+b' '),'DECLARATION_SHA_MISMATCH')
    elif which=='missing_mapping':
        decl['all_exported_descriptor_formulas']=[x for x in decl['all_exported_descriptor_formulas'] if x['literal_descriptor_kind']!='mono']
        expect_reject(lambda:validate_declaration(decl),'DECLARATION_DESCRIPTOR_SET_MISMATCH')
    elif which=='duplicate_mapping':
        decl['all_exported_descriptor_formulas'].append(copy.deepcopy(next(x for x in decl['all_exported_descriptor_formulas'] if x['literal_descriptor_kind']=='mono')))
        expect_reject(lambda:validate_declaration(decl),'DECLARATION_DUPLICATE_DESCRIPTOR')
    elif which=='changed_formula':
        next(x for x in decl['all_exported_descriptor_formulas'] if x['literal_descriptor_kind']=='mono')['EXACT_unweighted_base_formula']='H(0)'
        expect_reject(lambda:validate_declaration(decl),'DECLARATION_FORMULA_MISMATCH')
    elif which=='conflicting_resolution':
        decl['EXPLICIT_PAIR_RESOLUTION']['EXACT_unweighted_base_formula']='0'
        expect_reject(lambda:validate_declaration(decl),'DECLARATION_RESOLUTION_MISMATCH')
    elif which=='arity':
        expect_reject(lambda:row_vector(['gate',1,2],system,scope),'DESCRIPTOR_ARITY')
    elif which=='pair_order':
        expect_reject(lambda:row_vector(['pair-determines-state',1,4,2],system,scope),'PAIR_ORDER')
    elif which=='gate_branch':
        expect_reject(lambda:row_vector(['gate',2],system,scope),'GATE_BRANCH_NOT_FULL_STATE')
    elif which=='local_guard':
        expect_reject(lambda:row_vector(['functional-local-fd',1,0],system,scope),'LOCAL_DECODER_NOT_SINGLETON_COLOR')
    elif which=='visibility_guard':
        expect_reject(lambda:row_vector(['state-neighborhood',2],system,scope),'STATE_NOT_VISIBLE')
    elif which in ('relation','sign','image'):
        vec=factor_gate_vector(True)
        row=one_row(['gate',1],'le','1',vec)
        expected=vec
        if which=='relation': row['relation']='ge'
        if which=='sign':
            row['multiplier']='-1'; expected={k:-v for k,v in vec.items()}
        if which=='image': row['image_vectors'][0][0][1]+=1
        reason={'relation':'ROW_RELATION_MISMATCH','sign':'ROW_SIGN','image':'IMAGE_VECTOR_MISMATCH'}[which]
        expect_reject(lambda:verify_rows([row],system,scope,'functional_branch',[action],expected,'le',10),reason)
    elif which=='action_guard':
        ident=list(range(1,11))
        record={'coordinate_system':system,'scope':scope,'action_count':2,
                'actions':[[ident,[0,1,2]],[ident,[1,0,2]]]}
        expect_reject(lambda:validate_actions(record,'functional_branch'),'ACTION_CHANGES_COLORING')
    elif which=='transport':
        base=data_processing_vector(1,2)
        moved=image_vector(base,((2,1,3,4,5,6,7,8,9,10),(1,2,0)),'functional_branch')
        assert moved=={13:1,11:-1}, ('TRANSPORT_WRONG',moved)
    elif which=='once_weight':
        proper={'type':'entropy_bitmask','variables':list(range(2,11)),'nonempty_coordinates':511}
        ps={'missing_vertex':1,'active_vertices':list(range(2,11)),'scale':1}
        row=one_row({'kind':'conditional_entropy','i':0,'multiplier':2},'ge','2',{511:1,510:-1})
        verify_rows([row],proper,ps,'entropy_bitmask_9',[tuple(range(9))],{511:2,510:-2},'ge',10)
    elif which=='averaged_weight':
        vec=factor_gate_vector(True)
        row=one_row(['gate',1],'le','2',vec)
        row['image_vectors'].append(literal(vec))
        actions=[action,(tuple(range(1,11)),(1,0,2))]
        expected={key:2*value for key,value in vec.items()}
        verify_rows([row],system,scope,'functional_branch',actions,expected,'le',10)
    elif which=='inner_weight':
        proper={'type':'entropy_bitmask','variables':list(range(2,11)),'nonempty_coordinates':511}
        ps={'missing_vertex':1,'active_vertices':list(range(2,11)),'scale':1}
        row=one_row({'kind':'conditional_entropy','i':0,'multiplier':3},'ge','2',{511:1,510:-1})
        expect_reject(lambda:verify_rows([row],proper,ps,'entropy_bitmask_9',[tuple(range(9))],{511:2,510:-2},'ge',10),'INNER_MULTIPLIER_MISMATCH')
    elif which=='data_formula':
        vec,_=row_vector(['data-processing',1,2],system,scope)
        assert vec=={7:1,6:-1}, ('DATA_FORMULA_WRONG',vec)
        states=[((a,b),[(a,),(),(),(),(),(),(),(),(),()]) for a in (0,1) for b in (0,1)]
        assert functional_entropy(vec,states)==-1
    elif which=='pair_formula':
        vec,_=row_vector(['pair-determines-state',1,3,4],system,scope)
        assert vec=={6:1,5:1,8:-1,9:-1}, ('PAIR_FORMULA_WRONG',vec)
        states=[((a,b),[(a,),(),(),(),(),(),(),(),(),()]) for a in (0,1) for b in (0,1)]
        assert functional_entropy(vec,states)==-1
    elif which=='gate_formula':
        vec,_=row_vector(['gate',1],system,scope)
        assert vec[5115]==3 and vec[1]==17 and all(vec[5*(1<<v)+1]==-2 for v in range(10)) and len(vec)==12
        states=[((a,b),[(a,),(b,),(),(),(),(),(),(),(),()]) for a in (0,1) for b in (0,1)]
        assert functional_entropy(vec,states)==0
    else:
        raise AssertionError('UNKNOWN_CONTROL:' + which)

def synthetic_smoke(raw):
    validate_declaration(parse_json(raw))
    tests=('digest','missing_mapping','duplicate_mapping','changed_formula','conflicting_resolution',
           'arity','pair_order','gate_branch','local_guard','visibility_guard','relation','sign',
           'image','action_guard','transport','once_weight','averaged_weight','inner_weight','data_formula','pair_formula','gate_formula')
    for name in tests: control(name,raw)
    # One protection/arithmetic mutation at a time, in memory only; no files are
    # created, removed, or overwritten. A mutant is killed only by its named case.
    mutations=(
      ('digest',"need(sha256(raw)==DECLARATION_SHA, 'DECLARATION_SHA_MISMATCH')","pass"),
      ('missing_mapping',"need(set(mapping)==set(SCHEMA), 'DECLARATION_DESCRIPTOR_SET_MISMATCH')","pass"),
      ('duplicate_mapping',"need(key not in mapping, 'DECLARATION_DUPLICATE_DESCRIPTOR')","pass"),
      ('changed_formula',"need(row['EXACT_unweighted_base_formula']==formula, 'DECLARATION_FORMULA_MISMATCH')","pass"),
      ('conflicting_resolution',"need(decl.get(title)==mapping[('functional_branch',kind)], 'DECLARATION_RESOLUTION_MISMATCH')","pass"),
      ('arity',"need(len(name)==arity, 'DESCRIPTOR_ARITY')","pass"),
      ('pair_order',"need(b<c, 'PAIR_ORDER')","pass"),
      ('gate_branch',"need(type(name[1]) is int and name[1]==1, 'GATE_BRANCH_NOT_FULL_STATE')","pass"),
      ('local_guard',"need(inc=={c}, 'LOCAL_DECODER_NOT_SINGLETON_COLOR')","pass"),
      ('visibility_guard',"need(len(incident_colors(v,colors))>=2, 'STATE_NOT_VISIBLE')","pass"),
      ('relation',"need(row['relation']==relation, 'ROW_RELATION_MISMATCH')","pass"),
      ('sign',"need(coeff>0 if relation==target_relation else coeff<0, 'ROW_SIGN')","pass"),
      ('image',"need(parse_vector(advertised,max_id,False)==actual, 'IMAGE_VECTOR_MISMATCH')","pass"),
      ('action_guard',"need(all(colors[fact[i]]==(None if colors[i] is None else c[colors[i]]) for i in range(10)), 'ACTION_CHANGES_COLORING')","pass"),
      ('transport',"mapped=5*permute_mask(mask,vertices)+(colors[b-2]+2 if b>=2 else b)","mapped=5*permute_mask(mask,vertices)+b"),
      ('once_weight',"scale=coeff/len(actions)","scale=coeff*coeff/len(actions)"),
      ('averaged_weight',"scale=coeff/len(actions)","scale=coeff"),
      ('inner_weight',"need(type(row['name']['multiplier']) is int and coeff==row['name']['multiplier'], 'INNER_MULTIPLIER_MISMATCH')","pass"),
      ('data_formula',"for key,value in ((5*a+b,1),(5*a+1,-1)): add(out,key,value)","for key,value in ((5*a+b,-1),(5*a+1,1)): add(out,key,value)"),
      ('pair_formula',"for key,value in ((5*a+1,1),(5*a,1),(5*a+b,-1),(5*a+c,-1)): add(out,key,value)","for key,value in ((5*a+1,1),(5*a,-1),(5*a+b,-1),(5*a+c,-1)): add(out,key,value)"),
      ('gate_formula',"for key,value in ((5*1023,3),(1,17)): add(out,key,value)","for key,value in ((5*1023,3),(1,16)): add(out,key,value)"),
    )
    source=Path(__file__).read_text(encoding='utf-8')
    prefix,marker,suffix=source.partition('\ndef synthetic_smoke(raw):')
    need(bool(marker), 'MUTATION_SECTION_NOT_FOUND')
    killed=[]
    for name,original,replacement in mutations:
        tick()
        need(prefix.count(original)==1, 'MUTATION_ANCHOR_NOT_UNIQUE:' + name)
        altered=prefix.replace(original,replacement,1)+marker+suffix
        namespace={'__name__':'checker_v3_mutant','__file__':__file__}
        exec(compile(altered,'<in-memory-mutant:'+name+'>','exec'),namespace)
        try:
            namespace['control'](name,raw)
        except (AssertionError,namespace['Reject'],namespace['Unknown']):
            killed.append(name)
        else:
            raise Reject('MUTANT_SURVIVED:' + name)
    # Extra fail-closed cases, separate from the one-protection mutants.
    try:
        row_vector(['unrecognized',1],fixture_system(),fixture_scope())
    except Unknown as exc:
        need(str(exc).startswith('UNSUPPORTED_DESCRIPTOR:'), 'UNKNOWN_DESCRIPTOR_REASON')
    else:
        raise Reject('UNKNOWN_DESCRIPTOR_ACCEPTED')
    bad=fixture_scope(); bad['data_processing_semantics']='mutual_information'
    try:
        validate_system(fixture_system(),bad)
    except Unknown as exc:
        need(str(exc).startswith('UNSUPPORTED_SCOPE_FIELDS:'), 'AMBIGUOUS_SCOPE_REASON')
    else:
        raise Reject('AMBIGUOUS_SCOPE_ACCEPTED')
    expect_reject(lambda:parse_json(b'{"x":1,"x":2}'),'DUPLICATE_JSON_KEY:x')
    try:
        read_pinned(MANIFEST.parent/'__absent_declaration_control__',DECLARATION_SHA,27364,685)
    except Unknown as exc:
        need(str(exc).startswith('INPUT_UNAVAILABLE:'), 'ABSENT_INPUT_REASON')
    else:
        raise Reject('ABSENT_INPUT_ACCEPTED')
    return {'fixtures':len(tests),'fixtures_passed':list(tests),'single_mutants':len(mutations),
            'mutants_killed':killed,'extra_controls':['unknown_descriptor','ambiguous_scope','duplicate_json','absent_input']}

def main():
    global DEADLINE
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=('smoke','r382'))
    parser.add_argument('--time-limit-ms',type=int,default=120000)
    parser.add_argument('--max-rows',type=int,default=5000)
    args=parser.parse_args()
    if not 1<=args.time_limit_ms<=120000 or not 1<=args.max_rows<=5000:
        print('INVALID_RESOURCE_CAP',file=sys.stderr); return 2
    started=time.monotonic(); DEADLINE=started+args.time_limit_ms/1000
    for sig in (signal.SIGINT,signal.SIGTERM,signal.SIGALRM): signal.signal(sig,stop)
    signal.setitimer(signal.ITIMER_REAL,args.time_limit_ms/1000)
    result={'mode':args.mode,'status':'UNKNOWN','manifest_sha256':MANIFEST_SHA,
            'declaration_sha256':DECLARATION_SHA,'predecessor_sha256':PREDECESSOR_SHA,
            'checker_sha256':sha256(Path(__file__).read_bytes()),
            'claim_boundary':'same-harness prospective checks only; no scientific theorem, full replay, provenance equality or coverage acceptance'}
    code=3
    try:
        manifest,raw,sources=verify_sources()
        result['source_bindings']=sources
        if args.mode=='smoke':
            result['details']=synthetic_smoke(raw)
            result['status']='SYNTHETIC_CONTROLS_PASS'; code=0
        else:
            result['archive_sha256']=ARCHIVE_SHA; result['record_sha256']=R382_SHA
            result['record_bytes']=R382_SIZE; result['record_index']=1
            result['details']=diagnostic_r382(manifest,args.max_rows)
            result['status']='R382_IDENTITY_CONDITIONAL'; code=0
    except Reject as exc:
        result['status']='REJECT'; result['reason']=str(exc); code=2
    except (Unknown,OSError) as exc:
        result['status']='UNKNOWN'; result['reason']=str(exc); code=3
    except Exception as exc:
        result['status']='UNKNOWN'; result['reason']='UNEXPECTED_EXCEPTION:'+type(exc).__name__+':'+str(exc); code=3
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
    result['elapsed_ms']=int((time.monotonic()-started)*1000)
    print(json.dumps(result,sort_keys=True,allow_nan=False))
    return code

if __name__=='__main__':
    sys.exit(main())
