"""Validate claims.json against the staged JSON Schema (standard library).

Supports all schema features actually present in claims.schema.json;
also checks evidence paths and the replay command restriction.
"""
import hashlib
import json
from pathlib import Path


def validate(value,schema,where='$'):
    typ=schema.get('type')
    if typ=='object':
        assert type(value) is dict,(where,'object')
        assert set(schema.get('required',[]))<=set(value),(where,'missing required')
        props=schema.get('properties',{})
        if schema.get('additionalProperties') is False:
            assert set(value)<=set(props),(where,'additional properties')
        for k,v in value.items():
            if k in props: validate(v,props[k],where+'.'+k)
    elif typ=='array':
        assert type(value) is list,(where,'array')
        for i,v in enumerate(value): validate(v,schema['items'],where+'[%d]'%i)
    elif typ=='string': assert type(value) is str,(where,'string')
    else: raise AssertionError(('unsupported schema feature',where,typ))
    if 'enum' in schema: assert value in schema['enum'],(where,'enum')


data=json.loads(Path('claims.json').read_text())
schema=json.loads(Path('claims.schema.json').read_text())
validate(data,schema)
assert len({c['cid'] for c in data['claims']})==len(data['claims'])
for claim in data['claims']:
    for name in claim['evidence']:
        p=Path(name)
        assert not p.is_absolute() and '..' not in p.parts
        assert p.is_file(),(claim['cid'],'missing evidence',name)
    for field in ('verify_command','check_command','control_command'):
        cmd=claim[field]
        assert not cmd or cmd.startswith('python3 '),(claim['cid'],field,'not Python replay')
assert data['outcome']=='partial'
assert all(c['scope']!='headline' for c in data['claims'])
result={'status':'PASS','schema_sha256':hashlib.sha256(Path('claims.schema.json').read_bytes()).hexdigest(),'claims_sha256':hashlib.sha256(Path('claims.json').read_bytes()).hexdigest(),'outcome':data['outcome'],'claim_count':len(data['claims']),'evidence_paths_exist':True,'all_nonempty_commands_use_python3':True}
Path('results/claims-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
