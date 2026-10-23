"""Hash-check recovered evidence and start an honest continuation report."""
import hashlib
import json
from pathlib import Path
import tarfile


Path("historical").mkdir(exist_ok=True)
for name in ("REPORT.md", "claims.json", "results/final-verification.json",
             "results/claims-validation.json", "results/delivery.json"):
    p = Path(name)
    if p.exists():
        dest = Path("historical") / (p.name + ".epoch1")
        if not dest.exists():
            dest.write_bytes(p.read_bytes())
manifest = json.loads(Path("selection-inputs/epoch1-small-evidence/MANIFEST.json").read_text())
arc = Path("selection-inputs/epoch1-small-evidence/omitted-small-files.tar.gz")
assert hashlib.sha256(arc.read_bytes()).hexdigest() == manifest["archive_sha256"]
files = {r["path"]: r for r in manifest["files"]}
restored = []
with tarfile.open(arc) as archive:
    for member in archive.getmembers():
        name = member.name
        assert not Path(name).is_absolute() and ".." not in Path(name).parts
        data = archive.extractfile(member).read()
        rec = files[name]
        assert len(data) == rec["bytes"]
        assert hashlib.sha256(data).hexdigest() == rec["sha256"]
        p = Path(name)
        if not p.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
            restored.append(name)
Path("results/recovery-audit.json").write_text(json.dumps({
    "archive_sha256": manifest["archive_sha256"],
    "verified_members": len(files), "restored": restored,
}, indent=2) + "\n")
claims = {
    "outcome": "partial",
    "summary": "The headline existence question is unresolved. A self-contained proof gives global balanced maximum in {240,242}, and rules out degree at most seven. Recovered computations await fresh replay. Missing large certificates are not claimed. Novelty is unknown.",
    "claims": [{
        "cid": "elementary-balanced-bounds", "type": "theorem", "scope": "sub-question",
        "statement": "The maximum balanced nonlinearity on nine variables is either 240 or 242. Every balanced function of degree at most seven has nonlinearity at most 240, with equality for x0+x1*x2+x3*x4+x5*x6+x7*x8. Any target has degree exactly eight and nonzero support XOR. The global upper bound uses a separate nonzero-support-XOR case and is independent of the cited unrefereed covering-radius claim.",
        "evidence": ["degree-bound-proof.md", "results/baseline240.json", "code/baseline.py", "code/check_witness.py"],
        "verify_command": "python3 code/baseline.py --compare",
        "check_command": "python3 code/check_witness.py results/baseline240.json --min-nl 240 --expect-degree 2 --xor-zero",
        "control_command": "python3 code/check_witness.py results/baseline240-broken.json --min-nl 240",
    }],
    "next_step": "First independently replay compact recovered exclusions, then use degree-eight/support-XOR necessary conditions in a bounded search. Missing certificates and timeouts imply no exclusion.",
}
tmp = Path("claims.json.tmp")
tmp.write_text(json.dumps(claims, indent=2) + "\n")
tmp.replace("claims.json")
Path("REPORT.md").write_text("""# Balanced nine-variable nonlinearity: continuation

Outcome: partial. The headline existence question remains unresolved. No balanced nonlinearity-242 witness or global nonexistence proof is supplied. Novelty is unknown.

Continuation started 2026-10-15 21:23:54 UTC. Deliverables due by 23:44:54 UTC (minute 141); hard stop 2026-10-16 00:09:54 UTC (minute 166). Only this directory is authorized. No network, delegation, installation, or locally compiled executable is used.

## Current verified mathematical result

The self-contained `degree-bound-proof.md` proves that the global balanced maximum is in {240,242}. It proves maximum 240 for algebraic degree at most seven and requires degree exactly eight/nonzero support XOR for a 242 target. The global upper bound uses its separate nonzero-support-XOR argument. This does not settle which endpoint is attained.

The explicit quadratic table passed both the FWHT reproduction and independent direct-character check: weight 256, nonlinearity 240, algebraic degree 2, support XOR 0.

## Recovery and current limitations

The previous report and claims were copied to `historical/`; they are historical assertions, not current claims. Every recovered archive member was checked against the staged hash manifest before extraction. Compact radius-two/four, flat, and two-coset artifacts are recovered and awaiting fresh replay. Large radius-six certificates and eleven quarter-class proofs are unavailable. Their prior claims are withdrawn unless independently re-established within delivery limits.

The staged literature is untrusted input. Its 2026 Section 6 explicitly leaves balanced attainment of 242 open. The 2024 full text is not staged; its reported baseline cannot be independently rechecked here. No online literature verification is possible. The 2026 unrestricted upper-bound claim is not assumed.

## Remaining gap and next step

Either an indexed 512-bit table of weight 256 with all 512 Walsh magnitudes at most 28, or a complete global nonexistence proof, remains required. First complete compact replays and controls, then undertake a bounded new search if time permits.
""")
print("Verified archive members", len(files), "restored", len(restored))
print("Early report and atomic claims update complete.")
