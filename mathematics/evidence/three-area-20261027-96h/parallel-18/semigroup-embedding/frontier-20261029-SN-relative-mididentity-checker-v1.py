from itertools import product
B=[[0,3,4,3,4],[0,1,1,3,4],[0,2,2,3,4],[0,3,3,3,4],[0,4,4,3,4]]
def reg(x,y,z):return B[B[B[B[x][y]][x]][z]][x]==B[B[B[x][y]][z]][x]
assert all(B[B[B[B[a][b]][c]][d]][a]==B[B[B[B[B[B[a][b]][c]][a]][c]][d]][a] for a,b,c,d in product(range(5),repeat=4))
rows=[]
for p in range(5):
 Cp={B[b][p] for b in range(5)};pC={B[p][b] for b in range(5)}
 for I in (Cp,pC):
  assert all(B[b][c] in I for b,c in product(I,repeat=2))
  assert all(reg(a,b,c) for a,b,c in product(I,repeat=3))
 # p is a left identity, hence relative mididentity, for the subband pC.
 assert all(B[p][b]==b for b in pC)
 image={b:(B[b][p],B[p][b]) for b in pC};assert len(set(image.values()))==len(pC)
 assert all(image[B[b][c]]==(B[image[b][0]][image[c][0]],B[image[b][1]][image[c][1]]) for b,c in product(pC,repeat=2))
 bad=next((b,c) for b,c in product(range(5),repeat=2) if B[B[b][p]][c]!=B[b][c])
 rows.append({'p':p,'Cp':sorted(Cp),'pC':sorted(pC),'whole_B5_mididentity_failure':bad})
assert not reg(1,0,2)
print('PASS all TENprincipalone-sidedidealsofSN B5 areGLOBALREG',rows)
print('PASS eachproperrightideal pC hasleftunit/relativeMIDunit p anditsmaptoCp×pC isinjectivehom')
print('PASS WHOLEB5 notGLOBALREG andnoexistingmidunit; NOexternalSNmidunitcomesfromWRITTENuniversaltheorem,notfiniteenumeration')
