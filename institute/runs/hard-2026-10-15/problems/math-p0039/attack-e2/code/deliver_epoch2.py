#!/usr/bin/env python3
"""Publish scoped claims atomically from completed evidence only.
No scanner is launched, imported, or executed. Oversized arithmetic sample
logs receive deterministic gzip companions for the delivery-limited snapshot.
"""
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path


def load(path):return json.loads(Path(path).read_text())


def claim(cid,statement,kind,scope,evidence,verify='',check='',control=''):
    return dict(cid=cid,statement=statement,type=kind,scope=scope,evidence=evidence,
                verify_command=verify,check_command=check,control_command=control)


def completed(task):
    path=Path('evidence/epoch2/'+task+'-comparison.json')
    return load(path) if path.exists() else None


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');args=parser.parse_args()
    e2=Path('evidence/epoch2');(e2/'prefix-groups').mkdir(exist_ok=True)
    compressed=[]
    for task in ('main','extension'):
        if not completed(task):continue
        for exe in ('scan128_digest','scan32'):
            p=Path('logs/e2-'+task+'-'+exe+'.records.jsonl')
            target=Path(str(p)+'.gz')
            if p.is_file() or target.is_file():
                raw=p.read_bytes() if p.is_file() else gzip.decompress(target.read_bytes())
                if p.is_file():
                    target.write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
                    assert gzip.decompress(target.read_bytes())==raw,'compression changed log bytes'
                    p.unlink() # reversible byte-exact gzip is the delivered production log
                compressed.append(dict(path=str(target),raw_bytes=len(raw),
                                       raw_sha256=hashlib.sha256(raw).hexdigest(),
                                       compressed_bytes=target.stat().st_size,
                                       compressed_sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
    if compressed:(e2/'compressed-log-integrity.json').write_text(json.dumps(compressed,indent=2)+'\n')
    inherited=load(e2/'inherited-claims.json')['claims'];claims=[]
    for c in inherited:
        if c['cid'] not in ('isolated-controls','closure-lemma','power-two-family','fixed-filter-limit'):continue
        if c['cid']=='isolated-controls':c['verify_command']='python3 code/check_controls.py';c['check_command']=''
        if c['cid']=='closure-lemma':c['statement']+=' Likely prior art includes Hall (1947), Cyclic projective planes, and successors; no priority conclusion is made.'
        if c['cid']=='power-two-family':c['statement']+=' These witnesses probably reproduce known Cunningham-type factorizations.'
        claims.append(c)
    claims.extend([
      claim('wide-arithmetic-vectors',
            'The two retained C backends match all 960 exact full-residue vectors, including 90 synthetic positive vectors at 65-94-bit odd moduli. Python manual exponentiation rechecks every stored residue. These are finite arithmetic controls, not natural plane-shaped survivors or a general-range proof.',
            'computation','related',['evidence/epoch2/vectors.json','evidence/epoch2/build.json','code/check_epoch2.py'],
            'python3 code/check_epoch2.py vectors',control='python3 code/check_epoch2.py vectors --broken'),
      claim('proper-factor-control',
            'Every one of 9999 even orders in [2,20000) has its actual sieve factor and complete ordinary power residue rechecked by Python trial division and exact powers. A separate Cipolla-root replay matches both C decision digests. A divisor q is accepted only when 1<q<p; prime controls are not sieved by themselves. This is a small-order control only.',
            'computation','related',['logs/e2-tiny-scan32.blocks.jsonl','logs/e2-tiny-scan128_digest.blocks.jsonl',
             'logs/e2-tiny-scan32.records.jsonl','logs/e2-tiny-scan128_digest.records.jsonl',
             'evidence/epoch2/tiny-comparison.json','code/check_epoch2.py','evidence/negative-self-factor.json'],
            'python3 code/check_epoch2.py samples --task tiny',
            'python3 code/check_epoch2.py blocks --task tiny --blocks 0',
            control='python3 code/check.py single evidence/negative-self-factor.json'),
      claim('published-control-interval-rerun',
            'Two new unsieved C runs report exactly 2,8,24,90,512,134217728,297474474 among all 2499999999 even orders in [2,5000000000). Their full-residue block digests agree for every order, and their binary hashes are in their headers. Python rechecks 1384 recorded full residues only. This control covers the unsieved small-modulus path (p<2^65), not the main sieve or full main-range arithmetic; entire control executions are not replayed in Python.',
            'evidence','related',['evidence/epoch2/controls-comparison.json','evidence/epoch2/controls-log-check.json',
             'evidence/epoch2/controls-sample-check.json','logs/e2-controls-scan32.blocks.jsonl',
             'logs/e2-controls-scan128_digest.blocks.jsonl','logs/e2-controls-scan32.records.jsonl',
             'logs/e2-controls-scan128_digest.records.jsonl','code/check_epoch2.py','evidence/epoch2/build.json'],
            'python3 code/check_epoch2.py compare --task controls',
            'python3 code/check_epoch2.py samples --task controls',
            'python3 code/check_epoch2.py compare --task controls --broken')])
    main_result=completed('main');ext_result=completed('extension');production_end=None
    survivor_scopes=[]
    for task,result in (('main',main_result),('extension',ext_result)):
        if result is None:continue
        start=200000000000 if task=='main' else 2000000000000
        if task=='extension':assert main_result and main_result['end']==start
        assert result['hits']==[]
        audit=load('evidence/epoch2/'+task+'-sample-check.json')
        survivor_scopes.append(dict(task=task,start=start,stop=result['end'],
            logged_unsieved_base_two_survivors=[],exact_eliminations=[],unresolved_logged_candidates=[],
            limitation='Zero rows are a preserved execution report outside the complete Python prefix.'))
        production_end=result['end']
        evidence=['evidence/PREMISES.md','evidence/epoch2/'+task+'-comparison.json',
                  'evidence/epoch2/'+task+'-log-check.json','evidence/epoch2/'+task+'-sample-check.json',
                  'evidence/epoch2/compressed-log-integrity.json','evidence/epoch2/build.json',
                  'code/scan32.c','code/scan128_digest.c','code/check_epoch2.py','evidence/epoch2/survivors.json']
        for exe in ('scan128_digest','scan32'):
            evidence.extend(['logs/e2-'+task+'-'+exe+'.blocks.jsonl',
                             'logs/e2-'+task+'-'+exe+'.records.jsonl.gz',
                             'evidence/epoch2/'+task+'-'+exe+'-run.json'])
        claims.append(claim('paired-'+task+'-production',
            'Two preserved C executions with different modular multiplication (three radix-2^32 limbs versus two radix-2^64 limbs) and different root algorithms report zero unsieved base-two survivors for n=8 mod 24 in [%d,%d). Their decision hashes agree in every one of %d consecutive common blocks, covering %d members. EVERY decision hashes the actual factor or the complete ordinary residue of an unsieved power; factor records explicitly have an uncomputed residue. Assuming the imported premises AND correctness of these executions, these orders are excluded. Python-only replay fully checks only the separately claimed prefix blocks and recorded samples; it does not certify this entire production interval. Both programs share author, compiler, OS, exponentiation recurrence, and hashing implementation.'
            %(start,result['end'],result['blocks'],result['count'])+
            ' Python rechecks exactly %d recorded samples (%d factor, %d unsieved), including %d contiguous windows; every sampled factor member also has a complete power residue checked.'
            %(audit['arithmetic_records'],audit['factor_records'],audit['unsieved_records'],len(audit['contiguous_windows'])),
            'evidence','sub-question',evidence,
            'python3 code/check_epoch2.py compare --task '+task,
            'python3 code/check_epoch2.py samples --task '+task,
            'python3 code/check_epoch2.py compare --task '+task+' --broken'))
    prefix_end=200000000000;groups=[]
    for group in range(8):
        file=e2/'prefix-groups'/('%02d.json'%group)
        if not file.exists():break
        row=load(file);expected_ids=list(range(group*32,(group+1)*32))
        assert row['task']=='main' and row['backend']=='pow'
        assert row['base_two_survivors']==[],'prefix has an unresolved hit'
        assert [b['block'] for b in row['blocks']]==expected_ids
        start=200000000000+24*8388608*expected_ids[0]
        end=200000000000+24*8388608*(expected_ids[-1]+1)
        assert start==prefix_end and row['blocks'][0]['start']==start and row['blocks'][-1]['end']==end
        assert row['fully_recomputed_members']==32*8388608
        prefix_end=end;groups.append(group)
        command='python3 code/check_epoch2.py blocks --task main --blocks '+','.join(map(str,expected_ids))
        claims.append(claim('python-prefix-%02d'%group,
            'For every n=8 mod 24 in [%d,%d), an exact proper factor of p=n^2+n+1 or a complete base-two residue different from 1 eliminates the candidate. All %d decisions were recomputed by Python with Cipolla root derivation and arbitrary-precision pow and matched both C block digests. This verify command itself is the separate arithmetic replay; no additional independent checker is claimed. Conditional on the imported geometric premises, only these orders are excluded.'
            %(start,end,row['fully_recomputed_members']),
            'computation','sub-question',[str(file),'evidence/PREMISES.md','code/check_epoch2.py',
             'logs/e2-main-scan32.blocks.jsonl','logs/e2-main-scan128_digest.blocks.jsonl'],
            command,control='python3 code/check_epoch2.py blocks --task main --blocks 0 --broken' if group==0 else ''))
    if not groups and (e2/'benchmark-all-pow.json').exists():
        row=load(e2/'benchmark-all-pow.json');prefix_end=row['blocks'][-1]['end']
        claims.append(claim('fresh-benchmark-prefix',
            'Every candidate n=8 mod 24 in [200000000000,%d) is eliminated by an exact proper factor or a complete base-two residue different from 1. Python independently recomputed all 67108864 decisions and matched both C digests. No other orders are certified by this claim.'%prefix_end,
            'computation','sub-question',['evidence/epoch2/benchmark-all-pow.json','code/check_epoch2.py',
             'logs/e2-benchmark-scan32.blocks.jsonl','logs/e2-benchmark-scan128_digest.blocks.jsonl','evidence/PREMISES.md'],
            'python3 code/check_epoch2.py blocks --task benchmark --blocks 0,1,2,3,4,5,6,7',
            control='python3 code/check_epoch2.py blocks --task benchmark --blocks 0 --broken'))
    (e2/'survivors.json').write_text(json.dumps(dict(
        row_fields=['n','p','exact_elimination_reason','witness'],production_scopes=survivor_scopes,
        complete_python_prefix=dict(start=200000000000,stop=prefix_end,base_two_survivors=[],unresolved=[]),
        isolated_controls='evidence/controls.json',
        rule='A future unresolved base-two survivor prevents the exclusion claim; probable primality is never elimination.'),indent=2)+'\n')
    claims.append(claim('inherited-entire-range-report',
        'One inherited C run reports no unsieved base-two survivor for n=8 mod 24 in [200000000000,10341223092224). Its entire reported range remains unreplicated. Conditional on the imported premises AND on that single entire-range execution being correct, it gives n<10341223092224. Reconstructed logs match the staged recovery manifest; hashes establish integrity, and sieved+tested counts are bookkeeping. New paired runs and Python replay corroborate only their explicitly stated subsets. No binary hash in the old log header links that run to a retained executable.',
        'evidence','sub-question',['evidence/result.json','evidence/PREMISES.md','code/recheck.py','code/recover_logs.py',
         'code/verify_result.py','selection-inputs/first-attempt-logs/MANIFEST.json']+
         [str(p) for p in sorted(Path('selection-inputs/first-attempt-logs').glob('*.gz'))],
        'python3 code/recheck.py main-metadata'))
    if (e2/'MOMENT-CRITERION.md').exists():
        claims.append(claim('finite-moment-reformulation',
            'For even n>2 and prime p=n^2+n+1, D=mu_(n+1) is planar if and only if sum_j (-1)^j binom(t(n+1),j(n+1)) is 0 mod p for every even t in [2,n-2]. This follows by finite-field power sums and an invertible Vandermonde matrix. It supplies no all-orders inconsistency proof, is not used to skip scan members, and is likely a classical cyclotomic criterion; novelty is unknown.',
            'theorem','related',['evidence/epoch2/MOMENT-CRITERION.md']))
    boundary_path=e2/'boundary-window.json';boundary_row='';boundary_text=''
    if boundary_path.exists():
        boundary=load(boundary_path);assert boundary['base_two_survivors']==[]
        evidence=[str(boundary_path),'code/check_boundary_epoch2.py','code/check_epoch2.py',
                  'evidence/PREMISES.md','logs/e2-main-scan32.blocks.jsonl',
                  'logs/e2-main-scan128_digest.blocks.jsonl','logs/e2-extension-scan32.blocks.jsonl',
                  'logs/e2-extension-scan128_digest.blocks.jsonl']
        for exe in ('scan128_digest','scan32'):
            raw='logs/e2-extension-'+exe+'.records.jsonl'
            evidence.append(raw+'.gz' if Path(raw+'.gz').exists() else raw)
        claims.append(claim('wide-boundary-window',
            'Every n=8 mod24 in [1999859732480,2000201326592) is eliminated by an exact proper factor or full base-two residue different from 1. Python completely recomputed all 14233088 decisions across main block8940 and extension block0, matching both C digests. At n=2000000000000 it also checked the complete ordinary residue and the actual proper factor7. This separated window does not enlarge the general contiguous prefix or certify any omitted order.',
            'computation','sub-question',evidence,'python3 code/check_boundary_epoch2.py',
            control='python3 code/check_boundary_epoch2.py --broken'))
        boundary_row='| Complete Python boundary window | [1999859732480,2000201326592) | Separate window; no general-bound increase |\n'
        boundary_text=('A further complete Python replay covers all 14,233,088 decisions in the '
                       'separated window [1999859732480,2000201326592), joining the last target block '
                       'to the first continuation block without gap or overlap. The actual divisor 7 '
                       'and full ordinary residue at n=2000000000000 are checked against both '
                       'arithmetic logs. This does not fill the large gap after the general prefix. '
                       'See evidence/epoch2/boundary-window.json and its independent replay command.')
    power_path=e2/'power-boundary.json';power_row='';power_text=''
    if power_path.exists():
        power=load(power_path);record=power['blocks'][0]
        a=2000000000000+24*988*8388608;z=a+24*8388608
        assert power['base_two_survivors']==[] and power['backend']=='pow'
        assert record['block']==988 and record['start']==a and record['end']==z and a<2**41<z
        claims.append(claim('exponent-boundary-window',
            'Every n=8 mod24 in [%d,%d) is eliminated by an exact proper factor or complete base-two residue different from 1. Python recomputed every one of the 8388608 decisions in extension block988 and matched both C digests. This block contains n=2^41, where the natural exponent and modulus gain a bit. It is a separated audit window and does not enlarge the general prefix.'%(a,z),
            'computation','sub-question',[str(power_path),'code/check_epoch2.py','evidence/PREMISES.md',
             'logs/e2-extension-scan32.blocks.jsonl','logs/e2-extension-scan128_digest.blocks.jsonl'],
            'python3 code/check_epoch2.py blocks --task extension --blocks 988',
            control='python3 code/check_epoch2.py blocks --task extension --blocks 988 --broken'))
        power_row='| Complete Python bit-boundary block | [%d,%d) | Separate window; no general-bound increase |\n'%(a,z)
        power_text=('Python also completely rechecked all 8,388,608 decisions in [%d,%d), '
                    'the block containing n=2^41. This tests the transition from 41- to 42-bit '
                    'exponents and from 82- to 83-bit natural moduli. Both C digests matched. '
                    'It is a second separated window, not a general-bound increase.'%(a,z))
    # Fail fast on all cheap integrity/control tasks before expensive replays.
    claims.sort(key=lambda c:c['cid'].startswith('python-prefix-'))
    extra_table_rows='\n'.join(row.rstrip('\n') for row in (boundary_row,power_row) if row)
    for c in claims:
        for f in c['evidence']:assert Path(f).is_file(),'missing evidence '+f
    from check import schema_validate
    summary=('Partial only. The all-orders flag-transitive-plane conjecture is unresolved. '
             'Complete Python replay excludes counterexample orders n<%d under the imported premises. '%prefix_end)
    if production_end:summary+='Two arithmetic implementations report matching decision digests through n<%d, conditional on their correct executions; that entire interval is not Python-replayed. '%production_end
    summary+='The inherited endpoint 10341223092224 still rests on one entire-range run. Novelty is unknown.'
    data=dict(outcome='partial',summary=summary,claims=claims,
              next_step='Obtain a fully replayable certificate or an external exhaustive reexecution for the remaining paired-production decisions. A universal solution needs a mathematical obstruction beyond fixed finite sieves and necessary power congruences. No continuation is scheduled.')
    schema_validate(data,load('claims.schema.json'))
    tmp=Path('claims.json.tmp');tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace('claims.json')
    replay_path=e2/'snapshot-replay.json';replay=load(replay_path) if replay_path.exists() else None
    expected_commands=[(c['cid'],field,c[field]) for c in claims
                       for field in ('verify_command','check_command','control_command') if c[field]]
    replay_complete=bool(replay and replay.get('all_passed') and all(r['passed'] for r in replay['commands'])
                         and replay['total_command_seconds']<=1800 and replay['max_command_seconds']<=300
                         and [(r['cid'],r['field'],r['command']) for r in replay['commands']]==expected_commands)
    if args.final:assert replay_complete,'final claim set has not passed its delivery-copy replay'
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    state=dict(updated_utc=now,phase='complete' if args.final else 'in-progress',outcome='partial',
               headline_resolved=False,python_exact_prefix_end=prefix_end,prefix_groups=groups,
               paired_production_end=production_end,inherited_entire_range_end=10341223092224,
               entire_paired_range_python_replayed=False,claims=len(claims),novelty='unknown')
    (e2/'status.json').write_text(json.dumps(state,indent=2)+'\n')
    production_text='The target scan is still in progress. No completed target endpoint is currently asserted.'
    audit_rows=[]
    for task,result in (('main',main_result),('extension',ext_result)):
        path=e2/(task+'-sample-check.json')
        if result is not None and path.exists():
            audit=load(path)
            audit_rows.append('| %s | %d | %d / %d | %d |'%(task,audit['arithmetic_records'],
                audit['factor_records'],audit['unsieved_records'],len(audit['contiguous_windows'])))
    audit_text='No completed target-sample audit is yet published.'
    if audit_rows:
        audit_text=('| Scope | Sample records | Factor / unsieved | Contiguous windows |\n'
                    '|---|---:|---:|---:|\n'+'\n'.join(audit_rows)+
                    '\n\nEvery block contributes its first two and last two members. Every 128th '
                    'block contributes its first 64 members, and a completed planned final block '
                    'also contributes its first 64. Every member of those windows, including '
                    'factor rejections, has its full ordinary power and actual smallest divisor '
                    'recomputed and included in a window hash. These samples partially overlap '
                    'the full Python prefix and do not certify the gaps between windows. We retain '
                    'the declared prefix at its complete-block boundary. Exact endpoints, '
                    'counts and full-residue hashes are in the sample-check JSON files.')
    if main_result:
        production_text=('Two preserved runs report no unsieved base-two survivor on n=8 (mod 24) in '
                         '[200000000000,%d). Their complete decision digests agree over %d target blocks '
                         'and %d target members. '%(main_result['end'],main_result['blocks'],main_result['count']))
        if ext_result:production_text+='A capped continuation agrees through %d over %d further common blocks. '%(ext_result['end'],ext_result['blocks'])
        production_text+=('Assuming the imported premises **and correctness of these executions**, the combined order '
                          'exclusion for non-Desarguesian flag-transitive planes is n<%d. This is a preserved computational report, not a full Python replay or '
                          'independent certification of that entire interval.'%production_end)
    replay_text='The delivery-copy replay has not yet been run for the final claim set.'
    extra_factor_text=''
    factor_attempt=e2/'factor-59049-extended.json'
    if factor_attempt.exists():
        attempt=load(factor_attempt)
        if 'result' in attempt and not attempt['result']['proper_factor']:
            extra_factor_text=('A supplementary 300-second search stopped at q=%d without a factor; '
                               'the planned 10^15 bound was not exhausted. It gives no primality conclusion.'
                               %attempt['result']['last_q'])
    if replay_complete:
        replay_text=('The final claim commands were run on an actual delivery-limited copy: %d commands, '
                     '%.3f seconds summed wall time, longest command %.3f seconds. All required successes and '
                     'deliberate nonzero failures were observed. This is a self-run delivery replay, not an external '
                     'referee verdict. The tested copy contained %d files totaling %d bytes; the three skipped '
                     'oversized inherited logs were reconstructed from their delivered gzip parts. '
                     'See evidence/epoch2/snapshot-replay.json.'
                     %(len(replay['commands']),replay['total_command_seconds'],replay['max_command_seconds'],
                       replay['package']['files'],replay['package']['bytes']))
    report=f'''# math-p0039 — bounded research continuation

**Outcome: partial. The all-orders conjecture is neither proved nor refuted here. Novelty is unknown.**

Question: Does every finite flag-transitive projective plane have to be Desarguesian?
Under the imported reduction, the target is to exclude the planar difference set
mu_(n+1) in F_p for every n>8 with p=n²+n+1 prime. No universal exclusion or
counterexample plane was found.

## Results and exact scopes

| Evidence | Interval in n=8 (mod 24) | Verification limit |
|---|---|---|
| Complete Python replay | [200000000000,{prefix_end}) | Every stated decision recomputed |
| Paired C executions | {'[200000000000,%d)'%production_end if production_end else 'Target run in progress'} | Entire interval not Python-replayed |
| Inherited C execution | [200000000000,10341223092224) | One entire-range run; only subsets corroborated |
{extra_table_rows}

The complete Python arithmetic replay in this visit covers the contiguous class
n=8 (mod 24) in **[200000000000,{prefix_end})**. Each member has either an exact
proper factor of p or a complete ordinary residue 2^(n+1) mod p different from 1.
Together with the imported below-200000000000 baseline and congruence reduction,
this excludes non-Desarguesian flag-transitive planes of every order
**n<{prefix_end}**, conditional on those imported premises and the usual correctness
assumptions for the exact computation.
The code and bounded replay commands are in claims.json. It is partial progress,
not resolution of the question.

{boundary_text}

{power_text}

{production_text}

One inherited C run reports no unsieved base-two survivor in
[200000000000,10341223092224). **Conditional on the imported premises AND on
that single entire-range run being correct**, it gives n<10341223092224.
Its entire range remains unreplicated. The old header contains no binary hash.
New computations corroborate only the explicit intervals above. Counts and file
hashes establish bookkeeping and integrity, not correctness of omitted decisions.

The prior referee externally replayed the old no-sieve pow prefix only through
201440000000, and both old Python control flows only through 201200000000.
The inherited later-chunk/window statements are not promoted to externally
confirmed results here. The new Python replay stated above was run in this visit;
its external referee status remains to be determined.

## Imported premises and target fidelity

The ledger is evidence/PREMISES.md. The staged Thas–Zagier reader conversion,
Sections 1–2 and the numerical appendix, was rechecked. It explicitly reports
the baseline n<200000000000, the seven even base-two exceptions below 5000000000,
Kantor's classification-dependent reduction, and the errors in the apparent older
power-of-two/prime-power resolutions. The source hash is recorded in the staged
SOURCES.json. The original PDF and later full texts are not staged. The contract's
dated literature screen is background data; no new literature/novelty search is
possible offline.

Imported: Kantor (1987), relying on the classification of finite simple groups,
leaves a nonclassical Frobenius/sharply flag-transitive case with even n and prime
p=n²+n+1. Thas–Zagier identify this case with the additive planar subgroup
D=(F_p*)^n=mu_(n+1); n=2,8 give classical planes. Feit's valid conditions give
8|n and d^(n+1)=1 (mod p) for every positive divisor d of n. The identity
n³-1=(n-1)p gives ord_p(n)=3; taking d=n yields 3|(n+1). Hence n=8 (mod 24).
Feit's invalid power-of-two exclusion and Ott's invalid prime-power argument are
not used. The full below-200000000000 computational baseline is imported, not
rerun here.

Base-two necessity also has a short proof. Planarity makes the set of x with
x,x+1 in D a singleton. Inversion preserves it, so x=x^(-1)=±1. The value -1
would require 0 in D, so x=1 and 2 belongs to D. Thus 2^(n+1)=1 (mod p).
Passing this necessity alone does not establish planarity.

The book page image was checked. Its literal graph wording has two defects:
reflection-generated dihedral Cayley graphs are bipartite with two parts of size
p and degree n+1<p, so opposite-part nonneighbors have odd distance at least
three and diameter two is impossible. Also, an unspecified reflection set does
not characterize non-Desarguesian planes: classical Singer difference sets give
diameter-three incidence Cayley graphs (Li 2005, as cited in the supplied source
screen). The valid geometric reduction is credited to Kantor plus Thas–Zagier,
not to those printed graph assertions.

## Computations, controls, and arithmetic independence

The 33 supplied gzip parts reconstruct all three missing inherited logs, matching
every compressed/raw-part and concatenated manifest hash without importing the
producer code. Raw sizes are 9,239,886, 46,531,770 and 9,257,179 bytes. Replay
restores them from the delivered parts; none of the claim commands executes a
local binary. One of the inherited manifests was the producer's own delivery
manifest; these hashes prove integrity only.

The new 128-bit scan is derived from the inherited C program and keeps its
two-64-bit-limb, full-256-bit-product Montgomery arithmetic. The separate scan32.c
uses three 32-bit limbs and only 64-bit intermediate products for modular
multiplication, a different Montgomery radix (2^96), and Tonelli–Shanks roots
instead of cube roots. It includes/imports no producer code. Both share author,
compiler, OS, left-to-right exponentiation recurrence, hash format and CommonCrypto
SHA-256. Their independence is explicitly partial. The binary SHA-256 is in each
new log header and the source/binary build ledger is preserved.

Every decision hashes this 32-byte little-endian record: n:u64, q:u32, tag:u32,
residue:u128. For a factor decision, q is the actual smallest sieve factor and
residue zero explicitly means **uncomputed**; no complete power is claimed there.
Every unsieved decision hashes the complete ordinary residue, not a Boolean or a
Montgomery representation. Selected factor audits compute complete residues too.
Matching digests compare every such decision, subject to SHA-256's collision
assumption, but are not proof that the executions were correct.

The independent Python replay derives roots using Cipolla's algorithm and
Eratosthenes, and uses arbitrary-precision pow. It imports no scanner code and
executes no scanner binary. NumPy only stores the fixed-width digest records;
all modular exponentiation uses exact Python integers. A separate manual
exponentiation loop was checked on one complete benchmark block and all stored
wide vectors. That loop shares CPython's big-integer multiplication/reduction with
pow; it is a separate control flow, not separate underlying arithmetic.

The sieve rejects only 1<q<p. The 32-bit scanner checks that guard at every mark
and verifies q|p for every marked production member. Full Python replay derives
and checks all proper-factor classes in its stated blocks. Every block's exact
class size, start/end, ID and sieved+tested=count identity are checked; the identity
alone is only bookkeeping. Only a last common, consecutive, completed block is
admitted as a capped endpoint.

{audit_text}

Controls passed before main production:

* All seven isolated controls have exact witness checks. The verifying command
  is check_controls.py; make_controls.py is only a separate regeneration tool.
* Both new unsieved C runs covered every even n in [2,5000000000), exactly
  2,499,999,999 members, reporting precisely 2,8,24,90,512,134217728,297474474.
  All full-residue block digests agree. Python rechecks 1,384 recorded residues
  only. This covers the small-modulus unsieved path, p<2^65.
* All 9,999 even n in [2,20000) received Python full decision/power checks.
  The q=p self-factor corruption is rejected, preserving the prime controls.
* All 960 full-residue vectors passed, including 90 synthetic positive vectors
  at 65–94-bit moduli. These test the power routine at large widths, not natural
  n-shaped survivors at those widths.
* The full 67,108,864-member production-sized benchmark matched both C digests
  under Python replay; the first 8,388,608-member block also matched the manual
  Python control flow. Negative residue/hash controls failed as required.

## Survivors and mathematical attempts

No unsieved base-two survivor is reported in the completed new production scopes.
The inherited production run also logged none. Thus the survivor/elimination
table for those scopes has zero rows and zero unresolved logged cases. This is a
log fact for un-replayed orders, not independent evidence that no hit was missed.
The explicit machine-readable table is evidence/epoch2/survivors.json.
A future hit must be eliminated by an exact proper factor, valid divisor-power
failure, or another proof. Probable primality never eliminates a survivor.

The isolated exceptions are resolved exactly: n=2,8 have every ordered difference
checked; n=24,90,512 have explicit collisions inside D; n=134217728 has
p=2593*71119*97685839; n=297474474 fails both the congruence class and the valid
d=n power condition. See evidence/controls.json.

The closure lemma excludes factors 3,5,7,17,31 of n under the valid multiplier
premise by duplicating the unique difference-1 pair (2,1). It likely overlaps
classical multiplier work, including Hall (1947), and is not used in the scan.
For n=2^a, primality of p forces a=3^t. Exact factors for t=3,...,9 and the
n=512 collision exclude this family for 3<a<59049. Those factors probably
reproduce known Cunningham-type factorizations. This is a sparse-family result,
not a general bound of 2^59049.

The next exponent a=59049 received a bounded factor-progression search through
q<=10^14 without a witness. Its failure is not a primality/nonexistence result.
{extra_factor_text}
The raw search log's last_k is a loop cursor one beyond the tested index on
exhaustion; no claim depends on it. The fixed-filter lemma proves why these
methods cannot settle all orders: sufficiently large n=2^(3^t) pass every
divisor-power condition and any fixed finite factor sieve, whether p is prime
or composite. This asserts no counterexample plane.

A finite-field moment/Vandermonde argument gives the exact binomial criterion
in evidence/epoch2/MOMENT-CRITERION.md. It supplies no general inconsistency
proof and direct evaluation is too costly for these production orders. It is
likely classical and is not used to omit any candidate. No universal obstruction
was obtained from these or the staged Gaussian-period/Fermat-curve reformulations.
Its small controls retain n=8; n=24 first fails at t=4, and n=90,512 fail at
t=2. These are alternate checks of already known isolated exceptions.

An initial Python checker attempted to import SymPy, which is absent from the
active python3 despite the resource list. Replacing it with standalone Cipolla
root derivation removed that dependency; no package was installed.
Process discovery was unavailable when a temporary resource-balancing pause was
considered. No signals were sent; the Python prefix workers instead wait for
the faster C scanner to finish.

## Remaining gap and replay limits

The all-orders conjecture remains unresolved. Outside the exact Python prefix,
the new large-range statement depends on the preserved C executions; the larger
inherited endpoint still depends on a single entire-range execution. Sampling,
zero logged hits, hashes, and matching aggregate counts do not fully certify the
omitted arithmetic. The imported classification and baseline remain dependencies.
The best next verification step is a fully replayable exact certificate or an
external exhaustive reexecution for those remaining decisions. A universal solution
needs mathematics beyond the fixed filters. No continuation or refill is scheduled.

{replay_text}

Each final command is Python-only and must run in <=300 seconds; the complete
set must total <=1800 seconds. Separated historical windows and redundant old
pow/manual chunk claims are archived rather than charged again to this replay
budget. Completed new sample logs have byte-exact deterministic gzip versions
below the 5 MB cap; their raw copies are removed only after byte-for-byte checks.
The packaging check enforces the 50 MB/2000-file limits and rejects missing
load-bearing artifacts. All work stays in this directory, with at most four
CPU-intensive scanner/replay workers; no network, delegation, installation,
credentials, commits, pushes, or external contact is used.

Status: {state['phase']}. Updated UTC: {now}.
Started 2026-10-15 21:23:55 UTC; deliverables due by minute 173,
2026-10-16 00:16:55 UTC; hard stop 00:47:55 UTC.
'''
    Path('REPORT.md').write_text(report)
    print(json.dumps(state,indent=2))


if __name__=='__main__':main()
