#!/usr/bin/env python3
"""Exact exponent check for affine-coordinate/chirp symmetries of I,U,D5U."""
count=0
for c in range(1,5):
 for d in range(5):
  eta=0 if c*c%5==1 else 4
  images=[]
  for q in (0,4):
   qp=(eta+q*c*c)%5;images.append(qp)
   js=[]
   for j in range(5):
    jp=(2*q*c*d+3*c*j)*2%5
    const=(q*d*d+3*d*j)%5
    js.append(jp)
    for t in range(5):
     lhs=eta*t*t+q*(c*t+d)**2+3*(c*t+d)*j
     rhs=qp*t*t+3*t*jp+const
     assert (lhs-rhs)%5==0;count+=1
   assert len(set(js))==5
  assert set(images)=={0,4}
print('PASS',count,'exact coordinate exponent identities for all c,d,q,j,t')
print('Each affine-coordinate/chirp map preserves I and permutes the two Fourier/chirp bases.')
