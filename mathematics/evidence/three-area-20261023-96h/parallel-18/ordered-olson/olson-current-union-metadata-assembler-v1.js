const base = "/Users/jinleic/repos/aifours/";
const own = "mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/";
const run = "institute/runs/three-area-2026-10-23-96h/";
const primary = await Bun.file(base + own + "olson-current-union-metadata-extraction-v1.json").json();
const supplement = await Bun.file(base + own + "olson-current-union-antecedent-metadata-extraction-v1.json").json();
const classification = await Bun.file(base + own + "olson-current-union-metadata-classification-v1.json").json();
const sources = primary.inputs.map((item, index) => ({
  id: classification.completed_source_roles[index][0],
  ...item,
  role: classification.completed_source_roles[index][1],
  scope_boundary: classification.completed_source_roles[index][2],
  coverage_kind: "CURRENT_BYTE_METADATA_ONLY_NOT_NEW_PROOF_READ",
  future_entire_input_range: item.supplied_range,
  input_kind: index < 19 ? "COMPLETED_WRITTEN_SOURCE" : "HISTORICAL_SELECTION_OR_SOURCE_QUALIFICATION"
}));
const extraIds = [
  "P_CYCLE", "P_GRAD", "P_SECOND", "P_SEPARATED", "P_GAP", "P_DB", "P_Z1", "P_LMAX",
  "RECEIPT_GAP", "RECEIPT_SEPARATED", "TA_UNION_PROPOSAL", "SCOPE_ERRATUM", "ARITHMETIC_ERRATUM",
  "L_MAX_PARK", "L_MAX_RECEIPT", "CRITICAL_RECEIPT", "REVIEW_GAP", "REVIEW_CYCLE",
  "BASELINE", "UNIFORM_PARTIAL", "OLD_UNIFORM_PARENT", "RESID_AUDIT", "THEOREM_P", "OLD_P_PARENT", "OLD_EXP", "OLD_REFLHI"
];
for (let index = 0; index < supplement.inputs.length; index++) {
  const id = extraIds[index];
  const role = id.startsWith("P_") || id.includes("RECEIPT") || id.startsWith("REVIEW_") || id.endsWith("PARENT")
    ? "SCOPED_HISTORICAL_REVIEW_PARENT_OR_RECEIPT_NOT_NEW_ACCEPTANCE"
    : id.includes("ERRATUM") || id === "L_MAX_PARK" ? "MANDATORY_CORRECTION_OR_FAILED_ROUTE_SCOPE"
    : id === "TA_UNION_PROPOSAL" ? "SEPARATE_COMPOSITION_CANDIDATE_NOT_ADOPTED"
    : "EXISTING_ANTECEDENT_AT_NAMED_HISTORICAL_TRUST_CUT_NOT_NEW_PROOF_RECONSTRUCTION";
  sources.push({ id, ...supplement.inputs[index], role, coverage_kind: "CURRENT_BYTE_METADATA_ONLY_NOT_NEW_PROOF_READ", future_entire_input_range: supplement.inputs[index].supplied_range });
}
const additional = [
  ["REVIEW_GRAD", "information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/peer-review-olson-gradient-run-continuant-v1.md", "SCOPED_HISTORICAL_REVIEW_NOT_NEW_VERDICT_TRANSFER"],
  ["REVIEW_SECOND", "information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/peer-review-olson-second-anchor-v1.md", "SCOPED_HISTORICAL_REVIEW_NOT_NEW_VERDICT_TRANSFER"],
  ["REVIEW_SEPARATED", "information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/peer-review-olson-separated-anchor-v1.md", "SCOPED_HISTORICAL_REVIEW_WITH_V10_CHRONOLOGY_AND_FROZEN_HREF_QUALIFICATION"],
  ["ERRATUM_V9", run + "parent-evidence-erratum-v9.md", "MANDATORY_PROCESS_IMPORT_AND_FREEZE_CORRECTION"],
  ["ERRATUM_V10", run + "parent-evidence-erratum-v10.md", "MANDATORY_OLDER_OLSON_READ_ORDER_AND_FROZEN_HREF_CORRECTION"],
  ["ERRATUM_V11", run + "parent-evidence-erratum-v11.md", "MANDATORY_CLOCK_AND_ASSURANCE_CORRECTION"],
  ["HOLD_V2", run + "scientific-admission-hold-v2.json", "MANDATORY_NO_SCIENTIFIC_ADMISSION"],
  ["AUTHORITY_170", run + "Olson-post154-full-cadence-and-current-union-metadata-only-v170.json", "CURRENT_METADATA_ONLY_AUTHORITY_NOT_PRIMARY_PROOF_PERMISSION"],
  ["OUTPUT_ERRATUM_150", run + "Olson154-comparison-control-and-Sun150b-newcount-qualified-reviews-v150.json", "MANDATORY_OLD626_HELD_NEW589_OUTPUT_AND_PROCESS_QUALIFICATION"],
  ["AUTHOR_CORRECTION_135", run + "Olson-v154-old-v122-NL-not-Werner-author-qualification-v135.json", "MANDATORY_OLD_NL_AUTHOR_NOT_WERNER_MIN0R"],
  ["PARENT_CADENCES_138", run + "parent-checkpoint103-104-105-two-cadence-findings-v138.json", "MANDATORY_TWO_LATER_PARENT_CADENCE_FINDINGS"],
  ["WHOLE_ACK_POST154", own + "primary-resumption-after-v154-ack-v1.json", "COMPLETE_EXISTING_STATE_EXPOSURE_AND_POSTRETURN_CADENCE_METADATA_ONLY"],
  ["HELD_C889", own + "primary-before-v117-opaque-review-v1.json", "HELD_METADATA_NONINPUT_NO_FORMULA_SERIALIZATION"],
  ["PRIOR_CURRENT_PARK8", own + "park-v8.json", "HISTORICAL_PARKABLE_STATE_NOT_ROUND_COMPLETION"],
  ["RESUME_METADATA", own + "primary-resumption-after-v112-ack-v1.json", "HISTORICAL_AUTHORITY_EXPOSURE_METADATA_NOT_NEW_PERMISSION"],
  ["CHECKPOINT_V3_METADATA", own + "primary-after-v112-arc-defect-checkpoint-v1.json", "ALREADY_COMPLETED_V3_CLAIM_METADATA_NOT_NEW_PROOF_OR_HELD_LEAD_INPUT"]
];
for (const [id, path, role] of additional) {
  const bytes = new Uint8Array(await Bun.file(base + path).arrayBuffer());
  const text = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  const rows = text.split("\n");
  const lf = rows.length - 1;
  if (rows.at(-1) === "") rows.pop();
  sources.push({ id, path, role, sha256: new Bun.CryptoHasher("sha256").update(bytes).digest("hex"), bytes: bytes.length, lf_newlines: lf, logical_lines: rows.length, future_entire_input_range: [1, rows.length], coverage_kind: "CURRENT_BYTE_HASH_LF_ONLY_NO_FRESH_PROOF_BODY" });
}
const ordinary = { id: "ORDINARY_GROUP_FIELD_BOX", role: "NAMED_ORDINARY_BACKGROUND_NOT_NEW_FORMAL_OR_NOVELTY_ACCEPTANCE", description: classification.ordinary_group_background };
const nodes = [];
for (const source of sources.filter(item => /^F\d+$/.test(item.id))) {
  const inputs = [source.id, ...(classification.source_dependencies_by_ID[source.id] || []), ordinary.id];
  for (const heading of source.headings || []) nodes.push({ id: source.id + ":SECTION" + heading.line, kind: "SOURCE_SECTION_CLAIM_OR_SCOPE_NODE", source_id: source.id, range: [heading.line, heading.end_line], title: heading.title, required_complete_source_range: source.future_entire_input_range, requires_snapshot_inputs: inputs, assurance: "ARCHIVAL_CLAIM_SCOPE_MAPPING_ONLY_NOT_NEW_PROOF_OR_ACCEPTANCE" });
  for (const label of source.labels || []) {
    const section = (source.headings || []).filter(item => item.line <= label.line && item.end_line >= label.line).sort((a, b) => b.depth - a.depth)[0];
    nodes.push({ id: source.id + ":LABEL" + label.line, kind: "NATIVE_BOLD_CLAIM_LABEL", source_id: source.id, range: [label.line, section ? section.end_line : source.logical_lines], native_label: label.label, containing_section: section ? source.id + ":SECTION" + section.line : null, required_complete_source_range: source.future_entire_input_range, requires_snapshot_inputs: inputs, assurance: "LABEL_AND_RANGE_METADATA_ONLY_NOT_NEW_PROOF_OR_ACCEPTANCE" });
  }
  const text = await Bun.file(base + source.path).text();
  const tokens = [];
  for (const [index, row] of text.split("\n").entries()) {
    for (const match of row.matchAll(/\(([A-Z][A-Z0-9_-]{1,23})\)/g)) tokens.push({ line: index + 1, token: match[1] });
  }
  source.parenthesized_native_ID_tokens = tokens;
  source.native_ID_token_boundary = "Equation/status/claim token metadata ONLY; tokens are not automatically theorems or accepted claims. All structural claims/labels have full-source required coverage above.";
}
const knownIds = new Set([...sources.map(item => item.id), ordinary.id, ...nodes.map(item => item.id)]);
const dangling = [];
for (const node of nodes) for (const id of node.requires_snapshot_inputs) if (!knownIds.has(id)) dangling.push({ from: node.id, missing: id });
for (const branch of classification.whole_branches) {
  for (const id of [branch.root, ...(branch.roots || []), ...(branch.inputs || [])].filter(Boolean)) if (!knownIds.has(id)) dangling.push({ branch: branch.id, missing: id });
}
const file = own + "olson-completed-current-source-claim-whole-branch-DAG-v1.json";
const map = {
  kind: "IMMUTABLE_CURRENT_COMPLETED_WRITTEN_SOURCE_CLAIM_WHOLE_BRANCH_METADATA_MAP",
  authority: classification.authority,
  authority_sha256: classification.authority_sha256,
  permission_observation: classification.actual_permission_observation,
  original_primary_stop: "112/125 SOURCE-PROOF-REHEARSAL-METHOD STOP UNCHANGED;170 authorizes metadata ONLY",
  scope: classification.policy,
  primary_roots: classification.primary_roots,
  literal_original_constraints: classification.literal_original_constraints,
  sources,
  individual_claim_section_nodes: nodes,
  whole_branch_roots: classification.whole_branches,
  correctness_DAG_shape: "BRANCH ROOTS→INDIVIDUAL SOURCE-BOUND CLAIM/SECTION NODES→COMPLETE SOURCE SNAPSHOTS + DECLARED ANTECEDENT SNAPSHOTS + NAMED ORDINARY/NR INPUTS. No theorem is derived by this metadata program. Citation backreferences below are NOT proof premises or circularity acceptance.",
  source_citation_edges_NOT_mathematical_DAG: classification.source_dependencies_by_ID,
  citation_edge_boundary: classification.dependency_edge_meaning,
  ordinary_inputs: ordinary,
  named_NR_boundaries: classification.named_NR_boundaries,
  held_leads: classification.held_metadata_noninputs,
  source_count_qualification: { path: run + "wave-v19-olson-park-parent-v1.md", current_actual_LF: 11, current_sha256: "aeca6d53012f3167cb05ca669b9fa6ab0ab89a07c8ee18fab81101f6e6db364b", historical_own_inventory_claim: "19LF", correction: "Current byte-only map uses11; earlier raw ranges reaching actual ending do not establish nonexistent12-19. Preserve old records; no backdated read/count/source-drift/math-falsity inference or rerun of a reported failed check." },
  unrelated_parent_side_records: "P_GAP receipt also contains Sun Q4/R4 source/review metadata. Those are unrelated co-disposition bookkeeping, NOT Olson correctness inputs or a Sun theorem import.",
  metadata_ID_validation: { dangling_metadata_IDs: dangling, boundary: "BYTE/FIELD/ID LINK VALIDATION ONLY; not group/arithmetic/inequality/rank/control/proof verification" },
  history: classification.history,
  handoff_boundary: classification.handoff_boundary,
  execution_artifacts: [own + "olson-current-union-metadata-extractor-v1.js", own + "olson-current-union-antecedent-metadata-extractor-v1.js", own + "olson-current-union-metadata-assembler-v1.js", own + "olson-current-union-metadata-classification-v1.json", own + "olson-current-union-metadata-extraction-v1.json", own + "olson-current-union-antecedent-metadata-extraction-v1.json"],
  nonclaims: "No new mathematical proof/serialization of held proofs, original route planning/source fetch, source proof reread/reassessment/adoption, scientific program/control calculation/enum/replay, formal/human/configured-family/executable/novelty acceptance or original all-prime completion. Full paths/hashes/LF ranges/roles are metadata."
};
await Bun.write(base + file, JSON.stringify(map, null, 2) + "\n");
export default { artifact: file, source_snapshots: sources.length, individual_metadata_nodes: nodes.length, whole_branch_roots: classification.whole_branches.length, dangling_metadata_IDs: dangling, status: "METADATA_MAP_WRITTEN_NOT_MATHEMATICAL_VERIFICATION" };
