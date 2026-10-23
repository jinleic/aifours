import KSatUpper.NumericalCriterionTables
import KSatUpper.K3Data
import KSatUpper.TrialDataK3
import KSatUpper.K3CheckTableA0
import KSatUpper.K3CheckTableA1
import KSatUpper.K3CheckTableA2
import KSatUpper.K3CheckTableA3
import KSatUpper.K3CheckTableA4
import KSatUpper.K3CheckTableA5
import KSatUpper.K3CheckTableA6
import KSatUpper.K3CheckTableA7
import KSatUpper.K3CheckTableA8
import KSatUpper.K3CheckTableA9
import KSatUpper.K3CheckTableA10
import KSatUpper.K3CheckTableA11
import KSatUpper.K3CheckTableA12
import KSatUpper.K3CheckTableA13
import KSatUpper.K3CheckTableA14
import KSatUpper.K3CheckTableA15
import KSatUpper.K3CheckTableA16
import KSatUpper.K3CheckTableA17
import KSatUpper.K3CheckTableA18
import KSatUpper.K3CheckTableA19
import KSatUpper.K3CheckTableA20
import KSatUpper.K3CheckTableA21
import KSatUpper.K3CheckMomA0
import KSatUpper.K3CheckMomA1
import KSatUpper.K3CheckMomA2
import KSatUpper.K3CheckMomA3
import KSatUpper.K3CheckMomA4
import KSatUpper.K3CheckMomA5
import KSatUpper.K3CheckMomA6
import KSatUpper.K3CheckMomA7
import KSatUpper.K3CheckMomA8
import KSatUpper.K3CheckMomA9
import KSatUpper.K3CheckMomA10
import KSatUpper.K3CheckMomA11
import KSatUpper.K3CheckMomA12
import KSatUpper.K3CheckMomA13
import KSatUpper.K3CheckMomA14
import KSatUpper.K3CheckEdgeA
import KSatUpper.K3CheckValueA
import KSatUpper.K3CheckTableB0
import KSatUpper.K3CheckTableB1
import KSatUpper.K3CheckTableB2
import KSatUpper.K3CheckTableB3
import KSatUpper.K3CheckTableB4
import KSatUpper.K3CheckTableB5
import KSatUpper.K3CheckTableB6
import KSatUpper.K3CheckTableB7
import KSatUpper.K3CheckTableB8
import KSatUpper.K3CheckTableB9
import KSatUpper.K3CheckTableB10
import KSatUpper.K3CheckTableB11
import KSatUpper.K3CheckTableB12
import KSatUpper.K3CheckTableB13
import KSatUpper.K3CheckTableB14
import KSatUpper.K3CheckTableB15
import KSatUpper.K3CheckTableB16
import KSatUpper.K3CheckTableB17
import KSatUpper.K3CheckTableB18
import KSatUpper.K3CheckTableB19
import KSatUpper.K3CheckTableB20
import KSatUpper.K3CheckTableB21
import KSatUpper.K3CheckMomB0
import KSatUpper.K3CheckMomB1
import KSatUpper.K3CheckMomB2
import KSatUpper.K3CheckMomB3
import KSatUpper.K3CheckMomB4
import KSatUpper.K3CheckMomB5
import KSatUpper.K3CheckMomB6
import KSatUpper.K3CheckMomB7
import KSatUpper.K3CheckMomB8
import KSatUpper.K3CheckMomB9
import KSatUpper.K3CheckMomB10
import KSatUpper.K3CheckMomB11
import KSatUpper.K3CheckMomB12
import KSatUpper.K3CheckMomB13
import KSatUpper.K3CheckMomB14
import KSatUpper.K3CheckEdgeB
import KSatUpper.K3CheckValueB

/-! Random 3-SAT certificates at 4.2672 and 4.26718 for the six-atom law `TrialDataK3.trialT128` (`T = 128`, edge
truncation `N = 256`), assembled from bounded kernel checks: every table chunk, moment
chunk, edge bound and final value is a separate small `decide +kernel` in a `K3Check*`
module. The statements are those of the superseded monolithic module
(`archive/k3-monolithic-12GiB/CertificatesK3.lean`), whose single `decide` per
certificate peaked at about 12 GB of memory. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.CertificatesK3

open K3Data NumericalCriterion TrialDataK3

