
import importlib.util, os, signal, sys, threading, time, json
src = open(sys.argv[1], "rb").read()
spec = importlib.util.spec_from_loader("v4draft", loader=None, origin=sys.argv[1])
m = importlib.util.module_from_spec(spec); m.__file__ = sys.argv[1]
exec(compile(src, sys.argv[1], "exec", dont_inherit=True), m.__dict__)
d = sys.argv[2]
stop = {}
def on_term(signum, frame): stop["signal"] = signal.Signals(signum).name
signal.signal(signal.SIGTERM, on_term); signal.signal(signal.SIGINT, on_term)
out = {}
n = {"i": 0}
def run(tag, eligible=True, setup=None):
    n["i"] += 1
    stem = "%s/%02d-%s" % (d, n["i"], tag)
    paths = {"commit": stem + ".commit.json", "complete": stem + ".complete.json", "cancel": stem + ".cancelled.json"}
    base = {"schema": m.COMMIT_SCHEMA, "label": tag, "receipt": "r", "receipt_sha256": "x"}
    stop.clear()
    restore = setup() if setup else None
    try:
        pub = m.publish_qualification(paths, base, eligible, stop)
    finally:
        if restore: restore()
    time.sleep(0.02)
    out[tag] = {"status": pub["status"], "completion": os.path.exists(paths["complete"]),
                "cancellation": os.path.exists(paths["cancel"]), "reason": (pub["cancel_reason"] or "")[:60],
                "errors": [e[:60] for e in pub["errors"]], "latched": stop.get("signal")}
def killer(sig):
    os.kill(os.getpid(), sig)
real_link, real_write, real_fsync_dir, real_mask = os.link, m.write_json_durable, m.fsync_dir, signal.pthread_sigmask
run("normal")
run("not-eligible", eligible=False)
def s_serial():
    def w(path, obj, real=real_write):
        if path.endswith(".commit.json.prepare"): killer(signal.SIGTERM)
        return real(path, obj)
    m.write_json_durable = w
    def r(): m.write_json_durable = real_write
    return r
run("signal-during-commit-serialization", setup=s_serial)
def s_before_link():
    def l(a, b, real=real_link):
        if b.endswith(".commit.json"): killer(signal.SIGINT)
        return real(a, b)
    os.link = l
    def r(): os.link = real_link
    return r
run("signal-before-commit-link", setup=s_before_link)
def s_after_link():
    def l(a, b, real=real_link):
        x = real(a, b)
        if b.endswith(".commit.json"): killer(signal.SIGTERM)
        return x
    os.link = l
    def r(): os.link = real_link
    return r
run("signal-after-commit-link", setup=s_after_link)
def s_completion():
    def l(a, b, real=real_link):
        x = real(a, b)
        if b.endswith(".complete.json"): killer(signal.SIGINT)
        return x
    os.link = l
    def r(): os.link = real_link
    return r
run("signal-after-completion-link", setup=s_completion)
def s_unmask():
    def mk(how, sigs, real=real_mask):
        if how == signal.SIG_SETMASK: killer(signal.SIGTERM)
        return real(how, sigs)
    signal.pthread_sigmask = mk
    def r(): signal.pthread_sigmask = real_mask
    return r
run("signal-at-unmask", setup=s_unmask)
cnt = {"k": 0}
def s_dirsync():
    def fd_(path, real=real_fsync_dir):
        cnt["k"] += 1
        if cnt["k"] == 3: raise OSError(5, "injected EIO on the directory sync after the commit link")
        return real(path)
    m.fsync_dir = fd_
    def r(): m.fsync_dir = real_fsync_dir
    return r
run("post-commit-link-dirsync-EIO", setup=s_dirsync)
def s_completion_fail():
    def w(path, obj, real=real_write):
        if path.endswith(".complete.json.prepare"): raise OSError(28, "injected ENOSPC in the completion")
        return real(path, obj)
    m.write_json_durable = w
    def r(): m.write_json_durable = real_write
    return r
run("completion-write-failure", setup=s_completion_fail)
def s_thread():
    threading.Thread(target=time.sleep, args=(3,), daemon=True).start()
    return None
run("extra-thread", setup=s_thread)
print(json.dumps(out, indent=1))
