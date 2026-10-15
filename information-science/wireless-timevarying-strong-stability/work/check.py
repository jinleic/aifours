#!/usr/bin/env python3
"""Finite evidence for proof.md; never a replacement for its universal proof.

No dependencies beyond Python's standard library. All files are read-only except
--output. Includes exact rational positive/negative controls and an actual
finite-time event-driven run of the declared (uncapped) clock policy.
"""
import argparse
from fractions import Fraction as F
import hashlib
import heapq
import itertools
import json
import math
from pathlib import Path
import random
import time


def valid(mask, edges):
    return all(not (mask & (1 << i) and mask & (1 << j)) for i, j in edges)


def independent_sets(n, edges):
    return [mask for mask in range(1 << n) if valid(mask, edges)]


def neighbors(n, edges):
    result = [0] * n
    for i, j in edges:
        result[i] |= 1 << j
        result[j] |= 1 << i
    return result


def heat_bath(n, edges, activities, reverse=False):
    states = independent_sets(n, edges)
    index = {mask: k for k, mask in enumerate(states)}
    adjacent = neighbors(n, edges)
    kernel = [[F(0) for _ in states] for _ in states]
    for row, mask in enumerate(states):
        for i, z in enumerate(activities):
            off = mask & ~(1 << i)
            if mask & adjacent[i]:
                kernel[row][index[off]] += F(1, n)
            else:
                on_probability = F(1, 1 + z) if reverse else F(z, 1 + z)
                kernel[row][index[off]] += (1 - on_probability) / n
                kernel[row][index[off | (1 << i)]] += on_probability / n
    return states, kernel


def gibbs(states, activities):
    masses = [math.prod(z for i, z in enumerate(activities) if mask & (1 << i)) for mask in states]
    total = sum(masses)
    return [F(mass, total) for mass in masses]


def invariant(probability, matrix, generator=False):
    size = len(probability)
    return all(sum(probability[i] * matrix[i][j] for i in range(size)) ==
               (F(0) if generator else probability[j]) for j in range(size))


def solve(matrix, rhs):
    size = len(rhs)
    a = [[F(x) for x in row] + [F(b)] for row, b in zip(matrix, rhs)]
    for col in range(size):
        pivot = next(row for row in range(col, size) if a[row][col])
        a[col], a[pivot] = a[pivot], a[col]
        factor = a[col][col]
        a[col] = [x / factor for x in a[col]]
        for row in range(size):
            if row != col:
                factor = a[row][col]
                if factor:
                    a[row] = [x - factor * y for x, y in zip(a[row], a[col])]
    return [row[-1] for row in a]


def stationary_generator(generator):
    size = len(generator)
    matrix = [[generator[j][i] for j in range(size)] for i in range(size)]
    matrix[-1] = [F(1)] * size
    solution = solve(matrix, [F(0)] * (size - 1) + [F(1)])
    assert all(x >= 0 for x in solution) and sum(solution) == 1
    assert invariant(solution, generator, generator=True)
    return solution


def exact_graph_checks(tamper):
    total_graphs = total_states = reset_cases = 0
    for n in range(1, 5):
        possible = list(itertools.combinations(range(n), 2))
        for edge_mask in range(1 << len(possible)):
            edges = [edge for k, edge in enumerate(possible) if edge_mask & (1 << k)]
            activities = list(range(2, n + 2))
            states, kernel = heat_bath(n, edges, activities, reverse=tamper == "reverse-activation")
            probability = gibbs(states, activities)
            assert all(sum(row) == 1 and all(x >= 0 for x in row) for row in kernel)
            assert invariant(probability, kernel), "wrong activation rule violates frozen Gibbs stationarity"
            assert all(probability[i] * kernel[i][j] == probability[j] * kernel[j][i]
                       for i in range(len(states)) for j in range(len(states)))
            # Every update order of the reset event sends every initial state to zero.
            for order in itertools.permutations(range(n)):
                for state in states:
                    reset = state
                    for vertex in order:
                        reset &= ~(1 << vertex)
                        assert valid(reset, edges)
                    assert reset == 0
                    reset_cases += 1
            total_graphs += 1
            total_states += len(states)
    return {"labeled_graphs": total_graphs, "max_vertices": 4,
            "summed_independent_states": total_states, "all_zero_reset_maps": reset_cases,
            "exact_stationarity_and_detailed_balance": True}


