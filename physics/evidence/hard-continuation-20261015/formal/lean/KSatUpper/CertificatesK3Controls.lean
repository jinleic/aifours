import KSatUpper.NumericalCriterionTables
import KSatUpper.K3Data
import KSatUpper.TrialDataK3
import KSatUpper.K3CheckTableC0
import KSatUpper.K3CheckTableC1
import KSatUpper.K3CheckTableC2
import KSatUpper.K3CheckTableC3
import KSatUpper.K3CheckTableC4
import KSatUpper.K3CheckTableC5
import KSatUpper.K3CheckTableC6
import KSatUpper.K3CheckTableC7
import KSatUpper.K3CheckTableC8
import KSatUpper.K3CheckTableC9
import KSatUpper.K3CheckTableC10
import KSatUpper.K3CheckTableC11
import KSatUpper.K3CheckTableC12
import KSatUpper.K3CheckTableC13
import KSatUpper.K3CheckTableC14
import KSatUpper.K3CheckTableC15
import KSatUpper.K3CheckTableC16
import KSatUpper.K3CheckTableC17
import KSatUpper.K3CheckTableC18
import KSatUpper.K3CheckTableC19
import KSatUpper.K3CheckTableC20
import KSatUpper.K3CheckTableC21
import KSatUpper.K3CheckMomC0
import KSatUpper.K3CheckMomC1
import KSatUpper.K3CheckMomC2
import KSatUpper.K3CheckMomC3
import KSatUpper.K3CheckMomC4
import KSatUpper.K3CheckMomC5
import KSatUpper.K3CheckMomC6
import KSatUpper.K3CheckMomC7
import KSatUpper.K3CheckMomC8
import KSatUpper.K3CheckMomC9
import KSatUpper.K3CheckMomC10
import KSatUpper.K3CheckMomC11
import KSatUpper.K3CheckMomC12
import KSatUpper.K3CheckMomC13
import KSatUpper.K3CheckMomC14
import KSatUpper.K3CheckEdgeC
import KSatUpper.K3CheckValueC
import KSatUpper.K3CheckTableD0
import KSatUpper.K3CheckTableD1
import KSatUpper.K3CheckTableD2
import KSatUpper.K3CheckTableD3
import KSatUpper.K3CheckTableD4
import KSatUpper.K3CheckTableD5
import KSatUpper.K3CheckTableD6
import KSatUpper.K3CheckTableD7
import KSatUpper.K3CheckTableD8
import KSatUpper.K3CheckTableD9
import KSatUpper.K3CheckTableD10
import KSatUpper.K3CheckTableD11
import KSatUpper.K3CheckTableD12
import KSatUpper.K3CheckTableD13
import KSatUpper.K3CheckTableD14
import KSatUpper.K3CheckTableD15
import KSatUpper.K3CheckTableD16
import KSatUpper.K3CheckTableD17
import KSatUpper.K3CheckTableD18
import KSatUpper.K3CheckTableD19
import KSatUpper.K3CheckTableD20
import KSatUpper.K3CheckTableD21
import KSatUpper.K3CheckMomD0
import KSatUpper.K3CheckMomD1
import KSatUpper.K3CheckMomD2
import KSatUpper.K3CheckMomD3
import KSatUpper.K3CheckMomD4
import KSatUpper.K3CheckMomD5
import KSatUpper.K3CheckMomD6
import KSatUpper.K3CheckMomD7
import KSatUpper.K3CheckMomD8
import KSatUpper.K3CheckMomD9
import KSatUpper.K3CheckMomD10
import KSatUpper.K3CheckMomD11
import KSatUpper.K3CheckMomD12
import KSatUpper.K3CheckMomD13
import KSatUpper.K3CheckMomD14
import KSatUpper.K3CheckEdgeD
import KSatUpper.K3CheckValueD

/-! Same-law controls at 4.2671 and 4.26717 (positive values) for the six-atom law `TrialDataK3.trialT128` (`T = 128`, edge
truncation `N = 256`), assembled from bounded kernel checks: every table chunk, moment
chunk, edge bound and final value is a separate small `decide +kernel` in a `K3Check*`
module. The statements are those of the superseded monolithic module
(`archive/k3-monolithic-12GiB/CertificatesK3.lean`), whose single `decide` per
certificate peaked at about 12 GB of memory. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.CertificatesK3Controls

open K3Data NumericalCriterion TrialDataK3

