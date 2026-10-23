# Tan–Zhou §4(3): parent verdict

Recorded after the 2026-10-17 23:50:52 PDT evidence-binding check.

**GATE MET — math-1.** Explicit certificates establish both objects requested in Tan–Zhou arXiv:2503.11934v1 §4(3):

1. A **gcDCQS(18⁴:2)**.
2. An **FDGDD(3,4,5{18})** in the source's own definition.

An explicit **mcDSQS(74)** is independently verified. Importing Tan–Zhou Constructions 2.1 and 2.3, Lemma 3.8 and the published mcDSQS(20) input gives the written consequence

\[
\operatorname{mcDSQS}(18\cdot4^t+2)\quad\text{exists for every integer }t\ge1.
\]

The finite objects are checked directly; higher orders are a reviewed consequence of the stated imports, not generated certificates or a Lean formalization. Priority is **NONE-FOUND-IN-SCOPE**, novelty **UNCLEAR**. The finite objects are a modest specialist extension; the resulting family is potentially substantive specialist work, not an established major result. No human peer review or publication.

## Frozen question and exact scope

[Slot contract](../screening/math-1-tz43-contract.json), SHA-256 `cfafe572e7ba1a2feaaa4224b3ab562d501295c0b07f0df9d8095ed3f9946a17`.

Primary source: Tan–Zhou arXiv:2503.11934v1, local text SHA-256 `df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164`, LF1114–1116. It requests a gcDCQS(18⁴:2) **and one of** FDGDD/RDGDD(3,4,5{18}). Both reviewers confirmed this interpretation and the unchanged quantifiers. We supply the FDGDD alternative; **no RDGDD is claimed**.

The secondary label “FDH(5,18,4,3)” appears in the lane and priority search. The original FDH definition was not supplied to both bridge reviewers. This verdict uses only the source's FDGDD definition; the alias is not an additional accepted premise or nomenclature claim.

## Pinned certificates

Files below are in [the verifier snapshot](tz43-verifier-inputs-v1/manifest.json).

| Object | SHA-256 | Directly checked structure |
|---|---|---|
| gcDCQS(18⁴:2) | `1382d572f8024c9b93ff6f5cf8aff942a9538119e8462ba54b02b6f160da282e` | 74 points; 2 stems; four groups of18; 15,066 blocks; all60,264 allowed triples covered once and all4,560 forbidden triples absent |
| FDGDD(3,4,5{18}) | `3e22f5021631ac82ea5b5fa6f884984bb874f1f9a384fd35bfeff523e731a998` | 90 points; five groups of18; 14,580 transverse blocks; all58,320 transverse triples covered once |
| mcDSQS(74), ASCII-v2 | `1122f1f49eb61e03c44b0686fc773a912b24039936697fe13e4488af34a8eb4c` | 16,206 blocks; all64,824 triples covered once; every one of74 derived STS(73)s has37 PPCs |

At each of the72 group points of the gcDCQS, the derivative is an STS(73,19), hole `(G∪S)\{x}`, with819 triples partitioned into37 partial parallel classes, exactly10 avoiding the hole. At each stem point it is a KF(18⁴), with36 classes, nine missing each group.

At each of the90 FDGDD points, the derivative on the other four groups is a KF(18⁴):648 triples and36 classes, nine missing each other group. Each frame class partitions exactly54 points into18 triples. These are definition checks, not symmetry assumptions.

For mcDSQS74, each derived STS(73) has876 triples and a partial parallel class has at most24 triples. Thus at least ceil(876/24)=37 colours are necessary; the37-colour certificates attain that bound. The weaker point-degree bound36 is not the optimality argument.

## Verification and reproducibility

### Parent definition-first checks

- gcDCQS: [report](gcdcqs18-parent-check-v1/report.md), [result](gcdcqs18-parent-check-v1/result.json), SHA-256 `220a06a81bfbac66232231fbd4faf1fe0db67a3083632804f88ec774f08d5b2b`. Strict parsing, exact triple-universe equality, all group-point colourings and both stem frames pass. Thirteen retained mutation fixtures reject for intended reasons under normal and optimized Python.
- FDGDD: [report](tz43-fdgdd18-parent-v1/report.md), [result](tz43-fdgdd18-parent-v1/result.json), SHA-256 `3197db9c6907fa191effc9f5df27bb75c006686e1e08af52e3c07f96f80f243f`. Twenty-two conditions pass. Fifteen retained fixtures reject for intended reasons in four Python/version-mode combinations:60/60 rejections. This checker read no lane code.
- mcDSQS74: the unchanged parent checker `check_mcdsqs_independent.py`, SHA-256 `ca74181eb7524c23aad002b0d913c74a03284ae96e97684aad5487ac83d78630`, directly accepts the pinned ASCII-v2 raw file ([receipt](mcdsqs74-ascii-parent-direct-v1.json), SHA-256 `236c3654cb1af526e16f7dfe1c6109ef0043b4f6cd370a24d6b2f02910e6cdb7`). Earlier parent controls used an explicitly hash-bound comment-free projection: eight fixtures reject in both modes.

