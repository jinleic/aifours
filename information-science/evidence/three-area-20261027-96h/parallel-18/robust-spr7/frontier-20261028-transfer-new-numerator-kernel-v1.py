# Transfer the already independently replayed new numerator to the three other
# actual rational boxes whose old numerator failed. Eval-only exact arithmetic.
transfer_b=[Q(x) for x in frozen_aniso['numerator']]
transfer_report=[]
for rec in aniso_report:
    if rec['wide']!='21/20' or rec['narrow_j'] not in (4,5,6):continue
    lo_case=[Q(x) for x in rec['lower']];hi_case=[Q(x) for x in rec['upper']];cs_case=corners(lo_case,hi_case)
    rs=[routh_ok(a) for a in cs_case];ds=[integer_hurwitz(a) for a in cs_case]
    if rs!=ds or not all(rs):raise ValueError('STABILITY_REPLAY')
    ps=[pairing_polynomial(a,transfer_b) for a in cs_case]
    proofs=[whole_halfline(p) for p in ps]
    for i,proof in enumerate(proofs):
        if proof['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i])
    success=all(x['status']=='STRICT_POSITIVITY' and 'leaves' in x for x in proofs)
    if success:
        for p,proof in zip(ps,proofs):verify_leaves_by_power(p,proof)
    transfer_report.append({'wide':rec['wide'],'narrow_j':rec['narrow_j'],'lower':rec['lower'],'upper':rec['upper'],
      'corner_hurwitz':rs,'pairing_polynomials':[[str(x) for x in p] for p in ps],'proofs':proofs,
      'status':'COMMON_NUMERATOR_PROVED' if success else 'NOT_CERTIFIED',
      'margin':str(min(Q(x['margin']) for x in proofs)) if success else None})
print('exact numerator transfer:',[{'narrow_j':r['narrow_j'],'status':r['status'],'margin':r['margin'],
 'proofs':[{'status':x['status'],'failure_t':x.get('t')} for x in r['proofs']]} for r in transfer_report])
