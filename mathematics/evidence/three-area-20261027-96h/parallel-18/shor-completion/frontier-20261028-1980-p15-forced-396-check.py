#!/usr/bin/env python3
"""Exact head/tail quota relaxations forcing gcd396 in both sides at n1980."""
from itertools import combinations
from math import gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
assert GA=={3,4,5,11} and GY=={1,2,6,12}

def run(old,bans,spec,anchors):
    C=[x for x in range(n) if any(x%m==r for m,r,k in spec) and
       all(x==a or gcd(x-a,n) not in bans for a in old)]
    N=len(C);idx={x:i for i,x in enumerate(C)}
    adj=[sum(1<<j for j,y in enumerate(C) if y!=x and gcd(x-y,n) in bans) for x in C]
    group=[sum(1<<i for i,x in enumerate(C) if x%m==r) for m,r,k in spec]
    mem=[tuple(j for j,g in enumerate(group) if g>>i&1) for i in range(N)]
    av=(1<<N)-1;need=[k for m,r,k in spec]
    for a in anchors:
        i=idx[a];assert av>>i&1;av &= ~(adj[i]|1<<i)
        for j in mem[i]:need[j]-=1
    stats={'nodes':0,'prunes':0};cache=set()
    def dfs(av,need):
        stats['nodes']+=1;need=list(need)
        for j,k in enumerate(need):
            if k<0:return False
            if k==0:av &= ~group[j]
        if any((av&group[j]).bit_count()<k for j,k in enumerate(need)):
            stats['prunes']+=1;return False
        if not any(need):return True
        key=(av,tuple(need))
        if key in cache:return False
        j=min((j for j,k in enumerate(need) if k),key=lambda j:((av&group[j]).bit_count()-need[j],(av&group[j]).bit_count()))
        bits=av&group[j];v=[]
        while bits:
            low=bits&-bits;bits-=low;v.append(low.bit_length()-1)
        i=max(v,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;n2=need.copy()
        for j in mem[i]:n2[j]-=1
        if dfs(av&~(adj[i]|b),tuple(n2)) or dfs(av&~b,tuple(need)):return True
        cache.add(key);return False
    if dfs(av,tuple(need)):raise AssertionError('unexpected quota witness')
    return {'candidates':N,'nodes':stats['nodes'],'prunes':stats['prunes']}

pspec=[(5,r,3) for r in (0,1,2,4)]
qspec=[(4,1,33),(4,2,33),(4,3,33),(11,1,12),(11,2,12),(11,7,12)]
p=run(A,GY|{396},pspec,(0,11));q=run(Y,GA|{396},qspec,(1,7,13,14))
assert p['candidates']==56 and q['candidates']==298
WP=[0,11,132,264,275,327,396,407,539,1320,1859,1911]
WQ=[1,7,13,14,61,67,74,110,127,133,181,193,211,230,247,271,277,290,313,337,343,350,374,391,410,457,470,494,523,554,601,607,614,674,721,727,734,770,787,793,841,853,871,890,907,973,991,997,1003,1010,1034,1051,1063,1070,1117,1123,1130,1154,1171,1183,1214,1237,1261,1267,1274,1303,1321,1327,1333,1334,1381,1387,1393,1394,1430,1447,1453,1501,1513,1531,1550,1591,1633,1657,1670,1694,1711,1717,1730,1777,1783,1790,1814,1831,1843,1861,1921,1927,1934]
for W,old,bans,spec,anchors in ((WP,A,GY,pspec,(0,11)),(WQ,Y,GA,qspec,(1,7,13,14))):
    assert len(W)==len(set(W)) and set(anchors)<=set(W)
    assert all(all(x==a or gcd(x-a,n) not in bans for a in old) for x in W)
    assert all(gcd(a-b,n) not in bans for a,b in combinations(W,2))
    assert all(sum(x%m==r for x in W)==k for m,r,k in spec)
    assert any(gcd(a-b,n)==396 for a,b in combinations(W,2))
print(json.dumps({'head':p,'tail':q,'both':'UNSAT','relaxed_controls':'SAT after removing 396',
                  'scope':'only n1980 P-size15 border branch'},indent=2))
