#!/usr/bin/env python3
"""Exactly audit evaluable source-branch rows on separator-refined point."""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
root=Path(__file__).resolve().parent
spec=spec_from_file_location('gap',root/'frontier-20261028-all-order-full-source-gap.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
mod.INPUT=root/'frontier-20261028-separator-bound-primal.json'
mod.EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
mod.OUTPUT=root/'frontier-20261028-separator-full-source-gap-result.json'
mod.main()
