#!/usr/bin/env python3
"""Independent SP and factor-automaton checks for the Shor dead-end family."""
from collections import deque
import json
import sys


def atom(i, j):
    return b'a' * i + b'b' + b'a' * j


def make_code(n):
    m = n // 16
    row0 = {0, 1, 7, 13, 14, 20, 26}
    row11 = {0, 1, 2, 14, 16, 18, 20}
    for k in range(m - 2):
        row0.update((30 + 16*k, 32 + 16*k, 36 + 16*k, 42 + 16*k))
        row11.update((30 + 16*k, 32 + 16*k, 34 + 16*k, 36 + 16*k))
    mid = {16*k+y for k in range(m) for y in (0, 2, 4, 6)}
    rows = {0: row0, 3: mid, 8: mid, 11: row11}
    return {atom(i, j) for i, values in rows.items() for j in values} | {b'a' * n}


def ud_sp(code):
    residual = {v[len(u):] for u in code for v in code if u != v and v.startswith(u)}
    seen = set()
    while residual:
        if b'' in residual or residual & code:
            return False
        new = residual - seen
        if not new:
            return True
        seen.update(new)
        nxt = set()
        for r in new:
            for w in code:
                if r.startswith(w):
                    nxt.add(r[len(w):])
                if w.startswith(r):
                    nxt.add(w[len(r):])
        residual = nxt
    return True


def shortest_missing_factor(code, state_cap=100000):
    # Trie NFA for C*: terminal -> root epsilon. All trie states are initial
    # and final because each is accessible from/root-coaccessible to C*.
    trie = [{}]
    terminals = set()
    for word in sorted(code):
        node = 0
        for ch in word:
            if ch not in trie[node]:
                trie[node][ch] = len(trie)
                trie.append({})
            node = trie[node][ch]
        terminals.add(node)
    term_mask = sum(1 << t for t in terminals)
    start = (1 << len(trie)) - 1
    queue = deque([start])
    prior = {start: None}
    while queue:
        current = queue.popleft()
        for ch in (ord('a'), ord('b')):
            out, bits = 0, current
            while bits:
                low = bits & -bits
                bits -= low
                node = low.bit_length() - 1
                target = trie[node].get(ch)
                if target is not None:
                    out |= 1 << target
            if out & term_mask:
                out |= 1
            if out not in prior:
                prior[out] = (current, ch)
                if out == 0:
                    data, state = [], out
                    while prior[state] is not None:
                        state, letter = prior[state]
                        data.append(letter)
                    return bytes(reversed(data)), len(trie), len(prior)
                if len(prior) >= state_cap:
                    raise RuntimeError('determinization state cap exceeded')
                queue.append(out)
    return None, len(trie), len(prior)


def check(n):
    code = make_code(n)
    if not ud_sp(code):
        raise AssertionError(('base not UD', n))
    missing, trie, explored = shortest_missing_factor(code)
    if missing != b'bbaab':
        raise AssertionError(('unexpected shortest missing factor', n, missing))
    extended = code | {missing}
    if not ud_sp(extended):
        raise AssertionError(('appending missing factor is not UD', n))
    return {'n': n, 'base_codewords': len(code), 'trie_states': trie,
            'subset_states_explored': explored, 'shortest_missing_factor': missing.decode(),
            'base_ud': True, 'appending_factor_ud': True}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: escape-factor-check.py MAX_N')
    limit = int(sys.argv[1])
    if not 32 <= limit <= 256:
        raise SystemExit('require 32 <= MAX_N <= 256')
    print(json.dumps([check(n) for n in range(32, limit + 1, 16)], indent=2))
