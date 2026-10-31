#!/opt/homebrew/bin/python3
"""Direct control of block Walsh transforms, XORs and odd radical phase."""
import argparse
import json
import pathlib


def rank(rows):
    piv={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i]
            else:piv[i]=v;break
    return len(piv)


def main():
    p=argparse.ArgumentParser();p.add_argument('--candidate',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    bits=list(map(int,json.loads(args.candidate.read_text(encoding='utf-8'))['bits']))
    assert len(bits)==512 and sum(bits)==256
    blocks=[[bits[u|(y<<7)] for u in range(128)] for y in range(4)]
    assert all(sum(v)==64 for v in blocks)
    xor=[]
    for block in blocks:
        t=0
        for x,v in enumerate(block):
            if v:t^=x
        xor.append(t)
    assert xor==[1,0,0,0]
    local=[[sum((1-2*block[x])*(-1 if (a&x).bit_count()%2 else 1) for x in range(128))
            for a in range(128)] for block in blocks]
    globalW=[sum((1-2*bits[x])*(-1 if (a&x).bit_count()%2 else 1) for x in range(512)) for a in range(512)]
    for b in range(128):
        for r in range(4):assert globalW[b|(r<<7)]==sum((-1 if (r&y).bit_count()%2 else 1)*local[y][b] for y in range(4))
    assert [globalW[x] for x in (0,128,256,384)]==[0,0,0,0]
    assert all(v%4==0 for v in globalW);k=[v//4 for v in globalW]
    # Odd frequencies have low bit one because T=1. On R, rho equals the
    # XOR of labels of blocks whose support XOR is T.
    rho=[]
    for r in (128,256):
        odd=[a for a in range(512) if a&1]
        diff={(((k[a^r]-1)//2)^((k[a]-1)//2))%2 for a in odd}
        assert len(diff)==1
        bit=0 if r==128 else 1
        expected=sum(int(t==1)*((y>>bit)&1) for y,t in enumerate(xor))%2
        assert next(iter(diff))==expected;rho.append(expected)
    # Both nonsingular six-variable quadratic zero sets span the quotient.
    singular=[]
    for arf in (0,1):
        Z=[x for x in range(64) if (sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+arf*((x&1)+((x>>1)&1)))%2==0]
        assert rank(Z)==6
        singular.append({'arf':arf,'zero_count':len(Z),'zero_span_rank':rank(Z)})
    result={'block_weights':[64]*4,'block_support_xors':xor,'T':1,'zero_plane':[0,128,256,384],
            'global_local_walsh_identity_512':True,'odd_radical_phase':rho,'exceptional_block':0,
            'singular_span_controls':singular,'peak':max(map(abs,globalW)),
            'actual_target_witness':max(map(abs,globalW))<=28,
            'scope':'actual high-peak control; finite tests supplement written proof'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('block_xors=',xor,'rho=',rho,'peak=',max(map(abs,globalW)),flush=True)


if __name__=='__main__':main()
