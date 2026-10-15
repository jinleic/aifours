"""Regression checks for the two executable boundary errors found by the focused review."""
import json
from pathlib import Path
import subprocess
import sys

from automaton import build_table
from complement_rules import ComplementRules
from check_complement_rules import validate_edges, replay_regex, language_check, growth_check


def main():
    compiler = Path(__file__).with_name('complement_rules.py')
    run = subprocess.run([sys.executable, str(compiler), 'I', '0', '--m', '4'],
                         capture_output=True, text=True, check=True)
    spec = json.loads(run.stdout)
    assert spec['order'] == [0, 1]
    table = build_table('I', 0, 4)
    edge = validate_edges(spec, table)
    assert replay_regex(spec)
    states = language_check(spec, table)
    growth = growth_check(spec, table)
    try:
        ComplementRules(build_table('A', 1))
    except ValueError as error:
        assert 'N >= 2' in str(error)
        rank_one_rejected = True
    else:
        raise AssertionError('rank-one core constructor accepted an invalid domain')
    print(json.dumps({'dihedral_I_0_default_order':[0,1], 'dihedral_certificate':edge,
                      'leading_language_product_states':states,'growth_certificate':growth,
                      'rank_one_constructor_rejected':rank_one_rejected,'ALL_OK':True},indent=1))


if __name__ == '__main__':
    main()
