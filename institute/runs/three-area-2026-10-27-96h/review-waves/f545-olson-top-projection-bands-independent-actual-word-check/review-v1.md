# F545 — FINITE independent actual-word checker candidate

**FINITE gate: NOT RUN / NOT PASS.**  
**Established candidate-defect findings: F=0 / M=0 / m=0.** This is not an executed zero-finding review or acceptance of the general theorem.

The assignment’s NOEXEC fallback is fulfilled below: complete independent checker source, exact prospective invocation, embedded inputs, targeted controls, and explicit limitations. No interpreter, scientific executable, external model, subagent, build, test, or file-write bypass was used.

## 1. Input binding and chronology

Before reading mathematical content, I completely read:

- The manifest, supplied SHA256 **8874aee68fcc39b9d6f45106cc8236f9335dce31fd939433e1c1434e07498272**.
- The freeze receipt, supplied SHA256 **76b950417ef3780b0586a1b02fe5e50e8e476ee316668d71a910d1c35a99debc**.
- The parent live-metadata supply and dispatch receipt.
- Every manifest-listed status/permission control, through its ending.

I then issued the direct pre-body ACK. Afterward, I read literal-packet-v1.md sequentially in raw windows 1–20, 21–40, …, 341–360, 361–379, through **S1|377**, before deriving or authoring this checker.

The supplied packet SHA256 is **3d4dda013b96fd776a6373ba56365618acf05344a40c12212d1b92ca8c9d59ce**. Its sole mathematical input is the complete F495 candidate, supplied source SHA256 **f02e2f8def6d00b078be42a7072c9458ea89d23b921e4b5407bed57671ea6ca4**.

These are **parent-supplied bindings, not child-computed hashes**. No child-native execution clock or elapsed-time measurement exists.

No cited-but-unpasted source, author program, sibling return, F497 body, or held scientific payload was opened. Held episodes and all their consumers remained NONINPUT. This records access/use chronology, not cognitive isolation, source authenticity, or clean-provenance certification.

## 2. Written actual-word checks

These are written calculations after the complete packet read, not machine results.

### Exact assigned \(p=5\) witness

The source’s reflection labels, S1|323–337, are

\[
(0,0,0,1,0,1,2,3,4,0,1,2,3),
\]

with \(\rho_1\) immediately after reflection occurrences 1 through 6.

Consequently, the reflection-to-actual-word position map, using one-based indices, is

\[
(1,3,5,7,9,11,13,14,15,16,17,18,19).
\]

The source’s selected reflection occurrences, S1|350–360,

\[
1,2,3,4,6,7,8,10,12,13,
\]

therefore select actual-word positions

\[
\boxed{1,3,5,7,11,13,14,16,18,19}.
\]

Their original-order labels are

\[
0,0,0,1,1,2,3,0,2,3,
\]

and the alternating exponent is

\[
0-0+0-1+1-2+3-0+2-3=0.
\]

There are exactly ten selected reflections and no selected rotations.

### The partition-phase control uses this same word

Cut before reflection occurrence 4. The rich first triple is \((r_4,r_5,r_6)\), labelled \((1,0,1)\).

The first partition phase has blocks

\[
(r_4,r_5,r_6),\ (r_7,r_8),\ (r_9,r_{10}),\
(r_{11},r_{12},r_{13}),\ (r_1,r_2,r_3).
\]

Its last triple is constant, so this phase is unsuitable.

The second phase has blocks

\[
(r_4,r_5,r_6),\ (r_7,r_8,r_9),\
(r_{10},r_{11},r_{12}),\ (r_{13},r_1),\ (r_2,r_3).
\]

Choosing pairs

\[
(r_4,r_6),\ (r_7,r_8),\ (r_{10},r_{12}),\
(r_{13},r_1),\ (r_2,r_3)
\]

