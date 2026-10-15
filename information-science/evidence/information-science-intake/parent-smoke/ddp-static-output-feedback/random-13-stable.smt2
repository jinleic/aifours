(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (- 1.0) 0.0))
(assert
 (= (* (* 1.0 (- 2.0)) k_0_0) 0.0))
(assert
 (let ((?x460 (+ (- 4.0) (* (* 1.0 (- 6.0)) (^ k_0_0 2.0)) (* (* 1.0 10.0) k_0_0))))
 (= ?x460 0.0)))
(assert
 (> (+ (- 1.0) (* (* 1.0 (- 3.0)) k_0_0)) 0.0))
(assert
 (let ((?x9 (+ (- 2.0) (* (* 1.0 (- 4.0)) k_0_0) (* (* 1.0 6.0) (^ k_0_0 2.0)))))
(> ?x9 0.0)))
(check-sat)
