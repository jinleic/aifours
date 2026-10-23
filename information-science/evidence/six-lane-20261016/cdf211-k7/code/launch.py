"""Start a command fully detached (new session), log stdout/stderr to files, record it in a registry.

usage: python3 launch.py RUN_DIR NAME -- CMD [ARGS...]
Writes RUN_DIR/NAME.log (stdout+stderr) and appends one JSON line to RUN_DIR/launch-registry.jsonl
with host time, pid, cwd and argv.  The command is started with cwd=RUN_DIR.
"""
import sys, os, json, subprocess, time

def main():
    run_dir, name = sys.argv[1], sys.argv[2]
    assert sys.argv[3] == "--"
    cmd = sys.argv[4:]
    os.makedirs(run_dir, exist_ok=True)
    log = open(os.path.join(run_dir, name + ".log"), "ab")
    p = subprocess.Popen(cmd, cwd=run_dir, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                         start_new_session=True)
    rec = dict(time=time.strftime("%Y-%m-%dT%H:%M:%S%z"), name=name, pid=p.pid, cwd=os.path.abspath(run_dir), argv=cmd)
    with open(os.path.join(run_dir, "launch-registry.jsonl"), "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(json.dumps(rec))

if __name__ == "__main__":
    main()