gives exponents \(0,4,3,3,0\), summing to zero modulo 5. These are exactly the source’s selected occurrences, merely displayed in cut order. This is not a replacement or synthetic shadow witness.

### Additional separating controls on the same actual word

- **Wrong sign:** replacing semidirect multiplication with ordinary coordinate addition gives the selected source witness exponent \(12\equiv2\pmod5\), rather than zero.
- **Quotient-only:** the first ten reflection occurrences have even parity but exponent \(1\pmod5\), so quotient identity does not certify group identity.
- **Ignoring occurrence order:** swapping the fourth and ninth entries of that invalid ten-occurrence selection produces exponent zero in the artificial order. The checker must reject that ordering; the original-order subsequence remains nonidentity.
- **Projection versus actual blocks:** deleting rotations gives \(o_\pi=11\). Treating rotations as barriers to merging equal reflection labels instead gives 13.
- **Nonidentity conjugation:** the complete assigned actual word has product \((3,1)\); moving its first actual letter \(\sigma_0\) to the end gives \((2,1)\). Thus arbitrary cyclic products are conjugate, not generally equal.

An **explanatory omission** of conjugation alone has no separating identity-output control: a valid selected identity remains identity at every cut. That omission is explicitly **NOT TESTED as a proof defect**, rather than being assigned an invented counterexample. The source below separately tests the concrete erroneous behavior “all cyclic products remain equal.”

## 3. Prospective finite scope

All entries below are **implemented but NOT RUN**.

| Component | Exact prospective coverage |
|---|---|
| \(p=3\) reflection lists | All \(3^7=2187\) lists, then filter by the rotation-deleted cyclic projection count \(o_\pi\in\{5,7\}\) |
| Actual words for those lists | Four legitimate \(\rho_1\) occurrences, in distinct singleton cyclic gaps |
| Selection comparison | Rich-partition/sumset-DP construction versus an independent original-order full-group subsequence DP |
| Witness consumption | Exactly \(2p\) distinct, increasing actual-word indices; reflections only; direct group product identity |
| Cut transport | Every actual-word cyclic cut for both selectors and the assigned witness |
| Assigned \(p=5\) example | Exact labels, rotations, occurrence indices, and source witness above |
| Bounded \(p=5,7,11\) controls | 24 listed cases per prime: all-single, one-double, one-triple cyclic-run constructions; not asserted distinct or exhaustive |
| Cauchy–Davenport interface | Every ordered pair of nonempty subsets for \(p=3,5,7\): 17,139 pairs |
| Triple-\(\Delta\) interface | Every triple over \(p=3,5,7,11\): 1,826 triples |
| Mutation controls | Wrong sign; quotient/order loss; wrong projection runs; wrong block count; duplicated partition phase; erroneous cyclic-product invariance; wrong selector length |
| Deadline | Cooperative computation cutoff at 54 seconds, with no PASS after that cutoff |

The 54-second computation cutoff leaves margin within the assignment’s 55-second bound. This is not a claim about an observed runtime or an operating-system hard scheduling guarantee.

## 4. Prospective invocation — NOT RUN

Proposed filename, **not created**: finite-checker-v1.py.

Working directory: the supplied F545 frozen-wave directory.

Exact prospective argv:

python3 -I -B ./finite-checker-v1.py

The checker takes no input files or arguments. It performs no file writes, network access, child-process launch, installation, or deletion. Its only output operation is a stdout status/counter report. Exit status 0 requires completion of every implemented check; status 1 reports an invariant failure; status 2 reports the cooperative deadline. An unexpected exception cannot produce PASS.

## 5. Complete source — NOT RUN

# BEGIN finite-checker-v1.py
from collections import Counter
from itertools import combinations, product
from time import monotonic


class CheckError(Exception):
 pass


class BudgetExpired(Exception):
 pass


END = 0.0
IDENTITY = (0, 0)


def need(condition, reason):
 if not condition:
  raise CheckError(reason)


