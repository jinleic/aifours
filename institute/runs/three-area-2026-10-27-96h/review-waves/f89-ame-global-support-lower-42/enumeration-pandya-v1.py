#!/usr/bin/env python3
# Independent exact 2-unitarity check of the pinned public-table transcription.
import hashlib, itertools, json, re, subprocess
from pathlib import Path

src=Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt')
b=src.read_bytes()
if hashlib.sha256(b).hexdigest()!='cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38':
    raise ValueError('input hash mismatch')
seen=set(); F={}
for line in b.decode('utf-8').splitlines():
    if not line or line.startswith('#'): continue
    parts=line.split()
    if len(parts) not in (3,4) or not all(x in '012345' and len(x)==1 for x in parts[:2]):
        raise ValueError('invalid row syntax')
    a,bv=map(int,parts[:2])
    if (a,bv) in seen: raise ValueError('duplicate table cell')
    seen.add((a,bv))
    for token in parts[2:]:
        match=re.fullmatch(r'([+\-s])([0-5])([0-5])',token)
        if not match: raise ValueError('invalid entry syntax')
        op,c,d=match.groups(); point=(a,bv,int(c),int(d))
        if point in F: raise ValueError('duplicate tensor position')
        F[point]=(0,1) if op=='s' else ((1,0) if op=='+' else (-1,0))
if seen!=set(itertools.product(range(6),repeat=2)) or len(F)!=60:
    raise ValueError('incomplete table')

def gram(M):
    G=[]
    for i in range(36):
        row=[]
        for j in range(36):
            a=b=0
            for k in range(36):
                x,y=M[i][k]; z,w=M[j][k]
                a+=x*z+2*y*w; b+=x*w+y*z
            row.append((a,b))
        G.append(row)
    return G

results=[]
for row_axes,col_axes in (((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))):
    M=[[(0,0) for j in range(36)] for i in range(36)]
    for point,value in F.items():
        r=6*point[row_axes[0]]+point[row_axes[1]]
        c=6*point[col_axes[0]]+point[col_axes[1]]
        M[r][c]=value
    target=[[(2 if i==j else 0,0) for j in range(36)] for i in range(36)]
    rowGram=gram(M)
    colGram=gram(list(map(list,zip(*M))))
    if rowGram!=target or colGram!=target: raise ValueError('failed exact 2-unitarity')
    results.append({'row_axes':row_axes,'column_axes':col_axes,'rows_and_columns':'exact 2I',
                    'singleton_rows':sum(sum(v!=(0,0) for v in row)==1 for row in M),
                    'two_entry_rows':sum(sum(v!=(0,0) for v in row)==2 for row in M)})
result={'table_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'support':len(F),'maximal_entries':sum(v==(0,1) for v in F.values()),
        'other_entries':sum(v!=(0,1) for v in F.values()),'cuts':results,
        'meaning':'Transcribed tensor is divided by sqrt(72); 6 times each flattening is matrix / sqrt(2).',
        'clock_before_write':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()}
out=Path(__file__).with_name('enumeration-pandya-v1.json')
with out.open('x',encoding='utf-8') as f: json.dump(result,f,indent=2); f.write(chr(10))
print('receipt',out,'sha256',hashlib.sha256(out.read_bytes()).hexdigest(),'code_sha256',result['code_sha256'])
