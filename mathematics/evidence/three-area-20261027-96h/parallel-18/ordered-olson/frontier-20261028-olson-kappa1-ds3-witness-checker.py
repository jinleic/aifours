#!/usr/bin/env python3
"""Independently verify one original p=11 adjacent-packet DS3 witness."""
import argparse
import copy
import hashlib
import json


def product(word,indices,p):
    x,e=0,0
    for i in indices:
        y,f=word[i]
        x=(x+(-y if e else y))%p
        e ^= f
    return x,e


def verify(word,p,w):
    K=w['K']
    if len(K)!=2 or K!=sorted(set(K)) or any(i<0 or i>=len(word) or word[i][1] for i in K):
        raise ValueError('BAD_ACTUAL_K')
    C=2*p-len(K)
    packets=w['packets']
    if len(packets)!=C or w['C']!=C:
        raise ValueError('PACKET_COUNT')
    S=sum(word[i][0] for i in K)%p
    def gauge(i):
        return (word[i][0]+2*sum(word[k][0] for k in K if k<i))%p
    prev=-1
    binary=0
    chosen=[]
    base=S
    increments=[]
    for q,pkt in enumerate(packets):
        positions=pkt['positions']
        if not positions or positions!=sorted(positions) or positions[0]<=prev or any(i<0 or i>=len(word) or not word[i][1] for i in positions):
            raise ValueError('PACKET_SPAN')
        prev=positions[-1]
        sign=1 if q%2==0 else -1
        base=(base+sign*gauge(positions[0]))%p
        if pkt['kind']=='single':
            if len(positions)!=1 or pkt['chosen']!=positions[0]:
                raise ValueError('SINGLETON')
        elif pkt['kind']=='binary':
            if len(positions)!=2 or positions[0]==positions[1]:
                raise ValueError('BINARY_DISTINCT')
            d=(gauge(positions[1])-gauge(positions[0]))%p
            if not d or pkt['gauge_delta']!=d:
                raise ValueError('GAUGE_DELTA')
            if pkt['chosen'] not in positions:
                raise ValueError('BINARY_CHOICE')
            increments.append((sign*d)%p)
            binary+=1
        else:
            raise ValueError('PACKET_KIND')
        chosen.append(pkt['chosen'])
    if binary!=p-3 or w['p_minus_3_binary_packets']!=p-3:
        raise ValueError('BINARY_COUNT')
    support={base}
    for d in increments:
        support |= {(x+d)%p for x in support}
    if 0 not in support:
        raise ValueError('PACKET_SUPPORT_MISSES_ZERO')
    selector=w['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or set(selector)!=set(K)|set(chosen):
        raise ValueError('SELECTOR_INDICES')
    if product(word,selector,p)!=(0,0):
        raise ValueError('ORIGINAL_PRODUCT')
    return {'binary_packets':binary,'singleton_packets':C-binary,'base':base,
            'signed_increments':increments,'packet_support':sorted(support),
            'original_selector':selector,'K':K}


def mutation(word,p,w,edit,expected):
    c=copy.deepcopy(w)
    edit(c)
    try:
        verify(word,p,c)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('MUTATION_WRONG: '+str(exc)) from exc
    raise ValueError('MUTATION_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('search')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    raw=open(args.input,'rb').read()
    sr=open(args.search,'rb').read()
    source=json.loads(raw)
    found=json.loads(sr)
    if found['result']!='ACTUAL_DS3_PACKET_WITNESS_FOUND' or found['p']!=11:
        raise ValueError('WRONG_SEARCH_RESULT')
    item=next(x for x in source['cases'] if x['p']==11)
    word=item['word']
    p=item['p']
    if found['input_sha256']!=hashlib.sha256(raw).hexdigest():
        raise ValueError('INPUT_HASH')
    witness=found['witness']
    checked=verify(word,p,witness)
    bi=next(i for i,pkt in enumerate(witness['packets']) if pkt['kind']=='binary')
    controls=[
        mutation(word,p,witness,lambda x:x['packets'][bi]['positions'].__setitem__(1,x['packets'][bi]['positions'][0]),'BINARY_DISTINCT'),
        mutation(word,p,witness,lambda x:x['selector'].__setitem__(1,x['selector'][0]),'SELECTOR_INDICES'),
        mutation(word,p,witness,lambda x:x['packets'][bi].__setitem__('gauge_delta',0),'GAUGE_DELTA'),
    ]
    result={'result':'PASS_INDEPENDENT_ACTUAL_DS3_WITNESS','input_sha256':hashlib.sha256(raw).hexdigest(),
            'search_sha256':hashlib.sha256(sr).hexdigest(),'p':p,'checked':checked,
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'one actual positive DS3 packet witness, not any negative/universal certificate'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
