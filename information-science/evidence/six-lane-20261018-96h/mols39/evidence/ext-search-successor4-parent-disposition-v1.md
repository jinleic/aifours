# Beta successor4 parent repair disposition

Recorded at 2026-10-19T10:40:15-0700. SOURCE-ONLY, CANDIDATE_UNVERIFIED. No source imports, compilation, tests, preparation, controls, calibration or search. GlobalruntimeHOLDunchanged.

## N1 (MAJOR), review aba8c5c3

Base: successor3 plan06bee9f7. Review: RUN/review/mols39-beta-successor3-admission_gate-codex-v1.prompt.stdout.txt, SHA256 aba8c5c3fcbaf7c4e320d9680cc530f687d349b9767e9fa35d1f74abc07f627c.

A caught buffered stdout OSError could return2 while leaving pending bytes; sys.exit(2) could flush them after the producer deadline and still produce an intended-looking rejection. New ext4_beta.py terminates that error branch with os._exit(5 if the freshly observed deadline is expired else2). The producer has already completed its existing file/publication attempts; this path does not reflush, append, rewrite, or claim partialcapture asvalid. Allnormalreturns unchanged.

Old:
```python
    except OSError:
        if deadline is not None and time.monotonic()>deadline:return CODES['INCOMPLETE_BUDGET']
        return CODES['IO_ERROR']
```

New:
```python
    except OSError:
        # No interpreter-shutdown retry of pending stdout after this final deadline observation.
        os._exit(CODES['INCOMPLETE_BUDGET'] if deadline is not None and time.monotonic()>deadline else CODES['IO_ERROR'])
```

Only functional algorithm delta is this error branch. Beta Engine4887B/233bd15e and jointtree11171B/020100ee byte-identical. Joint and DATA sources/entrypoints untouched. Gate onlydocstringline2 and beta/gate wrapperconstants repinned; no new generalabstraction or exitacceptance.

## New source and document pins

- /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext4_beta.py: `a319a4be1cc219a2de4c53211ac61cabc42bdc19d000f8bc740c6e4bc262b978`
- /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext4_entry_beta.py: `c6c21b83b3190685b3559c2ae08ba345ab3c931a986026d7fcab586909c656eb`
- /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext4_gate.py: `8d04c5ce7b9fdf3f42c5537bdf32c892b6c1af09e3e31096e41b2506597624fa`
- /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext4_entry_gate.py: `fbbba2306b1e9315313eb27456bf5861c2cb4d6ea7640af930ff25e48d3f50e7`
- /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor4-contract-v3.md: `ad5bb631adbe55511851fa54b0fb684807051436e35a5f4030a59ec674fc5f72`
- /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-integration-v4.md: `8fee3e7be364649d5ba9d6867cb865716e20222db4839dfb7bf64d2c1ee7e9af`
- /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-plan-v5.json: `254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731`
- /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor4-parent-metadata-v3.json: `81e5087369eb80f1f901ac721a76224b1685a04f88ae4e5948241c0ee7371658`

## Verification boundary

Metadata 81e5087369eb80f1f901ac721a76224b1685a04f88ae4e5948241c0ee7371658: all18regularone-linkpins,4algorithm/wrapperbindings,7literalplanv5calls,20jobs/order and2separatecalibrations checked; new outputroots version4 preservepriorroot identities. This is sourceconsistencyonly. Resource/work/storage mathematics unchanged from mathowneracceptancef6fe216e. Gate source re-review stillrequired; real CPython buffered-fault behavior, complete20controls, actualcapture/exit audits and qualifiedsupervisor remain unexercised. ExactanchorLemmaU/R1 unchanged; extensionquestionsUNKNOWN; MOLS39OPEN.
