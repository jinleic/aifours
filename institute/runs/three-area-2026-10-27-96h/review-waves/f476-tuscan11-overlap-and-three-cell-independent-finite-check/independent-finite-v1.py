import itertools
import signal
import sys
import time

LIMIT_SECONDS = 50.0
STARTED = time.monotonic()
STOP_SIGNAL = None
INF = -1
REPORT = []
INCOMPLETE_REASONS = frozenset(("DEADLINE", "SIGNAL"))

class GateFailure(Exception):
  def __init__(self, reason, detail):
    self.reason = reason
    self.detail = detail
    super().__init__(reason + ": " + str(detail))

def require(condition, reason, detail):
  if not condition:
    raise GateFailure(reason, detail)

def request_stop(signum, frame):
  global STOP_SIGNAL
  STOP_SIGNAL = signum

def tick():
  if STOP_SIGNAL is not None:
    raise GateFailure("SIGNAL", STOP_SIGNAL)
  if time.monotonic() - STARTED >= LIMIT_SECONDS:
    raise GateFailure("DEADLINE", LIMIT_SECONDS)

def record(name, value):
  REPORT.append(name + ": " + repr(value))

def directed_universe(vertices):
  return frozenset(
    (a, b) for a in vertices for b in vertices if a != b
  )

def augmented_singletons(row, cut):
  cycle = (INF,) + tuple(row)
  result = []
  for i, vertex in enumerate(cycle):
    left = cycle[i - 1]
    right = cycle[(i + 1) % len(cycle)]
    if ((left in cut) == (right in cut)
        and (vertex in cut) != (left in cut)):
      result.append(vertex)
  return frozenset(result)

def linear_counts(row, cut):
  n = len(row)
  q = 0
  s = 0
  t = 0
  for i, vertex in enumerate(row):
    if vertex in cut:
      if i == 0 or row[i - 1] not in cut:
        q += 1
      if ((i == 0 or row[i - 1] not in cut)
          and (i == n - 1 or row[i + 1] not in cut)):
        s += 1
    elif (0 < i < n - 1
          and row[i - 1] in cut and row[i + 1] in cut):
      t += 1
  d = sum(
    row[i] in cut and row[i + 2] in cut
    for i in range(n - 2)
  )
  require(
    d == len(cut) - 2 * q + s + t,
    "LINEAR_RUN_IDENTITY",
    (row, tuple(sorted(cut)), q, s, t, d)
  )
  return s + t, q, d

def validate_finite_count(candidate, actual):
  require(
    candidate == actual,
    "FINITE_EXCLUDES_INFINITY",
    (candidate, actual)
  )

def validate_ordered_universe(candidate, vertices):
  expected = directed_universe(vertices)
  require(
    candidate == expected,
    "ORDERED_ARC_UNIVERSE",
    (len(candidate), len(expected))
  )

def validate_n1_minimum(candidate, actual):
  require(
    candidate == actual,
    "SHARP_N1_MINIMUM",
    (candidate, actual)
  )

