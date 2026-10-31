#!/opt/homebrew/bin/python3
"""Independent bitset replay of the capped, balanced Walsh-swap component."""
import argparse
import collections
import hashlib
import json
import pathlib
import time

N=512
ALL=(1<<N)-1


def positions(bits):
    while bits:
        low=bits & -bits
        yield low.bit_length()-1
        bits ^= low


def spectrum(bits):
    w=[1-2*((bits>>x)&1) for x in range(N)]
    step=1
    while step<N:
        for base in range(0,N,2*step):
            for j in range(step):
                a,b=w[base+j],w[base+j+step]
                w[base+j],w[base+j+step]=a+b,a-b
        step*=2
    assert w[0]==0 and all(v%4==0 for v in w) and max(map(abs,w))<=32
    return [v//4 for v in w]


def direct_spectrum(bits):
    return [sum((-1 if ((bits>>x)&1) else 1)*(-1 if (a&x).bit_count()%2 else 1)
                for x in range(N)) for a in range(N)]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=pathlib.Path,required=True)
    ap.add_argument('--cap',type=int,required=True)
    ap.add_argument('--max-nodes',type=int,required=True)
    ap.add_argument('--max-seconds',type=int,required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    args=ap.parse_args()
    if args.output.exists(): raise FileExistsError(args.output)
    if not (0<=args.cap<=512 and 1<=args.max_nodes<=200000 and 1<=args.max_seconds<=300): raise ValueError('bad bounds')
    text=json.loads(args.input.read_text(encoding='utf-8'))['bits']
    if len(text)!=N or set(text)-{'0','1'} or text.count('1')!=256: raise ValueError('invalid initial truth table')
    original=int(text[::-1],2)
    # Character masks also serve as masks of coordinates of the same parity.
    positive=[]
    for x in range(N):
        positive.append(sum(1<<a for a in range(N) if not ((x&a).bit_count()&1)))
    negative=[ALL^p for p in positive]
    assert positive[0]==ALL and all(positive[x].bit_count()==256 for x in range(1,N))
    initial=spectrum(original)
    assert sum(v*v for v in initial)==16384
    assert direct_spectrum(original)==[4*v for v in initial]
    visited={original}; queue=collections.deque([original])
    expanded=0; peak_neighbors=0; within_cap=0; best_n32=sum(abs(v)==8 for v in initial)
    if best_n32>args.cap: raise ValueError('input exceeds cap')
    control_states=[]; hit_cap=False; target=False; timed_out=False
    started=time.monotonic()
    while queue and not hit_cap and not target and not timed_out:
        bits=queue.popleft(); expanded+=1; k=spectrum(bits)
        masks={v:sum(1<<a for a,t in enumerate(k) if t==v) for v in (-8,-7,7,8)}
        n32=(masks[-8]|masks[8]).bit_count()
        zeros=ALL^bits
        for x in positions(bits):
            # An outward move from a peak can be avoided only when x and y
            # have the same character value at each outward-aligned frequency.
            positive_out=masks[8]&positive[x]
            negative_out=masks[-8]&negative[x]
            allowed=zeros
            for a in positions(positive_out): allowed &= positive[a]
            for a in positions(negative_out): allowed &= negative[a]
            peak_neighbors += allowed.bit_count()
            up7=(masks[7]&positive[x])|(masks[-7]&negative[x])
            down8=(masks[8]&negative[x])|(masks[-8]&positive[x])
            for y in positions(allowed):
                changed=negative[x^y]
                new_n32=n32+(up7&changed).bit_count()-(down8&changed).bit_count()
                if new_n32>args.cap: continue
                within_cap+=1
                newbits=bits^(1<<x)^(1<<y)
                if len(control_states)<4:
                    expected=[4*(k[a]+(1 if (positive[x]>>a)&1 else -1)) if (changed>>a)&1 else 4*k[a] for a in range(N)]
                    actual=direct_spectrum(newbits)
                    assert actual==expected and max(map(abs,actual))<=32
                    wrong=expected.copy(); wrong[1]+=4
                    assert wrong!=actual
                    control_states.append({'x':x,'y':y,'n32':new_n32})
                if newbits in visited: continue
                visited.add(newbits)
                if new_n32<best_n32: best_n32=new_n32
                if new_n32==0: target=True; break
                if len(visited)>=args.max_nodes: hit_cap=True; break
                queue.append(newbits)
            if target or hit_cap: break
        if expanded%100==0: print('expanded=',expanded,'discovered=',len(visited),'best_n32=',best_n32,flush=True)
        if time.monotonic()-started>=args.max_seconds: timed_out=True
    digest=hashlib.sha256(b''.join(x.to_bytes(64,'little') for x in sorted(visited))).hexdigest()
    receipt={'input':str(args.input),'max_n32':args.cap,'max_nodes':args.max_nodes,
             'expanded':expanded,'discovered':len(visited),'best_n32':best_n32,
             'neighbors_examined':expanded*256*256,'peak32_neighbors':peak_neighbors,
             'neighbors_within_cap':within_cap,'target_met':target,'hit_node_cap':hit_cap,
             'timed_out':timed_out,'queue_drained':not queue and not target and not hit_cap and not timed_out,
             'vertex_set_sorted_sha256_le_64bytes':digest,'independent_direct_controls':control_states,
             'elapsed_seconds':time.monotonic()-started}
    with args.output.open('x',encoding='utf-8') as f: json.dump(receipt,f,indent=2,sort_keys=True); f.write('\n')
    print('expanded=',expanded,'discovered=',len(visited),'peak_neighbors=',peak_neighbors,'within_cap=',within_cap,'queue_drained=',receipt['queue_drained'],flush=True)


if __name__=='__main__': main()
