#!/usr/bin/env python3
"""Apply the independent full original/all-order check to the stronger point."""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
root=Path(__file__).resolve().parent
spec=spec_from_file_location('independent',root/'frontier-20261028-all-order-primal-independent.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
mod.PRIMAL=root/'frontier-20261028-source-closure-primal-frozen.json'
mod.EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
mod.OUTPUT=root/'frontier-20261028-closure-primal-independent-result.json'
mod.main()
