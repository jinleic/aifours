(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (* (* 1.0 2.0) k_0_0) 0.0))
(assert
 (= (* (* 1.0 6.0) k_0_0) 0.0))
(assert
 (let ((?x522 (+ (* (* 1.0 (- 16.0)) k_0_0) (* (* 1.0 (- 8.0)) (^ k_0_0 2.0)))))
(= ?x522 0.0)))
(check-sat)