def tick():
 if monotonic() >= END:
  raise BudgetExpired()


def mul(g, h, p):
 return ((g[0] + (h[0] if g[1] == 0 else -h[0])) % p,
         (g[1] + h[1]) % 2)


def inv(g, p):
 return ((-g[0] if g[1] == 0 else g[0]) % p, g[1])


def plus_mul(g, h, p):
 return ((g[0] + h[0]) % p, (g[1] + h[1]) % 2)


def word_product(word, indices, p, operation=mul):
 value = IDENTITY
 for index in indices:
  value = operation(value, word[index], p)
 return value


def cyclic_run_lengths(labels, joins=None):
 n = len(labels)
 need(n > 0, "empty-projection")
 if joins is None:
  joins = tuple(labels[i] == labels[(i + 1) % n] for i in range(n))
 need(len(joins) == n, "joins-length")
 if all(joins):
  return (n,)
 broken = next(i for i in range(n) if not joins[i])
 start = (broken + 1) % n
 lengths = []
 length = 1
 for step in range(1, n):
  if joins[(start + step - 1) % n]:
   length += 1
  else:
   lengths.append(length)
   length = 1
 lengths.append(length)
 return tuple(lengths)


def inspect_word(word, p):
 need(p in (3, 5, 7, 11), "unsupported-prime")
 need(len(word) > 0, "empty-word")
 need(all(len(g) == 2 and 0 <= g[0] < p and g[1] in (0, 1)
          for g in word), "group-element")
 refs = tuple(i for i, g in enumerate(word) if g[1] == 1)
 need(len(refs) == 3 * p - 2, "reflection-count")
 need(len(word) - len(refs) >= p + 1, "rotation-count")
 need(all(word[i][1] != 0 or word[(i + 1) % len(word)][1] != 0
          for i in range(len(word))), "rotation-gap")
 labels = tuple(word[i][0] for i in refs)
 runs = cyclic_run_lengths(labels)
 need(sum(runs) == len(refs), "run-cover")
 odd = sum(length % 2 for length in runs)
 return refs, runs, odd


def make_word(labels, p, gaps=None):
 n = len(labels)
 if gaps is None:
  gaps = tuple(range(p + 1))
 need(len(set(gaps)) == p + 1, "gap-count")
 need(all(0 <= i < n for i in gaps), "gap-index")
 occupied = set(gaps)
 word = []
 for i, label in enumerate(labels):
  word.append((label, 1))
  if i in occupied:
   word.append((1, 0))
 return tuple(word)


def pair_options(word, block, p):
 options = {}
 for i, j in combinations(block, 2):
  exponent = (word[i][0] - word[j][0]) % p
  options.setdefault(exponent, (i, j))
 return options


def pattern(p, phase, q=None):
 if q is None:
  q = p - 3
 if phase == 0:
  return (3, 2, 2) + (3,) * q
 return (3,) + (3,) * q + (2, 2)


def checked_partition(word, p, refs, cut, sizes):
 need(0 <= cut < len(refs), "cut-index")
 need(len(sizes) == p, "block-count")
 need(sum(sizes) == len(refs), "block-cover")
 need(sizes[0] == 3 and sizes.count(2) == 2
      and sizes.count(3) == p - 2, "block-shape")
 ordered = refs[cut:] + refs[:cut]
 option_sets = []
 offset = 0
 for block_index, size in enumerate(sizes):
  tick()
  block = ordered[offset:offset + size]
  offset += size
  options = pair_options(word, block, p)
  if block_index == 0:
   need(len(options) == 3, "rich-triple")
  elif size == 3:
   need(len(options) >= 2, "constant-triple")
  else:
   need(len(options) == 1, "pair-interface")
  option_sets.append(options)
 need(offset == len(refs), "block-cover")
 states = {0: ()}
 for options in option_sets:
  tick()
  following = {}
  for total, chosen in states.items():
   for exponent, pair in options.items():
    following.setdefault((total + exponent) % p, chosen + pair)
  states = following
 need(set(states) == set(range(p)), "sumset-cover")
 return states[0]


