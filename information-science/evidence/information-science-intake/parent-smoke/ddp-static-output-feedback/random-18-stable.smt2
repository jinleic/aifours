(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_1_0 () Real)
(declare-fun k_0_0 () Real)
(assert
 (= 1.0 0.0))
(assert
 (= (+ 2.0 (* (* 1.0 (- 2.0)) k_1_0)) 0.0))
(assert
 (let ((?x177 (* 1.0 (- 2.0))))
 (let ((?x47 (* ?x177 k_0_0)))
 (= (+ 12.0 ?x47 (* (* 1.0 16.0) k_1_0) (* ?x47 k_1_0)) 0.0))))
(assert
 (> (+ (- 2.0) (* (* 1.0 (- 1.0)) k_0_0)) 0.0))
(assert
 (> (+ (- 8.0) (* (* 1.0 2.0) (^ k_0_0 2.0))) 0.0))
(check-sat)
