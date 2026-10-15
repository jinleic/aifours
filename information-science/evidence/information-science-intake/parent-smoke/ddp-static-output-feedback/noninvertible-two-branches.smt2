(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_1 () Real)
(declare-fun k_1_1 () Real)
(declare-fun k_0_0 () Real)
(assert
 (= 0.0 0.0))
(assert
 (= 0.0 0.0))
(assert
 (= k_0_1 0.0))
(assert
 (let ((?x92 (+ 1.0 k_0_0 k_1_1 (* (* 1.0 (- 4.0)) k_0_1) (* (* 1.0 k_0_0) k_1_1))))
(= ?x92 0.0)))
(check-sat)
