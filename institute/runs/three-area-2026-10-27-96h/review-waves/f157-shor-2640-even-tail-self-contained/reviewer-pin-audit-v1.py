#!/usr/bin/env python3
"""Metadata and literal-source inspection only; never execute imported sources."""
import datetime, hashlib, json, pathlib, re
ROOT=pathlib.Path(__file__).resolve().parent
CAND=pathlib.Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261028-2640-even-tail-self-contained-review-v1.md')
raw=CAND.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='53296d698836288dc2354e1fb24e4c25f35b2c67454590b4d5a173134bd4706a'
assert len(raw)==38065 and raw.count(b'\n')==262
pins=[]
for line in raw.decode().splitlines():
    m=re.fullmatch(r'\| `([^`]+)` \| `([0-9a-f]{64})` \| ([0-9]+) / ([0-9]+) \| (.*) \|',line)
    if m:
        name,sha,lf,size,purpose=m.groups()
        b=(CAND.parent/name).read_bytes()
        actual={'name':name,'sha256':hashlib.sha256(b).hexdigest(),'LF':b.count(b'\n'),'bytes':len(b),'trailing_LF':b.endswith(b'\n')}
        assert actual['sha256']==sha,(name,'hash',actual)
        assert actual['LF']==int(lf),(name,'LF',actual)
        assert actual['bytes']==int(size),(name,'bytes',actual)
        b.decode('utf-8')
        pins.append((actual,b))
assert len(pins)==28,len(pins)
receipt={'observed_utc_before_writes':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_candidate':{'sha256':hashlib.sha256(raw).hexdigest(),'LF':262,'bytes':38065},'pins':[p for p,b in pins],'executed_author_programs':False}
text=[]
for p,b in pins:
    text.append('### '+p['name']+' SHA256='+p['sha256']+' LF='+str(p['LF'])+' bytes='+str(p['bytes'])+'\n')
    text.extend(str(i)+'|'+line+'\n' for i,line in enumerate(b.decode().splitlines(),1))
    text.append('\n')
for name,content in [('reviewer-pinned-dependency-audit-v1.json',json.dumps(receipt,indent=2)+'\n'),('reviewer-pinned-dependency-render-v1.txt',''.join(text))]:
    with (ROOT/name).open('x') as f:
        f.write(content)
    print(name,hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),(ROOT/name).stat().st_size)
print('verified_pins',len(pins))
