(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ (- 2.0) k_0_0) 0.0))
(assert
 (let ((?x38 (+ (- 2.0) (* (* 1.0 (- 1.0)) (^ k_0_0 2.0)) (* (* 1.0 2.0) k_0_0))))
 (= ?x38 0.0)))
(assert
 (let ((?x591 (^ k_0_0 3.0)))
 (let ((?x225 (+ 4.0 ?x591 (* (* 1.0 (- 1.0)) k_0_0) (* (* 1.0 (- 2.0)) (^ k_0_0 2.0)))))
 (= ?x225 0.0))))
(assert
 (let ((?x673 (+ 2.0 k_0_0)))
 (> ?x673 0.0)))
(assert
 (let ((?x233 (+ (* (* 1.0 2.0) (^ k_0_0 2.0)) (* (* 1.0 4.0) k_0_0))))
(> ?x233 0.0)))
(check-sat)
