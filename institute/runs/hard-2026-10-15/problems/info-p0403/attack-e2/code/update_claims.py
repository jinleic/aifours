"""Write the current supported claims atomically; no solver result assumed."""
import json
from pathlib import Path

data={
    'outcome':'partial',
    'summary':'The headline existence question remains unresolved. Complete two-flip searches exclude balanced nonlinearity >=242 in radius-two neighborhoods of all three staged Kavut-Yucel seeds and all their linear output shifts.',
    'claims':[
        {
            'cid':'radius-two-exclusion',
            'statement':'For each of the three explicitly staged Section 3 Kavut-Yucel seeds, every Hamming-distance <=2 modification and every linear output shift fails to be both balanced and of nonlinearity >=242. All 130816 two-point modifications per seed actually have some Walsh coefficient of magnitude >28. The original minimum balancing distances are 6,6,14; the minimum over linear output shifts is 2 for every seed, so this shifted neighborhood is non-vacuous.',
            'type':'computation',
            'scope':'sub-question',
            'evidence':['results/radius2.json','code/radius2.py','code/check_radius2.py','code/controls.py'],
            'verify_command':'python3 code/radius2.py --compare',
            'check_command':'python3 code/check_radius2.py',
            'control_command':'python3 code/controls.py reject-broken2',
        }
    ],
    'next_step':'Complete the independent radius-four audit, then attempt a bounded radius-six exact search and seeded balanced local search.'
}
if Path('results/radius4-audit.json').exists():
    data['summary']='The headline question remains unresolved. Verified complete neighborhoods through radius four, including all linear output shifts of three staged Kavut-Yucel seeds, contain no balanced function with nonlinearity >=242.'
    data['claims'].append({
        'cid':'radius-four-exclusion',
        'statement':'For each of the three staged Section 3 Kavut-Yucel seeds, no modification at distance <=4, followed by any linear output shift, is balanced with nonlinearity >=242. Exactly 45 four-point modifications per seed preserve max|W|<=28; none has a zero Walsh coefficient. All 22238720 triples per seed were examined in both the producer and an independent implementation, not sampled. Odd distances cannot be balanced, distance zero has no Walsh zero, and distance two was excluded separately. Original minimum balancing distances:6,6,14; minimum over shifts:2.',
        'type':'computation','scope':'sub-question',
        'evidence':['results/radius2.json','results/radius4.json','results/radius4-audit.json','code/radius4.py','code/check_radius4.py'],
        'verify_command':'python3 code/radius4.py --compare',
        'check_command':'python3 code/check_radius4.py',
        'control_command':'python3 code/controls.py reject-broken4',
    })
if Path('results/baseline240.json').exists():
    data['claims'].append({
        'cid':'degree-at-most-seven-maximum',
        'statement':'Among balanced nine-variable Boolean functions of algebraic degree at most seven, the exact maximum nonlinearity is 240, attained by x0+x1*x2+x3*x4+x5*x6+x7*x8. Thus any balanced function satisfying the headline target must have degree exactly eight and nonzero bitwise XOR of its support indices. The same self-contained Walsh-divisibility/Parseval argument gives the elementary global balanced upper bound 242, so the global balanced maximum is either 240 or 242; which endpoint holds remains unresolved. No novelty is asserted. The direct checker verifies only the attaining witness; the universal bounds are proved in the written proof.',
        'type':'theorem','scope':'sub-question',
        'evidence':['degree-bound-proof.md','results/baseline240.json','code/baseline.py','code/check_witness.py'],
        'verify_command':'',
        'check_command':'python3 code/check_witness.py results/baseline240.json --min-nl 240 --expect-degree 2 --xor-zero',
        'control_command':'python3 code/check_witness.py results/baseline240-broken.json --min-nl 240',
    })
