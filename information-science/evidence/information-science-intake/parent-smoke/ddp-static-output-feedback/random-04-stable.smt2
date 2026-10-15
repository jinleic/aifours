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
 (let ((?x135 (* (* 1.0 16.0) k_0_0)))
 (= (+ (- 7.0) (* (* 1.0 (- 1.0)) (^ k_0_1 2.0)) ?x135) 0.0)))
(assert
 (> (+ 1.0 (* (* 1.0 (- 1.0)) k_0_1)) 0.0))
(assert
 (let ((?x135 (* (* 1.0 16.0) k_0_0)))
(let ((?x320 (+ 2.0 (* (* 1.0 (- 8.0)) k_0_1) (* (* 1.0 6.0) (^ k_0_1 2.0)) ?x135 (* (* (* 1.0 (- 16.0)) k_0_0) k_0_1))))
(> ?x320 0.0))))
(check-sat)