def overlap_checks():
  row = tuple(range(1, 12))
  odd = frozenset(row[::2])
  counts = {t: 0 for t in range(1, 7)}
  finite_min = {t: 12 for t in range(1, 7)}
  augmented_min = {t: 13 for t in range(1, 7)}
  all_records = []
  for chosen in itertools.combinations(row, 6):
    tick()
    cut = frozenset(chosen)
    intersection = len(cut & odd)
    w, q, d = linear_counts(row, cut)
    singles = augmented_singletons(row, cut)
    finite = len(singles - frozenset((INF,)))
    augmented = len(singles)
    require(
      finite == w,
      "FINITE_LINEAR_CYCLIC_AGREEMENT",
      (chosen, finite, w)
    )
    closing_inside = int(row[0] in cut and row[-1] in cut)
    require(
      augmented - finite == closing_inside,
      "INFINITY_ENDPOINT_IDENTITY",
      (chosen, augmented, finite, closing_inside)
    )
    counts[intersection] += 1
    finite_min[intersection] = min(finite_min[intersection], finite)
    augmented_min[intersection] = min(
      augmented_min[intersection], augmented
    )
    all_records.append((cut, intersection, finite, augmented))
  require(
    len(all_records) == 462,
    "SIX_SUBSET_COVERAGE",
    len(all_records)
  )
  require(
    tuple(counts[t] for t in range(1, 7))
    == (6, 75, 200, 150, 30, 1),
    "INTERSECTION_CLASS_COUNTS",
    counts
  )
  require(
    tuple(finite_min[t] for t in range(1, 7))
    == (6, 0, 0, 0, 5, 11),
    "FINITE_OVERLAP_MINIMA",
    finite_min
  )
  require(
    tuple(augmented_min[t] for t in range(1, 7))
    == (6, 0, 0, 0, 6, 12),
    "AUGMENTED_OVERLAP_MINIMA",
    augmented_min
  )
  examples = (
    ((2, 4, 5, 6, 8, 10), 1, 6, 6),
    ((2, 3, 4, 8, 9, 10), 2, 0, 0),
    ((1, 2, 5, 6, 9, 10), 3, 0, 0),
    ((1, 2, 3, 7, 8, 9), 4, 0, 0),
    ((1, 3, 7, 8, 9, 11), 5, 5, 6),
    ((1, 3, 5, 7, 9, 11), 6, 11, 12),
  )
  checked_examples = []
  for chosen, expected_t, expected_w, expected_aug in examples:
    tick()
    cut = frozenset(chosen)
    w, q, d = linear_counts(row, cut)
    augmented = len(augmented_singletons(row, cut))
    actual = (len(cut & odd), w, augmented)
    require(
      actual == (expected_t, expected_w, expected_aug),
      "AUTHOR_SHARPNESS_INSTANCE",
      (chosen, actual)
    )
    checked_examples.append((chosen,) + actual)
  illustration_inputs = (
    ((1, 2, 3, 4, 5, 6), 1, 8),
    ((1, 2, 3, 4, 7, 8), 2, 4),
    ((1, 2, 5, 6, 9, 10), 3, 0),
  )
  illustrations = []
  for chosen, expected_runs, expected_e in illustration_inputs:
    tick()
    cut = frozenset(chosen)
    w, runs, d = linear_counts(row, cut)
    d_singletons = len(augmented_singletons(row, cut))
    e_singletons = len(augmented_singletons(row, odd ^ cut))
    require(
      len(odd & cut) == 3
      and d_singletons == 0
      and runs == expected_runs
      and e_singletons == expected_e
      and e_singletons == 12 - 4 * runs,
      "AUTHOR_ALTERNATING_INSTANCE",
      (chosen, runs, d_singletons, e_singletons)
    )
    illustrations.append((chosen, runs, d_singletons, e_singletons))
  record("six_subsets_checked", len(all_records))
  record("intersection_class_counts", tuple(counts.items()))
  record("finite_minima", tuple(finite_min.items()))
  record("augmented_minima", tuple(augmented_min.items()))
  record("sharpness_instances", tuple(checked_examples))
  record("alternating_instances", tuple(illustrations))
  return row, odd, finite_min

def parity(cell):
  return (cell & 1) ^ ((cell >> 1) & 1)

