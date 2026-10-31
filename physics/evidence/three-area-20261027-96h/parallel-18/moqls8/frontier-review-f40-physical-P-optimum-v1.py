#!/usr/bin/env python3
"""Exact physical rank-3 projector attaining the improved spin-flip subproblem."""
import argparse
import hashlib
import importlib.util
import json
import math
import pathlib
from fractions import Fraction as Q

HERE=pathlib.Path(__file__).parent
PINS={'M':('frontier-review-f5-depol-exact-check-v1.py','5de969371efd72585a6ffddf39c26ebb78e6f2252e7d652394eb3c9c730f720e'),
      'F':('frontier-review-f23-bloch-exact-check-v1.py','b6cfee53d2e89493fd430181f6601e42d5074e66cecacfbd12ec6a6b492bf05a')}
mods={}
for name,(filename,pin) in PINS.items():
 path=HERE/filename
 if hashlib.sha256(path.read_bytes()).hexdigest()!=pin:raise ValueError('own primitive pin mismatch')
 spec=importlib.util.spec_from_file_location('own_'+name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);mods[name]=mod
M,F=mods['M'],mods['F']


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 rho=F.ghz_asymmetric();tilde=M.spinflip(rho)
 if not M.hermitian(rho) or M.trace(rho)!=M.ONE or M.matrix_mul(rho,rho)!=rho:
  raise ValueError('input not exact pure density')
 c2=M.trace_product(rho,tilde);d=F.root_fraction(1-c2)
 s=Q(25,32);q=1-s;A=q**4;B=s*s*q*q/4
 if not (A<B and 0<d<1):raise ValueError('sample not strict-branch case')
 disc=A*A+4*B*(B-A)*d*d
 root=F.root_fraction(disc)
 lam_minus=(A-root)/2
 H=M.matrix_add(M.matrix_scale(rho,A-B),M.matrix_scale(tilde,B))
 span=M.empty();span[0][0]=M.ONE;span[15][15]=M.ONE
 Ppos=M.matrix_scale(M.matrix_add(H,M.matrix_scale(span,-lam_minus)),1/root)
 P=M.matrix_add(Ppos,M.empty());P[1][1]=M.ONE;P[2][2]=M.ONE
 if not M.hermitian(P) or M.matrix_mul(P,P)!=P or M.trace(P)!=(Q(3),Q(0)):
  raise ValueError('physical optimizing projector invalid')
 x=M.trace_product(P,rho);y=M.trace_product(P,tilde)
 physical=A*(1-x)+B*(1-y+x)
 sharp=B+(A-root)/2
 relaxed=B-d*(B-A)
 if physical!=sharp or not (sharp>relaxed):raise ValueError('exact physical optimization or strict improvement failed')
 identity=(A+2*d*(B-A))**2-disc
 if identity!=4*A*(B-A)*d*(1-d):raise ValueError('improvement comparison identity failed')
 R=sum(F.local_radii(rho));rs=sorted(F.local_radii(rho));L=rs[0]+rs[1]+3*rs[2]+3*rs[3]
 base=s*q*(8*s-(2-s)*(2*q*R+s*L))/16
 ref=(1-s/2)**4+2*(1-s/2)**3*(s/2)
 actual=M.trace_product(P,M.apply_channel(rho,s))
 if actual>ref-base-sharp:raise ValueError('new actual-channel lower bound failed')
 def gauss(z):return [str(z[0]),str(z[1])]
 report={'result':'PASS_EXACT_INTERMEDIATE_C_PHYSICAL_PROJECTOR_OPTIMUM',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'own_primitives':{n:p for n,(_,p) in PINS.items()},
         'state':'(3|0000>+4i|1111>)/5','s':str(s),'c_squared':str(c2),'d':str(d),
         'A':str(A),'B':str(B),'discriminant':str(disc),'sqrt_discriminant':str(root),
         'projector_rank3_idempotent_hermitian':True,
         'projector_nonzero_block_0_15':[[gauss(P[i][j]) for j in (0,15)] for i in (0,15)],
         'additional_projector_diagonal_indices':[1,2],
         'x':str(x),'y':str(y),'physical_subproblem_value':str(physical),
         'exact_new_bonus':str(sharp),'author_relaxed_bonus':str(relaxed),
         'strict_improvement':str(sharp-relaxed),
         'actual_channel_trace':str(actual),'reference':str(ref),
         'new_total_bound':str(base+sharp),'actual_slack':str(ref-actual-base-sharp),
         'arithmetic':'standard-library Fraction pairs, exact Gaussian rational matrix operations',
         'limits':'One exact physical state/projector/parameter; not universal computer proof or global solution.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))

if __name__=='__main__':main()