def choose_at_cut(word, p, refs, cut, duplicate_first_phase=False):
 phases = (0, 0) if duplicate_first_phase else (0, 1)
 for phase in phases:
  try:
   selected = checked_partition(word, p, refs, cut, pattern(p, phase))
   return selected, phase
  except CheckError as error:
   if str(error) != "constant-triple":
    raise
 raise CheckError("no-phase")


def constructive_selection(word, p, refs):
 n = len(refs)
 labels = tuple(word[i][0] for i in refs)
 for cut in range(n):
  tick()
  triple = tuple(refs[(cut + j) % n] for j in range(3))
  if len(pair_options(word, triple, p)) == 3:
   chosen, phase = choose_at_cut(word, p, refs, cut)
   need(word_product(word, chosen, p) == IDENTITY, "cut-product")
   return tuple(sorted(chosen)), chosen, "rich"
 equal_edges = tuple(i for i in range(n)
                     if labels[i] == labels[(i + 1) % n])
 if len(equal_edges) == 0:
  chain = refs
 elif len(equal_edges) == 1:
  start = (equal_edges[0] + 1) % n
  chain = refs[start:] + refs[:start]
 else:
  need(len(equal_edges) == 2, "ap-run-shape")
  start_of_triple = next(
   (i for i in range(n)
    if labels[i] == labels[(i + 1) % n] == labels[(i + 2) % n]),
   None)
  need(start_of_triple is not None, "ap-triple-run")
  start = (start_of_triple + 2) % n
  chain = tuple(refs[(start + j) % n] for j in range(n - 1))
 need(len(chain) >= 2 * p, "ap-chain-length")
 difference = (word[chain[1]][0] - word[chain[0]][0]) % p
 need(difference != 0, "ap-zero-difference")
 need(all((word[chain[j + 1]][0] - word[chain[j]][0]) % p
          == difference for j in range(len(chain) - 1)),
      "ap-recurrence")
 chosen = chain[:2 * p]
 need(word_product(word, chosen, p) == IDENTITY, "ap-product")
 return tuple(sorted(chosen)), chosen, "ap"


def independent_group_dp(word, p):
 target = 2 * p
 states = [dict() for _ in range(target + 1)]
 states[0][IDENTITY] = ()
 seen = 0
 for index, element in enumerate(word):
  tick()
  if element[1] != 1:
   continue
  for count in range(min(seen, target - 1), -1, -1):
   for value, chosen in states[count].items():
    following = mul(value, element, p)
    states[count + 1].setdefault(following, chosen + (index,))
  seen += 1
 return states[target].get(IDENTITY)


def validate_selection(word, p, selected, operation=mul):
 selected = tuple(selected)
 need(len(selected) == 2 * p, "length")
 need(all(isinstance(i, int) and 0 <= i < len(word)
          for i in selected), "index")
 need(len(set(selected)) == len(selected), "distinct")
 need(selected == tuple(sorted(selected)), "order")
 need(all(word[i][1] == 1 for i in selected), "selected-rotation")
 need(word_product(word, selected, p, operation) == IDENTITY, "product")


def all_identity_cuts(word, p, selected, stats):
 selected = tuple(selected)
 validate_selection(word, p, selected)
 original = word_product(word, selected, p)
 n = len(word)
 for cut in range(n):
  tick()
  rotated = word[cut:] + word[:cut]
  transported = tuple(sorted((i - cut) % n for i in selected))
  validate_selection(rotated, p, transported)
  prefix = word_product(word, (i for i in selected if i < cut), p)
  expected = mul(mul(inv(prefix, p), original, p), prefix, p)
  need(word_product(rotated, transported, p) == expected,
       "identity-cut-conjugacy")
  stats["selected_cut_checks"] += 1