def truth_table_checks():
  table = {}
  allowed_count = 0
  allowed_e_count = 0
  alternating_count = 0
  for center, left, right in itertools.product(range(4), repeat=3):
    tick()
    a = center ^ left
    b = center ^ right
    no_bd = all(
      not (((left & bit) != (center & bit))
           and ((right & bit) != (center & bit)))
      for bit in (1, 2)
    )
    e_singleton = (
      parity(left) != parity(center)
      and parity(right) != parity(center)
    )
    no_own_neighbor = left != center and right != center
    require(
      no_bd == ((a & b) == 0),
      "TRANSITION_DISJOINTNESS",
      (center, left, right)
    )
    if no_bd:
      allowed_count += 1
      allowed_e_count += int(e_singleton)
      require(
        e_singleton == no_own_neighbor,
        "FOUR_CELL_E_EQUIVALENCE",
        (center, left, right)
      )
      if a == 3:
        require(b == 0, "DIAGONAL_NEIGHBOR_FORCING", (a, b))
      if b == 3:
        require(a == 0, "DIAGONAL_NEIGHBOR_FORCING", (a, b))
    b_alternating = bool(a & 1) and bool(b & 1)
    no_d_singleton = not (bool(a & 2) and bool(b & 2))
    if b_alternating and no_d_singleton:
      alternating_count += 1
      d_run_internal = not bool((a | b) & 2)
      require(
        e_singleton == d_run_internal,
        "ALTERNATING_E_LOCAL_IDENTITY",
        (center, left, right)
      )
    key = (a, b)
    value = (int(no_bd), int(e_singleton), int(no_own_neighbor))
    if key in table:
      old_value, multiplicity = table[key]
      require(
        old_value == value,
        "CELL_TRANSLATION_INVARIANCE",
        (key, old_value, value)
      )
      table[key] = (value, multiplicity + 1)
    else:
      table[key] = (value, 1)
  require(
    len(table) == 16 and all(n == 4 for value, n in table.values()),
    "TRUTH_TABLE_COVERAGE",
    table
  )
  require(
    (allowed_count, allowed_e_count, alternating_count) == (36, 8, 12),
    "TRUTH_TABLE_COUNTS",
    (allowed_count, allowed_e_count, alternating_count)
  )
  record("neighbor_triples_checked", 64)
  record(
    "transition_table_a_b_noBD_E_noOwn_translations",
    tuple((a, b) + table[(a, b)][0] + (table[(a, b)][1],)
          for a, b in sorted(table))
  )

