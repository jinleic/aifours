import KSatUpper
import Lean.Util.CollectAxioms

/-! Audit driver (not part of the proof library).

1. Every constant declared in a `KSatUpper.*` module is inventoried; the axioms reachable from
   all of them are collected with Lean's own `CollectAxioms`, sharing one traversal.
2. The public endpoints are re-checked against their displayed statements by `example`s that
   mention only the model definitions. -/

open Lean Elab Command

run_cmd do
  let env ← getEnv
  let mods := env.header.moduleNames
  let mut roots : Array Name := #[]
  let mut nThm := 0
  let mut nDef := 0
  for (n, ci) in env.constants.map₁.toList do
    if let some idx := env.getModuleIdxFor? n then
      let modName := mods[idx.toNat]!
      if (`KSatUpper).isPrefixOf modName then
        roots := roots.push n
        match ci with
        | .thmInfo _ => nThm := nThm + 1
        | _ => nDef := nDef + 1
  let (_, st) := ((roots.forM CollectAxioms.collect).run env).run {}
  let modsK := mods.filter (fun m => (`KSatUpper).isPrefixOf m)
  logInfo m!"AUDIT_MODULES {modsK.size}"
  logInfo m!"AUDIT_CONSTANTS {roots.size} (theorems {nThm}, other {nDef})"
  logInfo m!"AUDIT_AXIOMS {st.axioms.toList}"

#print axioms KSatUpper.satisfiabilityProbability_4SAT_tendsto_zero
#print axioms KSatUpper.satisfiabilityProbability_5SAT_tendsto_zero
#print axioms KSatUpper.satisfiabilityProbability_3SAT_tendsto_zero
#print axioms KSatUpper.satisfiabilityProbability_4SAT_9934_tendsto_zero
#print axioms KSatUpper.satisfiabilityProbability_5SAT_21123_tendsto_zero
#print axioms KSatUpper.satisfiabilityProbability_3SAT_42672_tendsto_zero
#print axioms KSatUpper.satisfiabilityProbability_3SAT_426718_tendsto_zero
#print axioms KSatUpper.CertificatesK3Controls.control_42671_low
#print axioms KSatUpper.CertificatesK3Controls.control_426717_low
#print axioms KSatUpper.tendsto_zero_of_criterion
#print axioms KSatUpper.Certificates.control4_low
#print axioms KSatUpper.Certificates.control5_low

open Filter in
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 4 n (249*n/25)) atTop (nhds 0) :=
  KSatUpper.satisfiabilityProbability_4SAT_tendsto_zero

open Filter in
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 5 n (1057*n/50)) atTop (nhds 0) :=
  KSatUpper.satisfiabilityProbability_5SAT_tendsto_zero

open Filter in
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 3 n (1067*n/250)) atTop (nhds 0) :=
  KSatUpper.satisfiabilityProbability_3SAT_tendsto_zero

open Filter in
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 4 n (4967*n/500)) atTop (nhds 0) :=
  KSatUpper.satisfiabilityProbability_4SAT_9934_tendsto_zero

open Filter in
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 5 n (21123*n/1000)) atTop (nhds 0) :=
  KSatUpper.satisfiabilityProbability_5SAT_21123_tendsto_zero

open Filter in
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 3 n (2667*n/625)) atTop (nhds 0) :=
  KSatUpper.satisfiabilityProbability_3SAT_42672_tendsto_zero

open Filter in
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 3 n (213359*n/50000)) atTop
    (nhds 0) :=
  KSatUpper.satisfiabilityProbability_3SAT_426718_tendsto_zero

#check @KSatUpper.tendsto_zero_of_criterion
#check @KSatUpper.Criterion.finiteAnalyticBound
