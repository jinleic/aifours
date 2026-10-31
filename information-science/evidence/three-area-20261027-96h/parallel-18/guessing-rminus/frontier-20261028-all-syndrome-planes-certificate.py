#!/usr/bin/env python3
"""Construct a linear confusability-clique witness for every binary syndrome plane.

The overwhelming common-vertex cases follow a K4-free construction. The
remaining planes receive explicit two-generator coefficient certificates.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-all-syndrome-planes-certificate-result.json'
QS=ROOT/'frontier-20261028-multicoset-quotient-search.py'


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triangles=[tuple(x) for x in json.loads(raw)['chosen_triangles']]
    spec=spec_from_file_location('quotientsearch',QS);qs=module_from_spec(spec);spec.loader.exec_module(qs)
    stars,reps,kernels=qs.precompute(triangles)
    spans={v:qs.span(kernels[v]) for v in range(1,11)};cache={}
    def bad(s):
        if s not in cache:
            out=set()
            for v in range(1,11):
                if not s&stars[v]:continue
                r=0
                for j in range(10):
                    if s>>j&1:r ^= reps[v][j]
                out.update(r^k for k in spans[v])
            cache[s]=out
        return cache[s]
    common=0;special=[];planes=0
    for a in range(1,1024):
        for b in range(a+1,1024):
            if (a^b)<b:continue
            planes+=1
            if any((a&stars[v]) and (b&stars[v]) and (a&stars[v])!=(b&stars[v]) for v in range(1,11)):
                common+=1;continue
            B=bad(a^b);w=next(((x,y) for x in sorted(bad(a)) for y in sorted(bad(b)) if (x^y) in B),None)
            if w is None:raise ValueError(('NO_LINEAR_TRANSVERSAL',a,b))
            special.append({'syndrome_a':a,'syndrome_b':b,'code_coeff_a':w[0],'code_coeff_b':w[1]})
    if planes!=174251 or common+len(special)!=planes:raise ValueError('PLANE_CENSUS')
    out={'baseline_result_sha256':EXPECTED,'producer_dependency_sha256':sha256(QS.read_bytes()).hexdigest(),
         'plane_count':planes,'common_isolated_vertex_planes':common,
         'separately_certified_planes':len(special),'special_witnesses':special,
         'coefficient_encoding':'bits 2t and 2t+1 are triangle t first and second component; third is syndrome_t XOR both',
         'limits':'Exact binary q=8 graph construction only; no arbitrary-alphabet upper bound or nonlinear entropy-ratio upper follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='special_witnesses'},indent=2))


if __name__=='__main__':main()
