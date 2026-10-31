#!/usr/bin/env python3
"""Independent f142 q=5 finite replay. No author/prior-review code is imported."""
import hashlib
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "manifest-v1.json"
RECEIPT = HERE / "finite-receipt-v1.json"
MANIFEST_SHA = "18c99ee567c62fce537563f4fde06bebb1308b4549e5417191bfcecf7d331d02"
PDF_SHA = "b010546db8230a39741997807a1110402c4f24fb7e897441e66fc355284ce1ab"
PAGE_SHA = "7c084694f5cf69016e9931185d96e0918461027deac77165a2784bc4ed3676c6"
ZERO = (0,) * 10
SECOND = (0, 0, 1, 1, 2, 2, 3, 3, 4, 4)


class CheckError(Exception):
    def __init__(self, reason, detail=""):
        self.reason = reason
        super().__init__(reason + (": " + str(detail) if detail else ""))


def require(condition, reason, detail=""):
    if not condition:
        raise CheckError(reason, detail)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def pair_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate_json_key", key)
        result[key] = value
    return result


def invalid_constant(value):
    raise CheckError("invalid_json_constant", value)


def strict_json(text):
    try:
        return json.loads(text, object_pairs_hook=pair_object, parse_constant=invalid_constant)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise CheckError("invalid_json", str(exc)) from exc


def clock():
    return subprocess.check_output(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], text=True).strip()


def read_pinned_inputs():
    raw_manifest = MANIFEST.read_bytes()
    require(sha(raw_manifest) == MANIFEST_SHA, "manifest_sha")
    manifest = strict_json(raw_manifest.decode("utf-8"))
    require(manifest["id"] == "f142-rqls10-all-odd-fourier-product-obstruction", "manifest_id")
    entries = manifest["inputs_in_read_order"]
    require(type(entries) is list and len(entries) == 5, "manifest_input_count")
    texts, fingerprints = [], []
    for item in entries:
        raw = Path(item["path"]).read_bytes()
        actual = {"sha256": sha(raw), "bytes": len(raw), "LF": raw.count(b"\n")}
        require(actual == {key: item[key] for key in ("sha256", "bytes", "LF")}, "input_fingerprint", item["path"])
        texts.append(raw.decode("utf-8"))
        fingerprints.append({"path": item["path"], "role": item["role"], **actual})
    return texts, fingerprints


def next_permutation(values):
    """Advance a list in strict lexicographic multiset order; False after last."""
    i = len(values) - 2
    while i >= 0 and values[i] >= values[i + 1]:
        i -= 1
    if i < 0:
        return False
    j = len(values) - 1
    while values[j] <= values[i]:
        j -= 1
    values[i], values[j] = values[j], values[i]
    left, right = i + 1, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
    return True


def balanced_pair(a, b):
    counts = [0] * 5
    for x, y in zip(a, b):
        counts[(x - y) % 5] += 1
    return counts == [2, 2, 2, 2, 2]


def build_rows():
    tail = [0, 1, 1, 2, 2, 3, 3, 4, 4]
    rows = []
    previous = None
    count = 0
    while True:
        row = (0,) + tuple(tail)
        require(previous is None or previous < row, "generator_not_strictly_sorted")
        require(balanced_pair(row, ZERO), "generator_not_balanced")
        if balanced_pair(row, SECOND):
            rows.append(row)
        previous = row
        count += 1
        if not next_permutation(tail):
            break
    require(count == 22680, "tail_count", count)
    require(len(rows) == 1075, "candidate_count", len(rows))
    return rows, count


def build_graph(rows):
    adjacency = [0] * len(rows)
    edges = 0
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            if balanced_pair(rows[i], rows[j]):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
                edges += 1
    require(edges == 26715, "compatibility_edges", edges)
    return adjacency, edges


def vertices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def enumerate_triangles(adjacency):
    all_count = 0
    eligible = set()
    for a in range(len(adjacency)):
        later_a = adjacency[a] & ~((1 << (a + 1)) - 1)
        for b in vertices(later_a):
            later_common = adjacency[a] & adjacency[b] & ~((1 << (b + 1)) - 1)
            for c in vertices(later_common):
                all_count += 1
                if (adjacency[a] & adjacency[b] & adjacency[c]).bit_count() >= 5:
                    eligible.add((a, b, c))
    require(all_count == 53065, "triangle_count", all_count)
    require(len(eligible) == 16064, "eligible_count", len(eligible))
    return all_count, eligible


