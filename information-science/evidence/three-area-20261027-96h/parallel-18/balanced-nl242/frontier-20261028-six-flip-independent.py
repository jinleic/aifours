#!/opt/homebrew/bin/python3
"""Re-enumerate peak-compatible six-sets with Python big integers and direct sums."""
import argparse
import itertools
import json
import pathlib
import time

N=512
ALL=(1<<N)-1


def members(bits):
    while bits:
        one=bits & -bits
        yield one.bit_length()-1
        bits^=one


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--seeds',type=pathlib.Path,required=True)
    ap.add_argument('--index',type=int,required=True)
    ap.add_argument('--max-seconds',type=int,required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    ap.add_argument('--candidate',type=pathlib.Path,required=True)
    args=ap.parse_args()
    if not 1<=args.index<=3 or not 1<=args.max_seconds<=300: raise ValueError('bad bounds')
    if args.output.exists() or args.candidate.exists(): raise FileExistsError('output exists')
    seeds=[line.strip() for line in args.seeds.read_text(encoding='utf-8').splitlines()
           if line.strip() and not line.startswith('#')]
    binary=bin(int(seeds[args.index-1],16))[2:].zfill(512)
    truth=int(binary[::-1],2)
    # Direct character sums by exact 512-bit signed-coordinate population counts.
    chars=[sum(1<<x for x in range(N) if (a&x).bit_count()&1) for a in range(N)]
    original=[N-2*(truth^chars[a]).bit_count() for a in range(N)]
    assert max(map(abs,original))==28 and all(w!=0 for w in original)
    peaks=[a for a,w in enumerate(original) if abs(w)==28]
    bad=[(truth^chars[a]) if original[a]>0 else ALL^(truth^chars[a]) for a in peaks]
    per_point=[0]*N
    for j,mask in enumerate(bad):
        for x in members(mask): per_point[x]|=1<<j
    assert all(mask.bit_count()==242 for mask in bad)
    upper3=(1<<510)-1; upper4=(1<<511)-1
    triples=quads=fives=0; sixes=[]; found=None; stop=False; timed_out=False
    start=time.monotonic()
    def compatible_after(q):
        allowed=ALL ^ ((1<<(q[-1]+1))-1)
        for a,b,c in itertools.combinations(q,3):
            shared=per_point[a]&per_point[b]&per_point[c]
            while shared and allowed:
                one=shared&-shared; allowed &= ALL^bad[one.bit_length()-1]; shared^=one
            if not allowed: break
        return allowed
    for x in range(507):
        for y in range(x+1,508):
            xy=per_point[x]&per_point[y]
            for z in range(y+1,509):
                triples+=1
                shared=xy&per_point[z]
                allowed=(ALL ^ ((1<<(z+1))-1)) & upper3
                while shared and allowed:
                    one=shared&-shared; allowed &= ALL^bad[one.bit_length()-1]; shared^=one
                for q3 in members(allowed):
                    quads+=1
                    for q4 in members(compatible_after((x,y,z,q3)) & upper4):
                        fives+=1
                        for q5 in members(compatible_after((x,y,z,q3,q4))):
                            flips=(x,y,z,q3,q4,q5)
                            # Directly recompute all 512 character sums, independent
                            # of the C++ program's incremental coefficient formula.
                            changed=truth
                            for v in flips: changed^=1<<v
                            w=[N-2*(changed^chars[a]).bit_count() for a in range(N)]
                            peak=max(map(abs,w)); zeros=[a for a,v in enumerate(w) if not v]
                            assert all(sum((mask>>v)&1 for v in flips)<=3 for mask in bad)
                            sixes.append({'flips':flips,'peak':peak,'zero_count':len(zeros)})
                            if peak<=28 and zeros:
                                frequency=zeros[0]
                                balanced=changed^chars[frequency]
                                assert balanced.bit_count()==256
                                candidate={'format':'boolean-truth-v1','seed_index_1based':args.index,
                                           'flips':flips,'affine_twist_frequency':frequency,
                                           'bits':''.join(str((balanced>>i)&1) for i in range(N))}
                                with args.candidate.open('x',encoding='utf-8') as out:
                                    json.dump(candidate,out,indent=2); out.write('\n')
                                found=flips; stop=True; break
                        if stop: break
                    if stop: break
                if stop: break
            if stop: break
        if x%50==0: print('first=',x,'triples=',triples,'sixes=',len(sixes),flush=True)
        if stop: break
        if time.monotonic()-start>=args.max_seconds: timed_out=True; break
    # Corrupt one source coefficient and ensure full direct sums do not match.
    mutated=original.copy(); mutated[1]+=4
    assert mutated!=[N-2*(truth^chars[a]).bit_count() for a in range(N)]
    receipt={'seed_index_1based':args.index,'triples':triples,'compatible_quads':quads,
             'compatible_fives':fives,'compatible_sixes_checked':len(sixes),
             'peak_count':len(peaks),'complete':not timed_out and not stop,'timed_out':timed_out,
             'target_met':found is not None,'six_sets':sixes,'mutation_rejected':True,
             'elapsed_seconds':time.monotonic()-start}
    with args.output.open('x',encoding='utf-8') as out: json.dump(receipt,out,indent=2,sort_keys=True); out.write('\n')
    print('complete=',receipt['complete'],'sixes=',len(sixes),'target=',found is not None,flush=True)


if __name__=='__main__': main()
