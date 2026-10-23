#!/usr/bin/env python3
"""[F] Additional sensitivity control: tighten both QS* endpoints by a declared integer SHIFT, not a real theorem acceptance mode.
The review-requested one-unit tightening is retained separately in seedXstar3 MODE3.  This wrapper changes bounds in memory only;
no frozen source file is edited.  CLI: python3 -B star3_tightN.py SHIFT PMAX [detail].
"""
import sys,json,hashlib
G={'__name__':'star3_control_lib'}
src=open('seedXstar3.py').read();guard="if __name__ == '__main__':\n    main()"
exec(compile(src.replace(guard,''),'seedXstar3.py','exec'),G)
original=G['bounds']
def tightened(p,k,kap,B,d,mode):
    if mode!=3:return original(p,k,kap,B,d,mode)
    lo,hi=original(p,k,kap,B,d,0)
    return lo+SHIFT,hi-SHIFT
G['bounds']=tightened
if __name__=='__main__':
    SHIFT=int(sys.argv[1])
    print(json.dumps({'control_source_sha256':hashlib.sha256(open('star3_tightN.py','rb').read()).hexdigest(),
                      'mutation':'QS* lower+%d upper-%d; source unchanged on disk'%(SHIFT,SHIFT)}),flush=True)
    pmax=sys.argv[2];detail=sys.argv[3:] 
    sys.argv=['seedXstar3.py','3',pmax,*detail]
    G['main']()