def bind_certificate(cert, eligible, nrows):
    require(type(cert) is dict, "certificate_type")
    require(set(cert) == {"row_order", "candidate_count", "triples_examined", "certificates", "scope"}, "certificate_keys")
    require(cert["row_order"] == "lexicographic deduplicated dephased rows", "row_order")
    require(type(cert["candidate_count"]) is int and cert["candidate_count"] == nrows, "certificate_candidate_count")
    require(type(cert["triples_examined"]) is int and cert["triples_examined"] == 53065, "certificate_triangle_count")
    require(cert["scope"] == "eligible half-frames only, not a formal proof of full QLS impossibility", "certificate_scope")
    records = cert["certificates"]
    require(type(records) is list, "records_type")
    seen = {}
    for rec in records:
        require(type(rec) is dict, "record_type")
        require(set(rec) in ({"triple", "isolated"}, {"triple", "odd_component"}), "record_keys")
        triple = rec["triple"]
        require(type(triple) is list and len(triple) == 3 and all(type(x) is int and 0 <= x < nrows for x in triple)
                and triple[0] < triple[1] < triple[2], "triple_format", triple)
        key = tuple(triple)
        require(key not in seen, "duplicate_triple", key)
        require(key in eligible, "unexpected_triple", key)
        seen[key] = rec
    missing = eligible.difference(seen)
    require(not missing, "missing_triangles", len(missing))
    require(len(records) == len(eligible) and set(seen) == eligible, "coverage_mismatch")
    return seen


def half_graph(frame):
    require(len(frame) == 5 and all(len(row) == 10 for row in frame), "half_frame_shape")
    adjacency = [0] * 10
    for c in range(10):
        for d in range(c + 1, 10):
            if len({(row[c] - row[d]) % 5 for row in frame}) == 5:
                adjacency[c] |= 1 << d
                adjacency[d] |= 1 << c
    return adjacency


def verify_witness(record, adjacency):
    if "isolated" in record:
        vertex = record["isolated"]
        require(type(vertex) is int and 0 <= vertex < 10, "isolate_format")
        require(adjacency[vertex] == 0, "isolate_not_isolated", vertex)
        return "isolated"
    subset = record["odd_component"]
    require(type(subset) is list and all(type(v) is int and 0 <= v < 10 for v in subset)
            and len(set(subset)) == len(subset), "odd_cut_format")
    require(0 < len(subset) < 10 and len(subset) % 2 == 1, "odd_cut_parity")
    subset_mask = sum(1 << v for v in subset)
    outside = ((1 << 10) - 1) ^ subset_mask
    require(all(adjacency[v] & outside == 0 for v in subset), "odd_cut_crosses")
    return "odd_component"


def exact_matching(adjacency):
    """Return a full matching, or None, by an independent 10-bit subset recurrence."""
    @lru_cache(maxsize=None)
    def solve(mask):
        if mask == 0:
            return ()
        first_bit = mask & -mask
        first = first_bit.bit_length() - 1
        candidates = adjacency[first] & (mask ^ first_bit)
        for second in vertices(candidates):
            rest = solve(mask ^ first_bit ^ (1 << second))
            if rest is not None:
                return ((first, second),) + rest
        return None
    return solve((1 << 10) - 1)


def check_record_graphs(seen, rows):
    witness_counts = Counter()
    isolate_counts = Counter()
    cut_sizes = Counter()
    for triple, record in seen.items():
        frame = [ZERO, SECOND] + [rows[i] for i in triple]
        graph = half_graph(frame)
        witness_counts[verify_witness(record, graph)] += 1
        isolate_counts[sum(mask == 0 for mask in graph)] += 1
        if "odd_component" in record:
            cut_sizes[len(record["odd_component"])] += 1
        require(exact_matching(graph) is None, "matching_found_in_eligible_graph", triple)
    require(dict(witness_counts) == {"isolated": 16000, "odd_component": 64}, "witness_histogram", witness_counts)
    require(dict(isolate_counts) == {1: 12800, 2: 3200, 0: 64}, "isolate_histogram", isolate_counts)
    require(dict(cut_sizes) == {5: 64}, "cut_size_histogram", cut_sizes)
    return witness_counts, isolate_counts, cut_sizes


