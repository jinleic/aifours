#!/usr/bin/env python3
"""UNRUN companion: all local t26 q5 versus q3/q4 weighted pair graphs.

The companion is self-contained and does not import the other new verifier.
No files, subprocesses, network, third-party packages, or floating tolerances.
A parent full-source review and separate one-shot GO are required to execute it.
"""

import itertools
import json
import signal
import sys
import time
from collections import Counter

LIMIT_SECONDS = 39.0
START = None
STOP_SIGNAL = None
STAGE = "initialization"
PROGRESS = {}


class Violation(Exception):
    pass


class Incomplete(Exception):
    pass


def demand(condition, reason):
    if not condition:
        raise Violation(reason)


def emit(record):
    print(json.dumps(record, sort_keys=True, separators=(",", ":")), flush=True)


def request_stop(signum, _frame):
    global STOP_SIGNAL
    STOP_SIGNAL = signum


def guard():
    if STOP_SIGNAL is not None:
        raise Incomplete("SIGNAL_" + str(STOP_SIGNAL))
    if time.monotonic() - START >= LIMIT_SECONDS:
        raise Incomplete("INTERNAL_DEADLINE")


def expect(reason, fn, *args):
    try:
        fn(*args)
    except Violation as error:
        demand(str(error) == reason, "CONTROL_WRONG_REASON:" + reason + ":" + str(error))
        return
    raise Violation("CONTROL_DID_NOT_REJECT:" + reason)


def validate(graph, weights, q, row_h):
    """Check one labeled 5-by-q E pair graph and its E-line surpluses.

    q5 rows all have degree 2; its two possible h partitions are fixed up to
    row relabeling. The opposite q3/q4 vertices have degree >=2 and total 10.
    The t26 per-pair component lemma is used only as a conditional filter.
    """
    demand(q in (3, 4) and len(graph) == 5 and len(weights) == 5
           and all(len(row) == q for row in weights), "PAIR_SHAPE")
    demand(all(len(row) == 2 and tuple(sorted(set(row))) == row
               and all(0 <= c < q for c in row) for row in graph), "Q5_ROW_DEGREE")
    partner_d = tuple(sum(c in row for row in graph) for c in range(q))
    demand(all(d >= 2 for d in partner_d), "PARTNER_MIN_DEGREE")
    for i in range(5):
        for c in range(q):
            demand(weights[i][c] in (0, 1, 2), "WEIGHT_RANGE")
            demand(not weights[i][c] or c in graph[i], "WEIGHT_ON_NONEDGE")
    demand(tuple(sum(row) for row in weights) == tuple(row_h), "Q5_ROW_SURPLUS")
    edge_weights = [weights[i][c] for i in range(5) for c in graph[i]]
    counts = Counter(edge_weights)
    demand((counts[1] == 4 and counts[2] == 0)
           or (counts[1] == 0 and counts[2] == 2), "T26_PAIR_SPECTRUM")
    partner_h = tuple(sum(weights[i][c] for i in range(5)) for c in range(q))
    demand(sum(partner_h) == 4, "PARTNER_SURPLUS_TOTAL")
    demand(all(not (d == 2 and h == 1) for d, h in zip(partner_d, partner_h)),
           "PARTNER_H1_DEGREE2")
    return partner_d, partner_h


