(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_1_0 () Real)
(declare-fun k_0_0 () Real)
(assert
 (= (- 2.0) 0.0))
(assert
 (= (+ 1.0 k_1_0) 0.0))
(assert
 (let ((?x226 (+ 2.0 (* (* 1.0 (- 3.0)) (^ k_1_0 2.0)) (* (* 1.0 (- 2.0)) k_0_0) (* (* (* 1.0 4.0) k_0_0) k_1_0))))
(= ?x226 0.0)))
(check-sat)
