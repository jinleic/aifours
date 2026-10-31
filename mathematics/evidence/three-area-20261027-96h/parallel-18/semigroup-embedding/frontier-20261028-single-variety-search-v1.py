#!/usr/bin/env python3
import importlib.util
from pathlib import Path
import sys
p=Path(__file__).with_name('frontier-20261028-local-seminormal-implication-search-v1.py')
s=importlib.util.spec_from_file_location('variety_search',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
mode,n,ms=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]);m.search(n,mode,ms)