def path_and_layout_checks():
  vertices = (0, 1, 2)
  universe = directed_universe(vertices)
  paths = tuple(itertools.permutations(vertices))
  path_arcs = tuple(
    frozenset(((path[0], path[1]), (path[1], path[2])))
    for path in paths
  )
  ordered_count = 0
  distinct_ordered_count = 0
  partitions = []
  for indices in itertools.product(range(len(paths)), repeat=3):
    tick()
    ordered_count += 1
    distinct_ordered_count += int(len(set(indices)) == 3)
    used = frozenset()
    disjoint = True
    for index in indices:
      if not used.isdisjoint(path_arcs[index]):
        disjoint = False
        break
      used = used | path_arcs[index]
    if disjoint and used == universe:
      partitions.append(indices)
  require(
    ordered_count == 216 and distinct_ordered_count == 120,
    "THREE_PATH_ENUMERATION_COVERAGE",
    (ordered_count, distinct_ordered_count)
  )
  require(
    not partitions,
    "THREE_VERTEX_PATH_OBSTRUCTION",
    partitions
  )
  unordered_checked = 0
  unordered_partitions = 0
  for indices in itertools.combinations(range(len(paths)), 3):
    tick()
    unordered_checked += 1
    sets = tuple(path_arcs[index] for index in indices)
    disjoint = all(
      sets[i].isdisjoint(sets[j])
      for i in range(3) for j in range(i + 1, 3)
    )
    if disjoint and frozenset().union(*sets) == universe:
      unordered_partitions += 1
  require(
    unordered_checked == 20 and unordered_partitions == 0,
    "UNORDERED_PATH_TRIPLE_CROSSCHECK",
    (unordered_checked, unordered_partitions)
  )
  options = {
    0: (frozenset(),),
    1: tuple(frozenset((arc,)) for arc in sorted(universe)),
    2: path_arcs,
  }
  def has_local_arc_cover(word):
    def visit(slot, used):
      tick()
      if slot == len(word):
        return used == universe
      for choice in options[word[slot]]:
        if used.isdisjoint(choice):
          if visit(slot + 1, used | choice):
            return True
      return False
    return visit(0, frozenset())
  raw_frequencies = {}
  local_frequencies = {}
  words_checked = 0
  edge_total_words = 0
  local_cover_words = 0
  for word in itertools.product((0, 1, 2), repeat=5):
    tick()
    words_checked += 1
    if sum(word) != 6:
      continue
    edge_total_words += 1
    frequency = (word.count(2), word.count(1), word.count(0))
    raw_frequencies[frequency] = raw_frequencies.get(frequency, 0) + 1
    if has_local_arc_cover(word):
      local_cover_words += 1
      local_frequencies[frequency] = (
        local_frequencies.get(frequency, 0) + 1
      )
  require(
    words_checked == 243 and edge_total_words == 45,
    "FIVE_SLOT_LAYOUT_COVERAGE",
    (words_checked, edge_total_words)
  )
  require(
    raw_frequencies == {(1, 4, 0): 5, (2, 2, 1): 30, (3, 0, 2): 10},
    "RAW_CELL_FREQUENCIES",
    raw_frequencies
  )
  require(
    local_frequencies == {(1, 4, 0): 5, (2, 2, 1): 30}
    and local_cover_words == 35,
    "DIRECTED_LOCAL_CELL_COVERS",
    local_frequencies
  )
  a, b, c = vertices
  reported_covers = (
    (
      frozenset(((a, b), (b, c))),
      frozenset(((a, c),)),
      frozenset(((b, a),)),
      frozenset(((c, a),)),
      frozenset(((c, b),)),
    ),
    (
      frozenset(((a, b), (b, c))),
      frozenset(((b, a), (a, c))),
      frozenset(((c, a),)),
      frozenset(((c, b),)),
      frozenset(),
    ),
  )
  for cover in reported_covers:
    tick()
    require(
      frozenset().union(*cover) == universe
      and sum(map(len, cover)) == len(universe),
      "AUTHOR_LOCAL_ARC_COVER",
      cover
    )
  accepted = []
  frequency_assignments = 0
  choices = tuple(sorted(local_frequencies))
  for four_cells in itertools.product(choices, repeat=4):
    tick()
    frequency_assignments += 1
    g_values = tuple(frequency[0] for frequency in four_cells)
    G = sum(g_values)
    for T in range(6, 19):
      if 72 - 4 * T + 12 + G == 36:
        accepted.append((four_cells, G, T))
  expected = [
    (((1, 4, 0),) * 4, 4, 13),
    (((2, 2, 1),) * 4, 8, 14),
  ]
  require(
    frequency_assignments == 16 and accepted == expected,
    "FOUR_CELL_GLOBAL_E_LEDGER",
    (frequency_assignments, accepted)
  )
  record("directed_three_vertex_arcs", tuple(sorted(universe)))
  record("directed_three_vertex_paths", paths)
  record("ordered_path_triples", ordered_count)
  record("distinct_ordered_path_triples", distinct_ordered_count)
  record("unordered_distinct_path_triples", unordered_checked)
  record("three_path_partitions", len(partitions))
  record("five_slot_words_checked", words_checked)
  record("edge_total_six_layout_words", edge_total_words)
  record("raw_cell_frequency_counts", tuple(sorted(raw_frequencies.items())))
  record("local_arc_cover_frequency_counts",
         tuple(sorted(local_frequencies.items())))
  record("four_cell_frequency_assignments", frequency_assignments)
  record("E_budget_accepted_relational_ledgers", tuple(accepted))

def conditional_budget(n, b, missing, closing):
  require(
    missing == closing,
    "M_EQUALS_C_REQUIRED",
    (tuple(sorted(missing)), tuple(sorted(closing)))
  )
  return b * (n + 1 - b)

