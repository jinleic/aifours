# Executed only in the reviewer's Python Eval kernel; imports no author checker.
# Exact finite row/graph checks, conditional on PDF-to-text and figure fidelity.
from pathlib import Path
from fractions import Fraction
from collections import Counter, defaultdict
import hashlib, re

f26_root = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus')
f26_files = {
    'layout': ('frontier-20261028-gurpinar-annexc-pdf-layout.txt','6ff906bb54ddf33e46d5bfcddf50ffa0680c0315e118d6530e6f13f36adc2ca5'),
    'txt': ('frontier-20261028-gurpinar-annexc-original.txt','b0bd3f614397ed11edd475efdc4acb6e8f326c6722ede71d5a08760d84578b22'),
}
f26_bytes = {}
for kind, (name, expected) in f26_files.items():
    data = (f26_root / name).read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('INPUT_HASH:'+kind)
    f26_bytes[kind] = data

# Ordered finite-variable encoding; the original ten names are the low bits.
f26_names = ('a','b','c','d','e','f','g','h','i','j','b’0','d’1','e’1','g’2','f’3','g’3','h’4')
f26_bits = {s: 1 << i for i,s in enumerate(f26_names)}
f26_original = (1 << 10)-1

def f26_mask(names):
    out = 0
    for x in names:
        if x not in f26_bits or (out & f26_bits[x]):
            raise ValueError('VARIABLE:'+x)
        out |= f26_bits[x]
    return out

def f26_vec(pairs):
    d = defaultdict(int)
    for mask, sign in pairs:
        if mask: # H(empty)=0
            d[mask] += sign
    return {a:b for a,b in d.items() if b}

# Permutations transcribed from the article Appendix B, not inferred from rows.
def f26_perm(cycles):
    p=list(range(10))
    for cycle in cycles:
        for x,y in zip(cycle, cycle[1:]+cycle[:1]): p[x-1]=y-1
    return tuple(p)
f26_sigma=f26_perm([(1,8),(2,10,5,9),(3,7,4,6)])
f26_tau=f26_perm([(2,5),(3,6),(4,7)])
f26_edges=frozenset(tuple(sorted(e)) for e in [
 (1,2),(1,3),(1,4),(1,5),(1,6),(1,7),
 (2,3),(2,7),(2,9),(2,10),(3,4),(3,8),(3,9),
 (4,5),(4,8),(4,10),(5,6),(5,9),(5,10),
 (6,7),(6,8),(6,9),(7,8),(7,10),(8,9),(8,10)])
def f26_map_edges(p): return frozenset(tuple(sorted((p[a-1]+1,p[b-1]+1))) for a,b in f26_edges)
for p in (f26_sigma,f26_tau):
    if f26_map_edges(p) != f26_edges: raise ValueError('GRAPH_AUTOMORPHISM')
f26_group={tuple(range(10))}
while True:
    expanded = f26_group | {tuple(p[q[i]] for i in range(10)) for p in f26_group for q in (f26_sigma,f26_tau)}
    if expanded==f26_group: break
    f26_group=expanded
if len(f26_group)!=8: raise ValueError('GROUP_SIZE')

def f26_image(mask,p):
    return sum(1 << p[i] for i in range(10) if mask & (1<<i))
def f26_neighbors(edges):
    return {i:f26_mask([f26_names[y-1] for edge in edges if i in edge for y in edge if y!=i]) for i in range(1,11)}
f26_adj=f26_neighbors(f26_edges)

# Conditional-kernel steps: (original tuple, new tuple, conditioning base, prior branch variables).
f26_steps = [
 (('b',),('b’0',),('a','d','e','f','g','h','i','j'),()),
 (('d','e'),('d’1','e’1'),('a','b','c','f','g','h','i'),()),
 (('g',),('g’2',),('a','b','c','d','e’1','f','h','i'),('d’1','e’1')),
 (('f','g'),('f’3','g’3'),('a','b','c','d','e','h','i','j'),()),
 (('h',),('h’4',),('a','b','c','d','e','f','f’3','i','j'),('f’3','g’3')),
]
f26_cis=[]
for old,new,base,previous in f26_steps:
    O,N,B,P=f26_mask(old),f26_mask(new),f26_mask(base),f26_mask(previous)
    past=f26_original|P
    if O & B or N & past or B & ~past or O & ~past: raise ValueError('COPY_STEP')
    # I(new; past minus base | base)=0.
    f26_cis.append(f26_vec([(B|N,1),(past,1),(past|N,-1),(B,-1)]))