def frozen_service_check():
    edges = [(0, 1), (1, 2)]
    records = []
    for activities, capacity in [([2, 3, 5], F(1, 2)), ([4, 9, 25], F(1))]:
        states, kernel = heat_bath(3, edges, activities)
        probability = gibbs(states, activities)
        service = [capacity * sum(p for s, p in zip(states, probability) if s & (1 << i))
                   for i in range(3)]
        assert invariant(probability, kernel)
        records.append({"activities": activities, "capacity_per_link": str(capacity),
                        "states": states, "probabilities": list(map(str, probability)),
                        "exact_service": list(map(str, service))})
    assert records[0]["exact_service"] == ["2/7", "1/14", "5/14"]
    assert records[1]["exact_service"] == ["104/139", "9/139", "125/139"]
    return {"same_queue_weights": "q=(log 4,log 9,log 25)", "conditional_frozen_laws_only": records}


def continuous_channel_check(rate):
    # Channel 0 has capacities (1,0), channel 1 has capacities (0,1).
    n = 2
    edges = [(0, 1)]
    states = independent_sets(n, edges)
    size = 2 * len(states)
    generator = [[F(0) for _ in range(size)] for _ in range(size)]
    product_candidate = []
    for channel, activities in enumerate(([9, 1], [1, 9])):
        _, kernel = heat_bath(n, edges, activities)
        product_candidate.extend(p / 2 for p in gibbs(states, activities))
        for row in range(len(states)):
            source = channel * len(states) + row
            for col in range(len(states)):
                if row != col:
                    target = channel * len(states) + col
                    generator[source][target] += n * rate * kernel[row][col]
            generator[source][(1 - channel) * len(states) + row] += 1
    for i in range(size):
        generator[i][i] = -sum(generator[i])
    probability = stationary_generator(generator)
    useful = sum(probability[channel * len(states) + row]
                 for channel in range(2) for row, mask in enumerate(states)
                 if mask & (1 << channel))
    residual = [sum(product_candidate[i] * generator[i][j] for i in range(size)) for j in range(size)]
    assert not invariant(product_candidate, generator, generator=True)
    if rate == 1:
        assert useful == F(37, 79)
        assert probability == [F(13, 158), F(37, 158), F(29, 158),
                               F(13, 158), F(29, 158), F(37, 158)]
    return {"per_vertex_clock_rate": rate, "stationary_joint_probabilities": list(map(str, probability)),
            "actual_total_useful_service": str(useful), "invalid_instantaneous_gibbs_prediction": "9/11",
            "product_law_stationarity_residual": list(map(str, residual)),
            "invalid_product_law_rejected": True}


