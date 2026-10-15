(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ 1.0 (* (* 1.0 (- 1.0)) k_0_0)) 0.0))
(assert
 (= (+ (- 2.0) k_0_0) 0.0))
(assert
 (let ((?x1170 (+ 4.0 (* (* 1.0 (- 8.0)) k_0_0) (* (* 1.0 8.0) (^ k_0_0 2.0)))))
 (= ?x1170 0.0)))
(assert
 (let ((?x452 (+ (- 8.0) (* (* 1.0 (- 26.0)) (^ k_0_0 2.0)) (* (* 1.0 22.0) k_0_0))))
(= ?x452 0.0)))
(check-sat)
