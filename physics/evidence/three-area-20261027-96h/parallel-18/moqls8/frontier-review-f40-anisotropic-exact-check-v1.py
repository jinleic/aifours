#!/usr/bin/env python3
"""Independent exact tests of anisotropic/spin-flip bounds; not a proof."""
import argparse
import hashlib
import importlib.util
import json
import pathlib
from fractions import Fraction as Q

HERE=pathlib.Path(__file__).parent
FILES={
 'base':('frontier-review-f5-depol-exact-check-v1.py','5de969371efd72585a6ffddf39c26ebb78e6f2252e7d652394eb3c9c730f720e'),
 'radii':('frontier-review-f23-bloch-exact-check-v1.py','b6cfee53d2e89493fd430181f6601e42d5074e66cecacfbd12ec6a6b492bf05a')}
modules={}
for name,(file,pin) in FILES.items():
 path=HERE/file
 if hashlib.sha256(path.read_bytes()).hexdigest()!=pin:raise ValueError('own independent primitive pin mismatch')
 spec=importlib.util.spec_from_file_location('own_'+name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);modules[name]=mod
M,F=modules['base'],modules['radii']


def w_state():
 v=[M.ZERO for _ in range(16)]
 for i in (1,2,4,8):v[i]=(Q(1,2),Q(0))
 return F.outer(v)


def product_state():
 v=[M.ZERO for _ in range(16)];v[0]=M.ONE;return F.outer(v)


def add(A,B):
 out=dict(A)
 for key,value in B.items():
  out[key]=out.get(key,Q(0))+value
  if out[key]==0:del out[key]
 return out


def scale(A,c):return {k:v*c for k,v in A.items() if v*c}


def mul(*polys):
 out={(0,0,0,0):Q(1)}
 for poly in polys:
  next_={}
  for key,val in out.items():
   for key2,val2 in poly.items():
    k=tuple(a+b for a,b in zip(key,key2));next_[k]=next_.get(k,Q(0))+val*val2
  out={k:v for k,v in next_.items() if v}
 return out


def symbolic():
 one={(0,0,0,0):Q(1)};p={(1,0,0,0):Q(1)};R={(0,1,0,0):Q(1)};L={(0,0,1,0):Q(1)};x={(0,0,0,1):Q(1)}
 q=add(one,scale(p,-1));q2=mul(q,q);q3=mul(q2,q);q4=mul(q3,q);p2=mul(p,p)
 left=mul(q4,add(one,scale(x,-1)))
 left=add(left,scale(mul(R,p,q3),Q(-1,4)))
 left=add(left,mul(add(add(scale(one,Q(1,2)),scale(x,Q(1,4))),scale(add(R,L),Q(-1,8))),p2,q2))
 left=add(left,scale(mul(add(scale(one,8),scale(L,-1)),p2,p,q),Q(1,16)))
 two_minus_p=add(scale(one,2),scale(p,-1))
 combined=add(scale(mul(q,R),2),mul(p,L))
 base=scale(mul(p,q,add(scale(p,8),scale(mul(two_minus_p,combined),-1))),Q(1,16))
 right=add(add(base,mul(q4,add(one,scale(x,-1)))),scale(mul(p2,q2,x),Q(1,4)))
 if left!=right:raise ValueError('anisotropic full four-variable identity failed')
 old=scale(mul(p,q,add(scale(p,8),scale(mul(R,add(scale(one,4),scale(p2,-1))),-1))),Q(1,16))
 improvement=scale(mul(p2,q,two_minus_p,add(scale(R,3),scale(L,-1))),Q(1,16))
 if add(base,scale(old,-1))!=improvement:raise ValueError('anisotropy gain identity failed')
 return {'full_p_R_L_x_identity':True,'anisotropy_gain_identity':True}


def quantities(state):
 if not M.hermitian(state) or M.trace(state)!=M.ONE or M.matrix_mul(state,state)!=state:raise ValueError('state not pure density')
 radii=sorted(F.local_radii(state));R=sum(radii);L=radii[0]+radii[1]+3*radii[2]+3*radii[3]
 c2=M.trace_product(state,M.spinflip(state));c=F.root_fraction(c2);d=F.root_fraction(1-c2)
 return radii,R,L,c,d


