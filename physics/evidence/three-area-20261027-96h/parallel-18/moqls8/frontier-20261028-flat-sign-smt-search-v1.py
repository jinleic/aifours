#!/usr/bin/env python3
"""Bounded 4-MOQLS(8) search over real flat sign rays with a fixed first row.

SAT is meaningful only after exact full-Gram verification of the returned
actual arrays. UNSAT/UNKNOWN concerns this restricted model and is not an
unrestricted theorem. Uses z3 CLI with explicit time and memory bounds.
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import time

N=8
M=4


def gf8mul(a,b):
    ans=0
    for _ in range(3):
        if b&1: ans^=a
        b>>=1;a<<=1
        if a&8:a^=11
    return ans


def walsh_ray(label):
    return sum((1 << (x-1)) for x in range(1,8) if (label & x).bit_count() & 1)


def gram8(a,b):
    return 8-2*(a^b).bit_count()


def physical_errors(arr):
    row=col=pair=0
    for a in range(M):
        for line in range(N):
            for j in range(N):
                for k in range(N):
                    want=8 if j==k else 0
                    row += gram8(arr[a][line][j],arr[a][line][k]) != want
                    col += gram8(arr[a][j][line],arr[a][k][line]) != want
    for a in range(M):
        for b in range(a+1,M):
            for x in range(N*N):
                i,j=divmod(x,N)
                for y in range(N*N):
                    k,l=divmod(y,N)
                    want=64 if x==y else 0
                    pair += gram8(arr[a][i][j],arr[a][k][l])*gram8(arr[b][i][j],arr[b][k][l]) != want
    return {'row_gram_errors':row,'column_gram_errors':col,'pair_product_gram_errors':pair}


def bvadd(terms):
    out=terms[0]
    for term in terms[1:]:out=f'(bvadd {out} {term})'
    return out


def q(a,i,j):return f'q_{a}_{i}_{j}'


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prefix',required=True);args=ap.parse_args()
    prefix=pathlib.Path(args.prefix)
    if not prefix.name.startswith('frontier-20261028-'):
        raise ValueError('output prefix must be own frontier artifact')
    start=time.monotonic()
    baseline=[[[walsh_ray(gf8mul(a+1,i)^j) for j in range(N)] for i in range(N)] for a in range(M)]
    good=physical_errors(baseline)
    if any(good.values()):raise ValueError(f'classical control failed {good}')
    bad=[[row[:] for row in square] for square in baseline];bad[1]=[row[:] for row in bad[0]]
    negative=physical_errors(bad)
    if negative['row_gram_errors'] or negative['column_gram_errors'] or not negative['pair_product_gram_errors']:
        raise ValueError(f'pair-product negative control failed {negative}')
    lines=['(set-logic QF_BV)','(set-option :produce-models true)']
    bits=[f'((_ zero_extend 3) ((_ extract {k} {k}) t))' for k in range(7)]
    lines.append('(define-fun hd ((x (_ BitVec 7)) (y (_ BitVec 7))) (_ BitVec 4) (let ((t (bvxor x y))) '+bvadd(bits)+'))')
    lines.append('(define-fun ortho ((x (_ BitVec 7)) (y (_ BitVec 7))) Bool (= (hd x y) (_ bv4 4)))')
    for a in range(M):
        for i in range(N):
            for j in range(N):
                lines.append(f'(declare-fun {q(a,i,j)} () (_ BitVec 7))')
                if i==0:lines.append(f'(assert (= {q(a,i,j)} (_ bv{walsh_ray(j)} 7)))')
    line_assertions=0
    for a in range(M):
        for line in range(N):
            for j in range(N):
                for k in range(j+1,N):
                    lines.append(f'(assert (ortho {q(a,line,j)} {q(a,line,k)}))')
                    lines.append(f'(assert (ortho {q(a,j,line)} {q(a,k,line)}))')
                    line_assertions+=2
    pair_assertions=0
    for a in range(M):
        for b in range(a+1,M):
            for x in range(N*N):
                i,j=divmod(x,N)
                for y in range(x+1,N*N):
                    k,l=divmod(y,N)
                    if i==k or j==l:continue
                    lines.append(f'(assert (or (ortho {q(a,i,j)} {q(a,k,l)}) (ortho {q(b,i,j)} {q(b,k,l)})))')
                    pair_assertions+=1
    # Hamming distance2 or6 from the first basis ray gives |overlap|=1/2.
    lines.append(f'(assert (or (= (hd {q(0,0,0)} {q(0,1,1)}) (_ bv2 4)) (= (hd {q(0,0,0)} {q(0,1,1)}) (_ bv6 4))))')
    lines.append('(check-sat)')
    lines.append('(get-value ('+' '.join(q(a,i,j) for a in range(M) for i in range(N) for j in range(N))+'))')
    script='\n'.join(lines)+'\n'
    script_path=prefix.with_name(prefix.name+'-input.smt2')
    with script_path.open('x',encoding='utf-8') as h:h.write(script)
    script_sha=hashlib.sha256(script_path.read_bytes()).hexdigest()
    cmd=['z3','-T:15','-memory:768','-smt2',str(script_path)]
    try:
        process=subprocess.run(cmd,capture_output=True,text=True,timeout=20,check=False)
        stdout,stderr,exitcode=process.stdout,process.stderr,process.returncode
        outer_timeout=False
    except subprocess.TimeoutExpired as exc:
        stdout=exc.stdout.decode() if isinstance(exc.stdout,bytes) else (exc.stdout or '')
        stderr=exc.stderr.decode() if isinstance(exc.stderr,bytes) else (exc.stderr or '')
        exitcode=None;outer_timeout=True
    stdout_path=prefix.with_name(prefix.name+'-z3-stdout.txt')
    stderr_path=prefix.with_name(prefix.name+'-z3-stderr.txt')
    with stdout_path.open('x',encoding='utf-8') as h:h.write(stdout)
    with stderr_path.open('x',encoding='utf-8') as h:h.write(stderr)
    first=stdout.splitlines()[0].strip() if stdout.splitlines() else ''
    outcome='INCOMPLETE'
    candidate_sha=None;model_errors=None;target_hamming=None
    if first=='sat':
        matches=re.findall(r'\((q_\d+_\d+_\d+)\s+(#b[01]+|\(_ bv\d+ 7\))\)',stdout)
        values={name:(int(raw[2:],2) if raw.startswith('#b') else int(re.search(r'bv(\d+)',raw).group(1))) for name,raw in matches}
        if len(values)==M*N*N:
            arr=[[[values[q(a,i,j)] for j in range(N)] for i in range(N)] for a in range(M)]
            model_errors=physical_errors(arr)
            target_hamming=(arr[0][0][0]^arr[0][1][1]).bit_count()
            first_rows_ok=all(arr[a][0][j]==walsh_ray(j) for a in range(M) for j in range(N))
            if not any(model_errors.values()) and target_hamming in (2,6) and first_rows_ok:
                candidate_path=prefix.with_name(prefix.name+'-candidate.json')
                with candidate_path.open('x',encoding='utf-8') as h:
                    json.dump({'encoding':'8 signs per ray, first +, other 7 encoded in bit mask','ray_masks':arr,
                               'physical_errors':model_errors,'target_hamming':target_hamming},h,indent=2);h.write('\n')
                candidate_sha=hashlib.sha256(candidate_path.read_bytes()).hexdigest()
                outcome='SAT_MODEL_EXACT_FULL_GRAM_VERIFIED_NEEDS_INDEPENDENT_WITNESS_REVIEW'
            else:outcome='SAT_MODEL_REJECTED_BY_DIRECT_FULL_GRAM'
        else:outcome='SAT_MODEL_PARSE_INCOMPLETE'
    elif first=='unsat':outcome='UNSAT_RESTRICTED_FORMULA_SOLVER_RESULT_NO_CERTIFICATE_CHECKED'
    elif first=='unknown':outcome='UNKNOWN_RESTRICTED_FORMULA'
    elif first=='timeout' or outer_timeout:outcome='TIMEOUT_RESTRICTED_FORMULA'
    report={'result':outcome,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':script_sha,'stdout_sha256':hashlib.sha256(stdout_path.read_bytes()).hexdigest(),
            'stderr_sha256':hashlib.sha256(stderr_path.read_bytes()).hexdigest(),
            'z3_argv':cmd,'z3_exit':exitcode,'outer_timeout':outer_timeout,
            'solver_first_line':first,'line_orthogonality_assertions':line_assertions,
            'off_line_pair_product_assertions':pair_assertions,
            'classical_control_errors':good,'duplicate_square_control_errors':negative,
            'model_full_gram_errors':model_errors,'model_target_hamming':target_hamming,
            'candidate_sha256':candidate_sha,'elapsed_seconds':time.monotonic()-start,
            'limits':'Real flat sign-ray subclass, fixed Sylvester first row and one selected intermediate overlap. No global conclusion. SAT candidate needs independent triple verification.'}
    receipt=prefix.with_name(prefix.name+'-receipt.json')
    with receipt.open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