def f26_is_copy(left,right):
    shared=left & right
    for old,new,base,_ in f26_steps:
        OM,NM,B=f26_mask(old),f26_mask(new),f26_mask(base)
        for l,r in ((left,right),(right,left)):
            olddiff=l & ~r
            newdiff=r & ~l
            if not olddiff or olddiff & ~OM or newdiff & ~NM or shared & ~B: continue
            mapped=0
            for x,y in zip(old,new):
                if olddiff & f26_bits[x]: mapped |= f26_bits[y]
            if mapped==newdiff: return True
    return False

def f26_classify(row,adj=f26_adj):
    vec, rel, rhs, coeff, _ = row
    if coeff==0: raise ValueError('ZERO_WEIGHT')
    if rel=='>=' and (rhs!=0 or coeff>=0): raise ValueError('GE_SIGN')
    if rel=='<=' and (rhs!=1 or coeff<=0): raise ValueError('LE_SIGN')
    if rel=='=' and rhs!=0: raise ValueError('EQ_RHS')
    if rel=='<=':
        if len(vec)==1 and next(iter(vec.values()))==1 and next(iter(vec)) in [1<<i for i in range(10)]: return 'cap'
        raise ValueError('ROW')
    plus=[k for k,v in vec.items() if v==1]
    minus=[k for k,v in vec.items() if v==-1]
    if any(abs(v)!=1 for v in vec.values()): raise ValueError('ROW')
    if rel=='>=':
        if len(plus)==2:
            A,B=plus
            if f26_vec([(A,1),(B,1),(A|B,-1),(A&B,-1)])==vec: return 'cmi'
        if len(plus)==len(minus)==1:
            A,B=plus[0],minus[0]
            if B & ~A==0: return 'conditional_entropy'
            diff=B & ~A
            if A & ~B==0 and diff and diff & (diff-1)==0 and diff<=1<<9:
                vertex=diff.bit_length()
                if A==adj[vertex]: return 'graph_fd'
        raise ValueError('ROW')
    if rel=='=':
        if vec in f26_cis or {k:-v for k,v in vec.items()} in f26_cis: return 'copy_independence'
        if len(plus)==len(minus)==1:
            A,B=plus[0],minus[0]
            if (A|B) & ~f26_original==0 and any(f26_image(A,p)==B for p in f26_group): return 'symmetry'
            if f26_is_copy(A,B): return 'copy_marginal'
        raise ValueError('ROW')
    raise ValueError('RELATION')

# Strict parser consumes every line (apart from specified intro, blanks, page folios).
def f26_parse_text(layout,txt):
    lines=layout.decode('utf-8').splitlines()
    expected_intro=['A CERTIFICATE OF 1847⁄276 BOUND',
      'The following are the 1920 inequalities with their respective non-zero coefficients derived',
      'from the rational solution of the shortened linear program, which has optimal value 1847','276 .']
    nonblank_intro=[l.strip() for l in lines[:8] if l.strip()]
    if nonblank_intro!=expected_intro: raise ValueError('INTRO')
    pending=None; rows=[]; folios=[]
    pat=re.compile(r'\s*([+-]?)\s*H\{([^{}]+)\}')
    for lineno,line in enumerate(lines[8:],9):
        s=line.strip()
        if not s: continue
        if s.isdigit():
            folios.append(int(s)); continue
        if s.startswith('with coefficient '):
            if pending is None: raise ValueError('COEFF_WITHOUT_ROW')
            m=re.fullmatch(r'with coefficient\s+([+-]?\d+(?:/\d+)?)',s)
            if not m: raise ValueError('COEFF_PARSE')
            rows.append((*pending,Fraction(m.group(1)),lineno)); pending=None; continue
        if pending is not None: raise ValueError('MISSING_COEFF')
        m=re.fullmatch(r'(.+?)\s*(>=|<=|=)\s*(\d+)',s)
        if not m: raise ValueError('EXPRESSION')
        expression,rel,rhs=m.group(1),m.group(2),int(m.group(3))
        pos=0; items=[]
        while pos < len(expression):
            q=pat.match(expression,pos)
            if not q: raise ValueError('TERM_PARSE')
            sign=q.group(1)
            if items and not sign: raise ValueError('MISSING_OPERATOR')
            items.append((f26_mask(q.group(2).split('.')),-1 if sign=='-' else 1))
            pos=q.end()
        pending=(f26_vec(items),rel,rhs)
    if pending is not None or folios!=list(range(2,61)): raise ValueError('LAYOUT_END')
    if len(rows)!=1920: raise ValueError('ROW_COUNT')
    txtlines=txt.decode('utf-8').splitlines()
    if not txtlines or txtlines[0]!='Objective Value = 1847/276' or len(txtlines)!=1921: raise ValueError('TXT_HEADER_COUNT')
    names=[]
    for i,line in enumerate(txtlines[1:]):
        m=re.fullmatch(r'([A-Za-z0-9_/]+)\s*=\s*([+-]?\d+(?:/\d+)?)',line.strip())
        if not m: raise ValueError('TXT_PARSE')
        names.append(m.group(1))
        if Fraction(m.group(2))!=rows[i][3]: raise ValueError('COEFFICIENT_MISMATCH')
    if len(set(names))!=len(names): raise ValueError('TXT_DUPLICATE')
    return rows,names,folios