theorem tableC : ∀ j, j ≤ 128 →
    bounds trialT128 2 (42671/10000) j = tblC.getD j (0, 0) := by
  intro j hj
  rcases Nat.lt_or_ge j 6 with h | h0
  · exact K3CheckTableC0.chunk j h (Nat.zero_le _)
  rcases Nat.lt_or_ge j 12 with h | h1
  · exact K3CheckTableC1.chunk j h h0
  rcases Nat.lt_or_ge j 18 with h | h2
  · exact K3CheckTableC2.chunk j h h1
  rcases Nat.lt_or_ge j 24 with h | h3
  · exact K3CheckTableC3.chunk j h h2
  rcases Nat.lt_or_ge j 30 with h | h4
  · exact K3CheckTableC4.chunk j h h3
  rcases Nat.lt_or_ge j 36 with h | h5
  · exact K3CheckTableC5.chunk j h h4
  rcases Nat.lt_or_ge j 42 with h | h6
  · exact K3CheckTableC6.chunk j h h5
  rcases Nat.lt_or_ge j 48 with h | h7
  · exact K3CheckTableC7.chunk j h h6
  rcases Nat.lt_or_ge j 54 with h | h8
  · exact K3CheckTableC8.chunk j h h7
  rcases Nat.lt_or_ge j 60 with h | h9
  · exact K3CheckTableC9.chunk j h h8
  rcases Nat.lt_or_ge j 66 with h | h10
  · exact K3CheckTableC10.chunk j h h9
  rcases Nat.lt_or_ge j 72 with h | h11
  · exact K3CheckTableC11.chunk j h h10
  rcases Nat.lt_or_ge j 78 with h | h12
  · exact K3CheckTableC12.chunk j h h11
  rcases Nat.lt_or_ge j 84 with h | h13
  · exact K3CheckTableC13.chunk j h h12
  rcases Nat.lt_or_ge j 90 with h | h14
  · exact K3CheckTableC14.chunk j h h13
  rcases Nat.lt_or_ge j 96 with h | h15
  · exact K3CheckTableC15.chunk j h h14
  rcases Nat.lt_or_ge j 102 with h | h16
  · exact K3CheckTableC16.chunk j h h15
  rcases Nat.lt_or_ge j 108 with h | h17
  · exact K3CheckTableC17.chunk j h h16
  rcases Nat.lt_or_ge j 114 with h | h18
  · exact K3CheckTableC18.chunk j h h17
  rcases Nat.lt_or_ge j 120 with h | h19
  · exact K3CheckTableC19.chunk j h h18
  rcases Nat.lt_or_ge j 126 with h | h20
  · exact K3CheckTableC20.chunk j h h19
  exact K3CheckTableC21.chunk j (by omega) h20

theorem momC_all : ∀ k, k ≤ 128 →
    VertexEnclosures.momentLower (lowerOf tblC) (upperOf tblC) k = momC.getD k 0 := by
  intro k hk
  rcases Nat.lt_or_ge k 34 with h | h0
  · exact K3CheckMomC0.chunk k h (Nat.zero_le _)
  rcases Nat.lt_or_ge k 48 with h | h1
  · exact K3CheckMomC1.chunk k h h0
  rcases Nat.lt_or_ge k 59 with h | h2
  · exact K3CheckMomC2.chunk k h h1
  rcases Nat.lt_or_ge k 68 with h | h3
  · exact K3CheckMomC3.chunk k h h2
  rcases Nat.lt_or_ge k 76 with h | h4
  · exact K3CheckMomC4.chunk k h h3
  rcases Nat.lt_or_ge k 83 with h | h5
  · exact K3CheckMomC5.chunk k h h4
  rcases Nat.lt_or_ge k 89 with h | h6
  · exact K3CheckMomC6.chunk k h h5
  rcases Nat.lt_or_ge k 95 with h | h7
  · exact K3CheckMomC7.chunk k h h6
  rcases Nat.lt_or_ge k 101 with h | h8
  · exact K3CheckMomC8.chunk k h h7
  rcases Nat.lt_or_ge k 106 with h | h9
  · exact K3CheckMomC9.chunk k h h8
  rcases Nat.lt_or_ge k 111 with h | h10
  · exact K3CheckMomC10.chunk k h h9
  rcases Nat.lt_or_ge k 116 with h | h11
  · exact K3CheckMomC11.chunk k h h10
  rcases Nat.lt_or_ge k 121 with h | h12
  · exact K3CheckMomC12.chunk k h h11
  rcases Nat.lt_or_ge k 125 with h | h13
  · exact K3CheckMomC13.chunk k h h12
  exact K3CheckMomC14.chunk k (by omega) h13

theorem control_42671_low :
    0 < certUpper trialT128 2 (42671/10000) 128 256 (239949/250000) := by
  have h := le_certUpper_of_tables trialT128 2 (42671/10000) (by norm_num) 128 256 (239949/250000) tblC
    tableC K3CheckEdgeC.edge
  rw [vertexUpper_eq_vertexOf 128 _ _ (fun k => momC.getD k 0) momC_all] at h
  exact lt_of_lt_of_le K3CheckValueC.value h

