const base = "/Users/jinleic/repos/aifours/";
const own = "mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/";
const run = "institute/runs/three-area-2026-10-23-96h/";
const paths = [
  run + "olson-cycle-and-arc-selectors-parent-v1.md",
  run + "olson-gradient-run-continuant-parent-v1.md",
  run + "olson-second-anchor-parent-v1.md",
  run + "olson-separated-anchor-parent-v1.md",
  run + "olson-gap-sun-chain-current-parent-v1.md",
  run + "olson-double-box-band-parent-v1.md",
  run + "olson-consolidated-z1-parent-v1.md",
  run + "wave-v19-olson-park-parent-v1.md",
  run + "olson-gap-sun-chain-current-parent-receipt-v1.json",
  run + "olson-separated-anchor-parent-receipt-v1.json",
  own + "ta-singleton-fixed-count-union-audit-proposal-v1.json",
  own + "separated-anchor-scope-erratum-v1.json",
  own + "arithmetic-authority-correction-addendum-v1.json",
  own + "lower-matching-mechanism-PARK-v1.json",
  own + "lower-matching-reviewed-receipt-v1.json",
  own + "critical-branch-reviewed-receipt-v1.json",
  "information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/peer-review-olson-gap-box-bands-v1.md",
  "information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/peer-review-olson-cycle-and-arc-selectors-v1.md",
  "mathematics/evidence/six-lane-20261018-96h/olson/continuations/correct-length-dihedral-followon/STEP0-OWN-BASELINE-v1.md",
  "mathematics/evidence/six-lane-20261018-96h/olson/continuations/correct-length-residual-cover-followon/proof-UNIFORM-RESIDUAL-PARTIAL-v1.md",
  "institute/runs/six-lane-2026-10-18-96h/review/olson-residual-uniform-and-extended-parent-written-check-v1.md",
  "mathematics/evidence/six-lane-20261018-96h/olson/continuations/resid-band-followon-20261022/STEP0-RESID-BAND-AUDIT-v1.md",
  "mathematics/evidence/six-lane-20261016/olson/proof-theoremP.md",
  "institute/runs/six-lane-2026-10-18-96h/review/olson-TheoremP-import-closure-parent-verdict-v1.md",
  "mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-EXP-v2.md",
  "mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v2.md"
];
const records = [];
for (const path of paths) {
  const bytes = new Uint8Array(await Bun.file(base + path).arrayBuffer());
  const text = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  const rows = text.split("\n");
  const lf = rows.length - 1;
  if (rows.at(-1) === "") rows.pop();
  const headings = [];
  const references = [];
  const pins = [];
  for (let index = 0; index < rows.length; index++) {
    const line = rows[index];
    const heading = /^(#{1,6})\s+(.+)$/.exec(line);
    if (heading) headings.push({ line: index + 1, depth: heading[1].length, title: heading[2] });
    for (const match of line.matchAll(/`([^`\r\n]+\.(?:md|json|pdf)(?:#[^`\r\n]*)?)`/g)) references.push({ line: index + 1, reference: match[1] });
    for (const match of line.matchAll(/\b[0-9a-f]{64}\b/gi)) pins.push({ line: index + 1, sha256: match[0].toLowerCase() });
  }
  for (let index = 0; index < headings.length; index++) {
    const next = headings.slice(index + 1).find(item => item.depth <= headings[index].depth);
    headings[index].end_line = next ? next.line - 1 : rows.length;
  }
  records.push({ path, bytes: bytes.length, sha256: new Bun.CryptoHasher("sha256").update(bytes).digest("hex"), lf_newlines: lf, logical_lines: rows.length, supplied_range: [1, rows.length], headings, references, declared_pins: pins, json_top_level_keys: path.endsWith(".json") ? Object.keys(JSON.parse(text)) : undefined });
}
const artifact = own + "olson-current-union-antecedent-metadata-extraction-v1.json";
await Bun.write(base + artifact, JSON.stringify({
  kind: "EXISTING_ANTECEDENT_BYTE_HEADING_REFERENCE_HASH_LF_KEYS_ONLY",
  authority: "Olson-post154-full-cadence-and-current-union-metadata-only-v170.json",
  preceding_observation_bound: "Mon Oct 26 17:36:52 PDT 2026",
  nonclaim: "No source fetch/network/proof reconstruction/control or mathematical evaluation. Supplement reads metadata from named existing frozen antecedents; status/trust/dependencies require the explicit current mapping, not a filename or source hash. Held leads are excluded from correctness inputs.",
  inputs: records
}, null, 2) + "\n");
export default { artifact, inputs: paths.length, status: "SUPPLEMENTAL_METADATA_EXTRACTION_COMPLETE" };
