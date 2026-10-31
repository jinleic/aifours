from itertools import product
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
S=list(product(range(3),range(5),range(3)))
def sm(a,b):return (a[0],T[T[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
act=lambda a:(a[0],th[a[1]],a[2])
E=[s for s in S if sm(s,s)==s];fib={}
for e in E:fib.setdefault(act(e),[]).append(e)
assert len(S)==45 and len(E)==24 and len(fib)==9
for F in fib.values():
 assert all(sm(x,y) in F for x,y in product(F,repeat=2))
 assert all(sm(sm(x,y),x)==sm(y,x) for x,y in product(F,repeat=2))      # globally right regular
for g in E:
 C=[x for x in E if sm(sm(g,x),g)==x]
 assert all(sm(sm(x,y),x)==sm(y,x) for x,y in product(C,repeat=2))      # right-regular local bands
e,f=(1,1,1),(1,3,1)
assert act(e)==act(f) and sm(e,f)==f and sm(f,e)==e and e!=f
print('PASS S45: 45 elements, 24 idempotents in 9 actor fibres, EVERY fibre a GLOBALLY right regular band; all local bands right regular')
print('PASS same-fibre R-pair',e,f)
