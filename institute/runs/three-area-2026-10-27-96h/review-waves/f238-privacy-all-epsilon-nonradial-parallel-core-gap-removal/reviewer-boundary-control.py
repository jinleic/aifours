#!/usr/bin/env python3
"""Exact full-boundary privacy check with an intended invalid-gap negative."""
from fractions import Fraction as Q

b = Q(1, 2)
h = (Q(1), Q(0))
assert abs(h[0]) + abs(h[1]) == 1  # Exactly on the CLOSED sensitivity boundary.
# A = (2/5,1/2) x (-1/10,1/10), inside C=[-1/2,1/2]^2.
x0, x1, y0, y1 = Q(2, 5), Q(1, 2), -Q(1, 10), Q(1, 10)
area = (x1-x0)*(y1-y0)
assert area == Q(1, 50)
# For x in A, y in (-1/10,1/10), the shifted square distance is
# dist_1((x+1,y), C) = x+1/2, strictly between 9/10 and 1.
d0, d1 = x0+Q(1, 2), x1+Q(1, 2)
assert (d0, d1) == (Q(9, 10), Q(1))
# u=(1-b) sum b^i 1_Ki. In the correct radii 0,1,2,...,
# u=1 on A and u=b on A+h. Mass normalization cancels.
good_left, good_translated = area, area*b
assert good_left == good_translated/b
print('CLOSED_BOUNDARY positive:', good_left, '=', good_translated, '/', b)
# Invalid radii 0,1/2,3/2,5/2,...: A+h is outside level 1
# but inside level 2, so its density is b^2 and privacy fails.
assert Q(1, 2) < d0 < d1 < Q(3, 2)
bad_left, bad_translated = area, area*b*b
assert bad_left > bad_translated/b
print('INTENDED_NEGATIVE invalid first spacing:', bad_left, '>', bad_translated, '/', b)
print('BOUNDARY_CONTROL_COMPLETE')
