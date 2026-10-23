"""Replay the restricted 32-free-point family maximum and its audit."""
import argparse
import subprocess

p=argparse.ArgumentParser()
p.add_argument('--independent',action='store_true')
a=p.parse_args()
for seed in ('dsbf40','dsbf32','rsbf56'):
    if not a.independent:
        subprocess.run(['python3','code/two_coset.py','--seed',seed,'--pairs','all','--output','results/%s-two-cosets.json'%seed,'--compare'],check=True)
    subprocess.run(['python3','code/check_two_coset.py','results/%s-two-cosets.json'%seed],check=True)
print('PASS three complete 32-free-point class union maxima: balanced NL=240')
