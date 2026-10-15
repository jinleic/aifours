(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= 1.0 0.0))
(assert
 (= (+ 2.0 (* (* 1.0 2.0) k_0_0)) 0.0))
(assert
 (= (+ 12.0 (* (* 1.0 14.0) k_0_0)) 0.0))
(check-sat)
