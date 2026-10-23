"""Write only the continuation's replayed compact claims, atomically."""
import json
from pathlib import Path


data = json.loads(Path('claims.json').read_text())
base = [c for c in data['claims'] if c['cid']=='elementary-balanced-bounds']
assert len(base)==1
claims = base + [
    {
        'cid':'seed-invariants-and-inequivalence', 'type':'computation', 'scope':'related',
        'statement':'The three explicit hex tables in code/seeds.py have weights 250,250,242, nonlinearity 242, and no Walsh zero. Their forced balancing distances at the original origin are 6,6,14, and the minimum over linear output shifts is 2 for each. Their absolute autocorrelation indicators are respectively 40,32,56. Therefore they are pairwise not extended-affine equivalent, although their absolute Walsh histograms coincide.',
        'evidence':['code/seeds.py','code/check_seed_invariants.py','results/seed-invariants.json','selection-inputs/literature/kavut-yucel.reader.md','seed-and-local-proof.md'],
        'verify_command':'python3 code/check_seed_invariants.py', 'check_command':'', 'control_command':'',
    },
    {
        'cid':'radius-two-and-four-exclusion', 'type':'computation', 'scope':'sub-question',
        'statement':'For each explicit table dsbf40, dsbf32, rsbf56 in code/seeds.py, no modification at Hamming distance at most four followed by any linear output addition is both balanced and of nonlinearity at least 242. All 130816 pairs per seed fail the bound 28. Exhausting all 22238720 triples per seed gives 195 admissible triples and exactly 45 bound-preserving four-sets, none with a Walsh zero. Both the producer and independent checker exhaust the full ranges. Original forced distances are 6,6,14; over linear shifts they are 2,2,2, so the shifted exclusion is non-vacuous.',
        'evidence':['results/radius2.json','results/radius2-broken.json','results/radius4.json','results/radius4-broken.json','results/radius4-audit.json','code/radius2.py','code/radius4.py','code/check_radius2.py','code/check_radius4.py','code/controls.py','code/seeds.py','selection-inputs/literature/kavut-yucel.reader.md','seed-and-local-proof.md'],
        'verify_command':'python3 code/replay_radius4.py',
        'check_command':'python3 code/replay_radius4.py --independent',
        'control_command':'python3 code/controls.py reject-broken4',
    },
    {
        'cid':'sixteen-free-points-maximum', 'type':'computation','scope':'sub-question',
        'statement':'Allow arbitrary changes on the specified 16-point affine four-flat of each seed, followed by any linear output addition. Each of these three restricted classes has exact balanced maximum nonlinearity 240. All 65536 assignments per seed were independently checked at all 512 Walsh indices and compared to a separate 16-point transform reduction. Each class has 448 tables preserving bound 28, none with a zero. Explicit balanced 240 attainers are included.',
        'evidence':['results/flat-class.json','results/flat-class-audit.json','results/radius4.json','code/flat_class.py','code/check_flat_class.py','code/check_witness.py','code/seeds.py','selection-inputs/literature/kavut-yucel.reader.md','two-coset-proof.md'] + [f'results/{s}-flat-{tail}' for s in ('dsbf40','dsbf32','rsbf56') for tail in ('outcomes.bin','attainer.json')],
        'verify_command':'python3 code/flat_class.py --compare',
        'check_command':'python3 code/check_flat_class.py',
        'control_command':'python3 code/check_flat_class.py --broken',
    },
    {
        'cid':'two-parallel-cosets-maximum', 'type':'computation','scope':'sub-question',
        'statement':'For each seed and its explicit V in two-coset-proof.md, allow arbitrary changes on any pair of distinct V-cosets and then any linear output addition. The exact balanced maximum in each restricted union is 240. All 496 pairs per seed are covered by complete 65536-entry half catalogues and exact finite bitset intersections covering all 2^32 assignments per pair. The independent checker reconstructs the full catalogues by direct sums and audits every original character-block identity and inequality. Each pair containing the core has 448 bound-preserving assignments; each other pair has one; none has a Walsh zero. Counts across pairs have multiplicity.',
        'evidence':['two-coset-proof.md','results/flat-class.json','code/two_coset.py','code/check_two_coset.py','code/replay_two_coset.py','code/check_witness.py','code/seeds.py','selection-inputs/literature/kavut-yucel.reader.md'] + [f'results/{s}-two-cosets.json' for s in ('dsbf40','dsbf32','rsbf56')] + [f'results/{s}-flat-attainer.json' for s in ('dsbf40','dsbf32','rsbf56')],
        'verify_command':'python3 code/replay_two_coset.py',
        'check_command':'python3 code/replay_two_coset.py --independent',
        'control_command':'python3 code/check_two_coset.py results/dsbf40-two-cosets.json --broken',
    },
]
data.update(outcome='partial', claims=claims,
    summary='Partial only: the balanced nine-variable 242 existence question is unresolved. Replayed compact results give elementary global bounds {240,242}, degree-eight necessity, radius-four exclusions around three pairwise inequivalent explicit seeds, and restricted 16-point/32-point family maxima 240. Missing large prior certificates are not relied upon. Novelty is unknown.',
    next_step='Complete the new compact radius-six audit and retain only certificate-backed larger classes. A global degree-eight witness or global nonexistence proof is still needed.')
tmp=Path('claims.json.tmp'); tmp.write_text(json.dumps(data,indent=2)+'\n'); tmp.replace('claims.json')
print('Recorded',len(claims),'compact claims atomically.')
