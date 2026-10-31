#!/opt/homebrew/bin/python3
"""Exact integer controls for the q-zero-dependent energy/peak inequalities."""
import argparse
import json
import pathlib


def bound(z,Z):
    numerator=9216-20*z-16*Z
    m=2*(numerator//128)
    n=max(0,(64*(256-m)-6400+23)//24)
    return m,n


def main():
    p=argparse.ArgumentParser();p.add_argument('--formal-placement',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    table=[]
    for z in (64,96,112,120,128,136,144,160,192,256):
        m,n=bound(z,1)
        allowed=[x for x in range(0,257,2) if 64*x<=16*(z-1)+36*(256-z)]
        assert max(allowed)==m
        feasible=[n7 for n7 in range(257) if 64*(256-m)<=49*n7+25*(256-n7)]
        assert min(feasible)==n
        table.append({'q_zero_count':z,'Walsh_zeros_at_least':1,'m_upper':m,'peak_lower':n})
    data=json.loads(a.formal_placement.read_text());k=data['k_values']
    assert len(k)==512 and k[0]==0 and max(map(abs,k))<=7
    q=[(k[x]//2)%2 for x in range(256)];z=q.count(0);Z=k.count(0)
    assert z==136 and Z==10 and all(k[x]%2==0 for x in range(256))
    e=sum(v*v for v in k[:256]);o=sum(v*v for v in k[256:]);assert e%64==0 and e+o==16384
    m=e//64;n7=sum(abs(v)==7 for v in k[256:]);mmax,nmin=bound(z,Z)
    assert (m,n7,mmax,nmin)==(80,208,98,155)
    assert 64*m<=16*(z-Z)+36*(256-z)
    assert o<=49*n7+25*(256-n7)
    result={'scope':'integer energy controls; formal spectrum is a NON-WITNESS',
            'table_at_Z_at_least_1':table,'formal_control':{'z':z,'Z':Z,'formal_m':m,
              'n7':n7,'m_upper':mmax,'peak_lower':nmin,'boolean_witness':False}}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(result,dst,indent=2,sort_keys=True);dst.write('\n')
    print('ten integer energy rows; formal ten-zero non-witness satisfies its z/Z bounds')


if __name__=='__main__':main()
