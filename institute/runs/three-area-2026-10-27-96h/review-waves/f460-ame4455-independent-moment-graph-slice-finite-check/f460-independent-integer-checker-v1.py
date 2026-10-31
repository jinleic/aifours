from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from time import monotonic
import sys

Q = (4, 4, 5, 5)
B = tuple(6 - q for q in Q)
PAIR3 = ((0, 1), (0, 2), (1, 2))


class CheckFailure(Exception):
  pass


def need(condition, reason):
  if not condition:
    raise CheckFailure(reason)


def budget(deadline):
  need(monotonic() <= deadline, "COOPERATIVE_TIME_BOUND")


def reject_for(label, reason, function, controls):
  try:
    function()
  except CheckFailure as error:
    need(str(error) == reason, "WRONG_CONTROL_REASON:" + label)
  else:
    raise CheckFailure("CONTROL_NOT_REJECTED:" + label)
  controls.append((label, reason))


def compositions3(total):
  for a in range(total + 1):
    for b in range(total - a + 1):
      yield (a, b, total - a - b)


def histograms():
  found = set()
  for n4 in range(25):
    for n3 in range(25 - n4):
      for n2 in range(25 - n4 - n3):
        n1 = 60 - 4 * n4 - 3 * n3 - 2 * n2
        n0 = 24 - n4 - n3 - n2 - n1
        if min(n0, n1) >= 0 and n2 + 3 * n3 + 6 * n4 == 49:
          found.add((n0, n1, n2, n3, n4))
  need(found == {(0, 0, 13, 10, 1), (0, 1, 10, 13, 0)},
       "HISTOGRAM_CLASSIFICATION")
  return tuple(sorted(found))


def word_types(h):
  counts = [0] * 16
  if h is None:
    counts[15] = 1
  else:
    counts[1 << h] = 1
  for i in range(4):
    counts[15 ^ (1 << i)] = B[i] * B[i] + int(h is not None and i != h)
  for i, j in combinations(range(4), 2):
    k, l = (a for a in range(4) if a not in (i, j))
    counts[(1 << i) | (1 << j)] = (
      B[k] * B[l] - int(h is not None and h in (i, j))
    )
  return counts


