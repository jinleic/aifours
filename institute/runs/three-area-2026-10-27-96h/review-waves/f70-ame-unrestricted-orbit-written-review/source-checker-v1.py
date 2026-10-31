#!/usr/bin/env python3
"""Bind the frozen table and P-prime extension to selected public HTML source."""
import hashlib
import json
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'public-source-excerpts-v1.json'
MANIFEST = HERE / 'manifest-v1.json'
RECEIPT = HERE / 'source-receipt-v1.json'
SOURCE_SHA = '7e0a6b5b23e7af5d1a6fe0ff78a0493b1983326acf03abf6ba1e616c55dfdd19'
MANIFEST_SHA = '58bc6ef69b3bba96616a5a96e19b64d685590380482d537f749c617df0e0661a'


class CheckError(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise CheckError(reason)


def sha(data):
    return hashlib.sha256(data).hexdigest()


class MathElements(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.cell = None
        self.cells = {}
        self.math = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'td':
            cell_id = attrs.get('id', '')
            match = re.fullmatch(r'S2\.T1\.2\.([2-7])\.([2-7])', cell_id)
            self.cell = (int(match[1]) - 2, int(match[2]) - 2) if match else None
        if tag == 'math':
            text = attrs.get('alttext')
            math_id = attrs.get('id')
            if self.cell is not None:
                require(text is not None and self.cell not in self.cells, 'public table cell parsing')
                self.cells[self.cell] = text
            if math_id and math_id.startswith('S4.E6'):
                require(text is not None and math_id not in self.math, 'public Eq6 math parsing')
                self.math[math_id] = text

    def handle_endtag(self, tag):
        if tag == 'td':
            self.cell = None


def parse_public_table(fragment):
    parser = MathElements()
    parser.feed(fragment)
    parser.close()
    require(set(parser.cells) == {(a, b) for a in range(6) for b in range(6)}, 'public table coordinates')
    rows = []
    for a in range(6):
        for b in range(6):
            value = parser.cells[a, b]
            single = re.fullmatch(r'\\sqrt\{2\}\\,\\ket\{([0-5]{2})\}', value)
            if single:
                tokens = ['s' + single[1]]
            else:
                matches = list(re.finditer(r'([+\-]?)\\ket\{([0-5]{2})\}', value))
                require(len(matches) == 2 and ''.join(m[0] for m in matches) == value, 'public table coefficient expression')
                tokens = [(m[1] or '+') + m[2] for m in matches]
            rows.append(' '.join([str(a), str(b)] + tokens))
    return rows


def parse_public_eq6(fragment):
    parser = MathElements()
    parser.feed(fragment)
    parser.close()
    suffixes = ('', 'a', 'b', 'c', 'd', 'e')
    groups = []
    for n, suffix in enumerate(suffixes):
        stem = 'S4.E6X' + suffix
        expected_label = (r'\displaystyle P_{%d}' % (n + 1) if n < 3
                          else r'\displaystyle P^{\prime}_{%d}' % (n - 2))
        require(parser.math.get(stem + '.m2') == expected_label, 'public Eq6 label')
        expression = parser.math.get(stem + '.m3', '')
        match = re.fullmatch(r'\\displaystyle=\\\{([0-5]{4}(?:,[0-5]{4}){3})\\\}[,.]', expression)
        require(match is not None, 'public Eq6 tuple expression')
        groups.append(match[1].split(','))
    return groups[:3], groups[3:]


def check_table(fragment, local_rows):
    public_rows = parse_public_table(fragment)
    require(public_rows == local_rows, 'public source table mismatch')
    return public_rows


def check_eq6(fragment, local_rows, extension):
    p_groups, prime_groups = parse_public_eq6(fragment)
    p_list = sum(p_groups, [])
    prime_list = sum(prime_groups, [])
    table_p = []
    for row in local_rows:
        a, b, *tokens = row.split(' ')
        if len(tokens) == 1 and tokens[0].startswith('s'):
            table_p.append(a + b + tokens[0][1:])
    require(len(p_list) == len(set(p_list)) == 12 and set(p_list) == set(table_p), 'public Eq6 P mismatch')
    match = re.search(r'`([0-5]{4}(?:, [0-5]{4}){11})`', extension)
    require(match is not None, 'extension P prime list not found')
    claimed = match[1].split(', ')
    require(len(prime_list) == len(set(prime_list)) == 12 and prime_list == claimed, 'public Eq6 P prime mismatch')
    return p_groups, prime_groups


def intended_failure(fn, reason):
    try:
        fn()
    except CheckError as exc:
        require(str(exc) == reason, 'unexpected source mutation failure: ' + str(exc))
        return str(exc)
    raise CheckError('source mutation was not detected')


def main():
    require(not RECEIPT.exists(), 'refusing to overwrite source receipt')
    source_bytes = SOURCE.read_bytes()
    manifest_bytes = MANIFEST.read_bytes()
    require(sha(source_bytes) == SOURCE_SHA, 'public excerpt hash mismatch')
    require(sha(manifest_bytes) == MANIFEST_SHA, 'manifest hash mismatch')
    source = json.loads(source_bytes)
    manifest = json.loads(manifest_bytes)
    require(source['url'] == 'https://arxiv.org/html/2610.16673v1', 'public source URL mismatch')
    entries = manifest['inputs_in_read_order']
    table_bytes = Path(entries[0]['path']).read_bytes()
    extension_bytes = Path(entries[2]['path']).read_bytes()
    require(sha(table_bytes) == entries[0]['sha256'], 'table input hash mismatch')
    require(sha(extension_bytes) == entries[2]['sha256'], 'extension input hash mismatch')
    table_rows = [row for row in table_bytes.decode().splitlines() if not row.startswith('#')]
    table_fragment = source['sections']['table1']['html']
    eq6_fragment = source['sections']['eq6']['html']
    require(source['sections']['table1']['raw_source_lines'] == [290, 356], 'public table excerpt range mismatch')
    require(source['sections']['eq6']['raw_source_lines'] == [592, 625], 'public Eq6 excerpt range mismatch')
    check_table(table_fragment, table_rows)
    p_groups, prime_groups = check_eq6(eq6_fragment, table_rows, extension_bytes.decode())
    old_table = r'alttext="-\ket{12}+\ket{21}"'
    new_table = r'alttext="\ket{12}+\ket{21}"'
    require(table_fragment.count(old_table) == 1, 'table mutation anchor')
    table_mutation = table_fragment.replace(old_table, new_table, 1)
    old_eq = r'alttext="\displaystyle=\{0353,3530,4044,5405\},"'
    new_eq = r'alttext="\displaystyle=\{0354,3530,4044,5405\},"'
    require(eq6_fragment.count(old_eq) == 1, 'Eq6 mutation anchor')
    eq_mutation = eq6_fragment.replace(old_eq, new_eq, 1)
    controls = {
        'flipped_public_0012_sign': intended_failure(lambda: check_table(table_mutation, table_rows), 'public source table mismatch'),
        'changed_public_P_prime_0353_to_0354': intended_failure(lambda: check_eq6(eq_mutation, table_rows, extension_bytes.decode()), 'public Eq6 P prime mismatch'),
    }
    clock = subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], check=True, capture_output=True, text=True).stdout.strip()
    receipt = {
        'kind': 'PUBLIC_SOURCE_SELECTED_EXCERPT_TRANSCRIPTION_CHECK',
        'observed_native_clock_before_receipt_write': clock,
        'public_url': source['url'], 'source_excerpt_path': str(SOURCE), 'source_excerpt_sha256': sha(source_bytes),
        'manifest_sha256': sha(manifest_bytes), 'table_sha256': sha(table_bytes), 'extension_sha256': sha(extension_bytes),
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'table_cells_compared_including_order_sign_and_sqrt2': len(table_rows),
        'public_eq6_P_quartets': p_groups, 'public_eq6_P_prime_quartets': prime_groups,
        'negative_controls': controls,
        'limits': ['The source artifact retains exact selected textual HTML line ranges, not the full page or a whole-page byte hash.',
                   'This checks public MathML alttext; source rendering and the mathematical proof remain separate review obligations.']}
    with RECEIPT.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print('PASS 36 public table cells, both Eq6 sets, and two intended-failure source controls')
    print('source checker SHA256:', receipt['checker_sha256'])
    print('observed native clock:', clock)


if __name__ == '__main__':
    main()
