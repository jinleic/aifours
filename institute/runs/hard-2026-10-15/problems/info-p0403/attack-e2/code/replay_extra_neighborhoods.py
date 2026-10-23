"""Complete pair/four/six exclusions around exactly two additional tables."""
import argparse
import subprocess

p=argparse.ArgumentParser()
p.add_argument('--independent',action='store_true')
a=p.parse_args()
subprocess.run(['python3','code/check_extra_seed_search.py'] if a.independent else
               ['python3','code/extra_seed_search.py','--compare'],check=True)
for seed in ('perm104-ac48','perm74-ac64'):
    result='results/%s-radius6-hypergraph.json.gz'%seed
    subprocess.run(['python3','code/check_radius6_hypergraph.py',result] if a.independent else
                   ['python3','code/radius6_hypergraph.py','--seed',seed,'--output',result,'--compare'],check=True)
print('PASS complete neighborhoods through radius six for the two additional explicit Section 4 tables.')