### Two further separately authored implementations

- **Codex CLI gpt-6.1-sol:** its own in-memory verifier returns **RESULT: VALID for all three objects** ([note](tz43-codex-verify-v1.note.md), SHA-256 `3eca4a737b2fddc434f1164c658ec4f5ff3b718e94b54a9fb419c781f9ffacd7`). It rederived all expected counts and rejected three targeted corruptions per object, nine total, then reaccepted the originals.
- **Claude CLI claude-opus-5-5:** authored a prompt-only checker which the parent-side desk inspected and executed ([checker](tz43-claude-verifier-v1/checker.py), SHA-256 `2b2a7f19362b263c25721e7cb1db4ba3231cbcd7f68d636a624cf00b26bddd10`). [Result](tz43-claude-verifier-v1/result.json), SHA-256 `6393b7523a0991e2aa21a78d80882517d45b316d187b4d8426de4df6a6c86d7a`: **108/108 expected outcomes**, eight positive executions and100 rejections. Normal and optimized outputs are byte-identical. Positives include all three pins and the parent comment-free mcDSQS74 projection; rejections include the36 parent fixtures and14 argument controls, each in both modes.
- [Desk summary](tz43-verifier-desk-v1/summary.json) binds models, prompts, input pins, checker scans and every outcome. These are independent implementations of a shared quoted definition/format packet, not independent readings of the whole paper. The separate bridge audits address source semantics.

### Seed/action replay and construction explanation

- **gcDCQS parent replay:** [result](gcdcqs18-parent-check-v1/seed-replay/result.json), SHA-256 `e3d367163f71e0fba26c03e4c6805ca189b59c8f6aba933a0fa61902e4e2128b`. Own GF(9) arithmetic reconstructs the288-element group;65 seed blocks expand to precisely15,066 certificate blocks with orbit profile44×288,13×144,7×72,1×18. The point-0 colouring transports to all72 group points; both stem frames also match. Wrong stem action is rejected for block-invariance failure, including1,296 affected stem blocks. No lane code was imported. Equality is exact set/multiset equality, not a claim of byte-identical serialization by this parent route.
- **FDGDD parent replay:** from the pinned540-block bare H(5,6,4,3) master and zero-sum RDTD(3,4,3), independently re-expanded all14,580 blocks. Exact multiset equality: zero missing and zero extra. Frame partitions are checked directly at all90 points, not inferred from the master.
- **Important construction distinction:** the chosen size6 master is not used as a frame-derived design. Blocks are inflated first; the new Kirkman frames are found on the inflated size18 design. No theorem requiring an FDGDD of group size6 is invoked. The worker's exact diagnosis of that master is not promoted as a general size6 nonexistence theorem.
- Worker receipts separately retain byte-identical SAT/producer replays and solver-free expansions. Those are reproduction evidence, not additional independent checkers.

## Both-CLI mathematical bridge reviews

| Reviewer | Disposition | Scope of findings |
|---|---|---|
| Codex gpt-6.1-sol | ACCEPT | 0 FATAL;1 MAJOR on an unused exploration lemma;3 MINOR in lane wording/nomenclature |
| Claude claude-opus-5-5, v2 | ACCEPT | 0 FATAL/MAJOR;7 MINOR on historical status, conditional wording, an unchecked alias and a source-extraction typo |

[Codex note](tz43-bridge-codex-review-v1.note.md), SHA-256 `8f5afa7e59d0ea603e22f829c141da2ee1deab0ae92020a9098b355db74f0c48`; [Claude note](tz43-bridge-claude-review-v2.note.md), SHA-256 `392a5b4743bc68e1a2e7724d0665e89fb349d847dc6d04b8af49d4596d2f371e`.

