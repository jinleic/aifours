#!/usr/bin/env python3
"""Process/lock/cancellation/contract checks for the parallel launcher; no model calls."""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import run_parallel as launcher

ENGINE_PATH = Path.home() / "jinleic-workspace/research-institute/explorer/ri.py"
ENGINE_SHA = hashlib.sha256(ENGINE_PATH.read_bytes()).hexdigest()
engine = launcher.load_engine({"engine_path": str(ENGINE_PATH), "engine_sha256": ENGINE_SHA})
sys.path.insert(0, str(ENGINE_PATH.parent))
import test_ri as fixtures

QUOTAS = {"identify": 600, "sota": 1500, "attack": 14400, "replay": 1200, "review": 2400,
          "novelty": 900}


class ProbeExecutor:
    """Stands in for the model CLIs; the real process, record, lock and watchdog code runs."""
    mode = "quick"
    signal_after = None

    def preflight(self):
        pass

    def long_child(self, cwd, logs, on_start):
        def started(pid, identity):
            (cwd / "child-pid.txt").write_text(str(pid))
            if on_start:
                on_start(pid, identity)
            if ProbeExecutor.signal_after and "info-p0001" in str(cwd):
                threading.Timer(ProbeExecutor.signal_after, foreground_interrupt).start()
            if ProbeExecutor.mode == "crash":
                os.kill(os.getpid(), signal.SIGKILL)
        logs.mkdir(parents=True, exist_ok=True)
        engine.run_bounded([sys.executable, "-c", "import time; time.sleep(60)"], cwd=cwd,
                           stdin=None, stdout=logs / "probe.out", stderr=logs / "probe.err",
                           timeout=60, on_start=started)

    def __call__(self, stage, cwd, logs, prompt, timeout, on_start=None):
        if stage != "identify":
            raise AssertionError("this probe closes at identification")
        start = time.monotonic()
        try:
            descriptor = engine.acquire_lock(engine.STATE)
        except engine.Refused:
            lock_refused = True
        else:
            os.close(descriptor)
            lock_refused = False
        is_math = "math-p0001" in str(cwd)
        if self.mode == "limit" and is_math:
            time.sleep(1)
            return fixtures.result(status="limit", error="probe usage limit")
        if self.mode == "failed" and is_math:
            return fixtures.result(status="failed", error="probe lane failure")
        if self.mode == "replay-crash" and is_math:
            killer = threading.Timer(0.75, os.kill, args=(os.getpid(), signal.SIGKILL))
            killer.daemon = True
            killer.start()
            logs.mkdir(parents=True, exist_ok=True)
            engine.sandboxed("python3 -c 'import time; time.sleep(60)'", cwd,
                             logs / "sandbox-probe", 60)
        elif (self.mode in ("crash", "ignore-term") and is_math) or self.mode == "stubborn":
            if self.mode in ("ignore-term", "stubborn"):
                signal.signal(signal.SIGTERM, signal.SIG_IGN)
            self.long_child(cwd, logs, on_start)
        elif self.mode == "stall" and is_math:
            time.sleep(30)              # a stalled stage wrapper the engine cannot time out
        elif self.mode in ("limit", "interrupt"):
            self.long_child(cwd, logs, on_start)
        else:
            time.sleep(0.05 if self.mode == "staggered" and is_math else 0.5)
        (cwd / "interval.json").write_text(json.dumps({"start": start,
            "end": time.monotonic(), "lock_refused": lock_refused}))
        return fixtures.result(output={**fixtures.IDENTIFY, "questions": []})


def foreground_interrupt():
    """What Ctrl-C in a terminal does: SIGINT to the supervisor and every lane at once."""
    supervisor = os.getppid()
    lanes = [pid for pid, (ppid, _) in engine._ps().items() if ppid == supervisor]
    for pid in [supervisor, *lanes]:
        os.kill(pid, signal.SIGINT)


