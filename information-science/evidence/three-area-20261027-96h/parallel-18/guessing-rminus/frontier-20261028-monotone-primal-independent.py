#!/usr/bin/env python3
"""Independent all-original/all-n audit of monotonicity-refined point."""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
root=Path(__file__).resolve().parent
spec=spec_from_file_location('independent',root/'frontier-20261028-all-order-primal-independent.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
mod.PRIMAL=root/'frontier-20261028-source-monotone-primal-frozen.json'
mod.EXPECTED='55afaaa4dc2bdffca9bdc59fcbaf7d4988b58f2a4bdb8a72d06a5eae257502bc'
mod.OUTPUT=root/'frontier-20261028-monotone-primal-independent-result.json'
mod.main()
