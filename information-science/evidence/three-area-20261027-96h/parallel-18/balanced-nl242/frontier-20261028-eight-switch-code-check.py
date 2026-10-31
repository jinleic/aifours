#!/opt/homebrew/bin/python3
"""Exhaust relation-code types of eight signed F2^8 atoms, modulo 3."""
import argparse
import collections
import itertools
import json
import pathlib


def fw(a):
    a=list(a);step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):x,y=a[j],a[j+step];a[j]=x+y;a[j+step]=x-y
        step*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    # Sign patterns are encoded by the 8 bits whose signs are negative.
    nonzero=[x for x in range(256) if (8-2*x.bit_count())%3!=0]
    assert len(nonzero)==170
    relations=[x for x in range(1,256) if x.bit_count()%2==0 and x.bit_count()>=4]
    rank6={}
    for weight in (4,6,8):
        r=(1<<weight)-1
        rank6[str(weight)]={str(syndrome):2*sum(((x&r).bit_count()%2)==syndrome for x in nonzero)
                            for syndrome in (0,1)}
    assert {v for row in rank6.values() for v in row.values()}=={116,152,164,176,188,224}
    spaces2={tuple(sorted((x,y,x^y))) for i,x in enumerate(relations) for y in relations[i+1:]
             if (x^y).bit_count()>=4}
    assert len(spaces2)==1225
    hist2=collections.Counter()
    for sp in spaces2:
        x,y,_=sp;bins=collections.Counter((((p&x).bit_count()%2),((p&y).bit_count()%2)) for p in nonzero)
        for u,v in itertools.product((0,1),repeat=2):hist2[4*bins[(u,v)]]+=1
    expected2={104:35,128:245,152:1540,176:2240,200:770,224:70}
    assert dict(hist2)==expected2
    spaces3=set()
    for x,y,z in itertools.combinations(relations,3):
        span={x,y,z,x^y,x^z,y^z,x^y^z}
        if len(span)==7 and all(v.bit_count()>=4 for v in span):spaces3.add(tuple(sorted(span)))
    assert len(spaces3)==1605
    hist3=collections.Counter()
    for sp in spaces3:
        x=sp[0];y=next(v for v in sp if v!=x);z=next(v for v in sp if v not in (x,y,x^y))
        bins=collections.Counter((((p&x).bit_count()%2),((p&y).bit_count()%2),((p&z).bit_count()%2)) for p in nonzero)
        for u,v,w in itertools.product((0,1),repeat=3):hist3[8*bins[(u,v,w)]]+=1
    expected3={80:105,128:3075,176:7980,224:1680}
    assert dict(hist3)==expected3
    all_values={170}|{v for row in rank6.values() for v in row.values()}|set(hist2)|set(hist3)
    assert not any(130<=v<=148 for v in all_values)
    # A real eight-atom affine-rank-six configuration checks the rank-six count.
    d=[0]*256
    for x in (0,1,2,3,4,8,16,32):d[x]=1
    assert sum(v%3!=0 for v in fw(d))==164
    # Twelve atoms can pass the coarse interval; this is not a Boolean-target witness.
    pts=[164,167,228,91,231,10,210,9,64,163,2,43]
    signs=[-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1];d12=[0]*256
    for x,s in zip(pts,signs):d12[x]=s
    M12=sum(v%3!=0 for v in fw(d12));assert M12==144 and sum(v!=0 for v in d12)==12
    out={'scope':'finite signed-support code classification and formal D12 near miss, no Boolean witness',
         'rank7_M':170,'rank6_M_by_relation_weight_and_syndrome':rank6,
         'rank5_relation_space_count':len(spaces2),'rank5_M_histogram':dict(sorted(hist2.items())),
         'rank4_relation_space_count':len(spaces3),'rank4_M_histogram':dict(sorted(hist3.items())),
         'rank3_M_multiple_of_32':True,'required_interval':[130,148],
         'eight_atom_control_M':164,'twelve_atom_nearmiss_M':M12,'twelve_atom_positions':pts,'twelve_atom_signs':signs}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('all even-relation codes: no eight-atom M in [130,148]; D12 near miss M=144')


if __name__=='__main__':main()
