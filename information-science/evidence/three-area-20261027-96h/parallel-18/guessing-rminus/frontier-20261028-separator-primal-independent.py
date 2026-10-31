#!/usr/bin/env python3
"""Apply independent original/all-order checks to the separator-refined point."""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
root=Path(__file__).resolve().parent
spec=spec_from_file_location('independent',root/'frontier-20261028-all-order-primal-independent.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
mod.PRIMAL=root/'frontier-20261028-separator-bound-primal.json'
mod.EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
mod.OUTPUT=root/'frontier-20261028-separator-primal-independent-result.json'
mod.main()