theorem tableD : ∀ j, j ≤ 128 →
    bounds trialT128 2 (426717/100000) j = tblD.getD j (0, 0) := by
  intro j hj
  rcases Nat.lt_or_ge j 6 with h | h0
  · exact K3CheckTableD0.chunk j h (Nat.zero_le _)
  rcases Nat.lt_or_ge j 12 with h | h1
  · exact K3CheckTableD1.chunk j h h0
  rcases Nat.lt_or_ge j 18 with h | h2
  · exact K3CheckTableD2.chunk j h h1
  rcases Nat.lt_or_ge j 24 with h | h3
  · exact K3CheckTableD3.chunk j h h2
  rcases Nat.lt_or_ge j 30 with h | h4
  · exact K3CheckTableD4.chunk j h h3
  rcases Nat.lt_or_ge j 36 with h | h5
  · exact K3CheckTableD5.chunk j h h4
  rcases Nat.lt_or_ge j 42 with h | h6
  · exact K3CheckTableD6.chunk j h h5
  rcases Nat.lt_or_ge j 48 with h | h7
  · exact K3CheckTableD7.chunk j h h6
  rcases Nat.lt_or_ge j 54 with h | h8
  · exact K3CheckTableD8.chunk j h h7
  rcases Nat.lt_or_ge j 60 with h | h9
  · exact K3CheckTableD9.chunk j h h8
  rcases Nat.lt_or_ge j 66 with h | h10
  · exact K3CheckTableD10.chunk j h h9
  rcases Nat.lt_or_ge j 72 with h | h11
  · exact K3CheckTableD11.chunk j h h10
  rcases Nat.lt_or_ge j 78 with h | h12
  · exact K3CheckTableD12.chunk j h h11
  rcases Nat.lt_or_ge j 84 with h | h13
  · exact K3CheckTableD13.chunk j h h12
  rcases Nat.lt_or_ge j 90 with h | h14
  · exact K3CheckTableD14.chunk j h h13
  rcases Nat.lt_or_ge j 96 with h | h15
  · exact K3CheckTableD15.chunk j h h14
  rcases Nat.lt_or_ge j 102 with h | h16
  · exact K3CheckTableD16.chunk j h h15
  rcases Nat.lt_or_ge j 108 with h | h17
  · exact K3CheckTableD17.chunk j h h16
  rcases Nat.lt_or_ge j 114 with h | h18
  · exact K3CheckTableD18.chunk j h h17
  rcases Nat.lt_or_ge j 120 with h | h19
  · exact K3CheckTableD19.chunk j h h18
  rcases Nat.lt_or_ge j 126 with h | h20
  · exact K3CheckTableD20.chunk j h h19
  exact K3CheckTableD21.chunk j (by omega) h20

theorem momD_all : ∀ k, k ≤ 128 →
    VertexEnclosures.momentLower (lowerOf tblD) (upperOf tblD) k = momD.getD k 0 := by
  intro k hk
  rcases Nat.lt_or_ge k 34 with h | h0
  · exact K3CheckMomD0.chunk k h (Nat.zero_le _)
  rcases Nat.lt_or_ge k 48 with h | h1
  · exact K3CheckMomD1.chunk k h h0
  rcases Nat.lt_or_ge k 59 with h | h2
  · exact K3CheckMomD2.chunk k h h1
  rcases Nat.lt_or_ge k 68 with h | h3
  · exact K3CheckMomD3.chunk k h h2
  rcases Nat.lt_or_ge k 76 with h | h4
  · exact K3CheckMomD4.chunk k h h3
  rcases Nat.lt_or_ge k 83 with h | h5
  · exact K3CheckMomD5.chunk k h h4
  rcases Nat.lt_or_ge k 89 with h | h6
  · exact K3CheckMomD6.chunk k h h5
  rcases Nat.lt_or_ge k 95 with h | h7
  · exact K3CheckMomD7.chunk k h h6
  rcases Nat.lt_or_ge k 101 with h | h8
  · exact K3CheckMomD8.chunk k h h7
  rcases Nat.lt_or_ge k 106 with h | h9
  · exact K3CheckMomD9.chunk k h h8
  rcases Nat.lt_or_ge k 111 with h | h10
  · exact K3CheckMomD10.chunk k h h9
  rcases Nat.lt_or_ge k 116 with h | h11
  · exact K3CheckMomD11.chunk k h h10
  rcases Nat.lt_or_ge k 121 with h | h12
  · exact K3CheckMomD12.chunk k h h11
  rcases Nat.lt_or_ge k 125 with h | h13
  · exact K3CheckMomD13.chunk k h h12
  exact K3CheckMomD14.chunk k (by omega) h13

theorem control_426717_low :
    0 < certUpper trialT128 2 (426717/100000) 128 256 (239949/250000) := by
  have h := le_certUpper_of_tables trialT128 2 (426717/100000) (by norm_num) 128 256 (239949/250000) tblD
    tableD K3CheckEdgeD.edge
  rw [vertexUpper_eq_vertexOf 128 _ _ (fun k => momD.getD k 0) momD_all] at h
  exact lt_of_lt_of_le K3CheckValueD.value h

end KSatUpper.CertificatesK3Controls