def check_case(word, p, stats):
 refs, runs, odd = inspect_word(word, p)
 f = 3 * p - 2
 need(odd in (f - 2, f), "outside-top-bands")
 nonsingle = tuple(length for length in runs if length != 1)
 need(nonsingle in ((), (2,), (3,)), "top-band-run-shape")
 actual, cyclic, method = constructive_selection(word, p, refs)
 validate_selection(word, p, actual)
 need(len(cyclic) == 2 * p and set(cyclic) == set(actual),
      "transport-occurrences")
 need(word_product(word, cyclic, p) == IDENTITY, "cyclic-selection-product")
 exact = independent_group_dp(word, p)
 need(exact is not None, "exact-dp-no-witness")
 validate_selection(word, p, exact)
 all_identity_cuts(word, p, actual, stats)
 all_identity_cuts(word, p, exact, stats)
 stats["case_checks"] += 1
 stats["branch_" + method] += 1
 return method


def expect_error(reason, action):
 tick()
 try:
  action()
 except CheckError as error:
  need(str(error) == reason,
       "wrong-rejection:" + reason + ":" + str(error))
  return
 raise CheckError("mutant-not-separated:" + reason)


def author_controls(stats):
 p = 5
 labels = (0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1, 2, 3)
 word = make_word(labels, p)
 refs, runs, odd = inspect_word(word, p)
 need(tuple(i + 1 for i in refs)
      == (1, 3, 5, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19),
      "author-reflection-map")
 reflection_indices = (1, 2, 3, 4, 6, 7, 8, 10, 12, 13)
 selected = tuple(refs[i - 1] for i in reflection_indices)
 need(tuple(i + 1 for i in selected)
      == (1, 3, 5, 7, 11, 13, 14, 16, 18, 19),
      "author-selected-map")
 need(odd == 11 and sorted(runs) == [1] * 10 + [3],
      "author-projection")
 validate_selection(word, p, selected)
 all_identity_cuts(word, p, selected, stats)
 check_case(word, p, stats)
 stats["author_witness_checks"] += 1

 need(word_product(word, selected, p, plus_mul) == (2, 0),
      "sign-control-value")
 expect_error("product",
              lambda: validate_selection(word, p, selected, plus_mul))
 stats["mutant_wrong_sign"] = 1

 bad = refs[:10]
 need(sum(word[i][1] for i in bad) % 2 == 0, "quotient-control")
 need(word_product(word, bad, p) == (1, 0), "quotient-control-value")
 expect_error("product", lambda: validate_selection(word, p, bad))
 reordered = list(bad)
 reordered[3], reordered[8] = reordered[8], reordered[3]
 need(word_product(word, reordered, p) == IDENTITY, "order-control-value")
 expect_error("order", lambda: validate_selection(word, p, reordered))
 stats["mutant_quotient_order"] = 1

 joins = tuple(
  word[refs[j]][0] == word[refs[(j + 1) % len(refs)]][0]
  and refs[(j + 1) % len(refs)] == (refs[j] + 1) % len(word)
  for j in range(len(refs)))
 segmented_runs = cyclic_run_lengths(labels, joins)
 segmented_odd = sum(length % 2 for length in segmented_runs)
 need(segmented_odd == 13, "segmented-control-value")
 expect_error("projection-runs",
              lambda: need(segmented_odd == odd, "projection-runs"))
 stats["mutant_projection_runs"] = 1

 expect_error(
  "block-count",
  lambda: checked_partition(word, p, refs, 2,
                            pattern(p, 0, q=p - 2)))
 stats["mutant_block_count"] = 1

 expect_error(
  "constant-triple",
  lambda: checked_partition(word, p, refs, 3, pattern(p, 0)))
 phase_selected, phase = choose_at_cut(word, p, refs, 3)
 need(phase == 1, "phase-control-choice")
 validate_selection(word, p, tuple(sorted(phase_selected)))
 all_identity_cuts(word, p, tuple(sorted(phase_selected)), stats)
 expect_error(
  "no-phase",
  lambda: choose_at_cut(word, p, refs, 3, duplicate_first_phase=True))
 stats["mutant_partition_phase"] = 1

 full = word_product(word, range(len(word)), p)
 need(full == (3, 1), "full-word-control-value")
 for cut in range(len(word)):
  tick()
  rotated = word[cut:] + word[:cut]
  prefix = word_product(word, range(cut), p)
  expected = mul(mul(inv(prefix, p), full, p), prefix, p)
  need(word_product(rotated, range(len(word)), p) == expected,
       "full-word-conjugacy")
  stats["nonidentity_cut_checks"] += 1
 rotated_once = word[1:] + word[:1]
 moved = word_product(rotated_once, range(len(word)), p)
 need(moved == (2, 1), "moved-word-control-value")
 expect_error("cyclic-product-invariance",
              lambda: need(moved == full, "cyclic-product-invariance"))
 stats["mutant_cyclic_product_invariance"] = 1
 stats["proof_only_conjugation_omission_NOT_TESTED"] = 1

 expect_error("length",
              lambda: validate_selection(word, p, selected[:-2]))
 expect_error("length",
              lambda: validate_selection(word, p, refs[:12]))
 stats["mutant_selector_length"] = 1


