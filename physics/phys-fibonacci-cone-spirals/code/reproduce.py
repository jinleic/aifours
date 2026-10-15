#!/usr/bin/env python3
"""Recreate the fixed witness, exact certificate, and non-certifying controls."""
from pathlib import Path
import subprocess
import sys

CODE = Path(__file__).resolve().parent
for filename, options in (("generate_witness.py", []), ("verify.py", ["--write"]), ("diagnostics.py", [])):
    subprocess.run([sys.executable, str(CODE / filename), *options], check=True)