def expect_rejection(name, expected, action, mutations, input_value):
    try:
        action()
    except CheckError as exc:
        require(exc.reason == expected, "wrong_control_rejection", {"control": name, "wanted": expected, "actual": exc.reason})
        mutations[name] = {"result": "REJECTED", "intended_reason": expected,
                           "actual_reason": exc.reason, "input_sha256": sha(json_bytes(input_value))}
    else:
        raise CheckError("control_not_rejected", name)


def controls(cert, eligible, rows, adjacency, seen):
    out = {}
    records = cert["certificates"]
    missing = {**cert, "certificates": records[:-1]}
    expect_rejection("removed_record", "missing_triangles", lambda: bind_certificate(missing, eligible, len(rows)), out, missing)
    duplicate = {**cert, "certificates": records + [records[0]]}
    expect_rejection("duplicated_record", "duplicate_triple", lambda: bind_certificate(duplicate, eligible, len(rows)), out, duplicate)
    badkey = {**cert, "certificates": [{**records[0], "unexpected": 0}] + records[1:]}
    expect_rejection("unexpected_record_field", "record_keys", lambda: bind_certificate(badkey, eligible, len(rows)), out, badkey)
    badtriple = {**cert, "certificates": [{**records[0], "triple": [False, 1, 2]}] + records[1:]}
    expect_rejection("boolean_index", "triple_format", lambda: bind_certificate(badtriple, eligible, len(rows)), out, badtriple)
    expect_rejection("duplicate_json_key", "duplicate_json_key", lambda: strict_json('{"x":1,"x":2}'), out, '{"x":1,"x":2}')
    isolated = next(rec for rec in records if "isolated" in rec)
    tri = isolated["triple"]
    graph = half_graph([ZERO, SECOND] + [rows[i] for i in tri])
    not_isolated = next(v for v in range(10) if graph[v])
    badiso = {**isolated, "isolated": not_isolated}
    expect_rejection("wrong_isolated_witness", "isolate_not_isolated", lambda: verify_witness(badiso, graph), out, badiso)
    cut = next(rec for rec in records if "odd_component" in rec)
    graph_cut = half_graph([ZERO, SECOND] + [rows[i] for i in cut["triple"]])
    old = set(cut["odd_component"])
    replacement = None
    for v in sorted(old):
        for w in sorted(set(range(10)) - old):
            trial = sorted((old - {v}) | {w})
            mask = sum(1 << x for x in trial)
            if any(graph_cut[x] & (((1 << 10) - 1) ^ mask) for x in trial):
                replacement = trial
                break
        if replacement is not None:
            break
    require(replacement is not None, "cannot_construct_wrong_cut_control")
    badcut = {**cut, "odd_component": replacement}
    expect_rejection("wrong_crossing_odd_cut", "odd_cut_crosses", lambda: verify_witness(badcut, graph_cut), out, badcut)
    evencut = {**cut, "odd_component": cut["odd_component"][:-1]}
    expect_rejection("even_cut", "odd_cut_parity", lambda: verify_witness(evencut, graph_cut), out, evencut)
    return out


def positive_half_control(rows, adjacency):
    strings = ["0000000000", "0121230434", "0242410313", "0313140242", "0434320121"]
    frame = [tuple(int(x) for x in line) for line in strings]
    require(all(balanced_pair(frame[i], frame[j]) for i in range(5) for j in range(i + 1, 5)), "positive_half_not_orthogonal")
    graph = half_graph(frame)
    matching = exact_matching(graph)
    require(matching is not None and len(matching) == 5, "positive_matching_missing")
    require(len({v for pair in matching for v in pair}) == 10 and all(graph[a] & (1 << b) for a, b in matching), "positive_matching_invalid")
    order = [0] + sorted(range(1, 10), key=lambda c: (frame[1][c], c))
    normalized = [tuple(row[c] for c in order) for row in frame]
    require(normalized[0] == ZERO and normalized[1] == SECOND, "positive_normalization")
    indexes = {row: i for i, row in enumerate(rows)}
    triple = tuple(sorted(indexes[row] for row in normalized[2:]))
    require(all(adjacency[a] & (1 << b) for a, b in itertools.combinations(triple, 2)), "positive_not_triangle")
    common = (adjacency[triple[0]] & adjacency[triple[1]] & adjacency[triple[2]]).bit_count()
    require(common == 0, "positive_common_neighbors", common)
    signatures = Counter(tuple(row[c] for row in frame) for c in range(10))
    require(sorted(signatures.values()) == [2] * 5, "positive_signature_counts")
    return {"rows": strings, "all_10_row_pairs_orthogonal": True,
            "matching": matching, "normalized_triple": triple, "common_neighbors": common,
            "signature_multiplicities": sorted(signatures.values()), "result": "PASS"}


