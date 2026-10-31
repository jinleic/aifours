#!/usr/bin/env python3
"""Synthetic initial-state controls; no originals or frozen fixtures edited.

Each test builds a NEW variant. Missing evidence is omitted at construction,
not deleted. All tempfile directories are inside the exclusive owner root
and retained. Mutant drivers may select one fresh helper copy via the env.
"""
import hashlib
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path

OWNER=Path(os.environ['KAC_EXCLUSIVE_ROOT']).resolve()
BASE=Path(os.environ['KAC_GUARD_CONTROL_ROOT']).resolve()
assert BASE.is_relative_to(OWNER)
BASE.mkdir(parents=True,exist_ok=True)
MODULE=Path(os.environ.get('KAC_GUARD_MODULE',str(OWNER/'frontier-20261029-frozen-input-guard.py')))
assert MODULE.resolve().is_relative_to(OWNER)
spec=importlib.util.spec_from_file_location('tested_frozen_guard',MODULE)
G=importlib.util.module_from_spec(spec);spec.loader.exec_module(G)


def make_fixture(mode='good'):
    case=Path(tempfile.mkdtemp(prefix='guard-',dir=BASE));root=case/'input';root.mkdir()
    expected={'a.bin':b'one','b.json':b'{"ok":1}\n'}
    pins=[{'file':n,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)} for n,b in expected.items()]
    actual=dict(expected)
    if mode in ('missing','alias_only'):actual.pop('a.bin')
    if mode=='changed':actual['a.bin']=b'ONE'
    if mode=='extra':actual['foreign.json']=b'foreign'
    if mode=='alias_only':actual['a-copy.bin']=expected['a.bin']
    if mode=='duplicate_path':pins.append(dict(pins[0]))
    if mode=='duplicate_path_distinct_pin':
        alternate=b'ONE';pins.append({'file':'a.bin','sha256':hashlib.sha256(alternate).hexdigest(),'bytes':len(alternate)})
    if mode=='duplicate_digest':
        actual['same.bin']=expected['a.bin'];pins.append({'file':'same.bin','sha256':pins[0]['sha256'],'bytes':len(expected['a.bin'])})
    if mode=='symlink_escape':
        actual={};outside=case/'outside.bin';outside.write_bytes(expected['a.bin'])
        (root/'alias.bin').symlink_to(outside)
        pins=[{'file':'alias.bin','sha256':hashlib.sha256(expected['a.bin']).hexdigest(),'bytes':len(expected['a.bin'])}]
    for n,b in actual.items():
        with (root/n).open('xb') as stream:stream.write(b)
    inventory=(json.dumps({'files':pins},sort_keys=True)+'\n').encode()
    if mode!='missing_inventory':
        with (root/'inventory.json').open('xb') as stream:stream.write(inventory)
    return root,hashlib.sha256(inventory).hexdigest(),case/'output.json'


class GuardTests(unittest.TestCase):
    def rejected(self,mode,message,wrong_pin=False,request=None):
        root,sha,out=make_fixture(mode)
        with self.assertRaisesRegex(SystemExit,message):
            ctx=G.verify_inventory(root,'inventory.json','0'*64 if wrong_pin else sha)
            if request is not None:G.input_bytes(ctx,request)
            with out.open('x') as stream:stream.write('should not be written')
        self.assertFalse(out.exists(),'a refused fixture wrote an output')

    def test_valid_inventory_and_registered_read(self):
        root,sha,out=make_fixture()
        ctx=G.verify_inventory(root,'inventory.json',sha)
        self.assertEqual(G.input_bytes(ctx,'b.json'),b'{"ok":1}\n')
        with out.open('x') as stream:stream.write('accepted synthetic fixture')
        self.assertTrue(out.exists())

    def test_missing_inventory(self):
        self.rejected('missing_inventory','input inventory is missing')

    def test_changed_inventory_pin(self):
        self.rejected('good','input inventory bytes differ',wrong_pin=True)

    def test_missing_listed_file(self):
        self.rejected('missing','inventoried input is missing: a.bin')

    def test_changed_listed_bytes(self):
        self.rejected('changed','inventoried input bytes differ: a.bin')

    def test_unlisted_file(self):
        self.rejected('extra','unlisted sealed inputs: foreign.json')

    def test_duplicate_resolved_path(self):
        self.rejected('duplicate_path','duplicate inventoried source: a.bin')

    def test_duplicate_path_despite_distinct_expected_digest(self):
        self.rejected('duplicate_path_distinct_pin','duplicate inventoried source: a.bin')

    def test_duplicate_digest(self):
        self.rejected('duplicate_digest','duplicate inventoried source: same.bin')

    def test_symlink_escape(self):
        self.rejected('symlink_escape','unsafe inventoried path: alias.bin')

    def test_unlisted_requested_input(self):
        self.rejected('good','requested input is unlisted: ghost.json',request='ghost.json')

    def test_unlisted_copy_cannot_cure_missing_source(self):
        self.rejected('alias_only','inventoried input is missing: a.bin')


if __name__=='__main__':unittest.main(verbosity=2)
