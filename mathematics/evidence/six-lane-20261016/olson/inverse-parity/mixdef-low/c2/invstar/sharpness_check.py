"""Independent raw ordered-product DP checks of Proposition SH and its three explicit extensions.
No GR/GR0/WAS formulas. Usage: python3 sharpness_check.py
"""
import os,sys,json
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'..','..','..','..','code'))
import was_verify as wv
out=[]
for p in (5,7,11,13,17,19,23,29,31):
    for v in (0,1,p-1):
        u=(v-2)%p
        w=[('F',u)]+[('R',1)]*(2*p-3)+[('F',v)]*(2*p-1)
        cases=[w,
               [('F',u)]+[('R',1)]*(2*p-2)+[('F',v)]*(2*p-1),
               [('F',u)]+[('R',1)]*(2*p-3)+[('F',v)]*(2*p),
               [('F',u)]*2+[('R',1)]*(2*p-3)+[('F',v)]*(2*p-1)]
        hits=[wv.dp_has(x,p) for x in cases]
        assert hits==[False,True,True,True],(p,v,hits)
        out.append({'p':p,'v':v,'dp_has':hits,'lengths':[len(x) for x in cases]})
print(json.dumps({'cases':len(out),'raw_DP_checks':4*len(out),'failures':0,'rows':out},indent=1))
