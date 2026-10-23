"""Replay compact radius-six enumeration or its independent audit."""
import argparse
import subprocess

p=argparse.ArgumentParser()
p.add_argument('--independent',action='store_true')
a=p.parse_args()
for seed in ('dsbf40','dsbf32','rsbf56'):
    result='results/%s-radius6-hypergraph.json.gz'%seed
    command=(['python3','code/check_radius6_hypergraph.py',result] if a.independent else
             ['python3','code/radius6_hypergraph.py','--seed',seed,'--output',result,'--compare'])
    subprocess.run(command,check=True)
if not a.independent:
    subprocess.run(['python3','code/radius6_controls.py'],check=True)
print('PASS exact-six exclusions for all three explicit seeds; lower radii are a separate claim.')
