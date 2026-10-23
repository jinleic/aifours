#!/usr/bin/env python3
"""[F] Arithmetic controls only for proof-QF.md: the three finishers cover every NMH parameter tuple with quality seeds.
No seed-existence claim is made. This does not enumerate words or prove RUNS.
"""
import json,time
G={'__name__':'seedX2lib'}
exec(compile(open('seedX2.py').read().replace("if __name__ == '__main__':\n    main()",''),'seedX2.py','exec'),G)
stat={'classes':0,'B<=g_C0B':0,'B>g_C0W':0,'B>g_Cplus':0}
t=time.time()
for p in range(5,258):
    if not G['isprime'](p):continue
    for k,kap,B in G['classes'](p):
        g=kap-B;E=2*p-2*k+2*kap
        assert kap+E//2<=p-3
        if B<=g:
            assert k>=g+3*B
            stat['B<=g_C0B']+=1
        elif 3*g+1<=p:stat['B>g_C0W']+=1
        else:
            assert 2*g<=p
            assert E<=2*(k-g-2*B)-1
            stat['B>g_Cplus']+=1
        stat['classes']+=1
print(json.dumps(stat),flush=True)
print(json.dumps({'seconds':round(time.time()-t,2)}),flush=True)
