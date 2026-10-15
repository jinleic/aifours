(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_1 () Real)
(declare-fun k_0_0 () Real)
(assert
 (= (- 2.0) 0.0))
(assert
 (= (+ 5.0 (* (* 1.0 (- 1.0)) k_0_1)) 0.0))
(assert
 (let ((?x247 (+ (- 7.0) (* (* 1.0 (- 1.0)) (^ k_0_1 2.0)) (* (* 1.0 16.0) k_0_0))))
(= ?x247 0.0)))
(check-sat)
