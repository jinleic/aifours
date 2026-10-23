
import importlib.util, os, signal, sys, threading, time, json
src = open(sys.argv[1], "rb").read()
spec = importlib.util.spec_from_loader("v3draft", loader=None, origin=sys.argv[1])
m = importlib.util.module_from_spec(spec); m.__file__ = sys.argv[1]
exec(compile(src, sys.argv[1], "exec", dont_inherit=True), m.__dict__)
d = sys.argv[2]
stop = {}
def on_term(signum, frame): stop["signal"] = signal.Signals(signum).name
signal.signal(signal.SIGTERM, on_term); signal.signal(signal.SIGINT, on_term)
out = {"threads": threading.active_count()}
c, dg, e = m.publish_commit(d + "/p1.commit.json", {"label": "p1"}, True, stop); out["normal"] = (c["qualified"], e)
real_mask = signal.pthread_sigmask
def mask_then_kill(how, sigs, real=real_mask):
    r = real(how, sigs)
    if how == signal.SIG_BLOCK: os.kill(os.getpid(), signal.SIGINT)
    return r
signal.pthread_sigmask = mask_then_kill; stop.clear()
c, dg, e = m.publish_commit(d + "/p2.commit.json", {"label": "p2"}, True, stop)
signal.pthread_sigmask = real_mask
out["pending_inside"] = (c["qualified"], c["pending_signals_at_commit"], stop.get("signal"))
real_link = os.link
def link_then_kill(a, b, real=real_link):
    r = real(a, b); os.kill(os.getpid(), signal.SIGTERM); return r
os.link = link_then_kill; stop.clear()
c, dg, e = m.publish_commit(d + "/p3.commit.json", {"label": "p3"}, True, stop)
os.link = real_link
out["during_publication"] = (c["qualified"], c["stop_signal_at_commit"], stop.get("signal"))
stop.clear(); stop["signal"] = "SIGTERM"
c, dg, e = m.publish_commit(d + "/p4.commit.json", {"label": "p4"}, True, stop)
out["latched_before"] = (c["qualified"], c["stop_signal_at_commit"])
t = threading.Thread(target=time.sleep, args=(2,), daemon=True); t.start(); stop.clear()
c, dg, e = m.publish_commit(d + "/p5.commit.json", {"label": "p5"}, True, stop)
out["other_thread"] = (c["qualified"], c["driver_threads_at_commit"])
print(json.dumps(out))
