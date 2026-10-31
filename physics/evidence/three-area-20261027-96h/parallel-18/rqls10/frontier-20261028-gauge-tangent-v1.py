#!/usr/bin/env python3
"""Add exact first-row/phase gauges to the existing integer tangent systems."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
cert=json.loads((ROOT/'frontier-20261028-parker-13ray-result-v1.json').read_text())['partial_witness']
a=cert['array']
rotated=next((r,c) for r in range(1,10) for c in range(10)
             if all(a[r][c][k] for k in (7,8,9)) and all(a[r][c][k]==0 for k in range(7)))
for kind in ('real','imag'):
    src=ROOT/f'frontier-20261028-parker13-tangent-{kind}-v2.txt'
    lines=src.read_text().splitlines()
    oldrows,cols=map(int,lines[0].split())
    assert cols==1000 and len(lines)==oldrows+1
    rows=lines[1:]
    # First actual ONB has zero complex variation after common-unitary gauge.
    rows += [f'1 {i} 1' for i in range(100)]
    if kind=='imag':
        # Fix per-cell phases for all other cells: v_x dot Im(delta_x)=0.
        for r in range(1,10):
            for c in range(10):
                v=a[r][c]
                entries=[(10*(10*r+c)+k,z) for k,z in enumerate(v) if z]
                rows.append(str(len(entries))+''.join(f' {j} {z}' for j,z in entries))
        # Kill the two remaining diagonal-unitary directions on the embedded 3-space.
        x=10*rotated[0]+rotated[1]
        rows += [f'1 {10*x+7} 1',f'1 {10*x+8} 1']
    target=ROOT/f'frontier-20261028-parker13-tangent-{kind}-gauge-v1.txt'
    target.write_text(f'{len(rows)} {cols}\n'+'\n'.join(rows)+'\n')
    print(kind,'original_rows',oldrows,'gauge_rows',len(rows)-oldrows,'output',target.name)
print('rotated cell used for residual diagonal gauge',rotated)
