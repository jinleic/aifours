#!/usr/bin/env python3
"""Rerun the inspected independently rebuilt d=4 orbit checker to a new path.

This is a parent execution of the existing author-written independent checker,
not an independent implementation. It does not prove the physical bridge or
positive semidefiniteness of the corrected matrices.
"""
import hashlib
import importlib.util
import os
import sys
from pathlib import Path

SOURCE = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-independent-d4-global-identity-check.py')
OUTPUT = Path(__file__).with_name('parent-global-identity-result-v1.json')
EXPECTED_SOURCE = 'b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'


def main():
    if OUTPUT.exists():
        raise FileExistsError(OUTPUT)
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != EXPECTED_SOURCE:
        raise ValueError('source SHA-256 mismatch')
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    spec = importlib.util.spec_from_file_location('parent_d4_global', SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.OUT = OUTPUT
    return module.main()


if __name__ == '__main__':
    sys.exit(main())
