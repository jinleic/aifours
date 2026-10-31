#!/usr/bin/env python3
"""Small independent linear Z3 controls for the written n=32 spectral proof."""
import json
import z3

N=32
H={0:5,3:4,8:4,11:3}
T={0:4,1:2,2:3,4:2,6:2,7:1,13:1,14:1}


def branch(fixed,min_at_zero):
    fixed=[fixed.get(i%16,0) for i in range(N)]
    other=z3.IntVector('v_'+str(min_at_zero),N)
    s=z3.Solver();s.set(timeout=5000)
    s.add(*[v>=0 for v in other]);s.add(z3.Sum(other)==N)
    for gamma in range(N):
        s.add(z3.Sum([fixed[i]*other[(gamma-i)%N] for i in range(N)])==N)
    s.push();s.add(other[0]>=min_at_zero);bad=s.check();s.pop()
    good=s.check()
    if bad!=z3.unsat or good!=z3.sat:
        raise AssertionError((str(bad),str(good)))
    M=s.model();vals=[M.eval(x).as_long() for x in other]
    if any(sum(fixed[i]*vals[(g-i)%N] for i in range(N))!=N for g in range(N)):
        raise AssertionError('positive-control convolution invalid')
    return {'anchored_result':str(bad),'relaxed_result':str(good),
            'relaxed_zero_count':vals[0], 'direct_recheck':'pass'}


if __name__=='__main__':
    print(json.dumps({'periodic_head_tail0_at_least4':branch(H,4),
                      'periodic_tail_head0_at_least5':branch(T,5),
                      'scope':'finite linear-solver controls, not all-order proof'},indent=2))
