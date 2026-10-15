(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_1 () Real)
(declare-fun k_0_0 () Real)
(assert
 (= 1.0 0.0))
(assert
 (let ((?x180 (+ (- 1.0) (* (* 1.0 3.0) k_0_0) (* (* 1.0 3.0) k_0_1))))
 (= ?x180 0.0)))
(assert
 (let ((?x243 (+ 4.0 k_0_1 (* (* 1.0 (- 7.0)) k_0_0) (* (* 1.0 3.0) (^ k_0_1 2.0)) (* (* 1.0 6.0) (^ k_0_0 2.0)) (* (* (* 1.0 9.0) k_0_0) k_0_1))))
(= ?x243 0.0)))
(check-sat)
