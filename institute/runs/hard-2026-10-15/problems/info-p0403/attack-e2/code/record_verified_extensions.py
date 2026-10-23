"""Atomically add the four independently replayed continuation results."""
import json
from pathlib import Path

data=json.loads(Path('claims.json').read_text())
new_ids={'radius-six-compact-exclusion','two-preserved-flat-certificates','extra-seed-neighborhoods','fixed-half-screen'}
data['claims']=[c for c in data['claims'] if c['cid'] not in new_ids]
for c in data['claims']:
    if c['cid']=='elementary-balanced-bounds':
        c['control_command']='python3 code/check_witness.py results/baseline240-broken-spectrum.json --min-nl 240'
        c['evidence']=list(dict.fromkeys(c['evidence']+['results/baseline240-broken-spectrum.json']))

def add(cid,statement,evidence,verify,check,control):
    data['claims'].append(dict(cid=cid,statement=statement,type='computation',scope='sub-question',
        evidence=list(dict.fromkeys(evidence)),verify_command=verify,check_command=check,control_command=control))

source=['code/seeds.py','selection-inputs/literature/kavut-yucel.reader.md']
hyper=['radius-six-proof.md','seed-and-local-proof.md','code/radius6_hypergraph.py',
       'code/check_radius6_hypergraph.py','code/extra_seeds.py']+source
add('radius-six-compact-exclusion',
    'The three explicit Section 3.1 seeds have no exact-six modification with all Walsh magnitudes <=28 and any Walsh zero. Independent exhaustive hypergraph enumeration covers all 22238720 triples and all six-set extensions per seed: 195 candidates, 120 preserving all bounds, zero with a Walsh zero. With the separate radius-four exclusion and parity, this excludes balanced NL>=242 throughout radius six followed by any linear output addition. Original forced distances:6,6,14; shifted minimum:2 each. Missing old LRAT proofs are not used.',
    hyper+['code/radius6_controls.py','code/replay_radius6.py','results/radius2.json','results/radius4.json']+
    [f'results/{s}-radius6-hypergraph{t}' for s in ('dsbf40','dsbf32','rsbf56') for t in ('.json.gz','-audit.json')],
    'python3 code/replay_radius6.py','python3 code/replay_radius6.py --independent',
    'python3 code/check_radius6_hypergraph.py results/dsbf40-radius6-hypergraph.json.gz --broken')
add('two-preserved-flat-certificates',
    'Exactly two specified classes have exact balanced maximum 240, allowing arbitrary changes on their domains and every linear output addition: dsbf40 on 5+span(27,45,195,325,1,2), 64 free points; dsbf32 on span(63,90,139,278,1,2,4), 128 free points. Each has a universally audited integer-FWHT encoding and independently checked LRAT empty-clause certificate, plus a checked bound-32 planted SAT model and balanced NL240 attainer. The former twelve-quarter-class assertion is withdrawn.',
    ['compact-flat-proof.md','degree-bound-proof.md','code/replay_compact_flats.py','code/free_flat_sat.py','code/local_sat.py','code/audit_free_flat.py','code/check_lrat.py','code/check_witness.py']+source+
    ['results/dsbf40-flat-attainer.json','results/dsbf32-free128-origin0-control-balanced-attainer.json','results/continuation-free64-control-input.json','results/dsbf32-free128-origin0-control-input.json','logs/continuation-free64-control-solver.log','logs/dsbf32-free128-origin0-control-solver.log']+
    [p+t for p in ('results/dsbf40-free64','results/dsbf32-free128-origin0') for t in ('.cnf.gz','.encoding.json.gz','.lrat.gz')]+
    [p+t for p in ('results/continuation-free64-control','results/dsbf32-free128-origin0-control') for t in ('.cnf.gz','.encoding.json.gz')],
    'python3 code/replay_compact_flats.py','python3 code/replay_compact_flats.py --independent',
    'python3 code/audit_free_flat.py results/dsbf32-free128-origin0 --broken')
add('extra-seed-neighborhoods',
    'For the explicit Section 4 tables perm104-ac48 and perm74-ac64 in code/extra_seeds.py, no distance<=6 modification followed by any linear output shift is balanced with NL>=242. All pairs, triples and six-extensions are independently exhausted. No pairs or fours preserve bound 28; there are no saturated-constraint six-candidates. Weights:270,246; original forced balancing distances:14,10; shifted minima:2 each. Indicators 48,64 distinguish these seeds from each other and from the original three. This excludes explicit neighborhoods, not entire symmetry classes.',
    hyper+['extra-seed-proof.md','code/extra_seed_search.py','code/check_extra_seed_search.py','code/replay_extra_neighborhoods.py','code/radius2.py','code/radius4.py','results/extra-seed-neighborhoods.json']+
    [f'results/{s}-radius6-hypergraph{t}' for s in ('perm104-ac48','perm74-ac64') for t in ('.json.gz','-audit.json')],
    'python3 code/replay_extra_neighborhoods.py','python3 code/replay_extra_neighborhoods.py --independent',
    'python3 code/check_extra_seed_search.py --broken')
add('fixed-half-screen',
    'For an odd-weight eight-variable restriction g with spectrum G, any completion with max|W|<=28 and a Walsh zero requires max|G|<=26 and ||G||_1<=3570+max{|G(b)|:|G(b)|<=14}. The self-contained proof applied to all 31744 listed pairs from 124 explicit balanced NL240 sources proves exact balanced maximum 240 in 31492 specified 256-free-point classes, allowing every linear output addition. The remaining 252 classes are unresolved by this screen. Every source and restriction is independently checked by direct sums; every class has an NL240 attainer and a bound-32 planted control. Classes can overlap and are not claimed affine-inequivalent. This is not a global exclusion.',
    ['slice-reduction-proof.md','results/slice-screen.json.gz','results/slice-screen-audit.json','code/slice_screen.py','code/check_slice_screen.py','code/seeds.py','results/continuation-heuristic-starts.json','results/continuation-heuristic-best-tail.json']+
    [f'results/{s}-flat-attainer.json' for s in ('dsbf40','dsbf32','rsbf56')],
    'python3 code/slice_screen.py --compare','python3 code/check_slice_screen.py','python3 code/check_slice_screen.py --broken')
data.update(outcome='partial',summary='The headline balanced nine-variable NL242 question is unresolved. Verified scoped results give the elementary global alternatives {240,242}, degree-eight necessity, radius-six exclusions around five inequivalent explicit seeds, restricted 16/32/64/128-point maxima 240, and exact maximum 240 in 31492 listed fixed-half classes. The other 252 screened half-classes remain unresolved. Missing historical certificates are not used. Novelty is unknown.',
 next_step='Search the 252 explicit half-classes passing the necessary-condition screen, or develop a construction/proof for arbitrary degree-eight tables. UNKNOWN and uncertified negative statuses imply no exclusion; global maximum 240 versus 242 is unresolved in this attempt.')
tmp=Path('claims.json.tmp'); tmp.write_text(json.dumps(data,indent=2)+'\n'); tmp.replace('claims.json')
print('Recorded',len(data['claims']),'scoped claims atomically.')