def f26_audit(rows):
    if len(rows)!=1920: raise ValueError('ROW_COUNT')
    counts=Counter(); total=defaultdict(Fraction); bound=Fraction(0)
    for row in rows:
        kind=f26_classify(row); counts[kind]+=1
        vec,rel,rhs,weight,_=row
        for mask,entry in vec.items(): total[mask]+=entry*weight
        bound += rhs*weight
    nonzero={m:v for m,v in total.items() if v}
    if nonzero!={f26_original:Fraction(1)} or bound!=Fraction(1847,276): raise ValueError('WEIGHTED_IDENTITY')
    return dict(counts),nonzero,bound

f26_rows_checked,f26_row_names,f26_folios=f26_parse_text(f26_bytes['layout'],f26_bytes['txt'])
f26_counts,f26_acc,f26_bound=f26_audit(f26_rows_checked)

# In-memory mutation controls; no source bytes are changed.
f26_controls=[]
def f26_expect(label,expected,fn):
    try: fn()
    except ValueError as exc:
        actual=str(exc)
        if actual != expected: raise ValueError('CONTROL_'+label+':'+actual+'!='+expected)
        f26_controls.append((label,actual)); return
    raise ValueError('CONTROL_ACCEPTED_'+label)
f26_expect('drop_row','ROW_COUNT',lambda:f26_audit(f26_rows_checked[:-1]))
f26_i=next(i for i,r in enumerate(f26_rows_checked) if f26_classify(r)=='cmi')
f26_bad=list(f26_rows_checked); r=f26_bad[f26_i]; f26_bad[f26_i]=(r[0],r[1],r[2],-r[3],r[4])
f26_expect('reverse_cmi_weight','GE_SIGN',lambda:f26_audit(f26_bad))
f26_bad=list(f26_rows_checked); r=f26_bad[f26_i]; f26_bad[f26_i]=(r[0],r[1],r[2],r[3]*2,r[4])
f26_expect('alter_weight_preserve_sign','WEIGHTED_IDENTITY',lambda:f26_audit(f26_bad))
f26_fd=next(r for r in f26_rows_checked if f26_classify(r)=='graph_fd')
f26_fdmask=next(k for k,v in f26_fd[0].items() if v==1)
f26_larger=next(k for k,v in f26_fd[0].items() if v==-1)
f26_v=(f26_larger & ~f26_fdmask).bit_length()
f26_n=next(j for j in range(1,11) if f26_fdmask & (1<<(j-1)))
f26_broken=f26_edges-{tuple(sorted((f26_v,f26_n)))}
f26_expect('remove_fd_neighbor','ROW',lambda:f26_classify(f26_fd,f26_neighbors(f26_broken)))
f26_copyrow=next(r for r in f26_rows_checked if f26_classify(r)=='copy_marginal')
f26_vmap=dict(f26_copyrow[0]); f26_oldmask=next(k for k,v in f26_vmap.items() if v==1)
f26_vmap[f26_oldmask | f26_bits['h’4']]=f26_vmap.pop(f26_oldmask)
f26_copybad=(f26_vmap,*f26_copyrow[1:])
f26_expect('add_unrelated_copy_to_marginal','ROW',lambda:f26_classify(f26_copybad))
print('f26 exact replay:', {'row_count':len(f26_rows_checked),'folios':(f26_folios[0],f26_folios[-1],len(f26_folios)), 'group_order':len(f26_group), 'edge_count':len(f26_edges),'row_classes':f26_counts,'coefficient_matches':len(f26_row_names),'lhs':f26_acc,'rhs':str(f26_bound),'controls':f26_controls})
