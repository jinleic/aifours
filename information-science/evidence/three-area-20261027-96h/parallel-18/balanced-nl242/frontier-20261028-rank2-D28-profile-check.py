#!/opt/homebrew/bin/python3
"""Exact rank-two D28 necessary profile enumeration and non-witness controls."""
import argparse
import collections
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--placement',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    data=json.loads(a.placement.read_text());k=data['spectrum_k'];assert len(k)==512
    vals=[n for n in range(29) if n%3==2]
    possibilities=[]
    for wtQ in (64,128):
        for s in (0,128):
            for n1 in vals:
                n3=28-n1;n5=(356-n1)//3;n7=228-n5;h=(440-4*n1)//3
                for e in range(-28,29,2):
                    numerator=12*h-7*(256-2*wtQ)-8*e-s
                    if numerator%24:continue
                    q1h=numerator//24;q0h=h-q1h
                    if not (0<=q1h<=min(wtQ,h) and 0<=q0h<=256-wtQ):continue
                    q0delta=(e+6)//2;q1delta=(e-6)//2
                    if max(abs(q0delta),abs(q1delta))>28:continue
                    possibilities.append({'Q_weight':wtQ,'odd_sum':s,'delta_sum':e,
                                          'n1':n1,'n3':n3,'n5':n5,'n7':n7,
                                          'h_weight':h,'h_intersection_Q':q1h,'h_intersection_Q0':q0h})
    assert vals==[2,5,8,11,14,17,20,23,26]
    assert {p['Q_weight'] for p in possibilities}=={64,128}
    assert {p['odd_sum'] for p in possibilities}=={0,128}
    Q=[int(x%4==3) for x in k[256:]];h=[int(abs(x) in (3,5)) for x in k[256:]]
    vec={'Q_weight':sum(Q),'odd_sum':sum(k[256:]),'n1':sum(abs(x)==1 for x in k[256:]),
         'n3':sum(abs(x)==3 for x in k[256:]),'n5':sum(abs(x)==5 for x in k[256:]),
         'n7':sum(abs(x)==7 for x in k[256:]),'h_weight':sum(h),
         'h_intersection_Q':sum(x*y for x,y in zip(h,Q)),
         'h_intersection_Q0':sum(x*(1-y) for x,y in zip(h,Q)), 'delta_sum':-4}
    assert vec in possibilities and (vec['Q_weight'],vec['odd_sum'],vec['n1'])==(128,128,11)
    hvalues=sorted({p['h_weight'] for p in possibilities});assert hvalues==[112,116,120,124,128,132,136,140,144]
    multiples4=[p for p in possibilities if p['h_weight']%4==0]
    assert len(multiples4)==len(possibilities)
    result={'scope':'necessary scalar/profile calculations, formal NON-WITNESS positive control',
            'profiles':possibilities,'distinct_h_weights':hvalues,'profiles_h_divisible_by_4':len(multiples4),
            'formal_control_profile':vec,'formal_control_claims_boolean_witness':False}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(result,dst,indent=2,sort_keys=True);dst.write('\n')
    print('D28 basic profiles retain both Q weights and odd sums; no Boolean realization asserted')


if __name__=='__main__':main()
