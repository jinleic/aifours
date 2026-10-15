"""Fetch public primary-source endpoints, retaining every response in this repository."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
destination = ROOT / ('source-fetch-' + stamp)
destination.mkdir(exist_ok=False)
urls = [
    ('zhao-full-chapter', 'https://link.springer.com/content/pdf/10.1007/978-1-4615-7909-0_41.pdf'),
    ('zhao-preview', 'https://page-one.springer.com/pdf/preview/10.1007/978-1-4615-7909-0_41'),
    ('bai-wu-full', 'https://www.sciencedirect.com/science/article/pii/S0167715296001824/pdfft'),
    ('bai-wu-article-api', 'https://api.elsevier.com/content/article/pii/S0167715296001824?httpAccept=text/xml'),
    ('zhao-openalex', 'https://api.openalex.org/works/https://doi.org/10.1007/978-1-4615-7909-0_41'),
    ('bai-wu-openalex', 'https://api.openalex.org/works/https://doi.org/10.1016/S0167-7152(96)00182-4'),
]

def fetch(item):
    name, url = item
    receipt = {'name': name, 'requested_url': url, 'created_at_utc': stamp}
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0 (academic source verification)'})
        try:
            response = urlopen(request, timeout=25)
        except HTTPError as error:
            response = error
        with response:
            data = response.read()
            receipt.update(status=response.status, final_url=response.geturl(),
                           content_type=response.headers.get('Content-Type'),
                           bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                           begins_pdf=data.startswith(b'%PDF'))
        suffix = '.pdf' if data.startswith(b'%PDF') else '.response'
        body = destination / (name + suffix)
        body.write_bytes(data)
        receipt['body'] = str(body.relative_to(ROOT.parent))
    except Exception as error:
        receipt['error'] = repr(error)
    (destination / (name + '.json')).write_text(json.dumps(receipt, indent=2) + '\n')
    return receipt

with ThreadPoolExecutor(max_workers=2) as executor:
    receipts = list(executor.map(fetch, urls))
(destination / 'index.json').write_text(json.dumps(receipts, indent=2) + '\n')
for receipt in receipts:
    print(json.dumps(receipt))
