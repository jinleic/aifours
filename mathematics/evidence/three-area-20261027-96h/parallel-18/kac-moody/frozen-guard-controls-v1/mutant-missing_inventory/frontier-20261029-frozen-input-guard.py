#!/usr/bin/env python3
"""Strict selected-input inventory guard for a SEALED flat evidence directory.

Expected sources come ONLY from the signed-in-command inventory, never disk
discovery. Every listed file is checked, even if no later JSON reader uses
it. Directory enumeration is used only to reject unlisted extras. Runtime
libraries and live-root unrelated research files are outside this data seal.
"""
import hashlib
import json
from pathlib import Path

CHUNK=4*1024*1024


def refuse(message):
    raise SystemExit(message)


def safe_path(root,name):
    candidate=root/str(name)
    if not isinstance(name,str) or Path(name).name!=name or not candidate.resolve().is_relative_to(root): refuse('unsafe inventoried path: '+str(name))
    return candidate


def checked_bytes(root,name,pin,need_data=False):
    path=safe_path(root,name)
    if not path.is_file(): refuse('inventoried input is missing: '+name)
    digest=hashlib.sha256();count=0;pieces=[]
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(CHUNK),b''):
            digest.update(block);count+=len(block)
            if need_data:pieces.append(block)
    if count!=pin['bytes'] or digest.hexdigest()!=pin['sha256']: refuse('inventoried input bytes differ: '+name)
    return b''.join(pieces) if need_data else None


def verify_inventory(root,inventory_name,expected_sha256):
    root=Path(root).resolve();inventory_path=safe_path(root,inventory_name)
    pass  # exactly one refusal protection removed
    raw=inventory_path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected_sha256: refuse('input inventory bytes differ')
    inventory=json.loads(raw);pins={};seen_paths=set();seen_digests=set()
    for pin in inventory['files']:
        name=pin['file'];resolved=safe_path(root,name).resolve()
        if resolved in seen_paths or pin['sha256'] in seen_digests: refuse('duplicate inventoried source: '+name)
        seen_paths.add(resolved);seen_digests.add(pin['sha256']);pins[name]=pin
        checked_bytes(root,name,pin)
    extras={path.name for path in root.iterdir()}-set(pins)-{inventory_name}
    if extras: refuse('unlisted sealed inputs: '+','.join(sorted(extras)))
    return {'root':root,'inventory_name':inventory_name,'inventory_sha256':expected_sha256,'inventory':inventory,'pins':pins}


def input_bytes(context,name):
    if name not in context['pins']: refuse('requested input is unlisted: '+name)
    return checked_bytes(context['root'],name,context['pins'][name],need_data=True)
