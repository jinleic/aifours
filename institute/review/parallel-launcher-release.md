**REJECT**

One concrete defect remains:

- **P2 — Blocking cleanup still delays lanes that become due during teardown.** The supervisor classifies expiration using one `now` snapshot, then calls blocking cleanup. [run_parallel.py:320](/Users/jinleic/repos/aifours/institute/run_parallel.py:320) Because each fork receives a distinct deadline, the earliest lane can enter cleanup just before its siblings become due. A stubborn first lane can consume the full grace period while those siblings remain unsignaled; its subsequent kill and sweep can push their termination past their ceilings. [stop_lane:393](/Users/jinleic/repos/aifours/institute/run_parallel.py:393) Deadline supervision must continue while cleanup waits. The new regression covers siblings that finish during cleanup, rather than this remaining case. [test_parallel.py:339](/Users/jinleic/repos/aifours/institute/tests/test_parallel.py:339)

The other requested behavior is closed by inspection:

- **Replay publication:** the worker wrapper publishes PID/start identity before forwarding `on_start`, including calls from `engine.sandboxed`. Exit refresh and cleanup retain and sweep published executors after worker death. [publication:189](/Users/jinleic/repos/aifours/institute/run_parallel.py:189), [exit refresh:360](/Users/jinleic/repos/aifours/institute/run_parallel.py:360), [dead-worker sweep:401](/Users/jinleic/repos/aifours/institute/run_parallel.py:401). The replay regression asserts that the published process is dead afterward. [test:329](/Users/jinleic/repos/aifours/institute/tests/test_parallel.py:329)
- **Completed-sibling classification:** current `is_alive()` replaces the stale ready list, and deadline handling preserves successful `done` reports. [run_parallel.py:323](/Users/jinleic/repos/aifours/institute/run_parallel.py:323)

The pre-existing Popen-before-on_start window and SIGKILL of every lock holder remain separate exclusions.

Static review only; no tests or application code were executed, and no files were changed.