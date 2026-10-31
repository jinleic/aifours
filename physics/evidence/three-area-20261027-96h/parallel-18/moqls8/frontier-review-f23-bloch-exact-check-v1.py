#!/usr/bin/env python3
"""Independent exact Bloch-gap checks; no author code or floating point."""
import argparse
import hashlib
import importlib.util
import json
import math
import pathlib
from fractions import Fraction as Q

BASE = pathlib.Path(__file__).with_name('frontier-review-f5-depol-exact-check-v1.py')
EXPECTED = '5de969371efd72585a6ffddf39c26ebb78e6f2252e7d652394eb3c9c730f720e'
if hashlib.sha256(BASE.read_bytes()).hexdigest() != EXPECTED:
    raise ValueError('independent matrix primitives SHA mismatch')
spec = importlib.util.spec_from_file_location('f5_own_primitives', BASE)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def outer(vec):
    return [[M.mul(vec[i], M.conj(vec[j])) for j in range(16)] for i in range(16)]


def ghz_asymmetric():
    vec = [M.ZERO for _ in range(16)]
    vec[0] = (Q(3,5), Q(0))
    vec[15] = (Q(0), Q(4,5))
    return outer(vec)


def two_pairs():
    vec = [M.ZERO for _ in range(16)]
    vec[0] = (Q(15,65), Q(0))
    vec[3] = (Q(0), Q(20,65))
    vec[12] = (Q(0), Q(36,65))
    vec[15] = (Q(-48,65), Q(0))
    return outer(vec)


def root_fraction(z):
    if z < 0:
        raise ValueError('negative radicand')
    n, d = math.isqrt(z.numerator), math.isqrt(z.denominator)
    if n*n != z.numerator or d*d != z.denominator:
        raise ValueError('chosen sample has irrational local radius')
    return Q(n,d)


def local_radii(state):
    radii = []
    for bit_index in range(4):
        bit = 1 << bit_index
        reduced = [[M.ZERO for _ in range(2)] for _ in range(2)]
        for x in range(16):
            if x & bit:
                continue
            for a in range(2):
                for b in range(2):
                    reduced[a][b] = M.add(reduced[a][b], state[x | (a*bit)][x | (b*bit)])
        a, b, z = reduced[0][0], reduced[1][1], reduced[0][1]
        if a[1] or b[1] or a[0]+b[0] != 1:
            raise ValueError('invalid local density')
        radii.append(root_fraction((a[0]-b[0])**2 + 4*(z[0]**2+z[1]**2)))
    return radii


def padd(A,B):
    C = dict(A)
    for key,value in B.items():
        C[key] = C.get(key,Q(0)) + value
        if not C[key]:
            del C[key]
    return C


def pscale(A,c):
    return {k:v*c for k,v in A.items() if v*c}


def pmul(A,B):
    C = {}
    for (a,b,c),v in A.items():
        for (d,e,f),w in B.items():
            key=(a+d,b+e,c+f)
            C[key]=C.get(key,Q(0))+v*w
    return {k:v for k,v in C.items() if v}


def product(*args):
    out={(0,0,0):Q(1)}
    for arg in args:
        out=pmul(out,arg)
    return out


def symbolic_identities():
    one={(0,0,0):Q(1)}
    p={(1,0,0):Q(1)}
    R={(0,1,0):Q(1)}
    x={(0,0,1):Q(1)}
    q=padd(one,pscale(p,-1))
    p2=product(p,p)
    q2=product(q,q)
    q3=product(q2,q)
    q4=product(q3,q)
    left=product(q4,padd(one,pscale(x,-1)))
    left=padd(left,pscale(product(R,p,q3),Q(-1,4)))
    coefficient=padd(padd(pscale(one,Q(1,2)),pscale(x,Q(1,4))),pscale(R,Q(-1,2)))
    left=padd(left,product(coefficient,p2,q2))
    coefficient2=padd(pscale(one,Q(1,2)),pscale(R,Q(-3,16)))
    left=padd(left,product(coefficient2,p2,p,q))
    base=pscale(product(p,q,padd(pscale(p,8),pscale(product(R,padd(pscale(one,4),pscale(p2,-1))),-1))),Q(1,16))
    right=padd(base,product(q4,padd(one,pscale(x,-1))))
    right=padd(right,pscale(product(p2,q2,x),Q(1,4)))
    if left != right:
        raise ValueError('full three-variable polynomial identity failed')
    low=padd(base,pscale(product(p2,q2),Q(1,4)))
    threshold=pscale(product(p,q,padd(pscale(product(p,padd(pscale(one,3),pscale(p,-1))),4),
                                             pscale(product(R,padd(pscale(one,4),pscale(p2,-1))),-1))),Q(1,16))
    if low != threshold:
        raise ValueError('low-s threshold identity failed')
    diff=padd(q4,pscale(product(p2,q2),Q(-1,4)))
    factored=product(q2,padd(q,pscale(p,Q(-1,2))),padd(q,pscale(p,Q(1,2))))
    if diff != factored:
        raise ValueError('min-branch crossover factorization failed')
    return {'full_p_R_x_identity': True, 'low_threshold_polynomial_identity': True,
            'min_branch_crossover_factorization': True}