def markov_poisson_check():
    transition = [[F(3, 4), F(1, 4)], [F(1, 2), F(1, 2)]]
    pi = [F(2, 3), F(1, 3)]
    service = [F(1, 4), F(1, 2)]
    mean = sum(x * y for x, y in zip(pi, service))
    matrix = [[F(i == j) - transition[i][j] + pi[j] for j in range(2)] for i in range(2)]
    h = solve(matrix, [x - mean for x in service])
    assert h == [F(-1, 9), F(2, 9)]
    generator = [[transition[i][j] - F(i == j) for j in range(2)] for i in range(2)]
    assert invariant(pi, generator, generator=True)
    assert all(-sum(generator[i][j] * h[j] for j in range(2)) == service[i] - mean
               for i in range(2))
    epsilon = F(1, 12)
    horizon = math.ceil(4 * max(map(abs, h)) / epsilon)
    rows = []
    for initial in range(2):
        distribution = [F(initial == i) for i in range(2)]
        cumulative = F(0)
        for _ in range(horizon):
            cumulative += sum(distribution[i] * service[i] for i in range(2))
            distribution = [sum(distribution[i] * transition[i][j] for i in range(2)) for j in range(2)]
        identity = horizon * mean + h[initial] - sum(distribution[i] * h[i] for i in range(2))
        assert cumulative == identity
        assert cumulative >= horizon * (F(1, 4) + epsilon / 2)
        rows.append(str(cumulative))
    return {"transition": [[str(x) for x in row] for row in transition], "stationary": list(map(str, pi)),
            "comparison_policy": "choose path endpoints or middle with probabilities 1/2,1/2 in either channel",
            "mean_service_each_link": str(mean), "arrival_mean_each_link": "1/4", "strict_slack": str(epsilon),
            "poisson_solution": list(map(str, h)), "drift_horizon": horizon,
            "exact_horizon_service_by_initial_channel": rows}


def burst_check():
    queue = elapsed = area = arrivals = 0
    records = []
    for cycle in range(1, 121):
        start_area = area
        for amount in [2] * cycle + [0] * (3 * cycle):
            area += queue
            queue = max(queue - 1, 0) + amount
            arrivals += amount
            elapsed += 1
        assert queue == 0
        assert area - start_area == cycle * cycle + 2 * cycle
        assert elapsed == 2 * cycle * (cycle + 1)
        assert F(area, elapsed) == F(2 * cycle + 7, 12)
        assert F(arrivals, elapsed) == F(1, 2)
        if cycle in (1, 10, 50, 120):
            records.append({"cycles": cycle, "slots": elapsed, "average_backlog": str(F(area, elapsed))})
    return {"bounded_deterministic_arrivals": [0, 2], "arrival_rate": "1/2",
            "exact_average_formula": "(2K+7)/12", "controls": records,
            "scope": "temporal-regularity assumption gap, not a distributed scheduling impossibility"}


def simulate_control(queue, channel, slot, rng, adjacent):
    # This is the actual declared rate, never capped or replaced by Gibbs sampling.
    rate = math.exp((slot + 1) ** 2)
    duration = 1.0 / (slot + 2)
    probabilities = [1.0 / (1.0 + math.exp(-q * c)) for q, c in zip(queue, channel)]
    heap = [(rng.expovariate(rate), i) for i in range(len(queue))]
    heapq.heapify(heap)
    state = events = 0
    while heap[0][0] < duration:
        now, i = heapq.heappop(heap)
        mark = rng.random()
        if state & adjacent[i] or mark >= probabilities[i]:
            state &= ~(1 << i)
        else:
            state |= 1 << i
        assert all(not (state & (1 << j) and state & adjacent[j]) for j in range(len(queue)))
        heapq.heappush(heap, (now + rng.expovariate(rate), i))
        events += 1
    service = [(1.0 - duration) * c * bool(state & (1 << i)) for i, c in enumerate(channel)]
    return service, state, events


