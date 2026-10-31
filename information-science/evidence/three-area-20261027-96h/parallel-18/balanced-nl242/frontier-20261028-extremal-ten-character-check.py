#!/opt/homebrew/bin/python3
"""Enumerate ten high-character incidences in all extremal quadratic phases."""
import argparse
import importlib.util
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    path=pathlib.Path(__file__).with_name('frontier-20261028-extremal-sign-syndrome-check.py')
    spec=importlib.util.spec_from_file_location('phase',path);phase=importlib.util.module_from_spec(spec);spec.loader.exec_module(phase)
    def q6(x):return sum(((x>>i)&1)*((x>>(i+1))&1) for i in (0,2,4))%2
    S={0,1,2,7,11,31,47,63};H0=set(range(16))
    D7={x for x in range(64) if q6(x)^((12&x).bit_count()%2)^1}
    D3={x for x in range(64) if q6(x)^((60&x).bit_count()%2)}
    V={0,3,7,11,12,13,14,16,32,48}
    H1={0,3,13,14,16,19,29,30,32,35,45,46,48,51,61,62}
    H2={0,7,11,12,16,23,27,28,32,39,43,44,48,55,59,60}
    reps={'8-8-8-22':([S,S,S,S^D7],255),
          '8-8-14-16':([S,S,S^H0,S^(H0^D3)],143),
          '10-12-12-12':([V,V^H0,V^H1,V^H2],0)}
    result={}
    for name,(sl,center) in reps.items():
        h=[int((x&63) in sl[x>>6]) for x in range(256)];assert h[center] and sum(h)==46
        phases=0;sample=None
        for linear in range(256):
            for constant in (0,1):
                Q=[q6(x&63)^(((x>>6)&1)*((x>>7)&1))^((linear&x).bit_count()%2)^constant for x in range(256)]
                r=[(1+6*Q[x]+4*h[x])%8 for x in range(256)];b0=[int(v in (1,3)) for v in r]
                F=phase.fw([r[x]-8*b0[x] for x in range(256)]);assert F[0]%8==0
                amp=(F[0]//8)%16;assert amp in (5,11);alpha=1 if amp==5 else -1
                assert (r[center]==3 if alpha==1 else r[center]==5)
                delta0=[int(h[x] and x!=center)*(-1 if Q[x] else 1) for x in range(256)]
                FF=phase.fw(delta0)
                Y=[y for y in range(256) if alpha*(-1 if ((center&y).bit_count()%2) else 1)*FF[y]==27]
                assert len(Y)==10
                for x in range(256):
                    if x==center:continue
                    sign=-alpha*(-1 if Q[x] else 1)
                    positive=sum(sign*(-1 if (((center^x)&y).bit_count()%2) else 1)==1 for y in Y)
                    assert positive==(2 if h[x] else 6)
                # Independent direct identity for one deterministic allowed bit pattern.
                b=[int(((x*73+linear*17+constant)&7)<3) for x in range(256)]
                delta=[b[x]-b0[x] for x in range(256)];Fd=phase.fw(delta)
                total=sum(alpha*(-1 if ((center&y).bit_count()%2) else 1)*Fd[y] for y in Y)
                n3=sum(h[x] and delta[x]!=0 for x in range(256));n1=sum(not h[x] and delta[x]!=0 for x in range(256));j=int(delta[center]!=0)
                assert total==6*n3+2*n1-16*j
                if sample is None:sample={'linear_phase':linear,'constant_phase':constant,'indices':Y,'identity_sum':total}
                phases+=1
        assert phases==512
        result[name]={'center':center,'phase_count':phases,'high_characters_per_phase':10,
                      'noncenter_h_positive_incidence':2,'P_positive_incidence':6,'sample':sample}
    out={'scope':'finite extremal incidence table; not a Boolean witness',
         'all_1536_phases_and_all_255_noncenter_columns_checked':True,'representatives':result}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('1536 phases: ten high characters; h/P positive incidences 2/6')


if __name__=='__main__':main()
