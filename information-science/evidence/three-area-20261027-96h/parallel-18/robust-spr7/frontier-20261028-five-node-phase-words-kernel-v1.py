# Exact generic five-node phase-class table. Run only in Python Eval.
# This enumerates abstract sign/phase labels, not polynomial boxes or frequencies.
from itertools import product as spr5_product
spr5_states=('++','-+','--','+-','++','-+','--')
spr5_alt=(1,-1,1,-1,1)
spr5_words=[]
for pE in range(6):
    for pO in range(6):
        signs=[]
        for j in range(5):
            e=spr5_alt[j]*(-1 if j<pE else 1)
            o=spr5_alt[j]*(-1 if j<pO else 1)
            signs.append(('+' if e>0 else '-')+('+' if o>0 else '-'))
        choices=[[q for q in range(7) if spr5_states[q]==sgn] for sgn in signs]
        for q in spr5_product(*choices):
            if all(q[i]<=q[j]+1 for i in range(5) for j in range(i+1,5)):
                spr5_words.append((pE,pO,tuple(signs),q))
print('all monotone-threshold class pairs:',36)
print('surviving exact phase words:',spr5_words)
