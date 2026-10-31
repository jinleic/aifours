#!/usr/bin/env python3
"""Build deterministic divisor-conflict covers; independently checked separately."""
from math import gcd
from pathlib import Path
import json

n=1320;A=(0,3,8,11);Y=(0,1,7,13,14)
GA={gcd(a-b,n) for a in A for b in A if a!=b}
GY={gcd(a-b,n) for a in Y for b in Y if a!=b}
QC=[x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)]
triangles=[[195,256,418],[253,344,415],[459,916,1078],[872,913,1075],
 [33,987,1136],[80,638,1251],[35,198,216],[155,336,473],[395,456,858],
 [515,576,1133],[132,635,696],[143,755,816],[407,875,936],[924,995,1176],
 [1115,1188,1296],[96,1199,1235]]
p80=[0,3,8,11,33,63,68,88,123,128,132,143,183,188,198,243,248,253,264,
 275,303,308,363,368,396,407,418,423,428,473,483,488,528,539,543,548,
 583,603,608,638,660,663,668,671,693,723,728,748,783,788,792,803,843,848,
 858,903,908,913,924,935,963,968,1023,1028,1056,1067,1078,1083,1088,
 1133,1143,1148,1188,1199,1203,1208,1243,1263,1268,1298]


def dsatur_cover():
    N=len(QC);full=(1<<N)-1
    adj=[sum(1<<j for j,y in enumerate(QC) if y!=x and gcd(x-y,n) in GA) for x in QC]
    groups=[];unassigned=set(range(N))
    while unassigned:
        winner=None;score=None;legal_winner=None
        for x in unassigned:
            legal=[i for i,g in enumerate(groups) if not g&(full^adj[x])]
            sc=(len(groups)-len(legal),N-1-adj[x].bit_count(),-x)
            if score is None or sc>score:winner=x;score=sc;legal_winner=legal
        if legal_winner:
            k=max(legal_winner,key=lambda i:groups[i].bit_count());groups[k]|=1<<winner
        else:groups.append(1<<winner)
        unassigned.remove(winner)
    return [[QC[j] for j in range(N) if mask>>j&1] for mask in groups]


if __name__=='__main__':
    data={'n':n,'P_triangles':triangles,'P80_divisor_screen_witness':p80,
          'Q_conflict_cliques':dsatur_cover()}
    path=Path(__file__).with_name('frontier-20261028-1320-divisor-packing-v1.json')
    if path.exists():raise FileExistsError('refuse overwrite')
    path.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'artifact':str(path),'Q_groups':len(data['Q_conflict_cliques']),'bytes':path.stat().st_size}))