def bound(p,R,L,d):
 s=min(p,2-p);q=1-s;A=q**4;B=s*s*q*q/4
 base=s*q*(8*s-(2-s)*(2*q*R+s*L))/16
 return base,A,B,B-d*max(B-A,0)


def run_pure(name,state,P):
 radii,R,L,c,d=quantities(state);Ts=M.layers(state);t=[M.trace_product(P,T) for T in Ts]
 x=t[0];y=M.trace_product(P,M.spinflip(state))
 if t[1]>3+R/4 or t[3]>(12+L)/16 or 4*t[2]>10-x+(R+L)/2 or y-x>min(d,1-x):
  raise ValueError('pure state layer/spinflip condition failed')
 vals=[]
 for p in (Q(0),Q(1,3),Q(2,3),Q(5,6),Q(1),Q(7,6),Q(4,3)):
  s=min(p,2-p);a,b=1-s/2,s/2;ref=a**4+2*a**3*b
  actual=M.trace_product(P,M.apply_channel(state,p));base,A,B,bonus=bound(p,R,L,d)
  # The piecewise-linear z optimization is checked at ALL breakpoints.
  opt=min(A*z+B*(1-min(d,z)) for z in (Q(0),d,Q(1)))
  if opt!=bonus or actual>ref-base-bonus:raise ValueError('spinflip optimized bound failed')
  aniso=base+min(A,B);coarse=s*(1-s)*(8*s-R*(4-s*s))/16+min(A,B)
  if aniso-coarse != s*s*(1-s)*(2-s)*(3*R-L)/16:raise ValueError('claimed anisotropic improvement failed')
  vals.append({'p':str(p),'actual':str(actual),'reference':str(ref),'anisotropic_bound':str(aniso),
               'spinflip_bound':str(base+bonus),'spinflip_improvement':str(bonus-min(A,B)),
               'remaining_slack':str(ref-actual-base-bonus)})
 return {'state':name,'radii':[str(r) for r in radii],'R':str(R),'L':str(L),'c':str(c),'d':str(d),
         'x':str(x),'y':str(y),'layers':[str(v) for v in t],'parameters':vals}


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 P=M.rank_three_complex_projector()
 if not M.hermitian(P) or M.matrix_mul(P,P)!=P or M.trace(P)!=(Q(3),Q(0)):raise ValueError('invalid actual P')
 states=[('W',w_state()),('unequal_complex_GHZ',F.ghz_asymmetric()),('balanced_complex_GHZ',M.ghz_state()),('product',product_state())]
 results=[run_pure(name,state,P) for name,state in states]
 W=next(row for row in results if row['state']=='W')
 p23=next(row for row in W['parameters'] if row['p']=='2/3')
 if W['R']!='2' or W['L']!='4' or p23['anisotropic_bound']!='1/81':raise ValueError('W example failed')
 # Exact convex mixture of two pure states with stated R,L,d component caps.
 a,b=states[1][1],states[2][1]
 mixture=M.matrix_add(M.matrix_scale(a,Q(2,3)),M.matrix_scale(b,Q(1,3)))
 caps=[quantities(a)[i] for i in (1,2,4)];others=[quantities(b)[i] for i in (1,2,4)]
 caps=[max(x,y) for x,y in zip(caps,others)]
 mix_results=[]
 for p in (Q(1,3),Q(2,3),Q(5,6),Q(1),Q(4,3)):
  s=min(p,2-p);aa,bb=1-s/2,s/2;ref=aa**4+2*aa**3*bb
  actual=M.trace_product(P,M.apply_channel(mixture,p));base,A,B,bonus=bound(p,*caps)
  if actual>ref-base-bonus:raise ValueError('same-P convex mixture cap bound failed')
  mix_results.append({'p':str(p),'remaining_slack':str(ref-actual-base-bonus)})
 report={'result':'PASS_EXACT_ANISOTROPIC_SPINFLIP_SAMPLES_NOT_UNIVERSAL_PROOF',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'own_primitive_pins':{n:p for n,(_,p) in FILES.items()},'symbolic':symbolic(),
         'projector_hermitian_idempotent_trace3':True,'pure_samples':results,
         'convex_mixture_caps_R_L_d':[str(x) for x in caps],'convex_mixture_same_P':mix_results,
         'arithmetic':'exact Fraction complex matrix pairs and polynomial dictionaries',
         'limits':'Four pure samples, one mixture, one P and sampled p values; not universal proof.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))

if __name__=='__main__':main()
