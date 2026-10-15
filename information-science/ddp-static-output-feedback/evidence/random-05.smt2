(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ (- 2.0) k_0_0) 0.0))
(assert
 (let ((?x132 (+ (- 2.0) (* (* 1.0 (- 1.0)) k_0_0) (* (* 1.0 (- 2.0)) (^ k_0_0 2.0)))))
 (= ?x132 0.0)))
(assert
 (let ((?x331 (+ 10.0 (* (* 1.0 4.0) (^ k_0_0 3.0)) (* (* 1.0 7.0) k_0_0) (* (* 1.0 8.0) (^ k_0_0 2.0)))))
(= ?x331 0.0)))
(check-sat)