if all(Path('results/%s-r6-proof-check.json'%s).exists() and Path('results/%s-r6-encoding-audit.json'%s).exists() for s in ('dsbf40','dsbf32','rsbf56')):
    data['summary']='The headline existence question remains unresolved. Proof-checked and independently audited exclusions cover Hamming radius six around the three staged Kavut-Yucel seeds, including every linear output shift. A self-contained restriction excludes all balanced functions of degree at most seven from reaching 242.'
    evidence=['encoding-proof.md','code/local_sat.py','code/audit_local_sat.py','code/check_lrat.py','code/replay_local.py','results/control-r6-planted-audit.json','results/control-r6-planted-witness.json']
    for s in ('dsbf40','dsbf32','rsbf56'):
        pre='results/%s-r6'%s
        trimmed=Path(pre+'-trimmed-proof-check.json')
        use_trimmed=trimmed.exists() and json.loads(trimmed.read_text())['status']=='PASS'
        evidence.extend([pre+'.cnf',pre+'.encoding.json',pre+('-trimmed-proof-check.json' if use_trimmed else '-proof-check.json'),pre+'-encoding-audit.json'])
        evidence.append(pre+('-trimmed.lrat.gz' if use_trimmed else '.lrat.gz'))
    data['claims'].append({
        'cid':'radius-six-exclusion',
        'statement':'No Boolean function within Hamming distance <=6 of any of the three explicitly staged Section 3 Kavut-Yucel seeds, followed by any linear output shift, is balanced with nonlinearity >=242. The same transports under invertible affine input permutations and affine output addition. Exact-six CNFs have independently audited complete gate/lookup/character/cardinality/order correspondence and LRAT empty-clause proofs checked by a separate Python RUP checker; lower even distances are separately exhausted and odd distances have odd weight. The original forced balancing distances are 6,6,14, while each seed has shifted origins of forced distance 2; thus the claim including shifts is non-vacuous. This is a local exclusion, not a negative answer to the headline question.',
        'type':'negative-result','scope':'sub-question','evidence':evidence,
        'verify_command':'python3 code/replay_local.py --radius 6',
        'check_command':'python3 code/replay_local.py --radius 6 --independent',
        'control_command':'python3 code/audit_local_sat.py results/control-bad-encoding',
    })
    data['next_step']='Explore a larger audited neighborhood or genuinely different degree-eight balanced families. Radius-eight and heuristic runs remain inconclusive unless a certificate or verified target witness is recorded.'
if Path('results/flat-class-audit.json').exists():
    data['claims'].append({
        'cid':'sixteen-free-points-maximum',
        'statement':'For each of the three seeds, allow arbitrary truth-table changes on the explicitly listed 16-point affine four-flat in results/flat-class.json, then any linear output shift. The exact maximum balanced nonlinearity in each resulting class is 240. Each class has 448 underlying tables with max|W|<=28, and none has any zero Walsh coefficient. All 65536 patterns per seed were checked by both a 16-point transform reduction and an independent full-512-transform implementation, with every pattern outcome compared, and explicit attaining balanced tables were verified by direct character sums. This is a coordinate-subcube class, not a global result or a novelty assertion.',
        'type':'computation','scope':'sub-question',
        'evidence':['results/flat-class.json','results/flat-class-audit.json','code/flat_class.py','code/check_flat_class.py']+['results/%s-flat-outcomes.bin'%s for s in ('dsbf40','dsbf32','rsbf56')]+['results/%s-flat-attainer.json'%s for s in ('dsbf40','dsbf32','rsbf56')],
        'verify_command':'python3 code/flat_class.py --compare',
        'check_command':'python3 code/check_flat_class.py',
        'control_command':'python3 code/check_flat_class.py --broken',
    })
