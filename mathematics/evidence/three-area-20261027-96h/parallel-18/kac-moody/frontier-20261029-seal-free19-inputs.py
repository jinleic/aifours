#!/usr/bin/env python3
"""Materialize a selected immutable input snapshot WITHOUT changing originals.

Every destination is created once with exclusive mode. Existing destination
bytes may be preserved only after they match the expected inventory. No
file/directory is deleted. The snapshot inventory is written LAST, only after
every selected source/copy matches the previously pinned digest and byte size.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CHUNK=4*1024*1024


def fingerprint(path):
    h=hashlib.sha256();count=0
    with path.open('rb') as stream:
        for data in iter(lambda:stream.read(CHUNK),b''):h.update(data);count+=len(data)
    return h.hexdigest(),count


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--inventory',required=True);ap.add_argument('--sha256',required=True)
    args=ap.parse_args();assert Path(args.inventory).name==args.inventory
    raw=(ROOT/args.inventory).read_bytes();assert hashlib.sha256(raw).hexdigest()==args.sha256
    I=json.loads(raw);destination=Path(I['sealed_input_root']).resolve()
    assert destination.parent==ROOT.resolve() and destination!=ROOT.resolve()
    if not destination.exists():destination.mkdir()
    names=[];results=[]
    for pin in I['files']:
        name=pin['file'];assert Path(name).name==name and name not in names;names.append(name)
        source=Path(pin['original_path']);assert source.resolve().parent==ROOT.resolve() and source.name==name
        target=destination/name;expected=(pin['sha256'],pin['bytes'])
        if target.exists():
            assert fingerprint(target)==expected,('existing destination differs;preserve it and refuse',name)
            action='preserved_already_matching_copy'
        else:
            assert source.stat().st_size==pin['bytes'],('source size changed',name)
            h=hashlib.sha256();count=0
            with source.open('rb') as reader,target.open('xb') as writer:
                remaining=pin['bytes']
                while remaining:
                    block=reader.read(min(CHUNK,remaining))
                    assert block,('short inventoried source',name)
                    writer.write(block);h.update(block);count+=len(block);remaining-=len(block)
                assert not reader.read(1),('source grew during snapshot',name)
            assert (h.hexdigest(),count)==expected,('source bytes differ from prior pin',name)
            assert fingerprint(target)==expected,('snapshot copy mismatch',name)
            action='copied_and_reverified'
        results.append({'file':name,'sha256':pin['sha256'],'bytes':pin['bytes'],'action':action})
    extras={p.name for p in destination.iterdir()}-set(names)-{args.inventory}
    assert not extras,('unlisted snapshot entries',sorted(extras))
    inv_target=destination/args.inventory
    if inv_target.exists():assert inv_target.read_bytes()==raw,'existing snapshot inventory differs'
    else:
        with inv_target.open('xb') as stream:stream.write(raw)
    receipt={'owner':'MathKacMoody-2','inventory':{'file':args.inventory,'sha256':args.sha256},'sealed_input_root':str(destination),
        'selected_files':len(results),'total_bytes':sum(r['bytes'] for r in results),'files':results,
        'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'status':'PASS_SELECTED_INPUT_SNAPSHOT_MATERIALIZED_AND_REVERIFIED',
        'limits':'Byte preservation/integrity only,not mathematical or scientific adoption. Broader manifests and nonselected live-root files are not verified by this snapshot. No originals changed or files deleted.'}
    out=ROOT/'frontier-20261029-level7-free19-seal-copy-receipt-v1.json'
    with out.open('x') as stream:json.dump(receipt,stream,indent=2);stream.write('\n')
    print('PASS sealed selected inputs',len(results),'bytes',receipt['total_bytes'],out.name,flush=True)


if __name__=='__main__':main()
