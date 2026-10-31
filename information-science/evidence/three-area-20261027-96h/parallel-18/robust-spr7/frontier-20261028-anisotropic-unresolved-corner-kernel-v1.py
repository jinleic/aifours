# Resume ONLY Bernstein-capped candidate/corner pairs from the prior exact scan.
# Eval-kernel Fraction arithmetic only, no sampled floats or scientific subprocess.
def locate_strict_failure(poly,max_depth=64,max_nodes=10000):
    beta=[poly[k]/comb(7,k) for k in range(8)]
    todo=[(Q(0),Q(1),beta,0)];count=0
    while todo:
        left,right,coef,depth=todo.pop();count+=1
        for x,value in ((left,coef[0]),(right,coef[-1])):
            if x<1 and value<=0:
                t=x/(1-x)
                exact=sum(poly[k]*t**k for k in range(8))
                if exact!=value/(1-x)**7:raise ValueError('DIRECT_ENDPOINT_MISMATCH')
                return {'status':'NONPOSITIVE_EXACT','x':str(x),'t':str(t),'P':str(exact),'normalized':str(value),'nodes':count}
        if all(c>0 for c in coef):continue
        if depth>=max_depth or count>=max_nodes:return {'status':'UNRESOLVED_CAP','left':str(left),'right':str(right),'nodes':count,'depth':depth}
        b0,b1=halfsplit(coef);mid=(left+right)/2
        todo.extend([(mid,right,b1,depth+1),(left,mid,b0,depth+1)])
    return {'status':'STRICT_POSITIVITY','nodes':count}

aniso_diagnostics=[]
for rec in aniso_report:
    for i,result in enumerate(rec.get('whole_halfline',[])):
        if result['status']=='SUBDIVISION_CAP':
            poly=[Q(x) for x in rec['pairing_polynomials'][i]]
            result=locate_strict_failure(poly)
            aniso_diagnostics.append({'wide':rec['wide'],'narrow_j':rec['narrow_j'],'corner_index':i,'diagnostic':result})
print('anisotropic exact resumed diagnostics:',aniso_diagnostics)
