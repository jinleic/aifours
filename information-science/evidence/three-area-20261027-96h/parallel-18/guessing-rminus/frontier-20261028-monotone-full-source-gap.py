#!/usr/bin/env python3
"""Exactly audit all evaluable source-branch rows on monotone point."""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
root=Path(__file__).resolve().parent
spec=spec_from_file_location('gap',root/'frontier-20261028-all-order-full-source-gap.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
mod.INPUT=root/'frontier-20261028-source-monotone-primal-frozen.json'
mod.EXPECTED='55afaaa4dc2bdffca9bdc59fcbaf7d4988b58f2a4bdb8a72d06a5eae257502bc'
mod.OUTPUT=root/'frontier-20261028-monotone-full-source-gap-result.json'
mod.main()
