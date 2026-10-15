"""Render the complete finite paired regular-expression DAG as text.
Every rule is a pair in the root expression, plus the listed finite rules.
No normal-form calls or hidden word-problem conditions occur in this output.
"""
import json
import sys

spec = json.load(open(sys.argv[1]))
print('EXPLICIT PAIRED REGULAR EXPRESSION: type', spec['type'], 'order', spec['order'])
print('Alphabet: 0=Delta^-1; 1=Delta; a<b<c<... in the stated generator order.')
print('A pair [u=>v] denotes the single binomial u-v; empty word is "".')
print('Union +, coordinatewise concatenation ., and coupled Kleene star * act on sets of pairs.')
print('Use the SAME path/choice in both coordinates. The basis is generally NOT reduced.')
print('Definitions below are acyclic; all RHS node references have smaller indices.\n')
for i, node in enumerate(spec['paired_regex']['nodes']):
    tag, *args = node
    if tag == 'empty':
        rhs = 'EMPTY_SET'
    elif tag == 'epsilon':
        rhs = '[""=>""]'
    elif tag == 'pair':
        rhs = '[' + json.dumps(args[0]) + '=>' + json.dumps(args[1]) + ']'
    elif tag == 'union':
        rhs = f'R{args[0]} + R{args[1]}'
    elif tag == 'concat':
        rhs = f'R{args[0]} . R{args[1]}'
    elif tag == 'star':
        rhs = f'(R{args[0]})*'
    else:
        raise ValueError(tag)
    print(f'R{i} = {rhs}')
print('\nPOSITIVE RULE PAIRS = R' + str(spec['paired_regex']['root']))
print('ADJOIN THE FINITE RULES:')
for left, right in spec['twists'] + spec['cancellations']:
    print(json.dumps(left), '=>', json.dumps(right))