theorem tableA : ∀ j, j ≤ 128 →
    bounds trialT128 2 (2667/625) j = tblA.getD j (0, 0) := by
  intro j hj
  rcases Nat.lt_or_ge j 6 with h | h0
  · exact K3CheckTableA0.chunk j h (Nat.zero_le _)
  rcases Nat.lt_or_ge j 12 with h | h1
  · exact K3CheckTableA1.chunk j h h0
  rcases Nat.lt_or_ge j 18 with h | h2
  · exact K3CheckTableA2.chunk j h h1
  rcases Nat.lt_or_ge j 24 with h | h3
  · exact K3CheckTableA3.chunk j h h2
  rcases Nat.lt_or_ge j 30 with h | h4
  · exact K3CheckTableA4.chunk j h h3
  rcases Nat.lt_or_ge j 36 with h | h5
  · exact K3CheckTableA5.chunk j h h4
  rcases Nat.lt_or_ge j 42 with h | h6
  · exact K3CheckTableA6.chunk j h h5
  rcases Nat.lt_or_ge j 48 with h | h7
  · exact K3CheckTableA7.chunk j h h6
  rcases Nat.lt_or_ge j 54 with h | h8
  · exact K3CheckTableA8.chunk j h h7
  rcases Nat.lt_or_ge j 60 with h | h9
  · exact K3CheckTableA9.chunk j h h8
  rcases Nat.lt_or_ge j 66 with h | h10
  · exact K3CheckTableA10.chunk j h h9
  rcases Nat.lt_or_ge j 72 with h | h11
  · exact K3CheckTableA11.chunk j h h10
  rcases Nat.lt_or_ge j 78 with h | h12
  · exact K3CheckTableA12.chunk j h h11
  rcases Nat.lt_or_ge j 84 with h | h13
  · exact K3CheckTableA13.chunk j h h12
  rcases Nat.lt_or_ge j 90 with h | h14
  · exact K3CheckTableA14.chunk j h h13
  rcases Nat.lt_or_ge j 96 with h | h15
  · exact K3CheckTableA15.chunk j h h14
  rcases Nat.lt_or_ge j 102 with h | h16
  · exact K3CheckTableA16.chunk j h h15
  rcases Nat.lt_or_ge j 108 with h | h17
  · exact K3CheckTableA17.chunk j h h16
  rcases Nat.lt_or_ge j 114 with h | h18
  · exact K3CheckTableA18.chunk j h h17
  rcases Nat.lt_or_ge j 120 with h | h19
  · exact K3CheckTableA19.chunk j h h18
  rcases Nat.lt_or_ge j 126 with h | h20
  · exact K3CheckTableA20.chunk j h h19
  exact K3CheckTableA21.chunk j (by omega) h20

theorem momA_all : ∀ k, k ≤ 128 →
    VertexEnclosures.momentLower (lowerOf tblA) (upperOf tblA) k = momA.getD k 0 := by
  intro k hk
  rcases Nat.lt_or_ge k 34 with h | h0
  · exact K3CheckMomA0.chunk k h (Nat.zero_le _)
  rcases Nat.lt_or_ge k 48 with h | h1
  · exact K3CheckMomA1.chunk k h h0
  rcases Nat.lt_or_ge k 59 with h | h2
  · exact K3CheckMomA2.chunk k h h1
  rcases Nat.lt_or_ge k 68 with h | h3
  · exact K3CheckMomA3.chunk k h h2
  rcases Nat.lt_or_ge k 76 with h | h4
  · exact K3CheckMomA4.chunk k h h3
  rcases Nat.lt_or_ge k 83 with h | h5
  · exact K3CheckMomA5.chunk k h h4
  rcases Nat.lt_or_ge k 89 with h | h6
  · exact K3CheckMomA6.chunk k h h5
  rcases Nat.lt_or_ge k 95 with h | h7
  · exact K3CheckMomA7.chunk k h h6
  rcases Nat.lt_or_ge k 101 with h | h8
  · exact K3CheckMomA8.chunk k h h7
  rcases Nat.lt_or_ge k 106 with h | h9
  · exact K3CheckMomA9.chunk k h h8
  rcases Nat.lt_or_ge k 111 with h | h10
  · exact K3CheckMomA10.chunk k h h9
  rcases Nat.lt_or_ge k 116 with h | h11
  · exact K3CheckMomA11.chunk k h h10
  rcases Nat.lt_or_ge k 121 with h | h12
  · exact K3CheckMomA12.chunk k h h11
  rcases Nat.lt_or_ge k 125 with h | h13
  · exact K3CheckMomA13.chunk k h h12
  exact K3CheckMomA14.chunk k (by omega) h13

theorem cert_42672 :
    certUpper trialT128 2 (2667/625) 128 256 (239949/250000) ≤ -1/500000 := by
  have h := certUpper_le_of_tables trialT128 2 (2667/625) (by norm_num) 128 256 (239949/250000) tblA
    tableA K3CheckEdgeA.edge
  rw [vertexUpper_eq_vertexOf 128 _ _ (fun k => momA.getD k 0) momA_all] at h
  exact h.trans K3CheckValueA.value

