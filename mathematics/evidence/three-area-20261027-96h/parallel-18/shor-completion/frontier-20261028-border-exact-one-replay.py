#!/usr/bin/env python3
"""Independent exact-one-clause replay of six-head Shor border tilings.

This is a bounded finite search, not a full completion solver. Its choices are
Q-membership Boolean variables and exact-one clauses, not bitset tile-cover
state. Unknowns, including any interrupted case, are never marked refuted.
"""
from collections import deque
import json,sys,time

A=(0,3,8,11);Y=(0,1,7,13,14)


def exact_one(n,P,forced,deadline,nodecap):
    # q[v]: 0 unknown, 1 false, 2 true; remaining counts unassigned terms.
    # Every target t is a clause sum_{p in P} q[t-p] = 1.
    P=tuple(P); q=bytearray(n); rem=bytearray([len(P)])*n; hit=bytearray(n)
    nodes=[0]
    def apply(q,rem,hit,initial):
        queue=deque(initial)
        while queue:
            v,want=queue.popleft()
            if q[v]:
                if q[v]!=want:return False
                continue
            q[v]=want
            for p in P:
                t=v+p
                if t>=n:t-=n
                rem[t]-=1
                if want==2:
                    if hit[t]:return False
                    hit[t]=1
                    for x in P:
                        w=t-x
                        if w<0:w+=n
                        if w!=v:queue.append((w,1))
                elif not hit[t]:
                    if rem[t]==0:return False
                    if rem[t]==1:
                        for x in P:
                            w=t-x
                            if w<0:w+=n
                            if q[w]==0:
                                queue.append((w,2));break
        return True
    if not apply(q,rem,hit,[(v,2) for v in forced]):return False,0
    def visit(q,rem,hit):
        nodes[0]+=1
        if nodes[0]>nodecap or time.monotonic()>=deadline:return None
        best=-1;best_count=len(P)+1
        for t in range(n):
            if not hit[t] and rem[t]<best_count:
                best=t;best_count=rem[t]
                if best_count==2:break
        if best<0:return [v for v,x in enumerate(q) if x==2]
        # A single remaining literal was already propagated. Branch on every
        # possible true literal of one exact-one clause, hence exhaustive.
        for x in P:
            v=best-x
            if v<0:v+=n
            if q[v]!=0:continue
            cq=q.copy();cr=rem.copy();ch=hit.copy()
            if not apply(cq,cr,ch,[(v,2)]):continue
            answer=visit(cq,cr,ch)
            if answer is None:return None
            if answer is not False:return answer
        return False
    return visit(q,rem,hit),nodes[0]


def controls():
    for n,P,F,expected in [(6,range(6),(0,),True),(6,range(6),(0,1),False),
                           (12,range(6),(0,6),True),(12,range(6),(0,1),False)]:
        result,_=exact_one(n,P,F,time.monotonic()+10,10000)
        if (result is not False)!=expected:raise AssertionError(('control',n,F,result))
        if result is not False and len({(p+q)%n for p in P for q in result})!=n:
            raise AssertionError('invalid control tiling')


def valuation(n,p):
    v=0
    while n%p==0:v+=1;n//=p
    return v


def scan(n,start,end,seconds,nodecap):
    if not (26<=n<=3000 and valuation(n,2) in (2,3) and valuation(n,3)==1):
        raise ValueError('unsupported valuation')
    if not (0<seconds<=120 and 1<=nodecap<=1000000):raise ValueError('limits')
    first=range(1,n,6);second=range(4,n,6)
    total=len(first)*len(second)
    if not 0<=start<=end<=total:raise ValueError('range')
    deadline=time.monotonic()+seconds
    out={'n':n,'all_pairs':total,'ordering':'u=1 mod6 outer, v=4 mod6 inner',
         'start':start,'end':end,'next_index':start,'seconds_cap':seconds,'node_cap':nodecap,
         'propagation_conflicts':0,'searched_unsat':0,'unknown_cases':[],
         'dfs_nodes':0,'status':'INCOMPLETE'}
    for index in range(start,end):
        if time.monotonic()>=deadline:return out
        u=first[index//len(second)];v=second[index%len(second)];P=tuple(sorted(A+(u,v)))
        ans,nodes=exact_one(n,P,Y,deadline,nodecap);out['dfs_nodes']+=nodes
        if ans is None:
            out['unknown_cases'].append({'index':index,'P':P,'nodes':nodes})
            out['next_index']=index+1
            if time.monotonic()>=deadline:return out
        elif ans is False:
            out['propagation_conflicts' if nodes==0 else 'searched_unsat']+=1
            out['next_index']=index+1
        else:
            if len(ans)!=n//6 or not set(Y)<=set(ans):raise AssertionError('bad cardinality')
            sums=[(p+q)%n for p in P for q in ans]
            if len(sums)!=len(set(sums)) or len(sums)!=n:raise AssertionError('bad tiling')
            out['status']='SAT';out['factorization']={'P':P,'Q':ans};out['next_index']=index+1
            return out
    out['status']='CHUNK_EXHAUSTED' if not out['unknown_cases'] else 'CHUNK_WITH_UNKNOWNS'
    return out


if __name__=='__main__':
    controls()
    if len(sys.argv)!=6:raise SystemExit('usage: replay.py N START END SECONDS NODE_CAP')
    print(json.dumps(scan(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),
                          float(sys.argv[4]),int(sys.argv[5])),indent=2))
