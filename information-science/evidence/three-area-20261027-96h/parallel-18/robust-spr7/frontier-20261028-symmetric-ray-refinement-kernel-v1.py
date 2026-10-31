# Exact new width-factor checks after loading both prior independent kernels.
# No repeated factor, floating arithmetic, optimizer or author checker is used.
refine_factors=[Q(2003,2000),Q(501,500),Q(4009,4000),Q(4011,4000)]
refine_report=[]
for r in refine_factors:
    mid=[(x+y)/2 for x,y in zip(ray_base_lo,ray_base_hi)]
    rad=[r*(y-x)/2 for x,y in zip(ray_base_lo,ray_base_hi)]
    lo=[x-y for x,y in zip(mid,rad)];hi=[x+y for x,y in zip(mid,rad)]
    cs=corners(lo,hi)
    rst=[routh_ok(a) for a in cs];dst=[integer_hurwitz(a) for a in cs]
    if rst!=dst:raise ValueError('STABILITY_REPLAY_MISMATCH')
    rec={'factor':str(r),'corner_hurwitz':rst,'lower':[str(x) for x in lo],'upper':[str(x) for x in hi]}
    if all(rst):
        rec['pairing_polynomials']=[[str(z) for z in pairing_polynomial(a,ray_b)] for a in cs]
        rec['whole_halfline']=[whole_halfline([Q(x) for x in poly]) for poly in rec['pairing_polynomials']]
    refine_report.append(rec)
print('symmetric ray refinement:',[{'factor':r['factor'],'corner_hurwitz':r['corner_hurwitz'],
    'pairing':[{'status':x['status'],'leaves':len(x.get('leaves',[])), 'margin':x.get('margin'), 'x':x.get('x')} for x in r.get('whole_halfline',[])]} for r in refine_report])
