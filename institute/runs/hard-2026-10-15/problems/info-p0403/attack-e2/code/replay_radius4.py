"""Replay the compact small neighborhoods and a planted solvable control."""
import argparse
import os
import subprocess

os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
p=argparse.ArgumentParser()
p.add_argument('--independent',action='store_true')
a=p.parse_args()
commands = ([['python3','code/check_radius2.py'],['python3','code/check_radius4.py']]
            if a.independent else
            [['python3','code/radius2.py','--compare'],['python3','code/radius4.py','--compare'],
             ['python3','code/controls.py','planted']])
for command in commands:
    subprocess.run(command,check=True)
print('PASS complete neighborhoods through radius four')
