#!/usr/bin/env python3
"""Build conservatively scoped recovery deliverables from completed checks.

Never produces mathematical scan decisions. claims.json is always written
through claims.json.tmp and an atomic rename. --final requires all planned
finite arithmetic checks; an incomplete run is not relabeled successful.
"""
import argparse
import datetime
import json
from pathlib import Path

from check import schema_validate


def load(path):
    return json.loads(Path(path).read_text())


def claim(cid, statement, kind, scope, evidence, verify='', check='', control=''):
    return dict(cid=cid, statement=statement, type=kind, scope=scope,
                evidence=evidence, verify_command=verify, check_command=check,
                control_command=control)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--final', action='store_true')
    args = p.parse_args()
    old = load('evidence/previous-delivery/claims.json')
    main_audit = load('evidence/recovery-main.audit.json')
    python_audit = load('evidence/recovery-python-main.audit.json')
    comparison = json.loads(load('evidence/recovery-shared-comparison-run.json')['stdout'])
    recovery = load('evidence/recovery-integrity.json')
    assert main_audit['audit_sha256'] == load('evidence/main.audit.json')['audit_sha256']
    assert python_audit['audit_sha256'] == load('evidence/python-main.audit.json')['audit_sha256']
    assert main_audit['survivors'] == []
    end = main_audit['end']
    compressed = ['selection-inputs/first-attempt-logs/MANIFEST.json']
    for source in load(compressed[0])['sources']:
        compressed.extend('selection-inputs/first-attempt-logs/'+part['file'] for part in source['parts'])
    claims = [claim('main-range',
        'Assuming the imported Kantor/Thas-Zagier/Feit theorems, one preserved C production computation '
        'excluded n=8 mod 24 in [200000000000,%d). It reports 422550962176 candidates in 50372 '
        'consecutive complete blocks, 364818361313 proper-factor rejections, 57732600863 base-two tests '
        'and zero logged survivors. Recovered logs match both supplied manifests. Structural checks '
        'validate block bookkeeping; Python independently recomputed complete residues and actual sieve '
        'divisors at all 251526 recorded samples only (217011 factor and 34515 unsieved records). '
        'With the imported below-200000000000 baseline this gives the conditional computational bound '
        'n<%d. No independent exhaustive certification of that entire interval, all-orders conclusion, '
        'or novelty claim is made.' % (end, end),
        'computation', 'sub-question',
        ['REPORT.md', 'evidence/PREMISES.md', 'evidence/result.json',
         'evidence/recovery-main.audit.json', 'evidence/recovery-integrity.json',
         'evidence/survivors.json', 'code/scan.c', 'code/check.py',
         'code/verify_result.py', 'code/recheck.py', 'code/recover_logs.py',
         'evidence/build.json', 'evidence/production-plan.json',
         'evidence/previous-delivery/manifest.json']+compressed,
        'python3 code/recheck.py main-metadata',
        'python3 code/recheck.py main-records',
        'python3 code/recheck.py main-negative'),
        claim('shared-arithmetic-and-python-prefix',
        'The preserved separate Python scan reports no survivors on n=8 mod 24 in '
        '[200000000000,439679307776), covering 9986637824 class members. Current replay '
        'rechecked its 47748 recorded residues and factors. The two scans agree in totals for '
        '1190 complete C blocks; additionally all 6032 shared audit indices agree entrywise '
        'in COMPLETE residues and actual sieve divisors, with 5226 factor and 806 unsieved '
        'records, and were independently recomputed. The complete Python prefix was not rerun '
        'during recovery. Aggregate agreement alone does not check C exponentiation, and '
        'these sample checks do not certify every decision in either scan.',
        'evidence', 'related',
        ['logs/python-main.blocks.jsonl', 'evidence/recovery-python-main.audit.json',
         'evidence/recovery-shared-comparison-run.json', 'code/compare_scans.py',
         'code/check.py', 'code/independent_scan.py', 'evidence/independent-plan.json',
         'evidence/recovery-broken-shared.records.jsonl', 'code/recheck.py']+compressed,
        'python3 code/recheck.py comparison', 'python3 code/recheck.py python-records',
        'python3 code/recheck.py comparison-negative')]
    keep = {'isolated-controls', 'full-published-control-interval', 'closure-lemma',
            'power-two-family', 'fixed-filter-limit'}
    for c in old['claims']:
        if c['cid'] in keep:
            claims.append(c)
    # This small claim remains useful even before the larger prefix finishes.
    if not Path('evidence/prefix-chunks/00.manual.json').exists():
        claims.append(next(c for c in old['claims'] if c['cid'] == 'prefix-exact'))
    prefix_rows = []
    for chunk in range(10):
        path = 'evidence/prefix-chunks/%02d.json' % chunk
        manual_path = 'evidence/prefix-chunks/%02d.manual.json' % chunk
        pow_path = 'evidence/prefix-chunks/%02d.pow.json' % chunk
        if not all(Path(f).exists() for f in (path, manual_path, pow_path)):
            continue
        produced, manual, checked = map(load, (path, manual_path, pow_path))
        start = 200000000000+240000000*chunk
        stop = start+240000000
        assert (produced['start'], produced['stop'], produced['count']) == (start, stop, 10000000)
        assert not produced['base_two_hits'] and not produced['unresolved']
        for row, backend in ((manual, 'manual'), (checked, 'pow')):
            assert (row['chunk'], row['start'], row['stop'], row['step'], row['count'], row['backend']) == \
                   (chunk, start, stop, 24, 10000000, backend)
        digest = produced['every_n_decision_full_residue_sha256']
        assert digest == manual['every_n_decision_full_residue_sha256'] == checked['every_n_decision_full_residue_sha256']
        prefix_rows.append(dict(chunk=chunk, start=start, stop=stop, digest=digest))
        claims.append(claim('exact-prefix-chunk-%02d' % chunk,
            'Every one of the 10000000 integers n=%d+24i (0<=i<10000000), '
            'equivalently n=8 mod 24 in [%d,%d), has 2^(n+1) mod (n^2+n+1) != 1. '
            'A fresh no-sieve Python computation and an independent manual binary-exponentiation '
            'checker matched a hash containing every n, decision and full residue. This excludes '
            'only these orders under the imported theorems, not all orders.' % (start, start, stop),
            'computation', 'sub-question',
            [path, manual_path, pow_path, 'code/replay.py', 'code/check_interval.py', 'evidence/PREMISES.md'],
            'python3 code/check_interval.py %d --backend pow' % chunk,
            'python3 code/check_interval.py %d --backend manual' % chunk,
            'python3 code/check_interval.py 0 --evidence evidence/prefix-chunk-broken.json --backend pow'
            if chunk == 0 else ''))
    window_groups = []
    windows = [json.loads(line) for line in Path('logs/python-windows.jsonl').read_text().splitlines()]
    assert [w['window'] for w in windows] == list(range(100))
    for w in windows:
        assert w['start'] == 200000000000+24*8388608*512*w['window']
        assert w['step'] == 24 and w['count'] == 1048576
        assert w['end'] == w['start']+24*w['count'] and not w['base_two_hits']
    for group in range(5):
        pow_path = 'evidence/window-chunks/%02d.pow.json' % group
        manual_path = 'evidence/window-chunks/%02d.manual.json' % group
        if not all(Path(f).exists() for f in (pow_path, manual_path)):
            continue
        expected = list(range(group*20, group*20+20))
        for f, backend in ((pow_path, 'pow'), (manual_path, 'manual')):
            row = load(f)
            assert row['verified_windows'] == expected and row['backend'] == backend
            assert row['total_members'] == 20971520
        window_groups.append(group)
        indices = ','.join(map(str, expected))
        qualifier = (' Window 99 lies outside the main interval and does not enlarge its endpoint.'
                     if group == 4 else '')
        claims.append(claim('separated-windows-%02d-%02d' % (group*20, group*20+19),
            'For each j in [%d,%d], every member of the 1048576-element progression '
            'starting at 200000000000+24*8388608*512*j, with step 24, has full base-two '
            'residue != 1. Both built-in pow replay and manual binary exponentiation matched '
            'the stored hash of every (n,decision,full residue), totaling 20971520 members '
            'in this group. These separated windows do not certify the whole production interval.'
            % (group*20, group*20+19)+qualifier,
            'computation', 'sub-question',
            ['logs/python-windows.jsonl', pow_path, manual_path, 'code/windows.py', 'code/check_windows.py'],
            'python3 code/check_windows.py --indices '+indices+' --backend pow',
            'python3 code/check_windows.py --indices '+indices+' --backend manual',
            'python3 code/check_windows.py evidence/negative-window.jsonl --indices 0 --backend pow'
            if group == 0 else ''))
    if args.final:
        assert len(prefix_rows) == 10 and window_groups == list(range(5)), 'planned finite checks incomplete'
        assert all(r['passed'] for r in load('evidence/recovery-quick-checks.json'))
        assert load('evidence/recovery-snapshot-test.json')['returncode'] == 0
        assert load('evidence/recovery-main-records-run.json')['returncode'] == 0
    for filename in ('evidence/recovery-final-checks.json', 'evidence/recovery-snapshot-test.json'):
        if Path(filename).exists():
            claims[0]['evidence'].append(filename)
    prefix_end = 200000000000
    for row in prefix_rows:
        if row['start'] != prefix_end:
            break
        prefix_end = row['stop']
    claims_data = dict(outcome='partial',
        summary='Recovered and replay-checked the evidence for one conditional production exclusion '
                'through n<%d; all-record arithmetic samples and shared C/Python residues now pass. '
                'Independent exhaustive checks cover stated finite chunks only. The all-orders '
                'flag-transitive-plane conjecture is unresolved here; novelty is unknown.' % end,
        claims=claims,
        next_step='Independently recompute the complete target range using a distinct exact implementation, '
                  'starting with [200000000000,2000000000000), and compare every decision/full residue. '
                  'For a universal proof, find a mathematical obstruction beyond the fixed sieve and divisor-power '
                  'conditions. Check later literature before any novelty/best-bound statement; no continuation is scheduled.')
    schema_validate(claims_data, load('claims.schema.json'))
    for c in claims:
        for item in c['evidence']:
            assert Path(item).is_file(), 'missing evidence: '+item
    Path('claims.json.tmp').write_text(json.dumps(claims_data, indent=2)+'\n')
    Path('claims.json.tmp').replace('claims.json')
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    summary = dict(phase='complete' if args.final else 'finite follow-up checks in progress',
                   updated_utc=now, outcome='partial', headline_resolved=False,
                   main_end=end, raw_recovery=recovery, main_audit_count=main_audit['audit_records'],
                   main_audit_sha256=main_audit['audit_sha256'],
                   shared_arithmetic=comparison, fresh_exact_prefix_chunks=prefix_rows,
                   fresh_exact_prefix_end=prefix_end, rechecked_window_groups=window_groups,
                   independent_exhaustive_main_range=False, novelty='unknown')
    Path('evidence/recovery-result.json').write_text(json.dumps(summary, indent=2)+'\n')
    prior_status = Path('evidence/previous-delivery/STATUS.json')
    if not prior_status.exists():
        prior_status.write_text(Path('evidence/STATUS.json').read_text())
    Path('evidence/STATUS.json').write_text(json.dumps(dict(
        phase=summary['phase'], updated_utc=now, outcome='partial',
        headline_resolved=False, production_replayed_structurally=True,
        recorded_main_arithmetic_samples_checked=main_audit['audit_records'],
        production_endpoint=end, fresh_exact_prefix_end=prefix_end,
        independent_exhaustive_main_range=False,
        note='Recovery status. Previous status archived; full range is not independently certified.'
    ), indent=2)+'\n')
    prefix_description = ('The fresh contiguous prefix currently checked by both methods is '
                          '[200000000000,%d), with %d class members. ' %
                          (prefix_end, (prefix_end-200000000000)//24)
                          if prefix_end > 200000000000 else
                          'The larger fresh contiguous-prefix checks are still in progress. ')
    if prefix_end == 202400000000:
        prefix_description += ('With the same imported baseline and congruence reduction, this fresh '
                               'computation alone supports the conditional order bound n<202400000000. '
                               'It does not independently certify the larger production endpoint. ')
    report = '''# math-p0039: bounded recovery and research result

**Outcome: partial. The all-orders question is neither solved nor refuted.
Novelty is unknown.**

Assuming the imported Kantor, Thas–Zagier and valid Feit theorems, one preserved
production computation excluded candidates n=8 (mod 24) in
**200000000000 <= n < 10341223092224**. Together with the imported published
below-200000000000 baseline, its conditional computational bound is
**n < N=10341223092224**. The endpoint is the end of the last consecutive
complete block. The larger planned endpoint is not a result.

This recovery restored and checked the evidence for that computation; it did
not rerun its whole interval. Python arithmetic checks cover only the explicit
samples and finite chunks below. **The entire production range has not been
independently certified.** No counterexample plane was found.

## Recovery and the referee's objections

The missing main block log, main arithmetic log and Python arithmetic log were
reconstructed from **33 gzip parts**. Every compressed part, decompressed part,
file size and concatenated SHA-256 matches the recovery manifest and the
previous delivery's manifest. The raw files are 9,239,886, 46,531,770 and
9,257,179 bytes. Their compressed parts are all below the snapshot file cap.
`code/recheck.py` reconstructs them on every invocation, so its commands work
even when a snapshot omits the large raw files. It imports no producer code and
never executes the retained C binary. See `evidence/recovery-integrity.json`.

The previous delivery is preserved under `evidence/previous-delivery/`.
Its unqualified positive-check statement is superseded. Current successful
checks are recorded in the recovery audit/run files, with negative controls
reported as expected failures. File hashes prove integrity only.

The strengthened C/Python comparison now checks **full ordinary residues and
actual smallest sieve divisors at 6,032 shared indices**, then recomputes those
values independently: 5,226 factor records and 806 unsieved records. A zeroed
shared residue is rejected by the negative control. The 1,190 common complete
blocks also agree in totals; those totals are bookkeeping, not a decision
audit. Window replay is split into five 20-window claims, with separate commands
for pow and manual exponentiation, rather than the previous timed-out --all
command. See `claims.json` for exact independently replayable scopes.

## Target fidelity and declared imported premises

The target is whether every finite flag-transitive projective plane is
Desarguesian. Its valid special-prime reduction is credited to **Kantor plus
Thas–Zagier**, not the book's graph assertions. The book prints two defects:

* Reflection-generated dihedral Cayley graphs are bipartite with parts of size
  p. Their degree n+1<p leaves opposite-part nonneighbors, at odd distance at
  least three. Diameter two is impossible.
* An unspecified reflection set does not characterize non-Desarguesian planes:
  classical Singer difference sets also give diameter-three incidence Cayley
  graphs. The supplied contract cites Li (2005) for that construction.

The local Thas–Zagier reader conversion was rechecked, including Section 1,
Proposition 2.1, Theorem 2.4 and the numerical appendix. Its SHA-256 matches
`selection-inputs/literature/SOURCES.json`. No original PDF or later-paper full
text is staged for a fresh check. The dated literature screen in the contract
is background data; this offline visit cannot establish a current literature
or novelty verdict.
The staged image of book page 39 was also visually checked against its printed
graph wording.

The premise ledger is `evidence/PREMISES.md`:

1. Kantor's 1987 classification-dependent theorem, using the classification of
   finite simple groups, leaves a nonclassical Frobenius/sharply flag-transitive
   alternative with even n and prime p=n²+n+1.
2. Thas–Zagier identify that alternative with the additive planar difference set
   D=(F_p*)^n=mu_(n+1). The special cases n=2,8 are classical.
3. Feit's valid conditions give 8|n and d^(n+1)=1 (mod p) for every positive
   divisor d of n. His purported power-of-two exclusion and Ott's purported
   prime-power-order theorem are not used; the staged source identifies errors.
4. Since n³−1=(n−1)p and 1<n<p, ord_p(n)=3. The d=n condition gives 3|(n+1),
   hence n=2 (mod 3), and with 8|n this gives n=8 (mod 24).
5. The base-two necessity also has an elementary proof. The unique x with
   x,x+1 in D is fixed by inversion, so x=x^(-1)=±1. The choice −1 gives zero
   in D and is impossible; thus x=1 and 2^(n+1)=1 (mod p).
6. Thas–Zagier's appendix reports exclusion below 2×10^11. That entire baseline
   is imported, not independently rerun in this visit.

## Preserved production and exact coverage scope

The C run reports 422,550,962,176 progression members in 50,372 consecutive
blocks, each of size 8,388,608: 364,818,361,313 proper-factor sieve rejections
and 57,732,600,863 base-two tests. It used 3 threads and stopped after its
9,000-second cap, completing already assigned blocks (9,000.533128 s).
The current recovery launches no further C production scan.

For every block the checker verifies IDs, starts, exclusive endpoints, class
counts, survivor lists and sieved+tested=count. **That identity does not validate
individual decisions:** the producer enforces it by construction. Outside the
arithmetic subsets, decisions still rest on this one production run.

The sieve uses q<=10^6 and rejects only when 1<q<p. In large blocks it first
proves p at the smallest n exceeds the sieve bound; its small-order path checks
q<p at every mark. The Montgomery implementation keeps full 256-bit products
for 128-bit reduction, with p<2^127. The source was reviewed; the arithmetic
bounds and derivation are in the premise ledger. No proof of compiler or whole
execution correctness is asserted.

| Production survivors logged | Exact eliminations needed | Unresolved logged cases |
|---:|---:|---:|
| 0 | 0 | 0 |

This empty table (`evidence/survivors.json`) is a log fact, not independent
evidence that no survivor was missed. A future base-two survivor must receive
an explicit proper factor, a valid divisor-power failure or another exact
argument. A probable-prime result never eliminates a survivor.

## Arithmetic checks and controls

* **All preserved main samples:** 251,526 complete residues and actual smallest
  sieve divisors recomputed by Python: 217,011 factor and 34,515 unsieved records.
  The records include both edges of every block and 197 contiguous 256-member
  windows. Every n, decision, factor and full residue in each such window enters
  its hash. The matching complete sample digest is
  `8b7f8161d7f7e9715e5a2ecbf8fcfc66317adf871f950f1b37cdc5e34a49fb5d`.
* **Preserved separate Python prefix:** its run reports [200000000000,
  439679307776), with 9,986,637,824 class members and 1,363,854,354 powers.
  Recovery rechecked all its 47,748 samples, not its entire execution. It uses
  Tonelli–Shanks sieve roots and Python pow instead of C cube roots/Montgomery.
* **Published full control interval:** the preserved unsieved C computation of
  every even n in [2,5000000000) reports exactly the seven listed values below.
  Current replay checks its 299-block bookkeeping and all 3,991 recorded full
  residues. Unrecorded control values rest on that run. This control exercises
  the unsieved path at smaller moduli, not the main-range sieve or every large
  modulus.
* **Proper-divisor guard:** every one of 9,999 even orders in [2,20000) has a
  stored sieve decision and full residue, all rechecked. Primes p<=10^6 in the
  controls are retained, never rejected by q=p. The explicit self-factor
  negative witness fails. A further 1,024-member window near n=2^60 has matching
  full residues and factors; it has only factor decisions, so it checks the
  full-residue arithmetic on that path.

| n | Exact control classification |
|---:|---|
| 2 | D planar, every ordered difference checked |
| 8 | D planar, every ordered difference checked |
| 24 | (1,256) and (8,263) have equal nonzero differences |
| 90 | (1,7474) and (4,7477) have equal nonzero differences |
| 512 | (1,89785) and (4,89788) have equal nonzero differences |
| 134217728 | p=2593×71119×97685839 is composite |
| 297474474 | d=n fails the divisor-power condition; n is outside 8 mod 24 |

Each displayed collision's four elements are checked in D. Passing base two
alone is therefore insufficient. Isolated controls are distinct from the full
control-interval production report.

'''+prefix_description+'''
Every completed fresh chunk uses full powers for every class member, even
composite p, and is independently checked with manual binary exponentiation.
The ten chunks partition [200000000000,202400000000); the final status
and individual endpoints/digests are in `evidence/recovery-result.json`.

The separated-window check status is recorded there too. Each of the 100 windows
has 1,048,576 members, starting at 200000000000+24·8388608·512·j, 0<=j<100.
All successful group checks compare hashes of every n, decision and full residue.
Window 99 starts at 10404842295296 and lies outside [200000000000,N); it cannot
enlarge the contiguous bound. The other 99 windows lie within that interval.
Pow replay repeats the producing arithmetic; manual exponentiation has a
separate control flow using Python integer multiplication and reduction.
Neither selected windows nor hashes certify omitted orders.

'''+('Both backends completed all 100 windows in this visit: 104,857,600 members '
     'per backend. The groups are separate bounded replay commands.\n'
     if args.final else '')+'''

## Mathematical attempts and exact remaining gap

The preserved elementary closure lemma gives gcd(n,3·5·7·17·31)=1 under the
divisor-multiplier premise; consecutive pairs (4,3),(5,4),(8,7),(17,16),(32,31)
would otherwise duplicate the unique difference-1 pair (2,1). It was not used
to skip any production candidates. No novelty is claimed.

For n=2^a, primality of n²+n+1 forces a=3^t. If a has a prime divisor l!=3,
then 2^(2a/l)+2^(a/l)+1 is a proper divisor. At a=9, the n=512 collision
excludes planarity; at a=27,81,243,729,2187,6561,19683 explicit proper factors
are verified in `evidence/power-two-family.json`. Hence this restricted family
is excluded for 3<a<59049. It does not extend the general order bound to
2^59049. These factors may reproduce known factorizations; no novelty is claimed.

The filtering strategy has a proved limitation. For n=2^(3^t), every divisor
of n satisfies the necessary power congruence, even when p is composite, and
each prime factor of p is 1 modulo 6·3^t. Thus every fixed finite sieve bound
eventually admits these integer candidates. This says nothing about whether p
is prime or D is planar. The first unresolved exponent in the displayed factor
chain is 59049; a failed bounded factor search is not a primality proof.

No all-orders obstruction was derived from the Gaussian-period/Fermat-curve
reformulations. The conjecture remains unresolved by this work. Orders at or
above N, apart from the restricted family just stated, are outside the general
computation. The imported classification/baseline and the unrepeated part of
the production computation remain explicit dependencies.

The best verification next step is a complete, separately engineered exact
recomputation of the target [2×10^11,2×10^12), comparing every decision and full
residue, then the rest of the reported range. A universal solution requires
new mathematics beyond these fixed necessary-condition filters. No continuation,
refill, network access, package install, external contact or delegation is scheduled.

## Replay

All claim commands use python3 or preinstalled tools; none execute a local binary.
Run from this directory:

    python3 code/recheck.py main-metadata
    python3 code/recheck.py main-records
    python3 code/recheck.py comparison
    python3 code/recheck.py python-records
    python3 code/check.py schema

The first four reconstruct the logs from their compressed parts. Their per-child
timeouts are below 900 seconds. Each prefix and separated-window claim has its
own bounded verify/check command in `claims.json`; use those chunks rather than
--all. Deliberately broken endpoint/residue/factor/coverage/window witnesses are
negative controls and must exit nonzero. Their expected failures do not establish
the positive claims without the matching successful checks.

The current delivery status is **'''+('complete' if args.final else 'in progress')+'''**.
Updated UTC: '''+now+'''. Session deadlines are in `evidence/recovery-session.json`.
'''
    if args.final and Path('evidence/recovery-final-checks.json').exists():
        checked = load('evidence/recovery-final-checks.json')
        report += ('\nThe current quick suite passed 11 positive checks and rejected all 10 deliberate '
                   'corruptions for the expected reasons. The final consistency checker passed all '
                   '22 scoped claims. The longest recorded individual replay in this visit was '
                   '%.3f seconds. See `evidence/recovery-quick-checks.json`, '
                   '`evidence/recovery-final-checks.json` and the successful missing-log snapshot '
                   'test in `evidence/recovery-snapshot-test.json`. These checks retain the subset '
                   'limits stated above.\n' % checked['longest_recorded_individual_replay_seconds'])
    Path('REPORT.md').write_text(report)
    print(json.dumps(dict(outcome='partial', final=args.final, main_end=end,
                          exact_prefix_end=prefix_end, prefix_chunks=len(prefix_rows),
                          window_groups=window_groups, claims=len(claims)), indent=2))


if __name__ == '__main__':
    main()
