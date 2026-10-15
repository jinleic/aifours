"""Independent primitive-space and exact determinant audit. No producer import."""
from fractions import Fraction as Q
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import json, hashlib
import check_level4_invariant as independent

CELLS={(2,2,4):(7,25,13),(3,2,4):(6,36,13),(2,3,4):(6,36,13),(3,3,4):(8,65,18)}
ACTION={(a,i):independent.adjoint_action(a,i) for a in (0,1,2,3,4) for i in range(8)}

def clean(p):return {w:c for w,c in p.items() if c}

def linear_span(vectors):
    basis={}
    for original in vectors:
        v=dict(original)
        for pivot,row in sorted(basis.items()):
            scalar=v.get(pivot,Q(0))
            if scalar:
                for w,c in row.items():v[w]=v.get(w,Q(0))-scalar*c
                v=clean(v)
        if not v:continue
        pivot=min(v);c=v[pivot];v={w:x/c for w,x in v.items()}
        # Keep a reduced basis, unlike the producer's forward echelon basis.
        for old,row in list(basis.items()):
            scalar=row.get(pivot,Q(0))
            if scalar:
                basis[old]=clean({w:row.get(w,Q(0))-scalar*v.get(w,Q(0)) for w in set(row)|set(v)})
        basis[pivot]=v
    return basis

def reduce(v,basis):
    v=dict(v)
    for pivot,row in sorted(basis.items()):
        scalar=v.get(pivot,Q(0))
        if scalar:
            for w,c in row.items():v[w]=v.get(w,Q(0))-scalar*c
            v=clean(v)
    return v

def action(actor,p):
    out=defaultdict(Q)
    for w,c in p.items():
        for pos,i in enumerate(w):
            for j,d in ACTION[actor,i].items():out[w[:pos]+(j,)+w[pos+1:]]+=c*d
    return clean(out)

def lie_space(a,b,k):
    vectors=[]
    for w in product(range(8),repeat=k):
        if tuple(sum(independent.FULL[i][j] for i in w) for j in (0,1))==(a,b):
            vectors.append(independent.bracket_word(w))
    return linear_span(vectors)

def lower(p):
    leaf={3:(1,2,Q(-1)),4:(0,1,Q(1)),5:(-1,0,Q(-1)),6:(2,2,Q(-1)),7:(2,1,Q(-1))}
    result=defaultdict(lambda:[Q(0)]*3);terminal=defaultdict(Q)
    for w,c in p.items():
        for pos,letter in enumerate(w):
            if letter not in leaf:continue
            actor,slot,d=leaf[letter];deleted=w[:pos]+w[pos+1:]
            terminal[deleted,actor,slot]+=c*d
            for later in range(pos+1,len(w)):
                if actor==-1:
                    a,b=independent.FULL[w[later]]
                    for j,weight in enumerate((2,-a,-b)):result[deleted][j]+=c*d*weight
                else:
                    for new,value in ACTION[actor,w[later]].items():
                        replacement=deleted[:later-1]+(new,)+deleted[later:]
                        result[replacement][slot]+=c*d*value
    assert not clean(terminal)
    return {w:tuple(c) for w,c in result.items() if any(c)}

def add(a,b,sign=1):
    p=defaultdict(Q,a)
    for w,c in b.items():p[w]+=sign*c
    return clean(p)

def multiply(a,b):
    p=defaultdict(Q)
    for (i,j),c in a.items():
        for (k,l),d in b.items():p[i+k,j+l]+=c*d
    return clean(p)

def laplace(matrix):
    @lru_cache(None)
    def rec(row,cols):
        if not cols:return {(0,0):Q(1)}
        out={}
        for position,col in enumerate(cols):
            out=add(out,multiply(matrix[row][col],rec(row+1,cols[:position]+cols[position+1:])),(-1)**position)
        return out
    return rec(0,tuple(range(len(matrix))))

def unpack(items):
    p={tuple(w):Q(c) for w,c in items};assert len(p)==len(items);return p