theorem tableB : ∀ j, j ≤ 128 →
    bounds trialT128 2 (213359/50000) j = tblB.getD j (0, 0) := by
  intro j hj
  rcases Nat.lt_or_ge j 6 with h | h0
  · exact K3CheckTableB0.chunk j h (Nat.zero_le _)
  rcases Nat.lt_or_ge j 12 with h | h1
  · exact K3CheckTableB1.chunk j h h0
  rcases Nat.lt_or_ge j 18 with h | h2
  · exact K3CheckTableB2.chunk j h h1
  rcases Nat.lt_or_ge j 24 with h | h3
  · exact K3CheckTableB3.chunk j h h2
  rcases Nat.lt_or_ge j 30 with h | h4
  · exact K3CheckTableB4.chunk j h h3
  rcases Nat.lt_or_ge j 36 with h | h5
  · exact K3CheckTableB5.chunk j h h4
  rcases Nat.lt_or_ge j 42 with h | h6
  · exact K3CheckTableB6.chunk j h h5
  rcases Nat.lt_or_ge j 48 with h | h7
  · exact K3CheckTableB7.chunk j h h6
  rcases Nat.lt_or_ge j 54 with h | h8
  · exact K3CheckTableB8.chunk j h h7
  rcases Nat.lt_or_ge j 60 with h | h9
  · exact K3CheckTableB9.chunk j h h8
  rcases Nat.lt_or_ge j 66 with h | h10
  · exact K3CheckTableB10.chunk j h h9
  rcases Nat.lt_or_ge j 72 with h | h11
  · exact K3CheckTableB11.chunk j h h10
  rcases Nat.lt_or_ge j 78 with h | h12
  · exact K3CheckTableB12.chunk j h h11
  rcases Nat.lt_or_ge j 84 with h | h13
  · exact K3CheckTableB13.chunk j h h12
  rcases Nat.lt_or_ge j 90 with h | h14
  · exact K3CheckTableB14.chunk j h h13
  rcases Nat.lt_or_ge j 96 with h | h15
  · exact K3CheckTableB15.chunk j h h14
  rcases Nat.lt_or_ge j 102 with h | h16
  · exact K3CheckTableB16.chunk j h h15
  rcases Nat.lt_or_ge j 108 with h | h17
  · exact K3CheckTableB17.chunk j h h16
  rcases Nat.lt_or_ge j 114 with h | h18
  · exact K3CheckTableB18.chunk j h h17
  rcases Nat.lt_or_ge j 120 with h | h19
  · exact K3CheckTableB19.chunk j h h18
  rcases Nat.lt_or_ge j 126 with h | h20
  · exact K3CheckTableB20.chunk j h h19
  exact K3CheckTableB21.chunk j (by omega) h20

theorem momB_all : ∀ k, k ≤ 128 →
    VertexEnclosures.momentLower (lowerOf tblB) (upperOf tblB) k = momB.getD k 0 := by
  intro k hk
  rcases Nat.lt_or_ge k 34 with h | h0
  · exact K3CheckMomB0.chunk k h (Nat.zero_le _)
  rcases Nat.lt_or_ge k 48 with h | h1
  · exact K3CheckMomB1.chunk k h h0
  rcases Nat.lt_or_ge k 59 with h | h2
  · exact K3CheckMomB2.chunk k h h1
  rcases Nat.lt_or_ge k 68 with h | h3
  · exact K3CheckMomB3.chunk k h h2
  rcases Nat.lt_or_ge k 76 with h | h4
  · exact K3CheckMomB4.chunk k h h3
  rcases Nat.lt_or_ge k 83 with h | h5
  · exact K3CheckMomB5.chunk k h h4
  rcases Nat.lt_or_ge k 89 with h | h6
  · exact K3CheckMomB6.chunk k h h5
  rcases Nat.lt_or_ge k 95 with h | h7
  · exact K3CheckMomB7.chunk k h h6
  rcases Nat.lt_or_ge k 101 with h | h8
  · exact K3CheckMomB8.chunk k h h7
  rcases Nat.lt_or_ge k 106 with h | h9
  · exact K3CheckMomB9.chunk k h h8
  rcases Nat.lt_or_ge k 111 with h | h10
  · exact K3CheckMomB10.chunk k h h9
  rcases Nat.lt_or_ge k 116 with h | h11
  · exact K3CheckMomB11.chunk k h h10
  rcases Nat.lt_or_ge k 121 with h | h12
  · exact K3CheckMomB12.chunk k h h11
  rcases Nat.lt_or_ge k 125 with h | h13
  · exact K3CheckMomB13.chunk k h h12
  exact K3CheckMomB14.chunk k (by omega) h13

theorem cert_426718 :
    certUpper trialT128 2 (213359/50000) 128 256 (239949/250000) ≤ -1/2000000 := by
  have h := certUpper_le_of_tables trialT128 2 (213359/50000) (by norm_num) 128 256 (239949/250000) tblB
    tableB K3CheckEdgeB.edge
  rw [vertexUpper_eq_vertexOf 128 _ _ (fun k => momB.getD k 0) momB_all] at h
  exact h.trans K3CheckValueB.value

end KSatUpper.CertificatesK3
