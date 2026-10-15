"""Four fixed level-four primitive cells; exact rational affine minors."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib, json, random, time
import level4_invariant_check as old

CELLS = [(2,2,7,25,13),(3,2,6,36,13),(2,3,6,36,13),(3,3,8,65,18)]
DEADLINE = time.monotonic()+180

def addto(a,b,c=Q(1)):
    a=dict(a)
    for w,v in b.items():
        a[w]=a.get(w,Q(0))+c*v
        if not a[w]: del a[w]
    return a

def span(vectors):
    pivots={}
    for vector in vectors:
        v=dict(vector)
        while v:
            p=min(v)
            if p not in pivots:
                c=v[p]; pivots[p]={w:x/c for w,x in v.items()}; break
            v=addto(v,pivots[p],-v[p])
    return [pivots[p] for p in sorted(pivots)]

def nullspace(rows,n):
    pivots={}
    for row in rows:
        v={i:c for i,c in enumerate(row) if c}
        while v:
            p=min(v)
            if p not in pivots:
                c=v[p];pivots[p]={i:x/c for i,x in v.items()};break
            v=addto(v,pivots[p],-v[p])
    answer=[]
    for free in sorted(set(range(n))-set(pivots)):
        x=[Q(0)]*n;x[free]=Q(1)
        for p,row in sorted(pivots.items(),reverse=True):
            x[p]=-sum(c*x[i] for i,c in row.items() if i!=p)
        answer.append(x)
    return answer

ACTION={}
for actor in (3,4):
    for letter in range(8):
        ACTION[actor,letter]={i:c for i,c in enumerate(old.coordinates(old.matrix_bracket(
            old.BASIS[actor],old.BASIS[letter]))) if c}

def action(actor,p):
    out={}
    for w,c in p.items():
        for pos,letter in enumerate(w):
            for new,d in ACTION[actor,letter].items():
                word=w[:pos]+(new,)+w[pos+1:]
                out[word]=out.get(word,Q(0))+c*d
    return {w:c for w,c in out.items() if c}

def words(a,b,k):
    return [w for w in product(range(8),repeat=k)
      if sum(old.DEGREES[i][0] for i in w)==a and sum(old.DEGREES[i][1] for i in w)==b]

def tree(w):
    return w[0] if len(w)==1 else (w[0],tree(w[1:]))

def polyadd(a,b,c=Q(1)):
    return addto(a,b,c)

def polymul(a,b):
    out={}
    for (i,j),c in a.items():
        for (k,l),d in b.items():
            w=(i+k,j+l);out[w]=out.get(w,Q(0))+c*d
    return {w:c for w,c in out.items() if c}

def determinant(matrix):
    n=len(matrix);dp={0:{(0,0):Q(1)}}
    for mask in range(1<<n):
        if mask not in dp: continue
        row=bin(mask).count('1')
        if row==n: continue
        for col in range(n):
            if mask>>col&1:continue
            sign=(-1)**(bin(mask>>(col+1)).count('1'))
            new=mask|1<<col
            dp[new]=polyadd(dp.get(new,{}),polymul(dp[mask],matrix[row][col]),sign)
    return dp[(1<<n)-1]

def selected_rows(matrix,order):
    pivots={};chosen=[]
    for index in order:
        row={j:sum(c[i]*Q([1,4,4][i]) for i in range(3)) for j,c in enumerate(matrix[index])}
        row={j:c for j,c in row.items() if c}
        while row:
            p=min(row)
            if p not in pivots:
                c=row[p];pivots[p]={j:x/c for j,x in row.items()};chosen.append(index);break
            row=addto(row,pivots[p],-row[p])
        if len(chosen)==len(matrix[0]):return chosen
    raise AssertionError('Diagonal specialization failed rank')

def encode(p):return [[list(w),str(c)] for w,c in sorted(p.items())]

def main():
    records=[]
    for a,b,pdim,ldim,tdim in CELLS:
        candidates=words(a,b,4)
        raw=[old.evaluate_and_lower(tree(w))[0] for w in candidates]
        basis=span(raw);assert len(basis)==ldim
        target_basis=span([old.evaluate_and_lower(tree(w))[0] for w in words(a,b,3)])
        assert len(target_basis)==tdim
        acts=[[action(actor,v) for v in basis] for actor in (3,4)]
        keys=[(k,w) for k in range(2) for w in sorted(set().union(*(set(v) for v in acts[k])))]
        kernels=nullspace([[acts[k][j].get(w,Q(0)) for j in range(ldim)] for k,w in keys],ldim)
        assert len(kernels)==pdim
        primitive=[]
        for coeffs in kernels:
            v={}
            for c,p in zip(coeffs,basis):v=addto(v,p,c)
            assert not action(3,v) and not action(4,v)
            primitive.append(v)
        # Each Lie vector is 1/4 its independently recognizable Dynkin expansion.
        images=[]
        for p in primitive:
            image={}
            for w,c in p.items():
                image=old.affine_poly_add(image,old.affine_poly_scale(c/4,
                    old.evaluate_and_lower(tree(w))[1]))
            images.append(image)
        outwords=sorted(set().union(*(set(v) for v in images)))
        matrix=[[v.get(w,old.ZERO) for v in images] for w in outwords]
        certificate=None
        rng=random.Random(20261014+a*10+b)
        for attempt in range(12):
            assert time.monotonic()<DEADLINE
            order=list(range(len(outwords)))
            if attempt==1:order.reverse()
            elif attempt>1:rng.shuffle(order)
            chosen=selected_rows(matrix,order)
            polmatrix=[]
            for i in chosen:
                row=[]
                for c,r,s in matrix[i]:
                    row.append({w:v for w,v in [((0,0),c+4*r+4*s),((1,0),r),((0,1),s)] if v})
                polmatrix.append(row)
            det=determinant(polmatrix)
            constant=det.get((0,0),Q(0))
            if constant and all(c*constant>0 for c in det.values()):
                certificate={'rows':[list(outwords[i]) for i in chosen],
                  'det_shift_4':encode(det),'orientation':1 if constant>0 else -1,
                  'attempt':attempt};break
        assert certificate is not None,('No positive minor',a,b)
        records.append({'degree':[a,b,4],'primitive_dimension':pdim,'free_dimension':ldim,
          'target_dimension':tdim,'primitive_basis':[encode(p) for p in primitive],
          'lowering_images':[[[list(w),[str(x) for x in c]] for w,c in sorted(p.items())] for p in images],
          'minor':certificate})
        print('Certified',a,b,'Pdim',pdim,'attempt',certificate['attempt'],flush=True)
    root=Path(__file__).resolve().parent
    payload={'scope':'Four remaining primitive cells; original D3; r,s>=4',
      'full_goal_solved':False,'records':records,
      'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (root/'level4-cells-certificate.json').write_text(json.dumps(payload,indent=2)+'\n')

if __name__=='__main__':main()