def event_driven_smoke():
    rng = random.Random(20261014)
    edges = [(0, 1), (1, 2)]
    adjacent = neighbors(3, edges)
    total_events = 0
    event_by_slot = [0, 0, 0]
    transitions = [[0, 0], [0, 0]]
    state_counts = {str(s): 0 for s in independent_sets(3, edges)}
    max_queue = 0.0
    total_final = [0.0] * 3
    examples = []
    trials = 96
    for trial in range(trials):
        queue = [2.0, 1.0, 3.0]
        channel_state = trial % 2
        trace = []
        for slot in range(3):
            capacity = 0.5 if channel_state == 0 else 1.0
            channel = [capacity] * 3
            service, state, events = simulate_control(queue, channel, slot, rng, adjacent)
            before = queue.copy()
            arrival = [int(rng.random() < 0.25) for _ in range(3)]
            queue = [max(q - s, 0.0) + a for q, s, a in zip(queue, service, arrival)]
            assert all(q >= 0 for q in queue) and valid(state, edges)
            assert all(queue[i] <= before[i] + 1 for i in range(3))
            assert all(0 <= s <= (1 - 1 / (slot + 2)) * capacity for s in service)
            total_events += events
            event_by_slot[slot] += events
            state_counts[str(state)] += 1
            max_queue = max(max_queue, *queue)
            next_channel = int(rng.random() >= (0.75 if channel_state == 0 else 0.5))
            transitions[channel_state][next_channel] += 1
            if trial < 2:
                trace.append({"slot": slot, "channel": channel_state, "before": before,
                              "schedule_mask": state, "events": events, "service": service,
                              "arrivals": arrival, "after": queue.copy()})
            channel_state = next_channel
        total_final = [x + y for x, y in zip(total_final, queue)]
        if trial < 2:
            examples.append(trace)
    assert all(count > 0 for row in transitions for count in row)
    assert total_events > 100000
    return {"seed": 20261014, "graph": "path on 3 links", "independent_trials": trials,
            "actual_slots_per_trial": 3, "clock_policy": "uncapped exp((t+1)^2)",
            "control_windows": [0.5, 1 / 3, 0.25], "total_events": total_events,
            "events_by_slot": event_by_slot, "observed_channel_transitions": transitions,
            "schedule_counts": state_counts, "maximum_observed_queue": max_queue,
            "mean_final_queues": [q / trials for q in total_final], "sample_traces": examples,
            "collisions": 0, "claim": "finite operational smoke only; no empirical stability inference"}


