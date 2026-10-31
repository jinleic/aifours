#!/usr/bin/env python3
"""Produce an explicit 10th-root product QLS candidate, no transversal claimed."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent
f=[0,1,2,4,3]
t=[tau//2 for tau in range(10)]
exponents=[[[((r*tau+5*(tau%2)*h+2*(h*f[t[tau]]+b*t[tau]))%10)
             for tau in range(10)] for h in range(2) for b in range(5)]
             for r in range(10)]
result={'dimension':10,'normalization':'1/sqrt(10)','root':'exp(2*pi*i/10)',
        'coordinate_fifth_index':t,'phase_permutation':f,'exponents':exponents}
out=p/'frontier-20261028-dita-maximal-qls-result-v1.json'
out.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
print('wrote',out.name,'100 explicit tenth-root vectors; independent check required')