def actual_t2_four_checks():
  rows = (
    (0, 1, 3, 2),
    (1, 2, 0, 3),
    (2, 3, 1, 0),
    (3, 0, 2, 1),
  )
  vertices = tuple(range(4))
  vertex_set = frozenset(vertices)
  n = len(vertices)
  require(len(rows) == n, "ACTUAL_ROW_COUNT", len(rows))
  adjacency = []
  distance_two = []
  for row in rows:
    tick()
    require(
      len(row) == n and frozenset(row) == vertex_set,
      "ACTUAL_PERMUTATION_ROW",
      row
    )
    adjacency.extend(zip(row, row[1:]))
    distance_two.extend(zip(row, row[2:]))
  universe = directed_universe(vertices)
  require(
    len(adjacency) == n * (n - 1)
    and len(set(adjacency)) == len(adjacency)
    and frozenset(adjacency) == universe,
    "ACTUAL_DIRECTED_ADJACENCY",
    adjacency
  )
  require(
    len(distance_two) == n * (n - 2)
    and len(set(distance_two)) == len(distance_two)
    and frozenset(distance_two) <= universe,
    "ACTUAL_ORIGINAL_DISTANCE_TWO",
    distance_two
  )
  closing_events = tuple((row[-1], row[0]) for row in rows)
  closing = frozenset(closing_events)
  missing = universe - frozenset(distance_two)
  require(
    len(closing) == n
    and frozenset(row[0] for row in rows) == vertex_set
    and frozenset(row[-1] for row in rows) == vertex_set,
    "ACTUAL_ENDPOINT_PERMUTATIONS",
    closing_events
  )
  require(
    missing == closing
    == frozenset(((0, 2), (1, 3), (2, 0), (3, 1))),
    "ACTUAL_T2_FOUR_M_EQUALS_C",
    (missing, closing)
  )
  subset_records = []
  for b in range(n + 1):
    for chosen in itertools.combinations(vertices, b):
      tick()
      cut = frozenset(chosen)
      W = 0
      augmented_W = 0
      q_total = 0
      for row in rows:
        finite, q, d = linear_counts(row, cut)
        singles = augmented_singletons(row, cut)
        require(
          finite == len(singles - frozenset((INF,))),
          "ACTUAL_FINITE_SINGLETON_AGREEMENT",
          (row, chosen)
        )
        W += finite
        augmented_W += len(singles)
        q_total += q
      mu = sum(a in cut and b_vertex in cut
               for a, b_vertex in missing)
      nu = sum(a in cut and b_vertex in cut
               for a, b_vertex in closing)
      require(
        q_total == b * (n + 1 - b),
        "ACTUAL_BLACK_RUN_TOTAL",
        (chosen, q_total)
      )
      require(
        W == b * (n + 1 - b) - mu,
        "ACTUAL_FINITE_SINGLETON_BUDGET",
        (chosen, W, mu)
      )
      require(
        augmented_W == W + nu,
        "ACTUAL_AUGMENTED_ENDPOINT_BUDGET",
        (chosen, augmented_W, W, nu)
      )
      require(
        augmented_W == conditional_budget(n, b, missing, closing),
        "ACTUAL_CONDITIONAL_SINGLETON_BUDGET",
        (chosen, augmented_W)
      )
      subset_records.append((chosen, W, augmented_W, mu, nu))
  require(
    len(subset_records) == 16,
    "ACTUAL_T2_FOUR_SUBSET_COVERAGE",
    len(subset_records)
  )
  record("actual_T2_four_rows", rows)
  record("actual_T2_four_adjacency_events", tuple(adjacency))
  record("actual_T2_four_original_D2_events", tuple(distance_two))
  record("actual_T2_four_missing_pairs", tuple(sorted(missing)))
  record("actual_T2_four_closing_events", closing_events)
  record("actual_T2_four_all_subset_records", tuple(subset_records))
  return vertices, adjacency, missing, closing

def validate_hamilton_successor(successor):
  n = len(successor)
  require(
    n >= 3 and frozenset(successor) == frozenset(range(n)),
    "SUCCESSOR_PERMUTATION",
    successor
  )
  visited = set()
  current = 0
  while current not in visited:
    tick()
    visited.add(current)
    current = successor[current]
  require(
    current == 0 and len(visited) == n,
    "ACTUAL_HAMILTONICITY",
    (len(visited), n)
  )

def disconnected_control_fixture():
  successor = (1, 2, 3, 8, 5, 6, 7, 4, 9, 10, 11, 0)
  cells = (3, 3, 3, 3, 1, 1, 2, 2, 0, 0, 0, 0)
  predecessor = [None] * len(successor)
  require(
    frozenset(successor) == frozenset(range(12)),
    "DISCONNECTED_FIXTURE_PERMUTATION",
    successor
  )
  for vertex, target in enumerate(successor):
    predecessor[target] = vertex
  jk_arcs = []
  for vertex, target in enumerate(successor):
    tick()
    a = cells[vertex] ^ cells[predecessor[vertex]]
    b = cells[vertex] ^ cells[target]
    require(
      (a & b) == 0,
      "DISCONNECTED_FIXTURE_LOCAL_PREMISES",
      vertex
    )
    if frozenset((cells[vertex], cells[target])) == frozenset((1, 2)):
      jk_arcs.append((vertex, target))
  require(
    len(jk_arcs) == 2,
    "DISCONNECTED_FIXTURE_TWO_JK_ARCS",
    jk_arcs
  )
  record("disconnected_cover_fixture_cycles",
         ((4, 5, 6, 7), (0, 1, 2, 3, 8, 9, 10, 11)))
  record("disconnected_cover_fixture_JK_arcs", tuple(jk_arcs))
  return successor

