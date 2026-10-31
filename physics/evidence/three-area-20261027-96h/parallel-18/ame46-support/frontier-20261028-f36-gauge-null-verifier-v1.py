#!/usr/bin/env python3
"""Independently assemble gauge rows and verify rational null vectors exactly."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


def read_sparse(path,expected_rows):
    raw=path.read_bytes();lines=raw.decode('utf-8').splitlines()
    header=tuple(map(int,lines[0].split()))
    if header!=(expected_rows,1000) or len(lines)!=expected_rows+1:raise ValueError('sparse header/row mismatch')
    rows=[]
    for line in lines[1:]:
        values=list(map(int,line.split()));count=values[0]
        if len(values)!=1+2*count:raise ValueError('sparse row length mismatch')
        row={}
        for j in range(count):
            col,val=values[1+2*j:3+2*j]
            if col in row or not 0<=col<1000 or not val:raise ValueError('invalid sparse entry')
            row[col]=val
        rows.append(row)
    return rows,hashlib.sha256(raw).hexdigest()


def load_vectors(path,count):
    raw=path.read_bytes();obj=json.loads(raw);items=obj['vectors']
    if len(items)!=count:raise ValueError('null vector count mismatch')
    result=[]
    for item in items:
        v={}
        for col,num,den in item['entries']:
            if col in v or not 0<=col<1000 or not den:raise ValueError('invalid null-vector entry')
            v[col]=Fraction(num,den)
        result.append((item['free_column'],v))
    return result,hashlib.sha256(raw).hexdigest()


def check_null(rows,vectors):
    for free,v in vectors:
        if v.get(free)!=1:raise ValueError('free coordinate not normalized')
        for i,row in enumerate(rows):
            if sum((Fraction(c)*v.get(j,Fraction()) for j,c in row.items()),Fraction()):
                raise ValueError(f'null-vector failure row={i} free={free}')
    frees=[free for free,v in vectors]
    for i,(_,v) in enumerate(vectors):
        if any(v.get(f,Fraction())!=(1 if i==j else 0) for j,f in enumerate(frees)):
            raise ValueError('free-coordinate identity failure')


def write_sparse(path,rows):
    with path.open('x',encoding='utf-8') as out:
        out.write(f'{len(rows)} 1000\n')
        for row in rows:
            entries=sorted(row.items())
            out.write(str(len(entries))+''.join(f' {j} {c}' for j,c in entries)+'\n')


def main():
    p=argparse.ArgumentParser()
    for name in ('witness','real','imag','null_real','null_imag','out_real','out_imag','receipt'):
        p.add_argument(name,type=Path)
    a=p.parse_args()
    raw=a.witness.read_bytes();w=json.loads(raw)['partial_witness'];arr=w['array']
    vectors=[arr[r][c] for r in range(10) for c in range(10)]
    if w['denominator']!=3 or vectors[77]!=[0,0,0,0,0,0,0,1,-2,-2]:
        raise ValueError('unexpected anchor or denominator')
    real,real_sha=read_sparse(a.real,1450);imag,imag_sha=read_sparse(a.imag,1350)
    for j in range(100):
        real.append({j:1});imag.append({j:1})
    for cell in range(10,100):
        imag.append({10*cell+j:c for j,c in enumerate(vectors[cell]) if c})
    imag.extend(({777:1},{778:1}))
    if len(real)!=1550 or len(imag)!=1542:raise ValueError('gauge row count mismatch')
    rv,rvsha=load_vectors(a.null_real,3);iv,ivsha=load_vectors(a.null_imag,1)
    check_null(real,rv);check_null(imag,iv)
    write_sparse(a.out_real,real);write_sparse(a.out_imag,imag)
    result={'witness_sha256':hashlib.sha256(raw).hexdigest(),'input_real_sha256':real_sha,'input_imag_sha256':imag_sha,
            'null_real_sha256':rvsha,'null_imag_sha256':ivsha,
            'gauge_rows_real':len(real),'gauge_rows_imaginary':len(imag),
            'rational_vectors_checked_all_rows':{'real':len(rv),'imaginary':len(iv)},
            'free_coordinates_real':[f for f,v in rv],'free_coordinates_imaginary':[f for f,v in iv],
            'independence':'free-coordinate identity verified over Q',
            'scope':'Gauge assembly and exact null vectors; modular-rank upper bound checked separately.'}
    with a.receipt.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