class ParallelLifecycle(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="aifours-parallel-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / "visit"
        (self.root / "inventory").mkdir(parents=True)
        pdf = self.base / "book.pdf"
        pdf.write_bytes(b"%PDF-1.4 lifecycle probe\n")
        picks = []
        for volume in ("math", "info", "phys"):
            article = fixtures.art(volume, 1, volume + " probe article")
            inventory = {"book": {"title_zh": volume, "year": 2009, "pdf": str(pdf),
                                   "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()},
                         "articles": [article]}
            (self.root / "inventory" / f"{volume}.json").write_text(json.dumps(inventory))
            picks.append({"id": article["id"], "volume": volume, "baseline": "probe",
                          "question": "Does this test-generated article pose a precise question?",
                          "relation_to_book": "Synthetic input for lifecycle checks, not research.",
                          "solved_means": "a proof", "partial_means": "a scoped result"})
        (self.root / "config.json").write_text(json.dumps({"quota": QUOTAS}))
        self.selection = {"problems": picks}
        ProbeExecutor.mode, ProbeExecutor.signal_after = "quick", None
        for target, value in (("STATE", self.base / "state"),
                              ("Executors", ProbeExecutor),
                              ("extract_article", fixtures.fake_extract),
                              ("secret_values", lambda: set())):
            replacement = patch.object(engine, target, value)
            replacement.start()
            self.addCleanup(replacement.stop)

    def assert_lock_free(self):
        descriptor = engine.acquire_lock(engine.STATE)
        os.close(descriptor)

    def assert_no_live_children(self, expected):
        pid_files = list((self.base / "state").rglob("child-pid.txt"))
        self.assertEqual(len(pid_files), expected)
        self.assertTrue(all(not engine.alive(int(path.read_text())) for path in pid_files))

    def record(self, problem_id):
        return engine.Institute(self.root).load(problem_id)

    def test_three_visits_overlap_and_exclude_another_runner(self):
        summary = launcher.run(engine, self.root, self.selection)
        self.assertEqual(summary["status"], "done")
        intervals = [json.loads(p.read_text())
                     for p in (self.base / "state").rglob("interval.json")]
        self.assertEqual(len(intervals), 3)
        self.assertLess(max(i["start"] for i in intervals), min(i["end"] for i in intervals))
        self.assertTrue(all(i["lock_refused"] for i in intervals))
        for pick in self.selection["problems"]:
            self.assertEqual(engine.closed(self.record(pick["id"]))["code"], "no-precise-question")
        self.assert_lock_free()

    def test_usage_limit_stops_siblings_and_their_executor_processes(self):
        ProbeExecutor.mode = "limit"
        started = time.monotonic()
        summary = launcher.run(engine, self.root, self.selection)
        self.assertEqual(summary["status"], "stopped")
        self.assertLess(time.monotonic() - started, 30)
        self.assert_no_live_children(2)
        self.assertTrue(all(lane["status"] == "stopped" for lane in summary["lanes"]))
        for pick in self.selection["problems"]:
            record = self.record(pick["id"])
            self.assertIsNone(engine.closed(record))
            self.assertFalse(any(a.get("status") == "running" for a in record["log"]))
        self.assert_lock_free()

    def test_lane_failure_does_not_stop_its_siblings(self):
        ProbeExecutor.mode = "failed"
        summary = launcher.run(engine, self.root, self.selection)
        self.assertEqual(summary["status"], "incomplete")
        lanes = {lane["id"]: lane for lane in summary["lanes"]}
        self.assertEqual((lanes["math-p0001"]["status"], lanes["math-p0001"]["reason"]),
                         ("stopped", "failed"))
        for problem in ("info-p0001", "phys-p0001"):
            self.assertEqual(lanes[problem]["status"], "done")
            self.assertEqual(engine.closed(self.record(problem))["code"], "no-precise-question")
        self.assertIsNone(engine.closed(self.record("math-p0001")))
        self.assert_lock_free()

    def test_foreground_interrupt_cannot_cut_executor_cleanup_short(self):
        ProbeExecutor.mode, ProbeExecutor.signal_after = "interrupt", 1.5
        started = time.monotonic()
        summary = launcher.run(engine, self.root, self.selection)
        self.assertEqual((summary["status"], summary["reason"]), ("stopped", "interrupted"))
        self.assertLess(time.monotonic() - started, 30)
        self.assert_no_live_children(3)
        for pick in self.selection["problems"]:
            self.assertFalse(any(a.get("status") == "running"
                                 for a in self.record(pick["id"])["log"]))
        self.assert_lock_free()

    def test_hard_ceiling_stops_only_the_stalled_lane(self):
        ProbeExecutor.mode = "stall"
        quotas = {stage: 0.1 for stage in QUOTAS}
        (self.root / "config.json").write_text(json.dumps({"quota": quotas}))
        with patch.multiple(launcher, VISIT_SECONDS=3, RESERVE_SECONDS=0, ADMISSION_MARGIN=0,
                            JOIN_GRACE=5), patch.object(engine, "MIN_STAGE_SECONDS", 0):
            started = time.monotonic()
            summary = launcher.run(engine, self.root, self.selection)
            elapsed = time.monotonic() - started
        self.assertEqual(summary["status"], "incomplete")
        self.assertLess(elapsed, 3 + 5 + 5)
        lanes = {lane["id"]: lane for lane in summary["lanes"]}
        self.assertEqual((lanes["math-p0001"]["status"], lanes["math-p0001"]["reason"]),
                         ("stopped", "deadline"))
        self.assertEqual({lanes[p]["status"] for p in ("info-p0001", "phys-p0001")}, {"done"})
        self.assertFalse(any(a.get("status") == "running"
                             for a in self.record("math-p0001")["log"]))
        self.assert_lock_free()

    def test_interrupt_during_fork_registration_reaps_the_started_child(self):
        process_type = launcher.multiprocessing.get_context("fork").Process
        original_start = process_type.start
        spawned = []

        def interrupted_start(process):
            original_start(process)
            spawned.append(process)
            os.kill(os.getpid(), signal.SIGTERM)

        try:
            with patch.object(process_type, "start", interrupted_start):
                summary = launcher.run(engine, self.root, self.selection)
            self.assertEqual((summary["status"], summary["reason"]), ("stopped", "interrupted"))
            self.assertEqual(len(spawned), 1)
            self.assertFalse(spawned[0].is_alive())
            self.assert_lock_free()
        finally:
            for process in spawned:
                if process.is_alive():
                    process.terminate()
                process.join()

    def test_contract_binds_owner_target_and_refuses_unsafe_input_names(self):
        bundle = self.base / "bundle"
        bundle.mkdir()
        (bundle / "lead.txt").write_text("untrusted literature lead\n")
        pick = {**self.selection["problems"][0],
                "inputs": {"..": {"path": str(bundle), "sha256": engine.sha256_tree(bundle)}}}
        lane = launcher.selected_institute(engine, self.root, pick)
        sota = {**fixtures.SOTA, "attack": {**fixtures.SOTA["attack"], "qids": ["q1", "q2"]}}
        record = {"schema": "ri-record/2", "id": pick["id"], "log": [
            {"t": "attempt", "stage": "identify", "epoch": 0, "status": "ok",
             "output": fixtures.IDENTIFY},
            {"t": "attempt", "stage": "sota", "epoch": 0, "status": "ok", "output": sota},
            {"t": "attempt", "stage": "attack", "epoch": 0, "status": "running", "quota": 600,
             "output": None}]}
        contract = lane.contract(record, engine.Institute(self.root).article(pick["id"]))
        self.assertEqual([q["qid"] for q in contract["questions"]], ["owner-target"])
        self.assertEqual(contract["questions"][0]["formal_statement"], pick["question"])
        self.assertEqual(contract["ignored_sota_targets"], ["q2"])
        self.assertEqual(contract["owner_selection_sha256"], launcher.selection_digest(pick))
        cwd = self.base / "attack-cwd"
        cwd.mkdir()
        with self.assertRaisesRegex(ValueError, "unsafe input bundle name"):
            lane.prepare_attack(record, engine.Institute(self.root).article(pick["id"]), cwd)
        safe = {**pick, "inputs": {"literature": pick["inputs"][".."]}}
        lane = launcher.selected_institute(engine, self.root, safe)
        lane.prepare_attack(record, engine.Institute(self.root).article(pick["id"]), cwd)
        self.assertEqual((cwd / "selection-inputs/literature/lead.txt").read_text(),
                         "untrusted literature lead\n")
        self.assertTrue((cwd / "contract.json").is_file())

    def test_quotas_must_leave_the_reserve_inside_six_hours(self):
        path = self.root / "config.json"
        config = json.loads(path.read_text())
        config["quota"]["attack"] += 60
        path.write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError, "leave the reserve inside six hours"):
            launcher.validate(engine, self.root, self.selection)

    def test_changed_source_pdf_is_refused(self):
        (self.base / "book.pdf").write_bytes(b"%PDF-1.4 altered\n")
        with self.assertRaisesRegex(ValueError, "source PDF hash mismatch"):
            launcher.validate(engine, self.root, self.selection)

    def test_cli_refuses_changed_engine_and_unauthorized_location(self):
        selection = self.root / "selection.json"
        for digest, message in (("0" * 64, "engine changed since selection"),
                                (ENGINE_SHA, "run data must live in a directory under")):
            selection.write_text(json.dumps({"engine_path": str(ENGINE_PATH),
                                              "engine_sha256": digest}))
            completed = subprocess.run([sys.executable, "-B", str(Path(launcher.__file__)),
                                        str(selection), "--check"], capture_output=True, text=True)
            self.assertEqual(completed.returncode, 2)
            self.assertIn(message, completed.stderr)

    def test_crashed_lane_cannot_leave_its_reparented_executor_alive(self):
        ProbeExecutor.mode = "crash"
        summary = launcher.run(engine, self.root, self.selection)
        self.assertEqual(summary["status"], "stopped")
        self.assert_no_live_children(1)
        self.assert_lock_free()

    def test_interrupt_after_forced_kill_cannot_skip_retained_executor_sweep(self):
        ProbeExecutor.mode = "ignore-term"
        process_type = launcher.multiprocessing.get_context("fork").Process
        original_kill = process_type.kill

        def interrupted_kill(process):
            original_kill(process)
            os.kill(os.getpid(), signal.SIGINT)

        quotas = {stage: 0.1 for stage in QUOTAS}
        (self.root / "config.json").write_text(json.dumps({"quota": quotas}))
        with patch.multiple(launcher, VISIT_SECONDS=3, RESERVE_SECONDS=0, ADMISSION_MARGIN=0,
                            JOIN_GRACE=0.2), patch.object(engine, "MIN_STAGE_SECONDS", 0), \
                patch.object(process_type, "kill", interrupted_kill):
            summary = launcher.run(engine, self.root, self.selection)
        self.assertEqual((summary["status"], summary["reason"]), ("stopped", "interrupted"))
        self.assert_no_live_children(1)
        self.assert_lock_free()

    def test_frozen_inventory_and_durable_symlink_escape_are_refused(self):
        inventory = self.root / "inventory/math.json"
        self.selection["input_sha256"] = {"inventory/math.json": hashlib.sha256(
            inventory.read_bytes()).hexdigest()}
        inventory.write_text(inventory.read_text() + "\n")
        with self.assertRaisesRegex(ValueError, "frozen input hash mismatch"):
            launcher.validate(engine, self.root, self.selection)
        self.selection["input_sha256"] = {}
        outside = self.base / "outside"
        outside.mkdir()
        (self.root / "problems").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "durable destination escapes"):
            launcher.validate(engine, self.root, self.selection)
        self.assertEqual(list(outside.iterdir()), [])

    def test_replay_process_is_reaped_when_worker_dies_between_supervisor_samples(self):
        ProbeExecutor.mode = "replay-crash"
        summary = launcher.run(engine, self.root, self.selection)
        self.assertEqual(summary["status"], "stopped")
        published = list((self.base / "state").rglob("running.json"))
        self.assertEqual(len(published), 1)
        identity = json.loads(published[0].read_text())
        self.assertFalse(engine.alive(identity["pid"], identity["start"]))
        self.assert_lock_free()

    def test_siblings_finishing_during_another_lanes_cleanup_are_not_expired(self):
        ProbeExecutor.mode = "staggered"
        original = launcher.stop_lane
        delayed = []

        def slow_cleanup(engine_arg, process, tree, deadline=None):
            original(engine_arg, process, tree, deadline)
            if process.name == "math-p0001" and not delayed:
                delayed.append(True)
                time.sleep(3)

        quotas = {stage: 0.1 for stage in QUOTAS}
        (self.root / "config.json").write_text(json.dumps({"quota": quotas}))
        with patch.multiple(launcher, VISIT_SECONDS=3, RESERVE_SECONDS=0, ADMISSION_MARGIN=0,
                            JOIN_GRACE=0.2), patch.object(engine, "MIN_STAGE_SECONDS", 0), \
                patch.object(launcher, "stop_lane", slow_cleanup):
            summary = launcher.run(engine, self.root, self.selection)
        self.assertEqual(summary["status"], "done")
        self.assertTrue(all(lane["status"] == "done" for lane in summary["lanes"]))
        self.assert_lock_free()


    def test_all_stubborn_lanes_are_stopped_at_one_shared_ceiling(self):
        ProbeExecutor.mode = "stubborn"
        quotas = {stage: 0.1 for stage in QUOTAS}
        (self.root / "config.json").write_text(json.dumps({"quota": quotas}))
        with patch.multiple(launcher, VISIT_SECONDS=3, RESERVE_SECONDS=0, ADMISSION_MARGIN=0,
                            JOIN_GRACE=1), patch.object(engine, "MIN_STAGE_SECONDS", 0):
            started = time.monotonic()
            summary = launcher.run(engine, self.root, self.selection)
            elapsed = time.monotonic() - started
        self.assertLess(elapsed, 3 + 2)
        self.assertEqual({(lane["status"], lane["reason"]) for lane in summary["lanes"]},
                         {("stopped", "deadline")})
        self.assert_no_live_children(3)
        self.assert_lock_free()

    def test_requeued_epoch_uses_fresh_lane_state_and_selected_question_prompt(self):
        self.assertEqual(launcher.run(engine, self.root, self.selection)["status"], "done")
        first_pages = launcher.lane_state(engine, self.root, "math-p0001") / "pages"
        first_pages.mkdir(parents=True)
        institute = engine.Institute(self.root)
        for pick in self.selection["problems"]:
            institute.requeue(pick["id"], stage="identify", seconds=None,
                              reason="owner-approved fresh visit")
        fresh = launcher.lane_state(engine, self.root, "math-p0001")
        self.assertEqual(fresh.name, "epoch-1")
        self.assertNotEqual(fresh / "pages", first_pages)
        _, lanes = launcher.validate(engine, self.root, self.selection)
        prompt = lanes[0][0].prompt("identify", **institute.context(
            institute.load("math-p0001"), lanes[0][1]), garble_note="")
        self.assertIn("identify only the owner-selected hard question", prompt)
        self.assertNotIn("list every open question the article poses", prompt)
        self.assertEqual(launcher.run(engine, self.root, self.selection)["status"], "done")
        record = institute.load("math-p0001")
        self.assertEqual(engine.epoch_start(record)[0], 1)
        self.assertEqual(engine.closed(record)["epoch"], 1)
        self.assert_lock_free()

if __name__ == "__main__":
    unittest.main()