def same(a,b):
    assert a==b,'Altered exact evidence'

def main():
    root=Path(__file__).resolve().parent;p=root/'level4-cells-certificate.json'
    payload=json.loads(p.read_text());records=payload['records']
    assert {tuple(r['degree']) for r in records}==set(CELLS) and len(records)==4
    receipts=[]
    for record in records:
        degree=tuple(record['degree']);a,b,_=degree;pdim,ldim,tdim=CELLS[degree]
        same((record['primitive_dimension'],record['free_dimension'],record['target_dimension']),(pdim,ldim,tdim))
        L=lie_space(a,b,4);T=lie_space(a,b,3);same((len(L),len(T)),(ldim,tdim))
        packed=[]
        for v in L.values():
            packed.append({(actor,w):c for actor in (3,4) for w,c in action(actor,v).items()})
        assert ldim-len(linear_span(packed))==pdim
        primitive=[unpack(v) for v in record['primitive_basis']]
        assert len(primitive)==pdim and len(linear_span(primitive))==pdim
        for v in primitive:
            assert v and not reduce(v,L) and not action(3,v) and not action(4,v)
            for w in v:assert len(w)==4 and tuple(sum(independent.FULL[i][j] for i in w) for j in (0,1))==(a,b)
        images=[lower(v) for v in primitive]
        saved=[{tuple(w):tuple(Q(x) for x in c) for w,c in v} for v in record['lowering_images']]
        same(images,saved)
        for v in images:
            for slot in range(3):assert not reduce({w:c[slot] for w,c in v.items() if c[slot]},T)
        rows=[tuple(w) for w in record['minor']['rows']]
        assert len(rows)==pdim and len(set(rows))==pdim
        matrix=[]
        for w in rows:
            row=[]
            for image in images:
                c,r,s=image.get(w,(Q(0),)*3)
                row.append(clean({(0,0):c+4*r+4*s,(1,0):r,(0,1):s}))
            matrix.append(row)
        determinant=laplace(matrix);saved_det=unpack(record['minor']['det_shift_4'])
        same(determinant,saved_det)
        orientation=record['minor']['orientation'];assert orientation in (1,-1)
        assert orientation*determinant.get((0,0),0)>0
        assert all(orientation*c>0 for c in determinant.values())
        # Use the same exact comparison exercised above to reject two mutations.
        altered=dict(saved_det);first=next(iter(altered));altered[first]+=1
        try:same(determinant,altered)
        except AssertionError:pass
        else:raise AssertionError('determinant mutation accepted')
        altered_image=dict(saved[0]);first=next(iter(altered_image));c=altered_image[first]
        altered_image[first]=(c[0]+1,c[1],c[2])
        try:same(images[0],altered_image)
        except AssertionError:pass
        else:raise AssertionError('lowering mutation accepted')
        receipts.append({'degree':list(degree),'dimensions':[pdim,ldim,tdim],
          'positive_minor_terms':len(determinant),'positive_constant':str(orientation*determinant[(0,0)]),
          'primitive_basis_complete':True,'all_affine_images_checked':True,'mutations_rejected':2})
        print('Independently checked',degree,flush=True)
    assert {tuple(r['degree']) for r in records[:-1]}!=set(CELLS)
    receipt={'status':'PASS','scope':'Complete level-four primitive detection for A(r,s), r,s>=4, together with prior trivial-line and height-seven premises',
      'full_goal_solved':False,'producer_imported':False,'records':receipts,
      'determinant_method':'Independent memoized Laplace expansion in Q[x,y]',
      'basis_method':'Rebuilt all Dynkin images, Levi lowering ranks and primitive-space dimensions',
      'omitted_cell_rejected':True,
      'sha256':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in [
        p.name,'level4_cells_producer.py','level4_cells_check.py','level4_invariant_check.py','check_level4_invariant.py']}}
    (root/'level4-cells-independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