def check_interfaces(stats):
 for p in (3, 5, 7):
  subsets = tuple(
   tuple(i for i in range(p) if mask & (1 << i))
   for mask in range(1, 1 << p))
  for a, b in product(subsets, repeat=2):
   tick()
   sums = {(x + y) % p for x in a for y in b}
   need(len(sums) >= min(p, len(a) + len(b) - 1),
        "cauchy-davenport")
   stats["cd_subset_pairs"] += 1

 for p in (3, 5, 7, 11):
  for values in product(range(p), repeat=3):
   tick()
   a, b, c = values
   delta = {(a - b) % p, (a - c) % p, (b - c) % p}
   triple = tuple((value, 1) for value in values)
   direct = set()
   for i, j in combinations(range(3), 2):
    value = mul(triple[i], triple[j], p)
    need(value[1] == 0, "delta-pair-parity")
    direct.add(value[0])
   need(delta == direct, "delta-interface")
   if len(set(values)) == 1:
    need(delta == {0}, "constant-delta")
   else:
    need(len(delta) >= 2, "nonconstant-delta")
   if a != b and b != c and len(delta) < 3:
    need((a - b) % p == (b - c) % p, "nonrich-recurrence")
   stats["delta_triples"] += 1


def bounded_words(p):
 f = 3 * p - 2
 for run_length in (1, 2, 3):
  run_count = f - run_length + 1
  base = [i % 2 for i in range(run_count)]
  if run_count % 2:
   base[-1] = 2
  for variant in range(8):
   scale = 1 + variant % (p - 1)
   shift = (variant * variant + 3 * variant) % p
   colors = tuple((scale * value + shift) % p for value in base)
   need(all(colors[i] != colors[(i + 1) % run_count]
            for i in range(run_count)), "generated-cyclic-labels")
   long_run = (7 * variant + 1) % run_count
   labels = tuple(
    color
    for i, color in enumerate(colors)
    for _ in range(run_length if i == long_run else 1))
   need(len(labels) == f, "generated-reflection-count")
   cut = (5 * variant + 2) % f
   labels = labels[cut:] + labels[:cut]
   gaps = tuple((variant + j) % f for j in range(p + 1))
   word = make_word(labels, p, gaps)
   refs, runs, odd = inspect_word(word, p)
   expected_runs = sorted([run_length] + [1] * (run_count - 1))
   need(sorted(runs) == expected_runs, "generated-run-shape")
   expected_odd = f if run_length == 1 else f - 2
   need(odd == expected_odd, "generated-band")
   yield word, run_length


