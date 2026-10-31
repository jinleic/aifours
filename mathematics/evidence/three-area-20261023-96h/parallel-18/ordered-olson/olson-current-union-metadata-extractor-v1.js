const root = "/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/";
const names = [
  "consolidated-ACTUAL-ARC-DEFECT-AND-CARDINALITY-v3.md",
  "consolidated-ACTUAL-ARC-CONTRAST-AND-VALUE-RIGIDITY-v2.md",
  "consolidated-SATURATED-ACTUAL-ARC-COUPLING-v1.md",
  "consolidated-CYCLIC-SEPARATOR-CHARACTER-SELECTORS-v1.md",
  "consolidated-FULL-CYCLE-STATUS-AND-PARITY-SELECTORS-v1.md",
  "consolidated-SIMULTANEOUS-GRADIENT-RUN-CONTINUANT-v1.md",
  "consolidated-SECOND-ANCHOR-COUPLING-DISCRIMINATION-v1.md",
  "consolidated-SEPARATED-ANCHOR-MIXED-TERM-v1.md",
  "consolidated-UNRESTRICTED-BANDS-GAP-BOX-v1.md",
  "proof-MAXIMAL-REFLECTION-TRANSPORT-CONTROLS-v1.md",
  "proof-FIXED-ROTATION-DOUBLE-BOX-BAND-CLOSURE-v1.md",
  "proof-CRITICAL-BRANCH-MIX-CLOSURE-v1.md",
  "proof-DISPERSED-IDENTITY-PAIR-v1.md",
  "proof-CRITICAL-MATCHING-FREE-ROTATION-RIGIDITY-v1.md",
  "proof-TWO-FREE-ROTATION-CONTROLS-v1.md",
  "proof-DEEPER-SWITCH-CLASSIFICATION-v1.md",
  "proof-GAUGE-SWITCH-AND-CRITICAL-LADDER-v1.md",
  "consolidated-lower-band-v1.md",
  "obstruction-MAXIMUM-MATCHING-PACKET-LIFT-v1.md",
  "selection-lower-matching-packet-lift-v1.md",
  "selection-critical-branch-v1.md",
  "selection-addendum-1-gauge-and-prior-arcs.md",
  "selection-v1.md"
];
const output = [];
for (const name of names) {
  const bytes = new Uint8Array(await Bun.file(root + name).arrayBuffer());
  const text = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  const rows = text.split("\n");
  const newlineCount = rows.length - 1;
  if (rows.at(-1) === "") rows.pop();
  const headings = [];
  const labels = [];
  const references = [];
  const pins = [];
  for (let index = 0; index < rows.length; index++) {
    const line = rows[index];
    const heading = /^(#{1,6})\s+(.+)$/.exec(line);
    if (heading) headings.push({ line: index + 1, depth: heading[1].length, title: heading[2] });
    for (const match of line.matchAll(/\*\*((?:Theorem|Lemma|Corollary|Proposition|Claim|Criterion|Conclusion|Identity|Result|Scope|Status)[^*\r\n]*)\*\*/gi)) {
      labels.push({ line: index + 1, label: match[1] });
    }
    for (const match of line.matchAll(/`([^`\r\n]+\.(?:md|json|pdf)(?:#[^`\r\n]*)?)`/g)) {
      references.push({ line: index + 1, reference: match[1] });
    }
    for (const match of line.matchAll(/\b[0-9a-f]{64}\b/gi)) pins.push({ line: index + 1, sha256: match[0].toLowerCase() });
  }
  for (let index = 0; index < headings.length; index++) {
    const next = headings.slice(index + 1).find(item => item.depth <= headings[index].depth);
    headings[index].end_line = next ? next.line - 1 : rows.length;
  }
  output.push({
    path: "mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/" + name,
    bytes: bytes.length,
    sha256: new Bun.CryptoHasher("sha256").update(bytes).digest("hex"),
    lf_newlines: newlineCount,
    logical_lines: rows.length,
    supplied_range: [1, rows.length],
    headings,
    labels,
    references,
    declared_pins: pins
  });
}
const artifact = root + "olson-current-union-metadata-extraction-v1.json";
await Bun.write(artifact, JSON.stringify({
  kind: "BYTE_FILENAME_HEADING_LABEL_REFERENCE_HASH_LF_METADATA_ONLY",
  authority: "Olson-post154-full-cadence-and-current-union-metadata-only-v170.json",
  permission_observation: "Mon Oct 26 17:34:27 PDT 2026",
  nonclaim: "No mathematics, group/arithmetic/inequality/rank or control evaluation; no source proof is reconstructed. Headings/labels/reference strings are archival metadata, not current acceptance or dependency classification. Held c889 leads are not correctness inputs.",
  inputs: output
}, null, 2) + "\n");
console.log(JSON.stringify({ artifact, inputs: names.length, status: "METADATA_EXTRACTION_COMPLETE" }));