def run_sample(name,state,P,R_override=None):
    if not M.hermitian(state) or M.trace(state) != M.ONE:
        raise ValueError('state not Hermitian trace one')
    R = sum(local_radii(state)) if R_override is None else R_override
    x=M.trace_product(P,state)
    y=M.trace_product(P,M.spinflip(state))
    Ts=M.layers(state)
    t=[M.trace_product(P,T) for T in Ts]
    if not (0<=x<=1 and 0<=y<=1 and t[1]<=3+R/4 and t[3]<=(12+3*R)/16 and
            t[2]<=(10-x+2*R)/4):
        raise ValueError('Bloch-layer inequality failed')
    vals=[]
    for p in (Q(0),Q(1,3),Q(1,2),Q(2,3),Q(1),Q(7,6),Q(4,3)):
        s=min(p,2-p);q=1-s
        a,b=1-s/2,s/2
        reference=a**4+2*a**3*b
        actual=M.trace_product(P,M.apply_channel(state,p))
        basic=s*q*(8*s-R*(4-s*s))/16
        extra=min(q**4,s*s*q*q/4)
        if actual>reference-basic-extra:
            raise ValueError('sharpened Bloch bound failed')
        vals.append({'p':str(p),'actual':str(actual),'reference':str(reference),
                     'basic_bound':str(basic),'added_min':str(extra),
                     'remaining_slack':str(reference-actual-basic-extra)})
    return {'state':name,'R_or_pure_component_cap':str(R),'x':str(x),'spinflip_overlap':str(y),
            'layers':[str(v) for v in t],'parameters':vals}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    P=M.rank_three_complex_projector()
    if not M.hermitian(P) or M.matrix_mul(P,P)!=P or M.trace(P)!=(Q(3),Q(0)):
        raise ValueError('complex projector invalid')
    pure=[('asymmetric_complex_GHZ',ghz_asymmetric()),('two_complex_entangled_pairs',two_pairs())]
    samples=[]
    for name,state in pure:
        if M.matrix_mul(state,state)!=state or M.trace(state)!=M.ONE:
            raise ValueError('sample not a pure density')
        samples.append(run_sample(name,state,P))
    one_uniform=M.graph_state()
    if M.matrix_mul(one_uniform,one_uniform)!=one_uniform or M.trace(one_uniform)!=M.ONE or any(local_radii(one_uniform)):
        raise ValueError('mixture one-uniform component invalid')
    mixture=M.matrix_add(M.matrix_scale(one_uniform,Q(1,3)),M.matrix_scale(pure[0][1],Q(2,3)))
    cap=sum(local_radii(pure[0][1]))
    samples.append(run_sample('convex_mixture_R0_is_component_cap_not_mixed_radius',mixture,P,R_override=cap))
    report={'result':'PASS_EXACT_BLOCH_GAP_SAMPLES_NOT_UNIVERSAL_PROOF',
            'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            'independent_matrix_primitives_sha256':EXPECTED,'symbolic':symbolic_identities(),
            'complex_projector_hermitian_idempotent_trace3':True,'physical_samples':samples,
            'arithmetic':'fractions.Fraction complex matrix pairs and sparse polynomial dictionaries',
            'scope':'Two pure samples, one specified convex mixture, one actual P, seven p values; no universal proof.'}
    with pathlib.Path(args.output).open('x',encoding='utf-8') as handle:
        json.dump(report,handle,indent=2);handle.write('\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