if all(Path('results/%s-two-cosets-audit.json'%s).exists() for s in ('dsbf40','dsbf32','rsbf56')):
    data['claims'].append({
        'cid':'two-parallel-cosets-maximum',
        'statement':'For each seed, fix the explicit four-dimensional V in its two-cosets result file. Allow arbitrary changes on any pair of its 32 parallel V-cosets (32 input points), then any linear output shift. The exact maximum balanced nonlinearity of this restricted union is 240, with explicit attaining witnesses. All 496 coset pairs were checked. Every pair covers all 2^32 assignments via two complete 65536-entry half-spectral catalogues and exact bitset intersections; the independent checker derives the universal character-block identity and all inequalities directly, not by sampling assignments. Every max|W|<=28 survivor changes only the core 16-point coset and has no Walsh zero. This is not a global exclusion; novelty is unknown.',
        'type':'computation','scope':'sub-question',
        'evidence':['two-coset-proof.md','code/two_coset.py','code/check_two_coset.py','code/replay_two_coset.py','results/flat-class.json']+['results/%s-two-cosets.json'%s for s in ('dsbf40','dsbf32','rsbf56')]+['results/%s-two-cosets-audit.json'%s for s in ('dsbf40','dsbf32','rsbf56')]+['results/%s-flat-attainer.json'%s for s in ('dsbf40','dsbf32','rsbf56')],
        'verify_command':'python3 code/replay_two_coset.py',
        'check_command':'python3 code/replay_two_coset.py --independent',
        'control_command':'python3 code/check_two_coset.py results/dsbf40-two-cosets.json --broken',
    })
batchpath=Path('results/free128-batch.json')
if batchpath.exists():
    batch=json.loads(batchpath.read_text())
    if batch['complete'] and len(batch['cases'])==12 and all(Path(c['control_prefix']+'-balanced-attainer.json').exists() for c in batch['cases']):
        evidence=['quarter-class-proof.md','degree-bound-proof.md','results/free128-batch.json','code/free_flat_sat.py','code/audit_free_flat.py','code/check_lrat.py','code/replay_free128.py','code/materialize_quarter_attainers.py']
        for c in batch['cases']:
            pre=c['prefix']; ctl=c['control_prefix']
            evidence.extend([pre+'.cnf',pre+'.encoding.json',pre+'.lrat.gz',pre+'-encoding-audit.json',pre+'-proof-check.json',ctl+'.cnf',ctl+'.encoding.json',ctl+'-audit.json',ctl+'-input.json',ctl+'-balanced-attainer.json',c['control_model_log']])
        data['claims'].append({
            'cid':'twelve-quarter-table-maxima',
            'statement':'For each staged seed, form the explicit 128-element linear space U listed in results/free128-batch.json. In each of its four cosets independently, allow arbitrary truth-table changes on those 128 points, fix every other value to the seed, and allow any linear output shift. Each of these twelve classes has exact maximum balanced nonlinearity 240, with an explicit balanced attaining table and direct-sum verification. The degree-eight necessary condition is justified by the self-contained proof; the complete signed-FWHT circuits, every arithmetic bit identity, all original character rows, interval comparators, zero choices and support-XOR constraints are independently audited. Every class has an independently checked LRAT empty-clause certificate and a planted satisfiable relaxed-bound control. This covers all 2^128 assignments per individual class, not simultaneous arbitrary changes on multiple quarter domains. It does not exclude general Boolean functions.',
            'type':'computation','scope':'sub-question','evidence':evidence,
            'verify_command':'python3 code/replay_free128.py',
            'check_command':'python3 code/replay_free128.py --independent',
            'control_command':'python3 code/audit_free_flat.py results/dsbf40-free128 --broken',
        })
        data['summary']='Partial only. The balanced nine-variable 242 existence question is unresolved. Verified results include radius-six exclusions around all three staged seeds and all linear output shifts, exact balanced maximum 240 in specified 32-point families and twelve 128-point quarter-table classes, and self-contained bounds 240<=the global balanced maximum<=242 with degree-eight necessary for a target. No novelty is asserted.'
        data['next_step']='A target must be degree eight, escape the certified affine seed neighborhoods, and change more than one of the specified quarter domains relative to a seed after any linear output shift. A new degree-eight construction or a substantially stronger global search/proof method is needed. The recorded global and 256-free-point bounded runs were UNKNOWN, not exclusions.'
tmp=Path('claims.json.tmp')
tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
tmp.replace('claims.json')
