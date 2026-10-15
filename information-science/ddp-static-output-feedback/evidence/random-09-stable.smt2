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
 (let ((?x84 (+ 2.0 (* (* 1.0 (- 3.0)) (^ k_1_0 2.0)) (* (* 1.0 (- 2.0)) k_0_0) (* (* (* 1.0 4.0) k_0_0) k_1_0))))
 (= ?x84 0.0)))
(assert
 (let ((?x12 (+ (- 3.0) (* (* 1.0 (- 4.0)) k_0_0) (* (* 1.0 3.0) k_1_0))))
 (> ?x12 0.0)))
(assert
 (let ((?x256 (+ (- 6.0) (* (* 1.0 (- 14.0)) k_0_0) (* (* 1.0 (- 8.0)) (^ k_0_0 2.0)) (* (* 1.0 6.0) k_1_0) (* (* (* 1.0 6.0) k_0_0) k_1_0))))
(> ?x256 0.0)))
(check-sat)