def normalization_controls(prior_receipt, rows, graph, eligible):
    strings = prior_receipt["sample_bh_control"]["exponent_rows"]
    require(type(strings) is list and len(strings) == 10 and all(type(s) is str and len(s) == 10 and set(s) <= set("01234") for s in strings), "sample_shape")
    sample = [tuple(int(x) for x in s) for s in strings]
    require(all(balanced_pair(sample[i], sample[j]) for i, j in itertools.combinations(range(10), 2)), "sample_rows_not_hadamard")
    cols = [tuple(sample[r][c] for r in range(10)) for c in range(10)]
    require(all(balanced_pair(cols[i], cols[j]) for i, j in itertools.combinations(range(10), 2)), "sample_columns_not_hadamard")
    index = {row: i for i, row in enumerate(rows)}
    gauge = [[(sample[r][c] + 2 * r + 3 * c) % 5 for c in range(10)] for r in range(10)]
    count, physical_count = 0, 0
    sign_control = None
    for half in itertools.combinations(range(10), 5):
        outside = [r for r in range(10) if r not in half]
        original_graph = half_graph([sample[r] for r in half])
        for c, d in itertools.combinations(range(10), 2):
            ce = [0] * 5
            co = [0] * 5
            for r in half:
                ce[(sample[r][c] - sample[r][d]) % 5] += 1
            for r in outside:
                co[(sample[r][c] - sample[r][d]) % 5] += 1
            plus = [ce[k] + co[k] for k in range(5)]
            minus = [ce[k] - co[k] for k in range(5)]
            require(len(set(plus)) == 1, "sample_column_sum_not_zero")
            minus_zero = len(set(minus)) == 1
            edge = bool(original_graph[c] & (1 << d))
            require(minus_zero == edge, "opposite_row_sign_control")
            if not minus_zero and sign_control is None:
                sign_control = {"half": half, "columns": [c, d], "plus_counts": plus,
                                "minus_counts": minus, "plus_zero": True, "minus_zero": False}
            physical_count += 1
        for p in half:
            for q in half:
                if q == p:
                    continue
                for pivot in range(10):
                    raw = [[(sample[r][c] - sample[r][pivot] - sample[p][c] + sample[p][pivot]) % 5
                            for c in range(10)] for r in range(10)]
                    gauged_raw = [[(gauge[r][c] - gauge[r][pivot] - gauge[p][c] + gauge[p][pivot]) % 5
                                   for c in range(10)] for r in range(10)]
                    require(raw == gauged_raw, "sample_gauge_normalization")
                    order = [pivot] + sorted((c for c in range(10) if c != pivot), key=lambda c: (raw[q][c], c))
                    norm = [tuple(raw[r][c] for c in order) for r in range(10)]
                    require(norm[p] == ZERO and norm[q] == SECOND and all(row[0] == 0 for row in norm), "sample_dephasing")
                    inner = [r for r in half if r not in (p, q)]
                    try:
                        triple = tuple(sorted(index[norm[r]] for r in inner))
                        external = [index[norm[r]] for r in outside]
                    except KeyError as exc:
                        raise CheckError("sample_row_not_candidate") from exc
                    require(len(set(triple + tuple(external))) == 8, "sample_distinct_rows")
                    require(triple in eligible, "sample_triangle_not_eligible", triple)
                    common = graph[triple[0]] & graph[triple[1]] & graph[triple[2]]
                    require(all(common & (1 << i) for i in external), "sample_outside_not_common_neighbors")
                    transformed = half_graph([norm[r] for r in half])
                    for c, d in itertools.combinations(range(10), 2):
                        require(bool(transformed[c] & (1 << d)) == bool(original_graph[order[c]] & (1 << order[d])), "sample_half_graph_not_invariant")
                    count += 1
    require(count == 50400 and physical_count == 11340 and sign_control is not None, "normalization_control_count", (count, physical_count))
    return {"source": "frozen prior-review receipt sample data only; no prior-review code",
            "rows": strings, "row_pairs": 45, "column_pairs": 45, "halves": 252,
            "ordered_first_second_pivot_normalizations": count, "deterministic_gauge_normalizations": count,
            "half_column_pair_opposite_sign_checks": physical_count, "sign_negative_control": sign_control,
            "result": "PASS"}


