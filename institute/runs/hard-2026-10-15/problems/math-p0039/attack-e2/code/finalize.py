#!/usr/bin/env python3
"""Write final deliverables after production AND the declared audits finish.

This is a report builder, not a new producing scan. It refuses incomplete logs
or unresolved survivors. It never executes a compiled local binary.
"""
import datetime
import json
from pathlib import Path

from check import metadata, need, schema_validate


def load(path):
    return json.loads(Path(path).read_text())


def main():
    header, blocks, production = metadata('logs/main', expected_start=200000000000,
                                           expected_step=24, allow_partial=True)
    audit = load('evidence/main.audit.json')
    survivors = load('evidence/survivors.json')
    tail = load('evidence/python-full-tail.json')
    prefix = load('evidence/python-full-prefix.json')
    family = load('evidence/power-two-family.json')
    control = load('evidence/control-even.coverage.json')
    manual = load('evidence/python-windows.manual-check.json')
    full_windows = load('evidence/python-windows.full-replay.json')
    need(full_windows['verified_windows'] == list(range(100)) and
         full_windows['total_members'] == 104857600 and full_windows['backend'] == 'pow',
         'full separated-window replay not complete')
    _, _, python_scan = metadata('logs/python-main', expected_start=200000000000,
                                  expected_step=24, allow_partial=True)
    python_audit = load('evidence/python-main.audit.json')
    comparison = load('evidence/scans.comparison.json')
    for key in ('start', 'end', 'step', 'class_count', 'block_count', 'sieved', 'tested', 'survivors'):
        need(python_scan[key] == python_audit[key], 'independent prefix audit mismatch')
    need(not python_scan['survivors'], 'independent prefix contains unresolved candidates')
    windows = [json.loads(s) for s in Path('logs/python-windows.jsonl').read_text().splitlines()]
    for key in ('start', 'end', 'step', 'class_count', 'block_count', 'sieved', 'tested', 'survivors'):
        need(production[key] == audit[key], 'arithmetic audit does not cover final log metadata')
    need(survivors['end'] == production['end'] and not survivors['unresolved'], 'survivors not resolved')
    need(survivors['logged_survivor_count'] == len(production['survivors']), 'survivor count')
    need(tail['stop'] == production['end'] and tail['count'] == 1000000 and not tail['unresolved'] and not tail['base_two_hits'], 'tail replay')
    need(prefix['count'] == 1000000 and not prefix['unresolved'] and not prefix['base_two_hits'], 'prefix replay')
    need([w['window'] for w in windows] == list(range(100)), 'independent window list')
    need(manual['verified_windows'] == [0, 99] and manual['total_members'] == 2097152 and manual['backend'] == 'manual', 'manual window audit')
    for w in windows:
        need(w['count'] == 1048576 and w['step'] == 24 and not w['base_two_hits'], 'window unresolved or changed')
        need(w['start'] == 200000000000+24*8388608*512*w['window'], 'window grid')
        need(w['end'] == w['start']+24*w['count'], 'window length')
    end = production['end']
    need(comparison['c_scan_end'] == end and comparison['python_scan_end'] == python_scan['end'],
         'cross-comparison endpoints do not match final scans')
    need(python_scan['end'] < end, 'independent subset description requires a smaller prefix')
    inside = [w for w in windows if w['end'] <= end]
    finished = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = dict(outcome='partial', headline_resolved=False,
                  conditional_on_imported_premises=True,
                  start=production['start'], end=end, production=production,
                  recorded_arithmetic_audit_count=audit['audit_records'],
                  recorded_arithmetic_audit_sha256=audit['audit_sha256'],
                  full_python_prefix=prefix, full_python_tail=tail,
                  separate_python_window_count=len(windows),
                  separate_python_window_members=sum(w['count'] for w in windows),
                  separate_python_windows_inside_main=len(inside),
                  manual_rechecked_windows=manual,
                  all_separated_windows_replayed=full_windows,
                  independent_contiguous_python_prefix=python_scan,
                  independent_prefix_recorded_arithmetic_checks=python_audit['audit_records'],
                  independent_prefix_comparison=comparison,
                  power_two_exponent_bound_exclusive=family['max_exponent_exclusive'],
                  independent_full_main_range_certification=False,
                  novelty='unknown', finalized_utc=finished)
    Path('evidence/result.json').write_text(json.dumps(result, indent=2)+'\n')
    broken = json.loads(json.dumps(result)); broken['end'] += 24
    Path('evidence/result-broken.json').write_text(json.dumps(broken, indent=2)+'\n')

    old = load('claims.json')
    kept = [c for c in old['claims'] if c['cid'] not in ('main-range', 'python-windows', 'main-target-checkpoint', 'independent-prefix')]
    main_claim = dict(cid='main-range', type='computation', scope='sub-question',
        statement=('Assuming the declared Kantor/Thas-Zagier/Feit premises, one exact C production computation excluded all '
                   'candidates n=8 mod 24 in [200000000000,%d), with %d class members in %d unbroken complete blocks, '
                   '%d proper-factor sieve rejections and %d base-two tests. Every logged survivor was exactly eliminated; '
                   'unresolved count is zero. Combining the imported published below-200000000000 bound gives the conditional '
                   'computational nonexistence bound n<%d for non-Desarguesian flag-transitive planes. Independent arbitrary-precision '
                   'checks covered only the explicitly listed samples/windows, not the entire scan. This finite bound does not '
                   'resolve the all-orders conjecture; novelty is unknown.') %
                   (end, production['class_count'], production['block_count'], production['sieved'], production['tested'], end),
        evidence=['REPORT.md', 'evidence/PREMISES.md', 'evidence/result.json', 'evidence/main.audit.json',
                  'evidence/survivors.json', 'logs/main.blocks.jsonl', 'logs/main.records.jsonl',
                  'code/scan.c', 'code/check.py', 'code/verify_result.py', 'evidence/build.json',
                  'evidence/production-plan.json'],
        verify_command='python3 code/verify_result.py',
        check_command='python3 code/check.py records logs/main --allow-partial',
        control_command='python3 code/verify_result.py --result evidence/result-broken.json')
    window_claim = dict(cid='python-windows', type='computation', scope='sub-question',
        statement=('A separate Python arbitrary-precision computation tested every member of 100 separated windows, '
                   '1048576 members per window (104857600 full modular powers). Window j starts at '
                   '200000000000+24*8388608*512*j, for 0<=j<100, with step 24. Every base-two residue was different '
                   'from 1. Each full window hash includes every n, decision and full residue. A separate checker reran all '
                   '100 windows with built-in pow and matched every hash. A manual binary-exponentiation '
                   'checker rechecked only windows 0 and 99, 2097152 members, and matched their hashes. The separated '
                   'windows do not independently certify the entire production interval.'),
        evidence=['logs/python-windows.jsonl', 'evidence/python-windows.manual-check.json',
                  'evidence/python-windows.full-replay.json', 'code/windows.py', 'code/check_windows.py'],
        verify_command='python3 code/check_windows.py --all --backend pow',
        check_command='python3 code/check_windows.py --indices 0,99 --backend manual',
        control_command='python3 code/check_windows.py evidence/negative-window.jsonl --indices 0 --backend pow')
    independent_claim = dict(cid='independent-prefix', type='computation', scope='sub-question',
        statement=('A separate complete Python computation, importing neither C producing code nor its arithmetic, '
                   'repeated only the contiguous prefix [200000000000,%d) on n=8 mod 24. It processed %d class members '
                   'using %d proper-factor rejections and %d arbitrary-precision base-two tests, with no survivors. '
                   'Sieve roots use Tonelli-Shanks square roots of -3 rather than the C cube-root method. '
                   'All %d completely overlapping C blocks agree with its aggregated counts. Its own %d recorded '
                   'arithmetic samples were checked by trial division/full Python powers. This independently repeated '
                   'prefix is smaller than the general C interval and does not independently certify that entire interval.') %
                   (python_scan['end'], python_scan['class_count'], python_scan['sieved'], python_scan['tested'],
                    comparison['compared_c_blocks'], python_audit['audit_records']),
        evidence=['logs/python-main.blocks.jsonl', 'logs/python-main.records.jsonl',
                  'evidence/python-main.audit.json', 'evidence/scans.comparison.json',
                  'evidence/independent-plan.json', 'code/independent_scan.py', 'code/compare_scans.py'],
        verify_command='python3 code/compare_scans.py',
        check_command='python3 code/check.py records logs/python-main --allow-partial',
        control_command='python3 code/check.py metadata evidence/negative-coverage')
    claims = dict(outcome='partial', summary=('Conditional computational exclusion through n<%d, plus a separate '
                   'power-of-two-order exclusion for 3<a<59049. Independent checks cover stated subsets only. '
                   'The all-orders conjecture remains unresolved. Novelty is unknown.') % end,
                  claims=[main_claim, independent_claim]+kept+[window_claim],
                  next_step='Independently replay the full recorded general interval using a distinct exact arithmetic implementation and check later literature before any best-bound claim. A universal solution needs additional mathematics; the necessary-condition tests leave possible larger orders open.')
    schema_validate(claims, load('claims.schema.json'))
    Path('claims.json.tmp').write_text(json.dumps(claims, indent=2)+'\n')
    Path('claims.json.tmp').replace('claims.json')

    ct = load('evidence/controls.json')['controls']
    control_table = '| n | p | exact status |\n|---:|---:|---|\n'
    for r in ct:
        w = r['result']
        if w['kind'] == 'planar-direct':
            why = 'D planar, all differences checked (classical control)'
        elif w['kind'] == 'difference-collision':
            why = '%s and %s have the same nonzero difference %d' % (w['pair1'], w['pair2'], w['difference'])
        elif w['kind'] == 'proper-factor':
            why = 'proper factor %d; cofactor %d' % (w['factor'], w['cofactor'])
        else:
            why = 'n mod 24 = %d; d=n has residue %d, not 1' % (w['remainder_mod_24'], w['witness_residue'])
        control_table += '| %d | %s | %s |\n' % (r['n'], r['p'], why)
    if survivors['eliminations']:
        survivor_table = '| n | p | exact witness |\n|---:|---:|---|\n'
        for r in survivors['eliminations']:
            survivor_table += '| %d | %s | %s |\n' % (r['n'], r['p'], json.dumps(r['witness']))
    else:
        survivor_table = '| production base-two survivors after sieving | exact eliminations needed | unresolved |\n|---:|---:|---:|\n| 0 | 0 | 0 |\n'
    factor_table = '| a | proper factor of 2^(2a)+2^a+1 |\n|---:|---:|\n'
    for r in family['factors']:
        factor_table += '| %d | %d |\n' % (r['a'], r['proper_factor'])
    report = f'''# math-p0039: bounded research result

**Outcome: partial. The all-orders conjecture is not solved or refuted. Novelty is unknown.**

## General finite computational result

Assuming the declared imported theorems, one production computation excluded every
candidate in **200000000000 <= n < {end}**, with n=8 (mod 24).
The last unbroken audited block boundary is **N={end}**, exclusive.
The computation covered {production['class_count']:,} class members in
{production['block_count']:,} complete blocks: {production['sieved']:,} proper-factor
sieve rejections and {production['tested']:,} exact base-two tests. Every block
satisfies sieved+tested=its exact arithmetic-class count. There are no unresolved
survivors.

Together with the imported Thas–Zagier below-200000000000 exclusion, this gives
the **conditional computational bound: no non-Desarguesian flag-transitive
projective plane has order n<N**. Independent arbitrary-precision checks covered
only the explicitly stated subsets below. The complete production interval has
NOT been independently certified. This finite range is a sub-question, not a
solution of the universal question. The planned stop 20000000000000 is not a
reported bound.

A separate exact result excludes only power-of-two orders 2^a for 3<a<59049;
it does not extend the general bound N to 2^59049.

## Question fidelity and imported premises

The target is the finite flag-transitive-plane conjecture, with its special-prime
difference-set reformulation. The book's literal graph assertions are defective:
reflection-generated dihedral Cayley graphs are bipartite, each part has p
vertices, and degree n+1<p leaves opposite-part nonneighbors, making diameter
two impossible. Also an unspecified set of reflections does not give the stated
equivalence with non-Desarguesian planes: classical Singer difference sets yield
diameter-three incidence Cayley graphs too. The staged book-page image was
visually checked. No result here relies on that printed equivalence.

The detailed ledger is [PREMISES.md](evidence/PREMISES.md):

* Kantor (1987), via Thas–Zagier Section 1: the non-Desarguesian alternative has
  even n, prime p=n²+n+1 and a Frobenius/sharply flag-transitive action. This
  reduction relies on the classification of finite simple groups.
* Thas–Zagier Proposition 2.1/Theorem 2.4 identify the remaining case with
  D=mu_(n+1) being an additive planar difference set. Only n=2,8 give classical
  planes in this special construction. Their appendix gives the base-two
  necessary condition and the published computational baseline.
* Feit's VALID necessary conditions: 8|n and d^(n+1)=1 mod p for every positive
  divisor d of n. Feit's purported power-of-two exclusion and Ott's purported
  prime-power-order proof are not used; the staged paper identifies errors.
* Derived here: n³=1 mod p and n is not 1 mod p, so ord_p(n)=3. Taking d=n
  gives 3|(n+1); together with 8|n this gives n=8 mod 24.
* The base-two condition also has a short proof: the unique x with x,x+1 in D
  is fixed by inversion. Thus x=±1, with −1 impossible, so x=1 and 2 is in D.

Only staged local materials were available. The Thas–Zagier source is a
reader-converted text, whose SHA-256 matches SOURCES.json; its original PDF and
later papers were not available for a fresh literature check. Section 1,
Proposition 2.1, Theorem 2.4 and the appendix were rechecked before production.
The below-2×10^11 computation is imported, not independently rerun here.

## Controls, cheap falsification and arithmetic

The FULL published even-n interval [2,5000000000) was rerun without a sieve:
{control['class_count']:,} values, 299 blocks, {control['seconds']:.3f} seconds,
exactly the seven published exceptions. This reproduces the full list, not just
isolated positive checks. Python independently recomputed 3991 recorded full
residues, not the whole 2.5-billion-value control run.

{control_table}

For each n=24,90,512 collision, the four elements are verified members of D and
the ordered pairs are distinct. Thus passing base two is not sufficient.

The full even-n range [2,20000) was also checked both with and without a
B=1000000 sieve. All 9999 residues and every actual smallest proper sieve
factor were independently recomputed. In particular the controls whose prime
p lies below B (7,73,601,8191,262657) were retained: the sieve never uses q=p
as a rejection. Two further 1024-member arithmetic windows, one at the main
lower boundary and one near n=2^60, matched Python completely.

The producing [scan.c](code/scan.c) uses full 256-bit intermediate products for
128-bit Montgomery reduction. Inputs satisfy n<2^60, hence odd p<2^127.
The proof of the arithmetic bounds is in PREMISES.md. Audit records contain
complete ordinary residues after Montgomery conversion, not pass/fail flags.
The source and binary were frozen before controls and production; their hashes
and the compiler command are in build.json. Replay commands never execute that
binary.

## Production method, benchmark and coverage

Candidates are n=200000000000+24i. An Eratosthenes sieve generates trial primes
q<=1000000. The roots of n²+n+1 mod q are computed exactly; q=3 is handled
separately. Every sieve rejection is by a proper divisor 1<q<p. The fast path
first proves B<p at the block's smallest n, hence for the whole block; the
small-n path checks q<p at every proposed mark. Descending marking retains the
smallest sieve prime as the recorded witness.

All unsieved candidates receive an exact 2^(n+1) mod p test. A residue other
than 1 eliminates a proved necessary condition without requiring a primality
test. A residue of 1 must be resolved by an exact witness; probable primality
never eliminates one.

Three 100-million-member benchmarks gave 2.461 s (B=100000, large blocks),
2.113 s (B=1000000, large blocks), and 2.028 s (B=1000000, small blocks).
Large blocks (8388608 members) were selected to limit evidence volume and audit
memory. The two B=1000000 benchmarks agreed on all aggregate counts.

Production used 3 CPU threads with one CPU reserved for independent Python
work. Its hard compute cap was 9000 seconds, completing only already assigned
blocks after the cap. Actual production wall time: {production['seconds']:.3f}
seconds. All block IDs are consecutive from 0; starts, exclusive endpoints,
class counts, branch counts and every survivor list are structurally checked.
See production-plan.json and main.blocks.jsonl. No install, network, delegation,
credentials, outside-directory reads, or git commits were used.

## Survivor/elimination table

{survivor_table}

The machine-readable table is survivors.json. Its independent checker compares
the table with EVERY logged survivor, verifies proper factors or valid divisor
congruence failures, and rejects unresolved cases. It does not accept any
probable-prime elimination.

## Exactly what was independently checked

* **A second complete computation of a smaller contiguous prefix:** the
  separate Python scanner processed ALL {python_scan['class_count']:,} class
  members in [200000000000,{python_scan['end']}), using
  {python_scan['sieved']:,} proper-factor rejections and
  {python_scan['tested']:,} arbitrary-precision powers, with no survivors.
  It uses Tonelli–Shanks roots of −3 and bytearray slices, imports no producing
  C code, and ran for {python_scan['seconds']:.3f} s on one CPU. Every one of
  {comparison['compared_c_blocks']:,} fully overlapping C blocks agrees with
  its aggregate counts. That agreement is an aggregate control, not an
  entrywise residue hash of all n. The separate computation repeats its
  entire stated prefix, which is SMALLER than the general production range.
  Its own {python_audit['audit_records']:,} audit records received independent
  full-power/trial-factor checks. Parameters/source hash are in
  independent-plan.json, counts in python-main.blocks.jsonl, checks in
  python-main.audit.json and scans.comparison.json.
* **Production audit records:** {audit['audit_records']:,} records, including
  {audit['audit_factor_records']:,} factor decisions and
  {audit['audit_unsieved_records']:,} unsieved decisions. Python recomputes the
  COMPLETE power for each, and uses independent trial division to verify the
  actual smallest sieve factor. Records include the first/last two members of
  every completed block and {len(audit['contiguous_audit_windows']):,} contiguous
  256-member windows at the first block and every 256th block. Every member in
  each window is hashed as n, decision, factor, full residue, including sieved
  members. Exact window endpoints and hashes are in main.audit.json.
* **Separated exhaustive Python windows:** 100 predetermined windows of
  1048576 members each, {sum(w['count'] for w in windows):,} full powers total.
  Window j starts at 200000000000+24·8388608·512·j, for 0<=j<100. Every n,
  decision and full residue contributes to its hash, including composite
  moduli. {len(inside)} of these windows lie wholly inside the final main
  interval. All are listed individually in python-windows.jsonl; any outside
  the main endpoint do not enlarge the gap-free general bound.
* **A third arithmetic control:** an independent manual binary-exponentiation
  checker rechecked only windows 0 and 99 ({manual['total_members']:,} members)
  and matched their full hashes. It did not recheck all 100 windows. A separate
  replay with built-in pow reran all 100 windows ({full_windows['total_members']:,}
  full powers) and matched every hash; its output is
  python-windows.full-replay.json.
* **Exhaustive boundaries:** Python pow checked every one of the first
  1000000 class members [200000000000,200024000000), and every one of the last
  1000000 class members [{tail['start']},{end}). No base-two hits remained.
* **Controls:** the small full-range comparisons and the 3991 full published-
  control samples described above. Known positive controls were included.

These are implementations using Python arbitrary-precision integers that do
not import or execute the producing C code. Their scope is precisely these
subsets, including the explicitly smaller complete Python prefix. Neither
sampling nor hashes independently certify the entire
production scan. File hashes establish integrity only. The general bound is
reported as one production computation with declared subset checks.

## A separate power-of-two-order result and analytical limitations

For n=2^a, primality of p forces a=3^t: if a has a prime divisor l!=3, then
2^(2a/l)+2^(a/l)+1 is an explicit proper divisor of p. For a=3^t the order of
2 mod a hypothetical prime p is exactly 3^(t+1), which divides n+1. Thus
all base-two AND divisor-multiplier conditions automatically pass. The proof
is in POWER-TWO-LEMMA.md; no invalid Feit power-of-two argument is imported.
In fact for every t this congruence statement holds even when p is composite,
and every prime factor of that p is 1 mod (6·3^t). Consequently any FIXED
finite prime sieve plus these power conditions admits infinitely many integer
survivors at larger orders. This is a limitation of the filter, not a claim
that the associated p is prime or that any counterexample plane exists.

At a=9, n=512 is eliminated by the direct D collision above. All subsequent
exceptional exponents below 59049 have these exact proper factors:

{factor_table}

This is a gap-free factor chain for 3^t, 3<=t<=9. It proves the restricted
exclusion for every exponent 3<a<59049, not only the displayed seven exponents:
the algebraic lemma excludes all non-powers of three. check_family.py verifies
each factor by manual small-modulus exponentiation and verifies the n=512
collision; a separate full-integer factor check also passed. The first unhandled
exceptional exponent is a=59049. Failure to find a factor below 10^11 does not
prove this p prime or resolve that case. See POWER-TWO-RANGE.md.

Multiplicative closure also gives gcd(n,3·5·7·17·31)=1 under the valid
divisor-multiplier premise (CLOSURE-LEMMA.md). This corollary leaves substantial
families open and was NOT used by the production sieve. No novelty is claimed
for either elementary lemma or the factor chain.

The Gaussian-period/Fermat-curve reformulations in the staged paper were
considered, but no uniform rationality obstruction or difference collision was
derived. The elementary subgroup argument only excludes some factor patterns;
it leaves powers of two and other factor sets. A finite scan cannot fill this
all-orders gap.

## Replay commands and negative controls

All commands run from this directory using python3; no attack-built executable
is invoked. Fast structural replay (not a full recomputation):

    python3 code/verify_result.py
    python3 code/check.py schema
    python3 code/check_family.py
    python3 code/check_controls.py
    python3 code/compare_scans.py
    python3 code/seal.py check

Recompute ALL stored production arithmetic samples (still only a subset of n):

    python3 code/check.py records logs/main --allow-partial

Recompute the selected manual-control windows, or every separated window:

    python3 code/check_windows.py --indices 0,99 --backend manual
    python3 code/check_windows.py --all --backend pow

Slow complete Python reexecution of the entire general range is available but
was NOT performed; it can require far more time than this visit's budget:

    python3 code/replay.py --start 200000000000 --stop {end} --step 24

Each of the following deliberate corruptions must return nonzero: a changed
full residue, a q=p self-factor, a broken block count, a changed window hash,
a changed family factor, and a changed reported endpoint:

    python3 code/check.py single evidence/negative-residue.json --bound 1000000
    python3 code/check.py single evidence/negative-self-factor.json --bound 1000000
    python3 code/check.py metadata evidence/negative-coverage
    python3 code/check_windows.py evidence/negative-window.jsonl --indices 0 --backend pow
    python3 code/check_family.py evidence/power-two-family-broken.json
    python3 code/verify_result.py --result evidence/result-broken.json

## Remaining gap and best next step

No non-Desarguesian plane has been constructed, and no argument excludes every
remaining order. Orders n>=N outside the restricted power-of-two result remain
unhandled. Even within that family, a>=59049 is not excluded by its theorem.
The imported baseline and classification are not independently reproved, and
the complete new general interval has only one production implementation.
The separate Python computation repeated only the smaller prefix stated above.

The best verification next step is an independently engineered COMPLETE exact
replay of the reported interval, followed by checking later literature before
any best-bound or novelty statement. The universal conjecture requires an
additional mathematical obstruction, not interpretation of this finite scan
as a universal proof. No automatic continuation or extra visit is scheduled.

Finalized UTC: {finished}. Session deadlines are in session.json; production
began at the time in production-plan.json. Evidence file hashes are in
manifest.json and certify file integrity only.
'''
    Path('REPORT.md').write_text(report)
    print(json.dumps(dict(end=end, outcome='partial', finalized_utc=finished,
                          class_count=production['class_count'], audit_records=audit['audit_records']), indent=2))


if __name__ == '__main__':
    main()