def targeted_controls():
    graph = ((0, 1), (0, 1), (0, 2), (1, 2), (1, 2))
    row_h = (4, 0, 0, 0, 0)
    weights = ((2, 2, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    validate(graph, weights, 3, row_h)
    bad_nonedge = ((2, 0, 2),) + weights[1:]
    expect("WEIGHT_ON_NONEDGE", validate, graph, bad_nonedge, 3, row_h)
    expect("Q5_ROW_SURPLUS", validate, graph, ((0, 0, 0),) * 5, 3, row_h)
    graph4 = ((0, 1), (2, 3), (2, 3), (0, 2), (1, 3))
    h22 = (2, 2, 0, 0, 0)
    mixed = ((2, 0, 0, 0), (0, 0, 1, 1), (0, 0, 0, 0),
             (0, 0, 0, 0), (0, 0, 0, 0))
    expect("T26_PAIR_SPECTRUM", validate, graph4, mixed, 4, h22)
    h1_degree2 = ((1, 1, 0, 0), (0, 0, 1, 1), (0, 0, 0, 0),
                  (0, 0, 0, 0), (0, 0, 0, 0))
    expect("PARTNER_H1_DEGREE2", validate, graph4, h1_degree2, 4, h22)
    emit({"status": "COMPLETE_STAGE", "stage": "reason_controls",
          "positive": "q5_q3_two_surplus_two_lines",
          "targeted_reasons": ["WEIGHT_ON_NONEDGE", "Q5_ROW_SURPLUS",
                               "T26_PAIR_SPECTRUM", "PARTNER_H1_DEGREE2"]})


def row_weight_choices(h):
    if h == 0:
        return ((0, 0),)
    if h == 2:
        return ((2, 0), (0, 2), (1, 1))
    if h == 4:
        return ((2, 2),)
    raise Violation("UNEXPECTED_Q5_SURPLUS")


def enumerate_q(q):
    global STAGE, PROGRESS
    guard()
    STAGE = "q5_vs_q" + str(q)
    PROGRESS = {"row_graph_tuples": 0}
    emit({"status": "STARTED", "stage": STAGE})
    profiles = {"4": (4, 0, 0, 0, 0), "22": (2, 2, 0, 0, 0)}
    pairs = tuple(itertools.combinations(range(q), 2))
    statistics = {key: Counter() for key in profiles}
    partner_types = {key: Counter() for key in profiles}
    graphs = 0
    for number, graph in enumerate(itertools.product(pairs, repeat=5), 1):
        if number % 64 == 0:
            PROGRESS["row_graph_tuples"] = number
            guard()
            if number % 2048 == 0:
                emit({"status": "PARTIAL", "stage": STAGE, "progress": dict(PROGRESS)})
        d = tuple(sum(c in row for row in graph) for c in range(q))
        if any(value < 2 for value in d):
            continue
        graphs += 1
        for name, row_h in profiles.items():
            for choices in itertools.product(*(row_weight_choices(h) for h in row_h)):
                statistics[name]["raw_weighted_graphs"] += 1
                weights = [[0] * q for _ in range(5)]
                for i in range(5):
                    for column, weight in zip(graph[i], choices[i]):
                        weights[i][column] = weight
                weights = tuple(tuple(row) for row in weights)
                try:
                    partner_d, partner_h = validate(graph, weights, q, row_h)
                except Violation as error:
                    demand(str(error) in ("T26_PAIR_SPECTRUM", "PARTNER_H1_DEGREE2"),
                           "ENUMERATION_UNEXPECTED_REASON:" + str(error))
                    statistics[name]["rejected_" + str(error)] += 1
                    continue
                statistics[name]["accepted_local_necessary"] += 1
                # Sort paired (degree, surplus), not the two profiles separately.
                descriptor = tuple(sorted(zip(partner_d, partner_h)))
                partner_types[name][str(descriptor)] += 1
    demand(graphs > 0, "NO_PAIR_GRAPHS")
    demand(all(statistics[key]["accepted_local_necessary"] > 0 for key in profiles),
           "MISSING_Q5_SURPLUS_CLASS")
    guard()
    emit({"status": "COMPLETE_STAGE", "stage": STAGE,
          "row_graph_tuples": len(pairs) ** 5, "degree_eligible_graphs": graphs,
          "q5_surplus_cases": {name: {"counts": dict(sorted(statistics[name].items())),
                                        "partner_degree_surplus_types": dict(sorted(partner_types[name].items())),
                                        "labeled_row_profile_factor": 5 if name == "4" else 10}
                                for name in profiles},
          "scope": "local pair graphs only; no common four-party extension asserted"})


def main():
    global START, STAGE
    START = time.monotonic()
    try:
        signal.signal(signal.SIGTERM, request_stop)
        signal.signal(signal.SIGINT, request_stop)
        emit({"status": "STARTED", "stage": "run", "internal_limit_seconds": LIMIT_SECONDS,
              "scope": "conditional t26 q5 versus q3/q4 local pair necessities"})
        STAGE = "reason_controls"
        targeted_controls()
        enumerate_q(3)
        enumerate_q(4)
        guard()
        emit({"status": "COMPLETE_LOCAL_Q5_Q3_Q4", "elapsed_seconds": time.monotonic() - START,
              "not_claimed": "global P/E or AME realizability"})
        return 0
    except Incomplete as error:
        emit({"status": "INCOMPLETE", "reason": str(error), "stage": STAGE,
              "progress": dict(PROGRESS), "elapsed_seconds": time.monotonic() - START})
        return 2
    except Violation as error:
        emit({"status": "FAILED", "reason": str(error), "stage": STAGE,
              "progress": dict(PROGRESS), "elapsed_seconds": time.monotonic() - START})
        return 1
    except BaseException as error:
        emit({"status": "FAILED_EXCEPTION", "type": type(error).__name__, "reason": str(error),
              "stage": STAGE, "progress": dict(PROGRESS), "elapsed_seconds": time.monotonic() - START})
        return 1


if __name__ == "__main__":
    sys.exit(main())
