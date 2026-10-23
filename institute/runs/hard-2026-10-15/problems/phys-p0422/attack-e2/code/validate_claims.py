"""Validate this directory's small JSON schema vocabulary and evidence paths.

No third-party modules are required. Reject unknown schema assertions rather
than silently ignoring them. This checks structure, not mathematical truth.
"""
import json
from pathlib import Path


def validate(value, schema, location='$'):
    supported = {'type','additionalProperties','properties','required','enum','items','description'}
    assert set(schema) <= supported, f'Unsupported schema at {location}'
    kind = schema.get('type')
    expected = {'object':dict,'array':list,'string':str}
    if kind:
        assert type(value) is expected[kind], f'{location}: wrong type, expected {kind}'
    if 'enum' in schema:
        assert value in schema['enum'], f'{location}: value outside enum'
    if isinstance(value,dict):
        assert set(schema.get('required',[])) <= set(value), f'{location}: missing required fields'
        if schema.get('additionalProperties') is False:
            assert set(value) <= set(schema.get('properties',{})), f'{location}: extra fields'
        for key, sub in schema.get('properties',{}).items():
            if key in value:
                validate(value[key],sub,f'{location}.{key}')
    if isinstance(value,list) and 'items' in schema:
        for i, subvalue in enumerate(value):
            validate(subvalue,schema['items'],f'{location}[{i}]')


def main():
    ledger=json.loads(Path('claims.json').read_text())
    schema=json.loads(Path('claims.schema.json').read_text())
    validate(ledger,schema)
    seen=set()
    for claim in ledger['claims']:
        assert claim['cid'] not in seen, 'Duplicate cid'
        seen.add(claim['cid'])
        for filename in claim['evidence']:
            path=Path(filename)
            assert not path.is_absolute() and '..' not in path.parts, 'Evidence outside current directory'
            assert path.is_file(), f'Missing evidence: {filename}'
        for key in ('verify_command','check_command','control_command'):
            cmd=claim[key]
            assert not cmd or cmd.startswith('python3 '), f'Unexpected replay command: {cmd}'
    print(f"PASS claims.schema.json: outcome={ledger['outcome']}; {len(ledger['claims'])} claims; evidence exists.")


if __name__=='__main__':
    main()
