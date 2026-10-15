(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(declare-fun k_1_0 () Real)
(assert
 (= 1.0 0.0))
(assert
 (let ((?x105 (+ 2.0 (* (* 1.0 (- 2.0)) k_1_0) (* (* 1.0 4.0) k_0_0))))
 (= ?x105 0.0)))
(assert
 (let ((?x159 (+ (- 5.0) (* (* 1.0 (- 8.0)) k_0_0) (* (* 1.0 (- 2.0)) (^ k_1_0 2.0)) (* (* 1.0 4.0) (^ k_0_0 2.0)) (* (* 1.0 7.0) k_1_0) (* (* (* 1.0 2.0) k_0_0) k_1_0))))
(= ?x159 0.0)))
(check-sat)
