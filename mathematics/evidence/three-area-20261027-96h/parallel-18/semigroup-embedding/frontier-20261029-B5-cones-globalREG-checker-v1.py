from itertools import product
# x=0,u0=1,u1=2,v0=3,v1=4; this IS a band, not the separate five-element nonband A.
B=[[0,3,4,3,4],[0,1,1,3,4],[0,2,2,3,4],[0,3,3,3,4],[0,4,4,3,4]]
def reg(x,y,z):return B[B[B[B[x][y]][x]][z]][x]==B[B[B[x][y]][z]][x]
assert all(B[x][x]==x and B[x][0]==0 for x in range(5))
assert all(B[B[x][y]][z]==B[x][B[y][z]] for x,y,z in product(range(5),repeat=3))
assert all(B[B[B[B[x][y]][z]][w]][x]==B[B[B[B[B[B[x][y]][z]][x]][z]][w]][x] for x,y,z,w in product(range(5),repeat=4))
cones=[]
for e in range(5):
 low=[f for f in range(5) if B[e][f]==B[f][e]==f];up=[f for f in range(5) if B[e][f]==B[f][e]==e]
 for C in (low,up):
  assert all(B[x][y] in C for x,y in product(C,repeat=2))
  assert all(reg(x,y,z) for x,y,z in product(C,repeat=3))
 assert set(low)=={B[B[e][s]][e] for s in range(5)}
 cones.append({'e':e,'lower':low,'upper':up})
assert not reg(1,0,2)
print('PASS B5 band,125associativity,625SN; rightzero x=0 forces ANYsource-to-LZ mapconstant')
print('PASS EVERYlowercorner andEVERYuppercone isGLOBALREG',cones)
print('FAIL globalREG at(x,y,z)=(1,0,2):xyxzx=',B[B[B[B[1][0]][1]][2]][1],'xyzx=',B[B[B[1][0]][2]][1])
print('RESULT newcanonicalROW necessaryconditionexcludes idsepimages withGLOBALREGband despite BOTHlocalcorner anduppercone GLOBALREGtests passing; SNhostB5itselfpositive')
