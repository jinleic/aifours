#!/usr/bin/env python3
"""UNRUN prospective finite mask enumerator; parent audit and separate GO required.

The output is an exclusively-created JSONL file.  A mask record is
["M", order, row_hex, twin_necessary]; each two hexadecimal digits give one
labeled row's column-bit mask, least-significant bit = column 0.  Every
labeled row ordering is emitted separately.  Per-order digests hash the
exact UTF-8 mask-record lines, including LF, in their emitted order.  The
separate twin digest includes only those mask lines with twin_necessary true.
A terminal SUMMARY is complete only if all orders finish, controls succeed,
and the order-four analytical cross-check succeeds.  Any bound or signal
produces INCOMPLETE and prefix counts/digests only.  This is a support
necessity enumeration, not a phase-realizability or AME-witness test.
"""

import argparse
import hashlib
import json
import math
import signal
import sys
import time


ORDERS = (4, 6, 8)
EXCESS = 6
MAX_SECONDS = 38.0
MAX_NODES = 4_000_000
MAX_OUTPUT_BYTES = 64 * 1024 * 1024
SUMMARY_RESERVE = 32 * 1024


class StopEnumeration(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


class ControlFailure(Exception):
    pass


class Budget:
    def __init__(self, started, seconds, node_cap):
        self.started = started
        self.deadline = started + seconds
        self.node_cap = node_cap
        self.nodes = 0
        self.signal_number = None

    def signal_handler(self, signum, _frame):
        self.signal_number = signum

    def check(self):
        if self.signal_number is not None:
            raise StopEnumeration("SIGNAL_" + str(self.signal_number))
        if time.monotonic() >= self.deadline:
            raise StopEnumeration("DEADLINE")

    def visit(self):
        self.check()
        if self.nodes >= self.node_cap:
            raise StopEnumeration("NODE_CAP")
        self.nodes += 1


def transpose_rows(n, rows):
    return tuple(
        sum(1 << i for i, row in enumerate(rows) if row & (1 << j))
        for j in range(n)
    )


def connected(n, rows):
    seen_rows = 1
    seen_cols = 0
    while True:
        old_rows, old_cols = seen_rows, seen_cols
        for i, row in enumerate(rows):
            if seen_rows & (1 << i):
                seen_cols |= row
        for i, row in enumerate(rows):
            if row & seen_cols:
                seen_rows |= 1 << i
        if seen_rows == old_rows and seen_cols == old_cols:
            break
    full = (1 << n) - 1
    return seen_rows == full and seen_cols == full


def graph_reason(n, rows, excess):
    """Return one exact graph rejection reason, or None on acceptance."""
    if n not in ORDERS:
        return "ORDER"
    if (len(rows) != n or
            any(type(r) is not int or r < 0 or r >= (1 << n) for r in rows)):
        return "SHAPE"
    if any(r.bit_count() < 2 for r in rows):
        return "ROW_DEGREE"
    cols = transpose_rows(n, rows)
    if any(c.bit_count() < 2 for c in cols):
        return "COLUMN_DEGREE"
    if sum(r.bit_count() for r in rows) != 2 * n + excess:
        return "EXCESS"
    for i in range(n):
        for j in range(i):
            if (rows[i] & rows[j]).bit_count() == 1:
                return "ROW_SINGLETON"
    for i in range(n):
        for j in range(i):
            if (cols[i] & cols[j]).bit_count() == 1:
                return "COLUMN_SINGLETON"
    if not connected(n, rows):
        return "DISCONNECTED"
    return None


def twin_necessary_reason(n, rows):
    """Genuine-unitary twin/isolation necessity, separate from graph tests.

    Intended only after graph_reason accepts a connected order-greater-than-2
    mask. Direct helper-only controls also exercise the degree guard on
    deliberately graph-invalid inputs. None means necessary, not sufficient.
    """
    cols = transpose_rows(n, rows)
    for side, lines, opposite in (("ROW", rows, cols),
                                  ("COLUMN", cols, rows)):
        previous = 0
        for line in lines:
            if line.bit_count() != 2:
                continue
            for j in range(n):
                if line & (1 << j) and opposite[j].bit_count() < 3:
                    return "TWIN_" + side + "_DEGREE"
            if previous & line:
                return "TWIN_" + side + "_OVERLAP"
            previous |= line
    return None


def build_model(n, budget):
    """All row subsets, plus exact compatibility and column signatures."""
    options = tuple(r for r in range(1 << n) if r.bit_count() >= 2)
    count = len(options)
    all_bits = (1 << count) - 1
    by_weight = [0] * (n + 1)
    by_column = [0] * n
    index = {}
    for i, row in enumerate(options):
        index[row] = i
        bit = 1 << i
        by_weight[row.bit_count()] |= bit
        for c in range(n):
            if row & (1 << c):
                by_column[c] |= bit
    compatible = []
    suffix = []
    for i, row in enumerate(options):
        budget.check()
        allowed = 0
        for j, other in enumerate(options):
            if (row & other).bit_count() != 1:
                allowed |= 1 << j
        compatible.append(allowed)
        suffix.append(all_bits ^ ((1 << i) - 1))
    return {
        "options": options,
        "all": all_bits,
        "by_weight": by_weight,
        "by_column": by_column,
        "index": index,
        "compatible": compatible,
        "suffix": suffix,
    }


def signature(n, rows):
    return transpose_rows(n, rows)


def prefix_reason(n, rows, sig, available, target, model):
    """Necessary future feasibility only; no unitary-twin pruning here."""
    remaining = n - len(rows)
    if remaining == 0:
        return None
    if not available:
        return "NO_COMPATIBLE_ROW"
    needed = target - sum(row.bit_count() for row in rows)
    deficits = sum(max(0, 2 - col.bit_count()) for col in sig)
    if needed < deficits:
        return "COLUMN_DEGREE_DEFICIT"
    weights = [w for w in range(2, n + 1)
               if available & model["by_weight"][w]]
    if needed < remaining * weights[0] or needed > remaining * weights[-1]:
        return "EDGE_BOUND"
    for c, col in enumerate(sig):
        degree = col.bit_count()
        if degree + remaining < 2:
            return "COLUMN_DEGREE_UNREACHABLE"
        if degree < 2 and not (available & model["by_column"][c]):
            return "COLUMN_DEGREE_UNREACHABLE"
    for a in range(n):
        for b in range(a):
            if ((sig[a] & sig[b]).bit_count() == 1 and
                    not (available & model["by_column"][a] &
                         model["by_column"][b])):
                return "COLUMN_SINGLETON_UNFIXABLE"
    return None


def distinct_permutations(ordered, budget):
    """Yield each distinct permutation of an already sorted sequence once."""
    used = [False] * len(ordered)
    current = []

    def visit():
        budget.check()
        if len(current) == len(ordered):
            yield tuple(current)
            return
        previous = None
        for i, value in enumerate(ordered):
            if used[i] or value == previous:
                continue
            previous = value
            used[i] = True
            current.append(value)
            yield from visit()
            current.pop()
            used[i] = False

    yield from visit()


def controls(budget):
    """Intended-reason controls; a mismatch, including exception, aborts."""
    results = []

    def check(name, expected, fn):
        budget.check()
        try:
            actual = fn()
        except Exception as exc:
            if isinstance(exc, StopEnumeration):
                raise
            actual = "EXCEPTION:" + type(exc).__name__ + ":" + str(exc)
        results.append({"name": name, "expected": expected, "actual": actual})
        if actual != expected:
            raise ControlFailure(name + ": expected " + str(expected) +
                                 ", got " + str(actual))

    check("positive_graph_4_e6", None,
          lambda: graph_reason(4, (3, 15, 15, 15), 6))
    check("positive_twin_necessary_4_e6", None,
          lambda: twin_necessary_reason(4, (3, 15, 15, 15)))
    check("bad_order", "ORDER", lambda: graph_reason(3, (7, 7, 7), 3))
    check("bad_shape_length", "SHAPE", lambda: graph_reason(4, (15, 15, 15), 6))
    check("bad_shape_range", "SHAPE", lambda: graph_reason(4, (16, 15, 15, 15), 6))
    check("bad_row_degree", "ROW_DEGREE",
          lambda: graph_reason(4, (1, 15, 15, 15), 5))
    check("bad_column_degree", "COLUMN_DEGREE",
          lambda: graph_reason(4, (15, 14, 14, 14), 5))
    check("bad_excess", "EXCESS",
          lambda: graph_reason(4, (3, 15, 15, 15), 5))
    check("bad_row_singleton", "ROW_SINGLETON",
          lambda: graph_reason(4, (3, 13, 15, 15), 5))
    check("bad_column_singleton", "COLUMN_SINGLETON",
          lambda: graph_reason(4, (15, 13, 14, 14), 5))
    check("bad_disconnected", "DISCONNECTED",
          lambda: graph_reason(4, (3, 3, 12, 12), 0))

    row_twin = (3, 3, 63, 63, 60, 60)
    col_twin = (15, 15, 60, 60, 60, 60)
    check("row_twin_mutant_graph_accepted", None,
          lambda: graph_reason(6, row_twin, 12))
    check("row_twin_mutant_reason", "TWIN_ROW_OVERLAP",
          lambda: twin_necessary_reason(6, row_twin))
    check("column_twin_mutant_graph_accepted", None,
          lambda: graph_reason(6, col_twin, 12))
    check("column_twin_mutant_reason", "TWIN_COLUMN_OVERLAP",
          lambda: twin_necessary_reason(6, col_twin))
    check("helper_only_row_twin_degree", "TWIN_ROW_DEGREE",
          lambda: twin_necessary_reason(4, (3, 3, 12, 12)))
    check("helper_only_column_twin_degree", "TWIN_COLUMN_DEGREE",
          lambda: twin_necessary_reason(4, (1, 1, 14, 14)))
    check("distinct_multiset_permutations",
          [(1, 1, 2), (1, 2, 1), (2, 1, 1)],
          lambda: list(distinct_permutations((1, 1, 2), budget)))

    model = build_model(4, budget)

    def options_mask(values):
        return sum(1 << model["index"][v] for v in values)

    def prefix(rows, allowed, target):
        return prefix_reason(4, rows, signature(4, rows), allowed, target, model)

    check("prefix_no_compatible_row", "NO_COMPATIBLE_ROW",
          lambda: prefix((), 0, 14))
    check("prefix_column_degree_deficit", "COLUMN_DEGREE_DEFICIT",
          lambda: prefix((), model["all"], 7))
    check("prefix_edge_bound", "EDGE_BOUND",
          lambda: prefix((), options_mask((3,)), 14))
    check("prefix_column_unreachable", "COLUMN_DEGREE_UNREACHABLE",
          lambda: prefix((), options_mask((3,)), 8))
    check("prefix_singleton_unfixable", "COLUMN_SINGLETON_UNFIXABLE",
          lambda: prefix((7,), options_mask((13, 14)), 12))

    def positive_prefix_path():
        rows = []
        available = model["all"]
        for row in (3, 15, 15, 15):
            problem = prefix(tuple(rows), available, 14)
            if problem is not None:
                return problem
            i = model["index"][row]
            if not available & (1 << i):
                return "POSITIVE_NEXT_ROW_MISSING"
            rows.append(row)
            available &= model["compatible"][i] & model["suffix"][i]
        return None

    check("positive_prefix_path", None, positive_prefix_path)
    return results


def main():
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True,
                        help="new JSONL path; existing paths are never overwritten")
    parser.add_argument("--seconds", type=float, default=MAX_SECONDS)
    parser.add_argument("--node-cap", type=int, default=MAX_NODES)
    args = parser.parse_args()
    if not math.isfinite(args.seconds) or not 0 < args.seconds <= MAX_SECONDS:
        parser.error("--seconds must be finite and in (0, 38]")
    if not 1 <= args.node_cap <= MAX_NODES:
        parser.error("--node-cap must be in [1, 4000000]")

    budget = Budget(started, args.seconds, args.node_cap)
    stats = {
        n: {"order": n, "status": "NOT_STARTED", "nodes_at_entry": None,
            "nodes_at_exit": None, "complete_sorted_representatives": 0,
            "labeled_graph": 0, "labeled_twin_necessary": 0,
            "prunes": {}, "leaf_rejections": {}}
        for n in ORDERS
    }
    digests = {n: {"graph": hashlib.sha256(), "twin": hashlib.sha256()}
               for n in ORDERS}
    control_results = []
    stream = None
    written = 0
    handlers = {}
    status = "INCOMPLETE_INITIALIZATION"
    detail = None
    active_order = None
    output_error = None

    def write_record(obj, reserve=True):
        nonlocal written
        line = (json.dumps(obj, separators=(",", ":"), ensure_ascii=True) +
                "\n").encode("ascii")
        if reserve and written + len(line) > MAX_OUTPUT_BYTES - SUMMARY_RESERVE:
            raise StopEnumeration("OUTPUT_CAP")
        stream.write(line)
        written += len(line)
        return line

    def bump(table, reason):
        table[reason] = table.get(reason, 0) + 1

    def emit_label(n, rows, twin):
        budget.check()
        # All allowed column masks fit in exactly one byte at these orders.
        row_hex = "".join(format(row, "02x") for row in rows)
        line = write_record(["M", n, row_hex, twin])
        digests[n]["graph"].update(line)
        stats[n]["labeled_graph"] += 1
        if twin:
            digests[n]["twin"].update(line)
            stats[n]["labeled_twin_necessary"] += 1

    def search(n, model, rows, sig, available):
        budget.visit()
        current = stats[n]
        target = 2 * n + EXCESS
        remaining = n - len(rows)
        if not remaining:
            reason = graph_reason(n, rows, EXCESS)
            if reason is not None:
                bump(current["leaf_rejections"], reason)
                return
            twin = twin_necessary_reason(n, rows) is None
            for labeled_rows in distinct_permutations(rows, budget):
                emit_label(n, labeled_rows, twin)
            current["complete_sorted_representatives"] += 1
            return
        reason = prefix_reason(n, rows, sig, available, target, model)
        if reason is not None:
            bump(current["prunes"], reason)
            return
        used_edges = sum(row.bit_count() for row in rows)
        bits = available
        while bits:
            budget.check()
            bit = bits & -bits
            bits -= bit
            i = bit.bit_length() - 1
            row = model["options"][i]
            future = target - used_edges - row.bit_count()
            if future < 2 * (remaining - 1) or future > n * (remaining - 1):
                bump(current["prunes"], "EDGE_CHILD_BOUND")
                continue
            row_marker = 1 << len(rows)
            next_sig = tuple(col | row_marker if row & (1 << c) else col
                             for c, col in enumerate(sig))
            next_available = (available & model["compatible"][i] &
                              model["suffix"][i])
            search(n, model, rows + (row,), next_sig, next_available)

    try:
        stream = open(args.output, "xb")
        for sig in (signal.SIGINT, signal.SIGTERM):
            handlers[sig] = signal.signal(sig, budget.signal_handler)
        write_record({"kind": "HEADER", "format": "f812-excess6-jsonl-v1",
                      "orders": ORDERS, "excess": EXCESS,
                      "mask_record": ["M", "order", "rows_hex", "twin_necessary"],
                      "row_encoding": "one byte per labeled row; bit j is column j",
                      "digest": "SHA256 of exact selected M lines including LF",
                      "internal_seconds": args.seconds, "node_cap": args.node_cap,
                      "output_cap_bytes": MAX_OUTPUT_BYTES})
        control_results = controls(budget)
        write_record({"kind": "CONTROLS", "checks": control_results})
        for n in ORDERS:
            budget.check()
            active_order = n
            current = stats[n]
            current["status"] = "IN_PROGRESS"
            current["nodes_at_entry"] = budget.nodes
            model = build_model(n, budget)
            search(n, model, (), (0,) * n, model["all"])
            current["nodes_at_exit"] = budget.nodes
            if n == 4 and (current["labeled_graph"] != 120 or
                           current["labeled_twin_necessary"] != 120):
                raise ControlFailure("order-four analytical 120/120 check")
            current["status"] = "COMPLETE"
            active_order = None
        status = "COMPLETE_NECESSARY_SUPPORT_ENUMERATION"
    except FileExistsError:
        status = "REFUSED_OUTPUT_EXISTS"
        detail = "exclusive output already exists; no file was changed"
    except StopEnumeration as exc:
        status = "INCOMPLETE_" + exc.reason
        detail = "counts and hashes cover emitted mask-record prefixes only"
    except ControlFailure as exc:
        status = "CONTROL_FAILED"
        detail = str(exc)
    except Exception as exc:
        status = "ERROR"
        detail = type(exc).__name__ + ": " + str(exc)
    finally:
        if active_order is not None and stats[active_order]["status"] == "IN_PROGRESS":
            stats[active_order]["status"] = "INCOMPLETE"
            stats[active_order]["nodes_at_exit"] = budget.nodes
        if stream is not None:
            for n in ORDERS:
                stats[n]["graph_sha256"] = digests[n]["graph"].hexdigest()
                stats[n]["twin_sha256"] = digests[n]["twin"].hexdigest()
            summary = {"kind": "SUMMARY", "status": status, "detail": detail,
                       "controls_completed": len(control_results),
                       "orders": [stats[n] for n in ORDERS], "nodes": budget.nodes,
                       "node_cap": args.node_cap,
                       "elapsed_before_summary_seconds": time.monotonic() - started,
                       "bytes_before_summary": written,
                       "scope": "necessary graph and twin-isolation filters only; no phase or AME witness"}
            try:
                write_record(summary, reserve=False)
                stream.flush()
            except Exception as exc:
                output_error = type(exc).__name__ + ": " + str(exc)
            try:
                stream.close()
            except Exception as exc:
                output_error = type(exc).__name__ + ": " + str(exc)
        for sig, old in handlers.items():
            signal.signal(sig, old)
    if output_error is not None:
        print("OUTPUT_ERROR: " + output_error, file=sys.stderr)
        return 2
    print(status + (": " + detail if detail else ""), file=sys.stderr)
    return 0 if status == "COMPLETE_NECESSARY_SUPPORT_ENUMERATION" else 2


if __name__ == "__main__":
    sys.exit(main())
