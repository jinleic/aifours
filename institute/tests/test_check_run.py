#!/usr/bin/env python3
"""Behavior checks for sandboxed parent replay of a completed run; no model calls."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CHECKER = Path(__file__).resolve().parents[1] / "check_run.py"
ENGINE = Path.home() / "jinleic-workspace/research-institute/explorer/ri.py"


class CheckRun(unittest.TestCase):
    def write_run(self, root: Path, accept_control=False, seconds=10.0, status="done"):
        problem = root / "problems/math-p0001"
        attack = problem / "attack-e0"
        (attack / "code").mkdir(parents=True)
        (root / "selection.json").write_text(json.dumps({"hours_per_problem_ceiling": 6,
            "problems": [{"id": "math-p0001"}], "engine_path": str(ENGINE),
            "engine_sha256": hashlib.sha256(ENGINE.read_bytes()).hexdigest()}))
        (root / "run.json").write_text(json.dumps({"status": status}))
        (problem / "record.json").write_text(json.dumps({"log": [
            {"t": "attempt", "stage": "attack", "status": "ok", "quota": 14400,
             "seconds": seconds}, {"t": "outcome", "code": "partial", "epoch": 0}]}))
        (attack / "witness.json").write_text(json.dumps({"n": 91, "a": 7, "b": 13}))
        (attack / "bad.json").write_text(json.dumps({"n": 91, "a": 7, "b": 11}))
        (attack / "code/check.py").write_text(
            "import json, sys\n"
            "w=json.load(open(sys.argv[1]))\n"
            "assert 1 < w['a'] < w['n'] and 1 < w['b'] < w['n']\n"
            "assert w['a'] * w['b'] == w['n'], 'invalid factorization'\n"
            "json.dump(w, open('verified.json', 'w'))\n")
        control = "witness.json" if accept_control else "bad.json"
        (attack / "claims.json").write_text(json.dumps({"outcome": "partial", "claims": [{
            "cid": "factorization", "verify_command": "python3 code/check.py witness.json",
            "check_command": "", "control_command": f"python3 code/check.py {control}"}]}))
        return attack

    def run_checker(self, root):
        return subprocess.run([sys.executable, "-B", str(CHECKER), str(root), "--replay-timeout", "10"],
                              capture_output=True, text=True)

    def test_valid_factorization_and_rejected_mutation_do_not_modify_snapshot(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            attack = self.write_run(root)
            before = {str(p.relative_to(attack)): p.read_bytes() for p in attack.rglob("*") if p.is_file()}
            completed = self.run_checker(root)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            report = json.loads((root / "parent-check.json").read_text())
            replay = report["problems"][0]["parent_replay"][0]
            self.assertEqual(replay["verify_rc"], 0)
            self.assertNotEqual(replay["control_rc"], 0)
            self.assertIn("invalid factorization", replay["control_stderr_tail"])
            after = {str(p.relative_to(attack)): p.read_bytes() for p in attack.rglob("*") if p.is_file()}
            self.assertEqual(before, after)

    def test_accepting_negative_control_is_a_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.write_run(root, accept_control=True)
            completed = self.run_checker(root)
            self.assertEqual(completed.returncode, 1)
            self.assertIn("replay contract failed", completed.stdout)

    def test_budget_overrun_and_incomplete_visits_are_failures(self):
        for seconds, status, expected in [(21661, "done", "exceeded its six-hour allocation"),
                                          (10, "incomplete", "not all requested visits completed")]:
            with self.subTest(status=status), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.write_run(root, seconds=seconds, status=status)
                completed = self.run_checker(root)
                self.assertEqual(completed.returncode, 1)
                self.assertIn(expected, completed.stdout)

    def test_live_snapshots_are_refused_and_outside_writes_are_denied(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            attack = self.write_run(root, status="running")
            completed = self.run_checker(root)
            self.assertEqual(completed.returncode, 2)
            self.assertIn("still active", completed.stderr)
            (root / "run.json").write_text(json.dumps({"status": "done"}))
            outside = root / "must-not-exist"
            (attack / "code/tamper.py").write_text(f"open({str(outside)!r},'w').write('outside')\n")
            claims = json.loads((attack / "claims.json").read_text())
            claims["claims"][0]["verify_command"] = "python3 code/tamper.py"
            (attack / "claims.json").write_text(json.dumps(claims))
            completed = self.run_checker(root)
            self.assertEqual(completed.returncode, 1)
            self.assertFalse(outside.exists())

    def test_approved_requeue_counts_current_epoch_not_lifetime_usage(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old = self.write_run(root, seconds=21661)
            fresh = root / "problems/math-p0001/attack-e1"
            import shutil
            shutil.copytree(old, fresh)
            record_path = root / "problems/math-p0001/record.json"
            record = json.loads(record_path.read_text())
            record["log"].extend([
                {"t": "grant", "stage": "attack", "seconds": 17400,
                 "reason": "owner-approved fresh six-hour budget"},
                {"t": "attempt", "stage": "attack", "epoch": 1, "status": "ok",
                 "quota": 17400, "seconds": 5},
                {"t": "outcome", "code": "partial", "epoch": 1}])
            record_path.write_text(json.dumps(record))
            completed = self.run_checker(root)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            result = json.loads((root / "parent-check.json").read_text())["problems"][0]
            self.assertEqual(result["attempt_seconds"], 5)
            self.assertEqual(result["lifetime_attempt_seconds"], 21666)


if __name__ == "__main__":
    unittest.main()