def main():
    require(not RECEIPT.exists(), "receipt_already_exists")
    start_clock = clock()
    start = time.monotonic()
    texts, fingerprints = read_pinned_inputs()
    certificate = strict_json(texts[2])
    prior_receipt = strict_json(texts[4])
    require(sha((HERE / "finite-lam-leung-math9511209v1.pdf").read_bytes()) == PDF_SHA, "source_pdf_sha")
    require(sha((HERE / "finite-lam-leung-page1.png").read_bytes()) == PAGE_SHA, "source_page_sha")
    rows, tails = build_rows()
    adjacency, edges = build_graph(rows)
    triangle_count, eligible = enumerate_triangles(adjacency)
    seen = bind_certificate(certificate, eligible, len(rows))
    witnesses, isolates, cut_sizes = check_record_graphs(seen, rows)
    mutations = controls(certificate, eligible, rows, adjacency, seen)
    positive = positive_half_control(rows, adjacency)
    normalization = normalization_controls(prior_receipt, rows, adjacency, eligible)
    receipt = {
        "kind": "INDEPENDENT_F142_BH10_5_FINITE_REPLAY",
        "status": "ALL_CHECKS_PASSED_BEFORE_RECEIPT_WRITE",
        "observed_start_native_clock": start_clock,
        "observed_native_clock_immediately_before_receipt_write": clock(),
        "elapsed_monotonic_seconds_before_receipt_write": round(time.monotonic() - start, 3),
        "python": sys.version,
        "executable": sys.executable,
        "platform": platform.platform(),
        "checker": {"path": str(Path(__file__).resolve()), "sha256": sha(Path(__file__).read_bytes())},
        "manifest": {"path": str(MANIFEST), "sha256": MANIFEST_SHA},
        "pinned_inputs_in_read_order": fingerprints,
        "source_pdf": {"url": "https://arxiv.org/pdf/math/9511209v1", "sha256": PDF_SHA, "bytes": 201910,
                       "first_page_render_sha256": PAGE_SHA, "use": "identity inspection only; not imported by finite q=5 proof"},
        "finite": {"balanced_tails": tails, "candidate_rows": len(rows), "compatibility_edges": edges,
                   "triangles": triangle_count, "eligible_triangles": len(eligible), "certificate_records": len(seen),
                   "eligible_equals_certificate_set_exactly_once": True,
                   "independent_matching_dp_no_matching": len(seen),
                   "witness_counts": dict(witnesses), "isolate_histogram": dict(isolates), "odd_cut_sizes": dict(cut_sizes),
                   "candidate_rows_canonical_json_sha256": sha(json_bytes(rows)),
                   "eligible_triples_sorted_canonical_json_sha256": sha(json_bytes(sorted(eligible)))},
        "mutation_controls": mutations, "matching_positive_control": positive, "sample_normalizations": normalization,
        "limitations": ["Finite graph check is not the physical normalization and inclusion proof.",
                        "Full BH sample and gauges are controls only, not a universal enumeration of BH matrices.",
                        "No author or prior-review code imported, read or executed; prior written review and receipt were declared inputs.",
                        "Same harness, not human, independent-model-family, formal kernel, odd-q theorem, global QLS10 or novelty review."]
    }
    serialized = (json.dumps(receipt, sort_keys=True, indent=2) + "\n").encode("utf-8")
    with RECEIPT.open("xb") as stream:
        stream.write(serialized)
    print("PASS finite replay, all witnesses, independent matchings, controls and sample normalization")
    print("receipt_sha256", sha(serialized))
    print("elapsed_seconds", receipt["elapsed_monotonic_seconds_before_receipt_write"])


if __name__ == "__main__":
    try:
        main()
    except CheckError as exc:
        print("FAIL", str(exc), file=sys.stderr)
        sys.exit(1)