**All findings are disposed in the [dated parent correction](tz43-parent-review-dispositions-v1.md).** The unused Lemma-R TD(4,6) import is not relied upon; its odd-m exclusions follow from the Kirkman-frame degree count instead. Fixed-set and dihedral-label errors are historical search explanations, not witness premises. Frozen notes remain unchanged, with their historical statements superseded at parent integration.

Claude v1 timed out at2400 seconds and produced no verdict; v2 is the successful shorter packet. That packet omitted the full Construction2.3 proof. Codex read it, and the parent read LF444–541 directly after the review. The universal family is explicitly an application of the published theorem, not a claim that both reviewers independently re-proved every cited source.

## Infinite family: exact import chain

For integer t≥2:

1. **Import Lemma3.8**, which supplies an RDS(3,5,4^t+1); only its underlying Steiner3-design is needed here. The original Witt/Zhou–Chang proofs are not re-proved.
2. Delete one point. Blocks through it become4-blocks forming S(2,4,4^t); the remaining5-blocks plus those4-blocks cover triples once. With singleton groups this is a1-FG(3,({4},{5}),4^t) of type1^(4^t).
3. **Apply Construction2.3** with `(m,g,n,s)=(18,1,4^t,2)`. The certified gcDCQS(18⁴:2) fills the4-blocks and the certified FDGDD(3,4,5{18}) fills the5-blocks, yielding gcDCQS(18^(4^t):2). The FDGDD is not substituted into Construction2.2, which requires RDGDD.
4. **Apply Construction2.1**, using the published mcDSQS(20) as both mcDSQS(20) and gcDSQS(20,2), to obtain mcDSQS(18·4^t+2). For a designated two-point hole, the other stem point has degree9 in10 PPCs and hence is missed by exactly one, verifying the needed gcDSQS(20,2) condition.

The t=1 case is the directly checked mcDSQS74. Formula(1.1), Constructions2.1/2.3, Lemma3.8 and the mcDSQS20 input remain explicit imports. Higher orders are not finite replay claims. There is no unrestricted all-admissible-order mcDSQS theorem here.

## Primary-source comparison and significance

[Post-result priority screen](tz43-priority-scout-v1.md), SHA-256 `25c7d8fc4b3f6bbba9f31288991c309f8371df247dc3a728e7a58c8d1e9f3e37`: **NONE-FOUND-IN-SCOPE** for either finite ingredient, mcDSQS74 or the18·4^t+2 family. The screen checked equivalent-object terminology, forward citations, recent arXiv/DataCite/OpenAlex entries and Zenodo creator families.

- The original source explicitly asks for the two ingredients. Their combination closes that positive construction request, with no symmetry restriction in verification.
- Plain H(5,6,4,3) and H(5,18,4,3) existence is classical; it does not supply the newly required derived Kirkman frames. Zero-sum inflation and prescribed-automorphism search are established methods, not new methods claimed here.
- Main access hole: Chang–Zheng–Zhou2019 pp.1416–1431; only the first-page preview was read. Chang–Zhou2013, Xu–Ji2021/22/24 and Tan–Zhou's journal §4 remain incompletely accessible. Zenodo coverage is metadata-only. No priority claim follows from their absence in the search.
- The finite objects are a modest specialist contribution. The imported infinite-family consequence could be substantively useful within this design problem. No broader or major-science claim is established.

## Raw-format and procedural limits

The original mcDSQS74 raw file `eaff77fc…16c3` contains a non-ASCII union sign in a comment and fails the unchanged ASCII grammar. It is preserved as a format rejection. The accepted ASCII-v2 file has the same noncomment records and a distinct SHA. Neither the parser nor the old evidence was overwritten.

Failed extraction/control/launch attempts, corrected time labels, default compiler temporary output, review timeouts and the parent checkpoint gap remain recorded in [checkpoints](../checkpoints.md), the [outcome ledger](../outcomes.md) and individual desk receipts. Rejected, UNKNOWN and restricted-search outcomes are not certificates. No formal theorem, human review, commit or publication is implied.


## Dated constructive-frame addendum — 2026-10-18T01:11:53-07:00

A supplementary [parent-accepted tripling construction](tz43-tripling-parent-verdict.md) replaces only the FDGDD frame-SAT step. Its new certificate has identical block bytes and three separately authored checking implementations; the original accepted witness is unchanged. The master remains SAT-derived. This is no new gate or novelty claim.
