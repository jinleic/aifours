#!/usr/bin/env python3
"""Re-evaluate the explicit rational generalized-eigenvalue witness."""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def main():
    p=ROOT/'frontier-20261028-level6-226-ratio-cone-certificate-v1.json';raw=p.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b'
    C=json.loads(raw);W=json.loads((ROOT/'frontier-20261028-level6-226-ratio-endpoint-certificate-v1.json').read_text())
    plus=[[Q(x) for x in row] for row in C['symmetric_forms']['lambda_HL_plus_HK']]
    minus=[[Q(x) for x in row] for row in C['symmetric_forms']['lambda_HL_minus_HK']]
    x=[Q(q) for q in W['exact_negative_vector']];n=len(x);assert n==len(plus)==len(minus)==34
    # (449/100)HL-HK = (449/900)(plus+minus) - (plus-minus)/2.
    val=sum((x[i]*((Q(449,900)*(plus[i][j]+minus[i][j]))-(plus[i][j]-minus[i][j])/2)*x[j]
             for i in range(n) for j in range(n)),Q(0))
    assert val==Q(W['exact_negative_quadratic_value']) and val<0
    out=ROOT/'frontier-20261028-level6-226-ratio-endpoint-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'dimension':n,'lower_rational':'449/100','upper_rational':'9/2',
                               'negative_witness_value':str(val),'status':'PASS_EXACT_LOWER_NEGATIVE_WITNESS',
                               'scope':'given full ratio matrices; upper positive forms and source require separately pinned replay'},indent=2)+'\n')
    print('PASS exact negative witness at 449/100 from pinned plus/minus forms;',out.name)

if __name__=='__main__':main()
