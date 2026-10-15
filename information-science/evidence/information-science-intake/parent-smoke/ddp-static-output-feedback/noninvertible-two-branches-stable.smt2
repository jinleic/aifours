(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_1 () Real)
(declare-fun k_1_1 () Real)
(declare-fun k_0_0 () Real)
(declare-fun k_1_0 () Real)
(assert
 (= 0.0 0.0))
(assert
 (= 0.0 0.0))
(assert
 (= k_0_1 0.0))
(assert
 (let ((?x66 (+ 1.0 k_0_0 k_1_1 (* (* 1.0 (- 4.0)) k_0_1) (* (* 1.0 k_0_0) k_1_1))))
 (= ?x66 0.0)))
(assert
 (> (+ 6.0 (* (* 1.0 (- 1.0)) k_1_0)) 0.0))
(assert
 (let ((?x99 (+ 60.0 (* (* 1.0 (- 32.0)) k_1_0) (* (* 1.0 4.0) (^ k_1_0 2.0)))))
 (> ?x99 0.0)))
(assert
 (let ((?x31 (+ 360.0 (* (* 1.0 (- 372.0)) k_1_0) (* (* 1.0 (- 12.0)) (^ k_1_0 3.0)) (* (* 1.0 120.0) (^ k_1_0 2.0)))))
(> ?x31 0.0)))
(check-sat)
