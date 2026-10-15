#!/usr/bin/env python3
"""Expand the transcribed Denniston base schedule and run the independent checker.
Run from the target directory: python3 work/reproduce_denniston15.py
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
source = root / "sources/denniston15-base.txt"
base = []
for raw in source.read_text().splitlines():
    line = raw.partition("#")[0].strip()
    if line:
        base.append([tuple(ord(letter)-ord("A") for letter in triple) for triple in line.split()])
certificate = root / "evidence/denniston15.txt"
with certificate.open("w") as f:
    f.write("# Denniston base table, A..M=0..12, N=13, O=14\nLKTS 15\n")
    for shift in range(13):
        f.write(f"\nKTS {shift}\n")
        for ci, parallel in enumerate(base):
            f.write(f"CLASS {ci}\n")
            for block in parallel:
                f.write(" ".join(str((x+shift)%13 if x<13 else x) for x in block)+"\n")
check = subprocess.run([sys.executable, str(root / "work/check_lkts.py"), str(certificate)], capture_output=True, text=True)
(root / "evidence/denniston15.check.json").write_text(check.stdout)
result = {"command": sys.argv, "checker_exit_code": check.returncode,
          "base_source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
          "certificate_sha256": hashlib.sha256(certificate.read_bytes()).hexdigest(),
          "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root / "evidence/denniston15-reproduction.json").write_text(json.dumps(result, indent=2))
print(check.stdout, end="")
if check.returncode:
    print(check.stderr, file=sys.stderr)
sys.exit(check.returncode)