def validate_e_ledger(g_values, T):
  G = sum(g_values)
  require(
    72 - 4 * T + 12 + G == 36,
    "E_SINGLETON_BUDGET",
    (g_values, G, T, 72 - 4 * T + 12 + G)
  )

def expect_rejection(name, expected_reason, operation):
  tick()
  try:
    operation()
  except GateFailure as exc:
    if exc.reason in INCOMPLETE_REASONS:
      raise
    require(
      exc.reason == expected_reason,
      "CONTROL_WRONG_REASON",
      (name, expected_reason, exc.reason, exc.detail)
    )
    record("mutation_" + name, ("REJECTED", exc.reason, exc.detail))
  else:
    raise GateFailure(
      "MUTATION_NOT_REJECTED",
      (name, expected_reason)
    )

def main():
  require(len(sys.argv) == 1, "ARGUMENTS", sys.argv[1:])
  signal.signal(signal.SIGINT, request_stop)
  signal.signal(signal.SIGTERM, request_stop)
  row, odd, finite_min = overlap_checks()
  truth_table_checks()
  path_and_layout_checks()
  vertices, adjacency, missing, closing = actual_t2_four_checks()
  validate_hamilton_successor(tuple(range(1, 12)) + (0,))
  disconnected = disconnected_control_fixture()
  finite_odd = linear_counts(row, odd)[0]
  augmented_odd = len(augmented_singletons(row, odd))
  expect_rejection(
    "count_infinity",
    "FINITE_EXCLUDES_INFINITY",
    lambda: validate_finite_count(augmented_odd, finite_odd)
  )
  unordered_adjacency = frozenset(
    tuple(sorted(arc)) for arc in adjacency
  )
  expect_rejection(
    "unordered_arcs",
    "ORDERED_ARC_UNIVERSE",
    lambda: validate_ordered_universe(unordered_adjacency, vertices)
  )
  expect_rejection(
    "allow_disconnected_cycle4",
    "ACTUAL_HAMILTONICITY",
    lambda: validate_hamilton_successor(disconnected)
  )
  synthetic_closing = frozenset(
    (vertex, (vertex + 1) % 4) for vertex in vertices
  )
  record(
    "M_equals_C_negative_fixture_scope",
    "synthetic interface input; not actual closing pairs of the T2(4)"
  )
  expect_rejection(
    "omit_M_equals_C",
    "M_EQUALS_C_REQUIRED",
    lambda: conditional_budget(4, 2, missing, synthetic_closing)
  )
  expect_rejection(
    "lower_N1_bound_wrong",
    "SHARP_N1_MINIMUM",
    lambda: validate_n1_minimum(5, finite_min[1])
  )
  expect_rejection(
    "missing_E_constraint",
    "E_SINGLETON_BUDGET",
    lambda: validate_e_ledger((1, 1, 1, 2), 13)
  )
  tick()
  print("RESULT: PASS_REQUESTED_FINITE_COMPONENTS_ONLY")
  for line in REPORT:
    print(line)
  print("elapsed_seconds:", time.monotonic() - STARTED)
  print(
    "NOT_ESTABLISHED: actual T2(11), unrestricted nonexistence, "
    "five compatible global residual Hamilton cycles, "
    "universal M=C, novelty, human/family/kernel verification, "
    "or parent adoption"
  )

if __name__ == "__main__":
  try:
    main()
  except GateFailure as exc:
    status = (
      "INCOMPLETE"
      if exc.reason in INCOMPLETE_REASONS
      else "CHECK_FAILED"
    )
    print("RESULT:", status, file=sys.stderr)
    print("reason:", exc.reason, file=sys.stderr)
    print("detail:", repr(exc.detail), file=sys.stderr)
    sys.exit(1)

