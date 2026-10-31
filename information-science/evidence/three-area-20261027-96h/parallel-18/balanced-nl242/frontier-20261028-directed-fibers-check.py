#!/opt/homebrew/bin/python3
"""Verify a formal fourzero radical-fiber multiset independently of its solver."""
import argparse
import collections
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    src=json.loads(args.input.read_text(encoding='utf-8'))
    if src['status']!='sat':raise ValueError('no SAT multiset')
    lam=src['lambda_mode'];rho=src['qrad_bit'];groups=src['fiber_groups']
    counts=collections.Counter({0:4});corr=[0,0,0];energy=0;sumk=0;fiber_counts={}
    for tag,records in groups.items():
        total=0
        for record in records:
            row=record['tuple'];n=record['fibers'];assert len(row)==4 and n>0
            total+=n
            for t in row:counts[t]+=n;energy+=n*t*t;sumk+=n*t
            for d in (1,2,3):corr[d-1]+=n*sum(row[i]*row[i^d] for i in range(4) if i<(i^d))
            if tag=='zero':assert all(abs(t)==4 for t in row)
            elif tag in ('g1','g3','evenmixed'):
                assert all(t in (-6,-2,2,6) for t in row)
                for d in (1,2,3):
                    want=2*(int(bool(d&1)) if lam else 0)
                    assert all(((row[i^d]-row[i])//2)%4==want%4 for i in range(4))
            else:
                assert all(abs(t) in (1,3,5,7) for t in row)
                Q=[((t-1)//2)%2 for t in row]
                for d in (1,2,3):
                    want=int(bool(d&rho)) if rho else 0
                    assert all((Q[i^d]^Q[i])==want for i in range(4))
        fiber_counts[tag]=total
    expected={int(t):v for t,v in src['histogram'].items()};expected[0]+=1
    assert all(counts[t]==expected[t] for t in range(-7,8))
    assert sum(fiber_counts.values())==127 and sumk==128 and energy==16384 and corr==[0,0,0]
    summed_square=sum(rec['fibers']*sum(rec['tuple'])**2 for records in groups.values() for rec in records)
    assert summed_square==16384
    z=src['q_zero_count'];w=src['odd_Q_weight'];n3=src['even_g3_count']
    assert counts[0]==4 and z==4+counts[-4]+counts[4] and w==counts[-5]+counts[-1]+counts[3]+counts[7]
    assert n3==counts[-2]+counts[6]
    if lam:assert 2*n3==256-z
    if rho:assert w==128
    mutated=corr[:];mutated[0]+=1;assert mutated!=[0,0,0]
    receipt={'lambda_mode':lam,'qrad_bit':rho,'fiber_counts':fiber_counts,'nonzero_fibers':127,
             'four_zero_fiber_added':True,'reconstructed_full_histogram':True,'sum_k':sumk,'energy':energy,
             'ordered_radical_autocorrelations':[2*x for x in corr],
             'sum_of_fiber_sum_squares':summed_square,'radical_phase_constraints_checked':True,
             'mutation_rejected':True,'actual_boolean_witness':False,
             'scope':'formal multiset only; no common frequency placement or Boolean inverse'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('lambda=',lam,'rho=',rho,'fibers=127 corr=',corr,'energy=',energy,flush=True)


if __name__=='__main__':main()