def main():
 global END
 started = monotonic()
 END = started + 54.0
 stats = Counter()
 try:
  check_interfaces(stats)
  author_controls(stats)

  for labels in product(range(3), repeat=7):
   tick()
   stats["p3_lists_seen"] += 1
   word = make_word(labels, 3)
   refs, runs, odd = inspect_word(word, 3)
   if odd not in (5, 7):
    continue
   stats["p3_top_lists_checked"] += 1
   method = check_case(word, 3, stats)
   stats["p3_branch_" + method] += 1
  need(stats["p3_lists_seen"] == 2187, "p3-exhaustion")
  need(stats["p3_branch_rich"] > 0, "p3-rich-coverage")
  need(stats["p3_branch_ap"] > 0, "p3-ap-coverage")

  for p in (5, 7, 11):
   for word, run_length in bounded_words(p):
    tick()
    check_case(word, p, stats)
    stats["bounded_p" + str(p)] += 1
    stats["bounded_p" + str(p) + "_run" + str(run_length)] += 1
   need(stats["bounded_p" + str(p)] == 24, "bounded-case-count")
   for run_length in (1, 2, 3):
    need(stats["bounded_p" + str(p) + "_run" + str(run_length)] == 8,
         "bounded-shape-count")

  need(stats["cd_subset_pairs"] == 17139, "cd-exhaustion")
  need(stats["delta_triples"] == 1826, "delta-exhaustion")
  mutant_keys = (
   "mutant_wrong_sign",
   "mutant_quotient_order",
   "mutant_projection_runs",
   "mutant_block_count",
   "mutant_partition_phase",
   "mutant_cyclic_product_invariance",
   "mutant_selector_length")
  need(all(stats[key] == 1 for key in mutant_keys), "mutation-coverage")
  tick()
 except BudgetExpired:
  print("STATUS: NOTPASS_DEADLINE")
  print("Completed counters only:", sorted(stats.items()))
  print("Elapsed seconds:", monotonic() - started)
  return 2
 except CheckError as error:
  print("STATUS: NOTPASS_INVARIANT")
  print("Reason:", str(error))
  print("Completed counters only:", sorted(stats.items()))
  print("Elapsed seconds:", monotonic() - started)
  return 1

 print("STATUS: PASS_FINITE_SCOPE_ONLY")
 print("Counters:", sorted(stats.items()))
 print("Elapsed seconds:", monotonic() - started)
 print("NOTTESTED: proof-only omission of a conjugation explanation.")
 print("No general theorem, avoiding-word, or full Olson certificate.")
 return 0


if __name__ == "__main__":
 raise SystemExit(main())
# END finite-checker-v1.py

## 6. Disposition and exact unpaid obligations

**Current executable evidence: none.** The enumeration counts, DP comparisons, mutation rejections, cut checks, and runtime have not been observed. The source contains executable requirements for them, not fabricated results. It has not been independently checked by another implementation, family, human, or kernel.

The written \(p=5\) checks above support the exact source witness and expose concrete distinctions the checker must preserve. They do not substitute for executing the finite assignment.

The F495 statement remains a separate whole-parameter written-proof candidate for the two bands \(o_\pi=3p-4,3p-2\). Even a future complete finite-scope PASS would not prove that statement for every odd prime.

The source’s remaining high-run obligation, S1|287–317, is unchanged:

\[
p+4\le o_\pi\le3p-6,\qquad o_\pi\ \text{odd}.
\]

In particular, the uniform deficit-four structural bridge remains unpaid. Lower bands, unrestricted ordered-Olson closure, all-group closure, an actual avoiding-word certificate, novelty, and original-source authentication are not established.

**No repository or scratch file was created or edited. This full body is returned for Main materialization; the FINITE gate remains NOT RUN / NOT PASS.**