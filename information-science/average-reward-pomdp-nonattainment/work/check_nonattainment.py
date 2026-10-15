#!/usr/bin/env python3
"""Exact finite checks for the written POMDP nonattainment proof.

The infinite quantifier is proved in ../proof.md, not by this finite verifier.
Only the Python standard library is required.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

STATES = ("B", "G", "H", "L")


def plant(q):
    return {
        ("B", "W"): {"B": q, "G": 1 - q},
        ("B", "C"): {"L": F(1)},
        ("G", "W"): {"G": F(1)},
        ("G", "C"): {"H": F(1)},
        ("H", "W"): {"H": F(1)},
        ("H", "C"): {"H": F(1)},
        ("L", "W"): {"L": F(1)},
        ("L", "C"): {"L": F(1)},
    }


def forward(transitions, horizon, policy, reward=None):
    reward = reward or {s: F(s == "H") for s in STATES}
    state = {s: F(s == "B") for s in STATES}
    total = F(0)
    for t in range(horizon):
        total += sum(state[s] * reward[s] for s in STATES)
        following = dict.fromkeys(STATES, F(0))
        for s in STATES:
            actions = policy(t, s)
            assert sum(actions.values()) == 1
            for action, action_prob in actions.items():
                row = transitions[s, action]
                assert sum(row.values()) == 1
                for dest, transition_prob in row.items():
                    following[dest] += state[s] * action_prob * transition_prob
        state = following
    assert sum(state.values()) == 1
    return total / horizon, state


def waiting_policy(n):
    return lambda t, _: {"W" if t < n else "C": F(1)}


def check_wait(transitions, q, n, horizon, reward=None):
    actual, final = forward(transitions, horizon, waiting_policy(n), reward)
    target = F(max(horizon - n - 1, 0), horizon) * (1 - q**n)
    assert actual == target, (actual, target)
    if horizon > n:
        assert final["H"] == 1 - q**n
        assert final["L"] == q**n
    return actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    count = 0
    for q in (F(1, 4), F(1, 2), F(3, 4)):
        transitions = plant(q)
        for n in (0, 1, 2, 4, 8, 16):
            for horizon in (1, 2, 5, 19, 50):
                check_wait(transitions, q, n, horizon)
                count += 1

    # Independent state propagation versus an explicit first-commit mixture.
    stationary_checks = 0
    stationary = []
    q = F(1, 2)
    for c in (F(1), F(1, 2), F(1, 4), F(1, 16), F(1, 128)):
        policy = lambda t, s, c=c: {"C": c, "W": 1 - c}
        for horizon in (2, 3, 11, 40):
            actual, _ = forward(plant(q), horizon, policy)
            expected = sum(
                c * (1 - c)**n * (1 - q**n)
                * F(max(horizon - n - 1, 0), horizon)
                for n in range(horizon)
            )
            assert actual == expected
            stationary_checks += 1
        gain = 1 - c / (1 - q * (1 - c))
        assert gain == (1 - c) / (1 + c)
        stationary.append({"commit_probability": str(c), "limiting_gain": str(gain)})
    never, _ = forward(plant(q), 100, lambda t, s: {"W": F(1)})
    assert never == 0

    # Every finite randomized commit distribution has the stated positive gap.
    probabilities = {0: F(1, 10), 2: F(1, 5), 7: F(2, 5)}
    noncommit = F(3, 10)
    assert sum(probabilities.values()) + noncommit == 1
    gain = sum(p * (1 - q**n) for n, p in probabilities.items())
    gap = noncommit + sum(p * q**n for n, p in probabilities.items())
    assert gain + gap == 1 and gap > 0
    delayed_gain = sum(p * (1 - q**(n + 1)) for n, p in probabilities.items())
    assert delayed_gain - gain == (1 - q) * (gap - noncommit) > 0

    # A different information structure really removes the obstruction.
    full_observation = lambda t, s: {"W" if s == "B" else "C": F(1)}
    observed = []
    for horizon in (3, 10, 50):
        actual, state = forward(plant(q), horizon, full_observation)
        expected = sum((1 - q**(t - 1)) for t in range(1, horizon)) / horizon
        assert actual == expected
        assert state["L"] == 0 and state["H"] == 1 - q**(horizon - 1)
        observed.append({"horizon": horizon, "expected_average": str(actual)})

    # Behavioral negative controls: wrong rewards or transitions must invalidate
    # the absorbing-payoff formula, not merely change a source hash.
    rejected = []
    wrong_wait = plant(q)
    wrong_wait["B", "W"] = {"B": F(3, 4), "G": F(1, 4)}
    wrong_commit = plant(q)
    wrong_commit["G", "C"] = {"L": F(1)}
    controls = [
        ("wrong_wait_probability", wrong_wait, None),
        ("ready_commit_fails", wrong_commit, None),
        ("successful_state_has_zero_reward", plant(q), dict.fromkeys(STATES, F(0))),
    ]
    for name, transitions, rewards in controls:
        try:
            check_wait(transitions, q, 3, 20, rewards)
        except AssertionError:
            rejected.append(name)
        else:
            raise AssertionError("Invalid model passed: " + name)

    rows = []
    for n in (0, 1, 2, 4, 8, 16, 32):
        rows.append({"wait_actions": n, "limiting_gain": str(1 - q**n), "gap": str(q**n)})
    result = {
        "status": "PASS",
        "scope": "Exact finite identities and countermodel controls, not a kernel proof of nonattainment",
        "deterministic_forward_checks": count,
        "stationary_first_commit_checks": stationary_checks,
        "deterministic_policy_gains": rows,
        "stationary_policy_gains": stationary,
        "random_commit_distribution": {"gain": str(gain), "gap": str(gap), "delayed_gain": str(delayed_gain)},
        "full_observation_control": observed,
        "rejected_model_mutations": rejected,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "deterministic_checks": count, "stationary_checks": stationary_checks, "negative_controls": len(rejected)}))


if __name__ == "__main__":
    main()
