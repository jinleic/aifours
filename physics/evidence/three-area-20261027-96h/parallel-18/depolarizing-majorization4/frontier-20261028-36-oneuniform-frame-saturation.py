#!/usr/bin/env python3
"""Exact entangled saturation and same-projector incompatibility in Pauli frame."""

import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("simple_frame", ROOT / "frontier-20261028-33-simple-frame-witness.py")
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)
d, b, e = sc.d, sc.b, sc.e


def main():
    v = [F(0)] * 16
    for i, value in ((0,2),(5,1),(6,1),(9,1),(10,1),(15,2)):
        v[i] = F(value)
    rho = [[e.z(v[i]*v[j]/12) for j in range(16)] for i in range(16)]
    assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
    cuts = []
    for size in (1,2):
        for active in itertools.combinations(range(4), size):
            if size == 2 and 0 not in active:
                continue
            rest = tuple(i for i in range(4) if i not in active)
            matrix = [[F(0) for _ in range(2**len(rest))] for _ in range(2**len(active))]
            for index in range(16):
                bits = [(index >> (3-i)) & 1 for i in range(4)]
                row = sum(bits[i]*2**(len(active)-1-j) for j,i in enumerate(active))
                col = sum(bits[i]*2**(len(rest)-1-j) for j,i in enumerate(rest))
                matrix[row][col] = v[index]
            rank = sc.rectangular_rank(matrix)
            assert rank >= 2
            cuts.append({"parties_zero_based":list(active),"rank":rank})
    for site in range(4):
        assert e.local_marginal(rho,site)==[[e.z(F(1,2)),e.ZERO],[e.ZERO,e.z(F(1,2))]]
    frame=d.local_pauli_frame(rho)
    spectrum={F(8,3):3,F(2,3):6,F(0):7}
    eig=d.verify_spectrum(frame,spectrum)
    assert sum(eig[:3])==8
    vectors=[[F(0)]*16 for _ in range(3)]
    vectors[0][0],vectors[0][15]=1,-1
    for i in (1,2,7,11): vectors[1][i]=1
    for i in (4,8,13,14): vectors[2][i]=1
    projections=[]
    for vector,norm in zip(vectors,(2,4,4)):
        assert sum(x*x for x in vector)==norm
        projections.append([[e.z(F(vector[i]*vector[j],norm)) for j in range(16)] for i in range(16)])
    PF=e.zero(16)
    for Q in projections: PF=e.add_matrix(PF,Q)
    assert PF==e.adjoint(PF) and e.matmul(PF,PF)==PF and e.trace(PF)==e.z(3)
    assert e.trace(e.matmul(PF,frame))==e.z(8)
    assert e.matmul(PF,rho)==e.zero(16)
    assert e.matmul(frame,PF)==e.scale_matrix(PF,F(8,3))
    t1=e.zero(16)
    for site in range(4): t1=e.add_matrix(t1,e.one_erasure(rho,site))
    assert t1==e.add_matrix(rho,e.scale_matrix(frame,F(1,4)))
    t1_spectrum={F(1):1,F(2,3):3,F(1,6):6,F(0):6}
    t1_eig=d.verify_spectrum(t1,t1_spectrum)
    assert sum(t1_eig[:3])==F(7,3)
    assert e.trace(e.matmul(PF,t1))==e.z(2)
    Pchan=e.add_matrix(e.add_matrix(rho,projections[0]),projections[1])
    assert Pchan==e.adjoint(Pchan) and e.matmul(Pchan,Pchan)==Pchan and e.trace(Pchan)==e.z(3)
    assert e.trace(e.matmul(Pchan,t1))==e.z(F(7,3))
    originals=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p)
        assert out==b.direct_pauli(rho,p)
        expected={F(1,9):1,F(20,243):3,F(14,243):6,F(4,81):6}
        oeig=d.verify_spectrum(out,expected)
        assert all(x>=0 for x in oeig) and sum(oeig[:3])==F(67,243)
        assert e.trace(e.matmul(Pchan,out))==e.z(F(67,243))
        assert e.trace(e.matmul(PF,out))==e.z(F(20,81))
        originals.append({"p":str(p),"full_original_spectrum":[[str(x),m] for x,m in expected.items()],"original_top3":"67/243","same_Pchan_original_trace":"67/243","frame_maximizer_PF_original_trace":"20/81","product_reference_top3":"32/81","exact_gap":"29/243"})
    print(json.dumps({"scope":"exact physical equality in auxiliary F k3 and same-projector non-saturation; not a global inequality proof or original violation","state":"(2|0000>+|0101>+|0110>+|1001>+|1010>+2|1111>)/sqrt(12)","schmidt_cut_ranks":cuts,"all_local_marginals":"I/2","frame_spectrum":[[str(x),m] for x,m in spectrum.items()],"frame_top3":"8","frame_maximizer_overlap_with_input":"0","t1_max_exact":"7/3","t1_at_frame_maximizer":"2","t1_at_Pchan":"7/3","original_channel_checks":originals},indent=2,sort_keys=True))


if __name__=="__main__":
    main()
