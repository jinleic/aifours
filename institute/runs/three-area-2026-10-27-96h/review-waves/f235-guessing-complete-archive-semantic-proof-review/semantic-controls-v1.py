#!/usr/bin/env python3
"""Small, definition-first controls; does not read the archive or enumerate its atlas."""
from collections import Counter
from itertools import product
import json

N = {
 1:{2,3,4,5,6,7}, 2:{1,3,7,9,10}, 3:{1,2,4,8,9},
 4:{1,3,5,8,10}, 5:{1,4,6,9,10}, 6:{1,5,7,8,9},
 7:{1,2,6,8,10}, 8:{3,4,6,7,9,10}, 9:{2,3,5,6,8},
 10:{2,4,5,7,8},
}
T = [(1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),
     (3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8)]
G8 = [
 (1,2,3,4,5,6,7,8,9,10), (1,2,7,6,5,4,3,8,10,9),
 (1,5,4,3,2,7,6,8,10,9), (1,5,6,7,2,3,4,8,9,10),
 (8,9,3,4,10,7,6,1,2,5), (8,9,6,7,10,4,3,1,5,2),
 (8,10,4,3,9,6,7,1,5,2), (8,10,7,6,9,3,4,1,2,5),
]
G4 = [G8[i] for i in (0,2,4,6)]
INDUCED = [(0,1,2,3,4,5,6,7,8,9), (1,0,2,6,8,7,3,5,4,9),
           (5,7,9,3,8,0,6,1,4,2), (7,5,9,6,4,1,3,0,8,2)]
COLORS = {2:0,3:1,4:2,5:0,6:1,7:2,8:0,9:2,10:1}

class Rejection(Exception):
    pass

def need(condition, reason):
    if not condition:
        raise Rejection(reason)

def expected_rejection(label, fn, reason):
    try:
        fn()
    except Rejection as e:
        need(str(e) == reason, 'wrong_rejection_reason:' + label + ':' + str(e))
        negatives[label] = str(e)
    else:
        raise Rejection('unexpected_acceptance:' + label)

def image(g, v):
    return g[v-1]

def graph_action(g):
    need(set(g) == set(N), 'not_vertex_permutation')
    need(all({image(g,u) for u in N[v]} == N[image(g,v)] for v in N),
         'not_graph_automorphism')

def factor_action(g):
    graph_action(g)
    index = {frozenset(tri): i for i,tri in enumerate(T)}
    mapped = [frozenset(image(g,v) for v in tri) for tri in T]
    need(all(x in index for x in mapped), 'not_factor_automorphism')
    return tuple(index[x] for x in mapped)

def preserve_selected(g, selected):
    induced = factor_action(g)
    need({induced[t] for t in selected} == selected, 'selected_factors_not_preserved')

def check_coloring(c):
    need(set(c) == set(N)-{1}, 'incomplete_coloring')
    need(all(c[u] != c[v] for u in c for v in N[u] if v in c),
         'not_proper_coloring')

def compose(g,h):
    return tuple(image(g,image(h,v)) for v in N)

def closed(group):
    s = set(group)
    return len(s) == len(group) and all(compose(g,h) in s for g in group for h in group)

def distinct_by_key(states, key, target):
    table = {}
    for state in states:
        k, value = key(state), target(state)
        if k in table and table[k] != value:
            return False
        table[k] = value
    return True

def ent(states, key):
    counts = Counter(key(s) for s in states)
    need(len(set(counts.values())) == 1 and len(counts) & (len(counts)-1) == 0,
         'nonuniform_or_nonbinary_entropy_control')
    return len(counts).bit_length()-1

def make_state(a,b,c):
    bits = {(v,t):0 for t,tri in enumerate(T) for v in tri}
    bits[1,0] = c
    bits[2,0] = c
    bits[3,0] = a
    bits[4,1] = a
    for v in T[3]:
        bits[v,3] = b
    x = {v: tuple(bits[v,t] for t,tri in enumerate(T) if v in tri) for v in N}
    selected = (0,1,3)
    y = {v: tuple(bits[v,t] for t in selected if v in T[t]) for v in N}
    sigma = tuple(sum(bits[v,t] for v in tri) % 2 for t,tri in enumerate(T))
    return {'x':x, 'y':y, 's':(a,b), 'sigma':sigma}

def vals(state, kind, vertices):
    return tuple(state[kind][v] for v in sorted(vertices))

def local_set(v):
    return set().union(*(set(T[t])-{v} for t in (0,1,3) if v in T[t]))

def local_determined(v, auxiliary):
    need(distinct_by_key(states,
         lambda q:(vals(q,'y',local_set(v)), auxiliary(q)),
         lambda q:q['y'][v]), 'local_not_determined')

