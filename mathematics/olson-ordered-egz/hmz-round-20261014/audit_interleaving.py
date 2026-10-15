#!/usr/bin/env python3
"""Evaluate the specific interleaving obstruction using the saved Dic_3 table."""
import hashlib
import json
from pathlib import Path

path = Path('Dic3-search-best.json')
data = json.loads(path.read_text())
table, identity = data['table'], data['identity']
assert len(table) == 12 and identity == 0


def product(word):
    result = identity
    for element in word:
        result = table[result][element]
    return result


word = [6, 1, 9, 5]
pairs = [[6, 9], [1, 5]]
pair_products = [product(pair) for pair in pairs]
union_product = product(word)
assert pair_products == [identity, identity]
assert union_product == 4 and union_product != identity
print(json.dumps(dict(table_source=str(path),
    source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
    identity=identity, ordered_union=word, ordered_pair_sublists=pairs,
    pair_products=pair_products, ordered_union_product=union_product,
    block_product=product(pair_products), full_goal_counterexample=False), indent=2))
