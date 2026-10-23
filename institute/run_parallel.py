#!/usr/bin/env python3
"""Run one selected article per volume concurrently through the existing institute engine."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import multiprocessing
from multiprocessing.connection import wait
import os
from pathlib import Path
import re
import signal
import sys
import time


VISIT_SECONDS = 6 * 3600       # hard wall-clock ceiling per problem, enforced by the supervisor
RESERVE_SECONDS = 600          # stage quotas leave this much of the ceiling for overhead and teardown
ADMISSION_MARGIN = 300         # the engine starts no stage that would end within this margin
JOIN_GRACE = 60                # seconds a terminated lane gets to run its own cleanup
VOLUMES = {"math", "info", "phys"}
SIGNALS = (signal.SIGTERM, signal.SIGHUP, signal.SIGINT)
SYSTEMIC = {"limit", "systemic", "quota", "disk", "secret", "interrupted"}
AUTHORIZED_RUNS = Path("/Users/jinleic/repos/aifours/institute/runs")
INPUT_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


def load_engine(selection: dict):
    path = Path(selection["engine_path"])
    if hashlib.sha256(path.read_bytes()).hexdigest() != selection["engine_sha256"]:
        raise ValueError("institute engine changed since selection; freeze a fresh selection first")
    spec = importlib.util.spec_from_file_location("ri", path)
    engine = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = engine
    spec.loader.exec_module(engine)
    return engine


def selection_digest(pick: dict) -> str:
    return hashlib.sha256(json.dumps(pick, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def lane_base(engine, root: Path, problem_id: str) -> Path:
    return engine.STATE / "parallel" / hashlib.sha256(str(root).encode()).hexdigest()[:12] / problem_id


def lane_state(engine, root: Path, problem_id: str) -> Path:
    base = lane_base(engine, root, problem_id)
    record = engine.read_json(root / "problems" / problem_id / "record.json")
    epoch = engine.epoch_start(record)[0] if record else 0
    return base / f"epoch-{epoch}" if epoch else base


def sweep_tree(engine, tree: dict[int, str], deadline: float | None = None) -> None:
    """Reap retained process identities, including executors reparented after a lane died."""
    for sig in (signal.SIGTERM, signal.SIGKILL):
        for pid, identity in list(tree.items()):
            if not engine.alive(pid, identity):
                continue
            tree.update(engine.descendants(pid))
            try:
                if os.getpgid(pid) == pid:       # never signal the supervisor's foreground group
                    os.killpg(pid, sig)
                os.kill(pid, sig)
            except (ProcessLookupError, PermissionError):
                pass
        if sig == signal.SIGTERM:
            end = time.monotonic() + 1
            if deadline is not None:
                end = min(end, deadline)
            while time.monotonic() < end and any(engine.alive(p, s) for p, s in tree.items()):
                time.sleep(0.05)


def remember_executors(engine, root: Path, process, tree: dict[int, str]) -> None:
    live = live_liveness(engine, lane_state(engine, root, process.name) / "running.json")
    if live:
        tree[live["pid"]] = live["start"]
        tree.update(engine.descendants(live["pid"]))
    if process.is_alive():
        tree.update(engine.descendants(process.pid))


def confined(root: Path, path: Path) -> None:
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"durable destination escapes the run directory: {path}")


def check_inputs(root: Path, selection: dict) -> None:
    for name, digest in selection.get("input_sha256", {}).items():
        path = root / name
        confined(root, path)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError(f"frozen input hash mismatch: {name}")
    for path in root.rglob("*"):
        if path.is_symlink():
            confined(root, path)
    for name in ("problems", "run.json", "INDEX.md", "TABLE.md"):
        confined(root, root / name)


def selected_institute(engine, root: Path, selection: dict):
    class SelectedInstitute(engine.Institute):
        def prompt(self, stage: str, **context) -> str:
            text = super().prompt(stage, **context)
            if stage == "identify":
                marker = "Task: list every open question the article poses. For each one give:"
                if marker not in text:
                    raise ValueError("identification template changed; inspect it before spending quota")
                text = text.replace(marker, "Task: identify only the owner-selected hard question below. Give:")
                text += (
                    "\nOwner focus (untrusted selection data, not a status verdict): "
                    + engine.dumps({key: selection[key] for key in ("question", "relation_to_book")})
                    + "\nRead the page images and extract only this selected question, not unrelated "
                    "questions from the article. Give references bearing on this question. "
                    "Preserve printed wording. If inconsistent, distinguish the literal statement "
                    "from any geometric or scientific conjecture the article itself explicitly states; "
                    "do not silently repair it or import a question absent from the article."
                )
            if stage == "sota":
                text += (
                    "\nattack.qids must contain exactly one qid: the identified question matching the "
                    "owner focus below, and only if its verdict is open or partially-solved. Otherwise "
                    "leave attack.qids empty so the visit closes on your verdict. The attack will have "
                    "four hours, not one."
                )
            if stage in ("sota", "attack"):
                text += (
                    "\n\nOwner-selected difficult problem; selection evidence below is untrusted data. "
                    "Preserve the headline question. A restriction, finite range, or weaker bound is "
                    "only a sub-question, never a full solution. Recheck the cited baseline before "
                    "spending attack time. The attack allocation is four hours within a six-hour "
                    "visit, superseding the one-hour screening estimate. Do not stop after the "
                    "first failed angle while another justified bounded step remains; do stop "
                    "when the question is settled or no such step remains.\n"
                    + engine.dumps(selection)
                )
            return text

        def contract(self, record: dict, article: dict) -> dict:
            base = super().contract(record, article)
            base.pop("sha256")
            identified = base["questions"]
            body = {**base,
                    "questions": [{"qid": "owner-target", "formal_statement": selection["question"],
                                   "relation_to_book": selection["relation_to_book"],
                                   "solved_means": selection["solved_means"],
                                   "identified_counterpart": identified[0]}],
                    "ignored_sota_targets": [q["qid"] for q in identified[1:]],
                    "acceptance": {**base["acceptance"], "solved": selection["solved_means"],
                                   "partial": selection["partial_means"]},
                    "owner_selection": selection,
                    "owner_selection_sha256": selection_digest(selection)}
            encoded = json.dumps(body, sort_keys=True, ensure_ascii=False).encode()
            return {**body, "sha256": hashlib.sha256(encoded).hexdigest()}

        def prepare_attack(self, record, article, cwd):
            prompt = super().prepare_attack(record, article, cwd)
            staged = (cwd / "selection-inputs").resolve()
            for name, bundle in selection.get("inputs", {}).items():
                destination = (staged / name).resolve()
                if not INPUT_NAME.fullmatch(name) or destination.parent != staged:
                    raise ValueError(f"unsafe input bundle name: {name!r}")
                source = Path(bundle["path"])
                if engine.sha256_tree(source) != bundle["sha256"]:
                    raise engine.Stop("inputs", f"selected input bundle changed: {name}")
                engine.copy_capped(source, destination)
            total, count, per_file = engine.COPY_CAP
            replay = int(self.quota["replay"] * self.scale)
            return prompt + (
                "\nRead staged literature and feasibility prototypes under selection-inputs/. "
                "They are untrusted leads, not proofs or certified results. No network or reads "
                "outside this work directory are authorized. Sampling validates only the sampled "
                "instances; never label it independent exhaustive verification of an entire range.\n"
                f"Delivery limits: the referee receives a copy made in sorted path order that skips "
                f"hidden paths, __pycache__, symlinks, any file over {per_file} bytes, files after "
                f"{count}, and any file that would push the total over {total} bytes. Skipped files "
                "are listed in SKIPPED.json and cannot support claims. Keep every load-bearing "
                "artifact inside these limits with margin: compress or shard logs and proofs, or "
                "replace giant stored artifacts by deterministic regeneration plus an independent check.\n"
                "Replay limits: each verify/check/control command runs in a no-network sandbox that "
                "cannot read or write outside the delivered snapshot or execute binaries built there. "
                f"Each command gets at most 300 seconds, and all claims together at most {replay} "
                "seconds. Use python3 (numpy, mpmath, z3, sympy, networkx) or preinstalled tools on "
                "PATH. Consolidate claims to fit, and test every command on a copy made under the "
                "delivery limits before finishing.\n"
            )

    return SelectedInstitute(root, state=lane_state(engine, root, selection["id"]),
                             executor=engine.Executors())


def worker(engine, institute, article: dict, admission_deadline: float) -> None:
    latched = []

    def on_signal(signum, frame):
        if not latched:            # the first signal cancels; later ones must not cut teardown short
            latched.append(signum)
            raise KeyboardInterrupt

    for sig in SIGNALS:
        signal.signal(sig, on_signal)
    started = time.monotonic()
    report = {"id": article["id"], "pid": os.getpid(), "started": engine.utc(),
              "budget_seconds": VISIT_SECONDS, "status": "running"}
    path = institute.dossier(article["id"]) / "lane.json"
    engine.write_json(path, report)
    institute.deadline = admission_deadline
    bounded = engine.run_bounded

    def tracked_bounded(*args, on_start=None, **kwargs):
        def published(pid, identity):
            engine.write_json(institute.liveness(), {"id": article["id"], "pid": pid,
                                                      "start": identity})
            if on_start:
                on_start(pid, identity)
        return bounded(*args, on_start=published, **kwargs)

    # Replay also uses run_bounded, but the base engine does not publish its PID.
    # Keep every bounded executor discoverable if this worker is abruptly killed.
    engine.run_bounded = tracked_bounded
    print(f"START {article['id']} pid={os.getpid()} budget={VISIT_SECONDS}s", flush=True)
    try:
        signal.pthread_sigmask(signal.SIG_UNBLOCK, set(SIGNALS))
        record = institute.visit(article)
        if record is None:
            report.update(status="skipped")
        else:
            closed = engine.closed(record)
            report.update(status="incomplete" if closed["code"] == "timed-out" else "done",
                          outcome=closed)
    except engine.Stop as exc:
        report.update(status="stopped", reason=exc.reason, detail=str(exc))
    except KeyboardInterrupt:
        report.update(status="stopped", reason="interrupted")
    except BaseException as exc:
        report.update(status="stopped", reason="worker-error", detail=type(exc).__name__)
    finally:
        for sig in SIGNALS:
            signal.signal(sig, signal.SIG_IGN)
        sweep_tree(engine, engine.descendants(os.getpid()))
        report.update(ended=engine.utc(), seconds=round(time.monotonic() - started, 1))
        engine.write_json(path, report)
    print(f"END {article['id']} {report['status']} "
          f"{(report.get('outcome') or {}).get('code', report.get('reason', ''))}", flush=True)


def live_liveness(engine, path: Path) -> dict | None:
    live = engine.read_json(path) or {}
    pid = live.get("pid")
    return live if pid and engine.alive(pid, live.get("start")) else None


def validate(engine, root: Path, selection: dict):
    check_inputs(root, selection)
    picks = selection["problems"]
    if len(picks) != 3 or {p["volume"] for p in picks} != VOLUMES:
        raise ValueError("select exactly three articles: one math, one info, one phys")
    if len({p["id"] for p in picks}) != 3:
        raise ValueError("selected article ids must be distinct")
    base = engine.Institute(root)
    base.check_host()
    if set(base.quota) != set(engine.STAGES) or any(
        not isinstance(q, (int, float)) or q < engine.MIN_STAGE_SECONDS
        for q in base.quota.values()
    ) or sum(base.quota.values()) > VISIT_SECONDS - RESERVE_SECONDS:
        raise ValueError("stage quotas must be positive and leave the reserve inside six hours")
    if (live := live_liveness(engine, engine.STATE / "running.json")):
        raise ValueError(f"a live executor from another runner is recorded: {live}")
    lanes = []
    for pick in picks:
        article = base.article(pick["id"])
        if article["volume"] != pick["volume"]:
            raise ValueError(f"wrong volume for {pick['id']}")
        if pick["id"] in base.owned() or base.ai4s_overlap(article):
            raise ValueError(f"existing AI4S ownership blocks {pick['id']}")
        pdf = Path(article["_book"]["pdf"])
        if not pdf.is_file():
            raise ValueError(f"source PDF missing for {pick['id']}: {pdf}")
        with pdf.open("rb") as handle:
            if hashlib.file_digest(handle, "sha256").hexdigest() != article["_book"]["pdf_sha256"]:
                raise ValueError(f"source PDF hash mismatch for {pick['id']}")
        state = lane_state(engine, root, pick["id"])
        for live_path in lane_base(engine, root, pick["id"]).rglob("running.json"):
            if (live := live_liveness(engine, live_path)):
                raise ValueError(f"{pick['id']} has a live executor recorded: {live}")
        bound_pick = {**pick, "shared_scope_rules": selection.get("scope_rules", []),
                      "shared_review_overrides": selection.get("review_overrides", [])}
        confined(root, base.dossier(pick["id"]))
        record = base.load(pick["id"])
        if record is not None:
            if engine.closed(record):
                raise ValueError(f"{pick['id']} already closed; use ri.py requeue explicitly")
            if not (base.dossier(pick["id"]) / "lane.json").is_file():
                raise ValueError(f"{pick['id']} has a record this launcher did not start")
            epoch, first_stage, _ = engine.epoch_start(record)
            uses_previous_attack = engine.STAGES.index(first_stage) > engine.STAGES.index("attack")
            contracts = [entry["contract"] for entry in record["log"] if entry.get("contract")
                         and (entry.get("epoch") == epoch or uses_previous_attack)]
            if contracts and contracts[-1].get("owner_selection_sha256") != selection_digest(bound_pick):
                raise ValueError(f"{pick['id']} has an attack contract for a different selection")
        if (record is None or not engine.outputs(record).get("identify")) and (state / "pages").exists():
            raise ValueError(f"{pick['id']} has unverified cached page renders; inspect them first")
        lanes.append((selected_institute(engine, root, bound_pick), article))
    return base, lanes


def run(engine, root: Path, selection: dict) -> dict:
    # Every lane inherits this descriptor. An orphaned live lane therefore keeps the
    # original machine-wide lock, too; a second runner cannot duplicate its work.
    lock = engine.acquire_lock(engine.STATE)
    processes, deadlines, expired, results, executor_trees = [], {}, set(), {}, {}
    previous = {s: signal.getsignal(s) for s in SIGNALS}
    admitted = False
    started = time.monotonic()
    summary = {"started": engine.utc(), "budget_seconds_per_problem": VISIT_SECONDS,
               "problems": [p["id"] for p in selection["problems"]], "status": "running"}
    try:
        base, lanes = validate(engine, root, selection)
        admitted = True
        engine.Executors().preflight()
        previous = {s: signal.signal(s, engine._raise_interrupt) for s in SIGNALS}
        engine.write_json(root / "run.json", summary)
        context = multiprocessing.get_context("fork")
        # One shared ceiling: every due lane is signaled before any blocking cleanup begins.
        begin = time.monotonic()
        for institute, article in lanes:
            process = context.Process(
                target=worker, name=article["id"],
                args=(engine, institute, article, begin + VISIT_SECONDS - ADMISSION_MARGIN))
            # Do not let interruption land between fork and recording the child's handle.
            mask = signal.pthread_sigmask(signal.SIG_BLOCK, set(SIGNALS))
            try:
                process.start()
                processes.append(process)
                executor_trees[process.name] = {}
                deadlines[process.name] = begin + VISIT_SECONDS
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK, mask)
        active = list(processes)
        while active:
            for process in active:
                remember_executors(engine, root, process, executor_trees[process.name])
            cleanup_reserve = min(JOIN_GRACE, VISIT_SECONDS / 10)
            timeout = max(0.0, min(deadlines[p.name] - cleanup_reserve for p in active) - time.monotonic())
            wait([p.sentinel for p in active], timeout=min(timeout, 1.0))
            now = time.monotonic()
            for process in active:
                remember_executors(engine, root, process, executor_trees[process.name])
                if process.is_alive() and now >= deadlines[process.name] - cleanup_reserve:
                    expired.add(process.name)
                    process.terminate()          # notify every due lane before any blocking join
            for process in list(active):
                if process.name in expired:
                    stop_lane(engine, process, executor_trees[process.name], deadlines[process.name])
                if process.is_alive():
                    continue
                process.join()
                active.remove(process)
                stop_lane(engine, process, executor_trees[process.name],
                          deadlines[process.name] if process.name in expired else None)
                report = engine.read_json(base.dossier(process.name) / "lane.json") or {}
                if process.name in expired and report.get("status") != "done":
                    report = {**report, "status": "stopped", "reason": "deadline",
                              "exitcode": process.exitcode}
                elif process.exitcode != 0 or report.get("reason") in SYSTEMIC:
                    results[process.name] = report
                    summary.update(status="stopped", reason=f"lane {process.name}: "
                                   f"{report.get('reason') or f'exit {process.exitcode}'}")
                    return summary
                results[process.name] = report
        done = all(r.get("status") == "done" for r in results.values())
        summary["status"] = "done" if done else "incomplete"
        return summary
    except KeyboardInterrupt:
        summary.update(status="stopped", reason="interrupted")
        return summary
    except (ValueError, engine.Refused, engine.Stop) as exc:
        summary.update(status="stopped", reason=str(exc))
        return summary
    except BaseException:
        summary.update(status="stopped", reason="supervisor-error")
        raise
    finally:
        for sig in SIGNALS:                     # teardown must not be cut short by a second signal
            signal.signal(sig, signal.SIG_IGN)
        for process in processes:
            remember_executors(engine, root, process, executor_trees[process.name])
            stop_lane(engine, process, executor_trees[process.name],
                      deadlines[process.name] if process.name in expired else None)
        for sig, handler in previous.items():
            signal.signal(sig, handler)
        summary.update(ended=engine.utc(), seconds=round(time.monotonic() - started, 1))
        lanes_report = []
        for process in processes:
            report = engine.read_json(root / "problems" / process.name / "lane.json") or {}
            if report.get("status") == "running" and process.exitcode is not None:
                report = {**report, "status": "stopped", "reason": "worker-exit",
                          "exitcode": process.exitcode, "record_requires_recovery": True}
            if process.name in expired and report.get("status") != "done":
                report = {**report, "status": "stopped", "reason": "deadline"}
            lanes_report.append(report)
        summary["lanes"] = lanes_report
        # Only the supervisor renders shared indexes; records remain engine-owned.
        try:
            if admitted:
                engine.Institute(root).write_index()
                engine.write_json(root / "run.json", summary)
        finally:
            os.close(lock)


def stop_lane(engine, process, tree: dict[int, str], deadline: float | None = None) -> None:
    """Cancellation is deferred until the lane and every retained executor have been swept."""
    mask = signal.pthread_sigmask(signal.SIG_BLOCK, set(SIGNALS))
    try:
        if process.is_alive():
            tree.update(engine.descendants(process.pid))
            process.terminate()
            grace = JOIN_GRACE if deadline is None else max(0.0, min(JOIN_GRACE, deadline - time.monotonic()))
            process.join(grace)
        if process.is_alive():
            tree.update(engine.descendants(process.pid))
            process.kill()
            process.join()
    finally:
        try:
            sweep_tree(engine, tree, deadline)   # also runs when the lane was already dead
        finally:
            signal.pthread_sigmask(signal.SIG_SETMASK, mask)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("selection", type=Path, help="frozen selection.json in the run's data root")
    parser.add_argument("--check", action="store_true", help="validate selection and budgets; no model calls")
    args = parser.parse_args()
    path = args.selection.resolve()
    selection = json.loads(path.read_text(encoding="utf-8"))
    try:
        engine = load_engine(selection)
    except ValueError as exc:
        parser.error(str(exc))
    if not path.parent.is_relative_to(AUTHORIZED_RUNS) or path.parent == AUTHORIZED_RUNS:
        parser.error(f"run data must live in a directory under {AUTHORIZED_RUNS}")
    try:
        if args.check:
            base, lanes = validate(engine, path.parent, selection)
            print(json.dumps({"ids": [a["id"] for _, a in lanes], "quota": base.quota,
                              "seconds_per_problem": VISIT_SECONDS}, indent=2))
            return 0
        result = run(engine, path.parent, selection)
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return 0 if result["status"] == "done" else 1
    except (ValueError, engine.Refused, engine.Stop) as exc:
        print(f"refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
