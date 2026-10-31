#!/usr/bin/env python3
"""Repeat the bounded verified-support search with finer rationalization."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

here = Path(__file__).resolve().parent
spec = spec_from_file_location('frontier_law_search', here / 'frontier-20261028-fd-law-search.py')
module = module_from_spec(spec)
spec.loader.exec_module(module)
module.OUTPUT = here / 'frontier-20261028-fd-law-search-precise-result.json'
module.RATIONAL_TOTAL = 6000
module.MAX_ITERATIONS_PER_RESTART = 12000
module.TIME_LIMIT_SECONDS = 25.0
module.main()
