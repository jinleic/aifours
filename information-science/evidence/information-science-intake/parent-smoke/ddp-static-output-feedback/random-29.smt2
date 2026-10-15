(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= 2.0 0.0))
(assert
 (= 0.0 0.0))
(assert
 (= (+ 6.0 (* (* 1.0 (- 2.0)) k_0_0)) 0.0))
(assert
 (let ((?x1193 (+ (* (* 1.0 (- 10.0)) (^ k_0_0 2.0)) (* (* 1.0 6.0) k_0_0))))
(= ?x1193 0.0)))
(check-sat)
