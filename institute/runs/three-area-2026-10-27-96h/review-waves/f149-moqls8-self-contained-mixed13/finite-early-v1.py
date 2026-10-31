#!/usr/bin/env python3
"""Direct small-board controls for the ten/eleven/twelve-cell 4x4 cases."""
import argparse, collections, hashlib, itertools, json, pathlib, subprocess, sys


def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def stamp(): return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()


def boards(rows,cols):
    n=sum(rows)
    for a in itertools.combinations(range(16),n):
        board={(x//4,x%4) for x in a}
        if [sum(i==k for i,j in board) for k in range(4)] != list(rows): continue
        if [sum(j==k for i,j in board) for k in range(4)] != list(cols): continue
        yield board


def components(nodes,adj):
    unseen=set(nodes); out=[]
    while unseen:
        v=unseen.pop(); stack=[v]; part=[v]
        while stack:
            for w in adj[stack.pop()]:
                if w in unseen:
                    unseen.remove(w); stack.append(w); part.append(w)
        out.append(part)
    return out


def ten_controls():
    out=collections.Counter()
    for e in boards((3,3,2,2),(3,3,2,2)):
        if any(sum((i,j) in e for j in (2,3))>1 for i in (0,1)): continue
        if any(sum((i,j) in e for i in (2,3))>1 for j in (0,1)): continue
        assert all((i,j) in e for i in (0,1) for j in (0,1))
        boundary=[x for x in e if x[0]>=2 or x[1]>=2]
        assert len(boundary)==6
        adj={x:set() for x in boundary}
        for a,b in itertools.combinations(boundary,2):
            if (a[0]==b[0] and a[0]>=2) or (a[1]==b[1] and a[1]>=2):
                adj[a].add(b); adj[b].add(a)
        comps=components(boundary,adj)
        key=tuple(sorted(len(z) for z in comps))
        assert key in ((2,4),(3,3))
        out[str(key)]+=1
    assert out=={'(2, 4)':8,'(3, 3)':8}
    return {'fixed_high_line_labels_boundary_path_counts':dict(out),'both_shapes_seen':True}


def eleven_controls():
    board_counts=collections.Counter(); assignment_counts=collections.Counter()
    for e in boards((3,3,3,2),(3,3,3,2)):
        kind='low_low_present' if (3,3) in e else 'low_low_absent'
        board_counts[kind]+=1
        core=sorted((i,j) for i,j in e if i<3 and j<3)
        forced={x for x in e if 3 in x}
        for mask in range(1<<len(core)):
            size2=forced|{core[t] for t in range(len(core)) if mask>>t&1}
            if any(sum((i,j) in size2 for j in range(4))>1 for i in range(3)): continue
            if any(sum((i,j) in size2 for i in range(4))>1 for j in range(3)): continue
            full=[x for x in core if x not in size2]
            adj={i:set() for i in range(6)}
            for i,j in full: adj[i].add(3+j); adj[3+j].add(i)
            assert all(len(adj[v])>=2 for v in range(6))
            assert len(components(range(6),adj))==1
            assignment_counts[kind]+=1
    assert board_counts=={'low_low_present':9,'low_low_absent':18}
    return {'fixed_low_line_labels_graph_counts':dict(board_counts),
            'support_cardinality_assignments_checked':dict(assignment_counts),
            'every_full_support_core_connected':True,
            'mutation_allow_multiple_support2_on_a_degree3_line':'all core cells set support-2 leaves a disconnected empty full-support graph'}


def twelve_bb_controls():
    profiles=(4,3,3,2); board_counts=collections.Counter(); assignment_counts=collections.Counter(); examples={}
    for e in boards(profiles,profiles):
        kind='low_low_present' if (3,3) in e else 'low_low_absent'
        board_counts[kind]+=1
        edges=sorted(e)
        domains=[range(2,min(profiles[i],profiles[j])+1) for i,j in edges]
        for vals in itertools.product(*domains):
            if any(not line_valid([vals[k] for k,(i,j) in enumerate(edges) if i==v],profiles[v]) for v in range(4)): continue
            if any(not line_valid([vals[k] for k,(i,j) in enumerate(edges) if j==v],profiles[v]) for v in range(4)): continue
            assignment_counts[kind]+=1
            examples[kind]=[list(x)+[v] for x,v in zip(edges,vals)]
    assert board_counts=={'low_low_present':1,'low_low_absent':4}
    assert assignment_counts['low_low_absent']==0
    assert assignment_counts['low_low_present']>=1
    return {'fixed_all_degree_labels_graph_counts':dict(board_counts),
            'necessary_support_size_assignments':dict(assignment_counts),
            'surviving_size_example_not_an_actual_QLS':examples['low_low_present']}


def line_valid(vals,k):
    a=vals.count(2); b=vals.count(3)
    if k==3 and a>1: return False
    if k==4 and ((a>=2 and b>=1) or (a>=1 and b>=2)): return False
    return True


def main():
    p=argparse.ArgumentParser(); p.add_argument('--out',required=True); a=p.parse_args()
    out=pathlib.Path(a.out)
    if out.exists(): raise SystemExit('refusing overwrite')
    start=stamp()
    d={'kind':'finite-early-casechecks-v1','script_sha256':sha(__file__),
       'prior_result_sha256':sha('finite-results-v1.json'),'python':sys.version,'clock_before':start,
       'P05_ten_cell_boundary':ten_controls(),'P07_eleven_cell_BB':eleven_controls(),
       'P21_twelve_cell_BB':twelve_bb_controls()}
    d['clock_immediately_before_output']=stamp()
    with out.open('x',encoding='utf-8') as f: json.dump(d,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'output':str(out),'sha256':sha(out),'script_sha256':d['script_sha256'],'clock':d['clock_immediately_before_output']}))


if __name__=='__main__': main()
