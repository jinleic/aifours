#!/usr/bin/env python3
"""Recheck all evaluable full-source rows of the stronger frozen point."""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
root=Path(__file__).resolve().parent
spec=spec_from_file_location('gap',root/'frontier-20261028-all-order-full-source-gap.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
mod.INPUT=root/'frontier-20261028-source-closure-primal-frozen.json'
mod.EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
mod.OUTPUT=root/'frontier-20261028-closure-full-source-gap-result.json'
mod.main()