def check_word_types(counts):
  need(len(counts) == 16 and min(counts) >= 0, "TYPE_DOMAIN")
  need(sum(counts) == 24, "TYPE_TOTAL")
  first = sum(mask.bit_count() * count for mask, count in enumerate(counts))
  second = sum(
    (mask.bit_count() * (mask.bit_count() - 1) // 2) * count
    for mask, count in enumerate(counts)
  )
  need((first, second) == (60, 49), "TYPE_MOMENTS")
  for i in range(4):
    outside = sum(count for mask, count in enumerate(counts)
                  if not mask & (1 << i))
    need(outside == 6 * B[i], "OUTSIDE_COUNT")
  for i, j in combinations(range(4), 2):
    bits = (1 << i) | (1 << j)
    outside = sum(count for mask, count in enumerate(counts)
                  if not mask & bits)
    internal = sum(count for mask, count in enumerate(counts)
                   if mask & bits == bits)
    need(outside == B[i] * B[j], "OUTSIDE_PAIR_COUNT")
    need(internal == Q[i] * Q[j] - 12, "INTERNAL_PAIR_COUNT")


def local_rows(i, sigma_max, f_max):
  others = tuple(j for j in range(4) if j != i)
  rows = []
  for r in range(2, 7):
    p = 6 - r
    for sigma in range(sigma_max + 1):
      for f in range(f_max + 1):
        if sigma and f:
          continue
        tau = 12 - Q[i] - 2 * r + sigma - 2 * f
        delta = p - sigma - f - tau
        if min(tau, delta) < 0:
          continue
        for y in compositions3(delta):
          x = tuple(B[j] - sigma - delta + y[k]
                    for k, j in enumerate(others))
          if min(x) >= 0 and sum(x) == tau:
            rows.append((r, sigma, f, tau, delta, x, y))
  return tuple(sorted(rows))


def aggregate_local_profiles(h, i, counts, deadline):
  sigma_total = int(h is not None and h == i)
  f_total = int(h is None)
  rows = local_rows(i, sigma_total, f_total)
  others = tuple(j for j in range(4) if j != i)
  found = Counter()
  for index, multiset in enumerate(combinations_with_replacement(rows, Q[i])):
    if index % 256 == 0:
      budget(deadline)
    if sum(row[0] for row in multiset) != 12:
      continue
    if sum(row[1] for row in multiset) != sigma_total:
      continue
    if sum(row[2] for row in multiset) != f_total:
      continue
    if any(sum(row[5][k] for row in multiset) != counts[15 ^ (1 << j)]
           for k, j in enumerate(others)):
      continue
    if any(sum(row[6][k] for row in multiset) !=
           counts[(1 << i) | (1 << j)]
           for k, j in enumerate(others)):
      continue
    profile = tuple(sorted((row[0] for row in multiset), reverse=True))
    found[profile] += 1

  four = {(3, 3, 3, 3), (4, 3, 3, 2), (4, 4, 2, 2)}
  ordinary = {(3, 3, 2, 2, 2)}
  if Q[i] == 4:
    expected = four
    if h in (2, 3):
      expected = {(3, 3, 3, 3), (4, 3, 3, 2)}
    elif h == i:
      expected = {(4, 3, 3, 2), (4, 4, 2, 2)}
  else:
    expected = ordinary | ({(4, 2, 2, 2, 2)} if h == i else set())
  need(set(found) == expected, "AGGREGATE_SYMBOL_PROFILES")
  return found


def is_matching(edges):
  return (len({a for a, b in edges}) == len(edges)
          and len({b for a, b in edges}) == len(edges))


def maximum_matching(edges):
  for size in range(len(edges), -1, -1):
    if any(is_matching(part) for part in combinations(edges, size)):
      return size
  raise CheckFailure("MATCHING_SEARCH")


def disjoint(a, b):
  return a[0] != b[0] and a[1] != b[1]


def graph_degrees(edges):
  left = [0] * 4
  right = [0] * 4
  for a, b in edges:
    left[a] += 1
    right[b] += 1
  return tuple(left), tuple(right)


def abstract_key(edges):
  adjacency = [set() for _ in range(8)]
  for a, b in edges:
    adjacency[a].add(4 + b)
    adjacency[4 + b].add(a)
  seen = set()
  keys = []
  for root in range(8):
    if root in seen or not adjacency[root]:
      continue
    stack = [root]
    seen.add(root)
    vertices = []
    while stack:
      vertex = stack.pop()
      vertices.append(vertex)
      for neighbor in adjacency[vertex]:
        if neighbor not in seen:
          seen.add(neighbor)
          stack.append(neighbor)
    best = None
    for order in permutations(vertices):
      code = 0
      bit = 0
      for a in range(len(order)):
        for b in range(a + 1, len(order)):
          if order[b] in adjacency[order[a]]:
            code |= 1 << bit
          bit += 1
      if best is None or code < best:
        best = code
    keys.append((len(vertices), best))
  return tuple(sorted(keys))


def has_cycle(edges):
  parent = list(range(8))

  def find(vertex):
    while parent[vertex] != vertex:
      vertex = parent[vertex]
    return vertex

  for a, b in edges:
    x, y = find(a), find(4 + b)
    if x == y:
      return True
    parent[x] = y
  return False


def f_compatible(edges):
  for v in range(4):
    for f in range(4):
      if v != f and all(disjoint(edges[v], edges[t])
                        for t in range(4) if t not in (v, f)):
        return True
  return False


def s_five_compatible(edges):
  for v in range(4):
    rest = tuple(t for t in range(4) if t != v)
    if not all(disjoint(edges[v], edges[t]) for t in rest):
      continue
    if any(is_matching(tuple(edges[t] for t in group))
           for group in combinations(rest, 2)):
      return True
  return False


def s_four_compatible(edges):
  for group in combinations(range(4), 2):
    other = tuple(t for t in range(4) if t not in group)
    if (is_matching(tuple(edges[t] for t in group))
        and is_matching(tuple(edges[t] for t in other))):
      return True
  return False


def check_f_markers(edges, outside3, outside4):
  need(len(edges) == 4 and len(set(edges)) == 4, "EDGE_COUNT")
  need(outside3 | outside4 <= set(range(4)), "MARK_INDEX")
  need(len(outside3) == 2 and len(outside4) == 2, "OUTSIDE_COUNT")
  need(len(outside3 & outside4) == 1, "COMMON_MARKED_EDGE")
  need(is_matching(tuple(edges[t] for t in outside3)), "OUTSIDE_MATCHING")
  need(is_matching(tuple(edges[t] for t in outside4)), "OUTSIDE_MATCHING")


def enumerate_graphs(deadline):
  representatives = {
    "4P2": ((0, 0), (1, 1), (2, 2), (3, 3)),
    "P3+2P2": ((0, 0), (0, 1), (1, 2), (2, 3)),
    "2P3": ((0, 0), (0, 1), (1, 2), (1, 3)),
    "P4+P2": ((0, 0), (1, 0), (1, 1), (2, 2)),
    "P5": ((0, 0), (1, 0), (1, 1), (2, 1)),
    "C4": ((0, 0), (0, 1), (1, 0), (1, 1)),
  }
  catalog = {abstract_key(edges): name
             for name, edges in representatives.items()}
  need(len(catalog) == 6, "NONISOMORPHIC_REPRESENTATIVES")
  opposite_centers = ((0, 1), (0, 2), (1, 0), (2, 0))
  need(abstract_key(opposite_centers) ==
       abstract_key(representatives["2P3"]), "COMPONENT_FLIP_ISOMORPHISM")

  expected = Counter({
    "4P2": 24, "P3+2P2": 288, "2P3": 216,
    "P4+P2": 576, "P5": 288, "C4": 36,
  })
  matching_sizes = {
    "4P2": 4, "P3+2P2": 3, "2P3": 2,
    "P4+P2": 3, "P5": 2, "C4": 2,
  }
  counts = Counter()
  f_counts = Counter()
  s5_counts = Counter()
  s4_singleton_counts = Counter()
  total = 0
  for edges in combinations(tuple(product(range(4), repeat=2)), 4):
    total += 1
    if total % 128 == 0:
      budget(deadline)
    left, right = graph_degrees(edges)
    if max(left + right) > 2:
      continue
    key = abstract_key(edges)
    need(key in catalog, "UNCLASSIFIED_GRAPH")
    name = catalog[key]
    counts[name] += 1
    need(maximum_matching(edges) == matching_sizes[name], "MATCHING_NUMBER")
    cyclic = has_cycle(edges)
    need(cyclic == (name == "C4"), "CYCLE_CLASSIFICATION")
    both_extreme = (
      tuple(sorted(left)) == (0, 0, 2, 2)
      and tuple(sorted(right)) == (0, 0, 2, 2)
    )
    need(both_extreme == cyclic, "EXTREME_PROFILES_C4")

    f_ok = f_compatible(edges)
    s5_ok = s_five_compatible(edges)
    s4_ok = s_four_compatible(edges)
    need(f_ok == (not cyclic), "F_MARKED_CLASSIFICATION")
    isolated_edge = any(
      all(disjoint(edge, other) for other in edges if other != edge)
      for edge in edges
    )
    need(s5_ok == isolated_edge, "S5_MARKED_CLASSIFICATION")
    need(s4_ok, "S4_TWO_MATCHING_COLORING")
    if f_ok:
      f_counts[name] += 1
    if s5_ok:
      s5_counts[name] += 1
    if s4_ok and 0 in left:
      s4_singleton_counts[name] += 1

  need(total == 1820, "ALL_FOUR_EDGE_GRAPHS")
  need(counts == expected, "LABELED_GRAPH_COUNTS")
  need(sum(f_counts.values()) == 1392, "F_GRAPH_TOTAL")
  need(sum(s5_counts.values()) == 888, "S5_GRAPH_TOTAL")
  need(s4_singleton_counts == Counter({
    "P3+2P2": 144, "2P3": 180, "P4+P2": 576, "P5": 288, "C4": 36,
  }), "S4_SINGLETON_SIDE_COUNTS")
  return counts, f_counts, s5_counts, s4_singleton_counts


def require_distinct(words):
  need(len(words) == 4 and len(set(words)) == 4, "DISTINCT_SUPPORT")


def require_no_distance_one(words):
  require_distinct(words)
  need(all(sum(a != b for a, b in zip(x, y)) != 1
           for x, y in combinations(words, 2)), "UNPROVED_NO_DISTANCE_ONE")


def subsets(items):
  items = tuple(sorted(items))
  for size in range(len(items) + 1):
    yield from combinations(items, size)


def enumerate_slices(deadline):
  columns = tuple(column for column in product((0, 1), repeat=4)
                  if sum(column) == 2)
  need(len(columns) == 6, "BALANCED_COLUMNS")
  normalized = set()
  cases = Counter()
  subshadow_count = 0
  full_pairs = set(product((0, 1), repeat=2))
  for index, selected in enumerate(product(columns, repeat=3)):
    if index % 32 == 0:
      budget(deadline)
    key = tuple(min(column, tuple(1 - x for x in column))
                for column in selected)
    normalized.add(key)
    words = tuple(zip(*selected))
    distinct_partitions = len(set(key))
    if len(set(words)) != 4:
      need(distinct_partitions == 1 and len(set(words)) == 2,
           "DUPLICATE_PARTITION_CASE")
      cases["duplicates"] += 1
      continue
    need(distinct_partitions in (2, 3), "SLICE_PARTITION_CASE")
    omitted = tuple(
      full_pairs - {(word[a], word[b]) for word in words}
      for a, b in PAIR3
    )
    nonfull = tuple(missing for missing in omitted if missing)
    distance_one = sum(
      sum(a != b for a, b in zip(x, y)) == 1
      for x, y in combinations(words, 2)
    )
    if distinct_partitions == 3:
      cases["all_different"] += 1
      need(not nonfull and distance_one == 0, "FULL_SLICE_CASE")
    else:
      cases["two_equal"] += 1
      need(len(nonfull) == 1 and len(nonfull[0]) == 2,
           "NONFULL_SLICE_CASE")
      need(is_matching(tuple(nonfull[0])), "OMITTED_PAIRS_MATCHING")
      need(distance_one == 2, "DISTANCE_ONE_ALTERNATIVE")
    for chosen in product(*(tuple(subsets(missing)) for missing in omitted)):
      z = tuple(len(part) for part in chosen)
      need(max(z) <= 2 and sum(value > 0 for value in z) <= 1,
           "SLICE_DEFECT_PATTERN")
      subshadow_count += 1

  need(len(normalized) == 27, "UNORDERED_PARTITION_TRIPLES")
  need(cases == Counter({
    "duplicates": 24, "two_equal": 144, "all_different": 48,
  }), "ORIENTED_SLICE_COUNTS")
  need(subshadow_count == 624, "SLICE_SUBSHADOW_COUNT")
  return cases, subshadow_count


def enumerate_quadrants():
  counts = {}
  for right_size in (4, 5):
    missing_total = 4 * right_size - 12
    capacities = (4, 2 * (right_size - 2), 4, 2 * (right_size - 2))
    count = 0
    for z, x, y, s in product(*(range(cap + 1) for cap in capacities)):
      if z + x + y + s != missing_total:
        continue
      count += 1
      need(z - s == (z + x) - (x + s), "GENERIC_QUADRANT_IDENTITY")
      left_residual_sum = 2 * right_size - z - x
      right_residual_sum = 8 - z - y
      d = left_residual_sum - 6
      e = right_residual_sum - (6 if right_size == 4 else 4)
      need(z - s == -d - e, "SPECIALIZED_DEFECT_IDENTITY")
    counts[right_size] = count
  need(counts == {4: 35, 5: 117}, "QUADRANT_COUNTS")
  return counts


def scalar_case(d1, d2, h, f, u, z):
  if d1 not in range(-2, 3) or d2 not in range(-2, 3):
    return None
  if h not in range(3) or f not in (0, 1):
    return None
  if len(u) != 3 or len(z) != 3:
    return None
  if any(value not in range(3) for value in u + z):
    return None
  if sum(u) != 3 - 2 * f or sum(value > 0 for value in z) > 1:
    return None
  a = (d1 + d2, d1 + h, d2 + h)
  s = tuple(z[k] + a[k] for k in range(3))
  if any(s[k] < u[k] + f or s[k] > (4, 6, 6)[k]
         for k in range(3)):
    return None
  return s


def enumerate_scalar_cases(deadline):
  retained = 0
  regular = 0
  z_vectors = tuple(z for z in product(range(3), repeat=3)
                    if sum(value > 0 for value in z) <= 1)
  for d1, d2, h in product(range(-2, 3), range(-2, 3), range(3)):
    budget(deadline)
    for f in (0, 1):
      for u in product(range(3), repeat=3):
        if sum(u) != 3 - 2 * f:
          continue
        for z in z_vectors:
          s = scalar_case(d1, d2, h, f, u, z)
          if s is None:
            continue
          retained += 1
          a = (d1 + d2, d1 + h, d2 + h)
          need(sum(u[k] + f <= a[k] for k in range(3)) >= 2,
               "TWO_DEFECT_INEQUALITIES")
          if d1 == 0 and d2 == 0:
            regular += 1
            need(h >= 1, "REGULAR_HIGH_NEIGHBOR")
            if f:
              need(z[0] > 0 and z[1:] == (0, 0),
                   "REGULAR_F_DEFECT_LOCATION")
              if u[1] or u[2]:
                need(h == 2, "REGULAR_F_TWO_HIGH_NEIGHBORS")
              if h == 1:
                need(u == (1, 0, 0), "REGULAR_F_TRIPLE_LOCATION")
  need(retained > 0 and regular > 0, "NONVACUOUS_SCALAR_CASES")
  need(scalar_case(0, 0, 1, 0, (1, 1, 1), (1, 0, 0)) == (1, 1, 1),
       "POSITIVE_REGULAR_SCALAR")
  need(scalar_case(0, 0, 1, 1, (1, 0, 0), (2, 0, 0)) == (2, 1, 1),
       "POSITIVE_REGULAR_F_SCALAR")
  need(scalar_case(1, 1, 0, 0, (1, 1, 1), (0, 0, 0)) == (2, 1, 1),
       "NONREGULAR_ZERO_H_SHADOW")
  return retained, regular


def check_claimed_defect(edges, claimed):
  n = {0, 1}
  z = sum(a in n and b in n for a, b in edges)
  s = sum(a not in n and b not in n for a, b in edges)
  left_sum = 8 - sum(a in n for a, b in edges)
  right_sum = 8 - sum(b in n for a, b in edges)
  d1, d2 = left_sum - 6, right_sum - 6
  need(z - s == -d1 - d2, "DEFECT_IDENTITY")
  need(claimed == z - s, "DEFECT_SIGN")


def check_residual_graph(edges, left_profile, right_profile):
  need(len(edges) == 12 and len(set(edges)) == 12, "RESIDUAL_EDGE_COUNT")
  need(all(a in range(5) and b in range(5) for a, b in edges),
       "RESIDUAL_VERTEX")
  left = tuple(sum(a == i for a, b in edges) for i in range(5))
  right = tuple(sum(b == j for a, b in edges) for j in range(5))
  need(left == left_profile and right == right_profile, "RESIDUAL_DEGREES")


def low_edges(edges, left_profile, right_profile):
  return tuple((a, b) for a, b in edges
               if left_profile[a] == 2 and right_profile[b] == 2)


def require_low_matching(edges, left_profile, right_profile):
  need(is_matching(low_edges(edges, left_profile, right_profile)),
       "GENERALIZED_LOW_LOW_CONSTRAINT")


def sector_counts(edges, left_profile, right_profile):
  return (
    sum(left_profile[a] == 2 and right_profile[b] == 2 for a, b in edges),
    sum(left_profile[a] == 2 and right_profile[b] > 2 for a, b in edges),
    sum(left_profile[a] > 2 and right_profile[b] == 2 for a, b in edges),
    sum(left_profile[a] > 2 and right_profile[b] > 2 for a, b in edges),
  )


def ordinary_fixture(m):
  edges = {(a, b) for a in (2, 3, 4) for b in (0, 1)}
  edges |= {(a, b) for a in (0, 1) for b in (2, 3, 4)}
  switches = ((2, 2, 0, 0), (3, 3, 1, 1), (4, 4, 0, 1))
  for a, b, i, j in switches[:m]:
    edges.remove((a, j))
    edges.remove((i, b))
    edges.add((a, b))
    edges.add((i, j))
  return tuple(sorted(edges))


def enumerate_sectors(left_profile, right_profile, exceptional, deadline):
  choices = tuple(tuple(combinations(range(5), degree))
                  for degree in left_profile)
  retained = Counter()
  degree_valid = 0
  for index, rows in enumerate(product(*choices)):
    if index % 1024 == 0:
      budget(deadline)
    columns = tuple(sum(j in row for row in rows) for j in range(5))
    if columns != right_profile:
      continue
    degree_valid += 1
    edges = tuple((i, j) for i, row in enumerate(rows) for j in row)
    if not is_matching(low_edges(edges, left_profile, right_profile)):
      continue
    sectors = sector_counts(edges, left_profile, right_profile)
    m = sectors[0]
    expected = (3, 5, 3, 1) if exceptional else (m, 6 - m, 6 - m, m)
    need(sectors == expected, "LOW_LOW_SECTORS")
    if exceptional:
      need(m == 3, "EXCEPTIONAL_MATCHING_SIZE")
    for a, degree in enumerate(left_profile):
      if degree == 2:
        need(any(x == a and right_profile[y] > 2 for x, y in edges),
             "LEFT_HIGH_NEIGHBOR_FROM_MATCHING")
    for b, degree in enumerate(right_profile):
      if degree == 2:
        need(any(y == b and left_profile[x] > 2 for x, y in edges),
             "RIGHT_HIGH_NEIGHBOR_FROM_MATCHING")
    retained[m] += 1
  need(set(retained) == ({3} if exceptional else {0, 1, 2, 3}),
       "SECTOR_POSITIVE_SIZES")
  return degree_valid, retained


def main(argv):
  need(argv == ["--self-check"], "ARGV")
  deadline = monotonic() + 50.0
  controls = []
  print("HISTOGRAMS", histograms())

  for i in range(4):
    need(len(local_rows(i, 1, 1)) == (10 if Q[i] == 4 else 11),
         "COMPLETE_LOCAL_ROW_COUNT")
  for h in (None, 0, 1, 2, 3):
    counts = word_types(h)
    check_word_types(counts)
    label = "F" if h is None else "S" + str(h + 1)
    for i in range(4):
      profiles = aggregate_local_profiles(h, i, counts, deadline)
      print("LOCAL_PROFILES", label, i + 1, sorted(profiles.items()))

  mutated = word_types(None)
  mutated[3] += 1
  mutated[5] -= 1
  reject_for("wrong outside count", "OUTSIDE_COUNT",
             lambda: check_word_types(mutated), controls)

  diagonal = ((0, 0), (1, 1), (2, 2), (3, 3))
  check_f_markers(diagonal, {0, 1}, {0, 2})
  reject_for("wrong marked outside count", "OUTSIDE_COUNT",
             lambda: check_f_markers(diagonal, {0}, {0, 2}), controls)
  reject_for("missing common marked edge", "COMMON_MARKED_EDGE",
             lambda: check_f_markers(diagonal, {0, 1}, {2, 3}), controls)

  print("GRAPH_TABLE", enumerate_graphs(deadline))
  print("SLICE_COUNTS", enumerate_slices(deadline))

  duplicate = ((0, 0, 0), (0, 0, 0), (1, 1, 1), (1, 1, 1))
  distance_one = ((0, 0, 0), (0, 0, 1), (1, 1, 0), (1, 1, 1))
  parity = ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))
  require_distinct(distance_one)
  require_no_distance_one(parity)
  reject_for("duplicate slice words", "DISTINCT_SUPPORT",
             lambda: require_distinct(duplicate), controls)
  reject_for("unproved no-distance-one premise", "UNPROVED_NO_DISTANCE_ONE",
             lambda: require_no_distance_one(distance_one), controls)

  print("QUADRANT_COUNTS", enumerate_quadrants())
  defect_edges = ((0, 0), (2, 0), (2, 2), (3, 3))
  check_claimed_defect(defect_edges, -1)
  reject_for("reversed defect sign", "DEFECT_SIGN",
             lambda: check_claimed_defect(defect_edges, 1), controls)
  print("SCALAR_CASE_COUNTS", enumerate_scalar_cases(deadline))

  ordinary = (3, 3, 2, 2, 2)
  exceptional = (4, 2, 2, 2, 2)
  for m in range(4):
    edges = ordinary_fixture(m)
    check_residual_graph(edges, ordinary, ordinary)
    require_low_matching(edges, ordinary, ordinary)
    need(sector_counts(edges, ordinary, ordinary) == (m, 6 - m, 6 - m, m),
         "ORDINARY_POSITIVE_FIXTURE")

  exceptional_edges = (
    (0, 0), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 2), (2, 1), (2, 3),
    (3, 1), (3, 4), (4, 0), (4, 1),
  )
  check_residual_graph(exceptional_edges, exceptional, ordinary)
  require_low_matching(exceptional_edges, exceptional, ordinary)
  need(sector_counts(exceptional_edges, exceptional, ordinary) == (3, 5, 3, 1),
       "EXCEPTIONAL_POSITIVE_FIXTURE")

  weak_nonmatching = (
    (0, 0), (0, 1), (0, 4), (1, 0), (1, 1), (1, 2),
    (2, 2), (2, 3), (3, 0), (3, 4), (4, 1), (4, 3),
  )
  check_residual_graph(weak_nonmatching, ordinary, ordinary)
  reject_for("degree-only low-low generalization",
             "GENERALIZED_LOW_LOW_CONSTRAINT",
             lambda: require_low_matching(weak_nonmatching, ordinary, ordinary),
             controls)

  print("ORDINARY_SECTOR_ENUMERATION",
        enumerate_sectors(ordinary, ordinary, False, deadline))
  print("EXCEPTIONAL_SECTOR_ENUMERATION",
        enumerate_sectors(exceptional, ordinary, True, deadline))
  budget(deadline)
  for label, reason in controls:
    print("INTENDED_REJECTION", label, reason)
  print("PASS: finite necessary-condition models only; no P,E or tensor certificate")


if __name__ == "__main__":
  try:
    main(sys.argv[1:])
  except CheckFailure as error:
    print("FAIL:", error, file=sys.stderr)
    raise SystemExit(1)

