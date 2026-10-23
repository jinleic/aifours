#!/usr/bin/env python3
"""moqls7-k1-delta-v1 source fetch (delegated parent delta check). Read-only HTTPS GETs of three arXiv PDFs into
memory; text via pdftotext reading stdin (no PDF or text file is written); records hashes and whether each anchor
passage is present. Verbatim text is limited to short anchors (<= 40 words each). Prints a JSON receipt."""
import datetime, hashlib, json, os, re, subprocess, sys, urllib.request
from zoneinfo import ZoneInfo

SOURCES = {
    'ZC_2608.29201v2': 'https://arxiv.org/pdf/2608.29201v2',
    'HL_2606.27758v1': 'https://arxiv.org/pdf/2606.27758v1',
    'BS36_2603.02334v1': 'https://arxiv.org/pdf/2603.02334v1',
}
# (source, id, regex on whitespace-normalised text, max words kept)
ANCHORS = [
    ('ZC_2608.29201v2', 'ZC_def_1_1_resolvable', r'A QLS\(v\) is called t-resolvable', 6),
    ('ZC_2608.29201v2', 'ZC_def_1_1_one_cell', r'such that \|Ti \u2229 Tj \| = 1 for all r, s \u2208 \[t\] with r 6= s', 16),
    ('ZC_2608.29201v2', 'ZC_cardinality_def', r'The cardinality c of a QLS\(v\) is the number of distinct vectors in the array\.', 16),
    ('ZC_2608.29201v2', 'ZC_nonclassical_def', r'A QLS\(v\) is called nonclassical if c > v\.', 10),
    ('ZC_2608.29201v2', 'ZC_identical_up_to_phase', r'regarded as identical', 4),
    ('ZC_2608.29201v2', 'ZC_HL_pandiagonal_is_2RQLS', r'pandiagonal quantum Latin square of odd order v which is a 2-RQLS\(v\)\.', 14),
    ('ZC_2608.29201v2', 'ZC_thm_1_2_3', r'\(3\) For any v \u2208 / \{5, 7, 11\} and gcd\(v, 6\) = 1 there exists a maximal-cardinality 2-RQLS\(v\)\.', 18),
    ('ZC_2608.29201v2', 'ZC_lemma_2_2_statement', r'Lemma 2\.2\. A is a t-RQLS\(v\) if and only if there exist t classical QLS\(v\)s, B0 , \. \. \. , Bt\u22121 , such that A, B0 , \. \. \. , Bt\u22121 form a \(t \+ 1\)-MOQLS\(v\)\.', 40),
    ('ZC_2608.29201v2', 'ZC_s5_2RQLS_remaining', r'For maximal-cardinality 2-RQLS\(v\)s, the known result at present are gcd\(v, 6\) = 1 and v\u2208 / \{5, 7, 11\} or v = n2 for all n \u2265 6\. It remains to determine the existence of maximalcardinality 2-RQLS\(v\)s for the remaining orders\.', 40),
    ('HL_2606.27758v1', 'HL_cardinality_def', r'The cardinality c of a QLS\(n\) is the number of distinct \(up to a global phase\) vectors in the array\.', 19),
    ('HL_2606.27758v1', 'HL_transversal_def', r'a transversal in a QLS\(n\) refers to a set of n cells, no two in the same row or column, the vectors in these cells forming an orthonormal basis', 28),
    ('HL_2606.27758v1', 'HL_PQLS_def', r'A QLS\(n\) is called a pandiagonal quantum Latin square, denoted as PQLS\(n\), if its main diagonal, anti-diagonal, and all broken diagonals in both directions are each a transversal\.', 28),
    ('HL_2606.27758v1', 'HL_s5_heading', r'5 Conclusion', 2),
    ('HL_2606.27758v1', 'HL_s5_MCPQLS7_undetermined', r'Here, an MCPQLS\(5\) does not exist, and the existence of MCPQLS\(7\), MCPQLS\(11\), and MCPQLS\(n\) with gcd\(n, 6\) \u0338?= 1 remains to be determined\.', 24),
    ('HL_2606.27758v1', 'HL_thm_2_15', r'There exists an MCPQLS\(v\) if gcd\(n, 6\) = 1 and v \u0338?\u2208 ?\{5, 7, 11\}', 14),
    ('BS36_2603.02334v1', 'BS36_s4_2_heading', r'4\.2 Checking twelve cases', 4),
    ('BS36_2603.02334v1', 'BS36_lemma_21', r'Lemma 21\. There exist 2 MOQLS\(6\) if and only if there is a Latin square graph on 6 \u00d7 6 vertices whose complement has an orthonormal representation in C6', 30),
]


def now():
    return datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def main():
    env = dict(os.environ)
    env['TMPDIR'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')
    ver = subprocess.run(['pdftotext', '-v'], capture_output=True, text=True, env=env)
    rec = {'started_at_pt': now(), 'pdftotext_version': (ver.stdout + ver.stderr).splitlines()[0],
           'pdftotext_argv': ['pdftotext', '-q', '-enc', 'UTF-8', '-', '-'], 'TMPDIR': env['TMPDIR'], 'sources': {},
           'anchors': []}
    norm = {}
    for key, url in SOURCES.items():
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (read-only review fetch)'})
        t = now()
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read()
            info = {'url': url, 'fetched_at_pt': t, 'http_status': r.status, 'final_url': r.geturl(),
                    'content_type': r.headers.get('Content-Type'), 'bytes': len(body),
                    'sha256': hashlib.sha256(body).hexdigest()}
        p = subprocess.run(['pdftotext', '-q', '-enc', 'UTF-8', '-', '-'], input=body, capture_output=True, env=env,
                           timeout=300)
        text = p.stdout.decode('utf-8', 'replace')
        info['pdftotext_returncode'] = p.returncode
        norm[key] = re.sub(r'\s+', ' ', text)
        info['normalised_text_sha256'] = hashlib.sha256(norm[key].encode()).hexdigest()
        rec['sources'][key] = info
    for key, aid, pat, maxw in ANCHORS:
        m = re.search(pat, norm[key])
        entry = {'source': key, 'id': aid, 'found': bool(m)}
        if m:
            words = m.group(0).split(' ')
            entry['offset'] = m.start()
            entry['anchor_text'] = ' '.join(words[:maxw])
            entry['anchor_words'] = min(len(words), maxw)
            entry['truncated'] = len(words) > maxw
        rec['anchors'].append(entry)
    rec['all_anchors_found'] = all(a['found'] for a in rec['anchors'])
    rec['tmp_listing_after'] = sorted(os.listdir(env['TMPDIR']))
    rec['finished_at_pt'] = now()
    json.dump(rec, sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write('\n')
    return 0 if rec['all_anchors_found'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
