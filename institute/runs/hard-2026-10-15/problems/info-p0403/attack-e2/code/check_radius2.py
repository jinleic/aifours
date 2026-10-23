"""Independent full enumeration using direct character sums and NumPy.

No imports from producing code. Reconstructs the seed tables directly
from staged literature, constructs a character matrix using binary
parity, then checks all 130816 two-flip transforms per seed. This checks
every coefficient of every candidate, not a sample.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import numpy as np


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("path",nargs="?",default="results/radius2.json")
    args=parser.parse_args()
    data=json.loads(Path(args.path).read_text())
    source=Path("selection-inputs/literature/kavut-yucel.reader.md").read_text().split("#### 3.2")[0]
    tables=re.findall(r"(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$",source)
    assert len(tables)==3
    names=("dsbf40","dsbf32","rsbf56")
    # Direct characters; row a, column x.
    H=np.array([[1 if format(a&x,"b").count("1")%2==0 else -1 for x in range(512)] for a in range(512)],dtype=np.int32)
    for name,(part1,part2) in zip(names,tables):
        hx=part1+part2
        chars=''.join(format(int(ch,16),'04b') for ch in hx)
        bits=np.fromiter(map(int,chars),dtype=np.int32)
        signs=1-2*bits
        W=np.array([sum(int(signs[x])*int(H[a,x]) for x in range(512)) for a in range(512)],dtype=np.int32)
        rec=data["seeds"][name]
        assert rec["hex"]==hx
        assert rec["sha256_ascii_bits"]==hashlib.sha256(chars.encode()).hexdigest()
        assert rec["walsh"]==W.tolist()
        assert rec["weight"]==int(bits.sum())
        assert rec["W0"]==int(W[0])
        assert rec["original_minimum_balancing_distance"]==abs(int(W[0]))//2
        assert rec["minimum_over_linear_shifts"]==min(abs(int(w)) for w in W)//2
        assert rec["zero_count"]==0==int(np.count_nonzero(W==0))
        assert rec["max_abs_walsh"]==28==max(abs(int(w)) for w in W)
        assert rec["absolute_spectrum_histogram"]=={str(k):v for k,v in sorted(Counter(abs(int(w)) for w in W).items())}
        assert rec["linear_shift_indices_with_minimum_distance_2"]==np.flatnonzero(abs(W)==4).tolist()
        legal=[]
        balanced=[]
        columns=(H*signs).T.copy()
        count=0
        for x in range(511):
            # Every coefficient of every pair with this smaller endpoint.
            candidates=W[None,:]-2*columns[x,None,:]-2*columns[x+1:,:]
            valid=np.flatnonzero(np.max(abs(candidates),axis=1)<=28)
            for j in valid.tolist():
                y=x+1+j
                legal.append([x,y])
                zeros=np.flatnonzero(candidates[j]==0).tolist()
                if zeros:
                    balanced.append({"flips":[x,y],"zero_indices":zeros})
            count+=511-x
        assert count==rec["pairs_examined"]==130816
        assert legal==rec["pairs_preserving_bound"]
        assert balanced==rec["pairs_preserving_bound_and_giving_a_zero"]==[]
        print(name,"PASS direct sums; exhaustive pairs",count,"bound-preserving",len(legal),"balanced",len(balanced))
    assert data["radius"]==2 and data["bound"]==28
    print("PASS independent radius-two audit")


if __name__=="__main__":
    main()
