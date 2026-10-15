#!/usr/bin/env python3
"""Exact matrix data for the conditional finite-height-to-band lemma.

This verifies B^{-1}>=0 and the constants; it does not by itself certify the
assumed lower-height Serre equality. That acceptance is recorded separately.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path


def inverse(matrix):
    n=len(matrix)
    rows=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for column in range(n):
        pivot=next((i for i in range(column,n) if rows[i][column]),None)
        if pivot is None:
            return None
        rows[column],rows[pivot]=rows[pivot],rows[column]
        lead=rows[column][column]
        rows[column]=[x/lead for x in rows[column]]
        for i in range(n):
            if i!=column:
                factor=rows[i][column]
                rows[i]=[x-factor*y for x,y in zip(rows[i],rows[column])]
    return [row[n:] for row in rows]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--matrix',required=True)
    parser.add_argument('--height',type=int,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    matrix=json.loads(Path('work/matrices.json').read_text())['matrices'][args.matrix]
    results=[]
    for omitted in range(3):
        indices=[j for j in range(3) if j!=omitted]
        block=[[matrix[i][j] for j in indices] for i in indices]
        inv=inverse(block)
        if inv is None or any(x<0 for row in inv for x in row):
            results.append({'index':omitted+1,'applicable':False,'reason':'inverse-nonnegative hypothesis fails'})
            continue
        assert all(sum(Q(block[i][k])*inv[k][j] for k in range(2))==int(i==j) for i in range(2) for j in range(2))
        bounds=[-sum(inv[i][j]*matrix[indices[j]][omitted] for j in range(2)) for i in range(2)]
        constant=1+sum(bounds)
        threshold=Q(args.height+1)/constant
        largest=(threshold.numerator+threshold.denominator-1)//threshold.denominator-1
        assert math.floor(constant*largest)<=args.height and math.floor(constant*(largest+1))>args.height
        results.append({'index':omitted+1,'complement_indices':[j+1 for j in indices],
                        'applicable':True,'block':block,'inverse':[[str(x) for x in row] for row in inv],
                        'coordinate_bounds':[str(x) for x in bounds],'height_ratio':str(constant),
                        'certifiable_band_coefficient':largest,
                        'floor_height_at_band':math.floor(constant*largest)})
    result={'matrix_name':args.matrix,'matrix':matrix,'assumed_verified_height':args.height,
            'claim':'Conditional on equality through the stated height, all positive degrees in each listed coefficient band have equality.',
            'indices':results,'arithmetic':'exact fractions.Fraction',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