def check_color_perm(perm):
    need(set(perm) == {1,2,3} and len(perm) == 3, 'not_color_bijection')

negatives = {}
need(all(v not in N[v] and all(v in N[w] for w in N[v]) for v in N), 'bad_graph')
need(sum(map(len,N.values())) == 52 and 4 in N[3] and 10 not in N[9], 'bad_edge_set')
need(all(len(set(t)) == 3 and all(w in N[v] for v in t for w in t if v != w) for t in T), 'bad_triangle')
need(all(sum(v in t for t in T)==3 for v in N), 'bad_incidence')
need(closed(G8) and closed(G4), 'not_a_group')
for g in G8:
    graph_action(g)
need([factor_action(g) for g in G4] == INDUCED, 'wrong_induced_factor_action')
check_coloring(COLORS)
expected_rejection('graph_only_is_not_factor_action', lambda:factor_action(G8[1]), 'not_factor_automorphism')
expected_rejection('selected_set_must_be_preserved', lambda:preserve_selected(G4[1],{0,1,3}), 'selected_factors_not_preserved')
bad_colors = dict(COLORS); bad_colors[3] = 0
expected_rejection('bad_delete1_coloring', lambda:check_coloring(bad_colors), 'not_proper_coloring')

states = [make_state(a,b,c) for a,b,c in product((0,1), repeat=3)]
for v in N:
    need(distinct_by_key(states, lambda q:vals(q,'x',N[v]), lambda q:q['x'][v]),
         'original_neighbor_fd_failed:' + str(v))
    local_determined(v, lambda q:q['s'])
need(all(q['sigma'] == (q['s'][0],q['s'][0],0,q['s'][1],0,0,0,0,0,0) for q in states),
     'syndrome_not_intended_plane')
need(distinct_by_key(states, lambda q:vals(q,'y',N), lambda q:q['s']), 'full_syndrome_not_visible')
need(4 not in local_set(3) and 3 not in local_set(4), 'incorrect_local_set')
local_determined(4, lambda q:q['s'][0])
expected_rejection('wrong_singleton_functional', lambda:local_determined(4,lambda q:q['s'][1]), 'local_not_determined')
expected_rejection('two_incident_colors_one_functional', lambda:local_determined(3,lambda q:q['s'][1]), 'local_not_determined')
full_local3 = set().union(*(set(t)-{3} for t in T if 3 in t))
need(not distinct_by_key(states, lambda q:(vals(q,'x',full_local3),q['sigma'][2]),
                         lambda q:q['x'][3]), 'partial_aux_counterexample_missing')

hY = ent(states, lambda q:vals(q,'y',N))
hS = ent(states, lambda q:q['s'])
hjoint = sum(ent(states, lambda q:(q['y'][v],q['s'])) for v in N)
hY_given_S = ent(states,lambda q:(vals(q,'y',N),q['s'])) - hS
hsingles_given_S = sum(ent(states,lambda q:(q['y'][v],q['s']))-hS for v in N)
gate = 3*hY + 17*hS - 2*hjoint
need(gate == 3*hY_given_S - 2*hsingles_given_S and gate <= 0, 'gate_identity_or_sign')
need(3*hY + 18*hS - 2*hjoint > 0, 'mutated_gate_not_refuted')
expected_rejection('wrong_gate_coefficient', lambda:need(3*hY+18*hS-2*hjoint <= 0,'gate_inequality_false'), 'gate_inequality_false')

def parity(z): return z.bit_count() % 2
perms = {tuple(parity(form & c1) + 2*parity(form & c2) for form in (1,2,3))
         for c1 in (1,2,3) for c2 in (1,2,3) if c1 != c2}
need(len(perms)==6 and all(set(p)=={1,2,3} for p in perms), 'bad_gl2_action')
expected_rejection('duplicate_color_action', lambda:check_color_perm((1,1,3)), 'not_color_bijection')
print(json.dumps({'scope':'tiny literal-graph and eight-state controls, not archive replay',
 'graph_edges':26,'graph_action_count':8,'factor_action_count':4,'gl2_color_permutations':len(perms),
 'law_support_size':len(states),'original_neighbor_fds':'verified_for_this_law',
 'actual_local_full_S_fds':'verified_for_this_law',
 'syndrome_support':'(a,a,0,b,0,0,0,0,0,0), all four a,b',
 'gate':{'H_Y':hY,'H_S':hS,'sum_H_Yv_S':hjoint,'G_S':gate,'mutated_plus18':3*hY+18*hS-2*hjoint},
 'intended_reason_negative_controls':negatives}, indent=2, sort_keys=True))