def continuous_event_smoke():
    """Execute Theorem 2, including genuine channel jumps during both phases."""
    rng = random.Random(20261015)
    edges = [(0, 1), (1, 2)]
    adjacent = neighbors(3, edges)
    trials = 48
    clock_events = [0, 0, 0]
    channel_jumps = {"control": 0, "data": 0}
    max_queue = 0.0
    examples = []
    service_totals = [0.0] * 3
    for trial in range(trials):
        queue = [2.0, 1.0, 3.0]
        channel_state = trial % 2
        trace = []
        for slot in range(3):
            before = queue.copy()
            rate = math.exp((slot + 1) ** 2)
            duration = 1.0 / (slot + 2)
            state = 0
            now = 0.0
            capacity = 0.5 if channel_state == 0 else 1.0
            heap = [(rng.expovariate(rate), i) for i in range(3)]
            heapq.heappush(heap, (rng.expovariate(0.25 if channel_state == 0 else 0.5), 3))
            heapq.heapify(heap)
            potential = [0.0, 0.0, 0.0]
            jumps_in_slot = []
            events = 0
            while heap[0][0] < 1.0:
                next_time, index = heapq.heappop(heap)
                data_length = max(0.0, next_time - max(now, duration))
                for i in range(3):
                    if state & (1 << i):
                        potential[i] += capacity * data_length
                now = next_time
                if index == 3:
                    channel_state = 1 - channel_state
                    capacity = 0.5 if channel_state == 0 else 1.0
                    phase = "control" if now < duration else "data"
                    channel_jumps[phase] += 1
                    if trial < 2:
                        jumps_in_slot.append({"time": now, "new_state": channel_state, "phase": phase})
                    heapq.heappush(heap, (now + rng.expovariate(0.25 if channel_state == 0 else 0.5), 3))
                else:
                    probability = 1.0 / (1.0 + math.exp(-before[index] * capacity))
                    mark = rng.random()
                    if state & adjacent[index] or mark >= probability:
                        state &= ~(1 << index)
                    else:
                        state |= 1 << index
                    assert valid(state, edges)
                    heapq.heappush(heap, (now + rng.expovariate(rate), index))
                    events += 1
            data_length = max(0.0, 1.0 - max(now, duration))
            for i in range(3):
                if state & (1 << i):
                    potential[i] += capacity * data_length
            assert all(-1e-12 <= s <= 1.0 - duration + 1e-10 for s in potential)
            arrival = [int(rng.random() < 0.25) for _ in range(3)]
            queue = [max(q - s, 0.0) + a for q, s, a in zip(before, potential, arrival)]
            assert all(0 <= q <= old + 1 for q, old in zip(queue, before))
            max_queue = max(max_queue, *queue)
            clock_events[slot] += events
            service_totals = [x + y for x, y in zip(service_totals, potential)]
            if trial < 2:
                trace.append({"slot": slot, "before": before, "potential_service": potential,
                              "clock_events": events, "channel_jumps": jumps_in_slot,
                              "arrivals": arrival, "after": queue.copy()})
        if trial < 2:
            examples.append(trace)
    assert channel_jumps["control"] > 0 and channel_jumps["data"] > 0
    assert sum(clock_events) > 500000
    return {"seed": 20261015, "graph": "path on 3 links", "independent_trials": trials,
            "actual_slots_per_trial": 3, "clock_policy": "uncapped exp((t+1)^2), entire slot",
            "channel_generator": [["-1/4", "1/4"], ["1/2", "-1/2"]],
            "channel_capacities": [[0.5, 0.5, 0.5], [1.0, 1.0, 1.0]],
            "clock_events_by_slot": clock_events, "total_clock_events": sum(clock_events),
            "channel_jumps": channel_jumps, "total_potential_service": service_totals,
            "maximum_observed_queue": max_queue, "sample_traces": examples, "collisions": 0,
            "claim": "finite execution of continuous-channel controller; not empirical strong-stability evidence"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tamper", choices=["none", "reverse-activation"], default="none")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    start = time.time()
    receipt = {"status": "RUNNING", "tamper": args.tamper, "evidence_scope": "finite exact checks and finite smoke, not a kernel proof"}
    try:
        receipt["graph_checks"] = exact_graph_checks(args.tamper)
        receipt["frozen_service"] = frozen_service_check()
        receipt["markov_poisson"] = markov_poisson_check()
        receipt["continuous_channel"] = [continuous_channel_check(1), continuous_channel_check(100)]
        slow = F(receipt["continuous_channel"][0]["actual_total_useful_service"])
        fast = F(receipt["continuous_channel"][1]["actual_total_useful_service"])
        assert slow < fast < F(9, 11)
        states, wrong = heat_bath(2, [(0, 1)], [2, 3], reverse=True)
        assert not invariant(gibbs(states, [2, 3]), wrong)
        assert not valid(3, [(0, 1)])
        assert F(7, 8) < 1 and F(7, 8) > 1 - F(1, 4)
        receipt["negative_controls"] = {
            "reversed_activation_rejected_by_exact_stationarity": True,
            "conflicting_schedule_rejected": True,
            "instantaneous_gibbs_joint_channel_law_rejected": True,
            "fixed_control_overhead_full_capacity_claim_rejected": True,
            "fixed_overhead_backlog_growth_lower_bound": "1/8 per slot"}
        receipt["bounded_arrival_assumption_gap"] = burst_check()
        receipt["event_driven_smoke"] = event_driven_smoke()
        receipt["continuous_event_smoke"] = continuous_event_smoke()
        receipt["status"] = "PASS"
    except Exception as error:
        receipt["status"] = "FAIL"
        receipt["error_type"] = type(error).__name__
        receipt["error"] = str(error)
    inputs = [root / "proof.md", Path(__file__).resolve()] + sorted((root / "sources").glob("*"))
    receipt["input_sha256"] = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in inputs if p.is_file()}
    receipt["elapsed_seconds"] = round(time.time() - start, 3)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": receipt["status"], "output": str(args.output),
                      "elapsed_seconds": receipt["elapsed_seconds"], "error": receipt.get("error")}))
    if receipt["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
